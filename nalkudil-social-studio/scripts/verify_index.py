with open(r"D:\Websites\nalkudilstudio.github.io\nalkudil-social-studio\index.html", "r", encoding="utf-8") as f:
    h = f.read()

checks = [
    "switchSuite('comic_tales'",
    "count-comic",
    "comic_tales: 'nss_published_comic_tales'",
    "buildComicTalesCard",
    "cat_traffic",
    "comic_full_packet",
    "tamil_dialogue"
]

all_passed = True
for c in checks:
    present = c in h
    print(f"Check '{c}': {present}")
    if not present:
        all_passed = False

if all_passed:
    print("ALL CHECKS PASSED!")
