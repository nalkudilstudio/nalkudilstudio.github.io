import json
import re
import os
import shutil
from smart_trim import smart_trim
from generate_polls_100days import get_community_polls

CATALOG_PATH = r"D:\Websites\nalkudilstudio.github.io\nalkudil-social-studio\catalog.js"

print("=== 1. Loading catalog.js ===")
with open(CATALOG_PATH, "r", encoding="utf-8") as f:
    text = f.read()

prefix = text.split("=", 1)[0] + "= "
json_str = text.split("=", 1)[1].strip()
if json_str.endswith(";"):
    json_str = json_str[:-1].strip()

data = json.loads(json_str)

# ----------------------------------------------------------------------
# 1. COMIC TALES -> KARMA COURT (Case 1 | followed by title..)
# ----------------------------------------------------------------------
comic_tales = data.get("comic_tales", [])
print(f"Updating {len(comic_tales)} Comic Tales items to Karma Court...")

for i, item in enumerate(comic_tales, start=1):
    ep = item.get("episode") or i
    item["episode"] = ep
    item["day"] = f"Case {ep}"
    item["case_number"] = ep
    item["category"] = "Karma Court ⚖️"

    old_title = item.get("title", "")
    # Extract original Tamil topic title
    m = re.match(r"^(.*?)(?:\s*\|\s*Karma\s*(?:Strikes|Court)[\s\S]*)$", old_title)
    if m:
        tamil_topic = m.group(1).strip()
    else:
        tamil_topic = old_title.replace("#Shorts", "").replace("#TheLoop", "").strip()

    if not ("😂" in tamil_topic or "📢" in tamil_topic):
        tamil_topic += " 😂"

    # Strictly set: Karma Court: Case X | followed by title..
    if ep == 3:
        item["title"] = f"Karma Court: Case {ep} | Signal Red-ல இருக்கும்போதே Horn அடிக்கிற கும்பல்! 📢😂 #Shorts #TheLoop"
    else:
        item["title"] = f"Karma Court: Case {ep} | {tamil_topic} #Shorts #TheLoop"

    # Update description
    desc = item.get("description", "")
    desc = desc.replace("Karma Strikes (Poetic Divine Justice in Melogam)", "Karma Court ⚖️😂 | கர்மா கோர்ட் (Poetic Divine Justice in Melogam)")
    desc = desc.replace("SERIES: Karma Strikes", "SERIES: Karma Court ⚖️😂 | கர்மா கோர்ட்")
    desc = desc.replace("#KarmaStrikes", "#KarmaCourt")
    item["description"] = desc

    # Update pinned comment
    pinned = item.get("pinned_comment", "")
    pinned = pinned.replace("daily Karma Strikes", "daily Karma Court ⚖️😂")
    item["pinned_comment"] = pinned

    # Update tags
    tags = item.get("tags", "")
    tags = tags.replace("karma strikes", "karma court, karma court case, comic tales")
    item["tags"] = tags

    # Playlist
    item["playlist_name"] = "Karma Court ⚖️😂 | கர்மா கோர்ட் (Comic Tales)"
    item["playlist_url"] = "https://www.youtube.com/playlist?list=PLHuZo_k1eGx4"

# ----------------------------------------------------------------------
# 2. TECH RADAR TRENDS & COVERS
# ----------------------------------------------------------------------
trends = data.get("sarav_trends", [])
print(f"Updating {len(trends)} Tech Radar items & covers...")

for t in trends:
    ep = t.get("episode")
    if ep == 1:
        t["title"] = "Hit Claude’s Rate Limit? Never Pay $20 Again with 9Router #shorts #developer #tech"
        t["status"] = "PUBLISHED"
        t["youtube_id"] = "Nk2dD2AaCG0"
        t["youtube_url"] = "https://www.youtube.com/shorts/Nk2dD2AaCG0"
        t["cover_url"] = "assets/sarav_trends/cover_trend01.png"
        t["cover_filename"] = "Shorts_Cover_Trend01_9Router.png"
    elif ep == 2:
        t["title"] = "Stop Paying $200/mo for AI: Free Antigravity & Claude Code Setup #shorts #ai"
        t["status"] = "READY 🚀"
        t["cover_url"] = "assets/sarav_trends/cover_trend02.png"
        t["cover_filename"] = "Shorts_Cover_Trend02_Free_Setup.png"
    elif ep == 3:
        t["title"] = "Make AI Apps Look 100% Human Designed! (3 Essential Skills) #shorts #ai #coding"
        t["status"] = "PUBLISHED"
        t["youtube_id"] = "jmD_9Muyrtk"
        t["youtube_url"] = "https://www.youtube.com/shorts/jmD_9Muyrtk"
        t["cover_url"] = "assets/sarav_trends/cover_trend03.png"
        t["cover_filename"] = "Shorts_Cover_Trend03_Skills.png"
    elif ep == 4:
        t["title"] = "Google DeepMind Just Killed Single-Model Coding! (Gemini 4 Carbon + Hydrogen) #shorts #ai #coding"
        t["status"] = "PUBLISHED"
        t["youtube_id"] = "4H__rUlX1DU"
        t["youtube_url"] = "https://www.youtube.com/shorts/4H__rUlX1DU"
        t["cover_url"] = "assets/sarav_trends/cover_trend04.png"
        t["cover_filename"] = "Shorts_Cover_Trend04_Gemini_Carbon_Hydrogen.png"
    elif ep == 5:
        t["title"] = "Break the 1,000 Views Wall - Shorts Algorithm Blueprint #shorts #ai"
        t["status"] = "READY 🚀"
        t["cover_url"] = "assets/sarav_trends/cover_trend05.png"
        t["cover_filename"] = "Shorts_Cover_Trend05_Break_1K_Views_Wall.png"

# ----------------------------------------------------------------------
# 3. SARAV AI COMMUNITY POLLS (100% Verified Format & <= 75 char limit)
# ----------------------------------------------------------------------
sarav_ai = data.get("sarav_ai", [])
print(f"Updating {len(sarav_ai)} Sarav AI Community Polls...")

polls_source = get_community_polls()

for ep_item in sarav_ai:
    ep_num = ep_item.get("episode")
    if ep_num in polls_source:
        p_raw = polls_source[ep_num]
        
        # Trim options to <= 75 characters strictly
        trimmed_opts = [smart_trim(opt, 75) for opt in p_raw["options"]]
        for idx, opt in enumerate(trimmed_opts):
            assert len(opt) <= 75, f"Day {ep_num} option {idx+1} exceeds 75 chars: '{opt}' ({len(opt)} chars)"
            
        # Preserve existing live poll URL if present
        existing_poll = ep_item.get("poll", {})
        poll_url = existing_poll.get("poll_url") or existing_poll.get("poll_link")
        
        # Build community poll object
        q = p_raw["question"]
        correct_idx = p_raw["correct_index"]
        expl = p_raw["explanation"]
        
        # Build full_text packet
        full_text = (
            f"🗳️ COMMUNITY POLL • Day {ep_num}/100\n\n"
            f"{q}\n\n"
            f"A) {trimmed_opts[0]}\n"
            f"B) {trimmed_opts[1]}\n"
            f"C) {trimmed_opts[2]}\n\n"
            f"👉 Drop your explanation in the comments below!\n\n"
            f"💡 EXPLANATION:\n{expl}"
        )
        
        poll_obj = {
            "question": q,
            "options": trimmed_opts,
            "correct_index": correct_idx,
            "explanation": expl,
            "full_text": full_text
        }
        if poll_url:
            poll_obj["poll_url"] = poll_url
            
        ep_item["poll"] = poll_obj

# ----------------------------------------------------------------------
# 4. PLAYLIST HUB NAMES
# ----------------------------------------------------------------------
pls = data.get("sarav_playlists", [])
for p in pls:
    if p.get("id") == "karma_court":
        p["title"] = "Karma Court ⚖️😂 | கர்மா கோர்ட் (Comic Tales)"
        p["playlist_url"] = "https://www.youtube.com/playlist?list=PLHuZo_k1eGx4"

# ----------------------------------------------------------------------
# 5. WRITE BACK CATALOG.JS
# ----------------------------------------------------------------------
new_catalog_content = prefix + json.dumps(data, indent=2, ensure_ascii=False) + ";\n"
with open(CATALOG_PATH, "w", encoding="utf-8") as f:
    f.write(new_catalog_content)

print("✅ catalog.js successfully written!")
