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

last_idx = content.rfind('};')
if last_idx != -1:
    new_content = content[:last_idx].rstrip() + ',\n  "sarav_trends": ' + json.dumps(trends_items, indent=2) + '\n};\n'
    with open(catalog_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f'✅ Successfully appended {len(trends_items)} sarav_trends to catalog.js!')
else:
    print('❌ Could not find closing bracket in catalog.js')
