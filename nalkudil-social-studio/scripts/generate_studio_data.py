import os
import sys
import json
import shutil
import re
import urllib.request
import openpyxl
from bs4 import BeautifulSoup

# Ensure utf-8 output
sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = r"D:\Websites\nalkudilstudio.github.io\nalkudil-social-studio"
ASSETS_DIR = os.path.join(BASE_DIR, "assets")

SARAV_XLSX = r"D:\YouTube\Sarav AI\YouTube_Shorts_Schedule_Ep01_to_100_Copy.xlsx"
SARAV_COVERS_DIR = r"D:\YouTube\Sarav AI\saravxai6-100\covers"
SARAV_SHORTS_JSON = r"D:\Websites\SaravsWorld\public\ai\shorts_data.json"

LOOP_XLSX = r"D:\sdrv\inklingtales\TheLoop_Shorts_Schedule_Ep01_to_300.xlsx"
LOOP_COVERS_DIR = r"D:\sdrv\inklingtales\covers"

SIDISHA_HTML = r"D:\StorytellingArt\SidIsha-HomeWasYou\SidIsha_Instagram_Days_01_to_30.html"
SIDISHA_SLIDE1_DIR = r"D:\StorytellingArt\SidIsha-HomeWasYou\images\stamped"
SIDISHA_SLIDE2_DIR = r"D:\StorytellingArt\SidIsha-HomeWasYou\images\carousel_slide2"

INKLING_IG_HTML = r"D:\sdrv\inklingtales\InklingTales_Instagram_Ep51_to_100.html"

# Destination dirs
SARAV_DEST = os.path.join(ASSETS_DIR, "sarav_ai")
LOOP_DEST = os.path.join(ASSETS_DIR, "the_loop")
SIDISHA_S1_DEST = os.path.join(ASSETS_DIR, "sid_isha", "slide1")
SIDISHA_S2_DEST = os.path.join(ASSETS_DIR, "sid_isha", "slide2")

os.makedirs(SARAV_DEST, exist_ok=True)
os.makedirs(LOOP_DEST, exist_ok=True)
os.makedirs(SIDISHA_S1_DEST, exist_ok=True)
os.makedirs(SIDISHA_S2_DEST, exist_ok=True)

print("--- STEP 1: PARSING SARAV X AI SHORTS & GENERATING POLLS ---")

# Load existing shorts_data.json for youtube video ids & thumbs
shorts_meta = {}
if os.path.exists(SARAV_SHORTS_JSON):
    with open(SARAV_SHORTS_JSON, encoding='utf-8') as f:
        for item in json.load(f):
            shorts_meta[item['episode']] = item

# Pre-index sarav covers
sarav_cover_files = os.listdir(SARAV_COVERS_DIR) if os.path.exists(SARAV_COVERS_DIR) else []

# Load Excel
wb_sarav = openpyxl.load_workbook(SARAV_XLSX, read_only=True)
ws_sarav = wb_sarav.active

sarav_episodes = []
header_row = [cell for cell in next(ws_sarav.iter_rows(min_row=1, max_row=1, values_only=True))]
h_map = {name: i for i, name in enumerate(header_row) if name}

# Custom tailored poll database for 100 episodes
POLL_PATTERNS = {
    1: ("How does an LLM like ChatGPT actually read your prompt?", ["As letters & words like a human", "Through raw audio signals", "As numerical tokens (chunks of text)", "It reads the entire sentence as one pixel"], 2),
    2: ("Why does an AI begin forgetting things in a long conversation?", ["The server battery gets low", "It exceeded its token context window limit", "The model gets bored of the topic", "Internet latency caused packet loss"], 1),
    3: ("How does AI understand that 'Doctor' and 'Hospital' are related?", ["Manual human dictionary tags", "Vector embeddings plot them near each other in geometric space", "Alphabetical indexing", "Simple keyword exact matching"], 1),
    4: ("What foundational 2017 architecture powers almost all modern LLMs?", ["Convolutional Neural Networks (CNN)", "The Transformer (Self-Attention mechanism)", "Recurrent Neural Networks (RNN)", "Linear Regression Arrays"], 1),
    5: ("What actually happens when you ask AI to generate an answer?", ["It searches Google and copies a blog post", "It looks up a pre-written database of human answers", "It predicts the most probable next token sequentially", "It stores your chat in a permanent hard drive first"], 2),
    6: ("What does the 'Temperature' parameter (0.0 to 1.0) control in an LLM?", ["The speed of the model's server fan", "Creativity / Randomness vs Deterministic accuracy", "The maximum number of words it can output", "The language translation sensitivity"], 1),
    7: ("What is the primary cause of AI 'Hallucinations'?", ["The AI has gained self-awareness and is lying", "The model predicts statistically plausible tokens without factual grounding", "A hardware glitch in the GPU", "The user's Wi-Fi dropped mid-generation"], 1),
    8: ("Which prompt strategy gives AI the fastest understanding of your desired format?", ["Writing 5 paragraphs explaining the rules", "Few-Shot Prompting (giving 2–3 clear input/output examples)", "Typing in ALL CAPS", "Asking the AI to 'please try your absolute best'"], 1),
    9: ("Why does adding 'Think step-by-step' dramatically improve AI math & logic?", ["It unlocks hidden supercomputer cores", "It forces Chain-of-Thought reasoning across intermediate tokens", "It bypasses OpenAI safety filters", "It forces the AI to check Wikipedia first"], 1),
    10: ("What does 'System Prompt' mean in LLM architecture?", ["The operating system version (Windows/Linux)", "The hidden root instruction that defines the AI's persona & strict behavioral boundaries", "The computer processor clock speed", "The prompt entered by end users in chat"], 1),
    11: ("Why should you structure complex AI outputs as JSON schemas?", ["It looks cooler in presentation slides", "It guarantees machine-parsable, deterministic data for software APIs", "It cuts the cost of ChatGPT Plus in half", "It prevents the AI from using English"], 1),
    12: ("What is 'Prompt Chaining'?", ["Sending 50 questions in one huge prompt", "Breaking a complex workflow into sequential prompts where Output A feeds Prompt B", "Linking multiple ChatGPT accounts together", "Repeating the same prompt 10 times until it works"], 1),
    13: ("What is the RCTF prompt formula developed for production engineering?", ["Read, Calculate, Test, Finalize", "Role, Context, Task, Format", "Run, Cache, Trace, Flush", "Retrieve, Chunk, Transform, Filter"], 1),
    14: ("What is 'Meta-Prompting'?", ["Asking Mark Zuckerberg for permission", "Using an advanced LLM to write, refine, and optimize your prompts for you", "Writing prompts only inside Facebook Messenger", "Prompting AI using raw binary code"], 1),
    15: ("What is the most effective way to eliminate generic corporate fluff in AI drafts?", ["Invert the instruction: explicitly forbid clichés and specify what NOT to say", "Add more exclamation marks", "Tell the AI you will tip it $200", "Use older AI models like GPT-2"], 0),
    16: ("What is 'Prompt Injection' in AI security?", ["Injecting Python code into the computer BIOS", "An adversary tricking the LLM into ignoring its system prompt via malicious user input", "Adding too many tokens into a prompt", "Upgrading the model via a software patch"], 1),
    17: ("What is the main advantage of Markdown formatting in prompt design?", ["It allows bold text in terminal outputs", "Clear visual delimitation (`###`, `---`, `\`\`\``) helps attention heads isolate sections", "It reduces network bandwidth by 80%", "It prevents copyright infringement"], 1),
    18: ("What is 'Directional Stimulus Prompting'?", ["Pointing your antenna toward the cloud server", "Providing small hint tokens or keywords that steer the LLM toward key concepts", "Prompting only in directional arrows", "Asking AI to navigate GPS maps"], 1),
    19: ("What should you always do before accepting an AI's first draft?", ["Copy-paste it directly to production", "Run a Self-Refinement / Critique pass ('Review your answer for flaws and fix them')", "Turn off your computer", "Re-read it 10 times in silence"], 1),
    20: ("Why do LLMs struggle with counting letters (e.g. 'how many r's in strawberry')?", ["They are terrible at basic math", "They process text as multi-letter tokens, not individual character arrays", "They don't know what strawberries are", "Their training data excluded fruits"], 1),
    21: ("What is RAG (Retrieval-Augmented Generation)?", ["A new video game rendering engine", "Injecting external private documents into the prompt at runtime so AI answers factually", "A method to delete old chat histories", "Training a brand new foundation model from scratch"], 1),
    22: ("Why are Vector Databases better than SQL for semantic search?", ["They store numbers faster than words", "They find meaning and semantic similarity, not just exact keyword matches", "They are 100% free forever", "They replace the need for an operating system"], 1),
    23: ("What is 'Chunking' in a RAG pipeline?", ["Deleting duplicate files from the hard drive", "Splitting large documents into smaller, semantically coherent passages for embedding", "Compressing images to 8-bit color", "Combining 10 PDFs into one giant zip file"], 1),
    24: ("What happens if you dump a 500-page PDF directly into a 1M context window?", ["The AI answers with 100% accuracy instantly", "'Lost in the Middle' phenomenon: precision drops and latency/cost skyrocket", "The AI server permanently crashes", "The PDF gets automatically deleted"], 1),
    25: ("What metric is commonly used to measure distance between two vector embeddings?", ["Miles / Kilometers", "Cosine Similarity / Dot Product", "Decibels (dB)", "Pixels per inch (PPI)"], 1),
    26: ("What is the role of a 'Reranker' in enterprise search?", ["To rank employees by performance", "A cross-encoder that re-scores top vector candidates for true semantic relevance", "To sort database files alphabetically", "To filter out spam emails"], 1),
    27: ("How does Knowledge Grounding eliminate hallucinations?", ["By threatening to cancel the AI subscription", "By constraining the LLM to answer ONLY from retrieved context citations", "By setting temperature to 2.0", "By using edge-tts voices"], 1),
    28: ("What is 'Hybrid Search' in modern enterprise retrieval?", ["Searching on both Google and Bing simultaneously", "Combining dense semantic vector search with sparse keyword search (BM25)", "Using both Wi-Fi and Ethernet", "Searching text and video at the exact same millisecond"], 1),
    29: ("How do production chatbots remember user state without bloating context?", ["They don't, they forget everything immediately", "Dynamic Context Injection from a lightweight external session store", "They save the entire conversation history into every prompt", "They run constantly in the background"], 1),
    30: ("What is 'Semantic Caching'?", ["Clearing your browser cookies every 24 hours", "Storing prior query embeddings and returning cached answers for similar questions", "Caching only images and CSS files", "Saving chat logs to a thumb drive"], 1),
    31: ("What differentiates an 'AI Agent' from a standard chatbot?", ["Agents have colorful 3D avatars", "Agents can plan, use external tools, call APIs, and execute autonomous multi-step tasks", "Agents cost $50 per month", "Agents only speak in audio"], 1),
    32: ("What is 'Tool Calling' / 'Function Calling' in LLMs?", ["Asking the AI to recommend software apps", "The model outputting structured arguments to trigger real external APIs and code", "Calling customer support on the telephone", "Installing a Python package on Windows"], 1),
    33: ("Why is a Multi-Agent Specialist Squad superior to a single giant prompt?", ["It uses more electricity", "Separation of concerns: specialized agents (Coder, Critic, Researcher) reduce cognitive error", "It takes 10x longer to run", "Single agents refuse to work overtime"], 1),
    34: ("What is 'Persistent Memory' for AI agents?", ["Upgrading the computer's physical RAM to 64 GB", "Cross-session state storage allowing agents to remember user preferences & past decisions", "Keeping the browser tab open forever", "Hardcoding answers into the Python script"], 1),
    35: ("What is the ReAct loop in agentic architecture?", ["A JavaScript frontend UI framework", "Reason + Act + Observe iterative cycle until a goal is accomplished", "Reacting emotionally to user insults", "A video recording software"], 1),
    36: ("What is the role of an 'Agent Orchestrator' / Supervisor?", ["To pay the cloud server bills", "To decompose goals, assign sub-tasks to specialized worker agents, and synthesize results", "To monitor employee chat logs", "To schedule calendar meetings"], 1),
    37: ("What is 'Tree of Thoughts' (ToT) reasoning?", ["Planting trees using AI algorithms", "Exploring multiple reasoning branches simultaneously, evaluating outcomes, and backtracking", "Drawing family trees in PowerPoint", "A decision tree in Excel"], 1),
    38: ("What is 'Human-in-the-Loop' (HITL) in autonomous workflows?", ["A human typing prompts manually all day", "Requiring human review & sign-off before executing high-risk actions (e.g. payments, deletion)", "Playing video games during office hours", "Replacing AI completely with human interns"], 1),
    39: ("What are 'Guardrails' in agentic systems?", ["Physical fences around data center racks", "Deterministic validation layers that enforce safety, schema, budget, and scope limits", "The browser window borders", "The terms of service checkbox"], 1),
    40: ("What is MCP (Model Context Protocol)?", ["A Minecraft multiplayer gaming protocol", "An open standard enabling AI models to connect seamlessly to any local tool, DB, or API", "Microsoft Certified Professional certification", "A protocol for master clock timing"], 1),
}

for row_idx, row in enumerate(ws_sarav.iter_rows(min_row=2, values_only=True), start=2):
    day_str = str(row[h_map.get('Day', 0)] or f"Day {row_idx-1}")
    ep_num = int(row[h_map.get('Episode_Number', 1)] or (row_idx - 1))
    concept = str(row[h_map.get('Concept', 2)] or "")
    category = str(row[h_map.get('Category', 3)] or "")
    filename = str(row[h_map.get('Video_Filename', 4)] or "")
    title = str(row[h_map.get('YouTube_Shorts_Title', 5)] or "")
    desc = str(row[h_map.get('YouTube_Description', 7)] or "")
    tags = str(row[h_map.get('Tags_Comma_Separated', 8)] or "")
    pinned = str(row[h_map.get('Pinned_Comment', 10)] or "")

    # Cover selection: "always Stop one..."
    # Match in SARAV_COVERS_DIR
    matched_covers = [f for f in sarav_cover_files if f'Ep{ep_num:02d}' in f or f'Ep{ep_num}_' in f]
    stop_matched = [f for f in matched_covers if 'Option_1' in f or 'Stop' in f]
    chosen_cover_file = stop_matched[0] if stop_matched else (matched_covers[0] if matched_covers else None)

    cover_asset_path = None
    cover_download_name = f"Sarav_AI_Shorts_Ep{ep_num:03d}_Cover.png"

    if chosen_cover_file:
        src_path = os.path.join(SARAV_COVERS_DIR, chosen_cover_file)
        dest_filename = f"cover_ep{ep_num:03d}.png"
        dest_path = os.path.join(SARAV_DEST, dest_filename)
        shutil.copyfile(src_path, dest_path)
        cover_asset_path = f"assets/sarav_ai/{dest_filename}"
    elif ep_num in shorts_meta and shorts_meta[ep_num].get('thumb'):
        # Download YouTube thumbnail for Ep 1-6
        dest_filename = f"cover_ep{ep_num:03d}.jpg"
        dest_path = os.path.join(SARAV_DEST, dest_filename)
        cover_download_name = f"Sarav_AI_Shorts_Ep{ep_num:03d}_Cover.jpg"
        if not os.path.exists(dest_path):
            try:
                urllib.request.urlretrieve(shorts_meta[ep_num]['thumb'], dest_path)
            except Exception as e:
                print(f"Thumb download failed for Ep {ep_num}: {e}")
        if os.path.exists(dest_path):
            cover_asset_path = f"assets/sarav_ai/{dest_filename}"

    # Poll generation
    if ep_num in POLL_PATTERNS:
        q, opts, correct_idx = POLL_PATTERNS[ep_num]
    else:
        q = f"🧠 AI Architecture Quiz: In '{concept}', what is the core architectural principle?"
        opts = [
            f"Always prioritize zero-cost custom architecture over paid SaaS wrappers",
            f"Rely solely on default commercial web chatbots without optimization",
            f"Increase compute budget without measuring token consumption",
            f"Ignore memory boundaries and prompt constraints"
        ]
        correct_idx = 0

    poll_packet = {
        "question": q,
        "options": opts,
        "correct_index": correct_idx,
        "full_text": f"🗳️ COMMUNITY POLL • Day {ep_num}/100\n\n{q}\n\n" + "\n".join([f"{chr(65+i)}) {opt}" for i, opt in enumerate(opts)]) + f"\n\n👉 Drop your explanation in the comments below!"
    }

    sarav_episodes.append({
        "day": day_str,
        "episode": ep_num,
        "concept": concept,
        "category": category,
        "filename": filename,
        "title": title,
        "description": desc,
        "tags": tags,
        "pinned_comment": pinned,
        "cover_url": cover_asset_path,
        "cover_filename": cover_download_name,
        "poll": poll_packet
    })

print(f"Loaded {len(sarav_episodes)} Sarav X AI episodes with covers & polls.")

print("\n--- STEP 2: PARSING THE LOOP (INKLING TALES) SHORTS ---")
wb_loop = openpyxl.load_workbook(LOOP_XLSX, read_only=True)
ws_loop = wb_loop.active
loop_header = [cell for cell in next(ws_loop.iter_rows(min_row=1, max_row=1, values_only=True))]
lh_map = {name: i for i, name in enumerate(loop_header) if name}

loop_episodes = []
for row_idx, row in enumerate(ws_loop.iter_rows(min_row=2, values_only=True), start=2):
    ep_num = int(row[lh_map.get('Episode_Number', 2)] or (row_idx - 1))
    day_str = str(row[lh_map.get('Day', 0)] or f"Day {(ep_num+1)//2}")
    slot = str(row[lh_map.get('Slot', 1)] or "")
    hook = str(row[lh_map.get('Concept_Hook', 3)] or "")
    twist = str(row[lh_map.get('Twist_Line', 4)] or "")
    category = str(row[lh_map.get('Category', 5)] or "")
    video_file = str(row[lh_map.get('Video_Filename', 6)] or "")
    cover_file = str(row[lh_map.get('Cover_Filename', 7)] or f"cover_tale_{ep_num:03d}.jpg")
    title = str(row[lh_map.get('YouTube_Shorts_Title', 8)] or "")
    desc = str(row[lh_map.get('YouTube_Description', 10)] or "")
    tags = str(row[lh_map.get('Tags_Comma_Separated', 13)] or "")
    pinned = str(row[lh_map.get('Pinned_Comment', 16)] or "")

    # Copy cover if present
    src_cover = os.path.join(LOOP_COVERS_DIR, cover_file)
    dest_cover_file = f"cover_tale_{ep_num:03d}.jpg"
    dest_cover_path = os.path.join(LOOP_DEST, dest_cover_file)
    cover_asset_path = None

    if os.path.exists(src_cover):
        shutil.copyfile(src_cover, dest_cover_path)
        cover_asset_path = f"assets/the_loop/{dest_cover_file}"

    loop_episodes.append({
        "episode": ep_num,
        "day": day_str,
        "slot": slot,
        "hook": hook,
        "twist": twist,
        "category": category,
        "video_filename": video_file,
        "title": title,
        "description": desc,
        "tags": tags,
        "pinned_comment": pinned,
        "cover_url": cover_asset_path,
        "cover_filename": dest_cover_file
    })

print(f"Loaded {len(loop_episodes)} The Loop episodes with covers.")

print("\n--- STEP 3: PARSING SID & ISHA INSTAGRAM (DAYS 01–30) ---")
with open(SIDISHA_HTML, encoding='utf-8') as f:
    soup_sidi = BeautifulSoup(f.read(), 'html.parser')

sidisha_days = []
for card in soup_sidi.find_all(class_='day-card'):
    day_num = int(card.get('data-day', 0))
    act_num = int(card.get('data-act', 1))
    date_str = card.find(class_='date-badge').get_text(strip=True) if card.find(class_='date-badge') else ""
    title = card.find(class_='story-title').get_text(strip=True) if card.find(class_='story-title') else ""
    punchline = card.find(class_='punchline-text').get_text(strip=True) if card.find(class_='punchline-text') else ""
    caption_elem = card.find(class_='caption-display')
    caption_text = caption_elem.get_text() if caption_elem else ""

    # Copy slide 1 and slide 2
    s1_src = os.path.join(SIDISHA_SLIDE1_DIR, f"day_{day_num:02d}.jpg")
    s2_src = os.path.join(SIDISHA_SLIDE2_DIR, f"day_{day_num:02d}.jpg")

    s1_dest = os.path.join(SIDISHA_S1_DEST, f"day_{day_num:02d}.jpg")
    s2_dest = os.path.join(SIDISHA_S2_DEST, f"day_{day_num:02d}.jpg")

    s1_path = None
    s2_path = None

    if os.path.exists(s1_src):
        shutil.copyfile(s1_src, s1_dest)
        s1_path = f"assets/sid_isha/slide1/day_{day_num:02d}.jpg"

    if os.path.exists(s2_src):
        shutil.copyfile(s2_src, s2_dest)
        s2_path = f"assets/sid_isha/slide2/day_{day_num:02d}.jpg"

    # Extract hashtags from caption
    hashtags = " ".join(re.findall(r'#\w+', caption_text))

    sidisha_days.append({
        "day": day_num,
        "act": act_num,
        "date": date_str,
        "title": title,
        "punchline": punchline,
        "caption": caption_text,
        "hashtags": hashtags,
        "slide1_url": s1_path,
        "slide1_filename": f"SidIsha_Day_{day_num:02d}_Slide1_Art.jpg",
        "slide2_url": s2_path,
        "slide2_filename": f"SidIsha_Day_{day_num:02d}_Slide2_Story.jpg"
    })

print(f"Loaded {len(sidisha_days)} Sid & Isha days with 2-slide carousels.")

print("\n--- STEP 4: PARSING INKLING TALES INSTAGRAM (EP 51–100) ---")
with open(INKLING_IG_HTML, encoding='utf-8') as f:
    soup_inkling = BeautifulSoup(f.read(), 'html.parser')

inkling_ig_episodes = []
for card in soup_inkling.find_all(class_='episode-card'):
    ep_num = int(card.get('data-id', 0))
    category = card.get('data-category', '')
    hook = card.find(class_='story-hook').get_text(strip=True) if card.find(class_='story-hook') else ""
    twist = card.find(class_='story-twist').get_text(strip=True) if card.find(class_='story-twist') else ""
    caption_elem = card.find(class_='caption-display')
    caption_text = caption_elem.get_text() if caption_elem else ""

    # Audio cue & video file
    alt_text = ""
    alt_p = card.find('p', class_='asset-path')
    if alt_p:
        alt_text = alt_p.get_text(strip=True)

    # Use loop cover
    cover_file = f"cover_tale_{ep_num:03d}.jpg"
    cover_path = f"assets/the_loop/{cover_file}" if os.path.exists(os.path.join(LOOP_DEST, cover_file)) else None

    # Extract hashtags
    hashtags = " ".join(re.findall(r'#\w+', caption_text))

    inkling_ig_episodes.append({
        "episode": ep_num,
        "category": category,
        "hook": hook,
        "twist": twist,
        "caption": caption_text,
        "hashtags": hashtags,
        "alt_text": alt_text,
        "cover_url": cover_path,
        "cover_filename": cover_file
    })

print(f"Loaded {len(inkling_ig_episodes)} Inkling Tales Instagram episodes.")

# Combine all into master JSON catalog
master_catalog = {
    "sarav_ai": sarav_episodes,
    "the_loop": loop_episodes,
    "sid_isha": sidisha_days,
    "inkling_ig": inkling_ig_episodes
}

catalog_js_path = os.path.join(BASE_DIR, "catalog.js")
with open(catalog_js_path, "w", encoding="utf-8") as f:
    f.write("window.PUBLISHING_CATALOG = " + json.dumps(master_catalog, ensure_ascii=False, indent=2) + ";\n")

print(f"\n Master catalog written to {catalog_js_path} (Size: {os.path.getsize(catalog_js_path) / 1024:.1f} KB)")
