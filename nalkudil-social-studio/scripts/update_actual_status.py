import json
import os
import re

CATALOG_PATH = r"D:\Websites\nalkudilstudio.github.io\nalkudil-social-studio\catalog.js"
INDEX_PATH = r"D:\Websites\nalkudilstudio.github.io\nalkudil-social-studio\index.html"

# 1. Load catalog.js
with open(CATALOG_PATH, "r", encoding="utf-8") as f:
    raw = f.read()

prefix = "window.PUBLISHING_CATALOG = "
json_str = raw.replace(prefix, "").rstrip(";\n ")
catalog = json.loads(json_str)

# Map of Sarav x AI live video IDs (Days 1 to 40)
sarav_live_map = {
    1: "1beFkdxqO-s",
    2: "mvegAJR9Qdg",
    3: "ghOUtQoi9x8",
    4: "kWRB1bpI1QY",
    5: "TgiUHtfkWig",
    6: "-krKiNXAH_Y",
    7: "A7p_ETb7V48",
    8: "EM7Ue3j2u1c",
    9: "dI-iFQ1j_SY",
    10: "xnhOWpL_P0E",
    11: "os_bDL3rLKM",
    12: "tZ_ka5zOvz0",
    13: "xjEeQ-YiteU",
    14: "i9KuTmULUfs",
    15: "KFLDBvjufkA",
    16: "_yAo-Ej18eg",
    17: "LXaadvIMv6s",
    18: "8lG7o0zeCLA",
    19: "c-DmZdCa7W0",
    20: "-XcuPBDl2aM",
    21: "5MKvLB09J-c",
    22: "-AaLQMEHZAU",
    23: "cCyNsnQAe-Q",
    24: "8cc_WGDMOBU",
    25: "qY2LbgivWWU",
    26: "lswnFGuDIq8",
    27: "KSSWj-5mPus",
    28: "O6R4vPadEgk",
    29: "fwShBL1tWvo",
    30: "L61U79mMTLY",
    31: "ORpH9c0crUM",
    32: "smgvSDF_r2Y",
    33: "7EjgeXQrLsk",
    34: "08iitruCQgs",
    35: "5UY-dd-ZHN4",
    36: "ktqwATHzvS8",
    37: "fav-pse9DUs",
    38: "-BT8QtTRG8o",
    39: "c-R3SjKeUTg",
    40: "f-CCh39WHfg",
}

# Map of The Loop live video IDs (Episodes 1 to 34)
loop_live_map = {
    1: "X63h_VeCsW8",
    2: "5_DCih2Pnb4",
    3: "CjSIFUaPOFY",
    4: "RDhmdNBA3Jo",
    5: "0ou3XMg29q0",
    6: "-lV7TCRAI5Y",
    7: "bU2OeV8wCLQ",
    8: "1wMeutJGtc0",
    9: "X_QalCX-Q0U",
    10: "ilF0HoPIQtg",
    11: "7wF29SD6-LI",
    12: "g4V86FGbdeM",
    13: "8yx_NtGYVpQ",
    14: "4L1rkPyAg1c",
    15: "G-VIYdpaQ2g",
    16: "2f1ma97EXmg",
    17: "FNCk21kH0_A",
    18: "vjhlHng_3Fk",
    19: "mbckYG85Hbk",
    20: "ifM_tOaT-jw",
    21: "CIC8O381F4c",
    22: "g4TwV5lM1D8",
    23: "2vXrp2kVrB4",
    24: "GwmdZN5d0e8",
    25: "kNncJhSb8Zc",
    26: "zamOBe0-vPo",
    27: "MZrEJ-xejZE",
    28: "36Ai0o4E8HU",
    29: "IqP5HLEhgvY",
    30: "bSkSpR5CyGU",
    31: "YCapkhSNgT0",
    32: "JyL3bTLTM6E",
    33: "OeCjG-VmgMc",
    34: "6lp_9vJKdKA",
}

# Update sarav_ai
sarav_published_count = 0
for item in catalog.get("sarav_ai", []):
    ep = item.get("episode")
    if ep in sarav_live_map:
        item["status"] = "PUBLISHED"
        item["youtube_id"] = sarav_live_map[ep]
        item["youtube_url"] = f"https://www.youtube.com/shorts/{sarav_live_map[ep]}"
        sarav_published_count += 1
    else:
        item["status"] = "QUEUED"
print(f"Updated sarav_ai: {sarav_published_count} published")

# Update the_loop
loop_published_count = 0
for item in catalog.get("the_loop", []):
    ep = item.get("episode")
    if ep in loop_live_map:
        item["status"] = "PUBLISHED"
        item["youtube_id"] = loop_live_map[ep]
        item["youtube_url"] = f"https://www.youtube.com/shorts/{loop_live_map[ep]}"
        loop_published_count += 1
    else:
        item["status"] = "QUEUED"
print(f"Updated the_loop: {loop_published_count} published")

# Update sid_isha
sidisha_published_count = 0
for item in catalog.get("sid_isha", []):
    day = item.get("day")
    if day == 1:
        item["status"] = "PUBLISHED"
        item["instagram_url"] = "https://www.instagram.com/p/DfL5Rd7n68z/"
        sidisha_published_count += 1
    else:
        item["status"] = "READY 🚀"
print(f"Updated sid_isha: {sidisha_published_count} published")

# Update inkling_ig
inkling_published_count = 0
for item in catalog.get("inkling_ig", []):
    ep = item.get("episode")
    # Tale 58 (Reel Ep 002) is published
    if ep == 58 or ep == 52:
        item["status"] = "PUBLISHED"
        item["instagram_url"] = "https://www.instagram.com/reel/DfKcK-3CEuJ/"
        inkling_published_count += 1
    else:
        item["status"] = "QUEUED ⏳"
print(f"Updated inkling_ig: {inkling_published_count} published")

# Update comic_tales
for item in catalog.get("comic_tales", []):
    ep = item.get("episode")
    if ep == 1:
        item["youtube_url"] = "https://youtube.com/shorts/XgwwrULEAAw"

# Save updated catalog.js
with open(CATALOG_PATH, "w", encoding="utf-8") as f:
    f.write(prefix + json.dumps(catalog, indent=2, ensure_ascii=False) + ";\n")
print(f"Saved updated {CATALOG_PATH} successfully!")
