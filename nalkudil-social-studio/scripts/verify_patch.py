with open(r"D:\Websites\nalkudilstudio.github.io\nalkudil-social-studio\index.html", "r", encoding="utf-8") as f:
    h = f.read()

checks = [
    "switchSuite('sarav_playlists'",
    "count-playlists",
    "buildPlaylistsCard",
    "copyPlaylistField",
    "poll_opt_0",
    "poll_opt_1",
    "poll_opt_2",
    "poll_opt_3",
    "whatsapp_post",
    "WhatsApp Channel Broadcast",
    "📋 Copy Question Only",
    "📋 Copy"
]

all_passed = True
for c in checks:
    present = c in h
    print(f"Check '{c}': {present}")
    if not present:
        all_passed = False

assert all_passed, "Some checks failed!"
print("\n>>> ALL INDEX.HTML CHECKS PASSED 100%! <<<")
