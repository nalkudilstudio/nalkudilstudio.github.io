"""
Generates Comic Tales metadata catalog and injects it into catalog.js for Nalkudil Social Studio.
"""
import os
import json
import re

CATALOG_JS_PATH = r"D:\Websites\nalkudilstudio.github.io\nalkudil-social-studio\catalog.js"
SCENARIOS_JSON_PATH = r"D:\sdrv\inklingtales\comictales\satirical_divine_justice_50_comical_dialogues.json"

titles_tamil_short = {
    1: 'ஹை-பீம் போட்டு கண்ணை குருடாக்குற கும்பல்! 😂',
    2: 'கழுத்தை சாச்சு வண்டில போன் பேசுறது! 😂',
    3: 'சிக்னல் விழும் முன்னாடியே அலறுற ஹார்ன்! 😂',
    4: 'டிராபிக் சிக்னல்ல ரீல்ஸ் ஸ்க்ரோல் பண்றது! 😂',
    5: 'ஒன்-வே பாலத்துல ராங் ரூட்ல வர்றது! 😂',
    6: 'ஃப்ரீ லெஃப்ட் வழியில காரை குறுக்க நிறுத்துறது! 😂',
    7: 'சந்து பொந்துல ட்ரிபிள்ஸ் பறக்குறது! 😂',
    8: 'இன்டிகேட்டர் ஒன்னு... திரும்புறது இன்னொன்னு! 😂',
    9: 'ரோட்டோட நடுவுலயே வண்டிய நிறுத்தி அரட்டை! 😂',
    10: 'சைலன்சரை கழட்டிட்டு ஊரையே அலற விடுறது! 😂',
    11: 'மொபைல் போன்ல 5 நிமிஷத்துக்கு ஒருமுறை ஸ்க்ரோல்! 😂',
    12: 'வாட்ஸ்அப்ல விடியற்காலை பார்வர்டு மெசேஜ் தொல்லை! 😂',
    13: 'பப்ளிக்ல ஸ்பீக்கர் போட்டு ரீல்ஸ் பாக்குறது! 😂',
    14: 'சாப்பாடு வந்ததும் சாப்பிடாம போட்டோ எடுக்குறது! 😂',
    15: 'மெசேஜை பாத்துட்டு ரிப்ளை பண்ணாம சீன் போடுறது! 😂',
    16: 'மொபைல் சார்ஜரை எடுத்துட்டு தராம எஸ்கேப்! 😂',
    17: 'தியேட்டர்ல படம் பார்க்கும்போது போன் டார்ச்சர்! 😂',
    18: 'குரூப்ல தேவையில்லாம ஆட்களை ஆட் பண்றது! 😂',
    19: 'வீடியோ கால்ல மூஞ்சிய காட்டாம சீன்! 😂',
    20: 'போன் பேட்டரி 2% வச்சிட்டு ஊரெல்லாம் சுத்துறது! 😂',
    21: 'மீட்டிங்ல மைக் ஆன் பண்ணிட்டு குறட்டை விடுறது! 😂',
    22: 'ஈமெயிலுக்கு ரிப்ளை பண்ணாம ஓபி அடிக்கிறது! 😂',
    23: 'டெட்லைன் அன்னைக்கு லீவு போடுற புண்ணியவான்! 😂',
    24: 'வேலை பாக்காம மேனேஜர் கிட்ட ஐஸ் வைக்கிறது! 😂',
    25: 'ஃப்ரிட்ஜ்ல வச்ச மத்தவங்க சாப்பாட்டை திருடுறது! 😂',
    26: 'லஞ்ச் முடிஞ்சு 2 மணி நேரம் அரட்டை அடிக்கிறது! 😂',
    27: 'பிரசன்டேஷன் அன்னைக்கு நெட்வொர்க் பிரச்சனை டிராமா! 😂',
    28: 'வேலை செய்யாம கிரெடிட் மட்டும் அபேஸ் பண்றது! 😂',
    29: 'ஆபீஸ் பிரின்டர்ல பர்சனல் புக் பிரிண்ட் எடுக்குறது! 😂',
    30: 'திங்கள் கிழமை காலையில மீட்டிங் போடுற கொடுமை! 😂',
    31: 'ரோட்டுல சும்மா எச்சில் துப்பிட்டு போறது! 😂',
    32: 'குப்பையை கொண்டு வந்து அண்டை வீட்டு வாசல்ல போடுறது! 😂',
    33: 'பொது சுவத்துல போஸ்டர் ஒட்டி நாசம் பண்றது! 😂',
    34: 'பஸ் ஸ்டாப்ல வரிசையில நிக்காம முட்டி மோதுறது! 😂',
    35: 'லிஃப்ட்ல உள்ள இருக்கவங்க இறங்கும் முன்னாடியே முட்டுறது! 😂',
    36: 'மழை தண்ணி போகாம கால்வாயில பிளாஸ்டிக் போடுறது! 😂',
    37: 'பப்ளிக் பார்க்ல பூக்களை பறிச்சு நாசம் பண்றது! 😂',
    38: 'தண்ணி குழாயை திறந்து வச்சிட்டு போறது! 😂',
    39: 'நடபாதை முழுக்க கடையை விரிச்சு ஆக்கிரமிக்கிறது! 😂',
    40: 'பொது இடத்துல புகையை ஊதி தள்ளுறது! 😂',
    41: 'ராத்திரி 12 மணிக்கு பாட்டு போட்டு அலற விடுறது! 😂',
    42: 'மத்தவங்க வீட்டு முன்னாடி வண்டிய பார்க் பண்றது! 😂',
    43: 'வாங்குன கடனை திருப்பி தராம எஸ்கேப் ஆகுறது! 😂',
    44: 'அடுத்தவங்க வீட்டு விஷயத்துல மூக்கை நுழைக்கிறது! 😂',
    45: 'விருந்தாளி வந்து 10 நாளா கிளம்பாம இருக்கிறது! 😂',
    46: 'டிவி சத்தத்தை ஊரே கேக்குற அளவுக்கு வைக்கிறது! 😂',
    47: 'மத்தவங்க துவைச்சு போட்ட துணியில அழுக்கு தண்ணி ஊத்துறது! 😂',
    48: 'பக்கத்து வீட்டு வைஃபையை திருடி படம் பாக்குறது! 😂',
    49: 'கேட்காமலே இலவச அட்வைஸ் அள்ளி கொடுக்குறது! 😂',
    50: 'விசேஷத்துல மொய் வைக்காம ஃபுல் கட்டு கட்டுறது! 😂'
}

pinned_comments = {
    1: "உங்க ஏரியாவுலயும் இப்படி ஹை-பீம் போட்டு கண்ணை குருடாக்குற ஆட்கள் இருக்காங்களா? 😂👇 கமெண்ட்ல சொல்லுங்க!\n\n🔔 Subscribe to @theloopvid for daily Karma Strikes at 1:30 PM IST! 🚀",
    2: "நீங்களும் வண்டில போகும்போது இப்படி ஒரு பக்கமா சாஞ்சு போன் பேசுறவங்கள பாத்திருக்கீங்களா? 😂👇 கமெண்ட் பண்ணுங்க!\n\n🔔 Subscribe to @theloopvid for daily Karma Strikes at 1:30 PM IST! 🚀",
    3: "சிக்னல் விழும் முன்னாடியே காது கிழிய ஹார்ன் அடிக்கிறவங்களுக்கு உங்க ரியாக்ஷன் என்ன? 😂👇 சொல்லுங்க!\n\n🔔 Subscribe to @theloopvid for daily Karma Strikes at 1:30 PM IST! 🚀",
    4: "டிராபிக் சிக்னல்ல நின்னுகிட்டு ரீல்ஸ் பாக்குற ஆட்களை நீங்க பாத்திருக்கீங்களா? 😂👇 Tag that friend!\n\n🔔 Subscribe to @theloopvid for daily Karma Strikes at 1:30 PM IST! 🚀",
    5: "ஒன்-வே பாலத்துல எதிர் திசையில புகுந்து வர்றவங்களுக்கு மேலோக தண்டனை கரெக்டா? 😂👇 கமெண்ட்ல சொல்லுங்க!\n\n🔔 Subscribe to @theloopvid for daily Karma Strikes at 1:30 PM IST! 🚀"
}

def generate_comic_catalog():
    with open(SCENARIOS_JSON_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    scenarios = data["scenarios"]
    items = []
    
    for s in scenarios:
        ep_id = s["id"]
        title_en = s["title_en"]
        cat = s["category"]
        human_q = s["dialogue_tamil"]["part_1_human"]
        divine_v = s["dialogue_tamil"]["part_2_divine"]
        
        slug = re.sub(r'[^a-zA-Z0-9]+', '_', title_en.lower()).strip('_')
        video_filename = f"comic_tale_{ep_id:03d}_{slug}.mp4"
        
        short_title_head = titles_tamil_short.get(ep_id, f"{title_en} 😂")
        title = f"{short_title_head} | Karma Strikes: Ep. {ep_id} #Shorts #TheLoop"
        
        desc = (
            f"\"{human_q}\"\n\n"
            f"⚡ மேலோகத் தீர்ப்பு:\n"
            f"\"{divine_v}\"\n\n"
            f"───────────────\n"
            f"⚖️ SERIES: Karma Strikes (Poetic Divine Justice in Melogam)\n"
            f"🏛️ SETTING: Melogam (மேலோகம் — Celestial Cosmic Courtroom)\n"
            f"🔁 CHANNEL: The Loop Vid (@theloopvid)\n"
            f"🕒 DAILY DROP: 1:30 PM IST (Lunchtime Comedy)\n"
            f"───────────────\n\n"
            f"Relatable everyday civic habits and modern frustrations meet witty, poetic divine justice in Melogam!\n\n"
            f"🔔 SUBSCRIBE to @theloopvid for daily micro-shorts & cosmic justice!\n"
            f"📌 Share this with that one friend who does this! 😂\n\n"
            f"#KarmaStrikes #ComicTales #TheLoop #TamilComedy #Shorts #TamilShorts #DivineJustice #Melogam #RelatableComedy"
        )
        
        tags = "karma strikes, comic tales, the loop, the loop vid, tamil shorts, tamil comedy, relatable comedy, divine justice, melogam, poetic justice, everyday frustrations, funny tamil shorts, shorts, viral shorts, trending shorts"
        
        pinned = pinned_comments.get(
            ep_id,
            f"உங்க வாழ்க்கையிலும் இப்படி பண்ற ஆட்களை பாத்திருக்கீங்களா? 😂👇 Drop your thoughts in the comments!\n\n🔔 Subscribe to @theloopvid for daily Karma Strikes at 1:30 PM IST! 🚀"
        )
        
        is_ready = (ep_id <= 5)
        cover_url = f"assets/comic_tales/cover_comic_{ep_id:03d}.jpg" if is_ready else "assets/comic_tales/cover_comic_001.jpg"
        cover_filename = f"cover_comic_{ep_id:03d}.jpg"
        
        item = {
            "episode": ep_id,
            "day": f"Episode {ep_id}",
            "slot": "13:30 IST (Lunchtime Comedy)",
            "title_en": title_en,
            "category": cat,
            "situation": s["situation_description"],
            "human_complaint": human_q,
            "divine_verdict": divine_v,
            "video_filename": video_filename,
            "title": title,
            "description": desc,
            "tags": tags,
            "pinned_comment": pinned,
            "cover_url": cover_url,
            "cover_filename": cover_filename,
            "status": "READY 🚀" if is_ready else "QUEUED ⏳"
        }
        items.append(item)
        
    return items

def update_catalog():
    with open(CATALOG_JS_PATH, "r", encoding="utf-8") as f:
        content = f.read()
        
    prefix = "window.PUBLISHING_CATALOG = "
    if not content.startswith(prefix):
        raise ValueError("Unexpected prefix in catalog.js")
        
    raw_json = content[len(prefix):].rstrip(";\n ")
    catalog_data = json.loads(raw_json)
    
    comic_items = generate_comic_catalog()
    catalog_data["comic_tales"] = comic_items
    print(f"Added 'comic_tales' with {len(comic_items)} items!")
    
    # Save back
    new_content = prefix + json.dumps(catalog_data, ensure_ascii=False, indent=2) + ";\n"
    with open(CATALOG_JS_PATH, "w", encoding="utf-8") as f:
        f.write(new_content)
        
    print(f"Successfully updated {CATALOG_JS_PATH} ({len(new_content)} characters)!")

if __name__ == "__main__":
    update_catalog()
