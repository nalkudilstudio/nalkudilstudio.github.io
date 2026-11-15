import json, re

with open('D:/Websites/nalkudilstudio.github.io/nalkudil-social-studio/catalog.js', 'r', encoding='utf-8') as f:
    cat = json.loads(re.search(r'window\.PUBLISHING_CATALOG\s*=\s*(\{[\s\S]*\});?\s*$', f.read()).group(1))

print('=== VERIFICATION SUMMARY ===')
# 1. sarav_ai
published_ai = [x for x in cat['sarav_ai'] if x.get('status') == 'PUBLISHED']
print(f"sarav_ai: {len(published_ai)} published out of {len(cat['sarav_ai'])}")
print("Day 44 status:", cat['sarav_ai'][43]['status'], "YT:", cat['sarav_ai'][43]['youtube_url'], "Poll:", cat['sarav_ai'][43].get('poll_url'))
print("Day 45 status:", cat['sarav_ai'][44]['status'], "YT:", cat['sarav_ai'][44]['youtube_url'], "Poll:", cat['sarav_ai'][44].get('poll_url'))
print("Day 46 status:", cat['sarav_ai'][45]['status'], "YT:", cat['sarav_ai'][45]['youtube_url'])

# 2. sarav_trends
print('\nsarav_trends:')
for t in cat['sarav_trends']:
    print(f"  {t.get('title')[:55]}... | Status: {t.get('status')} | YT: {t.get('youtube_url')}")

# 3. the_loop
published_loop = [x for x in cat['the_loop'] if x.get('status') == 'PUBLISHED']
print(f"\nthe_loop: {len(published_loop)} published out of {len(cat['the_loop'])}")
print("The Loop Ep 1 playlists:", cat['the_loop'][0].get('master_playlist'), "+", cat['the_loop'][0].get('mood_playlist'))

# 4. comic_tales
published_comic = [x for x in cat['comic_tales'] if x.get('status') == 'PUBLISHED']
print(f"\ncomic_tales: {len(published_comic)} published out of {len(cat['comic_tales'])}")
for ct in cat['comic_tales'][:5]:
    print(f"  Ep {ct['episode']}: {ct['status']} | YT: {ct.get('youtube_url')}")

# 5. sid_isha
published_sid = [x for x in cat['sid_isha'] if x.get('status') == 'PUBLISHED']
print(f"\nsid_isha: {len(published_sid)} published out of {len(cat['sid_isha'])}")
print("Day 1 slide1_alt sample:", cat['sid_isha'][0]['slide1_alt'][:80])
print("Day 1 slide2_alt sample:", cat['sid_isha'][0]['slide2_alt'][:80])

# 6. sarav_playlists
print(f"\nsarav_playlists: {len(cat['sarav_playlists'])} playlists listed")
for pl in cat['sarav_playlists']:
    print(f"  [{pl.get('category')}] {pl.get('title')} -> {pl.get('playlist_url')}")
