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

def send_telegram_update(data):
    token = os.environ.get("TELEGRAM_BOT_TOKEN")
    chat_id = os.environ.get("TELEGRAM_CHAT_ID")
    if not token or not chat_id:
        print("Telegram bot token or chat_id not configured. Skipping Telegram notification.")
        return

    g = data.get("gold", {})
    s = data.get("silver", {})
    p = data.get("platinum", {})
    
    date_str = data.get("as_of_market_date", "Today")
    ist_time = data.get("formatted_ist", "")
    
    msg = (
        f"🪙 <b>IBJA Benchmark Precious Metal Rates</b>\n"
        f"📅 Market Date: <b>{date_str}</b>\n"
        f"🕒 Synced: <code>{ist_time}</code>\n\n"
        f"🟡 <b>Gold Rates (per gram):</b>\n"
        f"• 24K (999): <b>₹{g.get('24k_per_gram', 0):,.2f}</b>\n"
        f"• 22K (916): <b>₹{g.get('22k_per_gram', 0):,.2f}</b>\n"
        f"• 18K (750): <b>₹{g.get('18k_per_gram', 0):,.2f}</b>\n"
        f"• 14K (585): <b>₹{g.get('14k_per_gram', 0):,.2f}</b>\n"
        f"• 1 Pavan (8g 22K): <b>₹{g.get('sovereign_8g_22k', 0):,.2f}</b>\n\n"
        f"⚪ <b>Silver Rates:</b>\n"
        f"• Fine 999: <b>₹{s.get('fine_999_per_gram', 0):,.2f} / g</b> (₹{s.get('fine_999_per_kg', 0):,.2f} / kg)\n"
        f"• Sterling 925: <b>₹{s.get('sterling_925_per_gram', 0):,.2f} / g</b>\n\n"
        f"🔘 <b>Platinum (950):</b> <b>₹{p.get('950_per_gram', 0):,.2f} / g</b>\n\n"
        f"🌐 <a href=\"https://nalkudilstudio.github.io/data/rates.json\">rates.json</a> • "
        f"<a href=\"https://iamsaravofficial.com/apps/gold-price-estimator/\">Estimator</a> • "
        f"<a href=\"https://iamsaravofficial.com/apps/gold-loan-calculator/\">Loan Calc</a>"
    )

    # 1. Primary destination: @SaravMPBot (Sarav DM)
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": msg,
        "parse_mode": "HTML",
        "disable_web_page_preview": True
    }

    try:
        resp = requests.post(url, json=payload, timeout=15)
        if resp.status_code == 200:
            print("Successfully sent rate update to Telegram (@SaravMPBot).")
        else:
            print(f"Telegram API warning (status {resp.status_code}): {resp.text}", file=sys.stderr)
    except Exception as err:
        print(f"Failed to send Telegram message to @SaravMPBot: {err}", file=sys.stderr)

    # 2. Secondary destination: StashNStrike Telegram Channel
    sns_token = os.environ.get("SNS_BOT_TOKEN")
    sns_chat_id = os.environ.get("SNS_CHAT_ID")
    if sns_token and sns_chat_id:
        sns_url = f"https://api.telegram.org/bot{sns_token}/sendMessage"
        sns_payload = {
            "chat_id": sns_chat_id,
            "text": msg,
            "parse_mode": "HTML",
            "disable_web_page_preview": True
        }
        try:
            sns_resp = requests.post(sns_url, json=sns_payload, timeout=15)
            if sns_resp.status_code == 200:
                print("Successfully sent rate update to StashNStrike Channel.")
            else:
                print(f"Telegram SNS API warning (status {sns_resp.status_code}): {sns_resp.text}", file=sys.stderr)
        except Exception as err:
            print(f"Failed to send Telegram message to StashNStrike Channel: {err}", file=sys.stderr)

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

    has_changed = True
    if os.path.exists(OUTPUT_FILE):
        try:
            with open(OUTPUT_FILE, "r", encoding="utf-8") as f:
                prev = json.load(f)
            prev_gold_24k = prev.get("gold", {}).get("24k_per_gram")
            new_gold_24k = data.get("gold", {}).get("24k_per_gram")
            prev_date = prev.get("as_of_market_date")
            new_date = data.get("as_of_market_date")
            if prev_gold_24k == new_gold_24k and prev_date == new_date:
                has_changed = False
        except Exception:
            has_changed = True

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"Updated rates written to {OUTPUT_FILE}")

    force_tg = os.environ.get("FORCE_TELEGRAM", "").lower() in ("1", "true", "yes")
    if has_changed or force_tg:
        send_telegram_update(data)
    else:
        print("Rates have not changed since last run. Skipping Telegram notification to avoid duplicate spam.")

if __name__ == "__main__":
    main()
