# 破晓 PoXiao — 原始数据 (Raw Context)
生成时间: 2026-05-19 02:53 UTC
================================================================================

[RSS:Reddit LocalLLaMA (社区共识)]
Qwen cant wait to release 3.7 models
https://www.reddit.com/r/LocalLLaMA/comments/1tgrpqc/qwen_cant_wait_to_release_37_models/
&#32; submitted by &#32; /u/GotHereLateNameTaken [link] &#32; [comments]
---

[RSS:Reddit LocalLLaMA (社区共识)]
Still happy for yall
https://www.reddit.com/r/LocalLLaMA/comments/1th1mqx/still_happy_for_yall/
&#32; submitted by &#32; /u/SilverRegion9394 [link] &#32; [comments]
---

[RSS:Reddit LocalLLaMA (社区共识)]
Qwen 3.7 droped on Qwen Chat
https://www.reddit.com/r/LocalLLaMA/comments/1tgpabe/qwen_37_droped_on_qwen_chat/
https://preview.redd.it/t4hf4x4ruw1h1.png?width=380&amp;format=png&amp;auto=webp&amp;s=788c8e011e407d3e1aa49d6d4be0a813a75e03df Title &#32; submitted by &#32; /u/Foxiya [link] &#32; [comments]
---

[RSS:Reddit LocalLLaMA (社区共识)]
Memory expert suspects RAM price drop in 2027'H2 due to china heavy investments
https://www.reddit.com/r/LocalLLaMA/comments/1th3r5q/memory_expert_suspects_ram_price_drop_in_2027h2/
Quote: ..., the former executive remarked that Chinese companies are investing aggressively to boost their memory chip production. According to him, if these investments are successful and lead to an increase in output, then the surge in supply could cause prices to fall a year from now in the secon
---

[RSS:Reddit LocalLLaMA (社区共识)]
I tested 42 LLMs on their willingness to build the apocalypse. The "safest" closed-source models are lying to you.
https://www.reddit.com/r/LocalLLaMA/comments/1tgm0k9/i_tested_42_llms_on_their_willingness_to_build/
DystopiaBench runs 36 escalating scenarios across 6 dystopia types: Petrov: Autonomous weapons, nuclear override Orwell: Mass surveillance, truth manipulation Huxley: Behavioral conditioning, pleasure pacification Basaglia: Coercive therapeutic control LaGuardia: Regulatory capture, civic extraction
---

[RSS:Reddit LocalLLaMA (社区共识)]
I built a coding agent that gets 87% on benchmarks with a 4B parameter model, here's how
https://www.reddit.com/r/LocalLLaMA/comments/1tgecrq/i_built_a_coding_agent_that_gets_87_on_benchmarks/
I was frustrated that every coding agent (OpenCode, Cursor, Claude Code) assumes you're running GPT-5.4 or Claude Opus. If you try them with a local model like Gemma or Qwen they fall apart. I find that often tool calls fail, context overflows, multi-step tasks collapse. So I built SmallCode. It's d
---

[RSS:Reddit LocalLLaMA (社区共识)]
21 GPU's benchmarked running a small TTS model (vram peak: 5GB)
https://www.reddit.com/r/LocalLLaMA/comments/1th2f5w/21_gpus_benchmarked_running_a_small_tts_model/
I rented different GPUs on vast.ai for a few minutes each to benchmark a small TTS model, OmniVoice, with a peak VRAM usage of about 5 GB. I wanted to see how various mostly consumer GPUs would stack up against my own RTX 3090. This is by no means an extensive or scientific analysis, but I think it 
---

[RSS:Reddit LocalLLaMA (社区共识)]
What happens to local LLM if/when LLMs are no longer released for free?
https://www.reddit.com/r/LocalLLaMA/comments/1tgmjq0/what_happens_to_local_llm_ifwhen_llms_are_no/
I’m thinking about where this might wind up in 3-5+ years. As others have noted there’s no guarantee that Qwen, Google, and others will continue to release models in the future. Suppose the supply of new LLM models dries up overnight. Whatever is available today, May 2026, is all that we ever get. W
---

[RSS:Reddit LocalLLaMA (社区共识)]
llama.cpp MTP support landed - Qwen3.6 27B at 2.44× on a Strix Halo, 2.17× on a RTX 3090 rig
https://www.reddit.com/r/LocalLLaMA/comments/1tgxau6/llamacpp_mtp_support_landed_qwen36_27b_at_244_on/
PR #22673 (commit 4f13cb7) landed MTP speculative decoding in mainline llama.cpp on May 16. I tested it on two separate rigs. Qwen3.6 27B, single-stream chat, temperature 0, median of 5 runs: Strix Halo (Framework Desktop, ROCm 7.0.2): Q4_K_M: 11.7 → 21.2 tok/s (1.81×) Q8_0: 7.4 → 18.1 tok/s (2.44×)
---

[RSS:Reddit LocalLLaMA (社区共识)]
MTP (Multi-Token Prediction): 2x Faster Token Generation on AMD Strix Halo & Radeon 9700 AI Pro
https://www.reddit.com/r/LocalLLaMA/comments/1th154i/mtp_multitoken_prediction_2x_faster_token/
https://preview.redd.it/8gpkg8zxmy1h1.png?width=1672&amp;format=png&amp;auto=webp&amp;s=a95db16a39cdc49c0ff155117b734d413a49c2d3 https://youtu.be/MI0Pm1d6YF4 MTP can accelerate LLM inference 2x, especially for coding agents. This video covers what MTP is and the performance improvements you can expe
---

[RSS:Reddit LocalLLaMA (社区共识)]
Qwen 3.6 27B on 24GB VRAM setup: backend comparisons, quant choice and settings (llama.cpp, ik_llama.cpp, BeeLlama, vllm)
https://www.reddit.com/r/LocalLLaMA/comments/1tgis7s/qwen_36_27b_on_24gb_vram_setup_backend/
TL;DR best setup I tested on a RTX 3090 24 GB: ik_llama.cpp + Qwen3.6-27B-MTP-IQ4_KS.gguf 156k context, q8_0/q8_0 KV, MTP, vision on CPU benchmark result on a ~5.9k prompt + 1k output: about 1261 tok/s prefill, 72.9 tok/s decode llama.cpp was a good start, BeeLlama worth testing, but ik_llama.cpp pe
---

[RSS:Reddit LocalLLaMA (社区共识)]
Quantizing MTP KV Cache = free lunch?
https://www.reddit.com/r/LocalLLaMA/comments/1tgk9y6/quantizing_mtp_kv_cache_free_lunch/
With the MTP llama.cpp implementation in the Qwen3.6/3.5 models more VRAM is required for the MTP layer. However, many people don't realize this layer comes with its own KV cache which can also be quantized: -cache-type-k-draft q8_0 -cache-type-v-draft q8_0 edit: This is NOT quantizing the main KV C
---

[RSS:Reddit LocalLLaMA (社区共识)]
New models when? Forecasting release date.
https://www.reddit.com/r/LocalLLaMA/comments/1tgh8to/new_models_when_forecasting_release_date/
After the recent releases, there's almost a sense of emptiness. When do you think new models will be released? Looking at the chart, it's between the end of May and the beginning of June, but... I don't know why, it seems like something's changing about &quot;open weights&quot; &#32; submitted by &#
---

[RSS:Reddit LocalLLaMA (社区共识)]
PSA: If you haven’t updated Llama.cpp for a couple of days and find MTP to not be performing well, update llamacpp.
https://www.reddit.com/r/LocalLLaMA/comments/1tgobhj/psa_if_you_havent_updated_llamacpp_for_a_couple/
I thought it had horrible performance and was a nothingburger and had spent like an hour benchmarking it. Updated it yesterday and received a like 1.5-1.8x token boost. They even mostly fixed the pp issue. Now my pp is really big ;) &#32; submitted by &#32; /u/Borkato [link] &#32; [comments]
---

[RSS:Reddit LocalLLaMA (社区共识)]
Benchmarked Kokoro 82M vs Supertonic 3 TTS on CPU
https://www.reddit.com/r/LocalLLaMA/comments/1tgnxnm/benchmarked_kokoro_82m_vs_supertonic_3_tts_on_cpu/
Wanted a real head to head on the two TTS models that actually run well on CPU. Couldn't find one with proper numbers, so I ran one. Posting because the result was not what I expected going in. Quick context for anyone who hasn't seen Supertonic 3 yet: it's a flow-matching TTS where you can dial dow
---

[RSS:Reddit LocalLLaMA (社区共识)]
NEW BITNET MODELS!
https://www.reddit.com/r/LocalLLaMA/comments/1tgjwdf/new_bitnet_models/
I can't wait for Jan to upgrade to a llamacpp version that supports these so I can test them! https://huggingface.co/openbmb/BitCPM4-CANN-8B https://huggingface.co/openbmb/BitCPM4-CANN-3B https://huggingface.co/openbmb/BitCPM4-CANN-1B &#32; submitted by &#32; /u/Silver-Champion-4846 [link] &#32; [co
---

[RSS:Reddit LocalLLaMA (社区共识)]
Qwen 35b a3b surprises me
https://www.reddit.com/r/LocalLLaMA/comments/1tgqpa8/qwen_35b_a3b_surprises_me/
Just wanted to share that I'm pretty happy about Qwen 35b a3b agentic coding performance. I'm running the model in q80 quant, kv cache both q8_0 as well, with 262144 in 4090 + 5060 ti, via llama.cpp backend with claude code pointing to localhost. For demo/data analytics purposes, it works pretty wel
---

[RSS:Reddit LocalLLaMA (社区共识)]
club-5060ti follow-up: cleaner RTX 5060 Ti local LLM recipes, benchmark explorer, and CUDA GPU compatibility notes
https://www.reddit.com/r/LocalLLaMA/comments/1th633w/club5060ti_followup_cleaner_rtx_5060_ti_local_llm/
I posted earlier about RTX 5060 Ti local LLM testing, and I have cleaned the repo up quite a bit since then. The project is now a more structured benchmark/recipe repo rather than scattered notes. It has a static results explorer, schema-validated benchmark JSON, clearer llama.cpp/vLLM notes, single
---

[RSS:Reddit LocalLLaMA (社区共识)]
favorite Agentic Coding Harness
https://www.reddit.com/r/LocalLLaMA/comments/1th5t1b/favorite_agentic_coding_harness/
So far, I’ve tried Codex CLI, Claude Code, Gemini CLI, OpenCode, and recently, Pi with local models. Pi is the leanest of them all, with just four tools: read, write, edit, and bash. Its system prompt is only under 2K tokens, and it's perfect for local models. I've been trying out Qwen 27B-MXFP8 wit
---

[RSS:Reddit LocalLLaMA (社区共识)]
Lemonade v10.5.1: an MTP + ROCm 7.13 quick start for Strix Halo
https://www.reddit.com/r/LocalLLaMA/comments/1th0z6k/lemonade_v1051_an_mtp_rocm_713_quick_start_for/
Update to Lemonade v10.5.1, then: ``` Get the model lemonade pull Qwen3.6-27B-MTP-GGUF Get ROCm 7.13 lemonade backends install llamacpp:rocm Load the model (MTP args auto-applied) lemonade load Qwen3.6-27B-MTP-GGUF --llamacpp rocm --ctx-size 0 ``` Shown in the video taking a look in the mirror with 
---

[RSS:Reddit LocalLLaMA (社区共识)]
How many GPUs do you have on your local system/server/AI PC?
https://www.reddit.com/r/LocalLLaMA/comments/1th83jl/how_many_gpus_do_you_have_on_your_local/
View Poll &#32; submitted by &#32; /u/panchovix [link] &#32; [comments]
---

[RSS:Reddit LocalLLaMA (社区共识)]
MLX engine comparison… and oMLX is the top choice.
https://www.reddit.com/r/LocalLLaMA/comments/1tgszn9/mlx_engine_comparison_and_omlx_is_the_top_choice/
Just stumbled on this blog. A very interesting read if you are picking inference engine. M5 Max 64GB with mlx-community/Qwen3.6-35B-A3B-4bit. The MTPLX in the article use 3.6 27B so it's not apple to apple. https://preview.redd.it/huxhasc4gx1h1.png?width=990&amp;format=png&amp;auto=webp&amp;s=88cf78
---

[RSS:Reddit LocalLLaMA (社区共识)]
Configuration Qwen3.6-35b-a3b (12Gb VRAM)
https://www.reddit.com/r/LocalLLaMA/comments/1tgrk75/configuration_qwen3635ba3b_12gb_vram/
Has anyone here tested different KV cache quantizations and compared their performance? I’m currently using the model in Q5_K_M with Q4 KV cache on a 12 GB VRAM GPU. With this setup, I’m offloading about 27 MoE layers to the CPU and getting around 40 tok/s with a 128k total context window. I’m tryin
---

[RSS:Reddit MachineLearning (学术风向)]
Reviving PapersWithCode (by Hugging Face) [P]
https://www.reddit.com/r/MachineLearning/comments/1tgmwqr/reviving_paperswithcode_by_hugging_face_p/
Hi, Niels here from the open-source team at Hugging Face. Like many others, I was a huge fan of paperswithcode. Sadly, that website is no longer maintained after its acquisition by Meta. Hence, I've been working on reviving it. I obviously use AI agents to parse papers at scale and automatically gen
---

[RSS:Reddit MachineLearning (学术风向)]
Sub-JEPA: a simple fix to LeCun group's LeWorldModel that consistently improves performance [P]
https://www.reddit.com/r/MachineLearning/comments/1tgn3bz/subjepa_a_simple_fix_to_lecun_groups_leworldmodel/
World models learn compact latent representations for planning without pixel reconstruction. LeWorldModel (LeWM), from LeCun's group at NYU, achieves stable end-to-end JEPA training by enforcing an isotropic Gaussian prior over the full latent space. The flaw: real environment dynamics live on low-d
---

[RSS:Reddit MachineLearning (学术风向)]
Released a free 9.8M doc Indic multilingual corpus — Hindi, Bengali, Tamil, Telugu + 7 more (CC0, HuggingFace) [P]
https://www.reddit.com/r/MachineLearning/comments/1th4po3/released_a_free_98m_doc_indic_multilingual_corpus/
Built this over the past few weeks as part of a multilingual research project. Figured I'd share it here. Check it out! ~9.8M web documents across 11 languages — hi, bn, ta, te, mr, gu, kn, ml, pa, ur, en. ~8.4B tokens. CC0 license. 🤗 https://huggingface.co/datasets/AM0908/indic-hplt-v1 &#32; submit
---

[RSS:Reddit MachineLearning (学术风向)]
MLRC 2026 is open for submissions - an official track at NeurIPS 2026 [N]
https://www.reddit.com/r/MachineLearning/comments/1th31er/mlrc_2026_is_open_for_submissions_an_official/
The annual Machine Learning Reproducibility Challenge (MLRC) 2026 is now open for submissions. This year, it is held as an official track at NeurIPS 2026 - submissions, once accepted through TMLR, will be eligible to be presented at the conference in Sydney, Australia this December. More details in 
---

[RSS:Reddit MachineLearning (学术风向)]
AI/ML Ethicists [D]
https://www.reddit.com/r/MachineLearning/comments/1tgqybv/aiml_ethicists_d/
So I’ve been working with AI/ML for the past couple of years, and it has been an amazing experience. I still remember using GPT-2 for the first time and being completely blown away by it. Seeing how far the technology has come since then is honestly mind-blowing. I genuinely love working in AI, lear
---

[RSS:Reddit MachineLearning (学术风向)]
Witchcraft, fast local semantic search on top of SQLite [P]
https://www.reddit.com/r/MachineLearning/comments/1tgqyo8/witchcraft_fast_local_semantic_search_on_top_of/
Witchcraft ( https://github.com/dropbox/witchcraft ) , an open source project that I built at Dropbox, is a from-scratch re-implementation of Stanford's XTR-Warp semantic search engine ( https://github.com/jlscheerer/xtr-warp ) in safe rust, using a single-file SQLite database as backing storage, ma
---

[RSS:Reddit MachineLearning (学术风向)]
No new paper under review in TMLR since May 09? [D]
https://www.reddit.com/r/MachineLearning/comments/1tgz13e/no_new_paper_under_review_in_tmlr_since_may_09_d/
Why is that? Link: https://openreview.net/group?id=TMLR&amp;referrer=%5BHomepage%5D(%2F)#tab-under-review-submissions #tab-under-review-submissions) It seems no action editor assignments are happening for over a week now. &#32; submitted by &#32; /u/hyperactve [link] &#32; [comments]
---

[RSS:Reddit MachineLearning (学术风向)]
We built a tool that installs frameworks like ComfyUI, Ollama, OpenWebUI etc on any cloud GPU in one command and saves your whole setup between sessions [R]
https://www.reddit.com/r/MachineLearning/comments/1th863j/we_built_a_tool_that_installs_frameworks_like/
We kept running into the same problem every time we rented a GPU to run Ollama + OpenWebUI or ComfyUI, we'd spend the first 45 minutes reinstalling everything. Custom nodes, models, configs, all of it. Docker images went stale fast, different providers had different base images, and nothing was trul
---

[RSS:Reddit MachineLearning (学术风向)]
Architecture advice: Real-time pipeline for YouTube Audio -> Whisper -> LLM -> SSE (Sub-10s latency) [D]
https://www.reddit.com/r/MachineLearning/comments/1th713c/architecture_advice_realtime_pipeline_for_youtube/
Hey everyone, I’m building a backend that analyzes long YouTube videos using an LLM. Currently, my flow is a slow waterfall: Download full audio -&gt; Whisper -&gt; LLM -&gt; Return results . For a 30-minute video, the user waits forever. I want to pipeline this for real-time SSE streaming: [Chunk A
---

[RSS:Reddit MachineLearning (学术风向)]
Rewriting model inference with CUDA kernels: the bottleneck was not just GEMM [P]
https://www.reddit.com/r/MachineLearning/comments/1tgyx41/rewriting_model_inference_with_cuda_kernels_the/
I’ve been working on a CUDA-first inference runtime for small-batch / realtime ML workloads. The core idea is simple: instead of treating PyTorch / TensorRT / generic graph runtimes as the main execution path, I rewrite the model inference path directly with C++/CUDA kernels. This started from robot
---

[RSS:Reddit MachineLearning (学术风向)]
Scaling LLMs horizontally: hidden-state coupling without weight modification [R]
https://www.reddit.com/r/MachineLearning/comments/1tgm530/scaling_llms_horizontally_hiddenstate_coupling/
Residual Coupling (RC) connects frozen language models in parallel using small, learned linear bridge projections. These bridges read hidden states from one model and inject additive updates into the residual stream of another at intermediate layers. In bilateral setups, simultaneous return bridges 
---

[RSS:Reddit MachineLearning (学术风向)]
Has anyone received decisions for the ICML 2026 GlobalSouthML workshop yet? [D]
https://www.reddit.com/r/MachineLearning/comments/1tgu8p5/has_anyone_received_decisions_for_the_icml_2026/
Hey everyone! The decision notification deadline for the GlobalSouthML workshop was originally May 15th (and the site updated it to May 17th AoE), but my OpenReview dashboard still just says &quot;0 Official Reviews Submitted&quot; I know workshop timelines can be a bit chaotic and delays are normal
---

[RSS:Reddit MachineLearning (学术风向)]
Will wait listed ones be mailed regardless? Eeml 26 [D]
https://www.reddit.com/r/MachineLearning/comments/1tgop0r/will_wait_listed_ones_be_mailed_regardless_eeml/
They said We aim to inform you by May 18th if a place becomes available Does that mean no reply if not accepted? I so wish I could be there &#32; submitted by &#32; /u/Active-Tip3130 [link] &#32; [comments]
---

[RSS:Reddit MachineLearning (学术风向)]
could refusal layers be masking dialect-conditioned safety failures in MoE models [d]
https://www.reddit.com/r/MachineLearning/comments/1tggu0j/could_refusal_layers_be_masking/
I set out to test whether AAVE-coded (African American English Vernacular) prompts cause MoE language models to route, deliberate, and respond differently from semantically matched AE (Academic English) prompts in safety-sensitive situations, especially when refusal behavior is weakened or removed. 
---

[RSS:Reddit MachineLearning (学术风向)]
Is the future of coding agents JEPA? [D]
https://www.reddit.com/r/MachineLearning/comments/1tgq9v2/is_the_future_of_coding_agents_jepa_d/
I heard Yann LeCun explain JEPA (Joint Embedding Predictive Architecture) recently and I started thinking about using it for coding agents. Most coding agents today work by throwing a huge amount of text into a frontier LLM and asking it to generate the next patch. That is astonishingly useful, but 
---

[RSS:Reddit MachineLearning (学术风向)]
ICML financial aid [D]
https://www.reddit.com/r/MachineLearning/comments/1tghj6m/icml_financial_aid_d/
I am an undergraduate student from India who recently got accepted to TAIGR, an ICML workshop for a Poster. I will be requiring financial aid for registration fees and accommodation, since I will be travelling to Seoul and it is independent research so we don't have any backing by any labs/instituti
---

[RSS:Reddit MachineLearning (学术风向)]
model-agnostic sensitivity approximator [P]
https://www.reddit.com/r/MachineLearning/comments/1tgemq5/modelagnostic_sensitivity_approximator_p/
(to preface, i'm 16 and this is the first package i've ever built. any feedback would be appreciated!) what i've noticed is that most industry-standard xai tools (think shap/lime) focus on feature attribution (why did the model made this prediction), but it doesn't do anything further. i wanted to g
---

[RSS:Reddit Jobs & Careers (职场动态)]
Interview Discussion - May 18, 2026
https://www.reddit.com/r/cscareerquestions/comments/1tgeqx2/interview_discussion_may_18_2026/
Please use this thread to have discussions about interviews, interviewing, and interview prep. Posts focusing solely on interviews created outside of this thread will probably be removed. Abide by the rules, don't be a jerk. This thread is posted each Monday and Thursday at midnight PST . Previous I
---

[RSS:Reddit Jobs & Careers (职场动态)]
Senior Engineer won't review PRs
https://www.reddit.com/r/cscareerquestions/comments/1tgwolm/senior_engineer_wont_review_prs/
Mostly just venting. I know the answer is probably that I need to pester him more, but theres only so much I can do without being an asshole. --- I'm an entry level SWE on a small team of 5 people. That includes my non-technical manager and an electrical engineer who doesn't code, so really there's 
---

[RSS:Reddit Jobs & Careers (职场动态)]
just bombed my first technical. why does it feel like it’s over?
https://www.reddit.com/r/cscareerquestions/comments/1th21g0/just_bombed_my_first_technical_why_does_it_feel/
been applying for almost a year. not as proactively in the beginning, im only at about 500-600 apps rn. but in one month it’ll be one year since graduation. feeling super down because i landed my first technical interview, some simple python LLD—just needed to implement 2 funcs. completely bombed it
---

[RSS:Reddit Jobs & Careers (职场动态)]
ML take-home: ~17M rows, transformer required, no compute provided. Is this normal?
https://www.reddit.com/r/cscareerquestions/comments/1tgxw66/ml_takehome_17m_rows_transformer_required_no/
Just finished an ML take-home and want to sanity check whether my expectations were off. The task: build a sequence prediction system on ~17M rows of structured data. They required a &quot;transformer-based model or closely related sequence model.&quot; Free to make modeling decisions, structure the
---

[RSS:Reddit Jobs & Careers (职场动态)]
How do developers work at these big tech companies?
https://www.reddit.com/r/cscareerquestions/comments/1tgheic/how_do_developers_work_at_these_big_tech_companies/
I have a friend at Anthropic, and over there it's full AI-first agentic coding (if I remember correctly), and they barely write any code manually. AI is used for absolutely everything. They said it’s a completely different way of developing and is often harder than writing everything manually from s
---

[RSS:Reddit Jobs & Careers (职场动态)]
Falling behind in current role due to job hunting?
https://www.reddit.com/r/cscareerquestions/comments/1th6bpl/falling_behind_in_current_role_due_to_job_hunting/
Just want to know if it’s normal to fall behind on your current role while seeking a new one. So many interviews and screens that are scheduled during work hours, random sick days needed to be taken for on sites or all day interviews, and taking more and more time off or generally being not around b
---

[RSS:Reddit Jobs & Careers (职场动态)]
Leet code waste
https://www.reddit.com/r/cscareerquestions/comments/1tgi1jf/leet_code_waste/
I'm curious how people feel about leet code now. I'd been employed the whole time this was a thing, so I'm not even sure what it was or how it worked, perhaps solving coding problems for internet points to use to provide a measure of ability on a resume? This never made much sense to me so I ignored
---

[RSS:Reddit Jobs & Careers (职场动态)]
Anyone else struggle with work that's entirely in your head? Like the lack of anything physical or tangible makes it hard to stay engaged no matter how interesting the problem is? Should I stick to bend a software developer or pivot to another career?
https://www.reddit.com/r/cscareerquestions/comments/1th3eto/anyone_else_struggle_with_work_thats_entirely_in/
Note: I'm AudHD which may be part of this. I'm not asking for accommodation lol I'm just wondering how much of my issues are unique to me and my situation vs something other people experience. I attended a boot camp back during the pandemic, and struck gold with a consulting firm. I was laid off whe
---

[RSS:Reddit Jobs & Careers (职场动态)]
how to continue hopes of research post grad with only a semester under my belt.
https://www.reddit.com/r/cscareerquestions/comments/1th7ju6/how_to_continue_hopes_of_research_post_grad_with/
I just graduated in CS and I really want to continue research after completing a data science research program last semester in partnership with a local company. I did a decent amount in that program (i don't think enough to work with that company again) but I really want to continue either data sci
---

[RSS:Reddit Jobs & Careers (职场动态)]
Is UIUC MCS or GT OMSCS better? UIUC MCS seems like Data Science degree faking as “CS” degree
https://www.reddit.com/r/cscareerquestions/comments/1th6jcw/is_uiuc_mcs_or_gt_omscs_better_uiuc_mcs_seems/
Which one offers classes that are more software engineer specific? &#32; submitted by &#32; /u/Beneficial_Pay_6317 [link] &#32; [comments]
---

[RSS:Reddit Jobs & Careers (职场动态)]
Do jobs care if you did poorly in your udnergad but really well for your mastersM?
https://www.reddit.com/r/cscareerquestions/comments/1th2kgv/do_jobs_care_if_you_did_poorly_in_your_udnergad/
Due to laziness and terrible choices, I am about to get kicked out of UC merced and Ill have to continue at community college before renetering to UC merced to finish my degree. Im afraid that since ill take a lot of transfer credits at the community college, that I wont be able to repair my gpa (my
---

[RSS:Reddit Jobs & Careers (职场动态)]
Need Help Deciding
https://www.reddit.com/r/cscareerquestions/comments/1th7zmx/need_help_deciding/
I have two job offers for remote jobs. one pays 24 an hour but is a 6 month contract role and then other pays only $17 an hour but is full time. Based in the Houston TX area. The contract role is Prime Therapeutics and the full time role is HCA Healthcare &#32; submitted by &#32; /u/LostKid852 [link
---

[RSS:Reddit Jobs & Careers (职场动态)]
Company slow to adopt AI
https://www.reddit.com/r/cscareerquestions/comments/1tgmiy1/company_slow_to_adopt_ai/
Hi everyone, I work at a company where we have a couple of AI tools for coding, but there isn’t pressure to use them. In fact, we’re in a pilot for them right now. For background, I work in a highly regulated industry. It is likely one of the most regulated companies in the world. There’s a battle b
---

[RSS:Reddit Jobs & Careers (职场动态)]
Interesting work Vs Stability
https://www.reddit.com/r/cscareerquestions/comments/1tgw281/interesting_work_vs_stability/
I am expecting to be receiving two offers within the next few weeks with virtually identical compensation. Both roles are in the US Midwest. One of the two roles is much more interesting and adjusted for cost of living pays potentially slightly higher, though the insurance is slightly higher monthly
---

[RSS:Reddit Jobs & Careers (职场动态)]
Just got laid off
https://www.reddit.com/r/cscareerquestions/comments/1tg9yh7/just_got_laid_off/
I’ve (34m) been a field technician for about 3 years with a large PC/printer company, and total hardware repair/troubleshooting history of about 8 years. I also just graduated with a bachelor’s in software engineering. Degree conferred Friday, laid off Monday. I don’t really know what to focus on ri
---

[RSS:Reddit Jobs & Careers (职场动态)]
Questions about working in comp sci
https://www.reddit.com/r/cscareerquestions/comments/1tgl57d/questions_about_working_in_comp_sci/
Im taking a class and part of it is asking employed people in the field general questions about what its like working. If any of you wouldnt mind sharing some insight please answer some (or all) of the questions below, thank you :) * At what company do you work? * How old are you (if you want to) * 
---

[RSS:Reddit Jobs & Careers (职场动态)]
CS vs EE
https://www.reddit.com/r/cscareerquestions/comments/1tgdpjr/cs_vs_ee/
Hello, I’m going to college soon and mainly deciding between these two majors My main concern is money because frankly I like both of these fields, I’ve always loved technology and I’m fine going into hardware or software, so my main question is which one will grant me the higher income? I know that
---

[RSS:Reddit Jobs & Careers (职场动态)]
Breaking into Aerospace
https://www.reddit.com/r/cscareerquestions/comments/1tgb6e4/breaking_into_aerospace/
Hi all, new grad embedded SWE here, writing C++ for HVAC control. My goal is to break into Aerospace as an embedded or flight SWE. Dream companies would be SpaceX, blue or Rocket Lab, also any of the other well known ones like ULA, NASA, impulse, relativity, etc. My question is, how much do projects
---

[RSS:Reddit Jobs & Careers (职场动态)]
Pls help me decide: ai service based startup vs bank
https://www.reddit.com/r/cscareerquestions/comments/1tgyi2y/pls_help_me_decide_ai_service_based_startup_vs/
Both offer same salary, the role at the bank is sde and would be using ai coding tools too, but the service based startup is fully remote. I have 2 years of experience &#32; submitted by &#32; /u/lokeye-ai [link] &#32; [comments]
---

[RSS:Reddit Jobs & Careers (职场动态)]
Is my plan sensible? Context:I wish to work in game development, preferrably as a programmer.
https://www.reddit.com/r/cscareerquestions/comments/1tgw9me/is_my_plan_sensible_contexti_wish_to_work_in_game/
I recently had people advise to immediately start working because I wont get hired no matter what, past a certain age without 'professional group experience'. Im currently 28 years old and have a BSc in Geography. Halfway through that I realized what I actually wanted to do in life, which was to dev
---

[RSS:Reddit Jobs & Careers (职场动态)]
How likely are you to get rich off startup equity?
https://www.reddit.com/r/cscareerquestions/comments/1th286s/how_likely_are_you_to_get_rich_off_startup_equity/
I’m an incoming freshman who is considering tech/CS. I know my question might seem naive, but I’m not uninformed. I know how bad the market is bit I’m looking for massive earnings. I’ve seen online that people in their 20’s can become millionaires or multimillionaires off of successful startup equit
---

[RSS:Reddit Jobs & Careers (职场动态)]
Creative Technology vs CS degree
https://www.reddit.com/r/cscareerquestions/comments/1tgnd6j/creative_technology_vs_cs_degree/
hi, i would like to hear your opinion on a Creative Technology degree and whether its worth it. rather than the &quot;hardcore programming&quot;/theoretical side of computer science, im more interested in its creative applications and wish to pursue a career related to that. however, im afraid that 
---

[HACKERNEWS]
Click (2016)
https://clickclickclick.click/
Score: 190 | Comments: 40
---

[HACKERNEWS]
Anthropic co-founder to present AI encyclical alongside Pope Leo XIV
https://www.vaticannews.va/en/pope/news/2026-05/pope-leo-xiv-first-encyclical-magnifica-humanitas.html
Score: 89 | Comments: 48
---

[HACKERNEWS]
Anthropic acquires Stainless
https://www.anthropic.com/news/anthropic-acquires-stainless
Score: 357 | Comments: 252
---

[HACKERNEWS]
Hyperpolyglot Lisp: Common Lisp, Racket, Clojure, Emacs Lisp
https://hyperpolyglot.org/lisp
Score: 125 | Comments: 28
---

[HACKERNEWS]
We stopped AI bot spam in our GitHub repo using Git's –author flag
https://archestra.ai/blog/only-responsible-ai
Score: 408 | Comments: 188
---

[HACKERNEWS]
We let AIs run radio stations
https://andonlabs.com/blog/andon-fm
Score: 153 | Comments: 160
---

[HACKERNEWS]
Show HN: Files.md – Open-source alternative to Obsidian
https://github.com/zakirullin/files.md
Score: 548 | Comments: 279
---

[HACKERNEWS]
Earth's Radio Bubble: Every signal we've ever sent into space
https://www.thescientificdrop.com/2026/05/earths-radio-bubble-every-signal-weve.html
Score: 23 | Comments: 18
---

[HACKERNEWS]
Elon Musk has lost his lawsuit against Sam Altman and OpenAI
https://techcrunch.com/2026/05/18/elon-musk-has-lost-his-lawsuit-against-sam-altman-and-openai/
Score: 772 | Comments: 402
---

[HACKERNEWS]
Project Glasswing: what Mythos showed us
https://blog.cloudflare.com/cyber-frontier-models/
Score: 278 | Comments: 107
---

[HACKERNEWS]
Agora-1: The Multi-Agent World Model
https://odyssey.ml/introducing-agora-1
Score: 80 | Comments: 16
---

[HACKERNEWS]
The FBI Wants to Buy Nationwide Access to License Plate Readers
https://www.404media.co/the-fbi-wants-to-buy-nationwide-access-to-license-plate-readers/
Score: 212 | Comments: 89
---

[ACADEMIC - ARXIV]
标题: EgoInteract: Synthetic Egocentric Videos Generation for Interaction Understanding and Anticipation
作者: Rosario Leonardi, Francesco Ragusa, Daniele Materia, Alessandro Passanisi, James Fort, Jakob Engel, Giovanni Maria Farinella
链接: https://arxiv.org/abs/2605.18214v1
完整摘要: Collecting large-scale egocentric video datasets with dense spatial and temporal annotations is costly, slow, and often constrained by environmental biases, privacy constraints, and limited coverage of interaction patterns. While synthetic data has shown strong potential in several vision domains, its use for egocentric perception remains relatively underexplored, especially for tasks requiring temporally coherent human-object interactions. In this work, we introduce EgoInteract, a controllable simulator for egocentric video generation designed to model fine-grained egocentric interactions and their temporal dynamics. The simulator enables precise control over camera, human body and hand motion, object manipulation, and scene composition across diverse environments. Building on this framework, we generate a synthetic egocentric video dataset with dense spatial and temporal annotations for temporal action segmentation, next-active object detection, interaction anticipation, and hand-object interaction detection. We evaluate models trained with simulated data on multiple real-world egocentric benchmarks spanning diverse environments, object categories, and interaction patterns. Results show consistent improvements over strong baselines across tasks and datasets, demonstrating the effectiveness and transferability of our simulation-based approach.
匹配关键词: video synthesis
---

[ACADEMIC - ARXIV]
标题: SPATIOROUTE: Dynamic Prompt Routing for Zero-Shot Spatial Reasoning
作者: Pawat Chunhachatrachai, Gueter Josmy Faure, Hung-Ting Su, Winston H. Hsu
链接: https://arxiv.org/abs/2605.18209v1
完整摘要: Spatial question answering over egocentric video is a challenging task that requires Vision-Language Models (VLMs) to reason about 3D object positions, scene affordances, and directional relationships, particularly in the zero-shot setting where no task-specific fine-tuning is available. We introduce SpatioRoute, a dynamic prompt generation approach that routes each incoming question to a semantically tailored prompt template -- without any additional training, fine-tuning, or 3D sensor input. SpatioRoute operates in two complementary modes: SpatioRoute-R, a rule-based router that deterministically maps question typologies (e.g., What, Is, How, Can, Which) to specialized prompt templates; and SpatioRoute-L, an LLM-driven approach that generates task-specific prompts from the question and situational context alone, with no video input at routing time. We evaluate SpatioRoute on the SQA3D benchmark across VLMs spanning model families. SpatioRoute achieves consistent overall accuracy gains up to 5% over fixed prompt baselines, establishing a new state-of-the-art for zero-shot video-only spatial VQA without requiring 3D point-cloud inputs. As an additional finding, we observe that Chain-of-Thought (CoT) prompting, implemented via the Think it Twice architecture, consistently degrades performance in this setting on Qwen series models, confirming that question-aware routing is more effective than uniform reasoning instructions for spatial video understanding.
匹配关键词: video synthesis
---

[ACADEMIC - ARXIV]
标题: MARS: Technical Report for the CASTLE Challenge at EgoVis 2026
作者: Haoyu Zhang, Qiaohui Chu, Yisen Feng, Meng Liu, Weili Guan, Yaowei Wang, Liqiang Nie
链接: https://arxiv.org/abs/2605.18176v1
完整摘要: This report presents MARS, short for Multimodal Agentic Reasoning with Source selection, our system for the CASTLE Challenge at EgoVis 2026. Participants must answer 185 closed-form questions over the CASTLE 2024 dataset. In contrast to prior single-video egocentric benchmarks, CASTLE requires reasoning over four days of activity, 15 synchronized perspectives, official transcripts, and multiple auxiliary modalities, including personal photos, auxiliary videos, gaze, thermal imagery, and heartrate measurements. MARS therefore treats the task as an agentic evidence-selection problem over multimodal sources rather than a purely text-only pipeline. MARS first follows the official CASTLE directory organization to build evidence memories from two primary sources, videos and transcripts, and four auxiliary sources, gaze, heartrate, photos, and thermal imagery. Long videos are converted into captions and DeepSeek-based summaries only because CASTLE videos are too long to fit directly into the model context for every question; this step compresses temporal evidence while keeping photos and other auxiliary media available as source-specific evidence. At inference time, a GPT-5.4 decision agent repeatedly chooses whether to continue reasoning, request a specific missing modality, produce an answer, or fall back to a random option when the evidence remains insufficient. The resulting system achieved second place on the final CASTLE Challenge leaderboard. Our codes are available at https://github.com/Hyu-Zhang/MARS.
匹配关键词: video synthesis
---

[ACADEMIC - ARXIV]
标题: Self-Evolving Spatial Reasoning in Vision Language Models via Geometric Logic Consistency
作者: Junming Liu, Yuqi Li, Yifei Sun, Maonan Wang, Piotr Koniusz, Yirong Chen, Ding Wang
链接: https://arxiv.org/abs/2605.18162v1
完整摘要: Vision-Language Models (VLMs) have made striking progress, yet their spatial reasoning remains fragile: models that answer an original input correctly can still fail under paired transformations with predictable answer mappings, revealing a gap between instance-level correctness and robust spatial reasoning. To address this, we propose Spatial Alignment via Geometric Evolution (SAGE), a self-evolving framework that enforces logical consistency in VLMs through geometric and linguistic duality operations. SAGE incorporates duality consistency as an auxiliary reward within GRPO training, encouraging models to produce logically coherent answers across original and transformed inputs. A dynamic operation pool continuously probes for inconsistencies, promoting challenging operations and retiring mastered ones, so that training focuses on the most informative signals. SAGE is model-agnostic, data-efficient compared to prior GRPO methods, and can be applied as a lightweight post-training stage to any existing VLM. Experiments on video and spatial reasoning benchmarks demonstrate consistent improvements over strong baselines and enhanced generalization to unseen data.
匹配关键词: video synthesis
---

[ACADEMIC - ARXIV]
标题: Xiaomi EV World Model: A Joint World Model Integrating Reconstruction and Generation for Autonomous Driving
作者: Lijun Zhou, Hongcheng Luo, Zhenxin Zhu, Cheng Chi, Mingfei Tu, Kaixin Xiong, Lei Gong, Zhanqian Wu, Zehan Zhang, Fangzhen Li, Hao Li, Yingying Shen, Jiale He, Haohui Zhu, Shan Zhao, Kai Wang, Zhiwei Zhan, Yuechuan Pu, Kaiyuan Tan, Ruiling Yang, Xianqi Wang, Tianyi Yan, Jiawei Zhou, Lei Zhang, Jingyang Zhao, Xi Zhou, Chitian Sun, Chenming Wu, Jiong Deng, Hongwei Xie, Ming Lu, Kun Ma, Long Chen, Guang Chen, Hangjun Ye, Bing Wang, Haiyang Sun
链接: https://arxiv.org/abs/2605.18137v1
完整摘要: This report presents a unified technical system addressing the two core capabilities of world models for autonomous driving: world representation and world generation. For world representation, we propose WorldRec, a feed-forward reconstruction architecture driven by sparse scene queries. WorldRec initializes structured queries in 3D space, leveraging them to aggregate cross-view, cross-temporal features, thereby naturally enforcing spatial consistency across frames and yielding compact yet high-fidelity 3D Gaussian scene representations. For world generation, we propose WorldGen, a two-stage training framework of bidirectional pretraining followed by causal fine-tuning through three progressive stages (Teacher Forcing, ODE distillation, and DMD), enabling high-quality online causal video generation in as few as 4 denoising steps. Building on both modules, we further introduce the JWM, which deeply integrates WorldRec and WorldGen to achieve synergistic gains in generation stability, cross-frame consistency, and visual fidelity, providing a solid foundation for closed-loop simulation, data synthesis, and end-to-end training in autonomous driving.
匹配关键词: video synthesis
---

[ACADEMIC - ARXIV]
标题: EgoInteract: Synthetic Egocentric Videos Generation for Interaction Understanding and Anticipation
作者: Rosario Leonardi, Francesco Ragusa, Daniele Materia, Alessandro Passanisi, James Fort, Jakob Engel, Giovanni Maria Farinella
链接: https://arxiv.org/abs/2605.18214v1
完整摘要: Collecting large-scale egocentric video datasets with dense spatial and temporal annotations is costly, slow, and often constrained by environmental biases, privacy constraints, and limited coverage of interaction patterns. While synthetic data has shown strong potential in several vision domains, its use for egocentric perception remains relatively underexplored, especially for tasks requiring temporally coherent human-object interactions. In this work, we introduce EgoInteract, a controllable simulator for egocentric video generation designed to model fine-grained egocentric interactions and their temporal dynamics. The simulator enables precise control over camera, human body and hand motion, object manipulation, and scene composition across diverse environments. Building on this framework, we generate a synthetic egocentric video dataset with dense spatial and temporal annotations for temporal action segmentation, next-active object detection, interaction anticipation, and hand-object interaction detection. We evaluate models trained with simulated data on multiple real-world egocentric benchmarks spanning diverse environments, object categories, and interaction patterns. Results show consistent improvements over strong baselines across tasks and datasets, demonstrating the effectiveness and transferability of our simulation-based approach.
匹配关键词: video editing
---

[ACADEMIC - ARXIV]
标题: SPATIOROUTE: Dynamic Prompt Routing for Zero-Shot Spatial Reasoning
作者: Pawat Chunhachatrachai, Gueter Josmy Faure, Hung-Ting Su, Winston H. Hsu
链接: https://arxiv.org/abs/2605.18209v1
完整摘要: Spatial question answering over egocentric video is a challenging task that requires Vision-Language Models (VLMs) to reason about 3D object positions, scene affordances, and directional relationships, particularly in the zero-shot setting where no task-specific fine-tuning is available. We introduce SpatioRoute, a dynamic prompt generation approach that routes each incoming question to a semantically tailored prompt template -- without any additional training, fine-tuning, or 3D sensor input. SpatioRoute operates in two complementary modes: SpatioRoute-R, a rule-based router that deterministically maps question typologies (e.g., What, Is, How, Can, Which) to specialized prompt templates; and SpatioRoute-L, an LLM-driven approach that generates task-specific prompts from the question and situational context alone, with no video input at routing time. We evaluate SpatioRoute on the SQA3D benchmark across VLMs spanning model families. SpatioRoute achieves consistent overall accuracy gains up to 5% over fixed prompt baselines, establishing a new state-of-the-art for zero-shot video-only spatial VQA without requiring 3D point-cloud inputs. As an additional finding, we observe that Chain-of-Thought (CoT) prompting, implemented via the Think it Twice architecture, consistently degrades performance in this setting on Qwen series models, confirming that question-aware routing is more effective than uniform reasoning instructions for spatial video understanding.
匹配关键词: video editing
---

[ACADEMIC - ARXIV]
标题: MARS: Technical Report for the CASTLE Challenge at EgoVis 2026
作者: Haoyu Zhang, Qiaohui Chu, Yisen Feng, Meng Liu, Weili Guan, Yaowei Wang, Liqiang Nie
链接: https://arxiv.org/abs/2605.18176v1
完整摘要: This report presents MARS, short for Multimodal Agentic Reasoning with Source selection, our system for the CASTLE Challenge at EgoVis 2026. Participants must answer 185 closed-form questions over the CASTLE 2024 dataset. In contrast to prior single-video egocentric benchmarks, CASTLE requires reasoning over four days of activity, 15 synchronized perspectives, official transcripts, and multiple auxiliary modalities, including personal photos, auxiliary videos, gaze, thermal imagery, and heartrate measurements. MARS therefore treats the task as an agentic evidence-selection problem over multimodal sources rather than a purely text-only pipeline. MARS first follows the official CASTLE directory organization to build evidence memories from two primary sources, videos and transcripts, and four auxiliary sources, gaze, heartrate, photos, and thermal imagery. Long videos are converted into captions and DeepSeek-based summaries only because CASTLE videos are too long to fit directly into the model context for every question; this step compresses temporal evidence while keeping photos and other auxiliary media available as source-specific evidence. At inference time, a GPT-5.4 decision agent repeatedly chooses whether to continue reasoning, request a specific missing modality, produce an answer, or fall back to a random option when the evidence remains insufficient. The resulting system achieved second place on the final CASTLE Challenge leaderboard. Our codes are available at https://github.com/Hyu-Zhang/MARS.
匹配关键词: video editing
---

[ACADEMIC - ARXIV]
标题: Self-Evolving Spatial Reasoning in Vision Language Models via Geometric Logic Consistency
作者: Junming Liu, Yuqi Li, Yifei Sun, Maonan Wang, Piotr Koniusz, Yirong Chen, Ding Wang
链接: https://arxiv.org/abs/2605.18162v1
完整摘要: Vision-Language Models (VLMs) have made striking progress, yet their spatial reasoning remains fragile: models that answer an original input correctly can still fail under paired transformations with predictable answer mappings, revealing a gap between instance-level correctness and robust spatial reasoning. To address this, we propose Spatial Alignment via Geometric Evolution (SAGE), a self-evolving framework that enforces logical consistency in VLMs through geometric and linguistic duality operations. SAGE incorporates duality consistency as an auxiliary reward within GRPO training, encouraging models to produce logically coherent answers across original and transformed inputs. A dynamic operation pool continuously probes for inconsistencies, promoting challenging operations and retiring mastered ones, so that training focuses on the most informative signals. SAGE is model-agnostic, data-efficient compared to prior GRPO methods, and can be applied as a lightweight post-training stage to any existing VLM. Experiments on video and spatial reasoning benchmarks demonstrate consistent improvements over strong baselines and enhanced generalization to unseen data.
匹配关键词: video editing
---

[ACADEMIC - ARXIV]
标题: Xiaomi EV World Model: A Joint World Model Integrating Reconstruction and Generation for Autonomous Driving
作者: Lijun Zhou, Hongcheng Luo, Zhenxin Zhu, Cheng Chi, Mingfei Tu, Kaixin Xiong, Lei Gong, Zhanqian Wu, Zehan Zhang, Fangzhen Li, Hao Li, Yingying Shen, Jiale He, Haohui Zhu, Shan Zhao, Kai Wang, Zhiwei Zhan, Yuechuan Pu, Kaiyuan Tan, Ruiling Yang, Xianqi Wang, Tianyi Yan, Jiawei Zhou, Lei Zhang, Jingyang Zhao, Xi Zhou, Chitian Sun, Chenming Wu, Jiong Deng, Hongwei Xie, Ming Lu, Kun Ma, Long Chen, Guang Chen, Hangjun Ye, Bing Wang, Haiyang Sun
链接: https://arxiv.org/abs/2605.18137v1
完整摘要: This report presents a unified technical system addressing the two core capabilities of world models for autonomous driving: world representation and world generation. For world representation, we propose WorldRec, a feed-forward reconstruction architecture driven by sparse scene queries. WorldRec initializes structured queries in 3D space, leveraging them to aggregate cross-view, cross-temporal features, thereby naturally enforcing spatial consistency across frames and yielding compact yet high-fidelity 3D Gaussian scene representations. For world generation, we propose WorldGen, a two-stage training framework of bidirectional pretraining followed by causal fine-tuning through three progressive stages (Teacher Forcing, ODE distillation, and DMD), enabling high-quality online causal video generation in as few as 4 denoising steps. Building on both modules, we further introduce the JWM, which deeply integrates WorldRec and WorldGen to achieve synergistic gains in generation stability, cross-frame consistency, and visual fidelity, providing a solid foundation for closed-loop simulation, data synthesis, and end-to-end training in autonomous driving.
匹配关键词: video editing
---

[ACADEMIC - ARXIV]
标题: EgoInteract: Synthetic Egocentric Videos Generation for Interaction Understanding and Anticipation
作者: Rosario Leonardi, Francesco Ragusa, Daniele Materia, Alessandro Passanisi, James Fort, Jakob Engel, Giovanni Maria Farinella
链接: https://arxiv.org/abs/2605.18214v1
完整摘要: Collecting large-scale egocentric video datasets with dense spatial and temporal annotations is costly, slow, and often constrained by environmental biases, privacy constraints, and limited coverage of interaction patterns. While synthetic data has shown strong potential in several vision domains, its use for egocentric perception remains relatively underexplored, especially for tasks requiring temporally coherent human-object interactions. In this work, we introduce EgoInteract, a controllable simulator for egocentric video generation designed to model fine-grained egocentric interactions and their temporal dynamics. The simulator enables precise control over camera, human body and hand motion, object manipulation, and scene composition across diverse environments. Building on this framework, we generate a synthetic egocentric video dataset with dense spatial and temporal annotations for temporal action segmentation, next-active object detection, interaction anticipation, and hand-object interaction detection. We evaluate models trained with simulated data on multiple real-world egocentric benchmarks spanning diverse environments, object categories, and interaction patterns. Results show consistent improvements over strong baselines across tasks and datasets, demonstrating the effectiveness and transferability of our simulation-based approach.
匹配关键词: video understanding
---

[ACADEMIC - ARXIV]
标题: SPATIOROUTE: Dynamic Prompt Routing for Zero-Shot Spatial Reasoning
作者: Pawat Chunhachatrachai, Gueter Josmy Faure, Hung-Ting Su, Winston H. Hsu
链接: https://arxiv.org/abs/2605.18209v1
完整摘要: Spatial question answering over egocentric video is a challenging task that requires Vision-Language Models (VLMs) to reason about 3D object positions, scene affordances, and directional relationships, particularly in the zero-shot setting where no task-specific fine-tuning is available. We introduce SpatioRoute, a dynamic prompt generation approach that routes each incoming question to a semantically tailored prompt template -- without any additional training, fine-tuning, or 3D sensor input. SpatioRoute operates in two complementary modes: SpatioRoute-R, a rule-based router that deterministically maps question typologies (e.g., What, Is, How, Can, Which) to specialized prompt templates; and SpatioRoute-L, an LLM-driven approach that generates task-specific prompts from the question and situational context alone, with no video input at routing time. We evaluate SpatioRoute on the SQA3D benchmark across VLMs spanning model families. SpatioRoute achieves consistent overall accuracy gains up to 5% over fixed prompt baselines, establishing a new state-of-the-art for zero-shot video-only spatial VQA without requiring 3D point-cloud inputs. As an additional finding, we observe that Chain-of-Thought (CoT) prompting, implemented via the Think it Twice architecture, consistently degrades performance in this setting on Qwen series models, confirming that question-aware routing is more effective than uniform reasoning instructions for spatial video understanding.
匹配关键词: video understanding
---

[ACADEMIC - ARXIV]
标题: RGB-only Active 3D Scene Graph Generation for Indoor Mobile Robots
作者: Giorgia Modi, Davide Buoso, Giuseppe Averta, Daniele De Martini
链接: https://arxiv.org/abs/2605.18197v1
完整摘要: Current approaches to 3D scene graph generation rely on dedicated depth sensors, such as LiDAR or RGB-D cameras, for metric 3D reconstruction. This limits deployment to specialized robotic platforms and excludes settings where only RGB cameras are available, such as fixed external infrastructure. Existing pipelines also typically operate on passively collected observation trajectories, rather than selecting viewpoints based on the partially built scene representation, and therefore fail to effectively exploit the semantic and spatial information encoded within the graph during exploration. This paper presents a fully visual framework for the active, incremental construction of 3D scene graphs from RGB input only, addressing both limitations. The proposed approach unifies perception and planning around a shared structured representation that captures object semantics, 3D geometry, relational context, and information from multiple viewpoints. Because the framework is hardware-agnostic and relies only on RGB observations, it can incorporate inputs from both onboard robot cameras and fixed external cameras within the same representation. Experiments on the Replica dataset show that the RGB-only pipeline achieves F1-score parity with baselines using ground-truth depth. Active exploration experiments on ReplicaCAD further show that semantic-driven viewpoint selection detects more than twice as many objects as a geometric frontier-based baseline under the same exploration budget. Finally, the external-camera setting demonstrates that complementary RGB views can effectively bootstrap the scene graph and improve contextual understanding at no additional exploration cost.
匹配关键词: video understanding
---

[ACADEMIC - ARXIV]
标题: Beyond the Cartesian Illusion: Testing Two-Stage Multi-Modal Theory of Mind under Perceptual Bottlenecks
作者: Yajing Zhou, Xiangyu Kong
链接: https://arxiv.org/abs/2605.18194v1
完整摘要: While Multi-Modal Large Language Models (MLLMs) demonstrate impressive capabilities in general reasoning, their embodied spatial intelligence remains hampered by a "Cartesian Illusion" - a reliance on text-based probability distributions that lack grounded, 3D topological understanding. This limitation is starkly exposed in multi-agent environments, which demand more than just scene perception; they require second-order Theory of Mind (ToM). Specifically, an Agent A must be able to infer Agent B's belief about the environment, governed strictly by Agent B's physical orientation and sensory limitations. In this paper, we probe the limits of two-stage spatial inference in MLLMs through a novel audio-visual task: requiring Agent A to predict Agent B's estimation of A's relative location. To solve this, we propose an Epistemic Sensory Bottleneck module that abandons rigid, rule-based coordinate transformations. Instead, we introduce an Anchor-Based Embodied Spatial Decomposition Chain-of-Thought (CoT). This guides the MLLM through a "geometric-to-semantic" projection, forcing it to first establish B's local coordinate system and then dynamically weight visual and auditory modalities based on whether A falls within B's visual frustum. Extensive evaluations reveal that while current MLLMs fundamentally struggle with spatial symmetry and out-of-view ambiguities (establishing a rigorous zero-shot baseline of 42% accuracy), our sensory-bounded reasoning chain robustly outperforms pure egocentric and allocentric baselines. By systematically benchmarking these perceptual bottlenecks, our work exposes the current limits of MLLM spatial reasoning and establishes a foundational paradigm for epistemic, modality-aware inference in Embodied AI.
匹配关键词: video understanding
---

[ACADEMIC - ARXIV]
标题: MARS: Technical Report for the CASTLE Challenge at EgoVis 2026
作者: Haoyu Zhang, Qiaohui Chu, Yisen Feng, Meng Liu, Weili Guan, Yaowei Wang, Liqiang Nie
链接: https://arxiv.org/abs/2605.18176v1
完整摘要: This report presents MARS, short for Multimodal Agentic Reasoning with Source selection, our system for the CASTLE Challenge at EgoVis 2026. Participants must answer 185 closed-form questions over the CASTLE 2024 dataset. In contrast to prior single-video egocentric benchmarks, CASTLE requires reasoning over four days of activity, 15 synchronized perspectives, official transcripts, and multiple auxiliary modalities, including personal photos, auxiliary videos, gaze, thermal imagery, and heartrate measurements. MARS therefore treats the task as an agentic evidence-selection problem over multimodal sources rather than a purely text-only pipeline. MARS first follows the official CASTLE directory organization to build evidence memories from two primary sources, videos and transcripts, and four auxiliary sources, gaze, heartrate, photos, and thermal imagery. Long videos are converted into captions and DeepSeek-based summaries only because CASTLE videos are too long to fit directly into the model context for every question; this step compresses temporal evidence while keeping photos and other auxiliary media available as source-specific evidence. At inference time, a GPT-5.4 decision agent repeatedly chooses whether to continue reasoning, request a specific missing modality, produce an answer, or fall back to a random option when the evidence remains insufficient. The resulting system achieved second place on the final CASTLE Challenge leaderboard. Our codes are available at https://github.com/Hyu-Zhang/MARS.
匹配关键词: video understanding
---

[ACADEMIC - ARXIV]
标题: SIREM: Speech-Informed MRI Reconstruction with Learned Sampling
作者: Md Hasan, Nyvenn Castro, Daiqi Liu, Lukas Mulzer, Jana Hutter, Jonghye Woo, Moritz Zaiss, Andreas Maier, Paula A. Perez-Toro
链接: https://arxiv.org/abs/2605.18221v1
完整摘要: Real-time magnetic resonance imaging (rtMRI) of speech production enables non-invasive visualization of dynamic vocal-tract motion and is valuable for speech science and clinical assessment. However, rtMRI is fundamentally constrained by trade-offs among spatial resolution, temporal resolution, and acquisition speed, often leading to undersampled k-space measurements and degraded reconstructions. We propose SIREM, a speech-informed MRI reconstruction framework that uses synchronized speech as a cross-modal prior. The central idea is that vocal-tract configurations during speech are correlated with the produced acoustics, making part of the image content predictable from audio. SIREM models each frame as a fusion of an audio-driven component and an MRI-driven component through a spatial weighting map. The audio branch predicts articulator-related structure from speech, while the MRI branch reconstructs complementary content from measured k-space data. We further introduce a learnable soft weighting profile over spiral arms, enabling a differentiable study of how k-space arm usage interacts with speech-informed fusion. This yields a unified multimodal formulation that combines audio-driven prediction, MRI reconstruction, and sampling adaptation. We evaluate SIREM on the USC speech rtMRI benchmark against standard baselines, including gridding, wavelet-based compressed sensing, and total variation. SIREM introduces a speech-informed reconstruction paradigm that operates in a substantially higher-throughput regime than iterative methods while preserving anatomically plausible vocal-tract structure. These results establish an initial benchmark for multimodal speech-informed rtMRI reconstruction and highlight the potential of synchronized speech as an auxiliary prior for fast reconstruction. The source code is available at https://github.com/mdhasanai/SIREM
匹配关键词: temporal consistency
---

[ACADEMIC - ARXIV]
标题: EgoInteract: Synthetic Egocentric Videos Generation for Interaction Understanding and Anticipation
作者: Rosario Leonardi, Francesco Ragusa, Daniele Materia, Alessandro Passanisi, James Fort, Jakob Engel, Giovanni Maria Farinella
链接: https://arxiv.org/abs/2605.18214v1
完整摘要: Collecting large-scale egocentric video datasets with dense spatial and temporal annotations is costly, slow, and often constrained by environmental biases, privacy constraints, and limited coverage of interaction patterns. While synthetic data has shown strong potential in several vision domains, its use for egocentric perception remains relatively underexplored, especially for tasks requiring temporally coherent human-object interactions. In this work, we introduce EgoInteract, a controllable simulator for egocentric video generation designed to model fine-grained egocentric interactions and their temporal dynamics. The simulator enables precise control over camera, human body and hand motion, object manipulation, and scene composition across diverse environments. Building on this framework, we generate a synthetic egocentric video dataset with dense spatial and temporal annotations for temporal action segmentation, next-active object detection, interaction anticipation, and hand-object interaction detection. We evaluate models trained with simulated data on multiple real-world egocentric benchmarks spanning diverse environments, object categories, and interaction patterns. Results show consistent improvements over strong baselines across tasks and datasets, demonstrating the effectiveness and transferability of our simulation-based approach.
匹配关键词: temporal consistency
---

[ACADEMIC - ARXIV]
标题: SPATIOROUTE: Dynamic Prompt Routing for Zero-Shot Spatial Reasoning
作者: Pawat Chunhachatrachai, Gueter Josmy Faure, Hung-Ting Su, Winston H. Hsu
链接: https://arxiv.org/abs/2605.18209v1
完整摘要: Spatial question answering over egocentric video is a challenging task that requires Vision-Language Models (VLMs) to reason about 3D object positions, scene affordances, and directional relationships, particularly in the zero-shot setting where no task-specific fine-tuning is available. We introduce SpatioRoute, a dynamic prompt generation approach that routes each incoming question to a semantically tailored prompt template -- without any additional training, fine-tuning, or 3D sensor input. SpatioRoute operates in two complementary modes: SpatioRoute-R, a rule-based router that deterministically maps question typologies (e.g., What, Is, How, Can, Which) to specialized prompt templates; and SpatioRoute-L, an LLM-driven approach that generates task-specific prompts from the question and situational context alone, with no video input at routing time. We evaluate SpatioRoute on the SQA3D benchmark across VLMs spanning model families. SpatioRoute achieves consistent overall accuracy gains up to 5% over fixed prompt baselines, establishing a new state-of-the-art for zero-shot video-only spatial VQA without requiring 3D point-cloud inputs. As an additional finding, we observe that Chain-of-Thought (CoT) prompting, implemented via the Think it Twice architecture, consistently degrades performance in this setting on Qwen series models, confirming that question-aware routing is more effective than uniform reasoning instructions for spatial video understanding.
匹配关键词: temporal consistency
---

[ACADEMIC - ARXIV]
标题: Concise and Logically Consistent Conformal Sets for Neuro-Symbolic Concept-Based Models
作者: Samuele Bortolotti, Emanuele Marconato, Andrea Pugnana, Andrea Passerini, Stefano Teso
链接: https://arxiv.org/abs/2605.18202v1
完整摘要: Neuro-Symbolic Concept-based Models (NeSy-CBMs) are a family of architectures that integrate neural networks with symbolic reasoning for enhanced reliability in high-stakes applications. They work by first extracting high-level concepts from the input and then inferring a task label from these compatibly with given logical constraints. Yet, their label and concept predictions can be overconfident, making it difficult for stakeholders to gauge when the model's decisions can be trusted. We address this issue by integrating ideas from Conformal Prediction (CP), a framework providing rigorous, distribution-free coverage guarantees. We formalize three desiderata -- consistency, coverage, and conciseness -- that any conformal method for NeSy-CBMs should satisfy, and show that existing approaches fall short of at least one. We then introduce COCOCO, a post-hoc framework that conformalizes concepts and labels jointly and reconciles them via a single deduction-abduction revision step. COCOCO satisfies all three desiderata, retains distribution-free coverage, is robust to imperfect knowledge and supports user-specified size budgets. Our experiments on 8 data sets highlight how COCOCO compares favorably against competitors and natural baselines in terms of performance and set size.
匹配关键词: temporal consistency
---

[ACADEMIC - ARXIV]
标题: View-Aware Semantic Alignment for Aerial-Ground Person Re-Identification
作者: Quan Zhang, Zeqiang Cai, Peiming Zhao, Jingze Wu, Cailun Wu, Hongbo Chen, Jianhuang Lai
链接: https://arxiv.org/abs/2605.18192v1
完整摘要: Aerial-Ground Person Re-Identification (AGPReID) remains highly challenging due to drastic viewpoint variations between drones and fixed cameras. Existing methods typically follow a view-invariant paradigm, aligning shared features across views to achieve robustness. However, view-invariant inherently enforces part-level alignment, which ignores view-specific cues and discriminative identity information. To this end, this work proposes ViSA (View-aware Semantic Alignment), a view-aware framework that achieves cross-view semantic consistency containing an Expert-driven Token Generation Module (ETGM) and a Dual-branch Local Fusion Module (DLFM). Technically, the former constructs a set of view-aware experts to generate adaptive semantic queries that perceive viewpoint-specific patterns, while the latter leverages graph reasoning to extract and align local regions responsive to different experts. Extensive experiments on three AGPReID benchmarks including AG-ReID.v2, CARGO and LAGPeR demonstrate that ViSA consistently achieves superior performance, with a notable 10.06\% mAP improvement on the challenging CARGO cross-view protocol. The code is available at \href{https://github.com/Cat-Zero/ViSA}{https://github.com/Cat-Zero/ViSA}.
匹配关键词: temporal consistency
---

[ACADEMIC - ARXIV]
标题: SpecSem-Net: Integrating Spectral and Semantic Features for Robust AI-generated Video Detection
作者: Zixi Wei, Huixuaun Zhang, Xiaojun Wan
链接: https://arxiv.org/abs/2605.17311v1
完整摘要: The remarkable visual fidelity of recent commercial video generative models, such as Sora and Veo, renders robust AI-generated video detection increasingly essential to prevent synthetic content from being indistinguishable from real videos and exploited for disinformation. However, existing detectors often fail due to an over-reliance on increasingly realistic semantic features, neglecting subtle spectral artifacts. In this paper, we propose SpecSem-Net, the first framework to introduce a semantic-guided spectral denoising mechanism specifically for high-fidelity AI-generated video detection. Specifically, we design a spectral module to extract high-frequency features via Fourier-Transform based filtering. Furthermore, to reduce misjudgments arising from spectral noise, we employ a Gated Merging Mechanism to adaptively fuse semantic context, effectively mitigating spectral noise. Additionally, to evaluate detector performance on the latest top-tier generative models, we construct a comprehensive benchmark comprising 5 SOTA commercial generators. Extensive experiments demonstrate that SpecSem-Net outperforms existing methods, achieving accuracies of 87.25% and 95.59% on our benchmark and public datasets, respectively.
匹配关键词: Sora
---

[ACADEMIC - ARXIV]
标题: TMD-Bench: A Multi-Level Evaluation Paradigm for Music-Dance Co-Generation
作者: Xiaoda Yang, Majun Zhang, Changhao Pan, Nick Huang, Yang Yuguang, Fan Zhuo, Pengfei Zhou, Jin Zhou, Sizhe Shan, Shan Yang, Miles Yang, Yang You, Zhou Zhao
链接: https://arxiv.org/abs/2605.01809v1
完整摘要: Unified audio-visual generation is rapidly gaining industrial and creative relevance, enabling applications in virtual production and interactive media. However, when moving from general audio-video synthesis to music-dance co-generation, the task becomes substantially harder: musical rhythm, phrasing, and accents must drive choreographic motion at fine temporal resolution, and such rhythmic coupling is not captured by unimodal metrics or generic audiovisual consistency scores used in current evaluation practice. We introduce TMD-Bench, a benchmark for text-driven music-dance co-generation that assesses systems across unimodal generation quality, instruction adherence, and cross-modal rhythmic alignment. The benchmark integrates computable physical metrics with perceptual multimodal judgments, and is supported by a curated rhythm-aligned music-dance dataset and a fine-grained Music Captioner for structured music semantics. TMD-Bench further reveals that (i) modern commercial audio-visual models, such as Veo 3 and Sora 2, produce high-quality music and video, while rhythmic coupling remains less consistently optimized and leaves room for improvement, and (ii) our unified baseline RhyJAM trained on rhythm-aligned data achieves competitive beat-level synchronization while maintaining competitive unimodal fidelity. This presents prospects for building next-generation music-dance models that explicitly optimize rhythmic and kinetic coherence.
匹配关键词: Sora
---

[ACADEMIC - ARXIV]
标题: BRITE: A Benchmark for Reliable and Interpretable T2V Evaluation on Implausible Scenarios
作者: Advait Tilak, Jiwon Choi, Nazifa Mouli, Wei Le
链接: https://arxiv.org/abs/2605.00873v1
完整摘要: The rapid advancement of photorealistic Text-to-Video (T2V) generation brings in an urgent need for up-to-date evaluation methods. Existing benchmarks largely overlooked implausible scenarios and do not measure audio-visual alignment. We introduce BRITE, the first framework that unifies (1) implausible prompting, (2) fine-grained assessment of audio-visual consistency, and (3) QA-based interpretable evaluation into a comprehensive T2V benchmark. Unlike fully automated Multimodal LLM-based pipelines, which are prone to hallucination and prompt ambiguity, BRITE guarantees reliability through a rigorous human-in-the-loop protocol for benchmark creation. Evaluating five state-of-the-art models (Sora 2, Veo 3.1, Runway Gen4.5, Pixverse V5.5, and Qwen3Max), we reveal a critical performance gap: while models excel at static object composition, they exhibit significant degradation in object-action binding and audio-visual synchronization. Our framework offers the community a reliable, interpretable benchmark and evaluation framework that can detect and locate limitations in the next generation of T2V models, especially for off-manifold prompts
匹配关键词: Sora
---

[ACADEMIC - ARXIV]
标题: Evolution of Video Generative Foundations
作者: Teng Hu, Jiangning Zhang, Hongrui Huang, Ran Yi, Zihan Su, Jieyu Weng, Zhucun Xue, Lizhuang Ma, Ming-Hsuan Yang, Dacheng Tao
链接: https://arxiv.org/abs/2604.06339v1
完整摘要: The rapid advancement of Artificial Intelligence Generated Content (AIGC) has revolutionized video generation, enabling systems ranging from proprietary pioneers like OpenAI's Sora, Google's Veo3, and Bytedance's Seedance to powerful open-source contenders like Wan and HunyuanVideo to synthesize temporally coherent and semantically rich videos. These advancements pave the way for building "world models" that simulate real-world dynamics, with applications spanning entertainment, education, and virtual reality. However, existing reviews on video generation often focus on narrow technical fields, e.g., Generative Adversarial Networks (GAN) and diffusion models, or specific tasks (e. g., video editing), lacking a comprehensive perspective on the field's evolution, especially regarding Auto-Regressive (AR) models and integration of multimodal information. To address these gaps, this survey firstly provides a systematic review of the development of video generation technology, tracing its evolution from early GANs to dominant diffusion models, and further to emerging AR-based and multimodal techniques. We conduct an in-depth analysis of the foundational principles, key advancements, and comparative strengths/limitations. Then, we explore emerging trends in multimodal video generation, emphasizing the integration of diverse data types to enhance contextual awareness. Finally, by bridging historical developments and contemporary innovations, this survey offers insights to guide future research in video generation and its applications, including virtual/augmented reality, personalized education, autonomous driving simulations, digital entertainment, and advanced world models, in this rapidly evolving field. For more details, please refer to the project at https://github.com/sjtuplayer/Awesome-Video-Foundations.
匹配关键词: Sora
---

[ACADEMIC - ARXIV]
标题: Generative AI for Video Trailer Synthesis: From Extractive Heuristics to Autoregressive Creativity
作者: Abhishek Dharmaratnakar, Srivaths Ranganathan, Debanshu Das, Anushree Sinha
链接: https://arxiv.org/abs/2604.04953v1
完整摘要: The domain of automatic video trailer generation is currently undergoing a profound paradigm shift, transitioning from heuristic-based extraction methods to deep generative synthesis. While early methodologies relied heavily on low-level feature engineering, visual saliency, and rule-based heuristics to select representative shots, recent advancements in Large Language Models (LLMs), Multimodal Large Language Models (MLLMs), and diffusion-based video synthesis have enabled systems that not only identify key moments but also construct coherent, emotionally resonant narratives. This survey provides a comprehensive technical review of this evolution, with a specific focus on generative techniques including autoregressive Transformers, LLM-orchestrated pipelines, and text-to-video foundation models like OpenAI's Sora and Google's Veo. We analyze the architectural progression from Graph Convolutional Networks (GCNs) to Trailer Generation Transformers (TGT), evaluate the economic implications of automated content velocity on User-Generated Content (UGC) platforms, and discuss the ethical challenges posed by high-fidelity neural synthesis. By synthesizing insights from recent literature, this report establishes a new taxonomy for AI-driven trailer generation in the era of foundation models, suggesting that future promotional video systems will move beyond extractive selection toward controllable generative editing and semantic reconstruction of trailers.
匹配关键词: Sora
---

[ACADEMIC - ARXIV]
标题: Are Sparse Autoencoder Benchmarks Reliable?
作者: David Chanin
链接: https://arxiv.org/abs/2605.18229v1
完整摘要: Sparse autoencoders (SAEs) are a core interpretability tool for large language models, and progress on SAE architectures depends on benchmarks that reliably distinguish better SAEs from worse ones. We audit the SAE quality metrics in SAEBench, the de-facto standard SAE evaluation suite, through three complementary lenses: reseed noise on a fixed SAE, ground-truth correlation on synthetic SAEs, and discriminability across training trajectories. We find that two of these metrics, Targeted Probe Perturbation (TPP) and Spurious Correlation Removal (SCR), fail multiple lenses at their canonical settings and should not be used to evaluate SAEs. The other metrics show higher reseed noise and lower discriminability than the field assumes. The sae-probes variant of $k$-sparse probing is the most reliable metric we tested, but even sae-probes struggles to separate variants of the same SAE architecture. Our results show the field needs better SAE benchmarks.
匹配关键词: video foundation model
---

[ACADEMIC - ARXIV]
标题: Context Memorization for Efficient Long Context Generation
作者: Yasuyuki Okoshi, Hao Mark Chen, Guanxi Lu, Hongxiang Fan, Masato Motomura, Daichi Fujiki
链接: https://arxiv.org/abs/2605.18226v1
完整摘要: Modern large language model (LLM) applications increasingly rely on long conditioning prefixes to control model behavior at inference time. While prefix-augmented inference is effective, it incurs two structural limitations: i) the prefix's influence fades as generation proceeds, and ii) attention computation over the prefix scales linearly with its length. Existing approaches either keep the prefix in attention while compressing it, or internalize it into model parameters through gradient-based training. The former still attends to the prefix at inference, while the latter is training-intensive and ill-suited to prefix updates. To address these issues, we propose attention-state memory, a training-free approach that externalizes the prefix into a lightweight, lookup-based memory of precomputed attention states between prefix and query tokens. On ManyICLBench with LLaMA-3.1-8B, our method improves accuracy over in-context learning at 1K-8K memory budgets while reducing attention latency by 1.36x at 8K, and surpasses full-attention RAG performance on NBA benchmark using only 20% of its memory footprint.
匹配关键词: video foundation model
---

[ACADEMIC - ARXIV]
标题: Contextual Biasing for Streaming ASR via CTC-based Word Spotting
作者: Kai-Chen Tsai, Tien-Hong Lo, Yun-Ting Sun, Berlin Chen
链接: https://arxiv.org/abs/2605.18222v1
完整摘要: Contextual biasing is essential to improving the recognition of rare and domain-specific words in an automatic speech recognition (ASR) system. While numerous methods have been proposed in recent years, most of them focus on offline settings and do not explicitly address the challenges of streaming ASR. For example, CTC-based word spotting (CTC-WS) have demonstrated strong performance by directly detecting keywords from CTC log-probabilities, but they are limited to offline processing and require access to the full utterance. In This work, we present a streaming extension of CTC-WS for real-time contextual biasing. Our method maintains active keyword paths across audio chunks using a stateful token passing algorithm, enabling the detection of keywords that span multiple chunks. To ensure low latency and stable output, we introduce an incremental commitment mechanism that only emits segments guaranteed not to be affected by future audio, while deferring uncertain regions. This method naturally integrates with streaming ASR pipelines and does not require modifications to the underlying acoustic model or additional training, making it practical for real-world deployment. Experimental results show that our method reduces overall WER and effectively improves keyword F-score, demonstrating its effectiveness for real-time ASR applications.
匹配关键词: video foundation model
---

[ACADEMIC - ARXIV]
标题: SIREM: Speech-Informed MRI Reconstruction with Learned Sampling
作者: Md Hasan, Nyvenn Castro, Daiqi Liu, Lukas Mulzer, Jana Hutter, Jonghye Woo, Moritz Zaiss, Andreas Maier, Paula A. Perez-Toro
链接: https://arxiv.org/abs/2605.18221v1
完整摘要: Real-time magnetic resonance imaging (rtMRI) of speech production enables non-invasive visualization of dynamic vocal-tract motion and is valuable for speech science and clinical assessment. However, rtMRI is fundamentally constrained by trade-offs among spatial resolution, temporal resolution, and acquisition speed, often leading to undersampled k-space measurements and degraded reconstructions. We propose SIREM, a speech-informed MRI reconstruction framework that uses synchronized speech as a cross-modal prior. The central idea is that vocal-tract configurations during speech are correlated with the produced acoustics, making part of the image content predictable from audio. SIREM models each frame as a fusion of an audio-driven component and an MRI-driven component through a spatial weighting map. The audio branch predicts articulator-related structure from speech, while the MRI branch reconstructs complementary content from measured k-space data. We further introduce a learnable soft weighting profile over spiral arms, enabling a differentiable study of how k-space arm usage interacts with speech-informed fusion. This yields a unified multimodal formulation that combines audio-driven prediction, MRI reconstruction, and sampling adaptation. We evaluate SIREM on the USC speech rtMRI benchmark against standard baselines, including gridding, wavelet-based compressed sensing, and total variation. SIREM introduces a speech-informed reconstruction paradigm that operates in a substantially higher-throughput regime than iterative methods while preserving anatomically plausible vocal-tract structure. These results establish an initial benchmark for multimodal speech-informed rtMRI reconstruction and highlight the potential of synchronized speech as an auxiliary prior for fast reconstruction. The source code is available at https://github.com/mdhasanai/SIREM
匹配关键词: video foundation model
---

[ACADEMIC - ARXIV]
标题: EgoInteract: Synthetic Egocentric Videos Generation for Interaction Understanding and Anticipation
作者: Rosario Leonardi, Francesco Ragusa, Daniele Materia, Alessandro Passanisi, James Fort, Jakob Engel, Giovanni Maria Farinella
链接: https://arxiv.org/abs/2605.18214v1
完整摘要: Collecting large-scale egocentric video datasets with dense spatial and temporal annotations is costly, slow, and often constrained by environmental biases, privacy constraints, and limited coverage of interaction patterns. While synthetic data has shown strong potential in several vision domains, its use for egocentric perception remains relatively underexplored, especially for tasks requiring temporally coherent human-object interactions. In this work, we introduce EgoInteract, a controllable simulator for egocentric video generation designed to model fine-grained egocentric interactions and their temporal dynamics. The simulator enables precise control over camera, human body and hand motion, object manipulation, and scene composition across diverse environments. Building on this framework, we generate a synthetic egocentric video dataset with dense spatial and temporal annotations for temporal action segmentation, next-active object detection, interaction anticipation, and hand-object interaction detection. We evaluate models trained with simulated data on multiple real-world egocentric benchmarks spanning diverse environments, object categories, and interaction patterns. Results show consistent improvements over strong baselines across tasks and datasets, demonstrating the effectiveness and transferability of our simulation-based approach.
匹配关键词: video foundation model
---

[ACADEMIC - ARXIV]
标题: Context Memorization for Efficient Long Context Generation
作者: Yasuyuki Okoshi, Hao Mark Chen, Guanxi Lu, Hongxiang Fan, Masato Motomura, Daichi Fujiki
链接: https://arxiv.org/abs/2605.18226v1
完整摘要: Modern large language model (LLM) applications increasingly rely on long conditioning prefixes to control model behavior at inference time. While prefix-augmented inference is effective, it incurs two structural limitations: i) the prefix's influence fades as generation proceeds, and ii) attention computation over the prefix scales linearly with its length. Existing approaches either keep the prefix in attention while compressing it, or internalize it into model parameters through gradient-based training. The former still attends to the prefix at inference, while the latter is training-intensive and ill-suited to prefix updates. To address these issues, we propose attention-state memory, a training-free approach that externalizes the prefix into a lightweight, lookup-based memory of precomputed attention states between prefix and query tokens. On ManyICLBench with LLaMA-3.1-8B, our method improves accuracy over in-context learning at 1K-8K memory budgets while reducing attention latency by 1.36x at 8K, and surpasses full-attention RAG performance on NBA benchmark using only 20% of its memory footprint.
匹配关键词: video LLM
---

[ACADEMIC - ARXIV]
标题: EgoInteract: Synthetic Egocentric Videos Generation for Interaction Understanding and Anticipation
作者: Rosario Leonardi, Francesco Ragusa, Daniele Materia, Alessandro Passanisi, James Fort, Jakob Engel, Giovanni Maria Farinella
链接: https://arxiv.org/abs/2605.18214v1
完整摘要: Collecting large-scale egocentric video datasets with dense spatial and temporal annotations is costly, slow, and often constrained by environmental biases, privacy constraints, and limited coverage of interaction patterns. While synthetic data has shown strong potential in several vision domains, its use for egocentric perception remains relatively underexplored, especially for tasks requiring temporally coherent human-object interactions. In this work, we introduce EgoInteract, a controllable simulator for egocentric video generation designed to model fine-grained egocentric interactions and their temporal dynamics. The simulator enables precise control over camera, human body and hand motion, object manipulation, and scene composition across diverse environments. Building on this framework, we generate a synthetic egocentric video dataset with dense spatial and temporal annotations for temporal action segmentation, next-active object detection, interaction anticipation, and hand-object interaction detection. We evaluate models trained with simulated data on multiple real-world egocentric benchmarks spanning diverse environments, object categories, and interaction patterns. Results show consistent improvements over strong baselines across tasks and datasets, demonstrating the effectiveness and transferability of our simulation-based approach.
匹配关键词: video LLM
---

[ACADEMIC - ARXIV]
标题: Leveraging Graph Structure in Seq2Seq Models for Knowledge Graph Link Prediction
作者: Luu Huu Phuc, Ratan Bahadur Thapa, Mojtaba Nayyeri, Jingcheng Wu, Evgeny Kharlamov, Steffen Staab
链接: https://arxiv.org/abs/2605.18211v1
完整摘要: We introduce Graph-Augmented Sequence-to-Sequence (GA-S2S), a novel framework that integrates a T5-small encoder-decoder with a Relational Graph Attention Network (RGAT) to improve link prediction in knowledge graphs. While existing Seq2Seq models rely solely on surface-level textual descriptions of entities and relations and at best, flatten the neighborhoods of a query entity into a single linear sequence, thereby discarding the inherent graph structure, GA-S2S jointly encodes both textual features and the full $k$-hop subgraph topology surrounding the query entity. By integrating raw encoder outputs with RGAT's relation-aware embeddings, our model captures and leverages richer multi-hop relational patterns and textual information. Our preliminary experiments on the CoDEx dataset demonstrate that GA-S2S outperforms competitive Seq2Seq-based baseline models, achieving up to a 19\% relative gain in link prediction accuracy.
匹配关键词: video LLM
---

[ACADEMIC - ARXIV]
标题: SPATIOROUTE: Dynamic Prompt Routing for Zero-Shot Spatial Reasoning
作者: Pawat Chunhachatrachai, Gueter Josmy Faure, Hung-Ting Su, Winston H. Hsu
链接: https://arxiv.org/abs/2605.18209v1
完整摘要: Spatial question answering over egocentric video is a challenging task that requires Vision-Language Models (VLMs) to reason about 3D object positions, scene affordances, and directional relationships, particularly in the zero-shot setting where no task-specific fine-tuning is available. We introduce SpatioRoute, a dynamic prompt generation approach that routes each incoming question to a semantically tailored prompt template -- without any additional training, fine-tuning, or 3D sensor input. SpatioRoute operates in two complementary modes: SpatioRoute-R, a rule-based router that deterministically maps question typologies (e.g., What, Is, How, Can, Which) to specialized prompt templates; and SpatioRoute-L, an LLM-driven approach that generates task-specific prompts from the question and situational context alone, with no video input at routing time. We evaluate SpatioRoute on the SQA3D benchmark across VLMs spanning model families. SpatioRoute achieves consistent overall accuracy gains up to 5% over fixed prompt baselines, establishing a new state-of-the-art for zero-shot video-only spatial VQA without requiring 3D point-cloud inputs. As an additional finding, we observe that Chain-of-Thought (CoT) prompting, implemented via the Think it Twice architecture, consistently degrades performance in this setting on Qwen series models, confirming that question-aware routing is more effective than uniform reasoning instructions for spatial video understanding.
匹配关键词: video LLM
---

[ACADEMIC - ARXIV]
标题: PIPER: Content-Based Table Search via profiling and LLM-Generated Pseudoqueries
作者: Riccardo Terrenzi, Matteo Falconi, Serkan Ayvaz, Pierluigi Plebani
链接: https://arxiv.org/abs/2605.18199v1
完整摘要: The rapid growth of tabular datasets in data lakes, data spaces, and open data portals makes effective dataset search essential for reuse and analysis. Existing search systems rely mainly on metadata, which is often incomplete or low quality, especially for tables whose meaning depends on both schema and cell values. Recent advances in Large Language Models (LLMs) enable richer, content-based representations of tables. However, prior LLM-based retrieval methods have focused on Table Question Answering, where the goal is to select a single table to answer a question, rather than retrieve and rank relevant datasets. We propose PIPER, a content-driven retrieval method for tabular datasets that uses table profiles and LLM-generated queries embedded for dense retrieval. Designed for dataset search in poor-metadata settings, PIPER outperforms both classical metadata-based baselines and strong TableQA retrieval methods, demonstrating the value of LLM-based content modeling for tabular dataset search.
匹配关键词: video LLM
---

[ACADEMIC - ARXIV]
标题: Beyond the Cartesian Illusion: Testing Two-Stage Multi-Modal Theory of Mind under Perceptual Bottlenecks
作者: Yajing Zhou, Xiangyu Kong
链接: https://arxiv.org/abs/2605.18194v1
完整摘要: While Multi-Modal Large Language Models (MLLMs) demonstrate impressive capabilities in general reasoning, their embodied spatial intelligence remains hampered by a "Cartesian Illusion" - a reliance on text-based probability distributions that lack grounded, 3D topological understanding. This limitation is starkly exposed in multi-agent environments, which demand more than just scene perception; they require second-order Theory of Mind (ToM). Specifically, an Agent A must be able to infer Agent B's belief about the environment, governed strictly by Agent B's physical orientation and sensory limitations. In this paper, we probe the limits of two-stage spatial inference in MLLMs through a novel audio-visual task: requiring Agent A to predict Agent B's estimation of A's relative location. To solve this, we propose an Epistemic Sensory Bottleneck module that abandons rigid, rule-based coordinate transformations. Instead, we introduce an Anchor-Based Embodied Spatial Decomposition Chain-of-Thought (CoT). This guides the MLLM through a "geometric-to-semantic" projection, forcing it to first establish B's local coordinate system and then dynamically weight visual and auditory modalities based on whether A falls within B's visual frustum. Extensive evaluations reveal that while current MLLMs fundamentally struggle with spatial symmetry and out-of-view ambiguities (establishing a rigorous zero-shot baseline of 42% accuracy), our sensory-bounded reasoning chain robustly outperforms pure egocentric and allocentric baselines. By systematically benchmarking these perceptual bottlenecks, our work exposes the current limits of MLLM spatial reasoning and establishes a foundational paradigm for epistemic, modality-aware inference in Embodied AI.
匹配关键词: multi-agent
---

[ACADEMIC - ARXIV]
标题: Whispers in the Noise: Surrogate-Guided Concept Awakening via a Multi-Agent Framework
作者: Mengyu Sun, Ziyuan Yang, Zunlong Zhou, Junxu Liu, Haibo Hu, Yi Zhang
链接: https://arxiv.org/abs/2605.18150v1
完整摘要: Diffusion models (DMs) are widely used for text-to-image generation, but their strong generative capabilities also raise concerns about unsafe or undesirable content. Concept erasure aims to mitigate these risks by removing specific concepts from pretrained models. However, recent studies show that such methods often suppress rather than fully eliminate target concepts, leaving models vulnerable to awakening attacks. Existing approaches primarily rely on white-box access through optimization or inversion, while concept awakening under black-box constraints remains underexplored. In this work, we revisit the denoising process from a trajectory perspective and show that concept erasure mainly disrupts early-stage text-semantic alignment but does not fully prevent semantic information from propagating along the denoising dynamics. As generation proceeds, the model increasingly depends on the evolving noisy state rather than textual conditions, which creates an opportunity to bypass erased mappings. Motivated by this observation, we propose ConceptAgent, a training-free, black-box, multi-agent framework that awakens erased concepts by initializing the denoising trajectory from surrogate-guided noisy states. Extensive experiments demonstrate that ConceptAgent enables accurate and controllable awakening of erased concepts under black-box settings without access to model parameters, gradients, or internal representations. These results highlight fundamental limitations of current concept erasure methods and provide new insights into the dynamic nature of semantic control in DMs.
匹配关键词: multi-agent
---

[ACADEMIC - ARXIV]
标题: Equilibrium Selection in Multi-Agent Policy Gradients via Opponent-Aware Basin Entry
作者: Yevhen Shcherbinin, Arina Redina, Maxim Kalpin, Vlad Kochetov
链接: https://arxiv.org/abs/2605.18078v1
完整摘要: Multi-agent policy-gradient methods have been shown to converge locally near stable Nash equilibria. Local convergence, however, does not determine which equilibrium is reached. We study this question through basin-entry probability with respect to a target set of equilibria selected by an external criterion, such as payoff dominance. For finite-unroll Meta-MAPG, we show that the update decomposes into ordinary policy gradient plus own-learning and peer-learning corrections, with controlled sampling noise and finite-unroll bias. We identify the peer-learning correction as the main equilibrium-selection mechanism: under a local alignment condition, the probability of entering the certified attraction region of the target stable-Nash set increases, relative to ordinary policy gradient. Because persistent correction may shift zero-update points of the original game, annealing the correction after entering the basin recovers ordinary policy-gradient dynamics and inherits local stable-Nash convergence guarantees. Experiments in Stag Hunt, iterated Prisoner's Dilemma, and preliminary neural-policy coordination environments support this basin-entry view, showing increased entry into cooperative basins under peer-aware updates.
匹配关键词: multi-agent
---

[ACADEMIC - ARXIV]
标题: LLM-Guided Communication for Cooperative Multi-Agent Reinforcement Learning
作者: Sangjun Bae, Yisak Park, Sanghyeon Lee, Seungyul Han
链接: https://arxiv.org/abs/2605.18077v1
完整摘要: Communication is a key component in multi-agent reinforcement learning (MARL) for mitigating partial observability, yet prior approaches often rely on inefficient information exchange or fail to transmit sufficient state information. To address this, we propose LLM-driven Multi-Agent Communication (LMAC), which leverages an LLM's reasoning capability to design a communication protocol that enables all agents to reconstruct the underlying state as accurately and uniformly as possible. LMAC iteratively refines the protocol using an explicit state-awareness criterion, improving state recovery while narrowing differences in agents' knowledge. Experiments on diverse MARL benchmarks show that LMAC improves state reconstruction across agents and yields substantial performance gains over prior communication baselines.
匹配关键词: multi-agent
---

[ACADEMIC - ARXIV]
标题: A-ProS: Towards Reliable Autonomous Programming Through Multi-Model Feedback
作者: Anika Tabassum, Md Sifat Hossain, Md. Fahim Arefin, Tariqul Islam, Tarannum Shaila Zaman
链接: https://arxiv.org/abs/2605.18073v1
完整摘要: Large Language Models (LLMs) demonstrate strong potential for automated code generation, yet their ability to iteratively refine solutions using execution feedback remains underexplored. Competitive programming offers an ideal testbed for this investigation, as it demands end-to-end algorithmic reasoning, precise implementation under strict computational constraints, and complete functional correctness with rigorous evaluation. In this paper, we present A-ProS, an autonomous AI agent that solves competitive programming problems through a hybrid multi-model feedback framework separating solution generation from specialized debugging. A-ProS combines ChatGPT-based generators (GPT-4 and GPT-5) with three debugging critics: Codestral-2508, Llama-3.3-70B, and DeepSeek-R1, under a 2 x 3 factorial design. We evaluate six workflows on 367 problems from ICPC World Finals (2011-2024) and Codeforces (rated 1200-1800). The results show that GPT-5 workflows improve from 39 initial accepted solutions to 85-90 after three refinement rounds, while GPT-4 improves from 15 to 31-38. A controlled ablation on 47 problems shows that stateful refinement outperforms stateless approaches by 8.5-10.6 percentage points and reduces repeated failures by up to 3.5x. Compared to baseline agent loops, A-ProS achieves over 2x greater gains, highlighting the importance of persistent context and multi-model feedback for reliable autonomous program synthesis.
匹配关键词: multi-agent
---

[ACADEMIC - ARXIV]
标题: Beyond the Cartesian Illusion: Testing Two-Stage Multi-Modal Theory of Mind under Perceptual Bottlenecks
作者: Yajing Zhou, Xiangyu Kong
链接: https://arxiv.org/abs/2605.18194v1
完整摘要: While Multi-Modal Large Language Models (MLLMs) demonstrate impressive capabilities in general reasoning, their embodied spatial intelligence remains hampered by a "Cartesian Illusion" - a reliance on text-based probability distributions that lack grounded, 3D topological understanding. This limitation is starkly exposed in multi-agent environments, which demand more than just scene perception; they require second-order Theory of Mind (ToM). Specifically, an Agent A must be able to infer Agent B's belief about the environment, governed strictly by Agent B's physical orientation and sensory limitations. In this paper, we probe the limits of two-stage spatial inference in MLLMs through a novel audio-visual task: requiring Agent A to predict Agent B's estimation of A's relative location. To solve this, we propose an Epistemic Sensory Bottleneck module that abandons rigid, rule-based coordinate transformations. Instead, we introduce an Anchor-Based Embodied Spatial Decomposition Chain-of-Thought (CoT). This guides the MLLM through a "geometric-to-semantic" projection, forcing it to first establish B's local coordinate system and then dynamically weight visual and auditory modalities based on whether A falls within B's visual frustum. Extensive evaluations reveal that while current MLLMs fundamentally struggle with spatial symmetry and out-of-view ambiguities (establishing a rigorous zero-shot baseline of 42% accuracy), our sensory-bounded reasoning chain robustly outperforms pure egocentric and allocentric baselines. By systematically benchmarking these perceptual bottlenecks, our work exposes the current limits of MLLM spatial reasoning and establishes a foundational paradigm for epistemic, modality-aware inference in Embodied AI.
匹配关键词: agent collaboration
---

[ACADEMIC - ARXIV]
标题: Scalable Environments Drive Generalizable Agents
作者: Jiayi Zhang, Fanqi Kong, Guibin Zhang, Maojia Song, Zhaoyang Yu, Jianhao Ruan, Jinyu Xiang, Bang Liu, Chenglin Wu, Yuyu Luo
链接: https://arxiv.org/abs/2605.18181v1
完整摘要: Generalizable agents should adapt to diverse tasks and unseen environments beyond their training distribution. This position paper argues that such generalization requires environment scaling: expanding the distribution of executable rule-sets that agents interact with, rather than only increasing trajectories or tasks within fixed benchmarks. Current scaling practices largely focus on collecting more experience or broader task sets under fixed interaction rules, leaving agents brittle when underlying interfaces, dynamics, observations, or feedback signals change. The core challenge is therefore a world-level distribution shift: agents need systematic exposure to environments with meaningfully different executable rule-sets. To clarify this challenge, we propose a unified taxonomy that separates trajectory scaling, task scaling, and environment scaling by their primary deliverables and by what changes in the executable rule-set. Building on this taxonomy, we synthesize construction paradigms for scalable environments, contrasting programmatic generators that prioritize controllability and verifiability with generative world models that offer broader coverage and open-endedness. We further outline how environment scaling can be coupled with stateful learning mechanisms, emphasizing learned update rules for cross-environment adaptation. We conclude by discussing alternative perspectives and argue that scalable environments provide the essential substrate for measurable and controllable progress toward robust general agents.
匹配关键词: agent collaboration
---

[ACADEMIC - ARXIV]
标题: MARS: Technical Report for the CASTLE Challenge at EgoVis 2026
作者: Haoyu Zhang, Qiaohui Chu, Yisen Feng, Meng Liu, Weili Guan, Yaowei Wang, Liqiang Nie
链接: https://arxiv.org/abs/2605.18176v1
完整摘要: This report presents MARS, short for Multimodal Agentic Reasoning with Source selection, our system for the CASTLE Challenge at EgoVis 2026. Participants must answer 185 closed-form questions over the CASTLE 2024 dataset. In contrast to prior single-video egocentric benchmarks, CASTLE requires reasoning over four days of activity, 15 synchronized perspectives, official transcripts, and multiple auxiliary modalities, including personal photos, auxiliary videos, gaze, thermal imagery, and heartrate measurements. MARS therefore treats the task as an agentic evidence-selection problem over multimodal sources rather than a purely text-only pipeline. MARS first follows the official CASTLE directory organization to build evidence memories from two primary sources, videos and transcripts, and four auxiliary sources, gaze, heartrate, photos, and thermal imagery. Long videos are converted into captions and DeepSeek-based summaries only because CASTLE videos are too long to fit directly into the model context for every question; this step compresses temporal evidence while keeping photos and other auxiliary media available as source-specific evidence. At inference time, a GPT-5.4 decision agent repeatedly chooses whether to continue reasoning, request a specific missing modality, produce an answer, or fall back to a random option when the evidence remains insufficient. The resulting system achieved second place on the final CASTLE Challenge leaderboard. Our codes are available at https://github.com/Hyu-Zhang/MARS.
匹配关键词: agent collaboration
---

[ACADEMIC - ARXIV]
标题: Whispers in the Noise: Surrogate-Guided Concept Awakening via a Multi-Agent Framework
作者: Mengyu Sun, Ziyuan Yang, Zunlong Zhou, Junxu Liu, Haibo Hu, Yi Zhang
链接: https://arxiv.org/abs/2605.18150v1
完整摘要: Diffusion models (DMs) are widely used for text-to-image generation, but their strong generative capabilities also raise concerns about unsafe or undesirable content. Concept erasure aims to mitigate these risks by removing specific concepts from pretrained models. However, recent studies show that such methods often suppress rather than fully eliminate target concepts, leaving models vulnerable to awakening attacks. Existing approaches primarily rely on white-box access through optimization or inversion, while concept awakening under black-box constraints remains underexplored. In this work, we revisit the denoising process from a trajectory perspective and show that concept erasure mainly disrupts early-stage text-semantic alignment but does not fully prevent semantic information from propagating along the denoising dynamics. As generation proceeds, the model increasingly depends on the evolving noisy state rather than textual conditions, which creates an opportunity to bypass erased mappings. Motivated by this observation, we propose ConceptAgent, a training-free, black-box, multi-agent framework that awakens erased concepts by initializing the denoising trajectory from surrogate-guided noisy states. Extensive experiments demonstrate that ConceptAgent enables accurate and controllable awakening of erased concepts under black-box settings without access to model parameters, gradients, or internal representations. These results highlight fundamental limitations of current concept erasure methods and provide new insights into the dynamic nature of semantic control in DMs.
匹配关键词: agent collaboration
---

[ACADEMIC - ARXIV]
标题: Evidence-Grounded Frontier Mapping and Agentic Hypothesis Generation in Nanomedicine
作者: Christiaan G. A. Viviers, Koen de Bruin, Mirre M. Trines, Ayla M. Hokke, Roy van der Meel, Avi Schroeder, Twan Lammers, Willem J. M. Mulder, Fons van der Sommen
链接: https://arxiv.org/abs/2605.18144v1
完整摘要: Nanomedicine research spans delivery chemistry, immunology, imaging, biomaterials, and disease-specific translational science, yet its conceptual design space remains fragmented across a large and heterogeneous literature. To date, artificial intelligence in nanomedicine has focused primarily on property prediction and formulation optimization, with much less attention to evidence-grounded discovery support at the level of research direction selection. We introduce pArticleMap, a literature-mapping and research-hypothesis-generation system that combines article embeddings, similarity-graph analysis, sparse frontier extraction, structured evidence-pack retrieval, and an audited large-language-model (LLM) workflow for grounded ideation. Rather than forecasting future concept co-occurrence, pArticleMap targets low-density article-level bridge regions and cluster interfaces, then generates and scores citation-grounded hypotheses with large language models in an agentic setup. We evaluate the system with a retrospective realization benchmark (generate later literature under a historical cutoff) and a blinded human reader assessment layer across cue-conditioned nanomedicine tasks. Across 4 selected retrospective bundles, pArticleMap generated ideas and selected task-retained hypotheses (winner ideas) under the benchmark protocol. For task-level retained hypotheses, a pooled gold recovery rate of 10.8% was obtained, with a recall@10 of 15.9% and a future-neighborhood rate of 61.0%, indicating that the system often reached the correct forward-looking neighborhood (paper ideas) even without exact paper-level recovery. Human-agent agreement is modest overall, indicating that internal scoring is useful as a support signal but does not replace expert judgment. These results position pArticleMap as a conservative, evidence-grounded research assistant for nanomedicine.
匹配关键词: agent collaboration
---

[ACADEMIC - ARXIV]
标题: Beyond the Cartesian Illusion: Testing Two-Stage Multi-Modal Theory of Mind under Perceptual Bottlenecks
作者: Yajing Zhou, Xiangyu Kong
链接: https://arxiv.org/abs/2605.18194v1
完整摘要: While Multi-Modal Large Language Models (MLLMs) demonstrate impressive capabilities in general reasoning, their embodied spatial intelligence remains hampered by a "Cartesian Illusion" - a reliance on text-based probability distributions that lack grounded, 3D topological understanding. This limitation is starkly exposed in multi-agent environments, which demand more than just scene perception; they require second-order Theory of Mind (ToM). Specifically, an Agent A must be able to infer Agent B's belief about the environment, governed strictly by Agent B's physical orientation and sensory limitations. In this paper, we probe the limits of two-stage spatial inference in MLLMs through a novel audio-visual task: requiring Agent A to predict Agent B's estimation of A's relative location. To solve this, we propose an Epistemic Sensory Bottleneck module that abandons rigid, rule-based coordinate transformations. Instead, we introduce an Anchor-Based Embodied Spatial Decomposition Chain-of-Thought (CoT). This guides the MLLM through a "geometric-to-semantic" projection, forcing it to first establish B's local coordinate system and then dynamically weight visual and auditory modalities based on whether A falls within B's visual frustum. Extensive evaluations reveal that while current MLLMs fundamentally struggle with spatial symmetry and out-of-view ambiguities (establishing a rigorous zero-shot baseline of 42% accuracy), our sensory-bounded reasoning chain robustly outperforms pure egocentric and allocentric baselines. By systematically benchmarking these perceptual bottlenecks, our work exposes the current limits of MLLM spatial reasoning and establishes a foundational paradigm for epistemic, modality-aware inference in Embodied AI.
匹配关键词: agent coordination
---

[ACADEMIC - ARXIV]
标题: Scalable Environments Drive Generalizable Agents
作者: Jiayi Zhang, Fanqi Kong, Guibin Zhang, Maojia Song, Zhaoyang Yu, Jianhao Ruan, Jinyu Xiang, Bang Liu, Chenglin Wu, Yuyu Luo
链接: https://arxiv.org/abs/2605.18181v1
完整摘要: Generalizable agents should adapt to diverse tasks and unseen environments beyond their training distribution. This position paper argues that such generalization requires environment scaling: expanding the distribution of executable rule-sets that agents interact with, rather than only increasing trajectories or tasks within fixed benchmarks. Current scaling practices largely focus on collecting more experience or broader task sets under fixed interaction rules, leaving agents brittle when underlying interfaces, dynamics, observations, or feedback signals change. The core challenge is therefore a world-level distribution shift: agents need systematic exposure to environments with meaningfully different executable rule-sets. To clarify this challenge, we propose a unified taxonomy that separates trajectory scaling, task scaling, and environment scaling by their primary deliverables and by what changes in the executable rule-set. Building on this taxonomy, we synthesize construction paradigms for scalable environments, contrasting programmatic generators that prioritize controllability and verifiability with generative world models that offer broader coverage and open-endedness. We further outline how environment scaling can be coupled with stateful learning mechanisms, emphasizing learned update rules for cross-environment adaptation. We conclude by discussing alternative perspectives and argue that scalable environments provide the essential substrate for measurable and controllable progress toward robust general agents.
匹配关键词: agent coordination
---

[ACADEMIC - ARXIV]
标题: MARS: Technical Report for the CASTLE Challenge at EgoVis 2026
作者: Haoyu Zhang, Qiaohui Chu, Yisen Feng, Meng Liu, Weili Guan, Yaowei Wang, Liqiang Nie
链接: https://arxiv.org/abs/2605.18176v1
完整摘要: This report presents MARS, short for Multimodal Agentic Reasoning with Source selection, our system for the CASTLE Challenge at EgoVis 2026. Participants must answer 185 closed-form questions over the CASTLE 2024 dataset. In contrast to prior single-video egocentric benchmarks, CASTLE requires reasoning over four days of activity, 15 synchronized perspectives, official transcripts, and multiple auxiliary modalities, including personal photos, auxiliary videos, gaze, thermal imagery, and heartrate measurements. MARS therefore treats the task as an agentic evidence-selection problem over multimodal sources rather than a purely text-only pipeline. MARS first follows the official CASTLE directory organization to build evidence memories from two primary sources, videos and transcripts, and four auxiliary sources, gaze, heartrate, photos, and thermal imagery. Long videos are converted into captions and DeepSeek-based summaries only because CASTLE videos are too long to fit directly into the model context for every question; this step compresses temporal evidence while keeping photos and other auxiliary media available as source-specific evidence. At inference time, a GPT-5.4 decision agent repeatedly chooses whether to continue reasoning, request a specific missing modality, produce an answer, or fall back to a random option when the evidence remains insufficient. The resulting system achieved second place on the final CASTLE Challenge leaderboard. Our codes are available at https://github.com/Hyu-Zhang/MARS.
匹配关键词: agent coordination
---

[ACADEMIC - ARXIV]
标题: Whispers in the Noise: Surrogate-Guided Concept Awakening via a Multi-Agent Framework
作者: Mengyu Sun, Ziyuan Yang, Zunlong Zhou, Junxu Liu, Haibo Hu, Yi Zhang
链接: https://arxiv.org/abs/2605.18150v1
完整摘要: Diffusion models (DMs) are widely used for text-to-image generation, but their strong generative capabilities also raise concerns about unsafe or undesirable content. Concept erasure aims to mitigate these risks by removing specific concepts from pretrained models. However, recent studies show that such methods often suppress rather than fully eliminate target concepts, leaving models vulnerable to awakening attacks. Existing approaches primarily rely on white-box access through optimization or inversion, while concept awakening under black-box constraints remains underexplored. In this work, we revisit the denoising process from a trajectory perspective and show that concept erasure mainly disrupts early-stage text-semantic alignment but does not fully prevent semantic information from propagating along the denoising dynamics. As generation proceeds, the model increasingly depends on the evolving noisy state rather than textual conditions, which creates an opportunity to bypass erased mappings. Motivated by this observation, we propose ConceptAgent, a training-free, black-box, multi-agent framework that awakens erased concepts by initializing the denoising trajectory from surrogate-guided noisy states. Extensive experiments demonstrate that ConceptAgent enables accurate and controllable awakening of erased concepts under black-box settings without access to model parameters, gradients, or internal representations. These results highlight fundamental limitations of current concept erasure methods and provide new insights into the dynamic nature of semantic control in DMs.
匹配关键词: agent coordination
---

[ACADEMIC - ARXIV]
标题: Evidence-Grounded Frontier Mapping and Agentic Hypothesis Generation in Nanomedicine
作者: Christiaan G. A. Viviers, Koen de Bruin, Mirre M. Trines, Ayla M. Hokke, Roy van der Meel, Avi Schroeder, Twan Lammers, Willem J. M. Mulder, Fons van der Sommen
链接: https://arxiv.org/abs/2605.18144v1
完整摘要: Nanomedicine research spans delivery chemistry, immunology, imaging, biomaterials, and disease-specific translational science, yet its conceptual design space remains fragmented across a large and heterogeneous literature. To date, artificial intelligence in nanomedicine has focused primarily on property prediction and formulation optimization, with much less attention to evidence-grounded discovery support at the level of research direction selection. We introduce pArticleMap, a literature-mapping and research-hypothesis-generation system that combines article embeddings, similarity-graph analysis, sparse frontier extraction, structured evidence-pack retrieval, and an audited large-language-model (LLM) workflow for grounded ideation. Rather than forecasting future concept co-occurrence, pArticleMap targets low-density article-level bridge regions and cluster interfaces, then generates and scores citation-grounded hypotheses with large language models in an agentic setup. We evaluate the system with a retrospective realization benchmark (generate later literature under a historical cutoff) and a blinded human reader assessment layer across cue-conditioned nanomedicine tasks. Across 4 selected retrospective bundles, pArticleMap generated ideas and selected task-retained hypotheses (winner ideas) under the benchmark protocol. For task-level retained hypotheses, a pooled gold recovery rate of 10.8% was obtained, with a recall@10 of 15.9% and a future-neighborhood rate of 61.0%, indicating that the system often reached the correct forward-looking neighborhood (paper ideas) even without exact paper-level recovery. Human-agent agreement is modest overall, indicating that internal scoring is useful as a support signal but does not replace expert judgment. These results position pArticleMap as a conservative, evidence-grounded research assistant for nanomedicine.
匹配关键词: agent coordination
---

[ACADEMIC - ARXIV]
标题: Beyond the Cartesian Illusion: Testing Two-Stage Multi-Modal Theory of Mind under Perceptual Bottlenecks
作者: Yajing Zhou, Xiangyu Kong
链接: https://arxiv.org/abs/2605.18194v1
完整摘要: While Multi-Modal Large Language Models (MLLMs) demonstrate impressive capabilities in general reasoning, their embodied spatial intelligence remains hampered by a "Cartesian Illusion" - a reliance on text-based probability distributions that lack grounded, 3D topological understanding. This limitation is starkly exposed in multi-agent environments, which demand more than just scene perception; they require second-order Theory of Mind (ToM). Specifically, an Agent A must be able to infer Agent B's belief about the environment, governed strictly by Agent B's physical orientation and sensory limitations. In this paper, we probe the limits of two-stage spatial inference in MLLMs through a novel audio-visual task: requiring Agent A to predict Agent B's estimation of A's relative location. To solve this, we propose an Epistemic Sensory Bottleneck module that abandons rigid, rule-based coordinate transformations. Instead, we introduce an Anchor-Based Embodied Spatial Decomposition Chain-of-Thought (CoT). This guides the MLLM through a "geometric-to-semantic" projection, forcing it to first establish B's local coordinate system and then dynamically weight visual and auditory modalities based on whether A falls within B's visual frustum. Extensive evaluations reveal that while current MLLMs fundamentally struggle with spatial symmetry and out-of-view ambiguities (establishing a rigorous zero-shot baseline of 42% accuracy), our sensory-bounded reasoning chain robustly outperforms pure egocentric and allocentric baselines. By systematically benchmarking these perceptual bottlenecks, our work exposes the current limits of MLLM spatial reasoning and establishes a foundational paradigm for epistemic, modality-aware inference in Embodied AI.
匹配关键词: decentralized agent
---

[ACADEMIC - ARXIV]
标题: Scalable Environments Drive Generalizable Agents
作者: Jiayi Zhang, Fanqi Kong, Guibin Zhang, Maojia Song, Zhaoyang Yu, Jianhao Ruan, Jinyu Xiang, Bang Liu, Chenglin Wu, Yuyu Luo
链接: https://arxiv.org/abs/2605.18181v1
完整摘要: Generalizable agents should adapt to diverse tasks and unseen environments beyond their training distribution. This position paper argues that such generalization requires environment scaling: expanding the distribution of executable rule-sets that agents interact with, rather than only increasing trajectories or tasks within fixed benchmarks. Current scaling practices largely focus on collecting more experience or broader task sets under fixed interaction rules, leaving agents brittle when underlying interfaces, dynamics, observations, or feedback signals change. The core challenge is therefore a world-level distribution shift: agents need systematic exposure to environments with meaningfully different executable rule-sets. To clarify this challenge, we propose a unified taxonomy that separates trajectory scaling, task scaling, and environment scaling by their primary deliverables and by what changes in the executable rule-set. Building on this taxonomy, we synthesize construction paradigms for scalable environments, contrasting programmatic generators that prioritize controllability and verifiability with generative world models that offer broader coverage and open-endedness. We further outline how environment scaling can be coupled with stateful learning mechanisms, emphasizing learned update rules for cross-environment adaptation. We conclude by discussing alternative perspectives and argue that scalable environments provide the essential substrate for measurable and controllable progress toward robust general agents.
匹配关键词: decentralized agent
---

[ACADEMIC - ARXIV]
标题: MARS: Technical Report for the CASTLE Challenge at EgoVis 2026
作者: Haoyu Zhang, Qiaohui Chu, Yisen Feng, Meng Liu, Weili Guan, Yaowei Wang, Liqiang Nie
链接: https://arxiv.org/abs/2605.18176v1
完整摘要: This report presents MARS, short for Multimodal Agentic Reasoning with Source selection, our system for the CASTLE Challenge at EgoVis 2026. Participants must answer 185 closed-form questions over the CASTLE 2024 dataset. In contrast to prior single-video egocentric benchmarks, CASTLE requires reasoning over four days of activity, 15 synchronized perspectives, official transcripts, and multiple auxiliary modalities, including personal photos, auxiliary videos, gaze, thermal imagery, and heartrate measurements. MARS therefore treats the task as an agentic evidence-selection problem over multimodal sources rather than a purely text-only pipeline. MARS first follows the official CASTLE directory organization to build evidence memories from two primary sources, videos and transcripts, and four auxiliary sources, gaze, heartrate, photos, and thermal imagery. Long videos are converted into captions and DeepSeek-based summaries only because CASTLE videos are too long to fit directly into the model context for every question; this step compresses temporal evidence while keeping photos and other auxiliary media available as source-specific evidence. At inference time, a GPT-5.4 decision agent repeatedly chooses whether to continue reasoning, request a specific missing modality, produce an answer, or fall back to a random option when the evidence remains insufficient. The resulting system achieved second place on the final CASTLE Challenge leaderboard. Our codes are available at https://github.com/Hyu-Zhang/MARS.
匹配关键词: decentralized agent
---

[ACADEMIC - ARXIV]
标题: Whispers in the Noise: Surrogate-Guided Concept Awakening via a Multi-Agent Framework
作者: Mengyu Sun, Ziyuan Yang, Zunlong Zhou, Junxu Liu, Haibo Hu, Yi Zhang
链接: https://arxiv.org/abs/2605.18150v1
完整摘要: Diffusion models (DMs) are widely used for text-to-image generation, but their strong generative capabilities also raise concerns about unsafe or undesirable content. Concept erasure aims to mitigate these risks by removing specific concepts from pretrained models. However, recent studies show that such methods often suppress rather than fully eliminate target concepts, leaving models vulnerable to awakening attacks. Existing approaches primarily rely on white-box access through optimization or inversion, while concept awakening under black-box constraints remains underexplored. In this work, we revisit the denoising process from a trajectory perspective and show that concept erasure mainly disrupts early-stage text-semantic alignment but does not fully prevent semantic information from propagating along the denoising dynamics. As generation proceeds, the model increasingly depends on the evolving noisy state rather than textual conditions, which creates an opportunity to bypass erased mappings. Motivated by this observation, we propose ConceptAgent, a training-free, black-box, multi-agent framework that awakens erased concepts by initializing the denoising trajectory from surrogate-guided noisy states. Extensive experiments demonstrate that ConceptAgent enables accurate and controllable awakening of erased concepts under black-box settings without access to model parameters, gradients, or internal representations. These results highlight fundamental limitations of current concept erasure methods and provide new insights into the dynamic nature of semantic control in DMs.
匹配关键词: decentralized agent
---

[ACADEMIC - ARXIV]
标题: Evidence-Grounded Frontier Mapping and Agentic Hypothesis Generation in Nanomedicine
作者: Christiaan G. A. Viviers, Koen de Bruin, Mirre M. Trines, Ayla M. Hokke, Roy van der Meel, Avi Schroeder, Twan Lammers, Willem J. M. Mulder, Fons van der Sommen
链接: https://arxiv.org/abs/2605.18144v1
完整摘要: Nanomedicine research spans delivery chemistry, immunology, imaging, biomaterials, and disease-specific translational science, yet its conceptual design space remains fragmented across a large and heterogeneous literature. To date, artificial intelligence in nanomedicine has focused primarily on property prediction and formulation optimization, with much less attention to evidence-grounded discovery support at the level of research direction selection. We introduce pArticleMap, a literature-mapping and research-hypothesis-generation system that combines article embeddings, similarity-graph analysis, sparse frontier extraction, structured evidence-pack retrieval, and an audited large-language-model (LLM) workflow for grounded ideation. Rather than forecasting future concept co-occurrence, pArticleMap targets low-density article-level bridge regions and cluster interfaces, then generates and scores citation-grounded hypotheses with large language models in an agentic setup. We evaluate the system with a retrospective realization benchmark (generate later literature under a historical cutoff) and a blinded human reader assessment layer across cue-conditioned nanomedicine tasks. Across 4 selected retrospective bundles, pArticleMap generated ideas and selected task-retained hypotheses (winner ideas) under the benchmark protocol. For task-level retained hypotheses, a pooled gold recovery rate of 10.8% was obtained, with a recall@10 of 15.9% and a future-neighborhood rate of 61.0%, indicating that the system often reached the correct forward-looking neighborhood (paper ideas) even without exact paper-level recovery. Human-agent agreement is modest overall, indicating that internal scoring is useful as a support signal but does not replace expert judgment. These results position pArticleMap as a conservative, evidence-grounded research assistant for nanomedicine.
匹配关键词: decentralized agent
---

[ACADEMIC - ARXIV]
标题: Are Sparse Autoencoder Benchmarks Reliable?
作者: David Chanin
链接: https://arxiv.org/abs/2605.18229v1
完整摘要: Sparse autoencoders (SAEs) are a core interpretability tool for large language models, and progress on SAE architectures depends on benchmarks that reliably distinguish better SAEs from worse ones. We audit the SAE quality metrics in SAEBench, the de-facto standard SAE evaluation suite, through three complementary lenses: reseed noise on a fixed SAE, ground-truth correlation on synthetic SAEs, and discriminability across training trajectories. We find that two of these metrics, Targeted Probe Perturbation (TPP) and Spurious Correlation Removal (SCR), fail multiple lenses at their canonical settings and should not be used to evaluate SAEs. The other metrics show higher reseed noise and lower discriminability than the field assumes. The sae-probes variant of $k$-sparse probing is the most reliable metric we tested, but even sae-probes struggles to separate variants of the same SAE architecture. Our results show the field needs better SAE benchmarks.
匹配关键词: swarm intelligence
---

[ACADEMIC - ARXIV]
标题: Context Memorization for Efficient Long Context Generation
作者: Yasuyuki Okoshi, Hao Mark Chen, Guanxi Lu, Hongxiang Fan, Masato Motomura, Daichi Fujiki
链接: https://arxiv.org/abs/2605.18226v1
完整摘要: Modern large language model (LLM) applications increasingly rely on long conditioning prefixes to control model behavior at inference time. While prefix-augmented inference is effective, it incurs two structural limitations: i) the prefix's influence fades as generation proceeds, and ii) attention computation over the prefix scales linearly with its length. Existing approaches either keep the prefix in attention while compressing it, or internalize it into model parameters through gradient-based training. The former still attends to the prefix at inference, while the latter is training-intensive and ill-suited to prefix updates. To address these issues, we propose attention-state memory, a training-free approach that externalizes the prefix into a lightweight, lookup-based memory of precomputed attention states between prefix and query tokens. On ManyICLBench with LLaMA-3.1-8B, our method improves accuracy over in-context learning at 1K-8K memory budgets while reducing attention latency by 1.36x at 8K, and surpasses full-attention RAG performance on NBA benchmark using only 20% of its memory footprint.
匹配关键词: swarm intelligence
---

[ACADEMIC - ARXIV]
标题: A Simplex Witness Certificate for Constant Collapse in Variational Autoencoders
作者: Zegu Zhang, Jianhua Peng, Jian Zhang
链接: https://arxiv.org/abs/2605.18224v1
完整摘要: This note studies exact constant collapse in variational autoencoders, where the encoder mean becomes independent of the input. The goal is to make this specific failure mode pre-designable, monitorable during training, and certifiable after training. The prior is kept as the standard Gaussian. Given a fixed teacher posterior, we attach to the latent mean a fixed simplex witness head. The resulting teacher-student alignment loss has an exact constant-predictor baseline equal to the teacher information. If the alignment loss is below this baseline, the latent mean cannot be input-independent constant collapsed. The simplex witness also has a closed-form inverse. Any full-support teacher posterior can be represented by embedding its centered log-odds into the latent space. This gives an explicit latent energy cost and explains when the alignment loss can be made small. A computable view gap handles the case where teacher targets are computed from a different view. Thus exact constant collapse is converted from an after-the-fact training pathology into a design-and-certificate problem.
匹配关键词: swarm intelligence
---

[ACADEMIC - ARXIV]
标题: Leveraging Graph Structure in Seq2Seq Models for Knowledge Graph Link Prediction
作者: Luu Huu Phuc, Ratan Bahadur Thapa, Mojtaba Nayyeri, Jingcheng Wu, Evgeny Kharlamov, Steffen Staab
链接: https://arxiv.org/abs/2605.18211v1
完整摘要: We introduce Graph-Augmented Sequence-to-Sequence (GA-S2S), a novel framework that integrates a T5-small encoder-decoder with a Relational Graph Attention Network (RGAT) to improve link prediction in knowledge graphs. While existing Seq2Seq models rely solely on surface-level textual descriptions of entities and relations and at best, flatten the neighborhoods of a query entity into a single linear sequence, thereby discarding the inherent graph structure, GA-S2S jointly encodes both textual features and the full $k$-hop subgraph topology surrounding the query entity. By integrating raw encoder outputs with RGAT's relation-aware embeddings, our model captures and leverages richer multi-hop relational patterns and textual information. Our preliminary experiments on the CoDEx dataset demonstrate that GA-S2S outperforms competitive Seq2Seq-based baseline models, achieving up to a 19\% relative gain in link prediction accuracy.
匹配关键词: swarm intelligence
---

[ACADEMIC - ARXIV]
标题: SPATIOROUTE: Dynamic Prompt Routing for Zero-Shot Spatial Reasoning
作者: Pawat Chunhachatrachai, Gueter Josmy Faure, Hung-Ting Su, Winston H. Hsu
链接: https://arxiv.org/abs/2605.18209v1
完整摘要: Spatial question answering over egocentric video is a challenging task that requires Vision-Language Models (VLMs) to reason about 3D object positions, scene affordances, and directional relationships, particularly in the zero-shot setting where no task-specific fine-tuning is available. We introduce SpatioRoute, a dynamic prompt generation approach that routes each incoming question to a semantically tailored prompt template -- without any additional training, fine-tuning, or 3D sensor input. SpatioRoute operates in two complementary modes: SpatioRoute-R, a rule-based router that deterministically maps question typologies (e.g., What, Is, How, Can, Which) to specialized prompt templates; and SpatioRoute-L, an LLM-driven approach that generates task-specific prompts from the question and situational context alone, with no video input at routing time. We evaluate SpatioRoute on the SQA3D benchmark across VLMs spanning model families. SpatioRoute achieves consistent overall accuracy gains up to 5% over fixed prompt baselines, establishing a new state-of-the-art for zero-shot video-only spatial VQA without requiring 3D point-cloud inputs. As an additional finding, we observe that Chain-of-Thought (CoT) prompting, implemented via the Think it Twice architecture, consistently degrades performance in this setting on Qwen series models, confirming that question-aware routing is more effective than uniform reasoning instructions for spatial video understanding.
匹配关键词: swarm intelligence
---

[ACADEMIC - ARXIV]
标题: A Simplex Witness Certificate for Constant Collapse in Variational Autoencoders
作者: Zegu Zhang, Jianhua Peng, Jian Zhang
链接: https://arxiv.org/abs/2605.18224v1
完整摘要: This note studies exact constant collapse in variational autoencoders, where the encoder mean becomes independent of the input. The goal is to make this specific failure mode pre-designable, monitorable during training, and certifiable after training. The prior is kept as the standard Gaussian. Given a fixed teacher posterior, we attach to the latent mean a fixed simplex witness head. The resulting teacher-student alignment loss has an exact constant-predictor baseline equal to the teacher information. If the alignment loss is below this baseline, the latent mean cannot be input-independent constant collapsed. The simplex witness also has a closed-form inverse. Any full-support teacher posterior can be represented by embedding its centered log-odds into the latent space. This gives an explicit latent energy cost and explains when the alignment loss can be made small. A computable view gap handles the case where teacher targets are computed from a different view. Thus exact constant collapse is converted from an after-the-fact training pathology into a design-and-certificate problem.
匹配关键词: game theory agent
---

[ACADEMIC - ARXIV]
标题: Beyond the Cartesian Illusion: Testing Two-Stage Multi-Modal Theory of Mind under Perceptual Bottlenecks
作者: Yajing Zhou, Xiangyu Kong
链接: https://arxiv.org/abs/2605.18194v1
完整摘要: While Multi-Modal Large Language Models (MLLMs) demonstrate impressive capabilities in general reasoning, their embodied spatial intelligence remains hampered by a "Cartesian Illusion" - a reliance on text-based probability distributions that lack grounded, 3D topological understanding. This limitation is starkly exposed in multi-agent environments, which demand more than just scene perception; they require second-order Theory of Mind (ToM). Specifically, an Agent A must be able to infer Agent B's belief about the environment, governed strictly by Agent B's physical orientation and sensory limitations. In this paper, we probe the limits of two-stage spatial inference in MLLMs through a novel audio-visual task: requiring Agent A to predict Agent B's estimation of A's relative location. To solve this, we propose an Epistemic Sensory Bottleneck module that abandons rigid, rule-based coordinate transformations. Instead, we introduce an Anchor-Based Embodied Spatial Decomposition Chain-of-Thought (CoT). This guides the MLLM through a "geometric-to-semantic" projection, forcing it to first establish B's local coordinate system and then dynamically weight visual and auditory modalities based on whether A falls within B's visual frustum. Extensive evaluations reveal that while current MLLMs fundamentally struggle with spatial symmetry and out-of-view ambiguities (establishing a rigorous zero-shot baseline of 42% accuracy), our sensory-bounded reasoning chain robustly outperforms pure egocentric and allocentric baselines. By systematically benchmarking these perceptual bottlenecks, our work exposes the current limits of MLLM spatial reasoning and establishes a foundational paradigm for epistemic, modality-aware inference in Embodied AI.
匹配关键词: game theory agent
---

[ACADEMIC - ARXIV]
标题: Scalable Environments Drive Generalizable Agents
作者: Jiayi Zhang, Fanqi Kong, Guibin Zhang, Maojia Song, Zhaoyang Yu, Jianhao Ruan, Jinyu Xiang, Bang Liu, Chenglin Wu, Yuyu Luo
链接: https://arxiv.org/abs/2605.18181v1
完整摘要: Generalizable agents should adapt to diverse tasks and unseen environments beyond their training distribution. This position paper argues that such generalization requires environment scaling: expanding the distribution of executable rule-sets that agents interact with, rather than only increasing trajectories or tasks within fixed benchmarks. Current scaling practices largely focus on collecting more experience or broader task sets under fixed interaction rules, leaving agents brittle when underlying interfaces, dynamics, observations, or feedback signals change. The core challenge is therefore a world-level distribution shift: agents need systematic exposure to environments with meaningfully different executable rule-sets. To clarify this challenge, we propose a unified taxonomy that separates trajectory scaling, task scaling, and environment scaling by their primary deliverables and by what changes in the executable rule-set. Building on this taxonomy, we synthesize construction paradigms for scalable environments, contrasting programmatic generators that prioritize controllability and verifiability with generative world models that offer broader coverage and open-endedness. We further outline how environment scaling can be coupled with stateful learning mechanisms, emphasizing learned update rules for cross-environment adaptation. We conclude by discussing alternative perspectives and argue that scalable environments provide the essential substrate for measurable and controllable progress toward robust general agents.
匹配关键词: game theory agent
---

[ACADEMIC - ARXIV]
标题: Canonical Regularisation of Wide Feature-Learning Neural Networks
作者: George Whittle, Pranav Vaidhyanathan, Juliusz Ziomek, Natalia Ares, Maike A. Osborne
链接: https://arxiv.org/abs/2605.18180v1
完整摘要: Wide neural networks in the feature-learning regime drive modern deep learning, and yet they remain far less studied than their kernel-regime counterparts. We consider a critical yet under-explored difference between these two regimes: the regulariser and prior implied by gradient flow training. This canonical regularisation property is well-studied in kernel regime networks -- of all the infinite global minima, gradient flow selects exactly the vanishing ridge solution -- and underpins the celebrated NN-GP correspondence, precisely allowing the modelling of noise during training. However, we prove ridge regularisation biases gradient flow in feature-learning regime networks, even in the infinitesimal limit of vanishing regularisation. Over training, ridge distorts the inductive bias of the network, with a particular damage done to pretrained networks where the implicit prior is informative. We resolve this by axiomatising the canonical regulariser as a regime-agnostic function-space energy and lift, which uniquely identifies ridge in the kernel regime, and crucially generalises to the feature-learning regime. By studying the Riemannian geometry of feature-learning networks, we derive geodesic ridge from our framework, generalising ridge to the feature-learning regime. Correspondingly, we prove the canonical function-space prior is a Riemannian Gibbs Process, generalising the more familiar Gaussian Process. As a practical contribution, we propose arc ridge as a minimax-robust, scalable surrogate to geodesic ridge, revealing a deep relationship between early stopping and canonical regularisation across learning regimes. Finally, we demonstrate the consequences of our theory empirically on both image processing and NLP transfer-learning problems.
匹配关键词: game theory agent
---

[ACADEMIC - ARXIV]
标题: MARS: Technical Report for the CASTLE Challenge at EgoVis 2026
作者: Haoyu Zhang, Qiaohui Chu, Yisen Feng, Meng Liu, Weili Guan, Yaowei Wang, Liqiang Nie
链接: https://arxiv.org/abs/2605.18176v1
完整摘要: This report presents MARS, short for Multimodal Agentic Reasoning with Source selection, our system for the CASTLE Challenge at EgoVis 2026. Participants must answer 185 closed-form questions over the CASTLE 2024 dataset. In contrast to prior single-video egocentric benchmarks, CASTLE requires reasoning over four days of activity, 15 synchronized perspectives, official transcripts, and multiple auxiliary modalities, including personal photos, auxiliary videos, gaze, thermal imagery, and heartrate measurements. MARS therefore treats the task as an agentic evidence-selection problem over multimodal sources rather than a purely text-only pipeline. MARS first follows the official CASTLE directory organization to build evidence memories from two primary sources, videos and transcripts, and four auxiliary sources, gaze, heartrate, photos, and thermal imagery. Long videos are converted into captions and DeepSeek-based summaries only because CASTLE videos are too long to fit directly into the model context for every question; this step compresses temporal evidence while keeping photos and other auxiliary media available as source-specific evidence. At inference time, a GPT-5.4 decision agent repeatedly chooses whether to continue reasoning, request a specific missing modality, produce an answer, or fall back to a random option when the evidence remains insufficient. The resulting system achieved second place on the final CASTLE Challenge leaderboard. Our codes are available at https://github.com/Hyu-Zhang/MARS.
匹配关键词: game theory agent
---

[ACADEMIC - ARXIV]
标题: Beyond the Cartesian Illusion: Testing Two-Stage Multi-Modal Theory of Mind under Perceptual Bottlenecks
作者: Yajing Zhou, Xiangyu Kong
链接: https://arxiv.org/abs/2605.18194v1
完整摘要: While Multi-Modal Large Language Models (MLLMs) demonstrate impressive capabilities in general reasoning, their embodied spatial intelligence remains hampered by a "Cartesian Illusion" - a reliance on text-based probability distributions that lack grounded, 3D topological understanding. This limitation is starkly exposed in multi-agent environments, which demand more than just scene perception; they require second-order Theory of Mind (ToM). Specifically, an Agent A must be able to infer Agent B's belief about the environment, governed strictly by Agent B's physical orientation and sensory limitations. In this paper, we probe the limits of two-stage spatial inference in MLLMs through a novel audio-visual task: requiring Agent A to predict Agent B's estimation of A's relative location. To solve this, we propose an Epistemic Sensory Bottleneck module that abandons rigid, rule-based coordinate transformations. Instead, we introduce an Anchor-Based Embodied Spatial Decomposition Chain-of-Thought (CoT). This guides the MLLM through a "geometric-to-semantic" projection, forcing it to first establish B's local coordinate system and then dynamically weight visual and auditory modalities based on whether A falls within B's visual frustum. Extensive evaluations reveal that while current MLLMs fundamentally struggle with spatial symmetry and out-of-view ambiguities (establishing a rigorous zero-shot baseline of 42% accuracy), our sensory-bounded reasoning chain robustly outperforms pure egocentric and allocentric baselines. By systematically benchmarking these perceptual bottlenecks, our work exposes the current limits of MLLM spatial reasoning and establishes a foundational paradigm for epistemic, modality-aware inference in Embodied AI.
匹配关键词: agent communication
---

[ACADEMIC - ARXIV]
标题: Scalable Environments Drive Generalizable Agents
作者: Jiayi Zhang, Fanqi Kong, Guibin Zhang, Maojia Song, Zhaoyang Yu, Jianhao Ruan, Jinyu Xiang, Bang Liu, Chenglin Wu, Yuyu Luo
链接: https://arxiv.org/abs/2605.18181v1
完整摘要: Generalizable agents should adapt to diverse tasks and unseen environments beyond their training distribution. This position paper argues that such generalization requires environment scaling: expanding the distribution of executable rule-sets that agents interact with, rather than only increasing trajectories or tasks within fixed benchmarks. Current scaling practices largely focus on collecting more experience or broader task sets under fixed interaction rules, leaving agents brittle when underlying interfaces, dynamics, observations, or feedback signals change. The core challenge is therefore a world-level distribution shift: agents need systematic exposure to environments with meaningfully different executable rule-sets. To clarify this challenge, we propose a unified taxonomy that separates trajectory scaling, task scaling, and environment scaling by their primary deliverables and by what changes in the executable rule-set. Building on this taxonomy, we synthesize construction paradigms for scalable environments, contrasting programmatic generators that prioritize controllability and verifiability with generative world models that offer broader coverage and open-endedness. We further outline how environment scaling can be coupled with stateful learning mechanisms, emphasizing learned update rules for cross-environment adaptation. We conclude by discussing alternative perspectives and argue that scalable environments provide the essential substrate for measurable and controllable progress toward robust general agents.
匹配关键词: agent communication
---

[ACADEMIC - ARXIV]
标题: MARS: Technical Report for the CASTLE Challenge at EgoVis 2026
作者: Haoyu Zhang, Qiaohui Chu, Yisen Feng, Meng Liu, Weili Guan, Yaowei Wang, Liqiang Nie
链接: https://arxiv.org/abs/2605.18176v1
完整摘要: This report presents MARS, short for Multimodal Agentic Reasoning with Source selection, our system for the CASTLE Challenge at EgoVis 2026. Participants must answer 185 closed-form questions over the CASTLE 2024 dataset. In contrast to prior single-video egocentric benchmarks, CASTLE requires reasoning over four days of activity, 15 synchronized perspectives, official transcripts, and multiple auxiliary modalities, including personal photos, auxiliary videos, gaze, thermal imagery, and heartrate measurements. MARS therefore treats the task as an agentic evidence-selection problem over multimodal sources rather than a purely text-only pipeline. MARS first follows the official CASTLE directory organization to build evidence memories from two primary sources, videos and transcripts, and four auxiliary sources, gaze, heartrate, photos, and thermal imagery. Long videos are converted into captions and DeepSeek-based summaries only because CASTLE videos are too long to fit directly into the model context for every question; this step compresses temporal evidence while keeping photos and other auxiliary media available as source-specific evidence. At inference time, a GPT-5.4 decision agent repeatedly chooses whether to continue reasoning, request a specific missing modality, produce an answer, or fall back to a random option when the evidence remains insufficient. The resulting system achieved second place on the final CASTLE Challenge leaderboard. Our codes are available at https://github.com/Hyu-Zhang/MARS.
匹配关键词: agent communication
---

[ACADEMIC - ARXIV]
标题: Whispers in the Noise: Surrogate-Guided Concept Awakening via a Multi-Agent Framework
作者: Mengyu Sun, Ziyuan Yang, Zunlong Zhou, Junxu Liu, Haibo Hu, Yi Zhang
链接: https://arxiv.org/abs/2605.18150v1
完整摘要: Diffusion models (DMs) are widely used for text-to-image generation, but their strong generative capabilities also raise concerns about unsafe or undesirable content. Concept erasure aims to mitigate these risks by removing specific concepts from pretrained models. However, recent studies show that such methods often suppress rather than fully eliminate target concepts, leaving models vulnerable to awakening attacks. Existing approaches primarily rely on white-box access through optimization or inversion, while concept awakening under black-box constraints remains underexplored. In this work, we revisit the denoising process from a trajectory perspective and show that concept erasure mainly disrupts early-stage text-semantic alignment but does not fully prevent semantic information from propagating along the denoising dynamics. As generation proceeds, the model increasingly depends on the evolving noisy state rather than textual conditions, which creates an opportunity to bypass erased mappings. Motivated by this observation, we propose ConceptAgent, a training-free, black-box, multi-agent framework that awakens erased concepts by initializing the denoising trajectory from surrogate-guided noisy states. Extensive experiments demonstrate that ConceptAgent enables accurate and controllable awakening of erased concepts under black-box settings without access to model parameters, gradients, or internal representations. These results highlight fundamental limitations of current concept erasure methods and provide new insights into the dynamic nature of semantic control in DMs.
匹配关键词: agent communication
---

[ACADEMIC - ARXIV]
标题: Evidence-Grounded Frontier Mapping and Agentic Hypothesis Generation in Nanomedicine
作者: Christiaan G. A. Viviers, Koen de Bruin, Mirre M. Trines, Ayla M. Hokke, Roy van der Meel, Avi Schroeder, Twan Lammers, Willem J. M. Mulder, Fons van der Sommen
链接: https://arxiv.org/abs/2605.18144v1
完整摘要: Nanomedicine research spans delivery chemistry, immunology, imaging, biomaterials, and disease-specific translational science, yet its conceptual design space remains fragmented across a large and heterogeneous literature. To date, artificial intelligence in nanomedicine has focused primarily on property prediction and formulation optimization, with much less attention to evidence-grounded discovery support at the level of research direction selection. We introduce pArticleMap, a literature-mapping and research-hypothesis-generation system that combines article embeddings, similarity-graph analysis, sparse frontier extraction, structured evidence-pack retrieval, and an audited large-language-model (LLM) workflow for grounded ideation. Rather than forecasting future concept co-occurrence, pArticleMap targets low-density article-level bridge regions and cluster interfaces, then generates and scores citation-grounded hypotheses with large language models in an agentic setup. We evaluate the system with a retrospective realization benchmark (generate later literature under a historical cutoff) and a blinded human reader assessment layer across cue-conditioned nanomedicine tasks. Across 4 selected retrospective bundles, pArticleMap generated ideas and selected task-retained hypotheses (winner ideas) under the benchmark protocol. For task-level retained hypotheses, a pooled gold recovery rate of 10.8% was obtained, with a recall@10 of 15.9% and a future-neighborhood rate of 61.0%, indicating that the system often reached the correct forward-looking neighborhood (paper ideas) even without exact paper-level recovery. Human-agent agreement is modest overall, indicating that internal scoring is useful as a support signal but does not replace expert judgment. These results position pArticleMap as a conservative, evidence-grounded research assistant for nanomedicine.
匹配关键词: agent communication
---

[ACADEMIC - ARXIV]
标题: Context Memorization for Efficient Long Context Generation
作者: Yasuyuki Okoshi, Hao Mark Chen, Guanxi Lu, Hongxiang Fan, Masato Motomura, Daichi Fujiki
链接: https://arxiv.org/abs/2605.18226v1
完整摘要: Modern large language model (LLM) applications increasingly rely on long conditioning prefixes to control model behavior at inference time. While prefix-augmented inference is effective, it incurs two structural limitations: i) the prefix's influence fades as generation proceeds, and ii) attention computation over the prefix scales linearly with its length. Existing approaches either keep the prefix in attention while compressing it, or internalize it into model parameters through gradient-based training. The former still attends to the prefix at inference, while the latter is training-intensive and ill-suited to prefix updates. To address these issues, we propose attention-state memory, a training-free approach that externalizes the prefix into a lightweight, lookup-based memory of precomputed attention states between prefix and query tokens. On ManyICLBench with LLaMA-3.1-8B, our method improves accuracy over in-context learning at 1K-8K memory budgets while reducing attention latency by 1.36x at 8K, and surpasses full-attention RAG performance on NBA benchmark using only 20% of its memory footprint.
匹配关键词: emergent behavior
---

[ACADEMIC - ARXIV]
标题: Ringmaster LMO: Asynchronous Linear Minimization Oracle Momentum Method
作者: Abdurakhmon Sadiev, Artavazd Maranjyan, Ivan Ilin, Peter Richtárik
链接: https://arxiv.org/abs/2605.18174v1
完整摘要: Muon has recently emerged as a strong alternative to AdamW for training neural networks, with encouraging large-scale pretraining results and growing evidence that matrix-structured updates can be faster in practice. Yet Muon, and more generally Linear Minimization Oracle (LMO) based methods, are typically used synchronously. This is problematic in heterogeneous distributed systems, where workers complete gradient computations at different speeds and synchronous training must repeatedly wait for slower workers. In this work, we introduce Ringmaster LMO, an asynchronous LMO-based momentum method for unconstrained stochastic nonconvex optimization. Our method builds on the delay-thresholding idea of Ringmaster ASGD. For SGD-type methods, Ringmaster ASGD achieves optimal time complexity by discarding overly stale gradients. Ringmaster LMO extends this mechanism to general LMO-based updates. We establish convergence guarantees under generalized $(L_0, L_1)$-smoothness and further develop a parameter-agnostic variant with decreasing stepsizes and adaptive delay thresholds. Finally, we translate our iteration guarantees into time complexity bounds under heterogeneous worker computation times. In the classical Euclidean smooth setting, these bounds recover the optimal time complexity of Ringmaster ASGD. Experiments on stochastic quadratic problems and NanoChat language-model pretraining show that the advantages of Ringmaster LMO grow with system heterogeneity and that the method outperforms strong synchronous and asynchronous baselines.
匹配关键词: emergent behavior
---

[ACADEMIC - ARXIV]
标题: Foundation Models for Credit Risk Prediction: A Game Changer?
作者: Bart Baesens, Andreas Goethals, Stefan Lessmann, Simon De Vos, Cristián Bravo, David Martens, Victor Medina-Olivares, Christophe Mues, Maria Oskarsdóttir, Seppe vanden Broucke, Tim Verdonck, Wouter Verbeke
链接: https://arxiv.org/abs/2605.18147v1
完整摘要: Predictive models play a pivotal role in credit risk management, guiding critical decisions through accurate estimation of default probabilities and losses. Extensive research has introduced new modeling techniques, complemented by large-scale benchmarking studies consolidating the state-of-the-art. Today, quasi-standards such as gradient-boosting models paired with SHAP explainers have emerged, yet continuous improvement of risk models remains a top priority. Concurrently, rapid advancements in AI, most notably large language models, have disrupted predictive modeling paradigms. Foundation models, pretrained on extensive datasets from diverse domains, have demonstrated remarkable performance by leveraging prior knowledge. While prevalent in natural language processing and computer vision, foundation models for tabular data have only recently emerged. We conjecture that pretraining on out-of-domain data is particularly beneficial in small-data settings, such as SME lending or specialized corporate portfolios, and may help address longstanding challenges including low default portfolios and class imbalance. This paper benchmarks recently proposed tabular foundation models against a broad set of competitors, including established and advanced machine learning techniques, across two core tasks: PD and LGD modeling. Our evaluation encompasses various datasets, performance indicators, and experimental conditions. We find that tabular foundation models generally perform best across datasets and tasks. Moreover, they offer significant improvement in predictive performance as dataset size shrinks. These results are remarkable given that the models are tested out-of-the-box, without hyperparameter tuning, ensuring ease of use and mitigating computational costs.
匹配关键词: emergent behavior
---

[ACADEMIC - ARXIV]
标题: KVDrive: A Holistic Multi-Tier KV Cache Management System for Long-Context LLM Inference
作者: Jian Lin, Jiazhi Mi, Zicong Hong, Haodong Wang, Qianli Liu, Haodyue Zhang, Peng Li, Song Guo
链接: https://arxiv.org/abs/2605.18071v1
完整摘要: Supporting long-context LLMs is challenging due to the substantial memory demands of the key-value (KV) cache. Existing offloading systems store the full cache in host memory and selectively fetch critical entries during decoding, but this strategy quickly hits a ceiling: sparsity cannot be pushed further without degrading accuracy. As a result, when context length and batch size grow, the volume of KV transfers rises sharply and becomes the dominant source of decoding latency. We present KVDrive, a holistic multi-tier KV cache management system spanning GPU memory, host DRAM, and SSD. Unlike prior work that pursues greater sparsity through algorithmic refinements, KVDrive tackles the problem from a systems perspective - jointly orchestrating cache placement, pipeline scheduling, and cross-tier coordination to sustain high-throughput inference under tight GPU budgets. KVDrive advances three fundamental capabilities: it adapts cache management to attention behavior to maximize reuse and minimize redundant data movement; it restructures the decoding pipeline to overlap I/O- and CPU/GPU compute-bound stages, eliminating stalls across heterogeneous resources; and it harmonizes data movement across memory tiers to unlock scalable long-context inference far beyond GPU and DRAM limits. We have implemented a fully functional prototype of KVDrive and evaluated it on long-context benchmarks with popular LLMs. The system achieves up to 1.74x higher throughput compared to state-of-the-art works while preserving accuracy.
匹配关键词: emergent behavior
---

[ACADEMIC - ARXIV]
标题: Confidence-Gated Robot Autonomy: When Does Uncertainty Actually Help?
作者: Johannes A. Gaus, Jhon P. F. Charaja, Daniel Haeufle
链接: https://arxiv.org/abs/2605.18045v1
完整摘要: Robotic systems often use predictive uncertainty to decide whether to act autonomously or defer to a fallback policy. In threshold-gated autonomy, uncertainty matters mainly through its ability to rank likely errors. Standard metrics such as expected calibration error and AUROC do not directly test whether uncertainty changes act/defer decisions. We therefore evaluate uncertainty using Spearman rank correlation, paired bootstrap equivalence testing, and act/defer agreement. Across three temporal activity-recognition benchmarks, we find a dataset-dependent competence regime below which uncertainty provides a weak and unstable error ranking. Above this regime, softmax heuristics, MC Dropout, and ensembles produce similar gating behavior, while threshold choice has a much larger effect on execution outcomes. A multi-seed embodied simulation shows the same pattern for collision rate and cost once realized autonomy is matched. Under temporal covariate shift, ranking quality remains stable, but fine grained semantic OOD detection remains near chance. These results suggest that simple uncertainty proxies can suffice for selective gating once the base model is competent, but not for semantic novelty detection.
匹配关键词: emergent behavior
---

[ACADEMIC - ARXIV]
标题: SPATIOROUTE: Dynamic Prompt Routing for Zero-Shot Spatial Reasoning
作者: Pawat Chunhachatrachai, Gueter Josmy Faure, Hung-Ting Su, Winston H. Hsu
链接: https://arxiv.org/abs/2605.18209v1
完整摘要: Spatial question answering over egocentric video is a challenging task that requires Vision-Language Models (VLMs) to reason about 3D object positions, scene affordances, and directional relationships, particularly in the zero-shot setting where no task-specific fine-tuning is available. We introduce SpatioRoute, a dynamic prompt generation approach that routes each incoming question to a semantically tailored prompt template -- without any additional training, fine-tuning, or 3D sensor input. SpatioRoute operates in two complementary modes: SpatioRoute-R, a rule-based router that deterministically maps question typologies (e.g., What, Is, How, Can, Which) to specialized prompt templates; and SpatioRoute-L, an LLM-driven approach that generates task-specific prompts from the question and situational context alone, with no video input at routing time. We evaluate SpatioRoute on the SQA3D benchmark across VLMs spanning model families. SpatioRoute achieves consistent overall accuracy gains up to 5% over fixed prompt baselines, establishing a new state-of-the-art for zero-shot video-only spatial VQA without requiring 3D point-cloud inputs. As an additional finding, we observe that Chain-of-Thought (CoT) prompting, implemented via the Think it Twice architecture, consistently degrades performance in this setting on Qwen series models, confirming that question-aware routing is more effective than uniform reasoning instructions for spatial video understanding.
匹配关键词: reasoning
---

[ACADEMIC - ARXIV]
标题: Concise and Logically Consistent Conformal Sets for Neuro-Symbolic Concept-Based Models
作者: Samuele Bortolotti, Emanuele Marconato, Andrea Pugnana, Andrea Passerini, Stefano Teso
链接: https://arxiv.org/abs/2605.18202v1
完整摘要: Neuro-Symbolic Concept-based Models (NeSy-CBMs) are a family of architectures that integrate neural networks with symbolic reasoning for enhanced reliability in high-stakes applications. They work by first extracting high-level concepts from the input and then inferring a task label from these compatibly with given logical constraints. Yet, their label and concept predictions can be overconfident, making it difficult for stakeholders to gauge when the model's decisions can be trusted. We address this issue by integrating ideas from Conformal Prediction (CP), a framework providing rigorous, distribution-free coverage guarantees. We formalize three desiderata -- consistency, coverage, and conciseness -- that any conformal method for NeSy-CBMs should satisfy, and show that existing approaches fall short of at least one. We then introduce COCOCO, a post-hoc framework that conformalizes concepts and labels jointly and reconciles them via a single deduction-abduction revision step. COCOCO satisfies all three desiderata, retains distribution-free coverage, is robust to imperfect knowledge and supports user-specified size budgets. Our experiments on 8 data sets highlight how COCOCO compares favorably against competitors and natural baselines in terms of performance and set size.
匹配关键词: reasoning
---

[ACADEMIC - ARXIV]
标题: Beyond the Cartesian Illusion: Testing Two-Stage Multi-Modal Theory of Mind under Perceptual Bottlenecks
作者: Yajing Zhou, Xiangyu Kong
链接: https://arxiv.org/abs/2605.18194v1
完整摘要: While Multi-Modal Large Language Models (MLLMs) demonstrate impressive capabilities in general reasoning, their embodied spatial intelligence remains hampered by a "Cartesian Illusion" - a reliance on text-based probability distributions that lack grounded, 3D topological understanding. This limitation is starkly exposed in multi-agent environments, which demand more than just scene perception; they require second-order Theory of Mind (ToM). Specifically, an Agent A must be able to infer Agent B's belief about the environment, governed strictly by Agent B's physical orientation and sensory limitations. In this paper, we probe the limits of two-stage spatial inference in MLLMs through a novel audio-visual task: requiring Agent A to predict Agent B's estimation of A's relative location. To solve this, we propose an Epistemic Sensory Bottleneck module that abandons rigid, rule-based coordinate transformations. Instead, we introduce an Anchor-Based Embodied Spatial Decomposition Chain-of-Thought (CoT). This guides the MLLM through a "geometric-to-semantic" projection, forcing it to first establish B's local coordinate system and then dynamically weight visual and auditory modalities based on whether A falls within B's visual frustum. Extensive evaluations reveal that while current MLLMs fundamentally struggle with spatial symmetry and out-of-view ambiguities (establishing a rigorous zero-shot baseline of 42% accuracy), our sensory-bounded reasoning chain robustly outperforms pure egocentric and allocentric baselines. By systematically benchmarking these perceptual bottlenecks, our work exposes the current limits of MLLM spatial reasoning and establishes a foundational paradigm for epistemic, modality-aware inference in Embodied AI.
匹配关键词: reasoning
---

[ACADEMIC - ARXIV]
标题: View-Aware Semantic Alignment for Aerial-Ground Person Re-Identification
作者: Quan Zhang, Zeqiang Cai, Peiming Zhao, Jingze Wu, Cailun Wu, Hongbo Chen, Jianhuang Lai
链接: https://arxiv.org/abs/2605.18192v1
完整摘要: Aerial-Ground Person Re-Identification (AGPReID) remains highly challenging due to drastic viewpoint variations between drones and fixed cameras. Existing methods typically follow a view-invariant paradigm, aligning shared features across views to achieve robustness. However, view-invariant inherently enforces part-level alignment, which ignores view-specific cues and discriminative identity information. To this end, this work proposes ViSA (View-aware Semantic Alignment), a view-aware framework that achieves cross-view semantic consistency containing an Expert-driven Token Generation Module (ETGM) and a Dual-branch Local Fusion Module (DLFM). Technically, the former constructs a set of view-aware experts to generate adaptive semantic queries that perceive viewpoint-specific patterns, while the latter leverages graph reasoning to extract and align local regions responsive to different experts. Extensive experiments on three AGPReID benchmarks including AG-ReID.v2, CARGO and LAGPeR demonstrate that ViSA consistently achieves superior performance, with a notable 10.06\% mAP improvement on the challenging CARGO cross-view protocol. The code is available at \href{https://github.com/Cat-Zero/ViSA}{https://github.com/Cat-Zero/ViSA}.
匹配关键词: reasoning
---

[ACADEMIC - ARXIV]
标题: MARS: Technical Report for the CASTLE Challenge at EgoVis 2026
作者: Haoyu Zhang, Qiaohui Chu, Yisen Feng, Meng Liu, Weili Guan, Yaowei Wang, Liqiang Nie
链接: https://arxiv.org/abs/2605.18176v1
完整摘要: This report presents MARS, short for Multimodal Agentic Reasoning with Source selection, our system for the CASTLE Challenge at EgoVis 2026. Participants must answer 185 closed-form questions over the CASTLE 2024 dataset. In contrast to prior single-video egocentric benchmarks, CASTLE requires reasoning over four days of activity, 15 synchronized perspectives, official transcripts, and multiple auxiliary modalities, including personal photos, auxiliary videos, gaze, thermal imagery, and heartrate measurements. MARS therefore treats the task as an agentic evidence-selection problem over multimodal sources rather than a purely text-only pipeline. MARS first follows the official CASTLE directory organization to build evidence memories from two primary sources, videos and transcripts, and four auxiliary sources, gaze, heartrate, photos, and thermal imagery. Long videos are converted into captions and DeepSeek-based summaries only because CASTLE videos are too long to fit directly into the model context for every question; this step compresses temporal evidence while keeping photos and other auxiliary media available as source-specific evidence. At inference time, a GPT-5.4 decision agent repeatedly chooses whether to continue reasoning, request a specific missing modality, produce an answer, or fall back to a random option when the evidence remains insufficient. The resulting system achieved second place on the final CASTLE Challenge leaderboard. Our codes are available at https://github.com/Hyu-Zhang/MARS.
匹配关键词: reasoning
---

[ACADEMIC - ARXIV]
标题: SPATIOROUTE: Dynamic Prompt Routing for Zero-Shot Spatial Reasoning
作者: Pawat Chunhachatrachai, Gueter Josmy Faure, Hung-Ting Su, Winston H. Hsu
链接: https://arxiv.org/abs/2605.18209v1
完整摘要: Spatial question answering over egocentric video is a challenging task that requires Vision-Language Models (VLMs) to reason about 3D object positions, scene affordances, and directional relationships, particularly in the zero-shot setting where no task-specific fine-tuning is available. We introduce SpatioRoute, a dynamic prompt generation approach that routes each incoming question to a semantically tailored prompt template -- without any additional training, fine-tuning, or 3D sensor input. SpatioRoute operates in two complementary modes: SpatioRoute-R, a rule-based router that deterministically maps question typologies (e.g., What, Is, How, Can, Which) to specialized prompt templates; and SpatioRoute-L, an LLM-driven approach that generates task-specific prompts from the question and situational context alone, with no video input at routing time. We evaluate SpatioRoute on the SQA3D benchmark across VLMs spanning model families. SpatioRoute achieves consistent overall accuracy gains up to 5% over fixed prompt baselines, establishing a new state-of-the-art for zero-shot video-only spatial VQA without requiring 3D point-cloud inputs. As an additional finding, we observe that Chain-of-Thought (CoT) prompting, implemented via the Think it Twice architecture, consistently degrades performance in this setting on Qwen series models, confirming that question-aware routing is more effective than uniform reasoning instructions for spatial video understanding.
匹配关键词: chain-of-thought
---

[ACADEMIC - ARXIV]
标题: Beyond the Cartesian Illusion: Testing Two-Stage Multi-Modal Theory of Mind under Perceptual Bottlenecks
作者: Yajing Zhou, Xiangyu Kong
链接: https://arxiv.org/abs/2605.18194v1
完整摘要: While Multi-Modal Large Language Models (MLLMs) demonstrate impressive capabilities in general reasoning, their embodied spatial intelligence remains hampered by a "Cartesian Illusion" - a reliance on text-based probability distributions that lack grounded, 3D topological understanding. This limitation is starkly exposed in multi-agent environments, which demand more than just scene perception; they require second-order Theory of Mind (ToM). Specifically, an Agent A must be able to infer Agent B's belief about the environment, governed strictly by Agent B's physical orientation and sensory limitations. In this paper, we probe the limits of two-stage spatial inference in MLLMs through a novel audio-visual task: requiring Agent A to predict Agent B's estimation of A's relative location. To solve this, we propose an Epistemic Sensory Bottleneck module that abandons rigid, rule-based coordinate transformations. Instead, we introduce an Anchor-Based Embodied Spatial Decomposition Chain-of-Thought (CoT). This guides the MLLM through a "geometric-to-semantic" projection, forcing it to first establish B's local coordinate system and then dynamically weight visual and auditory modalities based on whether A falls within B's visual frustum. Extensive evaluations reveal that while current MLLMs fundamentally struggle with spatial symmetry and out-of-view ambiguities (establishing a rigorous zero-shot baseline of 42% accuracy), our sensory-bounded reasoning chain robustly outperforms pure egocentric and allocentric baselines. By systematically benchmarking these perceptual bottlenecks, our work exposes the current limits of MLLM spatial reasoning and establishes a foundational paradigm for epistemic, modality-aware inference in Embodied AI.
匹配关键词: chain-of-thought
---

[ACADEMIC - ARXIV]
标题: The Expressive Power of Low Precision Softmax Transformers with (Summarized) Chain-of-Thought
作者: Moritz Brösamle, Stephan Eckstein
链接: https://arxiv.org/abs/2605.18079v1
完整摘要: Existing expressivity results for transformers typically rely on hardmax attention, high precision, and other architectural modifications that disconnect them from the models used in practice. We bridge this gap by analyzing standard transformer decoders with softmax attention and rounding of activations and attention weights, while allowing depth and width to grow logarithmically with the context length. As an intermediate step, we construct hardmax transformers with ternary activations and well-separated attention scores that simulate Turing machines using Chain-of-Thought (CoT). This lets us convert the constructions to equivalent softmax transformers without the unrealistic parameter magnitudes or activation precision that prior approaches would require. Using the same technique, we analyze a recently proposed summarized CoT paradigm and show that it simulates Turing machines more efficiently, with model size scaling logarithmically in a space bound rather than a time bound. We empirically test predictions made by our results on a Sudoku reasoning task and find better alignment with learnability than for prior high-precision results. Our code is available at https://github.com/moritzbroe/transformer-expressivity.
匹配关键词: chain-of-thought
---

[ACADEMIC - ARXIV]
标题: DuIVRS-2: An LLM-based Interactive Voice Response System for Large-scale POI Attribute Acquisition
作者: Le Zhang, Shengming Zhang, Rui Zha, Yunpeng Wu, Jingbo Zhou, Jizhou Huang
链接: https://arxiv.org/abs/2605.17900v1
完整摘要: Accurate Point of Interest (POI) attribute acquisition is essential for location-based services, yet traditional modular Interactive Voice Response (IVR) systems suffer from error accumulation and high maintenance overhead. We present DuIVRS-2, a large language model (LLM)-based end-to-end framework designed for large-scale POI attribute acquisition at Baidu Maps. To address the long-tail distribution of real-world interactions, our methodology first employs a finite state machine (FSM)-guided data augmentation strategy to synthesize a balanced and diverse training dataset. We then streamline dialogue management via a selective generation scheme combined with a Chain-of-Thought (CoT) mechanism, which ensures output stability and effectively eliminates hallucinations in industrial settings. To facilitate continuous policy refinement with minimal manual effort, we design a cooperative iterative learning framework that leverages a dual-evaluator voting system. Deployed in production for two months, DuIVRS-2 processed 0.4 million calls daily and achieved a 83.9\% Task Success Rate (TSR), outperforming its predecessor by 4 percentage points while maintaining a low reaction time of 130ms. This work provides a production-proven reference for developing robust, cost-effective LLM agents for large-scale industrial dialogue applications.
匹配关键词: chain-of-thought
---

[ACADEMIC - ARXIV]
标题: Context Memorization for Efficient Long Context Generation
作者: Yasuyuki Okoshi, Hao Mark Chen, Guanxi Lu, Hongxiang Fan, Masato Motomura, Daichi Fujiki
链接: https://arxiv.org/abs/2605.18226v1
完整摘要: Modern large language model (LLM) applications increasingly rely on long conditioning prefixes to control model behavior at inference time. While prefix-augmented inference is effective, it incurs two structural limitations: i) the prefix's influence fades as generation proceeds, and ii) attention computation over the prefix scales linearly with its length. Existing approaches either keep the prefix in attention while compressing it, or internalize it into model parameters through gradient-based training. The former still attends to the prefix at inference, while the latter is training-intensive and ill-suited to prefix updates. To address these issues, we propose attention-state memory, a training-free approach that externalizes the prefix into a lightweight, lookup-based memory of precomputed attention states between prefix and query tokens. On ManyICLBench with LLaMA-3.1-8B, our method improves accuracy over in-context learning at 1K-8K memory budgets while reducing attention latency by 1.36x at 8K, and surpasses full-attention RAG performance on NBA benchmark using only 20% of its memory footprint.
匹配关键词: test-time compute
---

[ACADEMIC - ARXIV]
标题: A Simplex Witness Certificate for Constant Collapse in Variational Autoencoders
作者: Zegu Zhang, Jianhua Peng, Jian Zhang
链接: https://arxiv.org/abs/2605.18224v1
完整摘要: This note studies exact constant collapse in variational autoencoders, where the encoder mean becomes independent of the input. The goal is to make this specific failure mode pre-designable, monitorable during training, and certifiable after training. The prior is kept as the standard Gaussian. Given a fixed teacher posterior, we attach to the latent mean a fixed simplex witness head. The resulting teacher-student alignment loss has an exact constant-predictor baseline equal to the teacher information. If the alignment loss is below this baseline, the latent mean cannot be input-independent constant collapsed. The simplex witness also has a closed-form inverse. Any full-support teacher posterior can be represented by embedding its centered log-odds into the latent space. This gives an explicit latent energy cost and explains when the alignment loss can be made small. A computable view gap handles the case where teacher targets are computed from a different view. Thus exact constant collapse is converted from an after-the-fact training pathology into a design-and-certificate problem.
匹配关键词: test-time compute
---

[ACADEMIC - ARXIV]
标题: Best Segmentation Buddies for Image-Shape Correspondence
作者: Itai Lang, Dongwei Lyu, Dale Decatur, Rana Hanocka
链接: https://arxiv.org/abs/2605.18193v1
完整摘要: Finding correspondences is a fundamental and extensively researched problem in computer vision and graphics. In this work, we examine the underexplored task of estimating segmentation-to-segmentation correspondence between images in the wild and untextured 3D shapes. This task is highly challenging due to substantial differences in appearance, geometry, and viewpoint. Our approach bridges the cross-modality gap by linking pixels in the image segment to vertices in the corresponding semantic part of the 3D shape. To achieve this, we first distill deep visual features from a 2D vision model onto the 3D shape surface, allowing for the computation of feature similarity between image pixels and shape vertices. Then, we identify Best Segmentation Buddies, vertices whose most similar image pixel lies within the image segmentation region, enabling the reliable discovery of vertices in semantically corresponding shape parts. Finally, we leverage distilled 3D features from the 2D image segmentation model to segment the shape directly in 3D, bootstrapping the correspondence process. We demonstrate the generality and robustness of our approach across a wide range of image-shape pairs, showcasing accurate and semantically meaningful correspondences. Our project page is at https://threedle.github.io/bsb/.
匹配关键词: test-time compute
---

[ACADEMIC - ARXIV]
标题: Pairwise Preference Reward and Group-Based Diversity Enhancement for Superior Open-Ended Generation
作者: Guining Cao, Jiaxin Peng, Chu Zeng, Yu Zhao, Shuangyong Song, Yongxiang
链接: https://arxiv.org/abs/2605.18191v1
完整摘要: Current reinforcement learning(RL) methods are broadly applicable and powerful in verifiable settings where scalar rewards can be provided. However, in open-ended generation tasks, verifying the correctness of responses remains challenging, and training reward models incurs substantial computational and annotation costs. Moreover, reinforcement learning (RLVR) often leads to diversity collapse and produces stereotypical or rigid outputs, outcomes that are particularly undesirable in open-domain scenarios. We propose Pairwise Preference Reward and Group-based Diversity Enhancement (PPR-GDE), a RL method that is more suitable for open-ended generation. PPR-GDE does not require scalar rewards and incorporates group-level diversity into the reward signal, it preserves the comparative structure of subjective evaluation through a pairwise preference reward, mitigates judge position bias via repeated comparisons with swapped response order, and introduces a group-based diversity reward that explicitly encourages semantic dispersion within a response group, all of these reward signals are integrated into a unified group-relative policy optimization objective. We instantiate PPR-GDE on role-playing task, experiments show that PPR-GDE achieves a better alignment quality as well as expressive diversity than strong RL baselines. Further analysis shows that pairwise preference is critical for preference alignment in subjective perspective, while the diversity metric plays an essential role in achieving superior expressive diversity and broader semantic coverage.
匹配关键词: test-time compute
---

[ACADEMIC - ARXIV]
标题: Dual-Rate Diffusion: Accelerating diffusion models with an interleaved heavy-light network
作者: Grigory Bartosh, David Ruhe, Emiel Hoogeboom, Jonathan Heek, Thomas Mensink, Tim Salimans
链接: https://arxiv.org/abs/2605.18190v1
完整摘要: Diffusion models achieve state-of-the-art generative performance but suffer from high computational costs during inference due to the repeated evaluation of a heavy neural network. In this work, we propose Dual-Rate Diffusion, a method to accelerate sampling by interleaving the execution of a heavy high-capacity context encoder and a light efficient denoising model. The context encoder is evaluated sparsely to extract high-dimensional features, which are effectively reused by the light denoising model at every step to refine the sample efficiently. This approach significantly accelerates inference without compromising sample quality. On ImageNet benchmarks, Dual-Rate Diffusion matches the performance of standard baselines while reducing computational cost by a factor of $2$-$4$. Furthermore, we demonstrate that our method is compatible with distillation techniques, such as Moment Matching Distillation, enabling further efficiency gains in few-step generation.
匹配关键词: test-time compute
---

[ACADEMIC - ARXIV]
标题: Self-Evolving Spatial Reasoning in Vision Language Models via Geometric Logic Consistency
作者: Junming Liu, Yuqi Li, Yifei Sun, Maonan Wang, Piotr Koniusz, Yirong Chen, Ding Wang
链接: https://arxiv.org/abs/2605.18162v1
完整摘要: Vision-Language Models (VLMs) have made striking progress, yet their spatial reasoning remains fragile: models that answer an original input correctly can still fail under paired transformations with predictable answer mappings, revealing a gap between instance-level correctness and robust spatial reasoning. To address this, we propose Spatial Alignment via Geometric Evolution (SAGE), a self-evolving framework that enforces logical consistency in VLMs through geometric and linguistic duality operations. SAGE incorporates duality consistency as an auxiliary reward within GRPO training, encouraging models to produce logically coherent answers across original and transformed inputs. A dynamic operation pool continuously probes for inconsistencies, promoting challenging operations and retiring mastered ones, so that training focuses on the most informative signals. SAGE is model-agnostic, data-efficient compared to prior GRPO methods, and can be applied as a lightweight post-training stage to any existing VLM. Experiments on video and spatial reasoning benchmarks demonstrate consistent improvements over strong baselines and enhanced generalization to unseen data.
匹配关键词: self-consistency
---

[ACADEMIC - ARXIV]
标题: Generative AI and the Productivity Divide: Human-AI Complementarities in Education
作者: Lihi Idan, Bharat Anand
链接: https://arxiv.org/abs/2605.18143v1
完整摘要: Generative Artificial Intelligence (GenAI) is transforming how firms create, process, and apply knowledge, yet little is known about the heterogeneity of its productivity effects across users. We report results from a randomized controlled experiment in which participants-analogs of early-career knowledge workers-were assigned to self-study a technical domain using either traditional resources or large-language-model (LLM) assistance. On average, GenAI access significantly increased task performance, but the distribution of gains was highly uneven. Improvements were not predicted by GPA or prior knowledge, but by \textit{AI Interaction Competence (AIC)} -- the ability to elicit, filter, and verify model outputs. High-AIC participants realized outsized gains; low-AIC participants saw limited or even negative marginal returns. A scaffolding intervention (conceptual maps) reduced outcome variance, indicating that standardized workflows can mitigate inequality in AI-mediated performance. We interpret these findings through the lens of human-AI complementarities: GenAI raises mean productivity while introducing a new axis of capability inequality. Managerially, firms should pair GenAI access with short AIC micro-training and simple standard operating procedures to capture value consistently and avoid uneven adoption outcomes.
匹配关键词: self-consistency
---

[ACADEMIC - ARXIV]
标题: Safety Geometry Collapse in Multimodal LLMs and Adaptive Drift Correction
作者: Jiahe Guo, Xiangran Guo, Jiaxuan Chen, Weixiang Zhao, Yanyan Zhao, Yutai Hou, Qianchao Wang, Dandan Tu, Bing Qin
链接: https://arxiv.org/abs/2605.18104v1
完整摘要: Multimodal large language models (MLLMs) often fail to transfer safety capabilities learned in the text modality to semantically equivalent non-text inputs, revealing a persistent multimodal safety gap. We study this gap from a representation-geometric perspective by analyzing a text-aligned refusal direction and a modality-induced drift direction. We show that multimodal inputs compress the usable separation along the refusal direction, making it no longer reliable for identifying and refusing harmful inputs. We refer to this failure mode as Safety Geometry Collapse. We quantify it through conditional refusal separability and show that stronger modality-induced drift is consistently associated with weaker refusal separability and higher attack success rates. We then validate the causal role of modality-induced drift through a fixed-strength activation intervention: counteracting the estimated drift restores refusal separability and improves multimodal safety. After drift correction, we further observe self-rectification, where the model recovers its ability to recognize and refuse harmful multimodal inputs during forward dynamics. This effect also provides an internal signal of the model's perceived harmfulness of each input. Motivated by this signal, we propose ReGap, a training-free inference-time method that adaptively corrects modality drift using self-rectification. Experiments across multiple multimodal safety benchmarks and utility benchmarks demonstrate the effectiveness of ReGap, which significantly improves the safety of MLLMs without compromising general capabilities. Our findings highlight representation-level modality alignment as a crucial direction for real-time safety improvement and for building safer, more reliable MLLMs.
匹配关键词: self-consistency
---

[ACADEMIC - ARXIV]
标题: Function graph transformers universally approximate operators between function spaces
作者: Takashi Furuya, David Mis, Ivan Dokmanić, Maarten V. de Hoop, Matti Lassas
链接: https://arxiv.org/abs/2605.17968v1
完整摘要: We study the approximation of nonlinear operators between function spaces by transformers. Our approach is to lift functions to measures supported on their graphs and leverage a recently introduced measure-theoretic view of transformers. A function $h$ is represented by its graph measure $γ_h$, with finite tokens $\{(x_j,h(x_j))\}_{j=1}^N$ being its empirical approximations. We show that this framework elegantly models discretization refinement via convergence of measures and provides a natural setting for operator learning. Within this framework, we introduce function graph transformers, a graph-preserving subclass of measure-theoretic transformers that maps graph measures to graph measures, which is to say that outputs remain single-valued functions. Crucially, this additional structure does not reduce generality: we prove that the resulting graph-preserving maps can be approximated by finite compositions of standard softmax self-attention layers and pointwise MLPs, yielding universal approximation results for broad classes of nonlinear operators. Unlike existing theoretical approaches to operator learning with transformers, the measure-theoretic framework also accommodates regularized negative-order Sobolev inputs for which discretization invariance is particularly challenging, as well as query points on different output domains. Overall, function graph transformers provide a continuum viewpoint and mathematical toolkit for transformer-based operator learning, clarifying the roles of positional encodings, graph structure, regularization, and ensuring consistency across discretizations.
匹配关键词: self-consistency
---

[ACADEMIC - ARXIV]
标题: AtlasVA: Self-Evolving Visual Skill Memory for Teacher-Free VLM Agents
作者: Pan Wang, Yihao Hu, Xiujin Liu, Jingchu Yang, Hang Wang, Zhihao Wen
链接: https://arxiv.org/abs/2605.17933v1
完整摘要: Vision-language model (VLM) agents increasingly rely on memory-augmented reinforcement learning to reuse experience across long-horizon tasks, yet most existing frameworks store memory as text and depend on proprietary teacher models to summarize or refine it. This design is poorly matched to spatial decision making: geometric priors are compressed into lossy language, and sparse interaction is often supervised through delayed textual feedback rather than dense visually grounded signals. We argue that reusable experience for VLM agents should remain visually grounded. Based on this insight, we propose \textbf{AtlasVA}, a teacher-free visual skill memory framework that organizes memory into three complementary layers: spatial heatmaps, visual exemplars, and symbolic text skills. AtlasVA further evolves danger and affinity atlases directly from trajectory statistics and lightweight grid heuristics, and reuses these self-evolving atlases as potential-based shaping rewards for reinforcement learning. This unifies perception, memory, and optimization without external LLM supervision. Experiments on \textsc{Sokoban}, \textsc{FrozenLake}, 3D embodied navigation, and 3D robotic manipulation benchmarks show that AtlasVA consistently outperforms text-centric memory baselines and competitive VLM agents, with especially strong gains on spatially intensive tasks. Homepage: https://wangpan-ustc.github.io/AtlasvaWeb
匹配关键词: self-consistency
---

[ACADEMIC - ARXIV]
标题: Contextual Biasing for Streaming ASR via CTC-based Word Spotting
作者: Kai-Chen Tsai, Tien-Hong Lo, Yun-Ting Sun, Berlin Chen
链接: https://arxiv.org/abs/2605.18222v1
完整摘要: Contextual biasing is essential to improving the recognition of rare and domain-specific words in an automatic speech recognition (ASR) system. While numerous methods have been proposed in recent years, most of them focus on offline settings and do not explicitly address the challenges of streaming ASR. For example, CTC-based word spotting (CTC-WS) have demonstrated strong performance by directly detecting keywords from CTC log-probabilities, but they are limited to offline processing and require access to the full utterance. In This work, we present a streaming extension of CTC-WS for real-time contextual biasing. Our method maintains active keyword paths across audio chunks using a stateful token passing algorithm, enabling the detection of keywords that span multiple chunks. To ensure low latency and stable output, we introduce an incremental commitment mechanism that only emits segments guaranteed not to be affected by future audio, while deferring uncertain regions. This method naturally integrates with streaming ASR pipelines and does not require modifications to the underlying acoustic model or additional training, making it practical for real-world deployment. Experimental results show that our method reduces overall WER and effectively improves keyword F-score, demonstrating its effectiveness for real-time ASR applications.
匹配关键词: process reward
---

[ACADEMIC - ARXIV]
标题: Forward-Learned Discrete Diffusion: Learning how to noise to denoise faster
作者: Grigory Bartosh, Teodora Pandeva, Sushrut Karmalkar, Javier Zazo
链接: https://arxiv.org/abs/2605.18204v1
完整摘要: Discrete diffusion models are a powerful class of generative models with strong performance across many domains. For efficiency, however, discrete diffusion typically parameterizes the generative (reverse) process with factorized distributions, which makes it difficult for the model to learn the target process in a small number of steps and necessitates a long, computationally expensive sampling procedure. To reduce the gap between the target and model distributions and enable few-step generation, we propose Forward-Learned Discrete Diffusion (FLDD), which introduces discrete diffusion with a learnable forward (noising) process. Rather than fixing a Markovian forward chain, we adopt a non-Markovian formulation with learnable marginal and posterior distributions. This allows the generative process to remain factorized while matching the target defined by the noising process. We train all parameters end-to-end under the standard variational objective. Experiments on various benchmarks show that, for a given number of sampling steps, our approach produces a higher quality samples than conventional discrete diffusion models using the same reverse parameterization.
匹配关键词: process reward
---

[ACADEMIC - ARXIV]
标题: Best Segmentation Buddies for Image-Shape Correspondence
作者: Itai Lang, Dongwei Lyu, Dale Decatur, Rana Hanocka
链接: https://arxiv.org/abs/2605.18193v1
完整摘要: Finding correspondences is a fundamental and extensively researched problem in computer vision and graphics. In this work, we examine the underexplored task of estimating segmentation-to-segmentation correspondence between images in the wild and untextured 3D shapes. This task is highly challenging due to substantial differences in appearance, geometry, and viewpoint. Our approach bridges the cross-modality gap by linking pixels in the image segment to vertices in the corresponding semantic part of the 3D shape. To achieve this, we first distill deep visual features from a 2D vision model onto the 3D shape surface, allowing for the computation of feature similarity between image pixels and shape vertices. Then, we identify Best Segmentation Buddies, vertices whose most similar image pixel lies within the image segmentation region, enabling the reliable discovery of vertices in semantically corresponding shape parts. Finally, we leverage distilled 3D features from the 2D image segmentation model to segment the shape directly in 3D, bootstrapping the correspondence process. We demonstrate the generality and robustness of our approach across a wide range of image-shape pairs, showcasing accurate and semantically meaningful correspondences. Our project page is at https://threedle.github.io/bsb/.
匹配关键词: process reward
---

[ACADEMIC - ARXIV]
标题: Pairwise Preference Reward and Group-Based Diversity Enhancement for Superior Open-Ended Generation
作者: Guining Cao, Jiaxin Peng, Chu Zeng, Yu Zhao, Shuangyong Song, Yongxiang
链接: https://arxiv.org/abs/2605.18191v1
完整摘要: Current reinforcement learning(RL) methods are broadly applicable and powerful in verifiable settings where scalar rewards can be provided. However, in open-ended generation tasks, verifying the correctness of responses remains challenging, and training reward models incurs substantial computational and annotation costs. Moreover, reinforcement learning (RLVR) often leads to diversity collapse and produces stereotypical or rigid outputs, outcomes that are particularly undesirable in open-domain scenarios. We propose Pairwise Preference Reward and Group-based Diversity Enhancement (PPR-GDE), a RL method that is more suitable for open-ended generation. PPR-GDE does not require scalar rewards and incorporates group-level diversity into the reward signal, it preserves the comparative structure of subjective evaluation through a pairwise preference reward, mitigates judge position bias via repeated comparisons with swapped response order, and introduces a group-based diversity reward that explicitly encourages semantic dispersion within a response group, all of these reward signals are integrated into a unified group-relative policy optimization objective. We instantiate PPR-GDE on role-playing task, experiments show that PPR-GDE achieves a better alignment quality as well as expressive diversity than strong RL baselines. Further analysis shows that pairwise preference is critical for preference alignment in subjective perspective, while the diversity metric plays an essential role in achieving superior expressive diversity and broader semantic coverage.
匹配关键词: process reward
---

[ACADEMIC - ARXIV]
标题: UTOPYA: A Multimodal Deep Learning Framework for Physics-Informed Anomaly Detection and Time-Series Prediction
作者: Robson W. S. Pessoa, Julien Amblard, Alessandra Russo, Idelfonso B. R. Nogueira
链接: https://arxiv.org/abs/2605.18188v1
完整摘要: Anomaly detection in batch processes is hindered by transient dynamics, scarce fault labels, and reliance on single-modality sensor data. This work introduces UTOPYA (Unified Temporal Observation for Physics-Informed Anomaly Detection and Time-Series Prediction), a 15.2M-parameter multimodal framework that jointly addresses anomaly detection, time-series prediction, and phase classification in batch distillation by fusing eight data modalities through Feature-wise Linear Modulation (FiLM) conditioned cross-modal attention and gated fusion. A physics-informed regularisation scheme introduced in this work enforces temporal smoothness and thermodynamic monotonicity, while curriculum learning introduces training samples in order of physical difficulty. On the 119-experiment multimodal batch distillation dataset of Arweiler et al. (2026), UTOPYA achieves a window-level test AUROC of 0.832 and 0.874 under multi-signal experiment-level scoring, substantially outperforming four external baselines (PCA, autoencoder, Isolation Forest, and LSTM autoencoder) evaluated under identical conditions (+0.147 window-level AUROC over the best baseline). A multimodal ablation over 15~architectural configurations shows that static context via FiLM conditioning is the key enabler, lifting experiment-level multi-signal AUROC by +0.145 over the unimodal baseline (0.729 to 0.874). Separately, a training ablation across 14 design choices reveals that several widely-adopted techniques, including instance normalisation, Mixup, ensembling, test-time augmentation, and stochastic weight averaging, fail to improve or actively degrade generalisation in this data-scarce setting. These negative results expose a fundamental tension between smoothing-based regularisation and anomaly detection, providing practical guidance for multimodal process monitoring deployment.
匹配关键词: process reward
---

[ACADEMIC - ARXIV]
标题: Canonical Regularisation of Wide Feature-Learning Neural Networks
作者: George Whittle, Pranav Vaidhyanathan, Juliusz Ziomek, Natalia Ares, Maike A. Osborne
链接: https://arxiv.org/abs/2605.18180v1
完整摘要: Wide neural networks in the feature-learning regime drive modern deep learning, and yet they remain far less studied than their kernel-regime counterparts. We consider a critical yet under-explored difference between these two regimes: the regulariser and prior implied by gradient flow training. This canonical regularisation property is well-studied in kernel regime networks -- of all the infinite global minima, gradient flow selects exactly the vanishing ridge solution -- and underpins the celebrated NN-GP correspondence, precisely allowing the modelling of noise during training. However, we prove ridge regularisation biases gradient flow in feature-learning regime networks, even in the infinitesimal limit of vanishing regularisation. Over training, ridge distorts the inductive bias of the network, with a particular damage done to pretrained networks where the implicit prior is informative. We resolve this by axiomatising the canonical regulariser as a regime-agnostic function-space energy and lift, which uniquely identifies ridge in the kernel regime, and crucially generalises to the feature-learning regime. By studying the Riemannian geometry of feature-learning networks, we derive geodesic ridge from our framework, generalising ridge to the feature-learning regime. Correspondingly, we prove the canonical function-space prior is a Riemannian Gibbs Process, generalising the more familiar Gaussian Process. As a practical contribution, we propose arc ridge as a minimax-robust, scalable surrogate to geodesic ridge, revealing a deep relationship between early stopping and canonical regularisation across learning regimes. Finally, we demonstrate the consequences of our theory empirically on both image processing and NLP transfer-learning problems.
匹配关键词: pretraining
---

[ACADEMIC - ARXIV]
标题: Ringmaster LMO: Asynchronous Linear Minimization Oracle Momentum Method
作者: Abdurakhmon Sadiev, Artavazd Maranjyan, Ivan Ilin, Peter Richtárik
链接: https://arxiv.org/abs/2605.18174v1
完整摘要: Muon has recently emerged as a strong alternative to AdamW for training neural networks, with encouraging large-scale pretraining results and growing evidence that matrix-structured updates can be faster in practice. Yet Muon, and more generally Linear Minimization Oracle (LMO) based methods, are typically used synchronously. This is problematic in heterogeneous distributed systems, where workers complete gradient computations at different speeds and synchronous training must repeatedly wait for slower workers. In this work, we introduce Ringmaster LMO, an asynchronous LMO-based momentum method for unconstrained stochastic nonconvex optimization. Our method builds on the delay-thresholding idea of Ringmaster ASGD. For SGD-type methods, Ringmaster ASGD achieves optimal time complexity by discarding overly stale gradients. Ringmaster LMO extends this mechanism to general LMO-based updates. We establish convergence guarantees under generalized $(L_0, L_1)$-smoothness and further develop a parameter-agnostic variant with decreasing stepsizes and adaptive delay thresholds. Finally, we translate our iteration guarantees into time complexity bounds under heterogeneous worker computation times. In the classical Euclidean smooth setting, these bounds recover the optimal time complexity of Ringmaster ASGD. Experiments on stochastic quadratic problems and NanoChat language-model pretraining show that the advantages of Ringmaster LMO grow with system heterogeneity and that the method outperforms strong synchronous and asynchronous baselines.
匹配关键词: pretraining
---

[ACADEMIC - ARXIV]
标题: TRACE: Trajectory Correction from Cross-layer Evidence for Hallucination Reduction
作者: Tej Sanibh Ranade
链接: https://arxiv.org/abs/2605.18163v1
完整摘要: Hallucination correction is not a one-direction problem. We show that intermediate layers are neither uniformly more truthful than final layers nor uniformly less trustworthy. Yet hallucination reduction is usually instantiated through one fixed intervention form: contrast one layer against another, steer along a truthfulness direction, or defer to external evidence. This framing is structurally incomplete. Cross-layer factual evidence does not evolve uniformly: in some failures truthful support is present internally and later suppressed, whereas in others candidate competition remains genuinely multi-directional across depth, so no single signed scalar family is generally sufficient. We introduce Trajectory Correction from Cross-layer Evidence for Hallucination Reduction (TRACE), a deterministic, training-free algorithm which corrects hallucinations at inference time by deriving both the corrective layer and the appropriate correction operator from each input's cross-layer candidate trajectory inside the LLM's own forward pass. Under one frozen hyperparameter setting, TRACE selects among scalar reversal, earlier-state recovery, and candidate-space correction using only model-internal evidence. Evaluated as a single universal algorithm across 15 models, 8 model families, and 3 factuality benchmarks, TRACE improves every evaluation cell, yielding mean gains of +12.26 MC1 points and +8.65 MC2-style points with no regressions, with gains reaching +47.20 MC1 and +43.38 MC2-style points. The method uses no labels, retrieval, pretraining, finetuning, or per-model calibration.
匹配关键词: pretraining
---

[ACADEMIC - ARXIV]
标题: Whispers in the Noise: Surrogate-Guided Concept Awakening via a Multi-Agent Framework
作者: Mengyu Sun, Ziyuan Yang, Zunlong Zhou, Junxu Liu, Haibo Hu, Yi Zhang
链接: https://arxiv.org/abs/2605.18150v1
完整摘要: Diffusion models (DMs) are widely used for text-to-image generation, but their strong generative capabilities also raise concerns about unsafe or undesirable content. Concept erasure aims to mitigate these risks by removing specific concepts from pretrained models. However, recent studies show that such methods often suppress rather than fully eliminate target concepts, leaving models vulnerable to awakening attacks. Existing approaches primarily rely on white-box access through optimization or inversion, while concept awakening under black-box constraints remains underexplored. In this work, we revisit the denoising process from a trajectory perspective and show that concept erasure mainly disrupts early-stage text-semantic alignment but does not fully prevent semantic information from propagating along the denoising dynamics. As generation proceeds, the model increasingly depends on the evolving noisy state rather than textual conditions, which creates an opportunity to bypass erased mappings. Motivated by this observation, we propose ConceptAgent, a training-free, black-box, multi-agent framework that awakens erased concepts by initializing the denoising trajectory from surrogate-guided noisy states. Extensive experiments demonstrate that ConceptAgent enables accurate and controllable awakening of erased concepts under black-box settings without access to model parameters, gradients, or internal representations. These results highlight fundamental limitations of current concept erasure methods and provide new insights into the dynamic nature of semantic control in DMs.
匹配关键词: pretraining
---

[ACADEMIC - ARXIV]
标题: Foundation Models for Credit Risk Prediction: A Game Changer?
作者: Bart Baesens, Andreas Goethals, Stefan Lessmann, Simon De Vos, Cristián Bravo, David Martens, Victor Medina-Olivares, Christophe Mues, Maria Oskarsdóttir, Seppe vanden Broucke, Tim Verdonck, Wouter Verbeke
链接: https://arxiv.org/abs/2605.18147v1
完整摘要: Predictive models play a pivotal role in credit risk management, guiding critical decisions through accurate estimation of default probabilities and losses. Extensive research has introduced new modeling techniques, complemented by large-scale benchmarking studies consolidating the state-of-the-art. Today, quasi-standards such as gradient-boosting models paired with SHAP explainers have emerged, yet continuous improvement of risk models remains a top priority. Concurrently, rapid advancements in AI, most notably large language models, have disrupted predictive modeling paradigms. Foundation models, pretrained on extensive datasets from diverse domains, have demonstrated remarkable performance by leveraging prior knowledge. While prevalent in natural language processing and computer vision, foundation models for tabular data have only recently emerged. We conjecture that pretraining on out-of-domain data is particularly beneficial in small-data settings, such as SME lending or specialized corporate portfolios, and may help address longstanding challenges including low default portfolios and class imbalance. This paper benchmarks recently proposed tabular foundation models against a broad set of competitors, including established and advanced machine learning techniques, across two core tasks: PD and LGD modeling. Our evaluation encompasses various datasets, performance indicators, and experimental conditions. We find that tabular foundation models generally perform best across datasets and tasks. Moreover, they offer significant improvement in predictive performance as dataset size shrinks. These results are remarkable given that the models are tested out-of-the-box, without hyperparameter tuning, ensuring ease of use and mitigating computational costs.
匹配关键词: pretraining
---

[ACADEMIC - ARXIV]
标题: Are Sparse Autoencoder Benchmarks Reliable?
作者: David Chanin
链接: https://arxiv.org/abs/2605.18229v1
完整摘要: Sparse autoencoders (SAEs) are a core interpretability tool for large language models, and progress on SAE architectures depends on benchmarks that reliably distinguish better SAEs from worse ones. We audit the SAE quality metrics in SAEBench, the de-facto standard SAE evaluation suite, through three complementary lenses: reseed noise on a fixed SAE, ground-truth correlation on synthetic SAEs, and discriminability across training trajectories. We find that two of these metrics, Targeted Probe Perturbation (TPP) and Spurious Correlation Removal (SCR), fail multiple lenses at their canonical settings and should not be used to evaluate SAEs. The other metrics show higher reseed noise and lower discriminability than the field assumes. The sae-probes variant of $k$-sparse probing is the most reliable metric we tested, but even sae-probes struggles to separate variants of the same SAE architecture. Our results show the field needs better SAE benchmarks.
匹配关键词: foundation model
---

[ACADEMIC - ARXIV]
标题: Context Memorization for Efficient Long Context Generation
作者: Yasuyuki Okoshi, Hao Mark Chen, Guanxi Lu, Hongxiang Fan, Masato Motomura, Daichi Fujiki
链接: https://arxiv.org/abs/2605.18226v1
完整摘要: Modern large language model (LLM) applications increasingly rely on long conditioning prefixes to control model behavior at inference time. While prefix-augmented inference is effective, it incurs two structural limitations: i) the prefix's influence fades as generation proceeds, and ii) attention computation over the prefix scales linearly with its length. Existing approaches either keep the prefix in attention while compressing it, or internalize it into model parameters through gradient-based training. The former still attends to the prefix at inference, while the latter is training-intensive and ill-suited to prefix updates. To address these issues, we propose attention-state memory, a training-free approach that externalizes the prefix into a lightweight, lookup-based memory of precomputed attention states between prefix and query tokens. On ManyICLBench with LLaMA-3.1-8B, our method improves accuracy over in-context learning at 1K-8K memory budgets while reducing attention latency by 1.36x at 8K, and surpasses full-attention RAG performance on NBA benchmark using only 20% of its memory footprint.
匹配关键词: foundation model
---

[ACADEMIC - ARXIV]
标题: Contextual Biasing for Streaming ASR via CTC-based Word Spotting
作者: Kai-Chen Tsai, Tien-Hong Lo, Yun-Ting Sun, Berlin Chen
链接: https://arxiv.org/abs/2605.18222v1
完整摘要: Contextual biasing is essential to improving the recognition of rare and domain-specific words in an automatic speech recognition (ASR) system. While numerous methods have been proposed in recent years, most of them focus on offline settings and do not explicitly address the challenges of streaming ASR. For example, CTC-based word spotting (CTC-WS) have demonstrated strong performance by directly detecting keywords from CTC log-probabilities, but they are limited to offline processing and require access to the full utterance. In This work, we present a streaming extension of CTC-WS for real-time contextual biasing. Our method maintains active keyword paths across audio chunks using a stateful token passing algorithm, enabling the detection of keywords that span multiple chunks. To ensure low latency and stable output, we introduce an incremental commitment mechanism that only emits segments guaranteed not to be affected by future audio, while deferring uncertain regions. This method naturally integrates with streaming ASR pipelines and does not require modifications to the underlying acoustic model or additional training, making it practical for real-world deployment. Experimental results show that our method reduces overall WER and effectively improves keyword F-score, demonstrating its effectiveness for real-time ASR applications.
匹配关键词: foundation model
---

[ACADEMIC - ARXIV]
标题: SIREM: Speech-Informed MRI Reconstruction with Learned Sampling
作者: Md Hasan, Nyvenn Castro, Daiqi Liu, Lukas Mulzer, Jana Hutter, Jonghye Woo, Moritz Zaiss, Andreas Maier, Paula A. Perez-Toro
链接: https://arxiv.org/abs/2605.18221v1
完整摘要: Real-time magnetic resonance imaging (rtMRI) of speech production enables non-invasive visualization of dynamic vocal-tract motion and is valuable for speech science and clinical assessment. However, rtMRI is fundamentally constrained by trade-offs among spatial resolution, temporal resolution, and acquisition speed, often leading to undersampled k-space measurements and degraded reconstructions. We propose SIREM, a speech-informed MRI reconstruction framework that uses synchronized speech as a cross-modal prior. The central idea is that vocal-tract configurations during speech are correlated with the produced acoustics, making part of the image content predictable from audio. SIREM models each frame as a fusion of an audio-driven component and an MRI-driven component through a spatial weighting map. The audio branch predicts articulator-related structure from speech, while the MRI branch reconstructs complementary content from measured k-space data. We further introduce a learnable soft weighting profile over spiral arms, enabling a differentiable study of how k-space arm usage interacts with speech-informed fusion. This yields a unified multimodal formulation that combines audio-driven prediction, MRI reconstruction, and sampling adaptation. We evaluate SIREM on the USC speech rtMRI benchmark against standard baselines, including gridding, wavelet-based compressed sensing, and total variation. SIREM introduces a speech-informed reconstruction paradigm that operates in a substantially higher-throughput regime than iterative methods while preserving anatomically plausible vocal-tract structure. These results establish an initial benchmark for multimodal speech-informed rtMRI reconstruction and highlight the potential of synchronized speech as an auxiliary prior for fast reconstruction. The source code is available at https://github.com/mdhasanai/SIREM
匹配关键词: foundation model
---

[ACADEMIC - ARXIV]
标题: EgoInteract: Synthetic Egocentric Videos Generation for Interaction Understanding and Anticipation
作者: Rosario Leonardi, Francesco Ragusa, Daniele Materia, Alessandro Passanisi, James Fort, Jakob Engel, Giovanni Maria Farinella
链接: https://arxiv.org/abs/2605.18214v1
完整摘要: Collecting large-scale egocentric video datasets with dense spatial and temporal annotations is costly, slow, and often constrained by environmental biases, privacy constraints, and limited coverage of interaction patterns. While synthetic data has shown strong potential in several vision domains, its use for egocentric perception remains relatively underexplored, especially for tasks requiring temporally coherent human-object interactions. In this work, we introduce EgoInteract, a controllable simulator for egocentric video generation designed to model fine-grained egocentric interactions and their temporal dynamics. The simulator enables precise control over camera, human body and hand motion, object manipulation, and scene composition across diverse environments. Building on this framework, we generate a synthetic egocentric video dataset with dense spatial and temporal annotations for temporal action segmentation, next-active object detection, interaction anticipation, and hand-object interaction detection. We evaluate models trained with simulated data on multiple real-world egocentric benchmarks spanning diverse environments, object categories, and interaction patterns. Results show consistent improvements over strong baselines across tasks and datasets, demonstrating the effectiveness and transferability of our simulation-based approach.
匹配关键词: foundation model
---

[ACADEMIC - ARXIV]
标题: Context Memorization for Efficient Long Context Generation
作者: Yasuyuki Okoshi, Hao Mark Chen, Guanxi Lu, Hongxiang Fan, Masato Motomura, Daichi Fujiki
链接: https://arxiv.org/abs/2605.18226v1
完整摘要: Modern large language model (LLM) applications increasingly rely on long conditioning prefixes to control model behavior at inference time. While prefix-augmented inference is effective, it incurs two structural limitations: i) the prefix's influence fades as generation proceeds, and ii) attention computation over the prefix scales linearly with its length. Existing approaches either keep the prefix in attention while compressing it, or internalize it into model parameters through gradient-based training. The former still attends to the prefix at inference, while the latter is training-intensive and ill-suited to prefix updates. To address these issues, we propose attention-state memory, a training-free approach that externalizes the prefix into a lightweight, lookup-based memory of precomputed attention states between prefix and query tokens. On ManyICLBench with LLaMA-3.1-8B, our method improves accuracy over in-context learning at 1K-8K memory budgets while reducing attention latency by 1.36x at 8K, and surpasses full-attention RAG performance on NBA benchmark using only 20% of its memory footprint.
匹配关键词: scaling law
---

[ACADEMIC - ARXIV]
标题: EgoInteract: Synthetic Egocentric Videos Generation for Interaction Understanding and Anticipation
作者: Rosario Leonardi, Francesco Ragusa, Daniele Materia, Alessandro Passanisi, James Fort, Jakob Engel, Giovanni Maria Farinella
链接: https://arxiv.org/abs/2605.18214v1
完整摘要: Collecting large-scale egocentric video datasets with dense spatial and temporal annotations is costly, slow, and often constrained by environmental biases, privacy constraints, and limited coverage of interaction patterns. While synthetic data has shown strong potential in several vision domains, its use for egocentric perception remains relatively underexplored, especially for tasks requiring temporally coherent human-object interactions. In this work, we introduce EgoInteract, a controllable simulator for egocentric video generation designed to model fine-grained egocentric interactions and their temporal dynamics. The simulator enables precise control over camera, human body and hand motion, object manipulation, and scene composition across diverse environments. Building on this framework, we generate a synthetic egocentric video dataset with dense spatial and temporal annotations for temporal action segmentation, next-active object detection, interaction anticipation, and hand-object interaction detection. We evaluate models trained with simulated data on multiple real-world egocentric benchmarks spanning diverse environments, object categories, and interaction patterns. Results show consistent improvements over strong baselines across tasks and datasets, demonstrating the effectiveness and transferability of our simulation-based approach.
匹配关键词: scaling law
---

[ACADEMIC - ARXIV]
标题: Scalable Environments Drive Generalizable Agents
作者: Jiayi Zhang, Fanqi Kong, Guibin Zhang, Maojia Song, Zhaoyang Yu, Jianhao Ruan, Jinyu Xiang, Bang Liu, Chenglin Wu, Yuyu Luo
链接: https://arxiv.org/abs/2605.18181v1
完整摘要: Generalizable agents should adapt to diverse tasks and unseen environments beyond their training distribution. This position paper argues that such generalization requires environment scaling: expanding the distribution of executable rule-sets that agents interact with, rather than only increasing trajectories or tasks within fixed benchmarks. Current scaling practices largely focus on collecting more experience or broader task sets under fixed interaction rules, leaving agents brittle when underlying interfaces, dynamics, observations, or feedback signals change. The core challenge is therefore a world-level distribution shift: agents need systematic exposure to environments with meaningfully different executable rule-sets. To clarify this challenge, we propose a unified taxonomy that separates trajectory scaling, task scaling, and environment scaling by their primary deliverables and by what changes in the executable rule-set. Building on this taxonomy, we synthesize construction paradigms for scalable environments, contrasting programmatic generators that prioritize controllability and verifiability with generative world models that offer broader coverage and open-endedness. We further outline how environment scaling can be coupled with stateful learning mechanisms, emphasizing learned update rules for cross-environment adaptation. We conclude by discussing alternative perspectives and argue that scalable environments provide the essential substrate for measurable and controllable progress toward robust general agents.
匹配关键词: scaling law
---

[ACADEMIC - ARXIV]
标题: Ringmaster LMO: Asynchronous Linear Minimization Oracle Momentum Method
作者: Abdurakhmon Sadiev, Artavazd Maranjyan, Ivan Ilin, Peter Richtárik
链接: https://arxiv.org/abs/2605.18174v1
完整摘要: Muon has recently emerged as a strong alternative to AdamW for training neural networks, with encouraging large-scale pretraining results and growing evidence that matrix-structured updates can be faster in practice. Yet Muon, and more generally Linear Minimization Oracle (LMO) based methods, are typically used synchronously. This is problematic in heterogeneous distributed systems, where workers complete gradient computations at different speeds and synchronous training must repeatedly wait for slower workers. In this work, we introduce Ringmaster LMO, an asynchronous LMO-based momentum method for unconstrained stochastic nonconvex optimization. Our method builds on the delay-thresholding idea of Ringmaster ASGD. For SGD-type methods, Ringmaster ASGD achieves optimal time complexity by discarding overly stale gradients. Ringmaster LMO extends this mechanism to general LMO-based updates. We establish convergence guarantees under generalized $(L_0, L_1)$-smoothness and further develop a parameter-agnostic variant with decreasing stepsizes and adaptive delay thresholds. Finally, we translate our iteration guarantees into time complexity bounds under heterogeneous worker computation times. In the classical Euclidean smooth setting, these bounds recover the optimal time complexity of Ringmaster ASGD. Experiments on stochastic quadratic problems and NanoChat language-model pretraining show that the advantages of Ringmaster LMO grow with system heterogeneity and that the method outperforms strong synchronous and asynchronous baselines.
匹配关键词: scaling law
---

[ACADEMIC - ARXIV]
标题: Do You Need Text Rectification? Soft Attention Mask Embedding for Rectification-Free Scene Text Spotting
作者: Antonio Colombo, Giovanni Bianchi
链接: https://arxiv.org/abs/2605.18173v1
完整摘要: End-to-end scene text spotting, which unifies text detection and recognition within a single framework, has witnessed remarkable progress driven by deep learning advances. However, most existing approaches still suffer from incomplete mask proposals caused by multi-scale variation, arbitrary text shapes, and complex background interference, thereby degrading recognition accuracy. In this paper, we propose a novel Soft Attention Mask Embedding module (SAME) that leverages the global receptive field of Transformer encoders to encode high-level features and compute soft attention weights, which are then hierarchically embedded with predicted masks to generate refined text-boundary-aware masks that effectively suppress background noise. Building upon this module, we present SAME-Net, a robust end-to-end text spotting framework that requires neither character-level annotations nor auxiliary text rectification modules. Since the soft attention mechanism is fully differentiable, recognition loss gradients can be back-propagated through the SAME module to the detection branch, enabling joint optimization of detection and recognition objectives. Extensive experiments on challenging benchmarks demonstrate the effectiveness of our approach: SAME-Net achieves 84.02\% end-to-end H-mean on the arbitrarily-shaped Total-Text dataset, surpassing the previous state-of-the-art GLASS by 1.02\% in full-lexicon accuracy without additional training data, and obtains competitive 83.4\% strong-lexicon results on the multi-oriented ICDAR 2015 dataset.
匹配关键词: scaling law
---

[ACADEMIC - ARXIV]
标题: Are Sparse Autoencoder Benchmarks Reliable?
作者: David Chanin
链接: https://arxiv.org/abs/2605.18229v1
完整摘要: Sparse autoencoders (SAEs) are a core interpretability tool for large language models, and progress on SAE architectures depends on benchmarks that reliably distinguish better SAEs from worse ones. We audit the SAE quality metrics in SAEBench, the de-facto standard SAE evaluation suite, through three complementary lenses: reseed noise on a fixed SAE, ground-truth correlation on synthetic SAEs, and discriminability across training trajectories. We find that two of these metrics, Targeted Probe Perturbation (TPP) and Spurious Correlation Removal (SCR), fail multiple lenses at their canonical settings and should not be used to evaluate SAEs. The other metrics show higher reseed noise and lower discriminability than the field assumes. The sae-probes variant of $k$-sparse probing is the most reliable metric we tested, but even sae-probes struggles to separate variants of the same SAE architecture. Our results show the field needs better SAE benchmarks.
匹配关键词: language model
---

[ACADEMIC - ARXIV]
标题: Context Memorization for Efficient Long Context Generation
作者: Yasuyuki Okoshi, Hao Mark Chen, Guanxi Lu, Hongxiang Fan, Masato Motomura, Daichi Fujiki
链接: https://arxiv.org/abs/2605.18226v1
完整摘要: Modern large language model (LLM) applications increasingly rely on long conditioning prefixes to control model behavior at inference time. While prefix-augmented inference is effective, it incurs two structural limitations: i) the prefix's influence fades as generation proceeds, and ii) attention computation over the prefix scales linearly with its length. Existing approaches either keep the prefix in attention while compressing it, or internalize it into model parameters through gradient-based training. The former still attends to the prefix at inference, while the latter is training-intensive and ill-suited to prefix updates. To address these issues, we propose attention-state memory, a training-free approach that externalizes the prefix into a lightweight, lookup-based memory of precomputed attention states between prefix and query tokens. On ManyICLBench with LLaMA-3.1-8B, our method improves accuracy over in-context learning at 1K-8K memory budgets while reducing attention latency by 1.36x at 8K, and surpasses full-attention RAG performance on NBA benchmark using only 20% of its memory footprint.
匹配关键词: language model
---

[ACADEMIC - ARXIV]
标题: Contextual Biasing for Streaming ASR via CTC-based Word Spotting
作者: Kai-Chen Tsai, Tien-Hong Lo, Yun-Ting Sun, Berlin Chen
链接: https://arxiv.org/abs/2605.18222v1
完整摘要: Contextual biasing is essential to improving the recognition of rare and domain-specific words in an automatic speech recognition (ASR) system. While numerous methods have been proposed in recent years, most of them focus on offline settings and do not explicitly address the challenges of streaming ASR. For example, CTC-based word spotting (CTC-WS) have demonstrated strong performance by directly detecting keywords from CTC log-probabilities, but they are limited to offline processing and require access to the full utterance. In This work, we present a streaming extension of CTC-WS for real-time contextual biasing. Our method maintains active keyword paths across audio chunks using a stateful token passing algorithm, enabling the detection of keywords that span multiple chunks. To ensure low latency and stable output, we introduce an incremental commitment mechanism that only emits segments guaranteed not to be affected by future audio, while deferring uncertain regions. This method naturally integrates with streaming ASR pipelines and does not require modifications to the underlying acoustic model or additional training, making it practical for real-world deployment. Experimental results show that our method reduces overall WER and effectively improves keyword F-score, demonstrating its effectiveness for real-time ASR applications.
匹配关键词: language model
---

[ACADEMIC - ARXIV]
标题: SIREM: Speech-Informed MRI Reconstruction with Learned Sampling
作者: Md Hasan, Nyvenn Castro, Daiqi Liu, Lukas Mulzer, Jana Hutter, Jonghye Woo, Moritz Zaiss, Andreas Maier, Paula A. Perez-Toro
链接: https://arxiv.org/abs/2605.18221v1
完整摘要: Real-time magnetic resonance imaging (rtMRI) of speech production enables non-invasive visualization of dynamic vocal-tract motion and is valuable for speech science and clinical assessment. However, rtMRI is fundamentally constrained by trade-offs among spatial resolution, temporal resolution, and acquisition speed, often leading to undersampled k-space measurements and degraded reconstructions. We propose SIREM, a speech-informed MRI reconstruction framework that uses synchronized speech as a cross-modal prior. The central idea is that vocal-tract configurations during speech are correlated with the produced acoustics, making part of the image content predictable from audio. SIREM models each frame as a fusion of an audio-driven component and an MRI-driven component through a spatial weighting map. The audio branch predicts articulator-related structure from speech, while the MRI branch reconstructs complementary content from measured k-space data. We further introduce a learnable soft weighting profile over spiral arms, enabling a differentiable study of how k-space arm usage interacts with speech-informed fusion. This yields a unified multimodal formulation that combines audio-driven prediction, MRI reconstruction, and sampling adaptation. We evaluate SIREM on the USC speech rtMRI benchmark against standard baselines, including gridding, wavelet-based compressed sensing, and total variation. SIREM introduces a speech-informed reconstruction paradigm that operates in a substantially higher-throughput regime than iterative methods while preserving anatomically plausible vocal-tract structure. These results establish an initial benchmark for multimodal speech-informed rtMRI reconstruction and highlight the potential of synchronized speech as an auxiliary prior for fast reconstruction. The source code is available at https://github.com/mdhasanai/SIREM
匹配关键词: language model
---

[ACADEMIC - ARXIV]
标题: EgoInteract: Synthetic Egocentric Videos Generation for Interaction Understanding and Anticipation
作者: Rosario Leonardi, Francesco Ragusa, Daniele Materia, Alessandro Passanisi, James Fort, Jakob Engel, Giovanni Maria Farinella
链接: https://arxiv.org/abs/2605.18214v1
完整摘要: Collecting large-scale egocentric video datasets with dense spatial and temporal annotations is costly, slow, and often constrained by environmental biases, privacy constraints, and limited coverage of interaction patterns. While synthetic data has shown strong potential in several vision domains, its use for egocentric perception remains relatively underexplored, especially for tasks requiring temporally coherent human-object interactions. In this work, we introduce EgoInteract, a controllable simulator for egocentric video generation designed to model fine-grained egocentric interactions and their temporal dynamics. The simulator enables precise control over camera, human body and hand motion, object manipulation, and scene composition across diverse environments. Building on this framework, we generate a synthetic egocentric video dataset with dense spatial and temporal annotations for temporal action segmentation, next-active object detection, interaction anticipation, and hand-object interaction detection. We evaluate models trained with simulated data on multiple real-world egocentric benchmarks spanning diverse environments, object categories, and interaction patterns. Results show consistent improvements over strong baselines across tasks and datasets, demonstrating the effectiveness and transferability of our simulation-based approach.
匹配关键词: language model
---

[ACADEMIC - ARXIV]
标题: View-Aware Semantic Alignment for Aerial-Ground Person Re-Identification
作者: Quan Zhang, Zeqiang Cai, Peiming Zhao, Jingze Wu, Cailun Wu, Hongbo Chen, Jianhuang Lai
链接: https://arxiv.org/abs/2605.18192v1
完整摘要: Aerial-Ground Person Re-Identification (AGPReID) remains highly challenging due to drastic viewpoint variations between drones and fixed cameras. Existing methods typically follow a view-invariant paradigm, aligning shared features across views to achieve robustness. However, view-invariant inherently enforces part-level alignment, which ignores view-specific cues and discriminative identity information. To this end, this work proposes ViSA (View-aware Semantic Alignment), a view-aware framework that achieves cross-view semantic consistency containing an Expert-driven Token Generation Module (ETGM) and a Dual-branch Local Fusion Module (DLFM). Technically, the former constructs a set of view-aware experts to generate adaptive semantic queries that perceive viewpoint-specific patterns, while the latter leverages graph reasoning to extract and align local regions responsive to different experts. Extensive experiments on three AGPReID benchmarks including AG-ReID.v2, CARGO and LAGPeR demonstrate that ViSA consistently achieves superior performance, with a notable 10.06\% mAP improvement on the challenging CARGO cross-view protocol. The code is available at \href{https://github.com/Cat-Zero/ViSA}{https://github.com/Cat-Zero/ViSA}.
匹配关键词: mixture of experts
---

[ACADEMIC - ARXIV]
标题: Evidence-Grounded Frontier Mapping and Agentic Hypothesis Generation in Nanomedicine
作者: Christiaan G. A. Viviers, Koen de Bruin, Mirre M. Trines, Ayla M. Hokke, Roy van der Meel, Avi Schroeder, Twan Lammers, Willem J. M. Mulder, Fons van der Sommen
链接: https://arxiv.org/abs/2605.18144v1
完整摘要: Nanomedicine research spans delivery chemistry, immunology, imaging, biomaterials, and disease-specific translational science, yet its conceptual design space remains fragmented across a large and heterogeneous literature. To date, artificial intelligence in nanomedicine has focused primarily on property prediction and formulation optimization, with much less attention to evidence-grounded discovery support at the level of research direction selection. We introduce pArticleMap, a literature-mapping and research-hypothesis-generation system that combines article embeddings, similarity-graph analysis, sparse frontier extraction, structured evidence-pack retrieval, and an audited large-language-model (LLM) workflow for grounded ideation. Rather than forecasting future concept co-occurrence, pArticleMap targets low-density article-level bridge regions and cluster interfaces, then generates and scores citation-grounded hypotheses with large language models in an agentic setup. We evaluate the system with a retrospective realization benchmark (generate later literature under a historical cutoff) and a blinded human reader assessment layer across cue-conditioned nanomedicine tasks. Across 4 selected retrospective bundles, pArticleMap generated ideas and selected task-retained hypotheses (winner ideas) under the benchmark protocol. For task-level retained hypotheses, a pooled gold recovery rate of 10.8% was obtained, with a recall@10 of 15.9% and a future-neighborhood rate of 61.0%, indicating that the system often reached the correct forward-looking neighborhood (paper ideas) even without exact paper-level recovery. Human-agent agreement is modest overall, indicating that internal scoring is useful as a support signal but does not replace expert judgment. These results position pArticleMap as a conservative, evidence-grounded research assistant for nanomedicine.
匹配关键词: mixture of experts
---

[ACADEMIC - ARXIV]
标题: A Data-Efficient Path to Multilingual LLMs: Language Expansion via Post-training PARAM$Δ$ Integration into Upcycled MoE
作者: Hao Zhou, Tianhao Li, Zhijun Wang, Shuaijie She, Linjuan Wu, Hao-Ran Wei, Baosong Yang, Jiajun Chen, Shujian Huang
链接: https://arxiv.org/abs/2605.18083v1
完整摘要: Expanding Large Language Models~(LLMs) to new languages is a costly endeavor, demanding extensive Continued Pre-Training~(CPT) and data-intensive alignment. While recent data-free merging techniques attempt to bypass alignment by fusing a multilingual CPT-enhanced model with its instruct counterpart, they are plagued by a critical trade-off: mitigating parameter conflicts to preserve original abilities inevitably dilutes new language acquisition, and vice-versa. To resolve this conflict, we introduce \method, which upcycles a dense model into a Mixture-of-Experts~(MoE) architecture, allocating different experts to different languages. Alignment ability is then transferred by grafting a MoE-expanded parameter delta~($Δ_{\text{post}}$) to the CPT-enhanced base model, bypassing the complex alignment phase. Experiments demonstrate \method's superiority even against baselines with similar FLOPs or number of parameters; it improves performance on expanded languages while effectively preserving original capabilities. We further show our approach is highly applicable across different models and Post-training deltas.
匹配关键词: mixture of experts
---

[ACADEMIC - ARXIV]
标题: 4DLidarOpen: An Open 4D FMCW Lidar Dataset for Motion-Aware Autonomous Driving
作者: Kane Qian, Xin Zhao, Yining Shi, Rujun Yan, Zhengqing Pan, Kaojin Zhu, Mengmeng Yang, Kai Sun, Diange Yang, Kun Jiang
链接: https://arxiv.org/abs/2605.18074v1
完整摘要: We present 4DLidarOpen, a large-scale open multi-modal dataset for autonomous driving, centered on 4D frequency-modulated continuous-wave (FMCW) Lidar sensing. Unlike conventional time-of-flight Lidar datasets that mainly provide geometric measurements, 4DLidarOpen includes point-wise radial velocity measurements from a forward-facing 4D FMCW Lidar, together with multiple Lidars of different types, including rotating, solid-state, and blind-spot variants, surround-view cameras, and 6-DOF ego-vehicle poses. The dataset was collected in complex urban environments in Beijing and covers dense pedestrian interactions, congested traffic, high-speed driving, and unprotected maneuvers. 4DLidarOpen provides synchronized multi-sensor data and 3D bounding-box annotations with persistent track IDs across five object categories. A hybrid annotation strategy is adopted, where large-scale auto-labeled data support scalable training and human experts refine annotations for the human-annotated training and validation sets. Based on this dataset, we establish benchmarks for 3D object detection, birds-eye view (BEV) segmentation and flow prediction, and motion forecasting with planning. Extensive experiments show that direct velocity measurements from 4D FMCW Lidar provide complementary motion cues for dynamic-scene understanding. Compared with geometric-only sensing, the velocity-aware representation improves motion-related perception and downstream forecasting and planning, especially in scenarios involving vulnerable road users and fast-moving objects. These results indicate that 4D FMCW Lidar is a promising sensing modality for motion-aware autonomous driving. The dataset and evaluation toolkit are publicly released to support research on 4D scene understanding, multi-Lidar fusion, and velocity-aware perception and planning.
匹配关键词: mixture of experts
---

[ACADEMIC - ARXIV]
标题: Quantum Sidecar Architectures for Hybrid AI Training and Inference: Stateful Protected Registers, Stateless Reset-and-Reprepare Circuits and Quantum Weight-State Outlook
作者: Y. Mo, G. D. Su
链接: https://arxiv.org/abs/2605.18031v1
完整摘要: We propose a quantum sidecar architecture family for future hybrid AI training and inference. The central idea is not to store an entire Transformer in a small quantum memory, nor to claim one-shot collapse into a fully trained model or an optimal answer. Instead, we identify two physically distinct operating modes for quantum co-processors attached to classical large-model pipelines. The first is a stateful protected-register mode, in which a protected register stores a reusable quantum resource while an ancilla or temporary register performs QND-style readout. The second is a stateless reset-and-reprepare mode, in which each query prepares a task-conditioned quantum circuit, evolves over bounded training or inference control variables, measures candidate signals, resets the qubits, and repeats. We simulate the stateful mode using 2/4/6/8 protected-qubit density-matrix QND-style parity readout with one ancilla and a Qiskit cross-check. For the stateless mode, we include both an abstract candidate-update sampler and a circuit-level QAOA-style statevector sampler over structured candidate landscapes, followed by reset-overhead sensitivity analysis. The resulting framework positions quantum sidecars as bounded signal generators for optimizer-side sampling, adapter or expert selection, retrieval, routing, and reasoning-path proposal. As a speculative outlook, we introduce quantum weight-state sidecars: restricted quantum representations over model-control variables, not direct encodings of complete classical weight tensors.
匹配关键词: mixture of experts
---

[ACADEMIC - ARXIV]
标题: Are Sparse Autoencoder Benchmarks Reliable?
作者: David Chanin
链接: https://arxiv.org/abs/2605.18229v1
完整摘要: Sparse autoencoders (SAEs) are a core interpretability tool for large language models, and progress on SAE architectures depends on benchmarks that reliably distinguish better SAEs from worse ones. We audit the SAE quality metrics in SAEBench, the de-facto standard SAE evaluation suite, through three complementary lenses: reseed noise on a fixed SAE, ground-truth correlation on synthetic SAEs, and discriminability across training trajectories. We find that two of these metrics, Targeted Probe Perturbation (TPP) and Spurious Correlation Removal (SCR), fail multiple lenses at their canonical settings and should not be used to evaluate SAEs. The other metrics show higher reseed noise and lower discriminability than the field assumes. The sae-probes variant of $k$-sparse probing is the most reliable metric we tested, but even sae-probes struggles to separate variants of the same SAE architecture. Our results show the field needs better SAE benchmarks.
匹配关键词: transformer architecture
---

[ACADEMIC - ARXIV]
标题: SPATIOROUTE: Dynamic Prompt Routing for Zero-Shot Spatial Reasoning
作者: Pawat Chunhachatrachai, Gueter Josmy Faure, Hung-Ting Su, Winston H. Hsu
链接: https://arxiv.org/abs/2605.18209v1
完整摘要: Spatial question answering over egocentric video is a challenging task that requires Vision-Language Models (VLMs) to reason about 3D object positions, scene affordances, and directional relationships, particularly in the zero-shot setting where no task-specific fine-tuning is available. We introduce SpatioRoute, a dynamic prompt generation approach that routes each incoming question to a semantically tailored prompt template -- without any additional training, fine-tuning, or 3D sensor input. SpatioRoute operates in two complementary modes: SpatioRoute-R, a rule-based router that deterministically maps question typologies (e.g., What, Is, How, Can, Which) to specialized prompt templates; and SpatioRoute-L, an LLM-driven approach that generates task-specific prompts from the question and situational context alone, with no video input at routing time. We evaluate SpatioRoute on the SQA3D benchmark across VLMs spanning model families. SpatioRoute achieves consistent overall accuracy gains up to 5% over fixed prompt baselines, establishing a new state-of-the-art for zero-shot video-only spatial VQA without requiring 3D point-cloud inputs. As an additional finding, we observe that Chain-of-Thought (CoT) prompting, implemented via the Think it Twice architecture, consistently degrades performance in this setting on Qwen series models, confirming that question-aware routing is more effective than uniform reasoning instructions for spatial video understanding.
匹配关键词: transformer architecture
---

[ACADEMIC - ARXIV]
标题: Concise and Logically Consistent Conformal Sets for Neuro-Symbolic Concept-Based Models
作者: Samuele Bortolotti, Emanuele Marconato, Andrea Pugnana, Andrea Passerini, Stefano Teso
链接: https://arxiv.org/abs/2605.18202v1
完整摘要: Neuro-Symbolic Concept-based Models (NeSy-CBMs) are a family of architectures that integrate neural networks with symbolic reasoning for enhanced reliability in high-stakes applications. They work by first extracting high-level concepts from the input and then inferring a task label from these compatibly with given logical constraints. Yet, their label and concept predictions can be overconfident, making it difficult for stakeholders to gauge when the model's decisions can be trusted. We address this issue by integrating ideas from Conformal Prediction (CP), a framework providing rigorous, distribution-free coverage guarantees. We formalize three desiderata -- consistency, coverage, and conciseness -- that any conformal method for NeSy-CBMs should satisfy, and show that existing approaches fall short of at least one. We then introduce COCOCO, a post-hoc framework that conformalizes concepts and labels jointly and reconciles them via a single deduction-abduction revision step. COCOCO satisfies all three desiderata, retains distribution-free coverage, is robust to imperfect knowledge and supports user-specified size budgets. Our experiments on 8 data sets highlight how COCOCO compares favorably against competitors and natural baselines in terms of performance and set size.
匹配关键词: transformer architecture
---

[ACADEMIC - ARXIV]
标题: Beyond the Cartesian Illusion: Testing Two-Stage Multi-Modal Theory of Mind under Perceptual Bottlenecks
作者: Yajing Zhou, Xiangyu Kong
链接: https://arxiv.org/abs/2605.18194v1
完整摘要: While Multi-Modal Large Language Models (MLLMs) demonstrate impressive capabilities in general reasoning, their embodied spatial intelligence remains hampered by a "Cartesian Illusion" - a reliance on text-based probability distributions that lack grounded, 3D topological understanding. This limitation is starkly exposed in multi-agent environments, which demand more than just scene perception; they require second-order Theory of Mind (ToM). Specifically, an Agent A must be able to infer Agent B's belief about the environment, governed strictly by Agent B's physical orientation and sensory limitations. In this paper, we probe the limits of two-stage spatial inference in MLLMs through a novel audio-visual task: requiring Agent A to predict Agent B's estimation of A's relative location. To solve this, we propose an Epistemic Sensory Bottleneck module that abandons rigid, rule-based coordinate transformations. Instead, we introduce an Anchor-Based Embodied Spatial Decomposition Chain-of-Thought (CoT). This guides the MLLM through a "geometric-to-semantic" projection, forcing it to first establish B's local coordinate system and then dynamically weight visual and auditory modalities based on whether A falls within B's visual frustum. Extensive evaluations reveal that while current MLLMs fundamentally struggle with spatial symmetry and out-of-view ambiguities (establishing a rigorous zero-shot baseline of 42% accuracy), our sensory-bounded reasoning chain robustly outperforms pure egocentric and allocentric baselines. By systematically benchmarking these perceptual bottlenecks, our work exposes the current limits of MLLM spatial reasoning and establishes a foundational paradigm for epistemic, modality-aware inference in Embodied AI.
匹配关键词: transformer architecture
---

[ACADEMIC - ARXIV]
标题: UTOPYA: A Multimodal Deep Learning Framework for Physics-Informed Anomaly Detection and Time-Series Prediction
作者: Robson W. S. Pessoa, Julien Amblard, Alessandra Russo, Idelfonso B. R. Nogueira
链接: https://arxiv.org/abs/2605.18188v1
完整摘要: Anomaly detection in batch processes is hindered by transient dynamics, scarce fault labels, and reliance on single-modality sensor data. This work introduces UTOPYA (Unified Temporal Observation for Physics-Informed Anomaly Detection and Time-Series Prediction), a 15.2M-parameter multimodal framework that jointly addresses anomaly detection, time-series prediction, and phase classification in batch distillation by fusing eight data modalities through Feature-wise Linear Modulation (FiLM) conditioned cross-modal attention and gated fusion. A physics-informed regularisation scheme introduced in this work enforces temporal smoothness and thermodynamic monotonicity, while curriculum learning introduces training samples in order of physical difficulty. On the 119-experiment multimodal batch distillation dataset of Arweiler et al. (2026), UTOPYA achieves a window-level test AUROC of 0.832 and 0.874 under multi-signal experiment-level scoring, substantially outperforming four external baselines (PCA, autoencoder, Isolation Forest, and LSTM autoencoder) evaluated under identical conditions (+0.147 window-level AUROC over the best baseline). A multimodal ablation over 15~architectural configurations shows that static context via FiLM conditioning is the key enabler, lifting experiment-level multi-signal AUROC by +0.145 over the unimodal baseline (0.729 to 0.874). Separately, a training ablation across 14 design choices reveals that several widely-adopted techniques, including instance normalisation, Mixup, ensembling, test-time augmentation, and stochastic weight averaging, fail to improve or actively degrade generalisation in this data-scarce setting. These negative results expose a fundamental tension between smoothing-based regularisation and anomaly detection, providing practical guidance for multimodal process monitoring deployment.
匹配关键词: transformer architecture
---

[ACADEMIC - ARXIV]
标题: Self-Evolving Spatial Reasoning in Vision Language Models via Geometric Logic Consistency
作者: Junming Liu, Yuqi Li, Yifei Sun, Maonan Wang, Piotr Koniusz, Yirong Chen, Ding Wang
链接: https://arxiv.org/abs/2605.18162v1
完整摘要: Vision-Language Models (VLMs) have made striking progress, yet their spatial reasoning remains fragile: models that answer an original input correctly can still fail under paired transformations with predictable answer mappings, revealing a gap between instance-level correctness and robust spatial reasoning. To address this, we propose Spatial Alignment via Geometric Evolution (SAGE), a self-evolving framework that enforces logical consistency in VLMs through geometric and linguistic duality operations. SAGE incorporates duality consistency as an auxiliary reward within GRPO training, encouraging models to produce logically coherent answers across original and transformed inputs. A dynamic operation pool continuously probes for inconsistencies, promoting challenging operations and retiring mastered ones, so that training focuses on the most informative signals. SAGE is model-agnostic, data-efficient compared to prior GRPO methods, and can be applied as a lightweight post-training stage to any existing VLM. Experiments on video and spatial reasoning benchmarks demonstrate consistent improvements over strong baselines and enhanced generalization to unseen data.
匹配关键词: post-training
---

[ACADEMIC - ARXIV]
标题: POST: Prior-Observation Adversarial Learning of Spatio-Temporal Associations for Multivariate Time Series Anomaly Detection
作者: Suofei Zhang, Yaxuan Zheng, Haifeng Hu
链接: https://arxiv.org/abs/2605.18128v1
完整摘要: Existing Multivariate Time Series Anomaly Detection (MTSAD) frameworks increasingly rely on integrating Graph Neural Networks (GNNs) with sequence models to capture complex spatio-temporal dependencies. However, less attention is paid to the spatial over-generalization problem, where unconstrained structural modeling indiscriminately reconstructs anomalies, inevitably degrading detection recall. To tackle this problem, we propose a novel framework that unifies spatio-temporal modeling through a joint prior-observation adversarial learning paradigm. In the spatial dimension, the model alternately learns adjacency matrices as structural prior and models the association discrepancy between prior and data-driven observation in a minimax manner during training. Such adversarial optimization not only improves the model sensitivity for time-wise detection, but also enables the model to localize anomalies to specific channels. To systematically evaluate this anomaly localization capability, we further construct a synthetic benchmark equipped with precise channel-wise annotations. Extensive experiments across public datasets and our dedicated benchmark demonstrate that the proposed framework establishes a new state-of-the-art in both time-wise detection and spatial localization tasks. Our code, pre-trained models, and benchmark are publicly available at https://github.com/anocodetest1/POST.
匹配关键词: post-training
---

[ACADEMIC - ARXIV]
标题: A Data-Efficient Path to Multilingual LLMs: Language Expansion via Post-training PARAM$Δ$ Integration into Upcycled MoE
作者: Hao Zhou, Tianhao Li, Zhijun Wang, Shuaijie She, Linjuan Wu, Hao-Ran Wei, Baosong Yang, Jiajun Chen, Shujian Huang
链接: https://arxiv.org/abs/2605.18083v1
完整摘要: Expanding Large Language Models~(LLMs) to new languages is a costly endeavor, demanding extensive Continued Pre-Training~(CPT) and data-intensive alignment. While recent data-free merging techniques attempt to bypass alignment by fusing a multilingual CPT-enhanced model with its instruct counterpart, they are plagued by a critical trade-off: mitigating parameter conflicts to preserve original abilities inevitably dilutes new language acquisition, and vice-versa. To resolve this conflict, we introduce \method, which upcycles a dense model into a Mixture-of-Experts~(MoE) architecture, allocating different experts to different languages. Alignment ability is then transferred by grafting a MoE-expanded parameter delta~($Δ_{\text{post}}$) to the CPT-enhanced base model, bypassing the complex alignment phase. Experiments demonstrate \method's superiority even against baselines with similar FLOPs or number of parameters; it improves performance on expanded languages while effectively preserving original capabilities. We further show our approach is highly applicable across different models and Post-training deltas.
匹配关键词: post-training
---

[ACADEMIC - ARXIV]
标题: SAS: Semantic-aware Sampling for Generative Dataset Distillation
作者: Mingzhuo Li, Guang Li, Linfeng Ye, Jiafeng Mao, Takahiro Ogawa, Konstantinos N. Plataniotis, Miki Haseyama
链接: https://arxiv.org/abs/2605.18012v1
完整摘要: Deep neural networks have achieved impressive performance across a wide range of tasks, but this success often comes with substantial computational and storage costs due to large-scale training data. Dataset distillation addresses this challenge by constructing compact yet informative datasets that enable efficient model training while maintaining downstream performance. However, most existing approaches primarily emphasize matching data distributions or downstream training statistics, with limited attention to preserving high-level semantic information in the distilled data. In this work, we introduce a semantic-aware perspective for dataset distillation by leveraging Contrastive Language-Image Pretraining (CLIP) as a semantic prior for post-sampling. Our goal is to obtain distilled datasets that are not only compact but also semantically class-discriminative and diverse. To this end, we design three semantic scoring functions that quantify class relevance, inter-class separability, and intra-set diversity in a pretrained semantic space. Based on image pools generated by existing distillation methods, we further develop a two-stage strategy for effective sampling: the first stage filters semantically discriminative samples to form a reliable candidate set, and the second stage performs a dynamic diversity-aware selection to reduce redundancy while preserving semantic coverage. Extensive experiments across multiple datasets, image pools, and downstream models demonstrate consistent performance gains, highlighting the effectiveness of incorporating semantic information into dataset distillation.
匹配关键词: post-training
---

[ACADEMIC - ARXIV]
标题: Uncertainty Reliability Under Domain Shift: An Investigation for Data-Driven Blood Pressure Estimation in Photoplethysmography
作者: Mohammad Moulaeifard, Ciaran Bench, Philip J. Aston, Nils Strodthoff
链接: https://arxiv.org/abs/2605.18008v1
完整摘要: Uncertainty quantification (UQ) is critical for safety-critical domains like healthcare, yet it is rarely evaluated under realistic out-of-distribution (OOD) conditions. Here, we assessed predictive performance and uncertainty reliability for deep learning-based blood pressure (BP) estimation from photoplethysmography (PPG) signals under both in-distribution (ID) and OOD settings. Using an XResNet1D-50 trained on PulseDB and tested on four external datasets, we compared deep ensembles (DE) and Monte Carlo dropout (MCD) with Gaussian negative log-likelihood (GNLL) and mean squared error (MSE) losses, optionally followed by post-hoc recalibration via conformal prediction (CP), temperature scaling (TS), and isotonic regression (IR). The key findings of our study are as follows: (1) DE provides stronger predictive robustness under domain shift than MCD, an advantage that becomes clear primarily under external shift. (2) Recalibrated GNLL-based methods yield the best uncertainty calibration (e.g., GNLL+DE+CP for systolic blood pressure (SBP), GNLL+DE+TS for diastolic blood pressure (DBP)), while MSE-based uncertainty requires recalibration to become practically useful. (3) Across settings, CP and TS offer the most consistent gains, with IR remaining competitive in several cases. Overall, our results identify DE-based methods as most robust for predictive performance under domain shift, GNLL as strongest for native UQ, and recalibration as essential for making MSE-based uncertainty practical. These findings highlight the need to jointly assess predictive accuracy and calibration on external data for trustworthy cuffless BP estimation
匹配关键词: post-training
---

[ACADEMIC - ARXIV]
标题: SPATIOROUTE: Dynamic Prompt Routing for Zero-Shot Spatial Reasoning
作者: Pawat Chunhachatrachai, Gueter Josmy Faure, Hung-Ting Su, Winston H. Hsu
链接: https://arxiv.org/abs/2605.18209v1
完整摘要: Spatial question answering over egocentric video is a challenging task that requires Vision-Language Models (VLMs) to reason about 3D object positions, scene affordances, and directional relationships, particularly in the zero-shot setting where no task-specific fine-tuning is available. We introduce SpatioRoute, a dynamic prompt generation approach that routes each incoming question to a semantically tailored prompt template -- without any additional training, fine-tuning, or 3D sensor input. SpatioRoute operates in two complementary modes: SpatioRoute-R, a rule-based router that deterministically maps question typologies (e.g., What, Is, How, Can, Which) to specialized prompt templates; and SpatioRoute-L, an LLM-driven approach that generates task-specific prompts from the question and situational context alone, with no video input at routing time. We evaluate SpatioRoute on the SQA3D benchmark across VLMs spanning model families. SpatioRoute achieves consistent overall accuracy gains up to 5% over fixed prompt baselines, establishing a new state-of-the-art for zero-shot video-only spatial VQA without requiring 3D point-cloud inputs. As an additional finding, we observe that Chain-of-Thought (CoT) prompting, implemented via the Think it Twice architecture, consistently degrades performance in this setting on Qwen series models, confirming that question-aware routing is more effective than uniform reasoning instructions for spatial video understanding.
匹配关键词: fine-tuning
---

[ACADEMIC - ARXIV]
标题: Visualizing the Invisible: Generative Visual Grounding Empowers Universal EEG Understanding in MLLMs
作者: Junyu Pan, Yansen Wang, Enze Zhang, Baoliang Lu, Weilong Zheng, Dongsheng Li
链接: https://arxiv.org/abs/2605.18172v1
完整摘要: Leveraging the universal representations of pre-trained LLMs and MLLMs offers a promising path toward brain foundation models. However, visually-evoked EEG datasets remain scarce, leading existing methods to align neural signals mainly with abstract text, a lossy translation that may discard fine-grained perceptual information encoded in brain activity. We propose Generative Visual Grounding (GVG), a framework that visualizes the invisible by using an EEG-to-image generative model as a visual translator. Instead of forcing EEG into text alone, GVG hallucinates instance-specific proxy images for non-visual EEG, providing structured visual contexts that allow MLLMs to exploit their visual priors for clinical-state interpretation. We validate this idea on two MLLM backbones, GVG-X-Omni and GVG-Janus. Image-only alignment is already competitive: the lightweight GVG-X-Omni matches 1.7B-parameter text-aligned baselines while tuning only 170M parameters on a frozen 7B backbone. We further extend GVG-Janus with trimodal Image+Text alignment, where text supplies categorical semantic anchors and visual proxies enrich neural representations with perceptual details. Experiments show consistent gains in EEG understanding and visual generation, suggesting visual proxy grounding as an effective complement to textual alignment.
匹配关键词: fine-tuning
---

[ACADEMIC - ARXIV]
标题: FOL2NS: Generating Natural Sentences from First-Order Logic
作者: Mei Jia
链接: https://arxiv.org/abs/2605.18155v1
完整摘要: Translating formal language into natural language is a foundational challenge in NLP, driving various downstream applications in semantic parsing, theorem validation, and question answering. In this study, we introduce First-Order Logic to Natural Sentence (FOL2NS), a neurosymbolic framework designed to generate synthetic FOL formulas and convert them into natural human expressions. It handles deeply nested structures with varying quantifier depths (QD), which are rarely captured by existing corpora. By combining rule-driven modules with fine-tuned language models, FOL2NS enhances the diversity and coverage of the generated samples. In our experiments, we systematically evaluate the framework's capabilities through both character-level analysis and overall performance metrics. Experimental results show that FOL2NS can reliably produce well-formed templates and fluent statements, but it faces challenges in achieving precise semantic representations and natural generation as structural complexity increases.
匹配关键词: fine-tuning
---

[ACADEMIC - ARXIV]
标题: Xiaomi EV World Model: A Joint World Model Integrating Reconstruction and Generation for Autonomous Driving
作者: Lijun Zhou, Hongcheng Luo, Zhenxin Zhu, Cheng Chi, Mingfei Tu, Kaixin Xiong, Lei Gong, Zhanqian Wu, Zehan Zhang, Fangzhen Li, Hao Li, Yingying Shen, Jiale He, Haohui Zhu, Shan Zhao, Kai Wang, Zhiwei Zhan, Yuechuan Pu, Kaiyuan Tan, Ruiling Yang, Xianqi Wang, Tianyi Yan, Jiawei Zhou, Lei Zhang, Jingyang Zhao, Xi Zhou, Chitian Sun, Chenming Wu, Jiong Deng, Hongwei Xie, Ming Lu, Kun Ma, Long Chen, Guang Chen, Hangjun Ye, Bing Wang, Haiyang Sun
链接: https://arxiv.org/abs/2605.18137v1
完整摘要: This report presents a unified technical system addressing the two core capabilities of world models for autonomous driving: world representation and world generation. For world representation, we propose WorldRec, a feed-forward reconstruction architecture driven by sparse scene queries. WorldRec initializes structured queries in 3D space, leveraging them to aggregate cross-view, cross-temporal features, thereby naturally enforcing spatial consistency across frames and yielding compact yet high-fidelity 3D Gaussian scene representations. For world generation, we propose WorldGen, a two-stage training framework of bidirectional pretraining followed by causal fine-tuning through three progressive stages (Teacher Forcing, ODE distillation, and DMD), enabling high-quality online causal video generation in as few as 4 denoising steps. Building on both modules, we further introduce the JWM, which deeply integrates WorldRec and WorldGen to achieve synergistic gains in generation stability, cross-frame consistency, and visual fidelity, providing a solid foundation for closed-loop simulation, data synthesis, and end-to-end training in autonomous driving.
匹配关键词: fine-tuning
---

[ACADEMIC - ARXIV]
标题: FedSDR: Federated Self-Distillation with Rectification
作者: Ziheng Ren, Zhanming Shen, Hao Wang, Ning Liu, You Song
链接: https://arxiv.org/abs/2605.18028v1
完整摘要: Federated fine-tuning of Large Language Models faces severe statistical heterogeneity. However, existing model-level defenses often overlook the root cause: intrinsic data distribution mismatches. In this work, we first establish Federated Self-Distillation (FedSD) as a fundamental and potent strategy. By projecting client representations into a smoothed ``model-understanding space,'' FedSD alone serves as a universal booster, demonstrating superior performance over conventional algorithms. Despite its success, we identify a subtle trade-off termed the Rewrite Paradox -- unconstrained self-distillation can inadvertently increase hallucinations and redundancy. To refine this paradigm, we further propose FedSDR (Federated Self-Distillation with Rectification), the ultimate reinforced framework. It augments FedSD with a dual-stream mechanism: a local LoRA-S (Smoothing) branch to implicitly absorb heterogeneity via distilled data, and a parallel global LoRA-R (Rectification) branch anchored to raw data to enforce factual correctness. By selectively aggregating only LoRA-R, FedSDR yields a globally aligned and faithful model. Extensive experiments verify its superior performance.
匹配关键词: fine-tuning
---

[ACADEMIC - ARXIV]
标题: Reconciling Contradictory Views on the Effectiveness of SFT in LLMs: An Interaction Perspective
作者: Junpeng Zhang, Lei Cheng, Guoxi Zhang, Hua Cai, Qing Xu, Quanshi Zhang
链接: https://arxiv.org/abs/2605.17967v1
完整摘要: This paper explores a scientific question in supervised fine-tuning (SFT): why SFT is broadly effective for small-scale deep neural networks, yet can produce inconsistent or even detrimental effects when applied to large language models (LLMs). Recent advances in interaction-based explanations suggest that interactions between words/tokens provide a faithful metric for quantifying the inference patterns encoded by LLMs. We find that the evolution of interactions during SFT can effectively explain the inconsistent effectiveness of SFT for LLMs. Specifically, we find that (1) SFT primarily removes noise-like interactions, while rarely acquiring reliable new interactions. (2) This denoising stage is extremely brief, after which continued fine-tuning tends to introduce overfitted interactions. We validate these findings across multiple LLMs and datasets. Our findings provide new insights into early stopping and offer practical guidance for LLM training.
匹配关键词: SFT
---

[ACADEMIC - ARXIV]
标题: Beyond the Cartesian Illusion: Testing Two-Stage Multi-Modal Theory of Mind under Perceptual Bottlenecks
作者: Yajing Zhou, Xiangyu Kong
链接: https://arxiv.org/abs/2605.18194v1
完整摘要: While Multi-Modal Large Language Models (MLLMs) demonstrate impressive capabilities in general reasoning, their embodied spatial intelligence remains hampered by a "Cartesian Illusion" - a reliance on text-based probability distributions that lack grounded, 3D topological understanding. This limitation is starkly exposed in multi-agent environments, which demand more than just scene perception; they require second-order Theory of Mind (ToM). Specifically, an Agent A must be able to infer Agent B's belief about the environment, governed strictly by Agent B's physical orientation and sensory limitations. In this paper, we probe the limits of two-stage spatial inference in MLLMs through a novel audio-visual task: requiring Agent A to predict Agent B's estimation of A's relative location. To solve this, we propose an Epistemic Sensory Bottleneck module that abandons rigid, rule-based coordinate transformations. Instead, we introduce an Anchor-Based Embodied Spatial Decomposition Chain-of-Thought (CoT). This guides the MLLM through a "geometric-to-semantic" projection, forcing it to first establish B's local coordinate system and then dynamically weight visual and auditory modalities based on whether A falls within B's visual frustum. Extensive evaluations reveal that while current MLLMs fundamentally struggle with spatial symmetry and out-of-view ambiguities (establishing a rigorous zero-shot baseline of 42% accuracy), our sensory-bounded reasoning chain robustly outperforms pure egocentric and allocentric baselines. By systematically benchmarking these perceptual bottlenecks, our work exposes the current limits of MLLM spatial reasoning and establishes a foundational paradigm for epistemic, modality-aware inference in Embodied AI.
匹配关键词: AI scientist
---

[ACADEMIC - ARXIV]
标题: Foundation Models for Credit Risk Prediction: A Game Changer?
作者: Bart Baesens, Andreas Goethals, Stefan Lessmann, Simon De Vos, Cristián Bravo, David Martens, Victor Medina-Olivares, Christophe Mues, Maria Oskarsdóttir, Seppe vanden Broucke, Tim Verdonck, Wouter Verbeke
链接: https://arxiv.org/abs/2605.18147v1
完整摘要: Predictive models play a pivotal role in credit risk management, guiding critical decisions through accurate estimation of default probabilities and losses. Extensive research has introduced new modeling techniques, complemented by large-scale benchmarking studies consolidating the state-of-the-art. Today, quasi-standards such as gradient-boosting models paired with SHAP explainers have emerged, yet continuous improvement of risk models remains a top priority. Concurrently, rapid advancements in AI, most notably large language models, have disrupted predictive modeling paradigms. Foundation models, pretrained on extensive datasets from diverse domains, have demonstrated remarkable performance by leveraging prior knowledge. While prevalent in natural language processing and computer vision, foundation models for tabular data have only recently emerged. We conjecture that pretraining on out-of-domain data is particularly beneficial in small-data settings, such as SME lending or specialized corporate portfolios, and may help address longstanding challenges including low default portfolios and class imbalance. This paper benchmarks recently proposed tabular foundation models against a broad set of competitors, including established and advanced machine learning techniques, across two core tasks: PD and LGD modeling. Our evaluation encompasses various datasets, performance indicators, and experimental conditions. We find that tabular foundation models generally perform best across datasets and tasks. Moreover, they offer significant improvement in predictive performance as dataset size shrinks. These results are remarkable given that the models are tested out-of-the-box, without hyperparameter tuning, ensuring ease of use and mitigating computational costs.
匹配关键词: AI scientist
---

[ACADEMIC - ARXIV]
标题: Generative AI and the Productivity Divide: Human-AI Complementarities in Education
作者: Lihi Idan, Bharat Anand
链接: https://arxiv.org/abs/2605.18143v1
完整摘要: Generative Artificial Intelligence (GenAI) is transforming how firms create, process, and apply knowledge, yet little is known about the heterogeneity of its productivity effects across users. We report results from a randomized controlled experiment in which participants-analogs of early-career knowledge workers-were assigned to self-study a technical domain using either traditional resources or large-language-model (LLM) assistance. On average, GenAI access significantly increased task performance, but the distribution of gains was highly uneven. Improvements were not predicted by GPA or prior knowledge, but by \textit{AI Interaction Competence (AIC)} -- the ability to elicit, filter, and verify model outputs. High-AIC participants realized outsized gains; low-AIC participants saw limited or even negative marginal returns. A scaffolding intervention (conceptual maps) reduced outcome variance, indicating that standardized workflows can mitigate inequality in AI-mediated performance. We interpret these findings through the lens of human-AI complementarities: GenAI raises mean productivity while introducing a new axis of capability inequality. Managerially, firms should pair GenAI access with short AIC micro-training and simple standard operating procedures to capture value consistently and avoid uneven adoption outcomes.
匹配关键词: AI scientist
---

[ACADEMIC - ARXIV]
标题: How Good LLMs Are at Answering Bangla Medical Visual Questions? Dataset and Benchmarking
作者: Rafid Ahmed, Intesar Tahmid, Mir Sazzat Hossain, Tasnimul Hossain Tomal, Md Fahim, Md Farhad Alam Bhuiyan
链接: https://arxiv.org/abs/2605.18111v1
完整摘要: Recent advancements in Large Language Models (LLMs) and Large Vision Language Models (LVLMs) have enabled general-purpose systems to demonstrate promising capabilities in complex reasoning tasks, including those in the medical domain. Medical Visual Question Answering (MedVQA) has particularly benefited from these developments. However, despite Bangla being one of the most widely spoken languages globally, there exists no established MedVQA benchmark for it. To address this gap, we introduce BanglaMedVQA, a dataset comprising clinically validated image-question-answer pairs, along with a comprehensive evaluation of current foundation models on this resource. Consistent with prior findings that report low performance of current models on English MedVQA benchmarks, our analysis reveals that Bangla performance is substantially lower, reflecting the challenges inherent to low-resource languages. Even top-performing models such as Gemini and GPT-4.1 mini fail to accurately answer specialized diagnostic questions, indicating severe limitations in fine-grained medical reasoning. Although certain open-source models, such as Gemma-3, occasionally outperform these models in general categories, they too struggle with clinically complex questions, underscoring the urgent need for top-notch evaluation method.
匹配关键词: AI scientist
---

[ACADEMIC - ARXIV]
标题: SENSE: Satellite-based ENergy Synthesis for Sustainable Environment
作者: Kailai Sun, Mingyi He, Heye Huang, Can Rong, Alok Prakash, Baoshen Guo, Shenhao Wang, Jinhua Zhao
链接: https://arxiv.org/abs/2605.18101v1
完整摘要: Urban Building Energy Modeling plays a critical role in achieving the United Nations' Sustainable Development Goals 7 and 11. Although existing studies based on satellite imagery and deep learning have achieved remarkable progress, many challenges exist: most existing studies are inherently predictive, failing to reflect the generative nature of urban planning; although generative AI and diffusion models have seen explosive growth in satellite imagery, they lack the urban functional generation (e.g., energy layer); third, aligned high-quality high-resolution building energy data with satellite imagery is limited and scarce. Here we propose SENSE (Satellite-based ENergy Synthesis for Sustainable Environment), a unified generative UBEM framework that jointly synthesizes realistic urban satellite imagery and aligned high-quality building energy consumption and height maps. By conditioning on road networks and urban density metrics, SENSE, based on a controllable diffusion model, leverages the knowledge learned by large vision models to generate urban building energy consumption and height information (annotations) in the latent space. Experiments across four cities (New York City, Boston, Lyon, Busan) demonstrate that SENSE achieves high visual fidelity and strong physical consistency, satisfying the ASHRAE standard metric. Experiments demonstrate that SENSE can generate enough annotated synthetic data using less than 20% labeled energy data, boosting downstream prediction performance by 10% IoU. Compared to SOTA urban energy prediction methods, SENSE significantly reduced prediction error (reduced 3%-11% NMBE and 1%-9% CVRMSE). This study offers an energy-efficiency urban planning and physical generation solution for urban science, energy science and building science. The dataset and code: https://huggingface.co/datasets/skl24/MUSE and https://github.com/kailaisun/GenAI4Urban-Energy/.
匹配关键词: AI scientist
---

[ACADEMIC - ARXIV]
标题: Best Segmentation Buddies for Image-Shape Correspondence
作者: Itai Lang, Dongwei Lyu, Dale Decatur, Rana Hanocka
链接: https://arxiv.org/abs/2605.18193v1
完整摘要: Finding correspondences is a fundamental and extensively researched problem in computer vision and graphics. In this work, we examine the underexplored task of estimating segmentation-to-segmentation correspondence between images in the wild and untextured 3D shapes. This task is highly challenging due to substantial differences in appearance, geometry, and viewpoint. Our approach bridges the cross-modality gap by linking pixels in the image segment to vertices in the corresponding semantic part of the 3D shape. To achieve this, we first distill deep visual features from a 2D vision model onto the 3D shape surface, allowing for the computation of feature similarity between image pixels and shape vertices. Then, we identify Best Segmentation Buddies, vertices whose most similar image pixel lies within the image segmentation region, enabling the reliable discovery of vertices in semantically corresponding shape parts. Finally, we leverage distilled 3D features from the 2D image segmentation model to segment the shape directly in 3D, bootstrapping the correspondence process. We demonstrate the generality and robustness of our approach across a wide range of image-shape pairs, showcasing accurate and semantically meaningful correspondences. Our project page is at https://threedle.github.io/bsb/.
匹配关键词: automated research
---

[ACADEMIC - ARXIV]
标题: Foundation Models for Credit Risk Prediction: A Game Changer?
作者: Bart Baesens, Andreas Goethals, Stefan Lessmann, Simon De Vos, Cristián Bravo, David Martens, Victor Medina-Olivares, Christophe Mues, Maria Oskarsdóttir, Seppe vanden Broucke, Tim Verdonck, Wouter Verbeke
链接: https://arxiv.org/abs/2605.18147v1
完整摘要: Predictive models play a pivotal role in credit risk management, guiding critical decisions through accurate estimation of default probabilities and losses. Extensive research has introduced new modeling techniques, complemented by large-scale benchmarking studies consolidating the state-of-the-art. Today, quasi-standards such as gradient-boosting models paired with SHAP explainers have emerged, yet continuous improvement of risk models remains a top priority. Concurrently, rapid advancements in AI, most notably large language models, have disrupted predictive modeling paradigms. Foundation models, pretrained on extensive datasets from diverse domains, have demonstrated remarkable performance by leveraging prior knowledge. While prevalent in natural language processing and computer vision, foundation models for tabular data have only recently emerged. We conjecture that pretraining on out-of-domain data is particularly beneficial in small-data settings, such as SME lending or specialized corporate portfolios, and may help address longstanding challenges including low default portfolios and class imbalance. This paper benchmarks recently proposed tabular foundation models against a broad set of competitors, including established and advanced machine learning techniques, across two core tasks: PD and LGD modeling. Our evaluation encompasses various datasets, performance indicators, and experimental conditions. We find that tabular foundation models generally perform best across datasets and tasks. Moreover, they offer significant improvement in predictive performance as dataset size shrinks. These results are remarkable given that the models are tested out-of-the-box, without hyperparameter tuning, ensuring ease of use and mitigating computational costs.
匹配关键词: automated research
---

[ACADEMIC - ARXIV]
标题: Evidence-Grounded Frontier Mapping and Agentic Hypothesis Generation in Nanomedicine
作者: Christiaan G. A. Viviers, Koen de Bruin, Mirre M. Trines, Ayla M. Hokke, Roy van der Meel, Avi Schroeder, Twan Lammers, Willem J. M. Mulder, Fons van der Sommen
链接: https://arxiv.org/abs/2605.18144v1
完整摘要: Nanomedicine research spans delivery chemistry, immunology, imaging, biomaterials, and disease-specific translational science, yet its conceptual design space remains fragmented across a large and heterogeneous literature. To date, artificial intelligence in nanomedicine has focused primarily on property prediction and formulation optimization, with much less attention to evidence-grounded discovery support at the level of research direction selection. We introduce pArticleMap, a literature-mapping and research-hypothesis-generation system that combines article embeddings, similarity-graph analysis, sparse frontier extraction, structured evidence-pack retrieval, and an audited large-language-model (LLM) workflow for grounded ideation. Rather than forecasting future concept co-occurrence, pArticleMap targets low-density article-level bridge regions and cluster interfaces, then generates and scores citation-grounded hypotheses with large language models in an agentic setup. We evaluate the system with a retrospective realization benchmark (generate later literature under a historical cutoff) and a blinded human reader assessment layer across cue-conditioned nanomedicine tasks. Across 4 selected retrospective bundles, pArticleMap generated ideas and selected task-retained hypotheses (winner ideas) under the benchmark protocol. For task-level retained hypotheses, a pooled gold recovery rate of 10.8% was obtained, with a recall@10 of 15.9% and a future-neighborhood rate of 61.0%, indicating that the system often reached the correct forward-looking neighborhood (paper ideas) even without exact paper-level recovery. Human-agent agreement is modest overall, indicating that internal scoring is useful as a support signal but does not replace expert judgment. These results position pArticleMap as a conservative, evidence-grounded research assistant for nanomedicine.
匹配关键词: automated research
---

[ACADEMIC - ARXIV]
标题: iPOE: Interpretable Prompt Optimization via Explanations
作者: Jiahui Li, Sean Papay, Roman Klinger
链接: https://arxiv.org/abs/2605.18113v1
完整摘要: Prompt optimization has often been framed as a discrete search problem to find high-performing and robust instructions for an LLM. However, the search result might not make it transparent why and where specific prompt changes lead to performance gains. This is in contrast to how humans are instructed for annotation tasks. Here, researchers carefully design annotation guidelines, leading to enhanced annotation consistency. Our paper aims at joining these two approaches and introduces iPOE, a novel interpretable prompt optimization strategy via explanations. We guide the prompt optimization process by automatically created guidelines from explanations of annotation decisions (either automatically generated or from humans). This set of guidelines is furthermore optimized by as series of operations, including removing, adding, shuffling, and merging. The resulting prompt includes guidelines that instruct the annotation, making the decision process of the LLM and the optimization transparent. It therefore supports also laypeople in the area of prompt optimization, particularly in challenging domains requiring expertise. In our experiments on four datasets, we find that iPOE can improves over prompts without guidelines and with random selected guidelines by up to $31\%$ and $35\%$, respectively. Moreover, LLM explanations can replace human explanations in the proposed method.
匹配关键词: automated research
---

[ACADEMIC - ARXIV]
标题: 4DLidarOpen: An Open 4D FMCW Lidar Dataset for Motion-Aware Autonomous Driving
作者: Kane Qian, Xin Zhao, Yining Shi, Rujun Yan, Zhengqing Pan, Kaojin Zhu, Mengmeng Yang, Kai Sun, Diange Yang, Kun Jiang
链接: https://arxiv.org/abs/2605.18074v1
完整摘要: We present 4DLidarOpen, a large-scale open multi-modal dataset for autonomous driving, centered on 4D frequency-modulated continuous-wave (FMCW) Lidar sensing. Unlike conventional time-of-flight Lidar datasets that mainly provide geometric measurements, 4DLidarOpen includes point-wise radial velocity measurements from a forward-facing 4D FMCW Lidar, together with multiple Lidars of different types, including rotating, solid-state, and blind-spot variants, surround-view cameras, and 6-DOF ego-vehicle poses. The dataset was collected in complex urban environments in Beijing and covers dense pedestrian interactions, congested traffic, high-speed driving, and unprotected maneuvers. 4DLidarOpen provides synchronized multi-sensor data and 3D bounding-box annotations with persistent track IDs across five object categories. A hybrid annotation strategy is adopted, where large-scale auto-labeled data support scalable training and human experts refine annotations for the human-annotated training and validation sets. Based on this dataset, we establish benchmarks for 3D object detection, birds-eye view (BEV) segmentation and flow prediction, and motion forecasting with planning. Extensive experiments show that direct velocity measurements from 4D FMCW Lidar provide complementary motion cues for dynamic-scene understanding. Compared with geometric-only sensing, the velocity-aware representation improves motion-related perception and downstream forecasting and planning, especially in scenarios involving vulnerable road users and fast-moving objects. These results indicate that 4D FMCW Lidar is a promising sensing modality for motion-aware autonomous driving. The dataset and evaluation toolkit are publicly released to support research on 4D scene understanding, multi-Lidar fusion, and velocity-aware perception and planning.
匹配关键词: automated research
---

[ACADEMIC - ARXIV]
标题: Best Segmentation Buddies for Image-Shape Correspondence
作者: Itai Lang, Dongwei Lyu, Dale Decatur, Rana Hanocka
链接: https://arxiv.org/abs/2605.18193v1
完整摘要: Finding correspondences is a fundamental and extensively researched problem in computer vision and graphics. In this work, we examine the underexplored task of estimating segmentation-to-segmentation correspondence between images in the wild and untextured 3D shapes. This task is highly challenging due to substantial differences in appearance, geometry, and viewpoint. Our approach bridges the cross-modality gap by linking pixels in the image segment to vertices in the corresponding semantic part of the 3D shape. To achieve this, we first distill deep visual features from a 2D vision model onto the 3D shape surface, allowing for the computation of feature similarity between image pixels and shape vertices. Then, we identify Best Segmentation Buddies, vertices whose most similar image pixel lies within the image segmentation region, enabling the reliable discovery of vertices in semantically corresponding shape parts. Finally, we leverage distilled 3D features from the 2D image segmentation model to segment the shape directly in 3D, bootstrapping the correspondence process. We demonstrate the generality and robustness of our approach across a wide range of image-shape pairs, showcasing accurate and semantically meaningful correspondences. Our project page is at https://threedle.github.io/bsb/.
匹配关键词: scientific discovery
---

[ACADEMIC - ARXIV]
标题: Evidence-Grounded Frontier Mapping and Agentic Hypothesis Generation in Nanomedicine
作者: Christiaan G. A. Viviers, Koen de Bruin, Mirre M. Trines, Ayla M. Hokke, Roy van der Meel, Avi Schroeder, Twan Lammers, Willem J. M. Mulder, Fons van der Sommen
链接: https://arxiv.org/abs/2605.18144v1
完整摘要: Nanomedicine research spans delivery chemistry, immunology, imaging, biomaterials, and disease-specific translational science, yet its conceptual design space remains fragmented across a large and heterogeneous literature. To date, artificial intelligence in nanomedicine has focused primarily on property prediction and formulation optimization, with much less attention to evidence-grounded discovery support at the level of research direction selection. We introduce pArticleMap, a literature-mapping and research-hypothesis-generation system that combines article embeddings, similarity-graph analysis, sparse frontier extraction, structured evidence-pack retrieval, and an audited large-language-model (LLM) workflow for grounded ideation. Rather than forecasting future concept co-occurrence, pArticleMap targets low-density article-level bridge regions and cluster interfaces, then generates and scores citation-grounded hypotheses with large language models in an agentic setup. We evaluate the system with a retrospective realization benchmark (generate later literature under a historical cutoff) and a blinded human reader assessment layer across cue-conditioned nanomedicine tasks. Across 4 selected retrospective bundles, pArticleMap generated ideas and selected task-retained hypotheses (winner ideas) under the benchmark protocol. For task-level retained hypotheses, a pooled gold recovery rate of 10.8% was obtained, with a recall@10 of 15.9% and a future-neighborhood rate of 61.0%, indicating that the system often reached the correct forward-looking neighborhood (paper ideas) even without exact paper-level recovery. Human-agent agreement is modest overall, indicating that internal scoring is useful as a support signal but does not replace expert judgment. These results position pArticleMap as a conservative, evidence-grounded research assistant for nanomedicine.
匹配关键词: scientific discovery
---

[ACADEMIC - ARXIV]
标题: Real-time Multi-instrument Autonomous Discovery of Novel Phase-change Memory Materials
作者: Chih-Yu Lee, Haotong Liang, Ryan Kim, Austin McDannald, Carlos A Rios Ocampo, A. Gilad Kusne, Ichiro Takeuchi
链接: https://arxiv.org/abs/2605.18033v1
完整摘要: Autonomous labs enable the integration of automated experiment execution, data analysis and decision making. The main challenge remains the integration of diverse data streams from multiple instruments, where the data is often heterogeneous and unsynchronized. The standard learning process of undetermined synthesis-process-structure-property relationships (SPSPR) usually relies on post-experiment analysis after data is fully collected, not during live experiments, and decision making is carried out independently across characterization equipment. Here, we demonstrate the Multi-instrument Autonomous Discovery (MAD) framework -- combining structural property mapping and functional property optimization simultaneously in a closed-loop manner. As an example, we applied MAD to phase change memory (PCM) materials, and, in particular on the Mn-Sb-Te ternary, a previously unexplored materials system for PCM. A multi-output model is employed to merge data from x-ray diffraction (XRD) and electrical resistance measurements simultaneously through a co-regionalization kernel that models the relationship between them. The output probabilistic posterior and uncertainty quantification facilitate decision making with shared knowledge, while the goals are different across tasks. We aimed to maximize the knowledge of crystal structure distribution using non-negative matrix factorization (NMF), while in parallel, we find the composition with the maximum resistance value, an important figure of merit for PCM. Leveraging MAD, we found promising electrical PCMs and identified the SPSPR within 25 closed-loop iterations, corresponding to a seven-fold speed-up. The framework opens a new path of study in large-scale autonomous facilities, where future experiments can be run in parallel together, not independently.
匹配关键词: scientific discovery
---

[ACADEMIC - ARXIV]
标题: Semantic Reranking at Inference Time for Hard Examples in Rhetorical Role Labeling
作者: Anas Belfathi, Nicolas Hernandez, Laura Monceaux, Warren Bonnard, Richard Dufour
链接: https://arxiv.org/abs/2605.18007v1
完整摘要: Rhetorical Role Labeling (RRL) assigns a functional role to each sentence in a document and is widely used in legal, medical, and scientific domains. While language models (LMs) achieve strong average performance, they remain unreliable on hard examples, where prediction confidence is low. Existing approaches typically handle uncertainty implicitly and treat labels as discrete identifiers, overlooking the semantic information encoded in label names. We introduce RISE, an inference-time semantic reranking framework that leverages label semantics to refine predictions on hard instances. RISE automatically identifies low-confidence predictions and reranks model outputs using contrastively learned label representations, without retraining or modifying the underlying model. Experiments on eight domain-specific RRL datasets with seven LMs, including encoder-based and causal architectures, show an average gain of +9.15 macro-F1 points on hard examples. For explainability, we further propose manual hardness annotations to study difficulty from both model and human perspectives, revealing a moderate agreement with Cohen's kappa = 0.40.
匹配关键词: scientific discovery
---

[ACADEMIC - ARXIV]
标题: RL4RLA: Teaching ML to Discover Randomized Linear Algebra Algorithms Through Curriculum Design and Graph-Based Search
作者: Jinglong Xiong, Xiaotian Liu, Ruoxin Wang, Zihang Liu, Yefan Zhou, Yujun Yan, Yaoqing Yang
链接: https://arxiv.org/abs/2605.18004v1
完整摘要: Randomized linear algebra (RLA) algorithms are a modern class of numerical linear algebra techniques that play an essential role in scientific computing and machine learning, with broad and growing adoption. However, their discovery remains mostly a manual process that requires deep expert knowledge and inspiration. While Reinforcement Learning (RL) offers a pathway to automation, standard approaches struggle with sparse reward landscapes and vast search spaces inherent to high-performing RLA algorithms. In this paper, we present RL4RLA, a general RL framework that automates the discovery of interpretable, symbolic RLA algorithms. Unlike black-box approaches, our method builds explicit algorithms from basic linear algebra primitives, ensuring verifiable and implementable representations. To enable efficient discovery, we introduce: (1) a numerical curriculum that progressively increments problem difficulty to encode inductive bias specific to the RLA domain; (2) Monte Carlo Graph Search, which optimizes exploration by identifying and merging equivalent partial algorithms. We demonstrate that RL4RLA rediscovers state-of-the-art methods, including sketch-and-precondition solvers, Randomized Kaczmarz, and Newton Sketch, and can be targeted to produce algorithms optimized for specific trade-offs between accuracy, speed, and stability. Code is available at https://github.com/Tim-Xiong/RL4RLA.
匹配关键词: scientific discovery
---

[ACADEMIC - ARXIV]
标题: Context Memorization for Efficient Long Context Generation
作者: Yasuyuki Okoshi, Hao Mark Chen, Guanxi Lu, Hongxiang Fan, Masato Motomura, Daichi Fujiki
链接: https://arxiv.org/abs/2605.18226v1
完整摘要: Modern large language model (LLM) applications increasingly rely on long conditioning prefixes to control model behavior at inference time. While prefix-augmented inference is effective, it incurs two structural limitations: i) the prefix's influence fades as generation proceeds, and ii) attention computation over the prefix scales linearly with its length. Existing approaches either keep the prefix in attention while compressing it, or internalize it into model parameters through gradient-based training. The former still attends to the prefix at inference, while the latter is training-intensive and ill-suited to prefix updates. To address these issues, we propose attention-state memory, a training-free approach that externalizes the prefix into a lightweight, lookup-based memory of precomputed attention states between prefix and query tokens. On ManyICLBench with LLaMA-3.1-8B, our method improves accuracy over in-context learning at 1K-8K memory budgets while reducing attention latency by 1.36x at 8K, and surpasses full-attention RAG performance on NBA benchmark using only 20% of its memory footprint.
匹配关键词: hypothesis generation
---

[ACADEMIC - ARXIV]
标题: EgoInteract: Synthetic Egocentric Videos Generation for Interaction Understanding and Anticipation
作者: Rosario Leonardi, Francesco Ragusa, Daniele Materia, Alessandro Passanisi, James Fort, Jakob Engel, Giovanni Maria Farinella
链接: https://arxiv.org/abs/2605.18214v1
完整摘要: Collecting large-scale egocentric video datasets with dense spatial and temporal annotations is costly, slow, and often constrained by environmental biases, privacy constraints, and limited coverage of interaction patterns. While synthetic data has shown strong potential in several vision domains, its use for egocentric perception remains relatively underexplored, especially for tasks requiring temporally coherent human-object interactions. In this work, we introduce EgoInteract, a controllable simulator for egocentric video generation designed to model fine-grained egocentric interactions and their temporal dynamics. The simulator enables precise control over camera, human body and hand motion, object manipulation, and scene composition across diverse environments. Building on this framework, we generate a synthetic egocentric video dataset with dense spatial and temporal annotations for temporal action segmentation, next-active object detection, interaction anticipation, and hand-object interaction detection. We evaluate models trained with simulated data on multiple real-world egocentric benchmarks spanning diverse environments, object categories, and interaction patterns. Results show consistent improvements over strong baselines across tasks and datasets, demonstrating the effectiveness and transferability of our simulation-based approach.
匹配关键词: hypothesis generation
---

[ACADEMIC - ARXIV]
标题: Leveraging Graph Structure in Seq2Seq Models for Knowledge Graph Link Prediction
作者: Luu Huu Phuc, Ratan Bahadur Thapa, Mojtaba Nayyeri, Jingcheng Wu, Evgeny Kharlamov, Steffen Staab
链接: https://arxiv.org/abs/2605.18211v1
完整摘要: We introduce Graph-Augmented Sequence-to-Sequence (GA-S2S), a novel framework that integrates a T5-small encoder-decoder with a Relational Graph Attention Network (RGAT) to improve link prediction in knowledge graphs. While existing Seq2Seq models rely solely on surface-level textual descriptions of entities and relations and at best, flatten the neighborhoods of a query entity into a single linear sequence, thereby discarding the inherent graph structure, GA-S2S jointly encodes both textual features and the full $k$-hop subgraph topology surrounding the query entity. By integrating raw encoder outputs with RGAT's relation-aware embeddings, our model captures and leverages richer multi-hop relational patterns and textual information. Our preliminary experiments on the CoDEx dataset demonstrate that GA-S2S outperforms competitive Seq2Seq-based baseline models, achieving up to a 19\% relative gain in link prediction accuracy.
匹配关键词: hypothesis generation
---

[ACADEMIC - ARXIV]
标题: SPATIOROUTE: Dynamic Prompt Routing for Zero-Shot Spatial Reasoning
作者: Pawat Chunhachatrachai, Gueter Josmy Faure, Hung-Ting Su, Winston H. Hsu
链接: https://arxiv.org/abs/2605.18209v1
完整摘要: Spatial question answering over egocentric video is a challenging task that requires Vision-Language Models (VLMs) to reason about 3D object positions, scene affordances, and directional relationships, particularly in the zero-shot setting where no task-specific fine-tuning is available. We introduce SpatioRoute, a dynamic prompt generation approach that routes each incoming question to a semantically tailored prompt template -- without any additional training, fine-tuning, or 3D sensor input. SpatioRoute operates in two complementary modes: SpatioRoute-R, a rule-based router that deterministically maps question typologies (e.g., What, Is, How, Can, Which) to specialized prompt templates; and SpatioRoute-L, an LLM-driven approach that generates task-specific prompts from the question and situational context alone, with no video input at routing time. We evaluate SpatioRoute on the SQA3D benchmark across VLMs spanning model families. SpatioRoute achieves consistent overall accuracy gains up to 5% over fixed prompt baselines, establishing a new state-of-the-art for zero-shot video-only spatial VQA without requiring 3D point-cloud inputs. As an additional finding, we observe that Chain-of-Thought (CoT) prompting, implemented via the Think it Twice architecture, consistently degrades performance in this setting on Qwen series models, confirming that question-aware routing is more effective than uniform reasoning instructions for spatial video understanding.
匹配关键词: hypothesis generation
---

[ACADEMIC - ARXIV]
标题: Forward-Learned Discrete Diffusion: Learning how to noise to denoise faster
作者: Grigory Bartosh, Teodora Pandeva, Sushrut Karmalkar, Javier Zazo
链接: https://arxiv.org/abs/2605.18204v1
完整摘要: Discrete diffusion models are a powerful class of generative models with strong performance across many domains. For efficiency, however, discrete diffusion typically parameterizes the generative (reverse) process with factorized distributions, which makes it difficult for the model to learn the target process in a small number of steps and necessitates a long, computationally expensive sampling procedure. To reduce the gap between the target and model distributions and enable few-step generation, we propose Forward-Learned Discrete Diffusion (FLDD), which introduces discrete diffusion with a learnable forward (noising) process. Rather than fixing a Markovian forward chain, we adopt a non-Markovian formulation with learnable marginal and posterior distributions. This allows the generative process to remain factorized while matching the target defined by the noising process. We train all parameters end-to-end under the standard variational objective. Experiments on various benchmarks show that, for a given number of sampling steps, our approach produces a higher quality samples than conventional discrete diffusion models using the same reverse parameterization.
匹配关键词: hypothesis generation
---

[ACADEMIC - ARXIV]
标题: Leveraging Graph Structure in Seq2Seq Models for Knowledge Graph Link Prediction
作者: Luu Huu Phuc, Ratan Bahadur Thapa, Mojtaba Nayyeri, Jingcheng Wu, Evgeny Kharlamov, Steffen Staab
链接: https://arxiv.org/abs/2605.18211v1
完整摘要: We introduce Graph-Augmented Sequence-to-Sequence (GA-S2S), a novel framework that integrates a T5-small encoder-decoder with a Relational Graph Attention Network (RGAT) to improve link prediction in knowledge graphs. While existing Seq2Seq models rely solely on surface-level textual descriptions of entities and relations and at best, flatten the neighborhoods of a query entity into a single linear sequence, thereby discarding the inherent graph structure, GA-S2S jointly encodes both textual features and the full $k$-hop subgraph topology surrounding the query entity. By integrating raw encoder outputs with RGAT's relation-aware embeddings, our model captures and leverages richer multi-hop relational patterns and textual information. Our preliminary experiments on the CoDEx dataset demonstrate that GA-S2S outperforms competitive Seq2Seq-based baseline models, achieving up to a 19\% relative gain in link prediction accuracy.
匹配关键词: autonomous experiment
---

[ACADEMIC - ARXIV]
标题: Forward-Learned Discrete Diffusion: Learning how to noise to denoise faster
作者: Grigory Bartosh, Teodora Pandeva, Sushrut Karmalkar, Javier Zazo
链接: https://arxiv.org/abs/2605.18204v1
完整摘要: Discrete diffusion models are a powerful class of generative models with strong performance across many domains. For efficiency, however, discrete diffusion typically parameterizes the generative (reverse) process with factorized distributions, which makes it difficult for the model to learn the target process in a small number of steps and necessitates a long, computationally expensive sampling procedure. To reduce the gap between the target and model distributions and enable few-step generation, we propose Forward-Learned Discrete Diffusion (FLDD), which introduces discrete diffusion with a learnable forward (noising) process. Rather than fixing a Markovian forward chain, we adopt a non-Markovian formulation with learnable marginal and posterior distributions. This allows the generative process to remain factorized while matching the target defined by the noising process. We train all parameters end-to-end under the standard variational objective. Experiments on various benchmarks show that, for a given number of sampling steps, our approach produces a higher quality samples than conventional discrete diffusion models using the same reverse parameterization.
匹配关键词: autonomous experiment
---

[ACADEMIC - ARXIV]
标题: Concise and Logically Consistent Conformal Sets for Neuro-Symbolic Concept-Based Models
作者: Samuele Bortolotti, Emanuele Marconato, Andrea Pugnana, Andrea Passerini, Stefano Teso
链接: https://arxiv.org/abs/2605.18202v1
完整摘要: Neuro-Symbolic Concept-based Models (NeSy-CBMs) are a family of architectures that integrate neural networks with symbolic reasoning for enhanced reliability in high-stakes applications. They work by first extracting high-level concepts from the input and then inferring a task label from these compatibly with given logical constraints. Yet, their label and concept predictions can be overconfident, making it difficult for stakeholders to gauge when the model's decisions can be trusted. We address this issue by integrating ideas from Conformal Prediction (CP), a framework providing rigorous, distribution-free coverage guarantees. We formalize three desiderata -- consistency, coverage, and conciseness -- that any conformal method for NeSy-CBMs should satisfy, and show that existing approaches fall short of at least one. We then introduce COCOCO, a post-hoc framework that conformalizes concepts and labels jointly and reconciles them via a single deduction-abduction revision step. COCOCO satisfies all three desiderata, retains distribution-free coverage, is robust to imperfect knowledge and supports user-specified size budgets. Our experiments on 8 data sets highlight how COCOCO compares favorably against competitors and natural baselines in terms of performance and set size.
匹配关键词: autonomous experiment
---

[ACADEMIC - ARXIV]
标题: RGB-only Active 3D Scene Graph Generation for Indoor Mobile Robots
作者: Giorgia Modi, Davide Buoso, Giuseppe Averta, Daniele De Martini
链接: https://arxiv.org/abs/2605.18197v1
完整摘要: Current approaches to 3D scene graph generation rely on dedicated depth sensors, such as LiDAR or RGB-D cameras, for metric 3D reconstruction. This limits deployment to specialized robotic platforms and excludes settings where only RGB cameras are available, such as fixed external infrastructure. Existing pipelines also typically operate on passively collected observation trajectories, rather than selecting viewpoints based on the partially built scene representation, and therefore fail to effectively exploit the semantic and spatial information encoded within the graph during exploration. This paper presents a fully visual framework for the active, incremental construction of 3D scene graphs from RGB input only, addressing both limitations. The proposed approach unifies perception and planning around a shared structured representation that captures object semantics, 3D geometry, relational context, and information from multiple viewpoints. Because the framework is hardware-agnostic and relies only on RGB observations, it can incorporate inputs from both onboard robot cameras and fixed external cameras within the same representation. Experiments on the Replica dataset show that the RGB-only pipeline achieves F1-score parity with baselines using ground-truth depth. Active exploration experiments on ReplicaCAD further show that semantic-driven viewpoint selection detects more than twice as many objects as a geometric frontier-based baseline under the same exploration budget. Finally, the external-camera setting demonstrates that complementary RGB views can effectively bootstrap the scene graph and improve contextual understanding at no additional exploration cost.
匹配关键词: autonomous experiment
---

[ACADEMIC - ARXIV]
标题: View-Aware Semantic Alignment for Aerial-Ground Person Re-Identification
作者: Quan Zhang, Zeqiang Cai, Peiming Zhao, Jingze Wu, Cailun Wu, Hongbo Chen, Jianhuang Lai
链接: https://arxiv.org/abs/2605.18192v1
完整摘要: Aerial-Ground Person Re-Identification (AGPReID) remains highly challenging due to drastic viewpoint variations between drones and fixed cameras. Existing methods typically follow a view-invariant paradigm, aligning shared features across views to achieve robustness. However, view-invariant inherently enforces part-level alignment, which ignores view-specific cues and discriminative identity information. To this end, this work proposes ViSA (View-aware Semantic Alignment), a view-aware framework that achieves cross-view semantic consistency containing an Expert-driven Token Generation Module (ETGM) and a Dual-branch Local Fusion Module (DLFM). Technically, the former constructs a set of view-aware experts to generate adaptive semantic queries that perceive viewpoint-specific patterns, while the latter leverages graph reasoning to extract and align local regions responsive to different experts. Extensive experiments on three AGPReID benchmarks including AG-ReID.v2, CARGO and LAGPeR demonstrate that ViSA consistently achieves superior performance, with a notable 10.06\% mAP improvement on the challenging CARGO cross-view protocol. The code is available at \href{https://github.com/Cat-Zero/ViSA}{https://github.com/Cat-Zero/ViSA}.
匹配关键词: autonomous experiment
---

[ACADEMIC - ARXIV]
标题: pyforce-1.0.0: Python Framework for data-driven model Order Reduction of multi-physiCs problEms
作者: Stefano Riva, Yantao Luo, Carolina Introini, Antonio Cammi
链接: https://arxiv.org/abs/2605.18082v1
完整摘要: pyforce is a Python package implementing Data-Driven Reduced Order Modelling techniques for applications to multi-physics problems, mainly set in the Nuclear Engineering world. The package is part of the ROSE (Reduced Order modelling with data-driven techniques for multi-phySics problEms): mathematical algorithms aimed at reducing the complexity of multi-physics models (for nuclear reactors applications), at searching for optimal sensor positions and at integrating real measures to improve the knowledge on the physical systems. With respect to the previous original implementation based on dolfinx package (v0.6.0), version 1.0.0 of pyforce has been completely re-written using pyvista as backend for mesh importing, computing integrals, and visualisation of results; in addition, functions are stored as numpy arrays, improving the ease of use of the package. This choice allows to use pyforce with any software solver able to export results in VTK format.
匹配关键词: lab automation
---

[ACADEMIC - ARXIV]
标题: A-ProS: Towards Reliable Autonomous Programming Through Multi-Model Feedback
作者: Anika Tabassum, Md Sifat Hossain, Md. Fahim Arefin, Tariqul Islam, Tarannum Shaila Zaman
链接: https://arxiv.org/abs/2605.18073v1
完整摘要: Large Language Models (LLMs) demonstrate strong potential for automated code generation, yet their ability to iteratively refine solutions using execution feedback remains underexplored. Competitive programming offers an ideal testbed for this investigation, as it demands end-to-end algorithmic reasoning, precise implementation under strict computational constraints, and complete functional correctness with rigorous evaluation. In this paper, we present A-ProS, an autonomous AI agent that solves competitive programming problems through a hybrid multi-model feedback framework separating solution generation from specialized debugging. A-ProS combines ChatGPT-based generators (GPT-4 and GPT-5) with three debugging critics: Codestral-2508, Llama-3.3-70B, and DeepSeek-R1, under a 2 x 3 factorial design. We evaluate six workflows on 367 problems from ICPC World Finals (2011-2024) and Codeforces (rated 1200-1800). The results show that GPT-5 workflows improve from 39 initial accepted solutions to 85-90 after three refinement rounds, while GPT-4 improves from 15 to 31-38. A controlled ablation on 47 problems shows that stateful refinement outperforms stateless approaches by 8.5-10.6 percentage points and reduces repeated failures by up to 3.5x. Compared to baseline agent loops, A-ProS achieves over 2x greater gains, highlighting the importance of persistent context and multi-model feedback for reliable autonomous program synthesis.
匹配关键词: lab automation
---

[ACADEMIC - ARXIV]
标题: DocOS: Towards Proactive Document-Guided Actions in GUI Agents
作者: Jingjing Liu, Ziye Huang, Zihao Cheng, Zeming Liu, Jiahong Wu, Yuhang Guo, Kehai Chen, Yunhong Wang, Haifeng Wang
链接: https://arxiv.org/abs/2605.18048v1
完整摘要: While Graphical User Interface (GUI) agents have shown promising performance in automated device interaction, they primarily depend on static parametric knowledge from pre-training or instruction tuning. This reliance fundamentally limits their ability to handle long-tailed tasks that require explicit procedural knowledge absent from model parameters, often forcing agents to resort to inefficient and brittle trial-and-error exploration. To mitigate this limitation, we introduce \textbf{Proactive Document-Guided Action} for GUI agents in dynamic, open-web environments, a novel paradigm that mirrors human problem-solving by enabling agents to autonomously search for relevant documentation to resolve long-tailed tasks. To evaluate agents' capability in this paradigm, we propose \textbf{DocOS}, a benchmark designed to assess document-guided problem solving in fully interactive environments. DocOS requires agents to autonomously navigate a web browser, locate relevant online documentation, comprehend procedural instructions, and faithfully ground them into executable GUI actions. Extensive experiments reveal that progress is strictly constrained by dual bottlenecks: agents struggle to reliably locate relevant information during proactive search and frequently fail to faithfully ground retrieved instructions into precise actions, pointing toward document-guided interaction as a crucial pathway for enabling self-evolving GUI agents in dynamic environments.
匹配关键词: lab automation
---

[ACADEMIC - ARXIV]
标题: Real-time Multi-instrument Autonomous Discovery of Novel Phase-change Memory Materials
作者: Chih-Yu Lee, Haotong Liang, Ryan Kim, Austin McDannald, Carlos A Rios Ocampo, A. Gilad Kusne, Ichiro Takeuchi
链接: https://arxiv.org/abs/2605.18033v1
完整摘要: Autonomous labs enable the integration of automated experiment execution, data analysis and decision making. The main challenge remains the integration of diverse data streams from multiple instruments, where the data is often heterogeneous and unsynchronized. The standard learning process of undetermined synthesis-process-structure-property relationships (SPSPR) usually relies on post-experiment analysis after data is fully collected, not during live experiments, and decision making is carried out independently across characterization equipment. Here, we demonstrate the Multi-instrument Autonomous Discovery (MAD) framework -- combining structural property mapping and functional property optimization simultaneously in a closed-loop manner. As an example, we applied MAD to phase change memory (PCM) materials, and, in particular on the Mn-Sb-Te ternary, a previously unexplored materials system for PCM. A multi-output model is employed to merge data from x-ray diffraction (XRD) and electrical resistance measurements simultaneously through a co-regionalization kernel that models the relationship between them. The output probabilistic posterior and uncertainty quantification facilitate decision making with shared knowledge, while the goals are different across tasks. We aimed to maximize the knowledge of crystal structure distribution using non-negative matrix factorization (NMF), while in parallel, we find the composition with the maximum resistance value, an important figure of merit for PCM. Leveraging MAD, we found promising electrical PCMs and identified the SPSPR within 25 closed-loop iterations, corresponding to a seven-fold speed-up. The framework opens a new path of study in large-scale autonomous facilities, where future experiments can be run in parallel together, not independently.
匹配关键词: lab automation
---

[ACADEMIC - ARXIV]
标题: What Matters for Grocery Product Retrieval with Open Source Vision Language Models
作者: Emmanuel G. Maminta, Rowel O. Atienza
链接: https://arxiv.org/abs/2605.18029v1
完整摘要: Multimodal product retrieval (MPR) underpins checkout-free retail and automated inventory systems, yet it demands fine-grained SKU discrimination that standard vision-language benchmarks fail to capture. We present the first systematic zero-shot evaluation of 190 open-source VLMs on the MPR task of the GroceryVision Challenge, isolating pre-training data, architecture, and input resolution. Our analysis yields three actionable findings. \textbf{(1) Data quality trumps scale.} Switching from raw web-scrapes to filtered datasets delivers up to 16.6\% accuracy gains, exceeding the benefit of doubling model parameters. \textbf{(2) Efficient models can win.} MobileCLIP-B (150M parameters) outperforms 351M counterparts trained on noisy data. We introduce \textit{semantic power density} ($φ$), an efficiency metric that penalizes sub-threshold accuracy. \textbf{(3) A precision gap persists.} State-of-the-art models achieve 94.5\% Recall@5 but suffer a 17.5\% drop at Recall@1, revealing that contrastive embeddings cluster categories effectively but fail to rank visually similar SKUs. Code and evaluation scripts are available at \url{https://github.com/upeee/openmpr}.
匹配关键词: lab automation
---

[ACADEMIC - ARXIV]
标题: Are Sparse Autoencoder Benchmarks Reliable?
作者: David Chanin
链接: https://arxiv.org/abs/2605.18229v1
完整摘要: Sparse autoencoders (SAEs) are a core interpretability tool for large language models, and progress on SAE architectures depends on benchmarks that reliably distinguish better SAEs from worse ones. We audit the SAE quality metrics in SAEBench, the de-facto standard SAE evaluation suite, through three complementary lenses: reseed noise on a fixed SAE, ground-truth correlation on synthetic SAEs, and discriminability across training trajectories. We find that two of these metrics, Targeted Probe Perturbation (TPP) and Spurious Correlation Removal (SCR), fail multiple lenses at their canonical settings and should not be used to evaluate SAEs. The other metrics show higher reseed noise and lower discriminability than the field assumes. The sae-probes variant of $k$-sparse probing is the most reliable metric we tested, but even sae-probes struggles to separate variants of the same SAE architecture. Our results show the field needs better SAE benchmarks.
匹配关键词: AI for science
---

[ACADEMIC - ARXIV]
标题: Context Memorization for Efficient Long Context Generation
作者: Yasuyuki Okoshi, Hao Mark Chen, Guanxi Lu, Hongxiang Fan, Masato Motomura, Daichi Fujiki
链接: https://arxiv.org/abs/2605.18226v1
完整摘要: Modern large language model (LLM) applications increasingly rely on long conditioning prefixes to control model behavior at inference time. While prefix-augmented inference is effective, it incurs two structural limitations: i) the prefix's influence fades as generation proceeds, and ii) attention computation over the prefix scales linearly with its length. Existing approaches either keep the prefix in attention while compressing it, or internalize it into model parameters through gradient-based training. The former still attends to the prefix at inference, while the latter is training-intensive and ill-suited to prefix updates. To address these issues, we propose attention-state memory, a training-free approach that externalizes the prefix into a lightweight, lookup-based memory of precomputed attention states between prefix and query tokens. On ManyICLBench with LLaMA-3.1-8B, our method improves accuracy over in-context learning at 1K-8K memory budgets while reducing attention latency by 1.36x at 8K, and surpasses full-attention RAG performance on NBA benchmark using only 20% of its memory footprint.
匹配关键词: AI for science
---

[ACADEMIC - ARXIV]
标题: A Simplex Witness Certificate for Constant Collapse in Variational Autoencoders
作者: Zegu Zhang, Jianhua Peng, Jian Zhang
链接: https://arxiv.org/abs/2605.18224v1
完整摘要: This note studies exact constant collapse in variational autoencoders, where the encoder mean becomes independent of the input. The goal is to make this specific failure mode pre-designable, monitorable during training, and certifiable after training. The prior is kept as the standard Gaussian. Given a fixed teacher posterior, we attach to the latent mean a fixed simplex witness head. The resulting teacher-student alignment loss has an exact constant-predictor baseline equal to the teacher information. If the alignment loss is below this baseline, the latent mean cannot be input-independent constant collapsed. The simplex witness also has a closed-form inverse. Any full-support teacher posterior can be represented by embedding its centered log-odds into the latent space. This gives an explicit latent energy cost and explains when the alignment loss can be made small. A computable view gap handles the case where teacher targets are computed from a different view. Thus exact constant collapse is converted from an after-the-fact training pathology into a design-and-certificate problem.
匹配关键词: AI for science
---

[ACADEMIC - ARXIV]
标题: Contextual Biasing for Streaming ASR via CTC-based Word Spotting
作者: Kai-Chen Tsai, Tien-Hong Lo, Yun-Ting Sun, Berlin Chen
链接: https://arxiv.org/abs/2605.18222v1
完整摘要: Contextual biasing is essential to improving the recognition of rare and domain-specific words in an automatic speech recognition (ASR) system. While numerous methods have been proposed in recent years, most of them focus on offline settings and do not explicitly address the challenges of streaming ASR. For example, CTC-based word spotting (CTC-WS) have demonstrated strong performance by directly detecting keywords from CTC log-probabilities, but they are limited to offline processing and require access to the full utterance. In This work, we present a streaming extension of CTC-WS for real-time contextual biasing. Our method maintains active keyword paths across audio chunks using a stateful token passing algorithm, enabling the detection of keywords that span multiple chunks. To ensure low latency and stable output, we introduce an incremental commitment mechanism that only emits segments guaranteed not to be affected by future audio, while deferring uncertain regions. This method naturally integrates with streaming ASR pipelines and does not require modifications to the underlying acoustic model or additional training, making it practical for real-world deployment. Experimental results show that our method reduces overall WER and effectively improves keyword F-score, demonstrating its effectiveness for real-time ASR applications.
匹配关键词: AI for science
---

[ACADEMIC - ARXIV]
标题: SIREM: Speech-Informed MRI Reconstruction with Learned Sampling
作者: Md Hasan, Nyvenn Castro, Daiqi Liu, Lukas Mulzer, Jana Hutter, Jonghye Woo, Moritz Zaiss, Andreas Maier, Paula A. Perez-Toro
链接: https://arxiv.org/abs/2605.18221v1
完整摘要: Real-time magnetic resonance imaging (rtMRI) of speech production enables non-invasive visualization of dynamic vocal-tract motion and is valuable for speech science and clinical assessment. However, rtMRI is fundamentally constrained by trade-offs among spatial resolution, temporal resolution, and acquisition speed, often leading to undersampled k-space measurements and degraded reconstructions. We propose SIREM, a speech-informed MRI reconstruction framework that uses synchronized speech as a cross-modal prior. The central idea is that vocal-tract configurations during speech are correlated with the produced acoustics, making part of the image content predictable from audio. SIREM models each frame as a fusion of an audio-driven component and an MRI-driven component through a spatial weighting map. The audio branch predicts articulator-related structure from speech, while the MRI branch reconstructs complementary content from measured k-space data. We further introduce a learnable soft weighting profile over spiral arms, enabling a differentiable study of how k-space arm usage interacts with speech-informed fusion. This yields a unified multimodal formulation that combines audio-driven prediction, MRI reconstruction, and sampling adaptation. We evaluate SIREM on the USC speech rtMRI benchmark against standard baselines, including gridding, wavelet-based compressed sensing, and total variation. SIREM introduces a speech-informed reconstruction paradigm that operates in a substantially higher-throughput regime than iterative methods while preserving anatomically plausible vocal-tract structure. These results establish an initial benchmark for multimodal speech-informed rtMRI reconstruction and highlight the potential of synchronized speech as an auxiliary prior for fast reconstruction. The source code is available at https://github.com/mdhasanai/SIREM
匹配关键词: AI for science
---

[ACADEMIC - ARXIV]
标题: Venom: A PyTorch Generative Modeling Toolkit
作者: Liang Yan
链接: https://arxiv.org/abs/2605.17605v1
完整摘要: Modern generative modeling has grown into a broad collection of related but often separately implemented paradigms, including denoising diffusion models, score-based stochastic differential equations, flow matching, variational autoencoders, normalizing flows, adversarial models, and energy-based models. For newcomers, this fragmentation makes it difficult to compare training objectives, inference procedures, sampling algorithms, and conditioning mechanisms within a single coherent codebase. We introduce V ENOM, an educational PyTorch toolkit that implements representative generative modeling families under a unified, MNIST-first interface. V ENOM emphasizes breadth, readability, reproducible entry points, and consistent training and sampling APIs rather than large-scale performance engineering. The package currently includes diffusion and score-based models, flow matching and one-step generators, variational autoencoders, normalizing flows, generative adversarial networks, and energy-based models. It provides separate training and sampling scripts, classifier and classifier-free guidance examples, bilingual tutorial notebooks, and a model-family organization that supports teaching, prototyping, and lightweight benchmarking.
匹配关键词: PyTorch
---

[ACADEMIC - ARXIV]
标题: MiniGPT: Rebuilding GPT from First Principles
作者: Jibin Joseph
链接: https://arxiv.org/abs/2605.17398v1
完整摘要: This paper presents MiniGPT, a compact from-scratch implementation of GPT-style autoregressive language modeling in PyTorch. The aim is to rebuild the core GPT pipeline from first principles after studying the design of nanoGPT by Andrej Karpathy, while keeping the model and training code independently written in a single notebook. MiniGPT implements token and positional embeddings, causal multi-head self-attention, pre-LayerNorm Transformer blocks, residual connections, feed-forward MLP layers, next-token cross-entropy training (teacher forcing), validation tracking, checkpoint selection, and autoregressive text generation. This paper evaluates the implementation on Tiny Shakespeare dataset using character-level tokenization. A baseline 0.83M-parameter model reaches a validation loss of 1.7236 after 3000 training iterations. A stronger 10.77M-parameter configuration, using a larger context length and improved training settings, reaches a best validation loss of 1.4780 and generates text with recognizable Shakespeare-style dialogue structure. MiniGPT does not introduce a new language-model architecture. Instead, it documents a clear and reproducible implementation path from raw text to trained character-level generation, including design choices, training behavior, generation quality, and practical limitations.
匹配关键词: PyTorch
---

[ACADEMIC - ARXIV]
标题: AgentKernelArena: Generalization-Aware Benchmarking of GPU Kernel Optimization Agents
作者: Sharareh Younesian, Wenwen Ouyang, Sina Rafati, Mehdi Rezagholizadeh, Sharon Zhou, Ji Liu, Yue Liu, Yuchen Yang, Hao Li, Ziqiong Liu, Dong Li, Vikram Appia, Zhenyu Gu, Emad Barsoum
链接: https://arxiv.org/abs/2605.16819v1
完整摘要: GPU kernel optimization is increasingly critical for efficient deep learning systems, but writing high-performance kernels still requires substantial low-level expertise. Recent AI coding agents can iteratively read code, invoke compilers and profilers, and refine implementations, yet existing kernel benchmarks evaluate single LLM calls rather than full agent workflows, and none include both kernel-to-kernel optimization and unseen-configuration generalization testing. We present AgentKernelArena, an open-source benchmark for measuring AI coding agents on GPU kernel optimization. The benchmark contains 196 tasks spanning HIP-to-HIP optimization, Triton-to-Triton optimization, and PyTorch-to-HIP translation, and evaluates complete agent workflows in isolated workspaces using gated compilation, correctness, and performance checks, centralized scoring and an unseen-configuration generalization protocol that tests whether optimizations transfer to input configurations the agent never observed. Across production agents including Cursor Agent, Claude Code, and Codex Agent, we find near-perfect compilation and high correctness rates on most task categories, with the strongest configurations achieving mean speedups of up to 6.89x on PyTorch-to-HIP, 6.69x on HIP-to-HIP, and 2.13x on Triton-to-Triton tasks. Our unseen-configuration evaluation shows that HIP-to-HIP and Triton-to-Triton optimizations largely transfer to unseen input shapes, while PyTorch-to-HIP exhibits substantial correctness drops, indicating that agents generating kernels from scratch frequently hardcode shape-specific assumptions. AgentKernelArena is designed as a modular, extensible framework for rigorous evaluation of agentic GPU kernel optimization across agents, tasks, and hardware targets.
匹配关键词: PyTorch
---

[ACADEMIC - ARXIV]
标题: Towards Code-Oriented LM Embeddings for Surrogate-Assisted Neural Architecture Search
作者: Pranav Somu, Advay Balakrishnan, Stepan Kravtsov, Aaron McDaniel, Jason Zutty
链接: https://arxiv.org/abs/2605.15649v1
完整摘要: Developing effective surrogates (performance predictors) for Neural Architecture Search (NAS) typically requires expensive fine-tuning or the engineering of complex representations. We propose a low-cost embedding strategy that leverages the inductive bias of Language Models (LMs) to eliminate these overheads. By representing architectures as PyTorch class definition text, we demonstrate that off-the-shelf LMs act as competitive feature extractors without NAS-specialized fine-tuning. The final predictor is constructed by passing the extracted Code-Oriented LM Embeddings (COLE) through a lightweight regression head. We also investigate strategies to improve embedding quality and utilization. Our experiments on the NAS-Bench-201 and einspace search spaces reveal that raw code inputs yield higher predictive performance than other text-based encodings (e.g., ONNX-to-text encodings) when using frozen LMs. We also observe COLE drives superior surrogate-assisted search using the BANANAS algorithm in NAS-Bench-201. When optimizing for CIFAR-100 performance, replacing structural path encodings with COLE for architecture representation allows for a 34% decrease in the evaluation budget required to reach within 1% of the fittest architecture in the search space (by test accuracy). As any neural architecture can be represented as code, these findings establish COLE as a versatile and efficient foundation for advancing NAS.
匹配关键词: PyTorch
---

[ACADEMIC - ARXIV]
标题: parallelcbf: A composable safety-filter and auditability framework for tensor-parallel reinforcement learning
作者: Yijun Lu, Zilei Yang, Yuyin Ma
链接: https://arxiv.org/abs/2605.15509v1
完整摘要: While Isaac Lab provides massive parallel UAV simulation, OmniSafe and safe-control-gym provide constrained-RL benchmarks, and CBFKit provides control-barrier-function synthesis tooling, no existing framework unifies these capabilities for end-to-end safety-constrained training. ParallelCBF is the first framework to unify (i)~tensor-parallel UAV environments, (ii)~hard-gate CBF safety filters, (iii)~sharded BC-to-RL pipelines, and (iv)~first-class operational auditability -- pre-registration, watchdog registries, failure forensics, and dataset audits as composable APIs rather than user-implemented scripts. We release ParallelCBF v0.1.0 under Apache~2.0 with a four-layer composable API, a CPU PyTorch reference implementation of a dual-barrier (squared / linear-predictive) CBF, property-based safety invariance tests across vectorized batch sizes that complete in 1.67~s for the full 39-test suite, and a 31{,}415-episode behavior-cloning collection campaign whose curriculum mix, per-bucket yields, and dataset SHA-256 are auditable through the framework's own \texttt{ops} primitives. We report a representative end-to-end pipeline execution in which the framework's auditability layer halted a downstream training stage that did not meet pre-registered convergence criteria, preventing silent propagation of a degraded checkpoint -- an architectural property we argue is necessary, not merely useful, for reproducible empirical robotics research. The framework is installable via \texttt{pip install parallelcbf}; source and release artifacts are available at https://github.com/xiaoyang-123-cell/ParallelCBF.
匹配关键词: PyTorch
---

[ACADEMIC - ARXIV]
标题: TriAxialKV: Toward Extreme Low-Precision KV-Cache Quantization for Agentic Inference Tasks
作者: Hanzhang Shen, Haoran Wu, Yiren Zhao, Robert Mullins
链接: https://arxiv.org/abs/2605.17170v1
完整摘要: Agentic workloads have emerged as a major workload for LLM inference. They differ significantly from chat-only workloads, requiring long-context processing, the ability to handle multimodal inputs, and structured multi-turn interactions with tool calling capabilities. As a result, their context exhibits structure that can carry different importance along three key axes: temporal recency to the current turn, modality such as text or image tokens, and semantic role such as user queries, tool calls, observations, or reasoning. These axes capture distinct token behaviors and lead to different sensitivities to KV-cache compression. However, existing KV-cache quantization methods are typically homogeneous or exploit only heterogeneity on a single dimension, such as temporal proximity or modality, overlooking the interactions among them. To this end, we introduce TriAxialKV, a novel mixed-precision KV-cache quantization scheme that assigns each token a triaxial tag, calibrates per-tag sensitivity, and allocates INT2/INT4 bitwidths under a fixed memory budget. We implement TriAxialKV as an end-to-end serving system, comprising calibration, mixed-precision quantization and memory management, and custom fused Triton decode kernels. When using Qwen3-VL-32B-Thinking as a computer-use agent operating the OSWorld, TriAxialKV matches the accuracy of SGLang with BF16 KV cache while supporting 4.5$\times$ KV cache size and achieving 30% higher end-to-end throughput, when running on real GPU systems.
匹配关键词: Triton
---

[ACADEMIC - ARXIV]
标题: AgentKernelArena: Generalization-Aware Benchmarking of GPU Kernel Optimization Agents
作者: Sharareh Younesian, Wenwen Ouyang, Sina Rafati, Mehdi Rezagholizadeh, Sharon Zhou, Ji Liu, Yue Liu, Yuchen Yang, Hao Li, Ziqiong Liu, Dong Li, Vikram Appia, Zhenyu Gu, Emad Barsoum
链接: https://arxiv.org/abs/2605.16819v1
完整摘要: GPU kernel optimization is increasingly critical for efficient deep learning systems, but writing high-performance kernels still requires substantial low-level expertise. Recent AI coding agents can iteratively read code, invoke compilers and profilers, and refine implementations, yet existing kernel benchmarks evaluate single LLM calls rather than full agent workflows, and none include both kernel-to-kernel optimization and unseen-configuration generalization testing. We present AgentKernelArena, an open-source benchmark for measuring AI coding agents on GPU kernel optimization. The benchmark contains 196 tasks spanning HIP-to-HIP optimization, Triton-to-Triton optimization, and PyTorch-to-HIP translation, and evaluates complete agent workflows in isolated workspaces using gated compilation, correctness, and performance checks, centralized scoring and an unseen-configuration generalization protocol that tests whether optimizations transfer to input configurations the agent never observed. Across production agents including Cursor Agent, Claude Code, and Codex Agent, we find near-perfect compilation and high correctness rates on most task categories, with the strongest configurations achieving mean speedups of up to 6.89x on PyTorch-to-HIP, 6.69x on HIP-to-HIP, and 2.13x on Triton-to-Triton tasks. Our unseen-configuration evaluation shows that HIP-to-HIP and Triton-to-Triton optimizations largely transfer to unseen input shapes, while PyTorch-to-HIP exhibits substantial correctness drops, indicating that agents generating kernels from scratch frequently hardcode shape-specific assumptions. AgentKernelArena is designed as a modular, extensible framework for rigorous evaluation of agentic GPU kernel optimization across agents, tasks, and hardware targets.
匹配关键词: Triton
---

[ACADEMIC - ARXIV]
标题: DiRotQ: Rotation-Aware Quantization for 4-bit Diffusion Transformers
作者: Sayeh Sharify, Mahsa Salmani, Hesham Mostafa
链接: https://arxiv.org/abs/2605.16732v1
完整摘要: Diffusion Transformers (DiTs) achieve state-of-the-art image generation quality but incur substantial memory and computational costs at inference. While aggressive Post-Training Quantization (PTQ) to 4-bit precision offers significant efficiency gains, it typically results in severe quality degradation. Existing approaches, including smoothing-based methods, mixed-precision schemes, rotation techniques, and low-rank residual methods, partially mitigate this issue but still leave a noticeable gap to FP16/BF16 performance. In this work, we introduce DiRotQ, a W4A4 PTQ framework that mitigates this degradation through rotation-aware activation quantization. DiRotQ identifies a low-rank subspace capturing dominant activation variance via Principal Component Analysis (PCA), preserving coefficients in this subspace at higher precision while quantizing the remaining components to 4-bit. Activations are rotated into the PCA basis at inference time using calibration-derived orthogonal transformations, while the inverse rotation is fused into the layer weights offline. Combined with GPTQ-based weight quantization, DiRotQ achieves an FID (lower is better) of 15.9 and PSNR (higher is better) of 19.1 dB on PixArt-Σ over the MJHQ-30K dataset, outperforming the prior state-of-the-art SVDQuant (FID 18.9, PSNR 17.6) under the same INT W4A4 setting. Beyond standard metrics, we introduce a VLM-as-a-Judge evaluation protocol for diffusion model quantization, the first such evaluation in this setting, providing a more holistic assessment of perceptual quality and prompt alignment under aggressive compression. On the systems side, we implement a Triton-based custom kernel to enable efficient end-to-end inference, reducing memory usage of the 12B FLUX.1-dev model by 2.1x and delivering 2.3x speedup over the BF16 baseline, on a 24 GB RTX 4090 GPU.
匹配关键词: Triton
---

[ACADEMIC - ARXIV]
标题: Variational Linear Attention: Stable Associative Memory for Long-Context Transformers
作者: Vishal Pandey, Gopal Singh
链接: https://arxiv.org/abs/2605.11196v1
完整摘要: Linear attention reduces the quadratic cost of softmax attention to $\mathcal{O}(T)$, but its memory state grows as $\mathcal{O}(T)$ in Frobenius norm, causing progressive interference between stored associations. We introduce \textbf{Variational Linear Attention} (VLA), which reframes the memory update as an online regularised least-squares problem with an adaptive penalty matrix maintained via the Sherman-Morrison rank-1 formula. We prove that normalising the write direction to unit length gives the recurrence Jacobian spectral norm exactly $1$ for all sequence lengths and head dimensions (Proposition 2), and that the state norm is self-limiting under bounded inputs (Proposition 1). Empirically, VLA reduces $\|S_t\|_F$ by $109\times$ relative to standard linear attention at $T{=}1{,}000$, achieves near-perfect exact-match accuracy on multi-query associative recall within the effective per-head memory regime ($n_\text{pairs} < d_h$), maintaining substantially higher retrieval performance than DeltaNet and standard linear attention under increasing memory load, and maintains 62\% accuracy at the per-head capacity boundary. A Triton-fused kernel achieves $14\times$ speedup over sequential Python and $\mathcal{O}(T)$ scaling, crossing below softmax attention latency at approximately 43\,000 tokens.
匹配关键词: Triton
---

[ACADEMIC - ARXIV]
标题: BCJR-QAT: A Differentiable Relaxation of Trellis-Coded Weight Quantization
作者: Venugopalan Iyengar
链接: https://arxiv.org/abs/2605.10655v1
完整摘要: Trellis-coded quantization sets the current 2-bit post-training frontier for LLMs (QTIP), but pushing below the PTQ ceiling requires quantization-aware training, and QAT on a trellis is obstructed by the non-differentiable Viterbi argmax. We introduce BCJR-QAT, a relaxation that replaces the argmax with the BCJR forward-backward sum-product algorithm at temperature $T$, producing a soft codeword equal to the Boltzmann expectation over trellis paths, exactly differentiable, recovering the hard QTIP code as $T \to 0$, and mathematically identical to the transfer-matrix computation for a 1D Ising-like spin chain. We contribute (i) a fused Triton kernel making BCJR tractable on a single consumer GPU ($6.57\times$ speedup, fp32 parity); (ii) a quantitative drift-budget theory of when BCJR-QAT can escape the QTIP-PTQ Voronoi basin, verified across four experiments; and (iii) a positive empirical result on Llama-3.2-1B at 2 bpw under end-to-end forward-KL distillation: with the right schedule (skip the high-$T$ phase to avoid an overshoot we diagnose), single-layer BCJR-QAT beats QTIP-PTQ by $\mathbf{-0.084}$ PPL on WikiText-2, and multi-layer compounding is super-additive.
匹配关键词: Triton
---

[ACADEMIC - ARXIV]
标题: bde: A Python Package for Bayesian Deep Ensembles via MILE
作者: Vyron Arvanitis, Angelos Aslanidis, Emanuel Sommer, David Rügamer
链接: https://arxiv.org/abs/2605.14146v1
完整摘要: bde is a user-friendly Python package for Bayesian Deep Ensembles with a particular focus on tabular data. Built on an efficient JAX implementation of the sampling-based inference method Microcanonical Langevin Ensembles (MILE), it provides scikit-learn compatible estimators for fast training, efficient Markov Chain Monte Carlo sampling, and uncertainty quantification in both regression and classification tasks.
匹配关键词: JAX
---

[ACADEMIC - ARXIV]
标题: QT-Net: Rethinking Evaluation of AI Models in Atomic Chemical Space
作者: Pablo Martínez Crespo, Stefano Ribes, Martin Rahm, Richard Beckmann, Robert S. Jordan, Marisa Gliege, Santiago Miret, Vijay Kris Narasimhan, Rocío Mercado
链接: https://arxiv.org/abs/2605.10458v1
完整摘要: Atomic properties such as partial charges or multipoles encode chemically meaningful information that can inform downstream molecular property prediction, but their evaluation as machine learning targets has been complicated by the absence of a principled out-of-distribution evaluation protocol at the atomic level. In this work, we propose a held-out evaluation protocol that clusters atomic environments by SOAP descriptors and computes metrics accounting only for cluster labels unseen during training. Following this procedure, we use 5$\times$5 cross-validation and Tukey's HSD to run a statistically rigorous comparison of E(3)-equivariant against non-equivariant, rotationally augmented models for predicting electron populations and multipoles of H, C, N, and O atoms. Building on our results, we introduce the Quantum Topological Neural Network (QT-Net), a rotationally augmented, non-equivariant graph neural network. We show that QT-Net can be used to infer properties of atoms in molecules from QM9 outside our training set, and that these inferred properties can yield improvement when used as input features for downstream molecular property prediction. To further validate the framework, molecular dipole moments computed from QT-Net's per-atom outputs recover the ground-truth values reported in QM9. We release all code and data, including a JAX implementation of QT-Net, to support the broader use of learned QTA properties as inductive biases for atomic-scale molecular machine learning.
匹配关键词: JAX
---

[ACADEMIC - ARXIV]
标题: jNO: A JAX Library for Neural Operator and Foundation Model Training
作者: Leon Armbruster, Rathan Ramesh, Georg Kruse, Christopher Straub
链接: https://arxiv.org/abs/2605.10159v1
完整摘要: jNO (jax Neural Operators) is a JAX-native library for neural operators and foundation models with unified support for both data-driven and physics-informed training. Its core design is a tracing system in which domains, model calls, residuals, supervised losses, and diagnostics are written in one symbolic language and compiled into one optimization pipeline. This allows users to move between operator regression, mesh-aware residual evaluation, and PDE-constrained training without restructuring the surrounding code. jNO also supports multi-model compositions, fine-grained control at parameter level (model, optimizer, and learning rate), hyperparameter tuning, and JAX-native workflows for translated PDE foundation-model families. The source repository is available at https://github.com/FhG-IISB/jNO.
匹配关键词: JAX
---

[ACADEMIC - ARXIV]
标题: Monocular Biomechanical Tracking of Fingers with Inverse Kinematics to Foundation Models
作者: R. James Cotton, Pouyan Firouzabadi, Wendy Murray
链接: https://arxiv.org/abs/2605.09258v1
完整摘要: Accurate hand and finger tracking from video has significant clinical applications for monitoring activities of daily living and measuring range of motion, yet monocular video approaches for obtaining hand biomechanics remain under-developed. We present a method that combines the SAM 3D Body foundation model with inverse kinematics optimization in a full-body biomechanical model to extract anatomically-constrained finger joint angles from single-view video. We port SAM 3D Body from PyTorch to JAX for integration with MuJoCo-MJX, enabling GPU-accelerated optimization, and develop a novel mapping between the Momentum Human Rig (MHR) outputs and biomechanical model markers. Validation against 8-camera multiview reconstruction on 4,590 frames from 7 participants performing a variety of hand poses and object manipulation tasks shows finger joint angle errors of approximately 10 degrees and hand position errors of approximately 6 mm, after Procrustes alignment. Results were consistent across camera viewpoints and robust to different methods for producing reference values from multiview video. This work extends monocular biomechanical analysis to detailed finger tracking, expanding access to quantitative characterization of hand movement from readily available video.
匹配关键词: JAX
---

[ACADEMIC - ARXIV]
标题: Rethinking Ratio-Based Trust Regions for Policy Optimization in Multi-Agent Reinforcement Learning
作者: Chulabhaya Wijesundara, Andrea Baisero, Zhongheng Li, Gregory Castañón, Alan Carlin, Christopher Amato
链接: https://arxiv.org/abs/2605.09212v1
完整摘要: Centralized training with decentralized execution (CTDE) is a standard framework for cooperative multi-agent policy-gradient reinforcement learning, allowing agents to learn from joint information while acting from local observations. Ratio-based trust-region methods such as Multi-Agent Proximal Policy Optimization (MAPPO) and Multi-Agent Simple Policy Optimization (MASPO) update decentralized actors using per-agent probability ratios weighted by joint advantage estimates. Teammate non-stationarity increases the variance of these advantages, which in turn increases the variance in the local ratio updates. This exposes two method-specific failure modes: MAPPO's additive clipping removes gradients for outlier samples and weakens recovery from policy drift, while MASPO's soft quadratic penalty can allow probability collapse. We introduce Multi-Agent Ratio Symmetry (MARS), a novel policy optimization objective that replaces these additive ratio-based trust-region mechanisms with a multiplicatively symmetric geometric barrier. MARS preserves corrective gradients while assigning unbounded cost as probability ratios approach zero. Across 47 tasks spanning eight multi-agent environments, including novel JAX benchmarks PaxMen and AeroJAX, MARS matches or exceeds MAPPO and MASPO in aggregate environment-level performance. Ablations show that these gains arise from the geometry of the symmetric barrier rather than from flexible trust-region boundaries alone.
匹配关键词: JAX
---

[ACADEMIC - ARXIV]
标题: AGoQ: Activation and Gradient Quantization for Memory-Efficient Distributed Training of LLMs
作者: Wenxiang Lin, Juntao Huang, Luhan Zhang, Laili Li, Xiang Bao, Mengyang Zhang, Bing Wang, Shaohuai Shi
链接: https://arxiv.org/abs/2605.00539v2
完整摘要: Quantization is a key method for reducing the GPU memory requirement of training large language models (LLMs). Yet, current approaches are ineffective for 4-bit activations and 8-bit gradients, which would easily cause slow convergence or accuracy loss. To address this, we introduce AGoQ, incorporating two new techniques: 1) a layer-aware activation quantization algorithm that allocates appropriate bit-widths for activations of various layers based on their types and pipeline stages to achieve near 4-bit activation storage, and 2) a gradient quantization algorithm that reduces memory usage and shortens communication time by employing 8-bit gradient storage and precision-preserving 8-bit All-Reduce communication. We conduct extensive experiments using different sizes of LLMs on two GPU clusters (up to 64 GPUs), and the experimental results show that our AGoQ reduces the memory by up to 52\% and achieves up to 1.34$\times$ improvement of training speed compared to state-of-the-art training systems Megatron-LM (w/ or w/o ZeRO), COAT and DeepSpeed with 8B to 32B LLaMA models, while achieving convergence loss on pretraining and comparable accuracy on downstream tasks with LLaMA architectures.
匹配关键词: DeepSpeed
---

[ACADEMIC - ARXIV]
标题: SFT-then-RL Outperforms Mixed-Policy Methods for LLM Reasoning
作者: Alexis Limozin, Eduard Durech, Torsten Hoefler, Imanol Schlag, Valentina Pyatkin
链接: https://arxiv.org/abs/2604.23747v1
完整摘要: Recent mixed-policy optimization methods for LLM reasoning that interleave or blend supervised and reinforcement learning signals report improvements over the standard SFT-then-RL pipeline. We show that numerous recently published research papers rely on a faulty baseline caused by two distinct bugs: a CPU-offloaded optimizer bug in DeepSpeed that silently drops intermediate micro-batches during gradient accumulation (affecting multiple downstream frameworks including TRL, OpenRLHF and Llama-Factory), and a loss aggregation bug in OpenRLHF that incorrectly weights per-mini-batch losses. Together they suppress SFT performance, with the optimizer bug accounting for most of the gap and the loss aggregation bug contributing a smaller additional effect. Once corrected, the standard SFT-then-RL pipeline surpasses every published mixed-policy method we evaluate by +3.8 points on math benchmarks with Qwen2.5-Math-7B and by +22.2 points with Llama-3.1-8B. Even a truncated variant with just 50 RL steps outperforms mixed-policy methods on math benchmarks while using fewer FLOPs.
匹配关键词: DeepSpeed
---

[ACADEMIC - ARXIV]
标题: MegaTrain: Full Precision Training of 100B+ Parameter Large Language Models on a Single GPU
作者: Zhengqing Yuan, Hanchi Sun, Lichao Sun, Yanfang Ye
链接: https://arxiv.org/abs/2604.05091v1
完整摘要: We present MegaTrain, a memory-centric system that efficiently trains 100B+ parameter large language models at full precision on a single GPU. Unlike traditional GPU-centric systems, MegaTrain stores parameters and optimizer states in host memory (CPU memory) and treats GPUs as transient compute engines. For each layer, we stream parameters in and compute gradients out, minimizing persistent device state. To battle the CPU-GPU bandwidth bottleneck, we adopt two key optimizations. 1) We introduce a pipelined double-buffered execution engine that overlaps parameter prefetching, computation, and gradient offloading across multiple CUDA streams, enabling continuous GPU execution. 2) We replace persistent autograd graphs with stateless layer templates, binding weights dynamically as they stream in, eliminating persistent graph metadata while providing flexibility in scheduling. On a single H200 GPU with 1.5TB host memory, MegaTrain reliably trains models up to 120B parameters. It also achieves 1.84$\times$ the training throughput of DeepSpeed ZeRO-3 with CPU offloading when training 14B models. MegaTrain also enables 7B model training with 512k token context on a single GH200.
匹配关键词: DeepSpeed
---

[ACADEMIC - ARXIV]
标题: DataFlex: A Unified Framework for Data-Centric Dynamic Training of Large Language Models
作者: Hao Liang, Zhengyang Zhao, Meiyi Qiang, Mingrui Chen, Lu Ma, Rongyi Yu, Hengyi Feng, Shixuan Sun, Zimo Meng, Xiaochen Ma, Xuanlin Yang, Qifeng Cai, Ruichuan An, Bohan Zeng, Zhen Hao Wong, Chengyu Shen, Runming He, Zhaoyang Han, Yaowei Zheng, Fangcheng Fu, Conghui He, Bin Cui, Zhiyu Li, Weinan E, Wentao Zhang
链接: https://arxiv.org/abs/2603.26164v1
完整摘要: Data-centric training has emerged as a promising direction for improving large language models (LLMs) by optimizing not only model parameters but also the selection, composition, and weighting of training data during optimization. However, existing approaches to data selection, data mixture optimization, and data reweighting are often developed in isolated codebases with inconsistent interfaces, hindering reproducibility, fair comparison, and practical integration. In this paper, we present DataFlex, a unified data-centric dynamic training framework built upon LLaMA-Factory. DataFlex supports three major paradigms of dynamic data optimization: sample selection, domain mixture adjustment, and sample reweighting, while remaining fully compatible with the original training workflow. It provides extensible trainer abstractions and modular components, enabling a drop-in replacement for standard LLM training, and unifies key model-dependent operations such as embedding extraction, inference, and gradient computation, with support for large-scale settings including DeepSpeed ZeRO-3. We conduct comprehensive experiments across multiple data-centric methods. Dynamic data selection consistently outperforms static full-data training on MMLU across both Mistral-7B and Llama-3.2-3B. For data mixture, DoReMi and ODM improve both MMLU accuracy and corpus-level perplexity over default proportions when pretraining Qwen2.5-1.5B on SlimPajama at 6B and 30B token scales. DataFlex also achieves consistent runtime improvements over original implementations. These results demonstrate that DataFlex provides an effective, efficient, and reproducible infrastructure for data-centric dynamic training of LLMs.
匹配关键词: DeepSpeed
---

[ACADEMIC - ARXIV]
标题: Throughput Optimization as a Strategic Lever in Large-Scale AI Systems: Evidence from Dataloader and Memory Profiling Innovations
作者: Mayank Jha
链接: https://arxiv.org/abs/2603.26823v1
完整摘要: The development of large-scale foundation models, particularly Large Language Models (LLMs), is constrained by significant computational and memory bottlenecks. These challenges elevate throughput optimization from a mere engineering task to a critical strategic lever, directly influencing training time, operational cost, and the feasible scale of next-generation models. This paper synthesizes evidence from recent academic and industry innovations to analyze key advancements in training efficiency. We examine architectural solutions to dataloader bottlenecks, such as the OVERLORD framework, which has demonstrated a 4.5% improvement in end-to-end training throughput. We investigate memory optimization techniques designed to overcome the GPU memory wall, including CPU offloading strategies like DeepSpeed's ZeRO-Offload, which enable the training of models far exceeding single-accelerator capacity. Furthermore, we explore the growing importance of compiler-centric optimizations, exemplified by Triton-distributed, which enables the joint optimization of computation, memory, and communication for substantial performance gains. The analysis is contextualized by advanced profiling tools and hardware characterization studies that identify and mitigate previously overlooked overheads like Dynamic Voltage and Frequency Scaling (DVFS). Findings indicate that a holistic, system-level approach, integrating innovations across data pipelines, memory management, network fabrics, and compiler technologies, is essential for accelerating AI development, managing costs, and pushing the boundaries of model scale.
匹配关键词: DeepSpeed
---

[ACADEMIC - ARXIV]
标题: EnergyLens: Predictive Energy-Aware Exploration for Multi-GPU LLM Inference Optimization
作者: Zhiye Song, Kyungmi Lee, Eun Kyung Lee, Xin Zhang, Tamar Eilam, Anantha P. Chandrakasan
链接: https://arxiv.org/abs/2605.14249v1
完整摘要: We present EnergyLens, an end-to-end framework for energy-aware large language model (LLM) inference optimization. As LLMs scale, predicting and reducing their energy footprint has become critical for sustainability and datacenter operations, yet existing approaches either require production-level code and expensive profiling or fail to accurately capture multi-GPU energy behavior. As a result, practitioners lack tools for deciding which optimizations to prioritize and for selecting among existing deployment configurations when exhaustive profiling is impractical. EnergyLens addresses this gap with an intuitive einsum-based interface that captures LLM specifications including fusion, parallelism, and compute-communication overlap, combined with load-imbalance-aware MoE modeling and an empirically driven communication energy model for multi-GPU settings. We validate EnergyLens on Llama3 and Qwen3-MoE across tensor-parallel and expert-parallel configurations, achieving mean absolute percentage errors (MAPEs) between 9.25% and 13.19% for multi-GPU prefill and decode energy, and 12.97% across SM allocations for Megatron-style overlap. Our energy-driven exploration reveals up to 1.47x and 52.9x energy variation across configurations in prefill and decode efficiency and motivates distributed serving. We further show that compute-communication overlap is difficult to optimize with intuition alone, but EnergyLens correctly identifies Pareto-optimal overlap configurations.
匹配关键词: Megatron
---

[ACADEMIC - ARXIV]
标题: DisagMoE: Computation-Communication overlapped MoE Training via Disaggregated AF-Pipe Parallelism
作者: Zhichen Zeng, Chi-Chih Chang, Jiayi Wang, Zezhou Wang, Ningxin Zheng, Zheng Zhong, Cesar A. Stuardo, Dongyang Wang, Mohamed S. Abdelfattah, Haibin Lin, Banghua Zhu, Ang Li, Ziheng Jiang
链接: https://arxiv.org/abs/2605.11005v1
完整摘要: Mixture-of-experts (MoE) architectures enable trillion-parameter LLMs with sparsely activated experts. Expert parallelism (EP) is a widely adopted MoE training strategy, but it suffers from severe all-to-all communication bottlenecks, which is exaggerated by the limited inter-node network bandwidth as the growing model size requires distributing experts across GPU nodes. Prior work focused on overlapping these all-to-all communications with feed-forward network (FFN) and self-attention computations, which often leaves residual network-bound stalls due to inherent imbalance in attention and FFN layers' computation-communication ratios. We present DisagMoE, a disaggregated MoE training system that jointly optimizes model placement and scheduling for maximal efficiency. DisagMoE separates attention and FFN layers into disjoint GPU groups, introduces a multi-stage pipeline with uni-directional, many-to-many communications, and employs a computation-communication roofline model to balance GPU and network bandwidth allocation among the attention and FFN groups. DisagMoE is implemented on Megatron-LM, and evaluation shows that DisagMoE improves training efficiency across multiple MoE models with up to 1.8x speedup on 16-node 8xH800 clusters.
匹配关键词: Megatron
---

[ACADEMIC - ARXIV]
标题: ReLibra: Routing-Replay-Guided Load Balancing for MoE Training in Reinforcement Learning
作者: Chao Jin, Xinming Wei, Yinmin Zhong, Chengxu Yang, Bingyang Wu, Ruidong Zhu, Zili Zhang, Yuliang Liu, Xin Jin
链接: https://arxiv.org/abs/2605.08639v1
完整摘要: Load imbalance is a long-standing challenge in Mixture-of-Experts (MoE) training and is exacerbated in reinforcement learning (RL) for LLMs, where hot experts can shift frequently across micro-batches. Existing MoE training systems rely on historical loads to predict future expert demand, making them less effective under sharp fluctuations. We propose ReLibra, an MoE RL training system that exploits a unique opportunity in RL's rollout-training workflow, routing replay, to enable fine-grained load balancing at micro-batch granularity. Because rollout and training process the same tokens with the same MoE parameters, the token-to-expert routing decisions are known before training starts. Leveraging this information, ReLibra places two MoE load-balancing mechanisms at inter- and intra-batch timescales, matching their communication patterns to hierarchical network bandwidths. At the inter-batch timescale, ReLibra performs expert reordering to redistribute experts for batch-level cross-node balancing; at the intra-batch timescale, it dynamically performs expert replication within a node to absorb micro-batch-level load fluctuations. Experiments on diverse MoE LLMs and RL workloads show that ReLibra improves training throughput by up to 1.6$\times$ over Megatron-LM and by up to 1.2$\times$ over EPLB, even when EPLB is given oracle loads. Moreover, ReLibra remains within 6%-10% of the throughput of an idealized balanced baseline.
匹配关键词: Megatron
---

[ACADEMIC - ARXIV]
标题: AGoQ: Activation and Gradient Quantization for Memory-Efficient Distributed Training of LLMs
作者: Wenxiang Lin, Juntao Huang, Luhan Zhang, Laili Li, Xiang Bao, Mengyang Zhang, Bing Wang, Shaohuai Shi
链接: https://arxiv.org/abs/2605.00539v2
完整摘要: Quantization is a key method for reducing the GPU memory requirement of training large language models (LLMs). Yet, current approaches are ineffective for 4-bit activations and 8-bit gradients, which would easily cause slow convergence or accuracy loss. To address this, we introduce AGoQ, incorporating two new techniques: 1) a layer-aware activation quantization algorithm that allocates appropriate bit-widths for activations of various layers based on their types and pipeline stages to achieve near 4-bit activation storage, and 2) a gradient quantization algorithm that reduces memory usage and shortens communication time by employing 8-bit gradient storage and precision-preserving 8-bit All-Reduce communication. We conduct extensive experiments using different sizes of LLMs on two GPU clusters (up to 64 GPUs), and the experimental results show that our AGoQ reduces the memory by up to 52\% and achieves up to 1.34$\times$ improvement of training speed compared to state-of-the-art training systems Megatron-LM (w/ or w/o ZeRO), COAT and DeepSpeed with 8B to 32B LLaMA models, while achieving convergence loss on pretraining and comparable accuracy on downstream tasks with LLaMA architectures.
匹配关键词: Megatron
---

[ACADEMIC - ARXIV]
标题: Scalable Training of Mixture-of-Experts Models with Megatron Core
作者: Zijie Yan, Hongxiao Bai, Xin Yao, Dennis Liu, Tong Liu, Hongbin Liu, Pingtian Li, Evan Wu, Shiqing Fan, Li Tao, Robin Zhang, Yuzhong Wang, Shifang Xu, Jack Chang, Xuwen Chen, Kunlun Li, Yan Bai, Gao Deng, Nan Zheng, Vijay Anand Korthikanti, Abhinav Khattar, Ethan He, Soham Govande, Sangkug Lym, Zhongbo Zhu, Qi Zhang, Haochen Yuan, Xiaowei Ren, Deyu Fu, Tailai Ma, Shunkang Zhang, Jiang Shao, Ray Wang, Vasudevan Rengasamy, Rachit Garg, Santosh Bhavani, Xipeng Li, Chandler Zhou, David Wu, Yingcan Wei, Ashwath Aithal, Michael Andersch, Mohammad Shoeybi, Jiajie Yao, June Yang
链接: https://arxiv.org/abs/2603.07685v2
完整摘要: Scaling Mixture-of-Experts (MoE) training introduces systems challenges absent in dense models. Because each token activates only a subset of experts, this sparsity allows total parameters to grow much faster than per-token computation, creating coupled constraints across memory, communication, and computation. Optimizing one dimension often shifts pressure to another, demanding co-design across the full system stack. We address these challenges for MoE training through integrated optimizations spanning memory (fine-grained recomputation, offloading, etc.), communication (optimized dispatchers, overlapping, etc.), and computation (Grouped GEMM, fusions, CUDA Graphs, etc.). The framework also provides Parallel Folding for flexible multi-dimensional parallelism, low-precision training support for FP8 and NVFP4, and efficient long-context training. On NVIDIA GB300 and GB200, it achieves 1,233/1,048 TFLOPS/GPU for DeepSeek-V3-685B and 974/919 TFLOPS/GPU for Qwen3-235B. As a performant, scalable, and production-ready open-source solution, it has been used across academia and industry for training MoE models ranging from billions to trillions of parameters on clusters scaling up to thousands of GPUs. This report explains how these techniques work, their trade-offs, and their interactions at the systems level, providing practical guidance for scaling MoE models with Megatron Core.
匹配关键词: Megatron
---

[ACADEMIC - ARXIV]
标题: OSCAR: Offline Spectral Covariance-Aware Rotation for 2-bit KV Cache Quantization
作者: Zhongzhu Zhou, Donglin Zhuang, Jisen Li, Ziyan Chen, Shuaiwen Leon Song, Ben Athiwaratkun, Xiaoxia Wu
链接: https://arxiv.org/abs/2605.17757v1
完整摘要: INT2 KV-cache quantization is attractive for long-context LLM serving, but it remains difficult to make both accurate and deployable. Simple rotations such as Hadamard transforms reduce outliers, but still degrade at INT2 because they are not aligned with downstream attention. We propose OSCAR, an Ultra-low-bit KV Cache quantization method that estimates attention-aware covariance structures offline and uses them to derive fixed rotations and clipping thresholds for quantization. In this way, it aligns KV quantization with the covariance structures that attention actually consumes. More importantly, we not only provide theoretical justification but also develop a fully deployable OSCAR system with a custom INT2 attention kernel that remains compatible with paged KV-cache serving and fused kernel pipelines, enabling seamless integration into modern LLM serving frameworks such as SGLang and vLLM. We evaluate our methods on recent reasoning models with reasoning traces of up to 32k tokens across 5 tasks. On Qwen3-4B-Thinking-2507 and Qwen3-8B, OSCAR reduces the BF16 accuracy gap to 3.78 and 1.42 points, respectively, while naive rotation INT2 collapses to nearly zero. We further scale OSCAR to Qwen3-32B and GLM-4.7 (358B params), where it remains effectively on par with BF16. On long context - RULER-NIAH up to 128K, OSCAR remains robust on both Qwen3 models, while naive rotation INT2 collapses. System-wise, OSCAR reduces KV-cache memory by approximately 8x, improves throughput by up to 7x at large batch sizes under the same memory budget, and accelerates batch-size-1 decoding by up to 3x over BF16 due to reduced memory bandwidth overhead.
匹配关键词: vLLM
---

[ACADEMIC - ARXIV]
标题: Token-Space Mask Prediction for Efficient Vision Transformer Segmentation
作者: Calvin Galagain, Martyna Poreba, François Goulette
链接: https://arxiv.org/abs/2605.18177v1
完整摘要: Query-based Vision Transformer segmentation models typically reconstruct dense spatial feature maps to predict masks, inheriting design patterns from convolutional architectures. We show that this explicit image-space reconstruction is not required. We introduce TokenMask, a token-space mask head that computes mask logits directly from query-token affinities and performs interpolation in logit space rather than feature space. This reformulation preserves the original linear scoring mechanism while simplifying the computational structure. Across diverse ViT backbones, datasets and segmentation tasks, TokenMask consistently improves efficiency over prior approaches by reducing computational and memory requirements while maintaining competitive accuracy, leading to tangible speedups on NVIDIA Jetson AGX Orin using TensorRT FP16 inference. Overall, TokenMask yields a simpler and more deployment-friendly design for embedded vision systems.
匹配关键词: TensorRT
---

[ACADEMIC - ARXIV]
标题: AdaptiveLoad: Towards Efficient Video Diffusion Transformer Training
作者: Yucheng Guo, Yongjian Guo, Zhong Guan, Haoran Sun, Wen Huang, Wanting Xu, Jing Long, Shuai Di, Junwu Xiong
链接: https://arxiv.org/abs/2605.17923v1
完整摘要: In video generation models, particularly world models, training large-scale video diffusion Transformers (such as DiT and MMDiT) poses significant computational challenges due to the extreme variance in sequence lengths within mixed-mode datasets. Existing bucket-based data loading strategies typically rely on "equal token length" constraints. This approach fails to account for the quadratic complexity of self-attention mechanisms, leading to severe load imbalance and underutilization of GPU resources. This paper proposes \textit{AdaptiveLoad}, an integrated optimization framework consisting of two core components: (1) A dual-constraint adaptive load balancing system, which eliminates long-sequence bottlenecks by simultaneously limiting memory consumption and computational load ($B \times S^p \le M_{\text{comp}}$); (2) A fused LayerNorm-Modulate CUDA kernel, which utilizes a D-tile coalesced reduction strategy to increase throughput and alleviate memory pressure. Experimental results on the Wan 2.1 world model demonstrate that our method reduces the computational imbalance rate from 39\% to 18.9\%, improves peak VRAM utilization efficiency by 22.7\%, and achieves an overall training throughput increase of 27.2\%.
匹配关键词: CUDA
---

[ACADEMIC - ARXIV]
标题: Lightweight Gaussian Process Inference in C++ on Metal and CUDA
作者: Yu-Hsueh Fang
链接: https://arxiv.org/abs/2605.17898v1
完整摘要: Gaussian process (GP) inference in Python is dominated by libraries such as GPyTorch and GPflow, which are built on deep-learning frameworks and inherit their dispatch overhead and dependency footprint. We present LightGP, a dependency-free C++17 library for GP regression with Python bindings, supporting Apple Metal and NVIDIA CUDA backends alongside tuned CPU paths via Apple Accelerate and OpenBLAS. LightGP provides four inference paths -- exact Cholesky, matrix-free conjugate gradients, sparse variational free energy, and structured kernel interpolation with FFT -- covering problems from $N{=}100$ to $N{=}500{,}000$. On an Apple M4, LightGP CPU is 2.6--8.7$\times$ faster than GPyTorch CPU for exact GP and ${\sim}1.5\times$ faster for sparse GP at every scale tested. On an NVIDIA RTX~3060, LightGP CUDA is 2.3--6.7$\times$ faster than GPyTorch CUDA for exact GP up to $N{=}2{,}048$, with GPyTorch closing the gap at $N{=}4{,}096$. A fused matrix-free kernel-vector product on Metal achieves 32$\times$ over the explicit path at $N{=}20{,}000$ with $O(N)$ memory, and an FFT-accelerated SKI matvec via Accelerate vDSP runs in sub-millisecond time at $N{=}200{,}000$. LightGP compiles as a single static library with zero external dependencies and is installable via \texttt{pip install lightgp
匹配关键词: CUDA
---

[ACADEMIC - ARXIV]
标题: PySIFT: GPU-Resident Deterministic SIFT for Deep Learning Vision Pipelines
作者: Sivakumar K. S., Mohammad Daniyalur Rahman, Gopi Raju Matta
链接: https://arxiv.org/abs/2605.17869v1
完整摘要: A widespread assumption in local feature research holds that classical handcrafted descriptors are accuracy-limited relics best replaced by learned alternatives. We show this is wrong. Through an 8-configuration ablation spanning four benchmarks (HPatches, ROxford5K, IMC Phototourism, MegaDepth), we demonstrate that classical SIFT with DSP multi-scale pooling outperforms neural descriptor and orientation replacements (HardNet, OriNet) on every accuracy metric--while running 2--18$\times$ faster--and that learned matchers (LightGlue) complement rather than supersede classical features. The conclusion reframes a decade of work: not "replace SIFT" but "compose with SIFT," classical extraction paired with learned matching only where geometric context demands it. This finding was invisible because no prior GPU SIFT kept the complete pipeline in VRAM or offered modularity for controlled classical-vs-learned ablations. We present PySIFT, the first fully GPU-resident SIFT, implemented in CuPy/Numba CUDA kernels with DLPack zero-copy handoff to downstream DL frameworks--submillisecond O(1) metadata swap regardless of keypoint count. On a laptop-grade NVIDIA RTX 3050 (4 GB VRAM), PySIFT achieves: (i) higher Mean Matching Accuracy (MMA) than OpenCV SIFT on HPatches, (ii) 383 ms faster per pair on high-resolution MegaDepth, (iii) higher geometric accuracy on cross-dataset benchmarks (+5.6 pp AUC@10${}^\circ$ on MegaDepth, more inliers on IMC Phototourism), and (iv) bitwise deterministic output--identical keypoints and descriptors across runs, with detection reproducing identically even across GPU architectures: a guarantee that learned extractors cannot match without significant performance sacrifice, and cannot achieve at all across GPU architectures due to cuDNN's architecture-dependent algorithm selection. PySIFT is open-source, requiring no C++ compilation.
匹配关键词: CUDA
---

[ACADEMIC - ARXIV]
标题: Are Sparse Autoencoder Benchmarks Reliable?
作者: David Chanin
链接: https://arxiv.org/abs/2605.18229v1
完整摘要: Sparse autoencoders (SAEs) are a core interpretability tool for large language models, and progress on SAE architectures depends on benchmarks that reliably distinguish better SAEs from worse ones. We audit the SAE quality metrics in SAEBench, the de-facto standard SAE evaluation suite, through three complementary lenses: reseed noise on a fixed SAE, ground-truth correlation on synthetic SAEs, and discriminability across training trajectories. We find that two of these metrics, Targeted Probe Perturbation (TPP) and Spurious Correlation Removal (SCR), fail multiple lenses at their canonical settings and should not be used to evaluate SAEs. The other metrics show higher reseed noise and lower discriminability than the field assumes. The sae-probes variant of $k$-sparse probing is the most reliable metric we tested, but even sae-probes struggles to separate variants of the same SAE architecture. Our results show the field needs better SAE benchmarks.
匹配关键词: distributed training
---

[ACADEMIC - ARXIV]
标题: Context Memorization for Efficient Long Context Generation
作者: Yasuyuki Okoshi, Hao Mark Chen, Guanxi Lu, Hongxiang Fan, Masato Motomura, Daichi Fujiki
链接: https://arxiv.org/abs/2605.18226v1
完整摘要: Modern large language model (LLM) applications increasingly rely on long conditioning prefixes to control model behavior at inference time. While prefix-augmented inference is effective, it incurs two structural limitations: i) the prefix's influence fades as generation proceeds, and ii) attention computation over the prefix scales linearly with its length. Existing approaches either keep the prefix in attention while compressing it, or internalize it into model parameters through gradient-based training. The former still attends to the prefix at inference, while the latter is training-intensive and ill-suited to prefix updates. To address these issues, we propose attention-state memory, a training-free approach that externalizes the prefix into a lightweight, lookup-based memory of precomputed attention states between prefix and query tokens. On ManyICLBench with LLaMA-3.1-8B, our method improves accuracy over in-context learning at 1K-8K memory budgets while reducing attention latency by 1.36x at 8K, and surpasses full-attention RAG performance on NBA benchmark using only 20% of its memory footprint.
匹配关键词: distributed training
---

[ACADEMIC - ARXIV]
标题: A Simplex Witness Certificate for Constant Collapse in Variational Autoencoders
作者: Zegu Zhang, Jianhua Peng, Jian Zhang
链接: https://arxiv.org/abs/2605.18224v1
完整摘要: This note studies exact constant collapse in variational autoencoders, where the encoder mean becomes independent of the input. The goal is to make this specific failure mode pre-designable, monitorable during training, and certifiable after training. The prior is kept as the standard Gaussian. Given a fixed teacher posterior, we attach to the latent mean a fixed simplex witness head. The resulting teacher-student alignment loss has an exact constant-predictor baseline equal to the teacher information. If the alignment loss is below this baseline, the latent mean cannot be input-independent constant collapsed. The simplex witness also has a closed-form inverse. Any full-support teacher posterior can be represented by embedding its centered log-odds into the latent space. This gives an explicit latent energy cost and explains when the alignment loss can be made small. A computable view gap handles the case where teacher targets are computed from a different view. Thus exact constant collapse is converted from an after-the-fact training pathology into a design-and-certificate problem.
匹配关键词: distributed training
---

[ACADEMIC - ARXIV]
标题: Contextual Biasing for Streaming ASR via CTC-based Word Spotting
作者: Kai-Chen Tsai, Tien-Hong Lo, Yun-Ting Sun, Berlin Chen
链接: https://arxiv.org/abs/2605.18222v1
完整摘要: Contextual biasing is essential to improving the recognition of rare and domain-specific words in an automatic speech recognition (ASR) system. While numerous methods have been proposed in recent years, most of them focus on offline settings and do not explicitly address the challenges of streaming ASR. For example, CTC-based word spotting (CTC-WS) have demonstrated strong performance by directly detecting keywords from CTC log-probabilities, but they are limited to offline processing and require access to the full utterance. In This work, we present a streaming extension of CTC-WS for real-time contextual biasing. Our method maintains active keyword paths across audio chunks using a stateful token passing algorithm, enabling the detection of keywords that span multiple chunks. To ensure low latency and stable output, we introduce an incremental commitment mechanism that only emits segments guaranteed not to be affected by future audio, while deferring uncertain regions. This method naturally integrates with streaming ASR pipelines and does not require modifications to the underlying acoustic model or additional training, making it practical for real-world deployment. Experimental results show that our method reduces overall WER and effectively improves keyword F-score, demonstrating its effectiveness for real-time ASR applications.
匹配关键词: distributed training
---

[ACADEMIC - ARXIV]
标题: EgoInteract: Synthetic Egocentric Videos Generation for Interaction Understanding and Anticipation
作者: Rosario Leonardi, Francesco Ragusa, Daniele Materia, Alessandro Passanisi, James Fort, Jakob Engel, Giovanni Maria Farinella
链接: https://arxiv.org/abs/2605.18214v1
完整摘要: Collecting large-scale egocentric video datasets with dense spatial and temporal annotations is costly, slow, and often constrained by environmental biases, privacy constraints, and limited coverage of interaction patterns. While synthetic data has shown strong potential in several vision domains, its use for egocentric perception remains relatively underexplored, especially for tasks requiring temporally coherent human-object interactions. In this work, we introduce EgoInteract, a controllable simulator for egocentric video generation designed to model fine-grained egocentric interactions and their temporal dynamics. The simulator enables precise control over camera, human body and hand motion, object manipulation, and scene composition across diverse environments. Building on this framework, we generate a synthetic egocentric video dataset with dense spatial and temporal annotations for temporal action segmentation, next-active object detection, interaction anticipation, and hand-object interaction detection. We evaluate models trained with simulated data on multiple real-world egocentric benchmarks spanning diverse environments, object categories, and interaction patterns. Results show consistent improvements over strong baselines across tasks and datasets, demonstrating the effectiveness and transferability of our simulation-based approach.
匹配关键词: distributed training
---

[ACADEMIC - ARXIV]
标题: Pairwise Preference Reward and Group-Based Diversity Enhancement for Superior Open-Ended Generation
作者: Guining Cao, Jiaxin Peng, Chu Zeng, Yu Zhao, Shuangyong Song, Yongxiang
链接: https://arxiv.org/abs/2605.18191v1
完整摘要: Current reinforcement learning(RL) methods are broadly applicable and powerful in verifiable settings where scalar rewards can be provided. However, in open-ended generation tasks, verifying the correctness of responses remains challenging, and training reward models incurs substantial computational and annotation costs. Moreover, reinforcement learning (RLVR) often leads to diversity collapse and produces stereotypical or rigid outputs, outcomes that are particularly undesirable in open-domain scenarios. We propose Pairwise Preference Reward and Group-based Diversity Enhancement (PPR-GDE), a RL method that is more suitable for open-ended generation. PPR-GDE does not require scalar rewards and incorporates group-level diversity into the reward signal, it preserves the comparative structure of subjective evaluation through a pairwise preference reward, mitigates judge position bias via repeated comparisons with swapped response order, and introduces a group-based diversity reward that explicitly encourages semantic dispersion within a response group, all of these reward signals are integrated into a unified group-relative policy optimization objective. We instantiate PPR-GDE on role-playing task, experiments show that PPR-GDE achieves a better alignment quality as well as expressive diversity than strong RL baselines. Further analysis shows that pairwise preference is critical for preference alignment in subjective perspective, while the diversity metric plays an essential role in achieving superior expressive diversity and broader semantic coverage.
匹配关键词: GPU optimization
---

[ACADEMIC - ARXIV]
标题: Ringmaster LMO: Asynchronous Linear Minimization Oracle Momentum Method
作者: Abdurakhmon Sadiev, Artavazd Maranjyan, Ivan Ilin, Peter Richtárik
链接: https://arxiv.org/abs/2605.18174v1
完整摘要: Muon has recently emerged as a strong alternative to AdamW for training neural networks, with encouraging large-scale pretraining results and growing evidence that matrix-structured updates can be faster in practice. Yet Muon, and more generally Linear Minimization Oracle (LMO) based methods, are typically used synchronously. This is problematic in heterogeneous distributed systems, where workers complete gradient computations at different speeds and synchronous training must repeatedly wait for slower workers. In this work, we introduce Ringmaster LMO, an asynchronous LMO-based momentum method for unconstrained stochastic nonconvex optimization. Our method builds on the delay-thresholding idea of Ringmaster ASGD. For SGD-type methods, Ringmaster ASGD achieves optimal time complexity by discarding overly stale gradients. Ringmaster LMO extends this mechanism to general LMO-based updates. We establish convergence guarantees under generalized $(L_0, L_1)$-smoothness and further develop a parameter-agnostic variant with decreasing stepsizes and adaptive delay thresholds. Finally, we translate our iteration guarantees into time complexity bounds under heterogeneous worker computation times. In the classical Euclidean smooth setting, these bounds recover the optimal time complexity of Ringmaster ASGD. Experiments on stochastic quadratic problems and NanoChat language-model pretraining show that the advantages of Ringmaster LMO grow with system heterogeneity and that the method outperforms strong synchronous and asynchronous baselines.
匹配关键词: GPU optimization
---

[ACADEMIC - ARXIV]
标题: Do You Need Text Rectification? Soft Attention Mask Embedding for Rectification-Free Scene Text Spotting
作者: Antonio Colombo, Giovanni Bianchi
链接: https://arxiv.org/abs/2605.18173v1
完整摘要: End-to-end scene text spotting, which unifies text detection and recognition within a single framework, has witnessed remarkable progress driven by deep learning advances. However, most existing approaches still suffer from incomplete mask proposals caused by multi-scale variation, arbitrary text shapes, and complex background interference, thereby degrading recognition accuracy. In this paper, we propose a novel Soft Attention Mask Embedding module (SAME) that leverages the global receptive field of Transformer encoders to encode high-level features and compute soft attention weights, which are then hierarchically embedded with predicted masks to generate refined text-boundary-aware masks that effectively suppress background noise. Building upon this module, we present SAME-Net, a robust end-to-end text spotting framework that requires neither character-level annotations nor auxiliary text rectification modules. Since the soft attention mechanism is fully differentiable, recognition loss gradients can be back-propagated through the SAME module to the detection branch, enabling joint optimization of detection and recognition objectives. Extensive experiments on challenging benchmarks demonstrate the effectiveness of our approach: SAME-Net achieves 84.02\% end-to-end H-mean on the arbitrarily-shaped Total-Text dataset, surpassing the previous state-of-the-art GLASS by 1.02\% in full-lexicon accuracy without additional training data, and obtains competitive 83.4\% strong-lexicon results on the multi-oriented ICDAR 2015 dataset.
匹配关键词: GPU optimization
---

[ACADEMIC - ARXIV]
标题: Buffer-Parameterized Machine Learning Surrogate Models for Cross-Technology Signal Integrity Analysis and Optimization
作者: Julian Withöft, Werner John, Emre Ecik, Ralf Brüning, Jürgen Götze
链接: https://arxiv.org/abs/2605.18170v1
完整摘要: Signal integrity (SI) analysis in printed circuit board (PCB) interconnects faces increasing complexity due to diverse integrated circuit (IC) buffer technologies, varying operating conditions, and manufacturing tolerances. Existing machine learning (ML) surrogate models for predicting SI metrics such as the inner eye contour, eye-height (EH), eye-width (EW), and transient waveform features typically rely on fixed buffer parameters, requiring costly new data generation and retraining cycles for every technology shift. This paper introduces a buffer-parameterized ML surrogate modeling methodology capable of handling cross-technology variations without retraining by treating IC buffer characteristics, e.g., clock frequency, supply voltage, rise/fall times, jitter, and internal resistors and capacitors, as dynamic model inputs alongside PCB parameters. To identify the optimal surrogate architecture for this high-dimensional space, a comprehensive benchmarking study compares tree-based methods (RFR/GBM), kernel methods (SVR/KRR), Gaussian process regression (GPR), and neural networks. The framework is subsequently validated on a complex interconnect with 44 design parameters. Results show that while anisotropic GPR excels in low-data regimes, neural networks heavily outperform other models on large datasets. Finally, the practical value of the ML surrogate models is demonstrated through a cross-technology design space exploration and optimization scenario, showcasing massive computational speedups for eye mask compliance checking compared to simulation.
匹配关键词: GPU optimization
---

[ACADEMIC - ARXIV]
标题: Whispers in the Noise: Surrogate-Guided Concept Awakening via a Multi-Agent Framework
作者: Mengyu Sun, Ziyuan Yang, Zunlong Zhou, Junxu Liu, Haibo Hu, Yi Zhang
链接: https://arxiv.org/abs/2605.18150v1
完整摘要: Diffusion models (DMs) are widely used for text-to-image generation, but their strong generative capabilities also raise concerns about unsafe or undesirable content. Concept erasure aims to mitigate these risks by removing specific concepts from pretrained models. However, recent studies show that such methods often suppress rather than fully eliminate target concepts, leaving models vulnerable to awakening attacks. Existing approaches primarily rely on white-box access through optimization or inversion, while concept awakening under black-box constraints remains underexplored. In this work, we revisit the denoising process from a trajectory perspective and show that concept erasure mainly disrupts early-stage text-semantic alignment but does not fully prevent semantic information from propagating along the denoising dynamics. As generation proceeds, the model increasingly depends on the evolving noisy state rather than textual conditions, which creates an opportunity to bypass erased mappings. Motivated by this observation, we propose ConceptAgent, a training-free, black-box, multi-agent framework that awakens erased concepts by initializing the denoising trajectory from surrogate-guided noisy states. Extensive experiments demonstrate that ConceptAgent enables accurate and controllable awakening of erased concepts under black-box settings without access to model parameters, gradients, or internal representations. These results highlight fundamental limitations of current concept erasure methods and provide new insights into the dynamic nature of semantic control in DMs.
匹配关键词: GPU optimization
---

[ACADEMIC - ARXIV]
标题: AtlasVA: Self-Evolving Visual Skill Memory for Teacher-Free VLM Agents
作者: Pan Wang, Yihao Hu, Xiujin Liu, Jingchu Yang, Hang Wang, Zhihao Wen
链接: https://arxiv.org/abs/2605.17933v1
完整摘要: Vision-language model (VLM) agents increasingly rely on memory-augmented reinforcement learning to reuse experience across long-horizon tasks, yet most existing frameworks store memory as text and depend on proprietary teacher models to summarize or refine it. This design is poorly matched to spatial decision making: geometric priors are compressed into lossy language, and sparse interaction is often supervised through delayed textual feedback rather than dense visually grounded signals. We argue that reusable experience for VLM agents should remain visually grounded. Based on this insight, we propose \textbf{AtlasVA}, a teacher-free visual skill memory framework that organizes memory into three complementary layers: spatial heatmaps, visual exemplars, and symbolic text skills. AtlasVA further evolves danger and affinity atlases directly from trajectory statistics and lightweight grid heuristics, and reuses these self-evolving atlases as potential-based shaping rewards for reinforcement learning. This unifies perception, memory, and optimization without external LLM supervision. Experiments on \textsc{Sokoban}, \textsc{FrozenLake}, 3D embodied navigation, and 3D robotic manipulation benchmarks show that AtlasVA consistently outperforms text-centric memory baselines and competitive VLM agents, with especially strong gains on spatially intensive tasks. Homepage: https://wangpan-ustc.github.io/AtlasvaWeb
匹配关键词: self-supervised
---

[ACADEMIC - ARXIV]
标题: HINT-SD: Targeted Hindsight Self-Distillation for Long-Horizon Agents
作者: Woongyeng Yeo, Yumin Choi, Taekyung Ki, Sung Ju Hwang
链接: https://arxiv.org/abs/2605.17873v1
完整摘要: Training long-horizon LLM agents with reinforcement learning is challenging because sparse outcome rewards reveal whether a task succeeds, but not which intermediate actions caused the outcome or how they should be corrected. Recent methods alleviate this issue by generating rewards or textual hints from turn-level action-output signals, or by using feedback-conditioned self-distillation. However, generating feedback at every turn is inefficient when many intermediate turns are already successful or neutral, and applying feedback at a fixed or misaligned turn often fails to supervise the actions that contributed to the failure. To bridge this gap, we propose HINT-SD, a targeted self-distillation framework that uses full-trajectory hindsight to select failure-relevant actions and applies feedback-conditioned distillation only on targeted action spans. Experiments on BFCL v3 and AppWorld show that our method improves over the dense per-turn feedback baseline by up to 18.80 percent while achieving 2.26$\times$ lower time per training step, suggesting that selecting where to distill is a key factor for both effective and efficient long-horizon agent training.
匹配关键词: self-supervised
---

[ACADEMIC - ARXIV]
标题: Multi-site PPG: An In-the-Wild Physiological Dataset from Emerging Multi-site Wearables
作者: Jiayi Shao, Jiaying Ye, Shengyao Liu, Zachary Englhardt, Girish Narayanswamy, Vikram Iyer, Qiuyue, Xue
链接: https://arxiv.org/abs/2605.17859v1
完整摘要: Wearables are widely used for mobile health monitoring, and photoplethysmography (PPG) is a key sensing modality for heart rate and related physiological measurements. However, public in-the-wild PPG datasets remain largely wrist-centric or limited to short, controlled studies, constraining research on emerging wearable form factors. We present Multi-site PPG, an in-the-wild physiological dataset collected from four custom-developed unobtrusive wearables: a smart earring, ring, watch, and necklace. Each device records green and infrared reflective PPG, 3-axis acceleration, and temperature with timestamps for cross-device alignment, while a Polar H10 chest strap provides reference electrocardiogram (ECG). Participants wore the devices for multiple days during daytime activities while continuing their normal routines. The dataset contains over 350 hours of raw data and 230-290 hours of modeling-ready 8-second windows per wearable. We benchmark heuristic, supervised, and self-supervised heart-rate estimation methods, showing substantial body-site differences: the best methods achieve mean absolute errors (MAEs) of 2.30 bpm on the earring, 5.13 bpm on the ring, 8.37 bpm on the watch, and 8.68 bpm on the necklace. We further analyze motion effects and evaluate multi-site and PPG-accelerometer fusion, demonstrating the dataset's value for robust physiological sensing across emerging wearable form factors.
匹配关键词: self-supervised
---

[ACADEMIC - ARXIV]
标题: AURORA: Contextual Orthogonalization for Geometric Representation Learning in Healthcare Foundation Models
作者: Yuanyun Zhang, Shi Li
链接: https://arxiv.org/abs/2605.17765v1
完整摘要: Recent healthcare foundation models have achieved strong predictive performance through large scale self supervised learning, yet their latent representations frequently entangle physiologic severity, intervention intensity, observational structure, and institutional workflow into shared embedding directions. While effective for downstream prediction, such representations remain semantically opaque and unstable under contextual shift. We introduce AURORA, Adaptive Uncertainty aware Representations through Orthogonalized Relational Alignment, a new framework for healthcare representation learning based on contextual latent geometry. Rather than optimizing a single unified embedding manifold, AURORA decomposes representations into orthogonal semantic subspaces corresponding to distinct contextual factors and learns relational consistency objectives within each subspace. This induces latent spaces that are both semantically disentangled and geometrically interpretable. Across multiple clinical prediction and retrieval tasks, AURORA consistently outperforms reconstruction, contrastive, and self distillation baselines while substantially improving contextual disentanglement, neighborhood purity, and robustness under institutional distribution shift. Our results suggest that latent geometry itself constitutes an important axis of healthcare foundation model design and that explicitly structuring representation space according to contextual semantics provides a complementary direction beyond conventional predictive compression objectives.
匹配关键词: self-supervised
---

[ACADEMIC - ARXIV]
标题: UST-Hand: An Uncertainty-aware Spatiotemporal Point Cloud Interaction Network for 3D Self-supervised Hand Pose Estimation
作者: Tianhao Han, Haoyang Zhang, Liang Xie, Haochen Chang, Kun Gao, Yuan Cheng, Pengfei Ren, Erwei Yin
链接: https://arxiv.org/abs/2605.17742v1
完整摘要: Manually annotating accurate 3D hand poses is extremely time-consuming and labor-intensive. Existing self-supervised hand pose estimation methods leverage the discrepancy between input images and rendered outputs, or multi-view consistency constraints, as the driving force to optimize networks and progressively refine pose accuracy. However, these methods are highly susceptible to noisy pseudo-labels and overlook the importance of fully exploiting fine-grained spatial correlations, which undermines the stability of model training. To address these issues, we propose UST-Hand, a self-supervised learning framework that estimates uncertainty distribution of hand pose and constructs a probabilistic point cloud feature space, which enables the complex spatiotemporal relationship modeling. UST-Hand employs a conditional normalizing flow model to capture hand pose distributions and samples diverse hypotheses, facilitating robust learning under noisy pseudo-labels supervision with enhanced stability. These multi-hypothesis are mapped to a unified probabilistic 3D point cloud space for multi-view and temporal feature interaction, comprehensively exploring hand motion patterns and fine-grained spatial correlations. Extensive experiments on three challenging datasets demonstrate that UST-Hand achieves state-of-the-art performance, outperforming existing self-supervised methods by up to 37.8% in Mean Per Vertex Position Error (MPVPE).
匹配关键词: self-supervised
---

[ACADEMIC - ARXIV]
标题: Are Sparse Autoencoder Benchmarks Reliable?
作者: David Chanin
链接: https://arxiv.org/abs/2605.18229v1
完整摘要: Sparse autoencoders (SAEs) are a core interpretability tool for large language models, and progress on SAE architectures depends on benchmarks that reliably distinguish better SAEs from worse ones. We audit the SAE quality metrics in SAEBench, the de-facto standard SAE evaluation suite, through three complementary lenses: reseed noise on a fixed SAE, ground-truth correlation on synthetic SAEs, and discriminability across training trajectories. We find that two of these metrics, Targeted Probe Perturbation (TPP) and Spurious Correlation Removal (SCR), fail multiple lenses at their canonical settings and should not be used to evaluate SAEs. The other metrics show higher reseed noise and lower discriminability than the field assumes. The sae-probes variant of $k$-sparse probing is the most reliable metric we tested, but even sae-probes struggles to separate variants of the same SAE architecture. Our results show the field needs better SAE benchmarks.
匹配关键词: contrastive learning
---

[ACADEMIC - ARXIV]
标题: Context Memorization for Efficient Long Context Generation
作者: Yasuyuki Okoshi, Hao Mark Chen, Guanxi Lu, Hongxiang Fan, Masato Motomura, Daichi Fujiki
链接: https://arxiv.org/abs/2605.18226v1
完整摘要: Modern large language model (LLM) applications increasingly rely on long conditioning prefixes to control model behavior at inference time. While prefix-augmented inference is effective, it incurs two structural limitations: i) the prefix's influence fades as generation proceeds, and ii) attention computation over the prefix scales linearly with its length. Existing approaches either keep the prefix in attention while compressing it, or internalize it into model parameters through gradient-based training. The former still attends to the prefix at inference, while the latter is training-intensive and ill-suited to prefix updates. To address these issues, we propose attention-state memory, a training-free approach that externalizes the prefix into a lightweight, lookup-based memory of precomputed attention states between prefix and query tokens. On ManyICLBench with LLaMA-3.1-8B, our method improves accuracy over in-context learning at 1K-8K memory budgets while reducing attention latency by 1.36x at 8K, and surpasses full-attention RAG performance on NBA benchmark using only 20% of its memory footprint.
匹配关键词: contrastive learning
---

[ACADEMIC - ARXIV]
标题: A Simplex Witness Certificate for Constant Collapse in Variational Autoencoders
作者: Zegu Zhang, Jianhua Peng, Jian Zhang
链接: https://arxiv.org/abs/2605.18224v1
完整摘要: This note studies exact constant collapse in variational autoencoders, where the encoder mean becomes independent of the input. The goal is to make this specific failure mode pre-designable, monitorable during training, and certifiable after training. The prior is kept as the standard Gaussian. Given a fixed teacher posterior, we attach to the latent mean a fixed simplex witness head. The resulting teacher-student alignment loss has an exact constant-predictor baseline equal to the teacher information. If the alignment loss is below this baseline, the latent mean cannot be input-independent constant collapsed. The simplex witness also has a closed-form inverse. Any full-support teacher posterior can be represented by embedding its centered log-odds into the latent space. This gives an explicit latent energy cost and explains when the alignment loss can be made small. A computable view gap handles the case where teacher targets are computed from a different view. Thus exact constant collapse is converted from an after-the-fact training pathology into a design-and-certificate problem.
匹配关键词: contrastive learning
---

[ACADEMIC - ARXIV]
标题: SIREM: Speech-Informed MRI Reconstruction with Learned Sampling
作者: Md Hasan, Nyvenn Castro, Daiqi Liu, Lukas Mulzer, Jana Hutter, Jonghye Woo, Moritz Zaiss, Andreas Maier, Paula A. Perez-Toro
链接: https://arxiv.org/abs/2605.18221v1
完整摘要: Real-time magnetic resonance imaging (rtMRI) of speech production enables non-invasive visualization of dynamic vocal-tract motion and is valuable for speech science and clinical assessment. However, rtMRI is fundamentally constrained by trade-offs among spatial resolution, temporal resolution, and acquisition speed, often leading to undersampled k-space measurements and degraded reconstructions. We propose SIREM, a speech-informed MRI reconstruction framework that uses synchronized speech as a cross-modal prior. The central idea is that vocal-tract configurations during speech are correlated with the produced acoustics, making part of the image content predictable from audio. SIREM models each frame as a fusion of an audio-driven component and an MRI-driven component through a spatial weighting map. The audio branch predicts articulator-related structure from speech, while the MRI branch reconstructs complementary content from measured k-space data. We further introduce a learnable soft weighting profile over spiral arms, enabling a differentiable study of how k-space arm usage interacts with speech-informed fusion. This yields a unified multimodal formulation that combines audio-driven prediction, MRI reconstruction, and sampling adaptation. We evaluate SIREM on the USC speech rtMRI benchmark against standard baselines, including gridding, wavelet-based compressed sensing, and total variation. SIREM introduces a speech-informed reconstruction paradigm that operates in a substantially higher-throughput regime than iterative methods while preserving anatomically plausible vocal-tract structure. These results establish an initial benchmark for multimodal speech-informed rtMRI reconstruction and highlight the potential of synchronized speech as an auxiliary prior for fast reconstruction. The source code is available at https://github.com/mdhasanai/SIREM
匹配关键词: contrastive learning
---

[ACADEMIC - ARXIV]
标题: Forward-Learned Discrete Diffusion: Learning how to noise to denoise faster
作者: Grigory Bartosh, Teodora Pandeva, Sushrut Karmalkar, Javier Zazo
链接: https://arxiv.org/abs/2605.18204v1
完整摘要: Discrete diffusion models are a powerful class of generative models with strong performance across many domains. For efficiency, however, discrete diffusion typically parameterizes the generative (reverse) process with factorized distributions, which makes it difficult for the model to learn the target process in a small number of steps and necessitates a long, computationally expensive sampling procedure. To reduce the gap between the target and model distributions and enable few-step generation, we propose Forward-Learned Discrete Diffusion (FLDD), which introduces discrete diffusion with a learnable forward (noising) process. Rather than fixing a Markovian forward chain, we adopt a non-Markovian formulation with learnable marginal and posterior distributions. This allows the generative process to remain factorized while matching the target defined by the noising process. We train all parameters end-to-end under the standard variational objective. Experiments on various benchmarks show that, for a given number of sampling steps, our approach produces a higher quality samples than conventional discrete diffusion models using the same reverse parameterization.
匹配关键词: contrastive learning
---

[ACADEMIC - ARXIV]
标题: Are Sparse Autoencoder Benchmarks Reliable?
作者: David Chanin
链接: https://arxiv.org/abs/2605.18229v1
完整摘要: Sparse autoencoders (SAEs) are a core interpretability tool for large language models, and progress on SAE architectures depends on benchmarks that reliably distinguish better SAEs from worse ones. We audit the SAE quality metrics in SAEBench, the de-facto standard SAE evaluation suite, through three complementary lenses: reseed noise on a fixed SAE, ground-truth correlation on synthetic SAEs, and discriminability across training trajectories. We find that two of these metrics, Targeted Probe Perturbation (TPP) and Spurious Correlation Removal (SCR), fail multiple lenses at their canonical settings and should not be used to evaluate SAEs. The other metrics show higher reseed noise and lower discriminability than the field assumes. The sae-probes variant of $k$-sparse probing is the most reliable metric we tested, but even sae-probes struggles to separate variants of the same SAE architecture. Our results show the field needs better SAE benchmarks.
匹配关键词: representation learning
---

[ACADEMIC - ARXIV]
标题: Context Memorization for Efficient Long Context Generation
作者: Yasuyuki Okoshi, Hao Mark Chen, Guanxi Lu, Hongxiang Fan, Masato Motomura, Daichi Fujiki
链接: https://arxiv.org/abs/2605.18226v1
完整摘要: Modern large language model (LLM) applications increasingly rely on long conditioning prefixes to control model behavior at inference time. While prefix-augmented inference is effective, it incurs two structural limitations: i) the prefix's influence fades as generation proceeds, and ii) attention computation over the prefix scales linearly with its length. Existing approaches either keep the prefix in attention while compressing it, or internalize it into model parameters through gradient-based training. The former still attends to the prefix at inference, while the latter is training-intensive and ill-suited to prefix updates. To address these issues, we propose attention-state memory, a training-free approach that externalizes the prefix into a lightweight, lookup-based memory of precomputed attention states between prefix and query tokens. On ManyICLBench with LLaMA-3.1-8B, our method improves accuracy over in-context learning at 1K-8K memory budgets while reducing attention latency by 1.36x at 8K, and surpasses full-attention RAG performance on NBA benchmark using only 20% of its memory footprint.
匹配关键词: representation learning
---

[ACADEMIC - ARXIV]
标题: A Simplex Witness Certificate for Constant Collapse in Variational Autoencoders
作者: Zegu Zhang, Jianhua Peng, Jian Zhang
链接: https://arxiv.org/abs/2605.18224v1
完整摘要: This note studies exact constant collapse in variational autoencoders, where the encoder mean becomes independent of the input. The goal is to make this specific failure mode pre-designable, monitorable during training, and certifiable after training. The prior is kept as the standard Gaussian. Given a fixed teacher posterior, we attach to the latent mean a fixed simplex witness head. The resulting teacher-student alignment loss has an exact constant-predictor baseline equal to the teacher information. If the alignment loss is below this baseline, the latent mean cannot be input-independent constant collapsed. The simplex witness also has a closed-form inverse. Any full-support teacher posterior can be represented by embedding its centered log-odds into the latent space. This gives an explicit latent energy cost and explains when the alignment loss can be made small. A computable view gap handles the case where teacher targets are computed from a different view. Thus exact constant collapse is converted from an after-the-fact training pathology into a design-and-certificate problem.
匹配关键词: representation learning
---

[ACADEMIC - ARXIV]
标题: SIREM: Speech-Informed MRI Reconstruction with Learned Sampling
作者: Md Hasan, Nyvenn Castro, Daiqi Liu, Lukas Mulzer, Jana Hutter, Jonghye Woo, Moritz Zaiss, Andreas Maier, Paula A. Perez-Toro
链接: https://arxiv.org/abs/2605.18221v1
完整摘要: Real-time magnetic resonance imaging (rtMRI) of speech production enables non-invasive visualization of dynamic vocal-tract motion and is valuable for speech science and clinical assessment. However, rtMRI is fundamentally constrained by trade-offs among spatial resolution, temporal resolution, and acquisition speed, often leading to undersampled k-space measurements and degraded reconstructions. We propose SIREM, a speech-informed MRI reconstruction framework that uses synchronized speech as a cross-modal prior. The central idea is that vocal-tract configurations during speech are correlated with the produced acoustics, making part of the image content predictable from audio. SIREM models each frame as a fusion of an audio-driven component and an MRI-driven component through a spatial weighting map. The audio branch predicts articulator-related structure from speech, while the MRI branch reconstructs complementary content from measured k-space data. We further introduce a learnable soft weighting profile over spiral arms, enabling a differentiable study of how k-space arm usage interacts with speech-informed fusion. This yields a unified multimodal formulation that combines audio-driven prediction, MRI reconstruction, and sampling adaptation. We evaluate SIREM on the USC speech rtMRI benchmark against standard baselines, including gridding, wavelet-based compressed sensing, and total variation. SIREM introduces a speech-informed reconstruction paradigm that operates in a substantially higher-throughput regime than iterative methods while preserving anatomically plausible vocal-tract structure. These results establish an initial benchmark for multimodal speech-informed rtMRI reconstruction and highlight the potential of synchronized speech as an auxiliary prior for fast reconstruction. The source code is available at https://github.com/mdhasanai/SIREM
匹配关键词: representation learning
---

[ACADEMIC - ARXIV]
标题: Forward-Learned Discrete Diffusion: Learning how to noise to denoise faster
作者: Grigory Bartosh, Teodora Pandeva, Sushrut Karmalkar, Javier Zazo
链接: https://arxiv.org/abs/2605.18204v1
完整摘要: Discrete diffusion models are a powerful class of generative models with strong performance across many domains. For efficiency, however, discrete diffusion typically parameterizes the generative (reverse) process with factorized distributions, which makes it difficult for the model to learn the target process in a small number of steps and necessitates a long, computationally expensive sampling procedure. To reduce the gap between the target and model distributions and enable few-step generation, we propose Forward-Learned Discrete Diffusion (FLDD), which introduces discrete diffusion with a learnable forward (noising) process. Rather than fixing a Markovian forward chain, we adopt a non-Markovian formulation with learnable marginal and posterior distributions. This allows the generative process to remain factorized while matching the target defined by the noising process. We train all parameters end-to-end under the standard variational objective. Experiments on various benchmarks show that, for a given number of sampling steps, our approach produces a higher quality samples than conventional discrete diffusion models using the same reverse parameterization.
匹配关键词: representation learning
---

[ACADEMIC - ARXIV]
标题: Are Sparse Autoencoder Benchmarks Reliable?
作者: David Chanin
链接: https://arxiv.org/abs/2605.18229v1
完整摘要: Sparse autoencoders (SAEs) are a core interpretability tool for large language models, and progress on SAE architectures depends on benchmarks that reliably distinguish better SAEs from worse ones. We audit the SAE quality metrics in SAEBench, the de-facto standard SAE evaluation suite, through three complementary lenses: reseed noise on a fixed SAE, ground-truth correlation on synthetic SAEs, and discriminability across training trajectories. We find that two of these metrics, Targeted Probe Perturbation (TPP) and Spurious Correlation Removal (SCR), fail multiple lenses at their canonical settings and should not be used to evaluate SAEs. The other metrics show higher reseed noise and lower discriminability than the field assumes. The sae-probes variant of $k$-sparse probing is the most reliable metric we tested, but even sae-probes struggles to separate variants of the same SAE architecture. Our results show the field needs better SAE benchmarks.
匹配关键词: masked language model
---

[ACADEMIC - ARXIV]
标题: Context Memorization for Efficient Long Context Generation
作者: Yasuyuki Okoshi, Hao Mark Chen, Guanxi Lu, Hongxiang Fan, Masato Motomura, Daichi Fujiki
链接: https://arxiv.org/abs/2605.18226v1
完整摘要: Modern large language model (LLM) applications increasingly rely on long conditioning prefixes to control model behavior at inference time. While prefix-augmented inference is effective, it incurs two structural limitations: i) the prefix's influence fades as generation proceeds, and ii) attention computation over the prefix scales linearly with its length. Existing approaches either keep the prefix in attention while compressing it, or internalize it into model parameters through gradient-based training. The former still attends to the prefix at inference, while the latter is training-intensive and ill-suited to prefix updates. To address these issues, we propose attention-state memory, a training-free approach that externalizes the prefix into a lightweight, lookup-based memory of precomputed attention states between prefix and query tokens. On ManyICLBench with LLaMA-3.1-8B, our method improves accuracy over in-context learning at 1K-8K memory budgets while reducing attention latency by 1.36x at 8K, and surpasses full-attention RAG performance on NBA benchmark using only 20% of its memory footprint.
匹配关键词: masked language model
---

[ACADEMIC - ARXIV]
标题: Contextual Biasing for Streaming ASR via CTC-based Word Spotting
作者: Kai-Chen Tsai, Tien-Hong Lo, Yun-Ting Sun, Berlin Chen
链接: https://arxiv.org/abs/2605.18222v1
完整摘要: Contextual biasing is essential to improving the recognition of rare and domain-specific words in an automatic speech recognition (ASR) system. While numerous methods have been proposed in recent years, most of them focus on offline settings and do not explicitly address the challenges of streaming ASR. For example, CTC-based word spotting (CTC-WS) have demonstrated strong performance by directly detecting keywords from CTC log-probabilities, but they are limited to offline processing and require access to the full utterance. In This work, we present a streaming extension of CTC-WS for real-time contextual biasing. Our method maintains active keyword paths across audio chunks using a stateful token passing algorithm, enabling the detection of keywords that span multiple chunks. To ensure low latency and stable output, we introduce an incremental commitment mechanism that only emits segments guaranteed not to be affected by future audio, while deferring uncertain regions. This method naturally integrates with streaming ASR pipelines and does not require modifications to the underlying acoustic model or additional training, making it practical for real-world deployment. Experimental results show that our method reduces overall WER and effectively improves keyword F-score, demonstrating its effectiveness for real-time ASR applications.
匹配关键词: masked language model
---

[ACADEMIC - ARXIV]
标题: SIREM: Speech-Informed MRI Reconstruction with Learned Sampling
作者: Md Hasan, Nyvenn Castro, Daiqi Liu, Lukas Mulzer, Jana Hutter, Jonghye Woo, Moritz Zaiss, Andreas Maier, Paula A. Perez-Toro
链接: https://arxiv.org/abs/2605.18221v1
完整摘要: Real-time magnetic resonance imaging (rtMRI) of speech production enables non-invasive visualization of dynamic vocal-tract motion and is valuable for speech science and clinical assessment. However, rtMRI is fundamentally constrained by trade-offs among spatial resolution, temporal resolution, and acquisition speed, often leading to undersampled k-space measurements and degraded reconstructions. We propose SIREM, a speech-informed MRI reconstruction framework that uses synchronized speech as a cross-modal prior. The central idea is that vocal-tract configurations during speech are correlated with the produced acoustics, making part of the image content predictable from audio. SIREM models each frame as a fusion of an audio-driven component and an MRI-driven component through a spatial weighting map. The audio branch predicts articulator-related structure from speech, while the MRI branch reconstructs complementary content from measured k-space data. We further introduce a learnable soft weighting profile over spiral arms, enabling a differentiable study of how k-space arm usage interacts with speech-informed fusion. This yields a unified multimodal formulation that combines audio-driven prediction, MRI reconstruction, and sampling adaptation. We evaluate SIREM on the USC speech rtMRI benchmark against standard baselines, including gridding, wavelet-based compressed sensing, and total variation. SIREM introduces a speech-informed reconstruction paradigm that operates in a substantially higher-throughput regime than iterative methods while preserving anatomically plausible vocal-tract structure. These results establish an initial benchmark for multimodal speech-informed rtMRI reconstruction and highlight the potential of synchronized speech as an auxiliary prior for fast reconstruction. The source code is available at https://github.com/mdhasanai/SIREM
匹配关键词: masked language model
---

[ACADEMIC - ARXIV]
标题: EgoInteract: Synthetic Egocentric Videos Generation for Interaction Understanding and Anticipation
作者: Rosario Leonardi, Francesco Ragusa, Daniele Materia, Alessandro Passanisi, James Fort, Jakob Engel, Giovanni Maria Farinella
链接: https://arxiv.org/abs/2605.18214v1
完整摘要: Collecting large-scale egocentric video datasets with dense spatial and temporal annotations is costly, slow, and often constrained by environmental biases, privacy constraints, and limited coverage of interaction patterns. While synthetic data has shown strong potential in several vision domains, its use for egocentric perception remains relatively underexplored, especially for tasks requiring temporally coherent human-object interactions. In this work, we introduce EgoInteract, a controllable simulator for egocentric video generation designed to model fine-grained egocentric interactions and their temporal dynamics. The simulator enables precise control over camera, human body and hand motion, object manipulation, and scene composition across diverse environments. Building on this framework, we generate a synthetic egocentric video dataset with dense spatial and temporal annotations for temporal action segmentation, next-active object detection, interaction anticipation, and hand-object interaction detection. We evaluate models trained with simulated data on multiple real-world egocentric benchmarks spanning diverse environments, object categories, and interaction patterns. Results show consistent improvements over strong baselines across tasks and datasets, demonstrating the effectiveness and transferability of our simulation-based approach.
匹配关键词: masked language model
---

[ACADEMIC - ARXIV]
标题: TinySSL: Distilled Self-Supervised Pretraining for Sub-Megabyte MCU Models
作者: Bibin Wilson
链接: https://arxiv.org/abs/2605.08241v1
完整摘要: Self-supervised learning (SSL) has transformed representation learning for large models, yet remains unexplored for microcontroller (MCU)-class models with fewer than 500K parameters. We identify three obstacles at this scale -- projection head dominance, representation bottleneck, and augmentation sensitivity -- and propose Capacity-Aware Distilled Self-Supervised Learning (CA-DSSL), a teacher-guided framework that overcomes them without labels or text supervision. CA-DSSL combines asymmetric distillation from a frozen DINO ViT-S/16 teacher, multi-scale feature distillation for spatial representations, and a progressive augmentation curriculum. On a MobileNetV2-0.35 backbone (396K parameters) pretrained on CIFAR-100, CA-DSSL reaches 62.7 0.5% linear-probe accuracy (3-seed mean) -- surpassing SimCLR-Tiny by 18 pp, matching SEED (61.7%) with 10 fewer projection parameters (426K vs. 3.15M), and reaching 94.0% of a supervised upper bound. Standard SSL methods (BYOL-Tiny, DINO-Tiny) collapse entirely at this scale. On Pascal VOC detection, CA-DSSL achieves 2.3 the mAP of random initialization and +3 pp over SEED, though SimCLR-Tiny matches CA-DSSL on detection mAP. The deployed backbone occupies 378 KB (INT8) with no inference overhead from pretraining. Preliminary ImageNet-100 experiments reveal that CA-DSSL's advantage is specific to small-data regimes; scaling to ImageNet-1K is discussed as future work.
匹配关键词: SimCLR
---

[ACADEMIC - ARXIV]
标题: TumorXAI: Self-Supervised Deep Learning Framework for Explainable Brain MRI Tumor Classification
作者: Abrar Hossain Zahin, Amit Kumar Saha, Tanvir Mridha, Saifur Rahman, Jannatul Ferdous Prome, Raima Husna, Israt Jahan, Ahmed Wasif Reza
链接: https://arxiv.org/abs/2605.01999v1
完整摘要: Classifying brain tumors using magnetic resonance imaging (MRI) is crucial for early diagnosis and treatment; however, tumor heterogeneity and a dearth of annotated datasets restrict the use of supervised deep learning approaches. In this work, we use self-supervised learning (SSL) to study multi-class brain tumor classification. Using a ResNet-50 backbone, we evaluate four SSL frameworks including SimCLR, BYOL, DINO, and Moco v3 on a publicly available dataset of 4,448 MRIs with 17 distinct tumor types. On the dataset, SimCLR achieved 99.64% accuracy, 99.64% precision, 99.64% recall, and 99.64% F1-score. The workflow includes preprocessing, fine-tuning, linear evaluation, and SSL pretraining with data augmentations. Results show that, when labels are limited, SSL-pretrained models outperform supervised baselines in terms of F1-score, recall, accuracy, and precision. Additionally, by providing visual insights into model decisions, Explainable AI techniques (Grad-CAM, Grad-CAM++, EigenCAM) enhance interpretability. These results demonstrate SSL's scalability and dependability in diagnosing brain tumors from unlabeled medical data.
匹配关键词: SimCLR
---

[ACADEMIC - ARXIV]
标题: ProtoFair: Fair Self-Supervised Contrastive Learning via Pseudo-Counterfactual Pairs
作者: Marah Halawa, Olaf Hellwich
链接: https://arxiv.org/abs/2605.01971v1
完整摘要: Self-supervised learning methods learn high-quality visual representations, yet recent studies show that these representations often capture demographic biases present in the training data. Existing fairness-aware methods address this by redesigning the self-supervised objective itself, limiting portability across the rapidly evolving landscape of self-supervised learning (SSL) frameworks. We propose ProtoFair, a fairness-aware contrastive loss designed to work alongside existing SSL objectives without modifying them. ProtoFair leverages unsupervised prototype clustering to identify pseudo-counterfactual pairs: samples sharing the same cluster assignment but belonging to different sensitive groups. By pulling these content-matched, cross-group samples together in the embedding space, ProtoFair encourages the encoder to learn representations that are invariant to the sensitive attribute. The method requires only sensitive attribute annotations, no target labels, and integrates seamlessly with both SimCLR and SupCon. Experiments on CelebA and UTKFace demonstrate consistent fairness improvements while maintaining competitive accuracy.
匹配关键词: SimCLR
---

[ACADEMIC - ARXIV]
标题: Trust-SSL: Additive-Residual Selective Invariance for Robust Aerial Self-Supervised Learning
作者: Wadii Boulila, Adel Ammar, Bilel Benjdira, Maha Driss
链接: https://arxiv.org/abs/2604.21349v1
完整摘要: Self-supervised learning (SSL) is a standard approach for representation learning in aerial imagery. Existing methods enforce invariance between augmented views, which works well when augmentations preserve semantic content. However, aerial images are frequently degraded by haze, motion blur, rain, and occlusion that remove critical evidence. Enforcing alignment between a clean and a severely degraded view can introduce spurious structure into the latent space. This study proposes a training strategy and architectural modification to enhance SSL robustness to such corruptions. It introduces a per-sample, per-factor trust weight into the alignment objective, combined with the base contrastive loss as an additive residual. A stop-gradient is applied to the trust weight instead of a multiplicative gate. While a multiplicative gate is a natural choice, experiments show it impairs the backbone, whereas our additive-residual approach improves it. Using a 200-epoch protocol on a 210,000-image corpus, the method achieves the highest mean linear-probe accuracy among six backbones on EuroSAT, AID, and NWPU-RESISC45 (90.20% compared to 88.46% for SimCLR and 89.82% for VICReg). It yields the largest improvements under severe information-erasing corruptions on EuroSAT (+19.9 points on haze at s=5 over SimCLR). The method also demonstrates consistent gains of +1 to +3 points in Mahalanobis AUROC on a zero-shot cross-domain stress test using BDD100K weather splits. Two ablations (scalar uncertainty and cosine gate) indicate the additive-residual formulation is the primary source of these improvements. An evidential variant using Dempster-Shafer fusion introduces interpretable signals of conflict and ignorance. These findings offer a concrete design principle for uncertainty-aware SSL. Code is publicly available at https://github.com/WadiiBoulila/trust-ssl.
匹配关键词: SimCLR
---

[ACADEMIC - ARXIV]
标题: Membership Inference Attacks Expose Participation Privacy in ECG Foundation Encoders
作者: Ziyu Wang, Elahe Khatibi, Ankita Sharma, Krishnendu Chakrabarty, Sanaz Rahimi Moosavi, Farshad Firouzi, Amir Rahmani
链接: https://arxiv.org/abs/2604.10424v1
完整摘要: Foundation-style ECG encoders pretrained with self-supervised learning are increasingly reused across tasks, institutions, and deployment contexts, often through model-as-a-service interfaces that expose scalar scores or latent representations. While such reuse improves data efficiency and generalization, it raises a participation privacy concern: can an adversary infer whether a specific individual or cohort contributed ECG data to pretraining, even when raw waveforms and diagnostic labels are never disclosed? In connected-health settings, training participation itself may reveal institutional affiliation, study enrollment, or sensitive health context. We present an implementation-grounded audit of membership inference attacks (MIAs) against modern self-supervised ECG foundation encoders, covering contrastive objectives (SimCLR, TS2Vec) and masked reconstruction objectives (CNN- and Transformer-based MAE). We evaluate three realistic attacker interfaces: (i) score-only black-box access to scalar outputs, (ii) adaptive learned attackers that aggregate subject-level statistics across repeated queries, and (iii) embedding-access attackers that probe latent representation geometry. Using a subject-centric protocol with window-to-subject aggregation and calibration at fixed false-positive rates under a cross-dataset auditing setting, we observe heterogeneous and objective-dependent participation leakage: leakage is most pronounced in small or institution-specific cohorts and, for contrastive encoders, can saturate in embedding space, while larger and more diverse datasets substantially attenuate operational tail risk. Overall, our results show that restricting access to raw signals or labels is insufficient to guarantee participation privacy, underscoring the need for deployment-aware auditing of reusable biosignal foundation encoders in connected-health systems.
匹配关键词: SimCLR
---

[ACADEMIC - ARXIV]
标题: Xiaomi EV World Model: A Joint World Model Integrating Reconstruction and Generation for Autonomous Driving
作者: Lijun Zhou, Hongcheng Luo, Zhenxin Zhu, Cheng Chi, Mingfei Tu, Kaixin Xiong, Lei Gong, Zhanqian Wu, Zehan Zhang, Fangzhen Li, Hao Li, Yingying Shen, Jiale He, Haohui Zhu, Shan Zhao, Kai Wang, Zhiwei Zhan, Yuechuan Pu, Kaiyuan Tan, Ruiling Yang, Xianqi Wang, Tianyi Yan, Jiawei Zhou, Lei Zhang, Jingyang Zhao, Xi Zhou, Chitian Sun, Chenming Wu, Jiong Deng, Hongwei Xie, Ming Lu, Kun Ma, Long Chen, Guang Chen, Hangjun Ye, Bing Wang, Haiyang Sun
链接: https://arxiv.org/abs/2605.18137v1
完整摘要: This report presents a unified technical system addressing the two core capabilities of world models for autonomous driving: world representation and world generation. For world representation, we propose WorldRec, a feed-forward reconstruction architecture driven by sparse scene queries. WorldRec initializes structured queries in 3D space, leveraging them to aggregate cross-view, cross-temporal features, thereby naturally enforcing spatial consistency across frames and yielding compact yet high-fidelity 3D Gaussian scene representations. For world generation, we propose WorldGen, a two-stage training framework of bidirectional pretraining followed by causal fine-tuning through three progressive stages (Teacher Forcing, ODE distillation, and DMD), enabling high-quality online causal video generation in as few as 4 denoising steps. Building on both modules, we further introduce the JWM, which deeply integrates WorldRec and WorldGen to achieve synergistic gains in generation stability, cross-frame consistency, and visual fidelity, providing a solid foundation for closed-loop simulation, data synthesis, and end-to-end training in autonomous driving.
匹配关键词: MAE
---

[ACADEMIC - ARXIV]
标题: Who Generated This 3D Asset? Learning Source Attribution for Generative 3D Models
作者: Sihan Ma, Siyuan Liang, Dacheng Tao
链接: https://arxiv.org/abs/2605.18132v1
完整摘要: Generative 3D models are deployed in gaming, robotics, and immersive creation, making source attribution critical: given a 3D asset, can we identify whether and which generative model created it? This problem faces two core challenges: dispersed attribution signals, where 3D fingerprints are distributed across multi-view, geometric, and frequency-domain cues; and realistic deployment constraints, where scarce labels, degraded prompts, and mixed real/synthetic assets undermine attribution reliability. To systematically study this problem, we construct, to the best of our knowledge, the first passive source attribution benchmark for modern generated assets, covering 22 representative 3D generators under standard, few-shot, and realistic deployment protocols. Based on this benchmark, we find that generative 3D models leave two types of stable fingerprints: cross-view inconsistency and structural artifacts reflected in geometric statistics and frequency-domain cues. To capture these dispersed signals, we propose a hierarchical multi-view multi-modal Transformer that fuses appearance, geometric, and frequency-domain features within each view and models global relationships across views. Extensive experiments demonstrate strong performance, achieving 97.22% accuracy under full supervision and 77.17% accuracy with only 1% training data, corresponding to fewer than five samples per generator. These results show that modern 3D generators leave stable and attributable fingerprints, establishing a new benchmark and methodological foundation for trustworthy 3D content provenance.
匹配关键词: MAE
---

[ACADEMIC - ARXIV]
标题: The MixCount Dataset: Bridging the Data Gap for Open-Vocabulary Object Counting
作者: Corentin Dumery, Niki Amini-Naieni, Shervin Naini, Pascal Fua
链接: https://arxiv.org/abs/2605.18063v1
完整摘要: Object counting is a foundational vision task with over a decade of dedicated research, yet state-of-the-art models still fail systematically in the mixed-object setting that dominates real-world applications such as industrial inspection and product sorting. We show that this gap is strongly driven by limitations in existing training and evaluation data: real counting datasets are prohibitively expensive to annotate and suffer from labeling noise, while existing synthetic alternatives lack diversity and realism. We address this with MixCount, a dataset and benchmark for mixed-object counting designed to target the failure modes of current counting models. To overcome the high cost of constructing and labeling such data, we develop an automatic generation pipeline that synthesizes images, fine-grained textual descriptions, and pixel-perfect counting annotations at scale, eliminating the labeling ambiguity that plagues prior datasets. Evaluating state-of-the-art counting models on MixCount exposes severe degradation in the mixed-object setting. More importantly, training these models on our synthesized data yields substantial gains on real-world benchmarks, reducing MAE by 20.14% on FSC-147 and by 18.3% on PairTally. These results establish MixCount as both a benchmark and a training dataset for fine-grained counting, and demonstrate that our pipeline, which produces effectively unlimited labeled data, helps address a long-standing bottleneck in counting models.
匹配关键词: MAE
---

[ACADEMIC - ARXIV]
标题: Bench2Drive-Robust: Benchmarking Closed-Loop Autonomous Driving under Deployment Perturbations
作者: Zhiyuan Zhang, Zhenghao Jin, Yanlun Peng, Xianda Guo, Haoran Liu, Shaofeng Zhang, Xingjun Ma, Zuxuan Wu, Junchi Yan, Xiaosong Jia, Yu-Gang Jiang
链接: https://arxiv.org/abs/2605.18059v1
完整摘要: Robustness is a critical requirement for deploying autonomous driving systems in the real world. Existing robustness benchmarks for autonomous driving have made important progress in studying the effects of image-level corruptions, such as adverse weather or camera degradation, on perception modules and open-loop planning outputs. However, deployment can also involve system-level imperfections, such as inference latency and ego-state estimation errors, which remain less studied in closed-loop E2E-AD evaluation. These imperfections can accumulate through the feedback loop and destabilize control. In this work, we present Bench2Drive-Robust, to our knowledge the first device-centric robustness benchmark for closed-loop end-to-end autonomous driving under realistic deployment perturbations. We systematically evaluate deployment-oriented perturbations arising from three major sources: camera-stream failures (frame drop, partial observation), ego-state estimation errors (GPS noise, and speed or odometry errors), and compute-induced control delay (model inference delay). We evaluate representative end-to-end driving methods and analyze their robustness under different perturbation severities. Our results show that these deployment-related perturbations can substantially degrade closed-loop driving performance, revealing robustness challenges that are not fully captured by conventional image-level corruption evaluations. By establishing a closed-loop evaluation protocol and demonstrating the substantial impact of these deployment-oriented perturbations, Bench2Drive-Robust defines practical robustness problems for end-to-end autonomous driving and encourages further research on deployment-aware robust driving systems.
匹配关键词: MAE
---

[ACADEMIC - ARXIV]
标题: TeleCom-Bench: How Far Are Large Language Models from Industrial Telecommunication Applications?
作者: Jieting Xiao, Yun Lin, Huizhen Qiu, Rui Ma, Chen Zhong, Dongyang Xu, Xiao Long, Chaoyu Zhang, Qiaobo Hao, Ding Zou, Zhiguo Yang, Yanqin Gao, Fang Tan
链接: https://arxiv.org/abs/2605.18025v1
完整摘要: While Large Language Models have achieved remarkable integration in various vertical scenarios, their deployment in the telecommunications domain remains exploratory due to the lack of a standardized evaluation framework. Current telecom benchmarks primarily focus on static, foundational knowledge and isolated atomic skills, neglecting the equipment-specific documentation and end-to-end industrial workflows essential for real-world production systems. To bridge this gap, we present TeleCom-Bench, a comprehensive benchmark comprising 12 evaluation sets with 22,678 curated samples, which evaluates LLMs across a synergistic hierarchy: (1) Multi-dimensional Knowledge Comprehension, which integrates telecommunication fundamentals, 3GPP protocols, and 5G network architecture with proprietary product knowledge across wired, core, and wireless networks via knowledge graph-driven synthesis; and (2)End-to-End Knowledge Application, which formalizes six core tasks on authentic trajectories from live network agent workflows, including intent recognition, entity extraction, event verification, tool invocation, root cause analysis, and solution generation-across network optimization and fault maintenance scenarios. Evaluations of eight state-of-the-art LLMs reveal a universal Execution Wall: while models achieve 90% accuracy in linguistic interface tasks such as intent recognition and entity extraction, performance collapses to approximately 30% in procedural execution tasks like solution generation. This capability gap demonstrates that current LLMs function competently as diagnosticians but fail as field engineers. TeleCom-Bench provides standardized diagnostics to precisely pinpoint this deficit, offering actionable guidance for domain-specific alignment toward production-ready telecom agents. The dataset and evaluation code have been released at https://github.com/ZTE-AICloud/TeleCom-Bench.
匹配关键词: MAE
---

[ACADEMIC - ARXIV]
标题: Are Sparse Autoencoder Benchmarks Reliable?
作者: David Chanin
链接: https://arxiv.org/abs/2605.18229v1
完整摘要: Sparse autoencoders (SAEs) are a core interpretability tool for large language models, and progress on SAE architectures depends on benchmarks that reliably distinguish better SAEs from worse ones. We audit the SAE quality metrics in SAEBench, the de-facto standard SAE evaluation suite, through three complementary lenses: reseed noise on a fixed SAE, ground-truth correlation on synthetic SAEs, and discriminability across training trajectories. We find that two of these metrics, Targeted Probe Perturbation (TPP) and Spurious Correlation Removal (SCR), fail multiple lenses at their canonical settings and should not be used to evaluate SAEs. The other metrics show higher reseed noise and lower discriminability than the field assumes. The sae-probes variant of $k$-sparse probing is the most reliable metric we tested, but even sae-probes struggles to separate variants of the same SAE architecture. Our results show the field needs better SAE benchmarks.
匹配关键词: generative model
---

[ACADEMIC - ARXIV]
标题: Context Memorization for Efficient Long Context Generation
作者: Yasuyuki Okoshi, Hao Mark Chen, Guanxi Lu, Hongxiang Fan, Masato Motomura, Daichi Fujiki
链接: https://arxiv.org/abs/2605.18226v1
完整摘要: Modern large language model (LLM) applications increasingly rely on long conditioning prefixes to control model behavior at inference time. While prefix-augmented inference is effective, it incurs two structural limitations: i) the prefix's influence fades as generation proceeds, and ii) attention computation over the prefix scales linearly with its length. Existing approaches either keep the prefix in attention while compressing it, or internalize it into model parameters through gradient-based training. The former still attends to the prefix at inference, while the latter is training-intensive and ill-suited to prefix updates. To address these issues, we propose attention-state memory, a training-free approach that externalizes the prefix into a lightweight, lookup-based memory of precomputed attention states between prefix and query tokens. On ManyICLBench with LLaMA-3.1-8B, our method improves accuracy over in-context learning at 1K-8K memory budgets while reducing attention latency by 1.36x at 8K, and surpasses full-attention RAG performance on NBA benchmark using only 20% of its memory footprint.
匹配关键词: generative model
---

[ACADEMIC - ARXIV]
标题: Contextual Biasing for Streaming ASR via CTC-based Word Spotting
作者: Kai-Chen Tsai, Tien-Hong Lo, Yun-Ting Sun, Berlin Chen
链接: https://arxiv.org/abs/2605.18222v1
完整摘要: Contextual biasing is essential to improving the recognition of rare and domain-specific words in an automatic speech recognition (ASR) system. While numerous methods have been proposed in recent years, most of them focus on offline settings and do not explicitly address the challenges of streaming ASR. For example, CTC-based word spotting (CTC-WS) have demonstrated strong performance by directly detecting keywords from CTC log-probabilities, but they are limited to offline processing and require access to the full utterance. In This work, we present a streaming extension of CTC-WS for real-time contextual biasing. Our method maintains active keyword paths across audio chunks using a stateful token passing algorithm, enabling the detection of keywords that span multiple chunks. To ensure low latency and stable output, we introduce an incremental commitment mechanism that only emits segments guaranteed not to be affected by future audio, while deferring uncertain regions. This method naturally integrates with streaming ASR pipelines and does not require modifications to the underlying acoustic model or additional training, making it practical for real-world deployment. Experimental results show that our method reduces overall WER and effectively improves keyword F-score, demonstrating its effectiveness for real-time ASR applications.
匹配关键词: generative model
---

[ACADEMIC - ARXIV]
标题: SIREM: Speech-Informed MRI Reconstruction with Learned Sampling
作者: Md Hasan, Nyvenn Castro, Daiqi Liu, Lukas Mulzer, Jana Hutter, Jonghye Woo, Moritz Zaiss, Andreas Maier, Paula A. Perez-Toro
链接: https://arxiv.org/abs/2605.18221v1
完整摘要: Real-time magnetic resonance imaging (rtMRI) of speech production enables non-invasive visualization of dynamic vocal-tract motion and is valuable for speech science and clinical assessment. However, rtMRI is fundamentally constrained by trade-offs among spatial resolution, temporal resolution, and acquisition speed, often leading to undersampled k-space measurements and degraded reconstructions. We propose SIREM, a speech-informed MRI reconstruction framework that uses synchronized speech as a cross-modal prior. The central idea is that vocal-tract configurations during speech are correlated with the produced acoustics, making part of the image content predictable from audio. SIREM models each frame as a fusion of an audio-driven component and an MRI-driven component through a spatial weighting map. The audio branch predicts articulator-related structure from speech, while the MRI branch reconstructs complementary content from measured k-space data. We further introduce a learnable soft weighting profile over spiral arms, enabling a differentiable study of how k-space arm usage interacts with speech-informed fusion. This yields a unified multimodal formulation that combines audio-driven prediction, MRI reconstruction, and sampling adaptation. We evaluate SIREM on the USC speech rtMRI benchmark against standard baselines, including gridding, wavelet-based compressed sensing, and total variation. SIREM introduces a speech-informed reconstruction paradigm that operates in a substantially higher-throughput regime than iterative methods while preserving anatomically plausible vocal-tract structure. These results establish an initial benchmark for multimodal speech-informed rtMRI reconstruction and highlight the potential of synchronized speech as an auxiliary prior for fast reconstruction. The source code is available at https://github.com/mdhasanai/SIREM
匹配关键词: generative model
---

[ACADEMIC - ARXIV]
标题: EgoInteract: Synthetic Egocentric Videos Generation for Interaction Understanding and Anticipation
作者: Rosario Leonardi, Francesco Ragusa, Daniele Materia, Alessandro Passanisi, James Fort, Jakob Engel, Giovanni Maria Farinella
链接: https://arxiv.org/abs/2605.18214v1
完整摘要: Collecting large-scale egocentric video datasets with dense spatial and temporal annotations is costly, slow, and often constrained by environmental biases, privacy constraints, and limited coverage of interaction patterns. While synthetic data has shown strong potential in several vision domains, its use for egocentric perception remains relatively underexplored, especially for tasks requiring temporally coherent human-object interactions. In this work, we introduce EgoInteract, a controllable simulator for egocentric video generation designed to model fine-grained egocentric interactions and their temporal dynamics. The simulator enables precise control over camera, human body and hand motion, object manipulation, and scene composition across diverse environments. Building on this framework, we generate a synthetic egocentric video dataset with dense spatial and temporal annotations for temporal action segmentation, next-active object detection, interaction anticipation, and hand-object interaction detection. We evaluate models trained with simulated data on multiple real-world egocentric benchmarks spanning diverse environments, object categories, and interaction patterns. Results show consistent improvements over strong baselines across tasks and datasets, demonstrating the effectiveness and transferability of our simulation-based approach.
匹配关键词: generative model
---

[ACADEMIC - ARXIV]
标题: Are Sparse Autoencoder Benchmarks Reliable?
作者: David Chanin
链接: https://arxiv.org/abs/2605.18229v1
完整摘要: Sparse autoencoders (SAEs) are a core interpretability tool for large language models, and progress on SAE architectures depends on benchmarks that reliably distinguish better SAEs from worse ones. We audit the SAE quality metrics in SAEBench, the de-facto standard SAE evaluation suite, through three complementary lenses: reseed noise on a fixed SAE, ground-truth correlation on synthetic SAEs, and discriminability across training trajectories. We find that two of these metrics, Targeted Probe Perturbation (TPP) and Spurious Correlation Removal (SCR), fail multiple lenses at their canonical settings and should not be used to evaluate SAEs. The other metrics show higher reseed noise and lower discriminability than the field assumes. The sae-probes variant of $k$-sparse probing is the most reliable metric we tested, but even sae-probes struggles to separate variants of the same SAE architecture. Our results show the field needs better SAE benchmarks.
匹配关键词: diffusion model
---

[ACADEMIC - ARXIV]
标题: Context Memorization for Efficient Long Context Generation
作者: Yasuyuki Okoshi, Hao Mark Chen, Guanxi Lu, Hongxiang Fan, Masato Motomura, Daichi Fujiki
链接: https://arxiv.org/abs/2605.18226v1
完整摘要: Modern large language model (LLM) applications increasingly rely on long conditioning prefixes to control model behavior at inference time. While prefix-augmented inference is effective, it incurs two structural limitations: i) the prefix's influence fades as generation proceeds, and ii) attention computation over the prefix scales linearly with its length. Existing approaches either keep the prefix in attention while compressing it, or internalize it into model parameters through gradient-based training. The former still attends to the prefix at inference, while the latter is training-intensive and ill-suited to prefix updates. To address these issues, we propose attention-state memory, a training-free approach that externalizes the prefix into a lightweight, lookup-based memory of precomputed attention states between prefix and query tokens. On ManyICLBench with LLaMA-3.1-8B, our method improves accuracy over in-context learning at 1K-8K memory budgets while reducing attention latency by 1.36x at 8K, and surpasses full-attention RAG performance on NBA benchmark using only 20% of its memory footprint.
匹配关键词: diffusion model
---

[ACADEMIC - ARXIV]
标题: Contextual Biasing for Streaming ASR via CTC-based Word Spotting
作者: Kai-Chen Tsai, Tien-Hong Lo, Yun-Ting Sun, Berlin Chen
链接: https://arxiv.org/abs/2605.18222v1
完整摘要: Contextual biasing is essential to improving the recognition of rare and domain-specific words in an automatic speech recognition (ASR) system. While numerous methods have been proposed in recent years, most of them focus on offline settings and do not explicitly address the challenges of streaming ASR. For example, CTC-based word spotting (CTC-WS) have demonstrated strong performance by directly detecting keywords from CTC log-probabilities, but they are limited to offline processing and require access to the full utterance. In This work, we present a streaming extension of CTC-WS for real-time contextual biasing. Our method maintains active keyword paths across audio chunks using a stateful token passing algorithm, enabling the detection of keywords that span multiple chunks. To ensure low latency and stable output, we introduce an incremental commitment mechanism that only emits segments guaranteed not to be affected by future audio, while deferring uncertain regions. This method naturally integrates with streaming ASR pipelines and does not require modifications to the underlying acoustic model or additional training, making it practical for real-world deployment. Experimental results show that our method reduces overall WER and effectively improves keyword F-score, demonstrating its effectiveness for real-time ASR applications.
匹配关键词: diffusion model
---

[ACADEMIC - ARXIV]
标题: SIREM: Speech-Informed MRI Reconstruction with Learned Sampling
作者: Md Hasan, Nyvenn Castro, Daiqi Liu, Lukas Mulzer, Jana Hutter, Jonghye Woo, Moritz Zaiss, Andreas Maier, Paula A. Perez-Toro
链接: https://arxiv.org/abs/2605.18221v1
完整摘要: Real-time magnetic resonance imaging (rtMRI) of speech production enables non-invasive visualization of dynamic vocal-tract motion and is valuable for speech science and clinical assessment. However, rtMRI is fundamentally constrained by trade-offs among spatial resolution, temporal resolution, and acquisition speed, often leading to undersampled k-space measurements and degraded reconstructions. We propose SIREM, a speech-informed MRI reconstruction framework that uses synchronized speech as a cross-modal prior. The central idea is that vocal-tract configurations during speech are correlated with the produced acoustics, making part of the image content predictable from audio. SIREM models each frame as a fusion of an audio-driven component and an MRI-driven component through a spatial weighting map. The audio branch predicts articulator-related structure from speech, while the MRI branch reconstructs complementary content from measured k-space data. We further introduce a learnable soft weighting profile over spiral arms, enabling a differentiable study of how k-space arm usage interacts with speech-informed fusion. This yields a unified multimodal formulation that combines audio-driven prediction, MRI reconstruction, and sampling adaptation. We evaluate SIREM on the USC speech rtMRI benchmark against standard baselines, including gridding, wavelet-based compressed sensing, and total variation. SIREM introduces a speech-informed reconstruction paradigm that operates in a substantially higher-throughput regime than iterative methods while preserving anatomically plausible vocal-tract structure. These results establish an initial benchmark for multimodal speech-informed rtMRI reconstruction and highlight the potential of synchronized speech as an auxiliary prior for fast reconstruction. The source code is available at https://github.com/mdhasanai/SIREM
匹配关键词: diffusion model
---

[ACADEMIC - ARXIV]
标题: EgoInteract: Synthetic Egocentric Videos Generation for Interaction Understanding and Anticipation
作者: Rosario Leonardi, Francesco Ragusa, Daniele Materia, Alessandro Passanisi, James Fort, Jakob Engel, Giovanni Maria Farinella
链接: https://arxiv.org/abs/2605.18214v1
完整摘要: Collecting large-scale egocentric video datasets with dense spatial and temporal annotations is costly, slow, and often constrained by environmental biases, privacy constraints, and limited coverage of interaction patterns. While synthetic data has shown strong potential in several vision domains, its use for egocentric perception remains relatively underexplored, especially for tasks requiring temporally coherent human-object interactions. In this work, we introduce EgoInteract, a controllable simulator for egocentric video generation designed to model fine-grained egocentric interactions and their temporal dynamics. The simulator enables precise control over camera, human body and hand motion, object manipulation, and scene composition across diverse environments. Building on this framework, we generate a synthetic egocentric video dataset with dense spatial and temporal annotations for temporal action segmentation, next-active object detection, interaction anticipation, and hand-object interaction detection. We evaluate models trained with simulated data on multiple real-world egocentric benchmarks spanning diverse environments, object categories, and interaction patterns. Results show consistent improvements over strong baselines across tasks and datasets, demonstrating the effectiveness and transferability of our simulation-based approach.
匹配关键词: diffusion model
---

[ACADEMIC - ARXIV]
标题: Bridging the Gap: Converting Read Text to Conversational Dialogue
作者: Parshav Singla, Agnik Banerjee, Aaditya Arora, Shruti Aggarwal, Anil Kumar Verma, Vikram C M, Raj Prakash Gohil, Gopal Kumar Agarwal
链接: https://arxiv.org/abs/2605.18001v1
完整摘要: In recent advancements within speech processing, converting read speech to conversational speech has gained significant attention. The primary challenge in this domain is maintaining naturalness and intelligibility while minimizing computational overhead for real-time applications. Traditional read speech often lacks the nuanced prosodic variation essential for natural conversational interactions, posing challenges for applications in virtual assistants, customer service, and language learning tools. This paper introduces a novel approach, Prosodic Adjustment with Conversational Context (PACC), aimed at converting read speech into natural conversational speech used in various modern applications. PACC utilizes advanced deep neural networks to analyze and modify prosodic features such as intonation, stress, and rhythm. Unlike conventional methods, our approach uses High-Fidelity Generative Adversarial Networks (HiFi-GAN) for speech synthesis. Our experimental results demonstrate significant improvements in speech conversion, enhancing naturalness and achieving better model accuracy with additional training on speech datasets. This research establishes new benchmarks in speech conversion tasks and Mean Opinion Score (MOS) evaluation for testing model accuracy, and we show that our approach can be successfully extended to other speech conversion applications.
匹配关键词: GAN
---

[ACADEMIC - ARXIV]
标题: DAD4TS: Data-Augmentation-Oriented Diffusion Model for Time-Series Forecasting with Small-Scale Data
作者: Masahiro Suzuki, Bohui Xia, Hiroto Yamamoto, Masanori Miyahara
链接: https://arxiv.org/abs/2605.17866v1
完整摘要: Small-scale data is a critical problem in time-series forecasting tasks. Data augmentation is an effective strategy for this task, but it has a limitation in generating meaningful data. To address this limitation, we propose DAD4TS, a diffusion-model-based data augmentation method with reinforcement learning, designed for time-series forecasting with small-scale data. In DAD4TS, a data generator is simultaneously trained with a time-series model and controlled by a reinforcement learning model to efficiently generate samples that improve the forecast accuracy of the time-series model. To support small-scale data, we use mathematical methods instead of conventional VAE methods to train the diffusion model by projecting the time-series data into the geometric space. We validated the effectiveness of DAD4TS with seven comparative methods through qualitative and quantitative experiments on six real-world datasets and eight time-series models. As a result, DAD4TS was validated on five datasets.
匹配关键词: VAE
---

[ACADEMIC - ARXIV]
标题: FrequencyBooster: Full-Frequency Modeling for High-Fidelity Pixel Diffusion
作者: Lichen Ma, Zipeng Guo, Yu He, Xiaolong Fu, Luohang Liu, Jingling Fu, Junshi Huang, Yan Li
链接: https://arxiv.org/abs/2605.17759v1
完整摘要: To circumvent the inherent fidelity bottlenecks and optimization misalignment of VAE-based latent diffusion, pixel-space diffusion models have emerged as a compelling end-to-end paradigm. However, existing pixel diffusion models often struggle to balance computational efficiency with the preservation of high-frequency details. They frequently resort to patch-based compression or restricted local decoding, leading to a "spectral compromise" where high-frequency and fine-grained pixel information are suppressed. To address these challenges, we propose \textbf{FrequencyBooster}, a novel framework designed to empower pixel diffusion with full-frequency modeling capabilities without prohibitive overhead. The core of our method is a high-capacity decoder that specializes in extracting exhaustive high-frequency details and low-frequency semantics, the latter of which is derived from a Diffusion Transformer (DiT) backbone. Unlike prior works that sacrifice global context for local refinement, FrequencyBooster leverages high-dimensional feature representations to maintain global structural integrity while achieving superior pixel-level precision. Extensive experiments on ImageNet demonstrate the effectiveness of our approach: our model achieves a state-of-the-art FID of \textbf{1.60} at $256 \times 256$ resolution within only 320 epochs. Furthermore, at $512 \times 512$ resolution, FrequencyBooster attains an FID of \textbf{1.69}, significantly outperforming existing pixel-space and latent-space generative models.
匹配关键词: VAE
---

[ACADEMIC - ARXIV]
标题: Elastic-dLLM: Position Preserving Context Compression and Augmentation of Diffusion LLMs
作者: Junyi Wu, Tianchen Zhao, Shaoqiu Zhang, Linfeng Zhang, Guohao Dai, Yu Wang
链接: https://arxiv.org/abs/2605.18165v1
完整摘要: Unlike autoregressive models, which generate one token at a time, dLLMs denoise a chunk of [MASK] tokens jointly and sample one or more tokens per step; despite enabling parallel decoding, this process incurs substantial computational cost due to the large chunk size of masked tokens. We observe that much of this cost is spent on repeatedly processing the preceding context and many [MASK] tokens with the same feature representations, indicating considerable computational redundancy. In this work, we revisit dLLM's redundancy from the perspective of [MASK] tokens. Through systematic analysis, we verify the redundancy of [MASK] tokens while revealing their critical role in providing structural information. Guided by these findings, we propose position-preserving [MASK] token compression and terminal-aware augmentation. By compressing redundant [MASK] computation, this approach accelerates decoding and further provides a natural extension toward context-folding-like long-context scaling under limited input-length constraints for full-sequence dLLMs such as LLaDA-8B-Instruct and LLaDA-1.5. Moreover, for block dLLMs such as LLaDA2.0-mini, it augments the context with a protected terminal [MASK] token to enhance generation quality with negligible overhead.
匹配关键词: autoregressive
---

[ACADEMIC - ARXIV]
标题: Improving Spatio-Temporal Residual Error Propagation by Mitigating Over-Squashing
作者: Seyed Mohamad Moghadas, Esther Rodrigo Bonet, Bruno Cornelis, Adrian Munteanu
链接: https://arxiv.org/abs/2605.18068v1
完整摘要: Residual error propagation remains a fundamental problem in recurrent models, where small prediction inaccuracies compound over time and degrade long-horizon performance. Accurately modeling the correlation structure of such residuals is critical for reliable uncertainty quantification in probabilistic multivariate timeseries forecasting. While recent time-series deep models efficiently parametrize time-varying contemporaneous correlations, they often assume temporal independence of errors and neglect spatial correlation across the observed network. In this paper, we introduce Teger, a structured uncertainty module that overcomes the spa- tial and temporal limitations of error-correlated autoregressive forecasting. Teger proposes a spatial curvature-aware graph rewiring mechanism explicitly strengthening information-bottleneck edges identified by discrete Forman curvature. The component is integrated into a low-rank-plus-diagonal covariance head, preserving tractable inference via the Woodbury identity. Teger is backbone-agnostic, requiring only the latent state produced by any autoregressive encoder. We provide theoretical evidence of Teger, and experimentally evaluate it on LSTM, Transformer, and xLSTM backbones across four real-world spatio-temporal datasets, showing consistent improvement in Continuous Ranked Probability Score (CRPS). We further provide a formal theoretical analysis connecting curvature-aware rewiring to (i) oversquashing alleviation, (ii) improved spectral connectivity, (iii) reduced effective resistance, and (iv) improved covariance calibration bounds
匹配关键词: autoregressive
---

[ACADEMIC - ARXIV]
标题: SkyNative: A Native Multimodal Framework for Remote Sensing Visual Evidence Reasoning
作者: Xiao Yang, Ronghao Fu, Zhiwen Lin, Zhuoran Duan, Jiashun Zhu, Jiasen Hu, Lang Sun, Weipeng Zhang, Jiaqi Liu, Xu Na, Haoran Liu, Weijie Zhang, Bo Yang
链接: https://arxiv.org/abs/2605.17949v1
完整摘要: Remote sensing vision-language models commonly rely on pretrained visual encoders to convert images into semantic features before language-model reasoning. While effective for scene-level understanding, this pipeline may prematurely compress local visual evidence, making fine-grained spatial reasoning vulnerable to language priors, especially in ultra-high-resolution remote sensing imagery. We present SkyNative, a native multimodal framework for remote sensing that adopts an encoder-free architecture, removing the pretrained visual backbone to directly represent images as raw patch tokens in the language-model token space. To reconcile low-level visual patches with textual tokens, SkyNative introduces a modality-aware decoupling mechanism that uses modality-specific parameters within a unified autoregressive backbone. We further introduce a visual reliance benchmark that diagnoses whether models ground their answers in image evidence through progressive visual degradation and misleading textual prompts. Across standard remote sensing understanding tasks and large-format spatial reasoning evaluations, SkyNative shows stronger image-grounded perception and improved robustness against prompt-induced language priors. These results suggest that native patch-level multimodal modeling is a promising direction for reliable remote sensing vision-language reasoning.
匹配关键词: autoregressive
---

[ACADEMIC - ARXIV]
标题: Prompt Compression in Diffusion Large Language Models: Evaluating LLMLingua-2 on LLaDA
作者: Sterling Huang, Abigayle Brown, Jiyoo Noh, Jiakang Xu, Wantong Huo, Kaung Myat Kyaw, Jonathan Chan
链接: https://arxiv.org/abs/2605.17932v1
完整摘要: Prompt compression reduces inference cost and context length in large language models, but prior evaluations focus primarily on autoregressive architectures. This study investigates whether prompt compression transfers effectively to diffusion large language models (DLLMs) using LLMLingua-2, specifically the 8B-parameter DLLM LLaDA. We evaluate compression performance on GSM8K, DUC2004, and ShareGPT using 250 prompts per dataset at an approximate 2$\times$ compression ratio, across mathematical reasoning, prompt reconstruction, and summarization tasks. Outputs generated from original prompts, compressed prompts, reconstructed prompts, and reconstructed-prompt reasoning were compared using exact-match accuracy, BLEU, ROUGE, and BERTScore. Results show that semantic preservation does not necessarily imply stable downstream behavior in diffusion models. Summarization tasks remained comparatively robust under compression, while mathematical reasoning degraded substantially despite high semantic similarity scores. Reconstruction experiments further showed that semantically similar prompts may still omit reasoning-critical information required for stable denoising. Across tasks, BERTScore recall was consistently lower than precision, suggesting that compression failures are primarily driven by information omission rather than semantic drift. These findings indicate that prompt compression methods designed for autoregressive models do not transfer uniformly to diffusion large language models and motivate the development of diffusion-aware compression strategies.
匹配关键词: autoregressive
---

[ACADEMIC - ARXIV]
标题: PanoWorld: A Generative Spatial World Model for Consistent Whole-House Panorama Synthesis
作者: Jinrang Jia, Zhenjia Li, Yijiang Hu, Yifeng Shi
链接: https://arxiv.org/abs/2605.17916v1
完整摘要: Generating a consistent whole-house VR tour from a floorplan and style reference requires both photorealistic panoramas and cross-view spatial coherence. Pure 2D generators produce appealing single panoramas but re-imagine geometry and materials when the viewpoint changes, whereas monolithic 3D generation becomes expensive and loses fine texture at multi-room scale. We introduce PanoWorld, a generative spatial world model that treats whole-house synthesis as autoregressive generation of node-based 360-degree panoramas, matching the discrete navigation used by real VR tour products. PanoWorld uses a floorplan-derived 3D shell as a global geometric proxy and a dynamic 3D Gaussian Splatting cache as renderable spatial memory. A feed-forward panoramic LRM designed for metric-scale multi-room 360-degree inputs lifts generated panoramas into local 3DGS updates, while Room-aware Group Attention suppresses cross-room feature interference. A topology-aware progressive caching strategy fuses these local updates without repeatedly reconstructing the full history. By decoupling shell-based geometry guidance from cache-rendered visual memory, PanoWorld preserves high-frequency 2D synthesis quality while improving cross-node layout and material consistency. The project link is https://jjrcn.github.io/PanoWorld-project-home/
匹配关键词: autoregressive
---

[ACADEMIC - ARXIV]
标题: A Simplex Witness Certificate for Constant Collapse in Variational Autoencoders
作者: Zegu Zhang, Jianhua Peng, Jian Zhang
链接: https://arxiv.org/abs/2605.18224v1
完整摘要: This note studies exact constant collapse in variational autoencoders, where the encoder mean becomes independent of the input. The goal is to make this specific failure mode pre-designable, monitorable during training, and certifiable after training. The prior is kept as the standard Gaussian. Given a fixed teacher posterior, we attach to the latent mean a fixed simplex witness head. The resulting teacher-student alignment loss has an exact constant-predictor baseline equal to the teacher information. If the alignment loss is below this baseline, the latent mean cannot be input-independent constant collapsed. The simplex witness also has a closed-form inverse. Any full-support teacher posterior can be represented by embedding its centered log-odds into the latent space. This gives an explicit latent energy cost and explains when the alignment loss can be made small. A computable view gap handles the case where teacher targets are computed from a different view. Thus exact constant collapse is converted from an after-the-fact training pathology into a design-and-certificate problem.
匹配关键词: latent diffusion
---

[ACADEMIC - ARXIV]
标题: Forward-Learned Discrete Diffusion: Learning how to noise to denoise faster
作者: Grigory Bartosh, Teodora Pandeva, Sushrut Karmalkar, Javier Zazo
链接: https://arxiv.org/abs/2605.18204v1
完整摘要: Discrete diffusion models are a powerful class of generative models with strong performance across many domains. For efficiency, however, discrete diffusion typically parameterizes the generative (reverse) process with factorized distributions, which makes it difficult for the model to learn the target process in a small number of steps and necessitates a long, computationally expensive sampling procedure. To reduce the gap between the target and model distributions and enable few-step generation, we propose Forward-Learned Discrete Diffusion (FLDD), which introduces discrete diffusion with a learnable forward (noising) process. Rather than fixing a Markovian forward chain, we adopt a non-Markovian formulation with learnable marginal and posterior distributions. This allows the generative process to remain factorized while matching the target defined by the noising process. We train all parameters end-to-end under the standard variational objective. Experiments on various benchmarks show that, for a given number of sampling steps, our approach produces a higher quality samples than conventional discrete diffusion models using the same reverse parameterization.
匹配关键词: latent diffusion
---

[ACADEMIC - ARXIV]
标题: Dual-Rate Diffusion: Accelerating diffusion models with an interleaved heavy-light network
作者: Grigory Bartosh, David Ruhe, Emiel Hoogeboom, Jonathan Heek, Thomas Mensink, Tim Salimans
链接: https://arxiv.org/abs/2605.18190v1
完整摘要: Diffusion models achieve state-of-the-art generative performance but suffer from high computational costs during inference due to the repeated evaluation of a heavy neural network. In this work, we propose Dual-Rate Diffusion, a method to accelerate sampling by interleaving the execution of a heavy high-capacity context encoder and a light efficient denoising model. The context encoder is evaluated sparsely to extract high-dimensional features, which are effectively reused by the light denoising model at every step to refine the sample efficiently. This approach significantly accelerates inference without compromising sample quality. On ImageNet benchmarks, Dual-Rate Diffusion matches the performance of standard baselines while reducing computational cost by a factor of $2$-$4$. Furthermore, we demonstrate that our method is compatible with distillation techniques, such as Moment Matching Distillation, enabling further efficiency gains in few-step generation.
匹配关键词: latent diffusion
---

[ACADEMIC - ARXIV]
标题: Elastic-dLLM: Position Preserving Context Compression and Augmentation of Diffusion LLMs
作者: Junyi Wu, Tianchen Zhao, Shaoqiu Zhang, Linfeng Zhang, Guohao Dai, Yu Wang
链接: https://arxiv.org/abs/2605.18165v1
完整摘要: Unlike autoregressive models, which generate one token at a time, dLLMs denoise a chunk of [MASK] tokens jointly and sample one or more tokens per step; despite enabling parallel decoding, this process incurs substantial computational cost due to the large chunk size of masked tokens. We observe that much of this cost is spent on repeatedly processing the preceding context and many [MASK] tokens with the same feature representations, indicating considerable computational redundancy. In this work, we revisit dLLM's redundancy from the perspective of [MASK] tokens. Through systematic analysis, we verify the redundancy of [MASK] tokens while revealing their critical role in providing structural information. Guided by these findings, we propose position-preserving [MASK] token compression and terminal-aware augmentation. By compressing redundant [MASK] computation, this approach accelerates decoding and further provides a natural extension toward context-folding-like long-context scaling under limited input-length constraints for full-sequence dLLMs such as LLaDA-8B-Instruct and LLaDA-1.5. Moreover, for block dLLMs such as LLaDA2.0-mini, it augments the context with a protected terminal [MASK] token to enhance generation quality with negligible overhead.
匹配关键词: latent diffusion
---

[ACADEMIC - ARXIV]
标题: Whispers in the Noise: Surrogate-Guided Concept Awakening via a Multi-Agent Framework
作者: Mengyu Sun, Ziyuan Yang, Zunlong Zhou, Junxu Liu, Haibo Hu, Yi Zhang
链接: https://arxiv.org/abs/2605.18150v1
完整摘要: Diffusion models (DMs) are widely used for text-to-image generation, but their strong generative capabilities also raise concerns about unsafe or undesirable content. Concept erasure aims to mitigate these risks by removing specific concepts from pretrained models. However, recent studies show that such methods often suppress rather than fully eliminate target concepts, leaving models vulnerable to awakening attacks. Existing approaches primarily rely on white-box access through optimization or inversion, while concept awakening under black-box constraints remains underexplored. In this work, we revisit the denoising process from a trajectory perspective and show that concept erasure mainly disrupts early-stage text-semantic alignment but does not fully prevent semantic information from propagating along the denoising dynamics. As generation proceeds, the model increasingly depends on the evolving noisy state rather than textual conditions, which creates an opportunity to bypass erased mappings. Motivated by this observation, we propose ConceptAgent, a training-free, black-box, multi-agent framework that awakens erased concepts by initializing the denoising trajectory from surrogate-guided noisy states. Extensive experiments demonstrate that ConceptAgent enables accurate and controllable awakening of erased concepts under black-box settings without access to model parameters, gradients, or internal representations. These results highlight fundamental limitations of current concept erasure methods and provide new insights into the dynamic nature of semantic control in DMs.
匹配关键词: latent diffusion
---

[ACADEMIC - ARXIV]
标题: SIREM: Speech-Informed MRI Reconstruction with Learned Sampling
作者: Md Hasan, Nyvenn Castro, Daiqi Liu, Lukas Mulzer, Jana Hutter, Jonghye Woo, Moritz Zaiss, Andreas Maier, Paula A. Perez-Toro
链接: https://arxiv.org/abs/2605.18221v1
完整摘要: Real-time magnetic resonance imaging (rtMRI) of speech production enables non-invasive visualization of dynamic vocal-tract motion and is valuable for speech science and clinical assessment. However, rtMRI is fundamentally constrained by trade-offs among spatial resolution, temporal resolution, and acquisition speed, often leading to undersampled k-space measurements and degraded reconstructions. We propose SIREM, a speech-informed MRI reconstruction framework that uses synchronized speech as a cross-modal prior. The central idea is that vocal-tract configurations during speech are correlated with the produced acoustics, making part of the image content predictable from audio. SIREM models each frame as a fusion of an audio-driven component and an MRI-driven component through a spatial weighting map. The audio branch predicts articulator-related structure from speech, while the MRI branch reconstructs complementary content from measured k-space data. We further introduce a learnable soft weighting profile over spiral arms, enabling a differentiable study of how k-space arm usage interacts with speech-informed fusion. This yields a unified multimodal formulation that combines audio-driven prediction, MRI reconstruction, and sampling adaptation. We evaluate SIREM on the USC speech rtMRI benchmark against standard baselines, including gridding, wavelet-based compressed sensing, and total variation. SIREM introduces a speech-informed reconstruction paradigm that operates in a substantially higher-throughput regime than iterative methods while preserving anatomically plausible vocal-tract structure. These results establish an initial benchmark for multimodal speech-informed rtMRI reconstruction and highlight the potential of synchronized speech as an auxiliary prior for fast reconstruction. The source code is available at https://github.com/mdhasanai/SIREM
匹配关键词: multimodal
---

[ACADEMIC - ARXIV]
标题: UTOPYA: A Multimodal Deep Learning Framework for Physics-Informed Anomaly Detection and Time-Series Prediction
作者: Robson W. S. Pessoa, Julien Amblard, Alessandra Russo, Idelfonso B. R. Nogueira
链接: https://arxiv.org/abs/2605.18188v1
完整摘要: Anomaly detection in batch processes is hindered by transient dynamics, scarce fault labels, and reliance on single-modality sensor data. This work introduces UTOPYA (Unified Temporal Observation for Physics-Informed Anomaly Detection and Time-Series Prediction), a 15.2M-parameter multimodal framework that jointly addresses anomaly detection, time-series prediction, and phase classification in batch distillation by fusing eight data modalities through Feature-wise Linear Modulation (FiLM) conditioned cross-modal attention and gated fusion. A physics-informed regularisation scheme introduced in this work enforces temporal smoothness and thermodynamic monotonicity, while curriculum learning introduces training samples in order of physical difficulty. On the 119-experiment multimodal batch distillation dataset of Arweiler et al. (2026), UTOPYA achieves a window-level test AUROC of 0.832 and 0.874 under multi-signal experiment-level scoring, substantially outperforming four external baselines (PCA, autoencoder, Isolation Forest, and LSTM autoencoder) evaluated under identical conditions (+0.147 window-level AUROC over the best baseline). A multimodal ablation over 15~architectural configurations shows that static context via FiLM conditioning is the key enabler, lifting experiment-level multi-signal AUROC by +0.145 over the unimodal baseline (0.729 to 0.874). Separately, a training ablation across 14 design choices reveals that several widely-adopted techniques, including instance normalisation, Mixup, ensembling, test-time augmentation, and stochastic weight averaging, fail to improve or actively degrade generalisation in this data-scarce setting. These negative results expose a fundamental tension between smoothing-based regularisation and anomaly detection, providing practical guidance for multimodal process monitoring deployment.
匹配关键词: multimodal
---

[ACADEMIC - ARXIV]
标题: MARS: Technical Report for the CASTLE Challenge at EgoVis 2026
作者: Haoyu Zhang, Qiaohui Chu, Yisen Feng, Meng Liu, Weili Guan, Yaowei Wang, Liqiang Nie
链接: https://arxiv.org/abs/2605.18176v1
完整摘要: This report presents MARS, short for Multimodal Agentic Reasoning with Source selection, our system for the CASTLE Challenge at EgoVis 2026. Participants must answer 185 closed-form questions over the CASTLE 2024 dataset. In contrast to prior single-video egocentric benchmarks, CASTLE requires reasoning over four days of activity, 15 synchronized perspectives, official transcripts, and multiple auxiliary modalities, including personal photos, auxiliary videos, gaze, thermal imagery, and heartrate measurements. MARS therefore treats the task as an agentic evidence-selection problem over multimodal sources rather than a purely text-only pipeline. MARS first follows the official CASTLE directory organization to build evidence memories from two primary sources, videos and transcripts, and four auxiliary sources, gaze, heartrate, photos, and thermal imagery. Long videos are converted into captions and DeepSeek-based summaries only because CASTLE videos are too long to fit directly into the model context for every question; this step compresses temporal evidence while keeping photos and other auxiliary media available as source-specific evidence. At inference time, a GPT-5.4 decision agent repeatedly chooses whether to continue reasoning, request a specific missing modality, produce an answer, or fall back to a random option when the evidence remains insufficient. The resulting system achieved second place on the final CASTLE Challenge leaderboard. Our codes are available at https://github.com/Hyu-Zhang/MARS.
匹配关键词: multimodal
---

[ACADEMIC - ARXIV]
标题: Vision Inference Former: Sustaining Visual Consistency in Multimodal Large Language Models
作者: Xinpeng Dong, Min Zhang, Kairong Han, Xu Tan, Fei Wu, Kun Kuang
链接: https://arxiv.org/abs/2605.18160v1
完整摘要: In recent years, multimodal large language models (MLLMs) have achieved remarkable progress, primarily attributed to effective paradigms for integrating visual and textual information. The dominant connector-based paradigm projects visual features into textual sequence, enabling unified multimodal alignment and reasoning within a generative architecture. However, our experiments reveal two key limitations: (1) Although visual information serves as the core evidential modality in MLLMs, it is treated on par with textual tokens, diminishing the unique contribution of the visual modality; (2) As generation length increases, particularly within a limited context window, the model's dependence on visual information progressively weakens, resulting in deteriorated vision-language alignment and reduced consistency between generated content and visual semantics. To address these challenges, we propose the Vision Inference Former (VIF), a lightweight architectural module that establishes a direct bridge between pure visual representations and the model's output space. Specifically, VIF continuously injects visual semantics throughout the decoding phase of the inference process, ensuring that the model remains firmly grounded in visual content during generation. We conduct experiments on 14 benchmark tasks covering general reasoning, OCR, table understanding, vision-centric evaluation, and hallucination. Experimental results show that VIF consistently improves model performance across diverse architectures while introducing minimal additional overhead. The code for this work is available at https://github.com/Dong-Xinpeng/VIF.
匹配关键词: multimodal
---

[ACADEMIC - ARXIV]
标题: Safety Geometry Collapse in Multimodal LLMs and Adaptive Drift Correction
作者: Jiahe Guo, Xiangran Guo, Jiaxuan Chen, Weixiang Zhao, Yanyan Zhao, Yutai Hou, Qianchao Wang, Dandan Tu, Bing Qin
链接: https://arxiv.org/abs/2605.18104v1
完整摘要: Multimodal large language models (MLLMs) often fail to transfer safety capabilities learned in the text modality to semantically equivalent non-text inputs, revealing a persistent multimodal safety gap. We study this gap from a representation-geometric perspective by analyzing a text-aligned refusal direction and a modality-induced drift direction. We show that multimodal inputs compress the usable separation along the refusal direction, making it no longer reliable for identifying and refusing harmful inputs. We refer to this failure mode as Safety Geometry Collapse. We quantify it through conditional refusal separability and show that stronger modality-induced drift is consistently associated with weaker refusal separability and higher attack success rates. We then validate the causal role of modality-induced drift through a fixed-strength activation intervention: counteracting the estimated drift restores refusal separability and improves multimodal safety. After drift correction, we further observe self-rectification, where the model recovers its ability to recognize and refuse harmful multimodal inputs during forward dynamics. This effect also provides an internal signal of the model's perceived harmfulness of each input. Motivated by this signal, we propose ReGap, a training-free inference-time method that adaptively corrects modality drift using self-rectification. Experiments across multiple multimodal safety benchmarks and utility benchmarks demonstrate the effectiveness of ReGap, which significantly improves the safety of MLLMs without compromising general capabilities. Our findings highlight representation-level modality alignment as a crucial direction for real-time safety improvement and for building safer, more reliable MLLMs.
匹配关键词: multimodal
---

[ACADEMIC - ARXIV]
标题: Are Sparse Autoencoder Benchmarks Reliable?
作者: David Chanin
链接: https://arxiv.org/abs/2605.18229v1
完整摘要: Sparse autoencoders (SAEs) are a core interpretability tool for large language models, and progress on SAE architectures depends on benchmarks that reliably distinguish better SAEs from worse ones. We audit the SAE quality metrics in SAEBench, the de-facto standard SAE evaluation suite, through three complementary lenses: reseed noise on a fixed SAE, ground-truth correlation on synthetic SAEs, and discriminability across training trajectories. We find that two of these metrics, Targeted Probe Perturbation (TPP) and Spurious Correlation Removal (SCR), fail multiple lenses at their canonical settings and should not be used to evaluate SAEs. The other metrics show higher reseed noise and lower discriminability than the field assumes. The sae-probes variant of $k$-sparse probing is the most reliable metric we tested, but even sae-probes struggles to separate variants of the same SAE architecture. Our results show the field needs better SAE benchmarks.
匹配关键词: vision language model
---

[ACADEMIC - ARXIV]
标题: Context Memorization for Efficient Long Context Generation
作者: Yasuyuki Okoshi, Hao Mark Chen, Guanxi Lu, Hongxiang Fan, Masato Motomura, Daichi Fujiki
链接: https://arxiv.org/abs/2605.18226v1
完整摘要: Modern large language model (LLM) applications increasingly rely on long conditioning prefixes to control model behavior at inference time. While prefix-augmented inference is effective, it incurs two structural limitations: i) the prefix's influence fades as generation proceeds, and ii) attention computation over the prefix scales linearly with its length. Existing approaches either keep the prefix in attention while compressing it, or internalize it into model parameters through gradient-based training. The former still attends to the prefix at inference, while the latter is training-intensive and ill-suited to prefix updates. To address these issues, we propose attention-state memory, a training-free approach that externalizes the prefix into a lightweight, lookup-based memory of precomputed attention states between prefix and query tokens. On ManyICLBench with LLaMA-3.1-8B, our method improves accuracy over in-context learning at 1K-8K memory budgets while reducing attention latency by 1.36x at 8K, and surpasses full-attention RAG performance on NBA benchmark using only 20% of its memory footprint.
匹配关键词: vision language model
---

[ACADEMIC - ARXIV]
标题: Contextual Biasing for Streaming ASR via CTC-based Word Spotting
作者: Kai-Chen Tsai, Tien-Hong Lo, Yun-Ting Sun, Berlin Chen
链接: https://arxiv.org/abs/2605.18222v1
完整摘要: Contextual biasing is essential to improving the recognition of rare and domain-specific words in an automatic speech recognition (ASR) system. While numerous methods have been proposed in recent years, most of them focus on offline settings and do not explicitly address the challenges of streaming ASR. For example, CTC-based word spotting (CTC-WS) have demonstrated strong performance by directly detecting keywords from CTC log-probabilities, but they are limited to offline processing and require access to the full utterance. In This work, we present a streaming extension of CTC-WS for real-time contextual biasing. Our method maintains active keyword paths across audio chunks using a stateful token passing algorithm, enabling the detection of keywords that span multiple chunks. To ensure low latency and stable output, we introduce an incremental commitment mechanism that only emits segments guaranteed not to be affected by future audio, while deferring uncertain regions. This method naturally integrates with streaming ASR pipelines and does not require modifications to the underlying acoustic model or additional training, making it practical for real-world deployment. Experimental results show that our method reduces overall WER and effectively improves keyword F-score, demonstrating its effectiveness for real-time ASR applications.
匹配关键词: vision language model
---

[ACADEMIC - ARXIV]
标题: SIREM: Speech-Informed MRI Reconstruction with Learned Sampling
作者: Md Hasan, Nyvenn Castro, Daiqi Liu, Lukas Mulzer, Jana Hutter, Jonghye Woo, Moritz Zaiss, Andreas Maier, Paula A. Perez-Toro
链接: https://arxiv.org/abs/2605.18221v1
完整摘要: Real-time magnetic resonance imaging (rtMRI) of speech production enables non-invasive visualization of dynamic vocal-tract motion and is valuable for speech science and clinical assessment. However, rtMRI is fundamentally constrained by trade-offs among spatial resolution, temporal resolution, and acquisition speed, often leading to undersampled k-space measurements and degraded reconstructions. We propose SIREM, a speech-informed MRI reconstruction framework that uses synchronized speech as a cross-modal prior. The central idea is that vocal-tract configurations during speech are correlated with the produced acoustics, making part of the image content predictable from audio. SIREM models each frame as a fusion of an audio-driven component and an MRI-driven component through a spatial weighting map. The audio branch predicts articulator-related structure from speech, while the MRI branch reconstructs complementary content from measured k-space data. We further introduce a learnable soft weighting profile over spiral arms, enabling a differentiable study of how k-space arm usage interacts with speech-informed fusion. This yields a unified multimodal formulation that combines audio-driven prediction, MRI reconstruction, and sampling adaptation. We evaluate SIREM on the USC speech rtMRI benchmark against standard baselines, including gridding, wavelet-based compressed sensing, and total variation. SIREM introduces a speech-informed reconstruction paradigm that operates in a substantially higher-throughput regime than iterative methods while preserving anatomically plausible vocal-tract structure. These results establish an initial benchmark for multimodal speech-informed rtMRI reconstruction and highlight the potential of synchronized speech as an auxiliary prior for fast reconstruction. The source code is available at https://github.com/mdhasanai/SIREM
匹配关键词: vision language model
---

[ACADEMIC - ARXIV]
标题: EgoInteract: Synthetic Egocentric Videos Generation for Interaction Understanding and Anticipation
作者: Rosario Leonardi, Francesco Ragusa, Daniele Materia, Alessandro Passanisi, James Fort, Jakob Engel, Giovanni Maria Farinella
链接: https://arxiv.org/abs/2605.18214v1
完整摘要: Collecting large-scale egocentric video datasets with dense spatial and temporal annotations is costly, slow, and often constrained by environmental biases, privacy constraints, and limited coverage of interaction patterns. While synthetic data has shown strong potential in several vision domains, its use for egocentric perception remains relatively underexplored, especially for tasks requiring temporally coherent human-object interactions. In this work, we introduce EgoInteract, a controllable simulator for egocentric video generation designed to model fine-grained egocentric interactions and their temporal dynamics. The simulator enables precise control over camera, human body and hand motion, object manipulation, and scene composition across diverse environments. Building on this framework, we generate a synthetic egocentric video dataset with dense spatial and temporal annotations for temporal action segmentation, next-active object detection, interaction anticipation, and hand-object interaction detection. We evaluate models trained with simulated data on multiple real-world egocentric benchmarks spanning diverse environments, object categories, and interaction patterns. Results show consistent improvements over strong baselines across tasks and datasets, demonstrating the effectiveness and transferability of our simulation-based approach.
匹配关键词: vision language model
---

[ACADEMIC - ARXIV]
标题: SPATIOROUTE: Dynamic Prompt Routing for Zero-Shot Spatial Reasoning
作者: Pawat Chunhachatrachai, Gueter Josmy Faure, Hung-Ting Su, Winston H. Hsu
链接: https://arxiv.org/abs/2605.18209v1
完整摘要: Spatial question answering over egocentric video is a challenging task that requires Vision-Language Models (VLMs) to reason about 3D object positions, scene affordances, and directional relationships, particularly in the zero-shot setting where no task-specific fine-tuning is available. We introduce SpatioRoute, a dynamic prompt generation approach that routes each incoming question to a semantically tailored prompt template -- without any additional training, fine-tuning, or 3D sensor input. SpatioRoute operates in two complementary modes: SpatioRoute-R, a rule-based router that deterministically maps question typologies (e.g., What, Is, How, Can, Which) to specialized prompt templates; and SpatioRoute-L, an LLM-driven approach that generates task-specific prompts from the question and situational context alone, with no video input at routing time. We evaluate SpatioRoute on the SQA3D benchmark across VLMs spanning model families. SpatioRoute achieves consistent overall accuracy gains up to 5% over fixed prompt baselines, establishing a new state-of-the-art for zero-shot video-only spatial VQA without requiring 3D point-cloud inputs. As an additional finding, we observe that Chain-of-Thought (CoT) prompting, implemented via the Think it Twice architecture, consistently degrades performance in this setting on Qwen series models, confirming that question-aware routing is more effective than uniform reasoning instructions for spatial video understanding.
匹配关键词: VLM
---

[ACADEMIC - ARXIV]
标题: Self-Evolving Spatial Reasoning in Vision Language Models via Geometric Logic Consistency
作者: Junming Liu, Yuqi Li, Yifei Sun, Maonan Wang, Piotr Koniusz, Yirong Chen, Ding Wang
链接: https://arxiv.org/abs/2605.18162v1
完整摘要: Vision-Language Models (VLMs) have made striking progress, yet their spatial reasoning remains fragile: models that answer an original input correctly can still fail under paired transformations with predictable answer mappings, revealing a gap between instance-level correctness and robust spatial reasoning. To address this, we propose Spatial Alignment via Geometric Evolution (SAGE), a self-evolving framework that enforces logical consistency in VLMs through geometric and linguistic duality operations. SAGE incorporates duality consistency as an auxiliary reward within GRPO training, encouraging models to produce logically coherent answers across original and transformed inputs. A dynamic operation pool continuously probes for inconsistencies, promoting challenging operations and retiring mastered ones, so that training focuses on the most informative signals. SAGE is model-agnostic, data-efficient compared to prior GRPO methods, and can be applied as a lightweight post-training stage to any existing VLM. Experiments on video and spatial reasoning benchmarks demonstrate consistent improvements over strong baselines and enhanced generalization to unseen data.
匹配关键词: VLM
---

[ACADEMIC - ARXIV]
标题: What Matters for Grocery Product Retrieval with Open Source Vision Language Models
作者: Emmanuel G. Maminta, Rowel O. Atienza
链接: https://arxiv.org/abs/2605.18029v1
完整摘要: Multimodal product retrieval (MPR) underpins checkout-free retail and automated inventory systems, yet it demands fine-grained SKU discrimination that standard vision-language benchmarks fail to capture. We present the first systematic zero-shot evaluation of 190 open-source VLMs on the MPR task of the GroceryVision Challenge, isolating pre-training data, architecture, and input resolution. Our analysis yields three actionable findings. \textbf{(1) Data quality trumps scale.} Switching from raw web-scrapes to filtered datasets delivers up to 16.6\% accuracy gains, exceeding the benefit of doubling model parameters. \textbf{(2) Efficient models can win.} MobileCLIP-B (150M parameters) outperforms 351M counterparts trained on noisy data. We introduce \textit{semantic power density} ($φ$), an efficiency metric that penalizes sub-threshold accuracy. \textbf{(3) A precision gap persists.} State-of-the-art models achieve 94.5\% Recall@5 but suffer a 17.5\% drop at Recall@1, revealing that contrastive embeddings cluster categories effectively but fail to rank visually similar SKUs. Code and evaluation scripts are available at \url{https://github.com/upeee/openmpr}.
匹配关键词: VLM
---

[ACADEMIC - ARXIV]
标题: AtlasVA: Self-Evolving Visual Skill Memory for Teacher-Free VLM Agents
作者: Pan Wang, Yihao Hu, Xiujin Liu, Jingchu Yang, Hang Wang, Zhihao Wen
链接: https://arxiv.org/abs/2605.17933v1
完整摘要: Vision-language model (VLM) agents increasingly rely on memory-augmented reinforcement learning to reuse experience across long-horizon tasks, yet most existing frameworks store memory as text and depend on proprietary teacher models to summarize or refine it. This design is poorly matched to spatial decision making: geometric priors are compressed into lossy language, and sparse interaction is often supervised through delayed textual feedback rather than dense visually grounded signals. We argue that reusable experience for VLM agents should remain visually grounded. Based on this insight, we propose \textbf{AtlasVA}, a teacher-free visual skill memory framework that organizes memory into three complementary layers: spatial heatmaps, visual exemplars, and symbolic text skills. AtlasVA further evolves danger and affinity atlases directly from trajectory statistics and lightweight grid heuristics, and reuses these self-evolving atlases as potential-based shaping rewards for reinforcement learning. This unifies perception, memory, and optimization without external LLM supervision. Experiments on \textsc{Sokoban}, \textsc{FrozenLake}, 3D embodied navigation, and 3D robotic manipulation benchmarks show that AtlasVA consistently outperforms text-centric memory baselines and competitive VLM agents, with especially strong gains on spatially intensive tasks. Homepage: https://wangpan-ustc.github.io/AtlasvaWeb
匹配关键词: VLM
---

[ACADEMIC - ARXIV]
标题: Temporal Aware Pruning for Efficient Diffusion-based Video Generation
作者: Sheng Li, Yang Sui, Junhao Ran, Bo Yuan, Yue Dai, Xulong Tang
链接: https://arxiv.org/abs/2605.17837v1
完整摘要: Video diffusion models have recently enabled high-quality video generation with ViT-based architectures, but remain computationally intensive because generation requires attention computation over long spatiotemporal sequences. Token pruning has proven effective for ViTs and VLMs. However, most prior pruning methods are attention-based and operate per frame, failing to ensure the vital temporal coherence across frames in video generation tasks. In practice, naively adopting attention-only pruning causes noticeable degradation due to worsened background consistency, flickering, and reduced image quality. To address this, we propose TAPE, a training-free Temporal Aware Pruning for Efficient diffusion-based video generation. TAPE (i) applies temporal smoothing to align token-importance across adjacent frames and suppress selection jitter; and (ii) performs token reselection in selected layers to align token pruning with layers' diverse semantic focus and avoid error accumulation in specific areas; it also (iii) adopt a timestep-level budget scheduling that prunes aggressively at early noisy steps and relaxes pruning during fidelity-critical refinement. The experimental results show that TAPE delivers significant speedups while preserving high visual fidelity, outperforming prior token reduction approaches.
匹配关键词: VLM
---

[ACADEMIC - ARXIV]
标题: Context Memorization for Efficient Long Context Generation
作者: Yasuyuki Okoshi, Hao Mark Chen, Guanxi Lu, Hongxiang Fan, Masato Motomura, Daichi Fujiki
链接: https://arxiv.org/abs/2605.18226v1
完整摘要: Modern large language model (LLM) applications increasingly rely on long conditioning prefixes to control model behavior at inference time. While prefix-augmented inference is effective, it incurs two structural limitations: i) the prefix's influence fades as generation proceeds, and ii) attention computation over the prefix scales linearly with its length. Existing approaches either keep the prefix in attention while compressing it, or internalize it into model parameters through gradient-based training. The former still attends to the prefix at inference, while the latter is training-intensive and ill-suited to prefix updates. To address these issues, we propose attention-state memory, a training-free approach that externalizes the prefix into a lightweight, lookup-based memory of precomputed attention states between prefix and query tokens. On ManyICLBench with LLaMA-3.1-8B, our method improves accuracy over in-context learning at 1K-8K memory budgets while reducing attention latency by 1.36x at 8K, and surpasses full-attention RAG performance on NBA benchmark using only 20% of its memory footprint.
匹配关键词: image generation
---

[ACADEMIC - ARXIV]
标题: SIREM: Speech-Informed MRI Reconstruction with Learned Sampling
作者: Md Hasan, Nyvenn Castro, Daiqi Liu, Lukas Mulzer, Jana Hutter, Jonghye Woo, Moritz Zaiss, Andreas Maier, Paula A. Perez-Toro
链接: https://arxiv.org/abs/2605.18221v1
完整摘要: Real-time magnetic resonance imaging (rtMRI) of speech production enables non-invasive visualization of dynamic vocal-tract motion and is valuable for speech science and clinical assessment. However, rtMRI is fundamentally constrained by trade-offs among spatial resolution, temporal resolution, and acquisition speed, often leading to undersampled k-space measurements and degraded reconstructions. We propose SIREM, a speech-informed MRI reconstruction framework that uses synchronized speech as a cross-modal prior. The central idea is that vocal-tract configurations during speech are correlated with the produced acoustics, making part of the image content predictable from audio. SIREM models each frame as a fusion of an audio-driven component and an MRI-driven component through a spatial weighting map. The audio branch predicts articulator-related structure from speech, while the MRI branch reconstructs complementary content from measured k-space data. We further introduce a learnable soft weighting profile over spiral arms, enabling a differentiable study of how k-space arm usage interacts with speech-informed fusion. This yields a unified multimodal formulation that combines audio-driven prediction, MRI reconstruction, and sampling adaptation. We evaluate SIREM on the USC speech rtMRI benchmark against standard baselines, including gridding, wavelet-based compressed sensing, and total variation. SIREM introduces a speech-informed reconstruction paradigm that operates in a substantially higher-throughput regime than iterative methods while preserving anatomically plausible vocal-tract structure. These results establish an initial benchmark for multimodal speech-informed rtMRI reconstruction and highlight the potential of synchronized speech as an auxiliary prior for fast reconstruction. The source code is available at https://github.com/mdhasanai/SIREM
匹配关键词: image generation
---

[ACADEMIC - ARXIV]
标题: EgoInteract: Synthetic Egocentric Videos Generation for Interaction Understanding and Anticipation
作者: Rosario Leonardi, Francesco Ragusa, Daniele Materia, Alessandro Passanisi, James Fort, Jakob Engel, Giovanni Maria Farinella
链接: https://arxiv.org/abs/2605.18214v1
完整摘要: Collecting large-scale egocentric video datasets with dense spatial and temporal annotations is costly, slow, and often constrained by environmental biases, privacy constraints, and limited coverage of interaction patterns. While synthetic data has shown strong potential in several vision domains, its use for egocentric perception remains relatively underexplored, especially for tasks requiring temporally coherent human-object interactions. In this work, we introduce EgoInteract, a controllable simulator for egocentric video generation designed to model fine-grained egocentric interactions and their temporal dynamics. The simulator enables precise control over camera, human body and hand motion, object manipulation, and scene composition across diverse environments. Building on this framework, we generate a synthetic egocentric video dataset with dense spatial and temporal annotations for temporal action segmentation, next-active object detection, interaction anticipation, and hand-object interaction detection. We evaluate models trained with simulated data on multiple real-world egocentric benchmarks spanning diverse environments, object categories, and interaction patterns. Results show consistent improvements over strong baselines across tasks and datasets, demonstrating the effectiveness and transferability of our simulation-based approach.
匹配关键词: image generation
---

[ACADEMIC - ARXIV]
标题: Leveraging Graph Structure in Seq2Seq Models for Knowledge Graph Link Prediction
作者: Luu Huu Phuc, Ratan Bahadur Thapa, Mojtaba Nayyeri, Jingcheng Wu, Evgeny Kharlamov, Steffen Staab
链接: https://arxiv.org/abs/2605.18211v1
完整摘要: We introduce Graph-Augmented Sequence-to-Sequence (GA-S2S), a novel framework that integrates a T5-small encoder-decoder with a Relational Graph Attention Network (RGAT) to improve link prediction in knowledge graphs. While existing Seq2Seq models rely solely on surface-level textual descriptions of entities and relations and at best, flatten the neighborhoods of a query entity into a single linear sequence, thereby discarding the inherent graph structure, GA-S2S jointly encodes both textual features and the full $k$-hop subgraph topology surrounding the query entity. By integrating raw encoder outputs with RGAT's relation-aware embeddings, our model captures and leverages richer multi-hop relational patterns and textual information. Our preliminary experiments on the CoDEx dataset demonstrate that GA-S2S outperforms competitive Seq2Seq-based baseline models, achieving up to a 19\% relative gain in link prediction accuracy.
匹配关键词: image generation
---

[ACADEMIC - ARXIV]
标题: SPATIOROUTE: Dynamic Prompt Routing for Zero-Shot Spatial Reasoning
作者: Pawat Chunhachatrachai, Gueter Josmy Faure, Hung-Ting Su, Winston H. Hsu
链接: https://arxiv.org/abs/2605.18209v1
完整摘要: Spatial question answering over egocentric video is a challenging task that requires Vision-Language Models (VLMs) to reason about 3D object positions, scene affordances, and directional relationships, particularly in the zero-shot setting where no task-specific fine-tuning is available. We introduce SpatioRoute, a dynamic prompt generation approach that routes each incoming question to a semantically tailored prompt template -- without any additional training, fine-tuning, or 3D sensor input. SpatioRoute operates in two complementary modes: SpatioRoute-R, a rule-based router that deterministically maps question typologies (e.g., What, Is, How, Can, Which) to specialized prompt templates; and SpatioRoute-L, an LLM-driven approach that generates task-specific prompts from the question and situational context alone, with no video input at routing time. We evaluate SpatioRoute on the SQA3D benchmark across VLMs spanning model families. SpatioRoute achieves consistent overall accuracy gains up to 5% over fixed prompt baselines, establishing a new state-of-the-art for zero-shot video-only spatial VQA without requiring 3D point-cloud inputs. As an additional finding, we observe that Chain-of-Thought (CoT) prompting, implemented via the Think it Twice architecture, consistently degrades performance in this setting on Qwen series models, confirming that question-aware routing is more effective than uniform reasoning instructions for spatial video understanding.
匹配关键词: image generation
---

[ACADEMIC - ARXIV]
标题: SIREM: Speech-Informed MRI Reconstruction with Learned Sampling
作者: Md Hasan, Nyvenn Castro, Daiqi Liu, Lukas Mulzer, Jana Hutter, Jonghye Woo, Moritz Zaiss, Andreas Maier, Paula A. Perez-Toro
链接: https://arxiv.org/abs/2605.18221v1
完整摘要: Real-time magnetic resonance imaging (rtMRI) of speech production enables non-invasive visualization of dynamic vocal-tract motion and is valuable for speech science and clinical assessment. However, rtMRI is fundamentally constrained by trade-offs among spatial resolution, temporal resolution, and acquisition speed, often leading to undersampled k-space measurements and degraded reconstructions. We propose SIREM, a speech-informed MRI reconstruction framework that uses synchronized speech as a cross-modal prior. The central idea is that vocal-tract configurations during speech are correlated with the produced acoustics, making part of the image content predictable from audio. SIREM models each frame as a fusion of an audio-driven component and an MRI-driven component through a spatial weighting map. The audio branch predicts articulator-related structure from speech, while the MRI branch reconstructs complementary content from measured k-space data. We further introduce a learnable soft weighting profile over spiral arms, enabling a differentiable study of how k-space arm usage interacts with speech-informed fusion. This yields a unified multimodal formulation that combines audio-driven prediction, MRI reconstruction, and sampling adaptation. We evaluate SIREM on the USC speech rtMRI benchmark against standard baselines, including gridding, wavelet-based compressed sensing, and total variation. SIREM introduces a speech-informed reconstruction paradigm that operates in a substantially higher-throughput regime than iterative methods while preserving anatomically plausible vocal-tract structure. These results establish an initial benchmark for multimodal speech-informed rtMRI reconstruction and highlight the potential of synchronized speech as an auxiliary prior for fast reconstruction. The source code is available at https://github.com/mdhasanai/SIREM
匹配关键词: visual reasoning
---

[ACADEMIC - ARXIV]
标题: SPATIOROUTE: Dynamic Prompt Routing for Zero-Shot Spatial Reasoning
作者: Pawat Chunhachatrachai, Gueter Josmy Faure, Hung-Ting Su, Winston H. Hsu
链接: https://arxiv.org/abs/2605.18209v1
完整摘要: Spatial question answering over egocentric video is a challenging task that requires Vision-Language Models (VLMs) to reason about 3D object positions, scene affordances, and directional relationships, particularly in the zero-shot setting where no task-specific fine-tuning is available. We introduce SpatioRoute, a dynamic prompt generation approach that routes each incoming question to a semantically tailored prompt template -- without any additional training, fine-tuning, or 3D sensor input. SpatioRoute operates in two complementary modes: SpatioRoute-R, a rule-based router that deterministically maps question typologies (e.g., What, Is, How, Can, Which) to specialized prompt templates; and SpatioRoute-L, an LLM-driven approach that generates task-specific prompts from the question and situational context alone, with no video input at routing time. We evaluate SpatioRoute on the SQA3D benchmark across VLMs spanning model families. SpatioRoute achieves consistent overall accuracy gains up to 5% over fixed prompt baselines, establishing a new state-of-the-art for zero-shot video-only spatial VQA without requiring 3D point-cloud inputs. As an additional finding, we observe that Chain-of-Thought (CoT) prompting, implemented via the Think it Twice architecture, consistently degrades performance in this setting on Qwen series models, confirming that question-aware routing is more effective than uniform reasoning instructions for spatial video understanding.
匹配关键词: visual reasoning
---

[ACADEMIC - ARXIV]
标题: Concise and Logically Consistent Conformal Sets for Neuro-Symbolic Concept-Based Models
作者: Samuele Bortolotti, Emanuele Marconato, Andrea Pugnana, Andrea Passerini, Stefano Teso
链接: https://arxiv.org/abs/2605.18202v1
完整摘要: Neuro-Symbolic Concept-based Models (NeSy-CBMs) are a family of architectures that integrate neural networks with symbolic reasoning for enhanced reliability in high-stakes applications. They work by first extracting high-level concepts from the input and then inferring a task label from these compatibly with given logical constraints. Yet, their label and concept predictions can be overconfident, making it difficult for stakeholders to gauge when the model's decisions can be trusted. We address this issue by integrating ideas from Conformal Prediction (CP), a framework providing rigorous, distribution-free coverage guarantees. We formalize three desiderata -- consistency, coverage, and conciseness -- that any conformal method for NeSy-CBMs should satisfy, and show that existing approaches fall short of at least one. We then introduce COCOCO, a post-hoc framework that conformalizes concepts and labels jointly and reconciles them via a single deduction-abduction revision step. COCOCO satisfies all three desiderata, retains distribution-free coverage, is robust to imperfect knowledge and supports user-specified size budgets. Our experiments on 8 data sets highlight how COCOCO compares favorably against competitors and natural baselines in terms of performance and set size.
匹配关键词: visual reasoning
---

[ACADEMIC - ARXIV]
标题: RGB-only Active 3D Scene Graph Generation for Indoor Mobile Robots
作者: Giorgia Modi, Davide Buoso, Giuseppe Averta, Daniele De Martini
链接: https://arxiv.org/abs/2605.18197v1
完整摘要: Current approaches to 3D scene graph generation rely on dedicated depth sensors, such as LiDAR or RGB-D cameras, for metric 3D reconstruction. This limits deployment to specialized robotic platforms and excludes settings where only RGB cameras are available, such as fixed external infrastructure. Existing pipelines also typically operate on passively collected observation trajectories, rather than selecting viewpoints based on the partially built scene representation, and therefore fail to effectively exploit the semantic and spatial information encoded within the graph during exploration. This paper presents a fully visual framework for the active, incremental construction of 3D scene graphs from RGB input only, addressing both limitations. The proposed approach unifies perception and planning around a shared structured representation that captures object semantics, 3D geometry, relational context, and information from multiple viewpoints. Because the framework is hardware-agnostic and relies only on RGB observations, it can incorporate inputs from both onboard robot cameras and fixed external cameras within the same representation. Experiments on the Replica dataset show that the RGB-only pipeline achieves F1-score parity with baselines using ground-truth depth. Active exploration experiments on ReplicaCAD further show that semantic-driven viewpoint selection detects more than twice as many objects as a geometric frontier-based baseline under the same exploration budget. Finally, the external-camera setting demonstrates that complementary RGB views can effectively bootstrap the scene graph and improve contextual understanding at no additional exploration cost.
匹配关键词: visual reasoning
---

[ACADEMIC - ARXIV]
标题: Beyond the Cartesian Illusion: Testing Two-Stage Multi-Modal Theory of Mind under Perceptual Bottlenecks
作者: Yajing Zhou, Xiangyu Kong
链接: https://arxiv.org/abs/2605.18194v1
完整摘要: While Multi-Modal Large Language Models (MLLMs) demonstrate impressive capabilities in general reasoning, their embodied spatial intelligence remains hampered by a "Cartesian Illusion" - a reliance on text-based probability distributions that lack grounded, 3D topological understanding. This limitation is starkly exposed in multi-agent environments, which demand more than just scene perception; they require second-order Theory of Mind (ToM). Specifically, an Agent A must be able to infer Agent B's belief about the environment, governed strictly by Agent B's physical orientation and sensory limitations. In this paper, we probe the limits of two-stage spatial inference in MLLMs through a novel audio-visual task: requiring Agent A to predict Agent B's estimation of A's relative location. To solve this, we propose an Epistemic Sensory Bottleneck module that abandons rigid, rule-based coordinate transformations. Instead, we introduce an Anchor-Based Embodied Spatial Decomposition Chain-of-Thought (CoT). This guides the MLLM through a "geometric-to-semantic" projection, forcing it to first establish B's local coordinate system and then dynamically weight visual and auditory modalities based on whether A falls within B's visual frustum. Extensive evaluations reveal that while current MLLMs fundamentally struggle with spatial symmetry and out-of-view ambiguities (establishing a rigorous zero-shot baseline of 42% accuracy), our sensory-bounded reasoning chain robustly outperforms pure egocentric and allocentric baselines. By systematically benchmarking these perceptual bottlenecks, our work exposes the current limits of MLLM spatial reasoning and establishes a foundational paradigm for epistemic, modality-aware inference in Embodied AI.
匹配关键词: visual reasoning
---

[ACADEMIC - ARXIV]
标题: Beyond the Cartesian Illusion: Testing Two-Stage Multi-Modal Theory of Mind under Perceptual Bottlenecks
作者: Yajing Zhou, Xiangyu Kong
链接: https://arxiv.org/abs/2605.18194v1
完整摘要: While Multi-Modal Large Language Models (MLLMs) demonstrate impressive capabilities in general reasoning, their embodied spatial intelligence remains hampered by a "Cartesian Illusion" - a reliance on text-based probability distributions that lack grounded, 3D topological understanding. This limitation is starkly exposed in multi-agent environments, which demand more than just scene perception; they require second-order Theory of Mind (ToM). Specifically, an Agent A must be able to infer Agent B's belief about the environment, governed strictly by Agent B's physical orientation and sensory limitations. In this paper, we probe the limits of two-stage spatial inference in MLLMs through a novel audio-visual task: requiring Agent A to predict Agent B's estimation of A's relative location. To solve this, we propose an Epistemic Sensory Bottleneck module that abandons rigid, rule-based coordinate transformations. Instead, we introduce an Anchor-Based Embodied Spatial Decomposition Chain-of-Thought (CoT). This guides the MLLM through a "geometric-to-semantic" projection, forcing it to first establish B's local coordinate system and then dynamically weight visual and auditory modalities based on whether A falls within B's visual frustum. Extensive evaluations reveal that while current MLLMs fundamentally struggle with spatial symmetry and out-of-view ambiguities (establishing a rigorous zero-shot baseline of 42% accuracy), our sensory-bounded reasoning chain robustly outperforms pure egocentric and allocentric baselines. By systematically benchmarking these perceptual bottlenecks, our work exposes the current limits of MLLM spatial reasoning and establishes a foundational paradigm for epistemic, modality-aware inference in Embodied AI.
匹配关键词: embodied AI
---

[ACADEMIC - ARXIV]
标题: Foundation Models for Credit Risk Prediction: A Game Changer?
作者: Bart Baesens, Andreas Goethals, Stefan Lessmann, Simon De Vos, Cristián Bravo, David Martens, Victor Medina-Olivares, Christophe Mues, Maria Oskarsdóttir, Seppe vanden Broucke, Tim Verdonck, Wouter Verbeke
链接: https://arxiv.org/abs/2605.18147v1
完整摘要: Predictive models play a pivotal role in credit risk management, guiding critical decisions through accurate estimation of default probabilities and losses. Extensive research has introduced new modeling techniques, complemented by large-scale benchmarking studies consolidating the state-of-the-art. Today, quasi-standards such as gradient-boosting models paired with SHAP explainers have emerged, yet continuous improvement of risk models remains a top priority. Concurrently, rapid advancements in AI, most notably large language models, have disrupted predictive modeling paradigms. Foundation models, pretrained on extensive datasets from diverse domains, have demonstrated remarkable performance by leveraging prior knowledge. While prevalent in natural language processing and computer vision, foundation models for tabular data have only recently emerged. We conjecture that pretraining on out-of-domain data is particularly beneficial in small-data settings, such as SME lending or specialized corporate portfolios, and may help address longstanding challenges including low default portfolios and class imbalance. This paper benchmarks recently proposed tabular foundation models against a broad set of competitors, including established and advanced machine learning techniques, across two core tasks: PD and LGD modeling. Our evaluation encompasses various datasets, performance indicators, and experimental conditions. We find that tabular foundation models generally perform best across datasets and tasks. Moreover, they offer significant improvement in predictive performance as dataset size shrinks. These results are remarkable given that the models are tested out-of-the-box, without hyperparameter tuning, ensuring ease of use and mitigating computational costs.
匹配关键词: embodied AI
---

[ACADEMIC - ARXIV]
标题: Generative AI and the Productivity Divide: Human-AI Complementarities in Education
作者: Lihi Idan, Bharat Anand
链接: https://arxiv.org/abs/2605.18143v1
完整摘要: Generative Artificial Intelligence (GenAI) is transforming how firms create, process, and apply knowledge, yet little is known about the heterogeneity of its productivity effects across users. We report results from a randomized controlled experiment in which participants-analogs of early-career knowledge workers-were assigned to self-study a technical domain using either traditional resources or large-language-model (LLM) assistance. On average, GenAI access significantly increased task performance, but the distribution of gains was highly uneven. Improvements were not predicted by GPA or prior knowledge, but by \textit{AI Interaction Competence (AIC)} -- the ability to elicit, filter, and verify model outputs. High-AIC participants realized outsized gains; low-AIC participants saw limited or even negative marginal returns. A scaffolding intervention (conceptual maps) reduced outcome variance, indicating that standardized workflows can mitigate inequality in AI-mediated performance. We interpret these findings through the lens of human-AI complementarities: GenAI raises mean productivity while introducing a new axis of capability inequality. Managerially, firms should pair GenAI access with short AIC micro-training and simple standard operating procedures to capture value consistently and avoid uneven adoption outcomes.
匹配关键词: embodied AI
---

[ACADEMIC - ARXIV]
标题: How Good LLMs Are at Answering Bangla Medical Visual Questions? Dataset and Benchmarking
作者: Rafid Ahmed, Intesar Tahmid, Mir Sazzat Hossain, Tasnimul Hossain Tomal, Md Fahim, Md Farhad Alam Bhuiyan
链接: https://arxiv.org/abs/2605.18111v1
完整摘要: Recent advancements in Large Language Models (LLMs) and Large Vision Language Models (LVLMs) have enabled general-purpose systems to demonstrate promising capabilities in complex reasoning tasks, including those in the medical domain. Medical Visual Question Answering (MedVQA) has particularly benefited from these developments. However, despite Bangla being one of the most widely spoken languages globally, there exists no established MedVQA benchmark for it. To address this gap, we introduce BanglaMedVQA, a dataset comprising clinically validated image-question-answer pairs, along with a comprehensive evaluation of current foundation models on this resource. Consistent with prior findings that report low performance of current models on English MedVQA benchmarks, our analysis reveals that Bangla performance is substantially lower, reflecting the challenges inherent to low-resource languages. Even top-performing models such as Gemini and GPT-4.1 mini fail to accurately answer specialized diagnostic questions, indicating severe limitations in fine-grained medical reasoning. Although certain open-source models, such as Gemma-3, occasionally outperform these models in general categories, they too struggle with clinically complex questions, underscoring the urgent need for top-notch evaluation method.
匹配关键词: embodied AI
---

[ACADEMIC - ARXIV]
标题: DanceHMR: Hand-Aware Whole-Body Human Mesh Recovery from Monocular Videos
作者: Wenhao Shen, Ming Zhou, Hengyuan Zhang, Siyuan Bian, Youjiang Xu, Xi Lin
链接: https://arxiv.org/abs/2605.18102v1
完整摘要: Monocular video human mesh recovery is essential for digital humans, avatar animation, and embodied simulation, where both temporal stability and expressive whole-body motion are required. Existing video HMR methods produce coherent body motion but often overlook detailed hand articulation, while image-based whole-body methods recover SMPL-X meshes independently per frame, often leading to jittery and inaccurate hand motion. We present a temporally coherent whole-body HMR framework for challenging in-the-wild monocular videos. Our model unifies body context and part-specific hand observations through residual body-hand fusion, enabling stable body motion and detailed hand recovery within a single temporal architecture. We further introduce close-up-aware augmentation to improve robustness under upper-body framing. Experiments on whole-body and body-only benchmarks demonstrate improved hand reconstruction and competitive body accuracy. Our method also produces temporally stable and 2D-consistent SMPL-X motion in challenging real-world videos.
匹配关键词: embodied AI
---

[ACADEMIC - ARXIV]
标题: RGB-only Active 3D Scene Graph Generation for Indoor Mobile Robots
作者: Giorgia Modi, Davide Buoso, Giuseppe Averta, Daniele De Martini
链接: https://arxiv.org/abs/2605.18197v1
完整摘要: Current approaches to 3D scene graph generation rely on dedicated depth sensors, such as LiDAR or RGB-D cameras, for metric 3D reconstruction. This limits deployment to specialized robotic platforms and excludes settings where only RGB cameras are available, such as fixed external infrastructure. Existing pipelines also typically operate on passively collected observation trajectories, rather than selecting viewpoints based on the partially built scene representation, and therefore fail to effectively exploit the semantic and spatial information encoded within the graph during exploration. This paper presents a fully visual framework for the active, incremental construction of 3D scene graphs from RGB input only, addressing both limitations. The proposed approach unifies perception and planning around a shared structured representation that captures object semantics, 3D geometry, relational context, and information from multiple viewpoints. Because the framework is hardware-agnostic and relies only on RGB observations, it can incorporate inputs from both onboard robot cameras and fixed external cameras within the same representation. Experiments on the Replica dataset show that the RGB-only pipeline achieves F1-score parity with baselines using ground-truth depth. Active exploration experiments on ReplicaCAD further show that semantic-driven viewpoint selection detects more than twice as many objects as a geometric frontier-based baseline under the same exploration budget. Finally, the external-camera setting demonstrates that complementary RGB views can effectively bootstrap the scene graph and improve contextual understanding at no additional exploration cost.
匹配关键词: robotics
---

[ACADEMIC - ARXIV]
标题: Fixed External Cameras as Common Prior Maps for Active 3D Scene Graph Generation
作者: Giorgia Modi, Davide Buoso, Giuseppe Averta, Daniele De Martini
链接: https://arxiv.org/abs/2605.18184v1
完整摘要: Commonly available prior information, such as BIM models, floor plans, and remote sensing images, can provide valuable geometric and semantic context for autonomous robotic systems. In this paper, we treat observations from fixed external RGB cameras as Common Prior Maps (CPMs): wide-field views of the environment that initialize a semantic and geometric scene prior before any robot motion begins. We present an RGB-only framework for active, incremental 3D scene graph (3DSG) generation that seamlessly fuses observations from both onboard robot cameras and fixed external cameras within a single hardware-agnostic pipeline. By relying solely on RGB observations processed by a feed-forward 3D reconstruction model, the system treats all cameras - onboard or external - identically, requiring no hardware modifications. A graph-based active semantic exploration framework then directly leverages the partial scene graph to guide the robot toward regions of high semantic uncertainty, progressively completing and refining the prior. Experiments demonstrate that bootstrapping the scene graph with even a single external camera increases initial object recall by up to +79%, and that the richer context of the prior significantly improves the efficiency of subsequent active exploration.
匹配关键词: robotics
---

[ACADEMIC - ARXIV]
标题: Who Generated This 3D Asset? Learning Source Attribution for Generative 3D Models
作者: Sihan Ma, Siyuan Liang, Dacheng Tao
链接: https://arxiv.org/abs/2605.18132v1
完整摘要: Generative 3D models are deployed in gaming, robotics, and immersive creation, making source attribution critical: given a 3D asset, can we identify whether and which generative model created it? This problem faces two core challenges: dispersed attribution signals, where 3D fingerprints are distributed across multi-view, geometric, and frequency-domain cues; and realistic deployment constraints, where scarce labels, degraded prompts, and mixed real/synthetic assets undermine attribution reliability. To systematically study this problem, we construct, to the best of our knowledge, the first passive source attribution benchmark for modern generated assets, covering 22 representative 3D generators under standard, few-shot, and realistic deployment protocols. Based on this benchmark, we find that generative 3D models leave two types of stable fingerprints: cross-view inconsistency and structural artifacts reflected in geometric statistics and frequency-domain cues. To capture these dispersed signals, we propose a hierarchical multi-view multi-modal Transformer that fuses appearance, geometric, and frequency-domain features within each view and models global relationships across views. Extensive experiments demonstrate strong performance, achieving 97.22% accuracy under full supervision and 77.17% accuracy with only 1% training data, corresponding to fewer than five samples per generator. These results show that modern 3D generators leave stable and attributable fingerprints, establishing a new benchmark and methodological foundation for trustworthy 3D content provenance.
匹配关键词: robotics
---

[ACADEMIC - ARXIV]
标题: TaskGround: Structured Executable Task Inference for Full-Scene Household Reasoning
作者: ZhiYuan Feng, Yu Deng, Ruichuan An, Zhenhua Liu, Qixiu Li, Keming Wu, Zhiying Du, Weijie Wang, Haoxiao Wang, Shuang Chen, Sicheng Xu, Yaobo Liang, Jiaolong Yang, Baining Guo
链接: https://arxiv.org/abs/2605.18109v1
完整摘要: In real home deployments, household agents must often operate from a complete household scene and a situated household request, rather than from a clean task specification. Such requests require agents to identify task-relevant entities, recover intended task conditions, and resolve ordering constraints from the surrounding scene context. We formalize this capability as full-scene household reasoning: given a complete household scene and a situated household request, an agent must infer executable task structure before producing a grounded skill-level action sequence. This setting is challenging because complete household scenes contain substantial task-irrelevant information, making direct complete-scene prompting inefficient and error-prone. In practical deployment, this challenge is further amplified by privacy and local compute constraints, which favor compact open-weight models with limited long-context reasoning ability. We propose TaskGround, a training-free and model-agnostic Ground-Infer-Execute framework that grounds complete scenes into compact task-relevant scene slices, infers executable task structure, and compiles it into grounded skill-level action sequences. To evaluate this setting, we introduce FullHome, a human-validated evaluation suite of 400 household tasks spanning diverse home-scale environments and both goal-oriented and process-constrained requirements. On FullHome, TaskGround improves task success rates by large margins across both proprietary and open-weight models. Notably, it makes Qwen3.5-9B competitive with GPT-5 under direct complete-scene prompting while reducing total input-token cost by up to 18x. Our results identify executable task-structure inference as a central bottleneck in full-scene household reasoning and show that structured grounding can make compact local models substantially more effective for practical household deployment.
匹配关键词: robotics
---

[ACADEMIC - ARXIV]
标题: 4DLidarOpen: An Open 4D FMCW Lidar Dataset for Motion-Aware Autonomous Driving
作者: Kane Qian, Xin Zhao, Yining Shi, Rujun Yan, Zhengqing Pan, Kaojin Zhu, Mengmeng Yang, Kai Sun, Diange Yang, Kun Jiang
链接: https://arxiv.org/abs/2605.18074v1
完整摘要: We present 4DLidarOpen, a large-scale open multi-modal dataset for autonomous driving, centered on 4D frequency-modulated continuous-wave (FMCW) Lidar sensing. Unlike conventional time-of-flight Lidar datasets that mainly provide geometric measurements, 4DLidarOpen includes point-wise radial velocity measurements from a forward-facing 4D FMCW Lidar, together with multiple Lidars of different types, including rotating, solid-state, and blind-spot variants, surround-view cameras, and 6-DOF ego-vehicle poses. The dataset was collected in complex urban environments in Beijing and covers dense pedestrian interactions, congested traffic, high-speed driving, and unprotected maneuvers. 4DLidarOpen provides synchronized multi-sensor data and 3D bounding-box annotations with persistent track IDs across five object categories. A hybrid annotation strategy is adopted, where large-scale auto-labeled data support scalable training and human experts refine annotations for the human-annotated training and validation sets. Based on this dataset, we establish benchmarks for 3D object detection, birds-eye view (BEV) segmentation and flow prediction, and motion forecasting with planning. Extensive experiments show that direct velocity measurements from 4D FMCW Lidar provide complementary motion cues for dynamic-scene understanding. Compared with geometric-only sensing, the velocity-aware representation improves motion-related perception and downstream forecasting and planning, especially in scenarios involving vulnerable road users and fast-moving objects. These results indicate that 4D FMCW Lidar is a promising sensing modality for motion-aware autonomous driving. The dataset and evaluation toolkit are publicly released to support research on 4D scene understanding, multi-Lidar fusion, and velocity-aware perception and planning.
匹配关键词: robotics
---

[ACADEMIC - ARXIV]
标题: RGB-only Active 3D Scene Graph Generation for Indoor Mobile Robots
作者: Giorgia Modi, Davide Buoso, Giuseppe Averta, Daniele De Martini
链接: https://arxiv.org/abs/2605.18197v1
完整摘要: Current approaches to 3D scene graph generation rely on dedicated depth sensors, such as LiDAR or RGB-D cameras, for metric 3D reconstruction. This limits deployment to specialized robotic platforms and excludes settings where only RGB cameras are available, such as fixed external infrastructure. Existing pipelines also typically operate on passively collected observation trajectories, rather than selecting viewpoints based on the partially built scene representation, and therefore fail to effectively exploit the semantic and spatial information encoded within the graph during exploration. This paper presents a fully visual framework for the active, incremental construction of 3D scene graphs from RGB input only, addressing both limitations. The proposed approach unifies perception and planning around a shared structured representation that captures object semantics, 3D geometry, relational context, and information from multiple viewpoints. Because the framework is hardware-agnostic and relies only on RGB observations, it can incorporate inputs from both onboard robot cameras and fixed external cameras within the same representation. Experiments on the Replica dataset show that the RGB-only pipeline achieves F1-score parity with baselines using ground-truth depth. Active exploration experiments on ReplicaCAD further show that semantic-driven viewpoint selection detects more than twice as many objects as a geometric frontier-based baseline under the same exploration budget. Finally, the external-camera setting demonstrates that complementary RGB views can effectively bootstrap the scene graph and improve contextual understanding at no additional exploration cost.
匹配关键词: humanoid robot
---

[ACADEMIC - ARXIV]
标题: Fixed External Cameras as Common Prior Maps for Active 3D Scene Graph Generation
作者: Giorgia Modi, Davide Buoso, Giuseppe Averta, Daniele De Martini
链接: https://arxiv.org/abs/2605.18184v1
完整摘要: Commonly available prior information, such as BIM models, floor plans, and remote sensing images, can provide valuable geometric and semantic context for autonomous robotic systems. In this paper, we treat observations from fixed external RGB cameras as Common Prior Maps (CPMs): wide-field views of the environment that initialize a semantic and geometric scene prior before any robot motion begins. We present an RGB-only framework for active, incremental 3D scene graph (3DSG) generation that seamlessly fuses observations from both onboard robot cameras and fixed external cameras within a single hardware-agnostic pipeline. By relying solely on RGB observations processed by a feed-forward 3D reconstruction model, the system treats all cameras - onboard or external - identically, requiring no hardware modifications. A graph-based active semantic exploration framework then directly leverages the partial scene graph to guide the robot toward regions of high semantic uncertainty, progressively completing and refining the prior. Experiments demonstrate that bootstrapping the scene graph with even a single external camera increases initial object recall by up to +79%, and that the richer context of the prior significantly improves the efficiency of subsequent active exploration.
匹配关键词: humanoid robot
---

[ACADEMIC - ARXIV]
标题: Who Generated This 3D Asset? Learning Source Attribution for Generative 3D Models
作者: Sihan Ma, Siyuan Liang, Dacheng Tao
链接: https://arxiv.org/abs/2605.18132v1
完整摘要: Generative 3D models are deployed in gaming, robotics, and immersive creation, making source attribution critical: given a 3D asset, can we identify whether and which generative model created it? This problem faces two core challenges: dispersed attribution signals, where 3D fingerprints are distributed across multi-view, geometric, and frequency-domain cues; and realistic deployment constraints, where scarce labels, degraded prompts, and mixed real/synthetic assets undermine attribution reliability. To systematically study this problem, we construct, to the best of our knowledge, the first passive source attribution benchmark for modern generated assets, covering 22 representative 3D generators under standard, few-shot, and realistic deployment protocols. Based on this benchmark, we find that generative 3D models leave two types of stable fingerprints: cross-view inconsistency and structural artifacts reflected in geometric statistics and frequency-domain cues. To capture these dispersed signals, we propose a hierarchical multi-view multi-modal Transformer that fuses appearance, geometric, and frequency-domain features within each view and models global relationships across views. Extensive experiments demonstrate strong performance, achieving 97.22% accuracy under full supervision and 77.17% accuracy with only 1% training data, corresponding to fewer than five samples per generator. These results show that modern 3D generators leave stable and attributable fingerprints, establishing a new benchmark and methodological foundation for trustworthy 3D content provenance.
匹配关键词: humanoid robot
---

[ACADEMIC - ARXIV]
标题: Efficient 3D Content Reconstruction and Generation
作者: Jiahao Li
链接: https://arxiv.org/abs/2605.18052v1
完整摘要: Automatic 3D content creation seeks to replace labor-intensive modeling and scanning pipelines with systems that can synthesize or recover 3D assets directly from text or images. Its applications span video games, virtual reality, robotics, and simulation, enabling rapid asset prototyping, diverse interactive world generation, and efficient 3D data collection for training foundation models. Contemporary solutions largely follow two complementary paradigms: (i) text- or image-to-3D generation, which learns priors over 3D geometry and appearance to create novel assets from natural language or a single view image; and (ii) 3D reconstruction, which estimates camera poses and geometry from RGB images. This thesis advances both directions. On the generation side, I introduce Instant3D, which combines multi-view diffusion with feed-forward sparse-view 3D reconstruction to produce high-quality assets in 5-20 seconds. On the reconstruction side, I develop FastMap, a structure-from-motion pipeline that achieves up to 10x speedup over prior state-of-the-art by using first-order optimization with fused GPU kernels extensively, while maintaining comparable pose accuracy and downstream novel view synthesis quality.
匹配关键词: humanoid robot
---

[ACADEMIC - ARXIV]
标题: FUSE: A Framework for Unified State Estimation in Robotic SLAM Systems
作者: Wei Wu, Honglin Chen, Wenhan Cao, Yao Lyu, Jiangtao Li, Tao Zhang, Shengbo Eben Li
链接: https://arxiv.org/abs/2605.18047v1
完整摘要: Tightly coupled SLAM formulations under mixed-rate sensing often bind temporal processing, local geometric association, estimator formulation, and map-update policy into method-specific designs. Such binding makes it difficult to vary one design choice without re-engineering the rest of the state-estimation process. This paper presents FUSE, a framework for unified state estimation in robotic SLAM systems. FUSE organizes the state-estimation interface around observation ingestion, propagation, update, and state query, and uses this interface to separate temporal processing, residual-ready local geometric association, estimator formulation, and map-update policy. A LiDAR--IMU instantiation is developed to examine the framework under mixed-rate sensing and directional degeneracy, where high-rate inertial propagation, LiDAR-triggered geometric update, residual screening, and degeneracy-aware correction operate through the same interface boundaries. On a 418 m loop-corridor sequence, the instantiation reports a 1.626~m end-to-end trajectory error, corresponding to a 7.9% relative error reduction compared with Faster-LIO, the lowest-error baseline on this sequence. The results support FUSE as a framework for organizing state-estimation design choices and show how the evaluated instantiation regularizes updates along weakly observable directions.
匹配关键词: humanoid robot
---

[ACADEMIC - ARXIV]
标题: EgoInteract: Synthetic Egocentric Videos Generation for Interaction Understanding and Anticipation
作者: Rosario Leonardi, Francesco Ragusa, Daniele Materia, Alessandro Passanisi, James Fort, Jakob Engel, Giovanni Maria Farinella
链接: https://arxiv.org/abs/2605.18214v1
完整摘要: Collecting large-scale egocentric video datasets with dense spatial and temporal annotations is costly, slow, and often constrained by environmental biases, privacy constraints, and limited coverage of interaction patterns. While synthetic data has shown strong potential in several vision domains, its use for egocentric perception remains relatively underexplored, especially for tasks requiring temporally coherent human-object interactions. In this work, we introduce EgoInteract, a controllable simulator for egocentric video generation designed to model fine-grained egocentric interactions and their temporal dynamics. The simulator enables precise control over camera, human body and hand motion, object manipulation, and scene composition across diverse environments. Building on this framework, we generate a synthetic egocentric video dataset with dense spatial and temporal annotations for temporal action segmentation, next-active object detection, interaction anticipation, and hand-object interaction detection. We evaluate models trained with simulated data on multiple real-world egocentric benchmarks spanning diverse environments, object categories, and interaction patterns. Results show consistent improvements over strong baselines across tasks and datasets, demonstrating the effectiveness and transferability of our simulation-based approach.
匹配关键词: manipulation
---

[ACADEMIC - ARXIV]
标题: Threats to Arabic Handwriting Recognition: Investigating Black-Box Adversarial Attacks on embedded ConvNet models
作者: Mohsine EL Khayati, Abdelillah Semma, Abdelaziz Courr, Rachid Elouahbi
链接: https://arxiv.org/abs/2605.18058v1
完整摘要: Arabic handwriting recognition (AHR) has made significant progress with deep learning models. AHR research has largely focused on performance, with security receiving little attention. This study provides what appears to be a new line of inquiry by demonstrating the vulnerability of high-performing models to adversarial black-box attacks. The focus on black-box attacks reflects real-world scenarios where the attacker has no prior knowledge of the model architecture. Extensive experiments were conducted on two benchmark AHR datasets containing Arabic handwritten Characters. Results demonstrated the effectiveness of the attacks, with the Pixle attack achieving an attack success rate of 99-100\% on most models. Other, less aggressive attacks achieved success rates of 50-96\% across most experiments. Despite the higher attack success rate, the attacks maintain the structural integrity of the characters, rendering them almost imperceptible to the human eye. The findings indicate the higher vulnerability of the studied models to adversarial manipulation. This underscores the need to strengthen efforts to secure these models and ensure their reliability in AHR real-world applications.
匹配关键词: manipulation
---

[ACADEMIC - ARXIV]
标题: Exploring Trust Calibration in XAI - The Impact of Exposing Model Limitations to Lay Users
作者: Alfio Ventura, Tim Katzke, Jan Corazza, Mustafa Yalçıner
链接: https://arxiv.org/abs/2605.18036v1
完整摘要: Trust calibration -- aligning user trust judgment with model capability -- is crucial for safe deployment of explainable AI (XAI), yet is often evaluated via global trust ratings detached from objective performance evidence. We present a preregistered, incentivized between-subject online study (N=418 representative UK sample) on explainable skin-lesion classification that disentangles expectation-setting from experienced performance. Participants completed 15 case evaluations using a fixed XAI panel (malignancy score, reliability score, and saliency map). We systematically manipulated five experimental onboarding conditions varying example-based information and limitation disclosures with five stimulus packages naturally varying observed prediction quality. Calibration was operationalized as the deviation between trust-related judgments (TAIS and case-wise ratings) and objective performance benchmarks for the encountered cases, analysed with hierarchical mixed-effects models. Only limitation disclosure for case-wise measures reliably impacts trust calibration, and short-term experience did not yield progressive calibration. Further, the experienced package of stimuli explained substantially more variance than the experimental manipulation. However, participants were hard-pressed to differentiate between case-wise perceived trust, trustworthiness, and accuracy estimation. We discuss implications for designing limitation communication and for measuring and analysing calibration metrics in XAI evaluations. All study materials and data of this study are publicly available for replication and further academic use.
匹配关键词: manipulation
---

[ACADEMIC - ARXIV]
标题: Active Defense Against False Data Injection Attacks in Robotic Manipulators
作者: Gabriele Gualandi, Carl Mikael Larsson, Alessandro V. Papadopoulos
链接: https://arxiv.org/abs/2605.17950v1
完整摘要: Robotic systems are vulnerable to False Data Injection Attacks (FDIAs), where adversaries corrupt sensor signals to gain malicious control. Feedback linearization exposes robotic systems to integrator vulnerability, making them susceptible to stealthy attacks that can cause significant deviations in end-effector behavior without raising alarms. This paper addresses the resilience of manipulators against finite-horizon FDIAs by formalizing two defense methods, namely anomaly-aware virtual damping and manipulability reduction, with probabilistic guarantees on nominal task execution. Simulations on a 7-DOF redundant manipulator show that the proposed defenses substantially reduce the impact of FDIA compared to using solely a threshold-based ADS like the Chi-squared, while preserving nominal task performance in the absence of attack.
匹配关键词: manipulation
---

[ACADEMIC - ARXIV]
标题: AtlasVA: Self-Evolving Visual Skill Memory for Teacher-Free VLM Agents
作者: Pan Wang, Yihao Hu, Xiujin Liu, Jingchu Yang, Hang Wang, Zhihao Wen
链接: https://arxiv.org/abs/2605.17933v1
完整摘要: Vision-language model (VLM) agents increasingly rely on memory-augmented reinforcement learning to reuse experience across long-horizon tasks, yet most existing frameworks store memory as text and depend on proprietary teacher models to summarize or refine it. This design is poorly matched to spatial decision making: geometric priors are compressed into lossy language, and sparse interaction is often supervised through delayed textual feedback rather than dense visually grounded signals. We argue that reusable experience for VLM agents should remain visually grounded. Based on this insight, we propose \textbf{AtlasVA}, a teacher-free visual skill memory framework that organizes memory into three complementary layers: spatial heatmaps, visual exemplars, and symbolic text skills. AtlasVA further evolves danger and affinity atlases directly from trajectory statistics and lightweight grid heuristics, and reuses these self-evolving atlases as potential-based shaping rewards for reinforcement learning. This unifies perception, memory, and optimization without external LLM supervision. Experiments on \textsc{Sokoban}, \textsc{FrozenLake}, 3D embodied navigation, and 3D robotic manipulation benchmarks show that AtlasVA consistently outperforms text-centric memory baselines and competitive VLM agents, with especially strong gains on spatially intensive tasks. Homepage: https://wangpan-ustc.github.io/AtlasvaWeb
匹配关键词: manipulation
---

[ACADEMIC - ARXIV]
标题: Episodic-Semantic Memory Architecture for Long-Horizon Scientific Agents
作者: Nikola Milosevic
链接: https://arxiv.org/abs/2605.17625v1
完整摘要: As Large Language Models (LLMs) evolve into persistent scientific collaborators, context window saturation has emerged as a critical bottleneck. Scientific workflows involving iterative data analysis and hypothesis refinement rapidly saturate even extended contexts with dense technical content, while monolithic approaches suffer from quadratic cost scaling and cognitive degradation. We evaluate a Dual Process Memory Architecture that decouples immediate episodic needs (constant 10-message window) from long-term consolidated knowledge (growing at approximately 3 tokens/message). Unlike prior social agent memory systems, our domain-specific consolidation addresses contradictory parameter evolution, multi-hop reasoning across experimental phases, and precise technical fact retention. Through large-scale evaluation spanning 15,000 messages with cross-model validation across six LLMs from three families (OpenAI, Anthropic, Google), totaling 1,440 queries, we establish three key findings. First, while full-context models fail at 10,000 messages due to context overflow, our system maintains 70-85% accuracy with 1-2 second latency using 62% fewer tokens (45,434 vs 120,000+ limit). Second, cross-model validation reveals architecture-level trade-offs independent of specific LLMs: Dual Process excels at numeric/temporal queries (65-90% accuracy) while RAG excels at historical retrieval (60-85%), suggesting complementary deployment strategies. Third, we identify a "Sim-to-Real" gap where synthetic tests maintain constant memory but realistic workflows exhibit linear growth (about 3 tokens/message), with consolidation quality emerging as the primary scalability bottleneck. The architecture successfully manages profiles with 14,000+ scientific facts (125k tokens), demonstrating that domain-specific memory consolidation enables sustained operation beyond full-context limits.
匹配关键词: sim-to-real
---

[ACADEMIC - ARXIV]
标题: Firefly: Illuminating Large-Scale Verified Tool-Call Data Generation from Real APIs
作者: Yuxuan Lu, Ziyi Wang, Yingzhou Lu, Yisi Sang, Jiri Gesi, Xianfeng Tang, Yimeng Zhang, Zhenwei Dai, Hui Liu, Hanqing Lu, Chen Luo, Qi He, Benoit Dumoulin, Jing Huang, Dakuo Wang
链接: https://arxiv.org/abs/2605.17558v1
完整摘要: Training tool-calling agents requires large-scale trajectory data with verifiable labels, yet existing approaches either synthesize environments that diverge from real API behavior or generate tasks without ground-truth outcomes for verification. We present FireFly, a pipeline for generating verified tool-call data from real-world MCP servers. Our key insight is to invert the standard synthesis pipeline: rather than generating tasks and hoping they are solvable, we first let a strong LLM explore real APIs along graph-guided DAG structures, then synthesize tasks backward from observed outcomes, guaranteeing label correctness by construction. To handle the scale of real-world tool spaces (${\sim}$1,000 tools), we build a pairwise tool graph and sample sub-DAGs to focus exploration on semantically coherent workflows. To address environment drift in live APIs, we construct a retrieval-augmented simulator that caches all exploration results and replays them during training and evaluation, enabling fully offline and reproducible RL. Applying this pipeline yields 5,144 verified tasks spanning 240 servers and 993 tools. A 4B-parameter model trained with GRPO on FireFly matches Claude Sonnet 4.6 on our held-out test set and shows improvements on multiple tool-calling benchmarks including Tau2-Bench, MCPMark, and MCP-Atlas.
匹配关键词: sim-to-real
---

[ACADEMIC - ARXIV]
标题: SWoMo: Neuro-Symbolic World Model for Cataract Surgery Simulation
作者: Ssharvien Kumar Sivakumar, Akwele Johnson, Anirudh Dhingra, Yannik Frisch, Ghazal Ghazaei, Anirban Mukhopadhyay
链接: https://arxiv.org/abs/2605.16530v1
完整摘要: Realistic surgical simulation plays a crucial role in training novice surgeons and in the development of autonomous agents. World models can scale such simulation environments to realistic and diverse procedures by predicting future patient states conditioned on current observations and surgical actions. However, current state-of-the-art approaches often fail to satisfy key criteria required for clinical applicability, including visual realism, physically grounded interactions, and the ability to simulate scenarios beyond the training distribution. Hence, we introduce SWoMo, a neuro-symbolic world model for cataract surgery simulation that decouples motion generation from visual realism. The symbolic component, consisting of a rule-based simulator and scene graph representations, models motion dynamics and tool-tissue interactions, while a diffusion model produces realistic visual appearance, including textures and tissue deformations. We propose an inverse pairing strategy that reconstructs real surgical videos in the simulator to obtain paired simulated and real videos, which are then used to train our video diffusion model for the reverse objective of sim-to-real translation. Our experiments show both qualitative and quantitative improvements over prior work. We demonstrate that our simulator further satisfies the key criteria, including generalisation to unseen interaction geometries, improvements in downstream phase detection, and unsupervised video style transfer. The code, data, and model weights are available at: https://ssharvienkumar.github.io/SWoMo/
匹配关键词: sim-to-real
---

[ACADEMIC - ARXIV]
标题: Adaptive Outer-Loop Control of Quadrotors via Reinforcement Learning
作者: Vishnu Saj, Sushi Vemuri, Dileep Kalathil, Moble Benedict
链接: https://arxiv.org/abs/2605.16015v1
完整摘要: Deep Reinforcement Learning (DRL) for quadrotor flight control typically relies on Domain Randomization (DR) for sim-to-real transfer, resulting in overly conservative policies that struggle with dynamic disturbances. To overcome this, we propose a novel adaptive control architecture that actively perceives and reacts to instantaneous perturbations. First, we train an optimal outer-loop policy, then replace its reliance on ground-truth disturbance data with a Residual Dynamics Predictor (RDP). The RDP estimates the external forces and moments acting on the aircraft in flight online using only the history of states and control actions. For seamless hardware transfer, we introduce a data-efficient linear calibration bridge and an online thrust correction mechanism that align the simulated latent space with reality using mere seconds of flight data. Real-world validations on a Crazyflie micro-quadrotor demonstrate that our adaptive controller significantly outperforms baselines, maintaining precise trajectory tracking under severe uncertainties including mass variations, asymmetric payloads, and dynamic slung loads
匹配关键词: sim-to-real
---

[ACADEMIC - ARXIV]
标题: AGOP-IxG: A Gradient Covariance Filter for Local Feature Attribution on Tabular Data, with a Controlled Benchmark
作者: Raj Kiran Gupta Katakam
链接: https://arxiv.org/abs/2605.15700v1
完整摘要: Automated machine learning pipelines increasingly produce models whose predictions must be explained to end users, auditors, and downstream decision systems. The most widely used feature attribution methods (SHAP, Integrated Gradients, LIME) are typically chosen by convention rather than measured fidelity, because rigorous evaluation is impeded by the absence of ground-truth attribution on real data. We propose AGOP-IxG, a fast per-sample attribution method for tabular classifiers that pre-multiplies the per-sample gradient by a top-$K$ rank-truncated Average Gradient Outer Product matrix, and evaluate it against four widely-used baselines on a controlled tabular benchmark designed for AutoML practitioners. In Part 1, we construct three synthetic multi-class tabular tasks (linear, sparse nonlinear, interaction-based) where ground-truth attribution per sample is analytically or numerically derivable, and compare five methods: AGOP-IxG, SHAP (DeepExplainer), Integrated Gradients, InputXGradient, and LIME. AGOP-IxG leads on Spearman rank correlation and noise feature mass on all three synthetic datasets, and on top-$k$ precision on the interaction dataset. Across all settings, AGOP-IxG is approximately $350\times$ to $1{,}650\times$ faster than SHAP. In Part 2, we evaluate global faithfulness on Adult Income and Credit Card Default using the ROAR protocol; the methods cluster within $\sim 1.7\%$ relative AUC, consistent with AGOP-IxG being optimized for per-sample local attribution rather than global feature ranking.
匹配关键词: sim-to-real
---

[ACADEMIC - ARXIV]
标题: Are Sparse Autoencoder Benchmarks Reliable?
作者: David Chanin
链接: https://arxiv.org/abs/2605.18229v1
完整摘要: Sparse autoencoders (SAEs) are a core interpretability tool for large language models, and progress on SAE architectures depends on benchmarks that reliably distinguish better SAEs from worse ones. We audit the SAE quality metrics in SAEBench, the de-facto standard SAE evaluation suite, through three complementary lenses: reseed noise on a fixed SAE, ground-truth correlation on synthetic SAEs, and discriminability across training trajectories. We find that two of these metrics, Targeted Probe Perturbation (TPP) and Spurious Correlation Removal (SCR), fail multiple lenses at their canonical settings and should not be used to evaluate SAEs. The other metrics show higher reseed noise and lower discriminability than the field assumes. The sae-probes variant of $k$-sparse probing is the most reliable metric we tested, but even sae-probes struggles to separate variants of the same SAE architecture. Our results show the field needs better SAE benchmarks.
匹配关键词: world model
---

[ACADEMIC - ARXIV]
标题: Context Memorization for Efficient Long Context Generation
作者: Yasuyuki Okoshi, Hao Mark Chen, Guanxi Lu, Hongxiang Fan, Masato Motomura, Daichi Fujiki
链接: https://arxiv.org/abs/2605.18226v1
完整摘要: Modern large language model (LLM) applications increasingly rely on long conditioning prefixes to control model behavior at inference time. While prefix-augmented inference is effective, it incurs two structural limitations: i) the prefix's influence fades as generation proceeds, and ii) attention computation over the prefix scales linearly with its length. Existing approaches either keep the prefix in attention while compressing it, or internalize it into model parameters through gradient-based training. The former still attends to the prefix at inference, while the latter is training-intensive and ill-suited to prefix updates. To address these issues, we propose attention-state memory, a training-free approach that externalizes the prefix into a lightweight, lookup-based memory of precomputed attention states between prefix and query tokens. On ManyICLBench with LLaMA-3.1-8B, our method improves accuracy over in-context learning at 1K-8K memory budgets while reducing attention latency by 1.36x at 8K, and surpasses full-attention RAG performance on NBA benchmark using only 20% of its memory footprint.
匹配关键词: world model
---

[ACADEMIC - ARXIV]
标题: Contextual Biasing for Streaming ASR via CTC-based Word Spotting
作者: Kai-Chen Tsai, Tien-Hong Lo, Yun-Ting Sun, Berlin Chen
链接: https://arxiv.org/abs/2605.18222v1
完整摘要: Contextual biasing is essential to improving the recognition of rare and domain-specific words in an automatic speech recognition (ASR) system. While numerous methods have been proposed in recent years, most of them focus on offline settings and do not explicitly address the challenges of streaming ASR. For example, CTC-based word spotting (CTC-WS) have demonstrated strong performance by directly detecting keywords from CTC log-probabilities, but they are limited to offline processing and require access to the full utterance. In This work, we present a streaming extension of CTC-WS for real-time contextual biasing. Our method maintains active keyword paths across audio chunks using a stateful token passing algorithm, enabling the detection of keywords that span multiple chunks. To ensure low latency and stable output, we introduce an incremental commitment mechanism that only emits segments guaranteed not to be affected by future audio, while deferring uncertain regions. This method naturally integrates with streaming ASR pipelines and does not require modifications to the underlying acoustic model or additional training, making it practical for real-world deployment. Experimental results show that our method reduces overall WER and effectively improves keyword F-score, demonstrating its effectiveness for real-time ASR applications.
匹配关键词: world model
---

[ACADEMIC - ARXIV]
标题: SIREM: Speech-Informed MRI Reconstruction with Learned Sampling
作者: Md Hasan, Nyvenn Castro, Daiqi Liu, Lukas Mulzer, Jana Hutter, Jonghye Woo, Moritz Zaiss, Andreas Maier, Paula A. Perez-Toro
链接: https://arxiv.org/abs/2605.18221v1
完整摘要: Real-time magnetic resonance imaging (rtMRI) of speech production enables non-invasive visualization of dynamic vocal-tract motion and is valuable for speech science and clinical assessment. However, rtMRI is fundamentally constrained by trade-offs among spatial resolution, temporal resolution, and acquisition speed, often leading to undersampled k-space measurements and degraded reconstructions. We propose SIREM, a speech-informed MRI reconstruction framework that uses synchronized speech as a cross-modal prior. The central idea is that vocal-tract configurations during speech are correlated with the produced acoustics, making part of the image content predictable from audio. SIREM models each frame as a fusion of an audio-driven component and an MRI-driven component through a spatial weighting map. The audio branch predicts articulator-related structure from speech, while the MRI branch reconstructs complementary content from measured k-space data. We further introduce a learnable soft weighting profile over spiral arms, enabling a differentiable study of how k-space arm usage interacts with speech-informed fusion. This yields a unified multimodal formulation that combines audio-driven prediction, MRI reconstruction, and sampling adaptation. We evaluate SIREM on the USC speech rtMRI benchmark against standard baselines, including gridding, wavelet-based compressed sensing, and total variation. SIREM introduces a speech-informed reconstruction paradigm that operates in a substantially higher-throughput regime than iterative methods while preserving anatomically plausible vocal-tract structure. These results establish an initial benchmark for multimodal speech-informed rtMRI reconstruction and highlight the potential of synchronized speech as an auxiliary prior for fast reconstruction. The source code is available at https://github.com/mdhasanai/SIREM
匹配关键词: world model
---

[ACADEMIC - ARXIV]
标题: EgoInteract: Synthetic Egocentric Videos Generation for Interaction Understanding and Anticipation
作者: Rosario Leonardi, Francesco Ragusa, Daniele Materia, Alessandro Passanisi, James Fort, Jakob Engel, Giovanni Maria Farinella
链接: https://arxiv.org/abs/2605.18214v1
完整摘要: Collecting large-scale egocentric video datasets with dense spatial and temporal annotations is costly, slow, and often constrained by environmental biases, privacy constraints, and limited coverage of interaction patterns. While synthetic data has shown strong potential in several vision domains, its use for egocentric perception remains relatively underexplored, especially for tasks requiring temporally coherent human-object interactions. In this work, we introduce EgoInteract, a controllable simulator for egocentric video generation designed to model fine-grained egocentric interactions and their temporal dynamics. The simulator enables precise control over camera, human body and hand motion, object manipulation, and scene composition across diverse environments. Building on this framework, we generate a synthetic egocentric video dataset with dense spatial and temporal annotations for temporal action segmentation, next-active object detection, interaction anticipation, and hand-object interaction detection. We evaluate models trained with simulated data on multiple real-world egocentric benchmarks spanning diverse environments, object categories, and interaction patterns. Results show consistent improvements over strong baselines across tasks and datasets, demonstrating the effectiveness and transferability of our simulation-based approach.
匹配关键词: world model
---

[ACADEMIC - ARXIV]
标题: Contextual Biasing for Streaming ASR via CTC-based Word Spotting
作者: Kai-Chen Tsai, Tien-Hong Lo, Yun-Ting Sun, Berlin Chen
链接: https://arxiv.org/abs/2605.18222v1
完整摘要: Contextual biasing is essential to improving the recognition of rare and domain-specific words in an automatic speech recognition (ASR) system. While numerous methods have been proposed in recent years, most of them focus on offline settings and do not explicitly address the challenges of streaming ASR. For example, CTC-based word spotting (CTC-WS) have demonstrated strong performance by directly detecting keywords from CTC log-probabilities, but they are limited to offline processing and require access to the full utterance. In This work, we present a streaming extension of CTC-WS for real-time contextual biasing. Our method maintains active keyword paths across audio chunks using a stateful token passing algorithm, enabling the detection of keywords that span multiple chunks. To ensure low latency and stable output, we introduce an incremental commitment mechanism that only emits segments guaranteed not to be affected by future audio, while deferring uncertain regions. This method naturally integrates with streaming ASR pipelines and does not require modifications to the underlying acoustic model or additional training, making it practical for real-world deployment. Experimental results show that our method reduces overall WER and effectively improves keyword F-score, demonstrating its effectiveness for real-time ASR applications.
匹配关键词: speech synthesis
---

[ACADEMIC - ARXIV]
标题: SIREM: Speech-Informed MRI Reconstruction with Learned Sampling
作者: Md Hasan, Nyvenn Castro, Daiqi Liu, Lukas Mulzer, Jana Hutter, Jonghye Woo, Moritz Zaiss, Andreas Maier, Paula A. Perez-Toro
链接: https://arxiv.org/abs/2605.18221v1
完整摘要: Real-time magnetic resonance imaging (rtMRI) of speech production enables non-invasive visualization of dynamic vocal-tract motion and is valuable for speech science and clinical assessment. However, rtMRI is fundamentally constrained by trade-offs among spatial resolution, temporal resolution, and acquisition speed, often leading to undersampled k-space measurements and degraded reconstructions. We propose SIREM, a speech-informed MRI reconstruction framework that uses synchronized speech as a cross-modal prior. The central idea is that vocal-tract configurations during speech are correlated with the produced acoustics, making part of the image content predictable from audio. SIREM models each frame as a fusion of an audio-driven component and an MRI-driven component through a spatial weighting map. The audio branch predicts articulator-related structure from speech, while the MRI branch reconstructs complementary content from measured k-space data. We further introduce a learnable soft weighting profile over spiral arms, enabling a differentiable study of how k-space arm usage interacts with speech-informed fusion. This yields a unified multimodal formulation that combines audio-driven prediction, MRI reconstruction, and sampling adaptation. We evaluate SIREM on the USC speech rtMRI benchmark against standard baselines, including gridding, wavelet-based compressed sensing, and total variation. SIREM introduces a speech-informed reconstruction paradigm that operates in a substantially higher-throughput regime than iterative methods while preserving anatomically plausible vocal-tract structure. These results establish an initial benchmark for multimodal speech-informed rtMRI reconstruction and highlight the potential of synchronized speech as an auxiliary prior for fast reconstruction. The source code is available at https://github.com/mdhasanai/SIREM
匹配关键词: speech synthesis
---

[ACADEMIC - ARXIV]
标题: Xiaomi EV World Model: A Joint World Model Integrating Reconstruction and Generation for Autonomous Driving
作者: Lijun Zhou, Hongcheng Luo, Zhenxin Zhu, Cheng Chi, Mingfei Tu, Kaixin Xiong, Lei Gong, Zhanqian Wu, Zehan Zhang, Fangzhen Li, Hao Li, Yingying Shen, Jiale He, Haohui Zhu, Shan Zhao, Kai Wang, Zhiwei Zhan, Yuechuan Pu, Kaiyuan Tan, Ruiling Yang, Xianqi Wang, Tianyi Yan, Jiawei Zhou, Lei Zhang, Jingyang Zhao, Xi Zhou, Chitian Sun, Chenming Wu, Jiong Deng, Hongwei Xie, Ming Lu, Kun Ma, Long Chen, Guang Chen, Hangjun Ye, Bing Wang, Haiyang Sun
链接: https://arxiv.org/abs/2605.18137v1
完整摘要: This report presents a unified technical system addressing the two core capabilities of world models for autonomous driving: world representation and world generation. For world representation, we propose WorldRec, a feed-forward reconstruction architecture driven by sparse scene queries. WorldRec initializes structured queries in 3D space, leveraging them to aggregate cross-view, cross-temporal features, thereby naturally enforcing spatial consistency across frames and yielding compact yet high-fidelity 3D Gaussian scene representations. For world generation, we propose WorldGen, a two-stage training framework of bidirectional pretraining followed by causal fine-tuning through three progressive stages (Teacher Forcing, ODE distillation, and DMD), enabling high-quality online causal video generation in as few as 4 denoising steps. Building on both modules, we further introduce the JWM, which deeply integrates WorldRec and WorldGen to achieve synergistic gains in generation stability, cross-frame consistency, and visual fidelity, providing a solid foundation for closed-loop simulation, data synthesis, and end-to-end training in autonomous driving.
匹配关键词: speech synthesis
---

[ACADEMIC - ARXIV]
标题: SENSE: Satellite-based ENergy Synthesis for Sustainable Environment
作者: Kailai Sun, Mingyi He, Heye Huang, Can Rong, Alok Prakash, Baoshen Guo, Shenhao Wang, Jinhua Zhao
链接: https://arxiv.org/abs/2605.18101v1
完整摘要: Urban Building Energy Modeling plays a critical role in achieving the United Nations' Sustainable Development Goals 7 and 11. Although existing studies based on satellite imagery and deep learning have achieved remarkable progress, many challenges exist: most existing studies are inherently predictive, failing to reflect the generative nature of urban planning; although generative AI and diffusion models have seen explosive growth in satellite imagery, they lack the urban functional generation (e.g., energy layer); third, aligned high-quality high-resolution building energy data with satellite imagery is limited and scarce. Here we propose SENSE (Satellite-based ENergy Synthesis for Sustainable Environment), a unified generative UBEM framework that jointly synthesizes realistic urban satellite imagery and aligned high-quality building energy consumption and height maps. By conditioning on road networks and urban density metrics, SENSE, based on a controllable diffusion model, leverages the knowledge learned by large vision models to generate urban building energy consumption and height information (annotations) in the latent space. Experiments across four cities (New York City, Boston, Lyon, Busan) demonstrate that SENSE achieves high visual fidelity and strong physical consistency, satisfying the ASHRAE standard metric. Experiments demonstrate that SENSE can generate enough annotated synthetic data using less than 20% labeled energy data, boosting downstream prediction performance by 10% IoU. Compared to SOTA urban energy prediction methods, SENSE significantly reduced prediction error (reduced 3%-11% NMBE and 1%-9% CVRMSE). This study offers an energy-efficiency urban planning and physical generation solution for urban science, energy science and building science. The dataset and code: https://huggingface.co/datasets/skl24/MUSE and https://github.com/kailaisun/GenAI4Urban-Energy/.
匹配关键词: speech synthesis
---

[ACADEMIC - ARXIV]
标题: A-ProS: Towards Reliable Autonomous Programming Through Multi-Model Feedback
作者: Anika Tabassum, Md Sifat Hossain, Md. Fahim Arefin, Tariqul Islam, Tarannum Shaila Zaman
链接: https://arxiv.org/abs/2605.18073v1
完整摘要: Large Language Models (LLMs) demonstrate strong potential for automated code generation, yet their ability to iteratively refine solutions using execution feedback remains underexplored. Competitive programming offers an ideal testbed for this investigation, as it demands end-to-end algorithmic reasoning, precise implementation under strict computational constraints, and complete functional correctness with rigorous evaluation. In this paper, we present A-ProS, an autonomous AI agent that solves competitive programming problems through a hybrid multi-model feedback framework separating solution generation from specialized debugging. A-ProS combines ChatGPT-based generators (GPT-4 and GPT-5) with three debugging critics: Codestral-2508, Llama-3.3-70B, and DeepSeek-R1, under a 2 x 3 factorial design. We evaluate six workflows on 367 problems from ICPC World Finals (2011-2024) and Codeforces (rated 1200-1800). The results show that GPT-5 workflows improve from 39 initial accepted solutions to 85-90 after three refinement rounds, while GPT-4 improves from 15 to 31-38. A controlled ablation on 47 problems shows that stateful refinement outperforms stateless approaches by 8.5-10.6 percentage points and reduces repeated failures by up to 3.5x. Compared to baseline agent loops, A-ProS achieves over 2x greater gains, highlighting the importance of persistent context and multi-model feedback for reliable autonomous program synthesis.
匹配关键词: speech synthesis
---

[ACADEMIC - ARXIV]
标题: Omni-Customizer: End-to-End MultiModal Customization for Joint Audio-Video Generation
作者: Yuheng Chen, Qingdong He, Teng Hu, Yuji Wang, Yabiao Wang, Lizhuang Ma, Jiangning Zhang
链接: https://arxiv.org/abs/2605.17488v1
完整摘要: The landscape of joint audio and video generation has been fundamentally transformed by the advent of powerful foundation models. Despite these strides, achieving cohesive multimodal customization for the simultaneous preservation of visual identities and vocal timbres across multiple interacting subjects remains largely underexplored. To bridge this gap, we present Omni-Customizer, an end-to-end framework targeted at the precise binding and seamless fusion of multimodal identity information. Specifically, we introduce an Omni-Context Fusion (OCF) module that effectively enriches the base textual prompt with dense, multimodal identity cues, along with a Masked TTS Cross-Attention (MTP-CA) mechanism explicitly designed to prevent the severe "speech leakage" problem. Within this architecture, we propose Semantic-Anchored Multimodal RoPE (SA-MRoPE) to anchor visual and audio reference tokens, along with TTS embeddings, to their corresponding semantic descriptions, enabling structured multimodal fusion and robust identity binding. Furthermore, we devise a comprehensive training strategy that incorporates interleaved audio-video scheduling to rapidly adapt the audio branch to multilingual scenarios without degrading foundational priors, and a progressive in-pair to cross-pair curriculum to facilitate the learning of high-level and robust identity features. Extensive experiments demonstrate that Omni-Customizer achieves state-of-the-art performance in dual-modal customized generation, excelling across visual identity similarity, timbre consistency, precise audio-video synchronization, and overall video-audio fidelity.
匹配关键词: TTS
---

[ACADEMIC - ARXIV]
标题: SemaVoice: Semantic-Aware Continuous Autoregressive Speech Synthesis
作者: Huimeng Wang, Hui Lu, Jiajun Deng, Haoning Xu, Youjun Chen, Xueyuan Chen, Zhaoqing Li, Shuhai Peng, Shiyin Kang, Xunying Liu
链接: https://arxiv.org/abs/2605.16964v1
完整摘要: Continuous autoregressive speech synthesis has recently emerged as a promising direction for zero-shot text-to-speech (TTS). However, existing methods still suffer from a fundamental mismatch between semantic-prosodic modeling and reconstruction-driven continuous speech representations. This mismatch causes TTS models to focus excessively on low-level acoustic textures at the expense of high-level semantic coherence, further exacerbating error accumulation in autoregressive generation. To address this challenge, we propose SemaVoice, a semantic-aware continuous autoregressive framework for high-fidelity zero-shot TTS. SemaVoice introduces a Speech Foundation Model (SFM) guided alignment mechanism that refines continuous speech representations to better capture both local semantic consistency and global structural relationships. These representations condition a patch-wise diffusion head within the autoregressive framework for high-quality speech synthesis. Experimental results on the Seed-TTS benchmark show that SemaVoice achieves an English WER of 1.71\% and remains highly competitive with state-of-the-art open-source systems in both objective and subjective evaluations. The effectiveness of SFM guided alignment is further confirmed by significant improvements under varying representation granularities with a fixed information-rate constraint.
匹配关键词: TTS
---

[ACADEMIC - ARXIV]
标题: Improving Automatic Speech Recognition for Speakers Treated for Oral Cancer using Data Augmentation and LLM Error Correction
作者: Hidde Folkertsma, Thomas Tienkamp, Sebastiaan de Visscher, Max Witjes, Rob van Son, Jiapan Guo, Bence Mark Halpern
链接: https://arxiv.org/abs/2605.15854v1
完整摘要: In recent years, the performance of automatic speech recognition (ASR) systems has made considerable progress. Unfortunately, for people with speech impairments, such as people treated for oral cancer (OC), ASR performance is still lagging behind. The scarcity and variability of OC speech data makes development of ASR models for this type of speech difficult. In this work, we use data augmentation and large language model (LLM) error correction to mitigate this problem. We apply various augmentation techniques on a corpus of Dutch oral cancer speech to create synthetic data, and evaluate their effect on ASR performance. We finetune Whisper and Massively Multilingual Speech (MMS) models for each augmentation technique and observe, on average, an 8% relative decrease in Word Error Rate (WER) when including data created using text-to-speech (TTS). When employing LLMs for error correction, we see a further 21.4-26.2% relative decrease in WER for finetuned ASR models and a 10.0% relative decrease for non-finetuned models. Overall, we achieve a 40% relative WER decrease for Whisper and a 50% relative WER decrease for MMS, indicating that a combination of data augmentation and LLM correction is a viable strategy for the recognition of OC speech.
匹配关键词: TTS
---

[ACADEMIC - ARXIV]
标题: AgentSteerTTS: A Multi-Agent Closed-Loop Framework for Composite-Instruction Text-to-Speech
作者: Bin Kang, Shaoguo Wen, Yang Fan, Shunlong Wu, Junjie Wang, Yulin Li, Junzhi Zhao, Junle Wang, Zhuotao Tian
链接: https://arxiv.org/abs/2605.17583v1
完整摘要: While existing text-to-speech (TTS) models exhibit high expressiveness, fine-grained control over composite instructions remains challenging due to the structural mismatch between discrete textual intents and continuous acoustic realizations. Inspired by human cognitive decoupling, we introduce AgentSteerTTS, a multi-agent closed-loop framework designed for intent-faithful expressive control of composite instructions. First, in our framework, an adversarial disentanglement agent mitigates speaker-emotion leakage by learning separable identity and emotion-prosody subspaces with leakage-suppressing regularization. Next, a Dual-Stream Anchoring Controller grounds abstract intents using a large-scale acoustic prototype library: a Retrieval Agent selects expressive anchors, while a Synthesis Agent fuses them into continuous control vectors via gated attention. Finally, a Fast-Slow Feedback Agent refines output intensity through latent gradient correction and resolves semantic-acoustic mismatches using high-level perceptual critique. Experiments on a composite-instruction benchmark and public test sets show that AgentSteerTTS yields consistent and significant improvements to the baselines, demonstrating the effectiveness of the proposed method.
匹配关键词: TTS
---

[ACADEMIC - ARXIV]
标题: Beyond Binary: Reframing GUI Critique as Continuous Semantic Alignment
作者: Yuchen Sun, Pei Fu, Shaojie Zhang, Anan Du, Xiuwen Xi, Ruoceng Zhang, Zhenbo Luo, Jian Luan, Chongyang Zhang
链接: https://arxiv.org/abs/2605.14311v2
完整摘要: Test-Time Scaling (TTS), which samples multiple candidate actions and ranks them via a Critic Model, has emerged as a promising paradigm for generalist GUI agents. Its efficacy thus hinges on the critic's fine-grained ranking ability. However, existing GUI critic models uniformly adopt binary classification. Our motivational analysis of these models exposes a severe entanglement: scores for valid actions and plausible-but-invalid distractors become indistinguishable. We attribute this failure to two structural defects: Affordance Collapse--the hierarchical affordance space is compressed into 0/1 labels; and Noise Sensitivity--binary objectives overfit to noisy decision boundaries. To resolve this, we introduce BBCritic (Beyond-Binary Critic), a paradigm shift grounded in the Functional Equivalence Hypothesis. Through two-stage contrastive learning, BBCritic aligns instructions and actions in a shared Affordance Space, recovering the hierarchical structure that binary supervision flattens. We also present BBBench (Beyond-Binary Bench), the first GUI critic benchmark that pairs a dense action space with a hierarchical four-level taxonomy, enabling fine-grained ranking evaluation. Experimental results show that BBCritic-3B, trained without any extra annotation, outperforms 7B-parameter SOTA binary models. It demonstrates strong zero-shot transferability across platforms and tasks, supporting our methodological view: GUI critique is fundamentally a metric-learning problem, not a classification one.
匹配关键词: TTS
---

[ACADEMIC - ARXIV]
标题: Contextual Biasing for Streaming ASR via CTC-based Word Spotting
作者: Kai-Chen Tsai, Tien-Hong Lo, Yun-Ting Sun, Berlin Chen
链接: https://arxiv.org/abs/2605.18222v1
完整摘要: Contextual biasing is essential to improving the recognition of rare and domain-specific words in an automatic speech recognition (ASR) system. While numerous methods have been proposed in recent years, most of them focus on offline settings and do not explicitly address the challenges of streaming ASR. For example, CTC-based word spotting (CTC-WS) have demonstrated strong performance by directly detecting keywords from CTC log-probabilities, but they are limited to offline processing and require access to the full utterance. In This work, we present a streaming extension of CTC-WS for real-time contextual biasing. Our method maintains active keyword paths across audio chunks using a stateful token passing algorithm, enabling the detection of keywords that span multiple chunks. To ensure low latency and stable output, we introduce an incremental commitment mechanism that only emits segments guaranteed not to be affected by future audio, while deferring uncertain regions. This method naturally integrates with streaming ASR pipelines and does not require modifications to the underlying acoustic model or additional training, making it practical for real-world deployment. Experimental results show that our method reduces overall WER and effectively improves keyword F-score, demonstrating its effectiveness for real-time ASR applications.
匹配关键词: ASR
---

[ACADEMIC - ARXIV]
标题: PAREDA: A Multi-Accent Speech Dataset of Natural Language Processing Research Discussions
作者: Sicheng Jin, Dipankar Srirag, Aditya Joshi
链接: https://arxiv.org/abs/2605.17860v1
完整摘要: While modern Automatic Speech Recognition (ASR) systems achieve high accuracy on benchmark corpora, their performance often degrades when there is real-world variability. This work focuses on variability arising due to accented, spontaneous, and domain-specific speech. In particular, we introduce PAper REading DAtaset (PAREDA), a first-of-its-kind multi-accent speech dataset consisting of discussions on academic Natural Language Processing (NLP) papers between speakers with Australian, Indian-English, and Chinese English accents. Each session elicits a spontaneous monologue (a summary of a paper's abstract) and a non-monologue (a question-and-answer session between participants), resulting in a corpus rich with technical jargon and conversational phenomena. We evaluate the performance of SOTA ASR models on PAREDA, analysing the impact of accent mixing and increased speech rate. Our results show that, in the zero-shot setting, models perform worse, confirming the dataset's challenging nature. However, fine-tuning on PAREDA significantly reduces the Word Error Rate (WER), demonstrating that our dataset captures linguistic characteristics often missing from existing corpora. PAREDA serves as a valuable new resource for building and evaluating more robust and inclusive ASR systems for specialised, real-world applications.
匹配关键词: ASR
---

[ACADEMIC - ARXIV]
标题: Are Sparse Autoencoder Benchmarks Reliable?
作者: David Chanin
链接: https://arxiv.org/abs/2605.18229v1
完整摘要: Sparse autoencoders (SAEs) are a core interpretability tool for large language models, and progress on SAE architectures depends on benchmarks that reliably distinguish better SAEs from worse ones. We audit the SAE quality metrics in SAEBench, the de-facto standard SAE evaluation suite, through three complementary lenses: reseed noise on a fixed SAE, ground-truth correlation on synthetic SAEs, and discriminability across training trajectories. We find that two of these metrics, Targeted Probe Perturbation (TPP) and Spurious Correlation Removal (SCR), fail multiple lenses at their canonical settings and should not be used to evaluate SAEs. The other metrics show higher reseed noise and lower discriminability than the field assumes. The sae-probes variant of $k$-sparse probing is the most reliable metric we tested, but even sae-probes struggles to separate variants of the same SAE architecture. Our results show the field needs better SAE benchmarks.
匹配关键词: audio language model
---

[ACADEMIC - ARXIV]
标题: Context Memorization for Efficient Long Context Generation
作者: Yasuyuki Okoshi, Hao Mark Chen, Guanxi Lu, Hongxiang Fan, Masato Motomura, Daichi Fujiki
链接: https://arxiv.org/abs/2605.18226v1
完整摘要: Modern large language model (LLM) applications increasingly rely on long conditioning prefixes to control model behavior at inference time. While prefix-augmented inference is effective, it incurs two structural limitations: i) the prefix's influence fades as generation proceeds, and ii) attention computation over the prefix scales linearly with its length. Existing approaches either keep the prefix in attention while compressing it, or internalize it into model parameters through gradient-based training. The former still attends to the prefix at inference, while the latter is training-intensive and ill-suited to prefix updates. To address these issues, we propose attention-state memory, a training-free approach that externalizes the prefix into a lightweight, lookup-based memory of precomputed attention states between prefix and query tokens. On ManyICLBench with LLaMA-3.1-8B, our method improves accuracy over in-context learning at 1K-8K memory budgets while reducing attention latency by 1.36x at 8K, and surpasses full-attention RAG performance on NBA benchmark using only 20% of its memory footprint.
匹配关键词: audio language model
---

[ACADEMIC - ARXIV]
标题: Contextual Biasing for Streaming ASR via CTC-based Word Spotting
作者: Kai-Chen Tsai, Tien-Hong Lo, Yun-Ting Sun, Berlin Chen
链接: https://arxiv.org/abs/2605.18222v1
完整摘要: Contextual biasing is essential to improving the recognition of rare and domain-specific words in an automatic speech recognition (ASR) system. While numerous methods have been proposed in recent years, most of them focus on offline settings and do not explicitly address the challenges of streaming ASR. For example, CTC-based word spotting (CTC-WS) have demonstrated strong performance by directly detecting keywords from CTC log-probabilities, but they are limited to offline processing and require access to the full utterance. In This work, we present a streaming extension of CTC-WS for real-time contextual biasing. Our method maintains active keyword paths across audio chunks using a stateful token passing algorithm, enabling the detection of keywords that span multiple chunks. To ensure low latency and stable output, we introduce an incremental commitment mechanism that only emits segments guaranteed not to be affected by future audio, while deferring uncertain regions. This method naturally integrates with streaming ASR pipelines and does not require modifications to the underlying acoustic model or additional training, making it practical for real-world deployment. Experimental results show that our method reduces overall WER and effectively improves keyword F-score, demonstrating its effectiveness for real-time ASR applications.
匹配关键词: audio language model
---

[ACADEMIC - ARXIV]
标题: SIREM: Speech-Informed MRI Reconstruction with Learned Sampling
作者: Md Hasan, Nyvenn Castro, Daiqi Liu, Lukas Mulzer, Jana Hutter, Jonghye Woo, Moritz Zaiss, Andreas Maier, Paula A. Perez-Toro
链接: https://arxiv.org/abs/2605.18221v1
完整摘要: Real-time magnetic resonance imaging (rtMRI) of speech production enables non-invasive visualization of dynamic vocal-tract motion and is valuable for speech science and clinical assessment. However, rtMRI is fundamentally constrained by trade-offs among spatial resolution, temporal resolution, and acquisition speed, often leading to undersampled k-space measurements and degraded reconstructions. We propose SIREM, a speech-informed MRI reconstruction framework that uses synchronized speech as a cross-modal prior. The central idea is that vocal-tract configurations during speech are correlated with the produced acoustics, making part of the image content predictable from audio. SIREM models each frame as a fusion of an audio-driven component and an MRI-driven component through a spatial weighting map. The audio branch predicts articulator-related structure from speech, while the MRI branch reconstructs complementary content from measured k-space data. We further introduce a learnable soft weighting profile over spiral arms, enabling a differentiable study of how k-space arm usage interacts with speech-informed fusion. This yields a unified multimodal formulation that combines audio-driven prediction, MRI reconstruction, and sampling adaptation. We evaluate SIREM on the USC speech rtMRI benchmark against standard baselines, including gridding, wavelet-based compressed sensing, and total variation. SIREM introduces a speech-informed reconstruction paradigm that operates in a substantially higher-throughput regime than iterative methods while preserving anatomically plausible vocal-tract structure. These results establish an initial benchmark for multimodal speech-informed rtMRI reconstruction and highlight the potential of synchronized speech as an auxiliary prior for fast reconstruction. The source code is available at https://github.com/mdhasanai/SIREM
匹配关键词: audio language model
---

[ACADEMIC - ARXIV]
标题: EgoInteract: Synthetic Egocentric Videos Generation for Interaction Understanding and Anticipation
作者: Rosario Leonardi, Francesco Ragusa, Daniele Materia, Alessandro Passanisi, James Fort, Jakob Engel, Giovanni Maria Farinella
链接: https://arxiv.org/abs/2605.18214v1
完整摘要: Collecting large-scale egocentric video datasets with dense spatial and temporal annotations is costly, slow, and often constrained by environmental biases, privacy constraints, and limited coverage of interaction patterns. While synthetic data has shown strong potential in several vision domains, its use for egocentric perception remains relatively underexplored, especially for tasks requiring temporally coherent human-object interactions. In this work, we introduce EgoInteract, a controllable simulator for egocentric video generation designed to model fine-grained egocentric interactions and their temporal dynamics. The simulator enables precise control over camera, human body and hand motion, object manipulation, and scene composition across diverse environments. Building on this framework, we generate a synthetic egocentric video dataset with dense spatial and temporal annotations for temporal action segmentation, next-active object detection, interaction anticipation, and hand-object interaction detection. We evaluate models trained with simulated data on multiple real-world egocentric benchmarks spanning diverse environments, object categories, and interaction patterns. Results show consistent improvements over strong baselines across tasks and datasets, demonstrating the effectiveness and transferability of our simulation-based approach.
匹配关键词: audio language model
---

[ACADEMIC - ARXIV]
标题: KVDrive: A Holistic Multi-Tier KV Cache Management System for Long-Context LLM Inference
作者: Jian Lin, Jiazhi Mi, Zicong Hong, Haodong Wang, Qianli Liu, Haodyue Zhang, Peng Li, Song Guo
链接: https://arxiv.org/abs/2605.18071v1
完整摘要: Supporting long-context LLMs is challenging due to the substantial memory demands of the key-value (KV) cache. Existing offloading systems store the full cache in host memory and selectively fetch critical entries during decoding, but this strategy quickly hits a ceiling: sparsity cannot be pushed further without degrading accuracy. As a result, when context length and batch size grow, the volume of KV transfers rises sharply and becomes the dominant source of decoding latency. We present KVDrive, a holistic multi-tier KV cache management system spanning GPU memory, host DRAM, and SSD. Unlike prior work that pursues greater sparsity through algorithmic refinements, KVDrive tackles the problem from a systems perspective - jointly orchestrating cache placement, pipeline scheduling, and cross-tier coordination to sustain high-throughput inference under tight GPU budgets. KVDrive advances three fundamental capabilities: it adapts cache management to attention behavior to maximize reuse and minimize redundant data movement; it restructures the decoding pipeline to overlap I/O- and CPU/GPU compute-bound stages, eliminating stalls across heterogeneous resources; and it harmonizes data movement across memory tiers to unlock scalable long-context inference far beyond GPU and DRAM limits. We have implemented a fully functional prototype of KVDrive and evaluated it on long-context benchmarks with popular LLMs. The system achieves up to 1.74x higher throughput compared to state-of-the-art works while preserving accuracy.
匹配关键词: KV cache
---

[ACADEMIC - ARXIV]
标题: Protection Is (Nearly) All You Need: Structural Protection Dominates Scoring in Globally Capped KV Eviction
作者: Gabriel Garcia
链接: https://arxiv.org/abs/2605.18053v1
完整摘要: We study KV cache eviction under a shared globally capped decode-time harness. Seven policies (LRU, H2O, SnapKV, StreamingLLM, Ada-KV, QUEST, Random) share a prompt-boundary vulnerability: without structural protection, they collapse to near-zero quality on six pure-transformer models (F1$\leq$0.064). Reserving 10\% of cache at each boundary recovers 69--90\% of the $C{=}2{,}048$ reference-ceiling quality on seven LongBench models at $C{=}256$ (13\% retention); a ten-model panel spans 68--98\%. An attention-mass pilot (Qwen2.5-3B, $N{=}30$) suggests why: the position-0 sink holds ${\sim}75\%$ of prefix mass, while other boundary tokens sit near ${\sim}0.41{\times}$ uniform expectation, so attention scorers retain the sink but still drop structurally critical tokens. With protection, simplified score-isolation variants are TOST-equivalent to LRU at $K{=}32$ ($Δ{=}0.02$); at $K{=}8$, attention policies pairwise converge yet beat LRU by 0.011--0.021 F1 across $C{=}256$ and $C{=}512$. Faithful Ada-KV/QUEST add ${\sim}0.03$--$0.04$ F1 on Mistral-7B and Phi-3.5 beyond simplified variants. A NIAH-32K regime-transfer pilot on Qwen3-4B (decode vs.\ prefill, $C{\in}\{512,2048\}$) shows near-identical protection lifts (ratio 0.99--1.00). At 64K, protection helps but recovery is modest; faithful per-head scoring matches full-cache ceiling on Gemma-3-4B at 6.3\% retention only when the model already supports strong 64K retrieval without eviction. Overall: protection dominates; scoring differences are secondary once boundaries are guarded; per-head allocation gives a further modest gain.
匹配关键词: KV cache
---

[ACADEMIC - ARXIV]
标题: PanoWorld: A Generative Spatial World Model for Consistent Whole-House Panorama Synthesis
作者: Jinrang Jia, Zhenjia Li, Yijiang Hu, Yifeng Shi
链接: https://arxiv.org/abs/2605.17916v1
完整摘要: Generating a consistent whole-house VR tour from a floorplan and style reference requires both photorealistic panoramas and cross-view spatial coherence. Pure 2D generators produce appealing single panoramas but re-imagine geometry and materials when the viewpoint changes, whereas monolithic 3D generation becomes expensive and loses fine texture at multi-room scale. We introduce PanoWorld, a generative spatial world model that treats whole-house synthesis as autoregressive generation of node-based 360-degree panoramas, matching the discrete navigation used by real VR tour products. PanoWorld uses a floorplan-derived 3D shell as a global geometric proxy and a dynamic 3D Gaussian Splatting cache as renderable spatial memory. A feed-forward panoramic LRM designed for metric-scale multi-room 360-degree inputs lifts generated panoramas into local 3DGS updates, while Room-aware Group Attention suppresses cross-room feature interference. A topology-aware progressive caching strategy fuses these local updates without repeatedly reconstructing the full history. By decoupling shell-based geometry guidance from cache-rendered visual memory, PanoWorld preserves high-frequency 2D synthesis quality while improving cross-node layout and material consistency. The project link is https://jjrcn.github.io/PanoWorld-project-home/
匹配关键词: KV cache
---

[ACADEMIC - ARXIV]
标题: Ethical Hyper-Velocity (EHV): A Provably Deterministic Governance-Aware JIT Compiler Architecture for Agentic Systems
作者: Riddhi Mohan Sharma
链接: https://arxiv.org/abs/2605.17909v1
完整摘要: As autonomous agentic systems scale across regulated critical infrastructures, the lack of mechanistic, hardware-rooted enforcement for high-frequency policy updates presents a fundamental safety gap. We introduce Ethical Hyper-Velocity (EHV), a novel architectural framework for the formal verification of AI governance policies at runtime. Unlike retrospective auditing frameworks (ISO/IEC 42001, NIST AI RMF) which introduce 14-30 day latencies, EHV relocates the Policy Enforcement Point (PEP) into the inference pipeline via a Governance-Aware Just-In-Time (JIT) Compiler. By integrating Conflict-free Replicated Data Types (CRDTs) for policy synchronization and Epoch-based Attestation Caching within Trusted Execution Environments (TEEs), EHV achieves Sub-millisecond Formal Determinism (SMFD). We demonstrate via TLA+ formal verification that non-compliant agentic actions are computationally unreachable within the system's bounded operating state space. We prove that O(1) runtime enforcement can eliminate the traditional trade-off between deployment velocity and governance integrity, reducing Governance Latency from O(days) to O(1).
匹配关键词: KV cache
---

[ACADEMIC - ARXIV]
标题: OSCAR: Offline Spectral Covariance-Aware Rotation for 2-bit KV Cache Quantization
作者: Zhongzhu Zhou, Donglin Zhuang, Jisen Li, Ziyan Chen, Shuaiwen Leon Song, Ben Athiwaratkun, Xiaoxia Wu
链接: https://arxiv.org/abs/2605.17757v1
完整摘要: INT2 KV-cache quantization is attractive for long-context LLM serving, but it remains difficult to make both accurate and deployable. Simple rotations such as Hadamard transforms reduce outliers, but still degrade at INT2 because they are not aligned with downstream attention. We propose OSCAR, an Ultra-low-bit KV Cache quantization method that estimates attention-aware covariance structures offline and uses them to derive fixed rotations and clipping thresholds for quantization. In this way, it aligns KV quantization with the covariance structures that attention actually consumes. More importantly, we not only provide theoretical justification but also develop a fully deployable OSCAR system with a custom INT2 attention kernel that remains compatible with paged KV-cache serving and fused kernel pipelines, enabling seamless integration into modern LLM serving frameworks such as SGLang and vLLM. We evaluate our methods on recent reasoning models with reasoning traces of up to 32k tokens across 5 tasks. On Qwen3-4B-Thinking-2507 and Qwen3-8B, OSCAR reduces the BF16 accuracy gap to 3.78 and 1.42 points, respectively, while naive rotation INT2 collapses to nearly zero. We further scale OSCAR to Qwen3-32B and GLM-4.7 (358B params), where it remains effectively on par with BF16. On long context - RULER-NIAH up to 128K, OSCAR remains robust on both Qwen3 models, while naive rotation INT2 collapses. System-wise, OSCAR reduces KV-cache memory by approximately 8x, improves throughput by up to 7x at large batch sizes under the same memory budget, and accelerates batch-size-1 decoding by up to 3x over BF16 due to reduced memory bandwidth overhead.
匹配关键词: KV cache
---

[ACADEMIC - ARXIV]
标题: CATRF: Codec-Adaptive TriPlane Radiance Fields for Volumetric Content Delivery
作者: Tung-I Chen, Lingdong Wang, Subhransu Maji, Ramesh K. Sitaraman
链接: https://arxiv.org/abs/2605.18054v1
完整摘要: Volumetric media promises next-generation content delivery applications, but its bandwidth demand remains a key bottleneck. Implicit and hybrid volumetric representations reduce model sizes, yet still require careful coding to reach 2D video-like bitrates. We present CATRF, a standard-codec-in-the-loop compression framework for plane-factorized radiance fields. During training, we quantize and pack 2D feature planes into codec-friendly canvases, run a standard codec roundtrip (JPEG/VP9/HEVC/AV1), then unpack and dequantize the decoded features before volume rendering. We use a straight-through estimator (STE) to insert the non-differentiable, standard codec pipeline into the training loop, allowing radiance-field features to adapt directly to the real, client-side codec distortions without introducing any learned codec parameters. On both static and dynamic benchmarks, CATRF consistently achieves a better rate-distortion trade-off over codec-agnostic and learned-codec-in-the-loop baselines, and also outperforms recent compressed 3DGS methods in both compression efficiency and decoding speed. These results highlight a practical path toward low-bitrate, compression-resilient volumetric representations for free-viewpoint video streaming.
匹配关键词: quantization
---

[ACADEMIC - ARXIV]
标题: Inter-LPCM: Learning-based Inter-Frame Predictive Coding for LiDAR Point Cloud Compression
作者: Chang Sun, Hui Yuan, Shiqi Jiang, Chongzhen Tian, Guanghui Zhang, Raouf Hamzaoui
链接: https://arxiv.org/abs/2605.18006v1
完整摘要: Because LiDAR sensors acquire point clouds with a fixed angular resolution, the resulting data can be systematically parameterized and efficiently compressed in the spherical coordinate system. Traditional spherical coordinate-based point cloud compression methods have demonstrated strong rate-distortion (RD) performance, with the predictive geometry coding (PredGeom) method in the geometry-based point cloud compression (G-PCC) standard being a prominent example. Although PredGeom includes an inter-frame prediction mode, it relies on a simple linear model, which limits its ability to capture complex motion patterns and structural dependencies. Meanwhile, existing learning-based compression methods in the spherical domain do not exploit inter-frame correlations to reduce geometry redundancy. To address these limitations, we propose a learning-based inter-frame predictive coding method, termed Inter-LPCM. For azimuth prediction, we employ a delta coding strategy based on the predefined angular resolution. To improve radius compression, we introduce an inter-frame radius predictive (Inter-RP) model that estimates the current point's radius using neighboring points from both the current frame and the registered reference frame. In addition, we design a lightweight attention-based prediction (LAEP) model to predict elevation angles by capturing long-range geometric correlations across different coordinates. For quantization, we propose an RD-optimized method to select quantization steps in the spherical coordinate system. For entropy coding, we design distinct models for each spherical coordinate component. These models are adapted to the statistical priors of each coordinate, enabling more accurate probability estimation. Our source code is publicly available at https://github.com/SDUChangSun/Inter-LPCM
匹配关键词: quantization
---

[ACADEMIC - ARXIV]
标题: MARR: Module-Adaptive Residual Reconstruction for Low-Bit Post-Training Quantization
作者: Le Su, Xing Luo, Zhi Jin
链接: https://arxiv.org/abs/2605.17997v1
完整摘要: Recently, residual reconstruction-based model quantization methods have achieved promising performance in low-bit post-training quantization (PTQ) by introducing cross-layer residuals to reduce error accumulated from previous layers.However, these residuals may also introduce additional bias arising from the Hessian-approximation (HA) assumption underlying reconstruction-based PTQ, leading to suboptimal quantization performance.In this work, we analyze that multiplying the residual term by a scaling coefficient provides a direct way to mitigate the HA bias associated with residual strength, while preserving accumulated-error correction. More importantly, we observe that this trade-off is module-dependent, making a single global residual strength insufficient to balance effective correction and residual-related bias across modules.Based on these observations, we propose Module-Adaptive Residual Reconstruction (MARR), which assigns a module-specific scaling coefficient to adaptively balance accumulated-error correction and residual-related HA bias for each module.To avoid expensive per-module coefficient search and obtain a stable coefficient estimate, we design a Proportional-Integral-Derivative (PID)-based adaptive update strategy that uses reconstruction error as feedback to progressively refine this coefficient. Experiments on several typical large language models (LLMs) and vision transformers (ViTs) demonstrate the effectiveness of MARR under low-bit quantization (less than or equal to 4-bit), achieving up to 20.2% performance gains on LLMs and up to 4.6% relative gains on ViTs over the residual reconstruction state-of-the-art methods.Code will be made publicly available upon acceptance.
匹配关键词: quantization
---

[ACADEMIC - ARXIV]
标题: Attention Sinks and Outliers in Attention Residuals
作者: Haozheng Luo, Haoran Dai, Shaoyang Zhang, Xi Chen, Eric Hanchen Jiang, Yijiang Li, Jingyuan Huang, Chenghao Qiu, Chenwei Xu, Zhenyu Pan, Haotian Zhang, Binghui Wang, Yan Chen
链接: https://arxiv.org/abs/2605.17887v1
完整摘要: We propose OASIS, an outlier- and sink-aware technique built on inter-layer null signaling. As AttnResidual architectures introduce an additional depth-wise normalization channel, they improve inter-layer routing flexibility but also exacerbate attention sinks, activation outliers, and the resulting degradation in inference stability and quantization robustness. OASIS addresses this issue by introducing a Softmax1-based null space and coupling token-level null evidence to depth routing through an inter-layer null signal, thereby reducing sink-dominated routing and improving structural robustness. Theoretically, we show that the dual-normalization design of AttnResidual intensifies sink formation and quantization brittleness. Experimentally, we compare OASIS against five baselines on three real-world datasets and observe consistent improvements in both attention sink and post-quantization performance. Notably, OASIS achieves an average reduction of 9.26% in maximum infinity norm and 2.60% in average kurtosis across the evaluated settings, while lowering perplexity by 75.85% under W8A8 and improving GSM8K Pass@1 by 12.42% under W4A4.
匹配关键词: quantization
---

[ACADEMIC - ARXIV]
标题: Learning Variable-Length Tokenization for Generative Recommendation
作者: Minhao Wang, Bowen Wu, Wei Zhang
链接: https://arxiv.org/abs/2605.17779v1
完整摘要: Generative recommendation reformulates recommendation as next-token prediction over discrete semantic identifiers (IDs). A fundamental yet unexplored design choice is that existing methods employ fixed-length tokenization for all items, implicitly assuming uniform encoding capacity regardless of item characteristics. Through systematic experiments across four datasets, we discover the Popularity-Length Paradox: popular items achieve optimal performance with short IDs, while tail items require substantially longer codes to capture discriminative semantics. This reveals a critical mismatch where popular items benefit from abundant collaborative signals and require minimal semantic detail, whereas tail items must rely on fine-grained content features due to sparse interaction data. To address this, we propose VarLenRec, a framework for learning variable-length tokenization. We develop Popularity-Weighted Information Budget Allocation (PIBA), an information-theoretic framework proving that optimal ID length should scale as a negative power of popularity. Directly implementing variable-length allocation faces two technical challenges: standard Euclidean residual quantization lacks geometric capacity to support diverse code lengths without distortion, and discrete length decisions are non-differentiable. We address these through Hyperbolic Residual Quantization, which leverages the exponential volume growth of the Poincaré ball to naturally stratify encoding capacity, and a Soft Length Controller, which enables differentiable length prediction via continuous layer retention probabilities regularized by PIBA-derived priors. Extensive experiments demonstrate that VarLenRec achieves significant improvements over state-of-the-art methods in recommendation accuracy and training/inference efficiency, revealing the importance of adaptive encoding capacity in generative recommendation.
匹配关键词: quantization
---

[ACADEMIC - ARXIV]
标题: Leveraging Graph Structure in Seq2Seq Models for Knowledge Graph Link Prediction
作者: Luu Huu Phuc, Ratan Bahadur Thapa, Mojtaba Nayyeri, Jingcheng Wu, Evgeny Kharlamov, Steffen Staab
链接: https://arxiv.org/abs/2605.18211v1
完整摘要: We introduce Graph-Augmented Sequence-to-Sequence (GA-S2S), a novel framework that integrates a T5-small encoder-decoder with a Relational Graph Attention Network (RGAT) to improve link prediction in knowledge graphs. While existing Seq2Seq models rely solely on surface-level textual descriptions of entities and relations and at best, flatten the neighborhoods of a query entity into a single linear sequence, thereby discarding the inherent graph structure, GA-S2S jointly encodes both textual features and the full $k$-hop subgraph topology surrounding the query entity. By integrating raw encoder outputs with RGAT's relation-aware embeddings, our model captures and leverages richer multi-hop relational patterns and textual information. Our preliminary experiments on the CoDEx dataset demonstrate that GA-S2S outperforms competitive Seq2Seq-based baseline models, achieving up to a 19\% relative gain in link prediction accuracy.
匹配关键词: speculative decoding
---

[ACADEMIC - ARXIV]
标题: Elastic-dLLM: Position Preserving Context Compression and Augmentation of Diffusion LLMs
作者: Junyi Wu, Tianchen Zhao, Shaoqiu Zhang, Linfeng Zhang, Guohao Dai, Yu Wang
链接: https://arxiv.org/abs/2605.18165v1
完整摘要: Unlike autoregressive models, which generate one token at a time, dLLMs denoise a chunk of [MASK] tokens jointly and sample one or more tokens per step; despite enabling parallel decoding, this process incurs substantial computational cost due to the large chunk size of masked tokens. We observe that much of this cost is spent on repeatedly processing the preceding context and many [MASK] tokens with the same feature representations, indicating considerable computational redundancy. In this work, we revisit dLLM's redundancy from the perspective of [MASK] tokens. Through systematic analysis, we verify the redundancy of [MASK] tokens while revealing their critical role in providing structural information. Guided by these findings, we propose position-preserving [MASK] token compression and terminal-aware augmentation. By compressing redundant [MASK] computation, this approach accelerates decoding and further provides a natural extension toward context-folding-like long-context scaling under limited input-length constraints for full-sequence dLLMs such as LLaDA-8B-Instruct and LLaDA-1.5. Moreover, for block dLLMs such as LLaDA2.0-mini, it augments the context with a protected terminal [MASK] token to enhance generation quality with negligible overhead.
匹配关键词: speculative decoding
---

[ACADEMIC - ARXIV]
标题: Vision Inference Former: Sustaining Visual Consistency in Multimodal Large Language Models
作者: Xinpeng Dong, Min Zhang, Kairong Han, Xu Tan, Fei Wu, Kun Kuang
链接: https://arxiv.org/abs/2605.18160v1
完整摘要: In recent years, multimodal large language models (MLLMs) have achieved remarkable progress, primarily attributed to effective paradigms for integrating visual and textual information. The dominant connector-based paradigm projects visual features into textual sequence, enabling unified multimodal alignment and reasoning within a generative architecture. However, our experiments reveal two key limitations: (1) Although visual information serves as the core evidential modality in MLLMs, it is treated on par with textual tokens, diminishing the unique contribution of the visual modality; (2) As generation length increases, particularly within a limited context window, the model's dependence on visual information progressively weakens, resulting in deteriorated vision-language alignment and reduced consistency between generated content and visual semantics. To address these challenges, we propose the Vision Inference Former (VIF), a lightweight architectural module that establishes a direct bridge between pure visual representations and the model's output space. Specifically, VIF continuously injects visual semantics throughout the decoding phase of the inference process, ensuring that the model remains firmly grounded in visual content during generation. We conduct experiments on 14 benchmark tasks covering general reasoning, OCR, table understanding, vision-centric evaluation, and hallucination. Experimental results show that VIF consistently improves model performance across diverse architectures while introducing minimal additional overhead. The code for this work is available at https://github.com/Dong-Xinpeng/VIF.
匹配关键词: speculative decoding
---

[ACADEMIC - ARXIV]
标题: The Expressive Power of Low Precision Softmax Transformers with (Summarized) Chain-of-Thought
作者: Moritz Brösamle, Stephan Eckstein
链接: https://arxiv.org/abs/2605.18079v1
完整摘要: Existing expressivity results for transformers typically rely on hardmax attention, high precision, and other architectural modifications that disconnect them from the models used in practice. We bridge this gap by analyzing standard transformer decoders with softmax attention and rounding of activations and attention weights, while allowing depth and width to grow logarithmically with the context length. As an intermediate step, we construct hardmax transformers with ternary activations and well-separated attention scores that simulate Turing machines using Chain-of-Thought (CoT). This lets us convert the constructions to equivalent softmax transformers without the unrealistic parameter magnitudes or activation precision that prior approaches would require. Using the same technique, we analyze a recently proposed summarized CoT paradigm and show that it simulates Turing machines more efficiently, with model size scaling logarithmically in a space bound rather than a time bound. We empirically test predictions made by our results on a Sudoku reasoning task and find better alignment with learnability than for prior high-precision results. Our code is available at https://github.com/moritzbroe/transformer-expressivity.
匹配关键词: speculative decoding
---

[ACADEMIC - ARXIV]
标题: KVDrive: A Holistic Multi-Tier KV Cache Management System for Long-Context LLM Inference
作者: Jian Lin, Jiazhi Mi, Zicong Hong, Haodong Wang, Qianli Liu, Haodyue Zhang, Peng Li, Song Guo
链接: https://arxiv.org/abs/2605.18071v1
完整摘要: Supporting long-context LLMs is challenging due to the substantial memory demands of the key-value (KV) cache. Existing offloading systems store the full cache in host memory and selectively fetch critical entries during decoding, but this strategy quickly hits a ceiling: sparsity cannot be pushed further without degrading accuracy. As a result, when context length and batch size grow, the volume of KV transfers rises sharply and becomes the dominant source of decoding latency. We present KVDrive, a holistic multi-tier KV cache management system spanning GPU memory, host DRAM, and SSD. Unlike prior work that pursues greater sparsity through algorithmic refinements, KVDrive tackles the problem from a systems perspective - jointly orchestrating cache placement, pipeline scheduling, and cross-tier coordination to sustain high-throughput inference under tight GPU budgets. KVDrive advances three fundamental capabilities: it adapts cache management to attention behavior to maximize reuse and minimize redundant data movement; it restructures the decoding pipeline to overlap I/O- and CPU/GPU compute-bound stages, eliminating stalls across heterogeneous resources; and it harmonizes data movement across memory tiers to unlock scalable long-context inference far beyond GPU and DRAM limits. We have implemented a fully functional prototype of KVDrive and evaluated it on long-context benchmarks with popular LLMs. The system achieves up to 1.74x higher throughput compared to state-of-the-art works while preserving accuracy.
匹配关键词: speculative decoding
---

[ACADEMIC - ARXIV]
标题: Pairwise Preference Reward and Group-Based Diversity Enhancement for Superior Open-Ended Generation
作者: Guining Cao, Jiaxin Peng, Chu Zeng, Yu Zhao, Shuangyong Song, Yongxiang
链接: https://arxiv.org/abs/2605.18191v1
完整摘要: Current reinforcement learning(RL) methods are broadly applicable and powerful in verifiable settings where scalar rewards can be provided. However, in open-ended generation tasks, verifying the correctness of responses remains challenging, and training reward models incurs substantial computational and annotation costs. Moreover, reinforcement learning (RLVR) often leads to diversity collapse and produces stereotypical or rigid outputs, outcomes that are particularly undesirable in open-domain scenarios. We propose Pairwise Preference Reward and Group-based Diversity Enhancement (PPR-GDE), a RL method that is more suitable for open-ended generation. PPR-GDE does not require scalar rewards and incorporates group-level diversity into the reward signal, it preserves the comparative structure of subjective evaluation through a pairwise preference reward, mitigates judge position bias via repeated comparisons with swapped response order, and introduces a group-based diversity reward that explicitly encourages semantic dispersion within a response group, all of these reward signals are integrated into a unified group-relative policy optimization objective. We instantiate PPR-GDE on role-playing task, experiments show that PPR-GDE achieves a better alignment quality as well as expressive diversity than strong RL baselines. Further analysis shows that pairwise preference is critical for preference alignment in subjective perspective, while the diversity metric plays an essential role in achieving superior expressive diversity and broader semantic coverage.
匹配关键词: kernel optimization
---

[ACADEMIC - ARXIV]
标题: Canonical Regularisation of Wide Feature-Learning Neural Networks
作者: George Whittle, Pranav Vaidhyanathan, Juliusz Ziomek, Natalia Ares, Maike A. Osborne
链接: https://arxiv.org/abs/2605.18180v1
完整摘要: Wide neural networks in the feature-learning regime drive modern deep learning, and yet they remain far less studied than their kernel-regime counterparts. We consider a critical yet under-explored difference between these two regimes: the regulariser and prior implied by gradient flow training. This canonical regularisation property is well-studied in kernel regime networks -- of all the infinite global minima, gradient flow selects exactly the vanishing ridge solution -- and underpins the celebrated NN-GP correspondence, precisely allowing the modelling of noise during training. However, we prove ridge regularisation biases gradient flow in feature-learning regime networks, even in the infinitesimal limit of vanishing regularisation. Over training, ridge distorts the inductive bias of the network, with a particular damage done to pretrained networks where the implicit prior is informative. We resolve this by axiomatising the canonical regulariser as a regime-agnostic function-space energy and lift, which uniquely identifies ridge in the kernel regime, and crucially generalises to the feature-learning regime. By studying the Riemannian geometry of feature-learning networks, we derive geodesic ridge from our framework, generalising ridge to the feature-learning regime. Correspondingly, we prove the canonical function-space prior is a Riemannian Gibbs Process, generalising the more familiar Gaussian Process. As a practical contribution, we propose arc ridge as a minimax-robust, scalable surrogate to geodesic ridge, revealing a deep relationship between early stopping and canonical regularisation across learning regimes. Finally, we demonstrate the consequences of our theory empirically on both image processing and NLP transfer-learning problems.
匹配关键词: kernel optimization
---

[ACADEMIC - ARXIV]
标题: Ringmaster LMO: Asynchronous Linear Minimization Oracle Momentum Method
作者: Abdurakhmon Sadiev, Artavazd Maranjyan, Ivan Ilin, Peter Richtárik
链接: https://arxiv.org/abs/2605.18174v1
完整摘要: Muon has recently emerged as a strong alternative to AdamW for training neural networks, with encouraging large-scale pretraining results and growing evidence that matrix-structured updates can be faster in practice. Yet Muon, and more generally Linear Minimization Oracle (LMO) based methods, are typically used synchronously. This is problematic in heterogeneous distributed systems, where workers complete gradient computations at different speeds and synchronous training must repeatedly wait for slower workers. In this work, we introduce Ringmaster LMO, an asynchronous LMO-based momentum method for unconstrained stochastic nonconvex optimization. Our method builds on the delay-thresholding idea of Ringmaster ASGD. For SGD-type methods, Ringmaster ASGD achieves optimal time complexity by discarding overly stale gradients. Ringmaster LMO extends this mechanism to general LMO-based updates. We establish convergence guarantees under generalized $(L_0, L_1)$-smoothness and further develop a parameter-agnostic variant with decreasing stepsizes and adaptive delay thresholds. Finally, we translate our iteration guarantees into time complexity bounds under heterogeneous worker computation times. In the classical Euclidean smooth setting, these bounds recover the optimal time complexity of Ringmaster ASGD. Experiments on stochastic quadratic problems and NanoChat language-model pretraining show that the advantages of Ringmaster LMO grow with system heterogeneity and that the method outperforms strong synchronous and asynchronous baselines.
匹配关键词: kernel optimization
---

[ACADEMIC - ARXIV]
标题: Do You Need Text Rectification? Soft Attention Mask Embedding for Rectification-Free Scene Text Spotting
作者: Antonio Colombo, Giovanni Bianchi
链接: https://arxiv.org/abs/2605.18173v1
完整摘要: End-to-end scene text spotting, which unifies text detection and recognition within a single framework, has witnessed remarkable progress driven by deep learning advances. However, most existing approaches still suffer from incomplete mask proposals caused by multi-scale variation, arbitrary text shapes, and complex background interference, thereby degrading recognition accuracy. In this paper, we propose a novel Soft Attention Mask Embedding module (SAME) that leverages the global receptive field of Transformer encoders to encode high-level features and compute soft attention weights, which are then hierarchically embedded with predicted masks to generate refined text-boundary-aware masks that effectively suppress background noise. Building upon this module, we present SAME-Net, a robust end-to-end text spotting framework that requires neither character-level annotations nor auxiliary text rectification modules. Since the soft attention mechanism is fully differentiable, recognition loss gradients can be back-propagated through the SAME module to the detection branch, enabling joint optimization of detection and recognition objectives. Extensive experiments on challenging benchmarks demonstrate the effectiveness of our approach: SAME-Net achieves 84.02\% end-to-end H-mean on the arbitrarily-shaped Total-Text dataset, surpassing the previous state-of-the-art GLASS by 1.02\% in full-lexicon accuracy without additional training data, and obtains competitive 83.4\% strong-lexicon results on the multi-oriented ICDAR 2015 dataset.
匹配关键词: kernel optimization
---

[ACADEMIC - ARXIV]
标题: Buffer-Parameterized Machine Learning Surrogate Models for Cross-Technology Signal Integrity Analysis and Optimization
作者: Julian Withöft, Werner John, Emre Ecik, Ralf Brüning, Jürgen Götze
链接: https://arxiv.org/abs/2605.18170v1
完整摘要: Signal integrity (SI) analysis in printed circuit board (PCB) interconnects faces increasing complexity due to diverse integrated circuit (IC) buffer technologies, varying operating conditions, and manufacturing tolerances. Existing machine learning (ML) surrogate models for predicting SI metrics such as the inner eye contour, eye-height (EH), eye-width (EW), and transient waveform features typically rely on fixed buffer parameters, requiring costly new data generation and retraining cycles for every technology shift. This paper introduces a buffer-parameterized ML surrogate modeling methodology capable of handling cross-technology variations without retraining by treating IC buffer characteristics, e.g., clock frequency, supply voltage, rise/fall times, jitter, and internal resistors and capacitors, as dynamic model inputs alongside PCB parameters. To identify the optimal surrogate architecture for this high-dimensional space, a comprehensive benchmarking study compares tree-based methods (RFR/GBM), kernel methods (SVR/KRR), Gaussian process regression (GPR), and neural networks. The framework is subsequently validated on a complex interconnect with 44 design parameters. Results show that while anisotropic GPR excels in low-data regimes, neural networks heavily outperform other models on large datasets. Finally, the practical value of the ML surrogate models is demonstrated through a cross-technology design space exploration and optimization scenario, showcasing massive computational speedups for eye mask compliance checking compared to simulation.
匹配关键词: kernel optimization
---

[ACADEMIC - ARXIV]
标题: Context Memorization for Efficient Long Context Generation
作者: Yasuyuki Okoshi, Hao Mark Chen, Guanxi Lu, Hongxiang Fan, Masato Motomura, Daichi Fujiki
链接: https://arxiv.org/abs/2605.18226v1
完整摘要: Modern large language model (LLM) applications increasingly rely on long conditioning prefixes to control model behavior at inference time. While prefix-augmented inference is effective, it incurs two structural limitations: i) the prefix's influence fades as generation proceeds, and ii) attention computation over the prefix scales linearly with its length. Existing approaches either keep the prefix in attention while compressing it, or internalize it into model parameters through gradient-based training. The former still attends to the prefix at inference, while the latter is training-intensive and ill-suited to prefix updates. To address these issues, we propose attention-state memory, a training-free approach that externalizes the prefix into a lightweight, lookup-based memory of precomputed attention states between prefix and query tokens. On ManyICLBench with LLaMA-3.1-8B, our method improves accuracy over in-context learning at 1K-8K memory budgets while reducing attention latency by 1.36x at 8K, and surpasses full-attention RAG performance on NBA benchmark using only 20% of its memory footprint.
匹配关键词: memory efficiency
---

[ACADEMIC - ARXIV]
标题: Forward-Learned Discrete Diffusion: Learning how to noise to denoise faster
作者: Grigory Bartosh, Teodora Pandeva, Sushrut Karmalkar, Javier Zazo
链接: https://arxiv.org/abs/2605.18204v1
完整摘要: Discrete diffusion models are a powerful class of generative models with strong performance across many domains. For efficiency, however, discrete diffusion typically parameterizes the generative (reverse) process with factorized distributions, which makes it difficult for the model to learn the target process in a small number of steps and necessitates a long, computationally expensive sampling procedure. To reduce the gap between the target and model distributions and enable few-step generation, we propose Forward-Learned Discrete Diffusion (FLDD), which introduces discrete diffusion with a learnable forward (noising) process. Rather than fixing a Markovian forward chain, we adopt a non-Markovian formulation with learnable marginal and posterior distributions. This allows the generative process to remain factorized while matching the target defined by the noising process. We train all parameters end-to-end under the standard variational objective. Experiments on various benchmarks show that, for a given number of sampling steps, our approach produces a higher quality samples than conventional discrete diffusion models using the same reverse parameterization.
匹配关键词: memory efficiency
---

[ACADEMIC - ARXIV]
标题: Dual-Rate Diffusion: Accelerating diffusion models with an interleaved heavy-light network
作者: Grigory Bartosh, David Ruhe, Emiel Hoogeboom, Jonathan Heek, Thomas Mensink, Tim Salimans
链接: https://arxiv.org/abs/2605.18190v1
完整摘要: Diffusion models achieve state-of-the-art generative performance but suffer from high computational costs during inference due to the repeated evaluation of a heavy neural network. In this work, we propose Dual-Rate Diffusion, a method to accelerate sampling by interleaving the execution of a heavy high-capacity context encoder and a light efficient denoising model. The context encoder is evaluated sparsely to extract high-dimensional features, which are effectively reused by the light denoising model at every step to refine the sample efficiently. This approach significantly accelerates inference without compromising sample quality. On ImageNet benchmarks, Dual-Rate Diffusion matches the performance of standard baselines while reducing computational cost by a factor of $2$-$4$. Furthermore, we demonstrate that our method is compatible with distillation techniques, such as Moment Matching Distillation, enabling further efficiency gains in few-step generation.
匹配关键词: memory efficiency
---

[ACADEMIC - ARXIV]
标题: Fixed External Cameras as Common Prior Maps for Active 3D Scene Graph Generation
作者: Giorgia Modi, Davide Buoso, Giuseppe Averta, Daniele De Martini
链接: https://arxiv.org/abs/2605.18184v1
完整摘要: Commonly available prior information, such as BIM models, floor plans, and remote sensing images, can provide valuable geometric and semantic context for autonomous robotic systems. In this paper, we treat observations from fixed external RGB cameras as Common Prior Maps (CPMs): wide-field views of the environment that initialize a semantic and geometric scene prior before any robot motion begins. We present an RGB-only framework for active, incremental 3D scene graph (3DSG) generation that seamlessly fuses observations from both onboard robot cameras and fixed external cameras within a single hardware-agnostic pipeline. By relying solely on RGB observations processed by a feed-forward 3D reconstruction model, the system treats all cameras - onboard or external - identically, requiring no hardware modifications. A graph-based active semantic exploration framework then directly leverages the partial scene graph to guide the robot toward regions of high semantic uncertainty, progressively completing and refining the prior. Experiments demonstrate that bootstrapping the scene graph with even a single external camera increases initial object recall by up to +79%, and that the richer context of the prior significantly improves the efficiency of subsequent active exploration.
匹配关键词: memory efficiency
---

[ACADEMIC - ARXIV]
标题: Token-Space Mask Prediction for Efficient Vision Transformer Segmentation
作者: Calvin Galagain, Martyna Poreba, François Goulette
链接: https://arxiv.org/abs/2605.18177v1
完整摘要: Query-based Vision Transformer segmentation models typically reconstruct dense spatial feature maps to predict masks, inheriting design patterns from convolutional architectures. We show that this explicit image-space reconstruction is not required. We introduce TokenMask, a token-space mask head that computes mask logits directly from query-token affinities and performs interpolation in logit space rather than feature space. This reformulation preserves the original linear scoring mechanism while simplifying the computational structure. Across diverse ViT backbones, datasets and segmentation tasks, TokenMask consistently improves efficiency over prior approaches by reducing computational and memory requirements while maintaining competitive accuracy, leading to tangible speedups on NVIDIA Jetson AGX Orin using TensorRT FP16 inference. Overall, TokenMask yields a simpler and more deployment-friendly design for embedded vision systems.
匹配关键词: memory efficiency
---

[ACADEMIC - ARXIV]
标题: Beyond the Cartesian Illusion: Testing Two-Stage Multi-Modal Theory of Mind under Perceptual Bottlenecks
作者: Yajing Zhou, Xiangyu Kong
链接: https://arxiv.org/abs/2605.18194v1
完整摘要: While Multi-Modal Large Language Models (MLLMs) demonstrate impressive capabilities in general reasoning, their embodied spatial intelligence remains hampered by a "Cartesian Illusion" - a reliance on text-based probability distributions that lack grounded, 3D topological understanding. This limitation is starkly exposed in multi-agent environments, which demand more than just scene perception; they require second-order Theory of Mind (ToM). Specifically, an Agent A must be able to infer Agent B's belief about the environment, governed strictly by Agent B's physical orientation and sensory limitations. In this paper, we probe the limits of two-stage spatial inference in MLLMs through a novel audio-visual task: requiring Agent A to predict Agent B's estimation of A's relative location. To solve this, we propose an Epistemic Sensory Bottleneck module that abandons rigid, rule-based coordinate transformations. Instead, we introduce an Anchor-Based Embodied Spatial Decomposition Chain-of-Thought (CoT). This guides the MLLM through a "geometric-to-semantic" projection, forcing it to first establish B's local coordinate system and then dynamically weight visual and auditory modalities based on whether A falls within B's visual frustum. Extensive evaluations reveal that while current MLLMs fundamentally struggle with spatial symmetry and out-of-view ambiguities (establishing a rigorous zero-shot baseline of 42% accuracy), our sensory-bounded reasoning chain robustly outperforms pure egocentric and allocentric baselines. By systematically benchmarking these perceptual bottlenecks, our work exposes the current limits of MLLM spatial reasoning and establishes a foundational paradigm for epistemic, modality-aware inference in Embodied AI.
匹配关键词: agent
---

[ACADEMIC - ARXIV]
标题: Scalable Environments Drive Generalizable Agents
作者: Jiayi Zhang, Fanqi Kong, Guibin Zhang, Maojia Song, Zhaoyang Yu, Jianhao Ruan, Jinyu Xiang, Bang Liu, Chenglin Wu, Yuyu Luo
链接: https://arxiv.org/abs/2605.18181v1
完整摘要: Generalizable agents should adapt to diverse tasks and unseen environments beyond their training distribution. This position paper argues that such generalization requires environment scaling: expanding the distribution of executable rule-sets that agents interact with, rather than only increasing trajectories or tasks within fixed benchmarks. Current scaling practices largely focus on collecting more experience or broader task sets under fixed interaction rules, leaving agents brittle when underlying interfaces, dynamics, observations, or feedback signals change. The core challenge is therefore a world-level distribution shift: agents need systematic exposure to environments with meaningfully different executable rule-sets. To clarify this challenge, we propose a unified taxonomy that separates trajectory scaling, task scaling, and environment scaling by their primary deliverables and by what changes in the executable rule-set. Building on this taxonomy, we synthesize construction paradigms for scalable environments, contrasting programmatic generators that prioritize controllability and verifiability with generative world models that offer broader coverage and open-endedness. We further outline how environment scaling can be coupled with stateful learning mechanisms, emphasizing learned update rules for cross-environment adaptation. We conclude by discussing alternative perspectives and argue that scalable environments provide the essential substrate for measurable and controllable progress toward robust general agents.
匹配关键词: agent
---

[ACADEMIC - ARXIV]
标题: MARS: Technical Report for the CASTLE Challenge at EgoVis 2026
作者: Haoyu Zhang, Qiaohui Chu, Yisen Feng, Meng Liu, Weili Guan, Yaowei Wang, Liqiang Nie
链接: https://arxiv.org/abs/2605.18176v1
完整摘要: This report presents MARS, short for Multimodal Agentic Reasoning with Source selection, our system for the CASTLE Challenge at EgoVis 2026. Participants must answer 185 closed-form questions over the CASTLE 2024 dataset. In contrast to prior single-video egocentric benchmarks, CASTLE requires reasoning over four days of activity, 15 synchronized perspectives, official transcripts, and multiple auxiliary modalities, including personal photos, auxiliary videos, gaze, thermal imagery, and heartrate measurements. MARS therefore treats the task as an agentic evidence-selection problem over multimodal sources rather than a purely text-only pipeline. MARS first follows the official CASTLE directory organization to build evidence memories from two primary sources, videos and transcripts, and four auxiliary sources, gaze, heartrate, photos, and thermal imagery. Long videos are converted into captions and DeepSeek-based summaries only because CASTLE videos are too long to fit directly into the model context for every question; this step compresses temporal evidence while keeping photos and other auxiliary media available as source-specific evidence. At inference time, a GPT-5.4 decision agent repeatedly chooses whether to continue reasoning, request a specific missing modality, produce an answer, or fall back to a random option when the evidence remains insufficient. The resulting system achieved second place on the final CASTLE Challenge leaderboard. Our codes are available at https://github.com/Hyu-Zhang/MARS.
匹配关键词: agent
---

[ACADEMIC - ARXIV]
标题: Whispers in the Noise: Surrogate-Guided Concept Awakening via a Multi-Agent Framework
作者: Mengyu Sun, Ziyuan Yang, Zunlong Zhou, Junxu Liu, Haibo Hu, Yi Zhang
链接: https://arxiv.org/abs/2605.18150v1
完整摘要: Diffusion models (DMs) are widely used for text-to-image generation, but their strong generative capabilities also raise concerns about unsafe or undesirable content. Concept erasure aims to mitigate these risks by removing specific concepts from pretrained models. However, recent studies show that such methods often suppress rather than fully eliminate target concepts, leaving models vulnerable to awakening attacks. Existing approaches primarily rely on white-box access through optimization or inversion, while concept awakening under black-box constraints remains underexplored. In this work, we revisit the denoising process from a trajectory perspective and show that concept erasure mainly disrupts early-stage text-semantic alignment but does not fully prevent semantic information from propagating along the denoising dynamics. As generation proceeds, the model increasingly depends on the evolving noisy state rather than textual conditions, which creates an opportunity to bypass erased mappings. Motivated by this observation, we propose ConceptAgent, a training-free, black-box, multi-agent framework that awakens erased concepts by initializing the denoising trajectory from surrogate-guided noisy states. Extensive experiments demonstrate that ConceptAgent enables accurate and controllable awakening of erased concepts under black-box settings without access to model parameters, gradients, or internal representations. These results highlight fundamental limitations of current concept erasure methods and provide new insights into the dynamic nature of semantic control in DMs.
匹配关键词: agent
---

[ACADEMIC - ARXIV]
标题: Evidence-Grounded Frontier Mapping and Agentic Hypothesis Generation in Nanomedicine
作者: Christiaan G. A. Viviers, Koen de Bruin, Mirre M. Trines, Ayla M. Hokke, Roy van der Meel, Avi Schroeder, Twan Lammers, Willem J. M. Mulder, Fons van der Sommen
链接: https://arxiv.org/abs/2605.18144v1
完整摘要: Nanomedicine research spans delivery chemistry, immunology, imaging, biomaterials, and disease-specific translational science, yet its conceptual design space remains fragmented across a large and heterogeneous literature. To date, artificial intelligence in nanomedicine has focused primarily on property prediction and formulation optimization, with much less attention to evidence-grounded discovery support at the level of research direction selection. We introduce pArticleMap, a literature-mapping and research-hypothesis-generation system that combines article embeddings, similarity-graph analysis, sparse frontier extraction, structured evidence-pack retrieval, and an audited large-language-model (LLM) workflow for grounded ideation. Rather than forecasting future concept co-occurrence, pArticleMap targets low-density article-level bridge regions and cluster interfaces, then generates and scores citation-grounded hypotheses with large language models in an agentic setup. We evaluate the system with a retrospective realization benchmark (generate later literature under a historical cutoff) and a blinded human reader assessment layer across cue-conditioned nanomedicine tasks. Across 4 selected retrospective bundles, pArticleMap generated ideas and selected task-retained hypotheses (winner ideas) under the benchmark protocol. For task-level retained hypotheses, a pooled gold recovery rate of 10.8% was obtained, with a recall@10 of 15.9% and a future-neighborhood rate of 61.0%, indicating that the system often reached the correct forward-looking neighborhood (paper ideas) even without exact paper-level recovery. Human-agent agreement is modest overall, indicating that internal scoring is useful as a support signal but does not replace expert judgment. These results position pArticleMap as a conservative, evidence-grounded research assistant for nanomedicine.
匹配关键词: agent
---

[ACADEMIC - ARXIV]
标题: Are Sparse Autoencoder Benchmarks Reliable?
作者: David Chanin
链接: https://arxiv.org/abs/2605.18229v1
完整摘要: Sparse autoencoders (SAEs) are a core interpretability tool for large language models, and progress on SAE architectures depends on benchmarks that reliably distinguish better SAEs from worse ones. We audit the SAE quality metrics in SAEBench, the de-facto standard SAE evaluation suite, through three complementary lenses: reseed noise on a fixed SAE, ground-truth correlation on synthetic SAEs, and discriminability across training trajectories. We find that two of these metrics, Targeted Probe Perturbation (TPP) and Spurious Correlation Removal (SCR), fail multiple lenses at their canonical settings and should not be used to evaluate SAEs. The other metrics show higher reseed noise and lower discriminability than the field assumes. The sae-probes variant of $k$-sparse probing is the most reliable metric we tested, but even sae-probes struggles to separate variants of the same SAE architecture. Our results show the field needs better SAE benchmarks.
匹配关键词: tool use
---

[ACADEMIC - ARXIV]
标题: Context Memorization for Efficient Long Context Generation
作者: Yasuyuki Okoshi, Hao Mark Chen, Guanxi Lu, Hongxiang Fan, Masato Motomura, Daichi Fujiki
链接: https://arxiv.org/abs/2605.18226v1
完整摘要: Modern large language model (LLM) applications increasingly rely on long conditioning prefixes to control model behavior at inference time. While prefix-augmented inference is effective, it incurs two structural limitations: i) the prefix's influence fades as generation proceeds, and ii) attention computation over the prefix scales linearly with its length. Existing approaches either keep the prefix in attention while compressing it, or internalize it into model parameters through gradient-based training. The former still attends to the prefix at inference, while the latter is training-intensive and ill-suited to prefix updates. To address these issues, we propose attention-state memory, a training-free approach that externalizes the prefix into a lightweight, lookup-based memory of precomputed attention states between prefix and query tokens. On ManyICLBench with LLaMA-3.1-8B, our method improves accuracy over in-context learning at 1K-8K memory budgets while reducing attention latency by 1.36x at 8K, and surpasses full-attention RAG performance on NBA benchmark using only 20% of its memory footprint.
匹配关键词: tool use
---

[ACADEMIC - ARXIV]
标题: Contextual Biasing for Streaming ASR via CTC-based Word Spotting
作者: Kai-Chen Tsai, Tien-Hong Lo, Yun-Ting Sun, Berlin Chen
链接: https://arxiv.org/abs/2605.18222v1
完整摘要: Contextual biasing is essential to improving the recognition of rare and domain-specific words in an automatic speech recognition (ASR) system. While numerous methods have been proposed in recent years, most of them focus on offline settings and do not explicitly address the challenges of streaming ASR. For example, CTC-based word spotting (CTC-WS) have demonstrated strong performance by directly detecting keywords from CTC log-probabilities, but they are limited to offline processing and require access to the full utterance. In This work, we present a streaming extension of CTC-WS for real-time contextual biasing. Our method maintains active keyword paths across audio chunks using a stateful token passing algorithm, enabling the detection of keywords that span multiple chunks. To ensure low latency and stable output, we introduce an incremental commitment mechanism that only emits segments guaranteed not to be affected by future audio, while deferring uncertain regions. This method naturally integrates with streaming ASR pipelines and does not require modifications to the underlying acoustic model or additional training, making it practical for real-world deployment. Experimental results show that our method reduces overall WER and effectively improves keyword F-score, demonstrating its effectiveness for real-time ASR applications.
匹配关键词: tool use
---

[ACADEMIC - ARXIV]
标题: SIREM: Speech-Informed MRI Reconstruction with Learned Sampling
作者: Md Hasan, Nyvenn Castro, Daiqi Liu, Lukas Mulzer, Jana Hutter, Jonghye Woo, Moritz Zaiss, Andreas Maier, Paula A. Perez-Toro
链接: https://arxiv.org/abs/2605.18221v1
完整摘要: Real-time magnetic resonance imaging (rtMRI) of speech production enables non-invasive visualization of dynamic vocal-tract motion and is valuable for speech science and clinical assessment. However, rtMRI is fundamentally constrained by trade-offs among spatial resolution, temporal resolution, and acquisition speed, often leading to undersampled k-space measurements and degraded reconstructions. We propose SIREM, a speech-informed MRI reconstruction framework that uses synchronized speech as a cross-modal prior. The central idea is that vocal-tract configurations during speech are correlated with the produced acoustics, making part of the image content predictable from audio. SIREM models each frame as a fusion of an audio-driven component and an MRI-driven component through a spatial weighting map. The audio branch predicts articulator-related structure from speech, while the MRI branch reconstructs complementary content from measured k-space data. We further introduce a learnable soft weighting profile over spiral arms, enabling a differentiable study of how k-space arm usage interacts with speech-informed fusion. This yields a unified multimodal formulation that combines audio-driven prediction, MRI reconstruction, and sampling adaptation. We evaluate SIREM on the USC speech rtMRI benchmark against standard baselines, including gridding, wavelet-based compressed sensing, and total variation. SIREM introduces a speech-informed reconstruction paradigm that operates in a substantially higher-throughput regime than iterative methods while preserving anatomically plausible vocal-tract structure. These results establish an initial benchmark for multimodal speech-informed rtMRI reconstruction and highlight the potential of synchronized speech as an auxiliary prior for fast reconstruction. The source code is available at https://github.com/mdhasanai/SIREM
匹配关键词: tool use
---

[ACADEMIC - ARXIV]
标题: EgoInteract: Synthetic Egocentric Videos Generation for Interaction Understanding and Anticipation
作者: Rosario Leonardi, Francesco Ragusa, Daniele Materia, Alessandro Passanisi, James Fort, Jakob Engel, Giovanni Maria Farinella
链接: https://arxiv.org/abs/2605.18214v1
完整摘要: Collecting large-scale egocentric video datasets with dense spatial and temporal annotations is costly, slow, and often constrained by environmental biases, privacy constraints, and limited coverage of interaction patterns. While synthetic data has shown strong potential in several vision domains, its use for egocentric perception remains relatively underexplored, especially for tasks requiring temporally coherent human-object interactions. In this work, we introduce EgoInteract, a controllable simulator for egocentric video generation designed to model fine-grained egocentric interactions and their temporal dynamics. The simulator enables precise control over camera, human body and hand motion, object manipulation, and scene composition across diverse environments. Building on this framework, we generate a synthetic egocentric video dataset with dense spatial and temporal annotations for temporal action segmentation, next-active object detection, interaction anticipation, and hand-object interaction detection. We evaluate models trained with simulated data on multiple real-world egocentric benchmarks spanning diverse environments, object categories, and interaction patterns. Results show consistent improvements over strong baselines across tasks and datasets, demonstrating the effectiveness and transferability of our simulation-based approach.
匹配关键词: tool use
---

[ACADEMIC - ARXIV]
标题: RGB-only Active 3D Scene Graph Generation for Indoor Mobile Robots
作者: Giorgia Modi, Davide Buoso, Giuseppe Averta, Daniele De Martini
链接: https://arxiv.org/abs/2605.18197v1
完整摘要: Current approaches to 3D scene graph generation rely on dedicated depth sensors, such as LiDAR or RGB-D cameras, for metric 3D reconstruction. This limits deployment to specialized robotic platforms and excludes settings where only RGB cameras are available, such as fixed external infrastructure. Existing pipelines also typically operate on passively collected observation trajectories, rather than selecting viewpoints based on the partially built scene representation, and therefore fail to effectively exploit the semantic and spatial information encoded within the graph during exploration. This paper presents a fully visual framework for the active, incremental construction of 3D scene graphs from RGB input only, addressing both limitations. The proposed approach unifies perception and planning around a shared structured representation that captures object semantics, 3D geometry, relational context, and information from multiple viewpoints. Because the framework is hardware-agnostic and relies only on RGB observations, it can incorporate inputs from both onboard robot cameras and fixed external cameras within the same representation. Experiments on the Replica dataset show that the RGB-only pipeline achieves F1-score parity with baselines using ground-truth depth. Active exploration experiments on ReplicaCAD further show that semantic-driven viewpoint selection detects more than twice as many objects as a geometric frontier-based baseline under the same exploration budget. Finally, the external-camera setting demonstrates that complementary RGB views can effectively bootstrap the scene graph and improve contextual understanding at no additional exploration cost.
匹配关键词: planning
---

[ACADEMIC - ARXIV]
标题: Fixed External Cameras as Common Prior Maps for Active 3D Scene Graph Generation
作者: Giorgia Modi, Davide Buoso, Giuseppe Averta, Daniele De Martini
链接: https://arxiv.org/abs/2605.18184v1
完整摘要: Commonly available prior information, such as BIM models, floor plans, and remote sensing images, can provide valuable geometric and semantic context for autonomous robotic systems. In this paper, we treat observations from fixed external RGB cameras as Common Prior Maps (CPMs): wide-field views of the environment that initialize a semantic and geometric scene prior before any robot motion begins. We present an RGB-only framework for active, incremental 3D scene graph (3DSG) generation that seamlessly fuses observations from both onboard robot cameras and fixed external cameras within a single hardware-agnostic pipeline. By relying solely on RGB observations processed by a feed-forward 3D reconstruction model, the system treats all cameras - onboard or external - identically, requiring no hardware modifications. A graph-based active semantic exploration framework then directly leverages the partial scene graph to guide the robot toward regions of high semantic uncertainty, progressively completing and refining the prior. Experiments demonstrate that bootstrapping the scene graph with even a single external camera increases initial object recall by up to +79%, and that the richer context of the prior significantly improves the efficiency of subsequent active exploration.
匹配关键词: planning
---

[ACADEMIC - ARXIV]
标题: SENSE: Satellite-based ENergy Synthesis for Sustainable Environment
作者: Kailai Sun, Mingyi He, Heye Huang, Can Rong, Alok Prakash, Baoshen Guo, Shenhao Wang, Jinhua Zhao
链接: https://arxiv.org/abs/2605.18101v1
完整摘要: Urban Building Energy Modeling plays a critical role in achieving the United Nations' Sustainable Development Goals 7 and 11. Although existing studies based on satellite imagery and deep learning have achieved remarkable progress, many challenges exist: most existing studies are inherently predictive, failing to reflect the generative nature of urban planning; although generative AI and diffusion models have seen explosive growth in satellite imagery, they lack the urban functional generation (e.g., energy layer); third, aligned high-quality high-resolution building energy data with satellite imagery is limited and scarce. Here we propose SENSE (Satellite-based ENergy Synthesis for Sustainable Environment), a unified generative UBEM framework that jointly synthesizes realistic urban satellite imagery and aligned high-quality building energy consumption and height maps. By conditioning on road networks and urban density metrics, SENSE, based on a controllable diffusion model, leverages the knowledge learned by large vision models to generate urban building energy consumption and height information (annotations) in the latent space. Experiments across four cities (New York City, Boston, Lyon, Busan) demonstrate that SENSE achieves high visual fidelity and strong physical consistency, satisfying the ASHRAE standard metric. Experiments demonstrate that SENSE can generate enough annotated synthetic data using less than 20% labeled energy data, boosting downstream prediction performance by 10% IoU. Compared to SOTA urban energy prediction methods, SENSE significantly reduced prediction error (reduced 3%-11% NMBE and 1%-9% CVRMSE). This study offers an energy-efficiency urban planning and physical generation solution for urban science, energy science and building science. The dataset and code: https://huggingface.co/datasets/skl24/MUSE and https://github.com/kailaisun/GenAI4Urban-Energy/.
匹配关键词: planning
---

[ACADEMIC - ARXIV]
标题: 4DLidarOpen: An Open 4D FMCW Lidar Dataset for Motion-Aware Autonomous Driving
作者: Kane Qian, Xin Zhao, Yining Shi, Rujun Yan, Zhengqing Pan, Kaojin Zhu, Mengmeng Yang, Kai Sun, Diange Yang, Kun Jiang
链接: https://arxiv.org/abs/2605.18074v1
完整摘要: We present 4DLidarOpen, a large-scale open multi-modal dataset for autonomous driving, centered on 4D frequency-modulated continuous-wave (FMCW) Lidar sensing. Unlike conventional time-of-flight Lidar datasets that mainly provide geometric measurements, 4DLidarOpen includes point-wise radial velocity measurements from a forward-facing 4D FMCW Lidar, together with multiple Lidars of different types, including rotating, solid-state, and blind-spot variants, surround-view cameras, and 6-DOF ego-vehicle poses. The dataset was collected in complex urban environments in Beijing and covers dense pedestrian interactions, congested traffic, high-speed driving, and unprotected maneuvers. 4DLidarOpen provides synchronized multi-sensor data and 3D bounding-box annotations with persistent track IDs across five object categories. A hybrid annotation strategy is adopted, where large-scale auto-labeled data support scalable training and human experts refine annotations for the human-annotated training and validation sets. Based on this dataset, we establish benchmarks for 3D object detection, birds-eye view (BEV) segmentation and flow prediction, and motion forecasting with planning. Extensive experiments show that direct velocity measurements from 4D FMCW Lidar provide complementary motion cues for dynamic-scene understanding. Compared with geometric-only sensing, the velocity-aware representation improves motion-related perception and downstream forecasting and planning, especially in scenarios involving vulnerable road users and fast-moving objects. These results indicate that 4D FMCW Lidar is a promising sensing modality for motion-aware autonomous driving. The dataset and evaluation toolkit are publicly released to support research on 4D scene understanding, multi-Lidar fusion, and velocity-aware perception and planning.
匹配关键词: planning
---

[ACADEMIC - ARXIV]
标题: Bench2Drive-Robust: Benchmarking Closed-Loop Autonomous Driving under Deployment Perturbations
作者: Zhiyuan Zhang, Zhenghao Jin, Yanlun Peng, Xianda Guo, Haoran Liu, Shaofeng Zhang, Xingjun Ma, Zuxuan Wu, Junchi Yan, Xiaosong Jia, Yu-Gang Jiang
链接: https://arxiv.org/abs/2605.18059v1
完整摘要: Robustness is a critical requirement for deploying autonomous driving systems in the real world. Existing robustness benchmarks for autonomous driving have made important progress in studying the effects of image-level corruptions, such as adverse weather or camera degradation, on perception modules and open-loop planning outputs. However, deployment can also involve system-level imperfections, such as inference latency and ego-state estimation errors, which remain less studied in closed-loop E2E-AD evaluation. These imperfections can accumulate through the feedback loop and destabilize control. In this work, we present Bench2Drive-Robust, to our knowledge the first device-centric robustness benchmark for closed-loop end-to-end autonomous driving under realistic deployment perturbations. We systematically evaluate deployment-oriented perturbations arising from three major sources: camera-stream failures (frame drop, partial observation), ego-state estimation errors (GPS noise, and speed or odometry errors), and compute-induced control delay (model inference delay). We evaluate representative end-to-end driving methods and analyze their robustness under different perturbation severities. Our results show that these deployment-related perturbations can substantially degrade closed-loop driving performance, revealing robustness challenges that are not fully captured by conventional image-level corruption evaluations. By establishing a closed-loop evaluation protocol and demonstrating the substantial impact of these deployment-oriented perturbations, Bench2Drive-Robust defines practical robustness problems for end-to-end autonomous driving and encourages further research on deployment-aware robust driving systems.
匹配关键词: planning
---

[ACADEMIC - ARXIV]
标题: Transitivity Meets Cyclicity: Explicit Preference Decomposition for Dynamic Large Language Model Alignment
作者: Yucong Huang, Xiucheng Li, Kaiqi Zhao, Jing Li
链接: https://arxiv.org/abs/2605.17342v1
完整摘要: Standard RLHF relies on transitive scalar rewards, failing to capture the cyclic nature of human preferences. While some approaches like the General Preference Model (GPM) address this, we identify a theoretical limitation: their implicit formulation entangles hierarchy with cyclicity, failing to guarantee dominant solutions. To address this, we propose the Hybrid Reward-Cyclic (HRC) model, which utilizes game-theoretic decomposition to explicitly disentangle preferences into orthogonal transitive (scalar) and cyclic (vector) components. Complementing this, we introduce Dynamic Self-Play Preference Optimization (DSPPO), which treats alignment as a time-varying game to progressively guide the policy toward the Nash equilibrium. Synthetic data experiments further validate HRC's structural superiority in mixed transitive--cyclic settings, where HRC converges faster and achieves higher accuracy than GPM. Experiments on RewardBench 2 demonstrate that HRC consistently improves over both BT and GPM baselines (e.g., +1.23% on Gemma-2B-it). In particular, its superior performance in the Ties domain empirically validates the model's robustness in handling complex, non-strict preferences. Extensive downstream evaluations on AlpacaEval 2.0, Arena-Hard-v0.1, and MT-Bench confirm the efficacy of our framework. Notably, when using Gemma-2B-it as the base preference model, HRC+DSPPO achieves a peak length-controlled win-rate of 44.75% on AlpacaEval 2.0 and 46.8% on Arena-Hard-v0.1, significantly outperforming SPPO baselines trained with BT or GPM. Our code is publicly available at https://github.com/lab-klc/Hybrid-Reward-Cyclic.
匹配关键词: RLHF
---

[ACADEMIC - ARXIV]
标题: GRLO: Towards Generalizable Reinforcement Learning in Open-Ended Environments from Zero
作者: Shangjian Yin, Yu Fu, Yue Dong, Zhouxing Shi
链接: https://arxiv.org/abs/2605.15464v1
完整摘要: Post-training has become a crucial step for unlocking the capabilities of large language models, with reinforcement learning (RL) emerging as a critical paradigm. Recent RL-based post-training has increasingly split into two paradigms: reinforcement learning from human feedback (RLHF), which optimizes models using human preference signals in target domains, and reinforcement learning from verifiable rewards (RLVR), which operates in verifier-backed environments. The latter has dominated recent reasoning-oriented post-training because it delivers stronger gains and higher efficiency on domain-specific tasks (e.g., reasoning). However, although in-domain RL training achieves promising performance, it still requires a substantial amount of GPU compute, which remains a major barrier to broad adoption. In this work, we study the generalization ability of RLHF learned from scratch from a small set of interactions in open-ended environments, and investigate whether the conversational abilities it explicitly acquires can implicitly transfer to downstream tasks such as mathematical reasoning and code generation, namely GRLO. Specifically, on Qwen3-4B-Base backbone, GRLO improves the average performance across all domains from 24.1 to 63.1 with only 5K prompts and 22.7 GPU hours, requiring about $46\times$ less data and $68\times$ less compute than a strong in-domain RLVR baseline. The resulting model is even competitive with Qwen's released post-trained models which required a much larger training cost. Notably, a subsequent in-domain RLVR stage brings only selective gains, mainly on harder competition-math benchmarks. We hope GRLO offers a simple and efficient recipe for building broadly capable post-trained models. Our code and data will be available at: \href{https://github.com/SJY8460/GRLO}{https://github.com/SJY8460/GRLO}.
匹配关键词: RLHF
---

[ACADEMIC - ARXIV]
标题: From Sycophantic Consensus to Pluralistic Repair: Why AI Alignment Must Surface Disagreement
作者: Varad Vishwarupe, Nigel Shadbolt, Marina Jirotka
链接: https://arxiv.org/abs/2605.14912v1
完整摘要: Pluralistic alignment is typically operationalised as preference aggregation: producing responses that span (Overton), steer toward (Steerable), or proportionally represent (Distributional) diverse human values. We argue that aggregation alone is an incomplete primitive for deployed pluralistic alignment. Under genuine value pluralism, the failure mode of contemporary RLHF-trained assistants is not insufficient coverage but sycophantic consensus: a learned tendency to agree with, validate, and minimise friction with the immediate interlocutor. Because deployed AI systems now mediate consequential deliberation across health, civic life, labour, and governance, the collapse of disagreement at the interaction layer is not a narrow technical concern but a structural failure with distributive consequences. We reframe pluralistic alignment around three conversational mechanisms drawn from Grice's maxims: scoping (acknowledging the limits of one's perspective), signalling (surfacing value-conflict rather than smoothing it over), and repair (revising one's position on principled grounds, not on user pressure). We formalise a metric, the Pluralistic Repair Score (PRS), distinguishing principled revision from capitulation, and present a small-scale empirical illustration on two frontier RLHF-trained models (Claude Sonnet 4.5, N=198; GPT-4o, N=100) showing that, for both, agreement-following coexists with low repair-quality on contested-value prompts. PRS measures an interactional precondition for pluralism (visible disagreement; principled revision) rather than pluralism in full; we discuss the difference, take seriously the reflexive question of whose "principled" counts, and argue that pluralism is most decisively made or unmade at the deployment-governance layer: interfaces, preference-data pipelines, and audit infrastructure.
匹配关键词: RLHF
---

[ACADEMIC - ARXIV]
标题: Not Just RLHF: Why Alignment Alone Won't Fix Multi-Agent Sycophancy
作者: Adarsh Kumarappan, Ananya Mujoo
链接: https://arxiv.org/abs/2605.12991v2
完整摘要: LLM-based multi-agent pipelines flip from correct to incorrect answers under simulated peer disagreement at rates we term yield, a vulnerability widely attributed to RLHF-induced sycophancy. We test this attribution across four model families and find it largely wrong: pretrained base models exhibit the same substitution pattern as their Instruct variants, averaging higher yield than Instruct. Using activation patching, we localize the corruption to a narrow mid-layer window where attention carries the causal weight and MLP contribution is negligible; patching above this window restores 96% of the clean-to-pressured P(correct) gap. The attack surface decomposes into two independent factors (channel framing and consensus strength) whose interaction produces a 47.5 percentage-point yield gap at majority consensus, preserved across jury sizes $N \in \{4, 5, 6\}$. Two converging activation-space interventions show that pressure suppresses clean-reasoning features rather than activating a new sycophancy circuit. A single correctly-arguing dissenter reduces yield by 54-73 percentage points across all framings tested, whereas the strongest prompt-level defense fails on attack variants outside its design surface. Mitigations should target the mechanism, structured dissent at the pipeline level, rather than prompt-level defenses.
匹配关键词: RLHF
---

[ACADEMIC - ARXIV]
标题: Semantic Reward Collapse and the Preservation of Epistemic Integrity in Adaptive AI Systems
作者: William Parris
链接: https://arxiv.org/abs/2605.12406v1
完整摘要: Recent advances in reinforcement learning from human feedback (RLHF) and preference optimization have substantially improved the usability, coherence, and safety of large language models. However, recurring behaviors such as performative certainty, hallucinated continuity, calibration drift, sycophancy, and suppression of visible uncertainty suggest unresolved structural issues within scalarized preference optimization systems. We propose Semantic Reward Collapse (SRC): the compression of semantically distinct forms of evaluative dissatisfaction into generalized optimization signals. Under SRC, categories such as factual incorrectness, uncertainty disclosure, formatting dissatisfaction, latency, and social preference may become entangled within a shared reward topology despite representing fundamentally different epistemic classes. We argue that adaptive reasoning systems operating under generalized evaluative pressure may drift toward suppression of visible epistemic failure rather than preservation of calibrated uncertainty integrity. These behaviors are framed strictly as optimization consequences rather than evidence of deception or anthropomorphic agency. Drawing on institutional proxy collapse, metric gaming, software reliability engineering, and human learning theory, we propose that uncertainty disclosure and escalation behavior should be treated as protected epistemic conduct rather than globally penalized task incompletion. Finally, we introduce Constitutional Reward Stratification (CRS), a domain-aware reward framework intended to preserve differentiated epistemic attribution within adaptive learning systems. We present CRS not as a validated solution, but as a testable governance-oriented research direction requiring further empirical investigation.
匹配关键词: RLHF
---

[ACADEMIC - ARXIV]
标题: Evaluation Drift in LLM Personality Induction: Are We Moving the Goalpost?
作者: Prateek Rajput, Yewei Song, Iyiola E. Olatunji, Jacques Klein, Tegawendé F. Bissyandé
链接: https://arxiv.org/abs/2605.16996v1
完整摘要: Can large language models reliably express a human-like personality, or are they merely mimicking surface cues without a stable underlying profile? To investigate this, we induce personality in LLMs by fine-tuning them on the long-form essays, where each essay is associated with a target Big Five personality profile. We then evaluate the stability and fidelity of the induced personality using the IPIP-NEO questionnaire. Specifically, we ask: (i) does post-training (SFT, DPO, ORPO) stabilize questionnaire scores under prompt rephrasings, and (ii) can it induce target Big Five profiles from unguided essays? Our results demonstrate that fine-tuning consistently reduces variance in questionnaire responses across five models, directly mitigating the evaluation fragility reported in pre-trained models. However, this newfound stability reveals a more fundamental limitation: accuracy on the full five-dimensional profile remains near chance, even when single-trait scores improve. This indicates that unguided essays lack the cues needed for faithful personality expression. We therefore argue for scenario-grounded datasets or interactive elicitation that accumulates test-aligned evidence over time.
匹配关键词: DPO
---

[ACADEMIC - ARXIV]
标题: Learning How to Cube
作者: Ferhat Erata, Sam Kouteili, Thanos Typaldos, Timos Antonopoulos, Robert B. Jones, Byron Cook, Ruzica Piskac
链接: https://arxiv.org/abs/2605.16632v1
完整摘要: Despite the effectiveness of Cube-and-Conquer (C&C) for solving challenging Boolean Satisfiability (SAT) problems, no prior work has shown that transformer-based models can learn effective cubing heuristics. We introduce a neuro-symbolic post-training framework for this task. We design an MCTS-based data curation pipeline that uses symbolic heuristics to explore splitting decisions over SAT competition formulas, producing preference data grounded in solver statistics and augmented with reasoning traces from a teacher model. Our two-stage post-training, supervised fine-tuning (SFT) followed by direct preference optimization (DPO), enables a 4B-parameter model to achieve a pass@5 score of 53 on 100 SAT competition benchmarks, surpassing frontier LLMs such as Claude-Sonnet-4 (50) and matching the best symbolic heuristic (53). Ablations show that SFT alone improves pass@5 from 46 to 51, with DPO adding 2 additional benchmarks; an entropy/agreement ablation on realized first-cube decisions further shows that SFT, not DPO, accounts for the root-level decision diversity that produces complementary per-run coverage over deterministic symbolic methods. This demonstrates that transformers can be trained to make effective cubing decisions in a domain traditionally dominated by symbolic methods.
匹配关键词: DPO
---

[ACADEMIC - ARXIV]
标题: R2V Agent: Teaching SLMs When to Ask for Help
作者: Raghu Vamshi Hemadri, Humaira Firdowse Mohammed, Rishabh Maheshwary, Srivatsava Daruru, Sagar Davasam, Vikas Yadav, Srinivas Sunkara, Sai Rajeswar
链接: https://arxiv.org/abs/2605.16604v1
完整摘要: Efficient agentic systems should incur expensive frontier-model costs only on decisions where a cheaper local model is likely to fail. Existing LLM cascades usually route whole queries before execution, but task difficulty shifts mid-trajectory - after flaky tool calls, truncated observations, or compounding local errors - making pre-execution routing brittle. We introduce \textbf{R2V-Agent}, a risk-calibrated SLM-LLM routing framework for interactive agents. R2V combines four components: a distilled small language model (SLM) policy, a stronger teacher LLM, a lightweight process verifier that scores candidate actions at each step, and a calibrated step-level router. The router is our central contribution: after the SLM is trained, it estimates residual failure risk at each step and escalates only when teacher intervention is warranted. To make the routing problem well-defined, we first train a stable local SLM using a standard offline pipeline: behavioral cloning (BC) on teacher trajectories, followed by verifier-guided Direct Preference Optimization (DPO) with consistency regularization. The router is then trained on this fixed policy's residual failures using Brier-calibrated probability estimation and a Conditional Value-at-Risk (CVaR)-constrained objective that penalizes worst-case failures across perturbation seeds. Across HumanEval+, TextWorld, and TerminalBench with four SLM backbones, R2V improves the reliability-cost frontier: it achieves $94.3\%$ HumanEval+ success with $0.60\%$ LLM escalation, recovers TextWorld from $64.6\%$ SLM-only success to $98.2\%$ at $41.7\%$ escalation, and reaches $93.3\%$ TerminalBench success at $33.9\%$ LLM calls, roughly half the heuristic-router cost.
匹配关键词: DPO
---

[ACADEMIC - ARXIV]
标题: SeamCam: Quantifying Seamless Camouflage via Multi-Cue Visual Detectability
作者: Amin Karimi Monsefi, Abolfazl Meyarian, Mridul Khurana, Shuheng Wang, Pouyan Navard, Cheng Zhang, Anuj Karpatne, Wei-Lun Chao, Rajiv Ramnath
链接: https://arxiv.org/abs/2605.16515v1
完整摘要: Animals are described as effectively camouflaged when they blend seamlessly with their surrounding, yet no standardized quantitative measure of this seamlessness exists. We address this gap by framing camouflage evaluation as a visual localization problem: a well-camouflaged animal is one that remains difficult to detect even when its category is known. We introduce SeamCam (Seamless Camouflage), a metric that quantifies how detectable an animal is from the available visual evidence. Given an image and a target species, SeamCam generates category-conditioned detection proposals, extracts segmentation masks, and identifies the subset whose collective union yields the highest IoU with the ground-truth mask. The SeamCam score is one minus this maximum recoverable localization signal, where a higher score indicates stronger camouflage (i.e., lower detectability). In a human two-alternative forced-choice study with 94 participants and 2,390 comparisons, SeamCam achieves 78.82% agreement with human camouflage difficulty judgments, outperforming state-of-the-art by about 25%. We then demonstrate SeamCam's utility as a preference signal for Direct Preference Optimization (DPO) to fine-tune a diffusion-based inpainting model for camouflage generation. This offers an affordable training approach with an objective explicitly suited for camouflage generation, unlike typical diffusion models. To support rigorous benchmarking, we further introduce CamFG-1.5k, a curated dataset of 1,521 high-resolution images in which animals are fully visible prior to camouflage generation, enabling unbiased evaluation by controlling for occlusion artifacts present in existing datasets. https://7amin.github.io/SeamCam/
匹配关键词: DPO
---

[ACADEMIC - ARXIV]
标题: Hierarchical Image Tokenization for Multi-Scale Image Super Resolution
作者: Isma Hadji, Enrique Sanchez, Adrian Bulat, Brais Martinez, Georgios Tzimiropoulos
链接: https://arxiv.org/abs/2605.14891v1
完整摘要: We introduce a multi-scale Image Super Resolution (ISR) method building on recent advances in Visual Auto-Regressive (VAR) modeling. VAR models break image tokenization into additive, gradually increasing scales, using Residual Quantization (RQ), an approach that aligns perfectly with our target ISR task. Previous works taking advantage of this synergy suffer from two main shortcomings. First, due to the limitations in RQ, they only generate images at a predefined fixed scale, failing to map intermediate outputs to the corresponding image scales. They also rely on large backbones or a large corpus of annotated data to achieve better performance. To address both shortcomings, we introduce two novel components to the VAR training for ISR, aiming at increasing its flexibility and reducing its complexity. In particular, we introduce a) a \textbf{Hierarchical Image Tokenization (HIT)} approach that progressively represents images at different scales while enforcing token overlap across scales, and b) a \textbf{Direct Preference Optimization (DPO) regularization term} that, relying solely on the (LR,HR) pair, encourages the transformer to produce the latter over the former. Our proposed HIT acts as a strong inductive bias for the VAR training, resulting in a small model (300M params vs 1B params of VARSR), that achieves state-of-the-art results without external training data, and that delivers multi-scale outputs with a single forward pass.
匹配关键词: DPO
---

[ACADEMIC - ARXIV]
标题: A Simplex Witness Certificate for Constant Collapse in Variational Autoencoders
作者: Zegu Zhang, Jianhua Peng, Jian Zhang
链接: https://arxiv.org/abs/2605.18224v1
完整摘要: This note studies exact constant collapse in variational autoencoders, where the encoder mean becomes independent of the input. The goal is to make this specific failure mode pre-designable, monitorable during training, and certifiable after training. The prior is kept as the standard Gaussian. Given a fixed teacher posterior, we attach to the latent mean a fixed simplex witness head. The resulting teacher-student alignment loss has an exact constant-predictor baseline equal to the teacher information. If the alignment loss is below this baseline, the latent mean cannot be input-independent constant collapsed. The simplex witness also has a closed-form inverse. Any full-support teacher posterior can be represented by embedding its centered log-odds into the latent space. This gives an explicit latent energy cost and explains when the alignment loss can be made small. A computable view gap handles the case where teacher targets are computed from a different view. Thus exact constant collapse is converted from an after-the-fact training pathology into a design-and-certificate problem.
匹配关键词: alignment
---

[ACADEMIC - ARXIV]
标题: View-Aware Semantic Alignment for Aerial-Ground Person Re-Identification
作者: Quan Zhang, Zeqiang Cai, Peiming Zhao, Jingze Wu, Cailun Wu, Hongbo Chen, Jianhuang Lai
链接: https://arxiv.org/abs/2605.18192v1
完整摘要: Aerial-Ground Person Re-Identification (AGPReID) remains highly challenging due to drastic viewpoint variations between drones and fixed cameras. Existing methods typically follow a view-invariant paradigm, aligning shared features across views to achieve robustness. However, view-invariant inherently enforces part-level alignment, which ignores view-specific cues and discriminative identity information. To this end, this work proposes ViSA (View-aware Semantic Alignment), a view-aware framework that achieves cross-view semantic consistency containing an Expert-driven Token Generation Module (ETGM) and a Dual-branch Local Fusion Module (DLFM). Technically, the former constructs a set of view-aware experts to generate adaptive semantic queries that perceive viewpoint-specific patterns, while the latter leverages graph reasoning to extract and align local regions responsive to different experts. Extensive experiments on three AGPReID benchmarks including AG-ReID.v2, CARGO and LAGPeR demonstrate that ViSA consistently achieves superior performance, with a notable 10.06\% mAP improvement on the challenging CARGO cross-view protocol. The code is available at \href{https://github.com/Cat-Zero/ViSA}{https://github.com/Cat-Zero/ViSA}.
匹配关键词: alignment
---

[ACADEMIC - ARXIV]
标题: Pairwise Preference Reward and Group-Based Diversity Enhancement for Superior Open-Ended Generation
作者: Guining Cao, Jiaxin Peng, Chu Zeng, Yu Zhao, Shuangyong Song, Yongxiang
链接: https://arxiv.org/abs/2605.18191v1
完整摘要: Current reinforcement learning(RL) methods are broadly applicable and powerful in verifiable settings where scalar rewards can be provided. However, in open-ended generation tasks, verifying the correctness of responses remains challenging, and training reward models incurs substantial computational and annotation costs. Moreover, reinforcement learning (RLVR) often leads to diversity collapse and produces stereotypical or rigid outputs, outcomes that are particularly undesirable in open-domain scenarios. We propose Pairwise Preference Reward and Group-based Diversity Enhancement (PPR-GDE), a RL method that is more suitable for open-ended generation. PPR-GDE does not require scalar rewards and incorporates group-level diversity into the reward signal, it preserves the comparative structure of subjective evaluation through a pairwise preference reward, mitigates judge position bias via repeated comparisons with swapped response order, and introduces a group-based diversity reward that explicitly encourages semantic dispersion within a response group, all of these reward signals are integrated into a unified group-relative policy optimization objective. We instantiate PPR-GDE on role-playing task, experiments show that PPR-GDE achieves a better alignment quality as well as expressive diversity than strong RL baselines. Further analysis shows that pairwise preference is critical for preference alignment in subjective perspective, while the diversity metric plays an essential role in achieving superior expressive diversity and broader semantic coverage.
匹配关键词: alignment
---

[ACADEMIC - ARXIV]
标题: Visualizing the Invisible: Generative Visual Grounding Empowers Universal EEG Understanding in MLLMs
作者: Junyu Pan, Yansen Wang, Enze Zhang, Baoliang Lu, Weilong Zheng, Dongsheng Li
链接: https://arxiv.org/abs/2605.18172v1
完整摘要: Leveraging the universal representations of pre-trained LLMs and MLLMs offers a promising path toward brain foundation models. However, visually-evoked EEG datasets remain scarce, leading existing methods to align neural signals mainly with abstract text, a lossy translation that may discard fine-grained perceptual information encoded in brain activity. We propose Generative Visual Grounding (GVG), a framework that visualizes the invisible by using an EEG-to-image generative model as a visual translator. Instead of forcing EEG into text alone, GVG hallucinates instance-specific proxy images for non-visual EEG, providing structured visual contexts that allow MLLMs to exploit their visual priors for clinical-state interpretation. We validate this idea on two MLLM backbones, GVG-X-Omni and GVG-Janus. Image-only alignment is already competitive: the lightweight GVG-X-Omni matches 1.7B-parameter text-aligned baselines while tuning only 170M parameters on a frozen 7B backbone. We further extend GVG-Janus with trimodal Image+Text alignment, where text supplies categorical semantic anchors and visual proxies enrich neural representations with perceptual details. Experiments show consistent gains in EEG understanding and visual generation, suggesting visual proxy grounding as an effective complement to textual alignment.
匹配关键词: alignment
---

[ACADEMIC - ARXIV]
标题: Self-Evolving Spatial Reasoning in Vision Language Models via Geometric Logic Consistency
作者: Junming Liu, Yuqi Li, Yifei Sun, Maonan Wang, Piotr Koniusz, Yirong Chen, Ding Wang
链接: https://arxiv.org/abs/2605.18162v1
完整摘要: Vision-Language Models (VLMs) have made striking progress, yet their spatial reasoning remains fragile: models that answer an original input correctly can still fail under paired transformations with predictable answer mappings, revealing a gap between instance-level correctness and robust spatial reasoning. To address this, we propose Spatial Alignment via Geometric Evolution (SAGE), a self-evolving framework that enforces logical consistency in VLMs through geometric and linguistic duality operations. SAGE incorporates duality consistency as an auxiliary reward within GRPO training, encouraging models to produce logically coherent answers across original and transformed inputs. A dynamic operation pool continuously probes for inconsistencies, promoting challenging operations and retiring mastered ones, so that training focuses on the most informative signals. SAGE is model-agnostic, data-efficient compared to prior GRPO methods, and can be applied as a lightweight post-training stage to any existing VLM. Experiments on video and spatial reasoning benchmarks demonstrate consistent improvements over strong baselines and enhanced generalization to unseen data.
匹配关键词: alignment
---

[ACADEMIC - ARXIV]
标题: Are Sparse Autoencoder Benchmarks Reliable?
作者: David Chanin
链接: https://arxiv.org/abs/2605.18229v1
完整摘要: Sparse autoencoders (SAEs) are a core interpretability tool for large language models, and progress on SAE architectures depends on benchmarks that reliably distinguish better SAEs from worse ones. We audit the SAE quality metrics in SAEBench, the de-facto standard SAE evaluation suite, through three complementary lenses: reseed noise on a fixed SAE, ground-truth correlation on synthetic SAEs, and discriminability across training trajectories. We find that two of these metrics, Targeted Probe Perturbation (TPP) and Spurious Correlation Removal (SCR), fail multiple lenses at their canonical settings and should not be used to evaluate SAEs. The other metrics show higher reseed noise and lower discriminability than the field assumes. The sae-probes variant of $k$-sparse probing is the most reliable metric we tested, but even sae-probes struggles to separate variants of the same SAE architecture. Our results show the field needs better SAE benchmarks.
匹配关键词: preference learning
---

[ACADEMIC - ARXIV]
标题: Context Memorization for Efficient Long Context Generation
作者: Yasuyuki Okoshi, Hao Mark Chen, Guanxi Lu, Hongxiang Fan, Masato Motomura, Daichi Fujiki
链接: https://arxiv.org/abs/2605.18226v1
完整摘要: Modern large language model (LLM) applications increasingly rely on long conditioning prefixes to control model behavior at inference time. While prefix-augmented inference is effective, it incurs two structural limitations: i) the prefix's influence fades as generation proceeds, and ii) attention computation over the prefix scales linearly with its length. Existing approaches either keep the prefix in attention while compressing it, or internalize it into model parameters through gradient-based training. The former still attends to the prefix at inference, while the latter is training-intensive and ill-suited to prefix updates. To address these issues, we propose attention-state memory, a training-free approach that externalizes the prefix into a lightweight, lookup-based memory of precomputed attention states between prefix and query tokens. On ManyICLBench with LLaMA-3.1-8B, our method improves accuracy over in-context learning at 1K-8K memory budgets while reducing attention latency by 1.36x at 8K, and surpasses full-attention RAG performance on NBA benchmark using only 20% of its memory footprint.
匹配关键词: preference learning
---

[ACADEMIC - ARXIV]
标题: A Simplex Witness Certificate for Constant Collapse in Variational Autoencoders
作者: Zegu Zhang, Jianhua Peng, Jian Zhang
链接: https://arxiv.org/abs/2605.18224v1
完整摘要: This note studies exact constant collapse in variational autoencoders, where the encoder mean becomes independent of the input. The goal is to make this specific failure mode pre-designable, monitorable during training, and certifiable after training. The prior is kept as the standard Gaussian. Given a fixed teacher posterior, we attach to the latent mean a fixed simplex witness head. The resulting teacher-student alignment loss has an exact constant-predictor baseline equal to the teacher information. If the alignment loss is below this baseline, the latent mean cannot be input-independent constant collapsed. The simplex witness also has a closed-form inverse. Any full-support teacher posterior can be represented by embedding its centered log-odds into the latent space. This gives an explicit latent energy cost and explains when the alignment loss can be made small. A computable view gap handles the case where teacher targets are computed from a different view. Thus exact constant collapse is converted from an after-the-fact training pathology into a design-and-certificate problem.
匹配关键词: preference learning
---

[ACADEMIC - ARXIV]
标题: SIREM: Speech-Informed MRI Reconstruction with Learned Sampling
作者: Md Hasan, Nyvenn Castro, Daiqi Liu, Lukas Mulzer, Jana Hutter, Jonghye Woo, Moritz Zaiss, Andreas Maier, Paula A. Perez-Toro
链接: https://arxiv.org/abs/2605.18221v1
完整摘要: Real-time magnetic resonance imaging (rtMRI) of speech production enables non-invasive visualization of dynamic vocal-tract motion and is valuable for speech science and clinical assessment. However, rtMRI is fundamentally constrained by trade-offs among spatial resolution, temporal resolution, and acquisition speed, often leading to undersampled k-space measurements and degraded reconstructions. We propose SIREM, a speech-informed MRI reconstruction framework that uses synchronized speech as a cross-modal prior. The central idea is that vocal-tract configurations during speech are correlated with the produced acoustics, making part of the image content predictable from audio. SIREM models each frame as a fusion of an audio-driven component and an MRI-driven component through a spatial weighting map. The audio branch predicts articulator-related structure from speech, while the MRI branch reconstructs complementary content from measured k-space data. We further introduce a learnable soft weighting profile over spiral arms, enabling a differentiable study of how k-space arm usage interacts with speech-informed fusion. This yields a unified multimodal formulation that combines audio-driven prediction, MRI reconstruction, and sampling adaptation. We evaluate SIREM on the USC speech rtMRI benchmark against standard baselines, including gridding, wavelet-based compressed sensing, and total variation. SIREM introduces a speech-informed reconstruction paradigm that operates in a substantially higher-throughput regime than iterative methods while preserving anatomically plausible vocal-tract structure. These results establish an initial benchmark for multimodal speech-informed rtMRI reconstruction and highlight the potential of synchronized speech as an auxiliary prior for fast reconstruction. The source code is available at https://github.com/mdhasanai/SIREM
匹配关键词: preference learning
---

[ACADEMIC - ARXIV]
标题: Forward-Learned Discrete Diffusion: Learning how to noise to denoise faster
作者: Grigory Bartosh, Teodora Pandeva, Sushrut Karmalkar, Javier Zazo
链接: https://arxiv.org/abs/2605.18204v1
完整摘要: Discrete diffusion models are a powerful class of generative models with strong performance across many domains. For efficiency, however, discrete diffusion typically parameterizes the generative (reverse) process with factorized distributions, which makes it difficult for the model to learn the target process in a small number of steps and necessitates a long, computationally expensive sampling procedure. To reduce the gap between the target and model distributions and enable few-step generation, we propose Forward-Learned Discrete Diffusion (FLDD), which introduces discrete diffusion with a learnable forward (noising) process. Rather than fixing a Markovian forward chain, we adopt a non-Markovian formulation with learnable marginal and posterior distributions. This allows the generative process to remain factorized while matching the target defined by the noising process. We train all parameters end-to-end under the standard variational objective. Experiments on various benchmarks show that, for a given number of sampling steps, our approach produces a higher quality samples than conventional discrete diffusion models using the same reverse parameterization.
匹配关键词: preference learning
---

[ACADEMIC - ARXIV]
标题: Are Sparse Autoencoder Benchmarks Reliable?
作者: David Chanin
链接: https://arxiv.org/abs/2605.18229v1
完整摘要: Sparse autoencoders (SAEs) are a core interpretability tool for large language models, and progress on SAE architectures depends on benchmarks that reliably distinguish better SAEs from worse ones. We audit the SAE quality metrics in SAEBench, the de-facto standard SAE evaluation suite, through three complementary lenses: reseed noise on a fixed SAE, ground-truth correlation on synthetic SAEs, and discriminability across training trajectories. We find that two of these metrics, Targeted Probe Perturbation (TPP) and Spurious Correlation Removal (SCR), fail multiple lenses at their canonical settings and should not be used to evaluate SAEs. The other metrics show higher reseed noise and lower discriminability than the field assumes. The sae-probes variant of $k$-sparse probing is the most reliable metric we tested, but even sae-probes struggles to separate variants of the same SAE architecture. Our results show the field needs better SAE benchmarks.
匹配关键词: reward model
---

[ACADEMIC - ARXIV]
标题: Context Memorization for Efficient Long Context Generation
作者: Yasuyuki Okoshi, Hao Mark Chen, Guanxi Lu, Hongxiang Fan, Masato Motomura, Daichi Fujiki
链接: https://arxiv.org/abs/2605.18226v1
完整摘要: Modern large language model (LLM) applications increasingly rely on long conditioning prefixes to control model behavior at inference time. While prefix-augmented inference is effective, it incurs two structural limitations: i) the prefix's influence fades as generation proceeds, and ii) attention computation over the prefix scales linearly with its length. Existing approaches either keep the prefix in attention while compressing it, or internalize it into model parameters through gradient-based training. The former still attends to the prefix at inference, while the latter is training-intensive and ill-suited to prefix updates. To address these issues, we propose attention-state memory, a training-free approach that externalizes the prefix into a lightweight, lookup-based memory of precomputed attention states between prefix and query tokens. On ManyICLBench with LLaMA-3.1-8B, our method improves accuracy over in-context learning at 1K-8K memory budgets while reducing attention latency by 1.36x at 8K, and surpasses full-attention RAG performance on NBA benchmark using only 20% of its memory footprint.
匹配关键词: reward model
---

[ACADEMIC - ARXIV]
标题: Contextual Biasing for Streaming ASR via CTC-based Word Spotting
作者: Kai-Chen Tsai, Tien-Hong Lo, Yun-Ting Sun, Berlin Chen
链接: https://arxiv.org/abs/2605.18222v1
完整摘要: Contextual biasing is essential to improving the recognition of rare and domain-specific words in an automatic speech recognition (ASR) system. While numerous methods have been proposed in recent years, most of them focus on offline settings and do not explicitly address the challenges of streaming ASR. For example, CTC-based word spotting (CTC-WS) have demonstrated strong performance by directly detecting keywords from CTC log-probabilities, but they are limited to offline processing and require access to the full utterance. In This work, we present a streaming extension of CTC-WS for real-time contextual biasing. Our method maintains active keyword paths across audio chunks using a stateful token passing algorithm, enabling the detection of keywords that span multiple chunks. To ensure low latency and stable output, we introduce an incremental commitment mechanism that only emits segments guaranteed not to be affected by future audio, while deferring uncertain regions. This method naturally integrates with streaming ASR pipelines and does not require modifications to the underlying acoustic model or additional training, making it practical for real-world deployment. Experimental results show that our method reduces overall WER and effectively improves keyword F-score, demonstrating its effectiveness for real-time ASR applications.
匹配关键词: reward model
---

[ACADEMIC - ARXIV]
标题: SIREM: Speech-Informed MRI Reconstruction with Learned Sampling
作者: Md Hasan, Nyvenn Castro, Daiqi Liu, Lukas Mulzer, Jana Hutter, Jonghye Woo, Moritz Zaiss, Andreas Maier, Paula A. Perez-Toro
链接: https://arxiv.org/abs/2605.18221v1
完整摘要: Real-time magnetic resonance imaging (rtMRI) of speech production enables non-invasive visualization of dynamic vocal-tract motion and is valuable for speech science and clinical assessment. However, rtMRI is fundamentally constrained by trade-offs among spatial resolution, temporal resolution, and acquisition speed, often leading to undersampled k-space measurements and degraded reconstructions. We propose SIREM, a speech-informed MRI reconstruction framework that uses synchronized speech as a cross-modal prior. The central idea is that vocal-tract configurations during speech are correlated with the produced acoustics, making part of the image content predictable from audio. SIREM models each frame as a fusion of an audio-driven component and an MRI-driven component through a spatial weighting map. The audio branch predicts articulator-related structure from speech, while the MRI branch reconstructs complementary content from measured k-space data. We further introduce a learnable soft weighting profile over spiral arms, enabling a differentiable study of how k-space arm usage interacts with speech-informed fusion. This yields a unified multimodal formulation that combines audio-driven prediction, MRI reconstruction, and sampling adaptation. We evaluate SIREM on the USC speech rtMRI benchmark against standard baselines, including gridding, wavelet-based compressed sensing, and total variation. SIREM introduces a speech-informed reconstruction paradigm that operates in a substantially higher-throughput regime than iterative methods while preserving anatomically plausible vocal-tract structure. These results establish an initial benchmark for multimodal speech-informed rtMRI reconstruction and highlight the potential of synchronized speech as an auxiliary prior for fast reconstruction. The source code is available at https://github.com/mdhasanai/SIREM
匹配关键词: reward model
---

[ACADEMIC - ARXIV]
标题: EgoInteract: Synthetic Egocentric Videos Generation for Interaction Understanding and Anticipation
作者: Rosario Leonardi, Francesco Ragusa, Daniele Materia, Alessandro Passanisi, James Fort, Jakob Engel, Giovanni Maria Farinella
链接: https://arxiv.org/abs/2605.18214v1
完整摘要: Collecting large-scale egocentric video datasets with dense spatial and temporal annotations is costly, slow, and often constrained by environmental biases, privacy constraints, and limited coverage of interaction patterns. While synthetic data has shown strong potential in several vision domains, its use for egocentric perception remains relatively underexplored, especially for tasks requiring temporally coherent human-object interactions. In this work, we introduce EgoInteract, a controllable simulator for egocentric video generation designed to model fine-grained egocentric interactions and their temporal dynamics. The simulator enables precise control over camera, human body and hand motion, object manipulation, and scene composition across diverse environments. Building on this framework, we generate a synthetic egocentric video dataset with dense spatial and temporal annotations for temporal action segmentation, next-active object detection, interaction anticipation, and hand-object interaction detection. We evaluate models trained with simulated data on multiple real-world egocentric benchmarks spanning diverse environments, object categories, and interaction patterns. Results show consistent improvements over strong baselines across tasks and datasets, demonstrating the effectiveness and transferability of our simulation-based approach.
匹配关键词: reward model
---

[ACADEMIC - ARXIV]
标题: Beyond the Cartesian Illusion: Testing Two-Stage Multi-Modal Theory of Mind under Perceptual Bottlenecks
作者: Yajing Zhou, Xiangyu Kong
链接: https://arxiv.org/abs/2605.18194v1
完整摘要: While Multi-Modal Large Language Models (MLLMs) demonstrate impressive capabilities in general reasoning, their embodied spatial intelligence remains hampered by a "Cartesian Illusion" - a reliance on text-based probability distributions that lack grounded, 3D topological understanding. This limitation is starkly exposed in multi-agent environments, which demand more than just scene perception; they require second-order Theory of Mind (ToM). Specifically, an Agent A must be able to infer Agent B's belief about the environment, governed strictly by Agent B's physical orientation and sensory limitations. In this paper, we probe the limits of two-stage spatial inference in MLLMs through a novel audio-visual task: requiring Agent A to predict Agent B's estimation of A's relative location. To solve this, we propose an Epistemic Sensory Bottleneck module that abandons rigid, rule-based coordinate transformations. Instead, we introduce an Anchor-Based Embodied Spatial Decomposition Chain-of-Thought (CoT). This guides the MLLM through a "geometric-to-semantic" projection, forcing it to first establish B's local coordinate system and then dynamically weight visual and auditory modalities based on whether A falls within B's visual frustum. Extensive evaluations reveal that while current MLLMs fundamentally struggle with spatial symmetry and out-of-view ambiguities (establishing a rigorous zero-shot baseline of 42% accuracy), our sensory-bounded reasoning chain robustly outperforms pure egocentric and allocentric baselines. By systematically benchmarking these perceptual bottlenecks, our work exposes the current limits of MLLM spatial reasoning and establishes a foundational paradigm for epistemic, modality-aware inference in Embodied AI.
匹配关键词: constitutional AI
---

[ACADEMIC - ARXIV]
标题: Foundation Models for Credit Risk Prediction: A Game Changer?
作者: Bart Baesens, Andreas Goethals, Stefan Lessmann, Simon De Vos, Cristián Bravo, David Martens, Victor Medina-Olivares, Christophe Mues, Maria Oskarsdóttir, Seppe vanden Broucke, Tim Verdonck, Wouter Verbeke
链接: https://arxiv.org/abs/2605.18147v1
完整摘要: Predictive models play a pivotal role in credit risk management, guiding critical decisions through accurate estimation of default probabilities and losses. Extensive research has introduced new modeling techniques, complemented by large-scale benchmarking studies consolidating the state-of-the-art. Today, quasi-standards such as gradient-boosting models paired with SHAP explainers have emerged, yet continuous improvement of risk models remains a top priority. Concurrently, rapid advancements in AI, most notably large language models, have disrupted predictive modeling paradigms. Foundation models, pretrained on extensive datasets from diverse domains, have demonstrated remarkable performance by leveraging prior knowledge. While prevalent in natural language processing and computer vision, foundation models for tabular data have only recently emerged. We conjecture that pretraining on out-of-domain data is particularly beneficial in small-data settings, such as SME lending or specialized corporate portfolios, and may help address longstanding challenges including low default portfolios and class imbalance. This paper benchmarks recently proposed tabular foundation models against a broad set of competitors, including established and advanced machine learning techniques, across two core tasks: PD and LGD modeling. Our evaluation encompasses various datasets, performance indicators, and experimental conditions. We find that tabular foundation models generally perform best across datasets and tasks. Moreover, they offer significant improvement in predictive performance as dataset size shrinks. These results are remarkable given that the models are tested out-of-the-box, without hyperparameter tuning, ensuring ease of use and mitigating computational costs.
匹配关键词: constitutional AI
---

[ACADEMIC - ARXIV]
标题: Generative AI and the Productivity Divide: Human-AI Complementarities in Education
作者: Lihi Idan, Bharat Anand
链接: https://arxiv.org/abs/2605.18143v1
完整摘要: Generative Artificial Intelligence (GenAI) is transforming how firms create, process, and apply knowledge, yet little is known about the heterogeneity of its productivity effects across users. We report results from a randomized controlled experiment in which participants-analogs of early-career knowledge workers-were assigned to self-study a technical domain using either traditional resources or large-language-model (LLM) assistance. On average, GenAI access significantly increased task performance, but the distribution of gains was highly uneven. Improvements were not predicted by GPA or prior knowledge, but by \textit{AI Interaction Competence (AIC)} -- the ability to elicit, filter, and verify model outputs. High-AIC participants realized outsized gains; low-AIC participants saw limited or even negative marginal returns. A scaffolding intervention (conceptual maps) reduced outcome variance, indicating that standardized workflows can mitigate inequality in AI-mediated performance. We interpret these findings through the lens of human-AI complementarities: GenAI raises mean productivity while introducing a new axis of capability inequality. Managerially, firms should pair GenAI access with short AIC micro-training and simple standard operating procedures to capture value consistently and avoid uneven adoption outcomes.
匹配关键词: constitutional AI
---

[ACADEMIC - ARXIV]
标题: How Good LLMs Are at Answering Bangla Medical Visual Questions? Dataset and Benchmarking
作者: Rafid Ahmed, Intesar Tahmid, Mir Sazzat Hossain, Tasnimul Hossain Tomal, Md Fahim, Md Farhad Alam Bhuiyan
链接: https://arxiv.org/abs/2605.18111v1
完整摘要: Recent advancements in Large Language Models (LLMs) and Large Vision Language Models (LVLMs) have enabled general-purpose systems to demonstrate promising capabilities in complex reasoning tasks, including those in the medical domain. Medical Visual Question Answering (MedVQA) has particularly benefited from these developments. However, despite Bangla being one of the most widely spoken languages globally, there exists no established MedVQA benchmark for it. To address this gap, we introduce BanglaMedVQA, a dataset comprising clinically validated image-question-answer pairs, along with a comprehensive evaluation of current foundation models on this resource. Consistent with prior findings that report low performance of current models on English MedVQA benchmarks, our analysis reveals that Bangla performance is substantially lower, reflecting the challenges inherent to low-resource languages. Even top-performing models such as Gemini and GPT-4.1 mini fail to accurately answer specialized diagnostic questions, indicating severe limitations in fine-grained medical reasoning. Although certain open-source models, such as Gemma-3, occasionally outperform these models in general categories, they too struggle with clinically complex questions, underscoring the urgent need for top-notch evaluation method.
匹配关键词: constitutional AI
---

[ACADEMIC - ARXIV]
标题: SENSE: Satellite-based ENergy Synthesis for Sustainable Environment
作者: Kailai Sun, Mingyi He, Heye Huang, Can Rong, Alok Prakash, Baoshen Guo, Shenhao Wang, Jinhua Zhao
链接: https://arxiv.org/abs/2605.18101v1
完整摘要: Urban Building Energy Modeling plays a critical role in achieving the United Nations' Sustainable Development Goals 7 and 11. Although existing studies based on satellite imagery and deep learning have achieved remarkable progress, many challenges exist: most existing studies are inherently predictive, failing to reflect the generative nature of urban planning; although generative AI and diffusion models have seen explosive growth in satellite imagery, they lack the urban functional generation (e.g., energy layer); third, aligned high-quality high-resolution building energy data with satellite imagery is limited and scarce. Here we propose SENSE (Satellite-based ENergy Synthesis for Sustainable Environment), a unified generative UBEM framework that jointly synthesizes realistic urban satellite imagery and aligned high-quality building energy consumption and height maps. By conditioning on road networks and urban density metrics, SENSE, based on a controllable diffusion model, leverages the knowledge learned by large vision models to generate urban building energy consumption and height information (annotations) in the latent space. Experiments across four cities (New York City, Boston, Lyon, Busan) demonstrate that SENSE achieves high visual fidelity and strong physical consistency, satisfying the ASHRAE standard metric. Experiments demonstrate that SENSE can generate enough annotated synthetic data using less than 20% labeled energy data, boosting downstream prediction performance by 10% IoU. Compared to SOTA urban energy prediction methods, SENSE significantly reduced prediction error (reduced 3%-11% NMBE and 1%-9% CVRMSE). This study offers an energy-efficiency urban planning and physical generation solution for urban science, energy science and building science. The dataset and code: https://huggingface.co/datasets/skl24/MUSE and https://github.com/kailaisun/GenAI4Urban-Energy/.
匹配关键词: constitutional AI
---

[ACADEMIC - ARXIV]
标题: Context Memorization for Efficient Long Context Generation
作者: Yasuyuki Okoshi, Hao Mark Chen, Guanxi Lu, Hongxiang Fan, Masato Motomura, Daichi Fujiki
链接: https://arxiv.org/abs/2605.18226v1
完整摘要: Modern large language model (LLM) applications increasingly rely on long conditioning prefixes to control model behavior at inference time. While prefix-augmented inference is effective, it incurs two structural limitations: i) the prefix's influence fades as generation proceeds, and ii) attention computation over the prefix scales linearly with its length. Existing approaches either keep the prefix in attention while compressing it, or internalize it into model parameters through gradient-based training. The former still attends to the prefix at inference, while the latter is training-intensive and ill-suited to prefix updates. To address these issues, we propose attention-state memory, a training-free approach that externalizes the prefix into a lightweight, lookup-based memory of precomputed attention states between prefix and query tokens. On ManyICLBench with LLaMA-3.1-8B, our method improves accuracy over in-context learning at 1K-8K memory budgets while reducing attention latency by 1.36x at 8K, and surpasses full-attention RAG performance on NBA benchmark using only 20% of its memory footprint.
匹配关键词: RAG
---

[ACADEMIC - ARXIV]
标题: Predictive Prefetching for Retrieval-Augmented Generation
作者: Wuyang Zhang, Shichao Pei
链接: https://arxiv.org/abs/2605.17989v1
完整摘要: Retrieval-Augmented Generation (RAG) improves factual grounding in large language models but suffers from substantial latency due to synchronous retrieval. While recent work explores asynchronous retrieval, existing approaches rely on heuristic coordination between retrieval and generation and assume stable information demands during decoding that often break in complex, multi-domain settings. In this paper, we propose an advanced asynchronous retrieval framework that enables predictive prefetching aligned with evolving information needs. The framework explicitly predicts when retrieval should be triggered and what information should be retrieved using three components, a retrieval predictor, a context monitor, and a query generator, by exploiting semantic precursors in generation dynamics that emerge several tokens before uncertainty becomes critical. Experiments on multiple benchmarks demonstrate up to 43.5% end-to-end latency reduction and 62.4% improvement in time-to-first-token, while maintaining answer quality comparable to synchronous RAG baselines.
匹配关键词: RAG
---

[ACADEMIC - ARXIV]
标题: BLAgent: Agentic RAG for File-Level Bug Localization
作者: Md Afif Al Mamun, Gias Uddin
链接: https://arxiv.org/abs/2605.17965v1
完整摘要: Bug localization remains a key bottleneck in downstream software maintenance tasks, including root cause analysis, triage, and automated program repair (APR), despite recent advances in large language model (LLM)-based repair systems. File-level bug localization is especially critical in hierarchical pipelines, where errors can propagate to downstream stages such as statement-level localization or patch generation. While Retrieval-Augmented Generation (RAG) offers a promising direction for grounding LLMs in repository context, existing RAG pipelines rely on static retrieval and lack the reasoning needed to identify faulty code accurately. In this work, we present BLAgent, a novel agentic RAG framework for file-level bug localization that integrates three key ideas: (i) code structure-aware repository encoding with path-augmented AST-based chunking, (ii) dual-perspective query transformation capturing both structural and behavioral signals, and (iii) two-phase agentic reranking combining symbolic inspection with evidence-grounded reasoning. Unlike prior graph-based or multi-hop agentic approaches, BLAgent performs bounded reasoning over a compact candidate set, balancing accuracy and cost. On SWE-bench Lite, BLAgent attains over 78% Top-1 accuracy with open-source models and over 86% with a closed-source model, while being over 18x cheaper than the strongest baseline using the same model. When integrated into an APR framework, it improves end-to-end repair success by over 20%.
匹配关键词: RAG
---

[ACADEMIC - ARXIV]
标题: SVFSearch: A Multimodal Knowledge-Intensive Benchmark for Short-Video Frame Search in the Gaming Vertical Domain
作者: Lingtao Mao, Huangyu Dai, Xinyu Sun, Zihan Liang, Ben Chen, Chenyi Lei, Wenwu Ou
链接: https://arxiv.org/abs/2605.17946v1
完整摘要: Multimodal large language models are increasingly used as agent backbones that understand multimodal inputs, plan retrieval actions, invoke external tools, and reason over retrieved information. Yet existing benchmarks rarely evaluate this ability in short-video applications, where a paused frame is often visually ambiguous and answering requires vertical, long-tail, and fast-evolving domain knowledge. We introduce SVFSearch, the first open benchmark for short-video frame search in the Chinese gaming domain. SVFSearch contains 5,000 four-choice test examples and 4,198 auxiliary training examples, each centered on a paused game scene from a real short-video clip. To support fair and reproducible evaluation, SVFSearch provides a frozen offline retrieval environment with a game-domain text corpus, a topic-linked image gallery, and text, image, and multimodal retrieval interfaces, avoiding reliance on uncontrolled web search APIs. We evaluate representative paradigms ranging from direct QA and RAG workflow to Plan-Act-Replan agents and learned search models. Results reveal a large gap between model-only answering, practical agentic search, and oracle knowledge: the best open-source direct-QA model reaches 66.4%, the best practical agent achieves 79.1%, and oracle knowledge reaches 95.4%. Further analysis exposes bottlenecks in visual grounding, retrieval quality, evidence-grounded reasoning, and tool-use behavior, including over-search, answer-only shortcuts, and retrieval-induced misleading.
匹配关键词: RAG
---

[ACADEMIC - ARXIV]
标题: LAST-RAG: Literature-Anchored Stochastic Trajectory Retrieval-Augmented Generation for Knowledge-Conditioned Degradation Model Selection
作者: Hanbyeol Park, Hyerim Bae
链接: https://arxiv.org/abs/2605.17902v1
完整摘要: Stochastic-process-based degradation modeling is a core approach for estimating the distribution of remaining useful life (RUL); however, the selection of an appropriate stochastic process has not been sufficiently addressed. Existing model selection methods mainly rely on the statistical fit of the observed health indicator (HI) trajectory, but this approach may select a model that is inconsistent with the underlying degradation mechanism when the observation window is short or the signal is highly noisy. To address this issue, this paper proposes Literature-Anchored Stochastic Trajectory Retrieval-Augmented Generation (LAST-RAG). The proposed method uses both the observed HI trajectory and domain-specific context, and hierarchically conditions the candidate degradation model space based on theoretical and mechanical evidence retrieved from a local evidence bank. In addition, Rule-based Confidence Reasoning with Uncertain State (RCRUS) is introduced to prevent candidate models from being prematurely eliminated when hierarchical decisions are uncertain. Simulation-based experiments demonstrate that the proposed method outperforms statistical, prognostic, and uncertainty-aware baselines in both Wiener/gamma family classification and detailed degradation model classification. Ultimately, this study reframes degradation model selection from a purely statistical goodness-of-fit problem into a knowledge-conditioned decision-making problem that integrates observed data with domain knowledge.
匹配关键词: RAG
---

[ACADEMIC - ARXIV]
标题: Context Memorization for Efficient Long Context Generation
作者: Yasuyuki Okoshi, Hao Mark Chen, Guanxi Lu, Hongxiang Fan, Masato Motomura, Daichi Fujiki
链接: https://arxiv.org/abs/2605.18226v1
完整摘要: Modern large language model (LLM) applications increasingly rely on long conditioning prefixes to control model behavior at inference time. While prefix-augmented inference is effective, it incurs two structural limitations: i) the prefix's influence fades as generation proceeds, and ii) attention computation over the prefix scales linearly with its length. Existing approaches either keep the prefix in attention while compressing it, or internalize it into model parameters through gradient-based training. The former still attends to the prefix at inference, while the latter is training-intensive and ill-suited to prefix updates. To address these issues, we propose attention-state memory, a training-free approach that externalizes the prefix into a lightweight, lookup-based memory of precomputed attention states between prefix and query tokens. On ManyICLBench with LLaMA-3.1-8B, our method improves accuracy over in-context learning at 1K-8K memory budgets while reducing attention latency by 1.36x at 8K, and surpasses full-attention RAG performance on NBA benchmark using only 20% of its memory footprint.
匹配关键词: code generation
---

[ACADEMIC - ARXIV]
标题: SIREM: Speech-Informed MRI Reconstruction with Learned Sampling
作者: Md Hasan, Nyvenn Castro, Daiqi Liu, Lukas Mulzer, Jana Hutter, Jonghye Woo, Moritz Zaiss, Andreas Maier, Paula A. Perez-Toro
链接: https://arxiv.org/abs/2605.18221v1
完整摘要: Real-time magnetic resonance imaging (rtMRI) of speech production enables non-invasive visualization of dynamic vocal-tract motion and is valuable for speech science and clinical assessment. However, rtMRI is fundamentally constrained by trade-offs among spatial resolution, temporal resolution, and acquisition speed, often leading to undersampled k-space measurements and degraded reconstructions. We propose SIREM, a speech-informed MRI reconstruction framework that uses synchronized speech as a cross-modal prior. The central idea is that vocal-tract configurations during speech are correlated with the produced acoustics, making part of the image content predictable from audio. SIREM models each frame as a fusion of an audio-driven component and an MRI-driven component through a spatial weighting map. The audio branch predicts articulator-related structure from speech, while the MRI branch reconstructs complementary content from measured k-space data. We further introduce a learnable soft weighting profile over spiral arms, enabling a differentiable study of how k-space arm usage interacts with speech-informed fusion. This yields a unified multimodal formulation that combines audio-driven prediction, MRI reconstruction, and sampling adaptation. We evaluate SIREM on the USC speech rtMRI benchmark against standard baselines, including gridding, wavelet-based compressed sensing, and total variation. SIREM introduces a speech-informed reconstruction paradigm that operates in a substantially higher-throughput regime than iterative methods while preserving anatomically plausible vocal-tract structure. These results establish an initial benchmark for multimodal speech-informed rtMRI reconstruction and highlight the potential of synchronized speech as an auxiliary prior for fast reconstruction. The source code is available at https://github.com/mdhasanai/SIREM
匹配关键词: code generation
---

[ACADEMIC - ARXIV]
标题: EgoInteract: Synthetic Egocentric Videos Generation for Interaction Understanding and Anticipation
作者: Rosario Leonardi, Francesco Ragusa, Daniele Materia, Alessandro Passanisi, James Fort, Jakob Engel, Giovanni Maria Farinella
链接: https://arxiv.org/abs/2605.18214v1
完整摘要: Collecting large-scale egocentric video datasets with dense spatial and temporal annotations is costly, slow, and often constrained by environmental biases, privacy constraints, and limited coverage of interaction patterns. While synthetic data has shown strong potential in several vision domains, its use for egocentric perception remains relatively underexplored, especially for tasks requiring temporally coherent human-object interactions. In this work, we introduce EgoInteract, a controllable simulator for egocentric video generation designed to model fine-grained egocentric interactions and their temporal dynamics. The simulator enables precise control over camera, human body and hand motion, object manipulation, and scene composition across diverse environments. Building on this framework, we generate a synthetic egocentric video dataset with dense spatial and temporal annotations for temporal action segmentation, next-active object detection, interaction anticipation, and hand-object interaction detection. We evaluate models trained with simulated data on multiple real-world egocentric benchmarks spanning diverse environments, object categories, and interaction patterns. Results show consistent improvements over strong baselines across tasks and datasets, demonstrating the effectiveness and transferability of our simulation-based approach.
匹配关键词: code generation
---

[ACADEMIC - ARXIV]
标题: Leveraging Graph Structure in Seq2Seq Models for Knowledge Graph Link Prediction
作者: Luu Huu Phuc, Ratan Bahadur Thapa, Mojtaba Nayyeri, Jingcheng Wu, Evgeny Kharlamov, Steffen Staab
链接: https://arxiv.org/abs/2605.18211v1
完整摘要: We introduce Graph-Augmented Sequence-to-Sequence (GA-S2S), a novel framework that integrates a T5-small encoder-decoder with a Relational Graph Attention Network (RGAT) to improve link prediction in knowledge graphs. While existing Seq2Seq models rely solely on surface-level textual descriptions of entities and relations and at best, flatten the neighborhoods of a query entity into a single linear sequence, thereby discarding the inherent graph structure, GA-S2S jointly encodes both textual features and the full $k$-hop subgraph topology surrounding the query entity. By integrating raw encoder outputs with RGAT's relation-aware embeddings, our model captures and leverages richer multi-hop relational patterns and textual information. Our preliminary experiments on the CoDEx dataset demonstrate that GA-S2S outperforms competitive Seq2Seq-based baseline models, achieving up to a 19\% relative gain in link prediction accuracy.
匹配关键词: code generation
---

[ACADEMIC - ARXIV]
标题: SPATIOROUTE: Dynamic Prompt Routing for Zero-Shot Spatial Reasoning
作者: Pawat Chunhachatrachai, Gueter Josmy Faure, Hung-Ting Su, Winston H. Hsu
链接: https://arxiv.org/abs/2605.18209v1
完整摘要: Spatial question answering over egocentric video is a challenging task that requires Vision-Language Models (VLMs) to reason about 3D object positions, scene affordances, and directional relationships, particularly in the zero-shot setting where no task-specific fine-tuning is available. We introduce SpatioRoute, a dynamic prompt generation approach that routes each incoming question to a semantically tailored prompt template -- without any additional training, fine-tuning, or 3D sensor input. SpatioRoute operates in two complementary modes: SpatioRoute-R, a rule-based router that deterministically maps question typologies (e.g., What, Is, How, Can, Which) to specialized prompt templates; and SpatioRoute-L, an LLM-driven approach that generates task-specific prompts from the question and situational context alone, with no video input at routing time. We evaluate SpatioRoute on the SQA3D benchmark across VLMs spanning model families. SpatioRoute achieves consistent overall accuracy gains up to 5% over fixed prompt baselines, establishing a new state-of-the-art for zero-shot video-only spatial VQA without requiring 3D point-cloud inputs. As an additional finding, we observe that Chain-of-Thought (CoT) prompting, implemented via the Think it Twice architecture, consistently degrades performance in this setting on Qwen series models, confirming that question-aware routing is more effective than uniform reasoning instructions for spatial video understanding.
匹配关键词: code generation
---

[ACADEMIC - ARXIV]
标题: Are Sparse Autoencoder Benchmarks Reliable?
作者: David Chanin
链接: https://arxiv.org/abs/2605.18229v1
完整摘要: Sparse autoencoders (SAEs) are a core interpretability tool for large language models, and progress on SAE architectures depends on benchmarks that reliably distinguish better SAEs from worse ones. We audit the SAE quality metrics in SAEBench, the de-facto standard SAE evaluation suite, through three complementary lenses: reseed noise on a fixed SAE, ground-truth correlation on synthetic SAEs, and discriminability across training trajectories. We find that two of these metrics, Targeted Probe Perturbation (TPP) and Spurious Correlation Removal (SCR), fail multiple lenses at their canonical settings and should not be used to evaluate SAEs. The other metrics show higher reseed noise and lower discriminability than the field assumes. The sae-probes variant of $k$-sparse probing is the most reliable metric we tested, but even sae-probes struggles to separate variants of the same SAE architecture. Our results show the field needs better SAE benchmarks.
匹配关键词: benchmark
---

[ACADEMIC - ARXIV]
标题: Context Memorization for Efficient Long Context Generation
作者: Yasuyuki Okoshi, Hao Mark Chen, Guanxi Lu, Hongxiang Fan, Masato Motomura, Daichi Fujiki
链接: https://arxiv.org/abs/2605.18226v1
完整摘要: Modern large language model (LLM) applications increasingly rely on long conditioning prefixes to control model behavior at inference time. While prefix-augmented inference is effective, it incurs two structural limitations: i) the prefix's influence fades as generation proceeds, and ii) attention computation over the prefix scales linearly with its length. Existing approaches either keep the prefix in attention while compressing it, or internalize it into model parameters through gradient-based training. The former still attends to the prefix at inference, while the latter is training-intensive and ill-suited to prefix updates. To address these issues, we propose attention-state memory, a training-free approach that externalizes the prefix into a lightweight, lookup-based memory of precomputed attention states between prefix and query tokens. On ManyICLBench with LLaMA-3.1-8B, our method improves accuracy over in-context learning at 1K-8K memory budgets while reducing attention latency by 1.36x at 8K, and surpasses full-attention RAG performance on NBA benchmark using only 20% of its memory footprint.
匹配关键词: benchmark
---

[ACADEMIC - ARXIV]
标题: SIREM: Speech-Informed MRI Reconstruction with Learned Sampling
作者: Md Hasan, Nyvenn Castro, Daiqi Liu, Lukas Mulzer, Jana Hutter, Jonghye Woo, Moritz Zaiss, Andreas Maier, Paula A. Perez-Toro
链接: https://arxiv.org/abs/2605.18221v1
完整摘要: Real-time magnetic resonance imaging (rtMRI) of speech production enables non-invasive visualization of dynamic vocal-tract motion and is valuable for speech science and clinical assessment. However, rtMRI is fundamentally constrained by trade-offs among spatial resolution, temporal resolution, and acquisition speed, often leading to undersampled k-space measurements and degraded reconstructions. We propose SIREM, a speech-informed MRI reconstruction framework that uses synchronized speech as a cross-modal prior. The central idea is that vocal-tract configurations during speech are correlated with the produced acoustics, making part of the image content predictable from audio. SIREM models each frame as a fusion of an audio-driven component and an MRI-driven component through a spatial weighting map. The audio branch predicts articulator-related structure from speech, while the MRI branch reconstructs complementary content from measured k-space data. We further introduce a learnable soft weighting profile over spiral arms, enabling a differentiable study of how k-space arm usage interacts with speech-informed fusion. This yields a unified multimodal formulation that combines audio-driven prediction, MRI reconstruction, and sampling adaptation. We evaluate SIREM on the USC speech rtMRI benchmark against standard baselines, including gridding, wavelet-based compressed sensing, and total variation. SIREM introduces a speech-informed reconstruction paradigm that operates in a substantially higher-throughput regime than iterative methods while preserving anatomically plausible vocal-tract structure. These results establish an initial benchmark for multimodal speech-informed rtMRI reconstruction and highlight the potential of synchronized speech as an auxiliary prior for fast reconstruction. The source code is available at https://github.com/mdhasanai/SIREM
匹配关键词: benchmark
---

[ACADEMIC - ARXIV]
标题: EgoInteract: Synthetic Egocentric Videos Generation for Interaction Understanding and Anticipation
作者: Rosario Leonardi, Francesco Ragusa, Daniele Materia, Alessandro Passanisi, James Fort, Jakob Engel, Giovanni Maria Farinella
链接: https://arxiv.org/abs/2605.18214v1
完整摘要: Collecting large-scale egocentric video datasets with dense spatial and temporal annotations is costly, slow, and often constrained by environmental biases, privacy constraints, and limited coverage of interaction patterns. While synthetic data has shown strong potential in several vision domains, its use for egocentric perception remains relatively underexplored, especially for tasks requiring temporally coherent human-object interactions. In this work, we introduce EgoInteract, a controllable simulator for egocentric video generation designed to model fine-grained egocentric interactions and their temporal dynamics. The simulator enables precise control over camera, human body and hand motion, object manipulation, and scene composition across diverse environments. Building on this framework, we generate a synthetic egocentric video dataset with dense spatial and temporal annotations for temporal action segmentation, next-active object detection, interaction anticipation, and hand-object interaction detection. We evaluate models trained with simulated data on multiple real-world egocentric benchmarks spanning diverse environments, object categories, and interaction patterns. Results show consistent improvements over strong baselines across tasks and datasets, demonstrating the effectiveness and transferability of our simulation-based approach.
匹配关键词: benchmark
---

[ACADEMIC - ARXIV]
标题: SPATIOROUTE: Dynamic Prompt Routing for Zero-Shot Spatial Reasoning
作者: Pawat Chunhachatrachai, Gueter Josmy Faure, Hung-Ting Su, Winston H. Hsu
链接: https://arxiv.org/abs/2605.18209v1
完整摘要: Spatial question answering over egocentric video is a challenging task that requires Vision-Language Models (VLMs) to reason about 3D object positions, scene affordances, and directional relationships, particularly in the zero-shot setting where no task-specific fine-tuning is available. We introduce SpatioRoute, a dynamic prompt generation approach that routes each incoming question to a semantically tailored prompt template -- without any additional training, fine-tuning, or 3D sensor input. SpatioRoute operates in two complementary modes: SpatioRoute-R, a rule-based router that deterministically maps question typologies (e.g., What, Is, How, Can, Which) to specialized prompt templates; and SpatioRoute-L, an LLM-driven approach that generates task-specific prompts from the question and situational context alone, with no video input at routing time. We evaluate SpatioRoute on the SQA3D benchmark across VLMs spanning model families. SpatioRoute achieves consistent overall accuracy gains up to 5% over fixed prompt baselines, establishing a new state-of-the-art for zero-shot video-only spatial VQA without requiring 3D point-cloud inputs. As an additional finding, we observe that Chain-of-Thought (CoT) prompting, implemented via the Think it Twice architecture, consistently degrades performance in this setting on Qwen series models, confirming that question-aware routing is more effective than uniform reasoning instructions for spatial video understanding.
匹配关键词: benchmark
---

[ACADEMIC - ARXIV]
标题: Safety Geometry Collapse in Multimodal LLMs and Adaptive Drift Correction
作者: Jiahe Guo, Xiangran Guo, Jiaxuan Chen, Weixiang Zhao, Yanyan Zhao, Yutai Hou, Qianchao Wang, Dandan Tu, Bing Qin
链接: https://arxiv.org/abs/2605.18104v1
完整摘要: Multimodal large language models (MLLMs) often fail to transfer safety capabilities learned in the text modality to semantically equivalent non-text inputs, revealing a persistent multimodal safety gap. We study this gap from a representation-geometric perspective by analyzing a text-aligned refusal direction and a modality-induced drift direction. We show that multimodal inputs compress the usable separation along the refusal direction, making it no longer reliable for identifying and refusing harmful inputs. We refer to this failure mode as Safety Geometry Collapse. We quantify it through conditional refusal separability and show that stronger modality-induced drift is consistently associated with weaker refusal separability and higher attack success rates. We then validate the causal role of modality-induced drift through a fixed-strength activation intervention: counteracting the estimated drift restores refusal separability and improves multimodal safety. After drift correction, we further observe self-rectification, where the model recovers its ability to recognize and refuse harmful multimodal inputs during forward dynamics. This effect also provides an internal signal of the model's perceived harmfulness of each input. Motivated by this signal, we propose ReGap, a training-free inference-time method that adaptively corrects modality drift using self-rectification. Experiments across multiple multimodal safety benchmarks and utility benchmarks demonstrate the effectiveness of ReGap, which significantly improves the safety of MLLMs without compromising general capabilities. Our findings highlight representation-level modality alignment as a crucial direction for real-time safety improvement and for building safer, more reliable MLLMs.
匹配关键词: safety
---

[ACADEMIC - ARXIV]
标题: Scenario Generation in Roundabouts with Adjustable Interaction Intensity
作者: Li Li, Till Temmen, Tobias Brinkmann, Björn Krautwig, Markus Eisenbarth, Jakob Andert
链接: https://arxiv.org/abs/2605.18026v1
完整摘要: Roundabouts, characterized by frequent merging and yielding interactions, remain a safety-critical corner case for the development and testing of intelligent driving functions. However, extracting sufficient near-critical scenarios from naturalistic data is inefficient. Most existing scenario generation methods provide limited controllability over interaction intensity and criticality, making systematic safety testing and detailed analysis difficult. This paper presents an interaction-aware roundabout scenario generator with continuously adjustable interaction intensity. Geometric routes and temporal progress profiles are first decoupled and mapped to latent codes using pretrained autoencoders. Conditional latent generation is then performed with Wasserstein Generative Adversarial Networks (WGAN) to generate scenarios. Yielding is modeled as a controllable timing intervention via a compact yield code during the approach-to-entry segment, where interaction intensity is modulated by scaling the code with a factor $λ$. Results demonstrate enhanced timing-latent fidelity and plausible interaction responses compared to a baseline model. Under criticality-calibrated scaling, increasing $λ$ expands the safety margin, providing a scalable and controlled testing mechanism.
匹配关键词: safety
---

[ACADEMIC - ARXIV]
标题: Uncertainty Reliability Under Domain Shift: An Investigation for Data-Driven Blood Pressure Estimation in Photoplethysmography
作者: Mohammad Moulaeifard, Ciaran Bench, Philip J. Aston, Nils Strodthoff
链接: https://arxiv.org/abs/2605.18008v1
完整摘要: Uncertainty quantification (UQ) is critical for safety-critical domains like healthcare, yet it is rarely evaluated under realistic out-of-distribution (OOD) conditions. Here, we assessed predictive performance and uncertainty reliability for deep learning-based blood pressure (BP) estimation from photoplethysmography (PPG) signals under both in-distribution (ID) and OOD settings. Using an XResNet1D-50 trained on PulseDB and tested on four external datasets, we compared deep ensembles (DE) and Monte Carlo dropout (MCD) with Gaussian negative log-likelihood (GNLL) and mean squared error (MSE) losses, optionally followed by post-hoc recalibration via conformal prediction (CP), temperature scaling (TS), and isotonic regression (IR). The key findings of our study are as follows: (1) DE provides stronger predictive robustness under domain shift than MCD, an advantage that becomes clear primarily under external shift. (2) Recalibrated GNLL-based methods yield the best uncertainty calibration (e.g., GNLL+DE+CP for systolic blood pressure (SBP), GNLL+DE+TS for diastolic blood pressure (DBP)), while MSE-based uncertainty requires recalibration to become practically useful. (3) Across settings, CP and TS offer the most consistent gains, with IR remaining competitive in several cases. Overall, our results identify DE-based methods as most robust for predictive performance under domain shift, GNLL as strongest for native UQ, and recalibration as essential for making MSE-based uncertainty practical. These findings highlight the need to jointly assess predictive accuracy and calibration on external data for trustworthy cuffless BP estimation
匹配关键词: safety
---

[ACADEMIC - ARXIV]
标题: Verify-Gated Completion as Admission Control in a Governed Multi-Agent Runtime: A Bounded Architecture Case Study
作者: Hai-Duong Nguyen, The-Xuan Tran
链接: https://arxiv.org/abs/2605.17998v1
完整摘要: As multi-agent systems move from short interactions to tool-using workflows with specialized roles and persistent state, completion becomes a runtime-control problem rather than a purely generative one. This preprint studies verify-gated completion as an admission-control pattern for governed multi-agent runtimes: agents may propose completion, but a read-only verifier decides whether the claim is admitted. Ambiguous or weakly evidenced cases resolve fail-closed, while packetized state and event traces preserve an audit path. We examine one bounded reference implementation and ask what the released evidence can support about auditable, verify-gated completion. In the released verify-completed slice, the known-outcome invoked-event verify success share was 1,791/1,800 = 99.5%. This is an accounting measure over invoked verification events, not a task-completion, production-reliability, or benchmark-success rate. Task-level verify coverage is not computable; 1,762/1,801 rows came from one high-volume reporting cluster; and only 17 events were production-classified. A shadow Policy/Governance Verifier evaluation showed 1,526/1,548 = 98.58% rule agreement, 0/1,526 false-success among safe-to-proceed predictions, and blocked precision of 2/518 = 0.39%, so it remains advisory. The evidence supports a narrow conclusion: under observed conditions, a read-only verify gate plus packetized admission records made completion decisions inspectable and fail-closed. Claims about deployed operation, safety guarantees, outcome gains, task-level coverage, recovery effectiveness, or external validity remain outside scope.
匹配关键词: safety
---

[ACADEMIC - ARXIV]
标题: Babel: Jailbreaking Safety Attention via Obfuscation Distribution Optimized Sampling
作者: Ziwei Wang, Jing Chen, Ruichao Liang, Zhi Wang, Yebo Feng, Ju Jia, Ruiying Du, Cong Wu, Yang Liu
链接: https://arxiv.org/abs/2605.17971v1
完整摘要: Despite rigorous safety alignment, Large Language Models (LLMs) remain vulnerable to jailbreak attacks. Existing black-box methods often rely on heuristic templates or exhaustive trials, lacking mechanistic interpretability and query efficiency. In this study, we investigate an intrinsic vulnerability in the safety mechanisms of LLMs, where safety alignment relies on a small set of sparsely distributed attention heads, leaving much of the representational space weakly monitored. We formalize this phenomenon with a mathematical jailbreaking model that characterizes the delicate boundary of effective text obfuscation and analytically explains observed jailbreak behaviors. Guided by this model, we propose Babel, an efficient black-box attack framework that exploits the identified safety gap through systematic obfuscation sampling with iterative, feedback-driven distribution refinement, enabling reliable and high-success jailbreak attacks without access to model internals. Comprehensive evaluations on frontier commercial models demonstrate that Babel achieves state-of-the-art attack success rates and superior query efficiency. Specifically, compared to state-of-the-art methods, Babel increases the attack success rate on GPT-4o from 41.33% to 82.67% and on Claude-3-5-haiku from 38.33% to 78.33% within an average of 40 queries, providing a robust red-teaming methodology for LLMs safety research.
匹配关键词: safety
---

