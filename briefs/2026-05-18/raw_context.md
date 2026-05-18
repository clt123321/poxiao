# raw_context.md - 2026-05-18

> 生成时间：2026-05-18 07:15 UTC+8
> 数据来源：gen_brief.sh (HuggingFace API + HackerNews Firebase API + Reddit RSS)
> 总条目：53条（HF Papers×13 + HN×20 + Reddit×20）

---

## HuggingFace Daily Papers (2026-05-18)

### [1] Nudging Beyond the Comfort Zone: Efficient Strategy-Guided Exploration for RLVR
- arxiv: https://arxiv.org/abs/2605.15726
- authors: Chanuk Lee, Sangwoo Park, Minki Kang
- 完整摘要: Reinforcement learning with verifiable rewards (RLVR) has emerged as a scalable paradigm for improving the reasoning capabilities of large language models. However, its effectiveness is fundamentally limited by exploration: the policy can only improve on trajectories it has already sampled. While increasing the number of rollouts alleviates this issue, such brute-force scaling is computationally expensive. [Strategy-guided exploration method proposed to efficiently push model beyond comfort zone without brute-force rollout expansion]

### [2] InsightTok: Improving Text and Face Fidelity in Discrete Tokenization for Autoregressive Image Generation
- arxiv: https://arxiv.org/abs/2605.14333
- authors: Yang Yue, Fangyun Wei, Tianyu He
- 完整摘要: Text and faces are among the most perceptually salient and practically important patterns in visual generation, yet they remain challenging for autoregressive generators built on discrete tokenization. A central bottleneck is the tokenizer: aggressive downsampling and quantization often discard the fine-grained structures needed to preserve readable glyphs and distinctive facial features.

### [3] ReactiveGWM: Steering NPC in Reactive Game World Models
- arxiv: https://arxiv.org/abs/2605.15256
- authors: Zeqing Wang, Danze Chen, Zhaohu Xing
- 完整摘要: Current game world models simulate environments from a subjective, player-centric perspective. However, by treating the Non-Player Character (NPC) merely as background pixels, these models cannot capture interactions between the player and NPC. In that sense, they act as passive video renderers rather than real simulation engines, lacking the physical understanding needed to model action-induced NPC responses.

### [4] MMSkills: Towards Multimodal Skills for General Visual Agents
- arxiv: https://arxiv.org/abs/2605.13527
- authors: Kangning Zhang, Shuai Shao, Qingyao Li
- 完整摘要: Reusable skills have become a core substrate for improving agent capabilities, yet most existing skill packages encode reusable behavior primarily as textual prompts, executable code, or learned routines. For visual agents, however, procedural knowledge is inherently multimodal: reuse depends not only on what operation to perform, but also on recognizing the relevant state, interpreting visual evidence.

### [5] PAGER: Bridging the Semantic-Execution Gap in Point-Precise Geometric GUI Control
- arxiv: https://arxiv.org/abs/2605.15963
- authors: Jingxuan Wei, Xi Bai, Shan Liu
- 完整摘要: Large vision-language models have significantly advanced GUI agents, enabling executable interaction across web, mobile, and desktop interfaces. Yet these gains largely rely on a forgiving region-tolerant paradigm, where many nearby pixels inside the same component remain valid. Precise geometric construction breaks this assumption: actions must land on points in continuous canvas space.

### [6] Flash-GRPO: Efficient Alignment for Video Diffusion via One-Step Policy Optimization
- arxiv: https://arxiv.org/abs/2605.15980
- authors: Xiaoxuan He, Siming Fu, Zeyue Xue
- 完整摘要: Group Relative Policy Optimization has emerged as essential for aligning video diffusion models with human preferences, but faces a critical computational bottleneck: training a 14B parametered model typically demands hundreds of GPU days per experiment. Existing efficiency methods reduce costs through sliding window subsampling training timesteps, but fundamentally compromise optimization, exhibiting an irreconcilable tension between optimization efficacy and efficiency.

### [7] FFAvatar: Few-Shot, Feed-Forward, and Generalizable Avatar Reconstruction
- arxiv: https://arxiv.org/abs/2605.15320
- authors: Thuan Hoang Nguyen, Jiahao Luo, Yinyu Nie
- 完整摘要: Avatar reconstruction has traditionally relied on per-subject optimization that requires hours of computation or on expensive preprocessing that limits scalability. We introduce FFAvatar, a generalizable feed-forward framework that reconstructs high-quality, animatable 3D Gaussian head avatars from few-shot unposed portrait images in seconds. FFAvatar fuses information from multiple source images.

### [8] DiagnosticIQ: A Benchmark for LLM-Based Industrial Maintenance Action Recommendation from Symbolic Rules
- arxiv: https://arxiv.org/abs/2605.08614
- authors: Devin Yasith De Silva, Dhaval Patel, Christodoulos Constantinides
- 完整摘要: Monitoring complex industrial assets relies on engineer-authored symbolic rules that trigger based on sensor conditions and prompt technicians to perform corrective actions. The bottleneck is not detection but response: translating rules into maintenance steps requires asset-specific knowledge gained through years of practice.

### [9] WorldAct: Activating Monolithic 3D Worlds into Interactive-Ready Object-Centric Scenes
- arxiv: https://arxiv.org/abs/2605.15843
- authors: Jichen Hu, Jiawei Guo, Jiazhong Cen
- 完整摘要: Recent 3D world modeling systems based on generative scene synthesis, such as Marble, can create coherent and explorable 3D environments, yet their outputs are typically static monolithic assets with limited editability and physical interaction. This restricts their use in immersive content creation and embodied simulation, where generated worlds must be actively modified and manipulated.

### [10] Solvita: Enhancing Large Language Models for Competitive Programming via Agentic Evolution
- arxiv: https://arxiv.org/abs/2605.15301
- authors: Han Li, Jinyu Tian, Rili Feng
- 完整摘要: Large language models (LLMs) still struggle with the rigorous reasoning demands of hard competitive programming. While recent multi-agent frameworks attempt to bridge this reliability gap, they remain fundamentally stateless: they rely on static retrieval and discard the valuable problem-solving and debugging experience gained from previous tasks. Solvita presents an agentic evolution framework.

### [11] HodgeCover: Higher-Order Topological Coverage Drives Compression of Sparse Mixture-of-Experts
- arxiv: https://arxiv.org/abs/2605.13997
- authors: Tao Zhong, Dongzhe Zheng, Christine Allen-Blanchette
- 完整摘要: Sparse Mixture-of-Experts (MoE) layers route tokens through a handful of experts, and learning-free compression of these layers reduces inference cost without retraining. A subtle obstruction blocks every existing compressor in this family: three experts can each be pairwise compatible yet form an irreducible cycle when merged together, so any score that ranks experts on pairwise signals is structurally flawed.

### [12] Agentic Discovery of Neural Architectures: AIRA-Compose and AIRA-Design
- arxiv: https://arxiv.org/abs/2605.15871
- authors: Alberto Pepe, Chien-Yu Lin, Despoina Magka
- 完整摘要: Toward recursive self-improvement, we investigate LLM agents autonomously designing foundation models beyond standard Transformers. We introduce a dual-framework approach: AIRA-Compose for high-level architecture search, and AIRA-Design for low-level mechanistic implementation. AIRA-Compose uses 11 agents to explore fundamental computational primitives under a 24-hour budget.

### [13] Look Before You Leap: Autonomous Exploration for LLM Agents
- arxiv: https://arxiv.org/abs/2605.16143
- authors: Ziang Ye, Wentao Shi, Yuxin Liu
- 完整摘要: Large language model based agents often fail in unfamiliar environments due to premature exploitation: a tendency to act on prior knowledge before acquiring sufficient environment-specific information. We identify autonomous exploration as a critical yet underexplored capability for building adaptive agents. We introduce Exploration Checkpoint Coverage as a quantification metric.

---

## HackerNews Top Stories (2026-05-18)

- [660] Mozilla to UK regulators: VPNs are essential privacy and security tools | https://blog.mozilla.org/netpolicy/2026/05/15/mozilla-to-uk-regulators-vpns-are-essential-privacy-and-security-tools-and-should-not-be-undermined/
- [502] I don't think AI will make your processes go faster | https://frederickvanbrabant.com/blog/2026-05-15-i-dont-think-ai-will-make-your-processes-go-faster/
- [392] Native all the way, until you need text | https://justsitandgrin.im/posts/native-all-the-way-until-you-need-text/
- [342] AI is a technology not a product | https://daringfireball.net/2026/05/ai_is_technology_not_a_product
- [314] A nicer voltmeter clock | https://lcamtuf.substack.com/p/a-nicer-voltmeter-clock
- [267] I turned a $80 RK3562 Android tablet into a Debian Linux workstation | https://github.com/tech4bot/rk3562deb
- [217] Colossus: The Forbin Project | https://en.wikipedia.org/wiki/Colossus:_The_Forbin_Project
- [211] Prolog Basics Explained with Pokémon | https://unplannedobsolescence.com/blog/prolog-basics-pokemon/
- [186] Show HN: Semble – Code search for agents that uses 98% fewer tokens than grep | https://github.com/MinishLab/semble
- [174] Tesla Solar Roof is on life support as it pivot to panels | https://electrek.co/2026/05/14/tesla-solar-roof-promise-vs-reality-pivot-panels/
- [164] Mercurial, 20 years and counting | https://fosdem.org/2026/schedule/event/AGWUVH-mercurial-aint-you-dead-yet/
- [159] Hindenburg's Smoking Room | https://www.airships.net/hindenburg-smoking-room/
- [133] CUDA Books | https://github.com/alternbits/awesome-cuda-books
- [129] GenCAD | https://gencad.github.io/
- [117] VoIP brings back old-fashioned pay phones to rural Vermont | https://spectrum.ieee.org/payphone-voip

---

## Reddit LocalLLaMA Hot (2026-05-18)

- M5 vs DGX Spark vs Strix Halo vs RTX 6000 | https://www.reddit.com/r/LocalLLaMA/comments/1tfzsd6/
- "Generate a photorealistic realtime render of a human face with webGL" (Qwen3.5-122B) | https://www.reddit.com/r/LocalLLaMA/comments/1tg2muq/
- I hope that someday we will have a 124B Gemma | https://www.reddit.com/r/LocalLLaMA/comments/1tfv8li/
- May 2026 updated chart of strix halo mini pc size chart | https://www.reddit.com/r/LocalLLaMA/comments/1tg6sgn/
- llama.cpp MTP logits optimization PR #23198 | https://www.reddit.com/r/LocalLLaMA/comments/1tft1il/
- 85 GPU-hours comparing 5 abliteration methods on Qwen3.6-27B | https://www.reddit.com/r/LocalLLaMA/comments/1tfmocw/
- Apple silicon costs more than OpenRouter: an analysis | https://www.reddit.com/r/LocalLLaMA/comments/1tg0y2h/
- The power of structured workflows and small local models | https://www.reddit.com/r/LocalLLaMA/comments/1tftaaa/
- Gemma-4-Gembrain-31B-it-uncensored-heretic release | https://www.reddit.com/r/LocalLLaMA/comments/1tg7s7j/
- Benchmarking vLLM vs SGLang vs llama.cpp on a mixed Blackwell/Ada cluster | https://www.reddit.com/r/LocalLLaMA/comments/1tg4mw0/
- Dual GPU llama.cpp speedup | https://www.reddit.com/r/LocalLLaMA/comments/1tflngz/
- Testing llama.cpp MTP support on Qwen3.6 - RTX 5090 | https://www.reddit.com/r/LocalLLaMA/comments/1tfgxc8/
- ROCm 7.13 nightly adds strix halo optimizations | https://www.reddit.com/r/LocalLLaMA/comments/1tftg09/
- Benchmarking b9200: Optimizing Qwen 3.6 27B mtp on single RTX 3090 | https://www.reddit.com/r/LocalLLaMA/comments/1tg6j9u/
- MTP experiences on 7900xtx? | https://www.reddit.com/r/LocalLLaMA/comments/1tg25fz/
- Moving from Composer 2/Kimi 2.6 to Qwen3.6:35b-a3b | https://www.reddit.com/r/LocalLLaMA/comments/1tfxah9/
- Pushing the limit: minimax m2.7 q8_0 128k on 2x3090 | https://www.reddit.com/r/LocalLLaMA/comments/1tg37t6/
- b9200 released - potential mtp pp increase | https://www.reddit.com/r/LocalLLaMA/comments/1tg5r5p/
