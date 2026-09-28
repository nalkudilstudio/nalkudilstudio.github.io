#!/usr/bin/env python3
"""
Nalkudil Studio — Live Precious Metal Rates Scraper & Normalizer
Fetches benchmark Indian bullion rates (Gold 24K, 22K, 18K, 14K, Silver, Platinum)
and publishes a standardized JSON payload for Sahi & Metal Price Estimator (MPE).
"""

import os
import sys
import json
import time
from datetime import datetime, timezone, timedelta
import requests
import bs4

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data")
OUTPUT_FILE = os.path.join(DATA_DIR, "rates.json")

IST = timezone(timedelta(hours=5, minutes=30))

def get_fallback_rates():
    """Returns safe fallback rates if no previous file exists."""
    return {
        "status": "fallback",
        "last_updated": datetime.now(timezone.utc).isoformat(),
        "formatted_ist": datetime.now(IST).strftime("%d %b %Y, %I:%M %p IST"),
        "source": "IBJA Benchmark (Fallback)",
        "currency": "INR",
        "gold": {
            "24k_per_gram": 15200.00,
            "22k_per_gram": 13900.00,
            "18k_per_gram": 11400.00,
            "14k_per_gram": 8900.00,
            "sovereign_8g_22k": 111200.00
        },
        "silver": {
            "fine_999_per_gram": 232.00,
            "fine_999_per_kg": 232000.00,
            "sterling_925_per_gram": 214.60
        },
        "platinum": {
            "950_per_gram": 5730.00
        },
        "diamond_benchmark": {
            "vvs_ef_per_carat": 125000.00,
            "vs_gh_per_carat": 95000.00,
            "si_ij_per_carat": 65000.00
        }
    }

def fetch_ibja_rates():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9"
    }
    
    url = "https://www.ibjarates.com"
    resp = requests.get(url, headers=headers, timeout=20)
    resp.raise_for_status()

    soup = bs4.BeautifulSoup(resp.text, "html.parser")

    import re
    date_pat = re.compile(r"^\d{2}/\d{2}/\d{4}$")
    valid_rows = []

    for tr in soup.find_all("tr"):
        tds = [td.get_text(strip=True) for td in tr.find_all("td")]
        if len(tds) == 8 and date_pat.match(tds[0]):
            try:
                float(tds[1])
                float(tds[3])
                valid_rows.append(tds)
            except ValueError:
                continue

    if not valid_rows:
        raise ValueError("Could not parse valid rate rows from IBJA website.")

    # Target the latest market date: prefer PM closing rate if available
    target_row = valid_rows[0]
    if len(valid_rows) >= 5 and valid_rows[4][0] == valid_rows[0][0]:
        target_row = valid_rows[4]

    date_str = target_row[0]
    g999_lot = float(target_row[1])   # Gold 999 per 10 grams
    g916_lot = float(target_row[3])   # Gold 916 (22K) per 10 grams
    g750_lot = float(target_row[4])   # Gold 750 (18K) per 10 grams
    g585_lot = float(target_row[5])   # Gold 585 (14K) per 10 grams
    silver_lot = float(target_row[6]) # Silver 999 per 1 kg (1000g)
    plat_lot = float(target_row[7])   # Platinum per 10 grams

    # IBJA statutory standard: Gold is quoted per 10gm, Silver per 1kg, Platinum per 10gm
    g24k = round(g999_lot / 10.0, 2)
    g22k = round(g916_lot / 10.0, 2)
    g18k = round(g750_lot / 10.0, 2)
    g14k = round(g585_lot / 10.0, 2)
    sovereign = round(g22k * 8.0, 2)

    silver_1g = round(silver_lot / 1000.0, 2)
    silver_1kg = round(silver_lot, 2)
    silver_925 = round(silver_1g * 0.925, 2)

    plat_1g = round((plat_lot / 10.0) * 0.95, 2)

    now_utc = datetime.now(timezone.utc)
    now_ist = datetime.now(IST)

    payload = {
        "status": "success",
        "as_of_market_date": date_str,
        "last_updated_utc": now_utc.isoformat(),
        "formatted_ist": now_ist.strftime("%d %b %Y, %I:%M %p IST"),
        "source": "IBJA Benchmark (India Bullion and Jewellers Association)",
        "currency": "INR",
        "gold": {
            "24k_per_gram": g24k,
            "22k_per_gram": g22k,
            "18k_per_gram": g18k,
            "14k_per_gram": g14k,
            "sovereign_8g_22k": sovereign
        },
        "silver": {
            "fine_999_per_gram": silver_1g,
            "fine_999_per_kg": silver_1kg,
            "sterling_925_per_gram": silver_925
        },
        "platinum": {
            "950_per_gram": plat_1g
        },
        "diamond_benchmark": {
            "vvs_ef_per_carat": 125000.00,
            "vs_gh_per_carat": 95000.00,
            "si_ij_per_carat": 65000.00
        }
    }
    return payload

def main():
    os.makedirs(DATA_DIR, exist_ok=True)

    try:
        print("Fetching latest precious metal rates from IBJA...")
        data = fetch_ibja_rates()
        print(f"Rates successfully fetched for market date: {data.get('as_of_market_date')}")
        print(f"24K Gold: Rs {data['gold']['24k_per_gram']}/g | 22K Gold: Rs {data['gold']['22k_per_gram']}/g | Silver: Rs {data['silver']['fine_999_per_gram']}/g")
    except Exception as e:
        print(f"Warning: Failed to fetch live rates: {e}", file=sys.stderr)
        if os.path.exists(OUTPUT_FILE):
            print("Existing rates.json found. Preserving previous rate snapshot.")
            sys.exit(0)
        else:
            print("No existing rate file. Writing safe fallback baseline.")
            data = get_fallback_rates()

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"Updated rates written to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
