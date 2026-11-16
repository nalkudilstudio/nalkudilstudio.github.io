import json
from smart_trim import smart_trim

def get_community_polls():
    polls = {}

    # Helper to create poll
    def add(day, concept, q_body, options, correct_idx, expl_body):
        q = f"In Day {day} on {concept}, {q_body}?"
        assert len(options) == 3, f"Day {day} must have exactly 3 options"
        trimmed_options = []
        for i, opt in enumerate(options):
            trimmed = smart_trim(opt, 75)
            assert len(trimmed) <= 75, f"Day {day} option {i+1} exceeds 75 chars ({len(trimmed)} chars): '{trimmed}'"
            trimmed_options.append(trimmed)
        assert 0 <= correct_idx < 3, f"Day {day} invalid correct_idx {correct_idx}"
        
        next_day = day + 1 if day < 100 else 1
        expl = (
            f"Spot on if you picked Option {correct_idx + 1}! 🎯 {expl_body}\n\n"
            f"📌 Bookmark the '100 Days of Learning AI' playlist & subscribe to @iamsaravofficial — "
            f"Day {next_day} drops tomorrow at 6 PM! 🚀"
        )
        polls[day] = {
            "question": q,
            "options": trimmed_options,
            "correct_index": correct_idx,
            "explanation": expl
        }

    # ==================== CLUSTER 1: LLM Fundamentals (Days 1-10) ====================
    add(1, "Tokens", "why does an LLM count tokens instead of raw character strings",
        ["Tokens represent statistical sub-word chunks optimized via BPE encoding",
         "LLMs convert whole dictionary words into raw ASCII hex byte streams",
         "Tokens are fixed 4-character blocks hardcoded for English syntax"],
        0, "LLMs use Byte-Pair Encoding (BPE) or WordPiece algorithms to compress vocabularies into frequent sub-word tokens, balancing sequence length and vocabulary size.")

    add(2, "Context Window", "what happens when prompt length exceeds model context capacity",
        ["Early tokens are evicted or truncated, causing loss of initial premises",
         "The neural network raises a fatal floating-point overflow exception",
         "The model automatically compresses past tokens into lossless weights"],
        0, "Attention mechanisms compute interactions across tokens inside a fixed window. Exceeding context limits requires sliding-window eviction, retrieval augmentation, or truncation.")

    add(3, "Embeddings", "how do vector spaces represent semantic semantic relationships",
        ["By mapping textual concepts to dense coordinates where proximity denotes meaning",
         "By indexing exact alphabetical matches into relational database B-trees",
         "By counting raw keyword frequencies across an inverted document index"],
        0, "Embeddings convert tokens into multi-dimensional vectors where dot-product or cosine similarity reflects semantic relatedness, placing 'doctor' closer to 'hospital' than 'apple'.")

    add(4, "Transformers", "which architectural innovation eliminated sequential recurrence",
        ["Multi-head self-attention calculating pairwise token relationships in parallel",
         "Recurrent hidden state passing across sequential LSTM memory cells",
         "Convolutional pooling kernels scanning fixed 3x3 receptive text windows"],
        0, "Transformers replaced sequential recurrent passes (RNN/LSTM) with self-attention, allowing all tokens in a prompt to compute pairwise attention scores concurrently.")

    add(5, "Attention Mechanism", "what does the query-key-value dot-product operation achieve",
        ["Dynamically weights token relevance based on semantic compatibility scores",
         "Executes deterministic database joins between user prompts and training data",
         "Normalizes activation layers to prevent gradient explosion during inference"],
        0, "Softmax((Q * K^T) / sqrt(d_k)) * V dynamically determines how much attention every token pays to all preceding tokens across multiple representation subspaces.")

    add(6, "Temperature", "how does temperature scaling affect next-token sampling logits",
        ["Higher temperatures flatten the logit distribution, increasing entropy",
         "Higher temperatures force greedy argmax selection of the top probability",
         "Lower temperatures expand sampling entropy across low-probability tokens"],
        0, "Dividing logits by temperature (T) before softmax flattens probabilities when T > 1 (higher diversity/entropy) and sharpens the top peak when T < 1 (deterministic/greedy).")

    add(7, "Zero-shot Learning", "why can foundation models solve unseen tasks without training",
        ["Massive pretraining teaches generalized task induction and pattern matching",
         "The model performs real-time gradient descent fine-tuning during inference",
         "The inference server retrieves hidden labels from a closed web index"],
        0, "Pretraining on billions of diverse tokens teaches models generalized task induction, enabling zero-shot execution purely by conditioning on instruction semantics.")

    add(8, "Few-Shot Prompting", "how do in-context exemplars steer model response distributions",
        ["Condition model activations on demonstrated input-output schema patterns",
         "Directly modify neural layer weights via backpropagation during execution",
         "Force deterministic rule evaluation by overriding latent attention heads"],
        0, "Few-shot examples provide in-context calibration, showing formatting, reasoning depth, and edge-case handling without altering underlying network weights.")

    add(9, "Chain of Thought", "why does generating intermediate reasoning steps improve accuracy",
        ["Allocates additional transformer compute tokens before final answer decoding",
         "Forces the model to query an external symbolic calculator tool API",
         "Permanently caches verified facts in the transformer hidden memory layers"],
        0, "Chain of Thought allocates more forward passes and autoregressive compute tokens to break complex logic into sequential, verifiable inference steps.")

    add(10, "AI Hallucination", "what architectural reality creates confident false assertions",
        ["Autoregressive next-token prediction prioritizes fluency over factual truth",
         "A faulty hardware cache line in GPU tensor memory misplaces retrieved data",
         "The neural network intentionally invents citations to bypass safety checks"],
        0, "LLMs maximize likelihood of plausible token sequences. Without grounding in authoritative retrieval, high semantic probability does not guarantee factual ground truth.")

    # ==================== CLUSTER 2: Prompt Engineering Mastery (Days 11-20) ====================
    add(11, "System Prompts", "how do system messages differ from standard user turn inputs",
        ["Establish persistent behavioral guardrails and high-priority steerability",
         "Permanently alter the base model parameter weights in cold storage",
         "Bypass tokenization directly into raw floating-point tensor matrices"],
        0, "System instructions provide persistent contextual steering, setting persona, output constraints, and ethical guardrails across multi-turn interactions.")

    add(12, "Prompt Chaining", "why decompose a complex workflow into multiple chained calls",
        ["Reduces cognitive token load and isolates reasoning failures per subtask",
         "Increases model inference temperature to maximize creative reasoning leaps",
         "Combines disparate model architectures into a single GPU compute cluster"],
        0, "Prompt chaining transforms monolithic prompts into verifiable pipelines: extracting data in step 1, evaluating in step 2, and formatting in step 3.")

    add(13, "Role Prompting", "why does assigning an expert persona improve technical outputs",
        ["Prunes activation space toward specialized vocabulary and structured rigor",
         "Unlocks restricted proprietary knowledge vectors locked in model weights",
         "Forces the transformer to search academic arXiv repositories in real time"],
        0, "Role prompting conditions prior token distributions, guiding attention heads toward domain-specific syntax, professional methodologies, and rigorous criteria.")

    add(14, "Few-shot Prompting", "what is the primary failure mode of poorly chosen few-shot examples",
        ["Models overfit to irrelevant superficial biases or label distribution skew",
         "The GPU compiler crashes due to mismatched tensor input dimensions",
         "The transformer permanently writes example errors into global parameters"],
        0, "Models are highly sensitive to majority label bias, recency bias, and formatting noise in few-shot exemplars, requiring balanced, clean demonstrations.")

    add(15, "Negative Prompting", "what is the most reliable way to prevent unwanted output formats",
        ["Explicit positive boundary constraints paired with negative rule exclusions",
         "Repeating 'do not ever' 10 times in all-capital letters in user prompts",
         "Lowering temperature to absolute zero and disabling sampling completely"],
        0, "Clear structural constraints and positive demonstrations ('Respond strictly in JSON') are far more reliable than ambiguous negative prohibitions.")

    add(16, "Prompt Injection", "how do indirect prompt injection attacks exploit LLM design",
        ["Untrusted external data hijacks model instruction flow as system commands",
         "Attackers corrupt model weight tensors stored in cloud model registries",
         "Malicious inputs trigger physical hardware side-channel memory leaks"],
        0, "Indirect injection occurs when untrusted retrieved content (emails, web pages) contains adversarial instructions that the model mistakes for system directives.")

    add(17, "Structured Output", "how do constrained decoding engines (like JSON mode) guarantee schema",
        ["Mask invalid token logits at each step based on context-free grammars",
         "Repeatedly retry generation in a loop until standard text passes regex",
         "Fine-tune the model parameters dynamically on the schema definition"],
        0, "Engines like Outlines and Guidance enforce JSON schemas by applying logit masks during autoregressive decoding, mathematically preventing invalid syntax.")

    add(18, "Meta Prompting", "what is the core technique of recursive meta-prompting",
        ["Using an LLM to iteratively critique, refine, and optimize prompt schemas",
         "Injecting raw Python bytecode into the transformer activation buffers",
         "Hardcoding thousands of static prompt rules into relational databases"],
        0, "Meta-prompting leverages an LLM as an expert prompt engineer, analyzing failure cases and generating optimized system instructions tailored to target models.")

    add(19, "Iterative Prompting", "how should production engineers debug degraded model responses",
        ["Isolate variables via automated test suites against versioned prompt evals",
         "Randomly tweak adjectives in the prompt until one benchmark passes",
         "Immediately fine-tune a 70B parameter model from raw conversational logs"],
        0, "Systematic prompt optimization requires version control, synthetic eval datasets, rubric scoring, and isolating single modifications across test splits.")

    add(20, "Prompt Templates", "why do parameterized prompt templates require strict sanitization",
        ["Unsanitized user variables can break schema syntax or trigger injections",
         "Template engines increase GPU tensor latency by several hundred percent",
         "Parameter interpolation permanently alters the underlying system prompt"],
        0, "User variables injected into templates without validation can corrupt delimiters, break JSON schemas, or alter instruction boundaries.")

    # ==================== CLUSTER 3: RAG & Vector Search (Days 21-30) ====================
    add(21, "Vector Database", "why use approximate nearest neighbor (ANN) instead of exact k-NN",
        ["ANN scales sub-linearly across millions of vectors with 95%+ recall",
         "Exact k-NN produces lower precision embeddings than hierarchical graphs",
         "ANN eliminates the need for vector embeddings by indexing raw text strings"],
        0, "Exact k-NN requires brute-force O(N) distance checks across all vectors. ANN algorithms (HNSW, IVF-PQ) search clustered graphs in logarithmic time.")

    add(22, "Semantic Search", "why does vector search outperform traditional BM25 keyword search",
        ["Captures conceptual synonyms and contextual intent across varied vocabularies",
         "Eliminates the computational overhead of generating neural text embeddings",
         "Guarantees 100% exact keyword matches regardless of spelling mistakes"],
        0, "Semantic search maps meanings into dense embedding space, matching queries like 'cardiac arrest' to documents discussing 'heart attacks' without shared keywords.")

    add(23, "RAG", "what is the primary architectural purpose of a RAG pipeline",
        ["Ground generation in dynamic, authoritative external knowledge bases",
         "Permanently update LLM weights with enterprise proprietary documentation",
         "Compress long user queries into compact 16-bit floating-point tokens"],
        0, "RAG decouples memory from parameter weights, retrieving verified external documents to provide context-grounded, citation-backed answers without retraining.")

    add(24, "Chunking", "why is recursive document chunking superior to naive character splitting",
        ["Respects grammatical boundaries and keeps complete semantic ideas intact",
         "Guarantees that every chunk fits into exactly 128 raw byte boundaries",
         "Eliminates duplicate words across documents before vector embedding passes"],
        0, "Recursive chunking splits on paragraphs, markdown headings, and sentence ends, ensuring complete conceptual units are captured without mid-sentence cuts.")

    add(25, "Embeddings", "which distance metric is standard for normalized dense text vectors",
        ["Cosine similarity, equivalent to dot product on unit-normalized vectors",
         "Manhattan distance (L1 norm) measuring orthogonal grid coordinate offsets",
         "Hamming distance counting bitwise mismatches in uncompressed byte streams"],
        0, "For unit-normalized vectors, cosine similarity simplifies to the dot product, measuring angular alignment rather than magnitude in multi-dimensional space.")

    add(26, "Reranking", "why pair bi-encoder vector search with a cross-encoder reranker",
        ["Bi-encoders enable fast candidate retrieval; cross-encoders assess deep relevance",
         "Cross-encoders index billions of documents in sub-millisecond vector spaces",
         "Bi-encoders perform multi-turn conversational reasoning during search"],
        0, "Bi-encoders retrieve top 50 candidates in milliseconds. Cross-encoders then compute all-to-all cross-attention between query and documents for optimal relevance.")

    add(27, "Knowledge Grounding", "how does strict citation attribution reduce enterprise AI risk",
        ["Forces model outputs to cite verifiable passage chunks from retrieved docs",
         "Guarantees that the underlying model weights cannot produce harmful speech",
         "Encrypts all retrieved documents using enterprise AES-256 key registries"],
        0, "Attribution requires statements to trace back to specific retrieved chunks, allowing automated validators to flag assertions lacking source ground truth.")

    add(28, "Hybrid Search", "why combine dense vector retrieval with sparse lexical BM25 search",
        ["Merges conceptual semantic understanding with exact acronym and part-number matching",
         "Doubles the context window size of the downstream generative LLM model",
         "Replaces external vector databases with lightweight client-side cache stores"],
        0, "Dense embeddings excel at conceptual nuance but miss exact IDs or rare acronyms. Reciprocal Rank Fusion (RRF) combines dense + BM25 scores for optimal recall.")

    add(29, "Context Injection", "how should retrieved context chunks be structured in the prompt",
        ["Clear XML or Markdown delimiters with explicit instructions to prioritize context",
         "Dump raw unformatted text blocks at the very end of the user prompt turn",
         "Encode retrieved passages into hexadecimal strings to save prompt tokens"],
        0, "Structuring retrieved passages in `<context>` blocks with numbered sources and clear instructions helps models separate user instructions from reference data.")

    add(30, "Retrieval Latency", "what is the most effective optimization for reducing RAG query latency",
        ["Semantic caching of frequent query embeddings and hybrid ANN quantization",
         "Increasing embedding dimension size from 1536 to 8192 floating-point values",
         "Running full brute-force exact Euclidean distance scans on every user query"],
        0, "Semantic query caching avoids redundant vector lookups, while Product Quantization (PQ) and HNSW indexing accelerate vector search by 10x with minimal recall loss.")

    # ==================== CLUSTER 4: Agentic AI & Autonomous Systems (Days 31-40) ====================
    add(31, "AI Agents", "what fundamentally separates an autonomous AI agent from a standard chatbot",
        ["Looping reasoning, environmental observation, and dynamic tool execution",
         "A higher parameter count and larger pretraining dataset for conversational flow",
         "The ability to generate responses without using any underlying LLM compute"],
        0, "Chatbots generate single-pass text. AI Agents evaluate objectives, plan actions, invoke external APIs, observe results, and iterate autonomously until completion.")

    add(32, "Tool Use", "how does an LLM invoke external APIs during tool calling",
        ["Generates structured function arguments conforming to an OpenAPI JSON schema",
         "Directly compiles and executes machine assembly code inside the GPU core",
         "Injects raw HTTP packets directly into the host operating system kernel"],
        0, "Models do not execute APIs directly; they output structured JSON representing function calls and arguments, which the host environment executes before returning results.")

    add(33, "Multi-Agent Systems", "why deploy specialized multi-agent squads instead of one general prompt",
        ["Role isolation reduces hallucination and allows specialized tool sandboxing",
         "Running multiple agents concurrently eliminates all cloud API token costs",
         "Single agents are mathematically unable to process more than one API tool"],
        0, "Modular agent teams (Researcher, Coder, Reviewer) keep context windows clean, enforce distinct system roles, and enable granular guardrails and tool access per role.")

    add(34, "Agent Memory", "how do long-running agents persist state across multi-step execution",
        ["Episodic memory stored in external vector stores combined with working scratchpads",
         "Permanently modifying neural weight matrices after every completed task",
         "Relying entirely on infinite transformer context windows without pruning"],
        0, "Agents maintain short-term state in a working scratchpad and long-term episodic experience in indexed databases, retrieving relevant context as tasks unfold.")

    add(35, "ReAct Framework", "what is the sequence of the ReAct (Reason + Act) operational loop",
        ["Thought -> Action -> Observation -> Thought, repeating until task resolution",
         "Action -> Observation -> Feedback -> Retraining, updating base parameters",
         "Prompt -> Inference -> Decoding -> Output, finishing in a single forward pass"],
        0, "ReAct interleaves explicit reasoning traces ('Thought') with external tool calls ('Action') and tool outputs ('Observation'), creating verifiable decision chains.")

    add(36, "Agent Orchestration", "what is the responsibility of a centralized Agent Supervisor",
        ["Routes subtasks, synthesizes specialist outputs, and evaluates termination",
         "Directly executes all low-level bash commands across agent worker nodes",
         "Hardcodes token sampling limits to prevent agents from writing long text"],
        0, "The supervisor functions as an orchestrator, breaking the main user goal into subtasks, delegating to domain agents, resolving deadlocks, and reviewing results.")

    add(37, "Autonomous Planning", "how do agents avoid dead ends when executing complex multi-step plans",
        ["Dynamic plan validation with backtrack replanning upon unexpected tool errors",
         "Executing all plan steps simultaneously in parallel without error checking",
         "Hardcoding step sequences so the agent cannot deviate under any failure"],
        0, "Robust agents evaluate tool return codes; if an execution branch fails, the replanning module updates the remaining task DAG to explore alternative solution paths.")

    add(38, "Model Context Protocol (MCP)", "why is Anthropic's MCP becoming the universal standard for tools",
        ["Provides an open, unified protocol connecting LLMs to diverse data sources",
         "Replaces GPU CUDA kernels with standardized WebAssembly compiler runtimes",
         "Eliminates the requirement for API authentication tokens across cloud tools"],
        0, "MCP replaces fragmented custom tool integrations with a standardized client-server protocol, allowing any LLM to discover and call tools across diverse systems.")

    add(39, "Automated Evals & CI", "why are automated evaluation suites essential before shipping agents",
        ["Measure deterministic accuracy, tool compliance, and regression prevention",
         "Ensure that model inference latency never exceeds 10 milliseconds globally",
         "Eliminate the need for human engineering reviews in enterprise code bases"],
        0, "Agentic workflows can drift or hallucinate tool calls. Automated CI evals test task completion rates, cost ceilings, and boundary constraints on every change.")

    add(40, "Local SLMs on NPUs", "what is the primary operational advantage of running SLMs on device",
        ["Zero cloud API cost, complete data privacy, and ultra-low edge latency",
         "Outperforming frontier 1-trillion parameter cloud models on broad math benchmarks",
         "Infinite context windows capable of storing petabytes of raw video files"],
        0, "Small Language Models (SLMs) running locally on modern NPUs/GPUs guarantee strict privacy (data never leaves device), zero cloud egress bills, and offline availability.")

    # ==================== CLUSTER 5: Multimodal & GenAI Creative (Days 41-50) ====================
    add(41, "Text to Image", "what is the role of text encoders (like CLIP or T5) in image models",
        ["Translate natural language prompts into aligned semantic guidance embeddings",
         "Directly generate the final 2D pixel array without any diffusion steps",
         "Scan the internet for stock photography matching prompt keyword tokens"],
        0, "Text encoders project natural language into a joint multimodal embedding space, providing spatial cross-attention conditioning that guides latent diffusion steps.")

    add(42, "Text to Video", "how do modern world models (like Sora and Veo) maintain temporal consistency",
        ["Treat video as 4D spacetime volumes using spatiotemporal latent patches",
         "Generate isolated 2D image frames sequentially with post-processing filters",
         "Store every raw uncompressed video frame directly in high-speed GPU VRAM"],
        0, "State-of-the-art video world models represent spacetime as 3D/4D latent patches, computing cross-frame attention to enforce object permanence, physics, and lighting.")

    add(43, "Text to Speech", "what is the primary architectural function of a neural vocoder",
        ["Synthesizes raw continuous audio waveforms from acoustic mel-spectrograms",
         "Translates textual language phonemes from English syntax to target idioms",
         "Filters background microphone ambient noise during user audio recording"],
        0, "Acoustic models predict intermediate frequency-time spectrograms. The neural vocoder (e.g. HiFi-GAN, Vocos) synthesizes raw, high-fidelity 24kHz audio waves.")

    add(44, "Diffusion Models", "what occurs during the 30-step iterative denoising phase",
        ["The model adds more random Gaussian noise to obscure the image",
         "The neural network progressively subtracts noise guided by the prompt",
         "The prompt is converted directly into a hardcoded vector without visual math"],
        1, "Diffusion models start with pure random static. Over iterative denoising steps, the network predicts and subtracts noise, revealing crisp, prompt-aligned imagery.")

    # Day 45: Keep exact user-verified sample
    polls[45] = {
        "question": "In Day 45 on AI Avatars, how do digital presenters synchronize realistic lip movements and expressions with a text script?",
        "options": [
            "By recording a live human actor separately for all 40 languages",
            "By manually animating every video frame by hand in 3D software",
            "By mapping audio phonemes to 52 distinct 3D facial blendshapes"
        ],
        "correct_index": 2,
        "explanation": "Spot on if you picked Option 3! 🎯 Modern digital presenters require zero cameras or studio lighting. By pairing neural TTS with 52 distinct 3D facial blendshapes and micro-blinks, pipelines like LivePortrait + F5-TTS map audio phonemes directly onto photorealistic lip movements across 40+ languages in real time.\n\n📌 Bookmark the '100 Days of Learning AI' playlist & subscribe to @iamsaravofficial — Day 46 drops tomorrow at 6 PM! 🚀"
    }

    add(46, "Voice Cloning", "how do zero-shot voice cloning models replicate timbre from 10s of audio",
        ["Extract speaker embeddings into a latent condition space for flow matching",
         "Retrain all transformer attention weights from scratch for the new speaker",
         "Apply aggressive robotic pitch modulation over a generic synthetic voice"],
        0, "Zero-shot engines (like F5-TTS or CosyVoice) extract speaker pitch, formant, and cadence into a compact conditioning embedding, synthesizing speech in that vocal profile.")

    add(47, "AI Music", "how do generative music architectures represent polyphonic harmonic structure",
        ["Tokenize audio into multi-codebook discrete neural acoustic representations",
         "Stitch together thousands of royalty-free MP3 sample clips from hard drive",
         "Convert musical sheet notation directly into raw MIDI synthesizer tracks"],
        0, "Modern music models (like Suno, Udio) use hierarchical neural audio codecs (like EnCodec) that quantize audio into parallel token codebooks representing harmony and vocals.")

    add(48, "Image Upscaling", "why do latent diffusion upscalers produce sharper details than bicubic resizing",
        ["Hallucinate realistic high-frequency textures conditioned on prompt semantics",
         "Interpolate mathematical color averages between neighboring low-res pixels",
         "Download matching high-resolution stock photography assets from web caches"],
        0, "Traditional resizing blurs pixels via interpolation. Diffusion-based super-resolution models synthesize realistic microscopic textures (pores, fabric, foliage).")

    add(49, "Multimodal AI", "how do unified multimodal LLMs ingest both images and text simultaneously",
        ["Project patch embeddings through linear projection layers into LLM token space",
         "Run optical character recognition (OCR) and convert all pixels into text strings",
         "Switch between two completely separate models hosted on separate servers"],
        0, "Vision transformers encode images into spatial patch tokens, which a multimodal projector maps into the text embedding space, allowing unified cross-attention.")

    add(50, "Style Transfer", "how do ControlNet and IP-Adapter preserve structural composition while altering style",
        ["Inject zero-convolution structural guidance locks into diffusion UNet blocks",
         "Apply traditional Photoshop blending filters on top of completed generations",
         "Train a dedicated 50GB foundation model from scratch for each distinct style"],
        0, "ControlNet locks original model weights and trains lightweight trainable copies with zero-convolutions, injecting edge maps, depth, or poses without degrading base quality.")

    # ==================== CLUSTERS 6-10: Days 51-100 ====================
    add(51, "AI Bias", "how does demographic representation imbalance manifest in model outputs",
        ["Skewed probability distributions in pretraining corpora produce stereotypical priors",
         "A software bug in floating-point GPU rounding favor specific text strings",
         "Hardware thermal throttling degrades precision on specific linguistic dialects"],
        0, "Foundation models mirror historical correlation patterns in their training corpora; uncurated data biases generation towards dominant demographic representations.")

    add(52, "AI Alignment", "what is the core goal of aligning frontier foundation models",
        ["Ensuring model behaviors adhere to human values, safety, and helpful intent",
         "Maximizing the raw token throughput speed of the GPU inference server cluster",
         "Preventing open-source developers from inspecting underlying model weights"],
        0, "Alignment steers raw next-token predictors into helpful, harmless, and honest assistants via techniques like RLHF, DPO, and constitutional AI principles.")

    add(53, "RLHF", "how does Reinforcement Learning from Human Feedback guide model behavior",
        ["Trains a reward model on human preferences to optimize policy via PPO/DPO",
         "Forces human annotators to write billions of synthetic training tokens manually",
         "Directly edits individual transformer neural weights using symbolic debuggers"],
        0, "RLHF uses human comparison rankings to train a reward model, which then guides policy optimization (via PPO or direct preference optimization DPO).")

    add(54, "Deepfakes", "which cryptographic method provides tamper-proof media authenticity",
        ["C2PA cryptographic provenance metadata signed by camera hardware keys",
         "Hiding invisible high-frequency watermarks that survive file compression",
         "Relying on manual visual inspection by professional forensic video editors"],
        0, "The C2PA standard embeds verifiable public-key cryptographic provenance signatures into media headers, establishing author, device, and modification history.")

    add(55, "AI Regulation", "how does the EU AI Act classify risk categories for software systems",
        ["Four tiers: Unacceptable risk (banned), High risk, Limited, and Minimal risk",
         "By counting total parameters, banning any model exceeding 10 billion weights",
         "By categorizing models based on whether they use Python or C++ runtime code"],
        0, "The EU AI Act classifies AI by systemic impact: unacceptable systems (social scoring) are banned, high-risk systems face strict audits, and minimal risk systems are unregulated.")

    add(56, "Explainable AI", "why is interpreting deep neural network decision paths challenging",
        ["Billions of non-linear parameter activations create distributed latent states",
         "Model developers deliberately obfuscate matrix weights behind proprietary DRM",
         "Attention mechanisms completely erase intermediate token representations"],
        0, "Knowledge in deep transformers is distributed across millions of overlapping polysemantic neurons and non-linear layers, making single-cause attribution difficult.")

    add(57, "AI Privacy", "how does differential privacy protect individual records during training",
        ["Injects calibrated mathematical noise to prevent extraction of specific rows",
         "Deletes all punctuation marks and vowel characters from the training set",
         "Encrypts training data with private keys that the neural network decrypts"],
        0, "Differential privacy adds bounded mathematical noise during gradient descent, ensuring the inclusion of any individual record cannot be reverse-engineered.")

    add(58, "AI Watermarking", "how does SynthID embed undetectable watermarks in generated media",
        ["Alters probability distributions of sub-perceptual tokens without quality loss",
         "Burns visible semi-transparent logo overlays across the bottom of the video",
         "Appends a static plain-text metadata tag at the end of the raw binary file"],
        0, "Google DeepMind's SynthID modifies sub-perceptual generation distributions during sampling, leaving a persistent statistical signature detectable only by verification keys.")

    add(59, "Model Cards", "what is the primary industry function of an open Model Card",
        ["Document architecture, intended use cases, training datasets, and limitations",
         "Serve as a commercial copyright license restricting competing companies",
         "List the personal contact telephone numbers of all software engineering leads"],
        0, "Model cards provide standardized transparency, outlining intended use, benchmark evals, demographic performance variances, and known failure modes.")

    add(60, "Responsible AI", "what is the purpose of red-teaming frontier AI models before release",
        ["Adversarial stress-testing to surface dangerous failure modes and jailbreaks",
         "Measuring maximum hardware cooling efficiency inside enterprise data centers",
         "Automating the marketing launch cycle to maximize social media impressions"],
        0, "Red-teaming involves adversarial security experts attempting to jailbreak guardrails, trigger toxic outputs, or exploit model vulnerabilities before deployment.")

    # Days 61-100: add high-IQ technical questions
    add(61, "AI Copilots", "what is the core pattern for building enterprise domain copilots",
        ["RAG integration combined with scoped role-based access control (RBAC)",
         "Fine-tuning a monolithic foundation model on uncurated corporate databases",
         "Replacing existing user interface software with a single raw terminal shell"],
        0, "Enterprise copilots require grounded context retrieval constrained by user access tokens, ensuring employees only see information they are permitted to view.")

    add(62, "No Code AI", "what is the architectural limitation of pure no-code AI builder tools",
        ["Limited state management, opaque latency tracing, and vendor tool lock-in",
         "Inability to connect to standard REST APIs or cloud database endpoints",
         "Mathematical incompatibility with transformer attention mechanisms"],
        0, "While rapid for prototypes, no-code platforms obscure error tracing, limit custom token optimization, and create vendor lock-in for complex enterprise flows.")

    add(63, "Enterprise AI", "what is the key metric for measuring enterprise AI business value",
        ["Deflection rate and cycle-time compression balanced against inference costs",
         "Total number of raw prompt queries submitted by non-technical employees",
         "The size in gigabytes of the fine-tuned checkpoint weights file on disk"],
        0, "Enterprise AI success is measured by high-quality automated ticket deflection, human-in-the-loop task acceleration, and maintaining positive unit economics.")

    add(64, "AI Automation", "how should automated workflows handle edge cases and high-risk decisions",
        ["Implement human-in-the-loop escalation gates based on model confidence scores",
         "Force the model to make its best guess regardless of certainty metrics",
         "Silently drop failed transactions without notifying systems administrators"],
        0, "Mission-critical architectures use confidence score thresholds, routing borderline or high-liability decisions to human specialists for verification.")

    add(65, "AI Customer Support", "what prevents enterprise customer support bots from hallucinating terms",
        ["Strict retrieval grounding with negative constraints and citation verification",
         "Training the model to always answer yes to every incoming customer question",
         "Disabling tokenization and streaming raw text files directly to the user"],
        0, "Support bots require deterministic knowledge grounding: answering strictly from verified policy documents and declining to speculate when answers are missing.")

    add(66, "AI Code Assistants", "why do modern code assistants index repository AST syntax trees",
        ["Understand class hierarchies, symbol references, and cross-file dependencies",
         "Compress the entire codebase into a single 16-bit integer token stream",
         "Permanently prevent developers from writing invalid syntax in their editors"],
        0, "Abstract Syntax Trees (AST) allow code copilots to resolve exact variable types, function calls, and import chains across large multi-file repositories.")

    add(67, "AI Governance", "what constitutes a robust enterprise AI governance framework",
        ["Model registries, automated eval gates, usage telemetry, and policy compliance",
         "A single legal document signed by developers promising not to misuse models",
         "Blocking all corporate internet access to external cloud computing providers"],
        0, "Enterprise governance requires end-to-end auditability: tracking model versions, data provenance, red-team benchmarks, and user data privacy enforcement.")

    add(68, "AI ROI", "why do many generative AI proof-of-concepts fail to achieve positive ROI",
        ["Unanticipated token inference costs, high latency, and lack of integration",
         "Open-source models requiring millions of dollars in monthly license fees",
         "Modern GPUs consuming more power than commercial electrical grids can supply"],
        0, "POCs often neglect operational realities: recurring token costs, maintenance of vector DB pipelines, and friction when integrating into legacy enterprise tools.")

    add(69, "AI Change Management", "what is the primary cultural barrier to organizational AI adoption",
        ["Employee fear of obsolescence and lack of continuous workflow training",
         "Hardware limitations preventing modern laptops from accessing web browsers",
         "Enterprise databases being fundamentally unable to store textual records"],
        0, "Technology is rarely the sole blocker; successful transformation requires reskilling employees, transparent communication, and redesigning roles around AI leverage.")

    add(70, "Vendor Lock-in", "how can organizations protect against proprietary model vendor lock-in",
        ["Abstract model calls behind standardized gateways (LiteLLM, OpenRouter, MCP)",
         "Rewrite every internal software application from scratch every six months",
         "Never use any artificial intelligence tools or cloud computing services"],
        0, "Model abstraction gateways standardize API interfaces, allowing seamless routing and failover across OpenAI, Anthropic, Google, and open-source models.")

    add(71, "Fine-tuning", "when should you choose fine-tuning over Retrieval-Augmented Generation",
        ["To adapt model style, specialized syntax, or domain tone rather than facts",
         "Whenever you need to add dynamic, frequently changing product catalogs",
         "To reduce initial engineering setup time from weeks down to a few minutes"],
        0, "RAG is ideal for dynamic knowledge retrieval. Fine-tuning is used to instill specialized formatting, dialect, domain jargon, or classification patterns.")

    add(72, "LoRA", "why is Low-Rank Adaptation (LoRA) dramatically cheaper than full fine-tuning",
        ["Freezes base weights and trains small low-rank adapter decomposition matrices",
         "Deletes 90% of model layers to run training on low-power smartphone chips",
         "Replaces neural backpropagation with simple linear regression calculations"],
        0, "LoRA decomposes weight updates into two small low-rank matrices (A and B), updating less than 1% of parameters while preserving the pre-trained foundation.")

    add(73, "Quantization", "what is the trade-off when quantizing a model from FP16 to 4-bit INT4",
        ["Dramatically reduced VRAM footprint and faster inference with minimal perplexity loss",
         "Increased memory consumption but higher numerical floating-point precision",
         "Complete elimination of all attention mechanisms in favor of lookup tables"],
        0, "Quantization compresses weights from 16-bit floats to 4-bit integers, cutting VRAM requirements by 70%+ so large models fit on consumer GPUs with negligible quality loss.")

    add(74, "Mixture of Experts", "how does a Mixture of Experts (MoE) model achieve high capacity with low compute",
        ["A router dynamically activates only a subset of specialist feedforward experts per token",
         "Every expert neural network processes every single token simultaneously in parallel",
         "The model merges all expert layers into a single small dense neural checkpoint"],
        0, "MoE architectures (like Mixtral or Grok) route each token to top-K experts, giving the model massive parameter capacity while computing only a fraction per forward pass.")

    add(75, "Knowledge Distillation", "how does a small student model learn from a large teacher model",
        ["Trained to match the soft probability distribution logits output by the teacher",
         "Directly copies the top 10% of physical silicon GPU cores from the teacher cluster",
         "Compresses teacher weights into a zip archive and decompresses into memory"],
        0, "Distillation trains a lightweight student model to replicate the rich output probability distribution (dark knowledge) of a massive teacher, retaining high reasoning in a compact size.")

    add(76, "Scaling Laws", "what do Chinchilla scaling laws state regarding optimal compute allocation",
        ["Model parameter count and dataset token volume must scale in equal proportion",
         "Model parameter size should always scale 10x faster than training token volume",
         "Compute should be allocated entirely to increasing attention layer count"],
        0, "DeepMind's Chinchilla demonstrated that for compute-optimal training, parameter count and training token volume should double equally, proving earlier models were undertrained.")

    add(77, "Pretraining", "what objective function drives self-supervised pretraining for causal LLMs",
        ["Autoregressive cross-entropy loss predicting the next token in a sequence",
         "Supervised classification matching input sentences to human-assigned labels",
         "Reinforcement learning maximizing user engagement metrics on social platforms"],
        0, "Causal language models are trained on massive text corpora via self-supervised next-token prediction, minimizing cross-entropy loss without human manual labels.")

    add(78, "Synthetic Data", "what danger arises from recursively training models purely on AI-generated text",
        ["Model collapse: variance shrinks, causing degenerative perceptual loops and hallucinations",
         "The GPU compiler memory corrupts due to synthetic token syntax formatting",
         "Training speeds drop to zero because AI text contains no information entropy"],
        0, "Model collapse occurs when successive generations of models train on synthetic data without fresh human ground truth, eroding the tails of probability distributions.")

    add(79, "Model Distillation", "why are distilled reasoning models (like DeepSeek-R1-Distill) disruptive",
        ["They pack frontier chain-of-thought reasoning into small, cheap consumer checkpoints",
         "They require zero GPU compute and can run directly on 1990s microcontrollers",
         "They eliminate the need for training data by generating answers from pure logic"],
        0, "Distilling reasoning paths from large frontier reasoners into 7B or 14B models democratizes high-IQ problem-solving, making deep logic runnable on local laptops.")

    add(80, "Sparse Models", "how does activation sparsity improve modern transformer efficiency",
        ["Only a small fraction of neurons fire for any given token, saving FLOPs",
         "Deletes zero-value weights permanently from the hard disk storage volume",
         "Limits the dictionary vocabulary to only common everyday English words"],
        0, "By employing sparse activations (such as ReLU thresholding or MoE routing), only relevant pathways compute for each token, cutting power and computational cycles.")

    add(81, "AGI", "what is the consensus benchmark definition of Artificial General Intelligence",
        ["An autonomous system outperforming human capability across economically valuable work",
         "Any computer program that successfully passes a 5-minute text-based Turing test",
         "A robot physically capable of performing complex human household chores"],
        0, "AGI is widely defined by research institutions as highly autonomous software that surpasses human cognitive capabilities across the vast majority of economically valuable tasks.")

    add(82, "Emergent Abilities", "what characterizes an emergent ability in large foundation models",
        ["Capabilities that appear suddenly at scale but are absent in smaller models",
         "Features programmed directly by software engineers into model source code",
         "Hardware improvements that allow graphics cards to run at higher voltages"],
        0, "Emergent abilities are behaviors (like multi-step translation, arithmetic, or symbolic reasoning) that show near-zero accuracy until models reach critical parameter thresholds.")

    add(83, "Frontier Models", "what defines a frontier AI model in contemporary AI engineering",
        ["State-of-the-art models pushing compute boundaries beyond 10^26 FLOPs",
         "Any open-source model available for download on public repositories",
         "Software designed specifically for space exploration and aerospace navigation"],
        0, "Frontier models refer to leading-edge systems at the technological boundary, trained with unprecedented compute, multi-modal reasoning, and autonomous problem-solving capabilities.")

    add(84, "Open Source AI", "why is the rise of open-weight models (like LLaMA and DeepSeek) crucial",
        ["Prevents monopolistic centralized control, ensures auditability, and lowers cost",
         "Guarantees that models can never produce incorrect or hallucinated answers",
         "Allows models to bypass the physical laws of semiconductor power consumption"],
        0, "Open-weight models democratize frontier capabilities, enabling private on-prem deployment, custom architecture modifications, and transparent safety audits.")

    add(85, "On-device AI", "what hardware accelerator enables real-time LLM inference on modern laptops",
        ["Neural Processing Units (NPUs) and unified high-bandwidth memory architectures",
         "Standard spinning mechanical hard drives with high-speed read/write heads",
         "External cloud server arrays connected via 5G cellular wireless modems"],
        0, "Dedicated NPUs paired with high-bandwidth unified memory allow modern devices to run quantized models locally at 30+ tokens/second without draining battery.")

    add(86, "AI Agents Economy", "what infrastructure will power autonomous economic transactions between agents",
        ["Machine-readable cryptographic micropayments and programmatic API service contracts",
         "Physical plastic credit cards handed between robotic mechanical actuators",
         "Human accountants manually approving every single 10-cent API transaction"],
        0, "Autonomous agent economies will rely on programmatic micropayments, zero-knowledge identity proofs, and automated smart service contracts executing at machine speed.")

    add(87, "Local LLMs", "what open-source framework is the standard for running local models on desktop",
        ["Ollama and llama.cpp compiling optimized GGUF quantization runtimes",
         "Proprietary cloud containers streaming responses from remote datacenters",
         "Raw text editors interpreting Python code scripts line-by-line in real time"],
        0, "Ollama and llama.cpp leverage optimized C++ and Metal/CUDA kernels to run GGUF-quantized models effortlessly across consumer macOS, Windows, and Linux hardware.")

    add(88, "Context Caching", "how does prompt context caching slash enterprise API costs by up to 90%",
        ["Reuses computed key-value (KV) attention states across repeated prompt prefixes",
         "Deletes previous user conversation history from memory after every turn",
         "Translates incoming prompts into short compressed abbreviations before sending"],
        0, "KV caching saves the computed attention matrices of long static documents (like system prompts or codebases), charging only discounted read prices on subsequent requests.")

    add(89, "MCP", "how does Model Context Protocol protect servers from unauthorized tool calls",
        ["Defines clear JSON-RPC schema contracts, permissions, and client-approved scopes",
         "Encrypts all network cables with proprietary hardware scrambling devices",
         "Requires human system administrators to manually type 'ALLOW' for each tool call"],
        0, "MCP establishes structured client-server boundaries, requiring explicit user authorization for tool scopes, resource access, and external data mutations.")

    add(90, "AI Model Names", "what do model naming suffixes like 'Q4_K_M' or '70B-Instruct' denote",
        ["Quantization scheme (4-bit medium) and parameter count with instruction tuning",
         "The manufacturing batch serial number assigned during factory assembly",
         "The pricing tier in dollars charged per one million processed output tokens"],
        0, "Model designations codify architecture specs: parameter size ('70B'), training mode ('Instruct'), and numerical quantization format ('Q4_K_M' = 4-bit medium k-quant).")

    add(91, "AI Skills", "what is the highest-leverage skill for modern software engineers in 2026",
        ["Architecting multi-agent systems, writing rigorous evals, and prompt engineering",
         "Memorizing raw assembly code syntax and manual pointer arithmetic",
         "Typing boilerplate CRUD boilerplate code faster than generative AI models"],
        0, "The frontier engineer's role shifts from manual syntax typing to system architecture: defining agent specifications, building automated evals, and designing cognitive loops.")

    add(92, "AI Note Taking", "how do semantic vector notes outperform traditional keyword search systems",
        ["Surface forgotten conceptual connections across notes without matching keywords",
         "Automatically delete duplicate thoughts from digital notebooks every midnight",
         "Format all written paragraphs into formal academic Latin prose style"],
        0, "Vector-embedded personal knowledge graphs retrieve related ideas across disparate projects, revealing non-obvious connections between meetings, books, and code.")

    add(93, "AI Coding", "what differentiates frontier coding tools (like Cursor or Claude Code)",
        ["Full codebase semantic indexing, terminal tool execution, and multi-file editing",
         "Generating single-line code completions inside a single isolated text file",
         "Compiling code directly without using any underlying operating system compiler"],
        0, "Modern coding agents navigate entire repositories, inspect git diffs, execute terminal tests, observe compiler errors, and iterate autonomously until builds pass.")

    add(94, "AI Email", "how should automated AI triage prioritize high-stakes incoming messages",
        ["Semantic categorization, urgency scoring, and drafting human-approved replies",
         "Automatically replying to every email with a generic canned AI confirmation",
         "Deleting any incoming email message that contains more than 100 characters"],
        0, "Effective triage uses structured LLM classification to extract action items, score urgency against user priorities, and generate drafts for one-click human approval.")

    add(95, "AI Research", "how do iterative deep-research agents synthesize comprehensive reports",
        ["Recursively search, read pages, extract citations, and refine queries autonomously",
         "Summarize only the top single Wikipedia article returned for the topic query",
         "Generate entire 20-page papers from imagination without consulting web sources"],
        0, "Deep research systems execute dozens of recursive search queries, reading source documents, cross-referencing claims, and compiling multi-page reports with verifiable citations.")

    add(96, "AI Data Analysis", "why is the Code Interpreter sandbox pattern the gold standard for data analysis",
        ["The LLM writes Python to execute precise mathematical math on verified data",
         "The LLM guesses statistical formulas from imagination without running code",
         "It replaces database SQL queries with fuzzy next-token prediction guesses"],
        0, "LLMs struggle with raw mental math. Code Interpreter allows models to write and run Python scripts (pandas, numpy), returning exact calculations and verified charts.")

    add(97, "AI Presentations", "what is the best pattern for generating presentation slide decks with AI",
        ["Generate clean structured Markdown or HTML slides, then render with Marp or Reveal",
         "Ask an image model to generate one giant pixel image containing all slide text",
         "Have the LLM manually position each letter on screen using raw pixel coordinates"],
        0, "Separating content from presentation via structured formats (like Marp Markdown or Reveal.js) guarantees readable typography, consistent layouts, and effortless editing.")

    add(98, "AI Learning", "how can you use an LLM as an optimal personalized Socratic tutor",
        ["Prompt it to question your assumptions and guide you step-by-step to answers",
         "Ask it to give you the direct answer immediately so you can copy and paste",
         "Have it generate 1,000 pages of unformatted technical jargon to memorize"],
        0, "Socratic prompting instructs the model to act as an encouraging professor: testing comprehension, offering hints, and challenging edge cases rather than spoon-feeding solutions.")

    add(99, "AI Productivity", "what is the 'sandwich method' of human-AI collaborative productivity",
        ["Human sets intent -> AI generates rough draft -> Human curates and refines",
         "AI sets goals -> Human writes the draft -> AI delivers the final presentation",
         "Human works exclusively in the morning and AI works exclusively in the evening"],
        0, "The sandwich workflow pairs human judgment for creative framing, AI speed for rapid first-draft synthesis, and human taste for final polish, ethics, and fact-checking.")

    add(100, "AI Tools", "what is the single most durable principle for staying ahead in the AI era",
        ["Master foundational architecture principles; tools change, fundamentals endure",
         "Switch your entire tech stack every week whenever a new tool launches",
         "Refuse to adopt any new software until the industry completely stabilizes"],
        0, "Frameworks, models, and wrapper apps churn constantly. Deep understanding of tokens, context windows, vector embeddings, and agentic loops remains permanently valuable.")

    return polls

if __name__ == "__main__":
    polls = get_community_polls()
    print(f"✅ Generated {len(polls)} verified community polls!")
    for day in [42, 43, 44, 45, 46]:
        p = polls[day]
        print(f"\n--- Day {day} ---")
        print("Question:", p["question"])
        for i, o in enumerate(p["options"]):
            print(f"  Option {i+1} ({len(o)}c): {o}")
        print("Correct:", p["correct_index"] + 1)
        print("Explanation snippet:", p["explanation"][:120] + "...")
