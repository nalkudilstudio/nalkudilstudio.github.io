import re
import json

with open('D:/Websites/nalkudilstudio.github.io/nalkudil-social-studio/catalog.js', 'r', encoding='utf-8') as f:
    text = f.read()

# catalog.js sets window.PUBLISHING_CATALOG = { ... }
m = re.search(r'window\.PUBLISHING_CATALOG\s*=\s*(\{[\s\S]*\});?\s*$', text)
if m:
    catalog_json = m.group(1)
    catalog = json.loads(catalog_json)
    print("Keys in catalog:", list(catalog.keys()))
    for k, v in catalog.items():
        if isinstance(v, list):
            print(f"  {k}: {len(v)} items")
            if v and 'status' in v[0]:
                statuses = {}
                for item in v:
                    s = item.get('status', 'UNKNOWN')
                    statuses[s] = statuses.get(s, 0) + 1
                print(f"    Statuses: {statuses}")
else:
    print("Could not match window.PUBLISHING_CATALOG")
