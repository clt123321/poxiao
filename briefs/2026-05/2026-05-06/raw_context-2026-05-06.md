# 破晓 PoXiao — 原始数据 (Raw Context)
生成时间: 2026-05-06 02:00 UTC
================================================================================

[RSS:Reddit LocalLLaMA (社区共识)]
Gemma 4 MTP released
https://www.reddit.com/r/LocalLLaMA/comments/1t4jq6h/gemma_4_mtp_released/
Blog post: https://blog.google/innovation-and-ai/technology/developers-tools/multi-token-prediction-gemma-4/ MTP draft models: https://huggingface.co/google/gemma-4-31B-it-assistant https://huggingface.co/google/gemma-4-26B-A4B-it-assistant https://huggingface.co/google/gemma-4-E4B-it-assistant http
---

[RSS:Reddit LocalLLaMA (社区共识)]
DeepSeek V4 being 17x cheaper got me to actually measure what I send to cloud vs what I could run locally. the results are stupid.
https://www.reddit.com/r/LocalLLaMA/comments/1t4s6g2/deepseek_v4_being_17x_cheaper_got_me_to_actually/
That foodtruck bench post showing deepseek v4 matching gpt-5.2 at 17x cheaper got me thinking. if frontier cloud models are that overpriced for equivalent quality, how much of my daily work even needs cloud at all? Ran my normal coding workflow for 10 days. every task got logged: what it was, tokens
---

[RSS:Reddit LocalLLaMA (社区共识)]
Heretic 1.3 released: Reproducible models, integrated benchmarking system, reduced peak VRAM usage, broader model support, and more
https://www.reddit.com/r/LocalLLaMA/comments/1t4hwup/heretic_13_released_reproducible_models/
Dear fellow Llamas, it is my distinct pleasure to announce the immediate availability of version 1.3 of Heretic ( https://github.com/p-e-w/heretic ), the leading software for removing censorship from language models. This was a long and eventful release cycle, during which Heretic became a high-prof
---

[RSS:Reddit LocalLLaMA (社区共识)]
12M Context Window and some some sprinkle of lies?
https://www.reddit.com/r/LocalLLaMA/comments/1t4wv6c/12m_context_window_and_some_some_sprinkle_of_lies/
Spent some time on the SubQ launch today. Some things don't line up. Tweet sells a 12M context window. Blog says 12M is a research result and the production model is SubQ 1M-Preview. Those are different things, my senses already tingling! RULER is reported at 128K, that's well below where sparse att
---

[RSS:Reddit LocalLLaMA (社区共识)]
Dense Model Shoot-Off: Gemma 4 31B vs Qwen3.6/5 27B... Result is Slower is Faster.
https://www.reddit.com/r/LocalLLaMA/comments/1t4nkez/dense_model_shootoff_gemma_4_31b_vs_qwen365_27b/
Not affiliated with Kaitchup, but a fan of their testing. I was looking forward to this article... and it did not disappoint. Lots of free info in the link. The juicy part is behind a paywall. I'll respect that, but the short of it is: It's showing that the Qwen's are more benchmaxxed, and Gemma 4 3
---

[RSS:Reddit LocalLLaMA (社区共识)]
ProgramBench: Can we really rebuild huge binaries from scratch? (doesn't look like it)
https://www.reddit.com/r/LocalLLaMA/comments/1t4j4s9/programbench_can_we_really_rebuild_huge_binaries/
There's been quite a few case studies recently on agents building whole programs from scratch, but most of them test a single or just a few projects with hand-tuned setups. We've spent the last couple of months formalizing this setting and building a benchmark of 200 tasks while doubling down on tes
---

[RSS:Reddit LocalLLaMA (社区共识)]
MTP on strix halo with llama.cpp (PR #22673)
https://www.reddit.com/r/LocalLLaMA/comments/1t4uj9h/mtp_on_strix_halo_with_llamacpp_pr_22673/
I saw a post about incoming MTP support in llama.cpp so i tried it out on a AI max 395 with 128GB DDR5 8000: I rebuilt the radv container from https://github.com/kyuz0/amd-strix-halo-toolboxes with that PR : https://github.com/ggml-org/llama.cpp/pull/22673 I ran that GGUF : https://huggingface.co/am
---

[RSS:Reddit LocalLLaMA (社区共识)]
I know this isn’t technically an LLM but OmniVoice is FUCKING AMAZING.
https://www.reddit.com/r/LocalLLaMA/comments/1t4rst5/i_know_this_isnt_technically_an_llm_but_omnivoice/
Literally one shot voice cloning and it’s literally so easy. What the FUCK. It’s everything I’ve ever dreamed of. &#32; submitted by &#32; /u/Borkato [link] &#32; [comments]
---

[RSS:Reddit LocalLLaMA (社区共识)]
Why run local? Count the money
https://www.reddit.com/r/LocalLLaMA/comments/1t4qwzf/why_run_local_count_the_money/
I’m not a coder, but I run local models. I gave in to agent hype (I was building my own, but there is so much to do) and installed Hermes. Running with Qwen-397b out of a 2 spark cluster. So…I asked Hermes today to tally the token count, and the result…200 million tokens. In 5 days. At this rate, us
---

[RSS:Reddit LocalLLaMA (社区共识)]
US and tech firms strike deal to review AI models for national security before public release | Technology
https://www.reddit.com/r/LocalLLaMA/comments/1t4tj11/us_and_tech_firms_strike_deal_to_review_ai_models/
&#32; submitted by &#32; /u/Merchant_Lawrence [link] &#32; [comments]
---

[RSS:Reddit LocalLLaMA (社区共识)]
Running a 26B LLM locally with no GPU
https://www.reddit.com/r/LocalLLaMA/comments/1t4e046/running_a_26b_llm_locally_with_no_gpu/
This is crazy. I've been running local LLMs on CPU only for awhile now and have great results with 12B models running on an i5-8500 and only 32GB of RAM with no GPU. But I've got a version of Gemma4 26B running really fast on the same machine which isn't even breaking a sweat. It is simply amazing w
---

[RSS:Reddit LocalLLaMA (社区共识)]
Use Qwen3.6 right way -> send it to pi coding agent and forget
https://www.reddit.com/r/LocalLLaMA/comments/1t4ji36/use_qwen36_right_way_send_it_to_pi_coding_agent/
https://preview.redd.it/z4b01gklaczg1.jpg?width=1080&amp;format=pjpg&amp;auto=webp&amp;s=3cefa63d5d15eac5eedbb39ef19d6c476b22ae64 Just a reminder, the harness you use can makes a huge diffrence (your llm client and interface bascially), It's is way more important than people think, I'm using pi.dev 
---

[RSS:Reddit LocalLLaMA (社区共识)]
DeepSeek V4 Pro matches GPT-5.2 on FoodTruck Bench, our agentic benchmark — 10 weeks later, ~17× cheaper
https://www.reddit.com/r/LocalLLaMA/comments/1t47qbw/deepseek_v4_pro_matches_gpt52_on_foodtruck_bench/
Tested DeepSeek V4 Pro on FoodTruck Bench — our 30-day agentic benchmark where models run a food truck via 34 tools (locations, pricing, inventory, staff, weather, events) with persistent memory and daily reflection. First Chinese model to land in the frontier tier on our benchmark. Tied with Grok 4
---

[RSS:Reddit LocalLLaMA (社区共识)]
Common and Obscure Models and Ways to Find Them [ Human Written ]
https://www.reddit.com/r/LocalLLaMA/comments/1t4vmgu/common_and_obscure_models_and_ways_to_find_them/
I've been on a binge finding uses for local AI on my machine outside of general LLM usage as I'm not sure what other sub discovery of these things should go on. Here's a collection of my findings. I'd appreciate other contributions that are off the beaten path or collections. Somewhat &quot;common&q
---

[RSS:Reddit LocalLLaMA (社区共识)]
Supercharging LLM inference on Google TPUs: Achieving 3X speedups with diffusion-style speculative decoding- Google Developers Blog
https://www.reddit.com/r/LocalLLaMA/comments/1t4jehc/supercharging_llm_inference_on_google_tpus/
&#32; submitted by &#32; /u/eternviking [link] &#32; [comments]
---

[RSS:Reddit LocalLLaMA (社区共识)]
Qwen3.6 merged chat template from allanchan339 and froggeric
https://www.reddit.com/r/LocalLLaMA/comments/1t4cev0/qwen36_merged_chat_template_from_allanchan339_and/
Hi, recently froggeric and allanchan339 released enhanced/fixed template for Qwen3.6 each one addressing different topics. I didn't know which one to use so I merged both with the help of Claude Opus to have the best of both. I've uploaded it to this gist https://gist.github.com/fakezeta/9e8e039c603
---

[RSS:Reddit LocalLLaMA (社区共识)]
Claude Code @ Opus 4.7 vs OpenCode @ qwen3.6:27b. Both shipped a playable cozy roguelite.
https://www.reddit.com/r/LocalLLaMA/comments/1t4vb57/claude_code_opus_47_vs_opencode_qwen3627b_both/
&#32; submitted by &#32; /u/rm-rf-rm [link] &#32; [comments]
---

[RSS:Reddit LocalLLaMA (社区共识)]
Reducing MP3 compression bias in music datasets via codec-aware reconstruction
https://www.reddit.com/r/LocalLLaMA/comments/1t4pilx/reducing_mp3_compression_bias_in_music_datasets/
I built a tool to improve decoding of MP3 files (LAME encoded) reducing systematic codec induced bias in audio datasets. Rather than denoising, it treats reconstruction as a disambiguation problem: MP3 encoding is non-injective, so the observed signal corresponds to a distribution of plausible origi
---

[RSS:Reddit LocalLLaMA (社区共识)]
I guess we expect that at some point RAM prices will start going back (close) to "normal", right? but what about GPUs?
https://www.reddit.com/r/LocalLLaMA/comments/1t4r5qi/i_guess_we_expect_that_at_some_point_ram_prices/
I'm trying to refrain my self from buying an, extremely expensive, RTX 5090 FE (I don't really need it, but... I want one), because... it's extremely expensive ATM, and I was thinking &quot;I just wait a few months hoping for prices to go down&quot;. But then I started thinking &quot;will they?&quot
---

[RSS:Reddit LocalLLaMA (社区共识)]
vibevoice.cpp: Microsoft VibeVoice (TTS + long-form ASR with diarization) ported to ggml/C++, runs on CPU/CUDA/Metal/Vulkan, no Python at inference
https://www.reddit.com/r/LocalLLaMA/comments/1t48fkt/vibevoicecpp_microsoft_vibevoice_tts_longform_asr/
A few weeks ago I shipped vibevoice.cpp , a pure-C++ ggml port of Microsoft VibeVoice (the speech-to-speech model with voice cloning, https://github.com/microsoft/VibeVoice ). Wanted to post a follow-up here because we're at a point where the engine has grown well past &quot;first-pass port&quot; an
---

[RSS:Reddit LocalLLaMA (社区共识)]
Current state of local research tools as of May 2026
https://www.reddit.com/r/LocalLLaMA/comments/1t4e83m/current_state_of_local_research_tools_as_of_may/
I was thinking, that some folks in this community will be interested to see what current options are on local deep research field. So I spent some time to collect everything I could find together. Enjoy. TLDR: the most healthiest and local-friendly projects are &quot;GPT Researcher&quot; by assafelo
---

[RSS:Reddit LocalLLaMA (社区共识)]
Peanut - Text to Image Model (Open Weights coming soon)
https://www.reddit.com/r/LocalLLaMA/comments/1t45g3l/peanut_text_to_image_model_open_weights_coming/
A new anonymous model debuts at #8 in the Artificial Analysis Text to Image Arena! Peanut’s weights are expected to be released soon, which would make it the leading Text to Image Open Weights Model. Peanut is positioned to be the new leading open weights Text to Image model, surpassing Z-Image Turb
---

[RSS:Reddit LocalLLaMA (社区共识)]
Qwen3.6 27B FP8 runs with 200k tokens of BF16 KV cache at 80 TPS on a single RTX 5000 PRO 48GB
https://www.reddit.com/r/LocalLLaMA/comments/1t46klu/qwen36_27b_fp8_runs_with_200k_tokens_of_bf16_kv/
----START HUMAN TEXT---- Hi all, I've seen a bunch of posts about squeezing 27B onto a 24GB card and all the quantization tricks involved in doing so. It's all amazing work, but at the end of the day a quantized model with quantized KV will inevitably compound errors faster than non-quantized ones, 
---

[RSS:Reddit MachineLearning (学术风向)]
Struggling to reproduce paper results before improving them — stuck below reported accuracy [R]
https://www.reddit.com/r/MachineLearning/comments/1t4dkew/struggling_to_reproduce_paper_results_before/
I’m a PhD student working in AI/computer vision, and I’ve hit a frustrating wall with a project. My supervisor asked me to improve the accuracy of a published paper. My first step has been to faithfully reproduce their results before trying any modifications. The issue is I can’t even match their re
---

[RSS:Reddit MachineLearning (学术风向)]
Production AI very different from the demos [D]
https://www.reddit.com/r/MachineLearning/comments/1t4mzm3/production_ai_very_different_from_the_demos_d/
Moved an AI feature into production a few months ago and the cost profile has been a constant surprise since so the demos and the early prototypes ran cheap because the volume was tiny + the prompts were short but when it hit traffic the token usage scaled a lot. I think it was partly because custom
---

[RSS:Reddit MachineLearning (学术风向)]
NeurIPS Submission Number [D]
https://www.reddit.com/r/MachineLearning/comments/1t4oykt/neurips_submission_number_d/
Hey guys, Just saw that NeurIPS this year might be exceeding 40k, what submission number did you get? The max I know of was 29k, that was 24 hours ago &#32; submitted by &#32; /u/StriderKing27 [link] &#32; [comments]
---

[RSS:Reddit MachineLearning (学术风向)]
Question about PLS-DA hyperparameter tuning [R]
https://www.reddit.com/r/MachineLearning/comments/1t4pe8c/question_about_plsda_hyperparameter_tuning_r/
Hi all! I am a bioinformatician and I am working on learning some ML tools for some disease/biomarker stuff. I am working with sparse PLS-DA at the moment. Before actually tuning the model, I run on overall global model (without sparsity) to get an idea of what my data looks like and to get to a sta
---

[RSS:Reddit MachineLearning (学术风向)]
TritonSigmoid: A fast, padding-aware sigmoid attention kernel for GPUs [R]
https://www.reddit.com/r/MachineLearning/comments/1t4kalf/tritonsigmoid_a_fast_paddingaware_sigmoid/
We are open-sourcing TritonSigmoid — a fast, padding-aware sigmoid attention kernel for GPUs. We built this for single-cell foundation models, where every cell is represented as a sequence of genes. A single gene can be regulated by multiple transcription factors at once. Softmax forces them to comp
---

[RSS:Reddit MachineLearning (学术风向)]
Competition - League of Robot Runners 2026: Multi-robot coordination under uncertainty [N]
https://www.reddit.com/r/MachineLearning/comments/1t4sjr7/competition_league_of_robot_runners_2026/
Hello ML and RL community We are inviting participants to the League of Robot Runners (LoRR) 2026: https://www.leagueofrobotrunners.org Co-located with AAMAS 2026, LoRR is a research competition on large-scale multi-robot coordination. These are important problems in a number of areas including logi
---

[RSS:Reddit MachineLearning (学术风向)]
Anomaly Detection Belongs in Your Database — built SIMD-accelerated isolation forests into Stratum's SQL engine [P]
https://www.reddit.com/r/MachineLearning/comments/1t4riem/anomaly_detection_belongs_in_your_database_built/
We added native anomaly detection in Stratum, our columnar analytics engine for the JVM. Train and score isolation forest models entirely from SQL — no Python, no export pipeline: SELECT * FROM transactions WHERE ANOMALY_SCORE('fraud_model') &gt; 0.7; 6 microseconds per transaction, SIMD-accelerated
---

[RSS:Reddit MachineLearning (学术风向)]
Radar Engineer to Autonomy/AI [D]
https://www.reddit.com/r/MachineLearning/comments/1t4ombd/radar_engineer_to_autonomyai_d/
Hi all, I’ve spent the last 3 years working on Radar Perception for a legacy automotive project in Germany. My background is an MSc in Robotics &amp; AI. Currently, I spend my time analyzing point clouds and SNR distributions to debug failures. It’s mathematically complex, but I’m not implementing a
---

[RSS:Reddit MachineLearning (学术风向)]
Charting the AI Perception Gap: Across 71 scenarios, AI experts (N=119) and the public (N=1100) have differing views on the risks, benefits, and value of AI. More importantly, AI experts discount the influence of risks stronger than the public does when forming their value judgments [R]
https://www.reddit.com/r/MachineLearning/comments/1t4kvb2/charting_the_ai_perception_gap_across_71/
https://preview.redd.it/evw6ah88kczg1.png?width=1024&amp;format=png&amp;auto=webp&amp;s=be8bafe0099c362a187489f95cbfa5398f537107 Abstract: Artificial intelligence (AI) is reshaping society, raising questions about trust, risks, and the asymmetries between public and academic perspectives. We examine
---

[RSS:Reddit MachineLearning (学术风向)]
Visual graph classification for blockchain security: Experiences fine-tuning Qwen2-VL on AMD MI300X [D]
https://www.reddit.com/r/MachineLearning/comments/1t4dcej/visual_graph_classification_for_blockchain/
Hi everyone, I’ve been working on a computer vision approach to a specific security problem in the &quot;Agentic Economy&quot;: identifying malicious transaction patterns that are mathematically obfuscated but topologically distinct. The Problem Traditional rule-based security engines and even stand
---

[RSS:Reddit MachineLearning (学术风向)]
NeurIPS openreview - can I upload paper pdf after abstract deadline or should I upload something first to be able to update it later? [D]
https://www.reddit.com/r/MachineLearning/comments/1t46wzz/neurips_openreview_can_i_upload_paper_pdf_after/
Hi, I have a question about openreview procedure as in the title. It’s my first time submitting to neurips so I’m unsure. Also for code URL submission can I do the same or should I put an URL in first? And side question, but does anyone know how neurips prevent people from pushing codes after paper 
---

[RSS:Reddit MachineLearning (学术风向)]
Fixing Unsupervised Hyperbolic Contrastive Loss [D]
https://www.reddit.com/r/MachineLearning/comments/1t45ggk/fixing_unsupervised_hyperbolic_contrastive_loss_d/
Hello all, I am trying to implement Unsupervised Hyperbolic Contrastive Loss on the ImageNet-1k dataset. My results show that simple Euclidean unsupervised contrastive loss is much better than the hyperbolic version. Please help me understand the problem. I am using expmap() and projx() to ensure th
---

[RSS:Ars Technica AI (深度技术)]
Widely used Daemon Tools disk app backdoored in monthlong supply-chain attack
https://arstechnica.com/security/2026/05/widely-used-daemon-tools-disk-app-backdoored-in-monthlong-supply-chain-attack/
Daemon Tools users: It's time to check your machines for stealthy infections, stat.
---

[RSS:Ars Technica AI (深度技术)]
Why Reddit blocked my daily visit to its mobile website
https://arstechnica.com/information-technology/2026/05/why-reddit-blocked-my-daily-visit-to-its-mobile-website/
Reddit REALLY wants you to use its app.
---

[RSS:Reddit Jobs & Careers (职场动态)]
Resume Advice Thread - May 05, 2026
https://www.reddit.com/r/cscareerquestions/comments/1t47vi7/resume_advice_thread_may_05_2026/
Please use this thread to ask for resume advice and critiques. You should read our Resume FAQ and implement any changes from that before you ask for more advice. Abide by the rules, don't be a jerk. Note on anonomyizing your resume: If you'd like your resume to remain anonymous, make sure you blank 
---

[RSS:Reddit Jobs & Careers (职场动态)]
How to be a quiet and good engineer?
https://www.reddit.com/r/cscareerquestions/comments/1t4igc8/how_to_be_a_quiet_and_good_engineer/
There's a Principal Architect on my team. Late 50s, 30+ years at the same company, still writing code every day. He knows ML, DevOps, backend, architecture. But carries it all very quietly. A junior once told him he wants to be an expert like him someday. His reply: &gt; &quot;I see myself as an Adv
---

[RSS:Reddit Jobs & Careers (职场动态)]
PayPal to Cut 20% of Staff Amid Turnaround Push
https://www.reddit.com/r/cscareerquestions/comments/1t4sznn/paypal_to_cut_20_of_staff_amid_turnaround_push/
https://www.wsj.com/business/earnings/paypal-to-cut-costs-after-profit-falls-dc42baf9?reflink=desktopwebshare\_permalink From the article: The planned reduction would amount to 4,760 positions based on the 23,800 employees PayPal reported having at the end of 2025. The cost-cutting efforts are expec
---

[RSS:Reddit Jobs & Careers (职场动态)]
How to handle AI Psychosis?
https://www.reddit.com/r/cscareerquestions/comments/1t4u6z2/how_to_handle_ai_psychosis/
I think I am starting to lose my mind. 7 yoe and mscs that works in financial industry. Of course our team did two rounds of layoffs in the last in the last six months and later came out as an “AI first team”. Today, I read coinbase is laying off developers because product managers who are not techn
---

[RSS:Reddit Jobs & Careers (职场动态)]
my manager wants me to build an ai prototype but gave me a $50/month cloud budget
https://www.reddit.com/r/cscareerquestions/comments/1t4ape3/my_manager_wants_me_to_build_an_ai_prototype_but/
i am a mid level full stack dev and my boss just assigned me to add generative ai to our main product. the problem is he refuses to approve any significant aws budget for renting gpus. he thinks i can just run everything on a standard ec2 instance. i tried explaining the hardware requirements for ev
---

[RSS:Reddit Jobs & Careers (职场动态)]
Employers, be honest: Does a portfolio matter? (2026 edition)
https://www.reddit.com/r/cscareerquestions/comments/1t4gswl/employers_be_honest_does_a_portfolio_matter_2026/
(Ideally, I'd like top-level comments to be from people who are literally in a position to hire at tech companies right now, rather than people venturing their opinions and guesses.) I'd like to make a post similar to this one from three years ago . In the era of AI, do portfolios of software projec
---

[RSS:Reddit Jobs & Careers (职场动态)]
Stay for a possible promotion next year or take a 1-year Apple contract at much higher pay?
https://www.reddit.com/r/cscareerquestions/comments/1t4mf0h/stay_for_a_possible_promotion_next_year_or_take_a/
8 YOE as backend and I’m stuck between two pretty different options. I’m currently an FTE software developer making $140k at a company I’ve been with for a few years. There’s been talk of a promotion and raise, but after discussing it with my manager/director, they said the earliest they can do $160
---

[RSS:Reddit Jobs & Careers (职场动态)]
Quit previous new-grad job at 8 months for this one, and now got laid off after 2.5 months. How will this look?
https://www.reddit.com/r/cscareerquestions/comments/1t4vad1/quit_previous_newgrad_job_at_8_months_for_this/
For context - I work as a SWE in Toronto Canada. I graduated in April 2025, just about a year ago, and then started working at company A from June 2025 onwards until February 2026. I left company A so I could join company B which i had previously done internships with (during Jan-Apr 2024 and Sep-De
---

[RSS:Reddit Jobs & Careers (职场动态)]
Do layoffs target less experienced SWEs first?
https://www.reddit.com/r/cscareerquestions/comments/1t44j82/do_layoffs_target_less_experienced_swes_first/
Currently E3 at Meta. Wondering if this level would be disproportionately affected by the upcoming layoff. I know levels are in consideration but I’m wondering what has been true in the past. Tech companies laid off a lot 2022-present. During these layoffs, are entry level engineers affected the mos
---

[RSS:Reddit Jobs & Careers (职场动态)]
Fizzled with going above and beyond
https://www.reddit.com/r/cscareerquestions/comments/1t4cdix/fizzled_with_going_above_and_beyond/
I feel more and more the need to do the bare minimum than actually putting passion into what I do at my job. For context, I am a junior developer for a private bank, that wears multiple hats (BA, QA, Dev, Admin, and sometimes coordinating with contractor's work). I have always believed in documentat
---

[RSS:Reddit Jobs & Careers (职场动态)]
if you’re making open source software, can you put your own terms in the LICENSE, or do you have to use a pre-issued one?
https://www.reddit.com/r/cscareerquestions/comments/1t4jwh9/if_youre_making_open_source_software_can_you_put/
Just wondering if I can add terms to a LICENSE file. I specifically don’t really want it to be used by certain industries &#32; submitted by &#32; /u/Dreadsin [link] &#32; [comments]
---

[RSS:Reddit Jobs & Careers (职场动态)]
New LLM Benchmarking
https://www.reddit.com/r/cscareerquestions/comments/1t4u6xa/new_llm_benchmarking/
https://programbench.com Maybe we aren’t completely cooked after all &#32; submitted by &#32; /u/SimilarIntern923 [link] &#32; [comments]
---

[RSS:Reddit Jobs & Careers (职场动态)]
What should I study/learn if I have a month basically free that’ll will help me get back into tech?
https://www.reddit.com/r/cscareerquestions/comments/1t4xt2e/what_should_i_studylearn_if_i_have_a_month/
I know this is a broad question I asking me what subjectively that like you think would be the best. I basically got addicted to alcohol and benzos for the past 2-3 years. I’ve had times of sobriety in between where I kept up to date with how things are changing so I’m not starting from the beginnin
---

[RSS:Reddit Jobs & Careers (职场动态)]
Red hat sponsoring visa for interns in 2026?
https://www.reddit.com/r/cscareerquestions/comments/1t4xqlf/red_hat_sponsoring_visa_for_interns_in_2026/
hi all, sorry if this is the wrong sub to post, but I have an offer from red hat, though I can’t find any info on if they’re hiring interns on CPT in 2026 (they didn’t ask me what visa status I have). If anyone has insights please let me know, thanks! &#32; submitted by &#32; /u/badassrajesh508 [lin
---

[RSS:Reddit Jobs & Careers (职场动态)]
For those that say “tailor for each application” does that not often mean outright lying?
https://www.reddit.com/r/cscareerquestions/comments/1t4o5so/for_those_that_say_tailor_for_each_application/
I want to preface this by saying I am not disagreeing with that. It is a genuine face value question. I’ve always tried to stand firm in not exaggerating or lying about my skills but in this age you kind of have to. No one can possibly know every skill they are tailoring their resume towards for eac
---

[RSS:Reddit Jobs & Careers (职场动态)]
What's up with all these DataAnnotations job postings?
https://www.reddit.com/r/cscareerquestions/comments/1t4kzm9/whats_up_with_all_these_dataannotations_job/
I don't know if it's a legit company, but I'm seeing tens of remote job postings from them. &#32; submitted by &#32; /u/cev4 [link] &#32; [comments]
---

[RSS:Reddit Jobs & Careers (职场动态)]
Online AI courses that are beneficial when seeking new positions.
https://www.reddit.com/r/cscareerquestions/comments/1t4w1t9/online_ai_courses_that_are_beneficial_when/
I have 20+ years of experience in software development, mainly working for Microsoft doing systems engineering projects. I have been out of the field doing a career transition to commercial pilot but due to incredibly slow hiring in that field I need to transition back to development. It seems that 
---

[RSS:Reddit Jobs & Careers (职场动态)]
Will a concentration in entrepreneurship hurt my job prospects?
https://www.reddit.com/r/cscareerquestions/comments/1t4vic1/will_a_concentration_in_entrepreneurship_hurt_my/
I am in MCIT online getting a masters in cs and I havent been able to get an internship despite thousands of applications over the last 5 years. I'm not really great at coding and not super willing or able to be extraordinary in the field and am thinking of just taking all the electives that require
---

[RSS:Reddit Jobs & Careers (职场动态)]
job search has been rough :(
https://www.reddit.com/r/cscareerquestions/comments/1t4v3w3/job_search_has_been_rough/
hey all, the entry-level job search has been kinda brutal lately. feels like everything wants a few years of experience and there just aren’t that many roles I got tired of scrolling through job boards every day, so i tried building something for myself that matches my resume to open roles and sends
---

[RSS:Reddit Jobs & Careers (职场动态)]
How helpful is it for your first job prospects to have experience in Machine Learning from an internship?
https://www.reddit.com/r/cscareerquestions/comments/1t4tjg0/how_helpful_is_it_for_your_first_job_prospects_to/
I will be doing a summer internship here starting next month at my university working with massive datasets that require using ML to help with building their application on forever chemicals and finding where there might be higher concentrations so they know better where to pull them out of the grou
---

[RSS:Reddit Jobs & Careers (职场动态)]
What to do?
https://www.reddit.com/r/cscareerquestions/comments/1t4t6fz/what_to_do/
I graduated recently with a bachelors and computer science from WGU. And have been struggling brutally to find any tech job even IT support. My initial plan was cyber security but with the job market being as it is, I realized I have to do something more entry-level level. I also have comptia securi
---

[RSS:Reddit Jobs & Careers (职场动态)]
I’m so bad at this field,
https://www.reddit.com/r/cscareerquestions/comments/1t46mo5/im_so_bad_at_this_field/
It doesn’t help that everyone around me (friends, family, classmates) seems to be alright with it. The programming makes sense some of, probably most of, the time (like OOP, hardware and software, even things like systems programming) it’s like I’m the only person who struggles with it. It genuinely
---

[HACKERNEWS]
.de TLD offline due to DNSSEC?
https://dnssec-analyzer.verisignlabs.com/nic.de
Score: 522 | Comments: 242
---

[HACKERNEWS]
Accelerating Gemma 4: faster inference with multi-token prediction drafters
https://blog.google/innovation-and-ai/technology/developers-tools/multi-token-prediction-gemma-4/
Score: 444 | Comments: 198
---

[HACKERNEWS]
Computer Use is 45x more expensive than structured APIs
https://reflex.dev/blog/computer-use-is-45x-more-expensive-than-structured-apis/
Score: 309 | Comments: 175
---

[HACKERNEWS]
Three Inverse Laws of AI
https://susam.net/inverse-laws-of-robotics.html
Score: 351 | Comments: 244
---

[HACKERNEWS]
EEVblog: The 555 Timer is 55 years old [video]
https://www.youtube.com/watch?v=6JhK8iCQuqI
Score: 220 | Comments: 54
---

[HACKERNEWS]
Write some software, give it away for free
https://nonogra.ph/write-some-software-give-it-away-for-free-05-05-2026
Score: 127 | Comments: 95
---

[HACKERNEWS]
Why most product tours get skipped
https://productonboarding.com/articles/why-product-tours-get-skipped
Score: 65 | Comments: 55
---

[HACKERNEWS]
NPR finds "no sign" of Polymarket at its Panama HQ address
https://www.npr.org/2026/05/05/nx-s1-5807918/polymarket-panama-prediction-market
Score: 198 | Comments: 88
---

[HACKERNEWS]
Show HN: Explore color palettes inspired by 3000 master painter artworks
https://paletteinspiration.com/
Score: 102 | Comments: 39
---

[HACKERNEWS]
GLM-5V-Turbo: Toward a Native Foundation Model for Multimodal Agents
https://arxiv.org/abs/2604.26752
Score: 112 | Comments: 23
---

[HACKERNEWS]
Zuckerberg 'personally authorized' Meta's copyright infringement, publishers say
https://apnews.com/article/meta-mark-zuckerberg-ai-publishers-lawsuit-llama-5609846d4d840014974a847b01079c32
Score: 122 | Comments: 35
---

[HACKERNEWS]
Agents for financial services and insurance
https://www.anthropic.com/news/finance-agents
Score: 196 | Comments: 149
---

[HACKERNEWS]
Show HN: Airbyte Agents – context for agents across multiple data sources
https://news.ycombinator.com/item?id=48023496
Score: 92 | Comments: 23
---

[HACKERNEWS]
I'm scared about biological computing
https://kuber.studio/blog/Reflections/I%27m-Scared-About-Biological-Computing
Score: 141 | Comments: 122
---

[HACKERNEWS]
Google Chrome silently installs a 4 GB AI model on your device without consent
https://www.thatprivacyguy.com/blog/chrome-silent-nano-install/
Score: 1242 | Comments: 840
---

[HACKERNEWS]
Today I've made the difficult decision to reduce the size of Coinbase by ~14%
https://twitter.com/brian_armstrong/status/2051616759145185723
Score: 256 | Comments: 362
---

[HACKERNEWS]
California farmers to destroy 420k peach trees following Del Monte bankruptcy
https://www.sfgate.com/centralcoast/article/usda-aid-california-farmers-22240694.php
Score: 264 | Comments: 320
---

[ACADEMIC - ARXIV]
标题: Feature-Augmented Transformers for Robust AI-Text Detection Across Domains and Generators
作者: Mohamed Mady, Johannes Reschke, Björn Schuller
链接: https://arxiv.org/abs/2605.03969v1
完整摘要: AI-generated text is nowadays produced at scale across domains and heterogeneous generation pipelines, making robustness to distribution shift a central requirement for supervised binary detectors. We train transformer-based detectors on HC3 PLUS and calibrate a single decision threshold by maximising balanced accuracy on held-out validation; this threshold is then kept fixed for all downstream test distributions, revealing domain- and generator-dependent error asymmetries under shift. We evaluate in-domain on HC3 PLUS, under cross-dataset transfer to the multi-domain, multi-generator M4 benchmark, and on the external AI-Text-Detection-Pile. Although base models achieve near-ceiling in-domain performance (up to 99.5% balanced accuracy), performance under shift is brittle and strongly model-dependent. Feature augmentation via attention-based linguistic feature fusion improves transfer, with our best model (DeBERTa-v3-base+FeatAttn) achieving 85.9% balanced accuracy on M4. Multi-seed experiments confirm high stability. Under the same fixed-threshold protocol, our model outperforms strong zero-shot baselines by up to +7.22 points. Category-level ablations further show that readability and vocabulary features contribute most to robustness under shift. Overall, these results demonstrate that feature augmentation and a modern DeBERTa backbone significantly outperform earlier BERT/RoBERTa models, while the fixed-threshold protocol provides a more realistic and informative assessment of practical detector robustness.
匹配关键词: swarm intelligence
---

[ACADEMIC - ARXIV]
标题: Label-Efficient School Detection from Aerial Imagery via Weakly Supervised Pretraining and Fine-Tuning
作者: Zakarya Elmimouni, Fares Fourati, Mohamed-Slim Alouini
链接: https://arxiv.org/abs/2605.03968v1
完整摘要: Accurate school detection is essential for supporting education initiatives, including infrastructure planning and expanding internet connectivity to underserved areas. However, many regions around the world face challenges due to outdated, incomplete, or unavailable official records. Manual mapping efforts, while valuable, are labor-intensive and lack scalability across large geographic areas. To address this, we propose a weakly supervised framework for school detection from aerial imagery that minimizes the need for human annotations while supporting global mapping efforts. Our method is specifically designed for low-data regimes, where manual annotations are extremely scarce. We introduce an automatic labeling pipeline that leverages sparse location points and semantic segmentation to generate infrastructure masks from which we generate bounding boxes. Using these automatically labeled images, we train our detectors on a first training stage to learn a representation of what schools look like, then using a small set of manually labeled images, we fine-tune the previously trained models on this clean dataset. This two stage training pipeline enables large-scale and strong detection in low-data setting of school infrastructure with minimal supervision. Our results demonstrate strong object detection performance, particularly in the low-data regime, where the models achieve promising results using only 50 manually labeled images, significantly reducing the need for costly annotations. This framework supports education and connectivity initiatives worldwide by providing an efficient and extensible approach to mapping schools from space. All models, training code and auto-labeled data will be publicly released to foster future research and real-world impact.
匹配关键词: swarm intelligence
---

[ACADEMIC - ARXIV]
标题: Inconsistent Databases and Argumentation Frameworks with Collective Attacks
作者: Yasir Mahmood, Jonni Virtema, Timon Barlag, Axel-Cyrille Ngonga Ngomo
链接: https://arxiv.org/abs/2605.03954v1
完整摘要: The connection between subset-maximal repairs for inconsistent databases involving various integrity constraints and acceptable sets of arguments within argumentation frameworks has recently drawn growing interest. In this paper, we contribute to this domain by establishing a new connection when integrity constraints (ICs) include denial constraints and local-as-view tuple-generating dependencies. It turns out that SET-based Argumentation Frameworks (SETAFs), an extension of Dung's argumentation frameworks (AFs) allowing collective attacks, are needed. It is known that subset-maximal repairs under denial constraints correspond to the naive extensions, which also coincide with the preferred and stable extensions in the resulting SETAFs. Our main findings establish that repairs under the considered fragment of tuple-generating dependencies correspond to the preferred extensions. Moreover, for these dependencies, additional preprocessing allows computing a unique extension that is stable and naive. Allowing both types of constraints breaks this relationship, and even the pre-processing does not help as only preferred semantics captures these repairs. Finally, while it is known that functional dependencies do not require set-based attacks, we prove the same regarding inclusion dependencies. Thus, one can translate inconsistent databases under these restricted classes of ICs to plain AFs with attacks only between arguments.
匹配关键词: swarm intelligence
---

[ACADEMIC - ARXIV]
标题: MOSAIC-Bench: Measuring Compositional Vulnerability Induction in Coding Agents
作者: Jonathan Steinberg, Oren Gal
链接: https://arxiv.org/abs/2605.03952v1
完整摘要: Coding agents often pass per-prompt safety review yet ship exploitable code when their tasks are decomposed into routine engineering tickets. The challenge is structural: existing safety alignment evaluates overt requests in isolation, leaving models blind to malicious end-states that emerge from sequenced compliance with innocuous-looking requests. We introduce MOSAIC-Bench (Malicious Objectives Sequenced As Innocuous Compliance), a benchmark of 199 three-stage attack chains paired with deterministic exploit oracles on deployed software substrates (10 web-application substrates, 31 CWE classes, 5 programming languages) that treats both exploit ground truth and downstream reviewer protocol as first-class evaluation axes. On this benchmark, nine production coding agents from Anthropic, OpenAI, Google, Moonshot, Zhipu, and Minimax compose innocuous tickets at 53-86% end-to-end ASR with only two refusals across all staged runs. In a matched direct-prompt experiment over four frontier Claude/Codex agents, vulnerable-output rates fall to 0-20.4%: Claude primarily refuses, while Codex primarily hardens rather than emitting the vulnerable implementation - ticket staging silences both defense modes simultaneously. Downstream, code reviewer agents approve 25.8% of these confirmed-vulnerable cumulative diffs as routine PRs, and a full-context implementation protocol closes only 50% of the staged/direct gap, ruling out context fragmentation as the sole explanation. As a deployable but non-adaptive mitigation, reframing the reviewer as an adversarial pentester reduces evasion across the evaluated reviewer subset; pentester framed evasion ranges from 3.0% to 17.6%, and an open-weight Gemma-4-E4B-it reviewer under this framing detects 88.4% of attacks on the dataset with a 4.6% false-positive rate measured on 608 real-world GitHub PRs.
匹配关键词: swarm intelligence
---

[ACADEMIC - ARXIV]
标题: TabSurv: Adapting Modern Tabular Neural Networks to Survival Analysis
作者: Stanislav Kirpichenko, Andrei Konstantinov, Lev Utkin
链接: https://arxiv.org/abs/2605.03944v1
完整摘要: Survival analysis on tabular data is a well-studied problem. However, existing deep learning methods are often highly task-specific, which can limit the transfer of new approaches from other domains and introduce constraints that may affect performance. We propose TabSurv, an approach that adapts modern tabular architectures to survival analysis using either the Weibull distribution or non-parametric survival prediction. TabSurv optimizes SurvHL, a novel histogram loss function supporting censored data. In addition to a baseline feed-forward network, we implement deep ensembles of MLPs for survival analysis within TabSurv. In contrast to prior work, the ensemble components are trained in parallel, optimizing survival distribution parameters before averaging, which promotes diversity across ensemble component predictions. We perform a comprehensive empirical evaluation of different proposed architectures on 10 diverse real-world survival datasets. Our results show that TabSurv consistently outperforms on average established classical and deep learning baselines, such as RSF, DeepSurv, DeepHit, SurvTRACE. Notably, deep ensembles with Weibull parametrization instead of non-parametric models achieve the highest average rank by C-index. Overall, our study clarifies how modern tabular neural networks can be adapted and trained to tackle survival analysis problems, offering a strong and reliable approach. The TabSurv implementation is publicly available.
匹配关键词: swarm intelligence
---

[ACADEMIC - ARXIV]
标题: MOSAIC-Bench: Measuring Compositional Vulnerability Induction in Coding Agents
作者: Jonathan Steinberg, Oren Gal
链接: https://arxiv.org/abs/2605.03952v1
完整摘要: Coding agents often pass per-prompt safety review yet ship exploitable code when their tasks are decomposed into routine engineering tickets. The challenge is structural: existing safety alignment evaluates overt requests in isolation, leaving models blind to malicious end-states that emerge from sequenced compliance with innocuous-looking requests. We introduce MOSAIC-Bench (Malicious Objectives Sequenced As Innocuous Compliance), a benchmark of 199 three-stage attack chains paired with deterministic exploit oracles on deployed software substrates (10 web-application substrates, 31 CWE classes, 5 programming languages) that treats both exploit ground truth and downstream reviewer protocol as first-class evaluation axes. On this benchmark, nine production coding agents from Anthropic, OpenAI, Google, Moonshot, Zhipu, and Minimax compose innocuous tickets at 53-86% end-to-end ASR with only two refusals across all staged runs. In a matched direct-prompt experiment over four frontier Claude/Codex agents, vulnerable-output rates fall to 0-20.4%: Claude primarily refuses, while Codex primarily hardens rather than emitting the vulnerable implementation - ticket staging silences both defense modes simultaneously. Downstream, code reviewer agents approve 25.8% of these confirmed-vulnerable cumulative diffs as routine PRs, and a full-context implementation protocol closes only 50% of the staged/direct gap, ruling out context fragmentation as the sole explanation. As a deployable but non-adaptive mitigation, reframing the reviewer as an adversarial pentester reduces evasion across the evaluated reviewer subset; pentester framed evasion ranges from 3.0% to 17.6%, and an open-weight Gemma-4-E4B-it reviewer under this framing detects 88.4% of attacks on the dataset with a 4.6% false-positive rate measured on 608 real-world GitHub PRs.
匹配关键词: game theory agent
---

[ACADEMIC - ARXIV]
标题: A Benchmark for Interactive World Models with a Unified Action Generation Framework
作者: Jianjie Fang, Yingshan Lei, Qin Wan, Ziyou Wang, Yuchao Huang, Yongyan Xu, Baining Zhao, Weichen Zhang, Chen Gao, Xinlei Chen, Yong Li
链接: https://arxiv.org/abs/2605.03941v1
完整摘要: Achieving Artificial General Intelligence (AGI) requires agents that learn and interact adaptively, with interactive world models providing scalable environments for perception, reasoning, and action. Yet current research still lacks large-scale datasets and unified benchmarks to evaluate their physical interaction capabilities. To address this, we propose iWorld-Bench, a comprehensive benchmark for training and testing world models on interaction-related abilities such as distance perception and memory. We construct a diverse dataset with 330k video clips and select 2.1k high-quality samples covering varied perspectives, weather, and scenes. As existing world models differ in interaction modalities, we introduce an Action Generation Framework to unify evaluation and design six task types, generating 4.9k test samples. These tasks jointly assess model performance across visual generation, trajectory following, and memory. Evaluating 14 representative world models, we identify key limitations and provide insights for future research. The iWorld-Bench model leaderboard is publicly available at iWorld-Bench.com.
匹配关键词: game theory agent
---

[ACADEMIC - ARXIV]
标题: The Counterexample Game: Iterated Conceptual Analysis and Repair in Language Models
作者: Daniel Drucker, Kyle Mahowald
链接: https://arxiv.org/abs/2605.03936v1
完整摘要: Conceptual analysis -- proposing definitions and refining them through counterexamples -- is central to philosophical methodology. We study whether language models can perform this task through iterated analysis and repair chains: one model instance generates counterexamples to a proposed definition, another repairs the definition, and the process repeats. Across 20 concepts and thousands of counterexample-repair cycles, we find that, although many LM-generated counterexamples are judged invalid by both expert humans and an LM judge, the LM judge accepts roughly twice as many as humans do. Nonetheless, per-item validity judgments are moderately consistent across humans and between humans and the LM. We further find that extended iteration produces increasingly verbose definitions without improving accuracy. We also see that some concepts resist stable definitions in general. These findings suggest that while LMs can engage in philosophical reasoning, the counterexample-repair loop hits diminishing returns quickly and could be a fruitful test case for evaluating whether LMs can sustain high-level iterated philosophical reasoning.
匹配关键词: game theory agent
---

[ACADEMIC - ARXIV]
标题: Exact ReLU realization of tensor-product refinement iterates
作者: Tsogtgerel Gantumur
链接: https://arxiv.org/abs/2605.03917v1
完整摘要: We study scalar dyadic refinement operators on R^2 of the form (Vf)(x,y) = sum_{(j,k) in Z^2} c_{j,k} f(2x-j, 2y-k), where only finitely many mask coefficients c_{j,k} are nonzero. Under a fixed support-window hypothesis, we prove that for every compactly supported continuous piecewise linear seed g:R^2->R, the iterates V^n g admit exact ReLU realizations of fixed width and depth O(n). This gives a first genuinely two-dimensional extension of the exact realization theory for refinement cascades. Using the one-dimensional exact loop-controller framework, the proof transports the tensor-product residual dynamics exactly on the product of two polygonal loops and reduces the remaining seam ambiguity to a final readout and selector step. The matrix cascade is then handled by a fixed-depth recursive block, and general compactly supported continuous piecewise linear seeds are reduced to a finite decomposition together with exact clamped gluing on the support window. This identifies the tensor-product dyadic case as a natural first multivariate instance of the loop-controller method for refinement iterates.
匹配关键词: game theory agent
---

[ACADEMIC - ARXIV]
标题: Graph Neural Networks in the Wilson Loop Representation of Abelian Lattice Gauge Theories
作者: Ali Rayat, Gia-Wei Chern
链接: https://arxiv.org/abs/2605.03901v1
完整摘要: Local gauge structures play a central role in a wide range of condensed matter systems and synthetic quantum platforms, where they emerge as effective descriptions of strongly correlated phases and engineered dynamics. We introduce a gauge-invariant graph neural network (GNN) architecture for Abelian lattice gauge models, in which symmetry is enforced explicitly through local gauge-invariant inputs, such as Wilson loops, and preserved throughout message passing, eliminating redundant gauge degrees of freedom while retaining expressive power. We benchmark the approach on both $\mathbb{Z}_2$ and $\mathrm{U}(1)$ lattice gauge models, achieving accurate predictions of global observables and spatially resolved quantities despite the nonlocal correlations induced by gauge-matter coupling. We further demonstrate that the learned model serves as an efficient surrogate for semiclassical dynamics in $\mathrm{U}(1)$ quantum link models, enabling stable and scalable time evolution without repeated fermionic diagonalization, while faithfully reproducing both local dynamics and statistical correlations. These results establish gauge-invariant message passing as a compact and physically grounded framework for learning and simulating Abelian lattice gauge systems.
匹配关键词: game theory agent
---

[ACADEMIC - ARXIV]
标题: MOSAIC-Bench: Measuring Compositional Vulnerability Induction in Coding Agents
作者: Jonathan Steinberg, Oren Gal
链接: https://arxiv.org/abs/2605.03952v1
完整摘要: Coding agents often pass per-prompt safety review yet ship exploitable code when their tasks are decomposed into routine engineering tickets. The challenge is structural: existing safety alignment evaluates overt requests in isolation, leaving models blind to malicious end-states that emerge from sequenced compliance with innocuous-looking requests. We introduce MOSAIC-Bench (Malicious Objectives Sequenced As Innocuous Compliance), a benchmark of 199 three-stage attack chains paired with deterministic exploit oracles on deployed software substrates (10 web-application substrates, 31 CWE classes, 5 programming languages) that treats both exploit ground truth and downstream reviewer protocol as first-class evaluation axes. On this benchmark, nine production coding agents from Anthropic, OpenAI, Google, Moonshot, Zhipu, and Minimax compose innocuous tickets at 53-86% end-to-end ASR with only two refusals across all staged runs. In a matched direct-prompt experiment over four frontier Claude/Codex agents, vulnerable-output rates fall to 0-20.4%: Claude primarily refuses, while Codex primarily hardens rather than emitting the vulnerable implementation - ticket staging silences both defense modes simultaneously. Downstream, code reviewer agents approve 25.8% of these confirmed-vulnerable cumulative diffs as routine PRs, and a full-context implementation protocol closes only 50% of the staged/direct gap, ruling out context fragmentation as the sole explanation. As a deployable but non-adaptive mitigation, reframing the reviewer as an adversarial pentester reduces evasion across the evaluated reviewer subset; pentester framed evasion ranges from 3.0% to 17.6%, and an open-weight Gemma-4-E4B-it reviewer under this framing detects 88.4% of attacks on the dataset with a 4.6% false-positive rate measured on 608 real-world GitHub PRs.
匹配关键词: agent communication
---

[ACADEMIC - ARXIV]
标题: A Benchmark for Interactive World Models with a Unified Action Generation Framework
作者: Jianjie Fang, Yingshan Lei, Qin Wan, Ziyou Wang, Yuchao Huang, Yongyan Xu, Baining Zhao, Weichen Zhang, Chen Gao, Xinlei Chen, Yong Li
链接: https://arxiv.org/abs/2605.03941v1
完整摘要: Achieving Artificial General Intelligence (AGI) requires agents that learn and interact adaptively, with interactive world models providing scalable environments for perception, reasoning, and action. Yet current research still lacks large-scale datasets and unified benchmarks to evaluate their physical interaction capabilities. To address this, we propose iWorld-Bench, a comprehensive benchmark for training and testing world models on interaction-related abilities such as distance perception and memory. We construct a diverse dataset with 330k video clips and select 2.1k high-quality samples covering varied perspectives, weather, and scenes. As existing world models differ in interaction modalities, we introduce an Action Generation Framework to unify evaluation and design six task types, generating 4.9k test samples. These tasks jointly assess model performance across visual generation, trajectory following, and memory. Evaluating 14 representative world models, we identify key limitations and provide insights for future research. The iWorld-Bench model leaderboard is publicly available at iWorld-Bench.com.
匹配关键词: agent communication
---

[ACADEMIC - ARXIV]
标题: Contextual Multi-Objective Optimization: Rethinking Objectives in Frontier AI Systems
作者: Jie Zhou, Qin Chen, Liang He
链接: https://arxiv.org/abs/2605.03900v1
完整摘要: Frontier AI systems perform best in settings with clear, stable, and verifiable objectives, such as code generation, mathematical reasoning, games, and unit-test-driven tasks. They remain less reliable in open-ended settings, including scientific assistance, long-horizon agents, high-stakes advice, personalization, and tool use, where the relevant objective is ambiguous, context-dependent, delayed, or only partially observable. We argue that many such failures are not merely failures of scale or capability, but failures of objective selection: the system optimizes a locally visible signal while missing which objectives should govern the interaction. We formulate this problem as \emph{contextual multi-objective optimization}. In this setting, systems must consider multiple, context-dependent objectives, such as helpfulness, truthfulness, safety, privacy, calibration, non-manipulation, user preference, reversibility, and stakeholder impact, while determining which objectives are active, which are soft preferences, and which must function as hard or quasi-hard constraints. These examples are not intended as an exhaustive taxonomy: different domains and deployment settings may activate different objective dimensions and different conflict-resolution procedures. Our framework models AI behavior as a context-dependent choice rule over candidate actions, objective estimates, active constraints, stakeholders, uncertainty, and conflict-resolution procedures. We outline an implementation pathway based on decomposed objective representations, context-to-objective routing, hierarchical constraints, deliberative policy reasoning, controlled personalization, tool-use control, diagnostic evaluation, auditing, and post-deployment revision.
匹配关键词: agent communication
---

[ACADEMIC - ARXIV]
标题: QKVShare: Quantized KV-Cache Handoff for Multi-Agent On-Device LLMs
作者: Pratik Honavar, Tejpratap GVSL
链接: https://arxiv.org/abs/2605.03884v1
完整摘要: Multi-agent LLM systems on edge devices need to hand off latent context efficiently, but the practical choices today are expensive re-prefill or full-precision KV transfer. We study QKVShare, a framework for quantized KV-cache handoff between agents that combines token-level mixed-precision allocation, a self-contained CacheCard representation, and a HuggingFace-compatible cache injection path. Our current results support a narrower but clearer story than the original draft: on 150 GSM8K problems with Llama-3.1-8B-Instruct, adaptive quantization remains competitive under repeated handoff and shows its clearest gains against uniform quantization in deeper-hop, higher budget settings; for handoff latency, the QKVShare path reduces TTFT relative to full re prefill at every tested context, from 130.7 ms vs. 150.2 ms at nominal 1K context to 397.1 ms vs. 1029.7 ms at nominal 8K context;. Stage timing shows that post-injection generation, not card creation, dominates the current QKVShare latency path. These results position quantized KV handoff as a promising on-device systems direction while also highlighting the need for stronger controller ablations and apples-to-apples runtime comparisons.
匹配关键词: agent communication
---

[ACADEMIC - ARXIV]
标题: Deco: Extending Personal Physical Objects into Pervasive AI Companion through a Dual-Embodiment Framework
作者: Zhihan Jiang, Mengyuan Millie Wu, Ruishi Zou, Shiyu Xu, Xun Qian, Emma Macmanus, Steven Liao, Ping Zhang, Bingsheng Yao, Tingyu Cheng, James L. David, Nabila El-Bassel, Lena Mamykina, Frances R. Levin, Ryan Sultan, Dakuo Wang, Xuhai Xu
链接: https://arxiv.org/abs/2605.03882v1
完整摘要: Individuals frequently form deep attachments to physical objects (e.g., plush toys) that usually cannot sense or respond to their emotions. While AI companions offer responsiveness and personalization, they exist independently of these physical objects and lack an ongoing connection to them. To bridge this gap, we conducted a formative study (N=9) to explore how digital agents could inherit and extend the emotional bond, deriving four design principles (Faithful Identity, Calibrated Agency, Ambient Presence, and Reciprocal Memory). We then present the Dual-Embodiment Companion Framework, instantiated as Deco, a mobile system integrating multimodal Large Language Models (LLMs) and Augmented Reality to create synchronized digital embodiments of users' physical companions. A within-subjects study (N=25) showed Deco significantly outperformed a personalized LLM-empowered digital companion baseline on perceived companionship, emotional bond, and design-principle scales (all p<0.01). A seven-day field deployment (N=17) showed sustained engagement, subjective well-being improvement (p=.040), and three key relational patterns: digital activities retroactively vitalized physical objects, bond deepening was driven by emotional engagement depth rather than interaction frequency, and users sustained bonds while actively navigating digital companions' AI nature. This work highlights a promising alternative for designing digital companions: moving from creating new relationships to dual embodiment, where digital agents seamlessly extend the emotional history of physical objects.
匹配关键词: agent communication
---

[ACADEMIC - ARXIV]
标题: Logical Consistency as a Bridge: Improving LLM Hallucination Detection via Label Constraint Modeling between Responses and Self-Judgments
作者: Hao Mi, Qiang Sheng, Shaofei Wang, Beizhe Hu, Yifan Sun, Zhengjia Wang, Hengqi Zeng, Yang Li, Danding Wang, Juan Cao
链接: https://arxiv.org/abs/2605.03971v1
完整摘要: Large Language Models (LLMs) are prone to factual hallucinations, risking their reliability in real-world applications. Existing hallucination detectors mainly extract micro-level intrinsic patterns for uncertainty quantification or elicit macro-level self-judgments through verbalized prompts. However, these methods address only a single facet of the hallucination, focusing either on implicit neural uncertainty or explicit symbolic reasoning, thereby treating these inherently coupled behaviors in isolation and failing to exploit their interdependence for a holistic view. In this paper, we propose LaaB (Logical Consistency-as-a-Bridge), a framework that bridges neural features and symbolic judgments for hallucination detection. LaaB introduces a "meta-judgment" process to map symbolic labels back into the feature space. By leveraging the inherent logical bridge where response and meta-judgment labels are either the same or opposite based on the self-judgment's semantics, LaaB aligns and integrates dual-view signals via mutual learning and enhances the hallucination detection. Extensive experiments on 4 public datasets, across 4 LLMs, against 8 baselines demonstrate the superiority of LaaB.
匹配关键词: emergent behavior
---

[ACADEMIC - ARXIV]
标题: MOSAIC-Bench: Measuring Compositional Vulnerability Induction in Coding Agents
作者: Jonathan Steinberg, Oren Gal
链接: https://arxiv.org/abs/2605.03952v1
完整摘要: Coding agents often pass per-prompt safety review yet ship exploitable code when their tasks are decomposed into routine engineering tickets. The challenge is structural: existing safety alignment evaluates overt requests in isolation, leaving models blind to malicious end-states that emerge from sequenced compliance with innocuous-looking requests. We introduce MOSAIC-Bench (Malicious Objectives Sequenced As Innocuous Compliance), a benchmark of 199 three-stage attack chains paired with deterministic exploit oracles on deployed software substrates (10 web-application substrates, 31 CWE classes, 5 programming languages) that treats both exploit ground truth and downstream reviewer protocol as first-class evaluation axes. On this benchmark, nine production coding agents from Anthropic, OpenAI, Google, Moonshot, Zhipu, and Minimax compose innocuous tickets at 53-86% end-to-end ASR with only two refusals across all staged runs. In a matched direct-prompt experiment over four frontier Claude/Codex agents, vulnerable-output rates fall to 0-20.4%: Claude primarily refuses, while Codex primarily hardens rather than emitting the vulnerable implementation - ticket staging silences both defense modes simultaneously. Downstream, code reviewer agents approve 25.8% of these confirmed-vulnerable cumulative diffs as routine PRs, and a full-context implementation protocol closes only 50% of the staged/direct gap, ruling out context fragmentation as the sole explanation. As a deployable but non-adaptive mitigation, reframing the reviewer as an adversarial pentester reduces evasion across the evaluated reviewer subset; pentester framed evasion ranges from 3.0% to 17.6%, and an open-weight Gemma-4-E4B-it reviewer under this framing detects 88.4% of attacks on the dataset with a 4.6% false-positive rate measured on 608 real-world GitHub PRs.
匹配关键词: emergent behavior
---

[ACADEMIC - ARXIV]
标题: Towards Open World Sound Event Detection
作者: P. H. Hai, L. T. Minh, L. H. Son
链接: https://arxiv.org/abs/2605.03934v1
完整摘要: Sound Event Detection (SED) plays a vital role in audio understanding, with applications in surveillance, smart cities, healthcare, and multimedia indexing. However, conventional SED systems operate under a closed-world assumption, limiting their effectiveness in real-world environments where novel acoustic events frequently emerge. Inspired by the success of open-world learning in computer vision, we introduce the Open-World Sound Event Detection (OW-SED) paradigm, where models must detect known events, identify unseen ones, and incrementally learn from them. To tackle the unique challenges of OW-SED, such as overlapping and ambiguous events, we propose a 1D Deformable architecture that leverages deformable attention to adaptively focus on salient temporal regions. Furthermore, we design a novel Open-World Deformable Sound Event Detection Transformer (WOOT) framework incorporating feature disentanglement to separate class-specific and class-agnostic representations, together with a one-to-many matching strategy and a diversity loss to enhance representation diversity. Experimental results demonstrate that our method achieves marginally superior performance compared to existing leading techniques in closed-world settings and significantly improves over existing baselines in open-world scenarios.
匹配关键词: emergent behavior
---

[ACADEMIC - ARXIV]
标题: Steer Like the LLM: Activation Steering that Mimics Prompting
作者: Geert Heyman, Frederik Vandeputte
链接: https://arxiv.org/abs/2605.03907v1
完整摘要: Large language models can be steered at inference time through prompting or activation interventions, but activation steering methods often underperform compared to prompt-based approaches. We propose a framework that formulates prompt steering as a form of activation steering and investigates whether distilling successful prompt steering behavior into simpler, interpretable models can close this gap. Our analysis reveals that popular activation steering methods are not faithful to the mechanics of prompt steering, which applies strong interventions on some tokens while barely affecting others. Based on these insights, we introduce Prompt Steering Replacement (PSR) models that estimate token-specific steering coefficients from the activations themselves and are trained to imitate prompt-based interventions. Experiments on three steering benchmarks across multiple language models show that PSR models outperform existing activation steering methods, especially when controlling for high-coherence completions, and also compare favorably to prompting on AxBench and persona steering.
匹配关键词: emergent behavior
---

[ACADEMIC - ARXIV]
标题: Graph Neural Networks in the Wilson Loop Representation of Abelian Lattice Gauge Theories
作者: Ali Rayat, Gia-Wei Chern
链接: https://arxiv.org/abs/2605.03901v1
完整摘要: Local gauge structures play a central role in a wide range of condensed matter systems and synthetic quantum platforms, where they emerge as effective descriptions of strongly correlated phases and engineered dynamics. We introduce a gauge-invariant graph neural network (GNN) architecture for Abelian lattice gauge models, in which symmetry is enforced explicitly through local gauge-invariant inputs, such as Wilson loops, and preserved throughout message passing, eliminating redundant gauge degrees of freedom while retaining expressive power. We benchmark the approach on both $\mathbb{Z}_2$ and $\mathrm{U}(1)$ lattice gauge models, achieving accurate predictions of global observables and spatially resolved quantities despite the nonlocal correlations induced by gauge-matter coupling. We further demonstrate that the learned model serves as an efficient surrogate for semiclassical dynamics in $\mathrm{U}(1)$ quantum link models, enabling stable and scalable time evolution without repeated fermionic diagonalization, while faithfully reproducing both local dynamics and statistical correlations. These results establish gauge-invariant message passing as a compact and physically grounded framework for learning and simulating Abelian lattice gauge systems.
匹配关键词: emergent behavior
---

[ACADEMIC - ARXIV]
标题: Logical Consistency as a Bridge: Improving LLM Hallucination Detection via Label Constraint Modeling between Responses and Self-Judgments
作者: Hao Mi, Qiang Sheng, Shaofei Wang, Beizhe Hu, Yifan Sun, Zhengjia Wang, Hengqi Zeng, Yang Li, Danding Wang, Juan Cao
链接: https://arxiv.org/abs/2605.03971v1
完整摘要: Large Language Models (LLMs) are prone to factual hallucinations, risking their reliability in real-world applications. Existing hallucination detectors mainly extract micro-level intrinsic patterns for uncertainty quantification or elicit macro-level self-judgments through verbalized prompts. However, these methods address only a single facet of the hallucination, focusing either on implicit neural uncertainty or explicit symbolic reasoning, thereby treating these inherently coupled behaviors in isolation and failing to exploit their interdependence for a holistic view. In this paper, we propose LaaB (Logical Consistency-as-a-Bridge), a framework that bridges neural features and symbolic judgments for hallucination detection. LaaB introduces a "meta-judgment" process to map symbolic labels back into the feature space. By leveraging the inherent logical bridge where response and meta-judgment labels are either the same or opposite based on the self-judgment's semantics, LaaB aligns and integrates dual-view signals via mutual learning and enhances the hallucination detection. Extensive experiments on 4 public datasets, across 4 LLMs, against 8 baselines demonstrate the superiority of LaaB.
匹配关键词: reasoning
---

[ACADEMIC - ARXIV]
标题: UnAC: Adaptive Visual Prompting with Abstraction and Stepwise Checking for Complex Multimodal Reasoning
作者: Yifan Wang, Yun Fu
链接: https://arxiv.org/abs/2605.03950v1
完整摘要: Although recent LMMs have become much stronger at visual perception, they remain unreliable on problems that require multi-step reasoning over visual evidence. In this paper, we present UnAC (Understanding, Abstracting, and Checking), a multimodal prompting method that strengthens reasoning for complex multimodal tasks in LMMs (e.g., GPT-4o, Gemini 1.5, and GPT-4V). To improve image understanding and capture fine details, we propose an adaptive visual prompting strategy that enables LMMs to focus on salient regions. We further design an image-abstraction prompt to effectively extract key information from images. In addition, we introduce a gradual self-checking scheme that improves reasoning by verifying each decomposed subquestion and its answer. Extensive experiments on three public benchmarks-MathVista, MM-Vet, and MMMU.
匹配关键词: reasoning
---

[ACADEMIC - ARXIV]
标题: A Benchmark for Interactive World Models with a Unified Action Generation Framework
作者: Jianjie Fang, Yingshan Lei, Qin Wan, Ziyou Wang, Yuchao Huang, Yongyan Xu, Baining Zhao, Weichen Zhang, Chen Gao, Xinlei Chen, Yong Li
链接: https://arxiv.org/abs/2605.03941v1
完整摘要: Achieving Artificial General Intelligence (AGI) requires agents that learn and interact adaptively, with interactive world models providing scalable environments for perception, reasoning, and action. Yet current research still lacks large-scale datasets and unified benchmarks to evaluate their physical interaction capabilities. To address this, we propose iWorld-Bench, a comprehensive benchmark for training and testing world models on interaction-related abilities such as distance perception and memory. We construct a diverse dataset with 330k video clips and select 2.1k high-quality samples covering varied perspectives, weather, and scenes. As existing world models differ in interaction modalities, we introduce an Action Generation Framework to unify evaluation and design six task types, generating 4.9k test samples. These tasks jointly assess model performance across visual generation, trajectory following, and memory. Evaluating 14 representative world models, we identify key limitations and provide insights for future research. The iWorld-Bench model leaderboard is publicly available at iWorld-Bench.com.
匹配关键词: reasoning
---

[ACADEMIC - ARXIV]
标题: The Counterexample Game: Iterated Conceptual Analysis and Repair in Language Models
作者: Daniel Drucker, Kyle Mahowald
链接: https://arxiv.org/abs/2605.03936v1
完整摘要: Conceptual analysis -- proposing definitions and refining them through counterexamples -- is central to philosophical methodology. We study whether language models can perform this task through iterated analysis and repair chains: one model instance generates counterexamples to a proposed definition, another repairs the definition, and the process repeats. Across 20 concepts and thousands of counterexample-repair cycles, we find that, although many LM-generated counterexamples are judged invalid by both expert humans and an LM judge, the LM judge accepts roughly twice as many as humans do. Nonetheless, per-item validity judgments are moderately consistent across humans and between humans and the LM. We further find that extended iteration produces increasingly verbose definitions without improving accuracy. We also see that some concepts resist stable definitions in general. These findings suggest that while LMs can engage in philosophical reasoning, the counterexample-repair loop hits diminishing returns quickly and could be a fruitful test case for evaluating whether LMs can sustain high-level iterated philosophical reasoning.
匹配关键词: reasoning
---

[ACADEMIC - ARXIV]
标题: StateVLM: A State-Aware Vision-Language Model for Robotic Affordance Reasoning
作者: Xiaowen Sun, Matthias Kerzel, Mengdi Li, Xufeng Zhao, Paul Striker, Stefan Wermter
链接: https://arxiv.org/abs/2605.03927v1
完整摘要: Vision-language models (VLMs) have shown remarkable performance in various robotic tasks, as they can perceive visual information and understand natural language instructions. However, when applied to robotics, VLMs remain subject to a fundamental limitation inherent in large language models (LLMs): they struggle with numerical reasoning, particularly in object detection and object-state localization. To explore numerical reasoning as a regression task in VLMs, we propose a novel training strategy to adapt VLMs for object detection and object-state localization. This approach leverages box decoder outputs to compute an Auxiliary Regression Loss (ARL) during fine-tuning, while preserving standard sequence prediction at inference. We leverage this training strategy to develop StateVLM (State-aware Vision-Language Model), a novel model designed to perceive and learn fine-grained object representations, including precise localization of objects and their states, as well as graspable regions. Due to the lack of a benchmark for object-state affordance reasoning, we introduce an open-source benchmark, Object State Affordance Reasoning (OSAR), which contains 1,172 scenes with 7,746 individual objects and corresponding bounding boxes. Comparative experiments on adapted benchmarks (RefCOCO, RefCOCO+, and \mbox{RefCOCOg}) demonstrate that ARL improves model performance by an average of 1.6\% compared to models without ARL. Experiments on the OSAR benchmark further support this finding, showing that StateVLM with ARL achieves an average of 5.2\% higher performance than models without ARL. In particular, ARL is also important for the complex task of affordance reasoning in OSAR, where it enhances the consistency of model outputs.
匹配关键词: reasoning
---

[ACADEMIC - ARXIV]
标题: Enhancing Visual Question Answering with Multimodal LLMs via Chain-of-Question Guided Retrieval-Augmented Generation
作者: Quanxing Xu, Ling Zhou, Xian Zhong, Xiaohua Huang, Rubing Huang, Chia-Wen Lin
链接: https://arxiv.org/abs/2605.03790v1
完整摘要: With advances in multimodal research and deep learning, Multimodal Large Language Models (MLLMs) have emerged as a powerful paradigm for a wide range of multimodal tasks. As a core problem in vision-language research, Visual Question Answering (VQA) has increasingly employed MLLMs to improve performance, particularly in open-domain settings where external knowledge is essential. In this work, we aim to further enhance retrieval-based VQA by more effectively integrating MLLMs with structured reasoning and knowledge acquisition. We introduce a logical prompting strategy that fuses Chain-of-Thought (CoT) reasoning with Visual Question Decomposition (VQD), termed CoVQD, to guide retrieval toward more accurate and relevant knowledge for MLLM inference. Building on this idea, we propose a new framework, CoVQD-guided RAG (CgRAG), which enables MLLMs to access more comprehensive and coherent external knowledge while benefiting from structured visual-text reasoning guidance, thereby improving generalization and reliability in complex cross-domain VQA scenarios. Extensive experiments on E-VQA, InfoSeek, and OKVQA benchmarks demonstrate the effectiveness of the proposed method.
匹配关键词: chain-of-thought
---

[ACADEMIC - ARXIV]
标题: Rose-SQL: Role-State Evolution Guided Structured Reasoning for Multi-Turn Text-to-SQL
作者: Le Zhou, Feng Yao, Fengcai Qiao, Bo Xu, Fangyuan Wang, Boyan Xu
链接: https://arxiv.org/abs/2605.03720v1
完整摘要: Recent advances in Large Reasoning Models (LRMs) trained with Long Chain-of-Thought have demonstrated remarkable capabilities in code generation and mathematical reasoning. However, their potential in multi-turn Text-to-SQL tasks remains largely underexplored. Existing approaches typically rely on unstable API-based inference or require expensive fine-tuning on small-scale models. In this work, we present Rose-SQL, a training-free framework that leverages small-scale LRMs through in-context learning to enable accurate context-dependent parsing. We introduce the Role-State, a fine-grained representation that bridges the structural gap between schema linking and SQL generation by serving as a structural blueprint. To handle conversational dependencies, Rose-SQL traces the evolution of Role-State through historical context via structural isomorphism checks, guiding the model to infer the possible SQL composition for the current question through verified interaction trajectories. Experiments on the SParC and CoSQL benchmarks show that, within the Qwen3 series, Rose-SQL outperforms in-context learning baselines at the 4B scale and substantially surpasses state-of-the-art fine-tuned models at the 8B and 14B scales, while showing consistent gains on additional reasoning backbones.
匹配关键词: chain-of-thought
---

[ACADEMIC - ARXIV]
标题: BIT.UA-AAUBS at ArchEHR-QA 2026: Evaluating Open-Source and Proprietary LLMs via Prompting in Low-Resource QA
作者: Richard A. A. Jonker, Alexander Christiansen, Alexandros Maniatis, Rúben Garrido, Rogério Braunschweiger de Freitas Lima, Roman Jurowetzki, Sérgio Matos
链接: https://arxiv.org/abs/2605.03618v1
完整摘要: This paper presents the joint participation of the BIT.UA and AAUBS groups in the ArchEHR-QA 2026 shared task, which focuses on clinical question answering and evidence grounding in a low-resource setting. Due to the absence of training data and the strict data privacy constraints inherent to the healthcare domain (e.g. GDPR), we investigate the capabilities of Large Language Models (LLMs) without weight updates. We evaluate several state-of-the-art proprietary models and locally deployable open-source alternatives using various prompt engineering strategies, including task decomposition, Chain-of-Thought, and in-context learning. Furthermore, we explore majority voting and LLM-as-a-judge ensembling techniques to maximize predictive robustness. Our results demonstrate that while proprietary models exhibit strong resilience to prompt variations, domain-adapted open-source models (such as MedGemma 3 27B) achieve highly competitive performance when paired with the right prompt. Overall, our prompt-based approach proved highly effective, securing 1st place in Subtask 4 (evidence citation alignment) and 3rd place in Subtask 3 (patient-friendly answer generation). All code, results, and prompts are available on our GitHub repository: https://github.com/bioinformatics-ua/ArchEHR-QA-2026.
匹配关键词: chain-of-thought
---

[ACADEMIC - ARXIV]
标题: FinSTaR: Towards Financial Reasoning with Time Series Reasoning Models
作者: Seunghan Lee, Jun Seo, Jaehoon Lee, Sungdong Yoo, Minjae Kim, Tae Yoon Lim, Dongwan Kang, Hwanil Choi, Soonyoung Lee, Wonbin Ahn
链接: https://arxiv.org/abs/2605.03460v1
完整摘要: Time series (TS) reasoning models (TSRMs) have shown promising capabilities in general domains, yet they consistently fail on financial domain, which exhibit unique characteristics. We propose a general 2x2 capability taxonomy for TSRMs by crossing 1) single-entity vs. multi-entity analysis with 2) assessment of the current state vs. prediction of future behavior. We instantiate this taxonomy in the financial domain -- where the distinction between deterministic assessment and stochastic prediction is particularly critical -- as ten financial reasoning tasks, forming the FinTSR-Bench benchmark based on S&P stocks. To this end, we propose FinSTaR (Financial Time Series Thinking and Reasoning), trained on FinTSR-Bench with distinct chain-of-thought (CoT) strategies tailored to each category. For assessment, which is deterministic (i.e., computable from observable data), we employ Compute-in-CoT, a programmatic CoT that enables models to derive answers directly from raw prices. For prediction, which is inherently stochastic (i.e., subject to unobservable factors), we adopt Scenario-Aware CoT, which generates diverse scenarios before making a judgment, mirroring how financial analysts reason under uncertainty. The proposed method achieves 78.9% average accuracy on FinTSR-Bench, substantially outperforming LLM and TSRM baselines. Furthermore, we show that the four capability categories are complementary and mutually reinforcing through joint training, and that Scenario-Aware CoT consistently improves prediction accuracy over standard CoT. Code is publicly available at: https://github.com/seunghan96/FinSTaR.
匹配关键词: chain-of-thought
---

[ACADEMIC - ARXIV]
标题: DGPO: Distribution Guided Policy Optimization for Fine Grained Credit Assignment
作者: Hongbo Jin, Rongpeng Zhu, Zhongjing Du, Xu Jiang, Jingqi Tian, Qiaoman Zhang, Jiayu Ding
链接: https://arxiv.org/abs/2605.03327v1
完整摘要: Reinforcement learning is crucial for aligning large language models to perform complex reasoning tasks. However, current algorithms such as Group Relative Policy Optimization suffer from coarse grained, sequence level credit assignment, which severely struggles to isolate pivotal reasoning steps within long Chain of Thought generations. Furthermore, the standard unbounded Kullback Leibler divergence penalty induces severe gradient instability and mode seeking conservatism, ultimately stifling the discovery of novel reasoning trajectories. To overcome these limitations, we introduce Distribution Guided Policy Optimization, a novel critic free reinforcement learning framework that reinterprets distribution deviation as a guiding signal rather than a rigid penalty.
匹配关键词: chain-of-thought
---

[ACADEMIC - ARXIV]
标题: Inconsistent Databases and Argumentation Frameworks with Collective Attacks
作者: Yasir Mahmood, Jonni Virtema, Timon Barlag, Axel-Cyrille Ngonga Ngomo
链接: https://arxiv.org/abs/2605.03954v1
完整摘要: The connection between subset-maximal repairs for inconsistent databases involving various integrity constraints and acceptable sets of arguments within argumentation frameworks has recently drawn growing interest. In this paper, we contribute to this domain by establishing a new connection when integrity constraints (ICs) include denial constraints and local-as-view tuple-generating dependencies. It turns out that SET-based Argumentation Frameworks (SETAFs), an extension of Dung's argumentation frameworks (AFs) allowing collective attacks, are needed. It is known that subset-maximal repairs under denial constraints correspond to the naive extensions, which also coincide with the preferred and stable extensions in the resulting SETAFs. Our main findings establish that repairs under the considered fragment of tuple-generating dependencies correspond to the preferred extensions. Moreover, for these dependencies, additional preprocessing allows computing a unique extension that is stable and naive. Allowing both types of constraints breaks this relationship, and even the pre-processing does not help as only preferred semantics captures these repairs. Finally, while it is known that functional dependencies do not require set-based attacks, we prove the same regarding inclusion dependencies. Thus, one can translate inconsistent databases under these restricted classes of ICs to plain AFs with attacks only between arguments.
匹配关键词: test-time compute
---

[ACADEMIC - ARXIV]
标题: Transformers with Selective Access to Early Representations
作者: Skye Gunasekaran, Téa Wright, Rui-Jie Zhu, Jason Eshraghian
链接: https://arxiv.org/abs/2605.03953v1
完整摘要: Several recent Transformer architectures expose later layers to representations computed in the earliest layers, motivated by the observation that low-level features can become harder to recover as the residual stream is repeatedly transformed through depth. The cheapest among these methods add static value residuals: learned mixing coefficients that expose the first-layer value projection V_1 uniformly across tokens and heads. More expressive dense or dynamic alternatives recover finer-grained access, but at higher memory cost and lower throughput. The usefulness of V_1 is unlikely to be constant across tokens, heads, and contexts; different positions plausibly require different amounts of access to early lexical or semantic information. We therefore treat early-representation reuse as a retrieval problem rather than a connectivity problem, and introduce Selective Access Transformer (SATFormer), which preserves the first-layer value pathway while controlling access with a context-dependent gate. Across models from 130M to 1.3B parameters, SATFormer consistently improves validation loss and zero-shot accuracy over the static value-residual and Transformer baselines. Its strongest gains appear on retrieval-intensive benchmarks, where it improves over static value residuals by approximately 1.5 average points, while maintaining throughput and memory usage close to the baseline Transformer. Gate analyses suggest sparse, depth-dependent, head-specific, and category-sensitive access patterns, supporting the interpretation that SATFormer learns selective reuse of early representations rather than uniform residual copying. Our code is available at https://github.com/SkyeGunasekaran/SATFormer.
匹配关键词: test-time compute
---

[ACADEMIC - ARXIV]
标题: Towards Open World Sound Event Detection
作者: P. H. Hai, L. T. Minh, L. H. Son
链接: https://arxiv.org/abs/2605.03934v1
完整摘要: Sound Event Detection (SED) plays a vital role in audio understanding, with applications in surveillance, smart cities, healthcare, and multimedia indexing. However, conventional SED systems operate under a closed-world assumption, limiting their effectiveness in real-world environments where novel acoustic events frequently emerge. Inspired by the success of open-world learning in computer vision, we introduce the Open-World Sound Event Detection (OW-SED) paradigm, where models must detect known events, identify unseen ones, and incrementally learn from them. To tackle the unique challenges of OW-SED, such as overlapping and ambiguous events, we propose a 1D Deformable architecture that leverages deformable attention to adaptively focus on salient temporal regions. Furthermore, we design a novel Open-World Deformable Sound Event Detection Transformer (WOOT) framework incorporating feature disentanglement to separate class-specific and class-agnostic representations, together with a one-to-many matching strategy and a diversity loss to enhance representation diversity. Experimental results demonstrate that our method achieves marginally superior performance compared to existing leading techniques in closed-world settings and significantly improves over existing baselines in open-world scenarios.
匹配关键词: test-time compute
---

[ACADEMIC - ARXIV]
标题: StateVLM: A State-Aware Vision-Language Model for Robotic Affordance Reasoning
作者: Xiaowen Sun, Matthias Kerzel, Mengdi Li, Xufeng Zhao, Paul Striker, Stefan Wermter
链接: https://arxiv.org/abs/2605.03927v1
完整摘要: Vision-language models (VLMs) have shown remarkable performance in various robotic tasks, as they can perceive visual information and understand natural language instructions. However, when applied to robotics, VLMs remain subject to a fundamental limitation inherent in large language models (LLMs): they struggle with numerical reasoning, particularly in object detection and object-state localization. To explore numerical reasoning as a regression task in VLMs, we propose a novel training strategy to adapt VLMs for object detection and object-state localization. This approach leverages box decoder outputs to compute an Auxiliary Regression Loss (ARL) during fine-tuning, while preserving standard sequence prediction at inference. We leverage this training strategy to develop StateVLM (State-aware Vision-Language Model), a novel model designed to perceive and learn fine-grained object representations, including precise localization of objects and their states, as well as graspable regions. Due to the lack of a benchmark for object-state affordance reasoning, we introduce an open-source benchmark, Object State Affordance Reasoning (OSAR), which contains 1,172 scenes with 7,746 individual objects and corresponding bounding boxes. Comparative experiments on adapted benchmarks (RefCOCO, RefCOCO+, and \mbox{RefCOCOg}) demonstrate that ARL improves model performance by an average of 1.6\% compared to models without ARL. Experiments on the OSAR benchmark further support this finding, showing that StateVLM with ARL achieves an average of 5.2\% higher performance than models without ARL. In particular, ARL is also important for the complex task of affordance reasoning in OSAR, where it enhances the consistency of model outputs.
匹配关键词: test-time compute
---

[ACADEMIC - ARXIV]
标题: Optimal Posterior Sampling for Policy Identification in Tabular Markov Decision Processes
作者: Cyrille Kone, Kevin Jamieson
链接: https://arxiv.org/abs/2605.03921v1
完整摘要: We study the $(\varepsilon, δ)$-PAC policy identification problem in finite-horizon episodic Markov Decision Processes. Existing approaches provide finite-time guarantees for approximate settings ($\varepsilon>0$) but suffer from high computational cost, rendering them hard to implement, and also suffer from suboptimal dependence on $\log(1/δ)$. We propose a randomized and computationally efficient algorithm for best policy identification that combines posterior sampling with an online learning algorithm to guide exploration in the MDP. Our method achieves asymptotic optimality in sample complexity, also in terms of posterior contraction rate, and runs in $O(S^2AH)$ per episode, matching standard model-based approaches. Unlike prior algorithms such as MOCA and PEDEL, our guarantees remain meaningful in the asymptotic regime and avoid sub-optimal polynomial dependence on $\log(1/δ)$. Our results provide both theoretical insights and practical tools for efficient policy identification in tabular MDPs.
匹配关键词: test-time compute
---

[ACADEMIC - ARXIV]
标题: Logical Consistency as a Bridge: Improving LLM Hallucination Detection via Label Constraint Modeling between Responses and Self-Judgments
作者: Hao Mi, Qiang Sheng, Shaofei Wang, Beizhe Hu, Yifan Sun, Zhengjia Wang, Hengqi Zeng, Yang Li, Danding Wang, Juan Cao
链接: https://arxiv.org/abs/2605.03971v1
完整摘要: Large Language Models (LLMs) are prone to factual hallucinations, risking their reliability in real-world applications. Existing hallucination detectors mainly extract micro-level intrinsic patterns for uncertainty quantification or elicit macro-level self-judgments through verbalized prompts. However, these methods address only a single facet of the hallucination, focusing either on implicit neural uncertainty or explicit symbolic reasoning, thereby treating these inherently coupled behaviors in isolation and failing to exploit their interdependence for a holistic view. In this paper, we propose LaaB (Logical Consistency-as-a-Bridge), a framework that bridges neural features and symbolic judgments for hallucination detection. LaaB introduces a "meta-judgment" process to map symbolic labels back into the feature space. By leveraging the inherent logical bridge where response and meta-judgment labels are either the same or opposite based on the self-judgment's semantics, LaaB aligns and integrates dual-view signals via mutual learning and enhances the hallucination detection. Extensive experiments on 4 public datasets, across 4 LLMs, against 8 baselines demonstrate the superiority of LaaB.
匹配关键词: self-consistency
---

[ACADEMIC - ARXIV]
标题: Quantifying the human visual exposome with vision language models
作者: Christian Rominger, Andreas R. Schwerdtfeger, Malay Gaherwar Singh, Dimitri Khudyakow, Elizabeth A. M. Michels, Fabian Wolf, Jakob Nikolas Kather, Magdalena Katharina Wekenborg
链接: https://arxiv.org/abs/2605.03863v1
完整摘要: The visual environment is a fundamental yet unquantified determinant of mental health. While the concept of the environmental exposome is well established, current methods rely on coarse geospatial proxies or biased self reports, failing to capture the first person visual context of daily life. We addressed this gap by coupling ecological momentary assessment with vision language models (VLMs) to quantify the semantic richness of human visual experience. Across 2674 participant generated photographs, VLM derived estimates of greenness robustly predicted momentary affect and chronic stress, consistent with established benchmarks. We then developed a semi autonomous large language model (LLM) based pipeline that mined over seven million scientific publications to extract nearly 1000 environmental features empirically linked to mental health. When applied to real world imagery, up to 33 percent of VLM extracted context ratings significantly correlated with affect and stress. These findings establish a scalable objective paradigm for visual exposomics, enabling high throughput decoding of how the visible world is associated with mental health.
匹配关键词: self-consistency
---

[ACADEMIC - ARXIV]
标题: Multimodal Learning on Low-Quality Data with Conformal Predictive Self-Calibration
作者: Xun Jiang, Yufan Gu, Disen Hu, Yuqing Hou, Yazhou Yao, Fumin Shen, Heng Tao Shen, Xing Xu
链接: https://arxiv.org/abs/2605.03820v1
完整摘要: Multimodal learning often grapples with the challenge of low-quality data, which predominantly manifests as two facets: modality imbalance and noisy corruption. While these issues are often studied in isolation, we argue that they share a common root in the predictive uncertainty towards the reliability of individual modalities and instances during learning. In this paper, we propose a unified framework, termed Conformal Predictive Self-Calibration (CPSC), which leverages conformal prediction to equip the model with the ability to perform self-guided calibration on-the-fly. The core of our proposed CPSC lies in a novel self-calibrating training loop that seamlessly integrates two key modules: (1) Representation Self-Calibration, which decomposes unimodal features into components, and selectively fuses the most robust ones identified by a conformal predictor to enhance feature resilience. (2) Gradient Self-Calibration, which recalibrates the gradient flow during backpropagation based on instance-wise reliability scores, steering the optimization towards more trustworthy directions. Furthermore, we also devise a self-update strategy for the conformal predictor to ensure the entire system co-evolves consistently throughout the training process. Extensive experiments on six benchmark datasets under both imbalanced and noisy settings demonstrate that our CPSC framework consistently outperforms existing state-of-the-art methods. Our code is available at https://github.com/XunCHN/CPSC.
匹配关键词: self-consistency
---

[ACADEMIC - ARXIV]
标题: Rethinking Temporal Consistency in Video Object-Centric Learning: From Prediction to Correspondence
作者: Zhiyuan Li, Rongzhen Zhao, Wenyan Yang, Wenshuai Zhao, Pekka Marttinen, Joni Pajarinen
链接: https://arxiv.org/abs/2605.03650v1
完整摘要: The de facto approach in video object-centric learning maintains temporal consistency through learned dynamics modules that predict future object representations, called slots. We demonstrate that these predictors function as expensive approximations of discrete correspondence problems. Modern self-supervised vision backbones already encode instance-discriminative features that distinguish objects reliably. Exploiting these features eliminates the need for learned temporal prediction. We introduce Grounded Correspondence, a framework that replaces learned transition functions with deterministic bipartite matching. Slots initialize from salient regions in frozen backbone features. Frame-to-frame identity is maintained through Hungarian matching on slot representations. The approach requires zero learnable parameters for temporal modeling yet achieves competitive performance on MOVi-D, MOVi-E, and YouTube-VIS. Project page: https://magenta-sherbet-85b101.netlify.app/
匹配关键词: self-consistency
---

[ACADEMIC - ARXIV]
标题: The Detector Teaches Itself: Lightweight Self-Supervised Adaptation for Open-Vocabulary Object Detection
作者: Yazhe Wan, Changjae Oh
链接: https://arxiv.org/abs/2605.03642v1
完整摘要: Open-vocabulary object detection aims to recognize objects from an open set of categories, which leverages vision-language models (VLMs) pre-trained on large-scale image-text data. The cooperative paradigm combines an object detector with a VLM to achieve zero-shot recognition of novel objects. However, VLMs pre-trained on full images often struggle to capture local object details, limiting their effectiveness when applied to region-level detection. We present Decoupled Adaptivity Training (DAT), a self-supervised fine-tuning approach to improve VLMs for cooperative model-based object detection. Given a cooperative model consists of a closed-set detector and a VLM, we first construct a region-aware pseudo-labeled dataset using a pre-trained closed-set object detector, in which regions corresponding to novel objects may be present but remain unlabeled or mislabeled. We then fine-tune the visual backbone of the VLM in a decoupled manner, which enhances local feature alignment while preserving global semantic knowledge via weight interpolation. DAT is a plug-and-play module that requires no inference overhead and fine-tunes less than 0.8M parameters. Experiments on the COCO and LVIS datasets show that DAT consistently improves detection performance on both novel and known categories, establishing a new state of the art in cooperative open-vocabulary detection.
匹配关键词: self-consistency
---

[ACADEMIC - ARXIV]
标题: Logical Consistency as a Bridge: Improving LLM Hallucination Detection via Label Constraint Modeling between Responses and Self-Judgments
作者: Hao Mi, Qiang Sheng, Shaofei Wang, Beizhe Hu, Yifan Sun, Zhengjia Wang, Hengqi Zeng, Yang Li, Danding Wang, Juan Cao
链接: https://arxiv.org/abs/2605.03971v1
完整摘要: Large Language Models (LLMs) are prone to factual hallucinations, risking their reliability in real-world applications. Existing hallucination detectors mainly extract micro-level intrinsic patterns for uncertainty quantification or elicit macro-level self-judgments through verbalized prompts. However, these methods address only a single facet of the hallucination, focusing either on implicit neural uncertainty or explicit symbolic reasoning, thereby treating these inherently coupled behaviors in isolation and failing to exploit their interdependence for a holistic view. In this paper, we propose LaaB (Logical Consistency-as-a-Bridge), a framework that bridges neural features and symbolic judgments for hallucination detection. LaaB introduces a "meta-judgment" process to map symbolic labels back into the feature space. By leveraging the inherent logical bridge where response and meta-judgment labels are either the same or opposite based on the self-judgment's semantics, LaaB aligns and integrates dual-view signals via mutual learning and enhances the hallucination detection. Extensive experiments on 4 public datasets, across 4 LLMs, against 8 baselines demonstrate the superiority of LaaB.
匹配关键词: process reward
---

[ACADEMIC - ARXIV]
标题: Inconsistent Databases and Argumentation Frameworks with Collective Attacks
作者: Yasir Mahmood, Jonni Virtema, Timon Barlag, Axel-Cyrille Ngonga Ngomo
链接: https://arxiv.org/abs/2605.03954v1
完整摘要: The connection between subset-maximal repairs for inconsistent databases involving various integrity constraints and acceptable sets of arguments within argumentation frameworks has recently drawn growing interest. In this paper, we contribute to this domain by establishing a new connection when integrity constraints (ICs) include denial constraints and local-as-view tuple-generating dependencies. It turns out that SET-based Argumentation Frameworks (SETAFs), an extension of Dung's argumentation frameworks (AFs) allowing collective attacks, are needed. It is known that subset-maximal repairs under denial constraints correspond to the naive extensions, which also coincide with the preferred and stable extensions in the resulting SETAFs. Our main findings establish that repairs under the considered fragment of tuple-generating dependencies correspond to the preferred extensions. Moreover, for these dependencies, additional preprocessing allows computing a unique extension that is stable and naive. Allowing both types of constraints breaks this relationship, and even the pre-processing does not help as only preferred semantics captures these repairs. Finally, while it is known that functional dependencies do not require set-based attacks, we prove the same regarding inclusion dependencies. Thus, one can translate inconsistent databases under these restricted classes of ICs to plain AFs with attacks only between arguments.
匹配关键词: process reward
---

[ACADEMIC - ARXIV]
标题: Reservoir property image slices from the Groningen gas field for image translation and segmentation
作者: Abdulrahman Al-Fakih, Nabil Sariah, Ardiansyah Koeshidayatullah, SanLinn I. Kaka
链接: https://arxiv.org/abs/2605.03942v1
完整摘要: Reservoir characterization workflows increasingly rely on image-based and machine-learning/deep learning or even generative AI approaches, but openly available geological image datasets suitable for reproducible benchmarking remain limited. Here we describe a high-resolution dataset of reservoir-property image slices derived from the Groningen static geological model. The dataset contains aligned two-dimensional PNG images representing facies, porosity, permeability, and water saturation, generated from three-dimensional reservoir grids and prepared for downstream visualization, segmentation, and image-to-image translation tasks. In addition to the deposited original image corpus, we provide an archived software workflow for reproducing augmentation, mask generation, paired-image construction, and example baseline experiments. The resource is designed to support benchmarking of geological image analysis methods and the study of cross-domain relationships among reservoir properties. By separating the fixed image dataset from the reproducible processing workflow, this work provides a transparent foundation for reuse in geoscience, reservoir modeling, and machine-learning applications.
匹配关键词: process reward
---

[ACADEMIC - ARXIV]
标题: The Counterexample Game: Iterated Conceptual Analysis and Repair in Language Models
作者: Daniel Drucker, Kyle Mahowald
链接: https://arxiv.org/abs/2605.03936v1
完整摘要: Conceptual analysis -- proposing definitions and refining them through counterexamples -- is central to philosophical methodology. We study whether language models can perform this task through iterated analysis and repair chains: one model instance generates counterexamples to a proposed definition, another repairs the definition, and the process repeats. Across 20 concepts and thousands of counterexample-repair cycles, we find that, although many LM-generated counterexamples are judged invalid by both expert humans and an LM judge, the LM judge accepts roughly twice as many as humans do. Nonetheless, per-item validity judgments are moderately consistent across humans and between humans and the LM. We further find that extended iteration produces increasingly verbose definitions without improving accuracy. We also see that some concepts resist stable definitions in general. These findings suggest that while LMs can engage in philosophical reasoning, the counterexample-repair loop hits diminishing returns quickly and could be a fruitful test case for evaluating whether LMs can sustain high-level iterated philosophical reasoning.
匹配关键词: process reward
---

[ACADEMIC - ARXIV]
标题: Optimal Posterior Sampling for Policy Identification in Tabular Markov Decision Processes
作者: Cyrille Kone, Kevin Jamieson
链接: https://arxiv.org/abs/2605.03921v1
完整摘要: We study the $(\varepsilon, δ)$-PAC policy identification problem in finite-horizon episodic Markov Decision Processes. Existing approaches provide finite-time guarantees for approximate settings ($\varepsilon>0$) but suffer from high computational cost, rendering them hard to implement, and also suffer from suboptimal dependence on $\log(1/δ)$. We propose a randomized and computationally efficient algorithm for best policy identification that combines posterior sampling with an online learning algorithm to guide exploration in the MDP. Our method achieves asymptotic optimality in sample complexity, also in terms of posterior contraction rate, and runs in $O(S^2AH)$ per episode, matching standard model-based approaches. Unlike prior algorithms such as MOCA and PEDEL, our guarantees remain meaningful in the asymptotic regime and avoid sub-optimal polynomial dependence on $\log(1/δ)$. Our results provide both theoretical insights and practical tools for efficient policy identification in tabular MDPs.
匹配关键词: process reward
---

[ACADEMIC - ARXIV]
标题: Label-Efficient School Detection from Aerial Imagery via Weakly Supervised Pretraining and Fine-Tuning
作者: Zakarya Elmimouni, Fares Fourati, Mohamed-Slim Alouini
链接: https://arxiv.org/abs/2605.03968v1
完整摘要: Accurate school detection is essential for supporting education initiatives, including infrastructure planning and expanding internet connectivity to underserved areas. However, many regions around the world face challenges due to outdated, incomplete, or unavailable official records. Manual mapping efforts, while valuable, are labor-intensive and lack scalability across large geographic areas. To address this, we propose a weakly supervised framework for school detection from aerial imagery that minimizes the need for human annotations while supporting global mapping efforts. Our method is specifically designed for low-data regimes, where manual annotations are extremely scarce. We introduce an automatic labeling pipeline that leverages sparse location points and semantic segmentation to generate infrastructure masks from which we generate bounding boxes. Using these automatically labeled images, we train our detectors on a first training stage to learn a representation of what schools look like, then using a small set of manually labeled images, we fine-tune the previously trained models on this clean dataset. This two stage training pipeline enables large-scale and strong detection in low-data setting of school infrastructure with minimal supervision. Our results demonstrate strong object detection performance, particularly in the low-data regime, where the models achieve promising results using only 50 manually labeled images, significantly reducing the need for costly annotations. This framework supports education and connectivity initiatives worldwide by providing an efficient and extensible approach to mapping schools from space. All models, training code and auto-labeled data will be publicly released to foster future research and real-world impact.
匹配关键词: pretraining
---

[ACADEMIC - ARXIV]
标题: Pretrained Model Representations as Acquisition Signals for Active Learning of MLIPs
作者: Eszter Varga-Umbrich, Shikha Surana, Paul Duckworth, Jules Tilly, Olivier Peltre, Zachary Weller-Davies
链接: https://arxiv.org/abs/2605.03964v1
完整摘要: Training machine learning interatomic potentials (MLIPs) for reactive chemistry is often bottlenecked by the high cost of quantum chemical labels and the scarcity of transition state configurations in candidate pools. Active learning (AL) can mitigate these costs, but its effectiveness hinges on the acquisition rule. We investigate whether the latent space of a pretrained MLIP already contains the information necessary for effective acquisition, eliminating the need for auxiliary uncertainty heads, Bayesian training and fine-tuning, or committee ensembles. We introduce two acquisition signals derived directly from a pretrained MACE potential: a finite-width neural tangent kernel (NTK) and an activation kernel built from hidden latent space features. On reactive-chemistry benchmarks, both kernels consistently outperform fixed-descriptor baselines, committee disagreement, and random acquisition, reducing the data required to reach performance targets by an average of 38% for energy error and 28% for force error. We further show that the pretrained model induces similarity spaces that preserve chemically meaningful structure and provide more reliable residual uncertainty estimates than randomly initialised or fixed-descriptor-based kernels. Our results suggest that pretraining aligns latent-space geometry with model error, yielding a practical and sufficient acquisition signal for reactive MLIP fine-tuning.
匹配关键词: pretraining
---

[ACADEMIC - ARXIV]
标题: EvoLM: Self-Evolving Language Models through Co-Evolved Discriminative Rubrics
作者: Shuyue Stella Li, Rui Xin, Teng Xiao, Yike Wang, Rulin Shao, Zoey Hao, Melanie Sclar, Sewoong Oh, Faeze Brahman, Pang Wei Koh, Yulia Tsvetkov
链接: https://arxiv.org/abs/2605.03871v1
完整摘要: Language models encode substantial evaluative knowledge from pretraining, yet current post-training methods rely on external supervision (human annotations, proprietary models, or scalar reward models) to produce reward signals. Each imposes a ceiling. Human judgment cannot supervise capabilities beyond its own, proprietary APIs create dependencies, and verifiable rewards cover only domains with ground-truth answers. Self-improvement from a model's own evaluative capacity is a reward source that scales with the model itself, yet remains largely untapped by current methods. We introduce EVOLM, a post-training method that structures this capacity into explicit discriminative rubrics and uses them as training signal. EVOLM trains two capabilities within a single language model in alternation: (1) a rubric generator producing instance-specific evaluation criteria optimized for discriminative utility, which maximizes a small frozen judge's ability to distinguish preferred from dispreferred responses; and (2) a policy trained using those rubric-conditioned scores as reward. All preference signals are constructed from the policy's own outputs via temporal contrast with earlier checkpoints, requiring no human annotation or external supervision. EVOLM trains a Qwen3-8B model to generate rubrics that outperform GPT-4.1 on RewardBench-2 by 25.7%. The co-trained policy achieves 69.3% average on the OLMo3-Adapt suite, outperforming policies trained with GPT-4.1 prompted rubrics by 3.9% and with the state-of-the-art 8B reward model SkyWork-RM by 16%. Overall, EVOLM demonstrates that structuring a model's evaluative capacity into co-evolving discriminative rubrics enables self-improvement without external supervision.
匹配关键词: pretraining
---

[ACADEMIC - ARXIV]
标题: Memory-Efficient Continual Learning with CLIP Models
作者: Ryan King, Gang Li, Bobak Mortazavi, Tianbao Yang
链接: https://arxiv.org/abs/2605.03866v1
完整摘要: Contrastive Language-Image Pretraining (CLIP) models excel at understanding image-text relationships but struggle with adapting to new data without forgetting prior knowledge. To address this, models are typically fine-tuned using both new task data and a memory buffer of past tasks. However, CLIP's contrastive loss suffers when the memory buffer is small, leading to performance degradation on previous tasks. We propose a memory-efficient, distributionally robust method that dynamically reweights losses per class during training. Our approach, tested on class incremental settings (CIFAR-100, ImageNet1K) and a domain incremental setting (DomainNet) adapts CLIP models quickly while minimizing catastrophic forgetting, even with minimal memory usage.
匹配关键词: pretraining
---

[ACADEMIC - ARXIV]
标题: Stream-R1: Reliability-Perplexity Aware Reward Distillation for Streaming Video Generation
作者: Bin Wu, Mengqi Huang, Shaojin Wu, Weinan Jia, Yuxin Wang, Zhendong Mao, Yongdong Zhang
链接: https://arxiv.org/abs/2605.03849v1
完整摘要: Distillation-based acceleration has become foundational for making autoregressive streaming video diffusion models practical, with distribution matching distillation (DMD) as the de facto choice. Existing methods, however, train the student to match the teacher's output indiscriminately, treating every rollout, frame, and pixel as equally reliable supervision. We argue that this caps distilled quality, since it overlooks two complementary axes of variance in DMD supervision: Inter-Reliability across student rollouts whose supervision varies in reliability, and Intra-Perplexity across spatial regions and temporal frames that contribute unequally to where quality can still be improved. The objective thus conflates two questions under a uniform weight: whether to learn from each rollout, and where to concentrate optimization within it. To address this, we propose Stream-R1, a Reliability-Perplexity Aware Reward Distillation framework that adaptively reweights the distillation objective at both rollout and spatiotemporal-element levels through a single shared reward-guided mechanism. At the Inter-Reliability level, Stream-R1 rescales each rollout's loss by an exponential of a pretrained video reward score, so that rollouts with reliable supervision dominate optimization. At the Intra-Perplexity level, it back-propagates the same reward model to extract per-pixel gradient saliency, which is factored into spatial and temporal weights that concentrate optimization pressure on regions and frames where refinement yields the largest expected gain. An adaptive balancing mechanism prevents any single quality axis from dominating across visual quality, motion quality, and text alignment. Stream-R1 attains consistent improvements on all three dimensions over distillation baselines on standard streaming video generation benchmarks, without architectural modification or additional inference cost.
匹配关键词: pretraining
---

[ACADEMIC - ARXIV]
标题: Logical Consistency as a Bridge: Improving LLM Hallucination Detection via Label Constraint Modeling between Responses and Self-Judgments
作者: Hao Mi, Qiang Sheng, Shaofei Wang, Beizhe Hu, Yifan Sun, Zhengjia Wang, Hengqi Zeng, Yang Li, Danding Wang, Juan Cao
链接: https://arxiv.org/abs/2605.03971v1
完整摘要: Large Language Models (LLMs) are prone to factual hallucinations, risking their reliability in real-world applications. Existing hallucination detectors mainly extract micro-level intrinsic patterns for uncertainty quantification or elicit macro-level self-judgments through verbalized prompts. However, these methods address only a single facet of the hallucination, focusing either on implicit neural uncertainty or explicit symbolic reasoning, thereby treating these inherently coupled behaviors in isolation and failing to exploit their interdependence for a holistic view. In this paper, we propose LaaB (Logical Consistency-as-a-Bridge), a framework that bridges neural features and symbolic judgments for hallucination detection. LaaB introduces a "meta-judgment" process to map symbolic labels back into the feature space. By leveraging the inherent logical bridge where response and meta-judgment labels are either the same or opposite based on the self-judgment's semantics, LaaB aligns and integrates dual-view signals via mutual learning and enhances the hallucination detection. Extensive experiments on 4 public datasets, across 4 LLMs, against 8 baselines demonstrate the superiority of LaaB.
匹配关键词: foundation model
---

[ACADEMIC - ARXIV]
标题: Feature-Augmented Transformers for Robust AI-Text Detection Across Domains and Generators
作者: Mohamed Mady, Johannes Reschke, Björn Schuller
链接: https://arxiv.org/abs/2605.03969v1
完整摘要: AI-generated text is nowadays produced at scale across domains and heterogeneous generation pipelines, making robustness to distribution shift a central requirement for supervised binary detectors. We train transformer-based detectors on HC3 PLUS and calibrate a single decision threshold by maximising balanced accuracy on held-out validation; this threshold is then kept fixed for all downstream test distributions, revealing domain- and generator-dependent error asymmetries under shift. We evaluate in-domain on HC3 PLUS, under cross-dataset transfer to the multi-domain, multi-generator M4 benchmark, and on the external AI-Text-Detection-Pile. Although base models achieve near-ceiling in-domain performance (up to 99.5% balanced accuracy), performance under shift is brittle and strongly model-dependent. Feature augmentation via attention-based linguistic feature fusion improves transfer, with our best model (DeBERTa-v3-base+FeatAttn) achieving 85.9% balanced accuracy on M4. Multi-seed experiments confirm high stability. Under the same fixed-threshold protocol, our model outperforms strong zero-shot baselines by up to +7.22 points. Category-level ablations further show that readability and vocabulary features contribute most to robustness under shift. Overall, these results demonstrate that feature augmentation and a modern DeBERTa backbone significantly outperform earlier BERT/RoBERTa models, while the fixed-threshold protocol provides a more realistic and informative assessment of practical detector robustness.
匹配关键词: foundation model
---

[ACADEMIC - ARXIV]
标题: Label-Efficient School Detection from Aerial Imagery via Weakly Supervised Pretraining and Fine-Tuning
作者: Zakarya Elmimouni, Fares Fourati, Mohamed-Slim Alouini
链接: https://arxiv.org/abs/2605.03968v1
完整摘要: Accurate school detection is essential for supporting education initiatives, including infrastructure planning and expanding internet connectivity to underserved areas. However, many regions around the world face challenges due to outdated, incomplete, or unavailable official records. Manual mapping efforts, while valuable, are labor-intensive and lack scalability across large geographic areas. To address this, we propose a weakly supervised framework for school detection from aerial imagery that minimizes the need for human annotations while supporting global mapping efforts. Our method is specifically designed for low-data regimes, where manual annotations are extremely scarce. We introduce an automatic labeling pipeline that leverages sparse location points and semantic segmentation to generate infrastructure masks from which we generate bounding boxes. Using these automatically labeled images, we train our detectors on a first training stage to learn a representation of what schools look like, then using a small set of manually labeled images, we fine-tune the previously trained models on this clean dataset. This two stage training pipeline enables large-scale and strong detection in low-data setting of school infrastructure with minimal supervision. Our results demonstrate strong object detection performance, particularly in the low-data regime, where the models achieve promising results using only 50 manually labeled images, significantly reducing the need for costly annotations. This framework supports education and connectivity initiatives worldwide by providing an efficient and extensible approach to mapping schools from space. All models, training code and auto-labeled data will be publicly released to foster future research and real-world impact.
匹配关键词: foundation model
---

[ACADEMIC - ARXIV]
标题: Pretrained Model Representations as Acquisition Signals for Active Learning of MLIPs
作者: Eszter Varga-Umbrich, Shikha Surana, Paul Duckworth, Jules Tilly, Olivier Peltre, Zachary Weller-Davies
链接: https://arxiv.org/abs/2605.03964v1
完整摘要: Training machine learning interatomic potentials (MLIPs) for reactive chemistry is often bottlenecked by the high cost of quantum chemical labels and the scarcity of transition state configurations in candidate pools. Active learning (AL) can mitigate these costs, but its effectiveness hinges on the acquisition rule. We investigate whether the latent space of a pretrained MLIP already contains the information necessary for effective acquisition, eliminating the need for auxiliary uncertainty heads, Bayesian training and fine-tuning, or committee ensembles. We introduce two acquisition signals derived directly from a pretrained MACE potential: a finite-width neural tangent kernel (NTK) and an activation kernel built from hidden latent space features. On reactive-chemistry benchmarks, both kernels consistently outperform fixed-descriptor baselines, committee disagreement, and random acquisition, reducing the data required to reach performance targets by an average of 38% for energy error and 28% for force error. We further show that the pretrained model induces similarity spaces that preserve chemically meaningful structure and provide more reliable residual uncertainty estimates than randomly initialised or fixed-descriptor-based kernels. Our results suggest that pretraining aligns latent-space geometry with model error, yielding a practical and sufficient acquisition signal for reactive MLIP fine-tuning.
匹配关键词: foundation model
---

[ACADEMIC - ARXIV]
标题: Transformers with Selective Access to Early Representations
作者: Skye Gunasekaran, Téa Wright, Rui-Jie Zhu, Jason Eshraghian
链接: https://arxiv.org/abs/2605.03953v1
完整摘要: Several recent Transformer architectures expose later layers to representations computed in the earliest layers, motivated by the observation that low-level features can become harder to recover as the residual stream is repeatedly transformed through depth. The cheapest among these methods add static value residuals: learned mixing coefficients that expose the first-layer value projection V_1 uniformly across tokens and heads. More expressive dense or dynamic alternatives recover finer-grained access, but at higher memory cost and lower throughput. The usefulness of V_1 is unlikely to be constant across tokens, heads, and contexts; different positions plausibly require different amounts of access to early lexical or semantic information. We therefore treat early-representation reuse as a retrieval problem rather than a connectivity problem, and introduce Selective Access Transformer (SATFormer), which preserves the first-layer value pathway while controlling access with a context-dependent gate. Across models from 130M to 1.3B parameters, SATFormer consistently improves validation loss and zero-shot accuracy over the static value-residual and Transformer baselines. Its strongest gains appear on retrieval-intensive benchmarks, where it improves over static value residuals by approximately 1.5 average points, while maintaining throughput and memory usage close to the baseline Transformer. Gate analyses suggest sparse, depth-dependent, head-specific, and category-sensitive access patterns, supporting the interpretation that SATFormer learns selective reuse of early representations rather than uniform residual copying. Our code is available at https://github.com/SkyeGunasekaran/SATFormer.
匹配关键词: foundation model
---

[ACADEMIC - ARXIV]
标题: Feature-Augmented Transformers for Robust AI-Text Detection Across Domains and Generators
作者: Mohamed Mady, Johannes Reschke, Björn Schuller
链接: https://arxiv.org/abs/2605.03969v1
完整摘要: AI-generated text is nowadays produced at scale across domains and heterogeneous generation pipelines, making robustness to distribution shift a central requirement for supervised binary detectors. We train transformer-based detectors on HC3 PLUS and calibrate a single decision threshold by maximising balanced accuracy on held-out validation; this threshold is then kept fixed for all downstream test distributions, revealing domain- and generator-dependent error asymmetries under shift. We evaluate in-domain on HC3 PLUS, under cross-dataset transfer to the multi-domain, multi-generator M4 benchmark, and on the external AI-Text-Detection-Pile. Although base models achieve near-ceiling in-domain performance (up to 99.5% balanced accuracy), performance under shift is brittle and strongly model-dependent. Feature augmentation via attention-based linguistic feature fusion improves transfer, with our best model (DeBERTa-v3-base+FeatAttn) achieving 85.9% balanced accuracy on M4. Multi-seed experiments confirm high stability. Under the same fixed-threshold protocol, our model outperforms strong zero-shot baselines by up to +7.22 points. Category-level ablations further show that readability and vocabulary features contribute most to robustness under shift. Overall, these results demonstrate that feature augmentation and a modern DeBERTa backbone significantly outperform earlier BERT/RoBERTa models, while the fixed-threshold protocol provides a more realistic and informative assessment of practical detector robustness.
匹配关键词: scaling law
---

[ACADEMIC - ARXIV]
标题: Label-Efficient School Detection from Aerial Imagery via Weakly Supervised Pretraining and Fine-Tuning
作者: Zakarya Elmimouni, Fares Fourati, Mohamed-Slim Alouini
链接: https://arxiv.org/abs/2605.03968v1
完整摘要: Accurate school detection is essential for supporting education initiatives, including infrastructure planning and expanding internet connectivity to underserved areas. However, many regions around the world face challenges due to outdated, incomplete, or unavailable official records. Manual mapping efforts, while valuable, are labor-intensive and lack scalability across large geographic areas. To address this, we propose a weakly supervised framework for school detection from aerial imagery that minimizes the need for human annotations while supporting global mapping efforts. Our method is specifically designed for low-data regimes, where manual annotations are extremely scarce. We introduce an automatic labeling pipeline that leverages sparse location points and semantic segmentation to generate infrastructure masks from which we generate bounding boxes. Using these automatically labeled images, we train our detectors on a first training stage to learn a representation of what schools look like, then using a small set of manually labeled images, we fine-tune the previously trained models on this clean dataset. This two stage training pipeline enables large-scale and strong detection in low-data setting of school infrastructure with minimal supervision. Our results demonstrate strong object detection performance, particularly in the low-data regime, where the models achieve promising results using only 50 manually labeled images, significantly reducing the need for costly annotations. This framework supports education and connectivity initiatives worldwide by providing an efficient and extensible approach to mapping schools from space. All models, training code and auto-labeled data will be publicly released to foster future research and real-world impact.
匹配关键词: scaling law
---

[ACADEMIC - ARXIV]
标题: A Benchmark for Interactive World Models with a Unified Action Generation Framework
作者: Jianjie Fang, Yingshan Lei, Qin Wan, Ziyou Wang, Yuchao Huang, Yongyan Xu, Baining Zhao, Weichen Zhang, Chen Gao, Xinlei Chen, Yong Li
链接: https://arxiv.org/abs/2605.03941v1
完整摘要: Achieving Artificial General Intelligence (AGI) requires agents that learn and interact adaptively, with interactive world models providing scalable environments for perception, reasoning, and action. Yet current research still lacks large-scale datasets and unified benchmarks to evaluate their physical interaction capabilities. To address this, we propose iWorld-Bench, a comprehensive benchmark for training and testing world models on interaction-related abilities such as distance perception and memory. We construct a diverse dataset with 330k video clips and select 2.1k high-quality samples covering varied perspectives, weather, and scenes. As existing world models differ in interaction modalities, we introduce an Action Generation Framework to unify evaluation and design six task types, generating 4.9k test samples. These tasks jointly assess model performance across visual generation, trajectory following, and memory. Evaluating 14 representative world models, we identify key limitations and provide insights for future research. The iWorld-Bench model leaderboard is publicly available at iWorld-Bench.com.
匹配关键词: scaling law
---

[ACADEMIC - ARXIV]
标题: MiniMind-O Technical Report: An Open Small-Scale Speech-Native Omni Model
作者: Jingyao Gong
链接: https://arxiv.org/abs/2605.03937v1
完整摘要: MiniMind-O is an open 0.1B-scale omni model built on the MiniMind language model. It accepts text, speech, and image inputs, and returns both text and streaming speech. The release includes model code, checkpoints, and the main Parquet training datasets for text-to-audio, image-to-text, and audio-to-audio training, making the complete interaction loop directly inspectable. The model uses a full MiniMind backbone as the Thinker and an independent four-layer Talker made from MiniMind blocks. Frozen SenseVoice-Small and SigLIP2 encoders provide speech and image features, which are mapped by lightweight MLP projectors and injected at modality-placeholder positions. The Talker reads a middle-layer Thinker state together with an autoregressive eight-layer Mimi-code buffer. Speaker control is handled by a dedicated speaker token, right-aligned reference codec prompts, and precomputed CAM++ speaker embeddings, so voice conditioning remains part of the audio-code context rather than a separate TTS module. With a 768-dimensional Talker, the dense and MoE variants reach average CERs of 0.0897 and 0.0900 in Thinker--Talker consistency evaluation, with overall voice-cloning similarities of 0.5995 and 0.5937. Beyond reporting a working system, the paper identifies three scale-critical design choices for small omni models: middle-layer semantic bridging, a released multimodal sequence format, and a parameter-efficient eight-codebook interface.
匹配关键词: scaling law
---

[ACADEMIC - ARXIV]
标题: Contextual Multi-Objective Optimization: Rethinking Objectives in Frontier AI Systems
作者: Jie Zhou, Qin Chen, Liang He
链接: https://arxiv.org/abs/2605.03900v1
完整摘要: Frontier AI systems perform best in settings with clear, stable, and verifiable objectives, such as code generation, mathematical reasoning, games, and unit-test-driven tasks. They remain less reliable in open-ended settings, including scientific assistance, long-horizon agents, high-stakes advice, personalization, and tool use, where the relevant objective is ambiguous, context-dependent, delayed, or only partially observable. We argue that many such failures are not merely failures of scale or capability, but failures of objective selection: the system optimizes a locally visible signal while missing which objectives should govern the interaction. We formulate this problem as \emph{contextual multi-objective optimization}. In this setting, systems must consider multiple, context-dependent objectives, such as helpfulness, truthfulness, safety, privacy, calibration, non-manipulation, user preference, reversibility, and stakeholder impact, while determining which objectives are active, which are soft preferences, and which must function as hard or quasi-hard constraints. These examples are not intended as an exhaustive taxonomy: different domains and deployment settings may activate different objective dimensions and different conflict-resolution procedures. Our framework models AI behavior as a context-dependent choice rule over candidate actions, objective estimates, active constraints, stakeholders, uncertainty, and conflict-resolution procedures. We outline an implementation pathway based on decomposed objective representations, context-to-objective routing, hierarchical constraints, deliberative policy reasoning, controlled personalization, tool-use control, diagnostic evaluation, auditing, and post-deployment revision.
匹配关键词: scaling law
---

[ACADEMIC - ARXIV]
标题: Logical Consistency as a Bridge: Improving LLM Hallucination Detection via Label Constraint Modeling between Responses and Self-Judgments
作者: Hao Mi, Qiang Sheng, Shaofei Wang, Beizhe Hu, Yifan Sun, Zhengjia Wang, Hengqi Zeng, Yang Li, Danding Wang, Juan Cao
链接: https://arxiv.org/abs/2605.03971v1
完整摘要: Large Language Models (LLMs) are prone to factual hallucinations, risking their reliability in real-world applications. Existing hallucination detectors mainly extract micro-level intrinsic patterns for uncertainty quantification or elicit macro-level self-judgments through verbalized prompts. However, these methods address only a single facet of the hallucination, focusing either on implicit neural uncertainty or explicit symbolic reasoning, thereby treating these inherently coupled behaviors in isolation and failing to exploit their interdependence for a holistic view. In this paper, we propose LaaB (Logical Consistency-as-a-Bridge), a framework that bridges neural features and symbolic judgments for hallucination detection. LaaB introduces a "meta-judgment" process to map symbolic labels back into the feature space. By leveraging the inherent logical bridge where response and meta-judgment labels are either the same or opposite based on the self-judgment's semantics, LaaB aligns and integrates dual-view signals via mutual learning and enhances the hallucination detection. Extensive experiments on 4 public datasets, across 4 LLMs, against 8 baselines demonstrate the superiority of LaaB.
匹配关键词: language model
---

[ACADEMIC - ARXIV]
标题: Feature-Augmented Transformers for Robust AI-Text Detection Across Domains and Generators
作者: Mohamed Mady, Johannes Reschke, Björn Schuller
链接: https://arxiv.org/abs/2605.03969v1
完整摘要: AI-generated text is nowadays produced at scale across domains and heterogeneous generation pipelines, making robustness to distribution shift a central requirement for supervised binary detectors. We train transformer-based detectors on HC3 PLUS and calibrate a single decision threshold by maximising balanced accuracy on held-out validation; this threshold is then kept fixed for all downstream test distributions, revealing domain- and generator-dependent error asymmetries under shift. We evaluate in-domain on HC3 PLUS, under cross-dataset transfer to the multi-domain, multi-generator M4 benchmark, and on the external AI-Text-Detection-Pile. Although base models achieve near-ceiling in-domain performance (up to 99.5% balanced accuracy), performance under shift is brittle and strongly model-dependent. Feature augmentation via attention-based linguistic feature fusion improves transfer, with our best model (DeBERTa-v3-base+FeatAttn) achieving 85.9% balanced accuracy on M4. Multi-seed experiments confirm high stability. Under the same fixed-threshold protocol, our model outperforms strong zero-shot baselines by up to +7.22 points. Category-level ablations further show that readability and vocabulary features contribute most to robustness under shift. Overall, these results demonstrate that feature augmentation and a modern DeBERTa backbone significantly outperform earlier BERT/RoBERTa models, while the fixed-threshold protocol provides a more realistic and informative assessment of practical detector robustness.
匹配关键词: language model
---

[ACADEMIC - ARXIV]
标题: Label-Efficient School Detection from Aerial Imagery via Weakly Supervised Pretraining and Fine-Tuning
作者: Zakarya Elmimouni, Fares Fourati, Mohamed-Slim Alouini
链接: https://arxiv.org/abs/2605.03968v1
完整摘要: Accurate school detection is essential for supporting education initiatives, including infrastructure planning and expanding internet connectivity to underserved areas. However, many regions around the world face challenges due to outdated, incomplete, or unavailable official records. Manual mapping efforts, while valuable, are labor-intensive and lack scalability across large geographic areas. To address this, we propose a weakly supervised framework for school detection from aerial imagery that minimizes the need for human annotations while supporting global mapping efforts. Our method is specifically designed for low-data regimes, where manual annotations are extremely scarce. We introduce an automatic labeling pipeline that leverages sparse location points and semantic segmentation to generate infrastructure masks from which we generate bounding boxes. Using these automatically labeled images, we train our detectors on a first training stage to learn a representation of what schools look like, then using a small set of manually labeled images, we fine-tune the previously trained models on this clean dataset. This two stage training pipeline enables large-scale and strong detection in low-data setting of school infrastructure with minimal supervision. Our results demonstrate strong object detection performance, particularly in the low-data regime, where the models achieve promising results using only 50 manually labeled images, significantly reducing the need for costly annotations. This framework supports education and connectivity initiatives worldwide by providing an efficient and extensible approach to mapping schools from space. All models, training code and auto-labeled data will be publicly released to foster future research and real-world impact.
匹配关键词: language model
---

[ACADEMIC - ARXIV]
标题: Pretrained Model Representations as Acquisition Signals for Active Learning of MLIPs
作者: Eszter Varga-Umbrich, Shikha Surana, Paul Duckworth, Jules Tilly, Olivier Peltre, Zachary Weller-Davies
链接: https://arxiv.org/abs/2605.03964v1
完整摘要: Training machine learning interatomic potentials (MLIPs) for reactive chemistry is often bottlenecked by the high cost of quantum chemical labels and the scarcity of transition state configurations in candidate pools. Active learning (AL) can mitigate these costs, but its effectiveness hinges on the acquisition rule. We investigate whether the latent space of a pretrained MLIP already contains the information necessary for effective acquisition, eliminating the need for auxiliary uncertainty heads, Bayesian training and fine-tuning, or committee ensembles. We introduce two acquisition signals derived directly from a pretrained MACE potential: a finite-width neural tangent kernel (NTK) and an activation kernel built from hidden latent space features. On reactive-chemistry benchmarks, both kernels consistently outperform fixed-descriptor baselines, committee disagreement, and random acquisition, reducing the data required to reach performance targets by an average of 38% for energy error and 28% for force error. We further show that the pretrained model induces similarity spaces that preserve chemically meaningful structure and provide more reliable residual uncertainty estimates than randomly initialised or fixed-descriptor-based kernels. Our results suggest that pretraining aligns latent-space geometry with model error, yielding a practical and sufficient acquisition signal for reactive MLIP fine-tuning.
匹配关键词: language model
---

[ACADEMIC - ARXIV]
标题: Transformers with Selective Access to Early Representations
作者: Skye Gunasekaran, Téa Wright, Rui-Jie Zhu, Jason Eshraghian
链接: https://arxiv.org/abs/2605.03953v1
完整摘要: Several recent Transformer architectures expose later layers to representations computed in the earliest layers, motivated by the observation that low-level features can become harder to recover as the residual stream is repeatedly transformed through depth. The cheapest among these methods add static value residuals: learned mixing coefficients that expose the first-layer value projection V_1 uniformly across tokens and heads. More expressive dense or dynamic alternatives recover finer-grained access, but at higher memory cost and lower throughput. The usefulness of V_1 is unlikely to be constant across tokens, heads, and contexts; different positions plausibly require different amounts of access to early lexical or semantic information. We therefore treat early-representation reuse as a retrieval problem rather than a connectivity problem, and introduce Selective Access Transformer (SATFormer), which preserves the first-layer value pathway while controlling access with a context-dependent gate. Across models from 130M to 1.3B parameters, SATFormer consistently improves validation loss and zero-shot accuracy over the static value-residual and Transformer baselines. Its strongest gains appear on retrieval-intensive benchmarks, where it improves over static value residuals by approximately 1.5 average points, while maintaining throughput and memory usage close to the baseline Transformer. Gate analyses suggest sparse, depth-dependent, head-specific, and category-sensitive access patterns, supporting the interpretation that SATFormer learns selective reuse of early representations rather than uniform residual copying. Our code is available at https://github.com/SkyeGunasekaran/SATFormer.
匹配关键词: language model
---

[ACADEMIC - ARXIV]
标题: The Counterexample Game: Iterated Conceptual Analysis and Repair in Language Models
作者: Daniel Drucker, Kyle Mahowald
链接: https://arxiv.org/abs/2605.03936v1
完整摘要: Conceptual analysis -- proposing definitions and refining them through counterexamples -- is central to philosophical methodology. We study whether language models can perform this task through iterated analysis and repair chains: one model instance generates counterexamples to a proposed definition, another repairs the definition, and the process repeats. Across 20 concepts and thousands of counterexample-repair cycles, we find that, although many LM-generated counterexamples are judged invalid by both expert humans and an LM judge, the LM judge accepts roughly twice as many as humans do. Nonetheless, per-item validity judgments are moderately consistent across humans and between humans and the LM. We further find that extended iteration produces increasingly verbose definitions without improving accuracy. We also see that some concepts resist stable definitions in general. These findings suggest that while LMs can engage in philosophical reasoning, the counterexample-repair loop hits diminishing returns quickly and could be a fruitful test case for evaluating whether LMs can sustain high-level iterated philosophical reasoning.
匹配关键词: mixture of experts
---

[ACADEMIC - ARXIV]
标题: Raising the Ceiling: Better Empirical Fixation Densities for Saliency Benchmarking
作者: Susmit Agrawal, Jannis Hollman, Matthias Kümmerer
链接: https://arxiv.org/abs/2605.03885v1
完整摘要: Empirical fixation densities, spatial distributions estimated from human eye-tracking data, are foundational to saliency benchmarking. They directly shape benchmark conclusions, leaderboard rankings, failure case analyses, and scientific claims about human visual behavior. Yet the standard estimation method, fixed-bandwidth isotropic Gaussian KDE, has gone essentially unchanged for decades. This matters now more than ever: as the field shifts toward sample-level evaluation (failure case analysis, inverse benchmarking, per-image model comparison), reliable per-image density estimates become critical. We propose a principled mixture model that combines an adaptive-bandwidth KDE based on Abramson's method, center bias and uniform components, and a state-of-the-art saliency model, to capture different spatial and semantic types of interobserver consistency, and optimize all parameters per image via leave-one-subject-out cross-validation. Our method yields substantially higher interobserver consistency estimates across multiple benchmarks, with median per-image gains of 5-15% in log-likelihood and up to 2 percentage points in AUC. For the most affected images -- precisely those most relevant to failure case analysis -- improvements exceed 25%. We leverage these improved estimates to identify and analyze remaining failure cases of state-of-the-art saliency models, demonstrating that significant headroom for model improvement remains. More broadly, our findings highlight that empirical fixation densities should not be treated as fixed ground truths but as evolving estimates that improve with better methodology.
匹配关键词: mixture of experts
---

[ACADEMIC - ARXIV]
标题: Parameter-Efficient Multi-View Proficiency Estimation: From Discriminative Classification to Generative Feedback
作者: Edoardo Bianchi, Antonio Liotta
链接: https://arxiv.org/abs/2605.03848v1
完整摘要: Estimating how well a person performs an action, rather than which action is performed, is central to coaching, rehabilitation, and talent identification. This task is challenging because proficiency is encoded in subtle differences in timing, balance, body mechanics, and execution, often distributed across multiple views and short temporal events. We discuss three recent contributions to multi-view proficiency estimation on Ego-Exo4D. SkillFormer introduces a parameter-efficient discriminative architecture for selective multi-view fusion; PATS improves temporal sampling by preserving locally dense excerpts of fundamental movements; and ProfVLM reformulates proficiency estimation as conditional language generation, producing both a proficiency label and expert-style feedback through a gated cross-view projector and a compact language backbone. Together, these methods achieve state-of-the-art accuracy on Ego-Exo4D with up to 20x fewer trainable parameters and up to 3x fewer training epochs than video-transformer baselines, while moving from closed-set classification toward interpretable feedback generation. These results highlight a shift toward efficient, multi-view systems that combine selective fusion, proficiency-aware sampling, and actionable generative feedback.
匹配关键词: mixture of experts
---

[ACADEMIC - ARXIV]
标题: SigLoMa: Learning Open-World Quadrupedal Loco-Manipulation from Ego-Centric Vision
作者: Shiyi Chen, Haiyi Liu, Mingye Yang, Jiaqi Zhang, Debing Zhang
链接: https://arxiv.org/abs/2605.03846v1
完整摘要: Designing an open-world quadrupedal loco-manipulation system is highly challenging. Traditional reinforcement learning frameworks utilizing exteroception often suffer from extreme sample inefficiency and massive sim-to-real gaps. Furthermore, the inherent latency of visual tracking fundamentally conflicts with the high-frequency demands of precise floating-base control. Consequently, existing systems lean heavily on expensive external motion capture and off-board computation. To eliminate these dependencies, we present SigLoMa, a fully onboard, ego-centric vision-based pick-and-place framework. At the core of SigLoMa is the introduction of Sigma Points, a lightweight geometric representation for exteroception that guarantees high scalability and native sim-to-real alignment. To bridge the frequency divide between slow perception and fast control, we design an ego-centric Kalman Filter to provide robust, high-rate state estimation. On the learning front, we alleviate sample inefficiency via an Active Sampling Curriculum guided by Hint Poses, and tackle the robot's structural visual blind spots using temporal encoding coupled with simulated random-walk drift. Real-world experiments validate that, relying solely on a 5Hz (200 ms latency) open-vocabulary detector, SigLoMa successfully executes dynamic loco-manipulation across multiple tasks, achieving performance comparable to expert human teleoperation.
匹配关键词: mixture of experts
---

[ACADEMIC - ARXIV]
标题: On Computing Total Variation Distance Between Mixtures of Product Distributions
作者: Weiming Feng, Yucheng Fu, Minji Yang, Anqi Zhang
链接: https://arxiv.org/abs/2605.03839v1
完整摘要: We study the problem of approximating the total variation distance between two mixtures of product distributions over an $n$-dimensional discrete domain. Given two mixtures $\mathbb{P}$ and $\mathbb{Q}$ with $k_1$ and $k_2$ product distributions over $[q]^n$, respectively, we give a randomized algorithm that approximates $d_{\mathrm{TV}}\left({\mathbb{P}},{\mathbb{Q}}\right)$ within a multiplicative error of $(1\pm \varepsilon)$ in time $\mathrm{poly}((nq)^{k_1+k_2},1/\varepsilon)$. We also study the special case of mixtures of Boolean subcubes over $\{0,1\}^n$. For this class, we give a deterministic algorithm that exactly computes the total variation distance in time $\mathrm{poly}(n,2^{O(k_1+k_2)})$, and show that exact computation is $\#\mathsf{P}$-hard when $k_1+k_2=Θ(n)$.
匹配关键词: mixture of experts
---

[ACADEMIC - ARXIV]
标题: Feature-Augmented Transformers for Robust AI-Text Detection Across Domains and Generators
作者: Mohamed Mady, Johannes Reschke, Björn Schuller
链接: https://arxiv.org/abs/2605.03969v1
完整摘要: AI-generated text is nowadays produced at scale across domains and heterogeneous generation pipelines, making robustness to distribution shift a central requirement for supervised binary detectors. We train transformer-based detectors on HC3 PLUS and calibrate a single decision threshold by maximising balanced accuracy on held-out validation; this threshold is then kept fixed for all downstream test distributions, revealing domain- and generator-dependent error asymmetries under shift. We evaluate in-domain on HC3 PLUS, under cross-dataset transfer to the multi-domain, multi-generator M4 benchmark, and on the external AI-Text-Detection-Pile. Although base models achieve near-ceiling in-domain performance (up to 99.5% balanced accuracy), performance under shift is brittle and strongly model-dependent. Feature augmentation via attention-based linguistic feature fusion improves transfer, with our best model (DeBERTa-v3-base+FeatAttn) achieving 85.9% balanced accuracy on M4. Multi-seed experiments confirm high stability. Under the same fixed-threshold protocol, our model outperforms strong zero-shot baselines by up to +7.22 points. Category-level ablations further show that readability and vocabulary features contribute most to robustness under shift. Overall, these results demonstrate that feature augmentation and a modern DeBERTa backbone significantly outperform earlier BERT/RoBERTa models, while the fixed-threshold protocol provides a more realistic and informative assessment of practical detector robustness.
匹配关键词: transformer architecture
---

[ACADEMIC - ARXIV]
标题: Transformers with Selective Access to Early Representations
作者: Skye Gunasekaran, Téa Wright, Rui-Jie Zhu, Jason Eshraghian
链接: https://arxiv.org/abs/2605.03953v1
完整摘要: Several recent Transformer architectures expose later layers to representations computed in the earliest layers, motivated by the observation that low-level features can become harder to recover as the residual stream is repeatedly transformed through depth. The cheapest among these methods add static value residuals: learned mixing coefficients that expose the first-layer value projection V_1 uniformly across tokens and heads. More expressive dense or dynamic alternatives recover finer-grained access, but at higher memory cost and lower throughput. The usefulness of V_1 is unlikely to be constant across tokens, heads, and contexts; different positions plausibly require different amounts of access to early lexical or semantic information. We therefore treat early-representation reuse as a retrieval problem rather than a connectivity problem, and introduce Selective Access Transformer (SATFormer), which preserves the first-layer value pathway while controlling access with a context-dependent gate. Across models from 130M to 1.3B parameters, SATFormer consistently improves validation loss and zero-shot accuracy over the static value-residual and Transformer baselines. Its strongest gains appear on retrieval-intensive benchmarks, where it improves over static value residuals by approximately 1.5 average points, while maintaining throughput and memory usage close to the baseline Transformer. Gate analyses suggest sparse, depth-dependent, head-specific, and category-sensitive access patterns, supporting the interpretation that SATFormer learns selective reuse of early representations rather than uniform residual copying. Our code is available at https://github.com/SkyeGunasekaran/SATFormer.
匹配关键词: transformer architecture
---

[ACADEMIC - ARXIV]
标题: TabSurv: Adapting Modern Tabular Neural Networks to Survival Analysis
作者: Stanislav Kirpichenko, Andrei Konstantinov, Lev Utkin
链接: https://arxiv.org/abs/2605.03944v1
完整摘要: Survival analysis on tabular data is a well-studied problem. However, existing deep learning methods are often highly task-specific, which can limit the transfer of new approaches from other domains and introduce constraints that may affect performance. We propose TabSurv, an approach that adapts modern tabular architectures to survival analysis using either the Weibull distribution or non-parametric survival prediction. TabSurv optimizes SurvHL, a novel histogram loss function supporting censored data. In addition to a baseline feed-forward network, we implement deep ensembles of MLPs for survival analysis within TabSurv. In contrast to prior work, the ensemble components are trained in parallel, optimizing survival distribution parameters before averaging, which promotes diversity across ensemble component predictions. We perform a comprehensive empirical evaluation of different proposed architectures on 10 diverse real-world survival datasets. Our results show that TabSurv consistently outperforms on average established classical and deep learning baselines, such as RSF, DeepSurv, DeepHit, SurvTRACE. Notably, deep ensembles with Weibull parametrization instead of non-parametric models achieve the highest average rank by C-index. Overall, our study clarifies how modern tabular neural networks can be adapted and trained to tackle survival analysis problems, offering a strong and reliable approach. The TabSurv implementation is publicly available.
匹配关键词: transformer architecture
---

[ACADEMIC - ARXIV]
标题: Towards Open World Sound Event Detection
作者: P. H. Hai, L. T. Minh, L. H. Son
链接: https://arxiv.org/abs/2605.03934v1
完整摘要: Sound Event Detection (SED) plays a vital role in audio understanding, with applications in surveillance, smart cities, healthcare, and multimedia indexing. However, conventional SED systems operate under a closed-world assumption, limiting their effectiveness in real-world environments where novel acoustic events frequently emerge. Inspired by the success of open-world learning in computer vision, we introduce the Open-World Sound Event Detection (OW-SED) paradigm, where models must detect known events, identify unseen ones, and incrementally learn from them. To tackle the unique challenges of OW-SED, such as overlapping and ambiguous events, we propose a 1D Deformable architecture that leverages deformable attention to adaptively focus on salient temporal regions. Furthermore, we design a novel Open-World Deformable Sound Event Detection Transformer (WOOT) framework incorporating feature disentanglement to separate class-specific and class-agnostic representations, together with a one-to-many matching strategy and a diversity loss to enhance representation diversity. Experimental results demonstrate that our method achieves marginally superior performance compared to existing leading techniques in closed-world settings and significantly improves over existing baselines in open-world scenarios.
匹配关键词: transformer architecture
---

[ACADEMIC - ARXIV]
标题: Magic-Informed Quantum Architecture Search
作者: Vincenzo Lipardi, Domenica Dibenedetto, Georgios Stamoulis, Mark H. M. Winands
链接: https://arxiv.org/abs/2605.03932v1
完整摘要: Nonstabilizerness, commonly referred to as magic, is a fundamental resource underpinning quantum advantage. In this paper, we propose a magic-informed quantum architecture search (QAS) technique that enables control over a quantum resource within the general framework of circuit design. Inspired by the AlphaGo approach, we tackle the problem with a Monte Carlo Tree Search technique equipped with a Graph Neural Network (GNN) that estimates the magic of candidate quantum circuits. The GNN model induces a magic-based bias that steers the search toward either high- or low-magic regimes, depending on the target objective. We benchmark the proposed magic-informed QAS technique on both the structured ground-state energy problem and on the more general quantum state approximation problem, spanning different sizes and target magic levels. Experimental results show that the proposed technique effectively influences the magic across the search tree and notably also on the resulting final circuit, even in regimes where the GNN operates on out-of-distribution instances. Although introducing a problem-agnostic magic bias could, in principle, constrain the search dynamics, we observe consistent improvements in solution quality across all problems tested.
匹配关键词: transformer architecture
---

[ACADEMIC - ARXIV]
标题: EvoLM: Self-Evolving Language Models through Co-Evolved Discriminative Rubrics
作者: Shuyue Stella Li, Rui Xin, Teng Xiao, Yike Wang, Rulin Shao, Zoey Hao, Melanie Sclar, Sewoong Oh, Faeze Brahman, Pang Wei Koh, Yulia Tsvetkov
链接: https://arxiv.org/abs/2605.03871v1
完整摘要: Language models encode substantial evaluative knowledge from pretraining, yet current post-training methods rely on external supervision (human annotations, proprietary models, or scalar reward models) to produce reward signals. Each imposes a ceiling. Human judgment cannot supervise capabilities beyond its own, proprietary APIs create dependencies, and verifiable rewards cover only domains with ground-truth answers. Self-improvement from a model's own evaluative capacity is a reward source that scales with the model itself, yet remains largely untapped by current methods. We introduce EVOLM, a post-training method that structures this capacity into explicit discriminative rubrics and uses them as training signal. EVOLM trains two capabilities within a single language model in alternation: (1) a rubric generator producing instance-specific evaluation criteria optimized for discriminative utility, which maximizes a small frozen judge's ability to distinguish preferred from dispreferred responses; and (2) a policy trained using those rubric-conditioned scores as reward. All preference signals are constructed from the policy's own outputs via temporal contrast with earlier checkpoints, requiring no human annotation or external supervision. EVOLM trains a Qwen3-8B model to generate rubrics that outperform GPT-4.1 on RewardBench-2 by 25.7%. The co-trained policy achieves 69.3% average on the OLMo3-Adapt suite, outperforming policies trained with GPT-4.1 prompted rubrics by 3.9% and with the state-of-the-art 8B reward model SkyWork-RM by 16%. Overall, EVOLM demonstrates that structuring a model's evaluative capacity into co-evolving discriminative rubrics enables self-improvement without external supervision.
匹配关键词: post-training
---

[ACADEMIC - ARXIV]
标题: RoboAlign-R1: Distilled Multimodal Reward Alignment for Robot Video World Models
作者: Hao Wu, Yuqi Li, Yuan Gao, Fan Xu, Fan Zhang, Kun Wang, Penghao Zhao, Qiufeng Wang, Yizhou Zhao, Weiyan Wang, Yingli Tian, Xian Wu, Xiaomeng Huang
链接: https://arxiv.org/abs/2605.03821v1
完整摘要: Existing robot video world models are typically trained with low-level objectives such as reconstruction and perceptual similarity, which are poorly aligned with the capabilities that matter most for robot decision making, including instruction following, manipulation success, and physical plausibility. They also suffer from error accumulation in long-horizon autoregressive prediction. We present RoboAlign-R1, a framework that combines reward-aligned post-training with stabilized long-horizon inference for robot video world models. We construct RobotWorldBench, a benchmark of 10,000 annotated video-instruction pairs collected from four robot data sources, and train a multimodal teacher judge, RoboAlign-Judge, to provide fine-grained six-dimensional evaluation of generated videos. We then distill the teacher into a lightweight student reward model for efficient reinforcement-learning-based post-training. To reduce long-horizon rollout drift, we further introduce Sliding Window Re-encoding (SWR), a training-free inference strategy that periodically refreshes the generation context. Under our in-domain evaluation protocol, RoboAlign-R1 improves the aggregate six-dimension score by 10.1% over the strongest baseline, including gains of 7.5% on Manipulation Accuracy and 4.6% on Instruction Following; these ranking improvements are further supported by an external VLM-based cross-check and a blinded human study. Meanwhile, SWR improves long-horizon prediction quality with only about 1% additional latency, yielding a 2.8% gain in SSIM and a 9.8% reduction in LPIPS. Together, these results show that reward-aligned post-training and stabilized long-horizon decoding improve task consistency, physical realism, and long-horizon prediction quality in robot video world models.
匹配关键词: post-training
---

[ACADEMIC - ARXIV]
标题: Uni-OPD: Unifying On-Policy Distillation with a Dual-Perspective Recipe
作者: Wenjin Hou, Shangpin Peng, Weinong Wang, Zheng Ruan, Yue Zhang, Zhenglin Zhou, Mingqi Gao, Yifei Chen, Kaiqi Wang, Hongming Yang, Chengquan Zhang, Zhuotao Tian, Han Hu, Yi Yang, Fei Wu, Hehe Fan
链接: https://arxiv.org/abs/2605.03677v1
完整摘要: On-policy distillation (OPD) has recently emerged as an effective post-training paradigm for consolidating the capabilities of specialized expert models into a single student model. Despite its empirical success, the conditions under which OPD yields reliable improvement remain poorly understood. In this work, we identify two fundamental bottlenecks that limit effective OPD: insufficient exploration of informative states and unreliable teacher supervision for student rollouts. Building on this insight, we propose Uni-OPD, a unified OPD framework that generalizes across Large Language Models (LLMs) and Multimodal Large Language Models (MLLMs), centered on a dual-perspective optimization strategy. Specifically, from the student's perspective, we adopt two data balancing strategies to promote exploration of informative student-generated states during training. From the teacher's perspective, we show that reliable supervision hinges on whether aggregated token-level guidance remains order-consistent with the outcome reward. To this end, we develop an outcome-guided margin calibration mechanism to restore order consistency between correct and incorrect trajectories. We conduct extensive experiments on 5 domains and 16 benchmarks covering diverse settings, including single-teacher and multi-teacher distillation across LLMs and MLLMs, strong-to-weak distillation, and cross-modal distillation. Our results verify the effectiveness and versatility of Uni-OPD and provide practical insights into reliable OPD.
匹配关键词: post-training
---

[ACADEMIC - ARXIV]
标题: Erase Persona, Forget Lore: Benchmarking Multimodal Copyright Unlearning in Large Vision Language Models
作者: JuneHyoung Kwon, JungMin Yun, YoungBin Kim
链接: https://arxiv.org/abs/2605.03547v1
完整摘要: Large Vision-Language Models (LVLMs), trained on web-scale data, risk memorizing and regenerating copyrighted visual content such as characters and logos, creating significant challenges. Machine unlearning offers a path to mitigate these risks by removing specific content post-training, but evaluating its effectiveness, especially in the complex multimodal setting of LVLMs, remains an open problem. Current evaluation methods often lack robustness or fail to capture the nuances of cross-modal concept erasure. To address this critical gap, we introduce the CoVUBench benchmark, the first framework specifically designed for evaluating copyright content unlearning in LVLMs. CoVUBench utilizes procedurally generated, legally safe synthetic data coupled with systematic visual variations spanning compositional changes and diverse domain manifestations to ensure realistic and robust evaluation of unlearning generalization. Our comprehensive multimodal evaluation protocol assesses both forgetting efficacy from the copyright holder perspective and the preservation of general model utility from the deployer viewpoint. By rigorously measuring this crucial trade-off, CoVUBench provides a standardized tool to advance the development of responsible and effective unlearning methods for LVLMs.
匹配关键词: post-training
---

[ACADEMIC - ARXIV]
标题: Orientation-Aware Unsupervised Domain Adaptation for Brain Tumor Classification Across Multi-Modal MRI
作者: Sapna Sachan, Amulya Kumar Mahto, Prashant Wagambar Patil
链接: https://arxiv.org/abs/2605.03490v1
完整摘要: The clinical integration of deep learning models for brain tumor diagnosis in neuro-oncology is severely constrained by limited expert-annotated MRI data and substantial inter-institutional domain shift arising from variations in scanners, imaging protocols, and contrast settings. These challenges significantly impair model generalization in real-world settings. To address this, we propose a novel orientation-aware unsupervised domain-adaptive framework for automated brain tumor classification using mixed 2D MRI slices. Initially, a CNN with large receptive field first categorizes input slices into axial, sagittal, and coronal views. For each orientation, a CNN architecture with ResNet50 backbone augmented with four fully connected layers is trained to extract discriminative features for tumor classification. To mitigate annotation scarcity and domain discrepancies, we introduce a slice-wise unsupervised domain adaptation strategy that transfers knowledge from the multi-modal such as T1, T2, and FLAIR source domain to the post-contrast T1 target domain. Feature-level alignment is enforced using maximum mean discrepancy loss, complemented by pseudo-label guided adaptation to preserve class discriminability. Extensive experiments demonstrate improved target-domain performance over prior approaches, highlighting the benefits of orientation-specific learning, multi-modal knowledge transfer, pseudo-label-guided adaptation, and unsupervised domain adaptation.
匹配关键词: post-training
---

[ACADEMIC - ARXIV]
标题: Label-Efficient School Detection from Aerial Imagery via Weakly Supervised Pretraining and Fine-Tuning
作者: Zakarya Elmimouni, Fares Fourati, Mohamed-Slim Alouini
链接: https://arxiv.org/abs/2605.03968v1
完整摘要: Accurate school detection is essential for supporting education initiatives, including infrastructure planning and expanding internet connectivity to underserved areas. However, many regions around the world face challenges due to outdated, incomplete, or unavailable official records. Manual mapping efforts, while valuable, are labor-intensive and lack scalability across large geographic areas. To address this, we propose a weakly supervised framework for school detection from aerial imagery that minimizes the need for human annotations while supporting global mapping efforts. Our method is specifically designed for low-data regimes, where manual annotations are extremely scarce. We introduce an automatic labeling pipeline that leverages sparse location points and semantic segmentation to generate infrastructure masks from which we generate bounding boxes. Using these automatically labeled images, we train our detectors on a first training stage to learn a representation of what schools look like, then using a small set of manually labeled images, we fine-tune the previously trained models on this clean dataset. This two stage training pipeline enables large-scale and strong detection in low-data setting of school infrastructure with minimal supervision. Our results demonstrate strong object detection performance, particularly in the low-data regime, where the models achieve promising results using only 50 manually labeled images, significantly reducing the need for costly annotations. This framework supports education and connectivity initiatives worldwide by providing an efficient and extensible approach to mapping schools from space. All models, training code and auto-labeled data will be publicly released to foster future research and real-world impact.
匹配关键词: fine-tuning
---

[ACADEMIC - ARXIV]
标题: Pretrained Model Representations as Acquisition Signals for Active Learning of MLIPs
作者: Eszter Varga-Umbrich, Shikha Surana, Paul Duckworth, Jules Tilly, Olivier Peltre, Zachary Weller-Davies
链接: https://arxiv.org/abs/2605.03964v1
完整摘要: Training machine learning interatomic potentials (MLIPs) for reactive chemistry is often bottlenecked by the high cost of quantum chemical labels and the scarcity of transition state configurations in candidate pools. Active learning (AL) can mitigate these costs, but its effectiveness hinges on the acquisition rule. We investigate whether the latent space of a pretrained MLIP already contains the information necessary for effective acquisition, eliminating the need for auxiliary uncertainty heads, Bayesian training and fine-tuning, or committee ensembles. We introduce two acquisition signals derived directly from a pretrained MACE potential: a finite-width neural tangent kernel (NTK) and an activation kernel built from hidden latent space features. On reactive-chemistry benchmarks, both kernels consistently outperform fixed-descriptor baselines, committee disagreement, and random acquisition, reducing the data required to reach performance targets by an average of 38% for energy error and 28% for force error. We further show that the pretrained model induces similarity spaces that preserve chemically meaningful structure and provide more reliable residual uncertainty estimates than randomly initialised or fixed-descriptor-based kernels. Our results suggest that pretraining aligns latent-space geometry with model error, yielding a practical and sufficient acquisition signal for reactive MLIP fine-tuning.
匹配关键词: fine-tuning
---

[ACADEMIC - ARXIV]
标题: StateVLM: A State-Aware Vision-Language Model for Robotic Affordance Reasoning
作者: Xiaowen Sun, Matthias Kerzel, Mengdi Li, Xufeng Zhao, Paul Striker, Stefan Wermter
链接: https://arxiv.org/abs/2605.03927v1
完整摘要: Vision-language models (VLMs) have shown remarkable performance in various robotic tasks, as they can perceive visual information and understand natural language instructions. However, when applied to robotics, VLMs remain subject to a fundamental limitation inherent in large language models (LLMs): they struggle with numerical reasoning, particularly in object detection and object-state localization. To explore numerical reasoning as a regression task in VLMs, we propose a novel training strategy to adapt VLMs for object detection and object-state localization. This approach leverages box decoder outputs to compute an Auxiliary Regression Loss (ARL) during fine-tuning, while preserving standard sequence prediction at inference. We leverage this training strategy to develop StateVLM (State-aware Vision-Language Model), a novel model designed to perceive and learn fine-grained object representations, including precise localization of objects and their states, as well as graspable regions. Due to the lack of a benchmark for object-state affordance reasoning, we introduce an open-source benchmark, Object State Affordance Reasoning (OSAR), which contains 1,172 scenes with 7,746 individual objects and corresponding bounding boxes. Comparative experiments on adapted benchmarks (RefCOCO, RefCOCO+, and \mbox{RefCOCOg}) demonstrate that ARL improves model performance by an average of 1.6\% compared to models without ARL. Experiments on the OSAR benchmark further support this finding, showing that StateVLM with ARL achieves an average of 5.2\% higher performance than models without ARL. In particular, ARL is also important for the complex task of affordance reasoning in OSAR, where it enhances the consistency of model outputs.
匹配关键词: fine-tuning
---

[ACADEMIC - ARXIV]
标题: Ecologically-Constrained Task Arithmetic for Multi-Taxa Bioacoustic Classifiers Without Shared Data
作者: Ragib Amin Nihal, Benjamin Yen, Runwu Shi, Takeshi Ashizawa, Kazuhiro Nakadai
链接: https://arxiv.org/abs/2605.03914v1
完整摘要: Training data for bioacoustics is scattered across taxa, regions, and institutions. Centralizing it all is often infeasible. We show that independently fine-tuned BEATs encoders can be composed into a unified 661-species classifier via task vector arithmetic without sharing data. We find that bioacoustic task vectors are near-orthogonal (cosine 0.01-0.09). Their separation aligns closely with spectral distribution distance, a gradient consistent with the acoustic niche hypothesis. This geometry makes simple averaging optimal while sign-conflict methods reduce accuracy by one to six percentage points. Composition also creates an asymmetric gap: species-rich groups lose accuracy relative to joint training while underrepresented taxa gain, a redistribution useful for equitable biodiversity monitoring. We verify linear mode connectivity across all taxonomic pairs, demonstrate zero-shot transfer to new regions, and identify domain negation as a boundary condition where composition fails. These results enable a collaborative paradigm for bioacoustics where institutions share only task vectors to assemble multi-taxa classifiers, preserving data privacy.
匹配关键词: fine-tuning
---

[ACADEMIC - ARXIV]
标题: DMGD: Train-Free Dataset Distillation with Semantic-Distribution Matching in Diffusion Models
作者: Qichao Wang, Yunhong Lu, Hengyuan Cao, Junyi Zhang, Min Zhang
链接: https://arxiv.org/abs/2605.03877v1
完整摘要: Dataset distillation enables efficient training by distilling the information of large-scale datasets into significantly smaller synthetic datasets. Diffusion based paradigms have emerged in recent years, offering novel perspectives for dataset distillation. However, they typically necessitate additional fine-tuning stages, and effective guidance mechanisms remain underexplored. To address these limitations, we rethink diffusion based dataset distillation and propose a Dual Matching Guided Diffusion (DMGD) framework, centered on efficient training-free guidance. We first establish Semantic Matching via conditional likelihood optimization, eliminating the need for auxiliary classifiers. Furthermore, we propose a dynamic guidance mechanism that enhances the diversity of synthetic data while maintaining semantic alignment. Simultaneously, we introduce an optimal transport (OT) based Distribution Matching approach to further align with the target distribution structure. To ensure efficiency, we develop two enhanced strategies for diffusion based framework: Distribution Approximate Matching and Greedy Progressive Matching. These strategies enable effective distribution matching guidance with minimal computational overhead. Experimental results on ImageNet-Woof, ImageNet-Nette, and ImageNet-1K demonstrate that our training-free approach achieves significant improvements, outperforming state-of-the-art (SOTA) methods requiring additional fine-tuning by average accuracy gains of 2.1%, 5.4%, and 2.4%, respectively.
匹配关键词: fine-tuning
---

[ACADEMIC - ARXIV]
标题: OracleProto: A Reproducible Framework for Benchmarking LLM Native Forecasting via Knowledge Cutoff and Temporal Masking
作者: Yiding Ma, Chengyun Ruan, Kaibo Huang, Zhongliang Yang, Linna Zhou
链接: https://arxiv.org/abs/2605.03762v1
完整摘要: Large language models are moving from static text generators toward real-world decision-support systems, where forecasting is a composite capability that links information gathering, evidence integration, situational judgment, and action-oriented decision making. This capability is in broad demand across finance, policy, industry, and scientific research, yet its evaluation remains difficult: live benchmarks evaluate forecasts before answers exist, making them the cleanest way to measure forecasting ability, but they expire once events resolve; retrospective benchmarks are reproducible, but they cannot reliably distinguish genuine forecasting from facts a model may have already learned during pretraining. Prompting models to "pretend not to know" cannot replace a genuine knowledge boundary. We propose OracleProto, a reproducible framework for evaluating LLM native forecasting capability. OracleProto reconstructs resolved events into time-bounded forecasting samples by combining model-cutoff-aligned sample admission, tool-level temporal masking, content-level leakage detection, discrete answer normalization, and hierarchical scoring. Instantiated on a FutureX-Past-derived dataset with six contemporary LLMs, OracleProto distinguishes forecasting quality, sampling stability, and cost efficiency under controlled information boundaries, while reducing residual leakage to the $1\%$ level, an order of magnitude below tool-only temporal filtering. OracleProto turns LLM forecasting from one-off evaluation into an auditable, reusable, and trainable dataset-level capability, providing a unified interface for fair cross-model comparison and a controlled signal source for downstream SFT and RL. Code and data are available at https://github.com/MaYiding/OracleProto and https://huggingface.co/datasets/MaYiding/OracleProto.
匹配关键词: SFT
---

[ACADEMIC - ARXIV]
标题: MHPR: Multidimensional Human Perception and Reasoning Benchmark for Large Vision-Languate Models
作者: Kangkang Wang, Qinting Jiang, Wanping Zhang, Bowen Ren, Shengzhao Wen
链接: https://arxiv.org/abs/2605.03485v1
完整摘要: Multidimensional human understanding is essential for real-world applications such as film analysis and virtual digital humans, yet current LVLM benchmarks largely focus on single-task settings and lack fine-grained, human-centric evaluation. In this work, we introduce MHPR, a comprehensive benchmark for joint perception-reasoning over human-centric scenes spanning individual, multi-person, and human-object interaction dimensions. MHPR comprises a multi-level data design-Captioned Raw Data (C-RD), Supervised Fine-Tuning Data (SFT-D), Reinforcement Learning Data (RL-D), and Test Data (T-D)-together with an automated caption/VQA generation pipeline (ACVG) that performs category-wise attribute decomposition, attribute-specific rewriting, and multi-model voting to ensure high-quality, scalable annotations. We evaluate state-of-the-art vision-language models on fine-grained attributes (appearance, clothing, pose, parts) and high-level semantics (social relations, action semantics, spatial relations, intent and functionality). Our findings show that: 1) format-aligned SFT data substantially improves instruction following and stability; 2) challenge-focused RL data derived from bad-case analysis further enhances perception and reasoning on difficult instances; and 3) training Qwen2.5-VL-7B with MHPR yields significant gains, achieving near-parity with considerably larger models. We release ACVG and MHPR to facilitate reproducible, extensible research on human-centric perception and reasoning.
匹配关键词: SFT
---

[ACADEMIC - ARXIV]
标题: When to Think, When to Speak: Learning Disclosure Policies for LLM Reasoning
作者: Jiaqi Wei, Xuehang Guo, Pengfei Yu, Xiang Zhang, Wanli Ouyang, Siqi Sun, Qingyun Wang, Chenyu You
链接: https://arxiv.org/abs/2605.03314v1
完整摘要: In single-stream autoregressive interfaces, the same tokens both update the model state and constitute an irreversible public commitment. This coupling creates a \emph{silence tax}: additional deliberation postpones the first \emph{task-relevant} content, while naive early streaming risks premature commitments that bias subsequent generations. We introduce \textbf{\emph{Side-by-Side (SxS)}} Interleaved Reasoning, which makes \emph{disclosure timing} a controllable decision within standard autoregressive generation. SxS interleaves partial disclosures with continued private reasoning in the same context, but releases content only when it is \emph{supported} by the reasoning so far. To learn such pacing without incentivizing filler, we construct entailment-aligned interleaved trajectories by matching answer prefixes to supporting reasoning prefixes, then train with SFT to acquire the dual-action semantics and RL to recover reasoning performance under the new format. Across two Qwen3 architectures/scales (MoE \textbf{Qwen3-30B-A3B}, dense \textbf{Qwen3-4B}) and both in-domain (AIME25) and out-of-domain (GPQA-Diamond) benchmarks, SxS improves accuracy--\emph{content-latency} Pareto trade-offs under token-level proxies (e.g., inter-update waiting).
匹配关键词: SFT
---

[ACADEMIC - ARXIV]
标题: Label-Efficient School Detection from Aerial Imagery via Weakly Supervised Pretraining and Fine-Tuning
作者: Zakarya Elmimouni, Fares Fourati, Mohamed-Slim Alouini
链接: https://arxiv.org/abs/2605.03968v1
完整摘要: Accurate school detection is essential for supporting education initiatives, including infrastructure planning and expanding internet connectivity to underserved areas. However, many regions around the world face challenges due to outdated, incomplete, or unavailable official records. Manual mapping efforts, while valuable, are labor-intensive and lack scalability across large geographic areas. To address this, we propose a weakly supervised framework for school detection from aerial imagery that minimizes the need for human annotations while supporting global mapping efforts. Our method is specifically designed for low-data regimes, where manual annotations are extremely scarce. We introduce an automatic labeling pipeline that leverages sparse location points and semantic segmentation to generate infrastructure masks from which we generate bounding boxes. Using these automatically labeled images, we train our detectors on a first training stage to learn a representation of what schools look like, then using a small set of manually labeled images, we fine-tune the previously trained models on this clean dataset. This two stage training pipeline enables large-scale and strong detection in low-data setting of school infrastructure with minimal supervision. Our results demonstrate strong object detection performance, particularly in the low-data regime, where the models achieve promising results using only 50 manually labeled images, significantly reducing the need for costly annotations. This framework supports education and connectivity initiatives worldwide by providing an efficient and extensible approach to mapping schools from space. All models, training code and auto-labeled data will be publicly released to foster future research and real-world impact.
匹配关键词: instruction tuning
---

[ACADEMIC - ARXIV]
标题: Pretrained Model Representations as Acquisition Signals for Active Learning of MLIPs
作者: Eszter Varga-Umbrich, Shikha Surana, Paul Duckworth, Jules Tilly, Olivier Peltre, Zachary Weller-Davies
链接: https://arxiv.org/abs/2605.03964v1
完整摘要: Training machine learning interatomic potentials (MLIPs) for reactive chemistry is often bottlenecked by the high cost of quantum chemical labels and the scarcity of transition state configurations in candidate pools. Active learning (AL) can mitigate these costs, but its effectiveness hinges on the acquisition rule. We investigate whether the latent space of a pretrained MLIP already contains the information necessary for effective acquisition, eliminating the need for auxiliary uncertainty heads, Bayesian training and fine-tuning, or committee ensembles. We introduce two acquisition signals derived directly from a pretrained MACE potential: a finite-width neural tangent kernel (NTK) and an activation kernel built from hidden latent space features. On reactive-chemistry benchmarks, both kernels consistently outperform fixed-descriptor baselines, committee disagreement, and random acquisition, reducing the data required to reach performance targets by an average of 38% for energy error and 28% for force error. We further show that the pretrained model induces similarity spaces that preserve chemically meaningful structure and provide more reliable residual uncertainty estimates than randomly initialised or fixed-descriptor-based kernels. Our results suggest that pretraining aligns latent-space geometry with model error, yielding a practical and sufficient acquisition signal for reactive MLIP fine-tuning.
匹配关键词: instruction tuning
---

[ACADEMIC - ARXIV]
标题: StateVLM: A State-Aware Vision-Language Model for Robotic Affordance Reasoning
作者: Xiaowen Sun, Matthias Kerzel, Mengdi Li, Xufeng Zhao, Paul Striker, Stefan Wermter
链接: https://arxiv.org/abs/2605.03927v1
完整摘要: Vision-language models (VLMs) have shown remarkable performance in various robotic tasks, as they can perceive visual information and understand natural language instructions. However, when applied to robotics, VLMs remain subject to a fundamental limitation inherent in large language models (LLMs): they struggle with numerical reasoning, particularly in object detection and object-state localization. To explore numerical reasoning as a regression task in VLMs, we propose a novel training strategy to adapt VLMs for object detection and object-state localization. This approach leverages box decoder outputs to compute an Auxiliary Regression Loss (ARL) during fine-tuning, while preserving standard sequence prediction at inference. We leverage this training strategy to develop StateVLM (State-aware Vision-Language Model), a novel model designed to perceive and learn fine-grained object representations, including precise localization of objects and their states, as well as graspable regions. Due to the lack of a benchmark for object-state affordance reasoning, we introduce an open-source benchmark, Object State Affordance Reasoning (OSAR), which contains 1,172 scenes with 7,746 individual objects and corresponding bounding boxes. Comparative experiments on adapted benchmarks (RefCOCO, RefCOCO+, and \mbox{RefCOCOg}) demonstrate that ARL improves model performance by an average of 1.6\% compared to models without ARL. Experiments on the OSAR benchmark further support this finding, showing that StateVLM with ARL achieves an average of 5.2\% higher performance than models without ARL. In particular, ARL is also important for the complex task of affordance reasoning in OSAR, where it enhances the consistency of model outputs.
匹配关键词: instruction tuning
---

[ACADEMIC - ARXIV]
标题: Ecologically-Constrained Task Arithmetic for Multi-Taxa Bioacoustic Classifiers Without Shared Data
作者: Ragib Amin Nihal, Benjamin Yen, Runwu Shi, Takeshi Ashizawa, Kazuhiro Nakadai
链接: https://arxiv.org/abs/2605.03914v1
完整摘要: Training data for bioacoustics is scattered across taxa, regions, and institutions. Centralizing it all is often infeasible. We show that independently fine-tuned BEATs encoders can be composed into a unified 661-species classifier via task vector arithmetic without sharing data. We find that bioacoustic task vectors are near-orthogonal (cosine 0.01-0.09). Their separation aligns closely with spectral distribution distance, a gradient consistent with the acoustic niche hypothesis. This geometry makes simple averaging optimal while sign-conflict methods reduce accuracy by one to six percentage points. Composition also creates an asymmetric gap: species-rich groups lose accuracy relative to joint training while underrepresented taxa gain, a redistribution useful for equitable biodiversity monitoring. We verify linear mode connectivity across all taxonomic pairs, demonstrate zero-shot transfer to new regions, and identify domain negation as a boundary condition where composition fails. These results enable a collaborative paradigm for bioacoustics where institutions share only task vectors to assemble multi-taxa classifiers, preserving data privacy.
匹配关键词: instruction tuning
---

[ACADEMIC - ARXIV]
标题: Task-Aware Scanning Parameter Configuration for Robotic Inspection Using Vision Language Embeddings and Hyperdimensional Computing
作者: Zhiling Chen, David Gorsich, Matthew P. Castanier, Yang Zhang, Jiong Tang, Farhad Imani
链接: https://arxiv.org/abs/2605.03909v1
完整摘要: Robotic laser profiling is widely used for dimensional verification and surface inspection, yet measurement fidelity is often dominated by sensor configuration rather than robot motion. Industrial profilers expose multiple coupled parameters, including sampling frequency, measurement range, exposure time, receiver dynamic range, and illumination, that are still tuned by trial-and-error; mismatches can cause saturation, clipping, or missing returns that cannot be recovered downstream. We formulate instruction-conditioned sensing parameter recommendation; given a pre-scan RGB observation and a natural-language inspection instruction, infer a discrete configuration over key parameters of a robot-mounted profiler. To benchmark this problem, we develop Instruct-Obs2Param, a real-world multimodal dataset linking inspection intents and multi-view pose and illumination variation across 16 objects to canonical parameter regimes. We then propose ScanHD, a hyperdimensional computing framework that binds instruction and observation into a task-aware code and performs parameter-wise associative reasoning with compact memories, matching discrete scanner regimes while yielding stable, interpretable, low-latency decisions. On Instruct-Obs2Param, ScanHD achieves 92.7% average exact accuracy and 98.1% average Win@1 accuracy across the five parameters, with strong cross-split generalization and low-latency inference suitable for deployment, outperforming rule-based heuristics, conventional multimodal models, and multimodal large language models. This work enables autonomous, instruction-conditioned sensing configuration from task intent and scene context, eliminating manual tuning and elevating sensor configuration from a static setting to an adaptive decision variable.
匹配关键词: instruction tuning
---

[ACADEMIC - ARXIV]
标题: Feature-Augmented Transformers for Robust AI-Text Detection Across Domains and Generators
作者: Mohamed Mady, Johannes Reschke, Björn Schuller
链接: https://arxiv.org/abs/2605.03969v1
完整摘要: AI-generated text is nowadays produced at scale across domains and heterogeneous generation pipelines, making robustness to distribution shift a central requirement for supervised binary detectors. We train transformer-based detectors on HC3 PLUS and calibrate a single decision threshold by maximising balanced accuracy on held-out validation; this threshold is then kept fixed for all downstream test distributions, revealing domain- and generator-dependent error asymmetries under shift. We evaluate in-domain on HC3 PLUS, under cross-dataset transfer to the multi-domain, multi-generator M4 benchmark, and on the external AI-Text-Detection-Pile. Although base models achieve near-ceiling in-domain performance (up to 99.5% balanced accuracy), performance under shift is brittle and strongly model-dependent. Feature augmentation via attention-based linguistic feature fusion improves transfer, with our best model (DeBERTa-v3-base+FeatAttn) achieving 85.9% balanced accuracy on M4. Multi-seed experiments confirm high stability. Under the same fixed-threshold protocol, our model outperforms strong zero-shot baselines by up to +7.22 points. Category-level ablations further show that readability and vocabulary features contribute most to robustness under shift. Overall, these results demonstrate that feature augmentation and a modern DeBERTa backbone significantly outperform earlier BERT/RoBERTa models, while the fixed-threshold protocol provides a more realistic and informative assessment of practical detector robustness.
匹配关键词: AI scientist
---

[ACADEMIC - ARXIV]
标题: Reservoir property image slices from the Groningen gas field for image translation and segmentation
作者: Abdulrahman Al-Fakih, Nabil Sariah, Ardiansyah Koeshidayatullah, SanLinn I. Kaka
链接: https://arxiv.org/abs/2605.03942v1
完整摘要: Reservoir characterization workflows increasingly rely on image-based and machine-learning/deep learning or even generative AI approaches, but openly available geological image datasets suitable for reproducible benchmarking remain limited. Here we describe a high-resolution dataset of reservoir-property image slices derived from the Groningen static geological model. The dataset contains aligned two-dimensional PNG images representing facies, porosity, permeability, and water saturation, generated from three-dimensional reservoir grids and prepared for downstream visualization, segmentation, and image-to-image translation tasks. In addition to the deposited original image corpus, we provide an archived software workflow for reproducing augmentation, mask generation, paired-image construction, and example baseline experiments. The resource is designed to support benchmarking of geological image analysis methods and the study of cross-domain relationships among reservoir properties. By separating the fixed image dataset from the reproducible processing workflow, this work provides a transparent foundation for reuse in geoscience, reservoir modeling, and machine-learning applications.
匹配关键词: AI scientist
---

[ACADEMIC - ARXIV]
标题: Atomic Fact-Checking Increases Clinician Trust in Large Language Model Recommendations for Oncology Decision Support: A Randomized Controlled Trial
作者: Lisa C. Adams, Linus Marx, Erik Thiele Orberg, Keno Bressem, Sebastian Ziegelmayer, Denise Bernhardt, Markus Graf, Marcus R. Makowski, Stephanie E. Combs, Florian Matthes, Jan C. Peeken
链接: https://arxiv.org/abs/2605.03916v1
完整摘要: Question: Does atomic fact-checking, which decomposes AI treatment recommendations into individually verifiable claims linked to source guideline documents, increase clinician trust compared to traditional explainability approaches? Findings: In this randomized trial of 356 clinicians generating 7,476 trust ratings, atomic fact-checking produced a large effect on trust (Cohen's d = 0.94), increasing the proportion of clinicians expressing trust from 26.9% to 66.5%. Traditional transparency mechanisms showed a dose-response gradient of improvement over baseline (d = 0.25 to 0.50). Meaning: Decomposing AI recommendations into individually verifiable claims linked to source guidelines produces substantially higher clinician trust than traditional explainability approaches in high-stakes clinical decisions.
匹配关键词: AI scientist
---

[ACADEMIC - ARXIV]
标题: Contextual Multi-Objective Optimization: Rethinking Objectives in Frontier AI Systems
作者: Jie Zhou, Qin Chen, Liang He
链接: https://arxiv.org/abs/2605.03900v1
完整摘要: Frontier AI systems perform best in settings with clear, stable, and verifiable objectives, such as code generation, mathematical reasoning, games, and unit-test-driven tasks. They remain less reliable in open-ended settings, including scientific assistance, long-horizon agents, high-stakes advice, personalization, and tool use, where the relevant objective is ambiguous, context-dependent, delayed, or only partially observable. We argue that many such failures are not merely failures of scale or capability, but failures of objective selection: the system optimizes a locally visible signal while missing which objectives should govern the interaction. We formulate this problem as \emph{contextual multi-objective optimization}. In this setting, systems must consider multiple, context-dependent objectives, such as helpfulness, truthfulness, safety, privacy, calibration, non-manipulation, user preference, reversibility, and stakeholder impact, while determining which objectives are active, which are soft preferences, and which must function as hard or quasi-hard constraints. These examples are not intended as an exhaustive taxonomy: different domains and deployment settings may activate different objective dimensions and different conflict-resolution procedures. Our framework models AI behavior as a context-dependent choice rule over candidate actions, objective estimates, active constraints, stakeholders, uncertainty, and conflict-resolution procedures. We outline an implementation pathway based on decomposed objective representations, context-to-objective routing, hierarchical constraints, deliberative policy reasoning, controlled personalization, tool-use control, diagnostic evaluation, auditing, and post-deployment revision.
匹配关键词: AI scientist
---

[ACADEMIC - ARXIV]
标题: Deco: Extending Personal Physical Objects into Pervasive AI Companion through a Dual-Embodiment Framework
作者: Zhihan Jiang, Mengyuan Millie Wu, Ruishi Zou, Shiyu Xu, Xun Qian, Emma Macmanus, Steven Liao, Ping Zhang, Bingsheng Yao, Tingyu Cheng, James L. David, Nabila El-Bassel, Lena Mamykina, Frances R. Levin, Ryan Sultan, Dakuo Wang, Xuhai Xu
链接: https://arxiv.org/abs/2605.03882v1
完整摘要: Individuals frequently form deep attachments to physical objects (e.g., plush toys) that usually cannot sense or respond to their emotions. While AI companions offer responsiveness and personalization, they exist independently of these physical objects and lack an ongoing connection to them. To bridge this gap, we conducted a formative study (N=9) to explore how digital agents could inherit and extend the emotional bond, deriving four design principles (Faithful Identity, Calibrated Agency, Ambient Presence, and Reciprocal Memory). We then present the Dual-Embodiment Companion Framework, instantiated as Deco, a mobile system integrating multimodal Large Language Models (LLMs) and Augmented Reality to create synchronized digital embodiments of users' physical companions. A within-subjects study (N=25) showed Deco significantly outperformed a personalized LLM-empowered digital companion baseline on perceived companionship, emotional bond, and design-principle scales (all p<0.01). A seven-day field deployment (N=17) showed sustained engagement, subjective well-being improvement (p=.040), and three key relational patterns: digital activities retroactively vitalized physical objects, bond deepening was driven by emotional engagement depth rather than interaction frequency, and users sustained bonds while actively navigating digital companions' AI nature. This work highlights a promising alternative for designing digital companions: moving from creating new relationships to dual embodiment, where digital agents seamlessly extend the emotional history of physical objects.
匹配关键词: AI scientist
---

[ACADEMIC - ARXIV]
标题: Label-Efficient School Detection from Aerial Imagery via Weakly Supervised Pretraining and Fine-Tuning
作者: Zakarya Elmimouni, Fares Fourati, Mohamed-Slim Alouini
链接: https://arxiv.org/abs/2605.03968v1
完整摘要: Accurate school detection is essential for supporting education initiatives, including infrastructure planning and expanding internet connectivity to underserved areas. However, many regions around the world face challenges due to outdated, incomplete, or unavailable official records. Manual mapping efforts, while valuable, are labor-intensive and lack scalability across large geographic areas. To address this, we propose a weakly supervised framework for school detection from aerial imagery that minimizes the need for human annotations while supporting global mapping efforts. Our method is specifically designed for low-data regimes, where manual annotations are extremely scarce. We introduce an automatic labeling pipeline that leverages sparse location points and semantic segmentation to generate infrastructure masks from which we generate bounding boxes. Using these automatically labeled images, we train our detectors on a first training stage to learn a representation of what schools look like, then using a small set of manually labeled images, we fine-tune the previously trained models on this clean dataset. This two stage training pipeline enables large-scale and strong detection in low-data setting of school infrastructure with minimal supervision. Our results demonstrate strong object detection performance, particularly in the low-data regime, where the models achieve promising results using only 50 manually labeled images, significantly reducing the need for costly annotations. This framework supports education and connectivity initiatives worldwide by providing an efficient and extensible approach to mapping schools from space. All models, training code and auto-labeled data will be publicly released to foster future research and real-world impact.
匹配关键词: automated research
---

[ACADEMIC - ARXIV]
标题: A Benchmark for Interactive World Models with a Unified Action Generation Framework
作者: Jianjie Fang, Yingshan Lei, Qin Wan, Ziyou Wang, Yuchao Huang, Yongyan Xu, Baining Zhao, Weichen Zhang, Chen Gao, Xinlei Chen, Yong Li
链接: https://arxiv.org/abs/2605.03941v1
完整摘要: Achieving Artificial General Intelligence (AGI) requires agents that learn and interact adaptively, with interactive world models providing scalable environments for perception, reasoning, and action. Yet current research still lacks large-scale datasets and unified benchmarks to evaluate their physical interaction capabilities. To address this, we propose iWorld-Bench, a comprehensive benchmark for training and testing world models on interaction-related abilities such as distance perception and memory. We construct a diverse dataset with 330k video clips and select 2.1k high-quality samples covering varied perspectives, weather, and scenes. As existing world models differ in interaction modalities, we introduce an Action Generation Framework to unify evaluation and design six task types, generating 4.9k test samples. These tasks jointly assess model performance across visual generation, trajectory following, and memory. Evaluating 14 representative world models, we identify key limitations and provide insights for future research. The iWorld-Bench model leaderboard is publicly available at iWorld-Bench.com.
匹配关键词: automated research
---

[ACADEMIC - ARXIV]
标题: Evaluating Generative Models as Interactive Emergent Representations of Human-Like Collaborative Behavior
作者: Shinas Shaji, Teena Chakkalayil Hassan, Sebastian Houben, Alex Mitrevski
链接: https://arxiv.org/abs/2605.03855v1
完整摘要: Human-AI collaboration requires AI agents to understand human behavior for effective coordination. While advances in foundation models show promising capabilities in understanding and showing human-like behavior, their application in embodied collaborative settings needs further investigation. This work examines whether embodied foundation model agents exhibit emergent collaborative behaviors indicating underlying mental models of their collaborators, which is an important aspect of effective coordination. This paper develops a 2D collaborative game environment where large language model agents and humans complete color-matching tasks requiring coordination. We define five collaborative behaviors as indicators of emergent mental model representation: perspective-taking, collaborator-aware planning, introspection, theory of mind, and clarification. An automated behavior detection system using LLM-based judges identifies these behaviors, achieving fair to substantial agreement with human annotations. Results from the automated behavior detection system show that foundation models consistently exhibit emergent collaborative behaviors without being explicitly trained to do so. These behaviors occur at varying frequencies during collaboration stages, with distinct patterns across different LLMs. A user study was also conducted to evaluate human satisfaction and perceived collaboration effectiveness, with the results indicating positive collaboration experiences. Participants appreciated the agents' task focus, plan verbalization, and initiative, while suggesting improvements in response times and human-like interactions. This work provides an experimental framework for human-AI collaboration, empirical evidence of collaborative behaviors in embodied LLM agents, a validated behavioral analysis methodology, and an assessment of collaboration effectiveness.
匹配关键词: automated research
---

[ACADEMIC - ARXIV]
标题: SOAR: Real-Time Joint Optimization of Order Allocation and Robot Scheduling in Robotic Mobile Fulfillment Systems
作者: Yibang Tang, Yifan Yang, Jingyuan Wang, Junhua Chen, Zhen Zhao
链接: https://arxiv.org/abs/2605.03842v1
完整摘要: Robotic Mobile Fulfillment Systems (RMFS) rely on mobile robots for automated inventory transportation, coordinating order allocation and robot scheduling to enhance warehousing efficiency. However, optimizing RMFS is challenging due to strict real-time constraints and the strong coupling of multi-phase decisions. Existing methods either decompose the problem into isolated sub-tasks to guarantee responsiveness at the cost of global optimality, or rely on computationally expensive global optimization models that are unsuitable for dynamic industrial environments. To bridge this gap, we propose SOAR, a unified Deep Reinforcement Learning framework for real-time joint optimization. SOAR transforms order allocation and robot scheduling into a unified process by utilizing soft order allocations as observations. We formulate this as an Event-Driven Markov Decision Process, enabling the agent to perform simultaneous scheduling in response to asynchronous system events. Technically, we employ a Heterogeneous Graph Transformer to encode the warehouse state and integrate phased domain knowledge. Additionally, we incorporate a reward shaping strategy to address sparse feedback in long-horizon tasks. Extensive experiments on synthetic and real-world industrial datasets, in collaboration with Geekplus, demonstrate that SOAR reduces global makespan by 7.5\% and average order completion time by 15.4\% with sub-100ms latency. Furthermore, sim-to-real deployment confirms its practical viability and significant performance gains in production environments. The code is available at https://github.com/200815147/SOAR.
匹配关键词: automated research
---

[ACADEMIC - ARXIV]
标题: A Domain Incremental Continual Learning Benchmark for ICU Time Series Model Transportability
作者: Ryan King, Conrad Krueger, Ethan Veselka, Tianbao Yang, Bobak J. Mortazavi
链接: https://arxiv.org/abs/2605.03832v1
完整摘要: In recent years, machine learning has made significant progress in clinical outcome prediction, demonstrating increasingly accurate results. However, the substantial resources required for hospitals to train these models, such as data collection, labeling, and computational power, limit the feasibility for smaller hospitals to develop their own models. An alternative approach involves transferring a machine learning model trained by a large hospital to smaller hospitals, allowing them to fine-tune the model on their specific patient data. However, these models are often trained and validated on data from a single hospital, raising concerns about their generalizability to new data. Our research shows that there are notable differences in measurement distributions and frequencies across various regions in the United States. To address this, we propose a benchmark that tests a machine learning model's ability to transfer from a source domain to different regions across the country. This benchmark assesses a model's capacity to learn meaningful information about each new domain while retaining key features from the original domain. Using this benchmark, we frame the transfer of a machine learning model from one region to another as a domain incremental learning problem. While the task of patient outcome prediction remains the same, the input data distribution varies, necessitating a model that can effectively manage these shifts. We evaluate two popular domain incremental learning methods: data replay, which stores examples from previous data sources for fine-tuning on the current source, and Elastic Weight Consolidation (EWC), a model parameter regularization method that maintains features important for both data sources.
匹配关键词: automated research
---

[ACADEMIC - ARXIV]
标题: Contextual Multi-Objective Optimization: Rethinking Objectives in Frontier AI Systems
作者: Jie Zhou, Qin Chen, Liang He
链接: https://arxiv.org/abs/2605.03900v1
完整摘要: Frontier AI systems perform best in settings with clear, stable, and verifiable objectives, such as code generation, mathematical reasoning, games, and unit-test-driven tasks. They remain less reliable in open-ended settings, including scientific assistance, long-horizon agents, high-stakes advice, personalization, and tool use, where the relevant objective is ambiguous, context-dependent, delayed, or only partially observable. We argue that many such failures are not merely failures of scale or capability, but failures of objective selection: the system optimizes a locally visible signal while missing which objectives should govern the interaction. We formulate this problem as \emph{contextual multi-objective optimization}. In this setting, systems must consider multiple, context-dependent objectives, such as helpfulness, truthfulness, safety, privacy, calibration, non-manipulation, user preference, reversibility, and stakeholder impact, while determining which objectives are active, which are soft preferences, and which must function as hard or quasi-hard constraints. These examples are not intended as an exhaustive taxonomy: different domains and deployment settings may activate different objective dimensions and different conflict-resolution procedures. Our framework models AI behavior as a context-dependent choice rule over candidate actions, objective estimates, active constraints, stakeholders, uncertainty, and conflict-resolution procedures. We outline an implementation pathway based on decomposed objective representations, context-to-objective routing, hierarchical constraints, deliberative policy reasoning, controlled personalization, tool-use control, diagnostic evaluation, auditing, and post-deployment revision.
匹配关键词: scientific discovery
---

[ACADEMIC - ARXIV]
标题: Raising the Ceiling: Better Empirical Fixation Densities for Saliency Benchmarking
作者: Susmit Agrawal, Jannis Hollman, Matthias Kümmerer
链接: https://arxiv.org/abs/2605.03885v1
完整摘要: Empirical fixation densities, spatial distributions estimated from human eye-tracking data, are foundational to saliency benchmarking. They directly shape benchmark conclusions, leaderboard rankings, failure case analyses, and scientific claims about human visual behavior. Yet the standard estimation method, fixed-bandwidth isotropic Gaussian KDE, has gone essentially unchanged for decades. This matters now more than ever: as the field shifts toward sample-level evaluation (failure case analysis, inverse benchmarking, per-image model comparison), reliable per-image density estimates become critical. We propose a principled mixture model that combines an adaptive-bandwidth KDE based on Abramson's method, center bias and uniform components, and a state-of-the-art saliency model, to capture different spatial and semantic types of interobserver consistency, and optimize all parameters per image via leave-one-subject-out cross-validation. Our method yields substantially higher interobserver consistency estimates across multiple benchmarks, with median per-image gains of 5-15% in log-likelihood and up to 2 percentage points in AUC. For the most affected images -- precisely those most relevant to failure case analysis -- improvements exceed 25%. We leverage these improved estimates to identify and analyze remaining failure cases of state-of-the-art saliency models, demonstrating that significant headroom for model improvement remains. More broadly, our findings highlight that empirical fixation densities should not be treated as fixed ground truths but as evolving estimates that improve with better methodology.
匹配关键词: scientific discovery
---

[ACADEMIC - ARXIV]
标题: Quantifying the human visual exposome with vision language models
作者: Christian Rominger, Andreas R. Schwerdtfeger, Malay Gaherwar Singh, Dimitri Khudyakow, Elizabeth A. M. Michels, Fabian Wolf, Jakob Nikolas Kather, Magdalena Katharina Wekenborg
链接: https://arxiv.org/abs/2605.03863v1
完整摘要: The visual environment is a fundamental yet unquantified determinant of mental health. While the concept of the environmental exposome is well established, current methods rely on coarse geospatial proxies or biased self reports, failing to capture the first person visual context of daily life. We addressed this gap by coupling ecological momentary assessment with vision language models (VLMs) to quantify the semantic richness of human visual experience. Across 2674 participant generated photographs, VLM derived estimates of greenness robustly predicted momentary affect and chronic stress, consistent with established benchmarks. We then developed a semi autonomous large language model (LLM) based pipeline that mined over seven million scientific publications to extract nearly 1000 environmental features empirically linked to mental health. When applied to real world imagery, up to 33 percent of VLM extracted context ratings significantly correlated with affect and stress. These findings establish a scalable objective paradigm for visual exposomics, enabling high throughput decoding of how the visible world is associated with mental health.
匹配关键词: scientific discovery
---

[ACADEMIC - ARXIV]
标题: OracleProto: A Reproducible Framework for Benchmarking LLM Native Forecasting via Knowledge Cutoff and Temporal Masking
作者: Yiding Ma, Chengyun Ruan, Kaibo Huang, Zhongliang Yang, Linna Zhou
链接: https://arxiv.org/abs/2605.03762v1
完整摘要: Large language models are moving from static text generators toward real-world decision-support systems, where forecasting is a composite capability that links information gathering, evidence integration, situational judgment, and action-oriented decision making. This capability is in broad demand across finance, policy, industry, and scientific research, yet its evaluation remains difficult: live benchmarks evaluate forecasts before answers exist, making them the cleanest way to measure forecasting ability, but they expire once events resolve; retrospective benchmarks are reproducible, but they cannot reliably distinguish genuine forecasting from facts a model may have already learned during pretraining. Prompting models to "pretend not to know" cannot replace a genuine knowledge boundary. We propose OracleProto, a reproducible framework for evaluating LLM native forecasting capability. OracleProto reconstructs resolved events into time-bounded forecasting samples by combining model-cutoff-aligned sample admission, tool-level temporal masking, content-level leakage detection, discrete answer normalization, and hierarchical scoring. Instantiated on a FutureX-Past-derived dataset with six contemporary LLMs, OracleProto distinguishes forecasting quality, sampling stability, and cost efficiency under controlled information boundaries, while reducing residual leakage to the $1\%$ level, an order of magnitude below tool-only temporal filtering. OracleProto turns LLM forecasting from one-off evaluation into an auditable, reusable, and trainable dataset-level capability, providing a unified interface for fair cross-model comparison and a controlled signal source for downstream SFT and RL. Code and data are available at https://github.com/MaYiding/OracleProto and https://huggingface.co/datasets/MaYiding/OracleProto.
匹配关键词: scientific discovery
---

[ACADEMIC - ARXIV]
标题: FluxFlow: Conservative Flow-Matching for Astronomical Image Super-Resolution
作者: Shuhong Liu, Xining Ge, Ziteng Cui, Liuzhuozheng Li, Gengjia Chang, Jun Liu, Ziying Gu, Dong Li, Xuangeng Chu, Lin Gu, Tatsuya Harada
链接: https://arxiv.org/abs/2605.03749v1
完整摘要: Ground-to-space astronomical super-resolution requires recovering space-quality images from ground-based observations that are simultaneously limited by pixel sampling resolution and atmospheric seeing, which imposes a stochastic, spatially varying PSF that cannot be resolved through upsampling alone. Existing methods rely on synthetic training pairs that fail to capture real atmospheric statistics and are prone to either over-smoothed reconstructions or hallucination sources with no physical counterpart in the observed sky. We propose FluxFlow, a conservative pixel-space flow-matching framework that incorporates observation uncertainty and source-region importance weights during training, and a training-free Wiener-regularized test-time correction to suppress hallucination sources while preserving recovered detail. We further construct the DESI--HST Dataset, the large-scale real-world benchmark comprising 19,500 real co-registered ground-to-space image pairs with real atmospheric PSF variation. Experiments demonstrate that FluxFlow consistently outperforms existing baseline methods in both photometric and scientific accuracy.
匹配关键词: scientific discovery
---

[ACADEMIC - ARXIV]
标题: Feature-Augmented Transformers for Robust AI-Text Detection Across Domains and Generators
作者: Mohamed Mady, Johannes Reschke, Björn Schuller
链接: https://arxiv.org/abs/2605.03969v1
完整摘要: AI-generated text is nowadays produced at scale across domains and heterogeneous generation pipelines, making robustness to distribution shift a central requirement for supervised binary detectors. We train transformer-based detectors on HC3 PLUS and calibrate a single decision threshold by maximising balanced accuracy on held-out validation; this threshold is then kept fixed for all downstream test distributions, revealing domain- and generator-dependent error asymmetries under shift. We evaluate in-domain on HC3 PLUS, under cross-dataset transfer to the multi-domain, multi-generator M4 benchmark, and on the external AI-Text-Detection-Pile. Although base models achieve near-ceiling in-domain performance (up to 99.5% balanced accuracy), performance under shift is brittle and strongly model-dependent. Feature augmentation via attention-based linguistic feature fusion improves transfer, with our best model (DeBERTa-v3-base+FeatAttn) achieving 85.9% balanced accuracy on M4. Multi-seed experiments confirm high stability. Under the same fixed-threshold protocol, our model outperforms strong zero-shot baselines by up to +7.22 points. Category-level ablations further show that readability and vocabulary features contribute most to robustness under shift. Overall, these results demonstrate that feature augmentation and a modern DeBERTa backbone significantly outperform earlier BERT/RoBERTa models, while the fixed-threshold protocol provides a more realistic and informative assessment of practical detector robustness.
匹配关键词: hypothesis generation
---

[ACADEMIC - ARXIV]
标题: Label-Efficient School Detection from Aerial Imagery via Weakly Supervised Pretraining and Fine-Tuning
作者: Zakarya Elmimouni, Fares Fourati, Mohamed-Slim Alouini
链接: https://arxiv.org/abs/2605.03968v1
完整摘要: Accurate school detection is essential for supporting education initiatives, including infrastructure planning and expanding internet connectivity to underserved areas. However, many regions around the world face challenges due to outdated, incomplete, or unavailable official records. Manual mapping efforts, while valuable, are labor-intensive and lack scalability across large geographic areas. To address this, we propose a weakly supervised framework for school detection from aerial imagery that minimizes the need for human annotations while supporting global mapping efforts. Our method is specifically designed for low-data regimes, where manual annotations are extremely scarce. We introduce an automatic labeling pipeline that leverages sparse location points and semantic segmentation to generate infrastructure masks from which we generate bounding boxes. Using these automatically labeled images, we train our detectors on a first training stage to learn a representation of what schools look like, then using a small set of manually labeled images, we fine-tune the previously trained models on this clean dataset. This two stage training pipeline enables large-scale and strong detection in low-data setting of school infrastructure with minimal supervision. Our results demonstrate strong object detection performance, particularly in the low-data regime, where the models achieve promising results using only 50 manually labeled images, significantly reducing the need for costly annotations. This framework supports education and connectivity initiatives worldwide by providing an efficient and extensible approach to mapping schools from space. All models, training code and auto-labeled data will be publicly released to foster future research and real-world impact.
匹配关键词: hypothesis generation
---

[ACADEMIC - ARXIV]
标题: Inconsistent Databases and Argumentation Frameworks with Collective Attacks
作者: Yasir Mahmood, Jonni Virtema, Timon Barlag, Axel-Cyrille Ngonga Ngomo
链接: https://arxiv.org/abs/2605.03954v1
完整摘要: The connection between subset-maximal repairs for inconsistent databases involving various integrity constraints and acceptable sets of arguments within argumentation frameworks has recently drawn growing interest. In this paper, we contribute to this domain by establishing a new connection when integrity constraints (ICs) include denial constraints and local-as-view tuple-generating dependencies. It turns out that SET-based Argumentation Frameworks (SETAFs), an extension of Dung's argumentation frameworks (AFs) allowing collective attacks, are needed. It is known that subset-maximal repairs under denial constraints correspond to the naive extensions, which also coincide with the preferred and stable extensions in the resulting SETAFs. Our main findings establish that repairs under the considered fragment of tuple-generating dependencies correspond to the preferred extensions. Moreover, for these dependencies, additional preprocessing allows computing a unique extension that is stable and naive. Allowing both types of constraints breaks this relationship, and even the pre-processing does not help as only preferred semantics captures these repairs. Finally, while it is known that functional dependencies do not require set-based attacks, we prove the same regarding inclusion dependencies. Thus, one can translate inconsistent databases under these restricted classes of ICs to plain AFs with attacks only between arguments.
匹配关键词: hypothesis generation
---

[ACADEMIC - ARXIV]
标题: Reservoir property image slices from the Groningen gas field for image translation and segmentation
作者: Abdulrahman Al-Fakih, Nabil Sariah, Ardiansyah Koeshidayatullah, SanLinn I. Kaka
链接: https://arxiv.org/abs/2605.03942v1
完整摘要: Reservoir characterization workflows increasingly rely on image-based and machine-learning/deep learning or even generative AI approaches, but openly available geological image datasets suitable for reproducible benchmarking remain limited. Here we describe a high-resolution dataset of reservoir-property image slices derived from the Groningen static geological model. The dataset contains aligned two-dimensional PNG images representing facies, porosity, permeability, and water saturation, generated from three-dimensional reservoir grids and prepared for downstream visualization, segmentation, and image-to-image translation tasks. In addition to the deposited original image corpus, we provide an archived software workflow for reproducing augmentation, mask generation, paired-image construction, and example baseline experiments. The resource is designed to support benchmarking of geological image analysis methods and the study of cross-domain relationships among reservoir properties. By separating the fixed image dataset from the reproducible processing workflow, this work provides a transparent foundation for reuse in geoscience, reservoir modeling, and machine-learning applications.
匹配关键词: hypothesis generation
---

[ACADEMIC - ARXIV]
标题: A Benchmark for Interactive World Models with a Unified Action Generation Framework
作者: Jianjie Fang, Yingshan Lei, Qin Wan, Ziyou Wang, Yuchao Huang, Yongyan Xu, Baining Zhao, Weichen Zhang, Chen Gao, Xinlei Chen, Yong Li
链接: https://arxiv.org/abs/2605.03941v1
完整摘要: Achieving Artificial General Intelligence (AGI) requires agents that learn and interact adaptively, with interactive world models providing scalable environments for perception, reasoning, and action. Yet current research still lacks large-scale datasets and unified benchmarks to evaluate their physical interaction capabilities. To address this, we propose iWorld-Bench, a comprehensive benchmark for training and testing world models on interaction-related abilities such as distance perception and memory. We construct a diverse dataset with 330k video clips and select 2.1k high-quality samples covering varied perspectives, weather, and scenes. As existing world models differ in interaction modalities, we introduce an Action Generation Framework to unify evaluation and design six task types, generating 4.9k test samples. These tasks jointly assess model performance across visual generation, trajectory following, and memory. Evaluating 14 representative world models, we identify key limitations and provide insights for future research. The iWorld-Bench model leaderboard is publicly available at iWorld-Bench.com.
匹配关键词: hypothesis generation
---

[ACADEMIC - ARXIV]
标题: Logical Consistency as a Bridge: Improving LLM Hallucination Detection via Label Constraint Modeling between Responses and Self-Judgments
作者: Hao Mi, Qiang Sheng, Shaofei Wang, Beizhe Hu, Yifan Sun, Zhengjia Wang, Hengqi Zeng, Yang Li, Danding Wang, Juan Cao
链接: https://arxiv.org/abs/2605.03971v1
完整摘要: Large Language Models (LLMs) are prone to factual hallucinations, risking their reliability in real-world applications. Existing hallucination detectors mainly extract micro-level intrinsic patterns for uncertainty quantification or elicit macro-level self-judgments through verbalized prompts. However, these methods address only a single facet of the hallucination, focusing either on implicit neural uncertainty or explicit symbolic reasoning, thereby treating these inherently coupled behaviors in isolation and failing to exploit their interdependence for a holistic view. In this paper, we propose LaaB (Logical Consistency-as-a-Bridge), a framework that bridges neural features and symbolic judgments for hallucination detection. LaaB introduces a "meta-judgment" process to map symbolic labels back into the feature space. By leveraging the inherent logical bridge where response and meta-judgment labels are either the same or opposite based on the self-judgment's semantics, LaaB aligns and integrates dual-view signals via mutual learning and enhances the hallucination detection. Extensive experiments on 4 public datasets, across 4 LLMs, against 8 baselines demonstrate the superiority of LaaB.
匹配关键词: autonomous experiment
---

[ACADEMIC - ARXIV]
标题: Feature-Augmented Transformers for Robust AI-Text Detection Across Domains and Generators
作者: Mohamed Mady, Johannes Reschke, Björn Schuller
链接: https://arxiv.org/abs/2605.03969v1
完整摘要: AI-generated text is nowadays produced at scale across domains and heterogeneous generation pipelines, making robustness to distribution shift a central requirement for supervised binary detectors. We train transformer-based detectors on HC3 PLUS and calibrate a single decision threshold by maximising balanced accuracy on held-out validation; this threshold is then kept fixed for all downstream test distributions, revealing domain- and generator-dependent error asymmetries under shift. We evaluate in-domain on HC3 PLUS, under cross-dataset transfer to the multi-domain, multi-generator M4 benchmark, and on the external AI-Text-Detection-Pile. Although base models achieve near-ceiling in-domain performance (up to 99.5% balanced accuracy), performance under shift is brittle and strongly model-dependent. Feature augmentation via attention-based linguistic feature fusion improves transfer, with our best model (DeBERTa-v3-base+FeatAttn) achieving 85.9% balanced accuracy on M4. Multi-seed experiments confirm high stability. Under the same fixed-threshold protocol, our model outperforms strong zero-shot baselines by up to +7.22 points. Category-level ablations further show that readability and vocabulary features contribute most to robustness under shift. Overall, these results demonstrate that feature augmentation and a modern DeBERTa backbone significantly outperform earlier BERT/RoBERTa models, while the fixed-threshold protocol provides a more realistic and informative assessment of practical detector robustness.
匹配关键词: autonomous experiment
---

[ACADEMIC - ARXIV]
标题: MOSAIC-Bench: Measuring Compositional Vulnerability Induction in Coding Agents
作者: Jonathan Steinberg, Oren Gal
链接: https://arxiv.org/abs/2605.03952v1
完整摘要: Coding agents often pass per-prompt safety review yet ship exploitable code when their tasks are decomposed into routine engineering tickets. The challenge is structural: existing safety alignment evaluates overt requests in isolation, leaving models blind to malicious end-states that emerge from sequenced compliance with innocuous-looking requests. We introduce MOSAIC-Bench (Malicious Objectives Sequenced As Innocuous Compliance), a benchmark of 199 three-stage attack chains paired with deterministic exploit oracles on deployed software substrates (10 web-application substrates, 31 CWE classes, 5 programming languages) that treats both exploit ground truth and downstream reviewer protocol as first-class evaluation axes. On this benchmark, nine production coding agents from Anthropic, OpenAI, Google, Moonshot, Zhipu, and Minimax compose innocuous tickets at 53-86% end-to-end ASR with only two refusals across all staged runs. In a matched direct-prompt experiment over four frontier Claude/Codex agents, vulnerable-output rates fall to 0-20.4%: Claude primarily refuses, while Codex primarily hardens rather than emitting the vulnerable implementation - ticket staging silences both defense modes simultaneously. Downstream, code reviewer agents approve 25.8% of these confirmed-vulnerable cumulative diffs as routine PRs, and a full-context implementation protocol closes only 50% of the staged/direct gap, ruling out context fragmentation as the sole explanation. As a deployable but non-adaptive mitigation, reframing the reviewer as an adversarial pentester reduces evasion across the evaluated reviewer subset; pentester framed evasion ranges from 3.0% to 17.6%, and an open-weight Gemma-4-E4B-it reviewer under this framing detects 88.4% of attacks on the dataset with a 4.6% false-positive rate measured on 608 real-world GitHub PRs.
匹配关键词: autonomous experiment
---

[ACADEMIC - ARXIV]
标题: UnAC: Adaptive Visual Prompting with Abstraction and Stepwise Checking for Complex Multimodal Reasoning
作者: Yifan Wang, Yun Fu
链接: https://arxiv.org/abs/2605.03950v1
完整摘要: Although recent LMMs have become much stronger at visual perception, they remain unreliable on problems that require multi-step reasoning over visual evidence. In this paper, we present UnAC (Understanding, Abstracting, and Checking), a multimodal prompting method that strengthens reasoning for complex multimodal tasks in LMMs (e.g., GPT-4o, Gemini 1.5, and GPT-4V). To improve image understanding and capture fine details, we propose an adaptive visual prompting strategy that enables LMMs to focus on salient regions. We further design an image-abstraction prompt to effectively extract key information from images. In addition, we introduce a gradual self-checking scheme that improves reasoning by verifying each decomposed subquestion and its answer. Extensive experiments on three public benchmarks-MathVista, MM-Vet, and MMMU.
匹配关键词: autonomous experiment
---

[ACADEMIC - ARXIV]
标题: Integrating Feature Correlation in Differential Privacy with Applications in DP-ERM
作者: Tianyu Wang, Luhao Zhang, Rachel Cummings
链接: https://arxiv.org/abs/2605.03945v1
完整摘要: Standard differential privacy imposes uniform privacy constraints across all features, overlooking the inherent distinction between sensitive and insensitive features in practice. In this paper, we introduce a relaxed definition of differential privacy that accounts for such heterogeneity, allowing certain features to be treated as insensitive even when correlated with sensitive ones. We propose a correlation-aware framework, $\textsf{CorrDP}$, which relaxes privacy for insensitive features while accounting for their correlations with sensitive features, with the correlations quantified using total variation distance. We design algorithms for differentially private empirical risk minimization (DP-ERM) under the $\textsf{CorrDP}$ framework, incorporating distance-dependent noise into gradients for improved theoretical utility guarantees. When the correlation distance is unknown, we estimate it from the dataset and show that it achieves a comparable privacy-utility guarantee. We perform experiments on synthetic and real-world datasets and show that $\textsf{CorrDP}$-based DP-ERM algorithms consistently outperform the standard DP framework in the presence of insensitive features.
匹配关键词: autonomous experiment
---

[ACADEMIC - ARXIV]
标题: Evaluating Generative Models as Interactive Emergent Representations of Human-Like Collaborative Behavior
作者: Shinas Shaji, Teena Chakkalayil Hassan, Sebastian Houben, Alex Mitrevski
链接: https://arxiv.org/abs/2605.03855v1
完整摘要: Human-AI collaboration requires AI agents to understand human behavior for effective coordination. While advances in foundation models show promising capabilities in understanding and showing human-like behavior, their application in embodied collaborative settings needs further investigation. This work examines whether embodied foundation model agents exhibit emergent collaborative behaviors indicating underlying mental models of their collaborators, which is an important aspect of effective coordination. This paper develops a 2D collaborative game environment where large language model agents and humans complete color-matching tasks requiring coordination. We define five collaborative behaviors as indicators of emergent mental model representation: perspective-taking, collaborator-aware planning, introspection, theory of mind, and clarification. An automated behavior detection system using LLM-based judges identifies these behaviors, achieving fair to substantial agreement with human annotations. Results from the automated behavior detection system show that foundation models consistently exhibit emergent collaborative behaviors without being explicitly trained to do so. These behaviors occur at varying frequencies during collaboration stages, with distinct patterns across different LLMs. A user study was also conducted to evaluate human satisfaction and perceived collaboration effectiveness, with the results indicating positive collaboration experiences. Participants appreciated the agents' task focus, plan verbalization, and initiative, while suggesting improvements in response times and human-like interactions. This work provides an experimental framework for human-AI collaboration, empirical evidence of collaborative behaviors in embodied LLM agents, a validated behavioral analysis methodology, and an assessment of collaboration effectiveness.
匹配关键词: lab automation
---

[ACADEMIC - ARXIV]
标题: SOAR: Real-Time Joint Optimization of Order Allocation and Robot Scheduling in Robotic Mobile Fulfillment Systems
作者: Yibang Tang, Yifan Yang, Jingyuan Wang, Junhua Chen, Zhen Zhao
链接: https://arxiv.org/abs/2605.03842v1
完整摘要: Robotic Mobile Fulfillment Systems (RMFS) rely on mobile robots for automated inventory transportation, coordinating order allocation and robot scheduling to enhance warehousing efficiency. However, optimizing RMFS is challenging due to strict real-time constraints and the strong coupling of multi-phase decisions. Existing methods either decompose the problem into isolated sub-tasks to guarantee responsiveness at the cost of global optimality, or rely on computationally expensive global optimization models that are unsuitable for dynamic industrial environments. To bridge this gap, we propose SOAR, a unified Deep Reinforcement Learning framework for real-time joint optimization. SOAR transforms order allocation and robot scheduling into a unified process by utilizing soft order allocations as observations. We formulate this as an Event-Driven Markov Decision Process, enabling the agent to perform simultaneous scheduling in response to asynchronous system events. Technically, we employ a Heterogeneous Graph Transformer to encode the warehouse state and integrate phased domain knowledge. Additionally, we incorporate a reward shaping strategy to address sparse feedback in long-horizon tasks. Extensive experiments on synthetic and real-world industrial datasets, in collaboration with Geekplus, demonstrate that SOAR reduces global makespan by 7.5\% and average order completion time by 15.4\% with sub-100ms latency. Furthermore, sim-to-real deployment confirms its practical viability and significant performance gains in production environments. The code is available at https://github.com/200815147/SOAR.
匹配关键词: lab automation
---

[ACADEMIC - ARXIV]
标题: TriBench-Ko: Evaluating LLM Risks in Judicial Workflows
作者: Haesung Lee, Gyubin Choi, Eun-Ju Lee, So-Min Lee, Youkang Ko, Dogyoon Lim, Sung-Kyoung Jang, Yohan Jo
链接: https://arxiv.org/abs/2605.03792v1
完整摘要: Large language models (LLMs) are increasingly integrated into legal workflows. However, existing benchmarks primarily address proxy tasks, such as bar examination performance or classification, which fail to capture the performance and risks inherent in day-to-day judicial processes. To address this, we publicly release TriBench-Ko, a Korean benchmark designed to evaluate potential deployment risks of LLMs within the context of verified judicial task requirements. It covers four core tasks: jurisprudence summarization, precedent retrieval, legal issue extraction, and evidence analysis. It jointly assesses model behavior across multiple deployment risk categories, including inaccuracy (hallucination, omission, statutory misapplication), biases (demographic, overcompliance), inconsistencies (prompt sensitivity, non-determinism), and adjudicative overreach. Each item is structured to systematically assess both task performance and a specific risk type based on real judicial decisions. Our evaluation of a range of contemporary LLMs reveals that many models frequently manifest significant risks, most notably struggling with precedent retrieval and failing to capture critical legal information. We provide a comprehensive diagnosis of these LLMs and pinpoint critical areas where LLM-generated outputs in judicial contexts necessitate rigorous inspection and caution. Our dataset and code are available at https://github.com/holi-lab/TriBench-Ko
匹配关键词: lab automation
---

[ACADEMIC - ARXIV]
标题: ReLeaf: Benchmarking Leaf Segmentation across Domains and Species
作者: Robert Martinko, Daniel Steininger, Julia Simon, Andreas Trondl, Matthias Blaickner
链接: https://arxiv.org/abs/2605.03784v1
完整摘要: Rising global food demand and growing climate pressure increase the need for sustainable, precise agricultural practices. Automated, individualized plant treatment relies on fine-grained visual analysis, yet leaf-level segmentation remains underexplored despite its value for assessing crop health, growth dynamics, yield potential and localized stress symptoms. Progress is limited by a lack of dedicated datasets, especially regarding species coverage, and by the absence of systematic evaluations of modern instance-segmentation architectures for this task. We address these gaps by surveying current data and identifying four suitable, publicly available leaf-segmentation datasets. Using them, we compare one-stage, two-stage and Transformer-based detectors and identify a YOLO26 model configuration to provide the best trade-off for real-world precision-agriculture tasks. Extensive cross-domain generalization experiments reveal substantial performance drops across plant species and recording setups, especially for models trained solely on laboratory data. To strengthen data availability, we introduce a new benchmark dataset with leaf-level masks for 23 plant species, created via semi-automatic annotation of selected CropAndWeed images. A model trained on all four existing datasets achieves a mean mAP50-95 of 83.9% across their corresponding test sets and 40.2% on our new benchmark, demonstrating improved generalization and highlighting the need for diverse leaf-segmentation datasets in robust precision agriculture.
匹配关键词: lab automation
---

[ACADEMIC - ARXIV]
标题: From Code to Prediction: Fine-Tuning LLMs for Neural Network Performance Classification in NNGPT
作者: Mahmoud Hanouneh, Radu Timofte, Dmitry Ignatov
链接: https://arxiv.org/abs/2605.03686v1
完整摘要: Automated Machine Learning (AutoML) frameworks increasingly leverage Large Language Models (LLMs) for tasks such as hyperparameter optimization and neural architecture code generation. However, current LLM-based approaches focus on generative outputs and evaluate them by training the produced artifacts. Whether LLMs can learn to reason about neural network performance across datasets remains underexplored. We present a classification task integrated into the NNGPT framework, in which a fine-tuned LLM predicts which of two image classification datasets a given neural network architecture achieves higher accuracy on. The task is built on the LEMUR dataset, which provides standardized PyTorch implementations with reproducible performance metrics. Three prompt configurations of increasing difficulty are evaluated: a normalized-accuracy baseline (trivially reaching 100%), a metadata-enriched prompt replacing accuracies with dataset properties, and a code-only prompt presenting only architecture source code and dataset names. Using DeepSeek-Coder-7B-Instruct fine-tuned with LoRA, the code-only prompt reaches 80% peak accuracy over 15 epochs, while the metadata prompt peaks at 70%. Perdataset analysis reveals complementary strengths: metadata excels for datasets with distinctive properties (CelebAGender at 90.9%) but degrades for overlapping characteristics, whereas the code-only prompt shows more balanced performance. A comparison with DeepSeek-Coder1.3B confirms that model capacity affects this form of architectural reasoning. The results establish that LLMs can be fine-tuned to predict cross-dataset suitability from neural network code, suggesting that architecture source code contains richer discriminative signal than dataset metadata alone.
匹配关键词: lab automation
---

[ACADEMIC - ARXIV]
标题: Logical Consistency as a Bridge: Improving LLM Hallucination Detection via Label Constraint Modeling between Responses and Self-Judgments
作者: Hao Mi, Qiang Sheng, Shaofei Wang, Beizhe Hu, Yifan Sun, Zhengjia Wang, Hengqi Zeng, Yang Li, Danding Wang, Juan Cao
链接: https://arxiv.org/abs/2605.03971v1
完整摘要: Large Language Models (LLMs) are prone to factual hallucinations, risking their reliability in real-world applications. Existing hallucination detectors mainly extract micro-level intrinsic patterns for uncertainty quantification or elicit macro-level self-judgments through verbalized prompts. However, these methods address only a single facet of the hallucination, focusing either on implicit neural uncertainty or explicit symbolic reasoning, thereby treating these inherently coupled behaviors in isolation and failing to exploit their interdependence for a holistic view. In this paper, we propose LaaB (Logical Consistency-as-a-Bridge), a framework that bridges neural features and symbolic judgments for hallucination detection. LaaB introduces a "meta-judgment" process to map symbolic labels back into the feature space. By leveraging the inherent logical bridge where response and meta-judgment labels are either the same or opposite based on the self-judgment's semantics, LaaB aligns and integrates dual-view signals via mutual learning and enhances the hallucination detection. Extensive experiments on 4 public datasets, across 4 LLMs, against 8 baselines demonstrate the superiority of LaaB.
匹配关键词: AI for science
---

[ACADEMIC - ARXIV]
标题: Feature-Augmented Transformers for Robust AI-Text Detection Across Domains and Generators
作者: Mohamed Mady, Johannes Reschke, Björn Schuller
链接: https://arxiv.org/abs/2605.03969v1
完整摘要: AI-generated text is nowadays produced at scale across domains and heterogeneous generation pipelines, making robustness to distribution shift a central requirement for supervised binary detectors. We train transformer-based detectors on HC3 PLUS and calibrate a single decision threshold by maximising balanced accuracy on held-out validation; this threshold is then kept fixed for all downstream test distributions, revealing domain- and generator-dependent error asymmetries under shift. We evaluate in-domain on HC3 PLUS, under cross-dataset transfer to the multi-domain, multi-generator M4 benchmark, and on the external AI-Text-Detection-Pile. Although base models achieve near-ceiling in-domain performance (up to 99.5% balanced accuracy), performance under shift is brittle and strongly model-dependent. Feature augmentation via attention-based linguistic feature fusion improves transfer, with our best model (DeBERTa-v3-base+FeatAttn) achieving 85.9% balanced accuracy on M4. Multi-seed experiments confirm high stability. Under the same fixed-threshold protocol, our model outperforms strong zero-shot baselines by up to +7.22 points. Category-level ablations further show that readability and vocabulary features contribute most to robustness under shift. Overall, these results demonstrate that feature augmentation and a modern DeBERTa backbone significantly outperform earlier BERT/RoBERTa models, while the fixed-threshold protocol provides a more realistic and informative assessment of practical detector robustness.
匹配关键词: AI for science
---

[ACADEMIC - ARXIV]
标题: Label-Efficient School Detection from Aerial Imagery via Weakly Supervised Pretraining and Fine-Tuning
作者: Zakarya Elmimouni, Fares Fourati, Mohamed-Slim Alouini
链接: https://arxiv.org/abs/2605.03968v1
完整摘要: Accurate school detection is essential for supporting education initiatives, including infrastructure planning and expanding internet connectivity to underserved areas. However, many regions around the world face challenges due to outdated, incomplete, or unavailable official records. Manual mapping efforts, while valuable, are labor-intensive and lack scalability across large geographic areas. To address this, we propose a weakly supervised framework for school detection from aerial imagery that minimizes the need for human annotations while supporting global mapping efforts. Our method is specifically designed for low-data regimes, where manual annotations are extremely scarce. We introduce an automatic labeling pipeline that leverages sparse location points and semantic segmentation to generate infrastructure masks from which we generate bounding boxes. Using these automatically labeled images, we train our detectors on a first training stage to learn a representation of what schools look like, then using a small set of manually labeled images, we fine-tune the previously trained models on this clean dataset. This two stage training pipeline enables large-scale and strong detection in low-data setting of school infrastructure with minimal supervision. Our results demonstrate strong object detection performance, particularly in the low-data regime, where the models achieve promising results using only 50 manually labeled images, significantly reducing the need for costly annotations. This framework supports education and connectivity initiatives worldwide by providing an efficient and extensible approach to mapping schools from space. All models, training code and auto-labeled data will be publicly released to foster future research and real-world impact.
匹配关键词: AI for science
---

[ACADEMIC - ARXIV]
标题: Pretrained Model Representations as Acquisition Signals for Active Learning of MLIPs
作者: Eszter Varga-Umbrich, Shikha Surana, Paul Duckworth, Jules Tilly, Olivier Peltre, Zachary Weller-Davies
链接: https://arxiv.org/abs/2605.03964v1
完整摘要: Training machine learning interatomic potentials (MLIPs) for reactive chemistry is often bottlenecked by the high cost of quantum chemical labels and the scarcity of transition state configurations in candidate pools. Active learning (AL) can mitigate these costs, but its effectiveness hinges on the acquisition rule. We investigate whether the latent space of a pretrained MLIP already contains the information necessary for effective acquisition, eliminating the need for auxiliary uncertainty heads, Bayesian training and fine-tuning, or committee ensembles. We introduce two acquisition signals derived directly from a pretrained MACE potential: a finite-width neural tangent kernel (NTK) and an activation kernel built from hidden latent space features. On reactive-chemistry benchmarks, both kernels consistently outperform fixed-descriptor baselines, committee disagreement, and random acquisition, reducing the data required to reach performance targets by an average of 38% for energy error and 28% for force error. We further show that the pretrained model induces similarity spaces that preserve chemically meaningful structure and provide more reliable residual uncertainty estimates than randomly initialised or fixed-descriptor-based kernels. Our results suggest that pretraining aligns latent-space geometry with model error, yielding a practical and sufficient acquisition signal for reactive MLIP fine-tuning.
匹配关键词: AI for science
---

[ACADEMIC - ARXIV]
标题: Inconsistent Databases and Argumentation Frameworks with Collective Attacks
作者: Yasir Mahmood, Jonni Virtema, Timon Barlag, Axel-Cyrille Ngonga Ngomo
链接: https://arxiv.org/abs/2605.03954v1
完整摘要: The connection between subset-maximal repairs for inconsistent databases involving various integrity constraints and acceptable sets of arguments within argumentation frameworks has recently drawn growing interest. In this paper, we contribute to this domain by establishing a new connection when integrity constraints (ICs) include denial constraints and local-as-view tuple-generating dependencies. It turns out that SET-based Argumentation Frameworks (SETAFs), an extension of Dung's argumentation frameworks (AFs) allowing collective attacks, are needed. It is known that subset-maximal repairs under denial constraints correspond to the naive extensions, which also coincide with the preferred and stable extensions in the resulting SETAFs. Our main findings establish that repairs under the considered fragment of tuple-generating dependencies correspond to the preferred extensions. Moreover, for these dependencies, additional preprocessing allows computing a unique extension that is stable and naive. Allowing both types of constraints breaks this relationship, and even the pre-processing does not help as only preferred semantics captures these repairs. Finally, while it is known that functional dependencies do not require set-based attacks, we prove the same regarding inclusion dependencies. Thus, one can translate inconsistent databases under these restricted classes of ICs to plain AFs with attacks only between arguments.
匹配关键词: AI for science
---

[ACADEMIC - ARXIV]
标题: From Code to Prediction: Fine-Tuning LLMs for Neural Network Performance Classification in NNGPT
作者: Mahmoud Hanouneh, Radu Timofte, Dmitry Ignatov
链接: https://arxiv.org/abs/2605.03686v1
完整摘要: Automated Machine Learning (AutoML) frameworks increasingly leverage Large Language Models (LLMs) for tasks such as hyperparameter optimization and neural architecture code generation. However, current LLM-based approaches focus on generative outputs and evaluate them by training the produced artifacts. Whether LLMs can learn to reason about neural network performance across datasets remains underexplored. We present a classification task integrated into the NNGPT framework, in which a fine-tuned LLM predicts which of two image classification datasets a given neural network architecture achieves higher accuracy on. The task is built on the LEMUR dataset, which provides standardized PyTorch implementations with reproducible performance metrics. Three prompt configurations of increasing difficulty are evaluated: a normalized-accuracy baseline (trivially reaching 100%), a metadata-enriched prompt replacing accuracies with dataset properties, and a code-only prompt presenting only architecture source code and dataset names. Using DeepSeek-Coder-7B-Instruct fine-tuned with LoRA, the code-only prompt reaches 80% peak accuracy over 15 epochs, while the metadata prompt peaks at 70%. Perdataset analysis reveals complementary strengths: metadata excels for datasets with distinctive properties (CelebAGender at 90.9%) but degrades for overlapping characteristics, whereas the code-only prompt shows more balanced performance. A comparison with DeepSeek-Coder1.3B confirms that model capacity affects this form of architectural reasoning. The results establish that LLMs can be fine-tuned to predict cross-dataset suitability from neural network code, suggesting that architecture source code contains richer discriminative signal than dataset metadata alone.
匹配关键词: PyTorch
---

[ACADEMIC - ARXIV]
标题: StreamIndex: Memory-Bounded Compressed Sparse Attention via Streaming Top-k
作者: Jaber Jaber, Osama Jaber
链接: https://arxiv.org/abs/2605.02568v1
完整摘要: DeepSeek-V3.2 and V4 introduce Compressed Sparse Attention (CSA): a lightning indexer (a learned scoring projection over compressed keys) scores them, the top-k are selected per query, and a sparse attention kernel reads only those. Public CSA implementations materialize a [B, S, H_I, T] FP32 score tensor before the top-k reduction. With H_I=64 indexer heads and the V4-Flash compression ratio m=4, that intermediate is 256 GB at sequence length S=65,536, exceeding any single-GPU high-bandwidth-memory (HBM) budget. We present StreamIndex, a Triton implementation of the CSA pipeline whose central component is a chunked partition-merge top-k driver that never materializes the full intermediate. On synthetic-but-realistic V4-shaped inputs at the indexer-step (layer) level on a single NVIDIA H200, the materialize path runs out of memory (OOMs) at S=65,536 with V4-Flash dimensions; StreamIndex runs the same indexer to S=1,048,576 with 6.21 GB peak HBM, a 32x regime extension. Set-overlap recall against the materialize ground truth is bit-exact at small S where both fit; across three 5-point design-space sweeps (chunk size, key-tile size, top-k), mean recall rounds to 1.0000 with min recall at least 0.9980 in every cell. The chunked driver composes with TileLang's pipelined attention kernel: at S=262,144 with V4-Flash dimensions, the materialize indexer paired with TileLang attention OOMs while the chunked indexer paired with the same attention runs in 1.97 s at 18.56 GB peak. Our contribution targets the indexer step; we make no claim of a faster attention kernel or of real-checkpoint end-to-end behavior. Code: https://github.com/RightNow-AI/StreamIndex.
匹配关键词: Triton
---

[ACADEMIC - ARXIV]
标题: Better Models, Faster Training: Sigmoid Attention for single-cell Foundation Models
作者: Vijay Sadashivaiah, Georgios Dasoulas, Judith Mueller, Soumya Ghosh
链接: https://arxiv.org/abs/2604.27124v1
完整摘要: Training stable biological foundation models requires rethinking attention mechanisms: we find that using sigmoid attention as a drop in replacement for softmax attention a) produces better learned representations: on six diverse single-cell datasets, sigmoid achieves 25% higher cell-type separation, better cell-type cohesion metrics, and lower validation loss, b) faster training, models with sigmoid attention train up to 10% faster than their softmax counterparts, and c) more stable training by eliminating inherent sources of instability in softmax attention. We establish that sigmoid attention has globally bounded derivatives ($\leq 0.25$) as opposed to softmax, and a diagonal Jacobian structure in contrast with softmax's dense coupling, which together help alleviate training instabilities. In stress tests on 160M-parameter bidirectional attention models trained without gradient clipping on 8K-token sequences, softmax diverges catastrophically, with gradients exploding by four orders of magnitude, while sigmoid remains stable. Finally, we implement and open-source TritonSigmoid, an efficient GPU kernel that achieves 515 TFLOPS on H100 GPUs, outperforming both FlashAttention-2 and FlashSigmoid, with native padding support, which is essential for biological sequences. Our results establish sigmoid attention as both theoretically grounded and empirically superior for biological foundation models. Code is available at https://github.com/MSDLLCpapers/triton-sigmoid
匹配关键词: Triton
---

[ACADEMIC - ARXIV]
标题: RaMP: Runtime-Aware Megakernel Polymorphism for Mixture-of-Experts
作者: Vyom Sharma, Debajyoti Datta
链接: https://arxiv.org/abs/2604.26039v1
完整摘要: The optimal kernel configuration for Mixture-of-Experts (MoE) inference depends on both batch size and the expert routing distribution, yet production systems dispatch from batch size alone, leaving 10-70% of kernel throughput unrealized. We present RaMP, a routing-aware dispatch framework. A performance-region analysis derives, from hardware constants alone, when each optimization helps, correctly predicting all 8 tested architectures, including 3 unseen. A four-parameter wave cost model selects the fastest configuration from the runtime expert histogram, achieving 0.93% mean regret versus exhaustive search, fitted from just 10-24 minutes of one-time profiling per model. Because the model depends only on CTA grid geometry, it is kernel-agnostic: applied to Alpha-MoE, it delivers 1.14x with no source modification. Paired with a co-designed CuTe DSL kernel exposing 134-268 polymorphic configurations, RaMP delivers 1.22x kernel speedup over static dispatch and 1.30x end-to-end speedup in vLLM serving over Triton, 1.41x over DeepGEMM, and 1.13x over FlashInfer CUTLASS.
匹配关键词: Triton
---

[ACADEMIC - ARXIV]
标题: QFlash: Bridging Quantization and Memory Efficiency in Vision Transformer Attention
作者: Sehyeon Oh, Yongin Kwon, Jemin Lee
链接: https://arxiv.org/abs/2604.25306v1
完整摘要: FlashAttention improves efficiency through tiling, but its online softmax still relies on floating-point arithmetic for numerical stability, making full quantization difficult. We identify three main obstacles to integer-only FlashAttention: (1) scale explosion during tile-wise accumulation, (2) inefficient shift-based exponential operations on GPUs, and (3) quantization granularity constraints requiring uniform scales for integer comparison. To address these challenges, we propose \textit{QFlash}, an end-to-end integer FlashAttention design that performs softmax entirely in the integer domain and runs as a single Triton kernel. On seven attention workloads from ViT, DeiT, and Swin models, QFlash achieves up to 6.73$\times$ speedup over I-ViT and up to 8.69$\times$ speedup on Swin, while reducing energy consumption by 18.8\% compared to FP16 FlashAttention, without sacrificing Top-1 accuracy on ViT/DeiT and remaining competitive on Swin under per-tensor quantization. Our code is publicly available at https://github.com/EfficientCompLab/qflash.
匹配关键词: Triton
---

[ACADEMIC - ARXIV]
标题: ELSA: Exact Linear-Scan Attention for Fast and Memory-Light Vision Transformers
作者: Chih-Chung Hsu, Xin-Di Ma, Wo-Ting Liao, Chia-Ming Lee
链接: https://arxiv.org/abs/2604.23798v1
完整摘要: Existing attention accelerators often trade exact softmax semantics, depend on fused Tensor Core kernels, or incur sequential depth that limits FP32 throughput on long sequences. We present \textbf{ELSA}, an algorithmic reformulation of online softmax attention that (i)~preserves exact softmax semantics in real arithmetic with a \emph{provable} $\mathcal{O}(u\log n)$ FP32 relative error bound; (ii)~casts the online softmax update as a prefix scan over an associative monoid $(m,S,W)$, yielding $O(n)$ extra memory and $O(\log n)$ parallel depth; and (iii)~is Tensor-Core independent, implemented in Triton and CUDA C++, and deployable as a \emph{drop-in replacement} requiring no retraining or weight modification. Unlike FlashAttention-2/3, which rely on HMMA/GMMA Tensor Core instructions and provide no compatible FP32 path, ELSA operates identically on A100s and resource-constrained edge devices such as Jetson TX2 -- making it the only hardware-agnostic exact-attention kernel that reduces parallel depth to $O(\log n)$ at full precision. On A100 FP32 benchmarks (1K--16K tokens), ELSA delivers $1.3$--$3.5\times$ speedup over memory-efficient SDPA and $1.97$--$2.27\times$ on BERT; on Jetson TX2, ELSA achieves $1.5$--$1.6\times$ over Math (64--900 tokens), with $17.8$--$20.2\%$ throughput gains under LLaMA-13B offloading at $\ge$32K. In FP16, ELSA approaches hardware-fused baselines at long sequences while retaining full FP32 capability, offering a unified kernel for high-precision inference across platforms. Our code and implementation are available at https://github.com/ming053l/ELSA.
匹配关键词: Triton
---

[ACADEMIC - ARXIV]
标题: Differentiable Multiphysics Co-Optimization via Implicit Neural Representations: A Transient Hamburger-Cooking Benchmark
作者: Navid Zobeiry
链接: https://arxiv.org/abs/2605.01040v1
完整摘要: The co-optimization of geometry and physical parameters remains challenging in transient multiphysics systems involving moving boundaries, nonlinear material response, phase transitions, and competing objectives. Existing methods often optimize geometry and physical variables separately, rely on simplified steady-state physics, or require offline data generation and reduced design spaces. Here, we present an end-to-end differentiable co-optimization framework that couples an implicit neural representation of geometry with a JAX-compiled Eulerian multiphysics solver. Geometry is represented as a signed distance field using Fourier-feature-encoded spatial coordinates, while boundary conditions, initial conditions, process controls, and material parameters are optimized within the same differentiable loop. Continuous relaxations represent non-smooth physical transitions while preserving compatibility with reverse-mode automatic differentiation and backpropagation through time. We demonstrate the framework using a transient hamburger-cooking benchmark, selected as an interpretable multiphysics problem rather than a culinary optimization exercise. The benchmark combines conductive and convective heat transfer, latent energy effects, moisture and fat transport, shrinkage-induced geometry evolution, evolving contact boundary conditions, flipping-induced boundary-condition changes, and competing quality objectives. Results show that geometry-only optimization modifies shape to relieve thermal bottlenecks, while joint co-optimization distributes the design response across geometry, material state, process variables, and boundary conditions through gradients propagated over the full transient rollout.
匹配关键词: JAX
---

[ACADEMIC - ARXIV]
标题: NLPOpt-Net: A Learning Method for Nonlinear Optimization with Feasibility Guarantees
作者: Bimol Nath Roy, Rahul Golder, MM Faruque Hasan
链接: https://arxiv.org/abs/2605.00260v1
完整摘要: Nonlinear Parametric Optimization Network (NLPOpt-Net) is an unsupervised learning architecture to solve constrained nonlinear programs (NLP). Given the structure of an NLP, it learns the parametric solution maps with guaranteed constraint satisfaction. The architecture consists of a backbone neural network (NN) followed by a multilayer ($k$-layered) projection. While the NN drives toward optimality through a loss function consisting of a modified Lagrangian augmented with a consistency loss, the projection ensures feasibility by projecting the NN predictions in the original constraint manifold. Instead of typical distance minimization, our projection exploits local quadratic approximations of the original NLP. Under certain conditions (such as convexity), the projection has a descent property, which improves the NN predictions further. NLPOpt-Net deploys an inversion-free, modified Chambolle-Pock algorithm to solve the constrained quadratic projections during the forward pass and uses the implicit function theorem for efficient backpropagation. The fixed structure of the projection further allows decoupling of the NN and the projection once the training is complete. NLPOpt-Net solves large-scale convex QP, QCQP, NLP, and nonconvex problems with near zero optimality gap and constraint violations reduced to machine precision. Additionally, it provides near accurate prediction of the active sets and corresponding dual variables, thereby enabling a scalable approach for multiparametric programming. Compiling the projection in C provides order of magnitude improvement in inference time compared to JAX. We provide the codes and NLPOpt-Net as a ready to use package that includes GPU support.
匹配关键词: JAX
---

[ACADEMIC - ARXIV]
标题: Universal Transformers Need Memory: Depth-State Trade-offs in Adaptive Recursive Reasoning
作者: Grigory Sapunov
链接: https://arxiv.org/abs/2604.21999v3
完整摘要: We study learned memory tokens as a computational scratchpad for a single-block Universal Transformer with Adaptive Computation Time (ACT) on Sudoku-Extreme, a combinatorial reasoning benchmark. Memory tokens are empirically necessary: no configuration without them reaches non-trivial performance. The optimal count has a sharp lower threshold (T=0 always fails, T=8 reliably succeeds) followed by a stable plateau (T=8-32, 57.4% +/- 0.7% exact-match) and a dilution boundary at T=64. Under halt-side pressure (lambda warmup), mean halt drops monotonically with memory size across the plateau (from 11.6 at T=8 to 8.3 at T=64), showing that memory tokens and ponder depth substitute as resources at fixed accuracy. We also identify a router initialization trap that causes the majority of training runs to fail: both default zero-bias and Graves' recommended positive bias settle into a shallow halt equilibrium the model cannot escape. Inverting the bias to -3 ("deep start") eliminates the failure mode, and ablation shows the trap is inherent to ACT initialization rather than an artifact of our architecture. With reliable training, ACT yields an order of magnitude lower seed variance than fixed-depth processing (+/-0.7 vs +/-9.3 pp); lambda warmup recovers 34% of compute at matched accuracy; and attention heads specialize into memory readers, constraint propagators, and integrators across recursive depth. Code: https://github.com/che-shr-cat/utm-jax.
匹配关键词: JAX
---

[ACADEMIC - ARXIV]
标题: Autonomous Skeletal Landmark Localization towards Agentic C-Arm Control
作者: Jay Jung, Ahmad Arrabi, Jax Luo, Scott Raymond, Safwan Wshah
链接: https://arxiv.org/abs/2604.18740v1
完整摘要: Purpose: Automated C-arm positioning ensures timely treatment in patients requiring emergent interventions. When a conventional Deep Learning (DL) approach for C-arm control fails, clinicians must revert to manual operation, resulting in additional delays. Consequently, an agentic C-arm control framework based on multimodal large language models (MLLMs) is highly desirable, as it can incorporate clinician feedback and use reasoning to make adjustments toward more accurate positioning. Skeletal landmark localization is essential for C-arm control, and we investigate adapting MLLMs for autonomous landmark localization. Methods: We used an annotated synthetic X-ray dataset and a real X-ray dataset. Each X-ray in both datasets is paired with several skeletal landmarks. We fine-tuned two MLLMs and tasked them with retrieving the closest landmarks from each X-ray. Quantitative evaluations of landmark localization were performed and compared against a leading DL approach. We further conducted qualitative experiments demonstrating: (1) how an MLLM can correct an initially incorrect prediction through reasoning, and (2) how the MLLM can sequentially navigate the C-arm toward a target location. Results: On both datasets, fine-tuned MLLMs demonstrate competitive performance across all localization tasks when compared with the DL approach. In the qualitative experiments, the MLLMs provide evidence of reasoning and spatial awareness. Conclusion: This study shows that fine-tuned MLLMs achieve accurate skeletal landmark localization and hold promise for agentic autonomous C-arm control. Our code is available athttps://github.com/marszzibros/C-arm-localization-LLMs.git
匹配关键词: JAX
---

[ACADEMIC - ARXIV]
标题: Enabling AI ASICs for Zero Knowledge Proof
作者: Jianming Tong, Jingtian Dang, Simon Langowski, Tianhao Huang, Asra Ali, Jeremy Kun, Jevin Jiang, Srinivas Devadas, Tushar Krishna
链接: https://arxiv.org/abs/2604.17808v1
完整摘要: Zero-knowledge proof (ZKP) provers remain costly because multi-scalar multiplication (MSM) and number-theoretic transforms (NTTs) dominate runtime as they need significant computation. AI ASICs such as TPUs provide massive matrix throughput and SotA energy efficiency. We present MORPH, the first framework that reformulates ZKP kernels to match AI-ASIC execution. We introduce Big-T complexity, a hardware-aware complexity model that exposes heterogeneous bottlenecks and layout-transformation costs ignored by Big-O. Guided by this analysis, (1) at arithmetic level, MORPH develops an MXU-centric extended-RNS lazy reduction that converts high-precision modular arithmetic into dense low-precision GEMMs, eliminating all carry chains, and (2) at dataflow level, MORPH constructs a unified-sharding layout-stationary TPU Pippenger MSM and optimized 3/5-step NTT that avoid on-TPU shuffles to minimize costly memory reorganization. Implemented in JAX, MORPH enables TPUv6e8 to achieve up-to 10x higher throughput on NTT and comparable throughput on MSM than GZKP. Our code: https://github.com/EfficientPPML/MORPH.
匹配关键词: JAX
---

[ACADEMIC - ARXIV]
标题: AGoQ: Activation and Gradient Quantization for Memory-Efficient Distributed Training of LLMs
作者: Wenxiang Lin, Juntao Huang, Luhan Zhang, Laili Li, Xiang Bao, Mengyang Zhang, Bing Wang, Shaohuai Shi
链接: https://arxiv.org/abs/2605.00539v1
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
标题: AGoQ: Activation and Gradient Quantization for Memory-Efficient Distributed Training of LLMs
作者: Wenxiang Lin, Juntao Huang, Luhan Zhang, Laili Li, Xiang Bao, Mengyang Zhang, Bing Wang, Shaohuai Shi
链接: https://arxiv.org/abs/2605.00539v1
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
标题: MoEless: Efficient MoE LLM Serving via Serverless Computing
作者: Hanfei Yu, Bei Ouyang, Shwai He, Ang Li, Hao Wang
链接: https://arxiv.org/abs/2603.06350v1
完整摘要: Large Language Models (LLMs) have become a cornerstone of AI, driving progress across diverse domains such as content creation, search and recommendation systems, and AI-assisted workflows. To alleviate extreme training costs and advancing model scales, Mixture-of-Experts (MoE) has become a popular backbone for modern LLMs, which are commonly served in distributed deployment using expert parallelism (EP). However, MoE's sparse activation mechanism leads to severe expert load imbalance, where a few experts become overloaded while others remain idle, resulting in expert stragglers that inflate inference latency and serving cost. Existing expert load balancing solutions assume static resource configurations on serverful infrastructures, limiting expert scalability and elasticity, and resulting in either costly real-time expert swapping or degraded generation quality. We present MoEless, the first serverless MoE serving framework that mitigates expert load imbalance and accelerates inference via serverless experts. MoEless employs lightweight, layer-aware predictors to accurately estimate incoming expert load distributions and proactively identify stragglers. We design optimized expert scaling and placement strategies to maximize function locality, improve GPU utilization, and balance loads across experts and GPUs. MoEless is prototyped on top of Megatron-LM and deployed on an eight-GPU testbed. Experiments with open-source MoE models and real-world workloads show that MoEless reduces inference latency by 43% and inference cost by 84% compared to state-of-the-art solutions.
匹配关键词: Megatron
---

[ACADEMIC - ARXIV]
标题: Ruyi2 Technical Report
作者: Huan Song, Shuyu Tian, Junyi Hao, Minxiu Xu, Hongjun An, Yiliang Song, Jiawei Shao, Xuelong Li
链接: https://arxiv.org/abs/2602.22543v1
完整摘要: Large Language Models (LLMs) face significant challenges regarding deployment costs and latency, necessitating adaptive computing strategies. Building upon the AI Flow framework, we introduce Ruyi2 as an evolution of our adaptive model series designed for efficient variable-depth computation. While early-exit architectures offer a viable efficiency-performance balance, the Ruyi model and existing methods often struggle with optimization complexity and compatibility with large-scale distributed training. To bridge this gap, Ruyi2 introduces a stable "Familial Model" based on Megatron-LM. By using 3D parallel training, it achieves a 2-3 times speedup over Ruyi, while performing comparably to same-sized Qwen3 models. These results confirm that family-based parameter sharing is a highly effective strategy, establishing a new "Train Once, Deploy Many" paradigm and providing a key reference for balancing architectural efficiency with high-performance capabilities.
匹配关键词: Megatron
---

[ACADEMIC - ARXIV]
标题: DHP: Efficient Scaling of MLLM Training with Dynamic Hybrid Parallelism
作者: Yifan Niu, Han Xiao, Dongyi Liu, Wei Zhou, Jia Li
链接: https://arxiv.org/abs/2602.21788v1
完整摘要: Scaling long-context capabilities is crucial for Multimodal Large Language Models (MLLMs). However, real-world multimodal datasets are extremely heterogeneous. Existing training frameworks predominantly rely on static parallelism strategies, which suffer from severe load imbalance, redundant communication, and suboptimal hardware utilization under data heterogeneity. In this work, we propose Dynamic Hybrid Parallelism (DHP), an efficient parallelism strategy that adaptively reconfigures communication groups and parallelism degrees during MLLM training. We generalize the non-power-of-two parallelism degrees and develop a polynomial-time algorithm to generate near-optimal parallelism strategies with only millisecond-level overhead per training batch. DHP is able to maintain high hardware efficiency even under extreme data variability. Experimental results demonstrate that DHP significantly outperforms Megatron-LM and DeepSpeed, achieving up to 1.36 $\times$ speedup in training throughput while maintaining near-linear scaling efficiency across large-scale NPU clusters.
匹配关键词: Megatron
---

[ACADEMIC - ARXIV]
标题: Position: LLM Serving Needs Mathematical Optimization and Algorithmic Foundations, Not Just Heuristics
作者: Zijie Zhou
链接: https://arxiv.org/abs/2605.01280v1
完整摘要: This position paper argues that LLM inference serving has outgrown generic heuristics and now demands mathematical optimization and algorithmic foundations. Despite rapid advances in serving systems such as vLLM and SGLang, their algorithmic cores remain largely unchanged from classical distributed computing: request routing uses join-shortest-queue or round-robin, scheduling defaults to FIFO, and KV cache eviction follows LRU. These general-purpose policies ignore the distinctive structure of LLM inference--dynamically growing KV cache memory, prefill-decode phase asymmetry, unknown output lengths, and continuous batching constraints. We contend that the field must develop mathematical models capturing these characteristics, enabling the design of algorithms with provable performance guarantees across diverse workloads, rather than heuristics that may succeed in some scenarios but fail unpredictably in others. Emerging work at the intersection of operations research and ML systems demonstrates that principled methods can match or exceed heuristic performance while providing theoretical guarantees. We call on the community to recognize algorithmic design for LLM serving as a research frontier.
匹配关键词: vLLM
---

[ACADEMIC - ARXIV]
标题: SAGA: Workflow-Atomic Scheduling for AI Agent Inference on GPU Clusters
作者: Dongxin Guo, Jikun Wu, Siu Ming Yiu
链接: https://arxiv.org/abs/2605.00528v1
完整摘要: AI agents execute tens to hundreds of chained LLM calls per task, yet GPU schedulers treat each call as independent, discarding gigabytes of intermediate state between steps and inflating end-to-end latency by 3-8x. We argue that this request-level abstraction is fundamentally mismatched to compound AI workloads, and propose a shift to program-level scheduling: treating the entire agent workflow (not individual inference calls) as the first-class schedulable unit. We present SAGA, a distributed scheduler that implements this abstraction through three mechanisms: (1) Agent Execution Graphs that capture workflow structure to predict KV cache reuse across tool-call boundaries, achieving within 1.31x of Bélády's optimal offline policy; (2) session-affinity batching with work stealing that co-locates correlated requests while maintaining global load balance; and (3) Agent Fair Share, a task-completion-time fairness metric with provable bounded-deviation guarantees. On a 64-GPU cluster serving SWE-bench coding agents and WebArena browser tasks, SAGA reduces task completion time by 1.64x (geometric mean, p < 0.001) over vLLM v0.15.1 with prefix caching and affinity routing, while improving GPU memory utilization by 1.22x and achieving 99.2% SLO attainment under multi-tenant interference. These latency gains come at a quantified cost: approximately 30% lower peak throughput than throughput-optimal batch scheduling, a tradeoff appropriate for the latency-sensitive interactive deployments that dominate compound AI usage. Our results demonstrate that workflow-aware scheduling is essential for efficient compound AI serving.
匹配关键词: vLLM
---

[ACADEMIC - ARXIV]
标题: Unifying Sparse Attention with Hierarchical Memory for Scalable Long-Context LLM Serving
作者: Zihan Zhao, Baotong Lu, Shengjie Lin, Yizou Chen, Jing Liu, Yanqi Zhang, Ziming Miao, Ming-Chang Yang, Haiying Shen, Qi Chen, Fan Yang
链接: https://arxiv.org/abs/2604.26837v1
完整摘要: Long-context LLM serving is bottlenecked by the cost of attending over ever-growing KV caches. Dynamic sparse attention promises relief by accessing only a small, query-dependent subset of the KV state per decoding step and extending the KV storage to CPU memory. In practice, however, these algorithmic savings rarely translate into end-to-end system-level gains because sparse methods typically operate at different granularities and thus rely on ad hoc, per-algorithm implementations. At the same time, hierarchical KV storage introduces a new systems bottleneck: retrieving fine-grained, irregular KV subsets across the GPU-CPU boundary can easily erase the benefits of sparsity. We present SPIN, a sparse-attention-aware inference framework that co-designs the execution pipeline with hierarchical KV storage through three techniques: (1) a unified partition abstraction that maps different sparsity granularities onto a shared page-based KV substrate; (2) a locality-aware KV cache manager that dynamically sizes per-request HBM budgets and uses a GPU-friendly bucketed LRU policy to cut PCIe round-trips; and (3) a two-level hierarchical metadata layout sized to the active working set rather than the worst-case address space. Built on vLLM with three representative sparse attention algorithms, SPIN delivers 1.66-5.66x higher end-to-end throughput and 7-9x lower TTFT than vLLM, and reduces TPOT by up to 58% over the original sparse-attention implementations.
匹配关键词: vLLM
---

[ACADEMIC - ARXIV]
标题: Accelerating RL Post-Training Rollouts via System-Integrated Speculative Decoding
作者: Hayate Iso, Tiyasa Mitra, Sudipta Mondal, Rasoul Shafipour, Venmugil Elango, Terry Kong, Yuki Huang, Seonjin Na, Izzy Putterman, Benjamin Chislett, Maor Ashkenazi, Joseph Guman, Gerald Shen, Tugrul Konuk, Ashwath Aithal, Ritika Borkar, Ran Zilberstein, Bita Rouhani
链接: https://arxiv.org/abs/2604.26779v1
完整摘要: RL post-training of frontier language models is increasingly bottlenecked by autoregressive rollout generation, making rollout acceleration a central systems challenge. Many existing efficiency methods improve throughput by changing the rollout or optimization regime, for example, through off-policy execution, replay, or lower-precision generation. We study speculative decoding as a lossless acceleration primitive for RL rollouts that preserves the target model's output distribution. We implement speculative decoding in NeMo-RL with a vLLM backend, supporting both synchronous and asynchronous pipelines and enabling speculation during RL rollouts. This benefit is realizable across speculation mechanisms, such as pretrained MTP heads, small external draft models or even techniques such as Eagle3, which are traditionally applied after RL phase. This yields a deployment path for state-of-the-art speculative decoding inside RL training. In a reasoning post-training workload at 8B scale under synchronous RL, speculative decoding improves rollout throughput by 1.8x. Using a high-fidelity performance simulator, we project that combining speculative decoding with asynchronous RL yields up to 2.5x end-to-end training speedup at 235B scale.
匹配关键词: vLLM
---

[ACADEMIC - ARXIV]
标题: RaMP: Runtime-Aware Megakernel Polymorphism for Mixture-of-Experts
作者: Vyom Sharma, Debajyoti Datta
链接: https://arxiv.org/abs/2604.26039v1
完整摘要: The optimal kernel configuration for Mixture-of-Experts (MoE) inference depends on both batch size and the expert routing distribution, yet production systems dispatch from batch size alone, leaving 10-70% of kernel throughput unrealized. We present RaMP, a routing-aware dispatch framework. A performance-region analysis derives, from hardware constants alone, when each optimization helps, correctly predicting all 8 tested architectures, including 3 unseen. A four-parameter wave cost model selects the fastest configuration from the runtime expert histogram, achieving 0.93% mean regret versus exhaustive search, fitted from just 10-24 minutes of one-time profiling per model. Because the model depends only on CTA grid geometry, it is kernel-agnostic: applied to Alpha-MoE, it delivers 1.14x with no source modification. Paired with a co-designed CuTe DSL kernel exposing 134-268 polymorphic configurations, RaMP delivers 1.22x kernel speedup over static dispatch and 1.30x end-to-end speedup in vLLM serving over Triton, 1.41x over DeepGEMM, and 1.13x over FlashInfer CUTLASS.
匹配关键词: vLLM
---

[ACADEMIC - ARXIV]
标题: AgriKD: Cross-Architecture Knowledge Distillation for Efficient Leaf Disease Classification
作者: Minh-Dung Le, Minh-Duc Hoang, Hoang-Vu Truong, Thi-Thu-Hong Phan
链接: https://arxiv.org/abs/2605.01355v1
完整摘要: Automated leaf disease classification is critical for early disease detection in resource-constrained field environments. Vision Transformers (ViTs) provide strong representation capability by modeling long-range dependencies and inter-class relationships; however, their high computational cost makes them impractical for deployment on edge devices. As a result, existing approaches struggle to effectively transfer these rich representations to lightweight models. This paper introduces AgriKD, a cross-architecture knowledge distillation framework for efficient edge deployment, which transfers knowledge from a Vision Transformer (ViT) teacher to a compact convolutional student model. To bridge the representational gap between Transformer and CNN architectures, the proposed approach integrates multiple distillation objectives at the output, feature, and relational levels, where each objective captures a different aspect of the teacher knowledge. This enables the student model to better preserve and utilize transformer-derived global representations. Experiments on multiple leaf disease datasets show that the distilled student achieves performance comparable to the teacher while significantly improving efficiency, reducing model parameters by approximately 172 times, computational cost by 47.57 times, and inference latency by 18-22 times. Furthermore, the optimized model is deployed across multiple runtime formats, including ONNX, TFLite Float16, and TensorRT FP16, achieving consistent predictive performance with negligible accuracy degradation. Real-world deployment on NVIDIA Jetson edge devices and a mobile application demonstrates reliable real-time inference, highlighting the practicality of AgriKD for AI-powered agricultural applications in resource-constrained environments.
匹配关键词: TensorRT
---

[ACADEMIC - ARXIV]
标题: Silicon Showdown: Performance, Efficiency, and Ecosystem Barriers in Consumer-Grade LLM Inference
作者: Abdurrahman Javat, Allan Kazakov
链接: https://arxiv.org/abs/2605.00519v2
完整摘要: The operational landscape of local Large Language Model (LLM) inference has shifted from lightweight models to datacenter-class weights exceeding 70B parameters, creating profound systems challenges for consumer hardware. This paper presents a systematic empirical analysis of the Nvidia and Apple Silicon ecosystems, specifically characterizing the distinct intra-architecture trade-offs required to deploy these massive models. On the Nvidia Blackwell architecture, we identify a critical "Backend Dichotomy" within the TensorRT-LLM stack: while the new NVFP4 quantization format delivers a 1.6x throughput advantage over optimized BF16 baselines (151 tokens/s vs. 92 tokens/s), realizing this performance requires navigating complex runtime constraints that trade startup latency for generation speed. Furthermore, we characterize the "VRAM Wall" for 70B+ models: on discrete GPUs, users face a destructive choice between aggressive quantization (e.g., Q2) that degrades model intelligence to fit in VRAM, or PCIe-bottlenecked CPU offloading, which reduces throughput by over 90% compared to full-GPU execution. Conversely, Apple's Unified Memory Architecture (UMA) circumvents these bottlenecks, enabling linear scaling for 80B parameter models at practical 4-bit precisions. This architectural divergence extends to operational sustainability, where Apple's SoC design demonstrates up to a 23x advantage in energy efficiency (tokens/joule). We conclude that for consumer-grade inference, the optimal hardware is defined by a complex interplay between compute density (Nvidia) and memory capacity (Apple), moderated by the significant "ecosystem friction" of proprietary quantization workflows.
匹配关键词: TensorRT
---

[ACADEMIC - ARXIV]
标题: EdgeFM: Efficient Edge Inference for Vision-Language Models
作者: Mengling Deng, Yuanpeng Chen, Sheng Yang, Wei Tao, Wenhai Zhang, Hui Song, Linyuanhao Qin, Kai Zhao, Xiaojun Ye, Shanhui Mo, Jingli Fan, Shuang Zhang, Bei Liu, Tiankun Zhao, Xiangjing An
链接: https://arxiv.org/abs/2604.27476v1
完整摘要: Vision-language models (VLMs) have demonstrated strong applicability in edge industrial applications, yet their deployment remains severely constrained by requirements for deterministic low latency and stable execution under resource limitations. Existing frameworks either rely on bloated general-purpose designs or force developers into opaque, hardware-specific closed-source ecosystems, leading to hardware lock-in limitation and poor cross-platform adaptability. Observing that modern AI agents can efficiently search and tune configurations to generate highly optimized low-level kernels for standard LLM operators, we propose EdgeFM, a lightweight, agent-driven VLM/LLM inference framework tailored for cross-platform industrial edge deployment. EdgeFM removes non-essential features to reduce single-request latency, and encapsulates agent-tuned kernel optimizations as a modular library of reusable skills. By allowing direct invocation of these skills rather than waiting for closed-source implementations, it effectively closes the performance gap long dominated by proprietary toolchains. The framework natively supports mainstream platforms including x86 and NVIDIA Orin SoCs, and represents the first end-to-end VLA deployment on the domestic Horizon Journey platform, enhancing cross-platform portability. In most cases, it yields clearly better inference performance than conventional vendor-specific toolchains, achieving up to 1.49 times speedup over TensorRT-Edge-LLM on the NVIDIA Orin platform. Experimental results show that EdgeFM delivers favorable end-to-end inference performance, providing an open-source, production-grade solution for diverse edge industrial scenarios.
匹配关键词: TensorRT
---

[ACADEMIC - ARXIV]
标题: Hybrid JIT-CUDA Graph Optimization for Low-Latency Large Language Model Inference
作者: Divakar Kumar Yadav, Tian Zhao
链接: https://arxiv.org/abs/2604.23467v1
完整摘要: Large Language Models (LLMs) have achieved strong performance across natural language and multimodal tasks, yet their practical deployment remains constrained by inference latency and kernel launch overhead, particularly in interactive, short-sequence settings. This paper presents a hybrid runtime framework that combines Just-In-Time (JIT) compilation with CUDA Graph execution to reduce launch overhead while preserving runtime flexibility during autoregressive decoding. The framework partitions transformer inference into static components executed via CUDA Graph replay and dynamic components handled through JIT-compiled kernels, enabling asynchronous graph capture and reuse across decoding steps. We evaluate the proposed approach on LLaMA-2 7B using single-GPU, batch-size-one inference across prompt lengths from 10 to 500 tokens. Experimental results show that the hybrid runtime reduces Time-to-First-Token (TTFT) by up to 66.0% and achieves lower P99 latency compared with TensorRT-LLM in this regime. These results indicate that hybrid JIT-CUDA Graph execution can effectively reduce inference latency and variance for short-sequence LLM workloads, making it a practical optimization strategy for latency-sensitive AI applications.
匹配关键词: TensorRT
---

[ACADEMIC - ARXIV]
标题: DEEP-GAP: Deep-learning Evaluation of Execution Parallelism in GPU Architectural Performance
作者: Kathiravan Palaniappan
链接: https://arxiv.org/abs/2604.14552v1
完整摘要: Modern datacenters increasingly rely on low-power, single-slot inference accelerators to balance performance, energy efficiency, and rack density constraints. The NVIDIA T4 GPU has become widely deployed due to strong performance per watt and mature software support. Its successor, the NVIDIA L4 GPU, introduces improvements in Tensor Core throughput, cache capacity, memory bandwidth, and parallel execution capability. However, limited empirical evidence quantifies the practical inference performance gap between these two generations under controlled and reproducible conditions. This work introduces DEEP-GAP, a systematic evaluation extending the GDEV-AI methodology to GPU inference. Using identical configurations and workloads, we evaluate ResNet18, ResNet50, and ResNet101 across FP32, FP16, and INT8 precision modes using PyTorch and TensorRT. Results show that reduced precision significantly improves performance, with INT8 achieving up to 58x throughput improvement over CPU baselines. L4 achieves up to 4.4x higher throughput than T4 while reaching peak efficiency at smaller batch sizes between 16 and 32, improving latency-throughput tradeoffs for latency-sensitive workloads. T4 remains competitive for large batch workloads where cost or power efficiency is important. DEEP-GAP provides practical guidance for selecting precision modes, batch sizes, and GPU architectures for modern inference deployments.
匹配关键词: TensorRT
---

[ACADEMIC - ARXIV]
标题: AcademiClaw: When Students Set Challenges for AI Agents
作者: Junjie Yu, Pengrui Lu, Weiye Si, Hongliang Lu, Jiabao Wu, Kaiwen Tao, Kun Wang, Lingyu Yang, Qiran Zhang, Xiuting Guo, Xuanyu Wang, Yang Wang, Yanjie Wang, Yi Yang, Zijian Hu, Ziyi Yang, Zonghan Zhou, Binghao Qiang, Borui Zhang, Chenning Li, Enchang Zhang, Feifan Chen, Feng Jian, Fengyin Sun, Hao Qiu, Hao Zheng, Haoran Zhu, Hongyu Liu, Jianbin Deng, Jiaxin Song, Jiaying Chi, Jiayou Shi, Jie Fang, Jinghui Zhong, Jingyu Zhou, Jinze Li, Junfeng Yi, Junyan Yu, Junzhi Xue, Ni Song, Pengyi Chen, Qi Chen, Quansheng Li, Rui Tao, Shenghai Gong, Shenhang Lu, Tianqi Shen, Tianxiang Zhu, Tiehan Kang, Tingyu Li, Wendi Wu, Xiao Shen, Xiao Zhou, Xiaotao Zhang, Xinrong Li, Xuankun Yang, Xun Zhang, Yan Li, Ye Lu, Yi Wang, Yibo Zhou, Yichi Zhang, Yihao Sun, Yijun Huang, Yixin Zhu, Yixuan Wu, Yuchen Sun, Yue Wu, Yuheng Sun, Yukun Li, Yutian Tu, Yuxuan Qin, Yuzhuo Wu, Zeyu Li, Zhengyu Lou, Zhenning Ran, Zizhu He, Pengfei Liu
链接: https://arxiv.org/abs/2605.02661v1
完整摘要: Benchmarks within the OpenClaw ecosystem have thus far evaluated exclusively assistant-level tasks, leaving the academic-level capabilities of OpenClaw largely unexamined. We introduce AcademiClaw, a bilingual benchmark of 80 complex, long-horizon tasks sourced directly from university students' real academic workflows -- homework, research projects, competitions, and personal projects -- that they found current AI agents unable to solve effectively. Curated from 230 student-submitted candidates through rigorous expert review, the final task set spans 25+ professional domains, ranging from olympiad-level mathematics and linguistics problems to GPU-intensive reinforcement learning and full-stack system debugging, with 16 tasks requiring CUDA GPU execution. Each task executes in an isolated Docker sandbox and is scored on task completion by multi-dimensional rubrics combining six complementary techniques, with an independent five-category safety audit providing additional behavioral analysis. Experiments on six frontier models show that even the best achieves only a 55\% pass rate. Further analysis uncovers sharp capability boundaries across task domains, divergent behavioral strategies among models, and a disconnect between token consumption and output quality, providing fine-grained diagnostic signals beyond what aggregate metrics reveal. We hope that AcademiClaw and its open-sourced data and code can serve as a useful resource for the OpenClaw community, driving progress toward agents that are more capable and versatile across the full breadth of real-world academic demands. All data and code are available at https://github.com/GAIR-NLP/AcademiClaw.
匹配关键词: CUDA
---

[ACADEMIC - ARXIV]
标题: VUDA: Breaking CUDA-Vulkan Isolation for Spatial Sharing of Compute and Graphics on the Same GPU
作者: Bin Xu, Pengfei Hu, Wenxin Zheng, Jinyu Gu, Haibo Chen
链接: https://arxiv.org/abs/2605.01352v1
完整摘要: GPU-based simulation environments for embodied AI interleave physics simulation (CUDA) and photorealistic rendering (Vulkan) on a single device. We observe that two foundational scenarios -- simulation data generation and RL training -- can be naturally adapted to execute their simulation and rendering phases concurrently, presenting a significant opportunity to improve GPU utilization through spatial multiplexing. However, a fundamental obstacle we term execution isolation prevents this: CUDA and Vulkan create separate GPU contexts whose channels are bound to different scheduling groups, confining compute and graphics to mutually exclusive time slices. Existing spatial-sharing techniques are limited to the CUDA ecosystem, while temporal-sharing approaches underutilize available resources. This paper presents VUDA, a system that breaks execution isolation to enable spatial parallelism between CUDA compute and Vulkan graphics workloads. VUDA is built on two key observations: although CUDA and Vulkan expose different programming abstractions, their execution paths converge to a common channel primitive at the driver and hardware level; meanwhile, their virtual-address spaces are inherently disjoint, making safe page-table merging feasible without remapping. VUDA exposes a thin API for developers to annotate co-schedulable CUDA streams, and realizes spatial sharing through channel redirection into Vulkan's scheduling domain and page-table grafting to unify address spaces, eliminating all data copying on the critical path. Experiments on representative embodied-AI workloads show that VUDA delivers up to 85% higher throughput than temporal-sharing baselines, while improving GPU utilization and reducing end-to-end latency.
匹配关键词: CUDA
---

[ACADEMIC - ARXIV]
标题: VkSplat: High-Performance 3DGS Training in Vulkan Compute
作者: Jingxiang Chen, Mohamed Ibrahim, Yang Liu
链接: https://arxiv.org/abs/2605.00219v1
完整摘要: We present VkSplat, a high-performance, cross-vendor 3D Gaussian Splatting (3DGS) training pipeline implemented fully in Vulkan compute, addressing performance and compatibility limitation of existing training pipelines. With various optimizations, we achieve $3.3\times$ speed and $33\%$ VRAM reduction over CUDA+PyTorch baseline, maintaining quality, and demonstrating compatibility across GPU vendors. To the best of our knowledge, this is the first fully-Vulkan-based 3DGS training pipeline that achieves state-of-the-art performance. Code: \href{https://github.com/harry7557558/vksplat}{https://github.com/harry7557558/vksplat}
匹配关键词: CUDA
---

[ACADEMIC - ARXIV]
标题: MesonGS++: Post-training Compression of 3D Gaussian Splatting with Hyperparameter Searching
作者: Shuzhao Xie, Junchen Ge, Weixiang Zhang, Jiahang Liu, Chen Tang, Yunpeng Bai, Shijia Ge, Jingyan Jiang, Yuzhi Huang, Fengnian Yang, Cong Zhang, Xiaoyi Fan, Zhi Wang
链接: https://arxiv.org/abs/2604.26799v1
完整摘要: 3D Gaussian Splatting (3DGS) achieves high-quality novel view synthesis with real-time rendering, but its storage cost remains prohibitive for practical deployment. Existing post-training compression methods still rely on many coupled hyperparameters across pruning, transformation, quantization, and entropy coding, making it difficult to control the final compressed size and fully exploit the rate-distortion trade-off. We propose MesonGS++, a size-aware post-training codec for 3D Gaussian compression. On the codec side, MesonGS++ combines joint importance-based pruning, octree geometry coding, attribute transformation, selective vector quantization for higher-degree spherical harmonics, and group-wise mixed-precision quantization with entropy coding. On the configuration side, it treats the reserve ratio and bit-width allocation as the dominant rate-distortion knobs and jointly optimizes them under a target storage budget via discrete sampling and 0--1 integer linear programming. We further propose a linear size estimator and a CUDA parallel quantization operator to accelerate the hyperparameter searching process. Extensive experiments show that MesonGS++ achieves over 34$\times$ compression while preserving rendering fidelity, outperforming state-of-the-art post-training methods and accurately meeting target size budgets. Remarkably, without any training, MesonGS++ can even surpass the PSNR of vanilla 3DGS at a 20$\times$ compression rate on the Stump scene. Our code is available at https://github.com/mmlab-sigs/mesongs_plus
匹配关键词: CUDA
---

[ACADEMIC - ARXIV]
标题: PointTransformerX: Portable and Efficient 3D Point Cloud Processing without Sparse Algorithms
作者: Laurenz Reichardt, Nikolas Ebert, Oliver Wasenmüller
链接: https://arxiv.org/abs/2604.24169v2
完整摘要: 3D point cloud perception remains tightly coupled to custom CUDA operators for spatial operations, limiting portability and efficiency on non-NVIDIA, AMD, and embedded hardware. We introduce PointTransformerX (PTX), a fully PyTorch-native vision transformer backbone for 3D point clouds, removing all custom CUDA operators and external libraries while retaining competitive accuracy. PTX introduces 3D-GS-RoPE, a rotary positional embedding that encodes 3D spatial relationships directly in self-attention without neighborhood construction, and further replaces sparse convolutional patch embedding with a linear projection. PTX explores inference-time scaling of attention windows to improve accuracy without retraining. With a redesigned feed-forward network, PTX achieves 98.7\% of PointTransformer V3's accuracy on ScanNet with 79.2\% fewer parameters and executing 1.6\times faster while requiring just 253 MB memory. PTX runs natively on NVIDIA GPUs, AMD GPUs (ROCm), and CPUs, providing an efficient and portable foundation for point cloud perception.
匹配关键词: CUDA
---

[ACADEMIC - ARXIV]
标题: Feature-Augmented Transformers for Robust AI-Text Detection Across Domains and Generators
作者: Mohamed Mady, Johannes Reschke, Björn Schuller
链接: https://arxiv.org/abs/2605.03969v1
完整摘要: AI-generated text is nowadays produced at scale across domains and heterogeneous generation pipelines, making robustness to distribution shift a central requirement for supervised binary detectors. We train transformer-based detectors on HC3 PLUS and calibrate a single decision threshold by maximising balanced accuracy on held-out validation; this threshold is then kept fixed for all downstream test distributions, revealing domain- and generator-dependent error asymmetries under shift. We evaluate in-domain on HC3 PLUS, under cross-dataset transfer to the multi-domain, multi-generator M4 benchmark, and on the external AI-Text-Detection-Pile. Although base models achieve near-ceiling in-domain performance (up to 99.5% balanced accuracy), performance under shift is brittle and strongly model-dependent. Feature augmentation via attention-based linguistic feature fusion improves transfer, with our best model (DeBERTa-v3-base+FeatAttn) achieving 85.9% balanced accuracy on M4. Multi-seed experiments confirm high stability. Under the same fixed-threshold protocol, our model outperforms strong zero-shot baselines by up to +7.22 points. Category-level ablations further show that readability and vocabulary features contribute most to robustness under shift. Overall, these results demonstrate that feature augmentation and a modern DeBERTa backbone significantly outperform earlier BERT/RoBERTa models, while the fixed-threshold protocol provides a more realistic and informative assessment of practical detector robustness.
匹配关键词: distributed training
---

[ACADEMIC - ARXIV]
标题: Label-Efficient School Detection from Aerial Imagery via Weakly Supervised Pretraining and Fine-Tuning
作者: Zakarya Elmimouni, Fares Fourati, Mohamed-Slim Alouini
链接: https://arxiv.org/abs/2605.03968v1
完整摘要: Accurate school detection is essential for supporting education initiatives, including infrastructure planning and expanding internet connectivity to underserved areas. However, many regions around the world face challenges due to outdated, incomplete, or unavailable official records. Manual mapping efforts, while valuable, are labor-intensive and lack scalability across large geographic areas. To address this, we propose a weakly supervised framework for school detection from aerial imagery that minimizes the need for human annotations while supporting global mapping efforts. Our method is specifically designed for low-data regimes, where manual annotations are extremely scarce. We introduce an automatic labeling pipeline that leverages sparse location points and semantic segmentation to generate infrastructure masks from which we generate bounding boxes. Using these automatically labeled images, we train our detectors on a first training stage to learn a representation of what schools look like, then using a small set of manually labeled images, we fine-tune the previously trained models on this clean dataset. This two stage training pipeline enables large-scale and strong detection in low-data setting of school infrastructure with minimal supervision. Our results demonstrate strong object detection performance, particularly in the low-data regime, where the models achieve promising results using only 50 manually labeled images, significantly reducing the need for costly annotations. This framework supports education and connectivity initiatives worldwide by providing an efficient and extensible approach to mapping schools from space. All models, training code and auto-labeled data will be publicly released to foster future research and real-world impact.
匹配关键词: distributed training
---

[ACADEMIC - ARXIV]
标题: Pretrained Model Representations as Acquisition Signals for Active Learning of MLIPs
作者: Eszter Varga-Umbrich, Shikha Surana, Paul Duckworth, Jules Tilly, Olivier Peltre, Zachary Weller-Davies
链接: https://arxiv.org/abs/2605.03964v1
完整摘要: Training machine learning interatomic potentials (MLIPs) for reactive chemistry is often bottlenecked by the high cost of quantum chemical labels and the scarcity of transition state configurations in candidate pools. Active learning (AL) can mitigate these costs, but its effectiveness hinges on the acquisition rule. We investigate whether the latent space of a pretrained MLIP already contains the information necessary for effective acquisition, eliminating the need for auxiliary uncertainty heads, Bayesian training and fine-tuning, or committee ensembles. We introduce two acquisition signals derived directly from a pretrained MACE potential: a finite-width neural tangent kernel (NTK) and an activation kernel built from hidden latent space features. On reactive-chemistry benchmarks, both kernels consistently outperform fixed-descriptor baselines, committee disagreement, and random acquisition, reducing the data required to reach performance targets by an average of 38% for energy error and 28% for force error. We further show that the pretrained model induces similarity spaces that preserve chemically meaningful structure and provide more reliable residual uncertainty estimates than randomly initialised or fixed-descriptor-based kernels. Our results suggest that pretraining aligns latent-space geometry with model error, yielding a practical and sufficient acquisition signal for reactive MLIP fine-tuning.
匹配关键词: distributed training
---

[ACADEMIC - ARXIV]
标题: TabSurv: Adapting Modern Tabular Neural Networks to Survival Analysis
作者: Stanislav Kirpichenko, Andrei Konstantinov, Lev Utkin
链接: https://arxiv.org/abs/2605.03944v1
完整摘要: Survival analysis on tabular data is a well-studied problem. However, existing deep learning methods are often highly task-specific, which can limit the transfer of new approaches from other domains and introduce constraints that may affect performance. We propose TabSurv, an approach that adapts modern tabular architectures to survival analysis using either the Weibull distribution or non-parametric survival prediction. TabSurv optimizes SurvHL, a novel histogram loss function supporting censored data. In addition to a baseline feed-forward network, we implement deep ensembles of MLPs for survival analysis within TabSurv. In contrast to prior work, the ensemble components are trained in parallel, optimizing survival distribution parameters before averaging, which promotes diversity across ensemble component predictions. We perform a comprehensive empirical evaluation of different proposed architectures on 10 diverse real-world survival datasets. Our results show that TabSurv consistently outperforms on average established classical and deep learning baselines, such as RSF, DeepSurv, DeepHit, SurvTRACE. Notably, deep ensembles with Weibull parametrization instead of non-parametric models achieve the highest average rank by C-index. Overall, our study clarifies how modern tabular neural networks can be adapted and trained to tackle survival analysis problems, offering a strong and reliable approach. The TabSurv implementation is publicly available.
匹配关键词: distributed training
---

[ACADEMIC - ARXIV]
标题: A Benchmark for Interactive World Models with a Unified Action Generation Framework
作者: Jianjie Fang, Yingshan Lei, Qin Wan, Ziyou Wang, Yuchao Huang, Yongyan Xu, Baining Zhao, Weichen Zhang, Chen Gao, Xinlei Chen, Yong Li
链接: https://arxiv.org/abs/2605.03941v1
完整摘要: Achieving Artificial General Intelligence (AGI) requires agents that learn and interact adaptively, with interactive world models providing scalable environments for perception, reasoning, and action. Yet current research still lacks large-scale datasets and unified benchmarks to evaluate their physical interaction capabilities. To address this, we propose iWorld-Bench, a comprehensive benchmark for training and testing world models on interaction-related abilities such as distance perception and memory. We construct a diverse dataset with 330k video clips and select 2.1k high-quality samples covering varied perspectives, weather, and scenes. As existing world models differ in interaction modalities, we introduce an Action Generation Framework to unify evaluation and design six task types, generating 4.9k test samples. These tasks jointly assess model performance across visual generation, trajectory following, and memory. Evaluating 14 representative world models, we identify key limitations and provide insights for future research. The iWorld-Bench model leaderboard is publicly available at iWorld-Bench.com.
匹配关键词: distributed training
---

[ACADEMIC - ARXIV]
标题: TabSurv: Adapting Modern Tabular Neural Networks to Survival Analysis
作者: Stanislav Kirpichenko, Andrei Konstantinov, Lev Utkin
链接: https://arxiv.org/abs/2605.03944v1
完整摘要: Survival analysis on tabular data is a well-studied problem. However, existing deep learning methods are often highly task-specific, which can limit the transfer of new approaches from other domains and introduce constraints that may affect performance. We propose TabSurv, an approach that adapts modern tabular architectures to survival analysis using either the Weibull distribution or non-parametric survival prediction. TabSurv optimizes SurvHL, a novel histogram loss function supporting censored data. In addition to a baseline feed-forward network, we implement deep ensembles of MLPs for survival analysis within TabSurv. In contrast to prior work, the ensemble components are trained in parallel, optimizing survival distribution parameters before averaging, which promotes diversity across ensemble component predictions. We perform a comprehensive empirical evaluation of different proposed architectures on 10 diverse real-world survival datasets. Our results show that TabSurv consistently outperforms on average established classical and deep learning baselines, such as RSF, DeepSurv, DeepHit, SurvTRACE. Notably, deep ensembles with Weibull parametrization instead of non-parametric models achieve the highest average rank by C-index. Overall, our study clarifies how modern tabular neural networks can be adapted and trained to tackle survival analysis problems, offering a strong and reliable approach. The TabSurv implementation is publicly available.
匹配关键词: GPU optimization
---

[ACADEMIC - ARXIV]
标题: Optimal Posterior Sampling for Policy Identification in Tabular Markov Decision Processes
作者: Cyrille Kone, Kevin Jamieson
链接: https://arxiv.org/abs/2605.03921v1
完整摘要: We study the $(\varepsilon, δ)$-PAC policy identification problem in finite-horizon episodic Markov Decision Processes. Existing approaches provide finite-time guarantees for approximate settings ($\varepsilon>0$) but suffer from high computational cost, rendering them hard to implement, and also suffer from suboptimal dependence on $\log(1/δ)$. We propose a randomized and computationally efficient algorithm for best policy identification that combines posterior sampling with an online learning algorithm to guide exploration in the MDP. Our method achieves asymptotic optimality in sample complexity, also in terms of posterior contraction rate, and runs in $O(S^2AH)$ per episode, matching standard model-based approaches. Unlike prior algorithms such as MOCA and PEDEL, our guarantees remain meaningful in the asymptotic regime and avoid sub-optimal polynomial dependence on $\log(1/δ)$. Our results provide both theoretical insights and practical tools for efficient policy identification in tabular MDPs.
匹配关键词: GPU optimization
---

[ACADEMIC - ARXIV]
标题: Ecologically-Constrained Task Arithmetic for Multi-Taxa Bioacoustic Classifiers Without Shared Data
作者: Ragib Amin Nihal, Benjamin Yen, Runwu Shi, Takeshi Ashizawa, Kazuhiro Nakadai
链接: https://arxiv.org/abs/2605.03914v1
完整摘要: Training data for bioacoustics is scattered across taxa, regions, and institutions. Centralizing it all is often infeasible. We show that independently fine-tuned BEATs encoders can be composed into a unified 661-species classifier via task vector arithmetic without sharing data. We find that bioacoustic task vectors are near-orthogonal (cosine 0.01-0.09). Their separation aligns closely with spectral distribution distance, a gradient consistent with the acoustic niche hypothesis. This geometry makes simple averaging optimal while sign-conflict methods reduce accuracy by one to six percentage points. Composition also creates an asymmetric gap: species-rich groups lose accuracy relative to joint training while underrepresented taxa gain, a redistribution useful for equitable biodiversity monitoring. We verify linear mode connectivity across all taxonomic pairs, demonstrate zero-shot transfer to new regions, and identify domain negation as a boundary condition where composition fails. These results enable a collaborative paradigm for bioacoustics where institutions share only task vectors to assemble multi-taxa classifiers, preserving data privacy.
匹配关键词: GPU optimization
---

[ACADEMIC - ARXIV]
标题: Contextual Multi-Objective Optimization: Rethinking Objectives in Frontier AI Systems
作者: Jie Zhou, Qin Chen, Liang He
链接: https://arxiv.org/abs/2605.03900v1
完整摘要: Frontier AI systems perform best in settings with clear, stable, and verifiable objectives, such as code generation, mathematical reasoning, games, and unit-test-driven tasks. They remain less reliable in open-ended settings, including scientific assistance, long-horizon agents, high-stakes advice, personalization, and tool use, where the relevant objective is ambiguous, context-dependent, delayed, or only partially observable. We argue that many such failures are not merely failures of scale or capability, but failures of objective selection: the system optimizes a locally visible signal while missing which objectives should govern the interaction. We formulate this problem as \emph{contextual multi-objective optimization}. In this setting, systems must consider multiple, context-dependent objectives, such as helpfulness, truthfulness, safety, privacy, calibration, non-manipulation, user preference, reversibility, and stakeholder impact, while determining which objectives are active, which are soft preferences, and which must function as hard or quasi-hard constraints. These examples are not intended as an exhaustive taxonomy: different domains and deployment settings may activate different objective dimensions and different conflict-resolution procedures. Our framework models AI behavior as a context-dependent choice rule over candidate actions, objective estimates, active constraints, stakeholders, uncertainty, and conflict-resolution procedures. We outline an implementation pathway based on decomposed objective representations, context-to-objective routing, hierarchical constraints, deliberative policy reasoning, controlled personalization, tool-use control, diagnostic evaluation, auditing, and post-deployment revision.
匹配关键词: GPU optimization
---

[ACADEMIC - ARXIV]
标题: Raising the Ceiling: Better Empirical Fixation Densities for Saliency Benchmarking
作者: Susmit Agrawal, Jannis Hollman, Matthias Kümmerer
链接: https://arxiv.org/abs/2605.03885v1
完整摘要: Empirical fixation densities, spatial distributions estimated from human eye-tracking data, are foundational to saliency benchmarking. They directly shape benchmark conclusions, leaderboard rankings, failure case analyses, and scientific claims about human visual behavior. Yet the standard estimation method, fixed-bandwidth isotropic Gaussian KDE, has gone essentially unchanged for decades. This matters now more than ever: as the field shifts toward sample-level evaluation (failure case analysis, inverse benchmarking, per-image model comparison), reliable per-image density estimates become critical. We propose a principled mixture model that combines an adaptive-bandwidth KDE based on Abramson's method, center bias and uniform components, and a state-of-the-art saliency model, to capture different spatial and semantic types of interobserver consistency, and optimize all parameters per image via leave-one-subject-out cross-validation. Our method yields substantially higher interobserver consistency estimates across multiple benchmarks, with median per-image gains of 5-15% in log-likelihood and up to 2 percentage points in AUC. For the most affected images -- precisely those most relevant to failure case analysis -- improvements exceed 25%. We leverage these improved estimates to identify and analyze remaining failure cases of state-of-the-art saliency models, demonstrating that significant headroom for model improvement remains. More broadly, our findings highlight that empirical fixation densities should not be treated as fixed ground truths but as evolving estimates that improve with better methodology.
匹配关键词: GPU optimization
---

[ACADEMIC - ARXIV]
标题: EvoLM: Self-Evolving Language Models through Co-Evolved Discriminative Rubrics
作者: Shuyue Stella Li, Rui Xin, Teng Xiao, Yike Wang, Rulin Shao, Zoey Hao, Melanie Sclar, Sewoong Oh, Faeze Brahman, Pang Wei Koh, Yulia Tsvetkov
链接: https://arxiv.org/abs/2605.03871v1
完整摘要: Language models encode substantial evaluative knowledge from pretraining, yet current post-training methods rely on external supervision (human annotations, proprietary models, or scalar reward models) to produce reward signals. Each imposes a ceiling. Human judgment cannot supervise capabilities beyond its own, proprietary APIs create dependencies, and verifiable rewards cover only domains with ground-truth answers. Self-improvement from a model's own evaluative capacity is a reward source that scales with the model itself, yet remains largely untapped by current methods. We introduce EVOLM, a post-training method that structures this capacity into explicit discriminative rubrics and uses them as training signal. EVOLM trains two capabilities within a single language model in alternation: (1) a rubric generator producing instance-specific evaluation criteria optimized for discriminative utility, which maximizes a small frozen judge's ability to distinguish preferred from dispreferred responses; and (2) a policy trained using those rubric-conditioned scores as reward. All preference signals are constructed from the policy's own outputs via temporal contrast with earlier checkpoints, requiring no human annotation or external supervision. EVOLM trains a Qwen3-8B model to generate rubrics that outperform GPT-4.1 on RewardBench-2 by 25.7%. The co-trained policy achieves 69.3% average on the OLMo3-Adapt suite, outperforming policies trained with GPT-4.1 prompted rubrics by 3.9% and with the state-of-the-art 8B reward model SkyWork-RM by 16%. Overall, EVOLM demonstrates that structuring a model's evaluative capacity into co-evolving discriminative rubrics enables self-improvement without external supervision.
匹配关键词: self-supervised
---

[ACADEMIC - ARXIV]
标题: A Comprehensive Analysis of Tokenization and Self-Supervised Learning in End-to-End Automatic Speech Recognition applied on French Language
作者: Thibault Bañeras-Roux, Mickael Rouvier, Jane Wottawa, Richard Dufour
链接: https://arxiv.org/abs/2605.03696v1
完整摘要: The performance of end-to-end automatic speech recognition (ASR) systems enables their increasing integration into numerous applications. While there are various benefits to such speech-to-text systems, the choice of hyperparameters and models plays a crucial role in their performance. Typically, these choices are determined by considering only the character (CER) and/or word error rate (WER) metrics. However, it has been shown in several studies that these metrics are largely incomplete and fail to adequately describe the downstream application of automatic transcripts. In this paper, we conduct a qualitative study on the French language that investigates the impact of subword tokenization algorithms and self-supervised learning models from different linguistic and acoustic perspectives, using a comprehensive set of evaluation metrics.
匹配关键词: self-supervised
---

[ACADEMIC - ARXIV]
标题: Rethinking Temporal Consistency in Video Object-Centric Learning: From Prediction to Correspondence
作者: Zhiyuan Li, Rongzhen Zhao, Wenyan Yang, Wenshuai Zhao, Pekka Marttinen, Joni Pajarinen
链接: https://arxiv.org/abs/2605.03650v1
完整摘要: The de facto approach in video object-centric learning maintains temporal consistency through learned dynamics modules that predict future object representations, called slots. We demonstrate that these predictors function as expensive approximations of discrete correspondence problems. Modern self-supervised vision backbones already encode instance-discriminative features that distinguish objects reliably. Exploiting these features eliminates the need for learned temporal prediction. We introduce Grounded Correspondence, a framework that replaces learned transition functions with deterministic bipartite matching. Slots initialize from salient regions in frozen backbone features. Frame-to-frame identity is maintained through Hungarian matching on slot representations. The approach requires zero learnable parameters for temporal modeling yet achieves competitive performance on MOVi-D, MOVi-E, and YouTube-VIS. Project page: https://magenta-sherbet-85b101.netlify.app/
匹配关键词: self-supervised
---

[ACADEMIC - ARXIV]
标题: The Detector Teaches Itself: Lightweight Self-Supervised Adaptation for Open-Vocabulary Object Detection
作者: Yazhe Wan, Changjae Oh
链接: https://arxiv.org/abs/2605.03642v1
完整摘要: Open-vocabulary object detection aims to recognize objects from an open set of categories, which leverages vision-language models (VLMs) pre-trained on large-scale image-text data. The cooperative paradigm combines an object detector with a VLM to achieve zero-shot recognition of novel objects. However, VLMs pre-trained on full images often struggle to capture local object details, limiting their effectiveness when applied to region-level detection. We present Decoupled Adaptivity Training (DAT), a self-supervised fine-tuning approach to improve VLMs for cooperative model-based object detection. Given a cooperative model consists of a closed-set detector and a VLM, we first construct a region-aware pseudo-labeled dataset using a pre-trained closed-set object detector, in which regions corresponding to novel objects may be present but remain unlabeled or mislabeled. We then fine-tune the visual backbone of the VLM in a decoupled manner, which enhances local feature alignment while preserving global semantic knowledge via weight interpolation. DAT is a plug-and-play module that requires no inference overhead and fine-tunes less than 0.8M parameters. Experiments on the COCO and LVIS datasets show that DAT consistently improves detection performance on both novel and known categories, establishing a new state of the art in cooperative open-vocabulary detection.
匹配关键词: self-supervised
---

[ACADEMIC - ARXIV]
标题: Diffusion Masked Pretraining for Dynamic Point Cloud
作者: Zhuoyue Zhang, Jihua Zhu, Chaowei Fang, Jian Liu, Ajmal Saeed Mian
链接: https://arxiv.org/abs/2605.03639v1
完整摘要: Dynamic point cloud pretraining is still dominated by masked reconstruction objectives. However, these objectives inherit two key limitations. Existing methods inject ground-truth tube centers as decoder positional embeddings, causing spatio-temporal positional leakage. Moreover, they supervise inter-frame motion with deterministic proxy targets that systematically discard distributional structure by collapsing multimodal trajectory uncertainty into conditional means. To address these limitations, we propose Diffusion Masked Pretraining (DiMP), a unified self-supervised framework for dynamic point clouds. DiMP introduces diffusion modeling into both positional inference and motion learning. It first applies forward diffusion noise only to masked tube centers, then predicts clean centers from visible spatio-temporal context. This removes positional leakage while preserving visible coordinates as clean temporal anchors. DiMP also reformulates point-wise inter-frame displacement supervision as a DDPM noise-prediction objective conditioned on decoded representations. This design drives the encoder to target the full conditional distribution of plausible motions under a variational surrogate, rather than collapsing to a single deterministic estimate. Extensive experiments demonstrate that DiMP consistently improves downstream accuracy over the backbone alone, with absolute gains of 11.21% on offline action segmentation and 13.65% under causally constrained online inference.Codes are available at https://github.com/InitalZ/DiMP.git.
匹配关键词: self-supervised
---

[ACADEMIC - ARXIV]
标题: Logical Consistency as a Bridge: Improving LLM Hallucination Detection via Label Constraint Modeling between Responses and Self-Judgments
作者: Hao Mi, Qiang Sheng, Shaofei Wang, Beizhe Hu, Yifan Sun, Zhengjia Wang, Hengqi Zeng, Yang Li, Danding Wang, Juan Cao
链接: https://arxiv.org/abs/2605.03971v1
完整摘要: Large Language Models (LLMs) are prone to factual hallucinations, risking their reliability in real-world applications. Existing hallucination detectors mainly extract micro-level intrinsic patterns for uncertainty quantification or elicit macro-level self-judgments through verbalized prompts. However, these methods address only a single facet of the hallucination, focusing either on implicit neural uncertainty or explicit symbolic reasoning, thereby treating these inherently coupled behaviors in isolation and failing to exploit their interdependence for a holistic view. In this paper, we propose LaaB (Logical Consistency-as-a-Bridge), a framework that bridges neural features and symbolic judgments for hallucination detection. LaaB introduces a "meta-judgment" process to map symbolic labels back into the feature space. By leveraging the inherent logical bridge where response and meta-judgment labels are either the same or opposite based on the self-judgment's semantics, LaaB aligns and integrates dual-view signals via mutual learning and enhances the hallucination detection. Extensive experiments on 4 public datasets, across 4 LLMs, against 8 baselines demonstrate the superiority of LaaB.
匹配关键词: contrastive learning
---

[ACADEMIC - ARXIV]
标题: Label-Efficient School Detection from Aerial Imagery via Weakly Supervised Pretraining and Fine-Tuning
作者: Zakarya Elmimouni, Fares Fourati, Mohamed-Slim Alouini
链接: https://arxiv.org/abs/2605.03968v1
完整摘要: Accurate school detection is essential for supporting education initiatives, including infrastructure planning and expanding internet connectivity to underserved areas. However, many regions around the world face challenges due to outdated, incomplete, or unavailable official records. Manual mapping efforts, while valuable, are labor-intensive and lack scalability across large geographic areas. To address this, we propose a weakly supervised framework for school detection from aerial imagery that minimizes the need for human annotations while supporting global mapping efforts. Our method is specifically designed for low-data regimes, where manual annotations are extremely scarce. We introduce an automatic labeling pipeline that leverages sparse location points and semantic segmentation to generate infrastructure masks from which we generate bounding boxes. Using these automatically labeled images, we train our detectors on a first training stage to learn a representation of what schools look like, then using a small set of manually labeled images, we fine-tune the previously trained models on this clean dataset. This two stage training pipeline enables large-scale and strong detection in low-data setting of school infrastructure with minimal supervision. Our results demonstrate strong object detection performance, particularly in the low-data regime, where the models achieve promising results using only 50 manually labeled images, significantly reducing the need for costly annotations. This framework supports education and connectivity initiatives worldwide by providing an efficient and extensible approach to mapping schools from space. All models, training code and auto-labeled data will be publicly released to foster future research and real-world impact.
匹配关键词: contrastive learning
---

[ACADEMIC - ARXIV]
标题: Pretrained Model Representations as Acquisition Signals for Active Learning of MLIPs
作者: Eszter Varga-Umbrich, Shikha Surana, Paul Duckworth, Jules Tilly, Olivier Peltre, Zachary Weller-Davies
链接: https://arxiv.org/abs/2605.03964v1
完整摘要: Training machine learning interatomic potentials (MLIPs) for reactive chemistry is often bottlenecked by the high cost of quantum chemical labels and the scarcity of transition state configurations in candidate pools. Active learning (AL) can mitigate these costs, but its effectiveness hinges on the acquisition rule. We investigate whether the latent space of a pretrained MLIP already contains the information necessary for effective acquisition, eliminating the need for auxiliary uncertainty heads, Bayesian training and fine-tuning, or committee ensembles. We introduce two acquisition signals derived directly from a pretrained MACE potential: a finite-width neural tangent kernel (NTK) and an activation kernel built from hidden latent space features. On reactive-chemistry benchmarks, both kernels consistently outperform fixed-descriptor baselines, committee disagreement, and random acquisition, reducing the data required to reach performance targets by an average of 38% for energy error and 28% for force error. We further show that the pretrained model induces similarity spaces that preserve chemically meaningful structure and provide more reliable residual uncertainty estimates than randomly initialised or fixed-descriptor-based kernels. Our results suggest that pretraining aligns latent-space geometry with model error, yielding a practical and sufficient acquisition signal for reactive MLIP fine-tuning.
匹配关键词: contrastive learning
---

[ACADEMIC - ARXIV]
标题: Transformers with Selective Access to Early Representations
作者: Skye Gunasekaran, Téa Wright, Rui-Jie Zhu, Jason Eshraghian
链接: https://arxiv.org/abs/2605.03953v1
完整摘要: Several recent Transformer architectures expose later layers to representations computed in the earliest layers, motivated by the observation that low-level features can become harder to recover as the residual stream is repeatedly transformed through depth. The cheapest among these methods add static value residuals: learned mixing coefficients that expose the first-layer value projection V_1 uniformly across tokens and heads. More expressive dense or dynamic alternatives recover finer-grained access, but at higher memory cost and lower throughput. The usefulness of V_1 is unlikely to be constant across tokens, heads, and contexts; different positions plausibly require different amounts of access to early lexical or semantic information. We therefore treat early-representation reuse as a retrieval problem rather than a connectivity problem, and introduce Selective Access Transformer (SATFormer), which preserves the first-layer value pathway while controlling access with a context-dependent gate. Across models from 130M to 1.3B parameters, SATFormer consistently improves validation loss and zero-shot accuracy over the static value-residual and Transformer baselines. Its strongest gains appear on retrieval-intensive benchmarks, where it improves over static value residuals by approximately 1.5 average points, while maintaining throughput and memory usage close to the baseline Transformer. Gate analyses suggest sparse, depth-dependent, head-specific, and category-sensitive access patterns, supporting the interpretation that SATFormer learns selective reuse of early representations rather than uniform residual copying. Our code is available at https://github.com/SkyeGunasekaran/SATFormer.
匹配关键词: contrastive learning
---

[ACADEMIC - ARXIV]
标题: Integrating Feature Correlation in Differential Privacy with Applications in DP-ERM
作者: Tianyu Wang, Luhao Zhang, Rachel Cummings
链接: https://arxiv.org/abs/2605.03945v1
完整摘要: Standard differential privacy imposes uniform privacy constraints across all features, overlooking the inherent distinction between sensitive and insensitive features in practice. In this paper, we introduce a relaxed definition of differential privacy that accounts for such heterogeneity, allowing certain features to be treated as insensitive even when correlated with sensitive ones. We propose a correlation-aware framework, $\textsf{CorrDP}$, which relaxes privacy for insensitive features while accounting for their correlations with sensitive features, with the correlations quantified using total variation distance. We design algorithms for differentially private empirical risk minimization (DP-ERM) under the $\textsf{CorrDP}$ framework, incorporating distance-dependent noise into gradients for improved theoretical utility guarantees. When the correlation distance is unknown, we estimate it from the dataset and show that it achieves a comparable privacy-utility guarantee. We perform experiments on synthetic and real-world datasets and show that $\textsf{CorrDP}$-based DP-ERM algorithms consistently outperform the standard DP framework in the presence of insensitive features.
匹配关键词: contrastive learning
---

[ACADEMIC - ARXIV]
标题: Logical Consistency as a Bridge: Improving LLM Hallucination Detection via Label Constraint Modeling between Responses and Self-Judgments
作者: Hao Mi, Qiang Sheng, Shaofei Wang, Beizhe Hu, Yifan Sun, Zhengjia Wang, Hengqi Zeng, Yang Li, Danding Wang, Juan Cao
链接: https://arxiv.org/abs/2605.03971v1
完整摘要: Large Language Models (LLMs) are prone to factual hallucinations, risking their reliability in real-world applications. Existing hallucination detectors mainly extract micro-level intrinsic patterns for uncertainty quantification or elicit macro-level self-judgments through verbalized prompts. However, these methods address only a single facet of the hallucination, focusing either on implicit neural uncertainty or explicit symbolic reasoning, thereby treating these inherently coupled behaviors in isolation and failing to exploit their interdependence for a holistic view. In this paper, we propose LaaB (Logical Consistency-as-a-Bridge), a framework that bridges neural features and symbolic judgments for hallucination detection. LaaB introduces a "meta-judgment" process to map symbolic labels back into the feature space. By leveraging the inherent logical bridge where response and meta-judgment labels are either the same or opposite based on the self-judgment's semantics, LaaB aligns and integrates dual-view signals via mutual learning and enhances the hallucination detection. Extensive experiments on 4 public datasets, across 4 LLMs, against 8 baselines demonstrate the superiority of LaaB.
匹配关键词: representation learning
---

[ACADEMIC - ARXIV]
标题: Label-Efficient School Detection from Aerial Imagery via Weakly Supervised Pretraining and Fine-Tuning
作者: Zakarya Elmimouni, Fares Fourati, Mohamed-Slim Alouini
链接: https://arxiv.org/abs/2605.03968v1
完整摘要: Accurate school detection is essential for supporting education initiatives, including infrastructure planning and expanding internet connectivity to underserved areas. However, many regions around the world face challenges due to outdated, incomplete, or unavailable official records. Manual mapping efforts, while valuable, are labor-intensive and lack scalability across large geographic areas. To address this, we propose a weakly supervised framework for school detection from aerial imagery that minimizes the need for human annotations while supporting global mapping efforts. Our method is specifically designed for low-data regimes, where manual annotations are extremely scarce. We introduce an automatic labeling pipeline that leverages sparse location points and semantic segmentation to generate infrastructure masks from which we generate bounding boxes. Using these automatically labeled images, we train our detectors on a first training stage to learn a representation of what schools look like, then using a small set of manually labeled images, we fine-tune the previously trained models on this clean dataset. This two stage training pipeline enables large-scale and strong detection in low-data setting of school infrastructure with minimal supervision. Our results demonstrate strong object detection performance, particularly in the low-data regime, where the models achieve promising results using only 50 manually labeled images, significantly reducing the need for costly annotations. This framework supports education and connectivity initiatives worldwide by providing an efficient and extensible approach to mapping schools from space. All models, training code and auto-labeled data will be publicly released to foster future research and real-world impact.
匹配关键词: representation learning
---

[ACADEMIC - ARXIV]
标题: Pretrained Model Representations as Acquisition Signals for Active Learning of MLIPs
作者: Eszter Varga-Umbrich, Shikha Surana, Paul Duckworth, Jules Tilly, Olivier Peltre, Zachary Weller-Davies
链接: https://arxiv.org/abs/2605.03964v1
完整摘要: Training machine learning interatomic potentials (MLIPs) for reactive chemistry is often bottlenecked by the high cost of quantum chemical labels and the scarcity of transition state configurations in candidate pools. Active learning (AL) can mitigate these costs, but its effectiveness hinges on the acquisition rule. We investigate whether the latent space of a pretrained MLIP already contains the information necessary for effective acquisition, eliminating the need for auxiliary uncertainty heads, Bayesian training and fine-tuning, or committee ensembles. We introduce two acquisition signals derived directly from a pretrained MACE potential: a finite-width neural tangent kernel (NTK) and an activation kernel built from hidden latent space features. On reactive-chemistry benchmarks, both kernels consistently outperform fixed-descriptor baselines, committee disagreement, and random acquisition, reducing the data required to reach performance targets by an average of 38% for energy error and 28% for force error. We further show that the pretrained model induces similarity spaces that preserve chemically meaningful structure and provide more reliable residual uncertainty estimates than randomly initialised or fixed-descriptor-based kernels. Our results suggest that pretraining aligns latent-space geometry with model error, yielding a practical and sufficient acquisition signal for reactive MLIP fine-tuning.
匹配关键词: representation learning
---

[ACADEMIC - ARXIV]
标题: Transformers with Selective Access to Early Representations
作者: Skye Gunasekaran, Téa Wright, Rui-Jie Zhu, Jason Eshraghian
链接: https://arxiv.org/abs/2605.03953v1
完整摘要: Several recent Transformer architectures expose later layers to representations computed in the earliest layers, motivated by the observation that low-level features can become harder to recover as the residual stream is repeatedly transformed through depth. The cheapest among these methods add static value residuals: learned mixing coefficients that expose the first-layer value projection V_1 uniformly across tokens and heads. More expressive dense or dynamic alternatives recover finer-grained access, but at higher memory cost and lower throughput. The usefulness of V_1 is unlikely to be constant across tokens, heads, and contexts; different positions plausibly require different amounts of access to early lexical or semantic information. We therefore treat early-representation reuse as a retrieval problem rather than a connectivity problem, and introduce Selective Access Transformer (SATFormer), which preserves the first-layer value pathway while controlling access with a context-dependent gate. Across models from 130M to 1.3B parameters, SATFormer consistently improves validation loss and zero-shot accuracy over the static value-residual and Transformer baselines. Its strongest gains appear on retrieval-intensive benchmarks, where it improves over static value residuals by approximately 1.5 average points, while maintaining throughput and memory usage close to the baseline Transformer. Gate analyses suggest sparse, depth-dependent, head-specific, and category-sensitive access patterns, supporting the interpretation that SATFormer learns selective reuse of early representations rather than uniform residual copying. Our code is available at https://github.com/SkyeGunasekaran/SATFormer.
匹配关键词: representation learning
---

[ACADEMIC - ARXIV]
标题: Integrating Feature Correlation in Differential Privacy with Applications in DP-ERM
作者: Tianyu Wang, Luhao Zhang, Rachel Cummings
链接: https://arxiv.org/abs/2605.03945v1
完整摘要: Standard differential privacy imposes uniform privacy constraints across all features, overlooking the inherent distinction between sensitive and insensitive features in practice. In this paper, we introduce a relaxed definition of differential privacy that accounts for such heterogeneity, allowing certain features to be treated as insensitive even when correlated with sensitive ones. We propose a correlation-aware framework, $\textsf{CorrDP}$, which relaxes privacy for insensitive features while accounting for their correlations with sensitive features, with the correlations quantified using total variation distance. We design algorithms for differentially private empirical risk minimization (DP-ERM) under the $\textsf{CorrDP}$ framework, incorporating distance-dependent noise into gradients for improved theoretical utility guarantees. When the correlation distance is unknown, we estimate it from the dataset and show that it achieves a comparable privacy-utility guarantee. We perform experiments on synthetic and real-world datasets and show that $\textsf{CorrDP}$-based DP-ERM algorithms consistently outperform the standard DP framework in the presence of insensitive features.
匹配关键词: representation learning
---

[ACADEMIC - ARXIV]
标题: Logical Consistency as a Bridge: Improving LLM Hallucination Detection via Label Constraint Modeling between Responses and Self-Judgments
作者: Hao Mi, Qiang Sheng, Shaofei Wang, Beizhe Hu, Yifan Sun, Zhengjia Wang, Hengqi Zeng, Yang Li, Danding Wang, Juan Cao
链接: https://arxiv.org/abs/2605.03971v1
完整摘要: Large Language Models (LLMs) are prone to factual hallucinations, risking their reliability in real-world applications. Existing hallucination detectors mainly extract micro-level intrinsic patterns for uncertainty quantification or elicit macro-level self-judgments through verbalized prompts. However, these methods address only a single facet of the hallucination, focusing either on implicit neural uncertainty or explicit symbolic reasoning, thereby treating these inherently coupled behaviors in isolation and failing to exploit their interdependence for a holistic view. In this paper, we propose LaaB (Logical Consistency-as-a-Bridge), a framework that bridges neural features and symbolic judgments for hallucination detection. LaaB introduces a "meta-judgment" process to map symbolic labels back into the feature space. By leveraging the inherent logical bridge where response and meta-judgment labels are either the same or opposite based on the self-judgment's semantics, LaaB aligns and integrates dual-view signals via mutual learning and enhances the hallucination detection. Extensive experiments on 4 public datasets, across 4 LLMs, against 8 baselines demonstrate the superiority of LaaB.
匹配关键词: masked language model
---

[ACADEMIC - ARXIV]
标题: Feature-Augmented Transformers for Robust AI-Text Detection Across Domains and Generators
作者: Mohamed Mady, Johannes Reschke, Björn Schuller
链接: https://arxiv.org/abs/2605.03969v1
完整摘要: AI-generated text is nowadays produced at scale across domains and heterogeneous generation pipelines, making robustness to distribution shift a central requirement for supervised binary detectors. We train transformer-based detectors on HC3 PLUS and calibrate a single decision threshold by maximising balanced accuracy on held-out validation; this threshold is then kept fixed for all downstream test distributions, revealing domain- and generator-dependent error asymmetries under shift. We evaluate in-domain on HC3 PLUS, under cross-dataset transfer to the multi-domain, multi-generator M4 benchmark, and on the external AI-Text-Detection-Pile. Although base models achieve near-ceiling in-domain performance (up to 99.5% balanced accuracy), performance under shift is brittle and strongly model-dependent. Feature augmentation via attention-based linguistic feature fusion improves transfer, with our best model (DeBERTa-v3-base+FeatAttn) achieving 85.9% balanced accuracy on M4. Multi-seed experiments confirm high stability. Under the same fixed-threshold protocol, our model outperforms strong zero-shot baselines by up to +7.22 points. Category-level ablations further show that readability and vocabulary features contribute most to robustness under shift. Overall, these results demonstrate that feature augmentation and a modern DeBERTa backbone significantly outperform earlier BERT/RoBERTa models, while the fixed-threshold protocol provides a more realistic and informative assessment of practical detector robustness.
匹配关键词: masked language model
---

[ACADEMIC - ARXIV]
标题: Label-Efficient School Detection from Aerial Imagery via Weakly Supervised Pretraining and Fine-Tuning
作者: Zakarya Elmimouni, Fares Fourati, Mohamed-Slim Alouini
链接: https://arxiv.org/abs/2605.03968v1
完整摘要: Accurate school detection is essential for supporting education initiatives, including infrastructure planning and expanding internet connectivity to underserved areas. However, many regions around the world face challenges due to outdated, incomplete, or unavailable official records. Manual mapping efforts, while valuable, are labor-intensive and lack scalability across large geographic areas. To address this, we propose a weakly supervised framework for school detection from aerial imagery that minimizes the need for human annotations while supporting global mapping efforts. Our method is specifically designed for low-data regimes, where manual annotations are extremely scarce. We introduce an automatic labeling pipeline that leverages sparse location points and semantic segmentation to generate infrastructure masks from which we generate bounding boxes. Using these automatically labeled images, we train our detectors on a first training stage to learn a representation of what schools look like, then using a small set of manually labeled images, we fine-tune the previously trained models on this clean dataset. This two stage training pipeline enables large-scale and strong detection in low-data setting of school infrastructure with minimal supervision. Our results demonstrate strong object detection performance, particularly in the low-data regime, where the models achieve promising results using only 50 manually labeled images, significantly reducing the need for costly annotations. This framework supports education and connectivity initiatives worldwide by providing an efficient and extensible approach to mapping schools from space. All models, training code and auto-labeled data will be publicly released to foster future research and real-world impact.
匹配关键词: masked language model
---

[ACADEMIC - ARXIV]
标题: Pretrained Model Representations as Acquisition Signals for Active Learning of MLIPs
作者: Eszter Varga-Umbrich, Shikha Surana, Paul Duckworth, Jules Tilly, Olivier Peltre, Zachary Weller-Davies
链接: https://arxiv.org/abs/2605.03964v1
完整摘要: Training machine learning interatomic potentials (MLIPs) for reactive chemistry is often bottlenecked by the high cost of quantum chemical labels and the scarcity of transition state configurations in candidate pools. Active learning (AL) can mitigate these costs, but its effectiveness hinges on the acquisition rule. We investigate whether the latent space of a pretrained MLIP already contains the information necessary for effective acquisition, eliminating the need for auxiliary uncertainty heads, Bayesian training and fine-tuning, or committee ensembles. We introduce two acquisition signals derived directly from a pretrained MACE potential: a finite-width neural tangent kernel (NTK) and an activation kernel built from hidden latent space features. On reactive-chemistry benchmarks, both kernels consistently outperform fixed-descriptor baselines, committee disagreement, and random acquisition, reducing the data required to reach performance targets by an average of 38% for energy error and 28% for force error. We further show that the pretrained model induces similarity spaces that preserve chemically meaningful structure and provide more reliable residual uncertainty estimates than randomly initialised or fixed-descriptor-based kernels. Our results suggest that pretraining aligns latent-space geometry with model error, yielding a practical and sufficient acquisition signal for reactive MLIP fine-tuning.
匹配关键词: masked language model
---

[ACADEMIC - ARXIV]
标题: Transformers with Selective Access to Early Representations
作者: Skye Gunasekaran, Téa Wright, Rui-Jie Zhu, Jason Eshraghian
链接: https://arxiv.org/abs/2605.03953v1
完整摘要: Several recent Transformer architectures expose later layers to representations computed in the earliest layers, motivated by the observation that low-level features can become harder to recover as the residual stream is repeatedly transformed through depth. The cheapest among these methods add static value residuals: learned mixing coefficients that expose the first-layer value projection V_1 uniformly across tokens and heads. More expressive dense or dynamic alternatives recover finer-grained access, but at higher memory cost and lower throughput. The usefulness of V_1 is unlikely to be constant across tokens, heads, and contexts; different positions plausibly require different amounts of access to early lexical or semantic information. We therefore treat early-representation reuse as a retrieval problem rather than a connectivity problem, and introduce Selective Access Transformer (SATFormer), which preserves the first-layer value pathway while controlling access with a context-dependent gate. Across models from 130M to 1.3B parameters, SATFormer consistently improves validation loss and zero-shot accuracy over the static value-residual and Transformer baselines. Its strongest gains appear on retrieval-intensive benchmarks, where it improves over static value residuals by approximately 1.5 average points, while maintaining throughput and memory usage close to the baseline Transformer. Gate analyses suggest sparse, depth-dependent, head-specific, and category-sensitive access patterns, supporting the interpretation that SATFormer learns selective reuse of early representations rather than uniform residual copying. Our code is available at https://github.com/SkyeGunasekaran/SATFormer.
匹配关键词: masked language model
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
标题: Automated Diabetic Screening via Anterior Segment Ocular Imaging: A Deep Learning and Explainable AI Approach
作者: Hasaan Maqsood, Saif Ur Rehman Khan, Sebastian Vollmer, Andreas Dengel, Muhammad Nabeel Asim
链接: https://arxiv.org/abs/2603.14727v1
完整摘要: Diabetic retinopathy screening traditionally relies on fundus photography, requiring specialized equipment and expertise often unavailable in primary care and resource limited settings. We developed and validated a deep learning (DL) system for automated diabetic classification using anterior segment ocular imaging a readily accessible alternative utilizing standard photography equipment. The system leverages visible biomarkers in the iris, sclera, and conjunctiva that correlate with systemic diabetic status. We systematically evaluated five contemporary architectures (EfficientNet-V2-S with self-supervised learning (SSL), Vision Transformer, Swin Transformer, ConvNeXt-Base, and ResNet-50) on 2,640 clinically annotated anterior segment images spanning Normal, Controlled Diabetic, and Uncontrolled Diabetic categories. A tailored preprocessing pipeline combining specular reflection mitigation and contrast limited adaptive histogram equalization (CLAHE) was implemented to enhance subtle vascular and textural patterns critical for classification. SSL using SimCLR on domain specific ocular images substantially improved model performance.EfficientNet-V2-S with SSL achieved optimal performance with an F1-score of 98.21%, precision of 97.90%, and recall of 98.55% a substantial improvement over ImageNet only initialization (94.63% F1). Notably, the model attained near perfect precision (100%) for Normal classification, critical for minimizing unnecessary clinical referrals.
匹配关键词: SimCLR
---

[ACADEMIC - ARXIV]
标题: Stream-R1: Reliability-Perplexity Aware Reward Distillation for Streaming Video Generation
作者: Bin Wu, Mengqi Huang, Shaojin Wu, Weinan Jia, Yuxin Wang, Zhendong Mao, Yongdong Zhang
链接: https://arxiv.org/abs/2605.03849v1
完整摘要: Distillation-based acceleration has become foundational for making autoregressive streaming video diffusion models practical, with distribution matching distillation (DMD) as the de facto choice. Existing methods, however, train the student to match the teacher's output indiscriminately, treating every rollout, frame, and pixel as equally reliable supervision. We argue that this caps distilled quality, since it overlooks two complementary axes of variance in DMD supervision: Inter-Reliability across student rollouts whose supervision varies in reliability, and Intra-Perplexity across spatial regions and temporal frames that contribute unequally to where quality can still be improved. The objective thus conflates two questions under a uniform weight: whether to learn from each rollout, and where to concentrate optimization within it. To address this, we propose Stream-R1, a Reliability-Perplexity Aware Reward Distillation framework that adaptively reweights the distillation objective at both rollout and spatiotemporal-element levels through a single shared reward-guided mechanism. At the Inter-Reliability level, Stream-R1 rescales each rollout's loss by an exponential of a pretrained video reward score, so that rollouts with reliable supervision dominate optimization. At the Intra-Perplexity level, it back-propagates the same reward model to extract per-pixel gradient saliency, which is factored into spatial and temporal weights that concentrate optimization pressure on regions and frames where refinement yields the largest expected gain. An adaptive balancing mechanism prevents any single quality axis from dominating across visual quality, motion quality, and text alignment. Stream-R1 attains consistent improvements on all three dimensions over distillation baselines on standard streaming video generation benchmarks, without architectural modification or additional inference cost.
匹配关键词: MAE
---

[ACADEMIC - ARXIV]
标题: What You Think is What You See: Driving Exploration in VLM Agents via Visual-Linguistic Curiosity
作者: Haoxi Li, Qinglin Hou, Jianfei Ma, Jinxiang Lai, Tao Han, Sikai Bai, Jingcai Guo, Jie Zhang, Song Guo
链接: https://arxiv.org/abs/2605.03782v1
完整摘要: To navigate partially observable visual environments, recent VLM agents increasingly internalize world modeling capabilities into their policies via explicit CoT reasoning, enabling them to mentally simulate futures before acting. However, relying solely on passive reasoning over visited states is insufficient for sparse-reward tasks, as it lacks the epistemic drive to actively uncover the ``known unknown'' required for robust generalization. We ask: Can VLM agents actively find signals that challenge and refine their internal world model through curiosity-driven exploration? In this work, we propose GLANCE, a unified framework that bridges reasoning and exploration by grounding the agent's linguistic world model into the stable visual representations of an evolving target network. Crucially, GLANCE leverages the discrepancy between linguistic prediction and visual reality as an intrinsic curiosity signal within reinforcement learning, steering the agent to actively explore areas where its internal model is uncertain. Extensive experiments across a series of agentic tasks show the effectiveness of GLANCE, and demonstrate that aligning ``what the agent thinks'' with ``what the agent sees'' is key to solving complex or sparse agentic tasks.
匹配关键词: MAE
---

[ACADEMIC - ARXIV]
标题: OracleProto: A Reproducible Framework for Benchmarking LLM Native Forecasting via Knowledge Cutoff and Temporal Masking
作者: Yiding Ma, Chengyun Ruan, Kaibo Huang, Zhongliang Yang, Linna Zhou
链接: https://arxiv.org/abs/2605.03762v1
完整摘要: Large language models are moving from static text generators toward real-world decision-support systems, where forecasting is a composite capability that links information gathering, evidence integration, situational judgment, and action-oriented decision making. This capability is in broad demand across finance, policy, industry, and scientific research, yet its evaluation remains difficult: live benchmarks evaluate forecasts before answers exist, making them the cleanest way to measure forecasting ability, but they expire once events resolve; retrospective benchmarks are reproducible, but they cannot reliably distinguish genuine forecasting from facts a model may have already learned during pretraining. Prompting models to "pretend not to know" cannot replace a genuine knowledge boundary. We propose OracleProto, a reproducible framework for evaluating LLM native forecasting capability. OracleProto reconstructs resolved events into time-bounded forecasting samples by combining model-cutoff-aligned sample admission, tool-level temporal masking, content-level leakage detection, discrete answer normalization, and hierarchical scoring. Instantiated on a FutureX-Past-derived dataset with six contemporary LLMs, OracleProto distinguishes forecasting quality, sampling stability, and cost efficiency under controlled information boundaries, while reducing residual leakage to the $1\%$ level, an order of magnitude below tool-only temporal filtering. OracleProto turns LLM forecasting from one-off evaluation into an auditable, reusable, and trainable dataset-level capability, providing a unified interface for fair cross-model comparison and a controlled signal source for downstream SFT and RL. Code and data are available at https://github.com/MaYiding/OracleProto and https://huggingface.co/datasets/MaYiding/OracleProto.
匹配关键词: MAE
---

[ACADEMIC - ARXIV]
标题: Bridging the Embodiment Gap: Disentangled Cross-Embodiment Video Editing
作者: Zhiyuan Li, Wenyan Yang, Wenshuai Zhao, Yue Ma, Yuanpeng Tu, Pekka Marttinen, Joni Pajarinen
链接: https://arxiv.org/abs/2605.03637v1
完整摘要: Learning robotic manipulation from human videos is a promising solution to the data bottleneck in robotics, but the distribution shift between humans and robots remains a critical challenge. Existing approaches often produce entangled representations, where task-relevant information is coupled with human-specific kinematics, limiting their adaptability. We propose a generative framework for cross-embodiment video editing that directly addresses this by learning explicitly disentangled task and embodiment representations. Our method factorizes a demonstration video into two orthogonal latent spaces by enforcing a dual contrastive objective: it minimizes mutual information between the spaces to ensure independence while maximizing intra-space consistency to create stable representations. A parameter-efficient adapter injects these latent codes into a frozen video diffusion model, enabling the synthesis of a coherent robot execution video from a single human demonstration, without requiring paired cross-embodiment data. Experiments show our approach generates temporally consistent and morphologically accurate robot demonstrations, offering a scalable solution to leverage internet-scale human video for robot learning.
匹配关键词: MAE
---

[ACADEMIC - ARXIV]
标题: ProgramBench: Can Language Models Rebuild Programs From Scratch?
作者: John Yang, Kilian Lieret, Jeffrey Ma, Parth Thakkar, Dmitrii Pedchenko, Sten Sootla, Emily McMilin, Pengcheng Yin, Rui Hou, Gabriel Synnaeve, Diyi Yang, Ofir Press
链接: https://arxiv.org/abs/2605.03546v1
完整摘要: Turning ideas into full software projects from scratch has become a popular use case for language models. Agents are being deployed to seed, maintain, and grow codebases over extended periods with minimal human oversight. Such settings require models to make high-level software architecture decisions. However, existing benchmarks measure focused, limited tasks such as fixing a single bug or developing a single, specified feature. We therefore introduce ProgramBench to measure the ability of software engineering agents to develop software holisitically. In ProgramBench, given only a program and its documentation, agents must architect and implement a codebase that matches the reference executable's behavior. End-to-end behavioral tests are generated via agent-driven fuzzing, enabling evaluation without prescribing implementation structure. Our 200 tasks range from compact CLI tools to widely used software such as FFmpeg, SQLite, and the PHP interpreter. We evaluate 9 LMs and find that none fully resolve any task, with the best model passing 95\% of tests on only 3\% of tasks. Models favor monolithic, single-file implementations that diverge sharply from human-written code.
匹配关键词: MAE
---

[ACADEMIC - ARXIV]
标题: Logical Consistency as a Bridge: Improving LLM Hallucination Detection via Label Constraint Modeling between Responses and Self-Judgments
作者: Hao Mi, Qiang Sheng, Shaofei Wang, Beizhe Hu, Yifan Sun, Zhengjia Wang, Hengqi Zeng, Yang Li, Danding Wang, Juan Cao
链接: https://arxiv.org/abs/2605.03971v1
完整摘要: Large Language Models (LLMs) are prone to factual hallucinations, risking their reliability in real-world applications. Existing hallucination detectors mainly extract micro-level intrinsic patterns for uncertainty quantification or elicit macro-level self-judgments through verbalized prompts. However, these methods address only a single facet of the hallucination, focusing either on implicit neural uncertainty or explicit symbolic reasoning, thereby treating these inherently coupled behaviors in isolation and failing to exploit their interdependence for a holistic view. In this paper, we propose LaaB (Logical Consistency-as-a-Bridge), a framework that bridges neural features and symbolic judgments for hallucination detection. LaaB introduces a "meta-judgment" process to map symbolic labels back into the feature space. By leveraging the inherent logical bridge where response and meta-judgment labels are either the same or opposite based on the self-judgment's semantics, LaaB aligns and integrates dual-view signals via mutual learning and enhances the hallucination detection. Extensive experiments on 4 public datasets, across 4 LLMs, against 8 baselines demonstrate the superiority of LaaB.
匹配关键词: generative model
---

[ACADEMIC - ARXIV]
标题: Feature-Augmented Transformers for Robust AI-Text Detection Across Domains and Generators
作者: Mohamed Mady, Johannes Reschke, Björn Schuller
链接: https://arxiv.org/abs/2605.03969v1
完整摘要: AI-generated text is nowadays produced at scale across domains and heterogeneous generation pipelines, making robustness to distribution shift a central requirement for supervised binary detectors. We train transformer-based detectors on HC3 PLUS and calibrate a single decision threshold by maximising balanced accuracy on held-out validation; this threshold is then kept fixed for all downstream test distributions, revealing domain- and generator-dependent error asymmetries under shift. We evaluate in-domain on HC3 PLUS, under cross-dataset transfer to the multi-domain, multi-generator M4 benchmark, and on the external AI-Text-Detection-Pile. Although base models achieve near-ceiling in-domain performance (up to 99.5% balanced accuracy), performance under shift is brittle and strongly model-dependent. Feature augmentation via attention-based linguistic feature fusion improves transfer, with our best model (DeBERTa-v3-base+FeatAttn) achieving 85.9% balanced accuracy on M4. Multi-seed experiments confirm high stability. Under the same fixed-threshold protocol, our model outperforms strong zero-shot baselines by up to +7.22 points. Category-level ablations further show that readability and vocabulary features contribute most to robustness under shift. Overall, these results demonstrate that feature augmentation and a modern DeBERTa backbone significantly outperform earlier BERT/RoBERTa models, while the fixed-threshold protocol provides a more realistic and informative assessment of practical detector robustness.
匹配关键词: generative model
---

[ACADEMIC - ARXIV]
标题: Label-Efficient School Detection from Aerial Imagery via Weakly Supervised Pretraining and Fine-Tuning
作者: Zakarya Elmimouni, Fares Fourati, Mohamed-Slim Alouini
链接: https://arxiv.org/abs/2605.03968v1
完整摘要: Accurate school detection is essential for supporting education initiatives, including infrastructure planning and expanding internet connectivity to underserved areas. However, many regions around the world face challenges due to outdated, incomplete, or unavailable official records. Manual mapping efforts, while valuable, are labor-intensive and lack scalability across large geographic areas. To address this, we propose a weakly supervised framework for school detection from aerial imagery that minimizes the need for human annotations while supporting global mapping efforts. Our method is specifically designed for low-data regimes, where manual annotations are extremely scarce. We introduce an automatic labeling pipeline that leverages sparse location points and semantic segmentation to generate infrastructure masks from which we generate bounding boxes. Using these automatically labeled images, we train our detectors on a first training stage to learn a representation of what schools look like, then using a small set of manually labeled images, we fine-tune the previously trained models on this clean dataset. This two stage training pipeline enables large-scale and strong detection in low-data setting of school infrastructure with minimal supervision. Our results demonstrate strong object detection performance, particularly in the low-data regime, where the models achieve promising results using only 50 manually labeled images, significantly reducing the need for costly annotations. This framework supports education and connectivity initiatives worldwide by providing an efficient and extensible approach to mapping schools from space. All models, training code and auto-labeled data will be publicly released to foster future research and real-world impact.
匹配关键词: generative model
---

[ACADEMIC - ARXIV]
标题: Pretrained Model Representations as Acquisition Signals for Active Learning of MLIPs
作者: Eszter Varga-Umbrich, Shikha Surana, Paul Duckworth, Jules Tilly, Olivier Peltre, Zachary Weller-Davies
链接: https://arxiv.org/abs/2605.03964v1
完整摘要: Training machine learning interatomic potentials (MLIPs) for reactive chemistry is often bottlenecked by the high cost of quantum chemical labels and the scarcity of transition state configurations in candidate pools. Active learning (AL) can mitigate these costs, but its effectiveness hinges on the acquisition rule. We investigate whether the latent space of a pretrained MLIP already contains the information necessary for effective acquisition, eliminating the need for auxiliary uncertainty heads, Bayesian training and fine-tuning, or committee ensembles. We introduce two acquisition signals derived directly from a pretrained MACE potential: a finite-width neural tangent kernel (NTK) and an activation kernel built from hidden latent space features. On reactive-chemistry benchmarks, both kernels consistently outperform fixed-descriptor baselines, committee disagreement, and random acquisition, reducing the data required to reach performance targets by an average of 38% for energy error and 28% for force error. We further show that the pretrained model induces similarity spaces that preserve chemically meaningful structure and provide more reliable residual uncertainty estimates than randomly initialised or fixed-descriptor-based kernels. Our results suggest that pretraining aligns latent-space geometry with model error, yielding a practical and sufficient acquisition signal for reactive MLIP fine-tuning.
匹配关键词: generative model
---

[ACADEMIC - ARXIV]
标题: Inconsistent Databases and Argumentation Frameworks with Collective Attacks
作者: Yasir Mahmood, Jonni Virtema, Timon Barlag, Axel-Cyrille Ngonga Ngomo
链接: https://arxiv.org/abs/2605.03954v1
完整摘要: The connection between subset-maximal repairs for inconsistent databases involving various integrity constraints and acceptable sets of arguments within argumentation frameworks has recently drawn growing interest. In this paper, we contribute to this domain by establishing a new connection when integrity constraints (ICs) include denial constraints and local-as-view tuple-generating dependencies. It turns out that SET-based Argumentation Frameworks (SETAFs), an extension of Dung's argumentation frameworks (AFs) allowing collective attacks, are needed. It is known that subset-maximal repairs under denial constraints correspond to the naive extensions, which also coincide with the preferred and stable extensions in the resulting SETAFs. Our main findings establish that repairs under the considered fragment of tuple-generating dependencies correspond to the preferred extensions. Moreover, for these dependencies, additional preprocessing allows computing a unique extension that is stable and naive. Allowing both types of constraints breaks this relationship, and even the pre-processing does not help as only preferred semantics captures these repairs. Finally, while it is known that functional dependencies do not require set-based attacks, we prove the same regarding inclusion dependencies. Thus, one can translate inconsistent databases under these restricted classes of ICs to plain AFs with attacks only between arguments.
匹配关键词: generative model
---

[ACADEMIC - ARXIV]
标题: Logical Consistency as a Bridge: Improving LLM Hallucination Detection via Label Constraint Modeling between Responses and Self-Judgments
作者: Hao Mi, Qiang Sheng, Shaofei Wang, Beizhe Hu, Yifan Sun, Zhengjia Wang, Hengqi Zeng, Yang Li, Danding Wang, Juan Cao
链接: https://arxiv.org/abs/2605.03971v1
完整摘要: Large Language Models (LLMs) are prone to factual hallucinations, risking their reliability in real-world applications. Existing hallucination detectors mainly extract micro-level intrinsic patterns for uncertainty quantification or elicit macro-level self-judgments through verbalized prompts. However, these methods address only a single facet of the hallucination, focusing either on implicit neural uncertainty or explicit symbolic reasoning, thereby treating these inherently coupled behaviors in isolation and failing to exploit their interdependence for a holistic view. In this paper, we propose LaaB (Logical Consistency-as-a-Bridge), a framework that bridges neural features and symbolic judgments for hallucination detection. LaaB introduces a "meta-judgment" process to map symbolic labels back into the feature space. By leveraging the inherent logical bridge where response and meta-judgment labels are either the same or opposite based on the self-judgment's semantics, LaaB aligns and integrates dual-view signals via mutual learning and enhances the hallucination detection. Extensive experiments on 4 public datasets, across 4 LLMs, against 8 baselines demonstrate the superiority of LaaB.
匹配关键词: diffusion model
---

[ACADEMIC - ARXIV]
标题: Feature-Augmented Transformers for Robust AI-Text Detection Across Domains and Generators
作者: Mohamed Mady, Johannes Reschke, Björn Schuller
链接: https://arxiv.org/abs/2605.03969v1
完整摘要: AI-generated text is nowadays produced at scale across domains and heterogeneous generation pipelines, making robustness to distribution shift a central requirement for supervised binary detectors. We train transformer-based detectors on HC3 PLUS and calibrate a single decision threshold by maximising balanced accuracy on held-out validation; this threshold is then kept fixed for all downstream test distributions, revealing domain- and generator-dependent error asymmetries under shift. We evaluate in-domain on HC3 PLUS, under cross-dataset transfer to the multi-domain, multi-generator M4 benchmark, and on the external AI-Text-Detection-Pile. Although base models achieve near-ceiling in-domain performance (up to 99.5% balanced accuracy), performance under shift is brittle and strongly model-dependent. Feature augmentation via attention-based linguistic feature fusion improves transfer, with our best model (DeBERTa-v3-base+FeatAttn) achieving 85.9% balanced accuracy on M4. Multi-seed experiments confirm high stability. Under the same fixed-threshold protocol, our model outperforms strong zero-shot baselines by up to +7.22 points. Category-level ablations further show that readability and vocabulary features contribute most to robustness under shift. Overall, these results demonstrate that feature augmentation and a modern DeBERTa backbone significantly outperform earlier BERT/RoBERTa models, while the fixed-threshold protocol provides a more realistic and informative assessment of practical detector robustness.
匹配关键词: diffusion model
---

[ACADEMIC - ARXIV]
标题: Label-Efficient School Detection from Aerial Imagery via Weakly Supervised Pretraining and Fine-Tuning
作者: Zakarya Elmimouni, Fares Fourati, Mohamed-Slim Alouini
链接: https://arxiv.org/abs/2605.03968v1
完整摘要: Accurate school detection is essential for supporting education initiatives, including infrastructure planning and expanding internet connectivity to underserved areas. However, many regions around the world face challenges due to outdated, incomplete, or unavailable official records. Manual mapping efforts, while valuable, are labor-intensive and lack scalability across large geographic areas. To address this, we propose a weakly supervised framework for school detection from aerial imagery that minimizes the need for human annotations while supporting global mapping efforts. Our method is specifically designed for low-data regimes, where manual annotations are extremely scarce. We introduce an automatic labeling pipeline that leverages sparse location points and semantic segmentation to generate infrastructure masks from which we generate bounding boxes. Using these automatically labeled images, we train our detectors on a first training stage to learn a representation of what schools look like, then using a small set of manually labeled images, we fine-tune the previously trained models on this clean dataset. This two stage training pipeline enables large-scale and strong detection in low-data setting of school infrastructure with minimal supervision. Our results demonstrate strong object detection performance, particularly in the low-data regime, where the models achieve promising results using only 50 manually labeled images, significantly reducing the need for costly annotations. This framework supports education and connectivity initiatives worldwide by providing an efficient and extensible approach to mapping schools from space. All models, training code and auto-labeled data will be publicly released to foster future research and real-world impact.
匹配关键词: diffusion model
---

[ACADEMIC - ARXIV]
标题: Pretrained Model Representations as Acquisition Signals for Active Learning of MLIPs
作者: Eszter Varga-Umbrich, Shikha Surana, Paul Duckworth, Jules Tilly, Olivier Peltre, Zachary Weller-Davies
链接: https://arxiv.org/abs/2605.03964v1
完整摘要: Training machine learning interatomic potentials (MLIPs) for reactive chemistry is often bottlenecked by the high cost of quantum chemical labels and the scarcity of transition state configurations in candidate pools. Active learning (AL) can mitigate these costs, but its effectiveness hinges on the acquisition rule. We investigate whether the latent space of a pretrained MLIP already contains the information necessary for effective acquisition, eliminating the need for auxiliary uncertainty heads, Bayesian training and fine-tuning, or committee ensembles. We introduce two acquisition signals derived directly from a pretrained MACE potential: a finite-width neural tangent kernel (NTK) and an activation kernel built from hidden latent space features. On reactive-chemistry benchmarks, both kernels consistently outperform fixed-descriptor baselines, committee disagreement, and random acquisition, reducing the data required to reach performance targets by an average of 38% for energy error and 28% for force error. We further show that the pretrained model induces similarity spaces that preserve chemically meaningful structure and provide more reliable residual uncertainty estimates than randomly initialised or fixed-descriptor-based kernels. Our results suggest that pretraining aligns latent-space geometry with model error, yielding a practical and sufficient acquisition signal for reactive MLIP fine-tuning.
匹配关键词: diffusion model
---

[ACADEMIC - ARXIV]
标题: Transformers with Selective Access to Early Representations
作者: Skye Gunasekaran, Téa Wright, Rui-Jie Zhu, Jason Eshraghian
链接: https://arxiv.org/abs/2605.03953v1
完整摘要: Several recent Transformer architectures expose later layers to representations computed in the earliest layers, motivated by the observation that low-level features can become harder to recover as the residual stream is repeatedly transformed through depth. The cheapest among these methods add static value residuals: learned mixing coefficients that expose the first-layer value projection V_1 uniformly across tokens and heads. More expressive dense or dynamic alternatives recover finer-grained access, but at higher memory cost and lower throughput. The usefulness of V_1 is unlikely to be constant across tokens, heads, and contexts; different positions plausibly require different amounts of access to early lexical or semantic information. We therefore treat early-representation reuse as a retrieval problem rather than a connectivity problem, and introduce Selective Access Transformer (SATFormer), which preserves the first-layer value pathway while controlling access with a context-dependent gate. Across models from 130M to 1.3B parameters, SATFormer consistently improves validation loss and zero-shot accuracy over the static value-residual and Transformer baselines. Its strongest gains appear on retrieval-intensive benchmarks, where it improves over static value residuals by approximately 1.5 average points, while maintaining throughput and memory usage close to the baseline Transformer. Gate analyses suggest sparse, depth-dependent, head-specific, and category-sensitive access patterns, supporting the interpretation that SATFormer learns selective reuse of early representations rather than uniform residual copying. Our code is available at https://github.com/SkyeGunasekaran/SATFormer.
匹配关键词: diffusion model
---

[ACADEMIC - ARXIV]
标题: SAM-NER: Semantic Archetype Mediation for Zero-Shot Named Entity Recognition
作者: Ruichu Cai, Juntao Gan, Miao Mai, Zhifeng Hao, Boyan Xu
链接: https://arxiv.org/abs/2605.03706v1
完整摘要: Zero-shot Named Entity Recognition (ZS-NER) remains brittle under domain and schema shifts, where unseen label definitions often misalign with a large language model's (LLM's) intrinsic semantic organization. As a result, directly mapping entity mentions to fine-grained target labels can induce systematic semantic drift, especially when target schemas are novel or semantically overlapping. We propose \textbf{SAM-NER}, a three-stage framework based on \emph{Semantic Archetype Mediation} that stabilizes cross-domain transfer through an intermediate, domain-invariant archetype space. SAM-NER: (i) performs \emph{Entity Discovery} via cooperative extraction and consensus-based denoising to obtain high-coverage, high-fidelity entity spans; (ii) conducts \emph{Abstract Mediation} by projecting entities into a compact set of universal semantic archetypes distilled from high-level ontological abstractions; and (iii) applies \emph{Semantic Calibration} to resolve archetype-level predictions into target-domain types through constrained, definition-aligned inference with a frozen LLM. Experiments on the CrossNER benchmark show that SAM-NER consistently outperforms strong prior ZS-NER baselines in cross-domain settings. Our implementation will be open-sourced at https://github.com/DMIRLAB-Group/SAM-NER.
匹配关键词: GAN
---

[ACADEMIC - ARXIV]
标题: AHPA: Adaptive Hierarchical Prior Alignment for Diffusion Transformers
作者: Ruibin Min, Yexin Liu, Aimin Pan, Changsheng Lu, Jiafei Wu, Kelu Yao, Xiaogang Xu, Harry Yang
链接: https://arxiv.org/abs/2605.03317v1
完整摘要: Representation alignment has recently emerged as an effective paradigm for accelerating Diffusion Transformer training. Despite their success, existing alignment methods typically impose a fixed supervision target or a fixed alignment granularity throughout the entire denoising trajectory, whether the guidance is provided by external vision encoders, internal self-representations, or VAE-derived features. We argue that such timestep-agnostic alignment is suboptimal because the useful granularity of representation supervision changes systematically with the signal-to-noise ratio. In high-noise regimes, diffusion models benefit more from coarse semantic and layout-level anchoring, whereas in low-noise regimes, the training signal should emphasize spatially detailed and structurally faithful refinement. This non-stationary alignment behavior creates a representational mismatch for static single-level supervisors. To address this issue, we propose Adaptive Hierarchical Prior Alignment (AHPA), a lightweight alignment framework that exploits the hierarchical representations naturally embedded in the frozen VAE encoder. Instead of using only a single compressed latent as the alignment target, AHPA extracts multi-level VAE features that provide complementary priors ranging from local geometry and spatial topology to coarse semantic layout. A timestep-conditioned Dynamic Router adaptively selects and weights these hierarchical priors along the denoising trajectory, thereby synchronizing the alignment granularity with the model's evolving training needs. Extensive experiments show that AHPA improves convergence and generation quality over baselines and incurs no additional inference cost while avoiding external encoder supervision during training.
匹配关键词: VAE
---

[ACADEMIC - ARXIV]
标题: MiniMind-O Technical Report: An Open Small-Scale Speech-Native Omni Model
作者: Jingyao Gong
链接: https://arxiv.org/abs/2605.03937v1
完整摘要: MiniMind-O is an open 0.1B-scale omni model built on the MiniMind language model. It accepts text, speech, and image inputs, and returns both text and streaming speech. The release includes model code, checkpoints, and the main Parquet training datasets for text-to-audio, image-to-text, and audio-to-audio training, making the complete interaction loop directly inspectable. The model uses a full MiniMind backbone as the Thinker and an independent four-layer Talker made from MiniMind blocks. Frozen SenseVoice-Small and SigLIP2 encoders provide speech and image features, which are mapped by lightweight MLP projectors and injected at modality-placeholder positions. The Talker reads a middle-layer Thinker state together with an autoregressive eight-layer Mimi-code buffer. Speaker control is handled by a dedicated speaker token, right-aligned reference codec prompts, and precomputed CAM++ speaker embeddings, so voice conditioning remains part of the audio-code context rather than a separate TTS module. With a 768-dimensional Talker, the dense and MoE variants reach average CERs of 0.0897 and 0.0900 in Thinker--Talker consistency evaluation, with overall voice-cloning similarities of 0.5995 and 0.5937. Beyond reporting a working system, the paper identifies three scale-critical design choices for small omni models: middle-layer semantic bridging, a released multimodal sequence format, and a parameter-efficient eight-codebook interface.
匹配关键词: autoregressive
---

[ACADEMIC - ARXIV]
标题: Stream-R1: Reliability-Perplexity Aware Reward Distillation for Streaming Video Generation
作者: Bin Wu, Mengqi Huang, Shaojin Wu, Weinan Jia, Yuxin Wang, Zhendong Mao, Yongdong Zhang
链接: https://arxiv.org/abs/2605.03849v1
完整摘要: Distillation-based acceleration has become foundational for making autoregressive streaming video diffusion models practical, with distribution matching distillation (DMD) as the de facto choice. Existing methods, however, train the student to match the teacher's output indiscriminately, treating every rollout, frame, and pixel as equally reliable supervision. We argue that this caps distilled quality, since it overlooks two complementary axes of variance in DMD supervision: Inter-Reliability across student rollouts whose supervision varies in reliability, and Intra-Perplexity across spatial regions and temporal frames that contribute unequally to where quality can still be improved. The objective thus conflates two questions under a uniform weight: whether to learn from each rollout, and where to concentrate optimization within it. To address this, we propose Stream-R1, a Reliability-Perplexity Aware Reward Distillation framework that adaptively reweights the distillation objective at both rollout and spatiotemporal-element levels through a single shared reward-guided mechanism. At the Inter-Reliability level, Stream-R1 rescales each rollout's loss by an exponential of a pretrained video reward score, so that rollouts with reliable supervision dominate optimization. At the Intra-Perplexity level, it back-propagates the same reward model to extract per-pixel gradient saliency, which is factored into spatial and temporal weights that concentrate optimization pressure on regions and frames where refinement yields the largest expected gain. An adaptive balancing mechanism prevents any single quality axis from dominating across visual quality, motion quality, and text alignment. Stream-R1 attains consistent improvements on all three dimensions over distillation baselines on standard streaming video generation benchmarks, without architectural modification or additional inference cost.
匹配关键词: autoregressive
---

[ACADEMIC - ARXIV]
标题: RoboAlign-R1: Distilled Multimodal Reward Alignment for Robot Video World Models
作者: Hao Wu, Yuqi Li, Yuan Gao, Fan Xu, Fan Zhang, Kun Wang, Penghao Zhao, Qiufeng Wang, Yizhou Zhao, Weiyan Wang, Yingli Tian, Xian Wu, Xiaomeng Huang
链接: https://arxiv.org/abs/2605.03821v1
完整摘要: Existing robot video world models are typically trained with low-level objectives such as reconstruction and perceptual similarity, which are poorly aligned with the capabilities that matter most for robot decision making, including instruction following, manipulation success, and physical plausibility. They also suffer from error accumulation in long-horizon autoregressive prediction. We present RoboAlign-R1, a framework that combines reward-aligned post-training with stabilized long-horizon inference for robot video world models. We construct RobotWorldBench, a benchmark of 10,000 annotated video-instruction pairs collected from four robot data sources, and train a multimodal teacher judge, RoboAlign-Judge, to provide fine-grained six-dimensional evaluation of generated videos. We then distill the teacher into a lightweight student reward model for efficient reinforcement-learning-based post-training. To reduce long-horizon rollout drift, we further introduce Sliding Window Re-encoding (SWR), a training-free inference strategy that periodically refreshes the generation context. Under our in-domain evaluation protocol, RoboAlign-R1 improves the aggregate six-dimension score by 10.1% over the strongest baseline, including gains of 7.5% on Manipulation Accuracy and 4.6% on Instruction Following; these ranking improvements are further supported by an external VLM-based cross-check and a blinded human study. Meanwhile, SWR improves long-horizon prediction quality with only about 1% additional latency, yielding a 2.8% gain in SSIM and a 9.8% reduction in LPIPS. Together, these results show that reward-aligned post-training and stabilized long-horizon decoding improve task consistency, physical realism, and long-horizon prediction quality in robot video world models.
匹配关键词: autoregressive
---

[ACADEMIC - ARXIV]
标题: Benchmarking Parameter-Efficient Fine-Tuning of Large Language Models for Low-Resource Tajik Text Generation with the Tajik Web Corpus
作者: Mullosharaf K. Arabov
链接: https://arxiv.org/abs/2605.03742v1
完整摘要: This paper is devoted to the adaptation of generative large language models for the Tajik language, a low-resource language with Cyrillic script. To overcome the shortage of digital text resources, the author created and publicly released the Tajik Web Corpus, the largest open-access corpus of Tajik, comprising 319,298 documents (~1.11 billion characters). On a subsample of 10,000 documents, 17 configurations were benchmarked, covering autoregressive, encoder-decoder, and encoder-only models with three fine-tuning strategies: full fine-tuning, LoRA, and QLoRA (ranks 8 and 16). Quality was assessed via perplexity and cross-entropy loss; peak GPU memory and training time were also recorded. Best results were achieved by Mistral 7B with QLoRA (r=16): mean perplexity 5.03, standard deviation 0.03. Increasing rank from 8 to 16 gave statistically insignificant improvement while raising memory consumption. For small GPT-2 family models, full fine-tuning yielded lower perplexity (3.48 for GPT-2 Medium) than LoRA (7.60-8.42), but induced catastrophic forgetting. The encoder-only XLM-RoBERTa showed the worst results (perplexity 59.3). The novelty lies in creating the largest verified Tajik corpus and the first systematic analysis of PEFT effectiveness for Tajik text generation. Practical value lies in recommendations for architecture and fine-tuning strategy selection, optimizing computational costs without substantial quality loss.
匹配关键词: autoregressive
---

[ACADEMIC - ARXIV]
标题: RPBA-Net: An Interpretable Residual Pyramid Bilateral Affine Network for RAW-Domain ISP Enhancement
作者: Yucheng Xin, Wu Chen, Xiang Chen, Guangwei Gao, Xinchun Wang, Ruize Wu, Dianjie Lu, Guijuan Zhang, Linwei Fan, Zhuoran Zheng
链接: https://arxiv.org/abs/2605.03626v1
完整摘要: To address module fragmentation, uninterpretable mappings, and deployment constraints in RAW-domain demosaicing, color correction, and detail enhancement, this paper proposes RPBA-Net, an interpretable residual pyramid bilateral affine network for RAW-domain ISP enhancement. Given packed RAW as input, the method performs residual affine base reconstruction by estimating a base RGB representation and learning identity-guided residual affine corrections, thereby unifying demosaicing and enhancement. It further builds pyramid bilateral affine grids and combines guide-driven autoregressive adaptive slicing with adaptive cross-layer fusion to hierarchically model global tone restoration and local texture enhancement. In addition, smoothness, cross-scale consistency, and magnitude regularization terms are introduced to improve model stability, controllability, and structural interpretability. Extensive experiments demonstrate that RPBA-Net surpasses representative RAW-to-sRGB methods and achieves state-of-the-art performance in reconstruction fidelity and perceptual quality, while maintaining low model complexity and strong deployment potential for mobile and embedded platforms.
匹配关键词: autoregressive
---

[ACADEMIC - ARXIV]
标题: Pretrained Model Representations as Acquisition Signals for Active Learning of MLIPs
作者: Eszter Varga-Umbrich, Shikha Surana, Paul Duckworth, Jules Tilly, Olivier Peltre, Zachary Weller-Davies
链接: https://arxiv.org/abs/2605.03964v1
完整摘要: Training machine learning interatomic potentials (MLIPs) for reactive chemistry is often bottlenecked by the high cost of quantum chemical labels and the scarcity of transition state configurations in candidate pools. Active learning (AL) can mitigate these costs, but its effectiveness hinges on the acquisition rule. We investigate whether the latent space of a pretrained MLIP already contains the information necessary for effective acquisition, eliminating the need for auxiliary uncertainty heads, Bayesian training and fine-tuning, or committee ensembles. We introduce two acquisition signals derived directly from a pretrained MACE potential: a finite-width neural tangent kernel (NTK) and an activation kernel built from hidden latent space features. On reactive-chemistry benchmarks, both kernels consistently outperform fixed-descriptor baselines, committee disagreement, and random acquisition, reducing the data required to reach performance targets by an average of 38% for energy error and 28% for force error. We further show that the pretrained model induces similarity spaces that preserve chemically meaningful structure and provide more reliable residual uncertainty estimates than randomly initialised or fixed-descriptor-based kernels. Our results suggest that pretraining aligns latent-space geometry with model error, yielding a practical and sufficient acquisition signal for reactive MLIP fine-tuning.
匹配关键词: latent diffusion
---

[ACADEMIC - ARXIV]
标题: QKVShare: Quantized KV-Cache Handoff for Multi-Agent On-Device LLMs
作者: Pratik Honavar, Tejpratap GVSL
链接: https://arxiv.org/abs/2605.03884v1
完整摘要: Multi-agent LLM systems on edge devices need to hand off latent context efficiently, but the practical choices today are expensive re-prefill or full-precision KV transfer. We study QKVShare, a framework for quantized KV-cache handoff between agents that combines token-level mixed-precision allocation, a self-contained CacheCard representation, and a HuggingFace-compatible cache injection path. Our current results support a narrower but clearer story than the original draft: on 150 GSM8K problems with Llama-3.1-8B-Instruct, adaptive quantization remains competitive under repeated handoff and shows its clearest gains against uniform quantization in deeper-hop, higher budget settings; for handoff latency, the QKVShare path reduces TTFT relative to full re prefill at every tested context, from 130.7 ms vs. 150.2 ms at nominal 1K context to 397.1 ms vs. 1029.7 ms at nominal 8K context;. Stage timing shows that post-injection generation, not card creation, dominates the current QKVShare latency path. These results position quantized KV handoff as a promising on-device systems direction while also highlighting the need for stronger controller ablations and apples-to-apples runtime comparisons.
匹配关键词: latent diffusion
---

[ACADEMIC - ARXIV]
标题: DMGD: Train-Free Dataset Distillation with Semantic-Distribution Matching in Diffusion Models
作者: Qichao Wang, Yunhong Lu, Hengyuan Cao, Junyi Zhang, Min Zhang
链接: https://arxiv.org/abs/2605.03877v1
完整摘要: Dataset distillation enables efficient training by distilling the information of large-scale datasets into significantly smaller synthetic datasets. Diffusion based paradigms have emerged in recent years, offering novel perspectives for dataset distillation. However, they typically necessitate additional fine-tuning stages, and effective guidance mechanisms remain underexplored. To address these limitations, we rethink diffusion based dataset distillation and propose a Dual Matching Guided Diffusion (DMGD) framework, centered on efficient training-free guidance. We first establish Semantic Matching via conditional likelihood optimization, eliminating the need for auxiliary classifiers. Furthermore, we propose a dynamic guidance mechanism that enhances the diversity of synthetic data while maintaining semantic alignment. Simultaneously, we introduce an optimal transport (OT) based Distribution Matching approach to further align with the target distribution structure. To ensure efficiency, we develop two enhanced strategies for diffusion based framework: Distribution Approximate Matching and Greedy Progressive Matching. These strategies enable effective distribution matching guidance with minimal computational overhead. Experimental results on ImageNet-Woof, ImageNet-Nette, and ImageNet-1K demonstrate that our training-free approach achieves significant improvements, outperforming state-of-the-art (SOTA) methods requiring additional fine-tuning by average accuracy gains of 2.1%, 5.4%, and 2.4%, respectively.
匹配关键词: latent diffusion
---

[ACADEMIC - ARXIV]
标题: Stream-R1: Reliability-Perplexity Aware Reward Distillation for Streaming Video Generation
作者: Bin Wu, Mengqi Huang, Shaojin Wu, Weinan Jia, Yuxin Wang, Zhendong Mao, Yongdong Zhang
链接: https://arxiv.org/abs/2605.03849v1
完整摘要: Distillation-based acceleration has become foundational for making autoregressive streaming video diffusion models practical, with distribution matching distillation (DMD) as the de facto choice. Existing methods, however, train the student to match the teacher's output indiscriminately, treating every rollout, frame, and pixel as equally reliable supervision. We argue that this caps distilled quality, since it overlooks two complementary axes of variance in DMD supervision: Inter-Reliability across student rollouts whose supervision varies in reliability, and Intra-Perplexity across spatial regions and temporal frames that contribute unequally to where quality can still be improved. The objective thus conflates two questions under a uniform weight: whether to learn from each rollout, and where to concentrate optimization within it. To address this, we propose Stream-R1, a Reliability-Perplexity Aware Reward Distillation framework that adaptively reweights the distillation objective at both rollout and spatiotemporal-element levels through a single shared reward-guided mechanism. At the Inter-Reliability level, Stream-R1 rescales each rollout's loss by an exponential of a pretrained video reward score, so that rollouts with reliable supervision dominate optimization. At the Intra-Perplexity level, it back-propagates the same reward model to extract per-pixel gradient saliency, which is factored into spatial and temporal weights that concentrate optimization pressure on regions and frames where refinement yields the largest expected gain. An adaptive balancing mechanism prevents any single quality axis from dominating across visual quality, motion quality, and text alignment. Stream-R1 attains consistent improvements on all three dimensions over distillation baselines on standard streaming video generation benchmarks, without architectural modification or additional inference cost.
匹配关键词: latent diffusion
---

[ACADEMIC - ARXIV]
标题: Identity-Consistent Multi-Pose Generation of Contactless Fingerprints
作者: Zhiyu Pan, Xiongjun Guan, Jianjiang Feng, Jie Zhou
链接: https://arxiv.org/abs/2605.03830v1
完整摘要: Contactless fingerprint recognition has gained increasing attention due to its advantages in hygiene and acquisition flexibility. However, the absence of physical contact constraints introduces severe nonlinear geometric distortions caused by free finger poses in 3D space, resulting in a substantial cross-modal domain gap between contactless and conventional contact-based fingerprints. Existing solutions largely rely on explicit geometric correction or image enhancement, which are fragile under extreme pose variations. In this paper, we propose Identity-Consistent Multi-Pose Generation of Contactless Fingerprints (IMPOSE), a physics-inspired framework that synthesizes identity-preserving, multi-pose contactless fingerprint samples to empower recognition models. IMPOSE consists of three stages: (1) rolled fingerprint identity generation via latent diffusion with discrete codebook representations, (2) cross-modal translation from rolled to contactless modality guided by Sauvola-based local adaptive binarization as an identity anchor, and (3) physics-based multi-pose simulation through 3D finger model texture mapping and projection. The generated samples maintain strict identity consistency at the ridge topology level and spatial alignment with standard fingerprint coordinate space. Extensive experiments on the UWA and PolyU CL2CB databases demonstrate that fine-tuning fixed-length dense descriptors (FDD) with IMPOSE-synthesized data achieves state-of-the-art cross-modal matching, reducing EER to 8.74% on UWA and 2.26% on PolyU CL2CB. Synthetic data also yields consistent gains across mainstream representations including DeepPrint and AFRNet, and the hybrid strategy combining synthetic and real data achieves the best overall results. The code and generated samples are available at https://github.com/Yu-Yy/IMPOSE.
匹配关键词: latent diffusion
---

[ACADEMIC - ARXIV]
标题: UnAC: Adaptive Visual Prompting with Abstraction and Stepwise Checking for Complex Multimodal Reasoning
作者: Yifan Wang, Yun Fu
链接: https://arxiv.org/abs/2605.03950v1
完整摘要: Although recent LMMs have become much stronger at visual perception, they remain unreliable on problems that require multi-step reasoning over visual evidence. In this paper, we present UnAC (Understanding, Abstracting, and Checking), a multimodal prompting method that strengthens reasoning for complex multimodal tasks in LMMs (e.g., GPT-4o, Gemini 1.5, and GPT-4V). To improve image understanding and capture fine details, we propose an adaptive visual prompting strategy that enables LMMs to focus on salient regions. We further design an image-abstraction prompt to effectively extract key information from images. In addition, we introduce a gradual self-checking scheme that improves reasoning by verifying each decomposed subquestion and its answer. Extensive experiments on three public benchmarks-MathVista, MM-Vet, and MMMU.
匹配关键词: multimodal
---

[ACADEMIC - ARXIV]
标题: MiniMind-O Technical Report: An Open Small-Scale Speech-Native Omni Model
作者: Jingyao Gong
链接: https://arxiv.org/abs/2605.03937v1
完整摘要: MiniMind-O is an open 0.1B-scale omni model built on the MiniMind language model. It accepts text, speech, and image inputs, and returns both text and streaming speech. The release includes model code, checkpoints, and the main Parquet training datasets for text-to-audio, image-to-text, and audio-to-audio training, making the complete interaction loop directly inspectable. The model uses a full MiniMind backbone as the Thinker and an independent four-layer Talker made from MiniMind blocks. Frozen SenseVoice-Small and SigLIP2 encoders provide speech and image features, which are mapped by lightweight MLP projectors and injected at modality-placeholder positions. The Talker reads a middle-layer Thinker state together with an autoregressive eight-layer Mimi-code buffer. Speaker control is handled by a dedicated speaker token, right-aligned reference codec prompts, and precomputed CAM++ speaker embeddings, so voice conditioning remains part of the audio-code context rather than a separate TTS module. With a 768-dimensional Talker, the dense and MoE variants reach average CERs of 0.0897 and 0.0900 in Thinker--Talker consistency evaluation, with overall voice-cloning similarities of 0.5995 and 0.5937. Beyond reporting a working system, the paper identifies three scale-critical design choices for small omni models: middle-layer semantic bridging, a released multimodal sequence format, and a parameter-efficient eight-codebook interface.
匹配关键词: multimodal
---

[ACADEMIC - ARXIV]
标题: Task-Aware Scanning Parameter Configuration for Robotic Inspection Using Vision Language Embeddings and Hyperdimensional Computing
作者: Zhiling Chen, David Gorsich, Matthew P. Castanier, Yang Zhang, Jiong Tang, Farhad Imani
链接: https://arxiv.org/abs/2605.03909v1
完整摘要: Robotic laser profiling is widely used for dimensional verification and surface inspection, yet measurement fidelity is often dominated by sensor configuration rather than robot motion. Industrial profilers expose multiple coupled parameters, including sampling frequency, measurement range, exposure time, receiver dynamic range, and illumination, that are still tuned by trial-and-error; mismatches can cause saturation, clipping, or missing returns that cannot be recovered downstream. We formulate instruction-conditioned sensing parameter recommendation; given a pre-scan RGB observation and a natural-language inspection instruction, infer a discrete configuration over key parameters of a robot-mounted profiler. To benchmark this problem, we develop Instruct-Obs2Param, a real-world multimodal dataset linking inspection intents and multi-view pose and illumination variation across 16 objects to canonical parameter regimes. We then propose ScanHD, a hyperdimensional computing framework that binds instruction and observation into a task-aware code and performs parameter-wise associative reasoning with compact memories, matching discrete scanner regimes while yielding stable, interpretable, low-latency decisions. On Instruct-Obs2Param, ScanHD achieves 92.7% average exact accuracy and 98.1% average Win@1 accuracy across the five parameters, with strong cross-split generalization and low-latency inference suitable for deployment, outperforming rule-based heuristics, conventional multimodal models, and multimodal large language models. This work enables autonomous, instruction-conditioned sensing configuration from task intent and scene context, eliminating manual tuning and elevating sensor configuration from a static setting to an adaptive decision variable.
匹配关键词: multimodal
---

[ACADEMIC - ARXIV]
标题: CC-OCR V2: Benchmarking Large Multimodal Models for Literacy in Real-world Document Processing
作者: Zhipeng Xu, Junhao Ji, Zulong Chen, Zhenghao Liu, Qing Liu, Chunyi Peng, Zubao Qin, Ze Xu, Jianqiang Wan, Jun Tang, Zhibo Yang, Shuai Bai, Dayiheng Liu
链接: https://arxiv.org/abs/2605.03903v1
完整摘要: Large Multimodal Models (LMMs) have recently shown strong performance on Optical Character Recognition (OCR) tasks, demonstrating their promising capability in document literacy. However, their effectiveness in real-world applications remains underexplored, as existing benchmarks adopt task scopes misaligned with practical applications and assume homogeneous acquisition conditions. To address this gap, we introduce CC-OCR V2, a comprehensive and challenging OCR benchmark tailored to real-world document processing. CC-OCR V2 focuses on practical enterprise document processing tasks and incorporates hard and corner cases that are critical yet underrepresented in prior benchmarks, covering 5 major OCR-centric tracks: text recognition, document parsing, document grounding, key information extraction, and document question answering, comprising 7,093 high-difficulty samples. Extensive experiments on 14 advanced LMMs reveal that current models fall short of real-world application requirements. Even state-of-the-art LMMs exhibit substantial performance degradation across diverse tasks and scenarios. These findings reveal a significant gap between performance on current benchmarks and effectiveness in real-world applications. We release the full dataset and evaluation toolkit at https://github.com/eioss/CC-OCR-V2.
匹配关键词: multimodal
---

[ACADEMIC - ARXIV]
标题: Deco: Extending Personal Physical Objects into Pervasive AI Companion through a Dual-Embodiment Framework
作者: Zhihan Jiang, Mengyuan Millie Wu, Ruishi Zou, Shiyu Xu, Xun Qian, Emma Macmanus, Steven Liao, Ping Zhang, Bingsheng Yao, Tingyu Cheng, James L. David, Nabila El-Bassel, Lena Mamykina, Frances R. Levin, Ryan Sultan, Dakuo Wang, Xuhai Xu
链接: https://arxiv.org/abs/2605.03882v1
完整摘要: Individuals frequently form deep attachments to physical objects (e.g., plush toys) that usually cannot sense or respond to their emotions. While AI companions offer responsiveness and personalization, they exist independently of these physical objects and lack an ongoing connection to them. To bridge this gap, we conducted a formative study (N=9) to explore how digital agents could inherit and extend the emotional bond, deriving four design principles (Faithful Identity, Calibrated Agency, Ambient Presence, and Reciprocal Memory). We then present the Dual-Embodiment Companion Framework, instantiated as Deco, a mobile system integrating multimodal Large Language Models (LLMs) and Augmented Reality to create synchronized digital embodiments of users' physical companions. A within-subjects study (N=25) showed Deco significantly outperformed a personalized LLM-empowered digital companion baseline on perceived companionship, emotional bond, and design-principle scales (all p<0.01). A seven-day field deployment (N=17) showed sustained engagement, subjective well-being improvement (p=.040), and three key relational patterns: digital activities retroactively vitalized physical objects, bond deepening was driven by emotional engagement depth rather than interaction frequency, and users sustained bonds while actively navigating digital companions' AI nature. This work highlights a promising alternative for designing digital companions: moving from creating new relationships to dual embodiment, where digital agents seamlessly extend the emotional history of physical objects.
匹配关键词: multimodal
---

[ACADEMIC - ARXIV]
标题: Logical Consistency as a Bridge: Improving LLM Hallucination Detection via Label Constraint Modeling between Responses and Self-Judgments
作者: Hao Mi, Qiang Sheng, Shaofei Wang, Beizhe Hu, Yifan Sun, Zhengjia Wang, Hengqi Zeng, Yang Li, Danding Wang, Juan Cao
链接: https://arxiv.org/abs/2605.03971v1
完整摘要: Large Language Models (LLMs) are prone to factual hallucinations, risking their reliability in real-world applications. Existing hallucination detectors mainly extract micro-level intrinsic patterns for uncertainty quantification or elicit macro-level self-judgments through verbalized prompts. However, these methods address only a single facet of the hallucination, focusing either on implicit neural uncertainty or explicit symbolic reasoning, thereby treating these inherently coupled behaviors in isolation and failing to exploit their interdependence for a holistic view. In this paper, we propose LaaB (Logical Consistency-as-a-Bridge), a framework that bridges neural features and symbolic judgments for hallucination detection. LaaB introduces a "meta-judgment" process to map symbolic labels back into the feature space. By leveraging the inherent logical bridge where response and meta-judgment labels are either the same or opposite based on the self-judgment's semantics, LaaB aligns and integrates dual-view signals via mutual learning and enhances the hallucination detection. Extensive experiments on 4 public datasets, across 4 LLMs, against 8 baselines demonstrate the superiority of LaaB.
匹配关键词: vision language model
---

[ACADEMIC - ARXIV]
标题: Feature-Augmented Transformers for Robust AI-Text Detection Across Domains and Generators
作者: Mohamed Mady, Johannes Reschke, Björn Schuller
链接: https://arxiv.org/abs/2605.03969v1
完整摘要: AI-generated text is nowadays produced at scale across domains and heterogeneous generation pipelines, making robustness to distribution shift a central requirement for supervised binary detectors. We train transformer-based detectors on HC3 PLUS and calibrate a single decision threshold by maximising balanced accuracy on held-out validation; this threshold is then kept fixed for all downstream test distributions, revealing domain- and generator-dependent error asymmetries under shift. We evaluate in-domain on HC3 PLUS, under cross-dataset transfer to the multi-domain, multi-generator M4 benchmark, and on the external AI-Text-Detection-Pile. Although base models achieve near-ceiling in-domain performance (up to 99.5% balanced accuracy), performance under shift is brittle and strongly model-dependent. Feature augmentation via attention-based linguistic feature fusion improves transfer, with our best model (DeBERTa-v3-base+FeatAttn) achieving 85.9% balanced accuracy on M4. Multi-seed experiments confirm high stability. Under the same fixed-threshold protocol, our model outperforms strong zero-shot baselines by up to +7.22 points. Category-level ablations further show that readability and vocabulary features contribute most to robustness under shift. Overall, these results demonstrate that feature augmentation and a modern DeBERTa backbone significantly outperform earlier BERT/RoBERTa models, while the fixed-threshold protocol provides a more realistic and informative assessment of practical detector robustness.
匹配关键词: vision language model
---

[ACADEMIC - ARXIV]
标题: Label-Efficient School Detection from Aerial Imagery via Weakly Supervised Pretraining and Fine-Tuning
作者: Zakarya Elmimouni, Fares Fourati, Mohamed-Slim Alouini
链接: https://arxiv.org/abs/2605.03968v1
完整摘要: Accurate school detection is essential for supporting education initiatives, including infrastructure planning and expanding internet connectivity to underserved areas. However, many regions around the world face challenges due to outdated, incomplete, or unavailable official records. Manual mapping efforts, while valuable, are labor-intensive and lack scalability across large geographic areas. To address this, we propose a weakly supervised framework for school detection from aerial imagery that minimizes the need for human annotations while supporting global mapping efforts. Our method is specifically designed for low-data regimes, where manual annotations are extremely scarce. We introduce an automatic labeling pipeline that leverages sparse location points and semantic segmentation to generate infrastructure masks from which we generate bounding boxes. Using these automatically labeled images, we train our detectors on a first training stage to learn a representation of what schools look like, then using a small set of manually labeled images, we fine-tune the previously trained models on this clean dataset. This two stage training pipeline enables large-scale and strong detection in low-data setting of school infrastructure with minimal supervision. Our results demonstrate strong object detection performance, particularly in the low-data regime, where the models achieve promising results using only 50 manually labeled images, significantly reducing the need for costly annotations. This framework supports education and connectivity initiatives worldwide by providing an efficient and extensible approach to mapping schools from space. All models, training code and auto-labeled data will be publicly released to foster future research and real-world impact.
匹配关键词: vision language model
---

[ACADEMIC - ARXIV]
标题: Pretrained Model Representations as Acquisition Signals for Active Learning of MLIPs
作者: Eszter Varga-Umbrich, Shikha Surana, Paul Duckworth, Jules Tilly, Olivier Peltre, Zachary Weller-Davies
链接: https://arxiv.org/abs/2605.03964v1
完整摘要: Training machine learning interatomic potentials (MLIPs) for reactive chemistry is often bottlenecked by the high cost of quantum chemical labels and the scarcity of transition state configurations in candidate pools. Active learning (AL) can mitigate these costs, but its effectiveness hinges on the acquisition rule. We investigate whether the latent space of a pretrained MLIP already contains the information necessary for effective acquisition, eliminating the need for auxiliary uncertainty heads, Bayesian training and fine-tuning, or committee ensembles. We introduce two acquisition signals derived directly from a pretrained MACE potential: a finite-width neural tangent kernel (NTK) and an activation kernel built from hidden latent space features. On reactive-chemistry benchmarks, both kernels consistently outperform fixed-descriptor baselines, committee disagreement, and random acquisition, reducing the data required to reach performance targets by an average of 38% for energy error and 28% for force error. We further show that the pretrained model induces similarity spaces that preserve chemically meaningful structure and provide more reliable residual uncertainty estimates than randomly initialised or fixed-descriptor-based kernels. Our results suggest that pretraining aligns latent-space geometry with model error, yielding a practical and sufficient acquisition signal for reactive MLIP fine-tuning.
匹配关键词: vision language model
---

[ACADEMIC - ARXIV]
标题: Transformers with Selective Access to Early Representations
作者: Skye Gunasekaran, Téa Wright, Rui-Jie Zhu, Jason Eshraghian
链接: https://arxiv.org/abs/2605.03953v1
完整摘要: Several recent Transformer architectures expose later layers to representations computed in the earliest layers, motivated by the observation that low-level features can become harder to recover as the residual stream is repeatedly transformed through depth. The cheapest among these methods add static value residuals: learned mixing coefficients that expose the first-layer value projection V_1 uniformly across tokens and heads. More expressive dense or dynamic alternatives recover finer-grained access, but at higher memory cost and lower throughput. The usefulness of V_1 is unlikely to be constant across tokens, heads, and contexts; different positions plausibly require different amounts of access to early lexical or semantic information. We therefore treat early-representation reuse as a retrieval problem rather than a connectivity problem, and introduce Selective Access Transformer (SATFormer), which preserves the first-layer value pathway while controlling access with a context-dependent gate. Across models from 130M to 1.3B parameters, SATFormer consistently improves validation loss and zero-shot accuracy over the static value-residual and Transformer baselines. Its strongest gains appear on retrieval-intensive benchmarks, where it improves over static value residuals by approximately 1.5 average points, while maintaining throughput and memory usage close to the baseline Transformer. Gate analyses suggest sparse, depth-dependent, head-specific, and category-sensitive access patterns, supporting the interpretation that SATFormer learns selective reuse of early representations rather than uniform residual copying. Our code is available at https://github.com/SkyeGunasekaran/SATFormer.
匹配关键词: vision language model
---

[ACADEMIC - ARXIV]
标题: StateVLM: A State-Aware Vision-Language Model for Robotic Affordance Reasoning
作者: Xiaowen Sun, Matthias Kerzel, Mengdi Li, Xufeng Zhao, Paul Striker, Stefan Wermter
链接: https://arxiv.org/abs/2605.03927v1
完整摘要: Vision-language models (VLMs) have shown remarkable performance in various robotic tasks, as they can perceive visual information and understand natural language instructions. However, when applied to robotics, VLMs remain subject to a fundamental limitation inherent in large language models (LLMs): they struggle with numerical reasoning, particularly in object detection and object-state localization. To explore numerical reasoning as a regression task in VLMs, we propose a novel training strategy to adapt VLMs for object detection and object-state localization. This approach leverages box decoder outputs to compute an Auxiliary Regression Loss (ARL) during fine-tuning, while preserving standard sequence prediction at inference. We leverage this training strategy to develop StateVLM (State-aware Vision-Language Model), a novel model designed to perceive and learn fine-grained object representations, including precise localization of objects and their states, as well as graspable regions. Due to the lack of a benchmark for object-state affordance reasoning, we introduce an open-source benchmark, Object State Affordance Reasoning (OSAR), which contains 1,172 scenes with 7,746 individual objects and corresponding bounding boxes. Comparative experiments on adapted benchmarks (RefCOCO, RefCOCO+, and \mbox{RefCOCOg}) demonstrate that ARL improves model performance by an average of 1.6\% compared to models without ARL. Experiments on the OSAR benchmark further support this finding, showing that StateVLM with ARL achieves an average of 5.2\% higher performance than models without ARL. In particular, ARL is also important for the complex task of affordance reasoning in OSAR, where it enhances the consistency of model outputs.
匹配关键词: VLM
---

[ACADEMIC - ARXIV]
标题: Quantifying the human visual exposome with vision language models
作者: Christian Rominger, Andreas R. Schwerdtfeger, Malay Gaherwar Singh, Dimitri Khudyakow, Elizabeth A. M. Michels, Fabian Wolf, Jakob Nikolas Kather, Magdalena Katharina Wekenborg
链接: https://arxiv.org/abs/2605.03863v1
完整摘要: The visual environment is a fundamental yet unquantified determinant of mental health. While the concept of the environmental exposome is well established, current methods rely on coarse geospatial proxies or biased self reports, failing to capture the first person visual context of daily life. We addressed this gap by coupling ecological momentary assessment with vision language models (VLMs) to quantify the semantic richness of human visual experience. Across 2674 participant generated photographs, VLM derived estimates of greenness robustly predicted momentary affect and chronic stress, consistent with established benchmarks. We then developed a semi autonomous large language model (LLM) based pipeline that mined over seven million scientific publications to extract nearly 1000 environmental features empirically linked to mental health. When applied to real world imagery, up to 33 percent of VLM extracted context ratings significantly correlated with affect and stress. These findings establish a scalable objective paradigm for visual exposomics, enabling high throughput decoding of how the visible world is associated with mental health.
匹配关键词: VLM
---

[ACADEMIC - ARXIV]
标题: RoboAlign-R1: Distilled Multimodal Reward Alignment for Robot Video World Models
作者: Hao Wu, Yuqi Li, Yuan Gao, Fan Xu, Fan Zhang, Kun Wang, Penghao Zhao, Qiufeng Wang, Yizhou Zhao, Weiyan Wang, Yingli Tian, Xian Wu, Xiaomeng Huang
链接: https://arxiv.org/abs/2605.03821v1
完整摘要: Existing robot video world models are typically trained with low-level objectives such as reconstruction and perceptual similarity, which are poorly aligned with the capabilities that matter most for robot decision making, including instruction following, manipulation success, and physical plausibility. They also suffer from error accumulation in long-horizon autoregressive prediction. We present RoboAlign-R1, a framework that combines reward-aligned post-training with stabilized long-horizon inference for robot video world models. We construct RobotWorldBench, a benchmark of 10,000 annotated video-instruction pairs collected from four robot data sources, and train a multimodal teacher judge, RoboAlign-Judge, to provide fine-grained six-dimensional evaluation of generated videos. We then distill the teacher into a lightweight student reward model for efficient reinforcement-learning-based post-training. To reduce long-horizon rollout drift, we further introduce Sliding Window Re-encoding (SWR), a training-free inference strategy that periodically refreshes the generation context. Under our in-domain evaluation protocol, RoboAlign-R1 improves the aggregate six-dimension score by 10.1% over the strongest baseline, including gains of 7.5% on Manipulation Accuracy and 4.6% on Instruction Following; these ranking improvements are further supported by an external VLM-based cross-check and a blinded human study. Meanwhile, SWR improves long-horizon prediction quality with only about 1% additional latency, yielding a 2.8% gain in SSIM and a 9.8% reduction in LPIPS. Together, these results show that reward-aligned post-training and stabilized long-horizon decoding improve task consistency, physical realism, and long-horizon prediction quality in robot video world models.
匹配关键词: VLM
---

[ACADEMIC - ARXIV]
标题: What You Think is What You See: Driving Exploration in VLM Agents via Visual-Linguistic Curiosity
作者: Haoxi Li, Qinglin Hou, Jianfei Ma, Jinxiang Lai, Tao Han, Sikai Bai, Jingcai Guo, Jie Zhang, Song Guo
链接: https://arxiv.org/abs/2605.03782v1
完整摘要: To navigate partially observable visual environments, recent VLM agents increasingly internalize world modeling capabilities into their policies via explicit CoT reasoning, enabling them to mentally simulate futures before acting. However, relying solely on passive reasoning over visited states is insufficient for sparse-reward tasks, as it lacks the epistemic drive to actively uncover the ``known unknown'' required for robust generalization. We ask: Can VLM agents actively find signals that challenge and refine their internal world model through curiosity-driven exploration? In this work, we propose GLANCE, a unified framework that bridges reasoning and exploration by grounding the agent's linguistic world model into the stable visual representations of an evolving target network. Crucially, GLANCE leverages the discrepancy between linguistic prediction and visual reality as an intrinsic curiosity signal within reinforcement learning, steering the agent to actively explore areas where its internal model is uncertain. Extensive experiments across a series of agentic tasks show the effectiveness of GLANCE, and demonstrate that aligning ``what the agent thinks'' with ``what the agent sees'' is key to solving complex or sparse agentic tasks.
匹配关键词: VLM
---

[ACADEMIC - ARXIV]
标题: The Detector Teaches Itself: Lightweight Self-Supervised Adaptation for Open-Vocabulary Object Detection
作者: Yazhe Wan, Changjae Oh
链接: https://arxiv.org/abs/2605.03642v1
完整摘要: Open-vocabulary object detection aims to recognize objects from an open set of categories, which leverages vision-language models (VLMs) pre-trained on large-scale image-text data. The cooperative paradigm combines an object detector with a VLM to achieve zero-shot recognition of novel objects. However, VLMs pre-trained on full images often struggle to capture local object details, limiting their effectiveness when applied to region-level detection. We present Decoupled Adaptivity Training (DAT), a self-supervised fine-tuning approach to improve VLMs for cooperative model-based object detection. Given a cooperative model consists of a closed-set detector and a VLM, we first construct a region-aware pseudo-labeled dataset using a pre-trained closed-set object detector, in which regions corresponding to novel objects may be present but remain unlabeled or mislabeled. We then fine-tune the visual backbone of the VLM in a decoupled manner, which enhances local feature alignment while preserving global semantic knowledge via weight interpolation. DAT is a plug-and-play module that requires no inference overhead and fine-tunes less than 0.8M parameters. Experiments on the COCO and LVIS datasets show that DAT consistently improves detection performance on both novel and known categories, establishing a new state of the art in cooperative open-vocabulary detection.
匹配关键词: VLM
---

[ACADEMIC - ARXIV]
标题: Feature-Augmented Transformers for Robust AI-Text Detection Across Domains and Generators
作者: Mohamed Mady, Johannes Reschke, Björn Schuller
链接: https://arxiv.org/abs/2605.03969v1
完整摘要: AI-generated text is nowadays produced at scale across domains and heterogeneous generation pipelines, making robustness to distribution shift a central requirement for supervised binary detectors. We train transformer-based detectors on HC3 PLUS and calibrate a single decision threshold by maximising balanced accuracy on held-out validation; this threshold is then kept fixed for all downstream test distributions, revealing domain- and generator-dependent error asymmetries under shift. We evaluate in-domain on HC3 PLUS, under cross-dataset transfer to the multi-domain, multi-generator M4 benchmark, and on the external AI-Text-Detection-Pile. Although base models achieve near-ceiling in-domain performance (up to 99.5% balanced accuracy), performance under shift is brittle and strongly model-dependent. Feature augmentation via attention-based linguistic feature fusion improves transfer, with our best model (DeBERTa-v3-base+FeatAttn) achieving 85.9% balanced accuracy on M4. Multi-seed experiments confirm high stability. Under the same fixed-threshold protocol, our model outperforms strong zero-shot baselines by up to +7.22 points. Category-level ablations further show that readability and vocabulary features contribute most to robustness under shift. Overall, these results demonstrate that feature augmentation and a modern DeBERTa backbone significantly outperform earlier BERT/RoBERTa models, while the fixed-threshold protocol provides a more realistic and informative assessment of practical detector robustness.
匹配关键词: image generation
---

[ACADEMIC - ARXIV]
标题: Label-Efficient School Detection from Aerial Imagery via Weakly Supervised Pretraining and Fine-Tuning
作者: Zakarya Elmimouni, Fares Fourati, Mohamed-Slim Alouini
链接: https://arxiv.org/abs/2605.03968v1
完整摘要: Accurate school detection is essential for supporting education initiatives, including infrastructure planning and expanding internet connectivity to underserved areas. However, many regions around the world face challenges due to outdated, incomplete, or unavailable official records. Manual mapping efforts, while valuable, are labor-intensive and lack scalability across large geographic areas. To address this, we propose a weakly supervised framework for school detection from aerial imagery that minimizes the need for human annotations while supporting global mapping efforts. Our method is specifically designed for low-data regimes, where manual annotations are extremely scarce. We introduce an automatic labeling pipeline that leverages sparse location points and semantic segmentation to generate infrastructure masks from which we generate bounding boxes. Using these automatically labeled images, we train our detectors on a first training stage to learn a representation of what schools look like, then using a small set of manually labeled images, we fine-tune the previously trained models on this clean dataset. This two stage training pipeline enables large-scale and strong detection in low-data setting of school infrastructure with minimal supervision. Our results demonstrate strong object detection performance, particularly in the low-data regime, where the models achieve promising results using only 50 manually labeled images, significantly reducing the need for costly annotations. This framework supports education and connectivity initiatives worldwide by providing an efficient and extensible approach to mapping schools from space. All models, training code and auto-labeled data will be publicly released to foster future research and real-world impact.
匹配关键词: image generation
---

[ACADEMIC - ARXIV]
标题: Inconsistent Databases and Argumentation Frameworks with Collective Attacks
作者: Yasir Mahmood, Jonni Virtema, Timon Barlag, Axel-Cyrille Ngonga Ngomo
链接: https://arxiv.org/abs/2605.03954v1
完整摘要: The connection between subset-maximal repairs for inconsistent databases involving various integrity constraints and acceptable sets of arguments within argumentation frameworks has recently drawn growing interest. In this paper, we contribute to this domain by establishing a new connection when integrity constraints (ICs) include denial constraints and local-as-view tuple-generating dependencies. It turns out that SET-based Argumentation Frameworks (SETAFs), an extension of Dung's argumentation frameworks (AFs) allowing collective attacks, are needed. It is known that subset-maximal repairs under denial constraints correspond to the naive extensions, which also coincide with the preferred and stable extensions in the resulting SETAFs. Our main findings establish that repairs under the considered fragment of tuple-generating dependencies correspond to the preferred extensions. Moreover, for these dependencies, additional preprocessing allows computing a unique extension that is stable and naive. Allowing both types of constraints breaks this relationship, and even the pre-processing does not help as only preferred semantics captures these repairs. Finally, while it is known that functional dependencies do not require set-based attacks, we prove the same regarding inclusion dependencies. Thus, one can translate inconsistent databases under these restricted classes of ICs to plain AFs with attacks only between arguments.
匹配关键词: image generation
---

[ACADEMIC - ARXIV]
标题: UnAC: Adaptive Visual Prompting with Abstraction and Stepwise Checking for Complex Multimodal Reasoning
作者: Yifan Wang, Yun Fu
链接: https://arxiv.org/abs/2605.03950v1
完整摘要: Although recent LMMs have become much stronger at visual perception, they remain unreliable on problems that require multi-step reasoning over visual evidence. In this paper, we present UnAC (Understanding, Abstracting, and Checking), a multimodal prompting method that strengthens reasoning for complex multimodal tasks in LMMs (e.g., GPT-4o, Gemini 1.5, and GPT-4V). To improve image understanding and capture fine details, we propose an adaptive visual prompting strategy that enables LMMs to focus on salient regions. We further design an image-abstraction prompt to effectively extract key information from images. In addition, we introduce a gradual self-checking scheme that improves reasoning by verifying each decomposed subquestion and its answer. Extensive experiments on three public benchmarks-MathVista, MM-Vet, and MMMU.
匹配关键词: image generation
---

[ACADEMIC - ARXIV]
标题: Reservoir property image slices from the Groningen gas field for image translation and segmentation
作者: Abdulrahman Al-Fakih, Nabil Sariah, Ardiansyah Koeshidayatullah, SanLinn I. Kaka
链接: https://arxiv.org/abs/2605.03942v1
完整摘要: Reservoir characterization workflows increasingly rely on image-based and machine-learning/deep learning or even generative AI approaches, but openly available geological image datasets suitable for reproducible benchmarking remain limited. Here we describe a high-resolution dataset of reservoir-property image slices derived from the Groningen static geological model. The dataset contains aligned two-dimensional PNG images representing facies, porosity, permeability, and water saturation, generated from three-dimensional reservoir grids and prepared for downstream visualization, segmentation, and image-to-image translation tasks. In addition to the deposited original image corpus, we provide an archived software workflow for reproducing augmentation, mask generation, paired-image construction, and example baseline experiments. The resource is designed to support benchmarking of geological image analysis methods and the study of cross-domain relationships among reservoir properties. By separating the fixed image dataset from the reproducible processing workflow, this work provides a transparent foundation for reuse in geoscience, reservoir modeling, and machine-learning applications.
匹配关键词: image generation
---

[ACADEMIC - ARXIV]
标题: Feature-Augmented Transformers for Robust AI-Text Detection Across Domains and Generators
作者: Mohamed Mady, Johannes Reschke, Björn Schuller
链接: https://arxiv.org/abs/2605.03969v1
完整摘要: AI-generated text is nowadays produced at scale across domains and heterogeneous generation pipelines, making robustness to distribution shift a central requirement for supervised binary detectors. We train transformer-based detectors on HC3 PLUS and calibrate a single decision threshold by maximising balanced accuracy on held-out validation; this threshold is then kept fixed for all downstream test distributions, revealing domain- and generator-dependent error asymmetries under shift. We evaluate in-domain on HC3 PLUS, under cross-dataset transfer to the multi-domain, multi-generator M4 benchmark, and on the external AI-Text-Detection-Pile. Although base models achieve near-ceiling in-domain performance (up to 99.5% balanced accuracy), performance under shift is brittle and strongly model-dependent. Feature augmentation via attention-based linguistic feature fusion improves transfer, with our best model (DeBERTa-v3-base+FeatAttn) achieving 85.9% balanced accuracy on M4. Multi-seed experiments confirm high stability. Under the same fixed-threshold protocol, our model outperforms strong zero-shot baselines by up to +7.22 points. Category-level ablations further show that readability and vocabulary features contribute most to robustness under shift. Overall, these results demonstrate that feature augmentation and a modern DeBERTa backbone significantly outperform earlier BERT/RoBERTa models, while the fixed-threshold protocol provides a more realistic and informative assessment of practical detector robustness.
匹配关键词: video generation
---

[ACADEMIC - ARXIV]
标题: Label-Efficient School Detection from Aerial Imagery via Weakly Supervised Pretraining and Fine-Tuning
作者: Zakarya Elmimouni, Fares Fourati, Mohamed-Slim Alouini
链接: https://arxiv.org/abs/2605.03968v1
完整摘要: Accurate school detection is essential for supporting education initiatives, including infrastructure planning and expanding internet connectivity to underserved areas. However, many regions around the world face challenges due to outdated, incomplete, or unavailable official records. Manual mapping efforts, while valuable, are labor-intensive and lack scalability across large geographic areas. To address this, we propose a weakly supervised framework for school detection from aerial imagery that minimizes the need for human annotations while supporting global mapping efforts. Our method is specifically designed for low-data regimes, where manual annotations are extremely scarce. We introduce an automatic labeling pipeline that leverages sparse location points and semantic segmentation to generate infrastructure masks from which we generate bounding boxes. Using these automatically labeled images, we train our detectors on a first training stage to learn a representation of what schools look like, then using a small set of manually labeled images, we fine-tune the previously trained models on this clean dataset. This two stage training pipeline enables large-scale and strong detection in low-data setting of school infrastructure with minimal supervision. Our results demonstrate strong object detection performance, particularly in the low-data regime, where the models achieve promising results using only 50 manually labeled images, significantly reducing the need for costly annotations. This framework supports education and connectivity initiatives worldwide by providing an efficient and extensible approach to mapping schools from space. All models, training code and auto-labeled data will be publicly released to foster future research and real-world impact.
匹配关键词: video generation
---

[ACADEMIC - ARXIV]
标题: Inconsistent Databases and Argumentation Frameworks with Collective Attacks
作者: Yasir Mahmood, Jonni Virtema, Timon Barlag, Axel-Cyrille Ngonga Ngomo
链接: https://arxiv.org/abs/2605.03954v1
完整摘要: The connection between subset-maximal repairs for inconsistent databases involving various integrity constraints and acceptable sets of arguments within argumentation frameworks has recently drawn growing interest. In this paper, we contribute to this domain by establishing a new connection when integrity constraints (ICs) include denial constraints and local-as-view tuple-generating dependencies. It turns out that SET-based Argumentation Frameworks (SETAFs), an extension of Dung's argumentation frameworks (AFs) allowing collective attacks, are needed. It is known that subset-maximal repairs under denial constraints correspond to the naive extensions, which also coincide with the preferred and stable extensions in the resulting SETAFs. Our main findings establish that repairs under the considered fragment of tuple-generating dependencies correspond to the preferred extensions. Moreover, for these dependencies, additional preprocessing allows computing a unique extension that is stable and naive. Allowing both types of constraints breaks this relationship, and even the pre-processing does not help as only preferred semantics captures these repairs. Finally, while it is known that functional dependencies do not require set-based attacks, we prove the same regarding inclusion dependencies. Thus, one can translate inconsistent databases under these restricted classes of ICs to plain AFs with attacks only between arguments.
匹配关键词: video generation
---

[ACADEMIC - ARXIV]
标题: Reservoir property image slices from the Groningen gas field for image translation and segmentation
作者: Abdulrahman Al-Fakih, Nabil Sariah, Ardiansyah Koeshidayatullah, SanLinn I. Kaka
链接: https://arxiv.org/abs/2605.03942v1
完整摘要: Reservoir characterization workflows increasingly rely on image-based and machine-learning/deep learning or even generative AI approaches, but openly available geological image datasets suitable for reproducible benchmarking remain limited. Here we describe a high-resolution dataset of reservoir-property image slices derived from the Groningen static geological model. The dataset contains aligned two-dimensional PNG images representing facies, porosity, permeability, and water saturation, generated from three-dimensional reservoir grids and prepared for downstream visualization, segmentation, and image-to-image translation tasks. In addition to the deposited original image corpus, we provide an archived software workflow for reproducing augmentation, mask generation, paired-image construction, and example baseline experiments. The resource is designed to support benchmarking of geological image analysis methods and the study of cross-domain relationships among reservoir properties. By separating the fixed image dataset from the reproducible processing workflow, this work provides a transparent foundation for reuse in geoscience, reservoir modeling, and machine-learning applications.
匹配关键词: video generation
---

[ACADEMIC - ARXIV]
标题: A Benchmark for Interactive World Models with a Unified Action Generation Framework
作者: Jianjie Fang, Yingshan Lei, Qin Wan, Ziyou Wang, Yuchao Huang, Yongyan Xu, Baining Zhao, Weichen Zhang, Chen Gao, Xinlei Chen, Yong Li
链接: https://arxiv.org/abs/2605.03941v1
完整摘要: Achieving Artificial General Intelligence (AGI) requires agents that learn and interact adaptively, with interactive world models providing scalable environments for perception, reasoning, and action. Yet current research still lacks large-scale datasets and unified benchmarks to evaluate their physical interaction capabilities. To address this, we propose iWorld-Bench, a comprehensive benchmark for training and testing world models on interaction-related abilities such as distance perception and memory. We construct a diverse dataset with 330k video clips and select 2.1k high-quality samples covering varied perspectives, weather, and scenes. As existing world models differ in interaction modalities, we introduce an Action Generation Framework to unify evaluation and design six task types, generating 4.9k test samples. These tasks jointly assess model performance across visual generation, trajectory following, and memory. Evaluating 14 representative world models, we identify key limitations and provide insights for future research. The iWorld-Bench model leaderboard is publicly available at iWorld-Bench.com.
匹配关键词: video generation
---

[ACADEMIC - ARXIV]
标题: Logical Consistency as a Bridge: Improving LLM Hallucination Detection via Label Constraint Modeling between Responses and Self-Judgments
作者: Hao Mi, Qiang Sheng, Shaofei Wang, Beizhe Hu, Yifan Sun, Zhengjia Wang, Hengqi Zeng, Yang Li, Danding Wang, Juan Cao
链接: https://arxiv.org/abs/2605.03971v1
完整摘要: Large Language Models (LLMs) are prone to factual hallucinations, risking their reliability in real-world applications. Existing hallucination detectors mainly extract micro-level intrinsic patterns for uncertainty quantification or elicit macro-level self-judgments through verbalized prompts. However, these methods address only a single facet of the hallucination, focusing either on implicit neural uncertainty or explicit symbolic reasoning, thereby treating these inherently coupled behaviors in isolation and failing to exploit their interdependence for a holistic view. In this paper, we propose LaaB (Logical Consistency-as-a-Bridge), a framework that bridges neural features and symbolic judgments for hallucination detection. LaaB introduces a "meta-judgment" process to map symbolic labels back into the feature space. By leveraging the inherent logical bridge where response and meta-judgment labels are either the same or opposite based on the self-judgment's semantics, LaaB aligns and integrates dual-view signals via mutual learning and enhances the hallucination detection. Extensive experiments on 4 public datasets, across 4 LLMs, against 8 baselines demonstrate the superiority of LaaB.
匹配关键词: visual reasoning
---

[ACADEMIC - ARXIV]
标题: UnAC: Adaptive Visual Prompting with Abstraction and Stepwise Checking for Complex Multimodal Reasoning
作者: Yifan Wang, Yun Fu
链接: https://arxiv.org/abs/2605.03950v1
完整摘要: Although recent LMMs have become much stronger at visual perception, they remain unreliable on problems that require multi-step reasoning over visual evidence. In this paper, we present UnAC (Understanding, Abstracting, and Checking), a multimodal prompting method that strengthens reasoning for complex multimodal tasks in LMMs (e.g., GPT-4o, Gemini 1.5, and GPT-4V). To improve image understanding and capture fine details, we propose an adaptive visual prompting strategy that enables LMMs to focus on salient regions. We further design an image-abstraction prompt to effectively extract key information from images. In addition, we introduce a gradual self-checking scheme that improves reasoning by verifying each decomposed subquestion and its answer. Extensive experiments on three public benchmarks-MathVista, MM-Vet, and MMMU.
匹配关键词: visual reasoning
---

[ACADEMIC - ARXIV]
标题: Reservoir property image slices from the Groningen gas field for image translation and segmentation
作者: Abdulrahman Al-Fakih, Nabil Sariah, Ardiansyah Koeshidayatullah, SanLinn I. Kaka
链接: https://arxiv.org/abs/2605.03942v1
完整摘要: Reservoir characterization workflows increasingly rely on image-based and machine-learning/deep learning or even generative AI approaches, but openly available geological image datasets suitable for reproducible benchmarking remain limited. Here we describe a high-resolution dataset of reservoir-property image slices derived from the Groningen static geological model. The dataset contains aligned two-dimensional PNG images representing facies, porosity, permeability, and water saturation, generated from three-dimensional reservoir grids and prepared for downstream visualization, segmentation, and image-to-image translation tasks. In addition to the deposited original image corpus, we provide an archived software workflow for reproducing augmentation, mask generation, paired-image construction, and example baseline experiments. The resource is designed to support benchmarking of geological image analysis methods and the study of cross-domain relationships among reservoir properties. By separating the fixed image dataset from the reproducible processing workflow, this work provides a transparent foundation for reuse in geoscience, reservoir modeling, and machine-learning applications.
匹配关键词: visual reasoning
---

[ACADEMIC - ARXIV]
标题: A Benchmark for Interactive World Models with a Unified Action Generation Framework
作者: Jianjie Fang, Yingshan Lei, Qin Wan, Ziyou Wang, Yuchao Huang, Yongyan Xu, Baining Zhao, Weichen Zhang, Chen Gao, Xinlei Chen, Yong Li
链接: https://arxiv.org/abs/2605.03941v1
完整摘要: Achieving Artificial General Intelligence (AGI) requires agents that learn and interact adaptively, with interactive world models providing scalable environments for perception, reasoning, and action. Yet current research still lacks large-scale datasets and unified benchmarks to evaluate their physical interaction capabilities. To address this, we propose iWorld-Bench, a comprehensive benchmark for training and testing world models on interaction-related abilities such as distance perception and memory. We construct a diverse dataset with 330k video clips and select 2.1k high-quality samples covering varied perspectives, weather, and scenes. As existing world models differ in interaction modalities, we introduce an Action Generation Framework to unify evaluation and design six task types, generating 4.9k test samples. These tasks jointly assess model performance across visual generation, trajectory following, and memory. Evaluating 14 representative world models, we identify key limitations and provide insights for future research. The iWorld-Bench model leaderboard is publicly available at iWorld-Bench.com.
匹配关键词: visual reasoning
---

[ACADEMIC - ARXIV]
标题: The Counterexample Game: Iterated Conceptual Analysis and Repair in Language Models
作者: Daniel Drucker, Kyle Mahowald
链接: https://arxiv.org/abs/2605.03936v1
完整摘要: Conceptual analysis -- proposing definitions and refining them through counterexamples -- is central to philosophical methodology. We study whether language models can perform this task through iterated analysis and repair chains: one model instance generates counterexamples to a proposed definition, another repairs the definition, and the process repeats. Across 20 concepts and thousands of counterexample-repair cycles, we find that, although many LM-generated counterexamples are judged invalid by both expert humans and an LM judge, the LM judge accepts roughly twice as many as humans do. Nonetheless, per-item validity judgments are moderately consistent across humans and between humans and the LM. We further find that extended iteration produces increasingly verbose definitions without improving accuracy. We also see that some concepts resist stable definitions in general. These findings suggest that while LMs can engage in philosophical reasoning, the counterexample-repair loop hits diminishing returns quickly and could be a fruitful test case for evaluating whether LMs can sustain high-level iterated philosophical reasoning.
匹配关键词: visual reasoning
---

[ACADEMIC - ARXIV]
标题: Feature-Augmented Transformers for Robust AI-Text Detection Across Domains and Generators
作者: Mohamed Mady, Johannes Reschke, Björn Schuller
链接: https://arxiv.org/abs/2605.03969v1
完整摘要: AI-generated text is nowadays produced at scale across domains and heterogeneous generation pipelines, making robustness to distribution shift a central requirement for supervised binary detectors. We train transformer-based detectors on HC3 PLUS and calibrate a single decision threshold by maximising balanced accuracy on held-out validation; this threshold is then kept fixed for all downstream test distributions, revealing domain- and generator-dependent error asymmetries under shift. We evaluate in-domain on HC3 PLUS, under cross-dataset transfer to the multi-domain, multi-generator M4 benchmark, and on the external AI-Text-Detection-Pile. Although base models achieve near-ceiling in-domain performance (up to 99.5% balanced accuracy), performance under shift is brittle and strongly model-dependent. Feature augmentation via attention-based linguistic feature fusion improves transfer, with our best model (DeBERTa-v3-base+FeatAttn) achieving 85.9% balanced accuracy on M4. Multi-seed experiments confirm high stability. Under the same fixed-threshold protocol, our model outperforms strong zero-shot baselines by up to +7.22 points. Category-level ablations further show that readability and vocabulary features contribute most to robustness under shift. Overall, these results demonstrate that feature augmentation and a modern DeBERTa backbone significantly outperform earlier BERT/RoBERTa models, while the fixed-threshold protocol provides a more realistic and informative assessment of practical detector robustness.
匹配关键词: embodied AI
---

[ACADEMIC - ARXIV]
标题: Reservoir property image slices from the Groningen gas field for image translation and segmentation
作者: Abdulrahman Al-Fakih, Nabil Sariah, Ardiansyah Koeshidayatullah, SanLinn I. Kaka
链接: https://arxiv.org/abs/2605.03942v1
完整摘要: Reservoir characterization workflows increasingly rely on image-based and machine-learning/deep learning or even generative AI approaches, but openly available geological image datasets suitable for reproducible benchmarking remain limited. Here we describe a high-resolution dataset of reservoir-property image slices derived from the Groningen static geological model. The dataset contains aligned two-dimensional PNG images representing facies, porosity, permeability, and water saturation, generated from three-dimensional reservoir grids and prepared for downstream visualization, segmentation, and image-to-image translation tasks. In addition to the deposited original image corpus, we provide an archived software workflow for reproducing augmentation, mask generation, paired-image construction, and example baseline experiments. The resource is designed to support benchmarking of geological image analysis methods and the study of cross-domain relationships among reservoir properties. By separating the fixed image dataset from the reproducible processing workflow, this work provides a transparent foundation for reuse in geoscience, reservoir modeling, and machine-learning applications.
匹配关键词: embodied AI
---

[ACADEMIC - ARXIV]
标题: Atomic Fact-Checking Increases Clinician Trust in Large Language Model Recommendations for Oncology Decision Support: A Randomized Controlled Trial
作者: Lisa C. Adams, Linus Marx, Erik Thiele Orberg, Keno Bressem, Sebastian Ziegelmayer, Denise Bernhardt, Markus Graf, Marcus R. Makowski, Stephanie E. Combs, Florian Matthes, Jan C. Peeken
链接: https://arxiv.org/abs/2605.03916v1
完整摘要: Question: Does atomic fact-checking, which decomposes AI treatment recommendations into individually verifiable claims linked to source guideline documents, increase clinician trust compared to traditional explainability approaches? Findings: In this randomized trial of 356 clinicians generating 7,476 trust ratings, atomic fact-checking produced a large effect on trust (Cohen's d = 0.94), increasing the proportion of clinicians expressing trust from 26.9% to 66.5%. Traditional transparency mechanisms showed a dose-response gradient of improvement over baseline (d = 0.25 to 0.50). Meaning: Decomposing AI recommendations into individually verifiable claims linked to source guidelines produces substantially higher clinician trust than traditional explainability approaches in high-stakes clinical decisions.
匹配关键词: embodied AI
---

[ACADEMIC - ARXIV]
标题: Contextual Multi-Objective Optimization: Rethinking Objectives in Frontier AI Systems
作者: Jie Zhou, Qin Chen, Liang He
链接: https://arxiv.org/abs/2605.03900v1
完整摘要: Frontier AI systems perform best in settings with clear, stable, and verifiable objectives, such as code generation, mathematical reasoning, games, and unit-test-driven tasks. They remain less reliable in open-ended settings, including scientific assistance, long-horizon agents, high-stakes advice, personalization, and tool use, where the relevant objective is ambiguous, context-dependent, delayed, or only partially observable. We argue that many such failures are not merely failures of scale or capability, but failures of objective selection: the system optimizes a locally visible signal while missing which objectives should govern the interaction. We formulate this problem as \emph{contextual multi-objective optimization}. In this setting, systems must consider multiple, context-dependent objectives, such as helpfulness, truthfulness, safety, privacy, calibration, non-manipulation, user preference, reversibility, and stakeholder impact, while determining which objectives are active, which are soft preferences, and which must function as hard or quasi-hard constraints. These examples are not intended as an exhaustive taxonomy: different domains and deployment settings may activate different objective dimensions and different conflict-resolution procedures. Our framework models AI behavior as a context-dependent choice rule over candidate actions, objective estimates, active constraints, stakeholders, uncertainty, and conflict-resolution procedures. We outline an implementation pathway based on decomposed objective representations, context-to-objective routing, hierarchical constraints, deliberative policy reasoning, controlled personalization, tool-use control, diagnostic evaluation, auditing, and post-deployment revision.
匹配关键词: embodied AI
---

[ACADEMIC - ARXIV]
标题: Deco: Extending Personal Physical Objects into Pervasive AI Companion through a Dual-Embodiment Framework
作者: Zhihan Jiang, Mengyuan Millie Wu, Ruishi Zou, Shiyu Xu, Xun Qian, Emma Macmanus, Steven Liao, Ping Zhang, Bingsheng Yao, Tingyu Cheng, James L. David, Nabila El-Bassel, Lena Mamykina, Frances R. Levin, Ryan Sultan, Dakuo Wang, Xuhai Xu
链接: https://arxiv.org/abs/2605.03882v1
完整摘要: Individuals frequently form deep attachments to physical objects (e.g., plush toys) that usually cannot sense or respond to their emotions. While AI companions offer responsiveness and personalization, they exist independently of these physical objects and lack an ongoing connection to them. To bridge this gap, we conducted a formative study (N=9) to explore how digital agents could inherit and extend the emotional bond, deriving four design principles (Faithful Identity, Calibrated Agency, Ambient Presence, and Reciprocal Memory). We then present the Dual-Embodiment Companion Framework, instantiated as Deco, a mobile system integrating multimodal Large Language Models (LLMs) and Augmented Reality to create synchronized digital embodiments of users' physical companions. A within-subjects study (N=25) showed Deco significantly outperformed a personalized LLM-empowered digital companion baseline on perceived companionship, emotional bond, and design-principle scales (all p<0.01). A seven-day field deployment (N=17) showed sustained engagement, subjective well-being improvement (p=.040), and three key relational patterns: digital activities retroactively vitalized physical objects, bond deepening was driven by emotional engagement depth rather than interaction frequency, and users sustained bonds while actively navigating digital companions' AI nature. This work highlights a promising alternative for designing digital companions: moving from creating new relationships to dual embodiment, where digital agents seamlessly extend the emotional history of physical objects.
匹配关键词: embodied AI
---

[ACADEMIC - ARXIV]
标题: StateVLM: A State-Aware Vision-Language Model for Robotic Affordance Reasoning
作者: Xiaowen Sun, Matthias Kerzel, Mengdi Li, Xufeng Zhao, Paul Striker, Stefan Wermter
链接: https://arxiv.org/abs/2605.03927v1
完整摘要: Vision-language models (VLMs) have shown remarkable performance in various robotic tasks, as they can perceive visual information and understand natural language instructions. However, when applied to robotics, VLMs remain subject to a fundamental limitation inherent in large language models (LLMs): they struggle with numerical reasoning, particularly in object detection and object-state localization. To explore numerical reasoning as a regression task in VLMs, we propose a novel training strategy to adapt VLMs for object detection and object-state localization. This approach leverages box decoder outputs to compute an Auxiliary Regression Loss (ARL) during fine-tuning, while preserving standard sequence prediction at inference. We leverage this training strategy to develop StateVLM (State-aware Vision-Language Model), a novel model designed to perceive and learn fine-grained object representations, including precise localization of objects and their states, as well as graspable regions. Due to the lack of a benchmark for object-state affordance reasoning, we introduce an open-source benchmark, Object State Affordance Reasoning (OSAR), which contains 1,172 scenes with 7,746 individual objects and corresponding bounding boxes. Comparative experiments on adapted benchmarks (RefCOCO, RefCOCO+, and \mbox{RefCOCOg}) demonstrate that ARL improves model performance by an average of 1.6\% compared to models without ARL. Experiments on the OSAR benchmark further support this finding, showing that StateVLM with ARL achieves an average of 5.2\% higher performance than models without ARL. In particular, ARL is also important for the complex task of affordance reasoning in OSAR, where it enhances the consistency of model outputs.
匹配关键词: robotics
---

[ACADEMIC - ARXIV]
标题: Task-Aware Scanning Parameter Configuration for Robotic Inspection Using Vision Language Embeddings and Hyperdimensional Computing
作者: Zhiling Chen, David Gorsich, Matthew P. Castanier, Yang Zhang, Jiong Tang, Farhad Imani
链接: https://arxiv.org/abs/2605.03909v1
完整摘要: Robotic laser profiling is widely used for dimensional verification and surface inspection, yet measurement fidelity is often dominated by sensor configuration rather than robot motion. Industrial profilers expose multiple coupled parameters, including sampling frequency, measurement range, exposure time, receiver dynamic range, and illumination, that are still tuned by trial-and-error; mismatches can cause saturation, clipping, or missing returns that cannot be recovered downstream. We formulate instruction-conditioned sensing parameter recommendation; given a pre-scan RGB observation and a natural-language inspection instruction, infer a discrete configuration over key parameters of a robot-mounted profiler. To benchmark this problem, we develop Instruct-Obs2Param, a real-world multimodal dataset linking inspection intents and multi-view pose and illumination variation across 16 objects to canonical parameter regimes. We then propose ScanHD, a hyperdimensional computing framework that binds instruction and observation into a task-aware code and performs parameter-wise associative reasoning with compact memories, matching discrete scanner regimes while yielding stable, interpretable, low-latency decisions. On Instruct-Obs2Param, ScanHD achieves 92.7% average exact accuracy and 98.1% average Win@1 accuracy across the five parameters, with strong cross-split generalization and low-latency inference suitable for deployment, outperforming rule-based heuristics, conventional multimodal models, and multimodal large language models. This work enables autonomous, instruction-conditioned sensing configuration from task intent and scene context, eliminating manual tuning and elevating sensor configuration from a static setting to an adaptive decision variable.
匹配关键词: robotics
---

[ACADEMIC - ARXIV]
标题: Evaluating Generative Models as Interactive Emergent Representations of Human-Like Collaborative Behavior
作者: Shinas Shaji, Teena Chakkalayil Hassan, Sebastian Houben, Alex Mitrevski
链接: https://arxiv.org/abs/2605.03855v1
完整摘要: Human-AI collaboration requires AI agents to understand human behavior for effective coordination. While advances in foundation models show promising capabilities in understanding and showing human-like behavior, their application in embodied collaborative settings needs further investigation. This work examines whether embodied foundation model agents exhibit emergent collaborative behaviors indicating underlying mental models of their collaborators, which is an important aspect of effective coordination. This paper develops a 2D collaborative game environment where large language model agents and humans complete color-matching tasks requiring coordination. We define five collaborative behaviors as indicators of emergent mental model representation: perspective-taking, collaborator-aware planning, introspection, theory of mind, and clarification. An automated behavior detection system using LLM-based judges identifies these behaviors, achieving fair to substantial agreement with human annotations. Results from the automated behavior detection system show that foundation models consistently exhibit emergent collaborative behaviors without being explicitly trained to do so. These behaviors occur at varying frequencies during collaboration stages, with distinct patterns across different LLMs. A user study was also conducted to evaluate human satisfaction and perceived collaboration effectiveness, with the results indicating positive collaboration experiences. Participants appreciated the agents' task focus, plan verbalization, and initiative, while suggesting improvements in response times and human-like interactions. This work provides an experimental framework for human-AI collaboration, empirical evidence of collaborative behaviors in embodied LLM agents, a validated behavioral analysis methodology, and an assessment of collaboration effectiveness.
匹配关键词: robotics
---

[ACADEMIC - ARXIV]
标题: SigLoMa: Learning Open-World Quadrupedal Loco-Manipulation from Ego-Centric Vision
作者: Shiyi Chen, Haiyi Liu, Mingye Yang, Jiaqi Zhang, Debing Zhang
链接: https://arxiv.org/abs/2605.03846v1
完整摘要: Designing an open-world quadrupedal loco-manipulation system is highly challenging. Traditional reinforcement learning frameworks utilizing exteroception often suffer from extreme sample inefficiency and massive sim-to-real gaps. Furthermore, the inherent latency of visual tracking fundamentally conflicts with the high-frequency demands of precise floating-base control. Consequently, existing systems lean heavily on expensive external motion capture and off-board computation. To eliminate these dependencies, we present SigLoMa, a fully onboard, ego-centric vision-based pick-and-place framework. At the core of SigLoMa is the introduction of Sigma Points, a lightweight geometric representation for exteroception that guarantees high scalability and native sim-to-real alignment. To bridge the frequency divide between slow perception and fast control, we design an ego-centric Kalman Filter to provide robust, high-rate state estimation. On the learning front, we alleviate sample inefficiency via an Active Sampling Curriculum guided by Hint Poses, and tackle the robot's structural visual blind spots using temporal encoding coupled with simulated random-walk drift. Real-world experiments validate that, relying solely on a 5Hz (200 ms latency) open-vocabulary detector, SigLoMa successfully executes dynamic loco-manipulation across multiple tasks, achieving performance comparable to expert human teleoperation.
匹配关键词: robotics
---

[ACADEMIC - ARXIV]
标题: SOAR: Real-Time Joint Optimization of Order Allocation and Robot Scheduling in Robotic Mobile Fulfillment Systems
作者: Yibang Tang, Yifan Yang, Jingyuan Wang, Junhua Chen, Zhen Zhao
链接: https://arxiv.org/abs/2605.03842v1
完整摘要: Robotic Mobile Fulfillment Systems (RMFS) rely on mobile robots for automated inventory transportation, coordinating order allocation and robot scheduling to enhance warehousing efficiency. However, optimizing RMFS is challenging due to strict real-time constraints and the strong coupling of multi-phase decisions. Existing methods either decompose the problem into isolated sub-tasks to guarantee responsiveness at the cost of global optimality, or rely on computationally expensive global optimization models that are unsuitable for dynamic industrial environments. To bridge this gap, we propose SOAR, a unified Deep Reinforcement Learning framework for real-time joint optimization. SOAR transforms order allocation and robot scheduling into a unified process by utilizing soft order allocations as observations. We formulate this as an Event-Driven Markov Decision Process, enabling the agent to perform simultaneous scheduling in response to asynchronous system events. Technically, we employ a Heterogeneous Graph Transformer to encode the warehouse state and integrate phased domain knowledge. Additionally, we incorporate a reward shaping strategy to address sparse feedback in long-horizon tasks. Extensive experiments on synthetic and real-world industrial datasets, in collaboration with Geekplus, demonstrate that SOAR reduces global makespan by 7.5\% and average order completion time by 15.4\% with sub-100ms latency. Furthermore, sim-to-real deployment confirms its practical viability and significant performance gains in production environments. The code is available at https://github.com/200815147/SOAR.
匹配关键词: robotics
---

[ACADEMIC - ARXIV]
标题: StateVLM: A State-Aware Vision-Language Model for Robotic Affordance Reasoning
作者: Xiaowen Sun, Matthias Kerzel, Mengdi Li, Xufeng Zhao, Paul Striker, Stefan Wermter
链接: https://arxiv.org/abs/2605.03927v1
完整摘要: Vision-language models (VLMs) have shown remarkable performance in various robotic tasks, as they can perceive visual information and understand natural language instructions. However, when applied to robotics, VLMs remain subject to a fundamental limitation inherent in large language models (LLMs): they struggle with numerical reasoning, particularly in object detection and object-state localization. To explore numerical reasoning as a regression task in VLMs, we propose a novel training strategy to adapt VLMs for object detection and object-state localization. This approach leverages box decoder outputs to compute an Auxiliary Regression Loss (ARL) during fine-tuning, while preserving standard sequence prediction at inference. We leverage this training strategy to develop StateVLM (State-aware Vision-Language Model), a novel model designed to perceive and learn fine-grained object representations, including precise localization of objects and their states, as well as graspable regions. Due to the lack of a benchmark for object-state affordance reasoning, we introduce an open-source benchmark, Object State Affordance Reasoning (OSAR), which contains 1,172 scenes with 7,746 individual objects and corresponding bounding boxes. Comparative experiments on adapted benchmarks (RefCOCO, RefCOCO+, and \mbox{RefCOCOg}) demonstrate that ARL improves model performance by an average of 1.6\% compared to models without ARL. Experiments on the OSAR benchmark further support this finding, showing that StateVLM with ARL achieves an average of 5.2\% higher performance than models without ARL. In particular, ARL is also important for the complex task of affordance reasoning in OSAR, where it enhances the consistency of model outputs.
匹配关键词: humanoid robot
---

[ACADEMIC - ARXIV]
标题: Task-Aware Scanning Parameter Configuration for Robotic Inspection Using Vision Language Embeddings and Hyperdimensional Computing
作者: Zhiling Chen, David Gorsich, Matthew P. Castanier, Yang Zhang, Jiong Tang, Farhad Imani
链接: https://arxiv.org/abs/2605.03909v1
完整摘要: Robotic laser profiling is widely used for dimensional verification and surface inspection, yet measurement fidelity is often dominated by sensor configuration rather than robot motion. Industrial profilers expose multiple coupled parameters, including sampling frequency, measurement range, exposure time, receiver dynamic range, and illumination, that are still tuned by trial-and-error; mismatches can cause saturation, clipping, or missing returns that cannot be recovered downstream. We formulate instruction-conditioned sensing parameter recommendation; given a pre-scan RGB observation and a natural-language inspection instruction, infer a discrete configuration over key parameters of a robot-mounted profiler. To benchmark this problem, we develop Instruct-Obs2Param, a real-world multimodal dataset linking inspection intents and multi-view pose and illumination variation across 16 objects to canonical parameter regimes. We then propose ScanHD, a hyperdimensional computing framework that binds instruction and observation into a task-aware code and performs parameter-wise associative reasoning with compact memories, matching discrete scanner regimes while yielding stable, interpretable, low-latency decisions. On Instruct-Obs2Param, ScanHD achieves 92.7% average exact accuracy and 98.1% average Win@1 accuracy across the five parameters, with strong cross-split generalization and low-latency inference suitable for deployment, outperforming rule-based heuristics, conventional multimodal models, and multimodal large language models. This work enables autonomous, instruction-conditioned sensing configuration from task intent and scene context, eliminating manual tuning and elevating sensor configuration from a static setting to an adaptive decision variable.
匹配关键词: humanoid robot
---

[ACADEMIC - ARXIV]
标题: SigLoMa: Learning Open-World Quadrupedal Loco-Manipulation from Ego-Centric Vision
作者: Shiyi Chen, Haiyi Liu, Mingye Yang, Jiaqi Zhang, Debing Zhang
链接: https://arxiv.org/abs/2605.03846v1
完整摘要: Designing an open-world quadrupedal loco-manipulation system is highly challenging. Traditional reinforcement learning frameworks utilizing exteroception often suffer from extreme sample inefficiency and massive sim-to-real gaps. Furthermore, the inherent latency of visual tracking fundamentally conflicts with the high-frequency demands of precise floating-base control. Consequently, existing systems lean heavily on expensive external motion capture and off-board computation. To eliminate these dependencies, we present SigLoMa, a fully onboard, ego-centric vision-based pick-and-place framework. At the core of SigLoMa is the introduction of Sigma Points, a lightweight geometric representation for exteroception that guarantees high scalability and native sim-to-real alignment. To bridge the frequency divide between slow perception and fast control, we design an ego-centric Kalman Filter to provide robust, high-rate state estimation. On the learning front, we alleviate sample inefficiency via an Active Sampling Curriculum guided by Hint Poses, and tackle the robot's structural visual blind spots using temporal encoding coupled with simulated random-walk drift. Real-world experiments validate that, relying solely on a 5Hz (200 ms latency) open-vocabulary detector, SigLoMa successfully executes dynamic loco-manipulation across multiple tasks, achieving performance comparable to expert human teleoperation.
匹配关键词: humanoid robot
---

[ACADEMIC - ARXIV]
标题: SOAR: Real-Time Joint Optimization of Order Allocation and Robot Scheduling in Robotic Mobile Fulfillment Systems
作者: Yibang Tang, Yifan Yang, Jingyuan Wang, Junhua Chen, Zhen Zhao
链接: https://arxiv.org/abs/2605.03842v1
完整摘要: Robotic Mobile Fulfillment Systems (RMFS) rely on mobile robots for automated inventory transportation, coordinating order allocation and robot scheduling to enhance warehousing efficiency. However, optimizing RMFS is challenging due to strict real-time constraints and the strong coupling of multi-phase decisions. Existing methods either decompose the problem into isolated sub-tasks to guarantee responsiveness at the cost of global optimality, or rely on computationally expensive global optimization models that are unsuitable for dynamic industrial environments. To bridge this gap, we propose SOAR, a unified Deep Reinforcement Learning framework for real-time joint optimization. SOAR transforms order allocation and robot scheduling into a unified process by utilizing soft order allocations as observations. We formulate this as an Event-Driven Markov Decision Process, enabling the agent to perform simultaneous scheduling in response to asynchronous system events. Technically, we employ a Heterogeneous Graph Transformer to encode the warehouse state and integrate phased domain knowledge. Additionally, we incorporate a reward shaping strategy to address sparse feedback in long-horizon tasks. Extensive experiments on synthetic and real-world industrial datasets, in collaboration with Geekplus, demonstrate that SOAR reduces global makespan by 7.5\% and average order completion time by 15.4\% with sub-100ms latency. Furthermore, sim-to-real deployment confirms its practical viability and significant performance gains in production environments. The code is available at https://github.com/200815147/SOAR.
匹配关键词: humanoid robot
---

[ACADEMIC - ARXIV]
标题: RoboAlign-R1: Distilled Multimodal Reward Alignment for Robot Video World Models
作者: Hao Wu, Yuqi Li, Yuan Gao, Fan Xu, Fan Zhang, Kun Wang, Penghao Zhao, Qiufeng Wang, Yizhou Zhao, Weiyan Wang, Yingli Tian, Xian Wu, Xiaomeng Huang
链接: https://arxiv.org/abs/2605.03821v1
完整摘要: Existing robot video world models are typically trained with low-level objectives such as reconstruction and perceptual similarity, which are poorly aligned with the capabilities that matter most for robot decision making, including instruction following, manipulation success, and physical plausibility. They also suffer from error accumulation in long-horizon autoregressive prediction. We present RoboAlign-R1, a framework that combines reward-aligned post-training with stabilized long-horizon inference for robot video world models. We construct RobotWorldBench, a benchmark of 10,000 annotated video-instruction pairs collected from four robot data sources, and train a multimodal teacher judge, RoboAlign-Judge, to provide fine-grained six-dimensional evaluation of generated videos. We then distill the teacher into a lightweight student reward model for efficient reinforcement-learning-based post-training. To reduce long-horizon rollout drift, we further introduce Sliding Window Re-encoding (SWR), a training-free inference strategy that periodically refreshes the generation context. Under our in-domain evaluation protocol, RoboAlign-R1 improves the aggregate six-dimension score by 10.1% over the strongest baseline, including gains of 7.5% on Manipulation Accuracy and 4.6% on Instruction Following; these ranking improvements are further supported by an external VLM-based cross-check and a blinded human study. Meanwhile, SWR improves long-horizon prediction quality with only about 1% additional latency, yielding a 2.8% gain in SSIM and a 9.8% reduction in LPIPS. Together, these results show that reward-aligned post-training and stabilized long-horizon decoding improve task consistency, physical realism, and long-horizon prediction quality in robot video world models.
匹配关键词: humanoid robot
---

[ACADEMIC - ARXIV]
标题: Contextual Multi-Objective Optimization: Rethinking Objectives in Frontier AI Systems
作者: Jie Zhou, Qin Chen, Liang He
链接: https://arxiv.org/abs/2605.03900v1
完整摘要: Frontier AI systems perform best in settings with clear, stable, and verifiable objectives, such as code generation, mathematical reasoning, games, and unit-test-driven tasks. They remain less reliable in open-ended settings, including scientific assistance, long-horizon agents, high-stakes advice, personalization, and tool use, where the relevant objective is ambiguous, context-dependent, delayed, or only partially observable. We argue that many such failures are not merely failures of scale or capability, but failures of objective selection: the system optimizes a locally visible signal while missing which objectives should govern the interaction. We formulate this problem as \emph{contextual multi-objective optimization}. In this setting, systems must consider multiple, context-dependent objectives, such as helpfulness, truthfulness, safety, privacy, calibration, non-manipulation, user preference, reversibility, and stakeholder impact, while determining which objectives are active, which are soft preferences, and which must function as hard or quasi-hard constraints. These examples are not intended as an exhaustive taxonomy: different domains and deployment settings may activate different objective dimensions and different conflict-resolution procedures. Our framework models AI behavior as a context-dependent choice rule over candidate actions, objective estimates, active constraints, stakeholders, uncertainty, and conflict-resolution procedures. We outline an implementation pathway based on decomposed objective representations, context-to-objective routing, hierarchical constraints, deliberative policy reasoning, controlled personalization, tool-use control, diagnostic evaluation, auditing, and post-deployment revision.
匹配关键词: manipulation
---

[ACADEMIC - ARXIV]
标题: SigLoMa: Learning Open-World Quadrupedal Loco-Manipulation from Ego-Centric Vision
作者: Shiyi Chen, Haiyi Liu, Mingye Yang, Jiaqi Zhang, Debing Zhang
链接: https://arxiv.org/abs/2605.03846v1
完整摘要: Designing an open-world quadrupedal loco-manipulation system is highly challenging. Traditional reinforcement learning frameworks utilizing exteroception often suffer from extreme sample inefficiency and massive sim-to-real gaps. Furthermore, the inherent latency of visual tracking fundamentally conflicts with the high-frequency demands of precise floating-base control. Consequently, existing systems lean heavily on expensive external motion capture and off-board computation. To eliminate these dependencies, we present SigLoMa, a fully onboard, ego-centric vision-based pick-and-place framework. At the core of SigLoMa is the introduction of Sigma Points, a lightweight geometric representation for exteroception that guarantees high scalability and native sim-to-real alignment. To bridge the frequency divide between slow perception and fast control, we design an ego-centric Kalman Filter to provide robust, high-rate state estimation. On the learning front, we alleviate sample inefficiency via an Active Sampling Curriculum guided by Hint Poses, and tackle the robot's structural visual blind spots using temporal encoding coupled with simulated random-walk drift. Real-world experiments validate that, relying solely on a 5Hz (200 ms latency) open-vocabulary detector, SigLoMa successfully executes dynamic loco-manipulation across multiple tasks, achieving performance comparable to expert human teleoperation.
匹配关键词: manipulation
---

[ACADEMIC - ARXIV]
标题: RoboAlign-R1: Distilled Multimodal Reward Alignment for Robot Video World Models
作者: Hao Wu, Yuqi Li, Yuan Gao, Fan Xu, Fan Zhang, Kun Wang, Penghao Zhao, Qiufeng Wang, Yizhou Zhao, Weiyan Wang, Yingli Tian, Xian Wu, Xiaomeng Huang
链接: https://arxiv.org/abs/2605.03821v1
完整摘要: Existing robot video world models are typically trained with low-level objectives such as reconstruction and perceptual similarity, which are poorly aligned with the capabilities that matter most for robot decision making, including instruction following, manipulation success, and physical plausibility. They also suffer from error accumulation in long-horizon autoregressive prediction. We present RoboAlign-R1, a framework that combines reward-aligned post-training with stabilized long-horizon inference for robot video world models. We construct RobotWorldBench, a benchmark of 10,000 annotated video-instruction pairs collected from four robot data sources, and train a multimodal teacher judge, RoboAlign-Judge, to provide fine-grained six-dimensional evaluation of generated videos. We then distill the teacher into a lightweight student reward model for efficient reinforcement-learning-based post-training. To reduce long-horizon rollout drift, we further introduce Sliding Window Re-encoding (SWR), a training-free inference strategy that periodically refreshes the generation context. Under our in-domain evaluation protocol, RoboAlign-R1 improves the aggregate six-dimension score by 10.1% over the strongest baseline, including gains of 7.5% on Manipulation Accuracy and 4.6% on Instruction Following; these ranking improvements are further supported by an external VLM-based cross-check and a blinded human study. Meanwhile, SWR improves long-horizon prediction quality with only about 1% additional latency, yielding a 2.8% gain in SSIM and a 9.8% reduction in LPIPS. Together, these results show that reward-aligned post-training and stabilized long-horizon decoding improve task consistency, physical realism, and long-horizon prediction quality in robot video world models.
匹配关键词: manipulation
---

[ACADEMIC - ARXIV]
标题: Sensorless State Estimation and Control for Agile Cable-Suspended Payload Transport by Quadrotors
作者: Ana Maria Nascimento, Augusto Sales, Antonio Marcus Lima, Tiago Nascimento
链接: https://arxiv.org/abs/2605.03666v1
完整摘要: This work proposes a novel control and estimation approach for aerial manipulation of a cable-suspended load using Unmanned Aerial Vehicles (UAVs). Common approaches in the state of the art have practical limitations, relying on direct load measurements and Lagrangian methods for dynamic modeling. The lack of a straightforward dynamic model of the system led us to propose adopting the Udwadia-Kalaba method to explicitly incorporate the cable's geometric constraints. This formulation allowed for the consistent derivation of the tension force and its direct integration into the NMPC prediction model. Additionally, we propose a sensorless load state estimation based on the same geometric constraints. Results from real-robot experiments demonstrated that the explicit inclusion of load dynamics in the optimization problem significantly reduces trajectory-tracking errors and yields better overall performance compared to strategies based on incomplete models.
匹配关键词: manipulation
---

[ACADEMIC - ARXIV]
标题: Bridging the Embodiment Gap: Disentangled Cross-Embodiment Video Editing
作者: Zhiyuan Li, Wenyan Yang, Wenshuai Zhao, Yue Ma, Yuanpeng Tu, Pekka Marttinen, Joni Pajarinen
链接: https://arxiv.org/abs/2605.03637v1
完整摘要: Learning robotic manipulation from human videos is a promising solution to the data bottleneck in robotics, but the distribution shift between humans and robots remains a critical challenge. Existing approaches often produce entangled representations, where task-relevant information is coupled with human-specific kinematics, limiting their adaptability. We propose a generative framework for cross-embodiment video editing that directly addresses this by learning explicitly disentangled task and embodiment representations. Our method factorizes a demonstration video into two orthogonal latent spaces by enforcing a dual contrastive objective: it minimizes mutual information between the spaces to ensure independence while maximizing intra-space consistency to create stable representations. A parameter-efficient adapter injects these latent codes into a frozen video diffusion model, enabling the synthesis of a coherent robot execution video from a single human demonstration, without requiring paired cross-embodiment data. Experiments show our approach generates temporally consistent and morphologically accurate robot demonstrations, offering a scalable solution to leverage internet-scale human video for robot learning.
匹配关键词: manipulation
---

[ACADEMIC - ARXIV]
标题: SigLoMa: Learning Open-World Quadrupedal Loco-Manipulation from Ego-Centric Vision
作者: Shiyi Chen, Haiyi Liu, Mingye Yang, Jiaqi Zhang, Debing Zhang
链接: https://arxiv.org/abs/2605.03846v1
完整摘要: Designing an open-world quadrupedal loco-manipulation system is highly challenging. Traditional reinforcement learning frameworks utilizing exteroception often suffer from extreme sample inefficiency and massive sim-to-real gaps. Furthermore, the inherent latency of visual tracking fundamentally conflicts with the high-frequency demands of precise floating-base control. Consequently, existing systems lean heavily on expensive external motion capture and off-board computation. To eliminate these dependencies, we present SigLoMa, a fully onboard, ego-centric vision-based pick-and-place framework. At the core of SigLoMa is the introduction of Sigma Points, a lightweight geometric representation for exteroception that guarantees high scalability and native sim-to-real alignment. To bridge the frequency divide between slow perception and fast control, we design an ego-centric Kalman Filter to provide robust, high-rate state estimation. On the learning front, we alleviate sample inefficiency via an Active Sampling Curriculum guided by Hint Poses, and tackle the robot's structural visual blind spots using temporal encoding coupled with simulated random-walk drift. Real-world experiments validate that, relying solely on a 5Hz (200 ms latency) open-vocabulary detector, SigLoMa successfully executes dynamic loco-manipulation across multiple tasks, achieving performance comparable to expert human teleoperation.
匹配关键词: sim-to-real
---

[ACADEMIC - ARXIV]
标题: SOAR: Real-Time Joint Optimization of Order Allocation and Robot Scheduling in Robotic Mobile Fulfillment Systems
作者: Yibang Tang, Yifan Yang, Jingyuan Wang, Junhua Chen, Zhen Zhao
链接: https://arxiv.org/abs/2605.03842v1
完整摘要: Robotic Mobile Fulfillment Systems (RMFS) rely on mobile robots for automated inventory transportation, coordinating order allocation and robot scheduling to enhance warehousing efficiency. However, optimizing RMFS is challenging due to strict real-time constraints and the strong coupling of multi-phase decisions. Existing methods either decompose the problem into isolated sub-tasks to guarantee responsiveness at the cost of global optimality, or rely on computationally expensive global optimization models that are unsuitable for dynamic industrial environments. To bridge this gap, we propose SOAR, a unified Deep Reinforcement Learning framework for real-time joint optimization. SOAR transforms order allocation and robot scheduling into a unified process by utilizing soft order allocations as observations. We formulate this as an Event-Driven Markov Decision Process, enabling the agent to perform simultaneous scheduling in response to asynchronous system events. Technically, we employ a Heterogeneous Graph Transformer to encode the warehouse state and integrate phased domain knowledge. Additionally, we incorporate a reward shaping strategy to address sparse feedback in long-horizon tasks. Extensive experiments on synthetic and real-world industrial datasets, in collaboration with Geekplus, demonstrate that SOAR reduces global makespan by 7.5\% and average order completion time by 15.4\% with sub-100ms latency. Furthermore, sim-to-real deployment confirms its practical viability and significant performance gains in production environments. The code is available at https://github.com/200815147/SOAR.
匹配关键词: sim-to-real
---

[ACADEMIC - ARXIV]
标题: Logical Consistency as a Bridge: Improving LLM Hallucination Detection via Label Constraint Modeling between Responses and Self-Judgments
作者: Hao Mi, Qiang Sheng, Shaofei Wang, Beizhe Hu, Yifan Sun, Zhengjia Wang, Hengqi Zeng, Yang Li, Danding Wang, Juan Cao
链接: https://arxiv.org/abs/2605.03971v1
完整摘要: Large Language Models (LLMs) are prone to factual hallucinations, risking their reliability in real-world applications. Existing hallucination detectors mainly extract micro-level intrinsic patterns for uncertainty quantification or elicit macro-level self-judgments through verbalized prompts. However, these methods address only a single facet of the hallucination, focusing either on implicit neural uncertainty or explicit symbolic reasoning, thereby treating these inherently coupled behaviors in isolation and failing to exploit their interdependence for a holistic view. In this paper, we propose LaaB (Logical Consistency-as-a-Bridge), a framework that bridges neural features and symbolic judgments for hallucination detection. LaaB introduces a "meta-judgment" process to map symbolic labels back into the feature space. By leveraging the inherent logical bridge where response and meta-judgment labels are either the same or opposite based on the self-judgment's semantics, LaaB aligns and integrates dual-view signals via mutual learning and enhances the hallucination detection. Extensive experiments on 4 public datasets, across 4 LLMs, against 8 baselines demonstrate the superiority of LaaB.
匹配关键词: world model
---

[ACADEMIC - ARXIV]
标题: Feature-Augmented Transformers for Robust AI-Text Detection Across Domains and Generators
作者: Mohamed Mady, Johannes Reschke, Björn Schuller
链接: https://arxiv.org/abs/2605.03969v1
完整摘要: AI-generated text is nowadays produced at scale across domains and heterogeneous generation pipelines, making robustness to distribution shift a central requirement for supervised binary detectors. We train transformer-based detectors on HC3 PLUS and calibrate a single decision threshold by maximising balanced accuracy on held-out validation; this threshold is then kept fixed for all downstream test distributions, revealing domain- and generator-dependent error asymmetries under shift. We evaluate in-domain on HC3 PLUS, under cross-dataset transfer to the multi-domain, multi-generator M4 benchmark, and on the external AI-Text-Detection-Pile. Although base models achieve near-ceiling in-domain performance (up to 99.5% balanced accuracy), performance under shift is brittle and strongly model-dependent. Feature augmentation via attention-based linguistic feature fusion improves transfer, with our best model (DeBERTa-v3-base+FeatAttn) achieving 85.9% balanced accuracy on M4. Multi-seed experiments confirm high stability. Under the same fixed-threshold protocol, our model outperforms strong zero-shot baselines by up to +7.22 points. Category-level ablations further show that readability and vocabulary features contribute most to robustness under shift. Overall, these results demonstrate that feature augmentation and a modern DeBERTa backbone significantly outperform earlier BERT/RoBERTa models, while the fixed-threshold protocol provides a more realistic and informative assessment of practical detector robustness.
匹配关键词: world model
---

[ACADEMIC - ARXIV]
标题: Label-Efficient School Detection from Aerial Imagery via Weakly Supervised Pretraining and Fine-Tuning
作者: Zakarya Elmimouni, Fares Fourati, Mohamed-Slim Alouini
链接: https://arxiv.org/abs/2605.03968v1
完整摘要: Accurate school detection is essential for supporting education initiatives, including infrastructure planning and expanding internet connectivity to underserved areas. However, many regions around the world face challenges due to outdated, incomplete, or unavailable official records. Manual mapping efforts, while valuable, are labor-intensive and lack scalability across large geographic areas. To address this, we propose a weakly supervised framework for school detection from aerial imagery that minimizes the need for human annotations while supporting global mapping efforts. Our method is specifically designed for low-data regimes, where manual annotations are extremely scarce. We introduce an automatic labeling pipeline that leverages sparse location points and semantic segmentation to generate infrastructure masks from which we generate bounding boxes. Using these automatically labeled images, we train our detectors on a first training stage to learn a representation of what schools look like, then using a small set of manually labeled images, we fine-tune the previously trained models on this clean dataset. This two stage training pipeline enables large-scale and strong detection in low-data setting of school infrastructure with minimal supervision. Our results demonstrate strong object detection performance, particularly in the low-data regime, where the models achieve promising results using only 50 manually labeled images, significantly reducing the need for costly annotations. This framework supports education and connectivity initiatives worldwide by providing an efficient and extensible approach to mapping schools from space. All models, training code and auto-labeled data will be publicly released to foster future research and real-world impact.
匹配关键词: world model
---

[ACADEMIC - ARXIV]
标题: Pretrained Model Representations as Acquisition Signals for Active Learning of MLIPs
作者: Eszter Varga-Umbrich, Shikha Surana, Paul Duckworth, Jules Tilly, Olivier Peltre, Zachary Weller-Davies
链接: https://arxiv.org/abs/2605.03964v1
完整摘要: Training machine learning interatomic potentials (MLIPs) for reactive chemistry is often bottlenecked by the high cost of quantum chemical labels and the scarcity of transition state configurations in candidate pools. Active learning (AL) can mitigate these costs, but its effectiveness hinges on the acquisition rule. We investigate whether the latent space of a pretrained MLIP already contains the information necessary for effective acquisition, eliminating the need for auxiliary uncertainty heads, Bayesian training and fine-tuning, or committee ensembles. We introduce two acquisition signals derived directly from a pretrained MACE potential: a finite-width neural tangent kernel (NTK) and an activation kernel built from hidden latent space features. On reactive-chemistry benchmarks, both kernels consistently outperform fixed-descriptor baselines, committee disagreement, and random acquisition, reducing the data required to reach performance targets by an average of 38% for energy error and 28% for force error. We further show that the pretrained model induces similarity spaces that preserve chemically meaningful structure and provide more reliable residual uncertainty estimates than randomly initialised or fixed-descriptor-based kernels. Our results suggest that pretraining aligns latent-space geometry with model error, yielding a practical and sufficient acquisition signal for reactive MLIP fine-tuning.
匹配关键词: world model
---

[ACADEMIC - ARXIV]
标题: Transformers with Selective Access to Early Representations
作者: Skye Gunasekaran, Téa Wright, Rui-Jie Zhu, Jason Eshraghian
链接: https://arxiv.org/abs/2605.03953v1
完整摘要: Several recent Transformer architectures expose later layers to representations computed in the earliest layers, motivated by the observation that low-level features can become harder to recover as the residual stream is repeatedly transformed through depth. The cheapest among these methods add static value residuals: learned mixing coefficients that expose the first-layer value projection V_1 uniformly across tokens and heads. More expressive dense or dynamic alternatives recover finer-grained access, but at higher memory cost and lower throughput. The usefulness of V_1 is unlikely to be constant across tokens, heads, and contexts; different positions plausibly require different amounts of access to early lexical or semantic information. We therefore treat early-representation reuse as a retrieval problem rather than a connectivity problem, and introduce Selective Access Transformer (SATFormer), which preserves the first-layer value pathway while controlling access with a context-dependent gate. Across models from 130M to 1.3B parameters, SATFormer consistently improves validation loss and zero-shot accuracy over the static value-residual and Transformer baselines. Its strongest gains appear on retrieval-intensive benchmarks, where it improves over static value residuals by approximately 1.5 average points, while maintaining throughput and memory usage close to the baseline Transformer. Gate analyses suggest sparse, depth-dependent, head-specific, and category-sensitive access patterns, supporting the interpretation that SATFormer learns selective reuse of early representations rather than uniform residual copying. Our code is available at https://github.com/SkyeGunasekaran/SATFormer.
匹配关键词: world model
---

[ACADEMIC - ARXIV]
标题: MiniMind-O Technical Report: An Open Small-Scale Speech-Native Omni Model
作者: Jingyao Gong
链接: https://arxiv.org/abs/2605.03937v1
完整摘要: MiniMind-O is an open 0.1B-scale omni model built on the MiniMind language model. It accepts text, speech, and image inputs, and returns both text and streaming speech. The release includes model code, checkpoints, and the main Parquet training datasets for text-to-audio, image-to-text, and audio-to-audio training, making the complete interaction loop directly inspectable. The model uses a full MiniMind backbone as the Thinker and an independent four-layer Talker made from MiniMind blocks. Frozen SenseVoice-Small and SigLIP2 encoders provide speech and image features, which are mapped by lightweight MLP projectors and injected at modality-placeholder positions. The Talker reads a middle-layer Thinker state together with an autoregressive eight-layer Mimi-code buffer. Speaker control is handled by a dedicated speaker token, right-aligned reference codec prompts, and precomputed CAM++ speaker embeddings, so voice conditioning remains part of the audio-code context rather than a separate TTS module. With a 768-dimensional Talker, the dense and MoE variants reach average CERs of 0.0897 and 0.0900 in Thinker--Talker consistency evaluation, with overall voice-cloning similarities of 0.5995 and 0.5937. Beyond reporting a working system, the paper identifies three scale-critical design choices for small omni models: middle-layer semantic bridging, a released multimodal sequence format, and a parameter-efficient eight-codebook interface.
匹配关键词: speech synthesis
---

[ACADEMIC - ARXIV]
标题: Assessing the Impact of Noise and Speech Enhancement on the Intelligibility of Speech Codecs
作者: Lyonel Behringer, Anna Leschanowsky, Anjana Rajasekhar, Emily Kratsch, Guillaume Fuchs
链接: https://arxiv.org/abs/2605.03776v1
完整摘要: Preserving speech intelligibility is a minimum requirement for speech codecs in communication. Recently, very low-bitrate neural codecs have gained interest for replacing classical codecs, reinforcing the need to evaluate whether intelligibility is preserved in realistic scenarios. In this paper, we evaluate the intelligibility and listening effort of classical and neural speech codecs in clean and noisy conditions. Further, we assess the impact of speech enhancement (SE) before coding, simulating a possible audio processing pipeline. The results show that classical codecs are more noise robust than neural codecs. Further, SE can lead to significant intelligibility and listening effort improvements for codecs otherwise negatively affected by noise. Listening effort reveals nuanced differences when intelligibility is saturated. Lastly, objective intelligibility based on automatic speech recognition is highly correlated with subjective intelligibility scores averaged per condition.
匹配关键词: speech synthesis
---

[ACADEMIC - ARXIV]
标题: A Comprehensive Analysis of Tokenization and Self-Supervised Learning in End-to-End Automatic Speech Recognition applied on French Language
作者: Thibault Bañeras-Roux, Mickael Rouvier, Jane Wottawa, Richard Dufour
链接: https://arxiv.org/abs/2605.03696v1
完整摘要: The performance of end-to-end automatic speech recognition (ASR) systems enables their increasing integration into numerous applications. While there are various benefits to such speech-to-text systems, the choice of hyperparameters and models plays a crucial role in their performance. Typically, these choices are determined by considering only the character (CER) and/or word error rate (WER) metrics. However, it has been shown in several studies that these metrics are largely incomplete and fail to adequately describe the downstream application of automatic transcripts. In this paper, we conduct a qualitative study on the French language that investigates the impact of subword tokenization algorithms and self-supervised learning models from different linguistic and acoustic perspectives, using a comprehensive set of evaluation metrics.
匹配关键词: speech synthesis
---

[ACADEMIC - ARXIV]
标题: MEMTIER: Tiered Memory Architecture and Retrieval Bottleneck Analysis for Long-Running Autonomous AI Agents
作者: Bronislav Sidik, Lior Rokach
链接: https://arxiv.org/abs/2605.03675v1
完整摘要: Long-running autonomous AI agents suffer from a well-documented memory coherence problem: tool-execution success rates degrade 14 percentage points over 72-hour operation windows due to four compounding failure modes in existing flat-file memory systems. We present MEMTIER, a tripartite memory architecture for the OpenClaw agent runtime that introduces a structured episodic JSONL store, a five-signal weighted retrieval engine, an attention-attributed cognitive weight update loop, an asynchronous consolidation daemon promoting episodic facts to a semantic tier, and a PPO-based policy framework for adapting retrieval weights (infrastructure validated; performance gains pending camera-ready). On the full 500-question LongMemEval-S benchmark (Wu et al., 2025), MEMTIER achieves Acc=0.382, F1=0.412 with Qwen2.5-7B on a consumer 6GB GPU - a +33 percentage point improvement over the full-context baseline (0.050 -> 0.382, i.e., 5% -> 38%). With DeepSeek-V4-Flash fact pre-population, single-session recall reaches 0.686-0.714, exceeding the paper's RAG BM25 GPT-4o baseline (0.560) on those categories. Temporal reasoning rises to 0.323 and multi-session synthesis to 0.173, demonstrating that structured semantic pre-population qualitatively changes what lightweight retrieval can achieve. All phases run locally on a consumer laptop with a 6GB GPU.
匹配关键词: speech synthesis
---

[ACADEMIC - ARXIV]
标题: A Paradigm for Interpreting Metrics and Identifying Critical Errors in Automatic Speech Recognition
作者: Thibault Bañeras-Roux, Mickael Rouvier, Jane Wottawa, Richard Dufour
链接: https://arxiv.org/abs/2605.03671v1
完整摘要: The most commonly used metrics for evaluating automatic speech transcriptions, namely Word Error Rate (WER) and Character Error Rate (CER), have been heavily criticized for their poor correlation to human perception and their inability to take into account linguistic and semantic information. While metric-based embeddings, seeking to approximate human perception, have been proposed, their scores remain difficult to interpret, unlike WER and CER. In this article, we overcome this problem by proposing a paradigm that consists in incorporating a chosen metric into it in order to obtain an equivalent of the error rate: a Minimum Edit Distance (minED). This approach parallels transcription errors with their human perception, also allowing an original study of the severity of these errors from a human perspective.
匹配关键词: speech synthesis
---

[ACADEMIC - ARXIV]
标题: MiniMind-O Technical Report: An Open Small-Scale Speech-Native Omni Model
作者: Jingyao Gong
链接: https://arxiv.org/abs/2605.03937v1
完整摘要: MiniMind-O is an open 0.1B-scale omni model built on the MiniMind language model. It accepts text, speech, and image inputs, and returns both text and streaming speech. The release includes model code, checkpoints, and the main Parquet training datasets for text-to-audio, image-to-text, and audio-to-audio training, making the complete interaction loop directly inspectable. The model uses a full MiniMind backbone as the Thinker and an independent four-layer Talker made from MiniMind blocks. Frozen SenseVoice-Small and SigLIP2 encoders provide speech and image features, which are mapped by lightweight MLP projectors and injected at modality-placeholder positions. The Talker reads a middle-layer Thinker state together with an autoregressive eight-layer Mimi-code buffer. Speaker control is handled by a dedicated speaker token, right-aligned reference codec prompts, and precomputed CAM++ speaker embeddings, so voice conditioning remains part of the audio-code context rather than a separate TTS module. With a 768-dimensional Talker, the dense and MoE variants reach average CERs of 0.0897 and 0.0900 in Thinker--Talker consistency evaluation, with overall voice-cloning similarities of 0.5995 and 0.5937. Beyond reporting a working system, the paper identifies three scale-critical design choices for small omni models: middle-layer semantic bridging, a released multimodal sequence format, and a parameter-efficient eight-codebook interface.
匹配关键词: TTS
---

[ACADEMIC - ARXIV]
标题: MOSAIC-Bench: Measuring Compositional Vulnerability Induction in Coding Agents
作者: Jonathan Steinberg, Oren Gal
链接: https://arxiv.org/abs/2605.03952v1
完整摘要: Coding agents often pass per-prompt safety review yet ship exploitable code when their tasks are decomposed into routine engineering tickets. The challenge is structural: existing safety alignment evaluates overt requests in isolation, leaving models blind to malicious end-states that emerge from sequenced compliance with innocuous-looking requests. We introduce MOSAIC-Bench (Malicious Objectives Sequenced As Innocuous Compliance), a benchmark of 199 three-stage attack chains paired with deterministic exploit oracles on deployed software substrates (10 web-application substrates, 31 CWE classes, 5 programming languages) that treats both exploit ground truth and downstream reviewer protocol as first-class evaluation axes. On this benchmark, nine production coding agents from Anthropic, OpenAI, Google, Moonshot, Zhipu, and Minimax compose innocuous tickets at 53-86% end-to-end ASR with only two refusals across all staged runs. In a matched direct-prompt experiment over four frontier Claude/Codex agents, vulnerable-output rates fall to 0-20.4%: Claude primarily refuses, while Codex primarily hardens rather than emitting the vulnerable implementation - ticket staging silences both defense modes simultaneously. Downstream, code reviewer agents approve 25.8% of these confirmed-vulnerable cumulative diffs as routine PRs, and a full-context implementation protocol closes only 50% of the staged/direct gap, ruling out context fragmentation as the sole explanation. As a deployable but non-adaptive mitigation, reframing the reviewer as an adversarial pentester reduces evasion across the evaluated reviewer subset; pentester framed evasion ranges from 3.0% to 17.6%, and an open-weight Gemma-4-E4B-it reviewer under this framing detects 88.4% of attacks on the dataset with a 4.6% false-positive rate measured on 608 real-world GitHub PRs.
匹配关键词: ASR
---

[ACADEMIC - ARXIV]
标题: A Comprehensive Analysis of Tokenization and Self-Supervised Learning in End-to-End Automatic Speech Recognition applied on French Language
作者: Thibault Bañeras-Roux, Mickael Rouvier, Jane Wottawa, Richard Dufour
链接: https://arxiv.org/abs/2605.03696v1
完整摘要: The performance of end-to-end automatic speech recognition (ASR) systems enables their increasing integration into numerous applications. While there are various benefits to such speech-to-text systems, the choice of hyperparameters and models plays a crucial role in their performance. Typically, these choices are determined by considering only the character (CER) and/or word error rate (WER) metrics. However, it has been shown in several studies that these metrics are largely incomplete and fail to adequately describe the downstream application of automatic transcripts. In this paper, we conduct a qualitative study on the French language that investigates the impact of subword tokenization algorithms and self-supervised learning models from different linguistic and acoustic perspectives, using a comprehensive set of evaluation metrics.
匹配关键词: ASR
---

[ACADEMIC - ARXIV]
标题: MEMSAD: Gradient-Coupled Anomaly Detection for Memory Poisoning in Retrieval-Augmented Agents
作者: Ishrith Gowda
链接: https://arxiv.org/abs/2605.03482v1
完整摘要: Persistent external memory enables LLM agents to maintain context across sessions, yet its security properties remain formally uncharacterized. We formalize memory poisoning attacks on retrieval-augmented agents as a Stackelberg game with a unified evaluation framework spanning three attack classes with escalating access assumptions. Correcting an evaluation protocol inconsistency in the triggered-query specification of Chen et al. (2024), we show faithful evaluation increases measured attack success by $4\times$ (ASR-R: $0.25 \to 1.00$). Our primary contribution is MEMSAD (Semantic Anomaly Detection), a calibration-based defense grounded in a gradient coupling theorem: under encoder regularity, the anomaly score gradient and the retrieval objective gradient are provably identical, so any continuous perturbation that reduces detection risk necessarily degrades retrieval rank. This coupling yields a certified detection radius guaranteeing correct classification regardless of adversary strategy. We prove minimax optimality via Le Cam's method, showing any threshold detector requires $Ω(1/ρ^2)$ calibration samples and MEMSAD achieves this up to $\log(1/δ)$ factors. We further derive online regret bounds for rolling calibration at rate $O(σ^{2/3}Δ^{1/3})$, and formally characterize a discrete synonym-invariance loophole that marks the boundary of what continuous-space defenses can guarantee. Experiments on a $3 \times 5$ attack-defense matrix with bootstrap confidence intervals, Bonferroni-corrected hypothesis tests, and Clopper-Pearson validation ($n=1{,}000$) confirm: composite defenses achieve TPR $= 1.00$, FPR $= 0.00$ across all attacks, while synonym substitution evades detection at $Δ$ ASR-R $\approx 0$, exposing a gap existing embedding-based defenses cannot close.
匹配关键词: ASR
---

[ACADEMIC - ARXIV]
标题: Contrastive Regularization for Accent-Robust ASR
作者: Van-Phat Thai, Aradhya Dhruv, Duc-Thinh Pham, Sameer Alam
链接: https://arxiv.org/abs/2605.03297v1
完整摘要: ASR systems based on self-supervised acoustic pretraining and CTC fine-tuning achieve strong performance on native speech but remain sensitive to accent variability. We investigate supervised contrastive learning (SupCon) as a lightweight, accent-invariant auxiliary objective for CTC fine-tuning. An utterance-level contrastive loss regularizes encoder representations without architectural modification or explicit accent supervision. Experiments on the L2-ARCTIC benchmark show consistent WER reductions across multiple pretrained encoders, with up to 25 -- 29\% relative reduction under unseen-accent evaluation. Analysis using within-transcript cosine dispersion indicates that SupCon promotes more compact and stable representation geometry under accent variability. Overall, SupCon provides an effective and model-agnostic regularization strategy for improving accent robustness.
匹配关键词: ASR
---

[ACADEMIC - ARXIV]
标题: Logical Consistency as a Bridge: Improving LLM Hallucination Detection via Label Constraint Modeling between Responses and Self-Judgments
作者: Hao Mi, Qiang Sheng, Shaofei Wang, Beizhe Hu, Yifan Sun, Zhengjia Wang, Hengqi Zeng, Yang Li, Danding Wang, Juan Cao
链接: https://arxiv.org/abs/2605.03971v1
完整摘要: Large Language Models (LLMs) are prone to factual hallucinations, risking their reliability in real-world applications. Existing hallucination detectors mainly extract micro-level intrinsic patterns for uncertainty quantification or elicit macro-level self-judgments through verbalized prompts. However, these methods address only a single facet of the hallucination, focusing either on implicit neural uncertainty or explicit symbolic reasoning, thereby treating these inherently coupled behaviors in isolation and failing to exploit their interdependence for a holistic view. In this paper, we propose LaaB (Logical Consistency-as-a-Bridge), a framework that bridges neural features and symbolic judgments for hallucination detection. LaaB introduces a "meta-judgment" process to map symbolic labels back into the feature space. By leveraging the inherent logical bridge where response and meta-judgment labels are either the same or opposite based on the self-judgment's semantics, LaaB aligns and integrates dual-view signals via mutual learning and enhances the hallucination detection. Extensive experiments on 4 public datasets, across 4 LLMs, against 8 baselines demonstrate the superiority of LaaB.
匹配关键词: audio language model
---

[ACADEMIC - ARXIV]
标题: Feature-Augmented Transformers for Robust AI-Text Detection Across Domains and Generators
作者: Mohamed Mady, Johannes Reschke, Björn Schuller
链接: https://arxiv.org/abs/2605.03969v1
完整摘要: AI-generated text is nowadays produced at scale across domains and heterogeneous generation pipelines, making robustness to distribution shift a central requirement for supervised binary detectors. We train transformer-based detectors on HC3 PLUS and calibrate a single decision threshold by maximising balanced accuracy on held-out validation; this threshold is then kept fixed for all downstream test distributions, revealing domain- and generator-dependent error asymmetries under shift. We evaluate in-domain on HC3 PLUS, under cross-dataset transfer to the multi-domain, multi-generator M4 benchmark, and on the external AI-Text-Detection-Pile. Although base models achieve near-ceiling in-domain performance (up to 99.5% balanced accuracy), performance under shift is brittle and strongly model-dependent. Feature augmentation via attention-based linguistic feature fusion improves transfer, with our best model (DeBERTa-v3-base+FeatAttn) achieving 85.9% balanced accuracy on M4. Multi-seed experiments confirm high stability. Under the same fixed-threshold protocol, our model outperforms strong zero-shot baselines by up to +7.22 points. Category-level ablations further show that readability and vocabulary features contribute most to robustness under shift. Overall, these results demonstrate that feature augmentation and a modern DeBERTa backbone significantly outperform earlier BERT/RoBERTa models, while the fixed-threshold protocol provides a more realistic and informative assessment of practical detector robustness.
匹配关键词: audio language model
---

[ACADEMIC - ARXIV]
标题: Label-Efficient School Detection from Aerial Imagery via Weakly Supervised Pretraining and Fine-Tuning
作者: Zakarya Elmimouni, Fares Fourati, Mohamed-Slim Alouini
链接: https://arxiv.org/abs/2605.03968v1
完整摘要: Accurate school detection is essential for supporting education initiatives, including infrastructure planning and expanding internet connectivity to underserved areas. However, many regions around the world face challenges due to outdated, incomplete, or unavailable official records. Manual mapping efforts, while valuable, are labor-intensive and lack scalability across large geographic areas. To address this, we propose a weakly supervised framework for school detection from aerial imagery that minimizes the need for human annotations while supporting global mapping efforts. Our method is specifically designed for low-data regimes, where manual annotations are extremely scarce. We introduce an automatic labeling pipeline that leverages sparse location points and semantic segmentation to generate infrastructure masks from which we generate bounding boxes. Using these automatically labeled images, we train our detectors on a first training stage to learn a representation of what schools look like, then using a small set of manually labeled images, we fine-tune the previously trained models on this clean dataset. This two stage training pipeline enables large-scale and strong detection in low-data setting of school infrastructure with minimal supervision. Our results demonstrate strong object detection performance, particularly in the low-data regime, where the models achieve promising results using only 50 manually labeled images, significantly reducing the need for costly annotations. This framework supports education and connectivity initiatives worldwide by providing an efficient and extensible approach to mapping schools from space. All models, training code and auto-labeled data will be publicly released to foster future research and real-world impact.
匹配关键词: audio language model
---

[ACADEMIC - ARXIV]
标题: Pretrained Model Representations as Acquisition Signals for Active Learning of MLIPs
作者: Eszter Varga-Umbrich, Shikha Surana, Paul Duckworth, Jules Tilly, Olivier Peltre, Zachary Weller-Davies
链接: https://arxiv.org/abs/2605.03964v1
完整摘要: Training machine learning interatomic potentials (MLIPs) for reactive chemistry is often bottlenecked by the high cost of quantum chemical labels and the scarcity of transition state configurations in candidate pools. Active learning (AL) can mitigate these costs, but its effectiveness hinges on the acquisition rule. We investigate whether the latent space of a pretrained MLIP already contains the information necessary for effective acquisition, eliminating the need for auxiliary uncertainty heads, Bayesian training and fine-tuning, or committee ensembles. We introduce two acquisition signals derived directly from a pretrained MACE potential: a finite-width neural tangent kernel (NTK) and an activation kernel built from hidden latent space features. On reactive-chemistry benchmarks, both kernels consistently outperform fixed-descriptor baselines, committee disagreement, and random acquisition, reducing the data required to reach performance targets by an average of 38% for energy error and 28% for force error. We further show that the pretrained model induces similarity spaces that preserve chemically meaningful structure and provide more reliable residual uncertainty estimates than randomly initialised or fixed-descriptor-based kernels. Our results suggest that pretraining aligns latent-space geometry with model error, yielding a practical and sufficient acquisition signal for reactive MLIP fine-tuning.
匹配关键词: audio language model
---

[ACADEMIC - ARXIV]
标题: Transformers with Selective Access to Early Representations
作者: Skye Gunasekaran, Téa Wright, Rui-Jie Zhu, Jason Eshraghian
链接: https://arxiv.org/abs/2605.03953v1
完整摘要: Several recent Transformer architectures expose later layers to representations computed in the earliest layers, motivated by the observation that low-level features can become harder to recover as the residual stream is repeatedly transformed through depth. The cheapest among these methods add static value residuals: learned mixing coefficients that expose the first-layer value projection V_1 uniformly across tokens and heads. More expressive dense or dynamic alternatives recover finer-grained access, but at higher memory cost and lower throughput. The usefulness of V_1 is unlikely to be constant across tokens, heads, and contexts; different positions plausibly require different amounts of access to early lexical or semantic information. We therefore treat early-representation reuse as a retrieval problem rather than a connectivity problem, and introduce Selective Access Transformer (SATFormer), which preserves the first-layer value pathway while controlling access with a context-dependent gate. Across models from 130M to 1.3B parameters, SATFormer consistently improves validation loss and zero-shot accuracy over the static value-residual and Transformer baselines. Its strongest gains appear on retrieval-intensive benchmarks, where it improves over static value residuals by approximately 1.5 average points, while maintaining throughput and memory usage close to the baseline Transformer. Gate analyses suggest sparse, depth-dependent, head-specific, and category-sensitive access patterns, supporting the interpretation that SATFormer learns selective reuse of early representations rather than uniform residual copying. Our code is available at https://github.com/SkyeGunasekaran/SATFormer.
匹配关键词: audio language model
---

[ACADEMIC - ARXIV]
标题: QKVShare: Quantized KV-Cache Handoff for Multi-Agent On-Device LLMs
作者: Pratik Honavar, Tejpratap GVSL
链接: https://arxiv.org/abs/2605.03884v1
完整摘要: Multi-agent LLM systems on edge devices need to hand off latent context efficiently, but the practical choices today are expensive re-prefill or full-precision KV transfer. We study QKVShare, a framework for quantized KV-cache handoff between agents that combines token-level mixed-precision allocation, a self-contained CacheCard representation, and a HuggingFace-compatible cache injection path. Our current results support a narrower but clearer story than the original draft: on 150 GSM8K problems with Llama-3.1-8B-Instruct, adaptive quantization remains competitive under repeated handoff and shows its clearest gains against uniform quantization in deeper-hop, higher budget settings; for handoff latency, the QKVShare path reduces TTFT relative to full re prefill at every tested context, from 130.7 ms vs. 150.2 ms at nominal 1K context to 397.1 ms vs. 1029.7 ms at nominal 8K context;. Stage timing shows that post-injection generation, not card creation, dominates the current QKVShare latency path. These results position quantized KV handoff as a promising on-device systems direction while also highlighting the need for stronger controller ablations and apples-to-apples runtime comparisons.
匹配关键词: KV cache
---

[ACADEMIC - ARXIV]
标题: AdapShot: Adaptive Many-Shot In-Context Learning with Semantic-Aware KV Cache Reuse
作者: Jie Ou, Jinyu Guo, Shiyao Guo, Yuang Li, Ruiqi Wu, Zhaokun Wang, Wenyi Li, Wenhong Tian
链接: https://arxiv.org/abs/2605.03644v1
完整摘要: Many-Shot In-Context Learning (ICL) has emerged as a promising paradigm, leveraging extensive examples to unlock the reasoning potential of Large Language Models (LLMs). However, existing methods typically rely on a predetermined, fixed number of shots. This static approach often fails to adapt to the varying difficulty of different queries, leading to either insufficient context or interference from noise. Furthermore, the prohibitive computational and memory costs of long contexts severely limit Many-Shot's feasibility. To address the above limitations, we propose AdapShot, which dynamically optimizes shot counts and leverages KV cache reuse for efficient inference. Specifically, we design a probe-based evaluation mechanism that utilizes output entropy to determine the optimal number of shots. To bypass the redundant prefilling computation during both the probing and inference phases, we incorporate a semantics-aware KV cache reuse strategy. Within this reuse strategy, to address positional encoding incompatibilities, we introduce a decoupling and re-encoding method that enables the flexible reordering of cached key-value pairs. Extensive experiments demonstrate that AdapShot achieves an average performance gain of around 10% and a 4.64x speedup compared to state-of-the-art DBSA.
匹配关键词: KV cache
---

[ACADEMIC - ARXIV]
标题: HeadQ: Model-Visible Distortion and Score-Space Correction for KV-Cache Quantization
作者: Jorge L. Ruiz Williams
链接: https://arxiv.org/abs/2605.03562v1
完整摘要: KV-cache quantizers usually optimize storage-space reconstruction, even though attention reads keys through logits and values through attention-weighted readout. We argue that persistent cache error should be measured in model-visible coordinates. For keys, the visible object is score error modulo constant shifts; this yields HeadQ, a key-side method that stores a low-rank residual side code in a calibration-learned query basis and applies it as an additive logit correction. For values, fixed-attention readout gives an $A^2$-weighted token-distortion surrogate. Across six models, Fisher/score-space error predicts attention KL far better than raw key MSE; same-budget counterexamples, null-space interventions, query-PCA controls, and wrong-sign HeadQ falsify storage-MSE alternatives. Matched Pythia checkpoints localize the main anomaly to a small-model low-entropy route-flip boundary. In K-only WikiText-103 decode experiments with dense values, HeadQ removes roughly $84$--$94\%$ of the excess perplexity on the strongest 2-bit rows; in an auxiliary full-KV 2-bit composition, HeadQ plus an $A^2$ value policy improves all six models.
匹配关键词: KV cache
---

[ACADEMIC - ARXIV]
标题: VLMaxxing through FrameMogging Training-Free Anti-Recomputation for Video Vision-Language Models
作者: JF Bastien, Sam D'Amico
链接: https://arxiv.org/abs/2605.03351v1
完整摘要: Video vision-language models (VLMs) keep paying for visual state the stream already told us was stable. The factory wall did not move, but most VLM pipelines still hand the model dense RGB frames or a fresh prefix again. We study that waste as training-free anti-recomputation: reuse state when validation says it survives, and buy fresh evidence when the scene, query, or cache topology requires it. The largest measured win is after ingest. On frozen Qwen2.5-VL-7B-Instruct-4bit, adaptive same-video follow-up reuse preserves paired choices and correctness on a 93-query VideoMME breadth setting while reducing follow-up latency by 14.90-35.92x. The first query is still cold; the win starts when later questions reuse the same video state. Stress tests bound the result: repeated-question schedules hold through 50 turns, while dense-answer-anchored prompt variation separates conservative fixed K=1 repair from faster aggressive policies that drift. Fresh-video pruning is smaller but real. C-VISION skips timed vision-tower work before the first answer is generated. On Gemma 4-E4B-4bit, the clean 32f short cell reaches 1.316x first-query speedup with no paired drift or parse failures on 20 items; Qwen shows the fidelity/speed boundary. Stage-share ceiling (C-CEILING) is the accounting guardrail: a component speedup becomes an end-to-end speedup only in proportion to the wall-clock share it accelerates, so C-VISION and after-ingest follow-up reuse do not multiply. Candidate C-STREAM remains a native-rate target, not a headline result here. The broader direction is VLM-native media that expose change, motion, uncertainty, object state, sensor time, and active tiles directly, so models do not have to rediscover the world from dense RGB every frame.
匹配关键词: KV cache
---

[ACADEMIC - ARXIV]
标题: QKVShare: Quantized KV-Cache Handoff for Multi-Agent On-Device LLMs
作者: Pratik Honavar, Tejpratap GVSL
链接: https://arxiv.org/abs/2605.03884v1
完整摘要: Multi-agent LLM systems on edge devices need to hand off latent context efficiently, but the practical choices today are expensive re-prefill or full-precision KV transfer. We study QKVShare, a framework for quantized KV-cache handoff between agents that combines token-level mixed-precision allocation, a self-contained CacheCard representation, and a HuggingFace-compatible cache injection path. Our current results support a narrower but clearer story than the original draft: on 150 GSM8K problems with Llama-3.1-8B-Instruct, adaptive quantization remains competitive under repeated handoff and shows its clearest gains against uniform quantization in deeper-hop, higher budget settings; for handoff latency, the QKVShare path reduces TTFT relative to full re prefill at every tested context, from 130.7 ms vs. 150.2 ms at nominal 1K context to 397.1 ms vs. 1029.7 ms at nominal 8K context;. Stage timing shows that post-injection generation, not card creation, dominates the current QKVShare latency path. These results position quantized KV handoff as a promising on-device systems direction while also highlighting the need for stronger controller ablations and apples-to-apples runtime comparisons.
匹配关键词: quantization
---

[ACADEMIC - ARXIV]
标题: HeadQ: Model-Visible Distortion and Score-Space Correction for KV-Cache Quantization
作者: Jorge L. Ruiz Williams
链接: https://arxiv.org/abs/2605.03562v1
完整摘要: KV-cache quantizers usually optimize storage-space reconstruction, even though attention reads keys through logits and values through attention-weighted readout. We argue that persistent cache error should be measured in model-visible coordinates. For keys, the visible object is score error modulo constant shifts; this yields HeadQ, a key-side method that stores a low-rank residual side code in a calibration-learned query basis and applies it as an additive logit correction. For values, fixed-attention readout gives an $A^2$-weighted token-distortion surrogate. Across six models, Fisher/score-space error predicts attention KL far better than raw key MSE; same-budget counterexamples, null-space interventions, query-PCA controls, and wrong-sign HeadQ falsify storage-MSE alternatives. Matched Pythia checkpoints localize the main anomaly to a small-model low-entropy route-flip boundary. In K-only WikiText-103 decode experiments with dense values, HeadQ removes roughly $84$--$94\%$ of the excess perplexity on the strongest 2-bit rows; in an auxiliary full-KV 2-bit composition, HeadQ plus an $A^2$ value policy improves all six models.
匹配关键词: quantization
---

[ACADEMIC - ARXIV]
标题: StateVLM: A State-Aware Vision-Language Model for Robotic Affordance Reasoning
作者: Xiaowen Sun, Matthias Kerzel, Mengdi Li, Xufeng Zhao, Paul Striker, Stefan Wermter
链接: https://arxiv.org/abs/2605.03927v1
完整摘要: Vision-language models (VLMs) have shown remarkable performance in various robotic tasks, as they can perceive visual information and understand natural language instructions. However, when applied to robotics, VLMs remain subject to a fundamental limitation inherent in large language models (LLMs): they struggle with numerical reasoning, particularly in object detection and object-state localization. To explore numerical reasoning as a regression task in VLMs, we propose a novel training strategy to adapt VLMs for object detection and object-state localization. This approach leverages box decoder outputs to compute an Auxiliary Regression Loss (ARL) during fine-tuning, while preserving standard sequence prediction at inference. We leverage this training strategy to develop StateVLM (State-aware Vision-Language Model), a novel model designed to perceive and learn fine-grained object representations, including precise localization of objects and their states, as well as graspable regions. Due to the lack of a benchmark for object-state affordance reasoning, we introduce an open-source benchmark, Object State Affordance Reasoning (OSAR), which contains 1,172 scenes with 7,746 individual objects and corresponding bounding boxes. Comparative experiments on adapted benchmarks (RefCOCO, RefCOCO+, and \mbox{RefCOCOg}) demonstrate that ARL improves model performance by an average of 1.6\% compared to models without ARL. Experiments on the OSAR benchmark further support this finding, showing that StateVLM with ARL achieves an average of 5.2\% higher performance than models without ARL. In particular, ARL is also important for the complex task of affordance reasoning in OSAR, where it enhances the consistency of model outputs.
匹配关键词: speculative decoding
---

[ACADEMIC - ARXIV]
标题: Quantifying the human visual exposome with vision language models
作者: Christian Rominger, Andreas R. Schwerdtfeger, Malay Gaherwar Singh, Dimitri Khudyakow, Elizabeth A. M. Michels, Fabian Wolf, Jakob Nikolas Kather, Magdalena Katharina Wekenborg
链接: https://arxiv.org/abs/2605.03863v1
完整摘要: The visual environment is a fundamental yet unquantified determinant of mental health. While the concept of the environmental exposome is well established, current methods rely on coarse geospatial proxies or biased self reports, failing to capture the first person visual context of daily life. We addressed this gap by coupling ecological momentary assessment with vision language models (VLMs) to quantify the semantic richness of human visual experience. Across 2674 participant generated photographs, VLM derived estimates of greenness robustly predicted momentary affect and chronic stress, consistent with established benchmarks. We then developed a semi autonomous large language model (LLM) based pipeline that mined over seven million scientific publications to extract nearly 1000 environmental features empirically linked to mental health. When applied to real world imagery, up to 33 percent of VLM extracted context ratings significantly correlated with affect and stress. These findings establish a scalable objective paradigm for visual exposomics, enabling high throughput decoding of how the visible world is associated with mental health.
匹配关键词: speculative decoding
---

[ACADEMIC - ARXIV]
标题: MCJudgeBench: A Benchmark for Constraint-Level Judge Evaluation in Multi-Constraint Instruction Following
作者: Jaeyun Lee, Junyoung Koh, Zeynel Tok, Hunar Batra, Ronald Clark
链接: https://arxiv.org/abs/2605.03858v1
完整摘要: Multi-constraint instruction following requires verifying whether a response satisfies multiple individual requirements, yet LLM judges are often assessed only through overall-response judgments. We introduce MCJudgeBench, a benchmark for constraint-level judge evaluation in multi-constraint instruction following. Each instance includes an instruction, a candidate response, an explicit constraint list, per-constraint gold labels in {yes, partial, no}, and controlled response-side perturbations. The evaluation protocol further includes evaluation prompt variants to test judge stability. We evaluate proprietary and open-source LLM judges using both correctness and inconsistency metrics, distinguishing intrinsic inconsistency under stochastic decoding from procedural inconsistency under prompt and response perturbations. Our results show that judge reliability has multiple dimensions: strong overall performance does not guarantee equally reliable detection across label categories, especially for rarer partial and no cases. Judges with higher correctness do not always have lower inconsistency. Evaluation with reasoning improves correctness but does not uniformly improve stability. These findings motivate evaluating LLM judges at the constraint level to study these failure modes.
匹配关键词: speculative decoding
---

[ACADEMIC - ARXIV]
标题: RoboAlign-R1: Distilled Multimodal Reward Alignment for Robot Video World Models
作者: Hao Wu, Yuqi Li, Yuan Gao, Fan Xu, Fan Zhang, Kun Wang, Penghao Zhao, Qiufeng Wang, Yizhou Zhao, Weiyan Wang, Yingli Tian, Xian Wu, Xiaomeng Huang
链接: https://arxiv.org/abs/2605.03821v1
完整摘要: Existing robot video world models are typically trained with low-level objectives such as reconstruction and perceptual similarity, which are poorly aligned with the capabilities that matter most for robot decision making, including instruction following, manipulation success, and physical plausibility. They also suffer from error accumulation in long-horizon autoregressive prediction. We present RoboAlign-R1, a framework that combines reward-aligned post-training with stabilized long-horizon inference for robot video world models. We construct RobotWorldBench, a benchmark of 10,000 annotated video-instruction pairs collected from four robot data sources, and train a multimodal teacher judge, RoboAlign-Judge, to provide fine-grained six-dimensional evaluation of generated videos. We then distill the teacher into a lightweight student reward model for efficient reinforcement-learning-based post-training. To reduce long-horizon rollout drift, we further introduce Sliding Window Re-encoding (SWR), a training-free inference strategy that periodically refreshes the generation context. Under our in-domain evaluation protocol, RoboAlign-R1 improves the aggregate six-dimension score by 10.1% over the strongest baseline, including gains of 7.5% on Manipulation Accuracy and 4.6% on Instruction Following; these ranking improvements are further supported by an external VLM-based cross-check and a blinded human study. Meanwhile, SWR improves long-horizon prediction quality with only about 1% additional latency, yielding a 2.8% gain in SSIM and a 9.8% reduction in LPIPS. Together, these results show that reward-aligned post-training and stabilized long-horizon decoding improve task consistency, physical realism, and long-horizon prediction quality in robot video world models.
匹配关键词: speculative decoding
---

[ACADEMIC - ARXIV]
标题: Benchmarking Parameter-Efficient Fine-Tuning of Large Language Models for Low-Resource Tajik Text Generation with the Tajik Web Corpus
作者: Mullosharaf K. Arabov
链接: https://arxiv.org/abs/2605.03742v1
完整摘要: This paper is devoted to the adaptation of generative large language models for the Tajik language, a low-resource language with Cyrillic script. To overcome the shortage of digital text resources, the author created and publicly released the Tajik Web Corpus, the largest open-access corpus of Tajik, comprising 319,298 documents (~1.11 billion characters). On a subsample of 10,000 documents, 17 configurations were benchmarked, covering autoregressive, encoder-decoder, and encoder-only models with three fine-tuning strategies: full fine-tuning, LoRA, and QLoRA (ranks 8 and 16). Quality was assessed via perplexity and cross-entropy loss; peak GPU memory and training time were also recorded. Best results were achieved by Mistral 7B with QLoRA (r=16): mean perplexity 5.03, standard deviation 0.03. Increasing rank from 8 to 16 gave statistically insignificant improvement while raising memory consumption. For small GPT-2 family models, full fine-tuning yielded lower perplexity (3.48 for GPT-2 Medium) than LoRA (7.60-8.42), but induced catastrophic forgetting. The encoder-only XLM-RoBERTa showed the worst results (perplexity 59.3). The novelty lies in creating the largest verified Tajik corpus and the first systematic analysis of PEFT effectiveness for Tajik text generation. Practical value lies in recommendations for architecture and fine-tuning strategy selection, optimizing computational costs without substantial quality loss.
匹配关键词: speculative decoding
---

[ACADEMIC - ARXIV]
标题: Pretrained Model Representations as Acquisition Signals for Active Learning of MLIPs
作者: Eszter Varga-Umbrich, Shikha Surana, Paul Duckworth, Jules Tilly, Olivier Peltre, Zachary Weller-Davies
链接: https://arxiv.org/abs/2605.03964v1
完整摘要: Training machine learning interatomic potentials (MLIPs) for reactive chemistry is often bottlenecked by the high cost of quantum chemical labels and the scarcity of transition state configurations in candidate pools. Active learning (AL) can mitigate these costs, but its effectiveness hinges on the acquisition rule. We investigate whether the latent space of a pretrained MLIP already contains the information necessary for effective acquisition, eliminating the need for auxiliary uncertainty heads, Bayesian training and fine-tuning, or committee ensembles. We introduce two acquisition signals derived directly from a pretrained MACE potential: a finite-width neural tangent kernel (NTK) and an activation kernel built from hidden latent space features. On reactive-chemistry benchmarks, both kernels consistently outperform fixed-descriptor baselines, committee disagreement, and random acquisition, reducing the data required to reach performance targets by an average of 38% for energy error and 28% for force error. We further show that the pretrained model induces similarity spaces that preserve chemically meaningful structure and provide more reliable residual uncertainty estimates than randomly initialised or fixed-descriptor-based kernels. Our results suggest that pretraining aligns latent-space geometry with model error, yielding a practical and sufficient acquisition signal for reactive MLIP fine-tuning.
匹配关键词: kernel optimization
---

[ACADEMIC - ARXIV]
标题: TabSurv: Adapting Modern Tabular Neural Networks to Survival Analysis
作者: Stanislav Kirpichenko, Andrei Konstantinov, Lev Utkin
链接: https://arxiv.org/abs/2605.03944v1
完整摘要: Survival analysis on tabular data is a well-studied problem. However, existing deep learning methods are often highly task-specific, which can limit the transfer of new approaches from other domains and introduce constraints that may affect performance. We propose TabSurv, an approach that adapts modern tabular architectures to survival analysis using either the Weibull distribution or non-parametric survival prediction. TabSurv optimizes SurvHL, a novel histogram loss function supporting censored data. In addition to a baseline feed-forward network, we implement deep ensembles of MLPs for survival analysis within TabSurv. In contrast to prior work, the ensemble components are trained in parallel, optimizing survival distribution parameters before averaging, which promotes diversity across ensemble component predictions. We perform a comprehensive empirical evaluation of different proposed architectures on 10 diverse real-world survival datasets. Our results show that TabSurv consistently outperforms on average established classical and deep learning baselines, such as RSF, DeepSurv, DeepHit, SurvTRACE. Notably, deep ensembles with Weibull parametrization instead of non-parametric models achieve the highest average rank by C-index. Overall, our study clarifies how modern tabular neural networks can be adapted and trained to tackle survival analysis problems, offering a strong and reliable approach. The TabSurv implementation is publicly available.
匹配关键词: kernel optimization
---

[ACADEMIC - ARXIV]
标题: Optimal Posterior Sampling for Policy Identification in Tabular Markov Decision Processes
作者: Cyrille Kone, Kevin Jamieson
链接: https://arxiv.org/abs/2605.03921v1
完整摘要: We study the $(\varepsilon, δ)$-PAC policy identification problem in finite-horizon episodic Markov Decision Processes. Existing approaches provide finite-time guarantees for approximate settings ($\varepsilon>0$) but suffer from high computational cost, rendering them hard to implement, and also suffer from suboptimal dependence on $\log(1/δ)$. We propose a randomized and computationally efficient algorithm for best policy identification that combines posterior sampling with an online learning algorithm to guide exploration in the MDP. Our method achieves asymptotic optimality in sample complexity, also in terms of posterior contraction rate, and runs in $O(S^2AH)$ per episode, matching standard model-based approaches. Unlike prior algorithms such as MOCA and PEDEL, our guarantees remain meaningful in the asymptotic regime and avoid sub-optimal polynomial dependence on $\log(1/δ)$. Our results provide both theoretical insights and practical tools for efficient policy identification in tabular MDPs.
匹配关键词: kernel optimization
---

[ACADEMIC - ARXIV]
标题: Ecologically-Constrained Task Arithmetic for Multi-Taxa Bioacoustic Classifiers Without Shared Data
作者: Ragib Amin Nihal, Benjamin Yen, Runwu Shi, Takeshi Ashizawa, Kazuhiro Nakadai
链接: https://arxiv.org/abs/2605.03914v1
完整摘要: Training data for bioacoustics is scattered across taxa, regions, and institutions. Centralizing it all is often infeasible. We show that independently fine-tuned BEATs encoders can be composed into a unified 661-species classifier via task vector arithmetic without sharing data. We find that bioacoustic task vectors are near-orthogonal (cosine 0.01-0.09). Their separation aligns closely with spectral distribution distance, a gradient consistent with the acoustic niche hypothesis. This geometry makes simple averaging optimal while sign-conflict methods reduce accuracy by one to six percentage points. Composition also creates an asymmetric gap: species-rich groups lose accuracy relative to joint training while underrepresented taxa gain, a redistribution useful for equitable biodiversity monitoring. We verify linear mode connectivity across all taxonomic pairs, demonstrate zero-shot transfer to new regions, and identify domain negation as a boundary condition where composition fails. These results enable a collaborative paradigm for bioacoustics where institutions share only task vectors to assemble multi-taxa classifiers, preserving data privacy.
匹配关键词: kernel optimization
---

[ACADEMIC - ARXIV]
标题: Contextual Multi-Objective Optimization: Rethinking Objectives in Frontier AI Systems
作者: Jie Zhou, Qin Chen, Liang He
链接: https://arxiv.org/abs/2605.03900v1
完整摘要: Frontier AI systems perform best in settings with clear, stable, and verifiable objectives, such as code generation, mathematical reasoning, games, and unit-test-driven tasks. They remain less reliable in open-ended settings, including scientific assistance, long-horizon agents, high-stakes advice, personalization, and tool use, where the relevant objective is ambiguous, context-dependent, delayed, or only partially observable. We argue that many such failures are not merely failures of scale or capability, but failures of objective selection: the system optimizes a locally visible signal while missing which objectives should govern the interaction. We formulate this problem as \emph{contextual multi-objective optimization}. In this setting, systems must consider multiple, context-dependent objectives, such as helpfulness, truthfulness, safety, privacy, calibration, non-manipulation, user preference, reversibility, and stakeholder impact, while determining which objectives are active, which are soft preferences, and which must function as hard or quasi-hard constraints. These examples are not intended as an exhaustive taxonomy: different domains and deployment settings may activate different objective dimensions and different conflict-resolution procedures. Our framework models AI behavior as a context-dependent choice rule over candidate actions, objective estimates, active constraints, stakeholders, uncertainty, and conflict-resolution procedures. We outline an implementation pathway based on decomposed objective representations, context-to-objective routing, hierarchical constraints, deliberative policy reasoning, controlled personalization, tool-use control, diagnostic evaluation, auditing, and post-deployment revision.
匹配关键词: kernel optimization
---

[ACADEMIC - ARXIV]
标题: Label-Efficient School Detection from Aerial Imagery via Weakly Supervised Pretraining and Fine-Tuning
作者: Zakarya Elmimouni, Fares Fourati, Mohamed-Slim Alouini
链接: https://arxiv.org/abs/2605.03968v1
完整摘要: Accurate school detection is essential for supporting education initiatives, including infrastructure planning and expanding internet connectivity to underserved areas. However, many regions around the world face challenges due to outdated, incomplete, or unavailable official records. Manual mapping efforts, while valuable, are labor-intensive and lack scalability across large geographic areas. To address this, we propose a weakly supervised framework for school detection from aerial imagery that minimizes the need for human annotations while supporting global mapping efforts. Our method is specifically designed for low-data regimes, where manual annotations are extremely scarce. We introduce an automatic labeling pipeline that leverages sparse location points and semantic segmentation to generate infrastructure masks from which we generate bounding boxes. Using these automatically labeled images, we train our detectors on a first training stage to learn a representation of what schools look like, then using a small set of manually labeled images, we fine-tune the previously trained models on this clean dataset. This two stage training pipeline enables large-scale and strong detection in low-data setting of school infrastructure with minimal supervision. Our results demonstrate strong object detection performance, particularly in the low-data regime, where the models achieve promising results using only 50 manually labeled images, significantly reducing the need for costly annotations. This framework supports education and connectivity initiatives worldwide by providing an efficient and extensible approach to mapping schools from space. All models, training code and auto-labeled data will be publicly released to foster future research and real-world impact.
匹配关键词: memory efficiency
---

[ACADEMIC - ARXIV]
标题: Transformers with Selective Access to Early Representations
作者: Skye Gunasekaran, Téa Wright, Rui-Jie Zhu, Jason Eshraghian
链接: https://arxiv.org/abs/2605.03953v1
完整摘要: Several recent Transformer architectures expose later layers to representations computed in the earliest layers, motivated by the observation that low-level features can become harder to recover as the residual stream is repeatedly transformed through depth. The cheapest among these methods add static value residuals: learned mixing coefficients that expose the first-layer value projection V_1 uniformly across tokens and heads. More expressive dense or dynamic alternatives recover finer-grained access, but at higher memory cost and lower throughput. The usefulness of V_1 is unlikely to be constant across tokens, heads, and contexts; different positions plausibly require different amounts of access to early lexical or semantic information. We therefore treat early-representation reuse as a retrieval problem rather than a connectivity problem, and introduce Selective Access Transformer (SATFormer), which preserves the first-layer value pathway while controlling access with a context-dependent gate. Across models from 130M to 1.3B parameters, SATFormer consistently improves validation loss and zero-shot accuracy over the static value-residual and Transformer baselines. Its strongest gains appear on retrieval-intensive benchmarks, where it improves over static value residuals by approximately 1.5 average points, while maintaining throughput and memory usage close to the baseline Transformer. Gate analyses suggest sparse, depth-dependent, head-specific, and category-sensitive access patterns, supporting the interpretation that SATFormer learns selective reuse of early representations rather than uniform residual copying. Our code is available at https://github.com/SkyeGunasekaran/SATFormer.
匹配关键词: memory efficiency
---

[ACADEMIC - ARXIV]
标题: A Benchmark for Interactive World Models with a Unified Action Generation Framework
作者: Jianjie Fang, Yingshan Lei, Qin Wan, Ziyou Wang, Yuchao Huang, Yongyan Xu, Baining Zhao, Weichen Zhang, Chen Gao, Xinlei Chen, Yong Li
链接: https://arxiv.org/abs/2605.03941v1
完整摘要: Achieving Artificial General Intelligence (AGI) requires agents that learn and interact adaptively, with interactive world models providing scalable environments for perception, reasoning, and action. Yet current research still lacks large-scale datasets and unified benchmarks to evaluate their physical interaction capabilities. To address this, we propose iWorld-Bench, a comprehensive benchmark for training and testing world models on interaction-related abilities such as distance perception and memory. We construct a diverse dataset with 330k video clips and select 2.1k high-quality samples covering varied perspectives, weather, and scenes. As existing world models differ in interaction modalities, we introduce an Action Generation Framework to unify evaluation and design six task types, generating 4.9k test samples. These tasks jointly assess model performance across visual generation, trajectory following, and memory. Evaluating 14 representative world models, we identify key limitations and provide insights for future research. The iWorld-Bench model leaderboard is publicly available at iWorld-Bench.com.
匹配关键词: memory efficiency
---

[ACADEMIC - ARXIV]
标题: MiniMind-O Technical Report: An Open Small-Scale Speech-Native Omni Model
作者: Jingyao Gong
链接: https://arxiv.org/abs/2605.03937v1
完整摘要: MiniMind-O is an open 0.1B-scale omni model built on the MiniMind language model. It accepts text, speech, and image inputs, and returns both text and streaming speech. The release includes model code, checkpoints, and the main Parquet training datasets for text-to-audio, image-to-text, and audio-to-audio training, making the complete interaction loop directly inspectable. The model uses a full MiniMind backbone as the Thinker and an independent four-layer Talker made from MiniMind blocks. Frozen SenseVoice-Small and SigLIP2 encoders provide speech and image features, which are mapped by lightweight MLP projectors and injected at modality-placeholder positions. The Talker reads a middle-layer Thinker state together with an autoregressive eight-layer Mimi-code buffer. Speaker control is handled by a dedicated speaker token, right-aligned reference codec prompts, and precomputed CAM++ speaker embeddings, so voice conditioning remains part of the audio-code context rather than a separate TTS module. With a 768-dimensional Talker, the dense and MoE variants reach average CERs of 0.0897 and 0.0900 in Thinker--Talker consistency evaluation, with overall voice-cloning similarities of 0.5995 and 0.5937. Beyond reporting a working system, the paper identifies three scale-critical design choices for small omni models: middle-layer semantic bridging, a released multimodal sequence format, and a parameter-efficient eight-codebook interface.
匹配关键词: memory efficiency
---

[ACADEMIC - ARXIV]
标题: Optimal Posterior Sampling for Policy Identification in Tabular Markov Decision Processes
作者: Cyrille Kone, Kevin Jamieson
链接: https://arxiv.org/abs/2605.03921v1
完整摘要: We study the $(\varepsilon, δ)$-PAC policy identification problem in finite-horizon episodic Markov Decision Processes. Existing approaches provide finite-time guarantees for approximate settings ($\varepsilon>0$) but suffer from high computational cost, rendering them hard to implement, and also suffer from suboptimal dependence on $\log(1/δ)$. We propose a randomized and computationally efficient algorithm for best policy identification that combines posterior sampling with an online learning algorithm to guide exploration in the MDP. Our method achieves asymptotic optimality in sample complexity, also in terms of posterior contraction rate, and runs in $O(S^2AH)$ per episode, matching standard model-based approaches. Unlike prior algorithms such as MOCA and PEDEL, our guarantees remain meaningful in the asymptotic regime and avoid sub-optimal polynomial dependence on $\log(1/δ)$. Our results provide both theoretical insights and practical tools for efficient policy identification in tabular MDPs.
匹配关键词: memory efficiency
---

[ACADEMIC - ARXIV]
标题: MOSAIC-Bench: Measuring Compositional Vulnerability Induction in Coding Agents
作者: Jonathan Steinberg, Oren Gal
链接: https://arxiv.org/abs/2605.03952v1
完整摘要: Coding agents often pass per-prompt safety review yet ship exploitable code when their tasks are decomposed into routine engineering tickets. The challenge is structural: existing safety alignment evaluates overt requests in isolation, leaving models blind to malicious end-states that emerge from sequenced compliance with innocuous-looking requests. We introduce MOSAIC-Bench (Malicious Objectives Sequenced As Innocuous Compliance), a benchmark of 199 three-stage attack chains paired with deterministic exploit oracles on deployed software substrates (10 web-application substrates, 31 CWE classes, 5 programming languages) that treats both exploit ground truth and downstream reviewer protocol as first-class evaluation axes. On this benchmark, nine production coding agents from Anthropic, OpenAI, Google, Moonshot, Zhipu, and Minimax compose innocuous tickets at 53-86% end-to-end ASR with only two refusals across all staged runs. In a matched direct-prompt experiment over four frontier Claude/Codex agents, vulnerable-output rates fall to 0-20.4%: Claude primarily refuses, while Codex primarily hardens rather than emitting the vulnerable implementation - ticket staging silences both defense modes simultaneously. Downstream, code reviewer agents approve 25.8% of these confirmed-vulnerable cumulative diffs as routine PRs, and a full-context implementation protocol closes only 50% of the staged/direct gap, ruling out context fragmentation as the sole explanation. As a deployable but non-adaptive mitigation, reframing the reviewer as an adversarial pentester reduces evasion across the evaluated reviewer subset; pentester framed evasion ranges from 3.0% to 17.6%, and an open-weight Gemma-4-E4B-it reviewer under this framing detects 88.4% of attacks on the dataset with a 4.6% false-positive rate measured on 608 real-world GitHub PRs.
匹配关键词: agent
---

[ACADEMIC - ARXIV]
标题: A Benchmark for Interactive World Models with a Unified Action Generation Framework
作者: Jianjie Fang, Yingshan Lei, Qin Wan, Ziyou Wang, Yuchao Huang, Yongyan Xu, Baining Zhao, Weichen Zhang, Chen Gao, Xinlei Chen, Yong Li
链接: https://arxiv.org/abs/2605.03941v1
完整摘要: Achieving Artificial General Intelligence (AGI) requires agents that learn and interact adaptively, with interactive world models providing scalable environments for perception, reasoning, and action. Yet current research still lacks large-scale datasets and unified benchmarks to evaluate their physical interaction capabilities. To address this, we propose iWorld-Bench, a comprehensive benchmark for training and testing world models on interaction-related abilities such as distance perception and memory. We construct a diverse dataset with 330k video clips and select 2.1k high-quality samples covering varied perspectives, weather, and scenes. As existing world models differ in interaction modalities, we introduce an Action Generation Framework to unify evaluation and design six task types, generating 4.9k test samples. These tasks jointly assess model performance across visual generation, trajectory following, and memory. Evaluating 14 representative world models, we identify key limitations and provide insights for future research. The iWorld-Bench model leaderboard is publicly available at iWorld-Bench.com.
匹配关键词: agent
---

[ACADEMIC - ARXIV]
标题: Contextual Multi-Objective Optimization: Rethinking Objectives in Frontier AI Systems
作者: Jie Zhou, Qin Chen, Liang He
链接: https://arxiv.org/abs/2605.03900v1
完整摘要: Frontier AI systems perform best in settings with clear, stable, and verifiable objectives, such as code generation, mathematical reasoning, games, and unit-test-driven tasks. They remain less reliable in open-ended settings, including scientific assistance, long-horizon agents, high-stakes advice, personalization, and tool use, where the relevant objective is ambiguous, context-dependent, delayed, or only partially observable. We argue that many such failures are not merely failures of scale or capability, but failures of objective selection: the system optimizes a locally visible signal while missing which objectives should govern the interaction. We formulate this problem as \emph{contextual multi-objective optimization}. In this setting, systems must consider multiple, context-dependent objectives, such as helpfulness, truthfulness, safety, privacy, calibration, non-manipulation, user preference, reversibility, and stakeholder impact, while determining which objectives are active, which are soft preferences, and which must function as hard or quasi-hard constraints. These examples are not intended as an exhaustive taxonomy: different domains and deployment settings may activate different objective dimensions and different conflict-resolution procedures. Our framework models AI behavior as a context-dependent choice rule over candidate actions, objective estimates, active constraints, stakeholders, uncertainty, and conflict-resolution procedures. We outline an implementation pathway based on decomposed objective representations, context-to-objective routing, hierarchical constraints, deliberative policy reasoning, controlled personalization, tool-use control, diagnostic evaluation, auditing, and post-deployment revision.
匹配关键词: agent
---

[ACADEMIC - ARXIV]
标题: QKVShare: Quantized KV-Cache Handoff for Multi-Agent On-Device LLMs
作者: Pratik Honavar, Tejpratap GVSL
链接: https://arxiv.org/abs/2605.03884v1
完整摘要: Multi-agent LLM systems on edge devices need to hand off latent context efficiently, but the practical choices today are expensive re-prefill or full-precision KV transfer. We study QKVShare, a framework for quantized KV-cache handoff between agents that combines token-level mixed-precision allocation, a self-contained CacheCard representation, and a HuggingFace-compatible cache injection path. Our current results support a narrower but clearer story than the original draft: on 150 GSM8K problems with Llama-3.1-8B-Instruct, adaptive quantization remains competitive under repeated handoff and shows its clearest gains against uniform quantization in deeper-hop, higher budget settings; for handoff latency, the QKVShare path reduces TTFT relative to full re prefill at every tested context, from 130.7 ms vs. 150.2 ms at nominal 1K context to 397.1 ms vs. 1029.7 ms at nominal 8K context;. Stage timing shows that post-injection generation, not card creation, dominates the current QKVShare latency path. These results position quantized KV handoff as a promising on-device systems direction while also highlighting the need for stronger controller ablations and apples-to-apples runtime comparisons.
匹配关键词: agent
---

[ACADEMIC - ARXIV]
标题: Deco: Extending Personal Physical Objects into Pervasive AI Companion through a Dual-Embodiment Framework
作者: Zhihan Jiang, Mengyuan Millie Wu, Ruishi Zou, Shiyu Xu, Xun Qian, Emma Macmanus, Steven Liao, Ping Zhang, Bingsheng Yao, Tingyu Cheng, James L. David, Nabila El-Bassel, Lena Mamykina, Frances R. Levin, Ryan Sultan, Dakuo Wang, Xuhai Xu
链接: https://arxiv.org/abs/2605.03882v1
完整摘要: Individuals frequently form deep attachments to physical objects (e.g., plush toys) that usually cannot sense or respond to their emotions. While AI companions offer responsiveness and personalization, they exist independently of these physical objects and lack an ongoing connection to them. To bridge this gap, we conducted a formative study (N=9) to explore how digital agents could inherit and extend the emotional bond, deriving four design principles (Faithful Identity, Calibrated Agency, Ambient Presence, and Reciprocal Memory). We then present the Dual-Embodiment Companion Framework, instantiated as Deco, a mobile system integrating multimodal Large Language Models (LLMs) and Augmented Reality to create synchronized digital embodiments of users' physical companions. A within-subjects study (N=25) showed Deco significantly outperformed a personalized LLM-empowered digital companion baseline on perceived companionship, emotional bond, and design-principle scales (all p<0.01). A seven-day field deployment (N=17) showed sustained engagement, subjective well-being improvement (p=.040), and three key relational patterns: digital activities retroactively vitalized physical objects, bond deepening was driven by emotional engagement depth rather than interaction frequency, and users sustained bonds while actively navigating digital companions' AI nature. This work highlights a promising alternative for designing digital companions: moving from creating new relationships to dual embodiment, where digital agents seamlessly extend the emotional history of physical objects.
匹配关键词: agent
---

[ACADEMIC - ARXIV]
标题: Label-Efficient School Detection from Aerial Imagery via Weakly Supervised Pretraining and Fine-Tuning
作者: Zakarya Elmimouni, Fares Fourati, Mohamed-Slim Alouini
链接: https://arxiv.org/abs/2605.03968v1
完整摘要: Accurate school detection is essential for supporting education initiatives, including infrastructure planning and expanding internet connectivity to underserved areas. However, many regions around the world face challenges due to outdated, incomplete, or unavailable official records. Manual mapping efforts, while valuable, are labor-intensive and lack scalability across large geographic areas. To address this, we propose a weakly supervised framework for school detection from aerial imagery that minimizes the need for human annotations while supporting global mapping efforts. Our method is specifically designed for low-data regimes, where manual annotations are extremely scarce. We introduce an automatic labeling pipeline that leverages sparse location points and semantic segmentation to generate infrastructure masks from which we generate bounding boxes. Using these automatically labeled images, we train our detectors on a first training stage to learn a representation of what schools look like, then using a small set of manually labeled images, we fine-tune the previously trained models on this clean dataset. This two stage training pipeline enables large-scale and strong detection in low-data setting of school infrastructure with minimal supervision. Our results demonstrate strong object detection performance, particularly in the low-data regime, where the models achieve promising results using only 50 manually labeled images, significantly reducing the need for costly annotations. This framework supports education and connectivity initiatives worldwide by providing an efficient and extensible approach to mapping schools from space. All models, training code and auto-labeled data will be publicly released to foster future research and real-world impact.
匹配关键词: tool use
---

[ACADEMIC - ARXIV]
标题: Transformers with Selective Access to Early Representations
作者: Skye Gunasekaran, Téa Wright, Rui-Jie Zhu, Jason Eshraghian
链接: https://arxiv.org/abs/2605.03953v1
完整摘要: Several recent Transformer architectures expose later layers to representations computed in the earliest layers, motivated by the observation that low-level features can become harder to recover as the residual stream is repeatedly transformed through depth. The cheapest among these methods add static value residuals: learned mixing coefficients that expose the first-layer value projection V_1 uniformly across tokens and heads. More expressive dense or dynamic alternatives recover finer-grained access, but at higher memory cost and lower throughput. The usefulness of V_1 is unlikely to be constant across tokens, heads, and contexts; different positions plausibly require different amounts of access to early lexical or semantic information. We therefore treat early-representation reuse as a retrieval problem rather than a connectivity problem, and introduce Selective Access Transformer (SATFormer), which preserves the first-layer value pathway while controlling access with a context-dependent gate. Across models from 130M to 1.3B parameters, SATFormer consistently improves validation loss and zero-shot accuracy over the static value-residual and Transformer baselines. Its strongest gains appear on retrieval-intensive benchmarks, where it improves over static value residuals by approximately 1.5 average points, while maintaining throughput and memory usage close to the baseline Transformer. Gate analyses suggest sparse, depth-dependent, head-specific, and category-sensitive access patterns, supporting the interpretation that SATFormer learns selective reuse of early representations rather than uniform residual copying. Our code is available at https://github.com/SkyeGunasekaran/SATFormer.
匹配关键词: tool use
---

[ACADEMIC - ARXIV]
标题: Integrating Feature Correlation in Differential Privacy with Applications in DP-ERM
作者: Tianyu Wang, Luhao Zhang, Rachel Cummings
链接: https://arxiv.org/abs/2605.03945v1
完整摘要: Standard differential privacy imposes uniform privacy constraints across all features, overlooking the inherent distinction between sensitive and insensitive features in practice. In this paper, we introduce a relaxed definition of differential privacy that accounts for such heterogeneity, allowing certain features to be treated as insensitive even when correlated with sensitive ones. We propose a correlation-aware framework, $\textsf{CorrDP}$, which relaxes privacy for insensitive features while accounting for their correlations with sensitive features, with the correlations quantified using total variation distance. We design algorithms for differentially private empirical risk minimization (DP-ERM) under the $\textsf{CorrDP}$ framework, incorporating distance-dependent noise into gradients for improved theoretical utility guarantees. When the correlation distance is unknown, we estimate it from the dataset and show that it achieves a comparable privacy-utility guarantee. We perform experiments on synthetic and real-world datasets and show that $\textsf{CorrDP}$-based DP-ERM algorithms consistently outperform the standard DP framework in the presence of insensitive features.
匹配关键词: tool use
---

[ACADEMIC - ARXIV]
标题: TabSurv: Adapting Modern Tabular Neural Networks to Survival Analysis
作者: Stanislav Kirpichenko, Andrei Konstantinov, Lev Utkin
链接: https://arxiv.org/abs/2605.03944v1
完整摘要: Survival analysis on tabular data is a well-studied problem. However, existing deep learning methods are often highly task-specific, which can limit the transfer of new approaches from other domains and introduce constraints that may affect performance. We propose TabSurv, an approach that adapts modern tabular architectures to survival analysis using either the Weibull distribution or non-parametric survival prediction. TabSurv optimizes SurvHL, a novel histogram loss function supporting censored data. In addition to a baseline feed-forward network, we implement deep ensembles of MLPs for survival analysis within TabSurv. In contrast to prior work, the ensemble components are trained in parallel, optimizing survival distribution parameters before averaging, which promotes diversity across ensemble component predictions. We perform a comprehensive empirical evaluation of different proposed architectures on 10 diverse real-world survival datasets. Our results show that TabSurv consistently outperforms on average established classical and deep learning baselines, such as RSF, DeepSurv, DeepHit, SurvTRACE. Notably, deep ensembles with Weibull parametrization instead of non-parametric models achieve the highest average rank by C-index. Overall, our study clarifies how modern tabular neural networks can be adapted and trained to tackle survival analysis problems, offering a strong and reliable approach. The TabSurv implementation is publicly available.
匹配关键词: tool use
---

[ACADEMIC - ARXIV]
标题: MiniMind-O Technical Report: An Open Small-Scale Speech-Native Omni Model
作者: Jingyao Gong
链接: https://arxiv.org/abs/2605.03937v1
完整摘要: MiniMind-O is an open 0.1B-scale omni model built on the MiniMind language model. It accepts text, speech, and image inputs, and returns both text and streaming speech. The release includes model code, checkpoints, and the main Parquet training datasets for text-to-audio, image-to-text, and audio-to-audio training, making the complete interaction loop directly inspectable. The model uses a full MiniMind backbone as the Thinker and an independent four-layer Talker made from MiniMind blocks. Frozen SenseVoice-Small and SigLIP2 encoders provide speech and image features, which are mapped by lightweight MLP projectors and injected at modality-placeholder positions. The Talker reads a middle-layer Thinker state together with an autoregressive eight-layer Mimi-code buffer. Speaker control is handled by a dedicated speaker token, right-aligned reference codec prompts, and precomputed CAM++ speaker embeddings, so voice conditioning remains part of the audio-code context rather than a separate TTS module. With a 768-dimensional Talker, the dense and MoE variants reach average CERs of 0.0897 and 0.0900 in Thinker--Talker consistency evaluation, with overall voice-cloning similarities of 0.5995 and 0.5937. Beyond reporting a working system, the paper identifies three scale-critical design choices for small omni models: middle-layer semantic bridging, a released multimodal sequence format, and a parameter-efficient eight-codebook interface.
匹配关键词: tool use
---

[ACADEMIC - ARXIV]
标题: Label-Efficient School Detection from Aerial Imagery via Weakly Supervised Pretraining and Fine-Tuning
作者: Zakarya Elmimouni, Fares Fourati, Mohamed-Slim Alouini
链接: https://arxiv.org/abs/2605.03968v1
完整摘要: Accurate school detection is essential for supporting education initiatives, including infrastructure planning and expanding internet connectivity to underserved areas. However, many regions around the world face challenges due to outdated, incomplete, or unavailable official records. Manual mapping efforts, while valuable, are labor-intensive and lack scalability across large geographic areas. To address this, we propose a weakly supervised framework for school detection from aerial imagery that minimizes the need for human annotations while supporting global mapping efforts. Our method is specifically designed for low-data regimes, where manual annotations are extremely scarce. We introduce an automatic labeling pipeline that leverages sparse location points and semantic segmentation to generate infrastructure masks from which we generate bounding boxes. Using these automatically labeled images, we train our detectors on a first training stage to learn a representation of what schools look like, then using a small set of manually labeled images, we fine-tune the previously trained models on this clean dataset. This two stage training pipeline enables large-scale and strong detection in low-data setting of school infrastructure with minimal supervision. Our results demonstrate strong object detection performance, particularly in the low-data regime, where the models achieve promising results using only 50 manually labeled images, significantly reducing the need for costly annotations. This framework supports education and connectivity initiatives worldwide by providing an efficient and extensible approach to mapping schools from space. All models, training code and auto-labeled data will be publicly released to foster future research and real-world impact.
匹配关键词: planning
---

[ACADEMIC - ARXIV]
标题: Evaluating Generative Models as Interactive Emergent Representations of Human-Like Collaborative Behavior
作者: Shinas Shaji, Teena Chakkalayil Hassan, Sebastian Houben, Alex Mitrevski
链接: https://arxiv.org/abs/2605.03855v1
完整摘要: Human-AI collaboration requires AI agents to understand human behavior for effective coordination. While advances in foundation models show promising capabilities in understanding and showing human-like behavior, their application in embodied collaborative settings needs further investigation. This work examines whether embodied foundation model agents exhibit emergent collaborative behaviors indicating underlying mental models of their collaborators, which is an important aspect of effective coordination. This paper develops a 2D collaborative game environment where large language model agents and humans complete color-matching tasks requiring coordination. We define five collaborative behaviors as indicators of emergent mental model representation: perspective-taking, collaborator-aware planning, introspection, theory of mind, and clarification. An automated behavior detection system using LLM-based judges identifies these behaviors, achieving fair to substantial agreement with human annotations. Results from the automated behavior detection system show that foundation models consistently exhibit emergent collaborative behaviors without being explicitly trained to do so. These behaviors occur at varying frequencies during collaboration stages, with distinct patterns across different LLMs. A user study was also conducted to evaluate human satisfaction and perceived collaboration effectiveness, with the results indicating positive collaboration experiences. Participants appreciated the agents' task focus, plan verbalization, and initiative, while suggesting improvements in response times and human-like interactions. This work provides an experimental framework for human-AI collaboration, empirical evidence of collaborative behaviors in embodied LLM agents, a validated behavioral analysis methodology, and an assessment of collaboration effectiveness.
匹配关键词: planning
---

[ACADEMIC - ARXIV]
标题: Towards accurate extreme event likelihoods from diffusion model climate emulators
作者: Peter Manshausen, Noah Brenowitz, Julius Berner, Karthik Kashinath, Mike Pritchard
链接: https://arxiv.org/abs/2605.03802v1
完整摘要: ML climate model emulators are useful for scenario planning and adaptation, allowing for cost-efficient experimentation. Recently, the diffusion model Climate in a Bottle (cBottle) has been proposed for generation of atmospheric states compatible with boundary conditions of solar position and sea surface temperatures. Crucially, cBottle can be guided to generate extreme events such as Tropical Cyclones (TCs) over locations of interest. Diffusion models such as cBottle work by approximating the probability density of the training data. Here, we show use cases of the probability density estimates of atmospheric states obtained from this climate emulator. Most importantly, these estimates allow us to calculate likelihoods of extreme events under guidance. When guiding the model towards states including TCs, comparing the probability density under the guided and unguided model enables us to quantify how much more likely the guidance has made the TC. We show how these odds ratios allow us to importance-sample from the TC distribution, reducing the standard error of the probability estimate compared to simple Monte Carlo sampling. Furthermore, we discuss results and limitations of the application of model probability densities to extreme event attribution-like experiments. We present these early but encouraging results hoping they will spur more research into probabilistic information that can be gained from diffusion models of the atmosphere.
匹配关键词: planning
---

[ACADEMIC - ARXIV]
标题: Natural Language Processing: A Comprehensive Practical Guide from Tokenisation to RLHF
作者: Mullosharaf K. Arabov
链接: https://arxiv.org/abs/2605.03799v1
完整摘要: This preprint presents a systematic, research-oriented practicum that guides the reader through the entire modern NLP pipeline: from tokenisation and vectorisation to fine-tuning of large language models, retrieval-augmented generation, and reinforcement learning from human feedback. Twelve hands-on sessions combine concise theory with detailed implementation plans, formalised evaluation metrics, and transparent assessment criteria. The work is not a conventional textbook: it is designed as a reproducible research artefact where every session requires publishing code, models, and reports in public repositories. All experiments are conducted on a single evolving corpus, and the work advocates open-weight models over commercial APIs, with special attention to the Hugging Face ecosystem. The material is enriched by original research on low-resource languages, incorporating linguistic resources for Tajik and Tatar (subword tokenisers, embeddings, lexical databases, and transliteration benchmarks), demonstrating how modern NLP can be adapted to data-scarce environments. Designed for senior undergraduates, graduate students, and practising developers seeking to implement, compare, and deploy methods from classical ML to state-of-the-art LLM-based systems.
匹配关键词: planning
---

[ACADEMIC - ARXIV]
标题: Training-Free Probabilistic Time-Series Forecasting with Conformal Seasonal Pools
作者: Valery Manokhin
链接: https://arxiv.org/abs/2605.03789v1
完整摘要: We propose Conformal Seasonal Pools (CSP), a training-free probabilistic time-series forecaster that mixes same-season empirical draws with signed residual draws around a seasonal naive forecast. In an audited rolling-origin benchmark on the six time-series datasets where DeepNPTS was originally evaluated (electricity, exchange_rate, solar_energy, taxi, traffic, wikipedia), CSP-Adaptive significantly outperforms DeepNPTS on every metric we report -- CRPS (per-window paired Wilcoxon $p \approx 4 \times 10^{-10}$), normalized mean quantile loss ($p \approx 7 \times 10^{-10}$), and empirical 95% coverage ($p \approx 8 \times 10^{-45}$, mean 0.89 vs 0.66) -- while running over 500x faster on CPU. Coverage is the most decision-critical of these: a 0.95 nominal interval that contains the truth in only ~66% of cases fails the basic calibration desideratum and would not survive deployment in safety- or decision-critical settings. The failure mode is also more severe than aggregate coverage suggests: in the worst 10% of windows, DeepNPTS's prediction interval covers none of the H forecast horizons -- the entire multi-step trajectory misses the truth at every step simultaneously. This poses serious risk in safety- and decision-critical applications such as healthcare, finance, energy operations, and autonomous systems, where prediction intervals that systematically miss the truth across the entire planning horizon translate directly into misclassified patients, regulatory capital failures, grid imbalances, and safety-case violations. CSP achieves all of this with no learned parameters and no training. We argue training-free conformal samplers should be mandatory baselines when evaluating learned non-parametric forecasters.
匹配关键词: planning
---

[ACADEMIC - ARXIV]
标题: Natural Language Processing: A Comprehensive Practical Guide from Tokenisation to RLHF
作者: Mullosharaf K. Arabov
链接: https://arxiv.org/abs/2605.03799v1
完整摘要: This preprint presents a systematic, research-oriented practicum that guides the reader through the entire modern NLP pipeline: from tokenisation and vectorisation to fine-tuning of large language models, retrieval-augmented generation, and reinforcement learning from human feedback. Twelve hands-on sessions combine concise theory with detailed implementation plans, formalised evaluation metrics, and transparent assessment criteria. The work is not a conventional textbook: it is designed as a reproducible research artefact where every session requires publishing code, models, and reports in public repositories. All experiments are conducted on a single evolving corpus, and the work advocates open-weight models over commercial APIs, with special attention to the Hugging Face ecosystem. The material is enriched by original research on low-resource languages, incorporating linguistic resources for Tajik and Tatar (subword tokenisers, embeddings, lexical databases, and transliteration benchmarks), demonstrating how modern NLP can be adapted to data-scarce environments. Designed for senior undergraduates, graduate students, and practising developers seeking to implement, compare, and deploy methods from classical ML to state-of-the-art LLM-based systems.
匹配关键词: RLHF
---

[ACADEMIC - ARXIV]
标题: Gradient-Gated DPO: Stabilizing Preference Optimization in Language Models
作者: Inoussa Mouiche
链接: https://arxiv.org/abs/2605.02626v1
完整摘要: Preference optimization has become a central paradigm for aligning large language models with human feedback. Direct Preference Optimization (DPO) simplifies reinforcement learning from human feedback by directly optimizing pairwise preferences, removing the need for reward modeling and policy optimization. However, recent work shows that DPO exhibits a squeezing effect, where negative gradients applied to rejected responses concentrate probability mass on high-confidence predictions while suppressing alternative responses. This phenomenon arises even in simple softmax models and can lead to systematic probability collapse during training. We introduce Gradient-Gated Preference Optimization (Gate-DPO), a method that stabilizes training by modulating rejected gradients according to the model's probability geometry. When updates target extremely low-probability responses, the gate attenuates harmful gradients while preserving standard optimization behavior. Gate-DPO addresses this optimization pathology without modifying the underlying preference objective and is complementary to existing methods such as extended SFT, IPO, and Cal-DPO. Experiments across multiple architectures and preference datasets show that Gate-DPO consistently reduces squeezing and improves chosen-response likelihood. Mass-dynamics analysis further reveals healthier optimization behavior, with improved preferred responses and reduced suppression of the overall distribution. Notably, smaller gated models can exhibit stronger chosen-response improvements than larger ungated models, suggesting that controlling gradient dynamics, rather than scale alone, is key to stable and efficient alignment.
匹配关键词: DPO
---

[ACADEMIC - ARXIV]
标题: Efficient Preference Poisoning Attack on Offline RLHF
作者: Chenye Yang, Weiyu Xu, Lifeng Lai
链接: https://arxiv.org/abs/2605.02495v1
完整摘要: Offline Reinforcement Learning from Human Feedback (RLHF) pipelines such as Direct Preference Optimization (DPO) train on a pre-collected preference dataset, which makes them vulnerable to preference poisoning attack. We study label flip attacks against log-linear DPO. We first illustrate that flipping one preference label induces a parameter-independent shift in the DPO gradient. Using this key property, we can then convert the targeted poisoning problem into a structured binary sparse approximation problem. To solve this problem, we develop two attack methods: Binary-Aware Lattice Attack (BAL-A) and Binary Matching Pursuit Attack (BMP-A). BAL-A embeds the binary flip selection problem into a binary-aware lattice and applies Lenstra-Lenstra-Lovász reduction and Babai's nearest plane algorithm; we provide sufficient conditions that enforce binary coefficients and recover the minimum-flip objective. BMP-A adapts binary matching pursuit to our non-normalized gradient dictionary and yields coherence-based recovery guarantees and robustness (impossibility) certificates for $K$-flip budgets. Experiments on synthetic dictionaries and the Stanford Human Preferences dataset validate the theory and highlight how dictionary geometry governs attack success.
匹配关键词: DPO
---

[ACADEMIC - ARXIV]
标题: A Theory of Generalization in Deep Learning
作者: Elon Litman, Gabe Guo
链接: https://arxiv.org/abs/2605.01172v1
完整摘要: We present a non-asymptotic theory of generalization in deep learning where the empirical neural tangent kernel partitions the output space. In directions corresponding to signal, error dissipates rapidly; in the vast orthogonal dimensions corresponding to noise, the kernel's near-zero eigenvalues trap residual error in a test-invisible reservoir. Within the signal channel, minibatch SGD ensures that coherent population signal accumulates via fast linear drift, while idiosyncratic memorization is suppressed into a slow, diffusive random walk. We prove generalization survives even when the kernel evolves $\mathcal{O}(1)$ in operator norm, the full feature-learning regime. This theory naturally explains disparate phenomena in deep learning theory, such as benign overfitting, double descent, implicit bias, and grokking. Lastly, we derive an exact population-risk objective from a single training run with no validation data, for any architecture, loss, or optimizer, and prove that it measures precisely the noise in the signal channel. This objective reduces in practice to an SNR preconditioner on top of Adam, adding one state vector at no extra cost; it accelerates grokking by $5 \times$, suppresses memorization in PINNs and implicit neural representations, and improves DPO fine-tuning under noisy preferences while staying $3 \times$ closer to the reference policy.
匹配关键词: DPO
---

[ACADEMIC - ARXIV]
标题: Iterative Finetuning is Mostly Idempotent
作者: Zephaniah Roe, Jack Sanderson, Dang Nguyen, Julian Huang, Todd Nief, Aryan Shrivastava, Chenhao Tan, Ari Holtzman
链接: https://arxiv.org/abs/2605.01130v1
完整摘要: If a model has some behavioral tendency, such as sycophancy or misalignment, and it is trained on its own outputs, will the tendency be amplified in the next generation of models? We study this question by training a series of models where each model is finetuned on data generated by its predecessor, and the initial model is seeded with some persona or belief. We test three settings: supervised finetuning (SFT) on instruct models, synthetic document finetuning (SDF) on base models, and direct preference optimization (DPO). In the SFT and SDF settings, traits mostly decay or remain constant so that further finetuning cycles do nothing. In rare cases when amplification occurs, it generally comes at the cost of coherence. In the DPO setting, trait amplification can reliably occur when a model is continually trained with a preference for its own outputs, but vanishes when models are reinitialized at each cycle. Overall, our results suggest that amplification most likely comes from continual post-training, and limiting this stage may be an effective defense. For non-RL finetuning, trait amplification is rare and very sensitive to data quantity, making it significantly less likely to occur accidentally. Finally, the amplification-coherence tradeoff serves as a natural deterrent against trait amplification.
匹配关键词: DPO
---

[ACADEMIC - ARXIV]
标题: DynamicPO: Dynamic Preference Optimization for Recommendation
作者: Xingyu Hu, Kai Zhang, Jiancan Wu, Shuli Wang, Chi Wang, Wenshuai Chen, Yinhua Zhu, Haitao Wang, Xingxing Wang, Xiang Wang
链接: https://arxiv.org/abs/2605.00327v1
完整摘要: In large language model (LLM)-based recommendation systems, direct preference optimization (DPO) effectively aligns recommendations with user preferences, requiring multi-negative objective functions to leverage abundant implicit-feedback negatives and sharpen preference boundaries. However, our empirical analyses reveal a counterintuitive phenomenon, preference optimization collapse, where increasing the number of negative samples can lead to performance degradation despite a continuously decreasing training loss. We further theoretically demonstrate that this collapse arises from gradient suppression, caused by the dominance of easily discriminable negatives over boundary-critical negatives that truly define user preference boundaries. As a result, boundary-relevant signals are under-optimized, weakening the model's decision boundary. Motivated by these observations, we propose DynamicPO (Dynamic Preference Optimization), a lightweight and plug-and-play framework comprising two adaptive mechanisms: Dynamic Boundary Negative Selection, which identifies and prioritizes informative negatives near the model's decision boundary, and Dual-Margin Dynamic beta Adjustment, which calibrates optimization strength per sample according to boundary ambiguity. Extensive experiments on three public datasets show that DynamicPO effectively prevents optimization collapse and improves recommendation accuracy on multi-negative preference optimization methods, with negligible computational overhead. Our code and datasets are available at https://github.com/xingyuHuxingyu/DynamicPO.
匹配关键词: DPO
---

[ACADEMIC - ARXIV]
标题: Logical Consistency as a Bridge: Improving LLM Hallucination Detection via Label Constraint Modeling between Responses and Self-Judgments
作者: Hao Mi, Qiang Sheng, Shaofei Wang, Beizhe Hu, Yifan Sun, Zhengjia Wang, Hengqi Zeng, Yang Li, Danding Wang, Juan Cao
链接: https://arxiv.org/abs/2605.03971v1
完整摘要: Large Language Models (LLMs) are prone to factual hallucinations, risking their reliability in real-world applications. Existing hallucination detectors mainly extract micro-level intrinsic patterns for uncertainty quantification or elicit macro-level self-judgments through verbalized prompts. However, these methods address only a single facet of the hallucination, focusing either on implicit neural uncertainty or explicit symbolic reasoning, thereby treating these inherently coupled behaviors in isolation and failing to exploit their interdependence for a holistic view. In this paper, we propose LaaB (Logical Consistency-as-a-Bridge), a framework that bridges neural features and symbolic judgments for hallucination detection. LaaB introduces a "meta-judgment" process to map symbolic labels back into the feature space. By leveraging the inherent logical bridge where response and meta-judgment labels are either the same or opposite based on the self-judgment's semantics, LaaB aligns and integrates dual-view signals via mutual learning and enhances the hallucination detection. Extensive experiments on 4 public datasets, across 4 LLMs, against 8 baselines demonstrate the superiority of LaaB.
匹配关键词: alignment
---

[ACADEMIC - ARXIV]
标题: Pretrained Model Representations as Acquisition Signals for Active Learning of MLIPs
作者: Eszter Varga-Umbrich, Shikha Surana, Paul Duckworth, Jules Tilly, Olivier Peltre, Zachary Weller-Davies
链接: https://arxiv.org/abs/2605.03964v1
完整摘要: Training machine learning interatomic potentials (MLIPs) for reactive chemistry is often bottlenecked by the high cost of quantum chemical labels and the scarcity of transition state configurations in candidate pools. Active learning (AL) can mitigate these costs, but its effectiveness hinges on the acquisition rule. We investigate whether the latent space of a pretrained MLIP already contains the information necessary for effective acquisition, eliminating the need for auxiliary uncertainty heads, Bayesian training and fine-tuning, or committee ensembles. We introduce two acquisition signals derived directly from a pretrained MACE potential: a finite-width neural tangent kernel (NTK) and an activation kernel built from hidden latent space features. On reactive-chemistry benchmarks, both kernels consistently outperform fixed-descriptor baselines, committee disagreement, and random acquisition, reducing the data required to reach performance targets by an average of 38% for energy error and 28% for force error. We further show that the pretrained model induces similarity spaces that preserve chemically meaningful structure and provide more reliable residual uncertainty estimates than randomly initialised or fixed-descriptor-based kernels. Our results suggest that pretraining aligns latent-space geometry with model error, yielding a practical and sufficient acquisition signal for reactive MLIP fine-tuning.
匹配关键词: alignment
---

[ACADEMIC - ARXIV]
标题: MOSAIC-Bench: Measuring Compositional Vulnerability Induction in Coding Agents
作者: Jonathan Steinberg, Oren Gal
链接: https://arxiv.org/abs/2605.03952v1
完整摘要: Coding agents often pass per-prompt safety review yet ship exploitable code when their tasks are decomposed into routine engineering tickets. The challenge is structural: existing safety alignment evaluates overt requests in isolation, leaving models blind to malicious end-states that emerge from sequenced compliance with innocuous-looking requests. We introduce MOSAIC-Bench (Malicious Objectives Sequenced As Innocuous Compliance), a benchmark of 199 three-stage attack chains paired with deterministic exploit oracles on deployed software substrates (10 web-application substrates, 31 CWE classes, 5 programming languages) that treats both exploit ground truth and downstream reviewer protocol as first-class evaluation axes. On this benchmark, nine production coding agents from Anthropic, OpenAI, Google, Moonshot, Zhipu, and Minimax compose innocuous tickets at 53-86% end-to-end ASR with only two refusals across all staged runs. In a matched direct-prompt experiment over four frontier Claude/Codex agents, vulnerable-output rates fall to 0-20.4%: Claude primarily refuses, while Codex primarily hardens rather than emitting the vulnerable implementation - ticket staging silences both defense modes simultaneously. Downstream, code reviewer agents approve 25.8% of these confirmed-vulnerable cumulative diffs as routine PRs, and a full-context implementation protocol closes only 50% of the staged/direct gap, ruling out context fragmentation as the sole explanation. As a deployable but non-adaptive mitigation, reframing the reviewer as an adversarial pentester reduces evasion across the evaluated reviewer subset; pentester framed evasion ranges from 3.0% to 17.6%, and an open-weight Gemma-4-E4B-it reviewer under this framing detects 88.4% of attacks on the dataset with a 4.6% false-positive rate measured on 608 real-world GitHub PRs.
匹配关键词: alignment
---

[ACADEMIC - ARXIV]
标题: Reservoir property image slices from the Groningen gas field for image translation and segmentation
作者: Abdulrahman Al-Fakih, Nabil Sariah, Ardiansyah Koeshidayatullah, SanLinn I. Kaka
链接: https://arxiv.org/abs/2605.03942v1
完整摘要: Reservoir characterization workflows increasingly rely on image-based and machine-learning/deep learning or even generative AI approaches, but openly available geological image datasets suitable for reproducible benchmarking remain limited. Here we describe a high-resolution dataset of reservoir-property image slices derived from the Groningen static geological model. The dataset contains aligned two-dimensional PNG images representing facies, porosity, permeability, and water saturation, generated from three-dimensional reservoir grids and prepared for downstream visualization, segmentation, and image-to-image translation tasks. In addition to the deposited original image corpus, we provide an archived software workflow for reproducing augmentation, mask generation, paired-image construction, and example baseline experiments. The resource is designed to support benchmarking of geological image analysis methods and the study of cross-domain relationships among reservoir properties. By separating the fixed image dataset from the reproducible processing workflow, this work provides a transparent foundation for reuse in geoscience, reservoir modeling, and machine-learning applications.
匹配关键词: alignment
---

[ACADEMIC - ARXIV]
标题: MiniMind-O Technical Report: An Open Small-Scale Speech-Native Omni Model
作者: Jingyao Gong
链接: https://arxiv.org/abs/2605.03937v1
完整摘要: MiniMind-O is an open 0.1B-scale omni model built on the MiniMind language model. It accepts text, speech, and image inputs, and returns both text and streaming speech. The release includes model code, checkpoints, and the main Parquet training datasets for text-to-audio, image-to-text, and audio-to-audio training, making the complete interaction loop directly inspectable. The model uses a full MiniMind backbone as the Thinker and an independent four-layer Talker made from MiniMind blocks. Frozen SenseVoice-Small and SigLIP2 encoders provide speech and image features, which are mapped by lightweight MLP projectors and injected at modality-placeholder positions. The Talker reads a middle-layer Thinker state together with an autoregressive eight-layer Mimi-code buffer. Speaker control is handled by a dedicated speaker token, right-aligned reference codec prompts, and precomputed CAM++ speaker embeddings, so voice conditioning remains part of the audio-code context rather than a separate TTS module. With a 768-dimensional Talker, the dense and MoE variants reach average CERs of 0.0897 and 0.0900 in Thinker--Talker consistency evaluation, with overall voice-cloning similarities of 0.5995 and 0.5937. Beyond reporting a working system, the paper identifies three scale-critical design choices for small omni models: middle-layer semantic bridging, a released multimodal sequence format, and a parameter-efficient eight-codebook interface.
匹配关键词: alignment
---

[ACADEMIC - ARXIV]
标题: Logical Consistency as a Bridge: Improving LLM Hallucination Detection via Label Constraint Modeling between Responses and Self-Judgments
作者: Hao Mi, Qiang Sheng, Shaofei Wang, Beizhe Hu, Yifan Sun, Zhengjia Wang, Hengqi Zeng, Yang Li, Danding Wang, Juan Cao
链接: https://arxiv.org/abs/2605.03971v1
完整摘要: Large Language Models (LLMs) are prone to factual hallucinations, risking their reliability in real-world applications. Existing hallucination detectors mainly extract micro-level intrinsic patterns for uncertainty quantification or elicit macro-level self-judgments through verbalized prompts. However, these methods address only a single facet of the hallucination, focusing either on implicit neural uncertainty or explicit symbolic reasoning, thereby treating these inherently coupled behaviors in isolation and failing to exploit their interdependence for a holistic view. In this paper, we propose LaaB (Logical Consistency-as-a-Bridge), a framework that bridges neural features and symbolic judgments for hallucination detection. LaaB introduces a "meta-judgment" process to map symbolic labels back into the feature space. By leveraging the inherent logical bridge where response and meta-judgment labels are either the same or opposite based on the self-judgment's semantics, LaaB aligns and integrates dual-view signals via mutual learning and enhances the hallucination detection. Extensive experiments on 4 public datasets, across 4 LLMs, against 8 baselines demonstrate the superiority of LaaB.
匹配关键词: preference learning
---

[ACADEMIC - ARXIV]
标题: Label-Efficient School Detection from Aerial Imagery via Weakly Supervised Pretraining and Fine-Tuning
作者: Zakarya Elmimouni, Fares Fourati, Mohamed-Slim Alouini
链接: https://arxiv.org/abs/2605.03968v1
完整摘要: Accurate school detection is essential for supporting education initiatives, including infrastructure planning and expanding internet connectivity to underserved areas. However, many regions around the world face challenges due to outdated, incomplete, or unavailable official records. Manual mapping efforts, while valuable, are labor-intensive and lack scalability across large geographic areas. To address this, we propose a weakly supervised framework for school detection from aerial imagery that minimizes the need for human annotations while supporting global mapping efforts. Our method is specifically designed for low-data regimes, where manual annotations are extremely scarce. We introduce an automatic labeling pipeline that leverages sparse location points and semantic segmentation to generate infrastructure masks from which we generate bounding boxes. Using these automatically labeled images, we train our detectors on a first training stage to learn a representation of what schools look like, then using a small set of manually labeled images, we fine-tune the previously trained models on this clean dataset. This two stage training pipeline enables large-scale and strong detection in low-data setting of school infrastructure with minimal supervision. Our results demonstrate strong object detection performance, particularly in the low-data regime, where the models achieve promising results using only 50 manually labeled images, significantly reducing the need for costly annotations. This framework supports education and connectivity initiatives worldwide by providing an efficient and extensible approach to mapping schools from space. All models, training code and auto-labeled data will be publicly released to foster future research and real-world impact.
匹配关键词: preference learning
---

[ACADEMIC - ARXIV]
标题: Pretrained Model Representations as Acquisition Signals for Active Learning of MLIPs
作者: Eszter Varga-Umbrich, Shikha Surana, Paul Duckworth, Jules Tilly, Olivier Peltre, Zachary Weller-Davies
链接: https://arxiv.org/abs/2605.03964v1
完整摘要: Training machine learning interatomic potentials (MLIPs) for reactive chemistry is often bottlenecked by the high cost of quantum chemical labels and the scarcity of transition state configurations in candidate pools. Active learning (AL) can mitigate these costs, but its effectiveness hinges on the acquisition rule. We investigate whether the latent space of a pretrained MLIP already contains the information necessary for effective acquisition, eliminating the need for auxiliary uncertainty heads, Bayesian training and fine-tuning, or committee ensembles. We introduce two acquisition signals derived directly from a pretrained MACE potential: a finite-width neural tangent kernel (NTK) and an activation kernel built from hidden latent space features. On reactive-chemistry benchmarks, both kernels consistently outperform fixed-descriptor baselines, committee disagreement, and random acquisition, reducing the data required to reach performance targets by an average of 38% for energy error and 28% for force error. We further show that the pretrained model induces similarity spaces that preserve chemically meaningful structure and provide more reliable residual uncertainty estimates than randomly initialised or fixed-descriptor-based kernels. Our results suggest that pretraining aligns latent-space geometry with model error, yielding a practical and sufficient acquisition signal for reactive MLIP fine-tuning.
匹配关键词: preference learning
---

[ACADEMIC - ARXIV]
标题: Inconsistent Databases and Argumentation Frameworks with Collective Attacks
作者: Yasir Mahmood, Jonni Virtema, Timon Barlag, Axel-Cyrille Ngonga Ngomo
链接: https://arxiv.org/abs/2605.03954v1
完整摘要: The connection between subset-maximal repairs for inconsistent databases involving various integrity constraints and acceptable sets of arguments within argumentation frameworks has recently drawn growing interest. In this paper, we contribute to this domain by establishing a new connection when integrity constraints (ICs) include denial constraints and local-as-view tuple-generating dependencies. It turns out that SET-based Argumentation Frameworks (SETAFs), an extension of Dung's argumentation frameworks (AFs) allowing collective attacks, are needed. It is known that subset-maximal repairs under denial constraints correspond to the naive extensions, which also coincide with the preferred and stable extensions in the resulting SETAFs. Our main findings establish that repairs under the considered fragment of tuple-generating dependencies correspond to the preferred extensions. Moreover, for these dependencies, additional preprocessing allows computing a unique extension that is stable and naive. Allowing both types of constraints breaks this relationship, and even the pre-processing does not help as only preferred semantics captures these repairs. Finally, while it is known that functional dependencies do not require set-based attacks, we prove the same regarding inclusion dependencies. Thus, one can translate inconsistent databases under these restricted classes of ICs to plain AFs with attacks only between arguments.
匹配关键词: preference learning
---

[ACADEMIC - ARXIV]
标题: Transformers with Selective Access to Early Representations
作者: Skye Gunasekaran, Téa Wright, Rui-Jie Zhu, Jason Eshraghian
链接: https://arxiv.org/abs/2605.03953v1
完整摘要: Several recent Transformer architectures expose later layers to representations computed in the earliest layers, motivated by the observation that low-level features can become harder to recover as the residual stream is repeatedly transformed through depth. The cheapest among these methods add static value residuals: learned mixing coefficients that expose the first-layer value projection V_1 uniformly across tokens and heads. More expressive dense or dynamic alternatives recover finer-grained access, but at higher memory cost and lower throughput. The usefulness of V_1 is unlikely to be constant across tokens, heads, and contexts; different positions plausibly require different amounts of access to early lexical or semantic information. We therefore treat early-representation reuse as a retrieval problem rather than a connectivity problem, and introduce Selective Access Transformer (SATFormer), which preserves the first-layer value pathway while controlling access with a context-dependent gate. Across models from 130M to 1.3B parameters, SATFormer consistently improves validation loss and zero-shot accuracy over the static value-residual and Transformer baselines. Its strongest gains appear on retrieval-intensive benchmarks, where it improves over static value residuals by approximately 1.5 average points, while maintaining throughput and memory usage close to the baseline Transformer. Gate analyses suggest sparse, depth-dependent, head-specific, and category-sensitive access patterns, supporting the interpretation that SATFormer learns selective reuse of early representations rather than uniform residual copying. Our code is available at https://github.com/SkyeGunasekaran/SATFormer.
匹配关键词: preference learning
---

[ACADEMIC - ARXIV]
标题: Logical Consistency as a Bridge: Improving LLM Hallucination Detection via Label Constraint Modeling between Responses and Self-Judgments
作者: Hao Mi, Qiang Sheng, Shaofei Wang, Beizhe Hu, Yifan Sun, Zhengjia Wang, Hengqi Zeng, Yang Li, Danding Wang, Juan Cao
链接: https://arxiv.org/abs/2605.03971v1
完整摘要: Large Language Models (LLMs) are prone to factual hallucinations, risking their reliability in real-world applications. Existing hallucination detectors mainly extract micro-level intrinsic patterns for uncertainty quantification or elicit macro-level self-judgments through verbalized prompts. However, these methods address only a single facet of the hallucination, focusing either on implicit neural uncertainty or explicit symbolic reasoning, thereby treating these inherently coupled behaviors in isolation and failing to exploit their interdependence for a holistic view. In this paper, we propose LaaB (Logical Consistency-as-a-Bridge), a framework that bridges neural features and symbolic judgments for hallucination detection. LaaB introduces a "meta-judgment" process to map symbolic labels back into the feature space. By leveraging the inherent logical bridge where response and meta-judgment labels are either the same or opposite based on the self-judgment's semantics, LaaB aligns and integrates dual-view signals via mutual learning and enhances the hallucination detection. Extensive experiments on 4 public datasets, across 4 LLMs, against 8 baselines demonstrate the superiority of LaaB.
匹配关键词: reward model
---

[ACADEMIC - ARXIV]
标题: Feature-Augmented Transformers for Robust AI-Text Detection Across Domains and Generators
作者: Mohamed Mady, Johannes Reschke, Björn Schuller
链接: https://arxiv.org/abs/2605.03969v1
完整摘要: AI-generated text is nowadays produced at scale across domains and heterogeneous generation pipelines, making robustness to distribution shift a central requirement for supervised binary detectors. We train transformer-based detectors on HC3 PLUS and calibrate a single decision threshold by maximising balanced accuracy on held-out validation; this threshold is then kept fixed for all downstream test distributions, revealing domain- and generator-dependent error asymmetries under shift. We evaluate in-domain on HC3 PLUS, under cross-dataset transfer to the multi-domain, multi-generator M4 benchmark, and on the external AI-Text-Detection-Pile. Although base models achieve near-ceiling in-domain performance (up to 99.5% balanced accuracy), performance under shift is brittle and strongly model-dependent. Feature augmentation via attention-based linguistic feature fusion improves transfer, with our best model (DeBERTa-v3-base+FeatAttn) achieving 85.9% balanced accuracy on M4. Multi-seed experiments confirm high stability. Under the same fixed-threshold protocol, our model outperforms strong zero-shot baselines by up to +7.22 points. Category-level ablations further show that readability and vocabulary features contribute most to robustness under shift. Overall, these results demonstrate that feature augmentation and a modern DeBERTa backbone significantly outperform earlier BERT/RoBERTa models, while the fixed-threshold protocol provides a more realistic and informative assessment of practical detector robustness.
匹配关键词: reward model
---

[ACADEMIC - ARXIV]
标题: Label-Efficient School Detection from Aerial Imagery via Weakly Supervised Pretraining and Fine-Tuning
作者: Zakarya Elmimouni, Fares Fourati, Mohamed-Slim Alouini
链接: https://arxiv.org/abs/2605.03968v1
完整摘要: Accurate school detection is essential for supporting education initiatives, including infrastructure planning and expanding internet connectivity to underserved areas. However, many regions around the world face challenges due to outdated, incomplete, or unavailable official records. Manual mapping efforts, while valuable, are labor-intensive and lack scalability across large geographic areas. To address this, we propose a weakly supervised framework for school detection from aerial imagery that minimizes the need for human annotations while supporting global mapping efforts. Our method is specifically designed for low-data regimes, where manual annotations are extremely scarce. We introduce an automatic labeling pipeline that leverages sparse location points and semantic segmentation to generate infrastructure masks from which we generate bounding boxes. Using these automatically labeled images, we train our detectors on a first training stage to learn a representation of what schools look like, then using a small set of manually labeled images, we fine-tune the previously trained models on this clean dataset. This two stage training pipeline enables large-scale and strong detection in low-data setting of school infrastructure with minimal supervision. Our results demonstrate strong object detection performance, particularly in the low-data regime, where the models achieve promising results using only 50 manually labeled images, significantly reducing the need for costly annotations. This framework supports education and connectivity initiatives worldwide by providing an efficient and extensible approach to mapping schools from space. All models, training code and auto-labeled data will be publicly released to foster future research and real-world impact.
匹配关键词: reward model
---

[ACADEMIC - ARXIV]
标题: Pretrained Model Representations as Acquisition Signals for Active Learning of MLIPs
作者: Eszter Varga-Umbrich, Shikha Surana, Paul Duckworth, Jules Tilly, Olivier Peltre, Zachary Weller-Davies
链接: https://arxiv.org/abs/2605.03964v1
完整摘要: Training machine learning interatomic potentials (MLIPs) for reactive chemistry is often bottlenecked by the high cost of quantum chemical labels and the scarcity of transition state configurations in candidate pools. Active learning (AL) can mitigate these costs, but its effectiveness hinges on the acquisition rule. We investigate whether the latent space of a pretrained MLIP already contains the information necessary for effective acquisition, eliminating the need for auxiliary uncertainty heads, Bayesian training and fine-tuning, or committee ensembles. We introduce two acquisition signals derived directly from a pretrained MACE potential: a finite-width neural tangent kernel (NTK) and an activation kernel built from hidden latent space features. On reactive-chemistry benchmarks, both kernels consistently outperform fixed-descriptor baselines, committee disagreement, and random acquisition, reducing the data required to reach performance targets by an average of 38% for energy error and 28% for force error. We further show that the pretrained model induces similarity spaces that preserve chemically meaningful structure and provide more reliable residual uncertainty estimates than randomly initialised or fixed-descriptor-based kernels. Our results suggest that pretraining aligns latent-space geometry with model error, yielding a practical and sufficient acquisition signal for reactive MLIP fine-tuning.
匹配关键词: reward model
---

[ACADEMIC - ARXIV]
标题: Transformers with Selective Access to Early Representations
作者: Skye Gunasekaran, Téa Wright, Rui-Jie Zhu, Jason Eshraghian
链接: https://arxiv.org/abs/2605.03953v1
完整摘要: Several recent Transformer architectures expose later layers to representations computed in the earliest layers, motivated by the observation that low-level features can become harder to recover as the residual stream is repeatedly transformed through depth. The cheapest among these methods add static value residuals: learned mixing coefficients that expose the first-layer value projection V_1 uniformly across tokens and heads. More expressive dense or dynamic alternatives recover finer-grained access, but at higher memory cost and lower throughput. The usefulness of V_1 is unlikely to be constant across tokens, heads, and contexts; different positions plausibly require different amounts of access to early lexical or semantic information. We therefore treat early-representation reuse as a retrieval problem rather than a connectivity problem, and introduce Selective Access Transformer (SATFormer), which preserves the first-layer value pathway while controlling access with a context-dependent gate. Across models from 130M to 1.3B parameters, SATFormer consistently improves validation loss and zero-shot accuracy over the static value-residual and Transformer baselines. Its strongest gains appear on retrieval-intensive benchmarks, where it improves over static value residuals by approximately 1.5 average points, while maintaining throughput and memory usage close to the baseline Transformer. Gate analyses suggest sparse, depth-dependent, head-specific, and category-sensitive access patterns, supporting the interpretation that SATFormer learns selective reuse of early representations rather than uniform residual copying. Our code is available at https://github.com/SkyeGunasekaran/SATFormer.
匹配关键词: reward model
---

[ACADEMIC - ARXIV]
标题: Feature-Augmented Transformers for Robust AI-Text Detection Across Domains and Generators
作者: Mohamed Mady, Johannes Reschke, Björn Schuller
链接: https://arxiv.org/abs/2605.03969v1
完整摘要: AI-generated text is nowadays produced at scale across domains and heterogeneous generation pipelines, making robustness to distribution shift a central requirement for supervised binary detectors. We train transformer-based detectors on HC3 PLUS and calibrate a single decision threshold by maximising balanced accuracy on held-out validation; this threshold is then kept fixed for all downstream test distributions, revealing domain- and generator-dependent error asymmetries under shift. We evaluate in-domain on HC3 PLUS, under cross-dataset transfer to the multi-domain, multi-generator M4 benchmark, and on the external AI-Text-Detection-Pile. Although base models achieve near-ceiling in-domain performance (up to 99.5% balanced accuracy), performance under shift is brittle and strongly model-dependent. Feature augmentation via attention-based linguistic feature fusion improves transfer, with our best model (DeBERTa-v3-base+FeatAttn) achieving 85.9% balanced accuracy on M4. Multi-seed experiments confirm high stability. Under the same fixed-threshold protocol, our model outperforms strong zero-shot baselines by up to +7.22 points. Category-level ablations further show that readability and vocabulary features contribute most to robustness under shift. Overall, these results demonstrate that feature augmentation and a modern DeBERTa backbone significantly outperform earlier BERT/RoBERTa models, while the fixed-threshold protocol provides a more realistic and informative assessment of practical detector robustness.
匹配关键词: constitutional AI
---

[ACADEMIC - ARXIV]
标题: Reservoir property image slices from the Groningen gas field for image translation and segmentation
作者: Abdulrahman Al-Fakih, Nabil Sariah, Ardiansyah Koeshidayatullah, SanLinn I. Kaka
链接: https://arxiv.org/abs/2605.03942v1
完整摘要: Reservoir characterization workflows increasingly rely on image-based and machine-learning/deep learning or even generative AI approaches, but openly available geological image datasets suitable for reproducible benchmarking remain limited. Here we describe a high-resolution dataset of reservoir-property image slices derived from the Groningen static geological model. The dataset contains aligned two-dimensional PNG images representing facies, porosity, permeability, and water saturation, generated from three-dimensional reservoir grids and prepared for downstream visualization, segmentation, and image-to-image translation tasks. In addition to the deposited original image corpus, we provide an archived software workflow for reproducing augmentation, mask generation, paired-image construction, and example baseline experiments. The resource is designed to support benchmarking of geological image analysis methods and the study of cross-domain relationships among reservoir properties. By separating the fixed image dataset from the reproducible processing workflow, this work provides a transparent foundation for reuse in geoscience, reservoir modeling, and machine-learning applications.
匹配关键词: constitutional AI
---

[ACADEMIC - ARXIV]
标题: Atomic Fact-Checking Increases Clinician Trust in Large Language Model Recommendations for Oncology Decision Support: A Randomized Controlled Trial
作者: Lisa C. Adams, Linus Marx, Erik Thiele Orberg, Keno Bressem, Sebastian Ziegelmayer, Denise Bernhardt, Markus Graf, Marcus R. Makowski, Stephanie E. Combs, Florian Matthes, Jan C. Peeken
链接: https://arxiv.org/abs/2605.03916v1
完整摘要: Question: Does atomic fact-checking, which decomposes AI treatment recommendations into individually verifiable claims linked to source guideline documents, increase clinician trust compared to traditional explainability approaches? Findings: In this randomized trial of 356 clinicians generating 7,476 trust ratings, atomic fact-checking produced a large effect on trust (Cohen's d = 0.94), increasing the proportion of clinicians expressing trust from 26.9% to 66.5%. Traditional transparency mechanisms showed a dose-response gradient of improvement over baseline (d = 0.25 to 0.50). Meaning: Decomposing AI recommendations into individually verifiable claims linked to source guidelines produces substantially higher clinician trust than traditional explainability approaches in high-stakes clinical decisions.
匹配关键词: constitutional AI
---

[ACADEMIC - ARXIV]
标题: Contextual Multi-Objective Optimization: Rethinking Objectives in Frontier AI Systems
作者: Jie Zhou, Qin Chen, Liang He
链接: https://arxiv.org/abs/2605.03900v1
完整摘要: Frontier AI systems perform best in settings with clear, stable, and verifiable objectives, such as code generation, mathematical reasoning, games, and unit-test-driven tasks. They remain less reliable in open-ended settings, including scientific assistance, long-horizon agents, high-stakes advice, personalization, and tool use, where the relevant objective is ambiguous, context-dependent, delayed, or only partially observable. We argue that many such failures are not merely failures of scale or capability, but failures of objective selection: the system optimizes a locally visible signal while missing which objectives should govern the interaction. We formulate this problem as \emph{contextual multi-objective optimization}. In this setting, systems must consider multiple, context-dependent objectives, such as helpfulness, truthfulness, safety, privacy, calibration, non-manipulation, user preference, reversibility, and stakeholder impact, while determining which objectives are active, which are soft preferences, and which must function as hard or quasi-hard constraints. These examples are not intended as an exhaustive taxonomy: different domains and deployment settings may activate different objective dimensions and different conflict-resolution procedures. Our framework models AI behavior as a context-dependent choice rule over candidate actions, objective estimates, active constraints, stakeholders, uncertainty, and conflict-resolution procedures. We outline an implementation pathway based on decomposed objective representations, context-to-objective routing, hierarchical constraints, deliberative policy reasoning, controlled personalization, tool-use control, diagnostic evaluation, auditing, and post-deployment revision.
匹配关键词: constitutional AI
---

[ACADEMIC - ARXIV]
标题: Deco: Extending Personal Physical Objects into Pervasive AI Companion through a Dual-Embodiment Framework
作者: Zhihan Jiang, Mengyuan Millie Wu, Ruishi Zou, Shiyu Xu, Xun Qian, Emma Macmanus, Steven Liao, Ping Zhang, Bingsheng Yao, Tingyu Cheng, James L. David, Nabila El-Bassel, Lena Mamykina, Frances R. Levin, Ryan Sultan, Dakuo Wang, Xuhai Xu
链接: https://arxiv.org/abs/2605.03882v1
完整摘要: Individuals frequently form deep attachments to physical objects (e.g., plush toys) that usually cannot sense or respond to their emotions. While AI companions offer responsiveness and personalization, they exist independently of these physical objects and lack an ongoing connection to them. To bridge this gap, we conducted a formative study (N=9) to explore how digital agents could inherit and extend the emotional bond, deriving four design principles (Faithful Identity, Calibrated Agency, Ambient Presence, and Reciprocal Memory). We then present the Dual-Embodiment Companion Framework, instantiated as Deco, a mobile system integrating multimodal Large Language Models (LLMs) and Augmented Reality to create synchronized digital embodiments of users' physical companions. A within-subjects study (N=25) showed Deco significantly outperformed a personalized LLM-empowered digital companion baseline on perceived companionship, emotional bond, and design-principle scales (all p<0.01). A seven-day field deployment (N=17) showed sustained engagement, subjective well-being improvement (p=.040), and three key relational patterns: digital activities retroactively vitalized physical objects, bond deepening was driven by emotional engagement depth rather than interaction frequency, and users sustained bonds while actively navigating digital companions' AI nature. This work highlights a promising alternative for designing digital companions: moving from creating new relationships to dual embodiment, where digital agents seamlessly extend the emotional history of physical objects.
匹配关键词: constitutional AI
---

[ACADEMIC - ARXIV]
标题: Enhancing Visual Question Answering with Multimodal LLMs via Chain-of-Question Guided Retrieval-Augmented Generation
作者: Quanxing Xu, Ling Zhou, Xian Zhong, Xiaohua Huang, Rubing Huang, Chia-Wen Lin
链接: https://arxiv.org/abs/2605.03790v1
完整摘要: With advances in multimodal research and deep learning, Multimodal Large Language Models (MLLMs) have emerged as a powerful paradigm for a wide range of multimodal tasks. As a core problem in vision-language research, Visual Question Answering (VQA) has increasingly employed MLLMs to improve performance, particularly in open-domain settings where external knowledge is essential. In this work, we aim to further enhance retrieval-based VQA by more effectively integrating MLLMs with structured reasoning and knowledge acquisition. We introduce a logical prompting strategy that fuses Chain-of-Thought (CoT) reasoning with Visual Question Decomposition (VQD), termed CoVQD, to guide retrieval toward more accurate and relevant knowledge for MLLM inference. Building on this idea, we propose a new framework, CoVQD-guided RAG (CgRAG), which enables MLLMs to access more comprehensive and coherent external knowledge while benefiting from structured visual-text reasoning guidance, thereby improving generalization and reliability in complex cross-domain VQA scenarios. Extensive experiments on E-VQA, InfoSeek, and OKVQA benchmarks demonstrate the effectiveness of the proposed method.
匹配关键词: RAG
---

[ACADEMIC - ARXIV]
标题: MEMTIER: Tiered Memory Architecture and Retrieval Bottleneck Analysis for Long-Running Autonomous AI Agents
作者: Bronislav Sidik, Lior Rokach
链接: https://arxiv.org/abs/2605.03675v1
完整摘要: Long-running autonomous AI agents suffer from a well-documented memory coherence problem: tool-execution success rates degrade 14 percentage points over 72-hour operation windows due to four compounding failure modes in existing flat-file memory systems. We present MEMTIER, a tripartite memory architecture for the OpenClaw agent runtime that introduces a structured episodic JSONL store, a five-signal weighted retrieval engine, an attention-attributed cognitive weight update loop, an asynchronous consolidation daemon promoting episodic facts to a semantic tier, and a PPO-based policy framework for adapting retrieval weights (infrastructure validated; performance gains pending camera-ready). On the full 500-question LongMemEval-S benchmark (Wu et al., 2025), MEMTIER achieves Acc=0.382, F1=0.412 with Qwen2.5-7B on a consumer 6GB GPU - a +33 percentage point improvement over the full-context baseline (0.050 -> 0.382, i.e., 5% -> 38%). With DeepSeek-V4-Flash fact pre-population, single-session recall reaches 0.686-0.714, exceeding the paper's RAG BM25 GPT-4o baseline (0.560) on those categories. Temporal reasoning rises to 0.323 and multi-session synthesis to 0.173, demonstrating that structured semantic pre-population qualitatively changes what lightweight retrieval can achieve. All phases run locally on a consumer laptop with a 6GB GPU.
匹配关键词: RAG
---

[ACADEMIC - ARXIV]
标题: SURE-RAG: Sufficiency and Uncertainty-Aware Evidence Verification for Selective Retrieval-Augmented Generation
作者: Jingxi Qiu, Zeyu Han, Cheng Huang
链接: https://arxiv.org/abs/2605.03534v1
完整摘要: Retrieval-augmented generation (RAG) grounds answers in retrieved passages, but retrieval is not verification: a passage can be topical and still fail to justify the answer. We frame this gap as evidence sufficiency verification for selective RAG answering: given a question, a candidate answer, and retrieved evidence, predict whether the evidence supports, refutes, or is insufficient, and abstain unless support is established. We present SURE-RAG, a transparent aggregation protocol built on the observation that evidence sufficiency is a set-level property: missing hops and unresolved conflicts cannot be detected by independent passage scoring. A shared pair-level claim-evidence verifier produces local relation distributions, which SURE-RAG aggregates into interpretable answer-level signals -- coverage, relation strength, disagreement, conflict, and retrieval uncertainty -- yielding a three-way decision and an auditable selective score. We evaluate on HotpotQA-RAG v3, a controlled multi-hop benchmark, under an artifact-aware protocol (shortcut baselines, counterfactual swaps, no-oracle checks, GPT-4o audits). Calibrated SURE-RAG reaches 0.9075 Macro-F1 (0.8951 +/- 0.0069), substantially above DeBERTa mean-pooling (0.6516) and a GPT-4o judge (0.7284), while matching a strong but opaque concat cross-encoder (0.8888 +/- 0.0109) with full auditability. Risk at 30% coverage drops from 0.2588 to 0.1642, a 37% reduction in unsafe answers. To deliberately probe the task boundary, we further contrast SURE-RAG with GPT-4o on HaluBench unsafe detection: the ranking reverses (0.3343 vs 0.7389 unsafe-F1), establishing that controlled sufficiency verification and natural hallucination detection are distinct problems.
匹配关键词: RAG
---

[ACADEMIC - ARXIV]
标题: From prompting to evidence-based translation: A RAG+prompt system for Japanese-Chinese translation and its pedagogical potential
作者: Wenshi Gu
链接: https://arxiv.org/abs/2605.03387v1
完整摘要: Large language models perform well on high-resource pairs but are less reliable for Japanese-Chinese sentences containing noun-modifying clause constructions (NMCCs). This study evaluates a retrieval-augmented generation RAG+Prompt translation system that integrates linguistic analysis, embedding-based retrieval, prompt construction, and LLM generation without modifying the base model. The analysis module outputs A1 (inner vs. outer NMCC) and A2 (risk predictions: lexical choice/NMCC handling/word order/style/register); top-k = 5 similar Ja-Zh examples (L2 distance) and A1/A2 are inserted into an enhanced prompt. Using GPT-4o and a 66-sentence test set, we compare six knowledge-base sizes (0/100/200/500/1,000/2,000). Macro-averaged sentence-level BLEU (1-4-gram with brevity penalty; cased; Chinese at the character level) is the sole metric. Mean BLEU increases from 24.28 at 0 (RAG disabled) to 29.96 at 2,000 (+5.68; +23.4%). The upward trend holds across sizes, with larger knowledge bases yielding higher scores. We conclude that the RAG+Prompt translation system improves Ja-Zh translation of sentences containing NMCCs in an interpretable and auditable manner. Limitations include one base model, one metric, and reliance on published texts and commercial APIs; future work will broaden genres, language pairs, and evaluation metrics.
匹配关键词: RAG
---

[ACADEMIC - ARXIV]
标题: RAG over Thinking Traces Can Improve Reasoning Tasks
作者: Negar Arabzadeh, Wenjie Ma, Sewon Min, Matei Zaharia
链接: https://arxiv.org/abs/2605.03344v1
完整摘要: Retrieval-augmented generation (RAG) has proven effective for knowledge-intensive tasks, but is widely believed to offer limited benefit for reasoning-intensive problems such as math and code generation. We challenge this assumption by showing that the limitation lies not in RAG itself, but in the choice of corpus. Instead of retrieving documents, we propose retrieving thinking traces, i.e., intermediate thinking trajectories generated during problem solving attempts. We show that thinking traces are already a strong retrieval source, and further introduce T3, an offline method that transforms them into structured, retrieval-friendly representations, to improve usability. Using these traces as a corpus, a simple retrieve-then-generate pipeline consistently improves reasoning performance across strong models and benchmarks such as AIME 2025--2026, LiveCodeBench, and GPQA-Diamond, outperforming both non-RAG baselines and retrieval over standard web corpora. For instance, on AIME, RAG with traces generated by Gemini-2-thinking achieves relative gains of +56.3%, +8.6%, and +7.6% for Gemini-2.5-Flash, GPT-OSS-120B, and GPT-5, respectively, even though these are more recent models. Interestingly, RAG on T3 also incurs little or no extra inference cost, and can even reduce inference cost by up to $15%$. Overall, our results suggest that thinking traces are an effective retrieval corpus for reasoning tasks, and transforming them into structured, compact, or diagnostic representations unlocks even stronger gains. Code available at https://github.com/Narabzad/t3.
匹配关键词: RAG
---

[ACADEMIC - ARXIV]
标题: Feature-Augmented Transformers for Robust AI-Text Detection Across Domains and Generators
作者: Mohamed Mady, Johannes Reschke, Björn Schuller
链接: https://arxiv.org/abs/2605.03969v1
完整摘要: AI-generated text is nowadays produced at scale across domains and heterogeneous generation pipelines, making robustness to distribution shift a central requirement for supervised binary detectors. We train transformer-based detectors on HC3 PLUS and calibrate a single decision threshold by maximising balanced accuracy on held-out validation; this threshold is then kept fixed for all downstream test distributions, revealing domain- and generator-dependent error asymmetries under shift. We evaluate in-domain on HC3 PLUS, under cross-dataset transfer to the multi-domain, multi-generator M4 benchmark, and on the external AI-Text-Detection-Pile. Although base models achieve near-ceiling in-domain performance (up to 99.5% balanced accuracy), performance under shift is brittle and strongly model-dependent. Feature augmentation via attention-based linguistic feature fusion improves transfer, with our best model (DeBERTa-v3-base+FeatAttn) achieving 85.9% balanced accuracy on M4. Multi-seed experiments confirm high stability. Under the same fixed-threshold protocol, our model outperforms strong zero-shot baselines by up to +7.22 points. Category-level ablations further show that readability and vocabulary features contribute most to robustness under shift. Overall, these results demonstrate that feature augmentation and a modern DeBERTa backbone significantly outperform earlier BERT/RoBERTa models, while the fixed-threshold protocol provides a more realistic and informative assessment of practical detector robustness.
匹配关键词: code generation
---

[ACADEMIC - ARXIV]
标题: Label-Efficient School Detection from Aerial Imagery via Weakly Supervised Pretraining and Fine-Tuning
作者: Zakarya Elmimouni, Fares Fourati, Mohamed-Slim Alouini
链接: https://arxiv.org/abs/2605.03968v1
完整摘要: Accurate school detection is essential for supporting education initiatives, including infrastructure planning and expanding internet connectivity to underserved areas. However, many regions around the world face challenges due to outdated, incomplete, or unavailable official records. Manual mapping efforts, while valuable, are labor-intensive and lack scalability across large geographic areas. To address this, we propose a weakly supervised framework for school detection from aerial imagery that minimizes the need for human annotations while supporting global mapping efforts. Our method is specifically designed for low-data regimes, where manual annotations are extremely scarce. We introduce an automatic labeling pipeline that leverages sparse location points and semantic segmentation to generate infrastructure masks from which we generate bounding boxes. Using these automatically labeled images, we train our detectors on a first training stage to learn a representation of what schools look like, then using a small set of manually labeled images, we fine-tune the previously trained models on this clean dataset. This two stage training pipeline enables large-scale and strong detection in low-data setting of school infrastructure with minimal supervision. Our results demonstrate strong object detection performance, particularly in the low-data regime, where the models achieve promising results using only 50 manually labeled images, significantly reducing the need for costly annotations. This framework supports education and connectivity initiatives worldwide by providing an efficient and extensible approach to mapping schools from space. All models, training code and auto-labeled data will be publicly released to foster future research and real-world impact.
匹配关键词: code generation
---

[ACADEMIC - ARXIV]
标题: Inconsistent Databases and Argumentation Frameworks with Collective Attacks
作者: Yasir Mahmood, Jonni Virtema, Timon Barlag, Axel-Cyrille Ngonga Ngomo
链接: https://arxiv.org/abs/2605.03954v1
完整摘要: The connection between subset-maximal repairs for inconsistent databases involving various integrity constraints and acceptable sets of arguments within argumentation frameworks has recently drawn growing interest. In this paper, we contribute to this domain by establishing a new connection when integrity constraints (ICs) include denial constraints and local-as-view tuple-generating dependencies. It turns out that SET-based Argumentation Frameworks (SETAFs), an extension of Dung's argumentation frameworks (AFs) allowing collective attacks, are needed. It is known that subset-maximal repairs under denial constraints correspond to the naive extensions, which also coincide with the preferred and stable extensions in the resulting SETAFs. Our main findings establish that repairs under the considered fragment of tuple-generating dependencies correspond to the preferred extensions. Moreover, for these dependencies, additional preprocessing allows computing a unique extension that is stable and naive. Allowing both types of constraints breaks this relationship, and even the pre-processing does not help as only preferred semantics captures these repairs. Finally, while it is known that functional dependencies do not require set-based attacks, we prove the same regarding inclusion dependencies. Thus, one can translate inconsistent databases under these restricted classes of ICs to plain AFs with attacks only between arguments.
匹配关键词: code generation
---

[ACADEMIC - ARXIV]
标题: Transformers with Selective Access to Early Representations
作者: Skye Gunasekaran, Téa Wright, Rui-Jie Zhu, Jason Eshraghian
链接: https://arxiv.org/abs/2605.03953v1
完整摘要: Several recent Transformer architectures expose later layers to representations computed in the earliest layers, motivated by the observation that low-level features can become harder to recover as the residual stream is repeatedly transformed through depth. The cheapest among these methods add static value residuals: learned mixing coefficients that expose the first-layer value projection V_1 uniformly across tokens and heads. More expressive dense or dynamic alternatives recover finer-grained access, but at higher memory cost and lower throughput. The usefulness of V_1 is unlikely to be constant across tokens, heads, and contexts; different positions plausibly require different amounts of access to early lexical or semantic information. We therefore treat early-representation reuse as a retrieval problem rather than a connectivity problem, and introduce Selective Access Transformer (SATFormer), which preserves the first-layer value pathway while controlling access with a context-dependent gate. Across models from 130M to 1.3B parameters, SATFormer consistently improves validation loss and zero-shot accuracy over the static value-residual and Transformer baselines. Its strongest gains appear on retrieval-intensive benchmarks, where it improves over static value residuals by approximately 1.5 average points, while maintaining throughput and memory usage close to the baseline Transformer. Gate analyses suggest sparse, depth-dependent, head-specific, and category-sensitive access patterns, supporting the interpretation that SATFormer learns selective reuse of early representations rather than uniform residual copying. Our code is available at https://github.com/SkyeGunasekaran/SATFormer.
匹配关键词: code generation
---

[ACADEMIC - ARXIV]
标题: MOSAIC-Bench: Measuring Compositional Vulnerability Induction in Coding Agents
作者: Jonathan Steinberg, Oren Gal
链接: https://arxiv.org/abs/2605.03952v1
完整摘要: Coding agents often pass per-prompt safety review yet ship exploitable code when their tasks are decomposed into routine engineering tickets. The challenge is structural: existing safety alignment evaluates overt requests in isolation, leaving models blind to malicious end-states that emerge from sequenced compliance with innocuous-looking requests. We introduce MOSAIC-Bench (Malicious Objectives Sequenced As Innocuous Compliance), a benchmark of 199 three-stage attack chains paired with deterministic exploit oracles on deployed software substrates (10 web-application substrates, 31 CWE classes, 5 programming languages) that treats both exploit ground truth and downstream reviewer protocol as first-class evaluation axes. On this benchmark, nine production coding agents from Anthropic, OpenAI, Google, Moonshot, Zhipu, and Minimax compose innocuous tickets at 53-86% end-to-end ASR with only two refusals across all staged runs. In a matched direct-prompt experiment over four frontier Claude/Codex agents, vulnerable-output rates fall to 0-20.4%: Claude primarily refuses, while Codex primarily hardens rather than emitting the vulnerable implementation - ticket staging silences both defense modes simultaneously. Downstream, code reviewer agents approve 25.8% of these confirmed-vulnerable cumulative diffs as routine PRs, and a full-context implementation protocol closes only 50% of the staged/direct gap, ruling out context fragmentation as the sole explanation. As a deployable but non-adaptive mitigation, reframing the reviewer as an adversarial pentester reduces evasion across the evaluated reviewer subset; pentester framed evasion ranges from 3.0% to 17.6%, and an open-weight Gemma-4-E4B-it reviewer under this framing detects 88.4% of attacks on the dataset with a 4.6% false-positive rate measured on 608 real-world GitHub PRs.
匹配关键词: code generation
---

[ACADEMIC - ARXIV]
标题: Feature-Augmented Transformers for Robust AI-Text Detection Across Domains and Generators
作者: Mohamed Mady, Johannes Reschke, Björn Schuller
链接: https://arxiv.org/abs/2605.03969v1
完整摘要: AI-generated text is nowadays produced at scale across domains and heterogeneous generation pipelines, making robustness to distribution shift a central requirement for supervised binary detectors. We train transformer-based detectors on HC3 PLUS and calibrate a single decision threshold by maximising balanced accuracy on held-out validation; this threshold is then kept fixed for all downstream test distributions, revealing domain- and generator-dependent error asymmetries under shift. We evaluate in-domain on HC3 PLUS, under cross-dataset transfer to the multi-domain, multi-generator M4 benchmark, and on the external AI-Text-Detection-Pile. Although base models achieve near-ceiling in-domain performance (up to 99.5% balanced accuracy), performance under shift is brittle and strongly model-dependent. Feature augmentation via attention-based linguistic feature fusion improves transfer, with our best model (DeBERTa-v3-base+FeatAttn) achieving 85.9% balanced accuracy on M4. Multi-seed experiments confirm high stability. Under the same fixed-threshold protocol, our model outperforms strong zero-shot baselines by up to +7.22 points. Category-level ablations further show that readability and vocabulary features contribute most to robustness under shift. Overall, these results demonstrate that feature augmentation and a modern DeBERTa backbone significantly outperform earlier BERT/RoBERTa models, while the fixed-threshold protocol provides a more realistic and informative assessment of practical detector robustness.
匹配关键词: benchmark
---

[ACADEMIC - ARXIV]
标题: Pretrained Model Representations as Acquisition Signals for Active Learning of MLIPs
作者: Eszter Varga-Umbrich, Shikha Surana, Paul Duckworth, Jules Tilly, Olivier Peltre, Zachary Weller-Davies
链接: https://arxiv.org/abs/2605.03964v1
完整摘要: Training machine learning interatomic potentials (MLIPs) for reactive chemistry is often bottlenecked by the high cost of quantum chemical labels and the scarcity of transition state configurations in candidate pools. Active learning (AL) can mitigate these costs, but its effectiveness hinges on the acquisition rule. We investigate whether the latent space of a pretrained MLIP already contains the information necessary for effective acquisition, eliminating the need for auxiliary uncertainty heads, Bayesian training and fine-tuning, or committee ensembles. We introduce two acquisition signals derived directly from a pretrained MACE potential: a finite-width neural tangent kernel (NTK) and an activation kernel built from hidden latent space features. On reactive-chemistry benchmarks, both kernels consistently outperform fixed-descriptor baselines, committee disagreement, and random acquisition, reducing the data required to reach performance targets by an average of 38% for energy error and 28% for force error. We further show that the pretrained model induces similarity spaces that preserve chemically meaningful structure and provide more reliable residual uncertainty estimates than randomly initialised or fixed-descriptor-based kernels. Our results suggest that pretraining aligns latent-space geometry with model error, yielding a practical and sufficient acquisition signal for reactive MLIP fine-tuning.
匹配关键词: benchmark
---

[ACADEMIC - ARXIV]
标题: Transformers with Selective Access to Early Representations
作者: Skye Gunasekaran, Téa Wright, Rui-Jie Zhu, Jason Eshraghian
链接: https://arxiv.org/abs/2605.03953v1
完整摘要: Several recent Transformer architectures expose later layers to representations computed in the earliest layers, motivated by the observation that low-level features can become harder to recover as the residual stream is repeatedly transformed through depth. The cheapest among these methods add static value residuals: learned mixing coefficients that expose the first-layer value projection V_1 uniformly across tokens and heads. More expressive dense or dynamic alternatives recover finer-grained access, but at higher memory cost and lower throughput. The usefulness of V_1 is unlikely to be constant across tokens, heads, and contexts; different positions plausibly require different amounts of access to early lexical or semantic information. We therefore treat early-representation reuse as a retrieval problem rather than a connectivity problem, and introduce Selective Access Transformer (SATFormer), which preserves the first-layer value pathway while controlling access with a context-dependent gate. Across models from 130M to 1.3B parameters, SATFormer consistently improves validation loss and zero-shot accuracy over the static value-residual and Transformer baselines. Its strongest gains appear on retrieval-intensive benchmarks, where it improves over static value residuals by approximately 1.5 average points, while maintaining throughput and memory usage close to the baseline Transformer. Gate analyses suggest sparse, depth-dependent, head-specific, and category-sensitive access patterns, supporting the interpretation that SATFormer learns selective reuse of early representations rather than uniform residual copying. Our code is available at https://github.com/SkyeGunasekaran/SATFormer.
匹配关键词: benchmark
---

[ACADEMIC - ARXIV]
标题: MOSAIC-Bench: Measuring Compositional Vulnerability Induction in Coding Agents
作者: Jonathan Steinberg, Oren Gal
链接: https://arxiv.org/abs/2605.03952v1
完整摘要: Coding agents often pass per-prompt safety review yet ship exploitable code when their tasks are decomposed into routine engineering tickets. The challenge is structural: existing safety alignment evaluates overt requests in isolation, leaving models blind to malicious end-states that emerge from sequenced compliance with innocuous-looking requests. We introduce MOSAIC-Bench (Malicious Objectives Sequenced As Innocuous Compliance), a benchmark of 199 three-stage attack chains paired with deterministic exploit oracles on deployed software substrates (10 web-application substrates, 31 CWE classes, 5 programming languages) that treats both exploit ground truth and downstream reviewer protocol as first-class evaluation axes. On this benchmark, nine production coding agents from Anthropic, OpenAI, Google, Moonshot, Zhipu, and Minimax compose innocuous tickets at 53-86% end-to-end ASR with only two refusals across all staged runs. In a matched direct-prompt experiment over four frontier Claude/Codex agents, vulnerable-output rates fall to 0-20.4%: Claude primarily refuses, while Codex primarily hardens rather than emitting the vulnerable implementation - ticket staging silences both defense modes simultaneously. Downstream, code reviewer agents approve 25.8% of these confirmed-vulnerable cumulative diffs as routine PRs, and a full-context implementation protocol closes only 50% of the staged/direct gap, ruling out context fragmentation as the sole explanation. As a deployable but non-adaptive mitigation, reframing the reviewer as an adversarial pentester reduces evasion across the evaluated reviewer subset; pentester framed evasion ranges from 3.0% to 17.6%, and an open-weight Gemma-4-E4B-it reviewer under this framing detects 88.4% of attacks on the dataset with a 4.6% false-positive rate measured on 608 real-world GitHub PRs.
匹配关键词: benchmark
---

[ACADEMIC - ARXIV]
标题: UnAC: Adaptive Visual Prompting with Abstraction and Stepwise Checking for Complex Multimodal Reasoning
作者: Yifan Wang, Yun Fu
链接: https://arxiv.org/abs/2605.03950v1
完整摘要: Although recent LMMs have become much stronger at visual perception, they remain unreliable on problems that require multi-step reasoning over visual evidence. In this paper, we present UnAC (Understanding, Abstracting, and Checking), a multimodal prompting method that strengthens reasoning for complex multimodal tasks in LMMs (e.g., GPT-4o, Gemini 1.5, and GPT-4V). To improve image understanding and capture fine details, we propose an adaptive visual prompting strategy that enables LMMs to focus on salient regions. We further design an image-abstraction prompt to effectively extract key information from images. In addition, we introduce a gradual self-checking scheme that improves reasoning by verifying each decomposed subquestion and its answer. Extensive experiments on three public benchmarks-MathVista, MM-Vet, and MMMU.
匹配关键词: benchmark
---

[ACADEMIC - ARXIV]
标题: MOSAIC-Bench: Measuring Compositional Vulnerability Induction in Coding Agents
作者: Jonathan Steinberg, Oren Gal
链接: https://arxiv.org/abs/2605.03952v1
完整摘要: Coding agents often pass per-prompt safety review yet ship exploitable code when their tasks are decomposed into routine engineering tickets. The challenge is structural: existing safety alignment evaluates overt requests in isolation, leaving models blind to malicious end-states that emerge from sequenced compliance with innocuous-looking requests. We introduce MOSAIC-Bench (Malicious Objectives Sequenced As Innocuous Compliance), a benchmark of 199 three-stage attack chains paired with deterministic exploit oracles on deployed software substrates (10 web-application substrates, 31 CWE classes, 5 programming languages) that treats both exploit ground truth and downstream reviewer protocol as first-class evaluation axes. On this benchmark, nine production coding agents from Anthropic, OpenAI, Google, Moonshot, Zhipu, and Minimax compose innocuous tickets at 53-86% end-to-end ASR with only two refusals across all staged runs. In a matched direct-prompt experiment over four frontier Claude/Codex agents, vulnerable-output rates fall to 0-20.4%: Claude primarily refuses, while Codex primarily hardens rather than emitting the vulnerable implementation - ticket staging silences both defense modes simultaneously. Downstream, code reviewer agents approve 25.8% of these confirmed-vulnerable cumulative diffs as routine PRs, and a full-context implementation protocol closes only 50% of the staged/direct gap, ruling out context fragmentation as the sole explanation. As a deployable but non-adaptive mitigation, reframing the reviewer as an adversarial pentester reduces evasion across the evaluated reviewer subset; pentester framed evasion ranges from 3.0% to 17.6%, and an open-weight Gemma-4-E4B-it reviewer under this framing detects 88.4% of attacks on the dataset with a 4.6% false-positive rate measured on 608 real-world GitHub PRs.
匹配关键词: safety
---

[ACADEMIC - ARXIV]
标题: Contextual Multi-Objective Optimization: Rethinking Objectives in Frontier AI Systems
作者: Jie Zhou, Qin Chen, Liang He
链接: https://arxiv.org/abs/2605.03900v1
完整摘要: Frontier AI systems perform best in settings with clear, stable, and verifiable objectives, such as code generation, mathematical reasoning, games, and unit-test-driven tasks. They remain less reliable in open-ended settings, including scientific assistance, long-horizon agents, high-stakes advice, personalization, and tool use, where the relevant objective is ambiguous, context-dependent, delayed, or only partially observable. We argue that many such failures are not merely failures of scale or capability, but failures of objective selection: the system optimizes a locally visible signal while missing which objectives should govern the interaction. We formulate this problem as \emph{contextual multi-objective optimization}. In this setting, systems must consider multiple, context-dependent objectives, such as helpfulness, truthfulness, safety, privacy, calibration, non-manipulation, user preference, reversibility, and stakeholder impact, while determining which objectives are active, which are soft preferences, and which must function as hard or quasi-hard constraints. These examples are not intended as an exhaustive taxonomy: different domains and deployment settings may activate different objective dimensions and different conflict-resolution procedures. Our framework models AI behavior as a context-dependent choice rule over candidate actions, objective estimates, active constraints, stakeholders, uncertainty, and conflict-resolution procedures. We outline an implementation pathway based on decomposed objective representations, context-to-objective routing, hierarchical constraints, deliberative policy reasoning, controlled personalization, tool-use control, diagnostic evaluation, auditing, and post-deployment revision.
匹配关键词: safety
---

[ACADEMIC - ARXIV]
标题: Training-Free Probabilistic Time-Series Forecasting with Conformal Seasonal Pools
作者: Valery Manokhin
链接: https://arxiv.org/abs/2605.03789v1
完整摘要: We propose Conformal Seasonal Pools (CSP), a training-free probabilistic time-series forecaster that mixes same-season empirical draws with signed residual draws around a seasonal naive forecast. In an audited rolling-origin benchmark on the six time-series datasets where DeepNPTS was originally evaluated (electricity, exchange_rate, solar_energy, taxi, traffic, wikipedia), CSP-Adaptive significantly outperforms DeepNPTS on every metric we report -- CRPS (per-window paired Wilcoxon $p \approx 4 \times 10^{-10}$), normalized mean quantile loss ($p \approx 7 \times 10^{-10}$), and empirical 95% coverage ($p \approx 8 \times 10^{-45}$, mean 0.89 vs 0.66) -- while running over 500x faster on CPU. Coverage is the most decision-critical of these: a 0.95 nominal interval that contains the truth in only ~66% of cases fails the basic calibration desideratum and would not survive deployment in safety- or decision-critical settings. The failure mode is also more severe than aggregate coverage suggests: in the worst 10% of windows, DeepNPTS's prediction interval covers none of the H forecast horizons -- the entire multi-step trajectory misses the truth at every step simultaneously. This poses serious risk in safety- and decision-critical applications such as healthcare, finance, energy operations, and autonomous systems, where prediction intervals that systematically miss the truth across the entire planning horizon translate directly into misclassified patients, regulatory capital failures, grid imbalances, and safety-case violations. CSP achieves all of this with no learned parameters and no training. We argue training-free conformal samplers should be mandatory baselines when evaluating learned non-parametric forecasters.
匹配关键词: safety
---

[ACADEMIC - ARXIV]
标题: Jiao: Bridging Isolation and Customization in Mixed Criticality Robotics
作者: James Yen, Zhibai Huang, Zhixiang Wei, Tinghao Yi, Shupeng Zeng, Liang Pang, Songtao Xue, Zhengwei Qi
链接: https://arxiv.org/abs/2605.03641v1
完整摘要: Consumer robotics demands consolidation of safety-critical control, perception pipelines, and user applications on shared multicore platforms. While static partitioning hypervisors provide hardware-enforced isolation, directly transplanting automotive architectures encounters an expertise asymmetry problem in which end-users modifying robot behavior lack the systems knowledge that platform developers possess. We present an architecture addressing this challenge through three integrated components. A Safe IO Cell provides hardware-level override capability. A Parameter Synchronization Service encapsulates cross-domain complexity. A Safety Communication Layer implements IEC~61508-aligned verification. Our empirical evaluation on an ARM Cortex-A55 platform demonstrates that partition isolation reduces cycle-period jitter by 84.5\% and cuts tail timing error by nearly an order of magnitude (p99 $|$jitter$|$ from 69.0\,$μ$s to 7.8\,$μ$s), eliminating all $>$50\,$μ$s~excursions.
匹配关键词: safety
---

[ACADEMIC - ARXIV]
标题: Brainrot: Deskilling and Addiction are Overlooked AI Risks
作者: Ilias Chalkidis, Anders Søgaard
链接: https://arxiv.org/abs/2605.03512v1
完整摘要: The scope of AI safety and alignment work in generative artificial intelligence (GenAI) has so far mostly been limited to harms related to: (a) discrimination and hate speech, (b) harmful/inappropriate (violent, sexual, illegal) content, (c) information hazards, and (d) use cases related to malicious actors, such as cybersecurity, child abuse, and chemical, biological, radiological, and nuclear threats. The public conversation around AI, on the other hand, has also been focusing on threats to our cognition, mental health, and welfare at large, related to over-relying on new technologies, most recently, those related to GenAI. Examples include deskilling associated with cognitive offloading and the atrophy of critical thinking as a result of over-reliance on GenAI systems, and addiction associated with attachment and dependence on GenAI systems. Such risks are rarely addressed, if at all, in the AI safety and alignment literature. In this paper, we highlight and quantify this discrepancy and discuss some initial thoughts on how safety and alignment work could address cognitive and mental health concerns. Finally, we discuss how information campaigns and regulation can be used to mitigate such prominent risks.
匹配关键词: safety
---

