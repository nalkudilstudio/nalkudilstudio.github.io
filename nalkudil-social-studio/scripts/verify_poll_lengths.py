import json

with open(r"D:\Websites\nalkudilstudio.github.io\nalkudil-social-studio\catalog.js", "r", encoding="utf-8") as f:
    raw = f.read()

data = json.loads(raw.replace("window.PUBLISHING_CATALOG = ", "").rstrip(";\n "))

all_valid = True
for ep_data in data.get("sarav_ai", []):
    ep = ep_data.get("episode")
    poll = ep_data.get("poll", {})
    options = poll.get("options", [])
    for idx, opt in enumerate(options):
        if len(opt) > 80:
            print(f"FAILED: Ep {ep} Option {chr(65+idx)} length {len(opt)} > 80 chars: '{opt}'")
            all_valid = False

if all_valid:
    print("SUCCESS: Every single poll option across all episodes is <= 80 characters!")
print(f"Total Sarav AI Episodes: {len(data.get('sarav_ai', []))}")
print(f"Total Playlists: {len(data.get('sarav_playlists', []))}")
