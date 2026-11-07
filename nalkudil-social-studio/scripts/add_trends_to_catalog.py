import json
import os

catalog_path = r'D:\Websites\nalkudilstudio.github.io\nalkudil-social-studio\catalog.js'
manifest_path = r'D:\YouTube\Sarav AI\sarav-xai-trends\trends_master_manifest.json'

with open(manifest_path, 'r', encoding='utf-8') as f:
    master = json.load(f)

trends_items = []
for t in master.get('trends', []):
    item = {
        'day': f"Trend {t['trendNumber']}",
        'episode': t['trendNumber'],
        'concept': t['topic'],
        'category': 'Zero-Cost AI Architecture',
        'filename': t['video_file'],
        'title': t['title'],
        'description': t['scenes'][0]['title'] + '\n\n' + t['voiceover_full'],
        'tags': ', '.join(t['tags']),
        'pinned_comment': t['pinned_comment'],
        'cover_url': f"assets/sarav_trends/cover_trend{String(t['trendNumber']).zfill(2) if 'String' in globals() else str(t['trendNumber']).zfill(2)}.png",
        'cover_filename': f"Shorts_Cover_Trend{str(t['trendNumber']).zfill(2)}.png",
        'status': t['status']
    }
    trends_items.append(item)

with open(catalog_path, 'r', encoding='utf-8') as f:
    content = f.read()

prefix = "window.PUBLISHING_CATALOG = "
if content.startswith(prefix):
    raw_json = content[len(prefix):].rstrip().rstrip(';')
    catalog = json.loads(raw_json)
    catalog["sarav_trends"] = trends_items
    with open(catalog_path, 'w', encoding='utf-8') as f:
        f.write("window.PUBLISHING_CATALOG = " + json.dumps(catalog, ensure_ascii=False, indent=2) + ";\n")
    print(f'✅ Successfully updated {len(trends_items)} sarav_trends in catalog.js!')
else:
    print('❌ Unexpected catalog.js prefix format')
