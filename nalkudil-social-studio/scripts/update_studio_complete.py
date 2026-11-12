import json
import os
import re

CATALOG_PATH = r"D:\Websites\nalkudilstudio.github.io\nalkudil-social-studio\catalog.js"

with open(CATALOG_PATH, "r", encoding="utf-8") as f:
    raw = f.read()

prefix = "window.PUBLISHING_CATALOG = "
json_str = raw.replace(prefix, "").rstrip(";\n ")
catalog = json.loads(json_str)

# Live YouTube Short IDs
sarav_live_map = {
    1: "1beFkdxqO-s",
    2: "mvegAJR9Qdg",
    3: "ghOUtQoi9x8",
    4: "kWRB1bpI1QY",
    5: "TgiUHtfkWig",
    6: "-krKiNXAH_Y",
    7: "A7p_ETb7V48",
    8: "EM7Ue3j2u1c",
    9: "dI-iFQ1j_SY",
    10: "xnhOWpL_P0E",
    11: "os_bDL3rLKM",
    12: "tZ_ka5zOvz0",
    13: "xjEeQ-YiteU",
    14: "i9KuTmULUfs",
    15: "KFLDBvjufkA",
    16: "_yAo-Ej18eg",
    17: "LXaadvIMv6s",
    18: "8lG7o0zeCLA",
    19: "c-DmZdCa7W0",
    20: "-XcuPBDl2aM",
    21: "5MKvLB09J-c",
    22: "-AaLQMEHZAU",
    23: "cCyNsnQAe-Q",
    24: "8cc_WGDMOBU",
    25: "qY2LbgivWWU",
    26: "lswnFGuDIq8",
    27: "KSSWj-5mPus",
    28: "O6R4vPadEgk",
    29: "fwShBL1tWvo",
    30: "L61U79mMTLY",
    31: "ORpH9c0crUM",
    32: "smgvSDF_r2Y",
    33: "7EjgeXQrLsk",
    34: "08iitruCQgs",
    35: "5UY-dd-ZHN4",
    36: "ktqwATHzvS8",
    37: "fav-pse9DUs",
    38: "-BT8QtTRG8o",
    39: "c-R3SjKeUTg",
    40: "f-CCh39WHfg",
    41: "Cptnp27fcfY",
    42: "FQvfrZT9x1w",
    43: "Li-x6Zidv4I",
}

# Community Poll Links
community_poll_links = {
    38: "https://youtube.com/post/UgkxnMDOeZMoHQ8ehgwwNo8K3760K2_qgnyh?si=UQwka27OwlWo2gJF",
    39: "https://youtube.com/post/UgkxGx0IdoIdUHDnobMMuT-G7UjiXkJCfttM?si=sBrqZUzZI8TkjGI3",
    40: "https://youtube.com/post/UgkxPKuDumAB-qebjr4mVL4W_ahJLWxUlwcp?si=9yQNqrAf32SOQdG_",
}

# Verified Polls for Days 41 to 50 with ALL OPTIONS <= 80 CHARACTERS
curated_polls_41_to_50 = {
    41: {
        "question": "When you prompt AI to generate an image, which model connects text to visuals?",
        "options": [
            "CLIP (Contrastive Language-Image Pretraining)",
            "Pure ChatGPT text tokenizer",
            "Standard SQL database index",
            "Edge-TTS speech synthesizer"
        ],
        "correct_index": 0
    },
    42: {
        "question": "What allows modern AI video models (like Sora) to keep objects consistent in time?",
        "options": [
            "Spatiotemporal latent patches (Space + Time)",
            "Generating 30 separate PNG images every second",
            "Using traditional Adobe Premiere filters",
            "Storing every single raw video frame in RAM"
        ],
        "correct_index": 0
    },
    43: {
        "question": "What is the primary role of a neural vocoder (like Vocos) in modern AI voice?",
        "options": [
            "Converts acoustic spectrograms into sound waves",
            "Translates English text into French audio",
            "Records human voice from a physical microphone",
            "Checks prompt grammar and spelling errors"
        ],
        "correct_index": 0
    },
    44: {
        "question": "How do Diffusion Models generate crisp, photorealistic art from pure static?",
        "options": [
            "Iteratively subtracting noise via reverse U-Net",
            "Copy-pasting pixels from Google Images",
            "Stretching and upscaling a 10x10 pixel thumbnail",
            "Blending 1,000 photos with 50% opacity"
        ],
        "correct_index": 0
    },
    45: {
        "question": "What math structure allows 2D AI avatars to speak with realistic lip-sync?",
        "options": [
            "3D Facial Blendshapes & FACS coefficients",
            "Playing an animated GIF on an infinite loop",
            "Static Photoshop warping layers",
            "Random pixel color inversion"
        ],
        "correct_index": 0
    },
    46: {
        "question": "How can zero-shot models (like F5-TTS) clone your voice in just 10 seconds?",
        "options": [
            "Matching speaker timbre in acoustic latent space",
            "Retraining the entire neural network from zero",
            "Applying an aggressive robotic pitch shifter",
            "Downloading your private WhatsApp voice notes"
        ],
        "correct_index": 0
    },
    47: {
        "question": "How do generative audio models (Suno/Udio) compose full multi-track songs?",
        "options": [
            "Dual-stream diffusion of melody, rhythm & vocal",
            "Splicing copyrighted MP3 tracks from Spotify",
            "Playing MIDI files using 90s soundcard fonts",
            "Auto-tuning a human singer's hum"
        ],
        "correct_index": 0
    },
    48: {
        "question": "How does Generative AI upscale blurry, low-res photos without smudging?",
        "options": [
            "Hallucinates sharp realistic texture priors",
            "Basic bilinear pixel stretching",
            "Increasing monitor brightness and contrast",
            "Applying heavy Gaussian blur to edges"
        ],
        "correct_index": 0
    },
    49: {
        "question": "What makes native multimodal AI (like Gemini) smarter than tool-stitched apps?",
        "options": [
            "Early fusion: pixels, audio & text share one space",
            "Chaining 5 separate external SaaS API calls",
            "Running 3 separate models on different laptops",
            "Converting all photos into plain text OCR first"
        ],
        "correct_index": 0
    },
    50: {
        "question": "How does Neural Style Transfer paint your photo in the exact style of Van Gogh?",
        "options": [
            "Separates content and style via CNN feature maps",
            "Overlays a translucent 50% opacity photo filter",
            "Converts all image pixels to black and white",
            "Pastes the artist's signature onto your photo"
        ],
        "correct_index": 0
    }
}

# Dedicated Curated WhatsApp Posts for Days 38 to 44
curated_whatsapp_posts = {
    38: (
        "Day 38 / 100: Why Anthropic’s MCP Changes Everything for AI Tooling\n\n"
        "Connecting AI to databases and APIs used to mean building custom spaghetti code for every single model.\n\n"
        "Anthropic’s Model Context Protocol (MCP) changes this forever. It is the universal USB-C cable for AI:\n"
        "1. The Core Standard: One open protocol connects any AI agent to your files, databases, and development tools.\n"
        "2. Zero Vendor Lock-in: Switch from Claude to Cursor or Antigravity instantly without rewriting your tool integrations.\n\n"
        "One universal socket powering the autonomous future.\n\n"
        "🎬 Watch the visual breakdown:\n"
        "https://www.youtube.com/shorts/-BT8QtTRG8o\n\n"
        "🗳️ Test your knowledge (Day 38 Quiz):\n"
        "https://youtube.com/post/UgkxnMDOeZMoHQ8ehgwwNo8K3760K2_qgnyh?si=UQwka27OwlWo2gJF"
    ),
    39: (
        "Day 39 / 100: You Cannot Improve an AI Pipeline You Don't Measure\n\n"
        "Most developers test AI prompts by hitting refresh and vibing. That is why enterprise AI breaks in production.\n\n"
        "Automated Evaluations turn subjective AI intuition into hard engineering data:\n"
        "1. Deterministic Checks: Code-level validation for strict JSON schemas, latency, and regex patterns.\n"
        "2. LLM-as-a-Judge: A secondary model scoring outputs for tone, accuracy, and hallucination regressions.\n\n"
        "If you don't benchmark your prompts in CI/CD, your users will benchmark them for you.\n\n"
        "🎬 Watch the visual breakdown:\n"
        "https://www.youtube.com/shorts/c-R3SjKeUTg\n\n"
        "🗳️ Test your knowledge (Day 39 Quiz):\n"
        "https://youtube.com/post/UgkxGx0IdoIdUHDnobMMuT-G7UjiXkJCfttM?si=sBrqZUzZI8TkjGI3"
    ),
    40: (
        "Day 40 / 100: Cloud AI Is Powerful, But Edge AI Is Private and Free\n\n"
        "Relying entirely on cloud AI APIs creates massive token bills and serious privacy vulnerabilities.\n\n"
        "The breakthrough of 2026 is Local Small Language Models (SLMs) running directly on your device:\n"
        "1. Edge Silicon (NPUs): Models like Phi-4-mini and Qwen run at 90 tokens/second on consumer hardware.\n"
        "2. Complete Data Sovereignty: Zero API costs, zero internet dependency, and 100% private data isolation.\n\n"
        "Heavy reasoning stays on the cloud; daily operational intelligence belongs on the edge.\n\n"
        "🎬 Watch the visual breakdown:\n"
        "https://www.youtube.com/shorts/f-CCh39WHfg\n\n"
        "🗳️ Test your knowledge (Day 40 Quiz):\n"
        "https://youtube.com/post/UgkxPKuDumAB-qebjr4mVL4W_ahJLWxUlwcp?si=9yQNqrAf32SOQdG_"
    ),
    41: (
        "Day 41 / 100: Type a Sentence. Get a Full Image. How?\n\n"
        "You type eight words into an AI prompt box, and two seconds later you have a 4K photorealistic image. How does text cross the bridge into pixels?\n\n"
        "The magic relies on an architectural bridge called CLIP:\n"
        "1. Contrastive Encoding: Your text prompt is translated into a mathematical coordinate vector in latent space.\n"
        "2. Concept Alignment: The model maps those words to millions of visual patterns it learned during training.\n\n"
        "It isn't searching a photo library—it is rendering mathematical imagination.\n\n"
        "🎬 Watch the visual breakdown:\n"
        "https://www.youtube.com/shorts/Cptnp27fcfY\n\n"
        "🗳️ Test your knowledge (Day 41 Quiz):\n"
        "[PASTE_COMMUNITY_POST_LINK_HERE]"
    ),
    42: (
        "Day 42 / 100: AI Now Generates Full Videos From Text\n\n"
        "First AI learned to write, then it learned to draw, and now it simulates physical motion across space and time.\n\n"
        "Models like Sora and Veo are not video stitchers—they are Spatiotemporal World Models:\n"
        "1. 3D Space + 1D Time: The model treats a video clip as a 4-dimensional volume of space-time latent patches.\n"
        "2. Physical Continuity: It simulates light rays, gravity, and object permanence across consecutive frames.\n\n"
        "We are witnessing the death of static cameras and the birth of infinite generative cinema.\n\n"
        "🎬 Watch the visual breakdown:\n"
        "https://www.youtube.com/shorts/FQvfrZT9x1w\n\n"
        "🗳️ Test your knowledge (Day 42 Quiz):\n"
        "[PASTE_COMMUNITY_POST_LINK_HERE]"
    ),
    43: (
        "Day 43 / 100: How AI Voices Sound So Human Now\n\n"
        "Remember robotic text-to-speech that sounded like an elevator announcement? Modern AI voice sounds indistinguishable from real human speech.\n\n"
        "The breakthrough comes down to Neural Vocoders and Flow Matching:\n"
        "1. Prosody Modeling: The AI predicts breath micro-pauses, vocal cadence, and emotional chest inflection.\n"
        "2. Neural Vocoders (Vocos/HiFi-GAN): Decodes abstract acoustic latents into clean 24kHz studio audio waves in 100 milliseconds.\n\n"
        "Speech synthesis is no longer robotic concatenation—it is acoustic physics in real time.\n\n"
        "🎬 Watch the visual breakdown:\n"
        "https://www.youtube.com/shorts/Li-x6Zidv4I\n\n"
        "🗳️ Test your knowledge (Day 43 Quiz):\n"
        "[PASTE_COMMUNITY_POST_LINK_HERE]"
    ),
    44: (
        "Day 44 / 100: Born From Static—How Diffusion Models Create Art!\n\n"
        "Every breathtaking AI artwork online started its life as a chaotic wall of television static.\n\n"
        "This is the magic of Diffusion Models. The process relies on a two-part duality:\n"
        "1. The Forward Process: Pure visual data is systematically destroyed by adding Gaussian noise.\n"
        "2. The Reverse Process: Guided by your prompt, the neural network learns to subtract that noise across 30 iterative steps.\n\n"
        "It is literally turning visual chaos into order. Pure randomness molded into museum-grade visuals.\n\n"
        "🎬 Watch the visual breakdown:\n"
        "[PASTE_YOUTUBE_SHORT_LINK_HERE]\n\n"
        "🗳️ Test your knowledge (Day 44 Quiz):\n"
        "[PASTE_COMMUNITY_POST_LINK_HERE]"
    )
}

# Update Sarav AI items
for item in catalog.get("sarav_ai", []):
    ep = item.get("episode")
    
    # 1. Update YouTube status & links
    if ep in sarav_live_map:
        item["status"] = "PUBLISHED"
        item["youtube_id"] = sarav_live_map[ep]
        item["youtube_url"] = f"https://www.youtube.com/shorts/{sarav_live_map[ep]}"
    elif ep == 44:
        item["status"] = "READY 🚀"
        item["youtube_id"] = ""
        item["youtube_url"] = ""

    # 2. Update Polls (especially Days 41 to 50)
    if ep in curated_polls_41_to_50:
        p_data = curated_polls_41_to_50[ep]
        opts = p_data["options"]
        # Verify length
        for opt in opts:
            assert len(opt) <= 80, f"Option too long in Ep {ep}: {opt} ({len(opt)} chars)"
        
        full_text = f"🗳️ COMMUNITY POLL • Day {ep}/100\n\n{p_data['question']}\n\n" + "\n".join([f"{chr(65+i)}) {opt}" for i, opt in enumerate(opts)]) + f"\n\n👉 Drop your explanation in the comments below!"
        item["poll"] = {
            "question": p_data["question"],
            "options": opts,
            "correct_index": p_data["correct_index"],
            "full_text": full_text
        }
    
    # Also verify existing polls in Ep 1-40: ensure options don't break hard 80-char rule
    if "poll" in item and "options" in item["poll"]:
        cleaned_opts = []
        for opt in item["poll"]["options"]:
            if len(opt) > 80:
                # Truncate cleanly or shorten
                cleaned_opts.append(opt[:77] + "...")
            else:
                cleaned_opts.append(opt)
        item["poll"]["options"] = cleaned_opts

    # 3. Add WhatsApp Broadcast text
    if ep in curated_whatsapp_posts:
        item["whatsapp_post"] = curated_whatsapp_posts[ep]
    else:
        # Generate default high-quality WhatsApp post for any other episode
        yt_link = item.get("youtube_url") or "[PASTE_YOUTUBE_SHORT_LINK_HERE]"
        quiz_link = community_poll_links.get(ep, "[PASTE_COMMUNITY_POST_LINK_HERE]")
        item["whatsapp_post"] = (
            f"Day {ep} / 100: {item.get('concept', '')} — {item.get('title', '').split('#')[0].strip()}\n\n"
            f"Dive into today's bite-sized AI architecture breakdown! We unpack {item.get('concept', '')} with clear intuition and zero fluff.\n\n"
            f"🎬 Watch the visual breakdown:\n{yt_link}\n\n"
            f"🗳️ Test your knowledge (Day {ep} Quiz):\n{quiz_link}"
        )

print("Updated sarav_ai items successfully.")

# Create the Sarav Playlists Dataset for Clusters 1 to 10 + Master Umbrella
playlists_data = [
    {
        "id": "cluster_01",
        "cluster_num": 1,
        "cluster_title": "Cluster 1: LLM Fundamentals (Ep 01–10)",
        "episodes_range": "Ep 01–10",
        "title": "100 Days of Learning AI 👉 Cluster 1: LLM Fundamentals (Ep 01–10) | Sigma Byte",
        "description": (
            "Master LLM Fundamentals in 10 bite-sized high-IQ episodes! 💡\n\n"
            "Stop treating AI like magic. In this 10-part series, Enterprise AI Architect Sarav breaks down the exact internal mechanics of LLMs — from how text turns into tokens and high-dimensional vectors to why models hallucinate and how to control output temperature.\n\n"
            "🧠 WHAT YOU WILL LEARN IN THIS CLUSTER:\n"
            "• Day 01: Tokens — Your AI Doesn't Read Words. It Reads THIS.\n"
            "• Day 02: Context Window — AI Has a Memory Limit. Here's How Big.\n"
            "• Day 03: Embeddings — AI Turns Words Into Numbers. Here's Why.\n"
            "• Day 04: Transformers — The One Invention Behind Every AI You Use.\n"
            "• Day 05: Attention Mechanism — Why AI Knows Which Words Matter Most.\n"
            "• Day 06: Temperature — This Setting Controls If AI Gets Creative or Boring.\n"
            "• Day 07: Zero-shot Learning — AI Can Do Tasks It Was NEVER Trained For.\n"
            "• Day 08: Few-Shot Prompting — Give AI 2-3 Examples. Watch It Learn Instantly.\n"
            "• Day 09: Chain of Thought — Ask AI to 'Think Step by Step.' It Actually Works.\n"
            "• Day 10: AI Hallucination — Why AI Confidently Lies to You Sometimes.\n\n"
            "───────────────\n"
            "🎯 ABOUT THIS SERIES:\n"
            "Welcome to '100 Days of Learning AI' with Sarav (Enterprise AI Architect & Digital Workplace Technology Head). Every day in under 45 seconds, we break down high-IQ Artificial Intelligence concepts into clear, practical intuition for creators, developers, and enterprise leaders.\n\n"
            "🔔 SUBSCRIBE to @iamsaravofficial to master AI one byte at a time!\n"
            "🌐 Projects, Architecture Blueprints & Masterclass: https://iamsaravofficial.com\n"
            "💬 Connect with Sarav on LinkedIn & explore the zero-cost open-source AI stack.\n"
            "───────────────\n\n"
            "#shorts #ai #artificialintelligence #learnai #llmfundamentals #sigmabyte #saravxai #100daysofai #techtips"
        ),
        "hashtags": "#shorts #ai #artificialintelligence #learnai #llmfundamentals #sigmabyte #saravxai #100daysofai #techtips",
        "playlist_url": "https://www.youtube.com/playlist?list=PLKVhcsbIqnjW_cluster1"
    },
    {
        "id": "cluster_02",
        "cluster_num": 2,
        "cluster_title": "Cluster 2: Prompt Engineering Mastery (Ep 11–20)",
        "episodes_range": "Ep 11–20",
        "title": "100 Days of Learning AI 👉 Cluster 2: Prompt Engineering Mastery (Ep 11–20) | Sigma Byte",
        "description": (
            "Master Prompt Engineering Mastery in 10 bite-sized high-IQ episodes! 💡\n\n"
            "99% of people prompt AI like an intern. In this masterclass cluster, discover how enterprise architects structure prompts for zero ambiguity, enforce valid JSON schemas for production APIs, and chain multi-step reasoning loops.\n\n"
            "🧠 WHAT YOU WILL LEARN IN THIS CLUSTER:\n"
            "• Day 11: System Prompts — The Hidden Instructions Behind Every AI Chat.\n"
            "• Day 12: Prompt Chaining — Stop Asking AI One Giant Question.\n"
            "• Day 13: Role Prompting — Tell AI 'You Are a Doctor' — Watch What Happens.\n"
            "• Day 14: Few-shot Prompting — Show, Don't Tell — AI's Favorite Learning Style.\n"
            "• Day 15: Negative Prompting — Tell AI What NOT to Do. It Changes Everything.\n"
            "• Day 16: Prompt Injection — The Security Flaw Hiding in AI Chatbots.\n"
            "• Day 17: Structured Output — Force AI to Reply in JSON. Here's How.\n"
            "• Day 18: Meta Prompting — Ask AI to Write Your Prompt For You.\n"
            "• Day 19: Iterative Prompting — The First AI Answer Is Never the Final One.\n"
            "• Day 20: Prompt Templates — Reuse This Prompt Structure Forever.\n\n"
            "───────────────\n"
            "🎯 ABOUT THIS SERIES:\n"
            "Welcome to '100 Days of Learning AI' with Sarav (Enterprise AI Architect & Digital Workplace Technology Head). Every day in under 45 seconds, we break down high-IQ Artificial Intelligence concepts into clear, practical intuition for creators, developers, and enterprise leaders.\n\n"
            "🔔 SUBSCRIBE to @iamsaravofficial to master AI one byte at a time!\n"
            "🌐 Projects, Architecture Blueprints & Masterclass: https://iamsaravofficial.com\n"
            "💬 Connect with Sarav on LinkedIn & explore the zero-cost open-source AI stack.\n"
            "───────────────\n\n"
            "#shorts #ai #artificialintelligence #learnai #promptengineeringmastery #sigmabyte #saravxai #100daysofai #techtips"
        ),
        "hashtags": "#shorts #ai #artificialintelligence #learnai #promptengineeringmastery #sigmabyte #saravxai #100daysofai #techtips",
        "playlist_url": "https://www.youtube.com/playlist?list=PLKVhcsbIqnjW_cluster2"
    },
    {
        "id": "cluster_03",
        "cluster_num": 3,
        "cluster_title": "Cluster 3: Production RAG & Vector Search (Ep 21–30)",
        "episodes_range": "Ep 21–30",
        "title": "100 Days of Learning AI 👉 Cluster 3: Production RAG & Vector Search (Ep 21–30) | Sigma Byte",
        "description": (
            "Master Production RAG & Vector Search in 10 bite-sized high-IQ episodes! 💡\n\n"
            "Feeding whole PDFs to AI is broken. This cluster reveals the complete production RAG (Retrieval-Augmented Generation) blueprint — how vector databases index meaning, how recursive chunking preserves context, and how hybrid search eliminates hallucinations.\n\n"
            "🧠 WHAT YOU WILL LEARN IN THIS CLUSTER:\n"
            "• Day 21: Vector Database — Where AI Actually Stores 'Memory.'\n"
            "• Day 22: Semantic Search — Search Engines That Understand MEANING, Not Just Words.\n"
            "• Day 23: RAG — How AI Answers Questions From YOUR Documents.\n"
            "• Day 24: Chunking — Feeding AI a Whole PDF? You're Doing It Wrong.\n"
            "• Day 25: Embeddings — How AI Measures If Two Ideas Are 'Close.'\n"
            "• Day 26: Reranking — AI's Second Opinion on Search Results.\n"
            "• Day 27: Knowledge Grounding — Why This Trick Stops AI From Making Things Up.\n"
            "• Day 28: Hybrid Search — Why the Best AI Search Uses TWO Methods.\n"
            "• Day 29: Context Injection — How Your Chatbot 'Remembers' Your Account Info.\n"
            "• Day 30: Retrieval Latency — Why Some AI Chatbots Feel Slow.\n\n"
            "───────────────\n"
            "🎯 ABOUT THIS SERIES:\n"
            "Welcome to '100 Days of Learning AI' with Sarav (Enterprise AI Architect & Digital Workplace Technology Head). Every day in under 45 seconds, we break down high-IQ Artificial Intelligence concepts into clear, practical intuition for creators, developers, and enterprise leaders.\n\n"
            "🔔 SUBSCRIBE to @iamsaravofficial to master AI one byte at a time!\n"
            "🌐 Projects, Architecture Blueprints & Masterclass: https://iamsaravofficial.com\n"
            "💬 Connect with Sarav on LinkedIn & explore the zero-cost open-source AI stack.\n"
            "───────────────\n\n"
            "#shorts #ai #artificialintelligence #learnai #productionragvectorsearch #sigmabyte #saravxai #100daysofai #techtips"
        ),
        "hashtags": "#shorts #ai #artificialintelligence #learnai #productionragvectorsearch #sigmabyte #saravxai #100daysofai #techtips",
        "playlist_url": "https://www.youtube.com/playlist?list=PLKVhcsbIqnjW_cluster3"
    },
    {
        "id": "cluster_04",
        "cluster_num": 4,
        "cluster_title": "Cluster 4: Agentic AI & Autonomous Systems (Ep 31–40)",
        "episodes_range": "Ep 31–40",
        "title": "100 Days of Learning AI 👉 Cluster 4: Agentic AI & Autonomous Systems (Ep 31–40) | Sigma Byte",
        "description": (
            "Master Agentic AI & Autonomous Systems in 10 bite-sized high-IQ episodes! 💡\n\n"
            "Chatbots talk. AI Agents execute. Learn the 2026 systems architecture powering autonomous AI — from function calling and ReAct loops to orchestrating multi-agent squads and connecting models to any database via the Model Context Protocol (MCP).\n\n"
            "🧠 WHAT YOU WILL LEARN IN THIS CLUSTER:\n"
            "• Day 31: AI Agents — AI That Doesn't Just Chat — It ACTS.\n"
            "• Day 32: Tool Use — How AI Uses Apps Just Like You Do.\n"
            "• Day 33: Multi-Agent Systems — Why One AI Agent Isn't Enough Anymore.\n"
            "• Day 34: Agent Memory — Why Some AI Agents Remember You Across Sessions.\n"
            "• Day 35: ReAct Framework — The Loop That Makes AI Agents Actually Smart.\n"
            "• Day 36: Agent Orchestration — Who's the 'Manager' When AI Agents Work Together?\n"
            "• Day 37: Autonomous Planning — AI That Breaks Down YOUR Goal Into Steps.\n"
            "• Day 38: Human in the Loop — Why the BEST AI Agents Still Ask Permission.\n"
            "• Day 39: Agent Guardrails — The Invisible Fence Keeping AI Agents in Check.\n"
            "• Day 40: MCP — The New Standard Letting AI Talk to ANY App.\n\n"
            "───────────────\n"
            "🎯 ABOUT THIS SERIES:\n"
            "Welcome to '100 Days of Learning AI' with Sarav (Enterprise AI Architect & Digital Workplace Technology Head). Every day in under 45 seconds, we break down high-IQ Artificial Intelligence concepts into clear, practical intuition for creators, developers, and enterprise leaders.\n\n"
            "🔔 SUBSCRIBE to @iamsaravofficial to master AI one byte at a time!\n"
            "🌐 Projects, Architecture Blueprints & Masterclass: https://iamsaravofficial.com\n"
            "💬 Connect with Sarav on LinkedIn & explore the zero-cost open-source AI stack.\n"
            "───────────────\n\n"
            "#shorts #ai #artificialintelligence #learnai #agenticaiautonomoussystems #sigmabyte #saravxai #100daysofai #techtips"
        ),
        "hashtags": "#shorts #ai #artificialintelligence #learnai #agenticaiautonomoussystems #sigmabyte #saravxai #100daysofai #techtips",
        "playlist_url": "https://www.youtube.com/playlist?list=PLKVhcsbIqnjU"
    },
    {
        "id": "cluster_05",
        "cluster_num": 5,
        "cluster_title": "Cluster 5: Multimodal & GenAI Creative (Ep 41–50)",
        "episodes_range": "Ep 41–50",
        "title": "100 Days of Learning AI 👉 Cluster 5: Multimodal & GenAI Creative (Ep 41–50) | Sigma Byte",
        "description": (
            "Master Multimodal AI & Generative Media in 10 bite-sized high-IQ episodes! 💡\n\n"
            "From typing eight words to generating museum-grade 4K art, photorealistic video, and studio vocal clones. In this cluster, Enterprise AI Architect Sarav demystifies the generative media revolution — from CLIP latent embeddings and diffusion denoising to neural vocoders, 3D facial blendshapes, and native multimodal models.\n\n"
            "🧠 WHAT YOU WILL LEARN IN THIS CLUSTER:\n"
            "• Day 41: Text to Image — Type a Sentence. Get a Full Image. How?\n"
            "• Day 42: Text to Video — AI Now Generates Full Videos From Text\n"
            "• Day 43: Text to Speech — How AI Voices Sound So Human Now\n"
            "• Day 44: Diffusion Models — The Math Trick Behind Every AI Image\n"
            "• Day 45: AI Avatars — This Video Host Isn't Real. Neither Am I (Almost)\n"
            "• Day 46: Voice Cloning — AI Can Copy ANY Voice From 30 Seconds of Audio\n"
            "• Day 47: AI Music — AI Just Composed a Full Song. From Text\n"
            "• Day 48: Image Upscaling — Blurry Old Photo? AI Fixes It Instantly\n"
            "• Day 49: Multimodal AI — AI That Sees, Hears, AND Reads at Once\n"
            "• Day 50: Style Transfer — Turn Any Photo Into a Painting Instantly\n\n"
            "───────────────\n"
            "🎯 ABOUT THIS SERIES:\n"
            "Welcome to '100 Days of Learning AI' with Sarav (Enterprise AI Architect & Digital Workplace Technology Head). Every day in under 45 seconds, we break down high-IQ Artificial Intelligence concepts into clear, practical intuition for creators, developers, and enterprise leaders.\n\n"
            "🔔 SUBSCRIBE to @iamsaravofficial to master AI one byte at a time!\n"
            "🌐 Projects, Architecture Blueprints & Masterclass: https://iamsaravofficial.com\n"
            "💬 Connect with Sarav on LinkedIn & explore the zero-cost open-source AI stack.\n"
            "───────────────\n\n"
            "#shorts #ai #artificialintelligence #learnai #genai #multimodal #diffusion #sigmabyte #saravxai #100daysofai #techtips"
        ),
        "hashtags": "#shorts #ai #artificialintelligence #learnai #genai #multimodal #diffusion #sigmabyte #saravxai #100daysofai #techtips",
        "playlist_url": ""
    },
    {
        "id": "cluster_06",
        "cluster_num": 6,
        "cluster_title": "Cluster 6: AI Safety & Ethics (Ep 51–60)",
        "episodes_range": "Ep 51–60",
        "title": "100 Days of Learning AI 👉 Cluster 6: AI Safety & Ethics (Ep 51–60) | Sigma Byte",
        "description": (
            "Master AI Safety, Ethics & Alignment in 10 bite-sized high-IQ episodes! 💡\n\n"
            "Building AI is powerful; controlling AI safely is critical. This cluster explores the guardrails of modern machine learning — from addressing algorithmic bias and Reinforcement Learning from Human Feedback (RLHF) to detecting deepfakes, auditing model cards, and navigating global AI regulation.\n\n"
            "🧠 WHAT YOU WILL LEARN IN THIS CLUSTER:\n"
            "• Day 51: AI Bias — Why AI Can Be Unfair Without Anyone Coding It That Way\n"
            "• Day 52: AI Alignment — Making Sure AI Actually Wants What WE Want\n"
            "• Day 53: RLHF — The Secret Training Step That Makes AI 'Nice'\n"
            "• Day 54: Deepfakes — Fake Videos That Look 100% Real. Here's the Danger\n"
            "• Day 55: AI Regulation — Governments Are Racing to Control AI. Here's Why\n"
            "• Day 56: Explainable AI — Why 'AI Said So' Isn't Good Enough Anymore\n"
            "• Day 57: AI Privacy — Is Your Data Training the Next AI Model?\n"
            "• Day 58: AI Watermarking — How We'll Tell AI Content From Real Content\n"
            "• Day 59: Model Cards — The 'Nutrition Label' for AI Models\n"
            "• Day 60: Responsible AI — The Framework Every Company Building AI Needs\n\n"
            "───────────────\n"
            "🎯 ABOUT THIS SERIES:\n"
            "Welcome to '100 Days of Learning AI' with Sarav (Enterprise AI Architect & Digital Workplace Technology Head). Every day in under 45 seconds, we break down high-IQ Artificial Intelligence concepts into clear, practical intuition for creators, developers, and enterprise leaders.\n\n"
            "🔔 SUBSCRIBE to @iamsaravofficial to master AI one byte at a time!\n"
            "🌐 Projects, Architecture Blueprints & Masterclass: https://iamsaravofficial.com\n"
            "💬 Connect with Sarav on LinkedIn & explore the zero-cost open-source AI stack.\n"
            "───────────────\n\n"
            "#shorts #ai #artificialintelligence #learnai #aisafety #rlhf #responsibleai #sigmabyte #saravxai #100daysofai #techtips"
        ),
        "hashtags": "#shorts #ai #artificialintelligence #learnai #aisafety #rlhf #responsibleai #sigmabyte #saravxai #100daysofai #techtips",
        "playlist_url": ""
    },
    {
        "id": "cluster_07",
        "cluster_num": 7,
        "cluster_title": "Cluster 7: Enterprise AI & Tools (Ep 61–70)",
        "episodes_range": "Ep 61–70",
        "title": "100 Days of Learning AI 👉 Cluster 7: Enterprise AI & Tools (Ep 61–70) | Sigma Byte",
        "description": (
            "Master Enterprise AI & Digital Workplace Automation in 10 bite-sized high-IQ episodes! 💡\n\n"
            "Why do 80% of enterprise AI pilots fail? In this cluster, Enterprise AI Architect Sarav unpacks how real companies deploy AI at scale — from AI coding copilots and autonomous background workflows to calculating true AI ROI, mitigating vendor lock-in, and mastering change management.\n\n"
            "🧠 WHAT YOU WILL LEARN IN THIS CLUSTER:\n"
            "• Day 61: AI Copilots — Why Every App Is Getting an AI Sidekick\n"
            "• Day 62: No Code AI — Build an AI App Without Writing Code\n"
            "• Day 63: Enterprise AI — Why Big Companies Are Slower to Use AI Than You Think\n"
            "• Day 64: AI Automation — AI Doing Your Repetitive Tasks While You Sleep\n"
            "• Day 65: AI Customer Support — Why That Chat Support Might Be AI, Not Human\n"
            "• Day 66: AI Code Assistants — How AI Writes Half Your Code Now\n"
            "• Day 67: AI Governance — The Rulebook Companies Need Before Using AI\n"
            "• Day 68: AI ROI — How Companies Know If AI Is Actually Worth It\n"
            "• Day 69: AI Change Management — Why AI Rollouts Fail Even With Great Tech\n"
            "• Day 70: Vendor Lock-in — The Hidden Cost of Betting on One AI Provider\n\n"
            "───────────────\n"
            "🎯 ABOUT THIS SERIES:\n"
            "Welcome to '100 Days of Learning AI' with Sarav (Enterprise AI Architect & Digital Workplace Technology Head). Every day in under 45 seconds, we break down high-IQ Artificial Intelligence concepts into clear, practical intuition for creators, developers, and enterprise leaders.\n\n"
            "🔔 SUBSCRIBE to @iamsaravofficial to master AI one byte at a time!\n"
            "🌐 Projects, Architecture Blueprints & Masterclass: https://iamsaravofficial.com\n"
            "💬 Connect with Sarav on LinkedIn & explore the zero-cost open-source AI stack.\n"
            "───────────────\n\n"
            "#shorts #ai #artificialintelligence #learnai #enterpriseai #aicopilot #automation #sigmabyte #saravxai #100daysofai #techtips"
        ),
        "hashtags": "#shorts #ai #artificialintelligence #learnai #enterpriseai #aicopilot #automation #sigmabyte #saravxai #100daysofai #techtips",
        "playlist_url": ""
    },
    {
        "id": "cluster_08",
        "cluster_num": 8,
        "cluster_title": "Cluster 8: Model Architecture & Training (Ep 71–80)",
        "episodes_range": "Ep 71–80",
        "title": "100 Days of Learning AI 👉 Cluster 8: Model Architecture & Training (Ep 71–80) | Sigma Byte",
        "description": (
            "Master Model Architecture & High-Performance Training in 10 bite-sized high-IQ episodes! 💡\n\n"
            "Step behind the API curtain and discover how state-of-the-art models are trained and compressed. Explore LoRA fine-tuning on a consumer laptop, 4-bit quantization, Mixture of Experts (MoE) routing, knowledge distillation, and synthetic data flywheels.\n\n"
            "🧠 WHAT YOU WILL LEARN IN THIS CLUSTER:\n"
            "• Day 71: Fine-tuning — Teaching AI YOUR Specific Knowledge & Tone\n"
            "• Day 72: LoRA — Train AI on a Laptop With 1% of the Weights: LoRA\n"
            "• Day 73: Quantization — How to Shrink Giant AI Models to Phone Size\n"
            "• Day 74: Mixture of Experts — Why Modern AI Uses Multiple Mini-Brains: MoE\n"
            "• Day 75: Knowledge Distillation — How Giant AI Models Teach Pocket SLMs\n"
            "• Day 76: Scaling Laws — The Secret Equation That Predicts How Smart AI Gets\n"
            "• Day 77: Pretraining — The 2 Training Steps Every AI Goes Through\n"
            "• Day 78: Synthetic Data — Can AI Train AI Without Human Data? Synthetic Sets\n"
            "• Day 79: Model Distillation — Cutting Token Bills by 90% With Distilled Models\n"
            "• Day 80: Sparse Models — How Sparse Models Save Massive Computing Power\n\n"
            "───────────────\n"
            "🎯 ABOUT THIS SERIES:\n"
            "Welcome to '100 Days of Learning AI' with Sarav (Enterprise AI Architect & Digital Workplace Technology Head). Every day in under 45 seconds, we break down high-IQ Artificial Intelligence concepts into clear, practical intuition for creators, developers, and enterprise leaders.\n\n"
            "🔔 SUBSCRIBE to @iamsaravofficial to master AI one byte at a time!\n"
            "🌐 Projects, Architecture Blueprints & Masterclass: https://iamsaravofficial.com\n"
            "💬 Connect with Sarav on LinkedIn & explore the zero-cost open-source AI stack.\n"
            "───────────────\n\n"
            "#shorts #ai #artificialintelligence #learnai #lora #quantization #moe #machinelearning #sigmabyte #saravxai #100daysofai #techtips"
        ),
        "hashtags": "#shorts #ai #artificialintelligence #learnai #lora #quantization #moe #machinelearning #sigmabyte #saravxai #100daysofai #techtips",
        "playlist_url": ""
    },
    {
        "id": "cluster_09",
        "cluster_num": 9,
        "cluster_title": "Cluster 9: AI Trends & Buzzwords (Ep 81–90)",
        "episodes_range": "Ep 81–90",
        "title": "100 Days of Learning AI 👉 Cluster 9: AI Trends & Buzzwords (Ep 81–90) | Sigma Byte",
        "description": (
            "Master AI Trends, Frontier Systems & Token Economics in 10 bite-sized high-IQ episodes! 💡\n\n"
            "Cut through the industry hype and understand the real engineering defining frontier AI. From Artificial General Intelligence (AGI) timelines and emergent abilities to on-device edge execution, prompt caching tokenomics, and universal agent standards.\n\n"
            "🧠 WHAT YOU WILL LEARN IN THIS CLUSTER:\n"
            "• Day 81: AGI — What Happens When AI Matches Human Intelligence?\n"
            "• Day 82: Emergent Abilities — AI Skills That Just... Appear Out of Nowhere\n"
            "• Day 83: Frontier Models — The 'Latest and Greatest' AI You Keep Hearing About\n"
            "• Day 84: Open Source AI — Should AI Models Be Free for Everyone to See?\n"
            "• Day 85: On-device AI — Why Your Phone Might Not Need the Internet for AI Soon\n"
            "• Day 86: AI Agents Economy — Are AI Agents About to Get Their Own Jobs?\n"
            "• Day 87: Local LLMs — Run a Full AI Model Without the Internet\n"
            "• Day 88: Context Caching — How AI Apps Got Cheaper AND Faster\n"
            "• Day 89: MCP — Why Every AI Company Is Suddenly Adopting ONE Standard\n"
            "• Day 90: AI Model Names — Why AI Models Have Such Weird, Epic Names\n\n"
            "───────────────\n"
            "🎯 ABOUT THIS SERIES:\n"
            "Welcome to '100 Days of Learning AI' with Sarav (Enterprise AI Architect & Digital Workplace Technology Head). Every day in under 45 seconds, we break down high-IQ Artificial Intelligence concepts into clear, practical intuition for creators, developers, and enterprise leaders.\n\n"
            "🔔 SUBSCRIBE to @iamsaravofficial to master AI one byte at a time!\n"
            "🌐 Projects, Architecture Blueprints & Masterclass: https://iamsaravofficial.com\n"
            "💬 Connect with Sarav on LinkedIn & explore the zero-cost open-source AI stack.\n"
            "───────────────\n\n"
            "#shorts #ai #artificialintelligence #learnai #agi #localai #tokenomics #mcp #sigmabyte #saravxai #100daysofai #techtips"
        ),
        "hashtags": "#shorts #ai #artificialintelligence #learnai #agi #localai #tokenomics #mcp #sigmabyte #saravxai #100daysofai #techtips",
        "playlist_url": ""
    },
    {
        "id": "cluster_10",
        "cluster_num": 10,
        "cluster_title": "Cluster 10: Practical AI Skills (Ep 91–100)",
        "episodes_range": "Ep 91–100",
        "title": "100 Days of Learning AI 👉 Cluster 10: Practical AI Skills (Ep 91–100) | Sigma Byte",
        "description": (
            "Master Practical 10x AI Workflows in 10 bite-sized high-IQ episodes! 💡\n\n"
            "The grand finale of the 100-Day Curriculum. Transition from conceptual understanding to raw daily productivity superpowers. Learn how to use AI for high-velocity research, automated coding, dynamic spreadsheet analysis, automated email triage, and accelerated self-learning.\n\n"
            "🧠 WHAT YOU WILL LEARN IN THIS CLUSTER:\n"
            "• Day 91: AI Skills — This Skill Could Be as Valuable as Coding Soon\n"
            "• Day 92: AI Note Taking — Turn Messy Notes Into Organized Summaries Instantly\n"
            "• Day 93: AI Coding — Write Code 10x Faster With This Workflow\n"
            "• Day 94: AI Email — Never Stare at a Blank Email Again\n"
            "• Day 95: AI Research — Turn Hours of Research Into Minutes\n"
            "• Day 96: AI Data Analysis — Ask Your Spreadsheet Questions in Plain English\n"
            "• Day 97: AI Presentations — Turn a Rough Outline Into Full Slides\n"
            "• Day 98: AI Learning — Your Personal Tutor Is Now Available 24/7\n"
            "• Day 99: AI Productivity — 5 Tasks You're Still Doing Manually (Stop That)\n"
            "• Day 100: AI Tools — Stop Using ONE AI for Everything\n\n"
            "───────────────\n"
            "🎯 ABOUT THIS SERIES:\n"
            "Welcome to '100 Days of Learning AI' with Sarav (Enterprise AI Architect & Digital Workplace Technology Head). Every day in under 45 seconds, we break down high-IQ Artificial Intelligence concepts into clear, practical intuition for creators, developers, and enterprise leaders.\n\n"
            "🔔 SUBSCRIBE to @iamsaravofficial to master AI one byte at a time!\n"
            "🌐 Projects, Architecture Blueprints & Masterclass: https://iamsaravofficial.com\n"
            "💬 Connect with Sarav on LinkedIn & explore the zero-cost open-source AI stack.\n"
            "───────────────\n\n"
            "#shorts #ai #artificialintelligence #learnai #aiproductivity #aicoding #10xengineer #sigmabyte #saravxai #100daysofai #techtips"
        ),
        "hashtags": "#shorts #ai #artificialintelligence #learnai #aiproductivity #aicoding #10xengineer #sigmabyte #saravxai #100daysofai #techtips",
        "playlist_url": ""
    },
    {
        "id": "master_umbrella",
        "cluster_num": 0,
        "cluster_title": "Master Series: Complete 100-Day Curriculum",
        "episodes_range": "Ep 01–100",
        "title": "100 Days of Learning AI | Complete Curriculum (Episodes 01–100) — Sarav × AI",
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
        "playlist_url": ""
    }
]

catalog["sarav_playlists"] = playlists_data
print("Added sarav_playlists to catalog successfully.")

with open(CATALOG_PATH, "w", encoding="utf-8") as f:
    f.write(prefix + json.dumps(catalog, indent=2, ensure_ascii=False) + ";\n")

print(f"Catalog saved to {CATALOG_PATH} with {len(catalog['sarav_ai'])} Sarav AI episodes and {len(catalog['sarav_playlists'])} Playlists!")
