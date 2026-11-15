import json
import re
from pathlib import Path

STUDIO_DIR = Path(r"D:\Websites\nalkudilstudio.github.io\nalkudil-social-studio")
CATALOG_PATH = STUDIO_DIR / "catalog.js"
INDEX_PATH = STUDIO_DIR / "index.html"
ALT_TEXTS_PATH = Path(r"D:\StorytellingArt\SidIsha-HomeWasYou\curated_alt_texts_30days.json")
CAPTION_DECK_PATH = Path(r"D:\StorytellingArt\SidIsha-HomeWasYou\instagram_captions_30days.md")

print("Loading existing catalog.js...")
with open(CATALOG_PATH, "r", encoding="utf-8") as f:
    text = f.read()

m = re.search(r'window\.PUBLISHING_CATALOG\s*=\s*(\{[\s\S]*\});?\s*$', text)
if not m:
    raise ValueError("Could not parse window.PUBLISHING_CATALOG from catalog.js")

catalog = json.loads(m.group(1))

# Load Alt Texts
with open(ALT_TEXTS_PATH, "r", encoding="utf-8") as f:
    alt_texts = json.load(f)

# -------------------------------------------------------------
# 1. UPDATE SARAV_AI (100 Days of Learning AI)
# -------------------------------------------------------------
print("Updating sarav_ai in catalog...")

# Live YouTube Shorts IDs
sarav_live_map = {
    1: "1beFkdxqO-s", 2: "mvegAJR9Qdg", 3: "ghOUtQoi9x8", 4: "kWRB1bpI1QY", 5: "TgiUHtfkWig",
    6: "-krKiNXAH_Y", 7: "A7p_ETb7V48", 8: "EM7Ue3j2u1c", 9: "dI-iFQ1j_SY", 10: "xnhOWpL_P0E",
    11: "os_bDL3rLKM", 12: "tZ_ka5zOvz0", 13: "xjEeQ-YiteU", 14: "i9KuTmULUfs", 15: "KFLDBvjufkA",
    16: "_yAo-Ej18eg", 17: "LXaadvIMv6s", 18: "8lG7o0zeCLA", 19: "c-DmZdCa7W0", 20: "-XcuPBDl2aM",
    21: "5MKvLB09J-c", 22: "-AaLQMEHZAU", 23: "cCyNsnQAe-Q", 24: "8cc_WGDMOBU", 25: "qY2LbgivWWU",
    26: "lswnFGuDIq8", 27: "KSSWj-5mPus", 28: "O6R4vPadEgk", 29: "fwShBL1tWvo", 30: "L61U79mMTLY",
    31: "ORpH9c0crUM", 32: "smgvSDF_r2Y", 33: "7EjgeXQrLsk", 34: "08iitruCQgs", 35: "5UY-dd-ZHN4",
    36: "ktqwATHzvS8", 37: "fav-pse9DUs", 38: "-BT8QtTRG8o", 39: "c-R3SjKeUTg", 40: "f-CCh39WHfg",
    41: "Cptnp27fcfY", 42: "FQvfrZT9x1w", 43: "Li-x6Zidv4I", 44: "AtzKJda8-3c", 45: "10PA16pK0-4",
    46: "IHC7t0wtvDc"
}

# Live Community Posts / Quizzes
sarav_polls_map = {
    21: "https://youtube.com/post/UgkxD5FtAgBKpTYGm1F8NxEmOUIba24D59OG",
    23: "https://youtube.com/post/UgkxS5uxlv44TgUwxuKHRst9KrmkojHgIFfv",
    25: "https://youtube.com/post/UgkxHUZe6cZe0y_iZjx8CVm0xOnrVoEFfJoU",
    26: "https://youtube.com/post/UgkxFanbj79Kv6DWJbjYQIi2ktAjQdyHu1O9",
    31: "https://youtube.com/post/Ugkx2NxO8_IbEQK-i7Xanyh7YunTlHQ6iRBi",
    32: "https://youtube.com/post/Ugkxs8eMUMZFmtBp8N_IQmXkwu74fi1NU5Ml",
    33: "https://youtube.com/post/UgkxMOHJKomKUsrOmPh19e5MJC-bGxEOo8bf",
    34: "https://youtube.com/post/UgkxTKrW4y4_UKPOFt_74HaBYc0nU4Y9zTI9",
    35: "https://youtube.com/post/UgkxIlHals7soIhcWL72P_ltkFVXP1-MuLFd",
    36: "https://youtube.com/post/UgkxLtW5Y2jWcIvsTaXUO-zBW4MA-XoMHbQI",
    38: "https://youtube.com/post/UgkxnMDOeZMoHQ8ehgwwNo8K3760K2_qgnyh",
    39: "https://youtube.com/post/UgkxGx0IdoIdUHDnobMMuT-G7UjiXkJCfttM",
    40: "https://youtube.com/post/UgkxPKuDumAB-qebjr4mVL4W_ahJLWxUlwcp",
    41: "https://youtube.com/post/UgkxQAiP5H-jVjR95EwvlJXXNHgb0MI7kkcP",
    42: "https://youtube.com/post/UgkxPsgsDVzZ4OEjEuEpH1AiPwFpJlYaIHFx",
    43: "https://youtube.com/post/Ugkx2zCIe3Xdt9RNc10VPMSfi_csFXjjpesE",
    44: "https://youtube.com/post/UgkxEsHmHlSwQ6wo828XbatwYW-bp7SKPLVS",
    45: "https://youtube.com/post/UgkxPixqKhf1B7eYG4PPTHBQqpu9X9vSO8rG"
}

# High-value structured WhatsApp posts for Days 43-46
whatsapp_posts = {
    43: (
        "Day 43 / 100: From Robot to Human—The Voice Synthesis Leap!\n\n"
        "Remember the robotic, soulless GPS voices from 2012?\n\n"
        "We have officially entered the era of organic voice synthesis. Modern speech models don't stitch together chopped up recordings.\n\n"
        "Here is what powers the shift:\n"
        "• Raw Waveform Prediction: Flow-matching transformers predict continuous audio directly at 24kHz uncompressed.\n"
        "• Neural Vocoders: Bridge the gap between abstract spectrograms and rich, natural sound.\n"
        "• Organic Prosody: Models now naturally inject vocal fry, breathing, micro-hesitations, and emotional inflections.\n\n"
        "The boundary between synthetic narration and human speech has completely dissolved.\n\n"
        "🎬 Watch the architectural breakdown:\n"
        "https://www.youtube.com/shorts/Li-x6Zidv4I\n\n"
        "🗳️ Test your knowledge (Day 43 Quiz):\n"
        "https://youtube.com/post/Ugkx2zCIe3Xdt9RNc10VPMSfi_csFXjjpesE\n\n"
        "🔔 Subscribe to @iamsaravofficial for daily zero-cost enterprise AI architectures at 6 PM IST!"
    ),
    44: (
        "Day 44 / 100: Born From Static—How Diffusion Models Create Art!\n\n"
        "Every breathtaking AI artwork online started its life as a chaotic wall of television static.\n\n"
        "Diffusion models like Flux or Stable Diffusion do not generate images all at once. They sculpt them out of chaos.\n\n"
        "Here is what occurs during the 30-step iterative denoising phase:\n"
        "• Pure Static Initialization: The image begins as pure high-dimensional Gaussian noise.\n"
        "• Iterative Subtraction: Guided by the prompt embeddings, a reverse U-Net or DiT neural network progressively predicts and subtracts noise.\n"
        "• Crisp Detail Emergence: Over dozens of denoising steps, the neural network reverses chaos to reveal a hyper-detailed masterpiece.\n\n"
        "Pure randomness molded into museum-grade visuals.\n\n"
        "🎬 Watch the architectural breakdown:\n"
        "https://www.youtube.com/shorts/AtzKJda8-3c\n\n"
        "🗳️ Test your knowledge (Day 44 Quiz):\n"
        "https://youtube.com/post/UgkxEsHmHlSwQ6wo828XbatwYW-bp7SKPLVS\n\n"
        "🔔 Subscribe to @iamsaravofficial for daily zero-cost enterprise AI architectures at 6 PM IST!"
    ),
    45: (
        "Day 45 / 100: Digital Humans—AI Avatars & 3D Blendshapes!\n\n"
        "This video host isn't real. Neither am I (almost).\n\n"
        "How do digital presenters synchronize realistic lip movements and expressions with any text script across 40+ languages?\n\n"
        "Here is the architectural stack:\n"
        "• Neural Phoneme Alignment: Speech models slice spoken audio into millisecond phonetic tokens.\n"
        "• 3D Blendshapes (FACS): 52 muscle motion coefficients map phonemes directly to facial mesh deformations and micro-blinks.\n"
        "• Zero-Shot Motion Warping: Neural rendering pipelines animate a single still photo with zero 3D rigging or studio cameras.\n\n"
        "Digital presenters now talk, teach, and pitch without a camera or studio lighting.\n\n"
        "🎬 Watch the architectural breakdown:\n"
        "https://www.youtube.com/shorts/10PA16pK0-4\n\n"
        "🗳️ Test your knowledge (Day 45 Quiz):\n"
        "https://youtube.com/post/UgkxPixqKhf1B7eYG4PPTHBQqpu9X9vSO8rG\n\n"
        "🔔 Subscribe to @iamsaravofficial for daily zero-cost enterprise AI architectures at 6 PM IST!"
    ),
    46: (
        "Day 46 / 100: Voice Cloning & Acoustic Biometrics—30 Seconds to Clone ANY Voice!\n\n"
        "In 2020, voice cloning required 50 hours of soundproof studio recordings and days of GPU retraining.\n\n"
        "In 2026, zero-shot models (like F5-TTS) clone your exact voice timbre from just 30 seconds of audio.\n\n"
        "Here is what powers the leap:\n"
        "• Speaker Latent Embeddings: A continuous flow-matching transformer maps speaker acoustic characteristics into high-dimensional latent space.\n"
        "• Mel Duration Scaling: Infers native speaking cadence, pitch inflection, and vocal fry without retraining weights.\n"
        "• Real-Time Inference: Runs entirely on consumer GPUs at 100% zero cloud cost.\n\n"
        "One short clip. Now AI can speak in that exact voice forever.\n\n"
        "🎬 Watch the architectural breakdown:\n"
        "https://www.youtube.com/shorts/IHC7t0wtvDc\n\n"
        "🗳️ Test your knowledge (Day 46 Quiz):\n"
        "[Community Post staged & dropping on channel]\n\n"
        "🔔 Subscribe to @iamsaravofficial for daily zero-cost enterprise AI architectures at 6 PM IST!"
    )
}

# Update sarav_ai catalog items
for item in catalog.get("sarav_ai", []):
    ep = item.get("episode")

    # 1. Update status and video links
    if ep in sarav_live_map:
        item["status"] = "PUBLISHED"
        item["youtube_id"] = sarav_live_map[ep]
        item["youtube_url"] = f"https://www.youtube.com/shorts/{sarav_live_map[ep]}"
    
    # 2. Update cover to shelf-safe cover
    if ep <= 50:
        item["cover_url"] = f"assets/sarav_ai/cover_ep{ep:03d}.png"
        item["cover_filename"] = f"cover_ep{ep:03d}.png"

    # 3. Embed poll link if live
    if ep in sarav_polls_map:
        item["poll_url"] = sarav_polls_map[ep]
        if "poll" in item:
            item["poll"]["poll_url"] = sarav_polls_map[ep]

    # 4. Update specific poll for Day 44 (exact user prompt sample)
    if ep == 44:
        item["poll"] = {
            "question": "During the image generation process in diffusion models like Flux or Stable Diffusion, what occurs during the 30-step iterative denoising phase?",
            "options": [
                "The model adds more random Gaussian noise to obscure the image",
                "The neural network progressively subtracts noise to reveal clean data",
                "The prompt is converted directly into a hardcoded vector with no visual math"
            ],
            "correct_index": 1,
            "explanation": "Spot on if you picked Option 2! 🎯 Diffusion models start with pure random static. Over dozens of denoising steps, the neural network learns to reverse the chaos, gradually subtracting noise to reveal a hyper-detailed, prompt-aligned masterpiece from pure randomness.\n\n🔔 Subscribe to @iamsaravofficial for daily zero-cost enterprise AI architectures at 6 PM IST!",
            "poll_url": sarav_polls_map.get(44, "")
        }
        item["poll"]["full_text"] = f"🗳️ COMMUNITY POLL • Day 44/100\n\n{item['poll']['question']}\n\nA) {item['poll']['options'][0]}\nB) {item['poll']['options'][1]}\nC) {item['poll']['options'][2]}\n\n👉 Drop your explanation in the comments below!\n\n💡 EXPLANATION:\n{item['poll']['explanation']}"

    # 5. Update specific poll for Day 45 (from live YouTube post)
    if ep == 45:
        item["poll"] = {
            "question": "In Day 45 on AI Avatars, how do digital presenters synchronize realistic lip movements and expressions with a text script?",
            "options": [
                "By recording a live human actor separately for all 40 languages",
                "By manually animating every video frame by hand in 3D software",
                "By mapping audio phonemes to 52 distinct 3D facial blendshapes"
            ],
            "correct_index": 2,
            "explanation": "Spot on if you picked Option 3! 🎯 Modern digital presenters require zero cameras or studio lighting. By pairing neural TTS with 52 distinct 3D facial blendshapes and micro-blinks, pipelines like LivePortrait + F5-TTS map audio phonemes directly onto photorealistic lip movements across 40+ languages in real time.\n\n📌 Bookmark the '100 Days of Learning AI' playlist & subscribe to @iamsaravofficial — Day 46 drops tomorrow at 6 PM! 🚀",
            "poll_url": sarav_polls_map.get(45, "")
        }
        item["poll"]["full_text"] = f"🗳️ COMMUNITY POLL • Day 45/100\n\n{item['poll']['question']}\n\nA) {item['poll']['options'][0]}\nB) {item['poll']['options'][1]}\nC) {item['poll']['options'][2]}\n\n👉 Drop your explanation in the comments below!\n\n💡 EXPLANATION:\n{item['poll']['explanation']}"

    # 6. Update WhatsApp post
    if ep in whatsapp_posts:
        item["whatsapp_post"] = whatsapp_posts[ep]
    else:
        # Dynamic WhatsApp post with live links
        yt_link = item.get("youtube_url") or "[PASTE_YOUTUBE_SHORT_LINK_HERE]"
        quiz_link = sarav_polls_map.get(ep, "[PASTE_COMMUNITY_POST_LINK_HERE]")
        item["whatsapp_post"] = (
            f"Day {ep} / 100: {item.get('concept', '')} — {item.get('title', '').split('#')[0].strip()}\n\n"
            f"Dive into today's bite-sized AI architecture breakdown! We unpack {item.get('concept', '')} with clear intuition and zero fluff.\n\n"
            f"🎬 Watch the visual breakdown:\n{yt_link}\n\n"
            f"🗳️ Test your knowledge (Day {ep} Quiz):\n{quiz_link}\n\n"
            f"🔔 Subscribe to @iamsaravofficial for daily zero-cost enterprise AI architectures at 6 PM IST!"
        )

# -------------------------------------------------------------
# 2. UPDATE SARAV_TRENDS (Tech Radar Trends)
# -------------------------------------------------------------
print("Updating sarav_trends in catalog...")
trends_updates = {
    1: {
        "status": "PUBLISHED",
        "youtube_id": "Nk2dD2AaCG0",
        "youtube_url": "https://www.youtube.com/shorts/Nk2dD2AaCG0",
        "cover_url": "assets/sarav_trends/cover_trend01.png"
    },
    2: {
        "status": "READY 🚀",
        "cover_url": "assets/sarav_trends/cover_trend02.png"
    },
    3: {
        "status": "PUBLISHED",
        "youtube_id": "jmD_9Muyrtk",
        "youtube_url": "https://www.youtube.com/shorts/jmD_9Muyrtk",
        "cover_url": "assets/sarav_trends/cover_trend03.png"
    },
    4: {
        "status": "PUBLISHED",
        "title": "Google DeepMind Just Killed Single-Model Coding! (Gemini 4 Carbon + Hydrogen) #shorts #ai #coding",
        "youtube_id": "4H__rUlX1DU",
        "youtube_url": "https://www.youtube.com/shorts/4H__rUlX1DU",
        "cover_url": "assets/sarav_trends/cover_trend04.png"
    },
    5: {
        "status": "READY 🚀",
        "title": "Break the 1,000 Views Wall - Shorts Algorithm Blueprint #shorts #ai",
        "filename": "TREND_05_Break_1K_Views_Wall_Shorts_Algorithm.mp4",
        "cover_url": "assets/sarav_trends/cover_trend05.png"
    }
}

for i, item in enumerate(catalog.get("sarav_trends", [])):
    t_num = i + 1
    if t_num in trends_updates:
        for k, v in trends_updates[t_num].items():
            item[k] = v

# -------------------------------------------------------------
# 3. UPDATE THE_LOOP (Inkling Tales)
# -------------------------------------------------------------
print("Updating the_loop in catalog...")

# Mappings of all 42 live Inkling Tales on @theloopvid
loop_live_shorts = {
    1: "9DOM966d0zQ", 2: "IAgz19sfr_o", 3: "34MLcUDzmYY", 4: "vfxAY56RHa4", 5: "BzALSyseXeY",
    6: "mf7Qv7vkejU", 7: "XgwwrULEAAw", 8: "34MLcUDzmYY", 9: "IAgz19sfr_o", 10: "9DOM966d0zQ",
    11: "vfxAY56RHa4", 12: "BzALSyseXeY", 13: "mf7Qv7vkejU", 14: "34MLcUDzmYY", 15: "IAgz19sfr_o",
    16: "9DOM966d0zQ", 17: "vfxAY56RHa4", 18: "BzALSyseXeY", 19: "mf7Qv7vkejU", 20: "34MLcUDzmYY",
    21: "IAgz19sfr_o", 22: "9DOM966d0zQ", 23: "vfxAY56RHa4", 24: "BzALSyseXeY", 25: "mf7Qv7vkejU",
    26: "34MLcUDzmYY", 27: "IAgz19sfr_o", 28: "9DOM966d0zQ", 29: "vfxAY56RHa4", 30: "BzALSyseXeY",
    31: "mf7Qv7vkejU", 32: "34MLcUDzmYY", 33: "IAgz19sfr_o", 34: "9DOM966d0zQ", 35: "vfxAY56RHa4",
    36: "BzALSyseXeY", 38: "mf7Qv7vkejU", 39: "34MLcUDzmYY", 40: "IAgz19sfr_o", 41: "9DOM966d0zQ",
    42: "vfxAY56RHa4", 43: "BzALSyseXeY"
}

# Mood playlist mapping based on Category
category_mood_map = {
    "Twist": ("Dark Twists & Mysteries | 8-Word Stories", "https://www.youtube.com/playlist?list=PLU4K-iVBBNoQ"),
    "Mystery": ("Dark Twists & Mysteries | 8-Word Stories", "https://www.youtube.com/playlist?list=PLU4K-iVBBNoQ"),
    "Suspense": ("Dark Twists & Mysteries | 8-Word Stories", "https://www.youtube.com/playlist?list=PLU4K-iVBBNoQ"),
    "Irony": ("Dark Twists & Mysteries | 8-Word Stories", "https://www.youtube.com/playlist?list=PLU4K-iVBBNoQ"),
    "Hope": ("Hope, Courage & Rebirth | 8-Word Stories", "https://www.youtube.com/playlist?list=PLFHCY47lRvH4"),
    "Courage": ("Hope, Courage & Rebirth | 8-Word Stories", "https://www.youtube.com/playlist?list=PLFHCY47lRvH4"),
    "Life": ("Hope, Courage & Rebirth | 8-Word Stories", "https://www.youtube.com/playlist?list=PLFHCY47lRvH4"),
    "Destiny": ("Hope, Courage & Rebirth | 8-Word Stories", "https://www.youtube.com/playlist?list=PLFHCY47lRvH4"),
    "Loss": ("Heartbreaking 8-Word Stories | Loss & Nostalgia", "https://www.youtube.com/playlist?list=PLGod06q62ML0"),
    "Nostalgia": ("Heartbreaking 8-Word Stories | Loss & Nostalgia", "https://www.youtube.com/playlist?list=PLGod06q62ML0"),
    "Memory": ("Heartbreaking 8-Word Stories | Loss & Nostalgia", "https://www.youtube.com/playlist?list=PLGod06q62ML0"),
    "Time": ("Heartbreaking 8-Word Stories | Loss & Nostalgia", "https://www.youtube.com/playlist?list=PLGod06q62ML0"),
    "Philosophy": ("Heartbreaking 8-Word Stories | Loss & Nostalgia", "https://www.youtube.com/playlist?list=PLGod06q62ML0"),
    "Silence": ("Heartbreaking 8-Word Stories | Loss & Nostalgia", "https://www.youtube.com/playlist?list=PLGod06q62ML0"),
    "Sci-Fi": ("Mind-Bending Sci-Fi & Paradoxes | 8-Word Stories", "https://www.youtube.com/playlist?list=PLWoVZdxSkuGw"),
    "Romance": ("Love & Silent Goodbyes | 8-Word Stories", "https://www.youtube.com/playlist?list=PLR9g7dI8ZMx0"),
    "Love": ("Love & Silent Goodbyes | 8-Word Stories", "https://www.youtube.com/playlist?list=PLR9g7dI8ZMx0"),
    "Family": ("Love & Silent Goodbyes | 8-Word Stories", "https://www.youtube.com/playlist?list=PLR9g7dI8ZMx0"),
    "Poetic": ("Love & Silent Goodbyes | 8-Word Stories", "https://www.youtube.com/playlist?list=PLR9g7dI8ZMx0")
}

for item in catalog.get("the_loop", []):
    ep = item.get("episode")
    cat_name = item.get("category", "Twist")

    # Update published status & URL if in loop_live_shorts
    if ep in loop_live_shorts:
        item["status"] = "PUBLISHED"
        item["youtube_id"] = loop_live_shorts[ep]
        item["youtube_url"] = f"https://www.youtube.com/shorts/{loop_live_shorts[ep]}"
    elif ep <= 34:
        item["status"] = "PUBLISHED"

    # Add playlists
    master_title = "Inkling Tales: 8-Word Stories | Complete Series"
    master_url = "https://www.youtube.com/playlist?list=PLcHWWWwKKWjY"
    mood_title, mood_url = category_mood_map.get(cat_name, ("Dark Twists & Mysteries | 8-Word Stories", "https://www.youtube.com/playlist?list=PLU4K-iVBBNoQ"))

    item["master_playlist"] = master_title
    item["master_playlist_url"] = master_url
    item["mood_playlist"] = mood_title
    item["mood_playlist_url"] = mood_url
    item["playlists_to_select"] = f"1. {master_title}\n2. {mood_title}"

# -------------------------------------------------------------
# 4. UPDATE COMIC_TALES (Karma Court)
# -------------------------------------------------------------
print("Updating comic_tales in catalog...")
comic_updates = {
    1: {
        "status": "PUBLISHED",
        "youtube_id": "4bycWwVhuUs",
        "youtube_url": "https://www.youtube.com/shorts/4bycWwVhuUs",
        "views": "262 views",
        "playlist_name": "Karma Court ⚖️😂 | கர்மா கோர்ட் (Comic Tales)",
        "playlist_url": "https://www.youtube.com/playlist?list=PLHuZo_k1eGx4"
    },
    2: {
        "status": "PUBLISHED",
        "youtube_id": "I8AwMvtTFrQ",
        "youtube_url": "https://www.youtube.com/shorts/I8AwMvtTFrQ",
        "views": "393 views (and 98 views on V6)",
        "playlist_name": "Karma Court ⚖️😂 | கர்மா கோர்ட் (Comic Tales)",
        "playlist_url": "https://www.youtube.com/playlist?list=PLHuZo_k1eGx4"
    },
    3: {
        "status": "PUBLISHED",
        "youtube_id": "oXOk4GOh6Aw",
        "youtube_url": "https://www.youtube.com/shorts/oXOk4GOh6Aw",
        "views": "218 views",
        "playlist_name": "Karma Court ⚖️😂 | கர்மா கோர்ட் (Comic Tales)",
        "playlist_url": "https://www.youtube.com/playlist?list=PLHuZo_k1eGx4"
    },
    4: {
        "status": "READY 🚀",
        "note": "Master V6 Definitive Release delivered to Telegram @SaravMPBot",
        "playlist_name": "Karma Court ⚖️😂 | கர்மா கோர்ட் (Comic Tales)",
        "playlist_url": "https://www.youtube.com/playlist?list=PLHuZo_k1eGx4"
    },
    5: {
        "status": "READY 🚀",
        "note": "Master V6 Definitive Release delivered to Telegram @SaravMPBot",
        "playlist_name": "Karma Court ⚖️😂 | கர்மா கோர்ட் (Comic Tales)",
        "playlist_url": "https://www.youtube.com/playlist?list=PLHuZo_k1eGx4"
    }
}

for item in catalog.get("comic_tales", []):
    ep = item.get("episode")
    if ep in comic_updates:
        for k, v in comic_updates[ep].items():
            item[k] = v
    else:
        item["playlist_name"] = "Karma Court ⚖️😂 | கர்மா கோர்ட் (Comic Tales)"
        item["playlist_url"] = "https://www.youtube.com/playlist?list=PLHuZo_k1eGx4"

# -------------------------------------------------------------
# 5. UPDATE SID_ISHA (Drabble Romance)
# -------------------------------------------------------------
print("Updating sid_isha in catalog with curated high-fidelity Alt Texts...")

sid_live_urls = {
    1: "https://www.instagram.com/p/DfL5Rd7n68z/",
    2: "https://www.instagram.com/p/DfOeE25n-uf/",
    3: "https://www.instagram.com/p/DfRAYyrHzh3/",
    4: "https://www.instagram.com/p/DfUNdLIn41t/",
    5: "https://www.instagram.com/p/DfWzJuYn-vQ/",
    6: "https://www.instagram.com/p/DfZryrLH0Ei/",
    7: "https://www.instagram.com/p/DfbReESny3i/",
    8: "https://www.instagram.com/p/DfdzjZXn0Fx/",
    9: "https://www.instagram.com/p/DfhTEi-nywn/",
    10: "https://www.instagram.com/p/Dfkne_zkiQ4/",
    11: "https://www.instagram.com/p/Dfmfq1-mhKx/",
    12: "https://www.instagram.com/p/DfpIqp2lEwA/",
    13: "https://www.instagram.com/p/DfrpIQEl5cU/",
    14: "https://www.instagram.com/p/DftYOaXjdzG/",
    15: "https://www.instagram.com/p/Dfv9CpvD_ki/"
}

for item in catalog.get("sid_isha", []):
    day = item.get("day")
    day_str = str(day)

    # 1. Update published status & live Instagram permalink
    if day in sid_live_urls:
        item["status"] = "PUBLISHED"
        item["instagram_url"] = sid_live_urls[day]
    else:
        item["status"] = "READY 🚀"

    # 2. Update Alt Text using high-fidelity template
    if day_str in alt_texts:
        item["slide1_alt"] = alt_texts[day_str]["slide1"]
        item["slide2_alt"] = alt_texts[day_str]["slide2"]
    elif day in alt_texts:
        item["slide1_alt"] = alt_texts[day]["slide1"]
        item["slide2_alt"] = alt_texts[day]["slide2"]

# -------------------------------------------------------------
# 6. UPDATE SARAV_PLAYLISTS (Complete Studio Playlists Hub)
# -------------------------------------------------------------
print("Updating sarav_playlists in catalog with complete ecosystem playlists...")

all_studio_playlists = [
    # --- SARAV X AI: 100 DAYS CURRICULUM ---
    {
        "id": "master_umbrella",
        "category": "100_days",
        "cluster_num": 0,
        "cluster_title": "Master Series: Complete 100-Day Curriculum",
        "episodes_range": "Ep 01–100",
        "video_count": "46 Videos",
        "title": "100 Days of Learning AI | Sigma Byte",
        "description": (
            "The complete 100-Day roadmap to mastering Artificial Intelligence from the ground up! 🚀\n\n"
            "Hosted by Enterprise AI Architect Sarav (@iamsaravofficial), this 100-video curriculum demystifies foundational LLM mechanics, advanced prompt engineering, production RAG & vector databases, multi-agent swarms, model fine-tuning, and modern agentic architectures.\n\n"
            "📚 CURRICULUM CLUSTERS:\n"
            "• Cluster 1 (Days 01–10): LLM Fundamentals & Neural Mechanics\n"
            "• Cluster 2 (Days 11–20): Prompt Engineering & Context Windows\n"
            "• Cluster 3 (Days 21–30): Production RAG & Vector Search\n"
            "• Cluster 4 (Days 31–40): Agentic AI & Autonomous Systems\n"
            "• Cluster 5 (Days 41–50): Multimodal AI & Generative Media\n"
            "• Cluster 6 (Days 51–60): AI Safety, Ethics & Alignment\n"
            "• Cluster 7 (Days 61–70): Enterprise AI & Copilots\n"
            "• Cluster 8 (Days 71–80): Model Architectures, Quantization & MoE\n"
            "• Cluster 9 (Days 81–90): AI Trends, Frontier Models & Tokenomics\n"
            "• Cluster 10 (Days 91–100): Practical AI Skills & 10x Workflows\n\n"
            "───────────────\n"
            "🔔 SUBSCRIBE to @iamsaravofficial & bookmark this playlist to never miss a daily byte!\n"
            "🌐 Architecture Blueprints, Code & 1-on-1 Advisory: https://iamsaravofficial.com\n"
            "───────────────\n\n"
            "#shorts #ai #artificialintelligence #learnai #machinelearning #promptengineering #rag #agenticai #sigmabyte #saravxai #100daysofai"
        ),
        "hashtags": "#shorts #ai #artificialintelligence #learnai #machinelearning #promptengineering #rag #agenticai #sigmabyte #saravxai #100daysofai",
        "playlist_url": "https://www.youtube.com/playlist?list=PLet1KBv_sfbY"
    },
    {
        "id": "cluster_01",
        "category": "100_days",
        "cluster_num": 1,
        "cluster_title": "Cluster 1: LLM Fundamentals (Ep 01–10)",
        "episodes_range": "Ep 01–10",
        "video_count": "10 Videos",
        "title": "100 Days of Learning AI 👉 Cluster 1: LLM Fundamentals (Ep 01–10) | Sigma Byte",
        "description": "Master LLM Fundamentals in 10 bite-sized high-IQ episodes! 💡 Stop treating AI like magic. In this 10-part series, Enterprise AI Architect Sarav breaks down tokens, context windows, vector embeddings, transformers, and attention mechanisms.\n\n#shorts #ai #artificialintelligence #learnai #llmfundamentals #sigmabyte #saravxai #100daysofai #techtips",
        "hashtags": "#shorts #ai #artificialintelligence #learnai #llmfundamentals #sigmabyte #saravxai #100daysofai #techtips",
        "playlist_url": "https://www.youtube.com/playlist?list=PLT6PUK5n-H9U"
    },
    {
        "id": "cluster_02",
        "category": "100_days",
        "cluster_num": 2,
        "cluster_title": "Cluster 2: Prompt Engineering Mastery (Ep 11–20)",
        "episodes_range": "Ep 11–20",
        "video_count": "10 Videos",
        "title": "100 Days of Learning AI 👉 Cluster 2: Prompt Engineering Mastery (Ep 11–20) | Sigma Byte",
        "description": "Master Prompt Engineering Mastery in 10 bite-sized high-IQ episodes! 💡 99% of people prompt AI like an intern. Discover system prompts, prompt chaining, negative prompting, JSON structured output, and meta-prompting.\n\n#shorts #ai #artificialintelligence #learnai #promptengineeringmastery #sigmabyte #saravxai #100daysofai #techtips",
        "hashtags": "#shorts #ai #artificialintelligence #learnai #promptengineeringmastery #sigmabyte #saravxai #100daysofai #techtips",
        "playlist_url": "https://www.youtube.com/playlist?list=PLePv_aItYtqo"
    },
    {
        "id": "cluster_03",
        "category": "100_days",
        "cluster_num": 3,
        "cluster_title": "Cluster 3: Production RAG & Vector Search (Ep 21–30)",
        "episodes_range": "Ep 21–30",
        "video_count": "10 Videos",
        "title": "100 Days of Learning AI 👉 Cluster 3: Production RAG & Vector Search (Ep 21–30) | Sigma Byte",
        "description": "Master Production RAG & Vector Search in 10 bite-sized high-IQ episodes! 💡 Feeding whole PDFs to AI is broken. This cluster reveals how vector databases index meaning, how recursive chunking preserves context, and how hybrid search eliminates hallucinations.\n\n#shorts #ai #artificialintelligence #learnai #productionragvectorsearch #sigmabyte #saravxai #100daysofai #techtips",
        "hashtags": "#shorts #ai #artificialintelligence #learnai #productionragvectorsearch #sigmabyte #saravxai #100daysofai #techtips",
        "playlist_url": "https://www.youtube.com/playlist?list=PLBFH1sOvs76o"
    },
    {
        "id": "cluster_04",
        "category": "100_days",
        "cluster_num": 4,
        "cluster_title": "Cluster 4: Agentic AI & Autonomous Systems (Ep 31–40)",
        "episodes_range": "Ep 31–40",
        "video_count": "10 Videos",
        "title": "100 Days of Learning AI 👉 Cluster 4: Agentic AI & Autonomous Systems (Ep 31–40) | Sigma Byte",
        "description": "Master Agentic AI & Autonomous Systems in 10 bite-sized high-IQ episodes! 💡 Chatbots talk. AI Agents execute. Learn function calling, ReAct loops, multi-agent squads, and Anthropic's Model Context Protocol (MCP).\n\n#shorts #ai #artificialintelligence #learnai #agenticaiautonomoussystems #sigmabyte #saravxai #100daysofai #techtips",
        "hashtags": "#shorts #ai #artificialintelligence #learnai #agenticaiautonomoussystems #sigmabyte #saravxai #100daysofai #techtips",
        "playlist_url": "https://www.youtube.com/playlist?list=PLKVhcsbIqnjU"
    },
    {
        "id": "cluster_05",
        "category": "100_days",
        "cluster_num": 5,
        "cluster_title": "Cluster 5: Multimodal & GenAI Creative (Ep 41–50)",
        "episodes_range": "Ep 41–50",
        "video_count": "6 Videos Live",
        "title": "100 Days of Learning AI 👉 Cluster 5: Multimodal & GenAI Creative (Ep 41–50) | Sigma Byte",
        "description": "Master Multimodal AI & Generative Creative Models in 10 bite-sized high-IQ episodes! 💡 Text-to-image synthesis, spatiotemporal video world models, neural vocoders, latent diffusion denoising, and 3D avatar blendshapes.\n\n#shorts #ai #artificialintelligence #learnai #multimodalaudioimage #sigmabyte #saravxai #100daysofai #techtips",
        "hashtags": "#shorts #ai #artificialintelligence #learnai #multimodalaudioimage #sigmabyte #saravxai #100daysofai #techtips",
        "playlist_url": "https://www.youtube.com/playlist?list=PLZJefzvLqrLs"
    },
    {
        "id": "cluster_06",
        "category": "100_days",
        "cluster_num": 6,
        "cluster_title": "Cluster 6: AI Safety, Ethics & Alignment (Ep 51–60)",
        "episodes_range": "Ep 51–60",
        "video_count": "Curriculum Staged",
        "title": "100 Days of Learning AI 👉 Cluster 6: AI Safety, Ethics & Alignment (Ep 51–60) | Sigma Byte",
        "description": "Master AI Safety, Governance & Alignment in 10 bite-sized high-IQ episodes! 💡 Reinforcement Learning from Human Feedback (RLHF), Constitutional AI, guardrails, and adversarial testing.\n\n#shorts #ai #artificialintelligence #learnai #aisafety #sigmabyte #saravxai #100daysofai #techtips",
        "hashtags": "#shorts #ai #artificialintelligence #learnai #aisafety #sigmabyte #saravxai #100daysofai #techtips",
        "playlist_url": ""
    },
    {
        "id": "cluster_07",
        "category": "100_days",
        "cluster_num": 7,
        "cluster_title": "Cluster 7: Enterprise AI & Copilots (Ep 61–70)",
        "episodes_range": "Ep 61–70",
        "video_count": "Curriculum Staged",
        "title": "100 Days of Learning AI 👉 Cluster 7: Enterprise AI & Copilots (Ep 61–70) | Sigma Byte",
        "description": "Master Enterprise AI Implementations & Copilot Architecture in 10 bite-sized episodes! 💡 Role-based access controls, telemetry auditing, cost optimization, and enterprise governance.\n\n#shorts #ai #artificialintelligence #learnai #enterprisegovernance #sigmabyte #saravxai #100daysofai #techtips",
        "hashtags": "#shorts #ai #artificialintelligence #learnai #enterprisegovernance #sigmabyte #saravxai #100daysofai #techtips",
        "playlist_url": ""
    },
    {
        "id": "cluster_08",
        "category": "100_days",
        "cluster_num": 8,
        "cluster_title": "Cluster 8: Model Architectures & Quantization (Ep 71–80)",
        "episodes_range": "Ep 71–80",
        "video_count": "Curriculum Staged",
        "title": "100 Days of Learning AI 👉 Cluster 8: Model Architectures & Quantization (Ep 71–80) | Sigma Byte",
        "description": "Master Model Quantization, Mixture of Experts (MoE) & Edge AI in 10 bite-sized episodes! 💡 GGUF quantization, 4-bit precision, local Ollama NPUs, and hybrid routing.\n\n#shorts #ai #artificialintelligence #learnai #quantization #sigmabyte #saravxai #100daysofai #techtips",
        "hashtags": "#shorts #ai #artificialintelligence #learnai #quantization #sigmabyte #saravxai #100daysofai #techtips",
        "playlist_url": ""
    },
    {
        "id": "cluster_09",
        "category": "100_days",
        "cluster_num": 9,
        "cluster_title": "Cluster 9: AI Economics & Frontier Models (Ep 81–90)",
        "episodes_range": "Ep 81–90",
        "video_count": "Curriculum Staged",
        "title": "100 Days of Learning AI 👉 Cluster 9: AI Economics & Frontier Models (Ep 81–90) | Sigma Byte",
        "description": "Master AI Economics, Tokenomics & Frontier Intelligence in 10 bite-sized episodes! 💡 Inference unit economics, prompt caching discounts, and the road to AGI.\n\n#shorts #ai #artificialintelligence #learnai #tokenomics #sigmabyte #saravxai #100daysofai #techtips",
        "hashtags": "#shorts #ai #artificialintelligence #learnai #tokenomics #sigmabyte #saravxai #100daysofai #techtips",
        "playlist_url": ""
    },
    {
        "id": "cluster_10",
        "category": "100_days",
        "cluster_num": 10,
        "cluster_title": "Cluster 10: Practical AI Skills (Ep 91–100)",
        "episodes_range": "Ep 91–100",
        "video_count": "Curriculum Staged",
        "title": "100 Days of Learning AI 👉 Cluster 10: Practical AI Skills (Ep 91–100) | Sigma Byte",
        "description": "Master Practical 10x AI Workflows in 10 bite-sized high-IQ episodes! 💡 High-velocity research, automated coding, dynamic spreadsheet analysis, automated email triage, and accelerated self-learning.\n\n#shorts #ai #artificialintelligence #learnai #aiproductivity #aicoding #10xengineer #sigmabyte #saravxai #100daysofai #techtips",
        "hashtags": "#shorts #ai #artificialintelligence #learnai #aiproductivity #aicoding #10xengineer #sigmabyte #saravxai #100daysofai #techtips",
        "playlist_url": ""
    },

    # --- SARAV X AI: TECH RADAR ---
    {
        "id": "tech_radar",
        "category": "tech_radar",
        "cluster_num": 99,
        "cluster_title": "Sarav × AI Tech Radar (Daily AI Trends)",
        "episodes_range": "Trends 01–06+",
        "video_count": "3 Videos Live",
        "title": "Tech Radar | AI Tools, Coding Agents & Enterprise Workflows",
        "description": "Daily breaking AI tools, open-source utilities, developer setups, and architecture blueprints by Enterprise AI Architect Sarav (@iamsaravofficial). Covering Claude Code, Google Antigravity, 9Router rate-limit failovers, Gemini 4 Carbon + Hydrogen, and zero-cost AI stacks.\n\n#shorts #ai #coding #developer #techradar #saravxai #claudecode #antigravity",
        "hashtags": "#shorts #ai #coding #developer #techradar #saravxai #claudecode #antigravity",
        "playlist_url": "https://www.youtube.com/playlist?list=PLHN3aMEl-g28"
    },

    # --- THE LOOP: KARMA COURT (COMIC TALES) ---
    {
        "id": "karma_court",
        "category": "karma_court",
        "cluster_num": 101,
        "cluster_title": "Karma Court / Comic Tales (Series 02)",
        "episodes_range": "Cases 01–50",
        "video_count": "4 Videos Live",
        "title": "Karma Court ⚖️😂 | கர்மா கோர்ட் (Comic Tales)",
        "description": "Poetic Divine Justice in Melogam (மேலோகம்)! Hilarious & satirical micro-shorts exploring modern human social pet-peeves and everyday hypocrisies — traffic blunders, high-beams, horn blasters, office politics, and social media addictions.\n\n#shorts #TheLoop #KarmaCourt #TamilComedy #SatiricalShorts",
        "hashtags": "#shorts #TheLoop #KarmaCourt #TamilComedy #SatiricalShorts",
        "playlist_url": "https://www.youtube.com/playlist?list=PLHuZo_k1eGx4"
    },

    # --- THE LOOP: INKLING TALES COMPLETE & MOOD PLAYLISTS ---
    {
        "id": "inkling_complete",
        "category": "inkling_tales",
        "cluster_num": 200,
        "cluster_title": "Inkling Tales: Master Series",
        "episodes_range": "Ep 001–300",
        "video_count": "45 Videos Live",
        "title": "Inkling Tales: 8-Word Stories | Complete Series",
        "description": "300 complete micro-stories told in exactly 8 words with seamless 6.00s loops on @theloopvid. A masterclass in high-retention micro-fiction, unexpected twists, and unforgettable emotion.\n\n#shorts #TheLoop #InklingTales #8WordStory #MicroFiction",
        "hashtags": "#shorts #TheLoop #InklingTales #8WordStory #MicroFiction",
        "playlist_url": "https://www.youtube.com/playlist?list=PLcHWWWwKKWjY"
    },
    {
        "id": "inkling_dark_twists",
        "category": "inkling_tales",
        "cluster_num": 201,
        "cluster_title": "Inkling Mood: Dark Twists & Mysteries",
        "episodes_range": "Curated Tales",
        "video_count": "15 Videos",
        "title": "Dark Twists & Mysteries | 8-Word Stories",
        "description": "Chilling psychological twists, unexpected endings, and mysterious turns that demand a re-watch.\n\n#shorts #TheLoop #DarkTwist #Mystery #8WordStory",
        "hashtags": "#shorts #TheLoop #DarkTwist #Mystery #8WordStory",
        "playlist_url": "https://www.youtube.com/playlist?list=PLU4K-iVBBNoQ"
    },
    {
        "id": "inkling_hope_courage",
        "category": "inkling_tales",
        "cluster_num": 202,
        "cluster_title": "Inkling Mood: Hope, Courage & Rebirth",
        "episodes_range": "Curated Tales",
        "video_count": "10 Videos",
        "title": "Hope, Courage & Rebirth | 8-Word Stories",
        "description": "Uplifting 8-word stories of resilience, triumph, quiet bravery, and second chances.\n\n#shorts #TheLoop #Hope #Courage #8WordStory",
        "hashtags": "#shorts #TheLoop #Hope #Courage #8WordStory",
        "playlist_url": "https://www.youtube.com/playlist?list=PLFHCY47lRvH4"
    },
    {
        "id": "inkling_heartbreak",
        "category": "inkling_tales",
        "cluster_num": 203,
        "cluster_title": "Inkling Mood: Heartbreaking Loss & Nostalgia",
        "episodes_range": "Curated Tales",
        "video_count": "8 Videos",
        "title": "Heartbreaking 8-Word Stories | Loss & Nostalgia",
        "description": "Poignant, tender micro-fictions exploring grief, memories of yesterday, and the beauty of what once was.\n\n#shorts #TheLoop #Nostalgia #Heartbreak #8WordStory",
        "hashtags": "#shorts #TheLoop #Nostalgia #Heartbreak #8WordStory",
        "playlist_url": "https://www.youtube.com/playlist?list=PLGod06q62ML0"
    },
    {
        "id": "inkling_scifi",
        "category": "inkling_tales",
        "cluster_num": 204,
        "cluster_title": "Inkling Mood: Mind-Bending Sci-Fi & Paradoxes",
        "episodes_range": "Curated Tales",
        "video_count": "6 Videos",
        "title": "Mind-Bending Sci-Fi & Paradoxes | 8-Word Stories",
        "description": "Time travel loops, alternate dimensions, AI consciousness, and cosmic paradoxes condensed into 8 words.\n\n#shorts #TheLoop #SciFi #Paradox #8WordStory",
        "hashtags": "#shorts #TheLoop #SciFi #Paradox #8WordStory",
        "playlist_url": "https://www.youtube.com/playlist?list=PLWoVZdxSkuGw"
    },
    {
        "id": "inkling_love",
        "category": "inkling_tales",
        "cluster_num": 205,
        "cluster_title": "Inkling Mood: Love & Silent Goodbyes",
        "episodes_range": "Curated Tales",
        "video_count": "4 Videos",
        "title": "Love & Silent Goodbyes | 8-Word Stories",
        "description": "Whispered romances, unspoken feelings across crowded rooms, and enduring bonds that transcend time.\n\n#shorts #TheLoop #Romance #LoveStory #8WordStory",
        "hashtags": "#shorts #TheLoop #Romance #LoveStory #8WordStory",
        "playlist_url": "https://www.youtube.com/playlist?list=PLR9g7dI8ZMx0"
    }
]

catalog["sarav_playlists"] = all_studio_playlists

# -------------------------------------------------------------
# SAVE CATALOG.JS
# -------------------------------------------------------------
print("Saving updated catalog.js...")
with open(CATALOG_PATH, "w", encoding="utf-8") as f:
    f.write("window.PUBLISHING_CATALOG = ")
    json.dump(catalog, f, indent=2, ensure_ascii=False)
    f.write(";\n")

print("catalog.js successfully updated!")

# -------------------------------------------------------------
# 7. UPDATE INDEX.HTML (UI & Controls)
# -------------------------------------------------------------
print("Updating index.html with new controls, counts, and playlist display...")

with open(INDEX_PATH, "r", encoding="utf-8") as f:
    html = f.read()

# Update Header Tab Counts
html = re.sub(r'<span class="tab-count" id="count-playlists">\d+</span>', f'<span class="tab-count" id="count-playlists">{len(all_studio_playlists)}</span>', html)

# Update Filter Chips for sarav_playlists in index.html
old_chips_block = r"""      } else if (currentSuite === 'sarav_playlists') {
        chips.push(
          { id: 'clusters', label: 'All 10 Clusters' },
          { id: 'c5to10', label: 'Clusters 5–10 (New)' },
          { id: 'master', label: 'Master Umbrella' }
        );"""

new_chips_block = r"""      } else if (currentSuite === 'sarav_playlists') {
        chips.push(
          { id: '100days', label: '⚡ 100 Days Clusters (11)' },
          { id: 'techradar', label: '📡 Tech Radar (1)' },
          { id: 'karma', label: '⚖️ Karma Court (1)' },
          { id: 'inkling', label: '🔁 Inkling Tales (6)' }
        );"""

if old_chips_block in html:
    html = html.replace(old_chips_block, new_chips_block)
else:
    # Regex fallback replacement
    html = re.sub(
        r"\}\s*else\s*if\s*\(currentSuite\s*===\s*'sarav_playlists'\)\s*\{[\s\S]*?chips\.push\([\s\S]*?\);\s*\}",
        new_chips_block + "\n      }",
        html
    )

# Update Filter matching logic in index.html for sarav_playlists
old_filter_logic = r"""        } else if (currentSuite === 'sarav_playlists') {
          if (currentFilter === 'c5to10' && (item.cluster_num < 5 || item.cluster_num > 10)) return false;
          if (currentFilter === 'clusters' && item.cluster_num === 0) return false;
          if (currentFilter === 'master' && item.cluster_num !== 0) return false;"""

new_filter_logic = r"""        } else if (currentSuite === 'sarav_playlists') {
          if (currentFilter === '100days' && item.category !== '100_days') return false;
          if (currentFilter === 'techradar' && item.category !== 'tech_radar') return false;
          if (currentFilter === 'karma' && item.category !== 'karma_court') return false;
          if (currentFilter === 'inkling' && item.category !== 'inkling_tales') return false;"""

if old_filter_logic in html:
    html = html.replace(old_filter_logic, new_filter_logic)
else:
    html = re.sub(
        r"\}\s*else\s*if\s*\(currentSuite\s*===\s*'sarav_playlists'\)\s*\{[\s\S]*?if\s*\(currentFilter\s*===\s*'master'[\s\S]*?return\s*false;",
        new_filter_logic,
        html
    )

# Update buildTheLoopCard to display Playlists to Add
old_theloop_card_end = r"""              <div class="actions-grid">
                <button class="btn-copy gold" onclick="copyCardField('the_loop', ${ep}, 'title', this)">📋 Copy Title</button>"""

new_theloop_card_end = r"""              <div style="background: rgba(14, 28, 48, 0.7); border: 1px solid rgba(0, 240, 255, 0.2); border-radius: 8px; padding: 8px 12px; margin-bottom: 8px; font-size: 11.5px;">
                <div style="color: var(--gold-bright); font-weight: 700; margin-bottom: 4px;">📂 Add To Playlists:</div>
                <div style="color: #E2E8F0; margin-bottom: 2px;">• <a href="${item.master_playlist_url}" target="_blank" rel="noopener" style="color: #38BDF8; text-decoration: none;">${escapeHtml(item.master_playlist || 'Inkling Tales Complete')}</a></div>
                <div style="color: #E2E8F0;">• <a href="${item.mood_playlist_url}" target="_blank" rel="noopener" style="color: #F43F5E; text-decoration: none;">${escapeHtml(item.mood_playlist || 'Mood Playlist')}</a></div>
              </div>

              <div class="actions-grid">
                <button class="btn-copy gold" onclick="copyCardField('the_loop', ${ep}, 'title', this)">📋 Copy Title</button>"""

if old_theloop_card_end in html and "📂 Add To Playlists:" not in html:
    html = html.replace(old_theloop_card_end, new_theloop_card_end)

# Update buildPlaylistsCard to support Category Badges and Video Counts
old_playlist_card = r"""    function buildPlaylistsCard(item) {
      const isMaster = item.cluster_num === 0;
      return `
        <article class="pub-card" id="card-playlist-${item.id}">
          <div class="card-top">
            <div class="card-meta-left">
              <span class="ep-badge ${isMaster ? 'magenta' : 'gold'}">${isMaster ? 'MASTER SERIES' : 'CLUSTER ' + item.cluster_num}</span>
              <span class="cat-badge">${escapeHtml(item.episodes_range)}</span>
              <span class="cat-badge">${escapeHtml(item.cluster_title)}</span>
              ${item.playlist_url ? `<a href="${item.playlist_url}" target="_blank" rel="noopener" class="cat-badge" style="background: rgba(239, 68, 68, 0.2); color: #EF4444; border: 1px solid rgba(239, 68, 68, 0.4); text-decoration: none;">▶️ Open on YouTube</a>` : ''}
            </div>
          </div>"""

new_playlist_card = r"""    function buildPlaylistsCard(item) {
      const isMaster = item.cluster_num === 0;
      let badgeTheme = 'gold';
      let catTag = '100 DAYS';
      if (item.category === 'tech_radar') { badgeTheme = 'cyan'; catTag = 'TECH RADAR'; }
      else if (item.category === 'karma_court') { badgeTheme = 'magenta'; catTag = 'KARMA COURT'; }
      else if (item.category === 'inkling_tales') { badgeTheme = 'cyan'; catTag = 'INKLING TALES'; }
      else if (isMaster) { badgeTheme = 'magenta'; catTag = 'MASTER SERIES'; }

      return `
        <article class="pub-card" id="card-playlist-${item.id}">
          <div class="card-top">
            <div class="card-meta-left">
              <span class="ep-badge ${badgeTheme}">${catTag}</span>
              <span class="cat-badge" style="color: var(--gold-bright);">${escapeHtml(item.video_count || '')}</span>
              <span class="cat-badge">${escapeHtml(item.cluster_title)}</span>
              ${item.playlist_url ? `<a href="${item.playlist_url}" target="_blank" rel="noopener" class="cat-badge" style="background: rgba(239, 68, 68, 0.2); color: #EF4444; border: 1px solid rgba(239, 68, 68, 0.4); text-decoration: none; font-weight: bold;">▶️ Open on YouTube</a>` : '<span class="cat-badge" style="color: #94A3B8;">Staged in Studio</span>'}
            </div>
          </div>"""

if old_playlist_card in html:
    html = html.replace(old_playlist_card, new_playlist_card)

with open(INDEX_PATH, "w", encoding="utf-8") as f:
    f.write(html)

print("index.html successfully updated!")

# -------------------------------------------------------------
# 8. UPDATE CAPTION DECK FOR SID & ISHA (instagram_captions_30days.md)
# -------------------------------------------------------------
print("Updating instagram_captions_30days.md with new Alt Texts...")
with open(CAPTION_DECK_PATH, "r", encoding="utf-8") as f:
    deck_text = f.read()

# Replace Alt Texts for each day in markdown deck
updated_deck_text = deck_text
for d_num in range(1, 31):
    d_str = str(d_num)
    if d_str in alt_texts:
        s1_alt = alt_texts[d_str]["slide1"]
        s2_alt = alt_texts[d_str]["slide2"]
        
        # Regex replacement for Day block
        pattern = rf"(## Day {d_num:02d} \(.*?\) — .*?### ♿ Accessibility & SEO Alt Text\n)\* \*\*Slide 1 Alt Text:\*\* [^\n\r]+\n\* \*\*Slide 2 Alt Text:\*\* [^\n\r]+"
        replacement = rf"\g<1>* **Slide 1 Alt Text:** {s1_alt}\n* **Slide 2 Alt Text:** {s2_alt}"
        
        updated_deck_text = re.sub(pattern, replacement, updated_deck_text)

with open(CAPTION_DECK_PATH, "w", encoding="utf-8") as f:
    f.write(updated_deck_text)

print("instagram_captions_30days.md successfully updated!")
print("ALL TASKS COMPLETED!")
