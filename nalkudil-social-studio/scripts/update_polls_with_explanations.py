import json
import os

CATALOG_PATH = r"D:\Websites\nalkudilstudio.github.io\nalkudil-social-studio\catalog.js"
INDEX_PATH = r"D:\Websites\nalkudilstudio.github.io\nalkudil-social-studio\index.html"

with open(CATALOG_PATH, "r", encoding="utf-8") as f:
    raw = f.read()

prefix = "window.PUBLISHING_CATALOG = "
json_str = raw.replace(prefix, "").rstrip(";\n ")
catalog = json.loads(json_str)

# Curated Explanations for episodes
EXPLANATIONS_DB = {
    1: "Spot on if you picked Option C! 🎯 LLMs do not see human words or letters. Text is segmented into sub-word numerical tokens (roughly 4 characters or 0.75 words each). This is why models can write complex code but sometimes miscount the number of 'r's in strawberry.",
    2: "Spot on if you picked Option B! 🎯 Every LLM has a finite context window budget. When conversation tokens exceed this threshold, the model drops early message history to accommodate new inputs, causing it to appear forgetful.",
    3: "Spot on if you picked Option B! 🎯 High-dimensional embeddings map conceptual relationships mathematically. Words sharing semantic contexts cluster together geometrically, enabling vector databases to perform similarity search.",
    4: "Spot on if you picked Option B! 🎯 The 2017 Transformer architecture introduced Self-Attention, allowing models to process tokens in parallel while calculating relevance weights across the entire sequence.",
    5: "Spot on if you picked Option C! 🎯 LLMs are probabilistic autoregressive predictors. At each step, they compute probability distributions over the vocabulary to sample the most likely next token based on context.",
    6: "Spot on if you picked Option B! 🎯 Temperature scales the logits before the softmax layer. Temperature 0.0 forces greedy deterministic output, while temperature 0.8+ flattens the distribution for creative variation.",
    7: "Spot on if you picked Option B! 🎯 Hallucinations occur because models optimize for plausible statistical token continuations rather than database truth. Without external grounding (RAG), plausibility overrides factual accuracy.",
    8: "Spot on if you picked Option B! 🎯 Few-Shot Prompting conditions the in-context attention heads with 2–3 input/output exemplars, enabling the model to infer desired formatting and reasoning steps with zero parameter updates.",
    9: "Spot on if you picked Option B! 🎯 'Think step by step' triggers Chain-of-Thought reasoning. By allocating dedicated tokens to intermediate reasoning steps, the transformer avoids compressing complex logic into a single forward pass.",
    10: "Spot on if you picked Option B! 🎯 The System Prompt sits at the root of the context window with highest conversational priority, defining persona boundaries, safety guardrails, and deterministic rules before user input is evaluated.",
    11: "Spot on if you picked Option B! 🎯 Enforcing structured JSON schemas turns freeform natural language into machine-parsable, deterministic data suitable for database ingestion and downstream API workflows.",
    12: "Spot on if you picked Option B! 🎯 Prompt Chaining decomposes multi-step goals into sequential sub-prompts where the validated output of Step A becomes the input of Step B, drastically reducing compounding hallucinations.",
    13: "Spot on if you picked Option B! 🎯 The RCTF framework (Role, Context, Task, Format) grounds every prompt with explicit persona steering, environmental context, core task objective, and strict output schema.",
    14: "Spot on if you picked Option B! 🎯 Meta-Prompting uses an advanced reasoning model to draft, critique, and optimize prompt specifications for smaller target models, eliminating trial-and-error manual phrasing.",
    15: "Spot on if you picked Option A! 🎯 Negative Prompting explicitly defines what the AI must NOT say or do. Banning corporate clichés and filler adjectives forces the model to focus on substantive, high-density facts.",
    16: "Spot on if you picked Option B! 🎯 Prompt Injection exploits the boundary ambiguity between instructions and data in LLMs, allowing untrusted user text to override system-level safety rules.",
    17: "Spot on if you picked Option B! 🎯 Markdown delimiters (`###`, `---`, ````) create distinct syntactic boundaries, helping transformer attention heads segment instructions from variable data payloads.",
    18: "Spot on if you picked Option B! 🎯 Directional Stimulus Prompting injects lightweight keyword hints into the prompt to steer the reasoning trajectory toward key concepts without hardcoding full answers.",
    19: "Spot on if you picked Option B! 🎯 Self-Refinement loops prompt the model to critique its own draft against predefined criteria, fixing subtle logical errors before delivering the final output.",
    20: "Spot on if you picked Option B! 🎯 Because tokenizers group character sequences into token IDs, models lack direct byte-level awareness unless prompts explicitly force character-level decomposition.",
    21: "Spot on if you picked Option B! 🎯 RAG (Retrieval-Augmented Generation) injects external private data into prompt context at runtime, providing factual accuracy without costly fine-tuning.",
    22: "Spot on if you picked Option B! 🎯 Vector databases perform nearest-neighbor searches in semantic embedding space, finding conceptual relevance even when queries share zero keywords with documents.",
    23: "Spot on if you picked Option B! 🎯 Chunking splits large documents into semantically coherent passages. Recursive splitting preserves paragraph context while keeping passages within optimal embedding sizes.",
    24: "Spot on if you picked Option B! 🎯 The 'Lost in the Middle' effect shows that LLM attention heads recall information at the extreme edges of huge context windows far better than information buried in the middle.",
    25: "Spot on if you picked Option B! 🎯 Cosine similarity measures the cosine of the angle between two normalized vectors in multi-dimensional space, capturing orientation and semantic alignment regardless of magnitude.",
    26: "Spot on if you picked Option B! 🎯 Cross-encoder rerankers jointly evaluate query-document pairs, providing high-precision scoring on top vector search candidates to eliminate false positives.",
    27: "Spot on if you picked Option B! 🎯 Knowledge grounding constrains the LLM to answer strictly from retrieved context passages and supply verifiable citations, preventing ungrounded speculation.",
    28: "Spot on if you picked Option B! 🎯 Hybrid search combines dense vector retrieval (semantic understanding) with sparse BM25 keyword matching (exact codes, SKUs, and names) for maximum retrieval recall.",
    29: "Spot on if you picked Option B! 🎯 Dynamic Context Injection pulls real-time session state from a lightweight cache (like Redis) into prompt context on demand without storing bulky chat histories.",
    30: "Spot on if you picked Option B! 🎯 Semantic caching stores previous query embeddings and pre-generated responses, returning instant answers for semantically equivalent queries and cutting token costs.",
    31: "Spot on if you picked Option B! 🎯 Unlike conversational chatbots, AI agents can plan multi-step workflows, call external tools/APIs, observe environment feedback, and persist until tasks are solved.",
    32: "Spot on if you picked Option B! 🎯 Function calling enables models to output valid JSON arguments to trigger external tools, database queries, and code execution environments reliably.",
    33: "Spot on if you picked Option B! 🎯 Multi-agent squads divide complex objectives among specialist agents (e.g. Researcher, Coder, Reviewer), reducing context bloat and compounding reasoning errors.",
    34: "Spot on if you picked Option B! 🎯 Persistent agent memory stores facts, user preferences, and intermediate state across sessions, allowing agents to maintain long-term context indefinitely.",
    35: "Spot on if you picked Option B! 🎯 The ReAct framework alternates between Thought (reasoning), Action (tool calling), and Observation (environment feedback) until a termination condition is reached.",
    36: "Spot on if you picked Option B! 🎯 An Agent Orchestrator acts as the central supervisor, decomposing high-level tasks into sub-tasks, routing them to specialist workers, and synthesizing the final output.",
    37: "Spot on if you picked Option B! 🎯 Autonomous planning constructs dynamic task graphs (DAGs) with dependency ordering, allowing agents to execute prerequisites before triggering subsequent actions.",
    38: "Spot on if you picked Option B! 🎯 Anthropic's Model Context Protocol (MCP) acts as the universal USB-C standard for AI. Instead of custom integrations for every model, one MCP server connects any client (Claude, Cursor, Antigravity) to your tools and databases.",
    39: "Spot on if you picked Option B! 🎯 'Vibe checks' fail in production because prompt changes often fix one edge case while silently breaking twenty others. Automated evaluations in CI/CD track benchmark metrics and prevent regressions.",
    40: "Spot on if you picked Option 2! 🎯 Pinging frontier cloud models for basic classification, data formatting, or embeddings adds network latency and high API costs. Quantized SLMs (like Phi-4-mini or Qwen 3B) running on local NPUs deliver sub-10ms response times with zero token bills and complete on-device privacy.",
    41: "Spot on if you picked CLIP! 🎯 CLIP (Contrastive Language-Image Pretraining) projects text prompts and images into a shared semantic latent space, providing the mathematical coordinates that guide diffusion models to synthesize matching pixels.",
    42: "Spot on if you picked Spatiotemporal latent patches! 🎬 Modern AI video world models (like Sora and Veo) treat video as a 4D spacetime volume, maintaining physical continuity, lighting, and object permanence across consecutive frames.",
    43: "Spot on if you picked converting spectrograms into sound waves! 🎙️ Modern zero-shot TTS models use flow matching to generate intermediate acoustic mel-spectrograms. The neural vocoder (like Vocos or HiFi-GAN) is the high-speed engine that decodes those latents into continuous 24kHz studio audio waves.",
    44: "Spot on if you picked reverse U-Net denoising! 🎨 Diffusion models start with pure Gaussian static and iteratively subtract predicted noise across 25–30 steps, transforming television static into photorealistic imagery guided by text latents.",
    45: "Spot on if you picked 3D Facial Blendshapes! 👤 Neural avatars track 3D Facial Action Coding System (FACS) blendshapes. By predicting rotation vectors and expression coefficients, the model deforms a 2D source portrait into natural lip-sync without full 3D mesh rendering.",
    46: "Spot on if you picked matching acoustic latent embeddings! 🎙️ Zero-shot models like F5-TTS extract vocal timbre, pitch distribution, and breath prosody into a compressed speaker embedding vector, synthesizing speech in that vocal signature without retraining weights.",
    47: "Spot on if you picked dual-stream diffusion! 🎵 Frontier AI music models run multi-stream diffusion across time-frequency representations, concurrently modeling harmonic progressions, percussion transients, and vocal phonemes.",
    48: "Spot on if you picked hallucinating texture priors! 🖼️ Unlike basic bilinear stretching which blurs edges, Generative Super-Resolution predicts plausible high-frequency textures (skin pores, fabric weaves, iris details) consistent with the real-world semantics of the scene.",
    49: "Spot on if you picked early fusion in a shared token space! 🧠 Native multimodal models (like Gemini) process text, audio, and pixel patches within one unified transformer architecture, eliminating the translation lag and context loss of tool-stitched pipelines.",
    50: "Spot on if you picked CNN feature map separation! 🎨 Deep Convolutional Neural Networks separate content representations (high-level feature maps) from artistic style representations (Gram matrices of spatial correlations), allowing style transfer without altering object geometry."
}

# Update catalog.js
updated_count = 0
for item in catalog.get("sarav_ai", []):
    ep = item.get("episode")
    if "poll" in item:
        exp = EXPLANATIONS_DB.get(ep, f"Spot on! In '{item.get('concept', '')}', mastering this architectural mechanic ensures high efficiency, minimal latency, and zero hallucination risk.")
        item["poll"]["explanation"] = exp
        # Append explanation to full_text for complete copy
        base_full = item["poll"].get("full_text", "")
        if "💡 EXPLANATION:" not in base_full:
            item["poll"]["full_text"] = base_full + f"\n\n💡 EXPLANATION:\n{exp}"
        updated_count += 1

with open(CATALOG_PATH, "w", encoding="utf-8") as f:
    f.write(prefix + json.dumps(catalog, indent=2, ensure_ascii=False) + ";\n")

print(f"Updated {updated_count} episodes in catalog.js with detailed explanations!")

# Now update index.html to make poll text bigger and render the Explanation Box with 1-click copy
with open(INDEX_PATH, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update copyCardField to support poll_explanation
if "case 'poll_explanation':" not in html:
    target = "case 'poll_options':"
    replacement = """case 'poll_explanation':
          text = (item.poll && item.poll.explanation) ? item.poll.explanation : '';
          label = 'Quiz Explanation';
          break;
        case 'poll_options':"""
    assert target in html
    html = html.replace(target, replacement, 1)
    print("Added poll_explanation case to copyCardField.")

# 2. Update buildSaravAICard poll rendering to make question & options bigger and include Explanation Box
old_poll_box = """              <!-- Community Poll Section with 1-Click Option Buttons -->
              <div class="poll-box" style="margin-top: 8px;">
                <div class="poll-header">
                  <span class="poll-title">🗳️ YouTube Community Poll (≤ 80 Chars / Option)</span>
                  <button class="btn-copy cyan" style="padding: 4px 10px; font-size: 11px;" onclick="copyCardField('sarav_ai', ${ep}, 'poll_full', this)">📋 Copy Full Poll</button>
                </div>
                <p class="poll-question-text" style="font-size: 13.5px; line-height: 1.45; margin: 4px 0;">${escapeHtml(poll.question || '')}</p>
                <div class="poll-options-list">
                  ${pollOptsHtml}
                </div>
                <div class="poll-actions-row" style="margin-top: 8px; display: flex; gap: 8px; flex-wrap: wrap;">
                  <button class="btn-copy gold" style="font-size: 11.5px; padding: 6px 12px;" onclick="copyCardField('sarav_ai', ${ep}, 'poll_question', this)">📋 Copy Question Only</button>
                  <button class="btn-copy" style="font-size: 11.5px; padding: 6px 12px;" onclick="copyCardField('sarav_ai', ${ep}, 'poll_options', this)">📋 Copy All Options (A-D)</button>
                </div>
              </div>"""

new_poll_box = """              <!-- Community Poll Section with Bigger Text & 1-Click Option/Explanation Buttons -->
              <div class="poll-box" style="margin-top: 10px; padding: 14px; background: rgba(10, 16, 28, 0.95); border: 1px solid rgba(0, 240, 255, 0.35); border-radius: 14px;">
                <div class="poll-header" style="margin-bottom: 8px;">
                  <span class="poll-title" style="font-size: 13px; font-weight: 800; color: var(--cyan); letter-spacing: 0.6px;">🗳️ YouTube Community Poll (≤ 80 Chars / Option)</span>
                  <button class="btn-copy cyan" style="padding: 5px 12px; font-size: 12px; font-weight: 700;" onclick="copyCardField('sarav_ai', ${ep}, 'poll_full', this)">📋 Copy Full Poll Packet</button>
                </div>
                
                <!-- Bigger Question Text -->
                <p class="poll-question-text" style="font-size: 15px; font-weight: 700; line-height: 1.5; color: #FFFFFF; margin: 6px 0 10px 0;">${escapeHtml(poll.question || '')}</p>
                
                <!-- Bigger Options List with 1-Click Copy -->
                <div class="poll-options-list" style="gap: 6px;">
                  ${pollOptsHtml}
                </div>
                
                <div class="poll-actions-row" style="margin-top: 10px; display: flex; gap: 8px; flex-wrap: wrap;">
                  <button class="btn-copy gold" style="font-size: 12px; padding: 6px 14px; font-weight: 700;" onclick="copyCardField('sarav_ai', ${ep}, 'poll_question', this)">📋 Copy Question Only</button>
                  <button class="btn-copy" style="font-size: 12px; padding: 6px 14px;" onclick="copyCardField('sarav_ai', ${ep}, 'poll_options', this)">📋 Copy All Options (A-D)</button>
                </div>

                <!-- Explanation Box with 1-Click Copy (Matches YouTube Quiz Format) -->
                ${poll.explanation ? `
                <div class="poll-explanation-box" style="background: rgba(16, 185, 129, 0.08); border-left: 3px solid #10B981; border-radius: 8px; padding: 12px 14px; margin-top: 12px;">
                  <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                    <span style="font-size: 11.5px; font-weight: 800; color: #10B981; text-transform: uppercase; letter-spacing: 0.5px; display: flex; align-items: center; gap: 6px;">
                      💡 YouTube Quiz Explanation
                    </span>
                    <button class="btn-copy" style="background: rgba(16, 185, 129, 0.22); border-color: rgba(16, 185, 129, 0.5); color: #6EE7B7; padding: 4px 12px; font-size: 11.5px; font-weight: 700; min-height: 26px;" onclick="copyCardField('sarav_ai', ${ep}, 'poll_explanation', this)">
                      📋 Copy Explanation
                    </button>
                  </div>
                  <p style="font-size: 13.5px; line-height: 1.5; color: #E2E8F0; margin: 0; font-weight: 500;">${escapeHtml(poll.explanation)}</p>
                </div>
                ` : ''}
              </div>"""

# Also update the opt item style in buildSaravAICard to be bigger
old_opt_code = """          <div class="poll-opt-item ${isCorrect ? 'correct' : ''}" style="display: flex; justify-content: space-between; align-items: center; gap: 8px; margin-bottom: 4px; padding: 6px 10px;">
            <span style="flex: 1; line-height: 1.35;">
              <b>${optChar})</b> ${escapeHtml(opt)} 
              ${isCorrect ? '<span style="color: #10B981; font-weight: 700; margin-left: 4px;">✓ (Key)</span>' : ''}
              <span style="font-size: 10px; color: ${isTooLong ? '#EF4444' : '#64748B'}; margin-left: 6px; font-weight: 500;">(${charCount}/80 chars)</span>
            </span>
            <button class="btn-copy" style="padding: 3px 8px; font-size: 11px; min-height: 26px; white-space: nowrap;" onclick="copyCardField('sarav_ai', ${ep}, 'poll_opt_${i}', this)">
              📋 Copy ${optChar}
            </button>
          </div>"""

new_opt_code = """          <div class="poll-opt-item ${isCorrect ? 'correct' : ''}" style="display: flex; justify-content: space-between; align-items: center; gap: 10px; margin-bottom: 5px; padding: 8px 12px; font-size: 13.5px; background: rgba(255, 255, 255, 0.05); border-radius: 8px;">
            <span style="flex: 1; line-height: 1.4; color: #F1F5F9;">
              <b style="color: var(--gold);">${optChar})</b> ${escapeHtml(opt)} 
              ${isCorrect ? '<span style="color: #10B981; font-weight: 800; margin-left: 6px;">✓ (Key)</span>' : ''}
              <span style="font-size: 11px; color: ${isTooLong ? '#EF4444' : '#94A3B8'}; margin-left: 8px; font-weight: 600;">(${charCount}/80 chars)</span>
            </span>
            <button class="btn-copy" style="padding: 4px 10px; font-size: 11.5px; font-weight: 700; min-height: 28px; white-space: nowrap;" onclick="copyCardField('sarav_ai', ${ep}, 'poll_opt_${i}', this)">
              📋 Copy ${optChar}
            </button>
          </div>"""

assert old_opt_code in html, "old_opt_code not found"
html = html.replace(old_opt_code, new_opt_code, 1)

assert old_poll_box in html, "old_poll_box not found"
html = html.replace(old_poll_box, new_poll_box, 1)

with open(INDEX_PATH, "w", encoding="utf-8") as f:
    f.write(html)

print("Updated index.html with bigger poll text & explanation box successfully!")
