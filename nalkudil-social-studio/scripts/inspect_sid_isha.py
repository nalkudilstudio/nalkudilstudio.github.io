import json, re

with open('D:/Websites/nalkudilstudio.github.io/nalkudil-social-studio/catalog.js', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'window\.PUBLISHING_CATALOG\s*=\s*(\{[\s\S]*\});?\s*$', text)
cat = json.loads(m.group(1))

for item in cat['sid_isha']:
    print(f"Day {item.get('day')}: {item.get('title')} | Status: {item.get('status')} | IG: {item.get('instagram_url')}")
