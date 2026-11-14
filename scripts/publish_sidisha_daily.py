#!/usr/bin/env python3
"""
Nalkudil Studio — Sid & Isha Daily Instagram Publisher (GitHub Actions Runner)
=============================================================================
Zero-Secrets Cloud Relay:
  - Access Token injected strictly via GitHub Actions Secrets (META_ACCESS_TOKEN).
  - Runs daily at 10:10 AM IST (04:40 UTC) via cron.
  - Automatically identifies the day's drabble by IST date.
  - Publishes 2-slide carousel to @iamsaravofficial via Meta Graph API.
  - Updates catalog.js in Nalkudil Social Studio.
  - Dispatches Telegram notifications to Sarav on success or failure.
"""

import os
import sys
import re
import json
import time
import urllib.request
import urllib.parse
from datetime import datetime, timezone, timedelta

IST_TZ = timezone(timedelta(hours=5, minutes=30))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CATALOG_FILE = os.path.join(BASE_DIR, "nalkudil-social-studio", "catalog.js")

META_ACCESS_TOKEN = os.environ.get("META_ACCESS_TOKEN", "").strip()
INSTAGRAM_BUSINESS_ID = os.environ.get("INSTAGRAM_BUSINESS_ID", "17841401278750705").strip()
TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "").strip()
TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID", "1738811053").strip()
FORCE_DAY = os.environ.get("FORCE_DAY", "").strip()

def notify_telegram(text):
    if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
        print("[!] Telegram credentials not configured; skipping alert.")
        return
    try:
        url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
        payload = {"chat_id": TELEGRAM_CHAT_ID, "text": text, "parse_mode": "HTML"}
        data = json.dumps(payload).encode("utf-8")
        req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"})
        with urllib.request.urlopen(req, timeout=10) as resp:
            pass
    except Exception as e:
        print(f"[!] Telegram alert dispatch failed: {e}")

def load_catalog():
    if not os.path.exists(CATALOG_FILE):
        raise FileNotFoundError(f"Catalog file not found at: {CATALOG_FILE}")
    with open(CATALOG_FILE, "r", encoding="utf-8") as f:
        text = f.read().strip()
    
    clean_js = text
    if clean_js.startswith("window.PUBLISHING_CATALOG ="):
        clean_js = clean_js[len("window.PUBLISHING_CATALOG ="):].strip()
    elif clean_js.startswith("const CATALOG ="):
        clean_js = clean_js[len("const CATALOG ="):].strip()
    if clean_js.endswith(";"):
        clean_js = clean_js[:-1].strip()
    
    return json.loads(clean_js)

def get_target_item(catalog_data):
    sid_isha_list = catalog_data.get("sid_isha", [])
    if FORCE_DAY and FORCE_DAY.isdigit():
        target_day = int(FORCE_DAY)
        for item in sid_isha_list:
            if item.get("day") == target_day:
                return item
        raise ValueError(f"Forced Day {target_day} not found in catalog.")
    
    today_ist = datetime.now(IST_TZ).strftime("%Y-%m-%d")
    print(f"[*] Determining target episode for date: {today_ist} (IST)")
    for item in sid_isha_list:
        if item.get("date") == today_ist:
            return item
    
    # Fallback to first pending/ready item if date does not match
    for item in sid_isha_list:
        if item.get("status") in ["PENDING", "READY 🚀", "READY"]:
            print(f"[!] No date match for {today_ist}; falling back to next available item (Day {item.get('day')})")
            return item
            
    raise ValueError(f"No pending episode found in catalog for date {today_ist}.")

def create_container_item(ig_id, token, image_url, alt_text=None):
    url = f"https://graph.facebook.com/v20.0/{ig_id}/media"
    payload = {
        "image_url": image_url,
        "is_carousel_item": "true",
        "access_token": token
    }
    if alt_text:
        payload["alt_text"] = alt_text
    data = urllib.parse.urlencode(payload).encode("utf-8")
    req = urllib.request.Request(url, data=data)
    with urllib.request.urlopen(req, timeout=30) as resp:
        res = json.loads(resp.read().decode())
        return res["id"]

def create_carousel_container(ig_id, token, child_ids, caption):
    url = f"https://graph.facebook.com/v20.0/{ig_id}/media"
    payload = {
        "media_type": "CAROUSEL",
        "children": ",".join(child_ids),
        "caption": caption,
        "access_token": token
    }
    data = urllib.parse.urlencode(payload).encode("utf-8")
    req = urllib.request.Request(url, data=data)
    with urllib.request.urlopen(req, timeout=30) as resp:
        res = json.loads(resp.read().decode())
        return res["id"]

def publish_container(ig_id, token, creation_id):
    url = f"https://graph.facebook.com/v20.0/{ig_id}/media_publish"
    payload = {
        "creation_id": creation_id,
        "access_token": token
    }
    data = urllib.parse.urlencode(payload).encode("utf-8")
    req = urllib.request.Request(url, data=data)
    with urllib.request.urlopen(req, timeout=45) as resp:
        res = json.loads(resp.read().decode())
        return res["id"]

def get_media_permalink(media_id, token):
    url = f"https://graph.facebook.com/v20.0/{media_id}?fields=id,permalink,timestamp&access_token={token}"
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req, timeout=20) as resp:
        res = json.loads(resp.read().decode())
        return res.get("permalink")

def check_instagram_live(ig_id, token, target_day, target_title=""):
    """
    Queries Instagram Graph API for @iamsaravofficial to see if the episode
    for target_day is already published live on the account.
    Returns (True, permalink) if found, or (False, None) if not.
    """
    url = f"https://graph.facebook.com/v20.0/{ig_id}/media?fields=id,caption,permalink,timestamp&limit=25&access_token={token}"
    req = urllib.request.Request(url, headers={"User-Agent": "NalkudilStudio/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode("utf-8"))
        day_regex = re.compile(rf"\bDAY\s+0?{target_day}\s+OF\s+30\b", re.IGNORECASE)
        for m in data.get("data", []):
            cap = m.get("caption", "")
            if day_regex.search(cap):
                return True, m.get("permalink")
            if target_title and target_title.lower() in cap.lower() and "#sidisha" in cap.lower():
                return True, m.get("permalink")
        return False, None
    except Exception as e:
        print(f"[!] Warning: Instagram live check error ({e})")
        return False, None

def update_catalog_file(day_num, permalink):
    with open(CATALOG_FILE, "r", encoding="utf-8") as f:
        content = f.read()
    
    day_str = f'"day": {day_num},'
    idx = content.find(day_str)
    if idx == -1:
        raise ValueError(f"Could not locate day {day_num} block in catalog.js")
    
    next_day_idx = content.find('"day":', idx + len(day_str))
    limit = next_day_idx if next_day_idx != -1 else (idx + 3000)
    block = content[idx:limit]

    if '"instagram_url":' in block:
        new_block = re.sub(r'"instagram_url":\s*"[^"]*"', f'"instagram_url": "{permalink}"', block)
        new_block = re.sub(r'"status":\s*"[^"]+"', '"status": "PUBLISHED"', new_block)
        content = content[:idx] + new_block + content[limit:]
        with open(CATALOG_FILE, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"[+] Updated catalog.js for Day {day_num} with permalink: {permalink}")
        return

    match = re.search(r'"status":\s*"[^"]+"', block)
    if match:
        pos = idx + match.start()
        end_pos = idx + match.end()
        replacement = f'"status": "PUBLISHED",\n      "instagram_url": "{permalink}"'
        content = content[:pos] + replacement + content[end_pos:]
        with open(CATALOG_FILE, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"[+] Updated catalog.js for Day {day_num} with permalink: {permalink}")
    else:
        print(f"[!] Warning: Could not find status for Day {day_num} to replace.")

def main():
    print("==================================================")
    print("📸 NALKUDIL STUDIO: DAILY INSTAGRAM PUBLISHER")
    print(f"   Time (IST): {datetime.now(IST_TZ).strftime('%Y-%m-%d %H:%M:%S IST')}")
    print("==================================================")

    if not META_ACCESS_TOKEN:
        err_msg = (
            "🚨 <b>SID & ISHA AUTO-PUBLISH BLOCKED</b>\n\n"
            "Secret <code>META_ACCESS_TOKEN</code> is missing in GitHub repository secrets.\n"
            "Please publish today's episode manually from Nalkudil Social Studio."
        )
        notify_telegram(err_msg)
        print("[!] ERROR: META_ACCESS_TOKEN environment variable not set.")
        sys.exit(1)

    catalog_data = load_catalog()
    item = get_target_item(catalog_data)
    day_num = item["day"]
    title = item["title"]
    caption = item["caption"]

    if item.get("status") == "PUBLISHED" and item.get("instagram_url"):
        print(f"[*] Day {day_num} is ALREADY marked published in catalog: {item['instagram_url']}")
        print("    Nothing to do. Exiting cleanly.")
        sys.exit(0)

    # -------------------------------------------------------------
    # Live Instagram Pre-Flight Check: NEVER duplicate if already live!
    # -------------------------------------------------------------
    print(f"[*] Running pre-flight live check on Instagram for Day {day_num} ('{title}')...")
    is_live, live_permalink = check_instagram_live(INSTAGRAM_BUSINESS_ID, META_ACCESS_TOKEN, day_num, title)
    if is_live:
        print(f"[✓] Day {day_num} is ALREADY live on Instagram: {live_permalink}")
        print("    Skipping publication to avoid duplicate post. Updating catalog...")
        update_catalog_file(day_num, live_permalink)
        sys.exit(0)

    slide1_cdn = f"https://nalkudilstudio.github.io/nalkudil-social-studio/assets/sid_isha/slide1/day_{day_num:02d}.jpg"
    slide2_cdn = f"https://nalkudilstudio.github.io/nalkudil-social-studio/assets/sid_isha/slide2/day_{day_num:02d}.jpg"
    slide1_alt = item.get("slide1_alt")
    slide2_alt = item.get("slide2_alt")

    print(f"[*] Publishing Day {day_num}: '{title}'")
    print(f"    Slide 1: {slide1_cdn}")
    print(f"    Slide 2: {slide2_cdn}")
    if slide1_alt:
        print(f"    Slide 1 Alt: {slide1_alt[:55]}...")
    if slide2_alt:
        print(f"    Slide 2 Alt: {slide2_alt[:55]}...")

    try:
        print("[*] Creating Slide 1 container (with Alt Text)...")
        c1 = create_container_item(INSTAGRAM_BUSINESS_ID, META_ACCESS_TOKEN, slide1_cdn, alt_text=slide1_alt)
        print(f"    Container 1: {c1}")

        print("[*] Creating Slide 2 container (with Alt Text)...")
        c2 = create_container_item(INSTAGRAM_BUSINESS_ID, META_ACCESS_TOKEN, slide2_cdn, alt_text=slide2_alt)
        print(f"    Container 2: {c2}")

        print("[*] Creating Carousel container...")
        car_id = create_carousel_container(INSTAGRAM_BUSINESS_ID, META_ACCESS_TOKEN, [c1, c2], caption)
        print(f"    Carousel Container: {car_id}")

        print("[*] Executing Media Publish...")
        media_id = publish_container(INSTAGRAM_BUSINESS_ID, META_ACCESS_TOKEN, car_id)
        print(f"    Published Media ID: {media_id}")

        time.sleep(5)
        permalink = get_media_permalink(media_id, META_ACCESS_TOKEN)
        print(f"    ✅ LIVE PERMALINK: {permalink}")

        # Update local catalog
        update_catalog_file(day_num, permalink)

        # Telegram Success Dispatch
        ist_now = datetime.now(IST_TZ).strftime("%I:%M %p IST")
        success_msg = (
            f"<b>📸 SID & ISHA DAY {day_num:02d} IS LIVE ON INSTAGRAM!</b>\n\n"
            f"📖 <b>Title:</b> {title}\n"
            f"🔗 <b>Post:</b> {permalink}\n"
            f"🌐 <b>Social Studio:</b> https://nalkudilstudio.github.io/nalkudil-social-studio/\n"
            f"⏰ <b>Published At:</b> {ist_now}\n"
            f"🤖 <i>Automated via GitHub Actions</i>"
        )
        notify_telegram(success_msg)
        print("    ✅ Notification dispatched to Sarav.")

    except Exception as e:
        err_msg = (
            f"🚨 <b>SID & ISHA DAY {day_num:02d} AUTO-PUBLISH FAILED</b>\n\n"
            f"<b>Error:</b> <code>{str(e)}</code>\n\n"
            f"👉 <b>Manual Action Required:</b> Please open Nalkudil Social Studio and post manually before 10:15 AM IST!\n"
            f"https://nalkudilstudio.github.io/nalkudil-social-studio/"
        )
        notify_telegram(err_msg)
        print(f"[!] FATAL PUBLISH ERROR: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
