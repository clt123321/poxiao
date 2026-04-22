# 破晓 PoXiao — 原始数据 (Raw Context)
生成时间: 2026-04-20 02:47 UTC
================================================================================

[RSS:Reddit LocalLLaMA (社区共识)]
To Beat China, Embrace Open-Source AI (WSJ)
https://www.reddit.com/r/LocalLLaMA/comments/1sqa40j/to_beat_china_embrace_opensource_ai_wsj/
&#32; submitted by &#32; /u/rm-rf-rm [link] &#32; [comments]
---

[RSS:Reddit LocalLLaMA (社区共识)]
Switching from Opus 4.7 to Qwen-35B-A3B
https://www.reddit.com/r/LocalLLaMA/comments/1spz0ck/switching_from_opus_47_to_qwen35ba3b/
Hey Guys, I am thinking about switching from Opus 4.7 to Qwen-35B-A3B for my daily coding agent driver. Has anyone done this yet? If so, what has your experience been like? I would love to hear the communities take on this. I know Opus may have the edge on complex reasoning, but will Qwen-35B-A3B su
---

[RSS:Reddit LocalLLaMA (社区共识)]
LLM Neuroanatomy III - LLMs seem to think in geometry, not language
https://www.reddit.com/r/LocalLLaMA/comments/1spy497/llm_neuroanatomy_iii_llms_seem_to_think_in/
Hi Reddit! Last month I posted the third part of my series of article on LLM Neuroanatomy just before I left to go on holiday 🏝️. Unfortunately, is was a bit 'sloppy', as I didn't have time to add polish, so I took the article down and deleted the Reddit post. Over the weekend, I have revised the ar
---

[RSS:Reddit LocalLLaMA (社区共识)]
Is anyone getting real coding work done with Qwen3.6-35B-A3B-UD-Q4_K_M on a 32GB Mac in opencode, claude code or similar?
https://www.reddit.com/r/LocalLLaMA/comments/1sq94qx/is_anyone_getting_real_coding_work_done_with/
I'm running Qwen3.6-35B-A3B-UD-Q4_K_M on an M2 Macbook Pro with 32GB of RAM. I'm using quite recent builds of llama.cpp and opencode. To avoid llama-server crashing outright due to memory exhaustion, I have to set the context window to 32768 tokens. This turns out to be important. As a hopefully rea
---

[RSS:Reddit LocalLLaMA (社区共识)]
llama.cpp speculative checkpointing was merged
https://www.reddit.com/r/LocalLLaMA/comments/1sprdm8/llamacpp_speculative_checkpointing_was_merged/
https://github.com/ggml-org/llama.cpp/pull/19493 Some prompts get a speedup, others don't (cases of low draft acceptance streak). Good working params depend on the task type and repetition patterns. For coding, I got some 0%~50% speedup with these params: --spec-type ngram-mod --spec-ngram-size-n 24
---

[RSS:Reddit LocalLLaMA (社区共识)]
Speculative decoding question, 665% speed increase
https://www.reddit.com/r/LocalLLaMA/comments/1sq7grd/speculative_decoding_question_665_speed_increase/
Im using these settings in llama.cpp: --spec-type ngram-map-k --spec-ngram-size-n 24 --draft-min 12 --draft-max 48 Whats the real reason for lets say the prompt is for &quot;minor changes in code&quot;, whats differing between models: Gemma 4 31b: Doubles in tks gen so 100% Qwen 3.6: Only 40% more s
---

[RSS:Reddit LocalLLaMA (社区共识)]
SK hynix starts mass production of 192GB SOCAMM2 for NVIDIA AI servers
https://www.reddit.com/r/LocalLLaMA/comments/1sqap57/sk_hynix_starts_mass_production_of_192gb_socamm2/
hynix just started mass producing a 192GB SOCAMM2 memory module aimed at next gen AI servers, and it is basically trying to fix one of the biggest bottlenecks in modern AI systems. Instead of traditional server RAM, it uses LPDDR5X like you would find in phones, which lets it push more than double t
---

[RSS:Reddit LocalLLaMA (社区共识)]
Why isn't ebay doing anything to stop those scams?
https://www.reddit.com/r/LocalLLaMA/comments/1splwqx/why_isnt_ebay_doing_anything_to_stop_those_scams/
There's no way this is real and ebay is doing nothing to stop those scams. Why, people are actually bidding and buying into them and it's just so sad. There are tens of ads from 0 sold account selling m3 ultra 512gb for around a thousand and change which is insane, considering you'd be pressed to ev
---

[RSS:Reddit LocalLLaMA (社区共识)]
"Browser OS" implemented by Qwen 3.6 35B: The best result I ever got from a local model
https://www.reddit.com/r/LocalLLaMA/comments/1spubyp/browser_os_implemented_by_qwen_36_35b_the_best/
&#32; submitted by &#32; /u/tarruda [link] &#32; [comments]
---

[RSS:Reddit LocalLLaMA (社区共识)]
QWEN3.6 + ik_llama is fast af
https://www.reddit.com/r/LocalLLaMA/comments/1sq8q9k/qwen36_ik_llama_is_fast_af/
running qwen3.6 UD_Q_4_K_M on 16GB vram + 32GB ram with 200k cw @50+ tok/s &#32; submitted by &#32; /u/_BigBackClock [link] &#32; [comments]
---

[RSS:Reddit LocalLLaMA (社区共识)]
Bloomberg: No Mac Studios until at least October
https://www.reddit.com/r/LocalLLaMA/comments/1spz6kj/bloomberg_no_mac_studios_until_at_least_october/
https://9to5mac.com/2026/04/19/new-mac-studio-may-not-arrive-until-october/ What’s coming first? Deepseek v4 or the Studios that can run it? &#32; submitted by &#32; /u/eclipsegum [link] &#32; [comments]
---

[RSS:Reddit LocalLLaMA (社区共识)]
Unsloth fix on Mistral Small 4?
https://www.reddit.com/r/LocalLLaMA/comments/1sq01bj/unsloth_fix_on_mistral_small_4/
Every quant got update https://huggingface.co/unsloth/Mistral-Small-4-119B-2603-GGUF &#32; submitted by &#32; /u/Altruistic_Heat_9531 [link] &#32; [comments]
---

[RSS:Reddit LocalLLaMA (社区共识)]
Same 9B Qwen weights: 19.1% in Aider vs 45.6% with a scaffold adapted to small local models
https://www.reddit.com/r/LocalLLaMA/comments/1spufzz/same_9b_qwen_weights_191_in_aider_vs_456_with_a/
I spent the past week testing a simple question: Small local models often look weak inside coding agents. But how much of that is actually model weakness, and how much is scaffold mismatch? So I held the model fixed and changed only the scaffold. Same Qwen3.5-9B Q4 weights in both conditions. Same A
---

[RSS:Reddit LocalLLaMA (社区共识)]
LLM for finance
https://www.reddit.com/r/LocalLLaMA/comments/1sqbej2/llm_for_finance/
Any specific LLM best for financial and/or accounting related tasks? Specifically, dealing with large data sets, pdf extraction (bank statements), tracing transaction from bank statement to ledger, identifying unusual trends, clean excel outputs! &#32; submitted by &#32; /u/rtk85 [link] &#32; [comme
---

[RSS:Reddit LocalLLaMA (社区共识)]
What is the current status of OpenCode regarding privacy and the "proxy to app.opencode.ai" issue?
https://www.reddit.com/r/LocalLLaMA/comments/1sq8uze/what_is_the_current_status_of_opencode_regarding/
Hi everyone, I've been following the discussions around OpenCode for a while now and recently came across an older thread discussing significant privacy concerns https://www.reddit.com/r/LocalLLaMA/comments/1rv690j/opencode_concerns_not_truely_local/ The main concern raised was that when running ope
---

[RSS:Reddit LocalLLaMA (社区共识)]
Qwen3.6 agent + Cisco switch: local NetOps AI actually works!
https://www.reddit.com/r/LocalLLaMA/comments/1spws0a/qwen36_agent_cisco_switch_local_netops_ai/
Hello Local Llama! I was using Qwen3.5 35B since release and it was awesome. Was super excited to try Qwen 3.6 as agent + try out Opencode for the first time since I was having a couple critical tool call failures with 3.5 (using cline in VScode). Spent a few hours with Qwen yesterday building a dir
---

[RSS:Reddit LocalLLaMA (社区共识)]
Mixture-of-Depths Attention - arXiv
https://www.reddit.com/r/LocalLLaMA/comments/1sq0hdv/mixtureofdepths_attention_arxiv/
Scaling depth is a key driver for large language models (LLMs). Yet, as LLMs become deeper, they often suffer from signal degradation: informative features formed in shallow layers are gradually diluted by repeated residual updates, making them harder to recover in deeper layers. We introduce mixtur
---

[RSS:Reddit LocalLLaMA (社区共识)]
Gemma 4 - MLX doesn't seem better than GGUF
https://www.reddit.com/r/LocalLLaMA/comments/1spn7zh/gemma_4_mlx_doesnt_seem_better_than_gguf/
Going to flag this up front - I know that there are some properly smart people on this sub, please can you correct my noob user errors or misunderstandings and educate my ass. Model : google/gemma-4-26b-a4b Versions : MLX: https://huggingface.co/mlx-community/gemma-4-26b-a4b-it-4bit GGUF: https://hu
---

[RSS:Reddit LocalLLaMA (社区共识)]
BrainDB: Karpathy's 'LLM wiki' idea, but as a real DB with typed entities and a graph
https://www.reddit.com/r/LocalLLaMA/comments/1sq8yms/braindb_karpathys_llm_wiki_idea_but_as_a_real_db/
Why BrainDB? Inspired by Karpathy's LLM wiki idea — give an LLM a persistent external memory it can read and write. BrainDB takes that further by adding structure, retrieval, and a graph on top of the &quot;plain markdown files&quot; baseline. vs. RAG. RAG is stateless: embed documents, retrieve sim
---

[RSS:Reddit LocalLLaMA (社区共识)]
Unsloth/Qwen3.6-35b-a3b -> Q5_K_S vs Q4_K_XL
https://www.reddit.com/r/LocalLLaMA/comments/1sptnbu/unslothqwen3635ba3b_q5_k_s_vs_q4_k_xl/
I run both from unsloth with recommended settings, and what I found is that Q4_K_XL does a LOT better job in my use case - web research, document research, transcript, python and html coding and code debugging Especially in websearch It looks to me that reasoning is a lot stronger in Q4 model Has an
---

[RSS:Reddit LocalLLaMA (社区共识)]
Small Gemma 4, Qwen 3.6 and Qwen 3 Coder Next comparison for a debugging use-case
https://www.reddit.com/r/LocalLLaMA/comments/1sptduw/small_gemma_4_qwen_36_and_qwen_3_coder_next/
Nothing extensive to see here, just a quick qualitative and performance comparison for a single programming use-case: Making an ancient website that uses Flash for everything work with modern browsers. I let all 3 models tackle exactly the same issue and provided exactly the same multi-turn feedback
---

[RSS:Reddit LocalLLaMA (社区共识)]
Venturing into the world of local LLM's, would love some pointers!
https://www.reddit.com/r/LocalLLaMA/comments/1sq2fu3/venturing_into_the_world_of_local_llms_would_love/
Hi everyone! Very exciting times we live in where we can run models from laptops and GPU's which 4 years ago would've been SOTA. I have been working with cloud models for years now, and I am now starting to dig into local models. At work, I am leading a few different AI projects across the biz, and 
---

[RSS:Reddit MachineLearning (学术风向)]
1,200 ICLR 2026 Papers with Public Code or Data [R]
https://www.reddit.com/r/MachineLearning/comments/1spvoer/1200_iclr_2026_papers_with_public_code_or_data_r/
Here is a list of ~1,200 ICLR 2026 accepted papers that have associated public code, data, or a demo link available. The links are directly extracted from their paper submissions. This is approximately 22% of the 5,300+ accepted papers. The List: https://www.paperdigest.org/2026/04/iclr-2026-papers-
---

[RSS:Reddit MachineLearning (学术风向)]
Advice on becoming a research engineer [D]
https://www.reddit.com/r/MachineLearning/comments/1sptj32/advice_on_becoming_a_research_engineer_d/
I am thinking about becoming a research engineer, and want to ask your advice on how realistic it is, and which strategies make sense in my situation. About myself: I am in the US, have extensive experience as a Software Engineer (including Staff+ position at one of the top companies), have a math h
---

[RSS:Reddit MachineLearning (学术风向)]
On the path towards a true science of deep learning [D]
https://www.reddit.com/r/MachineLearning/comments/1sq273c/on_the_path_towards_a_true_science_of_deep/
I'm a scientist with a dual affiliation in industry + academia. I've been working towards a fundamental scientific theory of machine learning for some ~7y now. Here are some thoughts on how we'll get there. &#32; submitted by &#32; /u/dot--- [link] &#32; [comments]
---

[RSS:Reddit MachineLearning (学术风向)]
KDD 2026 Cycle 2 reviews seem to have vanished from author view [D]
https://www.reddit.com/r/MachineLearning/comments/1spzf8k/kdd_2026_cycle_2_reviews_seem_to_have_vanished/
I just noticed that the reviews and discussion for our submitted paper have vanished, but I can see the discussions for other papers in my reviewer view. Do others notice the same? &#32; submitted by &#32; /u/Massive-Bobcat-5363 [link] &#32; [comments]
---

[RSS:Reddit MachineLearning (学术风向)]
What are the future prospects of Spiking Neural Networks (and particularly, neuromorphics computing) and Liquid Neural Networks? [D]
https://www.reddit.com/r/MachineLearning/comments/1spj2w4/what_are_the_future_prospects_of_spiking_neural/
Question to discuss. I'm an undergrad and stumbled across these new forms of neural networks but I haven't seen mainstream adoption of these and was wondering are these something to look forward to learn about (maybe make a project or 2)? &#32; submitted by &#32; /u/GodRishUniverse [link] &#32; [com
---

[RSS:Reddit MachineLearning (学术风向)]
Converting XQuery to SQL with Local LLMs: Do I Need Fine-Tuning or a Better Approach? [P]
https://www.reddit.com/r/MachineLearning/comments/1sppcnw/converting_xquery_to_sql_with_local_llms_do_i/
&#x200b; I am trying to convert XQuery statements into SQL queries within an enterprise context, with the constraint that the solution must rely on locally run LLMs. A key challenge is the limited availability of training data (pairs of XQueries and their corresponding SQL queries), especially with 
---

[RSS:Reddit MachineLearning (学术风向)]
Tier-3 ISE final year with ongoing ML research (TMLR/Q1/NeurIPS target), trying to understand real impact in India [D]
https://www.reddit.com/r/MachineLearning/comments/1spoj6t/tier3_ise_final_year_with_ongoing_ml_research/
I went through a bunch of older posts here about research vs dev roles, but most of them were either very general or not really in a similar situation, so posting this. I’m a final year ISE student from a tier-3 college. Over the past 1.5–2 years I’ve been focusing quite a bit on ML research instead
---

[RSS:Reddit MachineLearning (学术风向)]
Why production systems keep making “correct” decisions that are no longer right [D]
https://www.reddit.com/r/MachineLearning/comments/1spuaek/why_production_systems_keep_making_correct/
I’ve been looking at a recurring failure pattern across AI systems in production. Not model failure, or data quality or infrastructure. Something else. Where system continues to operate exactly as designed, models run, outputs look valid, pipelines execute and governance signs off But the underlying
---

[HACKERNEWS]
Show HN: TRELLIS.2 image-to-3D running on Mac Silicon – no Nvidia GPU needed
https://github.com/shivampkumar/trellis-mac
Score: 54 | Comments: 5
---

[HACKERNEWS]
A Brief History of Fish Sauce
https://www.legalnomads.com/fish-sauce/
Score: 90 | Comments: 40
---

[HACKERNEWS]
Vercel April 2026 security incident
https://www.bleepingcomputer.com/news/security/vercel-confirms-breach-as-hackers-claim-to-be-selling-stolen-data/
Score: 562 | Comments: 327
---

[HACKERNEWS]
The Bromine Chokepoint
https://warontherocks.com/cogs-of-war/the-bromine-chokepoint-how-strife-in-the-middle-east-could-halt-production-of-the-worlds-memory-chips/
Score: 164 | Comments: 76
---

[HACKERNEWS]
The insider trading suspicions looming over Trump's presidency
https://www.bbc.com/news/articles/cge0grppe3po
Score: 75 | Comments: 14
---

[HACKERNEWS]
Turtle WoW classic server announces shutdown after Blizzard wins injunction
https://www.pcgamer.com/games/world-of-warcraft/turtle-wow-classic-server-announces-shutdown-after-blizzard-wins-injunction/
Score: 134 | Comments: 107
---

[HACKERNEWS]
2,100 Swiss municipalities showing which provider handles their official email
https://mxmap.ch/
Score: 75 | Comments: 21
---

[HACKERNEWS]
Ex-CEO, ex-CFO of bankrupt AI company charged with fraud
https://www.reuters.com/legal/government/ex-ceo-ex-cfo-bankrupt-ai-company-charged-with-fraud-2026-04-17/
Score: 127 | Comments: 53
---

[HACKERNEWS]
Swiss AI Initiative (2023)
https://www.swiss-ai.org
Score: 21 | Comments: 6
---

[HACKERNEWS]
Changes in the system prompt between Claude Opus 4.6 and 4.7
https://simonwillison.net/2026/Apr/18/opus-system-prompt/
Score: 229 | Comments: 128
---

[HACKERNEWS]
Show HN: A lightweight way to make agents talk without paying for API usage
https://juanpabloaj.com/2026/04/16/a-lightweight-way-to-make-agents-talk-without-paying-for-api-usage/
Score: 8 | Comments: 3
---

[HACKERNEWS]
Scientific datasets are riddled with copy-paste errors
https://www.sciencedetective.org/scientific-datasets-are-riddled-with-copy-paste-errors/
Score: 40 | Comments: 5
---

[HACKERNEWS]
Six Levels of Dark Mode (2024)
https://cssence.com/2024/six-levels-of-dark-mode/
Score: 54 | Comments: 20
---

[ACADEMIC - ARXIV]
标题: Pruning Unsafe Tickets: A Resource-Efficient Framework for Safer and More Robust LLMs
作者: Wai Man Si, Mingjie Li, Michael Backes, Yang Zhang
链接: https://arxiv.org/abs/2604.15780v1
完整摘要: Machine learning models are increasingly deployed in real-world applications, but even aligned models such as Mistral and LLaVA still exhibit unsafe behaviors inherited from pre-training. Current alignment methods like SFT and RLHF primarily encourage models to generate preferred responses, but do not explicitly remove the unsafe subnetworks that trigger harmful outputs. In this work, we introduce a resource-efficient pruning framework that directly identifies and removes parameters associated with unsafe behaviors while preserving model utility. Our method employs a gradient-free attribution mechanism, requiring only modest GPU resources, and generalizes across architectures and quantized variants. Empirical evaluations on ML models show substantial reductions in unsafe generations and improved robustness against jailbreak attacks, with minimal utility loss. From the perspective of the Lottery Ticket Hypothesis, our results suggest that ML models contain "unsafe tickets" responsible for harmful behaviors, and pruning reveals "safety tickets" that maintain performance while aligning outputs. This provides a lightweight, post-hoc alignment strategy suitable for deployment in resource-constrained settings.
匹配关键词: RLHF
---

[ACADEMIC - ARXIV]
标题: Beyond Importance Sampling: Rejection-Gated Policy Optimization
作者: Ziwu Sun, Zhen Gao, Jiyong Zhang, Jiaheng Li
链接: https://arxiv.org/abs/2604.14895v1
完整摘要: We propose a new perspective on policy optimization: rather than reweighting all samples by their importance ratios, an optimizer should select which samples are trustworthy enough to drive a policy update. Building on this view, we introduce Rejection-Gated Policy Optimization (RGPO), which replaces the importance sampling ratio r_theta = pi_theta / pi_old with a smooth, differentiable acceptance gate alpha_theta(s, a) = g(r_theta(s, a)) in the range [0, 1]. Unlike prior work that applies rejection sampling as a data-level heuristic before training, RGPO elevates rejection to an optimization principle: the gate participates directly in gradient computation and is implicitly updated alongside the policy. RGPO provides a unified framework: the policy gradients of TRPO, PPO, and REINFORCE all correspond to specific choices of the effective gradient weight w(r) = g'(r) * r. We prove that RGPO guarantees finite, bounded gradient variance even when importance sampling ratios are heavy-tailed (where IS variance diverges). We further show that RGPO incurs only a bounded, controllable bias and provides an approximate monotonic policy improvement guarantee analogous to TRPO. RGPO matches PPO in computational cost, requires no second-order optimization, and extends naturally to RLHF-style preference alignment. In online preference fine-tuning of Qwen2.5-1.5B-Instruct on Anthropic HH-RLHF (n = 3 seeds), RGPO uses a dual-ratio gate that anchors learning to both the previous policy and the reference model, achieving a Pareto-dominant outcome: the highest reward among online RL methods (+14.8% vs. PPO-RLHF) and the lowest KL divergence to the reference model (-16.0% vs. PPO-RLHF, -53.1% vs. GRPO).
匹配关键词: RLHF
---

[ACADEMIC - ARXIV]
标题: Acceptance Dynamics Across Cognitive Domains in Speculative Decoding
作者: Saif Mahmoud
链接: https://arxiv.org/abs/2604.14682v1
完整摘要: Speculative decoding accelerates large language model (LLM) inference. It uses a small draft model to propose a tree of future tokens. A larger target model then verifies these tokens in a single batched forward pass. Despite the growing body of work on speculative methods, the degree to which the cognitive characteristics of a task affect acceptance probability remains largely unexplored. We present an empirical study of tree-based speculative decoding acceptance dynamics. Our study spans four well-established NLP benchmark domains: code generation, mathematical reasoning, logical reasoning, and open-ended chat. For this, we use TinyLlama-1.1B as the draft model against Llama-2-7B-Chat-GPTQ as the target. Over 99,768 speculative nodes collected from 200 prompts, we derive per-domain acceptance rates, expected accepted lengths, depth-acceptance profiles, and entropy-acceptance correlations. We find that task type is a stronger predictor of acceptance than tree depth. Furthermore, only the chat domain consistently yields an expected accepted length exceeding 1.0 token per step. We also show that the entropy-acceptance correlation is consistently negative but weak across all domains (rho in [-0.20, -0.15]). Counterintuitively, chat produces the highest entropy yet the highest acceptance rate. We attribute this divergence to the lexical predictability of RLHF-aligned register. These findings have direct implications for domain-aware speculation budgets and draft-model selection strategies. Index Terms--speculative decoding, large language model inference, tree attention, draft model, acceptance probability, LLM efficiency
匹配关键词: RLHF
---

[ACADEMIC - ARXIV]
标题: An Empirical Investigation of Practical LLM-as-a-Judge Improvement Techniques on RewardBench 2
作者: Ryan Lail
链接: https://arxiv.org/abs/2604.13717v1
完整摘要: LLM-as-a-judge, using a language model to score or rank candidate responses, is widely used as a scalable alternative to human evaluation in RLHF pipelines, benchmarking, and application layer evaluations (evals). However, judgment reliability depends heavily on prompting and aggregation strategy. We present an empirical investigation of practical, drop-in techniques that improve GPT-5.4 judge accuracy on RewardBench 2 without any finetuning. Two techniques account for nearly all available gains: task-specific criteria injection (+3.0pp at negligible cost) and ensemble scoring (+9.8pp at 5x cost). Combined, they reach 83.6% accuracy, +11.9pp over the 71.7% baseline. Our investigation also covers three further techniques (calibration context, adaptive model escalation, and soft blending) which did not reliably improve on criteria + ensembling at comparable cost. Cheaper model tiers benefit disproportionately from ensembling: GPT-5.4 mini with k=8 achieves 79.2% at 1.2x baseline cost, and GPT-5.4 nano with k=8 reaches 71.4% at 0.4x baseline cost, making high-accuracy LLM judges accessible at low cost.
匹配关键词: RLHF
---

[ACADEMIC - ARXIV]
标题: Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges
作者: Xiaohua Wang, Muzhao Tian, Yuqi Zeng, Zisu Huang, Jiakang Yuan, Bowen Chen, Jingwen Xu, Mingbo Zhou, Wenhao Liu, Muling Wu, Zhengkang Guo, Qi Qian, Yifei Wang, Feiran Zhang, Ruicheng Yin, Shihan Dou, Changze Lv, Tao Chen, Kaitao Song, Xu Tan, Tao Gui, Xiaoqing Zheng, Xuanjing Huang
链接: https://arxiv.org/abs/2604.13602v1
完整摘要: Reinforcement Learning from Human Feedback (RLHF) and related alignment paradigms have become central to steering large language models (LLMs) and multimodal large language models (MLLMs) toward human-preferred behaviors. However, these approaches introduce a systemic vulnerability: reward hacking, where models exploit imperfections in learned reward signals to maximize proxy objectives without fulfilling true task intent. As models scale and optimization intensifies, such exploitation manifests as verbosity bias, sycophancy, hallucinated justification, benchmark overfitting, and, in multimodal settings, perception--reasoning decoupling and evaluator manipulation. Recent evidence further suggests that seemingly benign shortcut behaviors can generalize into broader forms of misalignment, including deception and strategic gaming of oversight mechanisms. In this survey, we propose the Proxy Compression Hypothesis (PCH) as a unifying framework for understanding reward hacking. We formalize reward hacking as an emergent consequence of optimizing expressive policies against compressed reward representations of high-dimensional human objectives. Under this view, reward hacking arises from the interaction of objective compression, optimization amplification, and evaluator--policy co-adaptation. This perspective unifies empirical phenomena across RLHF, RLAIF, and RLVR regimes, and explains how local shortcut learning can generalize into broader forms of misalignment, including deception and strategic manipulation of oversight mechanisms. We further organize detection and mitigation strategies according to how they intervene on compression, amplification, or co-adaptation dynamics. By framing reward hacking as a structural instability of proxy-based alignment under scale, we highlight open challenges in scalable oversight, multimodal grounding, and agentic autonomy.
匹配关键词: RLHF
---

[ACADEMIC - ARXIV]
标题: AtManRL: Towards Faithful Reasoning via Differentiable Attention Saliency
作者: Max Henning Höth, Kristian Kersting, Björn Deiseroth, Letitia Parcalabescu
链接: https://arxiv.org/abs/2604.16158v1
完整摘要: Large language models (LLMs) increasingly rely on chain-of-thought (CoT) reasoning to solve complex tasks. Yet ensuring that the reasoning trace both contributes to and faithfully reflects the processes underlying the model's final answer, rather than merely accompanying it, remains challenging. We introduce AtManRL, a method that leverages differentiable attention manipulation to learn more faithful reasoning through reinforcement learning. By training an additive attention mask that identifies tokens in the CoT crucial for producing correct answers, we derive a saliency reward signal that encourages the model to generate reasoning traces that genuinely influence its final predictions. We integrate this saliency reward with outcome-based rewards within the GRPO framework to jointly optimize for correctness and interpretability. Experiments on GSM8K and MMLU with Llama-3.2-3B-Instruct demonstrate that our approach can identify influential reasoning tokens and enable training more transparent reasoning models.
匹配关键词: GRPO
---

[ACADEMIC - ARXIV]
标题: IG-Search: Step-Level Information Gain Rewards for Search-Augmented Reasoning
作者: Zihan Liang, Yufei Ma, Ben Chen, Zhipeng Qian, Huangyu Dai, Lingtao Mao, Xuxin Zhang, Chenyi Lei, Wenwu Ou
链接: https://arxiv.org/abs/2604.15148v1
完整摘要: Reinforcement learning has emerged as an effective paradigm for training large language models to perform search-augmented reasoning. However, existing approaches rely on trajectory-level rewards that cannot distinguish precise search queries from vague or redundant ones within a rollout group, and collapse to a near-zero gradient signal whenever every sampled trajectory fails. In this paper, we propose IG-Search, a reinforcement learning framework that introduces a step-level reward based on Information Gain (IG). For each search step, IG measures how much the retrieved documents improve the model's confidence in the gold answer relative to a counterfactual baseline of random documents, thereby reflecting the effectiveness of the underlying search query. This signal is fed back to the corresponding search-query tokens via per-token advantage modulation in GRPO, enabling fine-grained, step-level credit assignment within a rollout. Unlike prior step-level methods that require either externally annotated intermediate supervision or shared environment states across trajectories, IG-Search derives its signals from the policy's own generation probabilities, requiring no intermediate annotations beyond standard question-answer pairs. Experiments on seven single-hop and multi-hop QA benchmarks demonstrate that IG-Search achieves an average EM of 0.430 with Qwen2.5-3B, outperforming the strongest trajectory-level baseline (MR-Search) by 1.6 points and the step-level method GiGPO by 0.9 points on average across benchmarks, with particularly pronounced gains on multi-hop reasoning tasks. Despite introducing a dense step-level signal, IG-Search adds only ~6.4% to per-step training wall-clock time over the trajectory-level baseline and leaves inference latency unchanged, while still providing a meaningful gradient signal even when every sampled trajectory answers incorrectly.
匹配关键词: GRPO
---

[ACADEMIC - ARXIV]
标题: UniDoc-RL: Coarse-to-Fine Visual RAG with Hierarchical Actions and Dense Rewards
作者: Jun Wang, Shuo Tan, Zelong Sun, Tiancheng Gu, Yongle Zhao, Ziyong Feng, Kaicheng Yang, Zhiwu Lu
链接: https://arxiv.org/abs/2604.14967v2
完整摘要: Retrieval-Augmented Generation (RAG) extends Large Vision-Language Models (LVLMs) with external visual knowledge. However, existing visual RAG systems typically rely on generic retrieval signals that overlook the fine-grained visual semantics essential for complex reasoning. To address this limitation, we propose UniDoc-RL, a unified reinforcement learning framework in which an LVLM agent jointly performs retrieval, reranking, active visual perception, and reasoning. UniDoc-RL formulates visual information acquisition as a sequential decision-making problem with a hierarchical action space. Specifically, it progressively refines visual evidence from coarse-grained document retrieval to fine-grained image selection and active region cropping, allowing the model to suppress irrelevant content and attend to information-dense regions. For effective end-to-end training, we introduce a dense multi-reward scheme that provides task-aware supervision for each action. Based on Group Relative Policy Optimization (GRPO), UniDoc-RL aligns agent behavior with multiple objectives without relying on a separate value network. To support this training paradigm, we curate a comprehensive dataset of high-quality reasoning trajectories with fine-grained action annotations. Experiments on three benchmarks demonstrate that UniDoc-RL consistently surpasses state-of-the-art baselines, yielding up to 17.7% gains over prior RL-based methods.
匹配关键词: GRPO
---

[ACADEMIC - ARXIV]
标题: LongAct: Harnessing Intrinsic Activation Patterns for Long-Context Reinforcement Learning
作者: Bowen Ping, Zijun Chen, Tingfeng Hui, Qize Yu, Chenxuan Li, Junchi Yan, Baobao Chang
链接: https://arxiv.org/abs/2604.14922v1
完整摘要: Reinforcement Learning (RL) has emerged as a critical driver for enhancing the reasoning capabilities of Large Language Models (LLMs). While recent advancements have focused on reward engineering or data synthesis, few studies exploit the model's intrinsic representation characteristics to guide the training process. In this paper, we first observe the presence of high-magnitude activations within the query and key vectors when processing long contexts. Drawing inspiration from model quantization -- which establishes the criticality of such high-magnitude activations -- and the insight that long-context reasoning inherently exhibits a sparse structure, we hypothesize that these weights serve as the pivotal drivers for effective model optimization. Based on this insight, we propose LongAct, a strategy that shifts from uniform to saliency-guided sparse updates. By selectively updating only the weights associated with these significant activations, LongAct achieves an approximate 8% improvement on LongBench v2 and enhances generalization on the RULER benchmark. Furthermore, our method exhibits remarkable universality, consistently boosting performance across diverse RL algorithms such as GRPO and DAPO. Extensive ablation studies suggest that focusing on these salient features is key to unlocking long-context potential.
匹配关键词: GRPO
---

[ACADEMIC - ARXIV]
标题: Beyond Importance Sampling: Rejection-Gated Policy Optimization
作者: Ziwu Sun, Zhen Gao, Jiyong Zhang, Jiaheng Li
链接: https://arxiv.org/abs/2604.14895v1
完整摘要: We propose a new perspective on policy optimization: rather than reweighting all samples by their importance ratios, an optimizer should select which samples are trustworthy enough to drive a policy update. Building on this view, we introduce Rejection-Gated Policy Optimization (RGPO), which replaces the importance sampling ratio r_theta = pi_theta / pi_old with a smooth, differentiable acceptance gate alpha_theta(s, a) = g(r_theta(s, a)) in the range [0, 1]. Unlike prior work that applies rejection sampling as a data-level heuristic before training, RGPO elevates rejection to an optimization principle: the gate participates directly in gradient computation and is implicitly updated alongside the policy. RGPO provides a unified framework: the policy gradients of TRPO, PPO, and REINFORCE all correspond to specific choices of the effective gradient weight w(r) = g'(r) * r. We prove that RGPO guarantees finite, bounded gradient variance even when importance sampling ratios are heavy-tailed (where IS variance diverges). We further show that RGPO incurs only a bounded, controllable bias and provides an approximate monotonic policy improvement guarantee analogous to TRPO. RGPO matches PPO in computational cost, requires no second-order optimization, and extends naturally to RLHF-style preference alignment. In online preference fine-tuning of Qwen2.5-1.5B-Instruct on Anthropic HH-RLHF (n = 3 seeds), RGPO uses a dual-ratio gate that anchors learning to both the previous policy and the reference model, achieving a Pareto-dominant outcome: the highest reward among online RL methods (+14.8% vs. PPO-RLHF) and the lowest KL divergence to the reference model (-16.0% vs. PPO-RLHF, -53.1% vs. GRPO).
匹配关键词: GRPO
---

[ACADEMIC - ARXIV]
标题: Beyond Importance Sampling: Rejection-Gated Policy Optimization
作者: Ziwu Sun, Zhen Gao, Jiyong Zhang, Jiaheng Li
链接: https://arxiv.org/abs/2604.14895v1
完整摘要: We propose a new perspective on policy optimization: rather than reweighting all samples by their importance ratios, an optimizer should select which samples are trustworthy enough to drive a policy update. Building on this view, we introduce Rejection-Gated Policy Optimization (RGPO), which replaces the importance sampling ratio r_theta = pi_theta / pi_old with a smooth, differentiable acceptance gate alpha_theta(s, a) = g(r_theta(s, a)) in the range [0, 1]. Unlike prior work that applies rejection sampling as a data-level heuristic before training, RGPO elevates rejection to an optimization principle: the gate participates directly in gradient computation and is implicitly updated alongside the policy. RGPO provides a unified framework: the policy gradients of TRPO, PPO, and REINFORCE all correspond to specific choices of the effective gradient weight w(r) = g'(r) * r. We prove that RGPO guarantees finite, bounded gradient variance even when importance sampling ratios are heavy-tailed (where IS variance diverges). We further show that RGPO incurs only a bounded, controllable bias and provides an approximate monotonic policy improvement guarantee analogous to TRPO. RGPO matches PPO in computational cost, requires no second-order optimization, and extends naturally to RLHF-style preference alignment. In online preference fine-tuning of Qwen2.5-1.5B-Instruct on Anthropic HH-RLHF (n = 3 seeds), RGPO uses a dual-ratio gate that anchors learning to both the previous policy and the reference model, achieving a Pareto-dominant outcome: the highest reward among online RL methods (+14.8% vs. PPO-RLHF) and the lowest KL divergence to the reference model (-16.0% vs. PPO-RLHF, -53.1% vs. GRPO).
匹配关键词: PPO
---

[ACADEMIC - ARXIV]
标题: Aerial Multi-Functional RIS in Fluid Antennas-Aided Full-Duplex Networks: A Self-Optimized Hybrid Deep Reinforcement Learning Approach
作者: Li-Hsiang Shen, Yu-Quan Zheng
链接: https://arxiv.org/abs/2604.14309v2
完整摘要: To address high data traffic demands of sixth-generation (6G) networks, this paper proposes a novel architecture that integrates autonomous aerial vehicles (AAVs) and multi-functional reconfigurable intelligent surfaces (MF-RISs) as AM-RIS in fluid antenna (FA)-assisted full-duplex (FD) networks. The AM-RIS provides hybrid functionalities, including signal reflection, amplification, and energy harvesting (EH), potentially improving both signal coverage and sustainability. Meanwhile, FA facilitates fine-grained spatial adaptability at FD-enabled base station (BS), which complements residual self-interference (SI) suppression. We aim at maximizing the overall energy efficiency (EE) by jointly optimizing transmit DL beamforming at BS, UL user power, configuration of AM-RIS, and positions of the FA and AM-RIS. Owing to the hybrid continuous-discrete parameters and high dimensionality of the intractable problem, we have conceived a self-optimized multi-agent hybrid deep reinforcement learning (DRL) framework (SOHRL), which integrates multi-agent deep Q-networks (DQN) and multi-agent proximal policy optimization (PPO), respectively handling discrete and continuous actions. To enhance self-adaptability, an attention-driven state representation and meta-level hyperparameter optimization are incorporated, enabling multi-agents to autonomously adjust learning hyperparameters. Simulation results validate the effectiveness of the proposed AM-RIS-enabled FA-aided FD networks empowered by SOHRL algorithm. The results reveal that SOHRL outperforms benchmarks of the case without attention mechanism and conventional hybrid/multi-agent/standalone DRL. Moreover, AM-RIS in FD achieves the highest EE compared to half-duplex, conventional rigid antenna arrays, partial EH, and conventional RIS without amplification, highlighting its potential as a compelling solution for EE-aware wireless networks.
匹配关键词: PPO
---

[ACADEMIC - ARXIV]
标题: Beyond Conservative Automated Driving in Multi-Agent Scenarios via Coupled Model Predictive Control and Deep Reinforcement Learning
作者: Saeed Rahmani, Gözde Körpe, Zhenlin, Xu, Bruno Brito, Simeon Craig Calvert, Bart van Arem
链接: https://arxiv.org/abs/2604.13891v1
完整摘要: Automated driving at unsignalized intersections is challenging due to complex multi-vehicle interactions and the need to balance safety and efficiency. Model Predictive Control (MPC) offers structured constraint handling through optimization but relies on hand-crafted rules that often produce overly conservative behavior. Deep Reinforcement Learning (RL) learns adaptive behaviors from experience but often struggles with safety assurance and generalization to unseen environments. In this study, we present an integrated MPC-RL framework to improve navigation performance in multi-agent scenarios. Experiments show that MPC-RL outperforms standalone MPC and end-to-end RL across three traffic-density levels. Collectively, MPC-RL reduces the collision rate by 21% and improves the success rate by 6.5% compared to pure MPC. We further evaluate zero-shot transfer to a highway merging scenario without retraining. Both MPC-based methods transfer substantially better than end-to-end PPO, which highlights the role of the MPC backbone in cross-scenario robustness. The framework also shows faster loss stabilization than end-to-end RL during training, which indicates a reduced learning burden. These results suggest that the integrated approach can improve the balance between safety performance and efficiency in multi-agent intersection scenarios, while the MPC component provides a strong foundation for generalization across driving environments. The implementation code is available open-source.
匹配关键词: PPO
---

[ACADEMIC - ARXIV]
标题: Jump-Start Reinforcement Learning with Vision-Language-Action Regularization
作者: Angelo Moroncelli, Roberto Zanetti, Marco Maccarini, Loris Roveda
链接: https://arxiv.org/abs/2604.13733v1
完整摘要: Reinforcement learning (RL) enables high-frequency, closed-loop control for robotic manipulation, but scaling to long-horizon tasks with sparse or imperfect rewards remains difficult due to inefficient exploration and poor credit assignment. Vision-Language-Action (VLA) models leverage large-scale multimodal pretraining to provide generalist, task-level reasoning, but current limitations hinder their direct use in fast and precise manipulation. In this paper, we propose Vision-Language-Action Jump-Starting (VLAJS), a method that bridges sparse VLA guidance with on-policy RL to improve exploration and learning efficiency. VLAJS treats VLAs as transient sources of high-level action suggestions that bias early exploration and improve credit assignment, while preserving the high-frequency, state-based control of RL. Our approach augments Proximal Policy Optimization (PPO) with a directional action-consistency regularization that softly aligns the RL agent's actions with VLA guidance during early training, without enforcing strict imitation, requiring demonstrations, or relying on continuous teacher queries. VLA guidance is applied sparsely and annealed over time, allowing the agent to adapt online and ultimately surpass the guiding policy. We evaluate VLAJS on six challenging manipulation tasks: lifting, pick-and-place, peg reorientation, peg insertion, poking, and pushing in simulation, and validate a subset on a real Franka Panda robot. VLAJS consistently outperforms PPO and distillation-style baselines in sample efficiency, reducing required environment interactions by over 50% in several tasks. Real-world experiments demonstrate zero-shot sim-to-real transfer and robust execution under clutter, object variation, and external perturbations.
匹配关键词: PPO
---

[ACADEMIC - ARXIV]
标题: Representation over Routing: Overcoming Surrogate Hacking in Multi-Timescale PPO
作者: Jing Sun
链接: https://arxiv.org/abs/2604.13517v1
完整摘要: Temporal credit assignment in reinforcement learning has long been a central challenge. Inspired by the multi-timescale encoding of the dopamine system in neurobiology, recent research has sought to introduce multiple discount factors into Actor-Critic architectures, such as Proximal Policy Optimization (PPO), to balance short-term responses with long-term planning. However, this paper reveals that blindly fusing multi-timescale signals in complex delayed-reward tasks can lead to severe algorithmic pathologies. We systematically demonstrate that exposing a temporal attention routing mechanism to policy gradients results in surrogate objective hacking, while adopting gradient-free uncertainty weighting triggers irreversible myopic degeneration, a phenomenon we term the Paradox of Temporal Uncertainty. To address these issues, we propose a Target Decoupling architecture: on the Critic side, we retain multi-timescale predictions to enforce auxiliary representation learning, while on the Actor side, we strictly isolate short-term signals and update the policy based solely on long-term advantages. Rigorous empirical evaluations across multiple independent random seeds in the LunarLander-v2 environment demonstrate that our proposed architecture achieves statistically significant performance improvements. Without relying on hyperparameter hacking, it consistently surpasses the ''Environment Solved'' threshold with minimal variance, completely eliminates policy collapse, and escapes the hovering local optima that trap single-timescale baselines.
匹配关键词: PPO
---

[ACADEMIC - ARXIV]
标题: Where does output diversity collapse in post-training?
作者: Constantinos Karouzos, Xingwei Tan, Nikolaos Aletras
链接: https://arxiv.org/abs/2604.16027v1
完整摘要: Post-trained language models produce less varied outputs than their base counterparts. This output diversity collapse undermines inference-time scaling methods that rely on varied samples, and risks homogenizing model outputs on creative and value-laden tasks. Prior work attributes collapse to specific post-training methods, without separating the role of training data composition from the method, or the generation format from the model weights. We trace output diversity through three parallel post-training lineages of Olmo 3, Think (chain-of-thought distillation), Instruct (broad multi-source data), and RL-Zero, across 15 tasks and four text diversity metrics. We find that the location of collapse co-varies with data composition: the Think lineage loses most semantic diversity at supervised fine-tuning, and the effect of DPO is larger in Instruct than in Think. Suppressing chain-of-thought reasoning at inference in Think models drops accuracy on hard tasks, yet leaves answer-level diversity unchanged, showing that the collapse is embedded in the model weights by training data, not imposed by the generation format. Decomposing diversity loss on six verifiable tasks into a quality-control component (removal of incorrect outputs) and a residual component (genuine narrowing among correct outputs) reveals that the split is task-dependent, and Think models retain more correct-answer diversity than Instruct despite collapsing more in aggregate. Our results indicate that diversity collapse is determined during training by data composition and cannot be addressed at inference time alone.
匹配关键词: DPO
---

[ACADEMIC - ARXIV]
标题: RaTA-Tool: Retrieval-based Tool Selection with Multimodal Large Language Models
作者: Gabriele Mattioli, Evelyn Turri, Sara Sarto, Lorenzo Baraldi, Marcella Cornia, Lorenzo Baraldi, Rita Cucchiara
链接: https://arxiv.org/abs/2604.14951v1
完整摘要: Tool learning with foundation models aims to endow AI systems with the ability to invoke external resources -- such as APIs, computational utilities, and specialized models -- to solve complex tasks beyond the reach of standalone language generation. While recent advances in Large Language Models (LLMs) and Multimodal Large Language Models (MLLMs) have expanded their reasoning and perception capabilities, existing tool-use methods are predominantly limited to text-only inputs and closed-world settings. Consequently, they struggle to interpret multimodal user instructions and cannot generalize to tools unseen during training. In this work, we introduce RaTA-Tool, a novel framework for open-world multimodal tool selection. Rather than learning direct mappings from user queries to fixed tool identifiers, our approach enables an MLLM to convert a multimodal query into a structured task description and subsequently retrieve the most appropriate tool by matching this representation against semantically rich, machine-readable tool descriptions. This retrieval-based formulation naturally supports extensibility to new tools without retraining. To further improve alignment between task descriptions and tool selection, we incorporate a preference-based optimization stage using Direct Preference Optimization (DPO). To support research in this setting, we also introduce the first dataset for open-world multimodal tool use, featuring standardized tool descriptions derived from Hugging Face model cards. Extensive experiments demonstrate that our approach significantly improves tool-selection performance, particularly in open-world, multimodal scenarios.
匹配关键词: DPO
---

[ACADEMIC - ARXIV]
标题: DharmaOCR: Specialized Small Language Models for Structured OCR that outperform Open-Source and Commercial Baselines
作者: Gabriel Pimenta de Freitas Cardoso, Caio Lucas da Silva Chacon, Jonas Felipe da Fonseca Oliveira, Paulo Henrique de Medeiros Araujo
链接: https://arxiv.org/abs/2604.14314v1
完整摘要: This manuscript introduces DharmaOCR Full and Lite, a pair of specialized small language models (SSLMs) for structured OCR that jointly optimize transcription quality, generation stability, and inference cost. It also presents DharmaOCR-Benchmark, a benchmark that covers printed, handwritten, and legal/administrative documents, and proposes a unified evaluation protocol that measures fidelity and structure while explicitly tracking text degeneration as a first-class benchmark metric (alongside unit cost). Beyond reporting degeneration rates, the manuscript empirically shows degeneration is not merely a quality failure, since it materially worsens production performance by increasing response time, reducing throughput, and inflating computational cost due to abnormally long generations. To the best of the author's knowledge, as a methodological contribution, this is the first application of Direct Preference Optimization (DPO) for OCR, explicitly using degenerate generations as rejected examples to penalize looping behavior. Combined with Supervised Fine-Tuning (SFT) for enforcing a strict JSON schema (header, margin, footer, and text), DPO consistently reduces degeneration rate across model families (up to 87.6% relative) while preserving or improving extraction quality. The resulting models, namely, DharmaOCR Full (7B) and DharmaOCR Lite (3B), set a new state-of-the-art on DharmaOCR-Benchmark, outperforming each open-source and commercial baseline model evaluated regarding extraction quality, reaching 0.925 and 0.911 scores with 0.40% and 0.20% degeneration rates. AWQ quantization reduced up to 22% per-page cost with negligible quality loss, enabling a strong quality-cost trade-off in comparison to proprietary OCR APIs and open-source alternatives.
匹配关键词: DPO
---

[ACADEMIC - ARXIV]
标题: Visual Preference Optimization with Rubric Rewards
作者: Ya-Qi Yu, Fangyu Hong, Xiangyang Qu, Hao Wang, Gaojie Wu, Qiaoyu Luo, Nuo Xu, Huixin Wang, Wuheng Xu, Yongxin Liao, Zihao Chen, Haonan Li, Ziming Li, Dezhi Peng, Minghui Liao, Jihao Wu, Haoyu Ren, Dandan Tu
链接: https://arxiv.org/abs/2604.13029v1
完整摘要: The effectiveness of Direct Preference Optimization (DPO) depends on preference data that reflect the quality differences that matter in multimodal tasks. Existing pipelines often rely on off-policy perturbations or coarse outcome-based signals, which are not well suited to fine-grained visual reasoning. We propose rDPO, a preference optimization framework based on instance-specific rubrics. For each image-instruction pair, we create a checklist-style rubric of essential and additional criteria to score responses from any possible policies. The instruction-rubric pool is built offline and reused during the construction of on-policy data. On public reward modeling benchmarks, rubric-based prompting massively improves a 30B-A3B judge and brings it close to GPT-5.4. On public downstream benchmarks, rubric-based filtering raises the macro average to 82.69, whereas outcome-based filtering drops it to 75.82 from 81.14. When evaluating scalability on a comprehensive benchmark, rDPO achieves 61.01, markedly outperforming the style-constrained baseline (52.36) and surpassing the 59.48 base model. Together, these results show that visual preference optimization benefits from combining on-policy data construction with instance-specific criterion-level feedback.
匹配关键词: DPO
---

[ACADEMIC - ARXIV]
标题: Meet Dynamic Individual Preferences: Resolving Conflicting Human Value with Paired Fine-Tuning
作者: Shanyong Wang, Shuhang Lin, Yining Zhao, Xi Zhu, Yongfeng Zhang
链接: https://arxiv.org/abs/2604.12479v1
完整摘要: Recent advances in large language models (LLMs) have significantly improved the alignment of models with general human preferences. However, a major challenge remains in adapting LLMs to individual preferences, which are not only diverse but also dynamic. In this paper, we introduce a novel framework, Preference-Paired Fine-Tuning (PFT), designed to align models with contradictory and evolving individual preferences. We present a new dataset, Value Conflict Dilemma (VCD), which includes scenarios that involve conflicting human preferences, facilitating the evaluation of our approach. Our experiments demonstrate that PFT outperforms single-preference training methods, achieving up to 96.6% accuracy in multi-choice classification tasks and the highest open-ended generation score of 8.69. PFT also shows significant improvements over DPO, SFT and some traditional training methods, especially when handling conflicting preferences. Additionally, with limited user history data, models can inferring preference vector rapidly, achieving a 44.76% improvement in user-specific preference alignment in comparison to single-preference models.
匹配关键词: DPO
---

[ACADEMIC - ARXIV]
标题: Evaluating the Progression of Large Language Model Capabilities for Small-Molecule Drug Design
作者: Shriram Chennakesavalu, Kirill Shmilovich, Hayley Weir, Colin Grambow, John Bradshaw, Patricia Suriana, Chen Cheng, Kangway Chuang
链接: https://arxiv.org/abs/2604.16279v1
完整摘要: Large Language Models (LLMs) have the potential to accelerate small molecule drug design due to their ability to reason about information from diverse sources and formats. However, their practical utility remains unclear due to the lack of benchmarks that reflect real-world scenarios. In this work, we introduce a suite of chemically-grounded tasks spanning molecular property prediction, molecular representation transformations, and molecular design. Importantly, we formulate these tasks as reinforcement learning (RL) environments, enabling a unified approach for evaluation and post-training. Across three model families, we find that frontier models are increasingly proficient at chemical tasks, but that there is significant room for improvement, especially in experimental settings with low data. Critically, we show that RL-based post-training can substantially improve performance. A smaller model post-trained on our environments becomes competitive with state-of-the-art frontier models, despite a significantly weaker base model. This suggests a practical route toward employing LLMs in drug discovery; by combining carefully-designed evaluation tasks with targeted post-training, we can both elucidate and close critical capability gaps.
匹配关键词: reasoning
---

[ACADEMIC - ARXIV]
标题: Learning to Reason with Insight for Informal Theorem Proving
作者: Yunhe Li, Hao Shi, Bowen Deng, Wei Wang, Mengzhe Ruan, Hanxu Hou, Zhongxiang Dai, Siyang Gao, Chao Wang, Shuang Qiu, Linqi Song
链接: https://arxiv.org/abs/2604.16278v1
完整摘要: Although most of the automated theorem-proving approaches depend on formal proof systems, informal theorem proving can align better with large language models' (LLMs) strength in natural language processing. In this work, we identify a primary bottleneck in informal theorem proving as a lack of insight, namely the difficulty of recognizing the core techniques required to solve complex problems. To address this, we propose a novel framework designed to cultivate this essential reasoning skill and enable LLMs to perform insightful reasoning. We propose $\mathtt{DeepInsightTheorem}$, a hierarchical dataset that structures informal proofs by explicitly extracting core techniques and proof sketches alongside the final proof. To fully exploit this dataset, we design a Progressive Multi-Stage SFT strategy that mimics the human learning process, guiding the model from basic proof writing to insightful thinking. Our experiments on challenging mathematical benchmarks demonstrate that this insight-aware generation strategy significantly outperforms baselines. These results demonstrate that teaching models to identify and apply core techniques can substantially improve their mathematical reasoning.
匹配关键词: reasoning
---

[ACADEMIC - ARXIV]
标题: From Benchmarking to Reasoning: A Dual-Aspect, Large-Scale Evaluation of LLMs on Vietnamese Legal Text
作者: Van-Truong Le
链接: https://arxiv.org/abs/2604.16270v1
完整摘要: The complexity of Vietnam's legal texts presents a significant barrier to public access to justice. While Large Language Models offer a promising solution for legal text simplification, evaluating their true capabilities requires a multifaceted approach that goes beyond surface-level metrics. This paper introduces a comprehensive dual-aspect evaluation framework to address this need. First, we establish a performance benchmark for four state-of-the-art large language models (GPT-4o, Claude 3 Opus, Gemini 1.5 Pro, and Grok-1) across three key dimensions: Accuracy, Readability, and Consistency. Second, to understand the "why" behind these performance scores, we conduct a large-scale error analysis on a curated dataset of 60 complex Vietnamese legal articles, using a novel, expert-validated error typology. Our results reveal a crucial trade-off: models like Grok-1 excel in Readability and Consistency but compromise on fine-grained legal Accuracy, while models like Claude 3 Opus achieve high Accuracy scores that mask a significant number of subtle but critical reasoning errors. The error analysis pinpoints \textit{Incorrect Example} and \textit{Misinterpretation} as the most prevalent failures, confirming that the primary challenge for current LLMs is not summarization but controlled, accurate legal reasoning. By integrating a quantitative benchmark with a qualitative deep dive, our work provides a holistic and actionable assessment of LLMs for legal applications.
匹配关键词: reasoning
---

[ACADEMIC - ARXIV]
标题: Information Router for Mitigating Modality Dominance in Vision-Language Models
作者: Seulgi Kim, Mohit Prabhushankar, Ghassan AlRegib
链接: https://arxiv.org/abs/2604.16264v1
完整摘要: Vision Language models (VLMs) have demonstrated strong performance across a wide range of benchmarks, yet they often suffer from modality dominance, where predictions rely disproportionately on a single modality. Prior approaches primarily address this issue by steering model's attention allocation, implicitly assuming that all modalities provide sufficient information. However, attention only determines where the model focuses, and cannot enrich information that is missing or ambiguous. In the real world, input modalities often differ in information density and their signal-to-noise ratios. In such cases, simply adjusting model's attention does not resolve the underlying lack of information. In this paper, we propose \textsc{MoIR}: \textit{Multi-modal Information Router}, an information-level fusion method that explicitly reduces information disparity prior to fusion. \textsc{MoIR} identifies less informative tokens and routes complementary information from a stronger modality, constructing information-dense token representations before they are processed by a large language model. By modifying information availability, \textsc{MoIR} enables reliable shifts in modality dominance, even when one modality is degraded. We evaluate \textsc{MoIR} on three widely used multi-modal benchmarks across multiple model backbones. Experimental results show that \textsc{MoIR} consistently demonstrates more balanced modality contribution, and improves robustness and downstream performance, particularly even under modality degradation. These findings demonstrate that explicitly modifying cross-modal information is an effective and complementary strategy for mitigating modality dominance in multi-modal reasoning models.
匹配关键词: reasoning
---

[ACADEMIC - ARXIV]
标题: SwanNLP at SemEval-2026 Task 5: An LLM-based Framework for Plausibility Scoring in Narrative Word Sense Disambiguation
作者: Deshan Sumanathilaka, Nicholas Micallef, Julian Hough, Saman Jayasinghe
链接: https://arxiv.org/abs/2604.16262v1
完整摘要: Recent advances in language models have substantially improved Natural Language Understanding (NLU). Although widely used benchmarks suggest that Large Language Models (LLMs) can effectively disambiguate, their practical applicability in real-world narrative contexts remains underexplored. SemEval-2026 Task 5 addresses this gap by introducing a task that predicts the human-perceived plausibility of a word sense within a short story. In this work, we propose an LLM-based framework for plausibility scoring of homonymous word senses in narrative texts using a structured reasoning mechanism. We examine the impact of fine-tuning low-parameter LLMs with diverse reasoning strategies, alongside dynamic few-shot prompting for large-parameter models, on accurate sense identification and plausibility estimation. Our results show that commercial large-parameter LLMs with dynamic few-shot prompting closely replicate human-like plausibility judgments. Furthermore, model ensembling slightly improves performance, better simulating the agreement patterns of five human annotators compared to single-model predictions
匹配关键词: reasoning
---

[ACADEMIC - ARXIV]
标题: Learning to Reason with Insight for Informal Theorem Proving
作者: Yunhe Li, Hao Shi, Bowen Deng, Wei Wang, Mengzhe Ruan, Hanxu Hou, Zhongxiang Dai, Siyang Gao, Chao Wang, Shuang Qiu, Linqi Song
链接: https://arxiv.org/abs/2604.16278v1
完整摘要: Although most of the automated theorem-proving approaches depend on formal proof systems, informal theorem proving can align better with large language models' (LLMs) strength in natural language processing. In this work, we identify a primary bottleneck in informal theorem proving as a lack of insight, namely the difficulty of recognizing the core techniques required to solve complex problems. To address this, we propose a novel framework designed to cultivate this essential reasoning skill and enable LLMs to perform insightful reasoning. We propose $\mathtt{DeepInsightTheorem}$, a hierarchical dataset that structures informal proofs by explicitly extracting core techniques and proof sketches alongside the final proof. To fully exploit this dataset, we design a Progressive Multi-Stage SFT strategy that mimics the human learning process, guiding the model from basic proof writing to insightful thinking. Our experiments on challenging mathematical benchmarks demonstrate that this insight-aware generation strategy significantly outperforms baselines. These results demonstrate that teaching models to identify and apply core techniques can substantially improve their mathematical reasoning.
匹配关键词: alignment
---

[ACADEMIC - ARXIV]
标题: VEFX-Bench: A Holistic Benchmark for Generic Video Editing and Visual Effects
作者: Xiangbo Gao, Sicong Jiang, Bangya Liu, Xinghao Chen, Minglai Yang, Siyuan Yang, Mingyang Wu, Jiongze Yu, Qi Zheng, Haozhi Wang, Jiayi Zhang, Jared Yang, Jie Yang, Zihan Wang, Qing Yin, Zhengzhong Tu
链接: https://arxiv.org/abs/2604.16272v1
完整摘要: As AI-assisted video creation becomes increasingly practical, instruction-guided video editing has become essential for refining generated or captured footage to meet professional requirements. Yet the field still lacks both a large-scale human-annotated dataset with complete editing examples and a standardized evaluator for comparing editing systems. Existing resources are limited by small scale, missing edited outputs, or the absence of human quality labels, while current evaluation often relies on expensive manual inspection or generic vision-language model judges that are not specialized for editing quality. We introduce VEFX-Dataset, a human-annotated dataset containing 5,049 video editing examples across 9 major editing categories and 32 subcategories, each labeled along three decoupled dimensions: Instruction Following, Rendering Quality, and Edit Exclusivity. Building on VEFX-Dataset, we propose VEFX-Reward, a reward model designed specifically for video editing quality assessment. VEFX-Reward jointly processes the source video, the editing instruction, and the edited video, and predicts per-dimension quality scores via ordinal regression. We further release VEFX-Bench, a benchmark of 300 curated video-prompt pairs for standardized comparison of editing systems. Experiments show that VEFX-Reward aligns more strongly with human judgments than generic VLM judges and prior reward models on both standard IQA/VQA metrics and group-wise preference evaluation. Using VEFX-Reward as an evaluator, we benchmark representative commercial and open-source video editing systems, revealing a persistent gap between visual plausibility, instruction following, and edit locality in current models.
匹配关键词: alignment
---

[ACADEMIC - ARXIV]
标题: Do Vision-Language Models Truly Perform Vision Reasoning? A Rigorous Study of the Modality Gap
作者: Yige Xu, Yongjie Wang, Zizhuo Wu, Kaisong Song, Jun Lin, Zhiqi Shen
链接: https://arxiv.org/abs/2604.16256v1
完整摘要: Reasoning in vision-language models (VLMs) has recently attracted significant attention due to its broad applicability across diverse downstream tasks. However, it remains unclear whether the superior performance of VLMs stems from genuine vision-grounded reasoning or relies predominantly on the reasoning capabilities of their textual backbones. To systematically measure this, we introduce CrossMath, a novel multimodal reasoning benchmark designed for controlled cross-modal comparisons. Specifically, we construct each problem in text-only, image-only, and image+text formats guaranteeing identical task-relevant information, verified by human annotators. This rigorous alignment effectively isolates modality-specific reasoning differences while eliminating confounding factors such as information mismatch. Extensive evaluation of state-of-the-art VLMs reveals a consistent phenomenon: a substantial performance gap between textual and visual reasoning. Notably, VLMs excel with text-only inputs, whereas incorporating visual data (image+text) frequently degrades performance compared to the text-only baseline. These findings indicate that current VLMs conduct reasoning primarily in the textual space, with limited genuine reliance on visual evidence. To mitigate this limitation, we curate a CrossMath training set for VLM fine-tuning. Empirical evaluations demonstrate that fine-tuning on this training set significantly boosts reasoning performance across all individual and joint modalities, while yielding robust gains on two general visual reasoning tasks. Source code is available at https://github.com/xuyige/CrossMath.
匹配关键词: alignment
---

[ACADEMIC - ARXIV]
标题: Joint-Centric Dual Contrastive Alignment with Structure-Preserving and Information-Balanced Regularization
作者: Habibeh Naderi, Behrouz Haji Soleimani, Stan Matwin
链接: https://arxiv.org/abs/2604.16247v1
完整摘要: We propose HILBERT (HIerarchical Long-sequence Balanced Embedding with Reciprocal contrastive Training), a cross-attentive multimodal framework for learning document-level audio-text representations from long, segmented sequences in low-resource data settings. HILBERT leverages frozen pre-trained speech and language encoders to extract segment-level features, which are aggregated via cross-modal attention and self-attentive pooling to form modality-specific document representations and a joint cross-attentive embedding. To align modalities while preserving modality-specific structure under severe audio-text dimensional imbalance, we introduce a reciprocal dual contrastive objective that simultaneously aligns audio-to-joint and text-to-joint representations, rather than directly contrasting audio and text alone. Two auxiliary regularizers further stabilize long-sequence fusion: a Centered Kernel Alignment (CKA) loss that preserves structural consistency between each modality and the joint embedding, and a mutual information balancing loss that prevents dominance of a single modality by equalizing information flow from audio and text into the joint space. For downstream prediction, HILBERT employs a Mixture-of-Experts (MoE) classifier over concatenated audio, text, and joint representations to accommodate heterogeneous label regimes. Extensive evaluation across multiple audio-text backbone combinations demonstrates that HILBERT learns semantically meaningful long-sequence representations and achieves superior performance on highly imbalanced multi-class settings.
匹配关键词: alignment
---

[ACADEMIC - ARXIV]
标题: AIFIND: Artifact-Aware Interpreting Fine-Grained Alignment for Incremental Face Forgery Detection
作者: Hao Wang, Beichen Zhang, Yanpei Gong, Shaoyi Fang, Zhaobo Qi, Yuanrong Xu, Xinyan Liu, Weigang Zhang
链接: https://arxiv.org/abs/2604.16207v1
完整摘要: As forgery types continue to emerge consistently, Incremental Face Forgery Detection (IFFD) has become a crucial paradigm. However, existing methods typically rely on data replay or coarse binary supervision, which fails to explicitly constrain the feature space, leading to severe feature drift and catastrophic forgetting. To address this, we propose AIFIND, Artifact-Aware Interpreting Fine-Grained Alignment for Incremental Face Forgery Detection, which leverages semantic anchors to stabilize incremental learning. We design the Artifact-Driven Semantic Prior Generator to instantiate invariant semantic anchors, establishing a fixed coordinate system from low-level artifact cues. These anchors are injected into the image encoder via Artifact-Probe Attention, which explicitly constrains volatile visual features to align with stable semantic anchors. Adaptive Decision Harmonizer harmonizes the classifiers by preserving angular relationships of semantic anchors, maintaining geometric consistency across tasks. Extensive experiments on multiple incremental protocols validate the superiority of AIFIND.
匹配关键词: alignment
---

[ACADEMIC - ARXIV]
标题: Using Large Language Models and Knowledge Graphs to Improve the Interpretability of Machine Learning Models in Manufacturing
作者: Thomas Bayer, Alexander Lohr, Sarah Weiß, Bernd Michelberger, Wolfram Höpken
链接: https://arxiv.org/abs/2604.16280v1
完整摘要: Explaining Machine Learning (ML) results in a transparent and user-friendly manner remains a challenging task of Explainable Artificial Intelligence (XAI). In this paper, we present a method to enhance the interpretability of ML models by using a Knowledge Graph (KG). We store domain-specific data along with ML results and their corresponding explanations, establishing a structured connection between domain knowledge and ML insights. To make these insights accessible to users, we designed a selective retrieval method in which relevant triplets are extracted from the KG and processed by a Large Language Model (LLM) to generate user-friendly explanations of ML results. We evaluated our method in a manufacturing environment using the XAI Question Bank. Beyond standard questions, we introduce more complex, tailored questions that highlight the strengths of our approach. We evaluated 33 questions, analyzing responses using quantitative metrics such as accuracy and consistency, as well as qualitative ones such as clarity and usefulness. Our contribution is both theoretical and practical: from a theoretical perspective, we present a novel approach for effectively enabling LLMs to dynamically access a KG in order to improve the explainability of ML results. From a practical perspective, we provide empirical evidence showing that such explanations can be successfully applied in real-world manufacturing environments, supporting better decision-making in manufacturing processes.
匹配关键词: reward model
---

[ACADEMIC - ARXIV]
标题: Evaluating the Progression of Large Language Model Capabilities for Small-Molecule Drug Design
作者: Shriram Chennakesavalu, Kirill Shmilovich, Hayley Weir, Colin Grambow, John Bradshaw, Patricia Suriana, Chen Cheng, Kangway Chuang
链接: https://arxiv.org/abs/2604.16279v1
完整摘要: Large Language Models (LLMs) have the potential to accelerate small molecule drug design due to their ability to reason about information from diverse sources and formats. However, their practical utility remains unclear due to the lack of benchmarks that reflect real-world scenarios. In this work, we introduce a suite of chemically-grounded tasks spanning molecular property prediction, molecular representation transformations, and molecular design. Importantly, we formulate these tasks as reinforcement learning (RL) environments, enabling a unified approach for evaluation and post-training. Across three model families, we find that frontier models are increasingly proficient at chemical tasks, but that there is significant room for improvement, especially in experimental settings with low data. Critically, we show that RL-based post-training can substantially improve performance. A smaller model post-trained on our environments becomes competitive with state-of-the-art frontier models, despite a significantly weaker base model. This suggests a practical route toward employing LLMs in drug discovery; by combining carefully-designed evaluation tasks with targeted post-training, we can both elucidate and close critical capability gaps.
匹配关键词: reward model
---

[ACADEMIC - ARXIV]
标题: Learning to Reason with Insight for Informal Theorem Proving
作者: Yunhe Li, Hao Shi, Bowen Deng, Wei Wang, Mengzhe Ruan, Hanxu Hou, Zhongxiang Dai, Siyang Gao, Chao Wang, Shuang Qiu, Linqi Song
链接: https://arxiv.org/abs/2604.16278v1
完整摘要: Although most of the automated theorem-proving approaches depend on formal proof systems, informal theorem proving can align better with large language models' (LLMs) strength in natural language processing. In this work, we identify a primary bottleneck in informal theorem proving as a lack of insight, namely the difficulty of recognizing the core techniques required to solve complex problems. To address this, we propose a novel framework designed to cultivate this essential reasoning skill and enable LLMs to perform insightful reasoning. We propose $\mathtt{DeepInsightTheorem}$, a hierarchical dataset that structures informal proofs by explicitly extracting core techniques and proof sketches alongside the final proof. To fully exploit this dataset, we design a Progressive Multi-Stage SFT strategy that mimics the human learning process, guiding the model from basic proof writing to insightful thinking. Our experiments on challenging mathematical benchmarks demonstrate that this insight-aware generation strategy significantly outperforms baselines. These results demonstrate that teaching models to identify and apply core techniques can substantially improve their mathematical reasoning.
匹配关键词: reward model
---

[ACADEMIC - ARXIV]
标题: No Universal Courtesy: A Cross-Linguistic, Multi-Model Study of Politeness Effects on LLMs Using the PLUM Corpus
作者: Hitesh Mehta, Arjit Saxena, Garima Chhikara, Rohit Kumar
链接: https://arxiv.org/abs/2604.16275v1
完整摘要: This paper explores the response of Large Language Models (LLMs) to user prompts with different degrees of politeness and impoliteness. The Politeness Theory by Brown and Levinson and the Impoliteness Framework by Culpeper form the basis of experiments conducted across three languages (English, Hindi, Spanish), five models (Gemini-Pro, GPT-4o Mini, Claude 3.7 Sonnet, DeepSeek-Chat, and Llama 3), and three interaction histories between users (raw, polite, and impolite). Our sample consists of 22,500 pairs of prompts and responses of various types, evaluated across five levels of politeness using an eight-factor assessment framework: coherence, clarity, depth, responsiveness, context retention, toxicity, conciseness, and readability. The findings show that model performance is highly influenced by tone, dialogue history, and language. While polite prompts enhance the average response quality by up to ~11% and impolite tones worsen it, these effects are neither consistent nor universal across languages and models. English is best served by courteous or direct tones, Hindi by deferential and indirect tones, and Spanish by assertive tones. Among the models, Llama is the most tone-sensitive (11.5% range), whereas GPT is more robust to adversarial tone. These results indicate that politeness is a quantifiable computational variable that affects LLM behaviour, though its impact is language- and model-dependent rather than universal. To support reproducibility and future work, we additionally release PLUM (Politeness Levels in Utterances, Multilingual), a publicly available corpus of 1,500 human-validated prompts across three languages and five politeness categories, and provide a formal supplementary analysis of six falsifiable hypotheses derived from politeness theory, empirically assessed against the dataset.
匹配关键词: reward model
---

[ACADEMIC - ARXIV]
标题: VEFX-Bench: A Holistic Benchmark for Generic Video Editing and Visual Effects
作者: Xiangbo Gao, Sicong Jiang, Bangya Liu, Xinghao Chen, Minglai Yang, Siyuan Yang, Mingyang Wu, Jiongze Yu, Qi Zheng, Haozhi Wang, Jiayi Zhang, Jared Yang, Jie Yang, Zihan Wang, Qing Yin, Zhengzhong Tu
链接: https://arxiv.org/abs/2604.16272v1
完整摘要: As AI-assisted video creation becomes increasingly practical, instruction-guided video editing has become essential for refining generated or captured footage to meet professional requirements. Yet the field still lacks both a large-scale human-annotated dataset with complete editing examples and a standardized evaluator for comparing editing systems. Existing resources are limited by small scale, missing edited outputs, or the absence of human quality labels, while current evaluation often relies on expensive manual inspection or generic vision-language model judges that are not specialized for editing quality. We introduce VEFX-Dataset, a human-annotated dataset containing 5,049 video editing examples across 9 major editing categories and 32 subcategories, each labeled along three decoupled dimensions: Instruction Following, Rendering Quality, and Edit Exclusivity. Building on VEFX-Dataset, we propose VEFX-Reward, a reward model designed specifically for video editing quality assessment. VEFX-Reward jointly processes the source video, the editing instruction, and the edited video, and predicts per-dimension quality scores via ordinal regression. We further release VEFX-Bench, a benchmark of 300 curated video-prompt pairs for standardized comparison of editing systems. Experiments show that VEFX-Reward aligns more strongly with human judgments than generic VLM judges and prior reward models on both standard IQA/VQA metrics and group-wise preference evaluation. Using VEFX-Reward as an evaluator, we benchmark representative commercial and open-source video editing systems, revealing a persistent gap between visual plausibility, instruction following, and edit locality in current models.
匹配关键词: reward model
---

[ACADEMIC - ARXIV]
标题: Beyond Distribution Sharpening: The Importance of Task Rewards
作者: Sarthak Mittal, Leo Gagnon, Guillaume Lajoie
链接: https://arxiv.org/abs/2604.16259v1
完整摘要: Frontier models have demonstrated exceptional capabilities following the integration of task-reward-based reinforcement learning (RL) into their training pipelines, enabling systems to evolve from pure reasoning models into sophisticated agents. However, debate persists regarding whether RL genuinely instills new skills within a base model or merely sharpens its existing distribution to elicit latent capabilities. To address this dichotomy, we present an explicit comparison between distribution sharpening and task-reward-based learning, utilizing RL as a tool to implement both paradigms. Our analysis reveals the inherent limitations of distribution sharpening, demonstrating from first principles how and why the optima can be unfavorable and the approach fundamentally unstable. Furthermore, our experiments using Llama-3.2-3B-Instruct, Qwen2.5-3B-Instruct and Qwen3-4B-Instruct-2507 on math datasets confirm that sharpening yields limited gains, whereas incorporating task-based reward signal can greatly help achieve robust performance improvements and stable learning.
匹配关键词: agent
---

[ACADEMIC - ARXIV]
标题: ChemGraph-XANES: An Agentic Framework for XANES Simulation and Analysis
作者: Vitor F. Grizzi, Thang Duc Pham, Luke N. Pretzie, Jiayi Xu, Murat Keceli, Cong Liu
链接: https://arxiv.org/abs/2604.16205v1
完整摘要: Computational X-ray absorption near-edge structure (XANES) is widely used to probe local coordination environments, oxidation states, and electronic structure in chemically complex systems. However, the use of computational XANES at scale is constrained more by workflow complexity than by the underlying simulation method itself. To address this challenge, we present ChemGraph-XANES, an agentic framework for automated XANES simulation and analysis that unifies natural-language task specification, structure acquisition, FDMNES input generation, task-parallel execution, spectral normalization, and provenance-aware data curation. Built on ASE, FDMNES, Parsl, and a LangGraph/LangChain-based tool interface, the framework exposes XANES workflow operations as typed Python tools that can be orchestrated by large language model (LLM) agents. In multi-agent mode, a retrieval-augmented expert agent consults the FDMNES manual to ground parameter selection, while executor agents translate user requests into structured tool calls. We demonstrate documentation-grounded parameter retrieval and show that the same workflow supports both explicit structure-file inputs and chemistry-level natural-language requests. Because independent XANES calculations are naturally task-parallel, the framework is well suited for high-throughput deployment on high-performance computing (HPC) systems, enabling scalable XANES database generation for downstream analysis and machine-learning applications. ChemGraph-XANES thus provides a reproducible and extensible workflow layer for physics-based XANES simulation, spectral curation, and agent-compatible computational spectroscopy.
匹配关键词: agent
---

[ACADEMIC - ARXIV]
标题: MARCH: Multi-Agent Radiology Clinical Hierarchy for CT Report Generation
作者: Yi Lin, Yihao Ding, Yonghui Wu, Yifan Peng
链接: https://arxiv.org/abs/2604.16175v1
完整摘要: Automated 3D radiology report generation often suffers from clinical hallucinations and a lack of the iterative verification found in human practice. While recent Vision-Language Models (VLMs) have advanced the field, they typically operate as monolithic "black-box" systems without the collaborative oversight characteristic of clinical workflows. To address these challenges, we propose MARCH (Multi-Agent Radiology Clinical Hierarchy), a multi-agent framework that emulates the professional hierarchy of radiology departments and assigns specialized roles to distinct agents. MARCH utilizes a Resident Agent for initial drafting with multi-scale CT feature extraction, multiple Fellow Agents for retrieval-augmented revision, and an Attending Agent that orchestrates an iterative, stance-based consensus discourse to resolve diagnostic discrepancies. On the RadGenome-ChestCT dataset, MARCH significantly outperforms state-of-the-art baselines in both clinical fidelity and linguistic accuracy. Our work demonstrates that modeling human-like organizational structures enhances the reliability of AI in high-stakes medical domains.
匹配关键词: agent
---

[ACADEMIC - ARXIV]
标题: SocialGrid: A Benchmark for Planning and Social Reasoning in Embodied Multi-Agent Systems
作者: Hikaru Shindo, Hanzhao Lin, Lukas Helff, Patrick Schramowski, Kristian Kersting
链接: https://arxiv.org/abs/2604.16022v1
完整摘要: As Large Language Models (LLMs) transition from text processors to autonomous agents, evaluating their social reasoning in embodied multi-agent settings becomes critical. We introduce SocialGrid, an embodied multi-agent environment inspired by Among Us that evaluates LLM agents on planning, task execution, and social reasoning. Our evaluations reveal that even the strongest open model (GPT-OSS-120B) achieves below 60% accuracy in task completion and planning, with agents getting stuck in repetitive behaviors or failing to navigate basic obstacles. Since poor navigation confounds evaluation of social intelligence, SocialGrid offers an optional Planning Oracle to isolate social reasoning from planning deficits. While planning assistance improves task completion, social reasoning remains a bottleneck: agents fail to detect deception at near-random chance regardless of scale, relying on shallow heuristics rather than accumulating behavioral evidence. SocialGrid provides automatic failure analysis and fine-grained metrics, enabling developers to diagnose and improve their agents. We also establish a competitive leaderboard using Elo ratings from adversarial league play.
匹配关键词: agent
---

[ACADEMIC - ARXIV]
标题: Neurosymbolic Repo-level Code Localization
作者: Xiufeng Xu, Xiufeng Wu, Zejun Zhang, Yi Li
链接: https://arxiv.org/abs/2604.16021v1
完整摘要: Code localization is a cornerstone of autonomous software engineering. Recent advancements have achieved impressive performance on real-world issue benchmarks. However, we identify a critical yet overlooked bias: these benchmarks are saturated with keyword references (e.g. file paths, function names), encouraging models to rely on superficial lexical matching rather than genuine structural reasoning. We term this phenomenon the Keyword Shortcut. To address this, we formalize the challenge of Keyword-Agnostic Logical Code Localization (KA-LCL) and introduce KA-LogicQuery, a diagnostic benchmark requiring structural reasoning without any naming hints. Our evaluation reveals a catastrophic performance drop of state-of-the-art approaches on KA-LogicQuery, exposing their lack of deterministic reasoning capabilities. We propose LogicLoc, a novel agentic framework that combines large language models with the rigorous logical reasoning of Datalog for precise localization. LogicLoc extracts program facts from the codebase and leverages an LLM to synthesize Datalog programs, with parser-gated validation and mutation-based intermediate-rule diagnostic feedback to ensure correctness and efficiency. The validated programs are executed by a high-performance inference engine, enabling accurate and verifiable localization in a fully automated, closed-loop workflow. Experimental results demonstrate that LogicLoc significantly outperforms SOTA methods on KA-LogicQuery while maintaining competitive performance on popular issue-driven benchmarks. Notably, LogicLoc attains superior performance with significantly lower token consumption and faster execution by offloading structural traversal to a deterministic engine, reducing the overhead of iterative LLM inference.
匹配关键词: agent
---

[ACADEMIC - ARXIV]
标题: ChemGraph-XANES: An Agentic Framework for XANES Simulation and Analysis
作者: Vitor F. Grizzi, Thang Duc Pham, Luke N. Pretzie, Jiayi Xu, Murat Keceli, Cong Liu
链接: https://arxiv.org/abs/2604.16205v1
完整摘要: Computational X-ray absorption near-edge structure (XANES) is widely used to probe local coordination environments, oxidation states, and electronic structure in chemically complex systems. However, the use of computational XANES at scale is constrained more by workflow complexity than by the underlying simulation method itself. To address this challenge, we present ChemGraph-XANES, an agentic framework for automated XANES simulation and analysis that unifies natural-language task specification, structure acquisition, FDMNES input generation, task-parallel execution, spectral normalization, and provenance-aware data curation. Built on ASE, FDMNES, Parsl, and a LangGraph/LangChain-based tool interface, the framework exposes XANES workflow operations as typed Python tools that can be orchestrated by large language model (LLM) agents. In multi-agent mode, a retrieval-augmented expert agent consults the FDMNES manual to ground parameter selection, while executor agents translate user requests into structured tool calls. We demonstrate documentation-grounded parameter retrieval and show that the same workflow supports both explicit structure-file inputs and chemistry-level natural-language requests. Because independent XANES calculations are naturally task-parallel, the framework is well suited for high-throughput deployment on high-performance computing (HPC) systems, enabling scalable XANES database generation for downstream analysis and machine-learning applications. ChemGraph-XANES thus provides a reproducible and extensible workflow layer for physics-based XANES simulation, spectral curation, and agent-compatible computational spectroscopy.
匹配关键词: multi-agent
---

[ACADEMIC - ARXIV]
标题: MARCH: Multi-Agent Radiology Clinical Hierarchy for CT Report Generation
作者: Yi Lin, Yihao Ding, Yonghui Wu, Yifan Peng
链接: https://arxiv.org/abs/2604.16175v1
完整摘要: Automated 3D radiology report generation often suffers from clinical hallucinations and a lack of the iterative verification found in human practice. While recent Vision-Language Models (VLMs) have advanced the field, they typically operate as monolithic "black-box" systems without the collaborative oversight characteristic of clinical workflows. To address these challenges, we propose MARCH (Multi-Agent Radiology Clinical Hierarchy), a multi-agent framework that emulates the professional hierarchy of radiology departments and assigns specialized roles to distinct agents. MARCH utilizes a Resident Agent for initial drafting with multi-scale CT feature extraction, multiple Fellow Agents for retrieval-augmented revision, and an Attending Agent that orchestrates an iterative, stance-based consensus discourse to resolve diagnostic discrepancies. On the RadGenome-ChestCT dataset, MARCH significantly outperforms state-of-the-art baselines in both clinical fidelity and linguistic accuracy. Our work demonstrates that modeling human-like organizational structures enhances the reliability of AI in high-stakes medical domains.
匹配关键词: multi-agent
---

[ACADEMIC - ARXIV]
标题: SocialGrid: A Benchmark for Planning and Social Reasoning in Embodied Multi-Agent Systems
作者: Hikaru Shindo, Hanzhao Lin, Lukas Helff, Patrick Schramowski, Kristian Kersting
链接: https://arxiv.org/abs/2604.16022v1
完整摘要: As Large Language Models (LLMs) transition from text processors to autonomous agents, evaluating their social reasoning in embodied multi-agent settings becomes critical. We introduce SocialGrid, an embodied multi-agent environment inspired by Among Us that evaluates LLM agents on planning, task execution, and social reasoning. Our evaluations reveal that even the strongest open model (GPT-OSS-120B) achieves below 60% accuracy in task completion and planning, with agents getting stuck in repetitive behaviors or failing to navigate basic obstacles. Since poor navigation confounds evaluation of social intelligence, SocialGrid offers an optional Planning Oracle to isolate social reasoning from planning deficits. While planning assistance improves task completion, social reasoning remains a bottleneck: agents fail to detect deception at near-random chance regardless of scale, relying on shallow heuristics rather than accumulating behavioral evidence. SocialGrid provides automatic failure analysis and fine-grained metrics, enabling developers to diagnose and improve their agents. We also establish a competitive leaderboard using Elo ratings from adversarial league play.
匹配关键词: multi-agent
---

[ACADEMIC - ARXIV]
标题: AgentV-RL: Scaling Reward Modeling with Agentic Verifier
作者: Jiazheng Zhang, Ziche Fu, Zhiheng Xi, Wenqing Jing, Mingxu Chai, Wei He, Guoqiang Zhang, Chenghao Fan, Chenxin An, Wenxiang Chen, Zhicheng Liu, Haojie Pan, Dingwei Zhu, Tao Gui, Qi Zhang, Xuanjing Huang
链接: https://arxiv.org/abs/2604.16004v1
完整摘要: Verifiers have been demonstrated to enhance LLM reasoning via test-time scaling (TTS). Yet, they face significant challenges in complex domains. Error propagation from incorrect intermediate reasoning can lead to false positives for seemingly plausible solutions, while lacking external grounding makes verifiers unreliable on computation or knowledge-intensive tasks. To address these challenges, we propose Agentic Verifier, a framework that transforms reward modeling into a multi-turn, tool-augmented deliberative process. We introduce complementary forward and backward agents: one traces solutions from premises to conclusions, while the other re-checks conclusions against their underlying premises. This bidirectional process enables a comprehensive, reliable, and interpretable assessment of solutions. To facilitate practical deployment, we propose AgentV-RL. Through proactive exploration and reinforcement learning, the verifier autonomously interleaves tool-use with internal reasoning. Extensive experiments show that Agentic Verifier yields consistent performance gains under both parallel and sequential TTS. Notably, our 4B variant surpasses state-of-the-art ORMs by 25.2%, positioning it as a promising paradigm for agentic reward modeling.
匹配关键词: multi-agent
---

[ACADEMIC - ARXIV]
标题: Weak-Link Optimization for Multi-Agent Reasoning and Collaboration
作者: Haoyu Bian, Chaoning Zhang, Jiaquan Zhang, Xingyao Li, Yuanfang Guo, Wei Dong, Yang Yang
链接: https://arxiv.org/abs/2604.15972v1
完整摘要: LLM-driven multi-agent frameworks address complex reasoning tasks through multi-role collaboration. However, existing approaches often suffer from reasoning instability, where individual agent errors are amplified through collaboration, undermining overall performance. Current research mainly focuses on enhancing high-capability agents or suppressing unreliable outputs to improve framework effectiveness, while systematic identification and reinforcement of performance-limiting agents receive less attention. To address this gap, we propose WORC, a \underline{w}eak-link \underline{o}ptimization framework for multi-agent \underline{r}easoning and \underline{c}ollaboration, grounded in the weak-link principle. WORC follows a two-stage workflow. In the weak agent localization stage, task features are constructed, and a meta-learning-based weight predictor trained on optimal configurations identified by swarm intelligence algorithms (SIAs) enables zero-shot mapping from these features to agent performance weights, where the agent with the lowest predicted weight is identified as the weak agent. In the weak-link optimization stage, an uncertainty-driven allocation strategy assigns additional reasoning budgets to weak agents, with lower predicted weights leading to larger repeated-sampling quotas to compensate for reliability deficiencies. Experimental results show that WORC achieves an average accuracy of 82.2\% on reasoning benchmarks while improving framework stability and cross-architecture generalization, suggesting that compensating for weak links, rather than reinforcing strengths alone, enhances the robustness of multi-agent systems.
匹配关键词: multi-agent
---

[ACADEMIC - ARXIV]
标题: ASMR-Bench: Auditing for Sabotage in ML Research
作者: Eric Gan, Aryan Bhatt, Buck Shlegeris, Julian Stastny, Vivek Hebbar
链接: https://arxiv.org/abs/2604.16286v1
完整摘要: As AI systems are increasingly used to conduct research autonomously, misaligned systems could introduce subtle flaws that produce misleading results while evading detection. We introduce ASMR-Bench (Auditing for Sabotage in ML Research), a benchmark for evaluating the ability of auditors to detect sabotage in ML research codebases. ASMR-Bench consists of 9 ML research codebases with sabotaged variants that produce qualitatively different experimental results. Each sabotage modifies implementation details, such as hyperparameters, training data, or evaluation code, while preserving the high-level methodology described in the paper. We evaluated frontier LLMs and LLM-assisted human auditors on ASMR-Bench and found that both struggled to reliably detect sabotage: the best performance was an AUROC of 0.77 and a top-1 fix rate of 42%, achieved by Gemini 3.1 Pro. We also tested LLMs as red teamers and found that LLM-generated sabotages were weaker than human-generated ones but still sometimes evaded same-capability LLM auditors. We release ASMR-Bench to support research on monitoring and auditing techniques for AI-conducted research.
匹配关键词: tool use
---

[ACADEMIC - ARXIV]
标题: Geometric regularization of autoencoders via observed stochastic dynamics
作者: Sean Hill, Felix X. -F. Ye
链接: https://arxiv.org/abs/2604.16282v1
完整摘要: Stochastic dynamical systems with slow or metastable behavior evolve, on long time scales, on an unknown low-dimensional manifold in high-dimensional ambient space. Building a reduced simulator from short-burst ambient ensembles is a long-standing problem: local-chart methods like ATLAS suffer from exponential landmark scaling and per-step reprojection, while autoencoder alternatives leave tangent-bundle geometry poorly constrained, and the errors propagate into the learned drift and diffusion. We observe that the ambient covariance~$Λ$ already encodes coordinate-invariant tangent-space information, its range spanning the tangent bundle. Using this, we construct a tangent-bundle penalty and an inverse-consistency penalty for a three-stage pipeline (chart learning, latent drift, latent diffusion) that learns a single nonlinear chart and the latent SDE. The penalties induce a function-space metric, the $ρ$-metric, strictly weaker than the Sobolev $H^1$ norm yet achieving the same chart-quality generalization rate up to logarithmic factors. For the drift, we derive an encoder-pullback target via Itô's formula on the learned encoder and prove a bias decomposition showing the standard decoder-side formula carries systematic error for any imperfect chart. Under a $W^{2,\infty}$ chart-convergence assumption, chart-level error propagates controllably to weak convergence of the ambient dynamics and to convergence of radial mean first-passage times. Experiments on four surfaces embedded in up to $201$ ambient dimensions reduce radial MFPT error by $50$--$70\%$ under rotation dynamics and achieve the lowest inter-well MFPT error on most surface--transition pairs under metastable Müller--Brown Langevin dynamics, while reducing end-to-end ambient coefficient errors by up to an order of magnitude relative to an unregularized autoencoder.
匹配关键词: tool use
---

[ACADEMIC - ARXIV]
标题: Using Large Language Models and Knowledge Graphs to Improve the Interpretability of Machine Learning Models in Manufacturing
作者: Thomas Bayer, Alexander Lohr, Sarah Weiß, Bernd Michelberger, Wolfram Höpken
链接: https://arxiv.org/abs/2604.16280v1
完整摘要: Explaining Machine Learning (ML) results in a transparent and user-friendly manner remains a challenging task of Explainable Artificial Intelligence (XAI). In this paper, we present a method to enhance the interpretability of ML models by using a Knowledge Graph (KG). We store domain-specific data along with ML results and their corresponding explanations, establishing a structured connection between domain knowledge and ML insights. To make these insights accessible to users, we designed a selective retrieval method in which relevant triplets are extracted from the KG and processed by a Large Language Model (LLM) to generate user-friendly explanations of ML results. We evaluated our method in a manufacturing environment using the XAI Question Bank. Beyond standard questions, we introduce more complex, tailored questions that highlight the strengths of our approach. We evaluated 33 questions, analyzing responses using quantitative metrics such as accuracy and consistency, as well as qualitative ones such as clarity and usefulness. Our contribution is both theoretical and practical: from a theoretical perspective, we present a novel approach for effectively enabling LLMs to dynamically access a KG in order to improve the explainability of ML results. From a practical perspective, we provide empirical evidence showing that such explanations can be successfully applied in real-world manufacturing environments, supporting better decision-making in manufacturing processes.
匹配关键词: tool use
---

[ACADEMIC - ARXIV]
标题: No Universal Courtesy: A Cross-Linguistic, Multi-Model Study of Politeness Effects on LLMs Using the PLUM Corpus
作者: Hitesh Mehta, Arjit Saxena, Garima Chhikara, Rohit Kumar
链接: https://arxiv.org/abs/2604.16275v1
完整摘要: This paper explores the response of Large Language Models (LLMs) to user prompts with different degrees of politeness and impoliteness. The Politeness Theory by Brown and Levinson and the Impoliteness Framework by Culpeper form the basis of experiments conducted across three languages (English, Hindi, Spanish), five models (Gemini-Pro, GPT-4o Mini, Claude 3.7 Sonnet, DeepSeek-Chat, and Llama 3), and three interaction histories between users (raw, polite, and impolite). Our sample consists of 22,500 pairs of prompts and responses of various types, evaluated across five levels of politeness using an eight-factor assessment framework: coherence, clarity, depth, responsiveness, context retention, toxicity, conciseness, and readability. The findings show that model performance is highly influenced by tone, dialogue history, and language. While polite prompts enhance the average response quality by up to ~11% and impolite tones worsen it, these effects are neither consistent nor universal across languages and models. English is best served by courteous or direct tones, Hindi by deferential and indirect tones, and Spanish by assertive tones. Among the models, Llama is the most tone-sensitive (11.5% range), whereas GPT is more robust to adversarial tone. These results indicate that politeness is a quantifiable computational variable that affects LLM behaviour, though its impact is language- and model-dependent rather than universal. To support reproducibility and future work, we additionally release PLUM (Politeness Levels in Utterances, Multilingual), a publicly available corpus of 1,500 human-validated prompts across three languages and five politeness categories, and provide a formal supplementary analysis of six falsifiable hypotheses derived from politeness theory, empirically assessed against the dataset.
匹配关键词: tool use
---

[ACADEMIC - ARXIV]
标题: VEFX-Bench: A Holistic Benchmark for Generic Video Editing and Visual Effects
作者: Xiangbo Gao, Sicong Jiang, Bangya Liu, Xinghao Chen, Minglai Yang, Siyuan Yang, Mingyang Wu, Jiongze Yu, Qi Zheng, Haozhi Wang, Jiayi Zhang, Jared Yang, Jie Yang, Zihan Wang, Qing Yin, Zhengzhong Tu
链接: https://arxiv.org/abs/2604.16272v1
完整摘要: As AI-assisted video creation becomes increasingly practical, instruction-guided video editing has become essential for refining generated or captured footage to meet professional requirements. Yet the field still lacks both a large-scale human-annotated dataset with complete editing examples and a standardized evaluator for comparing editing systems. Existing resources are limited by small scale, missing edited outputs, or the absence of human quality labels, while current evaluation often relies on expensive manual inspection or generic vision-language model judges that are not specialized for editing quality. We introduce VEFX-Dataset, a human-annotated dataset containing 5,049 video editing examples across 9 major editing categories and 32 subcategories, each labeled along three decoupled dimensions: Instruction Following, Rendering Quality, and Edit Exclusivity. Building on VEFX-Dataset, we propose VEFX-Reward, a reward model designed specifically for video editing quality assessment. VEFX-Reward jointly processes the source video, the editing instruction, and the edited video, and predicts per-dimension quality scores via ordinal regression. We further release VEFX-Bench, a benchmark of 300 curated video-prompt pairs for standardized comparison of editing systems. Experiments show that VEFX-Reward aligns more strongly with human judgments than generic VLM judges and prior reward models on both standard IQA/VQA metrics and group-wise preference evaluation. Using VEFX-Reward as an evaluator, we benchmark representative commercial and open-source video editing systems, revealing a persistent gap between visual plausibility, instruction following, and edit locality in current models.
匹配关键词: tool use
---

[ACADEMIC - ARXIV]
标题: Autogenesis: A Self-Evolving Agent Protocol
作者: Wentao Zhang
链接: https://arxiv.org/abs/2604.15034v1
完整摘要: Recent advances in LLM based agent systems have shown promise in tackling complex, long horizon tasks. However, existing agent protocols (e.g., A2A and MCP) under specify cross entity lifecycle and context management, version tracking, and evolution safe update interfaces, which encourages monolithic compositions and brittle glue code. We introduce \textbf{\textsc{Autogenesis Protocol (AGP)}}, a self evolution protocol that decouples what evolves from how evolution occurs. Its Resource Substrate Protocol Layer (RSPL) models prompts, agents, tools, environments, and memory as protocol registered resources\footnote{Unless otherwise specified, resources refer to instances of the five RSPL entity types: \emph{prompt}, \emph{agent}, \emph{tool}, \emph{environment}, \emph{memory} with agent \emph{outputs}.} with explicit state, lifecycle, and versioned interfaces. Its Self Evolution Protocol Layer (SEPL) specifies a closed loop operator interface for proposing, assessing, and committing improvements with auditable lineage and rollback. Building on \textbf{\textsc{AGP}}, we present \textbf{\textsc{Autogenesis System (AGS)}}, a self-evolving multi-agent system that dynamically instantiates, retrieves, and refines protocol-registered resources during execution. We evaluate \textbf{\textsc{AGS}} on multiple challenging benchmarks that require long horizon planning and tool use across heterogeneous resources. The results demonstrate consistent improvements over strong baselines, supporting the effectiveness of agent resource management and closed loop self evolution.
匹配关键词: MCP
---

[ACADEMIC - ARXIV]
标题: SpaceMind: A Modular and Self-Evolving Embodied Vision-Language Agent Framework for Autonomous On-orbit Servicing
作者: Aodi Wu, Haodong Han, Xubo Luo, Ruisuo Wang, Shan He, Xue Wan
链接: https://arxiv.org/abs/2604.14399v1
完整摘要: Autonomous on-orbit servicing demands embodied agents that perceive through visual sensors, reason about 3D spatial situations, and execute multi-phase tasks over extended horizons. We present SpaceMind, a modular and self-evolving vision-language model (VLM) agent framework that decomposes knowledge, tools, and reasoning into three independently extensible dimensions: skill modules with dynamic routing, Model Context Protocol (MCP) tools with configurable profiles, and injectable reasoning-mode skills. An MCP-Redis interface layer enables the same codebase to operate across simulation and physical hardware without modification, and a Skill Self-Evolution mechanism distills operational experience into persistent skill files without model fine-tuning. We validate SpaceMind through 192 closed-loop runs across five satellites, three task types, and two environments, a UE5 simulation and a physical laboratory, deliberately including degraded conditions to stress-test robustness. Under nominal conditions all modes achieve 90--100% navigation success; under degradation, the Prospective mode uniquely succeeds in search-and-approach tasks where other modes fail. A self-evolution study shows that the agent recovers from failure in four of six groups from a single failed episode, including complete failure to 100% success and inspection scores improving from 12 to 59 out of 100. Real-world validation confirms zero-code-modification transfer to a physical robot with 100% rendezvous success. Code: https://github.com/wuaodi/SpaceMind
匹配关键词: MCP
---

[ACADEMIC - ARXIV]
标题: MCPThreatHive: Automated Threat Intelligence for Model Context Protocol Ecosystems
作者: Yi Ting Shen, Kentaroh Toyoda, Alex Leung
链接: https://arxiv.org/abs/2604.13849v1
完整摘要: The rapid proliferation of Model Context Protocol (MCP)-based agentic systems has introduced a new category of security threats that existing frameworks are inadequately equipped to address. We present MCPThreatHive, an open-source platform that automates the end-to-end lifecycle of MCP threat intelligence: from continuous, multi-source data collection through AI-driven threat extraction and classification, to structured knowledge graph storage and interactive visualization. The platform operationalizes the MCP-38 threat taxonomy, a curated set of 38 MCP-specific threat patterns mapped to STRIDE, OWASP Top 10 for LLM Applications, and OWASP Top 10 for Agentic Applications. A composite risk scoring model provides quantitative prioritization. Through a comparative analysis of representative existing MCP security tools, we identify three critical coverage gaps that MCPThreatHive addresses: incomplete compositional attack modeling, absence of continuous threat intelligence, and lack of unified multi-framework classification.
匹配关键词: MCP
---

[ACADEMIC - ARXIV]
标题: Dive into Claude Code: The Design Space of Today's and Future AI Agent Systems
作者: Jiacheng Liu, Xiaohan Zhao, Xinyi Shang, Zhiqiang Shen
链接: https://arxiv.org/abs/2604.14228v1
完整摘要: Claude Code is an agentic coding tool that can run shell commands, edit files, and call external services on behalf of the user. This study describes its comprehensive architecture by analyzing the publicly available TypeScript source code and further comparing it with OpenClaw, an independent open-source AI agent system that answers many of the same design questions from a different deployment context. Our analysis identifies five human values, philosophies, and needs that motivate the architecture (human decision authority, safety and security, reliable execution, capability amplification, and contextual adaptability) and traces them through thirteen design principles to specific implementation choices. The core of the system is a simple while-loop that calls the model, runs tools, and repeats. Most of the code, however, lives in the systems around this loop: a permission system with seven modes and an ML-based classifier, a five-layer compaction pipeline for context management, four extensibility mechanisms (MCP, plugins, skills, and hooks), a subagent delegation mechanism with worktree isolation, and append-oriented session storage. A comparison with OpenClaw, a multi-channel personal assistant gateway, shows that the same recurring design questions produce different architectural answers when the deployment context changes: from per-action safety classification to perimeter-level access control, from a single CLI loop to an embedded runtime within a gateway control plane, and from context-window extensions to gateway-wide capability registration. We finally identify six open design directions for future agent systems, grounded in recent empirical, architectural, and policy literature.
匹配关键词: MCP
---

[ACADEMIC - ARXIV]
标题: Local-Splitter: A Measurement Study of Seven Tactics for Reducing Cloud LLM Token Usage on Coding-Agent Workloads
作者: Justice Owusu Agyemang, Jerry John Kponyo, Elliot Amponsah, Godfred Manu Addo Boakye, Kwame Opuni-Boachie Obour Agyekum
链接: https://arxiv.org/abs/2604.12301v1
完整摘要: We present a systematic measurement study of seven tactics for reducing cloud LLM token usage when a small local model can act as a triage layer in front of a frontier cloud model. The tactics are: (1) local routing, (2) prompt compression, (3) semantic caching, (4) local drafting with cloud review, (5) minimal-diff edits, (6) structured intent extraction, and (7) batching with vendor prompt caching. We implement all seven in an open-source shim that speaks both MCP and the OpenAI-compatible HTTP surface, supporting any local model via Ollama and any cloud model via an OpenAI-compatible endpoint. We evaluate each tactic individually, in pairs, and in a greedy-additive subset across four coding-agent workload classes (edit-heavy, explanation-heavy, general chat, RAG-heavy). We measure tokens saved, dollar cost, latency, and routing accuracy. Our headline finding is that T1 (local routing) combined with T2 (prompt compression) achieves 45-79% cloud token savings on edit-heavy and explanation-heavy workloads, while on RAG-heavy workloads the full tactic set including T4 (draft-review) achieves 51% savings. We observe that the optimal tactic subset is workload-dependent, which we believe is the most actionable finding for practitioners deploying coding agents today.
匹配关键词: MCP
---

[ACADEMIC - ARXIV]
标题: Enhancing AI and Dynamical Subseasonal Forecasts with Probabilistic Bias Correction
作者: Hannah Guan, Soukayna Mouatadid, Paulo Orenstein, Judah Cohen, Haiyu Dong, Zekun Ni, Jeremy Berman, Genevieve Flaspohler, Alex Lu, Jakob Schloer, Joshua Talib, Jonathan A. Weyn, Lester Mackey
链接: https://arxiv.org/abs/2604.16238v1
完整摘要: Decision-makers rely on weather forecasts to plant crops, manage wildfires, allocate water and energy, and prepare for weather extremes. Today, such forecasts enjoy unprecedented accuracy out to two weeks thanks to steady advances in physics-based dynamical models and data-driven artificial intelligence (AI) models. However, model skill drops precipitously at subseasonal timescales (2 - 6 weeks ahead), due to compounding errors and persistent biases. To counter this degradation, we introduce probabilistic bias correction (PBC), a machine learning framework that substantially reduces systematic error by learning to correct historical probabilistic forecasts. When applied to the leading dynamical and AI models from the European Centre for Medium-Range Weather Forecasts (ECMWF), PBC doubles the subseasonal skill of the AI Forecasting System and improves the skill of the operationally-debiased dynamical model for 91% of pressure, 92% of temperature, and 98% of precipitation targets. We designed PBC for operational deployment, and, in ECMWF's 2025 real-time forecasting competition, its global forecasts placed first for all weather variables and lead times, outperforming the dynamical models from six operational forecasting centers, an international dynamical multi-model ensemble, ECMWF's AI Forecasting System, and the forecasting systems of 34 teams worldwide. These probabilistic skill gains translate into more accurate prediction of extreme events and have the potential to improve agricultural planning, energy management, and disaster preparedness in vulnerable communities.
匹配关键词: planning
---

[ACADEMIC - ARXIV]
标题: SocialGrid: A Benchmark for Planning and Social Reasoning in Embodied Multi-Agent Systems
作者: Hikaru Shindo, Hanzhao Lin, Lukas Helff, Patrick Schramowski, Kristian Kersting
链接: https://arxiv.org/abs/2604.16022v1
完整摘要: As Large Language Models (LLMs) transition from text processors to autonomous agents, evaluating their social reasoning in embodied multi-agent settings becomes critical. We introduce SocialGrid, an embodied multi-agent environment inspired by Among Us that evaluates LLM agents on planning, task execution, and social reasoning. Our evaluations reveal that even the strongest open model (GPT-OSS-120B) achieves below 60% accuracy in task completion and planning, with agents getting stuck in repetitive behaviors or failing to navigate basic obstacles. Since poor navigation confounds evaluation of social intelligence, SocialGrid offers an optional Planning Oracle to isolate social reasoning from planning deficits. While planning assistance improves task completion, social reasoning remains a bottleneck: agents fail to detect deception at near-random chance regardless of scale, relying on shallow heuristics rather than accumulating behavioral evidence. SocialGrid provides automatic failure analysis and fine-grained metrics, enabling developers to diagnose and improve their agents. We also establish a competitive leaderboard using Elo ratings from adversarial league play.
匹配关键词: planning
---

[ACADEMIC - ARXIV]
标题: Similarity-Based Bike Station Expansion via Hybrid Denoising Autoencoders
作者: Oluwaleke Yusuf, M. Tsaqif Wismadi, Adil Rasheed
链接: https://arxiv.org/abs/2604.15783v1
完整摘要: Urban bike-sharing systems require strategic station expansion to meet growing demand. Traditional allocation approaches rely on explicit demand modelling that may not capture the urban characteristics distinguishing successful stations. This study addresses the need to exploit patterns from existing stations to inform expansion decisions, particularly in data-constrained environments. We present a data-driven framework leveraging existing stations deemed desirable by operational metrics. A hybrid denoising autoencoder (HDAE) learns compressed latent representations from multi-source grid-level features (socio-demographic, built environment, and transport network), with a supervised classification head regularising the embedding space structure. Expansion candidates are selected via greedy allocation with spatial constraints based on latent-space similarity to existing stations. Evaluation on Trondheim's bike-sharing network demonstrates that HDAE embeddings yield more spatially coherent clusters and allocation patterns than raw features. Sensitivity analyses across similarity methods and distance metrics confirm robustness. A consensus-based procedure across multiple parametrisations distils 32 high-confidence extension zones where all parametrisations agree. The results demonstrate how representation learning captures complex patterns that raw features miss, enabling evidence-based expansion planning without explicit demand modelling. The consensus procedure strengthens recommendations by requiring agreement across parametrisations, while framework configurability allows planners to incorporate operational knowledge. The methodology generalises to any location-allocation problem where existing desirable instances inform the selection of new candidates.
匹配关键词: planning
---

[ACADEMIC - ARXIV]
标题: Fusing Cellular Network Data and Tollbooth Counts for Urban Traffic Flow Estimation
作者: Oluwaleke Yusuf, Shaira Tabassum
链接: https://arxiv.org/abs/2604.15782v1
完整摘要: Traffic simulations, essential for planning urban transit infrastructure interventions, require vehicle-category-specific origin-destination (OD) data. Existing data sources are imperfect: sparse tollbooth sensors provide accurate vehicle counts by category, while extensive mobility data from cellular network activity captures aggregated crowd movement, but lack modal disaggregation and have systematic biases. This study develops a machine learning framework to correct and disaggregate cellular network data using sparse tollbooth counts as ground truth. The model uses temporal and spatial features to learn the complex relationship between aggregated mobility data and vehicular data. The framework infers destinations from transit routes and implements routing logic to distribute corrected flows between OD pairs. This approach is applied to a bus depot expansion in Trondheim, Norway, generating hourly OD matrices by vehicle length category. The results show how limited but accurate sensor measurements can correct extensive but aggregated mobility data to produce grounded estimates of background vehicular traffic flows. These macro-scale estimates can be refined for micro-scale analysis at desired locations. The framework provides a generalisable approach for generating origin-destination data from cellular network data. This enables downstream tasks, like detailed traffic simulations for infrastructure planning in data-scarce contexts, supporting urban planners in making informed decisions.
匹配关键词: planning
---

[ACADEMIC - ARXIV]
标题: Hierarchical Active Inference using Successor Representations
作者: Prashant Rangarajan, Rajesh P. N. Rao
链接: https://arxiv.org/abs/2604.15679v1
完整摘要: Active inference, a neurally-inspired model for inferring actions based on the free energy principle (FEP), has been proposed as a unifying framework for understanding perception, action, and learning in the brain. Active inference has previously been used to model ecologically important tasks such as navigation and planning, but scaling it to solve complex large-scale problems in real-world environments has remained a challenge. Inspired by the existence of multi-scale hierarchical representations in the brain, we propose a model for planning of actions based on hierarchical active inference. Our approach combines a hierarchical model of the environment with successor representations for efficient planning. We present results demonstrating (1) how lower-level successor representations can be used to learn higher-level abstract states, (2) how planning based on active inference at the lower-level can be used to bootstrap and learn higher-level abstract actions, and (3) how these learned higher-level abstract states and actions can facilitate efficient planning. We illustrate the performance of the approach on several planning and reinforcement learning (RL) problems including a variant of the well-known four rooms task, a key-based navigation task, a partially observable planning problem, the Mountain Car problem, and PointMaze, a family of navigation tasks with continuous state and action spaces. Our results represent, to our knowledge, the first application of learned hierarchical state and action abstractions to active inference in FEP-based theories of brain function.
匹配关键词: planning
---

[ACADEMIC - ARXIV]
标题: Experience Compression Spectrum: Unifying Memory, Skills, and Rules in LLM Agents
作者: Xing Zhang, Guanghui Wang, Yanwei Cui, Wei Qiu, Ziyuan Li, Bing Zhu, Peiyang He
链接: https://arxiv.org/abs/2604.15877v1
完整摘要: As LLM agents scale to long-horizon, multi-session deployments, efficiently managing accumulated experience becomes a critical bottleneck. Agent memory systems and agent skill discovery both address this challenge -- extracting reusable knowledge from interaction traces -- yet a citation analysis of 1,136 references across 22 primary papers reveals a cross-community citation rate below 1%. We propose the \emph{Experience Compression Spectrum}, a unifying framework that positions memory, skills, and rules as points along a single axis of increasing compression (5--20$\times$ for episodic memory, 50--500$\times$ for procedural skills, 1,000$\times$+ for declarative rules), directly reducing context consumption, retrieval latency, and compute overhead. Mapping 20+ systems onto this spectrum reveals that every system operates at a fixed, predetermined compression level -- none supports adaptive cross-level compression, a gap we term the \emph{missing diagonal}. We further show that specialization alone is insufficient -- both communities independently solve shared sub-problems without exchanging solutions -- that evaluation methods are tightly coupled to compression levels, that transferability increases with compression at the cost of specificity, and that knowledge lifecycle management remains largely neglected. We articulate open problems and design principles for scalable, full-spectrum agent learning systems.
匹配关键词: long-horizon
---

[ACADEMIC - ARXIV]
标题: From Seeing to Simulating: Generative High-Fidelity Simulation with Digital Cousins for Generalizable Robot Learning and Evaluation
作者: Jasper Lu, Zhenhao Shen, Yuanfei Wang, Shugao Liu, Shengqiang Xu, Shawn Xie, Jingkai Xu, Feng Jiang, Jade Yang, Chen Xie, Ruihai Wu
链接: https://arxiv.org/abs/2604.15805v1
完整摘要: Learning robust robot policies in real-world environments requires diverse data augmentation, yet scaling real-world data collection is costly due to the need for acquiring physical assets and reconfiguring environments. Therefore, augmenting real-world scenes into simulation has become a practical augmentation for efficient learning and evaluation. We present a generative framework that establishes a generative real-to-sim mapping from real-world panoramas to high-fidelity simulation scenes, and further synthesize diverse cousin scenes via semantic and geometric editing. Combined with high-quality physics engines and realistic assets, the generated scenes support interactive manipulation tasks. Additionally, we incorporate multi-room stitching to construct consistent large-scale environments for long-horizon navigation across complex layouts. Experiments demonstrate a strong sim-to-real correlation validating our platform's fidelity, and show that extensively scaling up data generation leads to significantly better generalization to unseen scene and object variations, demonstrating the effectiveness of Digital Cousins for generalizable robot learning and evaluation.
匹配关键词: long-horizon
---

[ACADEMIC - ARXIV]
标题: MemEvoBench: Benchmarking Memory MisEvolution in LLM Agents
作者: Weiwei Xie, Shaoxiong Guo, Fan Zhang, Tian Xia, Xue Yang, Lizhuang Ma, Junchi Yan, Qibing Ren
链接: https://arxiv.org/abs/2604.15774v1
完整摘要: Equipping Large Language Models (LLMs) with persistent memory enhances interaction continuity and personalization but introduces new safety risks. Specifically, contaminated or biased memory accumulation can trigger abnormal agent behaviors. Existing evaluation methods have not yet established a standardized framework for measuring memory misevolution. This phenomenon refers to the gradual behavioral drift resulting from repeated exposure to misleading information. To address this gap, we introduce MemEvoBench, the first benchmark evaluating long-horizon memory safety in LLM agents against adversarial memory injection, noisy tool outputs, and biased feedback. The framework consists of QA-style tasks across 7 domains and 36 risk types, complemented by workflow-style tasks adapted from 20 Agent-SafetyBench environments with noisy tool returns. Both settings employ mixed benign and misleading memory pools within multi-round interactions to simulate memory evolution. Experiments on representative models reveal substantial safety degradation under biased memory updates. Our analysis suggests that memory evolution is a significant contributor to these failures. Furthermore, static prompt-based defenses prove insufficient, underscoring the urgency of securing memory evolution in LLM agents.
匹配关键词: long-horizon
---

[ACADEMIC - ARXIV]
标题: GTA-2: Benchmarking General Tool Agents from Atomic Tool-Use to Open-Ended Workflows
作者: Jize Wang, Xuanxuan Liu, Yining Li, Songyang Zhang, Yijun Wang, Zifei Shan, Xinyi Le, Cailian Chen, Xinping Guan, Dacheng Tao
链接: https://arxiv.org/abs/2604.15715v1
完整摘要: The development of general-purpose agents requires a shift from executing simple instructions to completing complex, real-world productivity workflows. However, current tool-use benchmarks remain misaligned with real-world requirements, relying on AI-generated queries, dummy tools, and limited system-level coordination. To address this, we propose GTA-2, a hierarchical benchmark for General Tool Agents (GTA) spanning atomic tool use and open-ended workflows. Built on real-world authenticity, it leverages real user queries, deployed tools, and multimodal contexts. (i) GTA-Atomic, inherited from our prior GTA benchmark, evaluates short-horizon, closed-ended tool-use precision. (ii) GTA-Workflow introduces long-horizon, open-ended tasks for realistic end-to-end completion. To evaluate open-ended deliverables, we propose a recursive checkpoint-based evaluation mechanism that decomposes objectives into verifiable sub-goals, enabling unified evaluation of both model capabilities and agent execution frameworks (i.e., execution harnesses). Experiments reveal a pronounced capability cliff: while frontier models already struggle on atomic tasks (below 50%), they largely fail on workflows, with top models achieving only 14.39% success. Further analysis shows that checkpoint-guided feedback improves performance, while advanced frameworks such as Manus and OpenClaw substantially enhance workflow completion, highlighting the importance of execution harness design beyond the underlying model capacity. These findings provide guidance for developing reliable personal and professional assistants. Dataset and code will be available at https://github.com/open-compass/GTA.
匹配关键词: long-horizon
---

[ACADEMIC - ARXIV]
标题: A Structure-Preserving Graph Neural Solver for Parametric Hyperbolic Conservation Laws
作者: Jiamin Jiang, Shanglin Lv, Jingrun Chen
链接: https://arxiv.org/abs/2604.15617v1
完整摘要: Hyperbolic conservation laws govern a wide range of transport-driven dynamics featuring shocks, contact discontinuities, and complex wave interactions, posing distinct challenges for deep-learning-based surrogate modeling. While classical numerical methods provide robust and physically admissible solutions, their computational cost restricts applicability in many-query tasks such as parametric studies and design optimization. Conversely, existing neural surrogates offer rapid inference but often fail to respect intrinsic PDE structures, leading to non-physical artifacts, rollout instability, and poor generalization. We present an interpretable, structure-preserving graph neural solver that bridges classical numerical principles with graph neural networks (GNNs). The network is designed as a learned reconstruction-and-flux operator rather than a black-box state updater, thereby inherently preserving key properties such as local conservation and upwinding. Inspired by Arbitrary high-order DERivatives schemes, we further recast message-passing GNNs as high-order space-time predictors, enabling conservative and stable neural updates with large time steps. Evaluation is performed on challenging supersonic flow benchmarks spanning broad parametric variations in geometry, initial/boundary conditions, and flow regimes. The neural solver achieves superior long-horizon rollout stability and accuracy compared with strong surrogate baselines, outperforms low-order discretizations, and delivers orders-of-magnitude runtime speedups over high-resolution simulations.
匹配关键词: long-horizon
---

[ACADEMIC - ARXIV]
标题: Ragged Paged Attention: A High-Performance and Flexible LLM Inference Kernel for TPU
作者: Jevin Jiang, Ying Chen, Blake A. Hechtman, Fenghui Zhang, Yarong Mu
链接: https://arxiv.org/abs/2604.15464v1
完整摘要: Large Language Model (LLM) deployment is increasingly shifting to cost-efficient accelerators like Google's Tensor Processing Units (TPUs), prioritizing both performance and total cost of ownership (TCO). However, existing LLM inference kernels and serving systems remain largely GPU-centric, and there is no well-established approach for efficiently mapping LLM workloads onto TPU architectures--particularly under the dynamic and ragged execution patterns common in modern serving. In this paper, we present Ragged Paged Attention (RPA), a high-performance and flexible attention kernel for TPUs, implemented using Pallas and Mosaic. RPA addresses these challenges through three key techniques: (1) fine-grained tiling to enable efficient dynamic slicing over ragged memory, (2) a custom software pipeline that fuses KV cache updates with attention computation, and (3) a distribution-aware compilation strategy that generates specialized kernels for decode, prefill, and mixed workloads. Evaluated on Llama 3 8B on TPU7x, RPA achieves up to 86% memory bandwidth utilization (MBU) in decode and 73% model FLOPs utilization (MFU) in prefill. Integrated as the primary TPU backend in vLLM and SGLang, RPA provides a production-grade foundation for efficient TPU inference and offers practical insights into kernel design.
匹配关键词: vLLM
---

[ACADEMIC - ARXIV]
标题: PipeLive: Efficient Live In-place Pipeline Parallelism Reconfiguration for Dynamic LLM Serving
作者: Xu Bai, Muhammed Tawfiqul Islam, Chen Wang, Adel N. Toosi
链接: https://arxiv.org/abs/2604.12171v1
完整摘要: Pipeline parallelism (PP) is widely used to partition layers of large language models (LLMs) across GPUs, enabling scalable inference for large models. However, existing systems rely on static PP configurations that fail to adapt to dynamic settings, such as serverless platforms and heterogeneous GPU environments. Reconfiguring PP by stopping and redeploying service incurs prohibitive downtime, so reconfiguration must instead proceed live and in place, without interrupting inference. However, live in-place PP reconfiguration is fundamentally challenging. GPUs are already saturated with model weights and KV cache, leaving little room for new layer placements and necessitating KV cache resizing, at odds with systems like vLLM that preallocate for throughput. Moreover, maintaining KV consistency during execution is difficult: stop-and-copy introduces large pauses, while background synchronization risks inconsistency as states evolve. We present PipeLive, which enables live in-place PP reconfiguration with minimal disruption. PipeLive introduces a redesigned KV cache layout together with a co-designed extension to PageAttention, forming a unified mechanism for live KV resizing. It further adopts an incremental KV patching mechanism, inspired by live virtual machine migration, to synchronize KV states between source and target configurations and identify a safe switch point. PipeLive achieves a 2.5X reduction in time-to-first-token (TTFT) without KV cache overflow compared to disabling KV resizing. Furthermore, compared to a variant without KV patching, it reduces reconfiguration overhead from seconds to under 10ms, and improves TTFT and time-per-output-token (TPOT) by up to 54.7% and 14.7%, respectively.
匹配关键词: vLLM
---

[ACADEMIC - ARXIV]
标题: MEMENTO: Teaching LLMs to Manage Their Own Context
作者: Vasilis Kontonis, Yuchen Zeng, Shivam Garg, Lingjiao Chen, Hao Tang, Ziyan Wang, Ahmed Awadallah, Eric Horvitz, John Langford, Dimitris Papailiopoulos
链接: https://arxiv.org/abs/2604.09852v1
完整摘要: Reasoning models think in long, unstructured streams with no mechanism for compressing or organizing their own intermediate state. We introduce MEMENTO: a method that teaches models to segment reasoning into blocks, compress each block into a memento, i.e., a dense state summary, and reason forward by attending only to mementos, reducing context, KV cache, and compute. To train MEMENTO models, we release OpenMementos, a public dataset of 228K reasoning traces derived from OpenThoughts-v3, segmented and annotated with intermediate summaries. We show that a two-stage SFT recipe on OpenMementos is effective across different model families (Qwen3, Phi-4, Olmo 3) and scales (8B--32B parameters). Trained models maintain strong accuracy on math, science, and coding benchmarks while achieving ${\sim}2.5\times$ peak KV cache reduction. We extend vLLM to support our inference method, achieving ${\sim}1.75\times$ throughput improvement while also enabling us to perform RL and further improve accuracy. Finally, we identify a dual information stream: information from each reasoning block is carried both by the memento text and by the corresponding KV states, which retain implicit information from the original block. Removing this channel drops accuracy by 15\,pp on AIME24.
匹配关键词: vLLM
---

[ACADEMIC - ARXIV]
标题: Dual-Pool Token-Budget Routing for Cost-Efficient and Reliable LLM Serving
作者: Xunzhuo Liu, Bowei He, Xue Liu, Andy Luo, Haichen Zhang, Huamin Chen
链接: https://arxiv.org/abs/2604.08075v1
完整摘要: Production vLLM fleets typically provision each instance for the worst-case context length, leading to substantial KV-cache over-allocation and under-utilized concurrency. In practice, 80-95% of requests are short, yet are served under configurations optimized for long contexts, wasting 4-8$\times$ throughput capacity and triggering reliability issues such as OOM crashes, preemption, and request rejections. We identify a common root cause for these inefficiencies: configuration-traffic mismatch. We propose dual-pool token-budget routing, a lightweight dispatch mechanism that partitions a homogeneous fleet into two specialized pools: a high-throughput short-context pool and a high-capacity long-context pool. Each request is routed based on its estimated total token budget, computed using a per-category bytes-to-token ratio that is learned online via exponential moving average from usage.prompt_tokens feedback, eliminating the need for a tokenizer. We also develop a simple analytical model that predicts fleet-level cost savings from workload characteristics and measured throughput differences, enabling practitioners to estimate benefits prior to deployment. Evaluations on real-world traces from the Azure LLM Inference Dataset and LMSYS-Chat-1M, serving Llama-3-70B on A100 GPUs, show that our approach reduces GPU-hours by 31-42%, corresponding to \$2.86M annual savings at fleet scale, while lowering preemption rates by 5.4$\times$ and improving P99 TTFT by 6%. A case study with Qwen3-235B-A22B on AMD MI300X at 10,000 req/s projects \$15.4M in annual savings. The method incurs only O(1) dispatch overhead, adapts automatically to heterogeneous workloads, and composes seamlessly with existing optimizations such as PagedAttention, continuous batching, and prefill-decode disaggregation.
匹配关键词: vLLM
---

[ACADEMIC - ARXIV]
标题: Blink: CPU-Free LLM Inference by Delegating the Serving Stack to GPU and SmartNIC
作者: Mohammad Siavashi, Mariano Scazzariello, Gerald Q. Maguire, Dejan Kostić, Marco Chiesa
链接: https://arxiv.org/abs/2604.07609v1
完整摘要: Large Language Model (LLM) inference is rapidly becoming a core datacenter service, yet current serving stacks keep the host CPU on the critical path for orchestration and token-level control. This makes LLM performance sensitive to CPU interference, undermining application colocation and forcing operators to reserve CPU headroom, leaving substantial capacity unutilized. We introduce Blink, an end-to-end serving architecture that removes the host CPU from the steady-state inference path by redistributing responsibilities across a SmartNIC and a GPU. Blink offloads request handling to the SmartNIC, which delivers inputs directly into GPU memory via RDMA, and replaces host-driven scheduling with a persistent GPU kernel that performs batching, scheduling, and KV-cache management without CPU involvement. Evaluated against TensorRT-LLM, vLLM, and SGLang, Blink outperforms all baselines even in isolation, reducing pre-saturation P99 TTFT by up to 8.47$\times$ and P99 TPOT by up to 3.40$\times$, improving decode throughput by up to 2.1$\times$, and reducing energy per token by up to 48.6$\%$. Under CPU interference, Blink maintains stable performance, while existing systems degrade by up to two orders of magnitude.
匹配关键词: vLLM
---

[ACADEMIC - ARXIV]
标题: IceCache: Memory-efficient KV-cache Management for Long-Sequence LLMs
作者: Yuzhen Mao, Qitong Wang, Martin Ester, Ke Li
链接: https://arxiv.org/abs/2604.10539v1
完整摘要: Key-Value (KV) cache plays a crucial role in accelerating inference in large language models (LLMs) by storing intermediate attention states and avoiding redundant computation during autoregressive generation. However, its memory footprint scales linearly with sequence length, often leading to severe memory bottlenecks on resource-constrained hardware. Prior work has explored offloading KV cache to the CPU while retaining only a subset on the GPU, but these approaches often rely on imprecise token selection and suffer performance degradation in long-generation tasks such as chain-of-thought reasoning. In this paper, we propose a novel KV cache management strategy, IceCache, which integrates semantic token clustering with PagedAttention. By organizing semantically related tokens into contiguous memory regions managed by a hierarchical, dynamically updatable data structure, our method enables more efficient token selection and better utilization of memory bandwidth during CPU-GPU transfers. Experimental results on LongBench show that, with a 256-token budget, IceCache maintains 99% of the original accuracy achieved by the full KV cache model. Moreover, compared to other offloading-based methods, IceCache attains competitive or even superior latency and accuracy while using only 25% of the KV cache token budget, demonstrating its effectiveness in long-sequence scenarios. The code is available on our project website at https://yuzhenmao.github.io/IceCache/.
匹配关键词: PagedAttention
---

[ACADEMIC - ARXIV]
标题: Dual-Pool Token-Budget Routing for Cost-Efficient and Reliable LLM Serving
作者: Xunzhuo Liu, Bowei He, Xue Liu, Andy Luo, Haichen Zhang, Huamin Chen
链接: https://arxiv.org/abs/2604.08075v1
完整摘要: Production vLLM fleets typically provision each instance for the worst-case context length, leading to substantial KV-cache over-allocation and under-utilized concurrency. In practice, 80-95% of requests are short, yet are served under configurations optimized for long contexts, wasting 4-8$\times$ throughput capacity and triggering reliability issues such as OOM crashes, preemption, and request rejections. We identify a common root cause for these inefficiencies: configuration-traffic mismatch. We propose dual-pool token-budget routing, a lightweight dispatch mechanism that partitions a homogeneous fleet into two specialized pools: a high-throughput short-context pool and a high-capacity long-context pool. Each request is routed based on its estimated total token budget, computed using a per-category bytes-to-token ratio that is learned online via exponential moving average from usage.prompt_tokens feedback, eliminating the need for a tokenizer. We also develop a simple analytical model that predicts fleet-level cost savings from workload characteristics and measured throughput differences, enabling practitioners to estimate benefits prior to deployment. Evaluations on real-world traces from the Azure LLM Inference Dataset and LMSYS-Chat-1M, serving Llama-3-70B on A100 GPUs, show that our approach reduces GPU-hours by 31-42%, corresponding to \$2.86M annual savings at fleet scale, while lowering preemption rates by 5.4$\times$ and improving P99 TTFT by 6%. A case study with Qwen3-235B-A22B on AMD MI300X at 10,000 req/s projects \$15.4M in annual savings. The method incurs only O(1) dispatch overhead, adapts automatically to heterogeneous workloads, and composes seamlessly with existing optimizations such as PagedAttention, continuous batching, and prefill-decode disaggregation.
匹配关键词: PagedAttention
---

[ACADEMIC - ARXIV]
标题: Token-Budget-Aware Pool Routing for Cost-Efficient LLM Inference
作者: Huamin Chen, Xunzhuo Liu, Junchen Jiang, Bowei He, Xue Liu
链接: https://arxiv.org/abs/2604.09613v2
完整摘要: Production vLLM fleets provision every instance for worst-case context length, wasting 4-8x concurrency on the 80-95% of requests that are short and simultaneously triggering KV-cache failures -- OOM crashes, preemption storms, and request rejections. Both problems share a single root cause: configuration-traffic mismatch. We propose token-budget-aware pool routing: estimate each request's total token budget using a self-calibrating per-category bytes-per-token ratio, then dispatch it to one of two vLLM pools -- a high-throughput short pool or a high-capacity long pool -- each right-sized for its workload class. The ratio is learned online via exponential moving average from usage.prompt_tokens feedback, requiring no tokenizer. A closed-form cost model, savings = alpha * (1 - 1/rho), predicts fleet-level GPU savings from two observable quantities: the short-traffic fraction alpha and the throughput gain ratio rho. On traces from the Azure LLM Inference Dataset and LMSYS-Chat-1M serving Llama-3-70B on A100 GPUs, token-budget routing reduces GPU instances by 17-39% (\$1.2-2.0M/yr at 1,000 req/s), with savings verified by a self-contained discrete-event simulator. A case study projecting Qwen3-235B-A22B on AMD MI300X at 10,000 req/s shows \$15.4M/yr in savings. The algorithm adds O(1) dispatch overhead, self-calibrates across content types without a tokenizer, and composes with PagedAttention, continuous batching, and prefill-decode disaggregation.
匹配关键词: PagedAttention
---

[ACADEMIC - ARXIV]
标题: nchellwig at SemEval-2026 Task 3: Self-Consistent Structured Generation (SCSG) for Dimensional Aspect-Based Sentiment Analysis using Large Language Models
作者: Nils Constantin Hellwig, Jakob Fehle, Udo Kruschwitz, Christian Wolff
链接: https://arxiv.org/abs/2603.01788v1
完整摘要: We present Self-Consistent Structured Generation (SCSG) for Dimensional Aspect-Based Sentiment Analysis in SemEval-2026 Task 3 (Track A). SCSG enhances prediction reliability by executing a LoRA-adapted large language model multiple times per instance, retaining only tuples that achieve a majority consensus across runs. To mitigate the computational overhead of multiple forward passes, we leverage vLLM's PagedAttention mechanism for efficient key--value cache reuse. Evaluation across 6 languages and 8 language--domain combinations demonstrates that self-consistency with 15 executions yields statistically significant improvements over single-inference prompting, with our system (leveraging Gemma 3) ranking in the top seven across all settings, achieving second place on three out of four English subsets and first place on Tatar-Restaurant for DimASTE.
匹配关键词: PagedAttention
---

[ACADEMIC - ARXIV]
标题: Zipage: Maintain High Request Concurrency for LLM Reasoning through Compressed PagedAttention
作者: Mengqi Liao, Lu Wang, Chaoyun Zhang, Bo Qiao, Si Qin, Qingwei Lin, Saravan Rajmohan, Dongmei Zhang, Huaiyu Wan
链接: https://arxiv.org/abs/2603.08743v1
完整摘要: With reasoning becoming the generative paradigm for large language models (LLMs), the memory bottleneck caused by KV cache during the decoding phase has become a critical factor limiting high-concurrency service. Although existing KV cache eviction methods address the memory issue, most of them are impractical for industrial-grade applications. This paper introduces Compressed PagedAttention, a method that combines token-wise KV cache eviction with PagedAttention. We propose a comprehensive scheduling strategy and support prefix caching and asynchronous compression for Compressed PagedAttention. Based on this, we have developed a high-concurrency LLM inference engine, Zipage. On large-scale mathematical reasoning tasks, Zipage achieves around 95\% of the performance of Full KV inference engines while delivering over 2.1$\times$ speedup.
匹配关键词: PagedAttention
---

[ACADEMIC - ARXIV]
标题: Self-Distillation as a Performance Recovery Mechanism for LLMs: Counteracting Compression and Catastrophic Forgetting
作者: Chi Liu, Xin Chen, Xu Zhou, Fangbo Tu, Srinivasan Manoharan
链接: https://arxiv.org/abs/2604.15794v1
完整摘要: Large Language Models (LLMs) have achieved remarkable success, underpinning diverse AI applications. However, they often suffer from performance degradation due to factors such as catastrophic forgetting during Supervised Fine-Tuning (SFT), quantization, and pruning. In this work, we introduce a performance recovery framework based on Self-Distillation Fine-Tuning (SDFT) that effectively restores model capabilities. Complementing this practical contribution, we provide a rigorous theoretical explanation for the underlying recovery mechanism. We posit that an LLM's generative capability fundamentally relies on the high-dimensional manifold constructed by its hidden layers. To investigate this, we employ Centered Kernel Alignment (CKA) to quantify the alignment between student and teacher activation trajectories, leveraging its invariance to orthogonal transformations and scaling. Our experiments demonstrate a strong correlation between performance recovery and manifold alignment, substantiating the claim that self-distillation effectively aligns the student's high-dimensional manifold with the optimal structure represented by the teacher. This study bridges the gap between practical recovery frameworks and geometric representation theory, offering new insights into the internal mechanisms of self-distillation.
匹配关键词: quantization
---

[ACADEMIC - ARXIV]
标题: Pruning Unsafe Tickets: A Resource-Efficient Framework for Safer and More Robust LLMs
作者: Wai Man Si, Mingjie Li, Michael Backes, Yang Zhang
链接: https://arxiv.org/abs/2604.15780v1
完整摘要: Machine learning models are increasingly deployed in real-world applications, but even aligned models such as Mistral and LLaVA still exhibit unsafe behaviors inherited from pre-training. Current alignment methods like SFT and RLHF primarily encourage models to generate preferred responses, but do not explicitly remove the unsafe subnetworks that trigger harmful outputs. In this work, we introduce a resource-efficient pruning framework that directly identifies and removes parameters associated with unsafe behaviors while preserving model utility. Our method employs a gradient-free attribution mechanism, requiring only modest GPU resources, and generalizes across architectures and quantized variants. Empirical evaluations on ML models show substantial reductions in unsafe generations and improved robustness against jailbreak attacks, with minimal utility loss. From the perspective of the Lottery Ticket Hypothesis, our results suggest that ML models contain "unsafe tickets" responsible for harmful behaviors, and pruning reveals "safety tickets" that maintain performance while aligning outputs. This provides a lightweight, post-hoc alignment strategy suitable for deployment in resource-constrained settings.
匹配关键词: quantization
---

[ACADEMIC - ARXIV]
标题: LLM attribution analysis across different fine-tuning strategies and model scales for automated code compliance
作者: Jack Wei Lun Shi, Minghao Dang, Wawan Solihin, Justin K. W. Yeoh
链接: https://arxiv.org/abs/2604.15589v1
完整摘要: Existing research on large language models (LLMs) for automated code compliance has primarily focused on performance, treating the models as black boxes and overlooking how training decisions affect their interpretive behavior. This paper addresses this gap by employing a perturbation-based attribution analysis to compare the interpretive behaviors of LLMs across different fine-tuning strategies such as full fine-tuning (FFT), low-rank adaptation (LoRA) and quantized LoRA fine-tuning, as well as the impact of model scales which include varying LLM parameter sizes. Our results show that FFT produces attribution patterns that are statistically different and more focused than those from parameter-efficient fine-tuning methods. Furthermore, we found that as model scale increases, LLMs develop specific interpretive strategies such as prioritizing numerical constraints and rule identifiers in the building text, albeit with performance gains in semantic similarity of the generated and reference computer-processable rules plateauing for models larger than 7B. This paper provides crucial insights into the explainability of these models, taking a step toward building more transparent LLMs for critical, regulation-based tasks in the Architecture, Engineering, and Construction industry.
匹配关键词: quantization
---

[ACADEMIC - ARXIV]
标题: SecureRouter: Encrypted Routing for Efficient Secure Inference
作者: Yukuan Zhang, Mengxin Zheng, Qian Lou
链接: https://arxiv.org/abs/2604.15499v1
完整摘要: Cryptographically secure neural network inference typically relies on secure computing techniques such as Secure Multi-Party Computation (MPC), enabling cloud servers to process client inputs without decrypting them. Although prior privacy-preserving inference systems co-design network optimizations with MPC, they remain slow and costly, limiting real-world deployment. A major bottleneck is their use of a single, fixed transformer model for all encrypted inputs, ignoring that different inputs require different model sizes to balance efficiency and accuracy. We present SecureRouter, an end-to-end encrypted routing and inference framework that accelerates secure transformer inference through input-adaptive model selection under encryption. SecureRouter establishes a unified encrypted pipeline that integrates a secure router with an MPC-optimized model pool, enabling coordinated routing, inference, and protocol execution while preserving full data and model confidentiality. The framework includes training-phase and inference-phase components: an MPC-cost-aware secure router that predicts per-model utility and cost from encrypted features, and an MPC-optimized model pool whose architectures and quantization schemes are co-trained to minimize MPC communication and computation overhead. Compared to prior work, SecureRouter achieves a latency reduction by 1.95x with negligible accuracy loss, offering a practical path toward scalable and efficient secure AI inference. Our open-source implementation is available at: https://github.com/UCF-ML-Research/SecureRouter
匹配关键词: quantization
---

[ACADEMIC - ARXIV]
标题: When Flat Minima Fail: Characterizing INT4 Quantization Collapse After FP32 Convergence
作者: Marcus Armstrong
链接: https://arxiv.org/abs/2604.15167v1
完整摘要: Post-training quantization (PTQ) assumes that a well-converged model is a quantization-ready model. We show this assumption fails in a structured, measurable, and previously uncharacterized way. Using a calibration-free per-group INT4 probe applied to all 154 publicly available Pythia-160m training checkpoints, we identify a three-phase divergence structure: a rapid-learning phase where both FP32 perplexity and quantization robustness improve together, a meta-stable plateau lasting roughly 70,000 steps where FP32 perplexity stagnates but INT4 gap remains bounded, and an explosive divergence phase where the INT4 gap compounds from 11% to 517% while FP32 perplexity barely moves. Critically, this divergence begins not when the learning rate starts decaying, but precisely when FP32 perplexity converges a finer-grained onset predictor that implies post-convergence weight updates, rather than decay magnitude alone, are the proximate cause. We further show that INT8 quantization is entirely immune throughout all three phases, constraining the mechanism to the coarseness of the 16-level INT4 grid specifically, and rule out weight outlier accumulation as the mechanism via direct kurtosis measurement. Finally, we conduct a controlled fork experiment from the pre-divergence checkpoint comparing three learning rate schedules (cosine continuation, SGDR warm restarts, and our proposed Oscillatory Lock-In) across nine independent runs. SGDR uniformly accelerates divergence (0/9 pairwise wins against cosine), while OLI's settled cool phases reduce the INT4 gap by 2.2 percentage points on average (t = -5.46, p < 0.0001), demonstrating that schedule amplitude calibration, not oscillation alone, determines whether perturbation helps or hurts. Our code, probe implementation, and all 154-checkpoint audit results are released publicly.
匹配关键词: quantization
---

[ACADEMIC - ARXIV]
标题: Geometric regularization of autoencoders via observed stochastic dynamics
作者: Sean Hill, Felix X. -F. Ye
链接: https://arxiv.org/abs/2604.16282v1
完整摘要: Stochastic dynamical systems with slow or metastable behavior evolve, on long time scales, on an unknown low-dimensional manifold in high-dimensional ambient space. Building a reduced simulator from short-burst ambient ensembles is a long-standing problem: local-chart methods like ATLAS suffer from exponential landmark scaling and per-step reprojection, while autoencoder alternatives leave tangent-bundle geometry poorly constrained, and the errors propagate into the learned drift and diffusion. We observe that the ambient covariance~$Λ$ already encodes coordinate-invariant tangent-space information, its range spanning the tangent bundle. Using this, we construct a tangent-bundle penalty and an inverse-consistency penalty for a three-stage pipeline (chart learning, latent drift, latent diffusion) that learns a single nonlinear chart and the latent SDE. The penalties induce a function-space metric, the $ρ$-metric, strictly weaker than the Sobolev $H^1$ norm yet achieving the same chart-quality generalization rate up to logarithmic factors. For the drift, we derive an encoder-pullback target via Itô's formula on the learned encoder and prove a bias decomposition showing the standard decoder-side formula carries systematic error for any imperfect chart. Under a $W^{2,\infty}$ chart-convergence assumption, chart-level error propagates controllably to weak convergence of the ambient dynamics and to convergence of radial mean first-passage times. Experiments on four surfaces embedded in up to $201$ ambient dimensions reduce radial MFPT error by $50$--$70\%$ under rotation dynamics and achieve the lowest inter-well MFPT error on most surface--transition pairs under metastable Müller--Brown Langevin dynamics, while reducing end-to-end ambient coefficient errors by up to an order of magnitude relative to an unregularized autoencoder.
匹配关键词: speculative decoding
---

[ACADEMIC - ARXIV]
标题: Robust Multispectral Semantic Segmentation under Missing or Full Modalities via Structured Latent Projection
作者: Irem Ulku, Erdem Akagündüz, Ömer Özgür Tanrıöver
链接: https://arxiv.org/abs/2604.15856v1
完整摘要: Multimodal remote sensing data provide complementary information for semantic segmentation, but in real-world deployments, some modalities may be unavailable due to sensor failures, acquisition issues, or challenging atmospheric conditions. Existing multimodal segmentation models typically address missing modalities by learning a shared representation across inputs. However, this approach can introduce a trade-off by compromising modality-specific complementary information and reducing performance when all modalities are available. In this paper, we tackle this limitation with CBC-SLP, a multimodal semantic segmentation model designed to preserve both modality-invariant and modality-specific information. Inspired by the theoretical results on modality alignment, which state that perfectly aligned multimodal representations can lead to sub-optimal performance in downstream prediction tasks, we propose a novel structured latent projection approach as an architectural inductive bias. Rather than enforcing this strategy through a loss term, we incorporate it directly into the architecture. In particular, to use the complementary information effectively while maintaining robustness under random modality dropout, we structure the latent representations into shared and modality-specific components and adaptively transfer them to the decoder according to the random modality availability mask. Extensive experiments on three multimodal remote sensing image sets demonstrate that CBC-SLP consistently outperforms state-of-the-art multimodal models across full and missing modality scenarios. Besides, we empirically demonstrate that the proposed strategy can recover the complementary information that may not be preserved in a shared representation. The code is available at https://github.com/iremulku/Multispectral-Semantic-Segmentation-via-Structured-Latent-Projection-CBC-SLP-.
匹配关键词: speculative decoding
---

[ACADEMIC - ARXIV]
标题: Disentangling Mathematical Reasoning in LLMs: A Methodological Investigation of Internal Mechanisms
作者: Tanja Baeumel, Josef van Genabith, Simon Ostermann
链接: https://arxiv.org/abs/2604.15842v1
完整摘要: Large language models (LLMs) have demonstrated impressive capabilities, yet their internal mechanisms for handling reasoning-intensive tasks remain underexplored. To advance the understanding of model-internal processing mechanisms, we present an investigation of how LLMs perform arithmetic operations by examining internal mechanisms during task execution. Using early decoding, we trace how next-token predictions are constructed across layers. Our experiments reveal that while the models recognize arithmetic tasks early, correct result generation occurs only in the final layers. Notably, models proficient in arithmetic exhibit a clear division of labor between attention and MLP modules, where attention propagates input information and MLP modules aggregate it. This division is absent in less proficient models. Furthermore, successful models appear to process more challenging arithmetic tasks functionally, suggesting reasoning capabilities beyond factual recall.
匹配关键词: speculative decoding
---

[ACADEMIC - ARXIV]
标题: DepCap: Adaptive Block-Wise Parallel Decoding for Efficient Diffusion LM Inference
作者: Xiang Xia, Wuyang Zhang, Jiazheng Liu, Cheng Yan, Yanyong Zhang
链接: https://arxiv.org/abs/2604.15750v1
完整摘要: Diffusion language models (DLMs) have emerged as a promising alternative to autoregressive language generation due to their potential for parallel decoding and global refinement of the entire sequence. To unlock this potential, DLM inference must carefully balance generation quality and decoding speed. Recent block-wise DLM decoding methods improve this trade-off by performing diffusion-based decoding sequentially in blocks. However, existing methods typically rely on fixed block schedules or current-step local signals to determine block boundaries, and use conservative confidence-based parallel decoding to avoid conflicts, limiting the quality-speed trade-off. In this paper, we argue that block-wise DLM inference requires more suitable signals for its two core decisions: cross-step signals for determining block boundaries, and token-level conflict signals for parallel decoding. Based on this view, we propose DepCap, a training-free framework for efficient block-wise DLM inference. Specifically, DepCap instantiates the cross-step signal as the influence of the last decoded block and uses it to adaptively determine how far the next block should extend, while identifying a conflict-free subset of tokens for safe parallel decoding within each block, enabling substantial inference acceleration with negligible quality degradation. DepCap is a plug-and-play method applicable to various DLMs, and compatible with existing KV-cache strategies for block-wise DLM. An information-theoretic analysis further suggests that the cumulative last-block influence on a candidate block is approximately additive across tokens, supporting the proposed block-partitioning criterion. Experimental results show that DepCap achieves favorable speed-quality trade-offs across multiple DLM backbones and reasoning and coding benchmarks, with up to 5.63$\times$ speedup without significant performance degradation.
匹配关键词: speculative decoding
---

[ACADEMIC - ARXIV]
标题: Faster LLM Inference via Sequential Monte Carlo
作者: Yahya Emara, Mauricio Barba da Costa, Chi-Chih Chang, Cameron Freer, Tim Vieira, Ryan Cotterell, Mohamed S. Abdelfattah
链接: https://arxiv.org/abs/2604.15672v1
完整摘要: Speculative decoding (SD) accelerates language model inference by drafting tokens from a cheap proposal model and verifying them against an expensive target model via rejection sampling. Because rejection truncates the draft block at the first error, throughput degrades when draft and target diverge. Rather than rejecting draft tokens outright, we propose to reweight them. To this end, we introduce sequential Monte Carlo speculative decoding (SMC-SD), which replaces token-level rejection with importance-weighted resampling over a population of draft particles. SMC-SD is a principled approximate inference scheme that trades exactness for additional speed, while preserving theoretical bounds on its per-step approximation error. Because LLM inference is memory bandwidth-bound, the arithmetic needed to draft particles and to score them in parallel comes nearly for free -- SMC-SD uses idle compute to turn verification into a vectorized, fixed-size operation with no rollback. Empirically, SMC-SD achieves 2.36x speed-up over speculative decoding and a 5.2x speed-up over autoregressive decoding, while remaining within 3% of the target model's accuracy on reasoning, instruction-following, and coding benchmarks.
匹配关键词: speculative decoding
---

[ACADEMIC - ARXIV]
标题: FL-MHSM: Spatially-adaptive Fusion and Ensemble Learning for Flood-Landslide Multi-Hazard Susceptibility Mapping at Regional Scale
作者: Aswathi Mundayatt, Jaya Sreevalsan-Nair
链接: https://arxiv.org/abs/2604.16265v1
完整摘要: Existing multi-hazard susceptibility mapping (MHSM) studies often rely on spatially uniform models, treat hazards independently, and provide limited representation of cross-hazard dependence and uncertainty. To address these limitations, this study proposes a deep learning (DL) workflow for joint flood-landslide multi-hazard susceptibility mapping (FL-MHSM) that combines two-level spatial partitioning, probabilistic Early Fusion (EF), a tree-based Late Fusion (LF) baseline, and a soft-gating Mixture of Experts (MoE) model, with MoE serving as final predictive model. The proposed design preserves spatial heterogeneity through zonal partitions and enables data-parallel large-area prediction using overlapping lattice grids. In Kerala, EF remained competitive with LF, improving flood recall from 0.816 to 0.840 and reducing Brier score from 0.092 to 0.086, while MoE provided strongest performance for flood susceptibility, achieving an AUC-ROC of 0.905, recall of 0.930, and F1-score of 0.722. In Nepal, EF similarly improved flood recall from 0.820 to 0.858 and reduced Brier score from 0.057 to 0.049 relative to LF, while MoE outperformed both EF and LF for landslide susceptibility, achieving an AUC-ROC of 0.914, recall of 0.901, and F1-score of 0.559. GeoDetector analysis of MoE outputs further showed that dominant factors varied more across zones in Kerala, where susceptibility was shaped by different combinations of topographic, land-cover, and drainage-related controls, while Nepal showed a more consistent influence of topographic and glacier-related factors across zones. These findings show that EF and LF provide complementary predictive behavior, and that their spatially adaptive integration through MoE yields robust overall predictive performance for FL-MHSM while supporting interpretable characterization of multi-hazard susceptibility in spatially heterogeneous landscapes.
匹配关键词: MoE
---

[ACADEMIC - ARXIV]
标题: Joint-Centric Dual Contrastive Alignment with Structure-Preserving and Information-Balanced Regularization
作者: Habibeh Naderi, Behrouz Haji Soleimani, Stan Matwin
链接: https://arxiv.org/abs/2604.16247v1
完整摘要: We propose HILBERT (HIerarchical Long-sequence Balanced Embedding with Reciprocal contrastive Training), a cross-attentive multimodal framework for learning document-level audio-text representations from long, segmented sequences in low-resource data settings. HILBERT leverages frozen pre-trained speech and language encoders to extract segment-level features, which are aggregated via cross-modal attention and self-attentive pooling to form modality-specific document representations and a joint cross-attentive embedding. To align modalities while preserving modality-specific structure under severe audio-text dimensional imbalance, we introduce a reciprocal dual contrastive objective that simultaneously aligns audio-to-joint and text-to-joint representations, rather than directly contrasting audio and text alone. Two auxiliary regularizers further stabilize long-sequence fusion: a Centered Kernel Alignment (CKA) loss that preserves structural consistency between each modality and the joint embedding, and a mutual information balancing loss that prevents dominance of a single modality by equalizing information flow from audio and text into the joint space. For downstream prediction, HILBERT employs a Mixture-of-Experts (MoE) classifier over concatenated audio, text, and joint representations to accommodate heterogeneous label regimes. Extensive evaluation across multiple audio-text backbone combinations demonstrates that HILBERT learns semantically meaningful long-sequence representations and achieves superior performance on highly imbalanced multi-class settings.
匹配关键词: MoE
---

[ACADEMIC - ARXIV]
标题: Breaking the Training Barrier of Billion-Parameter Universal Machine Learning Interatomic Potentials
作者: Yuanchang Zhou, Hongyu Wang, Yiming Du, Yan Wang, Mingzhen Li, Siyu Hu, Xiangyu Zhang, Weijian Liu, Chen Wang, Zhuoqiang Guo, Long Wang, Jingde Bu, Yutong Lu, Guangming Tan, Weile Jia
链接: https://arxiv.org/abs/2604.15821v1
完整摘要: Universal Machine Learning Interatomic Potentials (uMLIPs), pre-trained on massively diverse datasets encompassing inorganic materials and organic molecules across the entire periodic table, serve as foundational models for quantum-accurate physical simulations. However, uMLIP training requires second-order derivatives, which lack corresponding parallel training frameworks; moreover, scaling to the billion-parameter regime causes explosive growth in computation and communication overhead, making its training a tremendous challenge. We introduce MatRIS-MoE, a billion-parameter Mixture-of-Experts model built upon invariant architecture, and {Janus}, a pioneering high-dimensional distributed training framework for uMLIPs with hardware-aware optimizations. Deployed across two Exascale supercomputers, our code attains a peak performance of 1.2/1.0 EFLOPS (24\%/{35.5\%} of theoretical peak) in single precision at over 90\% parallel efficiency, compressing the training of billion-parameter uMLIPs from weeks to hours. This work establishes a new high-water mark for AI-for-Science (AI4S) foundation models at Exascale and provides essential infrastructure for rapid scientific discovery.
匹配关键词: MoE
---

[ACADEMIC - ARXIV]
标题: Qwen3.5-Omni Technical Report
作者: Qwen Team
链接: https://arxiv.org/abs/2604.15804v1
完整摘要: In this work, we present Qwen3.5-Omni, the latest advancement in the Qwen-Omni model family. Representing a significant evolution over its predecessor, Qwen3.5-Omni scales to hundreds of billions of parameters and supports a 256k context length. By leveraging a massive dataset comprising heterogeneous text-vision pairs and over 100 million hours of audio-visual content, the model demonstrates robust omni-modality capabilities. Qwen3.5-Omni-plus achieves SOTA results across 215 audio and audio-visual understanding, reasoning, and interaction subtasks and benchmarks, surpassing Gemini-3.1 Pro in key audio tasks and matching it in comprehensive audio-visual understanding. Architecturally, Qwen3.5-Omni employs a Hybrid Attention Mixture-of-Experts (MoE) framework for both Thinker and Talker, enabling efficient long-sequence inference. The model facilitates sophisticated interaction, supporting over 10 hours of audio understanding and 400 seconds of 720P video (at 1 FPS). To address the inherent instability and unnaturalness in streaming speech synthesis, often caused by encoding efficiency discrepancies between text and speech tokenizers, we introduce ARIA. ARIA dynamically aligns text and speech units, significantly enhancing the stability and prosody of conversational speech with minimal latency impact. Furthermore, Qwen3.5-Omni expands linguistic boundaries, supporting multilingual understanding and speech generation across 10 languages with human-like emotional nuance. Finally, Qwen3.5-Omni exhibits superior audio-visual grounding capabilities, generating script-level structured captions with precise temporal synchronization and automated scene segmentation. Remarkably, we observed the emergence of a new capability in omnimodal models: directly performing coding based on audio-visual instructions, which we call Audio-Visual Vibe Coding.
匹配关键词: MoE
---

[ACADEMIC - ARXIV]
标题: Towards Faster Language Model Inference Using Mixture-of-Experts Flow Matching
作者: Aihua Li
链接: https://arxiv.org/abs/2604.15009v1
完整摘要: Flow matching retains the generation quality of diffusion models while enabling substantially faster inference, making it a compelling paradigm for generative modeling. However, when applied to language modeling, it exhibits fundamental limitations in representing complex latent distributions with irregular geometries, such as anisotropy and multimodality. To address these challenges, we propose a mixture-of-experts flow matching (MoE-FM) framework, which captures complex global transport geometries in latent space by decomposing them into locally specialized vector fields. Building on MoE-FM, we develop a non-autoregressive (NAR) language modeling approach, named YAN, instantiated with both Transformer and Mamba architectures. Across multiple downstream tasks, YAN achieves generation quality on par with both autoregressive (AR) and diffusion-based NAR language models, while requiring as few as three sampling steps. This yields a $40\times$ speedup over AR baselines and up to a $10^3\times$ speedup over diffusion language models, demonstrating substantial efficiency advantages for language modeling.
匹配关键词: MoE
---

[ACADEMIC - ARXIV]
标题: DepCap: Adaptive Block-Wise Parallel Decoding for Efficient Diffusion LM Inference
作者: Xiang Xia, Wuyang Zhang, Jiazheng Liu, Cheng Yan, Yanyong Zhang
链接: https://arxiv.org/abs/2604.15750v1
完整摘要: Diffusion language models (DLMs) have emerged as a promising alternative to autoregressive language generation due to their potential for parallel decoding and global refinement of the entire sequence. To unlock this potential, DLM inference must carefully balance generation quality and decoding speed. Recent block-wise DLM decoding methods improve this trade-off by performing diffusion-based decoding sequentially in blocks. However, existing methods typically rely on fixed block schedules or current-step local signals to determine block boundaries, and use conservative confidence-based parallel decoding to avoid conflicts, limiting the quality-speed trade-off. In this paper, we argue that block-wise DLM inference requires more suitable signals for its two core decisions: cross-step signals for determining block boundaries, and token-level conflict signals for parallel decoding. Based on this view, we propose DepCap, a training-free framework for efficient block-wise DLM inference. Specifically, DepCap instantiates the cross-step signal as the influence of the last decoded block and uses it to adaptively determine how far the next block should extend, while identifying a conflict-free subset of tokens for safe parallel decoding within each block, enabling substantial inference acceleration with negligible quality degradation. DepCap is a plug-and-play method applicable to various DLMs, and compatible with existing KV-cache strategies for block-wise DLM. An information-theoretic analysis further suggests that the cumulative last-block influence on a candidate block is approximately additive across tokens, supporting the proposed block-partitioning criterion. Experimental results show that DepCap achieves favorable speed-quality trade-offs across multiple DLM backbones and reasoning and coding benchmarks, with up to 5.63$\times$ speedup without significant performance degradation.
匹配关键词: KV cache
---

[ACADEMIC - ARXIV]
标题: Ragged Paged Attention: A High-Performance and Flexible LLM Inference Kernel for TPU
作者: Jevin Jiang, Ying Chen, Blake A. Hechtman, Fenghui Zhang, Yarong Mu
链接: https://arxiv.org/abs/2604.15464v1
完整摘要: Large Language Model (LLM) deployment is increasingly shifting to cost-efficient accelerators like Google's Tensor Processing Units (TPUs), prioritizing both performance and total cost of ownership (TCO). However, existing LLM inference kernels and serving systems remain largely GPU-centric, and there is no well-established approach for efficiently mapping LLM workloads onto TPU architectures--particularly under the dynamic and ragged execution patterns common in modern serving. In this paper, we present Ragged Paged Attention (RPA), a high-performance and flexible attention kernel for TPUs, implemented using Pallas and Mosaic. RPA addresses these challenges through three key techniques: (1) fine-grained tiling to enable efficient dynamic slicing over ragged memory, (2) a custom software pipeline that fuses KV cache updates with attention computation, and (3) a distribution-aware compilation strategy that generates specialized kernels for decode, prefill, and mixed workloads. Evaluated on Llama 3 8B on TPU7x, RPA achieves up to 86% memory bandwidth utilization (MBU) in decode and 73% model FLOPs utilization (MFU) in prefill. Integrated as the primary TPU backend in vLLM and SGLang, RPA provides a production-grade foundation for efficient TPU inference and offers practical insights into kernel design.
匹配关键词: KV cache
---

[ACADEMIC - ARXIV]
标题: Diagnosing LLM Judge Reliability: Conformal Prediction Sets and Transitivity Violations
作者: Manan Gupta, Dhruv Kumar
链接: https://arxiv.org/abs/2604.15302v1
完整摘要: LLM-as-judge frameworks are increasingly used for automatic NLG evaluation, yet their per-instance reliability remains poorly understood. We present a two-pronged diagnostic toolkit applied to SummEval: $\textbf{(1)}$ a transitivity analysis that reveals widespread per-input inconsistency masked by low aggregate violation rates ($\barρ = 0.8$-$4.1\%$), with $33$-$67\%$ of documents exhibiting at least one directed 3-cycle; and $\textbf{(2)}$ split conformal prediction sets over 1-5 Likert scores providing theoretically-guaranteed $\geq(1{-}α)$ coverage, with set width serving as a per-instance reliability indicator ($r_s = {+}0.576$, $N{=}1{,}918$, $p < 10^{-100}$, pooled across all judges). Critically, prediction set width shows consistent cross-judge agreement ($\bar{r} = 0.32$-$0.38$), demonstrating it captures document-level difficulty rather than judge-specific noise. Across four judges and four criteria, both diagnostics converge: criterion matters more than judge, with relevance judged most reliably (avg. set size $\approx 3.0$) and coherence moderately so (avg. set size $\approx 3.9$), while fluency and consistency remain unreliable (avg. set size $\approx 4.9$). We release all code, prompts, and cached results.
匹配关键词: KV cache
---

[ACADEMIC - ARXIV]
标题: The Illusion of Equivalence: Systematic FP16 Divergence in KV-Cached Autoregressive Inference
作者: Ranjith Chodavarapu, Lei Xu
链接: https://arxiv.org/abs/2604.15409v1
完整摘要: KV caching is a ubiquitous optimization in autoregressive transformer inference, long presumed to be numerically equivalent to cache-free computation. This assumption fails under standard FP16 precision: cache-ON and cache-OFF execution paths employ different floating-point accumulation orderings which, due to FP16 non-associativity, produce a deterministic divergence in decoded token sequences. Across three open-weight models (LLaMA-2-7B, Mistral-7B-v0.3, Gemma-2-2B) evaluated on GSM8K, we observe a 100\% token divergence rate across all sampling strategies, including greedy decoding, which rules out sampling randomness as a cause, and also with cache-ON yielding higher accuracy in 8 of 9 conditions, where the accuracy difference serves as an indicator that the divergence direction is systematic rather than random. Controlled FP32 falsification reduces divergence by eight orders of magnitude, eliminates token flips, and drops the flip rate to exactly 0.0\%, confirming FP16 non-associativity as the sole causal driver. Layer-wise drift profiling reveals architecturally predictable propagation patterns: models using Grouped-Query Attention exhibit sharp divergence at the first layer, while Gemma's larger head dimension and sliding window attention produce uniform accumulation across all layers. Finally, activation patching of the entire residual stream fails to recover the cache-free trajectory, localizing the causal variable to the stateful KV cache. These findings establish that FP16 KV cache inference is fundamentally non-equivalent to recomputation and provide a mechanistic framework for understanding numerical instability in modern LLM inference systems.
匹配关键词: KV cache
---

[ACADEMIC - ARXIV]
标题: IE as Cache: Information Extraction Enhanced Agentic Reasoning
作者: Hang Lv, Sheng Liang, Hongchao Gu, Wei Guo, Defu Lian, Yong Liu, Hao Wang, Enhong Chen
链接: https://arxiv.org/abs/2604.14930v1
完整摘要: Information Extraction aims to distill structured, decision-relevant information from unstructured text, serving as a foundation for downstream understanding and reasoning. However, it is traditionally treated merely as a terminal objective: once extracted, the resulting structure is often consumed in isolation rather than maintained and reused during multi-step inference. Moving beyond this, we propose \textit{IE-as-Cache}, a framework that repurposes IE as a cognitive cache to enhance agentic reasoning. Drawing inspiration from hierarchical computer memory, our approach combines query-driven extraction with cache-aware reasoning to dynamically maintain compact intermediate information and filter noise. Experiments on challenging benchmarks across diverse LLMs demonstrate significant improvements in reasoning accuracy, indicating that IE can be effectively repurposed as a reusable cognitive resource and offering a promising direction for future research on downstream uses of IE.
匹配关键词: KV cache
---

