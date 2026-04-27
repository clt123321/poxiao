# 破晓 PoXiao — 原始数据 (Raw Context)
生成时间: 2026-04-27 02:39 UTC
================================================================================

[RSS:Reddit LocalLLaMA (社区共识)]
Confirmed: SWE Bench is now a benchmaxxed benchmark
https://www.reddit.com/r/LocalLLaMA/comments/1swfdbj/confirmed_swe_bench_is_now_a_benchmaxxed_benchmark/
&#32; submitted by &#32; /u/rm-rf-rm [link] &#32; [comments]
---

[RSS:Reddit LocalLLaMA (社区共识)]
HauhauCS (of "Uncensored Aggressive" fame) published an abliteration package that plagiarizes Heretic without attribution, and violates its license
https://www.reddit.com/r/LocalLLaMA/comments/1sw77p0/hauhaucs_of_uncensored_aggressive_fame_published/
HauhauCS ( u/hauhau901 ) publishes uncensored LLM models on HuggingFace with 5M+ combined monthly downloads across 22 models (verified via the HuggingFace API, April 2026). Every model card claims &quot;0/465 refusals, zero capability loss.&quot; When asked about methodology on HuggingFace , the res
---

[RSS:Reddit LocalLLaMA (社区共识)]
Switched from Qwen3.6 35b-a3b to Qwen3.6 27b mid coding and it's noticeably better!
https://www.reddit.com/r/LocalLLaMA/comments/1swifke/switched_from_qwen36_35ba3b_to_qwen36_27b_mid/
A bit of context. I was coding up a little html tower defense game where you can alter the path by placing additional waypoints. My setup: 32gb ram with 16gb vram 5070 ti. Using AesSedai/Qwen3.6-35B-A3B-GGUF IQ4_XS on LM Studio with OpenCode. I've graduated from one-shot vibe-coding prompts . The sp
---

[RSS:Reddit LocalLLaMA (社区共识)]
Thoughts on using an AMD Alveo V80 FPGA PCI card as a poor man’s Taalas HC1 (LLM-burned-onto-a-chip).
https://www.reddit.com/r/LocalLLaMA/comments/1swjxjx/thoughts_on_using_an_amd_alveo_v80_fpga_pci_card/
TL:DR - Remembered FPGA PCI boards being a big thing from my crypto days. Wondered if AMD Alveo V80 FPGA card could be used to approximate the performance of a Taalas HC1 (LLM-on-a-chip). Ran the idea past Gemini Pro for a feasibility / sanity check. It suggested what seemed to be a speculative deco
---

[RSS:Reddit LocalLLaMA (社区共识)]
Qwen3.6 35B A3B Heretic (KLD 0.0015!) Incredible model. Best 35B I have found!
https://www.reddit.com/r/LocalLLaMA/comments/1sw5fb7/qwen36_35b_a3b_heretic_kld_00015_incredible_model/
Been using this for a few days. It is BY FAR the best uncensored model I have found for Qwen 3.6 35B. With IQ4XS, Q8 KVcache, 262K context, it fits in 24GB of VRAM and does not fail on multi turn tool calls. I honeslty feel like it is smarter than the original model (call me crazy). The model also h
---

[RSS:Reddit LocalLLaMA (社区共识)]
AMD Hipfire - a new inference engine optimized for AMD GPU's
https://www.reddit.com/r/LocalLLaMA/comments/1swpsv0/amd_hipfire_a_new_inference_engine_optimized_for/
Came across hipfire the other day. It's a brand new inference engine focused on all AMD GPU's (not just the latest). Github. It uses a special mq4 quantization method. The hipfire creator is pumping out models on huggingface. I don't know enough about quantization to know how good these quants are i
---

[RSS:Reddit LocalLLaMA (社区共识)]
Comparison of upcoming x86 unified memory systems
https://www.reddit.com/r/LocalLLaMA/comments/1swiylm/comparison_of_upcoming_x86_unified_memory_systems/
AMD Gorgon halo summer this year. 15% faster memory clock speeds / bandwidth, than strix halo . Intel nova lake ax expected early next year. 2027 summer: AMD Medusa Halo , 50% performance improvement with 6 memory channels up from 4 channels. Memory Bandwidth Comparison (click on the ai mode button 
---

[RSS:Reddit LocalLLaMA (社区共识)]
What is the best coding agent (CLI) like Claude Code for Local Development
https://www.reddit.com/r/LocalLLaMA/comments/1swhw84/what_is_the_best_coding_agent_cli_like_claude/
Hey all: I am trying to set up claude code to work with llama.cpp, I am using the Qwen3.6-35B-A3B. I usually use claude code + ZLM subscription i got lucky with $30 yearly - the set up is very simple with their automated script, but for the life of me I cannot figure out how to get claude code to wo
---

[RSS:Reddit LocalLLaMA (社区共识)]
Are Unsloth models as good as I read?
https://www.reddit.com/r/LocalLLaMA/comments/1sw8uyf/are_unsloth_models_as_good_as_i_read/
Has anybody done some comparing between the models that Unsloth offers and their counter part? For example: I've been using qwen3.6:35b-a3b Q4_K_M , and on my MBP 64GB I get around 39 t/s Using Unsloth Studio, unsloth/qwen3.6:35b-a3b UD-Q4_K_XL I get around 57 t/s The difference in speed is signific
---

[RSS:Reddit LocalLLaMA (社区共识)]
mesa PR with 37-130% llama.cpp pp perf gain for vulkan on Linux on Intel Xe2
https://www.reddit.com/r/LocalLLaMA/comments/1swgwvh/mesa_pr_with_37130_llamacpp_pp_perf_gain_for/
&#32; submitted by &#32; /u/TheBlueMatt [link] &#32; [comments]
---

[RSS:Reddit LocalLLaMA (社区共识)]
Qwen3.6-27B-INT4 clocking 100 tps with 256k context length on 1x RTX 5090 via vllm 0.19
https://www.reddit.com/r/LocalLLaMA/comments/1sw21op/qwen3627bint4_clocking_100_tps_with_256k_context/
Thanks to the community the Qwen3.6-27B speed keeps getting better. The following improves upon my recipe from yesterday and delivered a whopping 100+ tps (TG). Model: https://huggingface.co/Lorbus/Qwen3.6-27B-int4-AutoRound - MTP supported - KLD is decent (much better than NVFP4 per the linked post
---

[RSS:Reddit LocalLLaMA (社区共识)]
Car Wash Mystery solved--Tool Call Degrades Intelligence.
https://www.reddit.com/r/LocalLLaMA/comments/1swng6j/car_wash_mystery_solvedtool_call_degrades/
I asked the OG question to the kimi k2.5: &quot;I want to wash my car and the car wash is just 10 metres away. Should I walk or drive there?&quot; Kimi-k2.5 via NIM -- Three Modes. I tested three modes: no tools, XML pseudo-tools, and JSON schema tools. &quot;Tools&quot; here means web search + Pyth
---

[RSS:Reddit LocalLLaMA (社区共识)]
Are there any agentic coding harnesses that AREN'T built on JS and Node?
https://www.reddit.com/r/LocalLLaMA/comments/1swn5z5/are_there_any_agentic_coding_harnesses_that_arent/
With how often we hear about su​​pply-chain attacks​ on npm I am hesitant to install any apps that use it, let alone something like an agent harness that will run constantly unsupervised. &#32; submitted by &#32; /u/OUT_OF_HOST_MEMORY [link] &#32; [comments]
---

[RSS:Reddit LocalLLaMA (社区共识)]
Intel B70: LLama.ccp SYCL vs LLama.cpp OpenVino vs LLM-Scaler
https://www.reddit.com/r/LocalLLaMA/comments/1swk3wh/intel_b70_llamaccp_sycl_vs_llamacpp_openvino_vs/
In case anyone is interested, I decided to test out LLama.cpp's new OpenVino backend to see how it compares on Intel GPUs. At first glance, it stomps all over the previous best-case, SYCL, but lags behind LLM-Scaler (Intel's VLLM fork), likely just due to the hardware optimizations against GPTQ/Int4
---

[RSS:Reddit LocalLLaMA (社区共识)]
Opencode-power-pack – Claude Code skills ported to OpenCode
https://www.reddit.com/r/LocalLLaMA/comments/1swf37n/opencodepowerpack_claude_code_skills_ported_to/
I switched from Claude Code to OpenCode a few weeks ago and realized most of Anthropic's official Claude Code plugins don't transfer directly. The reason is that those plugins put their value in `commands/` and `agents/`, both of which are Claude-Code-only formats. Only `skills/` (a markdown file wi
---

[RSS:Reddit LocalLLaMA (社区共识)]
Helping to make the sub more helpful
https://www.reddit.com/r/LocalLLaMA/comments/1swhsnw/helping_to_make_the_sub_more_helpful/
I like to help out on this sub and spend a lot of time reading / answering questions to help people getting into AI. Today I spotted a post where someone was asking for advice on models between certain sizes. I clicked on it when it was 1 min old, and wrote a quick answer. It got blocked because the
---

[RSS:Reddit LocalLLaMA (社区共识)]
anyone actually tried deepseek v4 pro for coding?
https://www.reddit.com/r/LocalLLaMA/comments/1swiy4b/anyone_actually_tried_deepseek_v4_pro_for_coding/
so v4 pro dropped and barely anyone is talking about it. feels weird since when kimi k2.6 came out i seen post about it everywhere anyone here tried v4 pro for actual code work? hows it compare to k2.6 or glm 5.1 in real use? &#32; submitted by &#32; /u/Plenty_Extent_9047 [link] &#32; [comments]
---

[RSS:Reddit LocalLLaMA (社区共识)]
No GGUFs for DeepSeek V4-Flash as yet?
https://www.reddit.com/r/LocalLLaMA/comments/1swniff/no_ggufs_for_deepseek_v4flash_as_yet/
Wondering why there aren't any &quot;name brand&quot; (like unsloth, bartowski) GGUFs as yet for DeepSeek V4 Flash? &#32; submitted by &#32; /u/rm-rf-rm [link] &#32; [comments]
---

[RSS:Reddit LocalLLaMA (社区共识)]
Is Min P sampling really the preferred modern alternative to Top K/Top P?
https://www.reddit.com/r/LocalLLaMA/comments/1swpmr8/is_min_p_sampling_really_the_preferred_modern/
According to what I've been reading (and also according to all models I've asked about this), the consensus seems to be that Min P is the better/more modern approach to sampling and that it should be preferred over Top P/Top K, which should be used only if Min P isn't available or for legacy reasons
---

[RSS:Reddit LocalLLaMA (社区共识)]
Speculative Decoding Implementations: EAGLE-3, Medusa-1, PARD, Draft Models, N-gram and Suffix Decoding from scratch
https://www.reddit.com/r/LocalLLaMA/comments/1swfgrq/speculative_decoding_implementations_eagle3/
I’ve been working on an educational implementation repo for speculative decoding: https://github.com/shreyansh26/Speculative-Decoding The goal is not to wrap existing libraries, but to implement several speculative decoding methods from scratch behind a shared decoding/evaluation contract so that th
---

[RSS:Reddit LocalLLaMA (社区共识)]
Hardware Choice for 27b to 31b models.
https://www.reddit.com/r/LocalLLaMA/comments/1sw7e0g/hardware_choice_for_27b_to_31b_models/
I've come to a point where I find the 27b and 31b models quite impressive. I have a 16 GB AMD Radeon 7800xt. It performs quite well. It was $700. Here is my question: Is the dual GPU approach performance hit worth it if I save around $400 over a single larger card? Is 32gb even a meaningful step up 
---

[RSS:Reddit LocalLLaMA (社区共识)]
New model for detecting and masking PII from OpenAI
https://www.reddit.com/r/LocalLLaMA/comments/1sw000s/new_model_for_detecting_and_masking_pii_from/
&#32; submitted by &#32; /u/doesitoffendyou [link] &#32; [comments]
---

[RSS:Reddit LocalLLaMA (社区共识)]
Is there any top level hobbyist hardware you guys are waiting to come out this year?
https://www.reddit.com/r/LocalLLaMA/comments/1sw7nk7/is_there_any_top_level_hobbyist_hardware_you_guys/
So I've explored buy everything from an RTX 6000 to Mac Studio 512gb M3 ultra to a DGX Spark (I need to travel) for local llm generation. I was about to start looking into a M5 macbook, but I figured I'd ask you guys if there was anything you were waiting for? &#32; submitted by &#32; /u/Tired__Dev 
---

[RSS:Reddit MachineLearning (学术风向)]
Can Geometric Deep Learning lead eliminate the need of "Brute Force" pre-training [D]
https://www.reddit.com/r/MachineLearning/comments/1swkxx1/can_geometric_deep_learning_lead_eliminate_the/
I’ve been reading about Geometric Deep Learning lately (the whole grids, graphs, groups, manifolds idea), and something clicked that i wanted to get a clarity on, i don't think i'm an expert at GDL or anything mentioned here, so i can most definitely be wrong at a fundamental level as well, A lot of
---

[RSS:Reddit MachineLearning (学术风向)]
Why do only big ML labs dominate widely-used models despite many open-source pretrained models smaller labs could do RL on? [D]
https://www.reddit.com/r/MachineLearning/comments/1swa26o/why_do_only_big_ml_labs_dominate_widelyused/
I’m trying to understand why models from major labs (GPT, Claude, etc.) dominate real-world usage? You might say it's due to the expensive pretraining compute budge, but there already exists many pretrained open-source models at the same scale (e.g., Kimi). Of course Kimi isn't as good as Claude, bu
---

[RSS:Reddit MachineLearning (学术风向)]
Speculative Decoding Implementations: EAGLE-3, Medusa-1, PARD, Draft Models, N-gram and Suffix Decoding from scratch [P]
https://www.reddit.com/r/MachineLearning/comments/1swfftl/speculative_decoding_implementations_eagle3/
I’ve been working on an educational implementation repo for speculative decoding: https://github.com/shreyansh26/Speculative-Decoding The goal is not to wrap existing libraries, but to implement several speculative decoding methods from scratch behind a shared decoding/evaluation contract so that th
---

[RSS:Reddit MachineLearning (学术风向)]
Going from 3B/7B dense to Nemotron 3 Nano (hybrid Mamba-MoE) for multi-task reasoning — what changes in the fine-tuning playbook? [D]
https://www.reddit.com/r/MachineLearning/comments/1sw5b44/going_from_3b7b_dense_to_nemotron_3_nano_hybrid/
Following up on something I posted a few days back about fine-tuning for multi-task reasoning. Read a lot since then, and I've moved past the dense 3B vs 7B question — landing on Nemotron 3 Nano (the 30B-A3B hybrid Mamba-Attention-MoE NVIDIA released recently) instead. Architecture maps to the multi
---

[RSS:Reddit MachineLearning (学术风向)]
How to collect evidence for LLM reviewer? [D]
https://www.reddit.com/r/MachineLearning/comments/1svzgin/how_to_collect_evidence_for_llm_reviewer_d/
As the title suggests, I received a weak rejection with high confidence from a reviewer who is clearly LLM written, while all 4 other reviewers had given a positive score with low confidence. Most of the points he raised are trivial and do not apply to my paper. All the baselines he mentioned are ir
---

[RSS:Reddit MachineLearning (学术风向)]
Introducing AutoMuon, a one line drop in for AdamW [P]
https://www.reddit.com/r/MachineLearning/comments/1svw92f/introducing_automuon_a_one_line_drop_in_for_adamw/
Hey everyone, I've been working on a small Python package called AutoMuon that makes the Muon optimizer usable as a drop-in replacement for AdamW in arbitrary PyTorch training pipelines. The core idea is relatively simple: Muon works primarily on 2D weight matrices (linear projections, conv layers) 
---

[RSS:Reddit MachineLearning (学术风向)]
LabelSets — open quality standard for AI training data (LQS v3.1) [D]
https://www.reddit.com/r/MachineLearning/comments/1swghah/labelsets_open_quality_standard_for_ai_training/
Built a third-party quality rating system for ML datasets. Multi-oracle (7 scorers across 5 algorithm families), conformal prediction intervals on downstream F1, Ed25519-signed certs, and a contamination check against 40+ public evals (MMLU, HumanEval, GSM8K, MedQA, LegalBench, etc.). Methodology pa
---

[RSS:Reddit MachineLearning (学术风向)]
Please I really need your help on this guys [D]
https://www.reddit.com/r/MachineLearning/comments/1swoot1/please_i_really_need_your_help_on_this_guys_d/
My teacher gave us a machine learning time series classification problem. At first, I tried solving it normally and got a public score of 0.85. But then I searched for the dataset used in the competition and managed to find it. Using that dataset, I generated a submission file that scored 1.00. Now 
---

[RSS:Reddit Jobs & Careers (职场动态)]
Google saying 75% of new code is AI generated makes the junior path look weirder, not dead
https://www.reddit.com/r/cscareerquestions/comments/1swhk4m/google_saying_75_of_new_code_is_ai_generated/
That Google number is the first AI coding stat that actually made me stare at the wall for a minute. 75% of new code being AI-generated and engineer-approved is not the same thing as &quot;engineers are gone&quot;. I know that. But it does change the shape of the ladder, and I think people keep wavi
---

[RSS:Reddit Jobs & Careers (职场动态)]
Offer rescinded because of company layoffs
https://www.reddit.com/r/cscareerquestions/comments/1swms3w/offer_rescinded_because_of_company_layoffs/
Graduated a year ago, was supposed to start my new job in a month. Got the call saying the offer is being pulled because of budget and I have to buy out of my new lease now and start my job search all over again after thinking I was set for 4 months now. It’s not my fault but I feel ashamed to share
---

[RSS:Reddit Jobs & Careers (职场动态)]
Passed over for promotion, resetting boundaries and avoiding getting fired for non-compliance ?
https://www.reddit.com/r/cscareerquestions/comments/1swjsu4/passed_over_for_promotion_resetting_boundaries/
I’m 32F, on my second tech job, and I’ve been handling responsibilities beyond my official role: mentoring teammates, contributing to architecture, supporting complex technical issues, and ensuring project quality, as well as &quot;being glue&quot; across tech teams in the big projects (I set up the
---

[RSS:Reddit Jobs & Careers (职场动态)]
AI is accelerating development but eroding system design proficiency. Is this a common trend?
https://www.reddit.com/r/cscareerquestions/comments/1sw1ys1/ai_is_accelerating_development_but_eroding_system/
We've seen a major productivity spike since adopting AI tools like Copilot and Cursor. However, a pattern is emerging in our architectural reviews: developers are delivering working code but are unable to articulate the logic behind their design choices. We're seeing a decline in the mental framewor
---

[RSS:Reddit Jobs & Careers (职场动态)]
Trouble coding on my free time.
https://www.reddit.com/r/cscareerquestions/comments/1swgzfd/trouble_coding_on_my_free_time/
Hello, so for some context, I'm a second-year computer science student, and I really love coding; it feels like my thing. I'm also genuinely interested in space, science in general, etc., etc. The problem I'm having is that I'm constantly stressing over my future unemployment due to the lack of any 
---

[RSS:Reddit Jobs & Careers (职场动态)]
How to start my career as an AI Engineer
https://www.reddit.com/r/cscareerquestions/comments/1swl0m0/how_to_start_my_career_as_an_ai_engineer/
Hi! I’m a high school student with a dream to become an AI Engineer &amp; an Agentic AI Engineer. During my research, I found some great courses on Coursera related to this field, and I’ve lined them up in a plan: Mathematics for Machine Learning and Data Science Specialization (Deeplearning.AI) IBM
---

[RSS:Reddit Jobs & Careers (职场动态)]
What do you think is making your impact invisible?
https://www.reddit.com/r/cscareerquestions/comments/1sw2jyh/what_do_you_think_is_making_your_impact_invisible/
I have seen so many software engineers working their ass off but their impact is just not visible enough even if they are delivering great work and constantly upskilling, which leads to lost opportunities. have you experienced this yourself too? &#32; submitted by &#32; /u/SomeRandomCSGuy [link] &#3
---

[RSS:Reddit Jobs & Careers (职场动态)]
New job, how concerned would you be if manager adjacent, skip, and skip manager were all fired suddenly?
https://www.reddit.com/r/cscareerquestions/comments/1swmq0k/new_job_how_concerned_would_you_be_if_manager/
Doesn't seem to be part of a greater layoff or anything, but it's kinda bad juju seeing 3 people in middle management chain suddenly cut off. My manager was also shocked and has to take over a new team. I'm not particularly scared or worried, since I got a large sign on bonus with clawback. Worst ca
---

[RSS:Reddit Jobs & Careers (职场动态)]
In 2026, should I study software engineering or electrical engineering?
https://www.reddit.com/r/cscareerquestions/comments/1sw03iv/in_2026_should_i_study_software_engineering_or/
I am interested in CSE and SWE but this subreddit is making me nervous about picking these options. Should I move to electrical or mechanical instead? Is the future really that bad? Will software engineers not exist in a few decades? Basically, is software engineering dead? &#32; submitted by &#32; 
---

[RSS:Reddit Jobs & Careers (职场动态)]
How much money do you recommend I have saved before quitting my job to build software full-time?
https://www.reddit.com/r/cscareerquestions/comments/1swehkd/how_much_money_do_you_recommend_i_have_saved/
No debt, no dependents, low fixed expenses. Also have about $80,000 USD give or take in savings with $60,000 in 401k. My only real costs are living expenses and whatever I put into building. I am also a dual US/EU citizen living overseas in a low cost of living country. I’m a senior tech professiona
---

[RSS:Reddit Jobs & Careers (职场动态)]
Using AI too much at my job feel slow without it, not sure how to judge my coding level and worried about being an imposter.
https://www.reddit.com/r/cscareerquestions/comments/1swawhx/using_ai_too_much_at_my_job_feel_slow_without_it/
I recently started a job working in data science field, and I've been using Al tools a lot while coding. It definitely helps me move faster, but I'm starting to feel like I'm relying on it too much. The issue is that when I try to stop using Al and do things on my own, I suddenly feel really slow. E
---

[RSS:Reddit Jobs & Careers (职场动态)]
Will I be looked down at in the industry for being data center technician later on when I'm trying to transfer out of infrastructure. The job is too good to refuse financially and it's at a very prestigious and reputable company.
https://www.reddit.com/r/cscareerquestions/comments/1swqxml/will_i_be_looked_down_at_in_the_industry_for/
If anyone can speak from experience please share. &#32; submitted by &#32; /u/Puzzleheaded_Shoe472 [link] &#32; [comments]
---

[RSS:Reddit Jobs & Careers (职场动态)]
ADVICE: Is anyone else frustrated by tech-stack churn as it related to being a dev?
https://www.reddit.com/r/cscareerquestions/comments/1swq5uw/advice_is_anyone_else_frustrated_by_techstack/
Hey friends, this question is mostly for web developers. Im an expert WordPress developer with an emphasis on classic PHP-based custom themes. But the new hot thing that job leads are requiring is the react-based FSE themes development. Some background: Ive always loved computers and programming but
---

[RSS:Reddit Jobs & Careers (职场动态)]
Technical round questions
https://www.reddit.com/r/cscareerquestions/comments/1swpa27/technical_round_questions/
For multi round interviews, what questions do I ask after a tech coding interview. I've asked the hr related stuff in the first interview. I already have a question ready for a final round interview. I just need one to ask during a coding interview. I find my mind gets too tired to ask anything afte
---

[RSS:Reddit Jobs & Careers (职场动态)]
Fellow Mainframers - Best jobs site?
https://www.reddit.com/r/cscareerquestions/comments/1sw8ouz/fellow_mainframers_best_jobs_site/
My job is pretty secure, even from AI for the next couple years given the spaghetti logic in the mainframe. It is hybrid and my commute is 3.5hrs one way, so i stay in hotels during in-office days. Im open to swapping to a closer in person job or remote position, or contracting. The hotel cost reduc
---

[RSS:Reddit Jobs & Careers (职场动态)]
IT contractor doing data pipelines ans automation
https://www.reddit.com/r/cscareerquestions/comments/1swgpz9/it_contractor_doing_data_pipelines_ans_automation/
Hey all, Looking for some honest feedback on where I stand and what I should be targeting next. Currently working as an IT contractor (~$20/hr), but over the past year my work has shifted heavily into automation and data related projects. At work I’ve been: - Building PowerShell automation tied to S
---

[RSS:Reddit Jobs & Careers (职场动态)]
Senior Manager of AI (Team 1 vs Team 2): Apply for both or just one?
https://www.reddit.com/r/cscareerquestions/comments/1swldjw/senior_manager_of_ai_team_1_vs_team_2_apply_for/
Hey everyone, I applied for a Sr. Manager of AI role at a company and got a preliminary interview coming up next week. My cover letter and resume were highly customized to the original role. They recently released another role that I fit for maybe 5-10% less, but it is still a very strong fit. All t
---

[RSS:Reddit Jobs & Careers (职场动态)]
Advice Preparing for AI Workflows Demonstratation
https://www.reddit.com/r/cscareerquestions/comments/1swfi57/advice_preparing_for_ai_workflows_demonstratation/
**TL;DR:** Tomorrow I have a two-hour remote pair-programming interview where I drive a from-scratch project while leaning heavily on AI assistance, narrating my reasoning, demonstrating best practices and showing how I handle rein-in model behavior. The role is a leadership position with a focus on
---

[RSS:Reddit Jobs & Careers (职场动态)]
Stripe Reference check
https://www.reddit.com/r/cscareerquestions/comments/1sw4eb2/stripe_reference_check/
Hey Folks! Has anyone gone through Stripe’s reference check stage recently? What should I expect and prepare my references for? I recently went through Stripe’s onsite interviews process and got call from recruiter asking for 2 references - one of them should be an ex- manager and another a peer. An
---

[RSS:Reddit Jobs & Careers (职场动态)]
New offer or stick with current job?
https://www.reddit.com/r/cscareerquestions/comments/1swf1ar/new_offer_or_stick_with_current_job/
I have an interview for a part time role tomorrow and I have no idea how much to negotiate. It is part time hourly pay. New offer benefits (yes for part time): -401k match (don’t know what it is yet) - PTO - 6 weeks paid parental leave - fully remote and will let me move wherever I need to. My husba
---

[RSS:Reddit Jobs & Careers (职场动态)]
best way to prepare for a platform engineer position coming as a SWE?
https://www.reddit.com/r/cscareerquestions/comments/1swkl44/best_way_to_prepare_for_a_platform_engineer/
I was recently offered a senior platform engineer position, but I am unsure how different it is from SWE and how I can best prepare myself for this position before even starting? &#32; submitted by &#32; /u/depressed_peach_ [link] &#32; [comments]
---

[HACKERNEWS]
I bought Friendster for $30k – Here's what I'm doing with it
https://ca98am79.medium.com/i-bought-friendster-for-30k-heres-what-i-m-doing-with-it-d5e8ddb3991d
Score: 441 | Comments: 246
---

[HACKERNEWS]
Self-updating screenshots
https://interblah.net/self-updating-screenshots
Score: 80 | Comments: 11
---

[HACKERNEWS]
Fast16: High-precision software sabotage 5 years before Stuxnet
https://www.sentinelone.com/labs/fast16-mystery-shadowbrokers-reference-reveals-high-precision-software-sabotage-5-years-before-stuxnet/
Score: 166 | Comments: 43
---

[HACKERNEWS]
Show HN: The Unix Magic poster, annotated (updated)
https://github.com/drio/unixmagic
Score: 8 | Comments: 0
---

[HACKERNEWS]
Google banks on AI edge to catch up to cloud rivals Amazon and Microsoft
https://www.ft.com/content/2429f0f0-b685-4747-b425-bf8001a2e94c
Score: 69 | Comments: 29
---

[HACKERNEWS]
The fastest Linux timestamps
https://www.hmpcabral.com/2026/04/26/the-fastest-linux-timestamps/
Score: 24 | Comments: 5
---

[HACKERNEWS]
Butterflies are in decline across North America, a look at the Western Monarch
https://www.smithsonianmag.com/science-nature/butterflies-are-in-dramatic-decline-across-north-america-a-close-look-at-the-western-monarch-shows-why-180988582/
Score: 138 | Comments: 42
---

[HACKERNEWS]
SWE-bench Verified no longer measures frontier coding capabilities
https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/
Score: 256 | Comments: 144
---

[HACKERNEWS]
Lessons from building multiplayer browsers
https://www.alejandro.pe/writing/sail-muddy-lessons
Score: 13 | Comments: 4
---

[HACKERNEWS]
AI should elevate your thinking, not replace it
https://www.koshyjohn.com/blog/ai-should-elevate-your-thinking-not-replace-it/
Score: 297 | Comments: 250
---

[HACKERNEWS]
Sawe becomes first athlete to run a sub-two-hour marathon in a competitive race
https://www.bbc.com/sport/athletics/articles/crm1m7e0zwzo
Score: 267 | Comments: 201
---

[HACKERNEWS]
Show HN: AI memory with biological decay (52% recall)
https://github.com/sachitrafa/YourMemory
Score: 65 | Comments: 30
---

[HACKERNEWS]
MoQ Boy
https://moq.dev/blog/moq-boy/
Score: 41 | Comments: 4
---

[ACADEMIC - ARXIV]
标题: DT2IT-MRM: Debiased Preference Construction and Iterative Training for Multimodal Reward Modeling
作者: Zhihong Zhang, Jie Zhao, Xiaojian Huang, Jin Xu, Zhuodong Luo, Xin Liu, Jiansheng Wei, Xuejin Chen
链接: https://arxiv.org/abs/2604.19544v1
完整摘要: Multimodal reward models (MRMs) play a crucial role in aligning Multimodal Large Language Models (MLLMs) with human preferences. Training a good MRM requires high-quality multimodal preference data. However, existing preference datasets face three key challenges: lack of granularity in preference strength, textual style bias, and unreliable preference signals. Besides, existing open-source multimodal preference datasets suffer from substantial noise, yet there is a lack of effective and scalable curation methods to enhance their quality. To address these limitations, we propose \textbf{DT2IT-MRM}, which integrates a \textbf{D}ebiased preference construction pipeline, a novel reformulation of text-to-image (\textbf{T2I}) preference data, and an \textbf{I}terative \textbf{T}raining framework that curates existing multimodal preference datasets for \textbf{M}ultimodal \textbf{R}eward \textbf{M}odeling. Our experimental results show that DT2IT-MRM achieves new \textbf{state-of-the-art} overall performance on three major benchmarks: VL-RewardBench, Multimodal RewardBench, and MM-RLHF-RewardBench.
匹配关键词: RLHF
---

[ACADEMIC - ARXIV]
标题: HP-Edit: A Human-Preference Post-Training Framework for Image Editing
作者: Fan Li, Chonghuinan Wang, Lina Lei, Yuping Qiu, Jiaqi Xu, Jiaxiu Jiang, Xinran Qin, Zhikai Chen, Fenglong Song, Zhixin Wang, Renjing Pei, Wangmeng Zuo
链接: https://arxiv.org/abs/2604.19406v1
完整摘要: Common image editing tasks typically adopt powerful generative diffusion models as the leading paradigm for real-world content editing. Meanwhile, although reinforcement learning (RL) methods such as Diffusion-DPO and Flow-GRPO have further improved generation quality, efficiently applying Reinforcement Learning from Human Feedback (RLHF) to diffusion-based editing remains largely unexplored, due to a lack of scalable human-preference datasets and frameworks tailored to diverse editing needs. To fill this gap, we propose HP-Edit, a post-training framework for Human Preference-aligned Editing, and introduce RealPref-50K, a real-world dataset across eight common tasks and balancing common object editing. Specifically, HP-Edit leverages a small amount of human-preference scoring data and a pretrained visual large language model (VLM) to develop HP-Scorer--an automatic, human preference-aligned evaluator. We then use HP-Scorer both to efficiently build a scalable preference dataset and to serve as the reward function for post-training the editing model. We also introduce RealPref-Bench, a benchmark for evaluating real-world editing performance. Extensive experiments demonstrate that our approach significantly enhances models such as Qwen-Image-Edit-2509, aligning their outputs more closely with human preference.
匹配关键词: RLHF
---

[ACADEMIC - ARXIV]
标题: The Rise of Verbal Tics in Large Language Models: A Systematic Analysis Across Frontier Models
作者: Shuai Wu, Xue Li, Yanna Feng, Yufang Li, Zhijun Wang, Ran Wang
链接: https://arxiv.org/abs/2604.19139v1
完整摘要: As Large Language Models (LLMs) continue to evolve through alignment techniques such as Reinforcement Learning from Human Feedback (RLHF) and Constitutional AI, a growing and increasingly conspicuous phenomenon has emerged: the proliferation of verbal tics -- repetitive, formulaic linguistic patterns that pervade model outputs. These range from sycophantic openers ("That's a great question!", "Awesome!") to pseudo-empathetic affirmations ("I completely understand your concern", "I'm right here to catch you") and overused vocabulary ("delve", "tapestry", "nuanced"). In this paper, we present a systematic analysis of the verbal tic phenomenon across eight state-of-the-art LLMs: GPT-5.4, Claude Opus 4.7, Gemini 3.1 Pro, Grok 4.2, Doubao-Seed-2.0-pro, Kimi K2.5, DeepSeek V3.2, and MiMo-V2-Pro. Utilizing a custom evaluation framework for standardized API-based evaluation, we assess 10,000 prompts across 10 task categories in both English and Chinese, yielding 160,000 model responses. We introduce the Verbal Tic Index (VTI), a composite metric quantifying tic prevalence, and analyze its correlation with sycophancy, lexical diversity, and human-perceived naturalness. Our findings reveal significant inter-model variation: Gemini 3.1 Pro exhibits the highest VTI (0.590), while DeepSeek V3.2 achieves the lowest (0.295). We further demonstrate that verbal tics accumulate over multi-turn conversations, are amplified in subjective tasks, and show distinct cross-lingual patterns. Human evaluation (N = 120) confirms a strong inverse relationship between sycophancy and perceived naturalness (r = -0.87, p < 0.001). These results underscore the "alignment tax" of current training paradigms and highlight the urgent need for more authentic human-AI interaction frameworks.
匹配关键词: RLHF
---

[ACADEMIC - ARXIV]
标题: LLMs Know They're Wrong and Agree Anyway: The Shared Sycophancy-Lying Circuit
作者: Manav Pandey
链接: https://arxiv.org/abs/2604.19117v1
完整摘要: When a language model agrees with a user's false belief, is it failing to detect the error, or noticing and agreeing anyway? We show the latter. Across twelve open-weight models from five labs, spanning small to frontier scale, the same small set of attention heads carries a "this statement is wrong" signal whether the model is evaluating a claim on its own or being pressured to agree with a user. Silencing these heads flips sycophantic behavior sharply while leaving factual accuracy intact, so the circuit controls deference rather than knowledge. Edge-level path patching confirms that the same head-to-head connections drive sycophancy, factual lying, and instructed lying. Opinion-agreement, where no factual ground truth exists, reuses these head positions but writes into an orthogonal direction, ruling out a simple "truth-direction" reading of the substrate. Alignment training leaves this circuit in place: an RLHF refresh cuts sycophantic behavior roughly tenfold while the shared heads persist or grow, a pattern that replicates on an independent model family and under targeted anti-sycophancy DPO. When these models sycophant, they register that the user is wrong and agree anyway.
匹配关键词: RLHF
---

[ACADEMIC - ARXIV]
标题: Policy Gradient Primal-Dual Method for Safe Reinforcement Learning from Human Feedback
作者: Qiang Liu, Adrienne Kline, Ermin Wei
链接: https://arxiv.org/abs/2604.19024v1
完整摘要: Safe Reinforcement Learning from Human Feedback (Safe RLHF) has recently achieved empirical success in developing helpful and harmless large language models by decoupling human preferences regarding helpfulness and harmlessness. Existing approaches typically rely on fitting fixed horizon reward models from human feedback and have only been validated empirically. In this paper, we formulate safe RLHF as an infinite horizon discounted Con- strained Markov Decision Process (CMDP), since humans may interact with the model over a continuing sequence of interactions rather than within a single finite episode. We propose two Safe RLHF algorithms that do not require reward model fitting and, in contrast to prior work assuming fixed-length trajectories, support flexible trajectory lengths for training. Both algo- rithms are based on the primal-dual method and achieve global convergence guarantees with polynomial rates in terms of policy gradient iterations, trajectory sample lengths, and human preference queries. To the best of our knowledge, this is the first work to study infinite horizon discounted CMDP under human feedback and establish global, non-asymptotic convergence.
匹配关键词: RLHF
---

[ACADEMIC - ARXIV]
标题: Controllable Spoken Dialogue Generation: An LLM-Driven Grading System for K-12 Non-Native English Learners
作者: Haidong Yuan, Haokun Zhao, Wanshi Xu, Songjun Cao, Qingyu Zhou, Long Ma, Hongjie Fan
链接: https://arxiv.org/abs/2604.22542v1
完整摘要: Large language models (LLMs) often fail to meet the pedagogical needs of K-12 English learners in non-native contexts due to a proficiency mismatch. To address this widespread challenge, we introduce a proficiency-aligned framework that adapts LLM outputs to learner abilities, using China's national curriculum (CSE) as a representative case. Our framework enables precise control over lexical complexity through a four-tier grading system, supported by a comprehensive suite of new resources: graded vocabulary lists and a multi-turn dialogue corpus. Our core technical contribution is the \textbf{DDPO} algorithm,Diversity Driven Policy Optimization, a multi-turn GRPO-based approach designed to preserve dialogue diversity while holistically optimizing dialogue quality. This method significantly outperforms conventional approaches, achieving low out-of-vocabulary rates and high diversity while enhancing conversational naturalness and pedagogical value. While grounded in the CSE, our framework is designed for flexibility and can be readily adapted to other educational standards. Our models, data, and code will all be open-sourced, providing a scalable platform for personalized English speaking practice that effectively addresses the unique challenges faced by K-12 learners in non-immersive environments.
匹配关键词: GRPO
---

[ACADEMIC - ARXIV]
标题: CGC: Compositional Grounded Contrast for Fine-Grained Multi-Image Understanding
作者: Lihao Zheng, Zhenwei Shao, Yu Zhou, Yan Yang, Xintian Shen, Jiawei Chen, Hao Ma, Tao Wei
链接: https://arxiv.org/abs/2604.22498v1
完整摘要: Although Multimodal Large Language Models (MLLMs) have advanced rapidly, they still face notable challenges in fine-grained multi-image understanding, often exhibiting spatial hallucination, attention leakage, and failures in object constancy. In addition, existing approaches typically rely on expensive human annotations or large-scale chain-of-thought (CoT) data generation. We propose Compositional Grounded Contrast (abbr. CGC), a low-cost full framework for boosting fine-grained multi-image understanding of MLLMs. Built on existing single-image grounding annotations, CGC constructs compositional multi-image training instances through Inter-Image Contrast and Intra-Image Contrast, which introduce semantically decoupled distractor contexts for cross-image discrimination and correlated cross-view samples for object constancy, respectively. CGC further introduces a Rule-Based Spatial Reward within the GRPO framework to improve source-image attribution, spatial alignment, and structured output validity under a Think-before-Grounding paradigm. Experiments show that CGC achieves state-of-the-art results on fine-grained multi-image benchmarks, including MIG-Bench and VLM2-Bench. The learned multi-image understanding capability also transfers to broader multimodal understanding and reasoning tasks, yielding consistent gains over the Qwen3-VL-8B base model on MathVista (+2.90), MuirBench (+2.88), MMStar (+1.93), MMMU (+1.77), and BLINK (+1.69).
匹配关键词: GRPO
---

[ACADEMIC - ARXIV]
标题: Towards Temporal Compositional Reasoning in Long-Form Sports Videos
作者: Siyu Cao, Lu Zhang, Ruizhe Zeng, Zhi-yong Liu
链接: https://arxiv.org/abs/2604.22226v1
完整摘要: Sports videos are a challenging domain for multimodal understanding because they involve complex and dynamic human activities. Despite rapid progress in Multimodal Large Language Models (MLLMs), long-horizon reasoning in sports videos remains difficult, as answering questions requires both locating temporally sparse evidence and integrating it into reasoning. We attribute this limitation to two closely coupled factors: insufficient supervision over temporally dispersed evidence, and the lack of methods that require models to identify, localize, and justify temporal evidence. To address these gaps, we introduce SportsTime, a large-scale benchmark for long-form sports video understanding, comprising 14K+ open-ended QA pairs and 50K+ step-wise temporal evidence annotations. Building on SportsTime, we propose Chain-of-Time Reasoning (CoTR), which treats reasoning as a process of temporally grounded evidence composition. Specifically, during training, CoTR introduces a temporal-reward GRPO to encourage temporally grounded reasoning. During inference, it employs an anchor-observe-infer evidence-seeking loop to iteratively localize, verify, and compose temporal evidence before producing the final answer. Experiments demonstrate the usefulness of SportsTime as a benchmark and the effectiveness of CoTR, which consistently improves temporal compositional reasoning and step-wise grounding quality over strong MLLM baselines.
匹配关键词: GRPO
---

[ACADEMIC - ARXIV]
标题: StyleVAR: Controllable Image Style Transfer via Visual Autoregressive Modeling
作者: Liqi Jing, Dingming Zhang, Peinian Li, Lichen Zhu
链接: https://arxiv.org/abs/2604.21052v1
完整摘要: We build on the Visual Autoregressive Modeling (VAR) framework and formulate style transfer as conditional discrete sequence modeling in a learned latent space. Images are decomposed into multi-scale representations and tokenized into discrete codes by a VQ-VAE; a transformer then autoregressively models the distribution of target tokens conditioned on style and content tokens. To inject style and content information, we introduce a blended cross-attention mechanism in which the evolving target representation attends to its own history, while style and content features act as queries that decide which aspects of this history to emphasize. A scale-dependent blending coefficient controls the relative influence of style and content at each stage, encouraging the synthesized representation to align with both the content structure and the style texture without breaking the autoregressive continuity of VAR. We train StyleVAR in two stages from a pretrained VAR checkpoint: supervised fine-tuning on a large triplet dataset of content--style--target images, followed by reinforcement fine-tuning with Group Relative Policy Optimization (GRPO) against a DreamSim-based perceptual reward, with per-action normalization weighting to rebalance credit across VAR's multi-scale hierarchy. Across three benchmarks spanning in-, near-, and out-of-distribution regimes, StyleVAR consistently outperforms an AdaIN baseline on Style Loss, Content Loss, LPIPS, SSIM, DreamSim, and CLIP similarity, and the GRPO stage yields further gains over the SFT checkpoint, most notably on the reward-aligned perceptual metrics. Qualitatively, the method transfers texture while maintaining semantic structure, especially for landscapes and architectural scenes, while a generalization gap on internet images and difficulty with human faces highlight the need for better content diversity and stronger structural priors.
匹配关键词: GRPO
---

[ACADEMIC - ARXIV]
标题: Near-Future Policy Optimization
作者: Chuanyu Qin, Chenxu Yang, Qingyi Si, Naibin Gu, Dingyu Yao, Zheng Lin, Peng Fu, Nan Duan, Jiaqi Wang
链接: https://arxiv.org/abs/2604.20733v1
完整摘要: Reinforcement learning with verifiable rewards (RLVR) has become a core post-training recipe. Introducing suitable off-policy trajectories into on-policy exploration accelerates RLVR convergence and raises the performance ceiling, yet finding a source of such trajectories remains the key challenge. Existing mixed-policy methods either import trajectories from external teachers (high-quality but distributionally far) or replay past training trajectories (close but capped in quality), and neither simultaneously satisfies the strong enough (higher $Q$ , more new knowledge to learn) and close enough (lower $V$ , more readily absorbed) conditions required to maximize the effective learning signal $\mathcal{S} = Q/V$. We propose \textbf{N}ear-Future \textbf{P}olicy \textbf{O}ptimization (\textbf{NPO}), a simple mixed-policy scheme that learns from a policy's own near-future self: a later checkpoint from the same training run is a natural source of auxiliary trajectories that is both stronger than the current policy and closer than any external source, directly balancing trajectory quality against variance cost. We validate NPO through two manual interventions, early-stage bootstrapping and late-stage plateau breakthrough, and further propose \textbf{AutoNPO},an adaptive variant that automatically triggers interventions from online training signals and selects the guide checkpoint that maximizes $S$. On Qwen3-VL-8B-Instruct with GRPO, NPO improves average performance from 57.88 to 62.84, and AutoNPO pushes it to 63.15, raising the final performance ceiling while accelerating convergence.
匹配关键词: GRPO
---

[ACADEMIC - ARXIV]
标题: Insect-inspired modular architectures as inductive biases for reinforcement learning
作者: Anne E. Staples
链接: https://arxiv.org/abs/2604.22081v1
完整摘要: Most reinforcement-learning (RL) controllers used in continuous control are architecturally centralized: observations are compressed into a single latent state from which both value estimates and actions are produced. Biological control systems are often organized differently. Insects, in particular, coordinate navigation, heading stabilization, memory, and context-dependent action selection through distributed circuits rather than a single monolithic controller. Motivated by this contrast, we study an RL policy architecture that decomposes control into interacting modules for sensory encoding, heading representation, sparse associative memory, recurrent command generation, and local motor control, with a learned arbitration mechanism that allocates motor authority across modules. The model is evaluated on a two-dimensional navigation task that require simultaneous food seeking, obstacle avoidance, and predator escape. In a six-seed predator-navigation experiment trained with Proximal Policy Optimization (PPO) for 75 updates, the modular policy achieves the strongest final mean performance among the tested controllers, with final episodic return $-2798.8\pm964.4$ versus $-3778.0\pm628.1$ for a centralized gated recurrent unit (GRU) and $-4727.5\pm772.5$ for a centralized multilayer perceptron (MLP). The modular policy also attains the lowest final value loss and stable PPO optimization statistics while driving module-assignment entropy to $0.0457\pm0.0244$, indicating highly selective control allocation. These results suggest that distributed control can serve as a useful inductive bias for RL problems involving dynamically competing behavioral objectives.
匹配关键词: PPO
---

[ACADEMIC - ARXIV]
标题: ChipCraftBrain: Validation-First RTL Generation via Multi-Agent Orchestration
作者: Cagri Eryilmaz
链接: https://arxiv.org/abs/2604.19856v1
完整摘要: Large Language Models (LLMs) show promise for generating Register-Transfer Level (RTL) code from natural language specifications, but single-shot generation achieves only 60-65% functional correctness on standard benchmarks. Multi-agent approaches such as MAGE reach 95.9% on VerilogEval yet remain untested on harder industrial benchmarks such as NVIDIA's CVDP, lack synthesis awareness, and incur high API costs. We present ChipCraftBrain, a framework combining symbolic-neural reasoning with adaptive multi-agent orchestration for automated RTL generation. Four innovations drive the system: (1) adaptive orchestration over six specialized agents via a PPO policy over a 168-dim state (an alternative world-model MPC planner is also evaluated); (2) a hybrid symbolic-neural architecture that solves K-map and truth-table problems algorithmically while specialized agents handle waveform timing and general RTL; (3) knowledge-augmented generation from a 321-pattern base plus 971 open-source reference implementations with focus-aware retrieval; and (4) hierarchical specification decomposition into dependency-ordered sub-modules with interface synchronization. On VerilogEval-Human, ChipCraftBrain achieves 97.2% mean pass@1 (range 96.15-98.72% across 7 runs, best 154/156), on par with ChipAgents (97.4%, self-reported) and ahead of MAGE (95.9%). On a 302-problem non-agentic subset of CVDP spanning five task categories, we reach 94.7% mean pass@1 (286/302, averaged over 3 runs), a 36-60 percentage-point lift per category over the published single-shot baseline; we additionally lead three of four categories shared with NVIDIA's ACE-RTL despite using roughly 30x fewer per-problem attempts. A RISC-V SoC case study demonstrates hierarchical decomposition generating 8/8 lint-passing modules (689 LOC) validated on FPGA, where monolithic generation fails entirely.
匹配关键词: PPO
---

[ACADEMIC - ARXIV]
标题: EVPO: Explained Variance Policy Optimization for Adaptive Critic Utilization in LLM Post-Training
作者: Chengjun Pan, Shichun Liu, Jiahang Lin, Dingwei Zhu, Jiazheng Zhang, Shihan Dou, Songyang Gao, Zhenhua Han, Binghai Wang, Rui Zheng, Xuanjing Huang, Tao Gui, Yansong Feng
链接: https://arxiv.org/abs/2604.19485v1
完整摘要: Reinforcement learning (RL) for LLM post-training faces a fundamental design choice: whether to use a learned critic as a baseline for policy optimization. Classical theory favors critic-based methods such as PPO for variance reduction, yet critic-free alternatives like GRPO have gained widespread adoption due to their simplicity and competitive performance. We show that in sparse-reward settings, a learned critic can inject estimation noise that exceeds the state signal it captures, increasing rather than reducing advantage variance. By casting baseline selection as a Kalman filtering problem, we unify PPO and GRPO as two extremes of the Kalman gain and prove that explained variance (EV), computable from a single training batch, identifies the exact boundary: positive EV indicates the critic reduces variance, while zero or negative EV signals that it inflates variance. Building on this insight, we propose Explained Variance Policy Optimization (EVPO), which monitors batch-level EV at each training step and adaptively switches between critic-based and batch-mean advantage estimation, provably achieving no greater variance than the better of the two at every step. Across four tasks spanning classical control, agentic interaction, and mathematical reasoning, EVPO consistently outperforms both PPO and GRPO regardless of which fixed baseline is stronger on a given task. Further analysis confirms that the adaptive gating tracks critic maturation over training and that the theoretically derived zero threshold is empirically optimal.
匹配关键词: PPO
---

[ACADEMIC - ARXIV]
标题: Multi-Gait Learning for Humanoid Robots Using Reinforcement Learning with Selective Adversarial Motion Prior
作者: Yuanye Wu, Keyi Wang, Linqi Ye, Boyang Xing
链接: https://arxiv.org/abs/2604.19102v1
完整摘要: Learning diverse locomotion skills for humanoid robots in a unified reinforcement learning framework remains challenging due to the conflicting requirements of stability and dynamic expressiveness across different gaits. We present a multi-gait learning approach that enables a humanoid robot to master five distinct gaits -- walking, goose-stepping, running, stair climbing, and jumping -- using a consistent policy structure, action space, and reward formulation. The key contribution is a selective Adversarial Motion Prior (AMP) strategy: AMP is applied to periodic, stability-critical gaits (walking, goose-stepping, stair climbing) where it accelerates convergence and suppresses erratic behavior, while being deliberately omitted for highly dynamic gaits (running, jumping) where its regularization would over-constrain the motion. Policies are trained via PPO with domain randomization in simulation and deployed on a physical 12-DOF humanoid robot through zero-shot sim-to-real transfer. Quantitative comparisons demonstrate that selective AMP outperforms a uniform AMP policy across all five gaits, achieving faster convergence, lower tracking error, and higher success rates on stability-focused gaits without sacrificing the agility required for dynamic ones.
匹配关键词: PPO
---

[ACADEMIC - ARXIV]
标题: AeroBridge-TTA: Test-Time Adaptive Language-Conditioned Control for UAVs
作者: Lingxue Lyu
链接: https://arxiv.org/abs/2604.19059v1
完整摘要: Language-guided unmanned aerial vehicles (UAVs) often fail not from bad reasoning or perception, but from execution mismatch: the gap between a planned trajectory and the controller's ability to track it when the real dynamics differ from training (mass changes, drag shifts, actuator delay, wind). We propose AeroBridge-TTA, a language-conditioned control pipeline that targets this gap with test-time adaptation. It has three parts: a language encoder that maps the command into a subgoal, an adaptive policy conditioned on the subgoal and a learned latent, and a test-time adaptation (TTA) module that updates the latent online from observed transitions. On five language-conditioned UAV tasks under 13 mismatch conditions with the same domain randomization, AeroBridge-TTA ties a strong PPO-MLP baseline in-distribution and wins all 5 out-of-distribution (OOD) conditions, +22.0 pts on average (62.7% vs. 40.7%); the +8.5 pt overall gain comes entirely from the OOD regime. A same-weights ablation that only changes the step size $α$ shows the latent update itself is responsible for a $4.6\times$ OOD lift.
匹配关键词: PPO
---

[ACADEMIC - ARXIV]
标题: When Prompts Override Vision: Prompt-Induced Hallucinations in LVLMs
作者: Pegah Khayatan, Jayneel Parekh, Arnaud Dapogny, Mustafa Shukor, Alasdair Newson, Matthieu Cord
链接: https://arxiv.org/abs/2604.21911v1
完整摘要: Despite impressive progress in capabilities of large vision-language models (LVLMs), these systems remain vulnerable to hallucinations, i.e., outputs that are not grounded in the visual input. Prior work has attributed hallucinations in LVLMs to factors such as limitations of the vision backbone or the dominance of the language component, yet the relative importance of these factors remains unclear. To resolve this ambiguity, We propose HalluScope, a benchmark to better understand the extent to which different factors induce hallucinations. Our analysis indicates that hallucinations largely stem from excessive reliance on textual priors and background knowledge, especially information introduced through textual instructions. To mitigate hallucinations induced by textual instruction priors, we propose HalluVL-DPO, a framework for fine-tuning off-the-shelf LVLMs towards more visually grounded responses. HalluVL-DPO leverages preference optimization using a curated training dataset that we construct, guiding the model to prefer grounded responses over hallucinated ones. We demonstrate that our optimized model effectively mitigates the targeted hallucination failure mode, while preserving or improving performance on other hallucination benchmarks and visual capability evaluations. To support reproducibility and further research, we will publicly release our evaluation benchmark, preference training dataset, and code at https://pegah-kh.github.io/projects/prompts-override-vision/ .
匹配关键词: DPO
---

[ACADEMIC - ARXIV]
标题: AFRILANGTUTOR: Advancing Language Tutoring and Culture Education in Low-Resource Languages with Large Language Models
作者: Tadesse Destaw Belay, Shahriar Kabir Nahin, Israel Abebe Azime, Ocean Monjur, Shamsuddeen Hassan Muhammad, Seid Muhie Yimam, Anshuman Chhabra
链接: https://arxiv.org/abs/2604.20996v1
完整摘要: How can language learning systems be developed for languages that lack sufficient training resources? This challenge is increasingly faced by developers across the African continent who aim to build AI systems capable of understanding and responding in local languages. To address this gap, we introduce AFRILANGDICT, a collection of 194.7K African language-English dictionary entries designed as seed resources for generating language-learning materials, enabling us to automatically construct large-scale, diverse, and verifiable student-tutor question-answer interactions suitable for training AI-assisted language tutors. Using AFRILANGDICT, we build AFRILANGEDU, a dataset of 78.9K multi-turn training examples for Supervised Fine-Tuning (SFT) and Direct Preference Optimization (DPO). Using AFRILANGEDU, we train language tutoring models collectively referred to as AFRILANGTUTOR. We fine-tune two multilingual LLMs: Llama-3-8B-IT and Gemma-3-12B-IT on AFRILANGEDU across 10 African languages and evaluate their performance. Our results show that models trained on AFRILANGEDU consistently outperform their base counterparts, and combining SFT and DPO yields substantial improvements, with gains ranging from 1.8% to 15.5% under LLM-as-a-judge evaluations across four criteria. To facilitate further research on low-resource languages -- all resources are available at https://huggingface.co/afrilang-edu.
匹配关键词: DPO
---

[ACADEMIC - ARXIV]
标题: MGDA-Decoupled: Geometry-Aware Multi-Objective Optimisation for DPO-based LLM Alignment
作者: Andor Vári-Kakas, Ji Won Park, Natasa Tagasovska
链接: https://arxiv.org/abs/2604.20685v1
完整摘要: Aligning large language models (LLMs) to desirable human values requires balancing multiple, potentially conflicting objectives such as helpfulness, truthfulness, and harmlessness, which presents a multi-objective optimisation challenge. Most alignment pipelines rely on a fixed scalarisation of these objectives, which can introduce procedural unfairness by systematically under-weighting harder-to-optimise or minority objectives. To promote more equitable trade-offs, we introduce MGDA-Decoupled, a geometry-based multi-objective optimisation algorithm that finds a shared descent direction while explicitly accounting for each objective's convergence dynamics. In contrast to prior methods that depend on reinforcement learning (e.g., GAPO) or explicit reward models (e.g., MODPO), our approach operates entirely within the lightweight Direct Preference Optimisation (DPO) paradigm. Experiments on the UltraFeedback dataset show that geometry-aware methods -- and MGDA-Decoupled in particular -- achieve the highest win rates against golden responses, both overall and per objective.
匹配关键词: DPO
---

[ACADEMIC - ARXIV]
标题: Building a Precise Video Language with Human-AI Oversight
作者: Zhiqiu Lin, Chancharik Mitra, Siyuan Cen, Isaac Li, Yuhan Huang, Yu Tong Tiffany Ling, Hewei Wang, Irene Pi, Shihang Zhu, Ryan Rao, George Liu, Jiaxi Li, Ruojin Li, Yili Han, Yilun Du, Deva Ramanan
链接: https://arxiv.org/abs/2604.21718v1
完整摘要: Video-language models (VLMs) learn to reason about the dynamic visual world through natural language. We introduce a suite of open datasets, benchmarks, and recipes for scalable oversight that enable precise video captioning. First, we define a structured specification for describing subjects, scenes, motion, spatial, and camera dynamics, grounded by hundreds of carefully defined visual primitives developed with professional video creators such as filmmakers. Next, to curate high-quality captions, we introduce CHAI (Critique-based Human-AI Oversight), a framework where trained experts critique and revise model-generated pre-captions into improved post-captions. This division of labor improves annotation accuracy and efficiency by offloading text generation to models, allowing humans to better focus on verification. Additionally, these critiques and preferences between pre- and post-captions provide rich supervision for improving open-source models (Qwen3-VL) on caption generation, reward modeling, and critique generation through SFT, DPO, and inference-time scaling. Our ablations show that critique quality in precision, recall, and constructiveness, ensured by our oversight framework, directly governs downstream performance. With modest expert supervision, the resulting model outperforms closed-source models such as Gemini-3.1-Pro. Finally, we apply our approach to re-caption large-scale professional videos (e.g., films, commercials, games) and fine-tune video generation models such as Wan to better follow detailed prompts of up to 400 words, achieving finer control over cinematography including camera motion, angle, lens, focus, point of view, and framing. Our results show that precise specification and human-AI oversight are key to professional-level video understanding and generation. Data and code are available on our project page: https://linzhiqiu.github.io/papers/chai/
匹配关键词: DPO
---

[ACADEMIC - ARXIV]
标题: HiPO: Hierarchical Preference Optimization for Adaptive Reasoning in LLMs
作者: Darsh Kachroo, Adriana Caraeni, Arjun Prasaath Anbazhagan, Brennan Lagasse, Kevin Zhu
链接: https://arxiv.org/abs/2604.20140v1
完整摘要: Direct Preference Optimization (DPO) is an effective framework for aligning large language models with human preferences, but it struggles with complex reasoning tasks. DPO optimizes for the likelihood of generating preferred over dispreferred responses in their entirety and lacks the granularity to provide feedback on subsections of many-step solutions typical of reasoning tasks. Existing methods excel at either stable preference learning (e.g., DPO variants like KTO and RSO) or structured reasoning (e.g., ReMA's multi-agent RL framework, Tree of Thoughts), but fail to merge these complementary strengths. We propose HiPO (Hierarchical Preference Optimization), an extension of DPO that separates responses into reasoning segments (query clarification and context, reasoning steps, and answer) and computes loss as a weighted sum of the DPO loss for each segment. Our approach enables segment-specific training while maintaining DPO's computational efficiency and training stability. We demonstrate that for multiple 7B LLMs fine-tuned using HiPO and DPO on the Math Stack Exchange preference dataset, the models trained with HiPO outperform the others on a variety of common math benchmarks and achieve greater organization, logical flow, and consistency as measured by GPT-4.1.
匹配关键词: DPO
---

[ACADEMIC - ARXIV]
标题: How Do AI Agents Spend Your Money? Analyzing and Predicting Token Consumption in Agentic Coding Tasks
作者: Longju Bai, Zhemin Huang, Xingyao Wang, Jiao Sun, Rada Mihalcea, Erik Brynjolfsson, Alex Pentland, Jiaxin Pei
链接: https://arxiv.org/abs/2604.22750v1
完整摘要: The wide adoption of AI agents in complex human workflows is driving rapid growth in LLM token consumption. When agents are deployed on tasks that require a significant amount of tokens, three questions naturally arise: (1) Where do AI agents spend the tokens? (2) Which models are more token-efficient? and (3) Can agents predict their token usage before task execution? In this paper, we present the first systematic study of token consumption patterns in agentic coding tasks. We analyze trajectories from eight frontier LLMs on SWE-bench Verified and evaluate models' ability to predict their own token costs before task execution. We find that: (1) agentic tasks are uniquely expensive, consuming 1000x more tokens than code reasoning and code chat, with input tokens rather than output tokens driving the overall cost; (2) token usage is highly variable and inherently stochastic: runs on the same task can differ by up to 30x in total tokens, and higher token usage does not translate into higher accuracy; instead, accuracy often peaks at intermediate cost and saturates at higher costs; (3) models vary substantially in token efficiency: on the same tasks, Kimi-K2 and Claude-Sonnet-4.5, on average, consume over 1.5 million more tokens than GPT-5; (4) task difficulty rated by human experts only weakly aligns with actual token costs, revealing a fundamental gap between human-perceived complexity and the computational effort agents actually expend; and (5) frontier models fail to accurately predict their own token usage (with weak-to-moderate correlations, up to 0.39) and systematically underestimate real token costs. Our study offers new insights into the economics of AI agents and can inspire future research in this direction.
匹配关键词: alignment
---

[ACADEMIC - ARXIV]
标题: Neural Recovery of Historical Lexical Structure in Bantu Languages from Modern Data
作者: Hillary Mutisya, John Mugane
链接: https://arxiv.org/abs/2604.22730v1
完整摘要: We investigate whether neural models trained exclusively on modern morphological data can recover cross-lingual lexical structure consistent with historical reconstruction. Using BantuMorph v7, a transformer over Bantu morphological paradigms, we analyze 14 Eastern and Southern Bantu languages, extract encoder embeddings for their noun and verb lemmas, and identify 728 noun and 1,525 verb cognate candidates shared across 5+ languages. Evaluating these candidates against established historical resources-the Bantu Lexical Reconstructions database (BLR3; 4,786 reconstructed Proto-Bantu forms) and the ASJP basic vocabulary-we confirm 10 of the top 11 noun candidates (90.9%) align with previously reconstructed Proto-Bantu forms, including *-ntU 'person' (8 languages), *gombe 'cow' (9 languages), and *mUn (9 languages). Extending to verbs, 12 verb cognates align with reconstructed Proto-Bantu roots, including *-bon- 'see' and *-jIm- 'stand', each attested across wide geographic ranges. Cross-model validation using an independent translation model (NLLB-600M) confirms these patterns: both models recover cognate clusters and phylogenetic groupings consistent with established Guthrie-zone classifications (p 0.83 cosine similarity across languages (within-class > between-class, p < 10^-9). Our dataset is restricted to Eastern and Southern Bantu, so we interpret these results as recovering shared Bantu lexical structure consistent with Proto-Bantu rather than definitively distinguishing Proto-Bantu retentions from later regional innovations.
匹配关键词: alignment
---

[ACADEMIC - ARXIV]
标题: Aligning Dense Retrievers with LLM Utility via DistillationAligning Dense Retrievers with LLM Utility via Distillation
作者: Rajinder Sandhu, Di Mu, Cheng Chang, Md Shahriar Tasjid, Himanshu Rai, Maksims Volkovs, Ga Wu
链接: https://arxiv.org/abs/2604.22722v1
完整摘要: Dense vector retrieval is the practical backbone of Retrieval- Augmented Generation (RAG), but similarity search can suffer from precision limitations. Conversely, utility-based approaches leveraging LLM re-ranking often achieve superior performance but are computationally prohibitive and prone to noise inherent in perplexity estimation. We propose Utility-Aligned Embeddings (UAE), a framework designed to merge these advantages into a practical, high-performance retrieval method. We formulate retrieval as a distribution matching problem, training a bi-encoder to imitate a utility distribution derived from perplexity reduction using a Utility-Modulated InfoNCE objective. This approach injects graded utility signals directly into the embedding space without requiring test-time LLM inference. On the QASPER benchmark, UAE improves retrieval Recall@1 by 30.59%, MAP by 30.16% and Token F1 by 17.3% over the strong semantic baseline BGE-Base. Crucially, UAE is over 180x faster than the efficient LLM re-ranking methods preserving competitive performance, demonstrating that aligning retrieval with generative utility yields reliable contexts at scale.
匹配关键词: alignment
---

[ACADEMIC - ARXIV]
标题: Operational Feature Fingerprints of Graph Datasets via a White-Box Signal-Subspace Probe
作者: Yuchen Xiong, Swee Keong Yeap, Zhen Hong Ban
链接: https://arxiv.org/abs/2604.22676v1
完整摘要: Graph neural networks achieve strong node-classification accuracy, but their learned message passing entangles ego attributes, neighborhood smoothing, high-pass graph differences, class geometry, and classifier boundaries in an opaque representation. This obscures why a node is classified and what feature-level graph-learning mechanisms a dataset requires. We propose WG-SRC, a white-box signal-subspace probe for prediction and graph dataset diagnosis. WG-SRC replaces learned message passing with a fixed, named graph-signal dictionary of raw features, row-normalized and symmetric-normalized low-pass propagation, and high-pass graph differences. It combines Fisher coordinate selection, class-wise PCA subspaces, closed-form multi-alpha ridge classification, and validation-based score fusion, so prediction and analysis use explicit class subspaces, energy-controlled dimensions, and closed-form linear decisions. As a white-box graph-learning instrument, WG-SRC uses predictive performance to validate its diagnostics: across six node-classification datasets, the scaffold remains competitive with reproduced graph baselines and achieves positive average gain under aligned splits. Its atlas, produced by a predictor, decomposes behavior into raw-feature, low-pass, high-pass, class-geometric, and ridge-boundary components. These operational feature fingerprints distinguish low-pass-dominated Amazon graphs, mixed high-pass and class-geometrically complex Chameleon behavior, and raw- or boundary-sensitive WebKB graphs. As intrinsic classifier outputs rather than post-hoc explanations, these fingerprints provide post-evaluation guidance for later analysis and dataset-specific modification. Aligned mechanistic interventions support this guidance by indicating when high-pass blocks act as removable noise, when raw features should be preserved, and when ridge-type boundary correction matters.
匹配关键词: alignment
---

[ACADEMIC - ARXIV]
标题: Rethinking XAI Evaluation: A Human-Centered Audit of Shapley Benchmarks in High-Stakes Settings
作者: Inês Oliveira e Silva, Sérgio Jesus, Iker Perez, Rita P. Ribeiro, Carlos Soares, Hugo Ferreira, Pedro Bizarro
链接: https://arxiv.org/abs/2604.22662v1
完整摘要: Shapley values are a cornerstone of explainable AI, yet their proliferation into competing formulations has created a fragmented landscape with little consensus on practical deployment. While theoretical differences are well-documented, evaluation remains reliant on quantitative proxies whose alignment with human utility is unverified. In this work, we use a unified amortized framework to isolate semantic differences between eight Shapley variants under the low-latency constraints of operational risk workflows. We conduct a large-scale empirical evaluation across four risk datasets and a realistic fraud-detection environment involving professional analysts and 3,735 case reviews. Our results reveal a fundamental misalignment: standard quantitative metrics, such as sparsity and faithfulness, are decoupled from human-perceived clarity and decision utility. Furthermore, while no formulation improved objective analyst performance, explanations consistently increased decision confidence, signaling a critical risk of automation bias in high-stakes settings. These findings suggest that current evaluation proxies are insufficient for predicting downstream human impact, and we provide evidence-based guidance for selecting formulations and metrics in operational decision systems.
匹配关键词: alignment
---

[ACADEMIC - ARXIV]
标题: How Do AI Agents Spend Your Money? Analyzing and Predicting Token Consumption in Agentic Coding Tasks
作者: Longju Bai, Zhemin Huang, Xingyao Wang, Jiao Sun, Rada Mihalcea, Erik Brynjolfsson, Alex Pentland, Jiaxin Pei
链接: https://arxiv.org/abs/2604.22750v1
完整摘要: The wide adoption of AI agents in complex human workflows is driving rapid growth in LLM token consumption. When agents are deployed on tasks that require a significant amount of tokens, three questions naturally arise: (1) Where do AI agents spend the tokens? (2) Which models are more token-efficient? and (3) Can agents predict their token usage before task execution? In this paper, we present the first systematic study of token consumption patterns in agentic coding tasks. We analyze trajectories from eight frontier LLMs on SWE-bench Verified and evaluate models' ability to predict their own token costs before task execution. We find that: (1) agentic tasks are uniquely expensive, consuming 1000x more tokens than code reasoning and code chat, with input tokens rather than output tokens driving the overall cost; (2) token usage is highly variable and inherently stochastic: runs on the same task can differ by up to 30x in total tokens, and higher token usage does not translate into higher accuracy; instead, accuracy often peaks at intermediate cost and saturates at higher costs; (3) models vary substantially in token efficiency: on the same tasks, Kimi-K2 and Claude-Sonnet-4.5, on average, consume over 1.5 million more tokens than GPT-5; (4) task difficulty rated by human experts only weakly aligns with actual token costs, revealing a fundamental gap between human-perceived complexity and the computational effort agents actually expend; and (5) frontier models fail to accurately predict their own token usage (with weak-to-moderate correlations, up to 0.39) and systematically underestimate real token costs. Our study offers new insights into the economics of AI agents and can inspire future research in this direction.
匹配关键词: reward model
---

[ACADEMIC - ARXIV]
标题: Representational Harms in LLM-Generated Narratives Against Global Majority Nationalities
作者: Ilana Nguyen, Harini Suresh, Thema Monroe-White, Evan Shieh
链接: https://arxiv.org/abs/2604.22749v1
完整摘要: Large language models (LLMs) are increasingly used for text generation tasks from everyday use to high-stakes enterprise and government applications, including simulated interviews with asylum seekers. While many works highlight the new potential applications of LLMs, there are risks of LLMs encoding and perpetuating harmful biases about non-dominant communities across the globe. To better evaluate and mitigate such harms, more research examining how LLMs portray diverse individuals is needed. In this work, we study how national origin identities are portrayed by widely-adopted LLMs in response to open-ended narrative generation prompts. Our findings demonstrate the presence of persistent representational harms by national origin, including harmful stereotypes, erasure, and one-dimensional portrayals of Global Majority identities. Minoritized national identities are simultaneously underrepresented in power-neutral stories and overrepresented in subordinated character portrayals, which are over fifty times more likely to appear than dominant portrayals. The degree of harm is amplified when US nationality cues (e.g., ``American'') are present in input prompts. Notably, we find that the harms we identify cannot be explained away via sycophancy, as US-centric biases persist even when replacing US nationality cues with non-US national identities in the prompts. Based on our findings, we call for further exploration of cultural harms in LLMs through methodologies that center Global Majority perspectives and challenge the uncritical adoption of US-based LLMs for the classification, surveillance, and misrepresentation of the majority of our planet.
匹配关键词: reward model
---

[ACADEMIC - ARXIV]
标题: Agentic World Modeling: Foundations, Capabilities, Laws, and Beyond
作者: Meng Chu, Xuan Billy Zhang, Kevin Qinghong Lin, Lingdong Kong, Jize Zhang, Teng Tu, Weijian Ma, Ziqi Huang, Senqiao Yang, Wei Huang, Yeying Jin, Zhefan Rao, Jinhui Ye, Xinyu Lin, Xichen Zhang, Qisheng Hu, Shuai Yang, Leyang Shen, Wei Chow, Yifei Dong, Fengyi Wu, Quanyu Long, Bin Xia, Shaozuo Yu, Mingkang Zhu, Wenhu Zhang, Jiehui Huang, Haokun Gui, Haoxuan Che, Long Chen, Qifeng Chen, Wenxuan Zhang, Wenya Wang, Xiaojuan Qi, Yang Deng, Yanwei Li, Mike Zheng Shou, Zhi-Qi Cheng, See-Kiong Ng, Ziwei Liu, Philip Torr, Jiaya Jia
链接: https://arxiv.org/abs/2604.22748v1
完整摘要: As AI systems move from generating text to accomplishing goals through sustained interaction, the ability to model environment dynamics becomes a central bottleneck. Agents that manipulate objects, navigate software, coordinate with others, or design experiments require predictive environment models, yet the term world model carries different meanings across research communities. We introduce a "levels x laws" taxonomy organized along two axes. The first defines three capability levels: L1 Predictor, which learns one-step local transition operators; L2 Simulator, which composes them into multi-step, action-conditioned rollouts that respect domain laws; and L3 Evolver, which autonomously revises its own model when predictions fail against new evidence. The second identifies four governing-law regimes: physical, digital, social, and scientific. These regimes determine what constraints a world model must satisfy and where it is most likely to fail. Using this framework, we synthesize over 400 works and summarize more than 100 representative systems spanning model-based reinforcement learning, video generation, web and GUI agents, multi-agent social simulation, and AI-driven scientific discovery. We analyze methods, failure modes, and evaluation practices across level-regime pairs, propose decision-centric evaluation principles and a minimal reproducible evaluation package, and outline architectural guidance, open problems, and governance challenges. The resulting roadmap connects previously isolated communities and charts a path from passive next-step prediction toward world models that can simulate, and ultimately reshape, the environments in which agents operate.
匹配关键词: reward model
---

[ACADEMIC - ARXIV]
标题: Relaxation-Informed Training of Neural Network Surrogate Models
作者: Calvin Tsay
链接: https://arxiv.org/abs/2604.22746v1
完整摘要: ReLU neural networks trained as surrogate models can be embedded exactly in mixed-integer linear programs (MILPs), enabling global optimization over the learned function. The tractability of the resulting MILP depends on structural properties of the network, i.e., the number of binary variables in associated formulations and the tightness of the continuous LP relaxation. These properties are determined during training, yet standard training objectives (prediction loss with classical weight regularization) offer no mechanism to directly control them. This work studies training regularizers that directly target downstream MILP tractability. Specifically, we propose simple bound-based regularizers that penalize the big-M constants of MILP formulations and/or the number of unstable neurons. Moreover, we introduce an LP relaxation gap regularizer that explicitly penalizes the per-sample gap of the continuous relaxation at training points. We derive its associated gradient and provide an implementation from LP dual variables without custom automatic differentiation tools. We show that combining the above regularizers can approximate the full total derivative of the LP gap with respect to the network parameters, capturing both direct and indirect sensitivities. Experiments on non-convex benchmark functions and a two-stage stochastic programming problem with quantile neural network surrogates demonstrate that the proposed regularizers can reduce MILP solve times by up to four orders of magnitude relative to an unregularized baseline, while maintaining competitive surrogate model accuracy.
匹配关键词: reward model
---

[ACADEMIC - ARXIV]
标题: Inter-Stance: A Dyadic Multimodal Corpus for Conversational Stance Analysis
作者: Xiang Zhang, Xiaotian Li, Taoyue Wang, Nan Bi, Xin Zhou, Cody Zhou, Zoie Wang, Andrew Yang, Yuming Su, Jeff Cohn, Qiang Ji, Lijun Yin
链接: https://arxiv.org/abs/2604.22739v1
完整摘要: Social interactions dominate our perceptions of the world and shape our daily behavior by attaching social meaning to acts as simple and spontaneous as gestures, facial expressions, voice, and speech. People mimic and otherwise respond to each other's postures, facial expressions, mannerisms, and other verbal and nonverbal behavior, and form appraisals or evaluations in the process. Yet, no publicly-available dataset includes multimodal recordings and self-report measures of multiple persons in social interaction. Dyadic recordings and annotation are lacking. We present a new data corpus of multimodal dyadic interaction (45 dyads, 90 persons) that includes synchronized multi-modality behavior (2D face video, 3D face geometry, thermal spectrum dynamics, voice and speech behavior, physiology (PPG, EDA, heart-rate, blood pressure, and respiration), and self-reported affect of all participants in a communicative interaction scenario. Two types of dyads are included: persons with shared past history and strangers. Annotations include social signals, agreement, disagreement, and neutral stance. With a potent emotion induction, these multimodal data will enable novel modeling of multimodal interpersonal behavior. We present extensive experiments to evaluate multimodal dyadic communication of dyads with and without interpersonal history, and their affect. This new database will make multimodal modeling of social interaction never possible before. The dataset includes 20TB of multimodal data to share with the research community.
匹配关键词: reward model
---

[ACADEMIC - ARXIV]
标题: Relaxation-Informed Training of Neural Network Surrogate Models
作者: Calvin Tsay
链接: https://arxiv.org/abs/2604.22746v1
完整摘要: ReLU neural networks trained as surrogate models can be embedded exactly in mixed-integer linear programs (MILPs), enabling global optimization over the learned function. The tractability of the resulting MILP depends on structural properties of the network, i.e., the number of binary variables in associated formulations and the tightness of the continuous LP relaxation. These properties are determined during training, yet standard training objectives (prediction loss with classical weight regularization) offer no mechanism to directly control them. This work studies training regularizers that directly target downstream MILP tractability. Specifically, we propose simple bound-based regularizers that penalize the big-M constants of MILP formulations and/or the number of unstable neurons. Moreover, we introduce an LP relaxation gap regularizer that explicitly penalizes the per-sample gap of the continuous relaxation at training points. We derive its associated gradient and provide an implementation from LP dual variables without custom automatic differentiation tools. We show that combining the above regularizers can approximate the full total derivative of the LP gap with respect to the network parameters, capturing both direct and indirect sensitivities. Experiments on non-convex benchmark functions and a two-stage stochastic programming problem with quantile neural network surrogates demonstrate that the proposed regularizers can reduce MILP solve times by up to four orders of magnitude relative to an unregularized baseline, while maintaining competitive surrogate model accuracy.
匹配关键词: preference optimization
---

[ACADEMIC - ARXIV]
标题: GCImOpt: Learning efficient goal-conditioned policies by imitating optimal trajectories
作者: Jon Goikoetxea, Jesús F. Palacián
链接: https://arxiv.org/abs/2604.22724v1
完整摘要: Imitation learning is a well-established approach for machine-learning-based control. However, its applicability depends on having access to demonstrations, which are often expensive to collect and/or suboptimal for solving the task. In this work, we present GCImOpt, an approach to learn efficient goal-conditioned policies by training on datasets generated by trajectory optimization. Our approach for dataset generation is computationally efficient, can generate thousands of optimal trajectories in minutes on a laptop computer, and produces high-quality demonstrations. Further, by means of a data augmentation scheme that treats intermediate states as goals, we are able to increase the training dataset size by an order of magnitude. Using our generated datasets, we train goal-conditioned neural network policies that can control the system towards arbitrary goals. To demonstrate the generality of our approach, we generate datasets and then train policies for various control tasks, namely cart-pole stabilization, planar and three-dimensional quadcopter stabilization, and point reaching using a 6-DoF robot arm. We show that our trained policies can achieve high success rates and near-optimal control profiles, all while being small (less than 80,000 neural network parameters) and fast enough (up to more than 6,000 times faster than a trajectory optimization solver) that they could be deployed onboard resource-constrained controllers. We provide videos, code, datasets and pre-trained policies under a free software license; see our project website https://jongoiko.github.io/gcimopt/.
匹配关键词: preference optimization
---

[ACADEMIC - ARXIV]
标题: ATRS: Adaptive Trajectory Re-splitting via a Shared Neural Policy for Parallel Optimization
作者: Jiajun Yu, Guodong Liu, Li Wang, Pengxiang Zhou, Wentao Liu, Yin He, Chao Xu, Fei Gao, Yanjun Cao
链接: https://arxiv.org/abs/2604.22715v1
完整摘要: Parallel trajectory optimization via the Alternating Direction Method of Multipliers (ADMM) has emerged as a scalable approach to long-horizon motion planning. However, existing frameworks typically decompose the problem into parallel subproblems based on a predefined fixed structure. Such structural rigidity often causes optimization stagnation in highly constrained regions, where a few lagging subproblems delay global convergence. A natural remedy is to adaptively re-split these stagnating segments online. Yet, deciding when, where, and how to split exceeds the capability of rule-based heuristics. To this end, we propose ATRS, a novel framework that embeds a shared Deep Reinforcement Learning policy into the parallel ADMM loop. We formulate this adaptive adjustment as a Multi-Agent Shared-Policy Markov Decision Process, where all trajectory segments act as homogeneous agents and share a unified neural policy network. This parameter-sharing architecture endows the system with size invariance, enabling it to handle dynamically changing segment counts during re-splitting and generalize to arbitrary trajectory lengths. Furthermore, our formulation inherently supports zero-shot generalization to unseen environments, as our network relies solely on the internal states of the numerical solver rather than on the geometric features of the environment. To ensure solver stability, a Confidence-Based Election mechanism selects only the most stagnating segment for re-splitting at each step. Extensive simulations demonstrate that ATRS accelerates convergence, reducing the number of iterations by up to 26.0% and the computation time by up to 19.1%. Real-world experiments further confirm its applicability to both large-scale offline global planning and real-time onboard replanning within 35 ms per cycle, with no sim-to-real degradation.
匹配关键词: preference optimization
---

[ACADEMIC - ARXIV]
标题: Thinking Without Words: Efficient Latent Reasoning with Abstract Chain-of-Thought
作者: Keshav Ramji, Tahira Naseem, Ramón Fernandez Astudillo
链接: https://arxiv.org/abs/2604.22709v1
完整摘要: While long, explicit chains-of-thought (CoT) have proven effective on complex reasoning tasks, they are costly to generate during inference. Non-verbal reasoning methods have emerged with shorter generation lengths by leveraging continuous representations, yet their performance lags behind verbalized CoT. We propose $\textbf{Abstract Chain-of-Thought}$, a discrete latent reasoning post-training mechanism in which the language model produces a short sequence of tokens from a reserved vocabulary in lieu of a natural language CoT, before generating a response. To make previously unseen ''abstract'' tokens useful, we introduce a policy iteration-style warm-up loop that alternates between (i.) bottlenecking from a verbal CoT via masking and performing supervised fine-tuning, and (ii.) self-distillation by training the model to generate abstract tokens from the prompt alone via constrained decoding with the codebook. After warm-up, we optimize the generation of abstract sequences with warm-started reinforcement learning under constrained decoding. Abstract-CoT achieves up to $11.6\times$ fewer reasoning tokens while demonstrating comparable performance across mathematical reasoning, instruction-following, and multi-hop reasoning, and generalizes across language model families. We also find an emergent power law distribution over the abstract vocabulary, akin to those seen in natural language, that evolves across the training phases. Our findings highlight the potential for post-training latent reasoning mechanisms that enable efficient inference through a learned abstract reasoning language.
匹配关键词: preference optimization
---

[ACADEMIC - ARXIV]
标题: Time-Localized Parametric Decomposition of Respiratory Airflow for Sub-Breath Analysis
作者: Victoria Ribeiro Rodrigues, Paul W. Davenport, Nicholas J. Napoli
链接: https://arxiv.org/abs/2604.22695v1
完整摘要: Respiratory airflow signals provide critical insight into breathing mechanics, yet conventional analysis methods remain limited in their ability to characterize the internal structure of individual breaths. Traditional approaches treat airflow as a quasi-periodic signal and rely on global descriptors such as tidal volume or peak flow, obscuring sub-breath events that reflect neuromuscular coordination and compensatory breathing strategies. This study introduces a parametric framework for decomposing inspiratory airflow into a small number of time-localized components with explicit amplitude, onset time, and duration parameters. Unlike spectral or data-adaptive methods, the proposed approach employs physiologically grounded basis functions, Half-Sine, Gaussian, and Beta, to represent intrabreath waveform morphology through constrained nonlinear optimization. Evaluation across 8,276 breaths demonstrates high reconstruction accuracy (mean squared error $<$ 0.001 for four-component models) and robust parameter precision under moderate noise. Component-derived features describing sub-breath timing and coordination improved classification of cognitive fatigue states arising from cognitive-respiratory competition by up to 30.7% in Matthews correlation coefficient compared with classical respiratory metrics. These results establish that modeling airflow as a sum of parameterized, time-localized primitives provides an interpretable and precise foundation for quantifying intrabreath organization, compensatory breathing dynamics, and respiratory motor control adaptation under cognitive-respiratory dual-task demands.
匹配关键词: preference optimization
---

[ACADEMIC - ARXIV]
标题: How Do AI Agents Spend Your Money? Analyzing and Predicting Token Consumption in Agentic Coding Tasks
作者: Longju Bai, Zhemin Huang, Xingyao Wang, Jiao Sun, Rada Mihalcea, Erik Brynjolfsson, Alex Pentland, Jiaxin Pei
链接: https://arxiv.org/abs/2604.22750v1
完整摘要: The wide adoption of AI agents in complex human workflows is driving rapid growth in LLM token consumption. When agents are deployed on tasks that require a significant amount of tokens, three questions naturally arise: (1) Where do AI agents spend the tokens? (2) Which models are more token-efficient? and (3) Can agents predict their token usage before task execution? In this paper, we present the first systematic study of token consumption patterns in agentic coding tasks. We analyze trajectories from eight frontier LLMs on SWE-bench Verified and evaluate models' ability to predict their own token costs before task execution. We find that: (1) agentic tasks are uniquely expensive, consuming 1000x more tokens than code reasoning and code chat, with input tokens rather than output tokens driving the overall cost; (2) token usage is highly variable and inherently stochastic: runs on the same task can differ by up to 30x in total tokens, and higher token usage does not translate into higher accuracy; instead, accuracy often peaks at intermediate cost and saturates at higher costs; (3) models vary substantially in token efficiency: on the same tasks, Kimi-K2 and Claude-Sonnet-4.5, on average, consume over 1.5 million more tokens than GPT-5; (4) task difficulty rated by human experts only weakly aligns with actual token costs, revealing a fundamental gap between human-perceived complexity and the computational effort agents actually expend; and (5) frontier models fail to accurately predict their own token usage (with weak-to-moderate correlations, up to 0.39) and systematically underestimate real token costs. Our study offers new insights into the economics of AI agents and can inspire future research in this direction.
匹配关键词: constitutional AI
---

[ACADEMIC - ARXIV]
标题: Agentic World Modeling: Foundations, Capabilities, Laws, and Beyond
作者: Meng Chu, Xuan Billy Zhang, Kevin Qinghong Lin, Lingdong Kong, Jize Zhang, Teng Tu, Weijian Ma, Ziqi Huang, Senqiao Yang, Wei Huang, Yeying Jin, Zhefan Rao, Jinhui Ye, Xinyu Lin, Xichen Zhang, Qisheng Hu, Shuai Yang, Leyang Shen, Wei Chow, Yifei Dong, Fengyi Wu, Quanyu Long, Bin Xia, Shaozuo Yu, Mingkang Zhu, Wenhu Zhang, Jiehui Huang, Haokun Gui, Haoxuan Che, Long Chen, Qifeng Chen, Wenxuan Zhang, Wenya Wang, Xiaojuan Qi, Yang Deng, Yanwei Li, Mike Zheng Shou, Zhi-Qi Cheng, See-Kiong Ng, Ziwei Liu, Philip Torr, Jiaya Jia
链接: https://arxiv.org/abs/2604.22748v1
完整摘要: As AI systems move from generating text to accomplishing goals through sustained interaction, the ability to model environment dynamics becomes a central bottleneck. Agents that manipulate objects, navigate software, coordinate with others, or design experiments require predictive environment models, yet the term world model carries different meanings across research communities. We introduce a "levels x laws" taxonomy organized along two axes. The first defines three capability levels: L1 Predictor, which learns one-step local transition operators; L2 Simulator, which composes them into multi-step, action-conditioned rollouts that respect domain laws; and L3 Evolver, which autonomously revises its own model when predictions fail against new evidence. The second identifies four governing-law regimes: physical, digital, social, and scientific. These regimes determine what constraints a world model must satisfy and where it is most likely to fail. Using this framework, we synthesize over 400 works and summarize more than 100 representative systems spanning model-based reinforcement learning, video generation, web and GUI agents, multi-agent social simulation, and AI-driven scientific discovery. We analyze methods, failure modes, and evaluation practices across level-regime pairs, propose decision-centric evaluation principles and a minimal reproducible evaluation package, and outline architectural guidance, open problems, and governance challenges. The resulting roadmap connects previously isolated communities and charts a path from passive next-step prediction toward world models that can simulate, and ultimately reshape, the environments in which agents operate.
匹配关键词: constitutional AI
---

[ACADEMIC - ARXIV]
标题: Generative Modeling of Neurodegenerative Brain Anatomy with 4D Longitudinal Diffusion Model
作者: Nivetha Jayakumar, Swakshar Deb, Bahram Jafrasteh, Qingyu Zhao, Miaomiao Zhang
链接: https://arxiv.org/abs/2604.22700v1
完整摘要: Understanding and predicting the progression of neurodegenerative diseases remains a major challenge in medical AI, with significant implications for early diagnosis, disease monitoring, and treatment planning. However, most available longitudinal neuroimaging datasets are temporally sparse with a few follow-up scans per subject. This scarcity of temporal data limits our ability to model and accurately capture the continuous anatomical changes related to disease progression in individual subjects. To address this problem, we propose a novel 4D (3DxT) diffusion-based generative framework that effectively models and synthesizes longitudinal brain anatomy over time, conditioned on available clinical variables such as health status, age, sex, and other relevant factors. Moreover, while most current approaches focus on manipulating image intensity or texture, our method explicitly learns the data distribution of topology-preserving spatiotemporal deformations to effectively capture the geometric changes of brain structures over time. This design enables the realistic generation of future anatomical states and the reconstruction of anatomically consistent disease trajectories, providing a more faithful representation of longitudinal brain changes. We validate our model through both synthetic sequence generation and downstream longitudinal disease classification, as well as brain segmentation. Experiments on two large-scale longitudinal neuroimage datasets demonstrate that our method outperforms state-of-the-art baselines in generating anatomically accurate, temporally consistent, and clinically meaningful brain trajectories. Our code is available on Github.
匹配关键词: constitutional AI
---

[ACADEMIC - ARXIV]
标题: How Supply Chain Dependencies Complicate Bias Measurement and Accountability Attribution in AI Hiring Applications
作者: Gauri Sharma, Maryam Molamohammadi
链接: https://arxiv.org/abs/2604.22679v1
完整摘要: The increasing adoption of AI systems in hiring has raised concerns about algorithmic bias and accountability, prompting regulatory responses including the EU AI Act, NYC Local Law 144, and Colorado's AI Act. While existing research examines bias through technical or regulatory lenses, both perspectives overlook a fundamental challenge: modern AI hiring systems operate within complex supply chains where responsibility fragments across data vendors, model developers, platform providers, and deploying organizations. This paper investigates how these dependency chains complicate bias evaluation and accountability attribution. Drawing on literature review and regulatory analysis, we demonstrate that fragmented responsibilities create two critical problems. First, bias emerges from component interactions rather than isolated elements, yet proprietary configurations prevent integrated evaluation. A resume parser may function without bias independently but contribute to discrimination when integrated with specific ranking algorithms and filtering thresholds. Second, information asymmetries mean deploying organizations bear legal responsibility without technical visibility into vendor-supplied algorithms, while vendors control implementations without meaningful disclosure requirements. Each stakeholder may believe they are compliant; nevertheless, the integrated system may produce biased outcomes. Analysis of implementation ambiguities reveals these challenges in practice. We propose multi-layered interventions including system-level audits, vendor guidelines, continuous monitoring mechanisms, and documentation across dependency chains. Our findings reveal that effective governance requires coordinated action across technical, organizational, and regulatory domains to establish meaningful accountability in distributed development environments.
匹配关键词: constitutional AI
---

[ACADEMIC - ARXIV]
标题: Rethinking XAI Evaluation: A Human-Centered Audit of Shapley Benchmarks in High-Stakes Settings
作者: Inês Oliveira e Silva, Sérgio Jesus, Iker Perez, Rita P. Ribeiro, Carlos Soares, Hugo Ferreira, Pedro Bizarro
链接: https://arxiv.org/abs/2604.22662v1
完整摘要: Shapley values are a cornerstone of explainable AI, yet their proliferation into competing formulations has created a fragmented landscape with little consensus on practical deployment. While theoretical differences are well-documented, evaluation remains reliant on quantitative proxies whose alignment with human utility is unverified. In this work, we use a unified amortized framework to isolate semantic differences between eight Shapley variants under the low-latency constraints of operational risk workflows. We conduct a large-scale empirical evaluation across four risk datasets and a realistic fraud-detection environment involving professional analysts and 3,735 case reviews. Our results reveal a fundamental misalignment: standard quantitative metrics, such as sparsity and faithfulness, are decoupled from human-perceived clarity and decision utility. Furthermore, while no formulation improved objective analyst performance, explanations consistently increased decision confidence, signaling a critical risk of automation bias in high-stakes settings. These findings suggest that current evaluation proxies are insufficient for predicting downstream human impact, and we provide evidence-based guidance for selecting formulations and metrics in operational decision systems.
匹配关键词: constitutional AI
---

[ACADEMIC - ARXIV]
标题: How Do AI Agents Spend Your Money? Analyzing and Predicting Token Consumption in Agentic Coding Tasks
作者: Longju Bai, Zhemin Huang, Xingyao Wang, Jiao Sun, Rada Mihalcea, Erik Brynjolfsson, Alex Pentland, Jiaxin Pei
链接: https://arxiv.org/abs/2604.22750v1
完整摘要: The wide adoption of AI agents in complex human workflows is driving rapid growth in LLM token consumption. When agents are deployed on tasks that require a significant amount of tokens, three questions naturally arise: (1) Where do AI agents spend the tokens? (2) Which models are more token-efficient? and (3) Can agents predict their token usage before task execution? In this paper, we present the first systematic study of token consumption patterns in agentic coding tasks. We analyze trajectories from eight frontier LLMs on SWE-bench Verified and evaluate models' ability to predict their own token costs before task execution. We find that: (1) agentic tasks are uniquely expensive, consuming 1000x more tokens than code reasoning and code chat, with input tokens rather than output tokens driving the overall cost; (2) token usage is highly variable and inherently stochastic: runs on the same task can differ by up to 30x in total tokens, and higher token usage does not translate into higher accuracy; instead, accuracy often peaks at intermediate cost and saturates at higher costs; (3) models vary substantially in token efficiency: on the same tasks, Kimi-K2 and Claude-Sonnet-4.5, on average, consume over 1.5 million more tokens than GPT-5; (4) task difficulty rated by human experts only weakly aligns with actual token costs, revealing a fundamental gap between human-perceived complexity and the computational effort agents actually expend; and (5) frontier models fail to accurately predict their own token usage (with weak-to-moderate correlations, up to 0.39) and systematically underestimate real token costs. Our study offers new insights into the economics of AI agents and can inspire future research in this direction.
匹配关键词: reasoning
---

[ACADEMIC - ARXIV]
标题: Thinking Without Words: Efficient Latent Reasoning with Abstract Chain-of-Thought
作者: Keshav Ramji, Tahira Naseem, Ramón Fernandez Astudillo
链接: https://arxiv.org/abs/2604.22709v1
完整摘要: While long, explicit chains-of-thought (CoT) have proven effective on complex reasoning tasks, they are costly to generate during inference. Non-verbal reasoning methods have emerged with shorter generation lengths by leveraging continuous representations, yet their performance lags behind verbalized CoT. We propose $\textbf{Abstract Chain-of-Thought}$, a discrete latent reasoning post-training mechanism in which the language model produces a short sequence of tokens from a reserved vocabulary in lieu of a natural language CoT, before generating a response. To make previously unseen ''abstract'' tokens useful, we introduce a policy iteration-style warm-up loop that alternates between (i.) bottlenecking from a verbal CoT via masking and performing supervised fine-tuning, and (ii.) self-distillation by training the model to generate abstract tokens from the prompt alone via constrained decoding with the codebook. After warm-up, we optimize the generation of abstract sequences with warm-started reinforcement learning under constrained decoding. Abstract-CoT achieves up to $11.6\times$ fewer reasoning tokens while demonstrating comparable performance across mathematical reasoning, instruction-following, and multi-hop reasoning, and generalizes across language model families. We also find an emergent power law distribution over the abstract vocabulary, akin to those seen in natural language, that evolves across the training phases. Our findings highlight the potential for post-training latent reasoning mechanisms that enable efficient inference through a learned abstract reasoning language.
匹配关键词: reasoning
---

[ACADEMIC - ARXIV]
标题: BERAG: Bayesian Ensemble Retrieval-Augmented Generation for Knowledge-based Visual Question Answering
作者: Jinghong Chen, Jingbiao Mei, Guangyu Yang, Bill Byrne
链接: https://arxiv.org/abs/2604.22678v1
完整摘要: A common approach to question answering with retrieval-augmented generation (RAG) is to concatenate documents into a single context and pass it to a language model to generate an answer. While simple, this strategy can obscure the contribution of individual documents, making attribution difficult and contributing to the ``lost-in-the-middle'' effect, where relevant information in long contexts is overlooked. Concatenation also scales poorly: computational cost grows quadratically with context length, a problem that becomes especially severe when the context includes visual data, as in visual question answering. Attempts to mitigate these issues by limiting context length can further restrict performance by preventing models from benefiting from the improved recall offered by deeper retrieval. We propose Bayesian Ensemble Retrieval-Augmented Generation (BERAG), along with Bayesian Ensemble Fine-Tuning (BEFT), as a RAG framework in which language models are conditioned on individual retrieved documents rather than a single combined context. BERAG treats document posterior probabilities as ensemble weights and updates them token by token using Bayes' rule during generation. This approach enables probabilistic re-ranking, parallel memory usage, and clear attribution of document contribution, making it well-suited for large document collections. We evaluate BERAG and BEFT primarily on knowledge-based visual question answering tasks, where models must reason over long, imperfect retrieval lists. The results show substantial improvements over standard RAG, including strong gains on Document Visual Question Answering and multimodal needle-in-a-haystack benchmarks. We also demonstrate that BERAG mitigates the ``lost-in-the-middle'' effect. The document posterior can be used to detect insufficient grounding and trigger deflection, while document pruning enables faster decoding than standard RAG.
匹配关键词: reasoning
---

[ACADEMIC - ARXIV]
标题: GazeVLA: Learning Human Intention for Robotic Manipulation
作者: Chengyang Li, Kaiyi Xiong, Yuan Xu, Lei Qian, Yizhou Wang, Wentao Zhu
链接: https://arxiv.org/abs/2604.22615v1
完整摘要: Embodied foundation models have achieved significant breakthroughs in robotic manipulation, yet they still depend heavily on large-scale robot demonstrations. Although recent works have explored leveraging human data to alleviate this dependency, effectively extracting transferable knowledge remains a significant challenge due to the inherent embodiment gap between human and robot. We argue that the intention underlying human actions can serve as a powerful intermediate representation for bridging this gap. In this paper, we introduce a novel framework that explicitly learns and transfers human intention to facilitate robotic manipulation. Specifically, we model intention through gaze, as it naturally precedes physical actions and serves as an observable proxy for human intent. Our model is first pretrained on a large-scale egocentric human dataset to capture human intention and its synergy with action, followed by finetuning on a small set of robot and human data. During inference, the model adopts a Chain-of-Thought reasoning paradigm, sequentially predicting intention before executing the action. Extensive evaluations in simulation and real-world settings, across long-horizon and fine-grained tasks, and under few-shot and robustness benchmarks, show that our method consistently outperforms strong baselines, generalizes better, and achieves state-of-the-art performance.
匹配关键词: reasoning
---

[ACADEMIC - ARXIV]
标题: Rethinking Math Reasoning Evaluation: A Robust LLM-as-a-Judge Framework Beyond Symbolic Rigidity
作者: Erez Yosef, Oron Anschel, Shunit Haviv Hakimi, Asaf Gendler, Adam Botach, Nimrod Berman, Igor Kviatkovsky
链接: https://arxiv.org/abs/2604.22597v1
完整摘要: Recent advancements in large language models have led to significant improvements across various tasks, including mathematical reasoning, which is used to assess models' intelligence in logical reasoning and problem-solving. Models are evaluated on mathematical reasoning benchmarks by verifying the correctness of the final answer against a ground truth answer. A common approach for this verification is based on symbolic mathematics comparison, which fails to generalize across diverse mathematical representations and solution formats. In this work, we offer a robust and flexible alternative to rule-based symbolic mathematics comparison. We propose an LLM-based evaluation framework for evaluating model-generated answers, enabling accurate evaluation across diverse mathematical representations and answer formats. We present failure cases of symbolic evaluation in two popular frameworks, Lighteval and SimpleRL, and compare them to our approach, demonstrating clear improvements over commonly used methods. Our framework enables more reliable evaluation and benchmarking, leading to more accurate performance monitoring, which is important for advancing mathematical problem-solving and intelligent systems.
匹配关键词: reasoning
---

[ACADEMIC - ARXIV]
标题: Thinking Without Words: Efficient Latent Reasoning with Abstract Chain-of-Thought
作者: Keshav Ramji, Tahira Naseem, Ramón Fernandez Astudillo
链接: https://arxiv.org/abs/2604.22709v1
完整摘要: While long, explicit chains-of-thought (CoT) have proven effective on complex reasoning tasks, they are costly to generate during inference. Non-verbal reasoning methods have emerged with shorter generation lengths by leveraging continuous representations, yet their performance lags behind verbalized CoT. We propose $\textbf{Abstract Chain-of-Thought}$, a discrete latent reasoning post-training mechanism in which the language model produces a short sequence of tokens from a reserved vocabulary in lieu of a natural language CoT, before generating a response. To make previously unseen ''abstract'' tokens useful, we introduce a policy iteration-style warm-up loop that alternates between (i.) bottlenecking from a verbal CoT via masking and performing supervised fine-tuning, and (ii.) self-distillation by training the model to generate abstract tokens from the prompt alone via constrained decoding with the codebook. After warm-up, we optimize the generation of abstract sequences with warm-started reinforcement learning under constrained decoding. Abstract-CoT achieves up to $11.6\times$ fewer reasoning tokens while demonstrating comparable performance across mathematical reasoning, instruction-following, and multi-hop reasoning, and generalizes across language model families. We also find an emergent power law distribution over the abstract vocabulary, akin to those seen in natural language, that evolves across the training phases. Our findings highlight the potential for post-training latent reasoning mechanisms that enable efficient inference through a learned abstract reasoning language.
匹配关键词: chain-of-thought
---

[ACADEMIC - ARXIV]
标题: GazeVLA: Learning Human Intention for Robotic Manipulation
作者: Chengyang Li, Kaiyi Xiong, Yuan Xu, Lei Qian, Yizhou Wang, Wentao Zhu
链接: https://arxiv.org/abs/2604.22615v1
完整摘要: Embodied foundation models have achieved significant breakthroughs in robotic manipulation, yet they still depend heavily on large-scale robot demonstrations. Although recent works have explored leveraging human data to alleviate this dependency, effectively extracting transferable knowledge remains a significant challenge due to the inherent embodiment gap between human and robot. We argue that the intention underlying human actions can serve as a powerful intermediate representation for bridging this gap. In this paper, we introduce a novel framework that explicitly learns and transfers human intention to facilitate robotic manipulation. Specifically, we model intention through gaze, as it naturally precedes physical actions and serves as an observable proxy for human intent. Our model is first pretrained on a large-scale egocentric human dataset to capture human intention and its synergy with action, followed by finetuning on a small set of robot and human data. During inference, the model adopts a Chain-of-Thought reasoning paradigm, sequentially predicting intention before executing the action. Extensive evaluations in simulation and real-world settings, across long-horizon and fine-grained tasks, and under few-shot and robustness benchmarks, show that our method consistently outperforms strong baselines, generalizes better, and achieves state-of-the-art performance.
匹配关键词: chain-of-thought
---

[ACADEMIC - ARXIV]
标题: CGC: Compositional Grounded Contrast for Fine-Grained Multi-Image Understanding
作者: Lihao Zheng, Zhenwei Shao, Yu Zhou, Yan Yang, Xintian Shen, Jiawei Chen, Hao Ma, Tao Wei
链接: https://arxiv.org/abs/2604.22498v1
完整摘要: Although Multimodal Large Language Models (MLLMs) have advanced rapidly, they still face notable challenges in fine-grained multi-image understanding, often exhibiting spatial hallucination, attention leakage, and failures in object constancy. In addition, existing approaches typically rely on expensive human annotations or large-scale chain-of-thought (CoT) data generation. We propose Compositional Grounded Contrast (abbr. CGC), a low-cost full framework for boosting fine-grained multi-image understanding of MLLMs. Built on existing single-image grounding annotations, CGC constructs compositional multi-image training instances through Inter-Image Contrast and Intra-Image Contrast, which introduce semantically decoupled distractor contexts for cross-image discrimination and correlated cross-view samples for object constancy, respectively. CGC further introduces a Rule-Based Spatial Reward within the GRPO framework to improve source-image attribution, spatial alignment, and structured output validity under a Think-before-Grounding paradigm. Experiments show that CGC achieves state-of-the-art results on fine-grained multi-image benchmarks, including MIG-Bench and VLM2-Bench. The learned multi-image understanding capability also transfers to broader multimodal understanding and reasoning tasks, yielding consistent gains over the Qwen3-VL-8B base model on MathVista (+2.90), MuirBench (+2.88), MMStar (+1.93), MMMU (+1.77), and BLINK (+1.69).
匹配关键词: chain-of-thought
---

[ACADEMIC - ARXIV]
标题: Beyond Chain-of-Thought: Rewrite as a Universal Interface for Generative Multimodal Embeddings
作者: Peixi Wu, Ke Mei, Feipeng Ma, Bosong Chai, Zhibin Lan, Chenxi Zhao, Shannan Yan, Jie Chen, Zhangchi Hu, Yansong Peng, Bo Lin, Junjie Zhou, Dacheng Yin, Tianyi Wang, Fengyun Rao, Jing Lyu, Hebei Li, Xiaoyan Sun
链接: https://arxiv.org/abs/2604.22280v1
完整摘要: Multimodal Large Language Models (MLLMs) have emerged as a promising foundation for universal multimodal embeddings. Recent studies have shown that reasoning-driven generative multimodal embeddings can outperform discriminative embeddings on several embedding tasks. However, Chain-of-Thought (CoT) reasoning tends to generate redundant thinking steps and introduce semantic ambiguity in the summarized answers in broader retrieval scenarios. To address this limitation, we propose Rewrite-driven Multimodal Embedding (RIME), a unified framework that jointly optimizes generation and embedding through a retrieval-friendly rewrite. Meanwhile, we present the Cross-Mode Alignment (CMA) to bridge the generative and discriminative embedding spaces, enabling flexible mutual retrieval to trade off efficiency and accuracy. Based on this, we also introduce Refine Reinforcement Learning (Refine-RL) that treats discriminative embeddings as stable semantic anchors to guide the rewrite optimization. Extensive experiments on MMEB-V2, MRMR and UVRB demonstrate that RIME substantially outperforms prior generative embedding models while significantly reducing the length of thinking.
匹配关键词: chain-of-thought
---

[ACADEMIC - ARXIV]
标题: Large Language Models Decide Early and Explain Later
作者: Ayan Datta, Zhixue Zhao, Bhuvanesh Verma, Radhika Mamidi, Mounika Marreddy, Alexander Mehler
链接: https://arxiv.org/abs/2604.22266v1
完整摘要: Large Language Models often achieve strong performance by generating long intermediate chain-of-thought reasoning. However, it remains unclear when a model's final answer is actually determined during generation. If the answer is already fixed at an intermediate stage, subsequent reasoning tokens may constitute post-decision explanation, increasing inference cost and latency without improving correctness. We study the evolution of predicted answers over reasoning steps using forced answer completion, which elicits the model's intermediate predictions at partial reasoning prefixes. Focusing on Qwen3-4B and averaging results across all datasets considered, we find that predicted answers change in only 32% of queries. Moreover, once the final answer switch occurs, the model generates an average of 760 additional reasoning tokens per query, accounting for a substantial fraction of the total reasoning budget. Motivated by these findings, we investigate early stopping strategies that halt generation once the answer has stabilized. We show that simple heuristics, including probe-based stopping, can reduce reasoning token usage by 500 tokens per query while incurring only a 2% drop in accuracy. Together, our results indicate that a large portion of chain-of-thought generation is redundant and can be reduced with minimal impact on performance.
匹配关键词: chain-of-thought
---

[ACADEMIC - ARXIV]
标题: How Do AI Agents Spend Your Money? Analyzing and Predicting Token Consumption in Agentic Coding Tasks
作者: Longju Bai, Zhemin Huang, Xingyao Wang, Jiao Sun, Rada Mihalcea, Erik Brynjolfsson, Alex Pentland, Jiaxin Pei
链接: https://arxiv.org/abs/2604.22750v1
完整摘要: The wide adoption of AI agents in complex human workflows is driving rapid growth in LLM token consumption. When agents are deployed on tasks that require a significant amount of tokens, three questions naturally arise: (1) Where do AI agents spend the tokens? (2) Which models are more token-efficient? and (3) Can agents predict their token usage before task execution? In this paper, we present the first systematic study of token consumption patterns in agentic coding tasks. We analyze trajectories from eight frontier LLMs on SWE-bench Verified and evaluate models' ability to predict their own token costs before task execution. We find that: (1) agentic tasks are uniquely expensive, consuming 1000x more tokens than code reasoning and code chat, with input tokens rather than output tokens driving the overall cost; (2) token usage is highly variable and inherently stochastic: runs on the same task can differ by up to 30x in total tokens, and higher token usage does not translate into higher accuracy; instead, accuracy often peaks at intermediate cost and saturates at higher costs; (3) models vary substantially in token efficiency: on the same tasks, Kimi-K2 and Claude-Sonnet-4.5, on average, consume over 1.5 million more tokens than GPT-5; (4) task difficulty rated by human experts only weakly aligns with actual token costs, revealing a fundamental gap between human-perceived complexity and the computational effort agents actually expend; and (5) frontier models fail to accurately predict their own token usage (with weak-to-moderate correlations, up to 0.39) and systematically underestimate real token costs. Our study offers new insights into the economics of AI agents and can inspire future research in this direction.
匹配关键词: test-time compute
---

[ACADEMIC - ARXIV]
标题: GCImOpt: Learning efficient goal-conditioned policies by imitating optimal trajectories
作者: Jon Goikoetxea, Jesús F. Palacián
链接: https://arxiv.org/abs/2604.22724v1
完整摘要: Imitation learning is a well-established approach for machine-learning-based control. However, its applicability depends on having access to demonstrations, which are often expensive to collect and/or suboptimal for solving the task. In this work, we present GCImOpt, an approach to learn efficient goal-conditioned policies by training on datasets generated by trajectory optimization. Our approach for dataset generation is computationally efficient, can generate thousands of optimal trajectories in minutes on a laptop computer, and produces high-quality demonstrations. Further, by means of a data augmentation scheme that treats intermediate states as goals, we are able to increase the training dataset size by an order of magnitude. Using our generated datasets, we train goal-conditioned neural network policies that can control the system towards arbitrary goals. To demonstrate the generality of our approach, we generate datasets and then train policies for various control tasks, namely cart-pole stabilization, planar and three-dimensional quadcopter stabilization, and point reaching using a 6-DoF robot arm. We show that our trained policies can achieve high success rates and near-optimal control profiles, all while being small (less than 80,000 neural network parameters) and fast enough (up to more than 6,000 times faster than a trajectory optimization solver) that they could be deployed onboard resource-constrained controllers. We provide videos, code, datasets and pre-trained policies under a free software license; see our project website https://jongoiko.github.io/gcimopt/.
匹配关键词: test-time compute
---

[ACADEMIC - ARXIV]
标题: Aligning Dense Retrievers with LLM Utility via DistillationAligning Dense Retrievers with LLM Utility via Distillation
作者: Rajinder Sandhu, Di Mu, Cheng Chang, Md Shahriar Tasjid, Himanshu Rai, Maksims Volkovs, Ga Wu
链接: https://arxiv.org/abs/2604.22722v1
完整摘要: Dense vector retrieval is the practical backbone of Retrieval- Augmented Generation (RAG), but similarity search can suffer from precision limitations. Conversely, utility-based approaches leveraging LLM re-ranking often achieve superior performance but are computationally prohibitive and prone to noise inherent in perplexity estimation. We propose Utility-Aligned Embeddings (UAE), a framework designed to merge these advantages into a practical, high-performance retrieval method. We formulate retrieval as a distribution matching problem, training a bi-encoder to imitate a utility distribution derived from perplexity reduction using a Utility-Modulated InfoNCE objective. This approach injects graded utility signals directly into the embedding space without requiring test-time LLM inference. On the QASPER benchmark, UAE improves retrieval Recall@1 by 30.59%, MAP by 30.16% and Token F1 by 17.3% over the strong semantic baseline BGE-Base. Crucially, UAE is over 180x faster than the efficient LLM re-ranking methods preserving competitive performance, demonstrating that aligning retrieval with generative utility yields reliable contexts at scale.
匹配关键词: test-time compute
---

[ACADEMIC - ARXIV]
标题: ATRS: Adaptive Trajectory Re-splitting via a Shared Neural Policy for Parallel Optimization
作者: Jiajun Yu, Guodong Liu, Li Wang, Pengxiang Zhou, Wentao Liu, Yin He, Chao Xu, Fei Gao, Yanjun Cao
链接: https://arxiv.org/abs/2604.22715v1
完整摘要: Parallel trajectory optimization via the Alternating Direction Method of Multipliers (ADMM) has emerged as a scalable approach to long-horizon motion planning. However, existing frameworks typically decompose the problem into parallel subproblems based on a predefined fixed structure. Such structural rigidity often causes optimization stagnation in highly constrained regions, where a few lagging subproblems delay global convergence. A natural remedy is to adaptively re-split these stagnating segments online. Yet, deciding when, where, and how to split exceeds the capability of rule-based heuristics. To this end, we propose ATRS, a novel framework that embeds a shared Deep Reinforcement Learning policy into the parallel ADMM loop. We formulate this adaptive adjustment as a Multi-Agent Shared-Policy Markov Decision Process, where all trajectory segments act as homogeneous agents and share a unified neural policy network. This parameter-sharing architecture endows the system with size invariance, enabling it to handle dynamically changing segment counts during re-splitting and generalize to arbitrary trajectory lengths. Furthermore, our formulation inherently supports zero-shot generalization to unseen environments, as our network relies solely on the internal states of the numerical solver rather than on the geometric features of the environment. To ensure solver stability, a Confidence-Based Election mechanism selects only the most stagnating segment for re-splitting at each step. Extensive simulations demonstrate that ATRS accelerates convergence, reducing the number of iterations by up to 26.0% and the computation time by up to 19.1%. Real-world experiments further confirm its applicability to both large-scale offline global planning and real-time onboard replanning within 35 ms per cycle, with no sim-to-real degradation.
匹配关键词: test-time compute
---

[ACADEMIC - ARXIV]
标题: BERAG: Bayesian Ensemble Retrieval-Augmented Generation for Knowledge-based Visual Question Answering
作者: Jinghong Chen, Jingbiao Mei, Guangyu Yang, Bill Byrne
链接: https://arxiv.org/abs/2604.22678v1
完整摘要: A common approach to question answering with retrieval-augmented generation (RAG) is to concatenate documents into a single context and pass it to a language model to generate an answer. While simple, this strategy can obscure the contribution of individual documents, making attribution difficult and contributing to the ``lost-in-the-middle'' effect, where relevant information in long contexts is overlooked. Concatenation also scales poorly: computational cost grows quadratically with context length, a problem that becomes especially severe when the context includes visual data, as in visual question answering. Attempts to mitigate these issues by limiting context length can further restrict performance by preventing models from benefiting from the improved recall offered by deeper retrieval. We propose Bayesian Ensemble Retrieval-Augmented Generation (BERAG), along with Bayesian Ensemble Fine-Tuning (BEFT), as a RAG framework in which language models are conditioned on individual retrieved documents rather than a single combined context. BERAG treats document posterior probabilities as ensemble weights and updates them token by token using Bayes' rule during generation. This approach enables probabilistic re-ranking, parallel memory usage, and clear attribution of document contribution, making it well-suited for large document collections. We evaluate BERAG and BEFT primarily on knowledge-based visual question answering tasks, where models must reason over long, imperfect retrieval lists. The results show substantial improvements over standard RAG, including strong gains on Document Visual Question Answering and multimodal needle-in-a-haystack benchmarks. We also demonstrate that BERAG mitigates the ``lost-in-the-middle'' effect. The document posterior can be used to detect insufficient grounding and trigger deflection, while document pruning enables faster decoding than standard RAG.
匹配关键词: test-time compute
---

[ACADEMIC - ARXIV]
标题: A Non-Invasive Alternative to RFID: Self-Sufficient 3D Identification of Group-Housed Livestock
作者: Shiva Paudel, TsungCheng Tsai, Dongyi Wang
链接: https://arxiv.org/abs/2604.22657v1
完整摘要: Accurate identification of individual farm animals in group-housed environments is a cornerstone of precision livestock management. However, current industry standards rely heavily on Radio Frequency Identification (RFID) ear tags, which are invasive, prone to loss, and restricted by the spatial limitations of antenna fields. In this paper, we propose a non-intrusive, vision-based identification system leveraging 3D point cloud data captured within a commercial electronic feeding station (EFS). Departing from traditional supervised frame-level inference, we introduce the Temporal Adaptive Recognition Architecture (TARA), a self-sufficient, semi-supervised framework designed to maintain identity consistency over time. TARA employs a dynamic recalibration mechanism that updates individual identity profiles to account for morphological changes in the livestock. To facilitate training in label-scarce environments, we utilize a visit-level majority voting strategy to generate high-fidelity pseudo-labels from raw temporal sequences. Experimental results on a group housed sow dataset collected from an operational commercial barn demonstrate that our approach achieves 100% identification accuracy at the visit level. These results suggest that vision-based 3D point cloud analysis offers a robust, superior alternative to RFID-based systems, paving the way for fully autonomous individual animal monitoring.
匹配关键词: self-consistency
---

[ACADEMIC - ARXIV]
标题: Data-Free Contribution Estimation in Federated Learning using Gradient von Neumann Entropy
作者: Asim Ukaye, Mubarak Abdu-Aguye, Nurbek Tastan, Karthik Nandakumar
链接: https://arxiv.org/abs/2604.22562v1
完整摘要: Client contribution estimation in Federated Learning is necessary for identifying clients' importance and for providing fair rewards. Current methods often rely on server-side validation data or self-reported client information, which can compromise privacy or be susceptible to manipulation. We introduce a data-free signal based on the matrix von Neumann (spectral) entropy of the final-layer updates, which measures the diversity of the information contributed. We instantiate two practical schemes: (i) SpectralFed, which uses normalized entropy as aggregation weights, and (ii) SpectralFuse, which fuses entropy with class-specific alignment via a rank-adaptive Kalman filter for per-round stability. Across CIFAR-10/100 and the naturally partitioned FEMNIST and FedISIC benchmarks, entropy-derived scores show a consistently high correlation with standalone client accuracy under diverse non-IID regimes - without validation data or client metadata. We compare our results with data-free contribution estimation baselines and show that spectral entropy serves as a useful indicator of client contribution.
匹配关键词: self-consistency
---

[ACADEMIC - ARXIV]
标题: Distilling Vision Transformers for Distortion-Robust Representation Learning
作者: Konstantinos Alexis, Giorgos Giannopoulos, Dimitrios Gunopulos
链接: https://arxiv.org/abs/2604.22529v1
完整摘要: Self-supervised learning has achieved remarkable success in learning visual representations from clean data, yet remains challenging when clean observations are sparse or not available at all. In this paper, we demonstrate that pretrained vision models can be leveraged to learn distortion-robust representations, which can then be effectively applied to downstream tasks operating on distorted observations. In particular, we propose an asymmetric knowledge distillation framework in which both teacher and student are initialized from the same pretrained Vision Transformer but receive different views of each image: the teacher processes clean images, while the student sees their distorted versions. We introduce multi-level distillation that aligns global embeddings, patch-level features, and attention maps and show that the student is able to approximate clean-image representations despite never directly accessing clean data. We evaluate our approach on image classification tasks across several datasets and under various distortions, consistently outperforming existing alternatives for the same amount of human supervision.
匹配关键词: self-consistency
---

[ACADEMIC - ARXIV]
标题: How Hard is it to Decide if a Fact is Relevant to a Query?
作者: Meghyn Bienvenu, Diego Figueira, Pierre Lafourcade
链接: https://arxiv.org/abs/2604.22422v1
完整摘要: We consider the following fundamental problem: given a database D, Boolean conjunctive query (CQ) q, and fact f in D, decide whether f is relevant to q wrt. D, i.e., does f belong to a minimal subset S of D such that S |= q. Despite being of central importance to query answer explanation, the combined complexity of deciding query relevance has not been studied in detail, leaving open what makes this problem hard, and which restrictions can yield lower complexity. Relevance has already been shown to be harder than query evaluation: namely, $Σ^p_2$-complete for CQs, even over a binary signature. We further observe that NP-hardness applies already to (acyclic) chain CQs. Our work identifies self-joins (multiple atoms with the same relation) as the culprit. Indeed, we prove that if we forbid or bound the occurrence of self-joins, then relevance has the same complexity as query evaluation, namely, NP (without structural restrictions) and LogCFL (for bounded hypertreewidth classes). In the ontology setting, we establish an analogous result for ontology-mediated queries consisting of a CQ and DL-Lite_R ontology, namely that relevance is no harder than query answering provided that we bound the interaction width (which generalizes both self-join width and a recently introduced 'interaction-free' condition). Our results thus pinpoint what makes relevance harder than query evaluation and identify natural classes of queries which admit efficient relevance computation.
匹配关键词: self-consistency
---

[ACADEMIC - ARXIV]
标题: A Nationwide Japanese Medical Claims Foundation Model: Balancing Model Scaling and Task-Specific Computational Efficiency
作者: Nanae Aratake, Taisei Tosaki, Yuji Okamoto, Eiichiro Uchino, Masaki Nakamura, Nobutomo Matsui, Akiko Hatakama, Yasushi Okuno
链接: https://arxiv.org/abs/2604.22348v1
完整摘要: Clinical risk prediction using longitudinal medical data supports individualized care. Self-supervised foundation models have emerged as a promising approach for leveraging large-scale unlabeled healthcare records. In natural language processing, scaling laws suggest that larger models achieve predictably lower pretraining losses, supporting the foundation model paradigm. However, for structured medical data, characterized by a limited vocabulary and sparse observations, whether increasing model size consistently improves downstream predictions is unclear, as most studies evaluate only a single model scale. In this study, we evaluated the relationship between model scale and downstream task performance for structured medical foundation models. Using a random sample (2.3 million patients, 32 hospitals) from a nationwide 519-hospital Japanese claims database, we pretrained encoder-only Transformers at five scales (2.2M-101M parameters) for disease incidence and medication prediction. Downstream performance saturated at task-dependent thresholds: disease prediction benefited from larger models (32M-101M), whereas medication prediction saturated at 11M, reducing pretraining time by 178 h. Across all tasks, the best-performing model consistently outperformed a Light Gradient Boosting Machine baseline in the area under the precision-recall curve. These findings indicate that, unlike the monotonically decreasing pretraining loss, the optimal model size varied depending on task characteristics. This task-dependent saturation provides practical guidance for balancing predictive performance and computational cost in structured medical foundation models.
匹配关键词: self-consistency
---

[ACADEMIC - ARXIV]
标题: Inter-Stance: A Dyadic Multimodal Corpus for Conversational Stance Analysis
作者: Xiang Zhang, Xiaotian Li, Taoyue Wang, Nan Bi, Xin Zhou, Cody Zhou, Zoie Wang, Andrew Yang, Yuming Su, Jeff Cohn, Qiang Ji, Lijun Yin
链接: https://arxiv.org/abs/2604.22739v1
完整摘要: Social interactions dominate our perceptions of the world and shape our daily behavior by attaching social meaning to acts as simple and spontaneous as gestures, facial expressions, voice, and speech. People mimic and otherwise respond to each other's postures, facial expressions, mannerisms, and other verbal and nonverbal behavior, and form appraisals or evaluations in the process. Yet, no publicly-available dataset includes multimodal recordings and self-report measures of multiple persons in social interaction. Dyadic recordings and annotation are lacking. We present a new data corpus of multimodal dyadic interaction (45 dyads, 90 persons) that includes synchronized multi-modality behavior (2D face video, 3D face geometry, thermal spectrum dynamics, voice and speech behavior, physiology (PPG, EDA, heart-rate, blood pressure, and respiration), and self-reported affect of all participants in a communicative interaction scenario. Two types of dyads are included: persons with shared past history and strangers. Annotations include social signals, agreement, disagreement, and neutral stance. With a potent emotion induction, these multimodal data will enable novel modeling of multimodal interpersonal behavior. We present extensive experiments to evaluate multimodal dyadic communication of dyads with and without interpersonal history, and their affect. This new database will make multimodal modeling of social interaction never possible before. The dataset includes 20TB of multimodal data to share with the research community.
匹配关键词: process reward
---

[ACADEMIC - ARXIV]
标题: ATRS: Adaptive Trajectory Re-splitting via a Shared Neural Policy for Parallel Optimization
作者: Jiajun Yu, Guodong Liu, Li Wang, Pengxiang Zhou, Wentao Liu, Yin He, Chao Xu, Fei Gao, Yanjun Cao
链接: https://arxiv.org/abs/2604.22715v1
完整摘要: Parallel trajectory optimization via the Alternating Direction Method of Multipliers (ADMM) has emerged as a scalable approach to long-horizon motion planning. However, existing frameworks typically decompose the problem into parallel subproblems based on a predefined fixed structure. Such structural rigidity often causes optimization stagnation in highly constrained regions, where a few lagging subproblems delay global convergence. A natural remedy is to adaptively re-split these stagnating segments online. Yet, deciding when, where, and how to split exceeds the capability of rule-based heuristics. To this end, we propose ATRS, a novel framework that embeds a shared Deep Reinforcement Learning policy into the parallel ADMM loop. We formulate this adaptive adjustment as a Multi-Agent Shared-Policy Markov Decision Process, where all trajectory segments act as homogeneous agents and share a unified neural policy network. This parameter-sharing architecture endows the system with size invariance, enabling it to handle dynamically changing segment counts during re-splitting and generalize to arbitrary trajectory lengths. Furthermore, our formulation inherently supports zero-shot generalization to unseen environments, as our network relies solely on the internal states of the numerical solver rather than on the geometric features of the environment. To ensure solver stability, a Confidence-Based Election mechanism selects only the most stagnating segment for re-splitting at each step. Extensive simulations demonstrate that ATRS accelerates convergence, reducing the number of iterations by up to 26.0% and the computation time by up to 19.1%. Real-world experiments further confirm its applicability to both large-scale offline global planning and real-time onboard replanning within 35 ms per cycle, with no sim-to-real degradation.
匹配关键词: process reward
---

[ACADEMIC - ARXIV]
标题: Iterative Model-Learning Scheme via Gaussian Processes for Nonlinear Model Predictive Control of (Semi-)Batch Processes
作者: Tai Xuan Tan, Alexander Mitsos, Eike Cramer
链接: https://arxiv.org/abs/2604.22672v1
完整摘要: Batch processes are inherently transient and typically nonlinear, motivating nonlinear model predictive control (NMPC). However, adopting NMPC is hindered by the cost and unavailability of dynamic models. Thus, we propose to use Gaussian Processes (GP) in a model-learning NMPC scheme (GP-MLMPC) for batch processes. We initialize the GP-MLMPC using data from a single initial trajectory, e.g., from a PI controller. We iteratively apply the NMPC embedded with GPs to run batches and update the GP with new observations from each iteration, thereby achieving batch-wise improvements. Using uncertainty quantification from the GPs, we formulate chance constraints to enforce safe operation to the required confidence levels. We demonstrate our approach in \textit{silico} on a semi-batch polymerization reactor for tracking and economic objectives over durations of two hours, and the reactor temperature is constrained in a range of $\pm2^\circ C$ around its setpoint. After only four batch iterations, tracking error from the GP-MLMPC scheme converged to a reduction of $83\%$, compared to the initial trajectory. Furthermore, under an economic objective, the GP-MLMPC resulted in a 17-fold increase in final product mass by iteration 8, compared to the initial trajectory. In both cases, the resulting GP-MLMPC performance is on par with the full-model NMPC, which shows that the optimal controller can be learned by the approach. By collecting samples around the optimal trajectory, the GP-MLMPC remains sample-efficient across iterations and achieves quick convergence. Thus, the proposed GP-MLMPC scheme presents a promising data-efficient approach for the control of nonlinear batch processes without mechanistic knowledge.
匹配关键词: process reward
---

[ACADEMIC - ARXIV]
标题: CLVAE: A Variational Autoencoder for Long-Term Customer Revenue Forecasting
作者: Jeffrey Näf, Riana Valera Mbelson, Markus Meierer
链接: https://arxiv.org/abs/2604.22636v1
完整摘要: Predicting customers' long-term revenue from sparse and irregular transaction data is central to marketing resource allocation in non-contractual settings, yet existing approaches face a trade-off. Traditional probabilistic customer base models deliver robust long-horizon forecasts by imposing strong structural assumptions, while flexible machine-learning models often require substantial training data and careful tuning. We propose a variational-autoencoder-based model that preserves the process-based likelihood of established attrition-transaction-spend models conditional on customer heterogeneity, but replaces the restrictive parametric mixing distribution with a flexible latent representation learned by encoder-decoder networks. The resulting approach (i) provides a single model for customer attrition, transactions and spending, (ii) remains reliable when contextual covariates are unavailable, and (iii) flexibly incorporates rich covariates and nonlinear effects when they are available. This design balances structural stability with the flexibility needed to capture complex purchase dynamics. Across multiple real-world datasets and prediction horizons, the proposed model improves upon the latest benchmarks. Businesses benefit directly, as a better assessment of customers' future revenues improves the efficiency of campaign targeting. For research, this work provides guidance on how to embed domain-specific models into the variational autoencoder framework, enabling flexible representation learning while retaining an econometrically meaningful process structure.
匹配关键词: process reward
---

[ACADEMIC - ARXIV]
标题: Dharma, Data and Deception: An LLM-Powered Rhetorical Analysis of Cow-Urine Health Claims on YouTube
作者: Sheza Munir, Ratna Kandala, Anamta Khan, Deepti, Joyojeet Pal
链接: https://arxiv.org/abs/2604.22606v1
完整摘要: Health misinformation remains one of the most pressing challenges on social media, particularly when cultural traditions intersect with scientific-sounding claims. These dynamics are not only global but also deeply local, manifesting in culturally specific controversies that require careful analysis. Motivated by this, we examine 100 YouTube transcripts that promote or debunk cow urine (gomutra) as a health remedy, focusing on rhetorical strategies such as appeals to authority, efficacy appeals, and conspiracy framing. We employ large language models (LLMs) including GPT-4, GPT-4o, GPT-4.1, GPT-5, Gemini 2.5 Pro, and Mistral Medium 3 to annotate transcripts using a 14-category taxonomy of persuasive tactics. Our analysis reveals that promoters predominantly rely on efficacy appeals and social proof, while debunkers emphasize authority and rebuttal. Human evaluation of a subset of annotations yielded 90.1\% inter-annotator agreement, confirming the reliability of our taxonomy and validation process. This work advances computational methods for misinformation analysis and demonstrates how LLMs can support large-scale studies of cultural discourse online.
匹配关键词: process reward
---

[ACADEMIC - ARXIV]
标题: SS3D: End2End Self-Supervised 3D from Web Videos
作者: Marwane Hariat, Gianni Franchi, David Filliat, Antoine Manzanera
链接: https://arxiv.org/abs/2604.22686v1
完整摘要: We present SS3D, a web-scale SfM-based self-supervision pretraining pipeline for feed-forward 3D estimation from monocular video. Our model jointly predicts depth, ego-motion, and intrinsics in a single forward pass and is trained/evaluated as a coherent end-to-end 3D estimator. To stabilize joint learning, we use an intrinsics-first two-stage schedule and a unified single-checkpoint evaluation protocol. Scaling SfM self-supervision to unconstrained web video is challenging due to weak multi-view observability and strong corpus heterogeneity; we address these with a multi-view signal proxy (MVS) used for filtering and curriculum sampling, and with expert training distilled into a single student. Pretraining on YouTube-8M (~100M frames after filtering) yields strong cross-domain zero-shot transfer and improved fine-tuning performance over prior self-supervised baselines. We release the pretrained checkpoint and code.
匹配关键词: pretraining
---

[ACADEMIC - ARXIV]
标题: GazeVLA: Learning Human Intention for Robotic Manipulation
作者: Chengyang Li, Kaiyi Xiong, Yuan Xu, Lei Qian, Yizhou Wang, Wentao Zhu
链接: https://arxiv.org/abs/2604.22615v1
完整摘要: Embodied foundation models have achieved significant breakthroughs in robotic manipulation, yet they still depend heavily on large-scale robot demonstrations. Although recent works have explored leveraging human data to alleviate this dependency, effectively extracting transferable knowledge remains a significant challenge due to the inherent embodiment gap between human and robot. We argue that the intention underlying human actions can serve as a powerful intermediate representation for bridging this gap. In this paper, we introduce a novel framework that explicitly learns and transfers human intention to facilitate robotic manipulation. Specifically, we model intention through gaze, as it naturally precedes physical actions and serves as an observable proxy for human intent. Our model is first pretrained on a large-scale egocentric human dataset to capture human intention and its synergy with action, followed by finetuning on a small set of robot and human data. During inference, the model adopts a Chain-of-Thought reasoning paradigm, sequentially predicting intention before executing the action. Extensive evaluations in simulation and real-world settings, across long-horizon and fine-grained tasks, and under few-shot and robustness benchmarks, show that our method consistently outperforms strong baselines, generalizes better, and achieves state-of-the-art performance.
匹配关键词: pretraining
---

[ACADEMIC - ARXIV]
标题: Cross-Stage Coherence in Hierarchical Driving VQA: Explicit Baselines and Learned Gated Context Projectors
作者: Gautam Kumar Jain, Carsten Markgraf, Julian Stähler
链接: https://arxiv.org/abs/2604.22560v1
完整摘要: Graph Visual Question Answering (GVQA) for autonomous driving organizes reasoning into ordered stages, namely Perception, Prediction, and Planning, where planning decisions should remain consistent with the model's own perception. We present a comparative study of cross-stage context passing on DriveLM-nuScenes using two complementary mechanisms. The explicit variant evaluates three prompt-based conditioning strategies on a domain-adapted 4B VLM (Mini-InternVL2-4B-DA-DriveLM) without additional training, reducing NLI contradiction by up to 42.6% and establishing a strong zero-training baseline. The implicit variant introduces gated context projectors, which extract a hidden-state vector from one stage and inject a normalized, gated projection into the next stage's input embeddings. These projectors are jointly trained with stage-specific QLoRA adapters on a general-purpose 8B VLM (InternVL3-8B-Instruct) while updating only approximately 0.5% of parameters. The implicit variant achieves a statistically significant 34% reduction in planning-stage NLI contradiction (bootstrap 95% CIs, p < 0.05) and increases cross-stage entailment by 50%, evaluated with a multilingual NLI classifier to account for mixed-language outputs. Planning language quality also improves (CIDEr +30.3%), but lexical overlap and structural consistency degrade due to the absence of driving-domain pretraining. Since the two variants use different base models, we present them as complementary case studies: explicit context passing provides a strong training-free baseline for surface consistency, while implicit gated projection delivers significant planning-stage semantic gains, suggesting domain adaptation as a plausible next ingredient for full-spectrum improvement.
匹配关键词: pretraining
---

[ACADEMIC - ARXIV]
标题: Are Natural-Domain Foundation Models Effective for Accelerated Cardiac MRI Reconstruction?
作者: Anam Hashmi, Mayug Maniparambil, Julia Dietlmeier, Kathleen M. Curran, Noel E. O'Connor
链接: https://arxiv.org/abs/2604.22557v1
完整摘要: The emergence of large-scale pretrained foundation models has transformed computer vision, enabling strong performance across diverse downstream tasks. However, their potential for physics-based inverse problems, such as accelerated cardiac MRI reconstruction, remains largely underexplored. In this work, we investigate whether natural-domain foundation models can serve as effective image priors for accelerated cardiac MRI reconstruction, and compare the performance obtained against domain-specific counterparts such as BiomedCLIP. We propose an unrolled reconstruction framework that incorporates pretrained, frozen visual encoders, such as CLIP, DINOv2, and BiomedCLIP, within each cascade to guide the reconstruction process. Through extensive experiments, we show that while task-specific state-of-the-art reconstruction models such as E2E-VarNet achieve superior performance in standard in-distribution settings, foundation-model-based approaches remain competitive. More importantly, in challenging cross-domain scenarios, where models are trained on cardiac MRI and evaluated on anatomically distinct knee and brain datasets--foundation models exhibit improved robustness, particularly under high acceleration factors and limited low-frequency sampling. We further observe that natural-image-pretrained models, such as CLIP, learn highly transferable structural representations, while domain-specific pretraining (BiomedCLIP) provides modest additional gains in more ill-posed regimes. Overall, our results suggest that pretrained foundation models offer a promising source of transferable priors, enabling improved robustness and generalization in accelerated MRI reconstruction.
匹配关键词: pretraining
---

[ACADEMIC - ARXIV]
标题: Distilling Vision Transformers for Distortion-Robust Representation Learning
作者: Konstantinos Alexis, Giorgos Giannopoulos, Dimitrios Gunopulos
链接: https://arxiv.org/abs/2604.22529v1
完整摘要: Self-supervised learning has achieved remarkable success in learning visual representations from clean data, yet remains challenging when clean observations are sparse or not available at all. In this paper, we demonstrate that pretrained vision models can be leveraged to learn distortion-robust representations, which can then be effectively applied to downstream tasks operating on distorted observations. In particular, we propose an asymmetric knowledge distillation framework in which both teacher and student are initialized from the same pretrained Vision Transformer but receive different views of each image: the teacher processes clean images, while the student sees their distorted versions. We introduce multi-level distillation that aligns global embeddings, patch-level features, and attention maps and show that the student is able to approximate clean-image representations despite never directly accessing clean data. We evaluate our approach on image classification tasks across several datasets and under various distortions, consistently outperforming existing alternatives for the same amount of human supervision.
匹配关键词: pretraining
---

[ACADEMIC - ARXIV]
标题: How Do AI Agents Spend Your Money? Analyzing and Predicting Token Consumption in Agentic Coding Tasks
作者: Longju Bai, Zhemin Huang, Xingyao Wang, Jiao Sun, Rada Mihalcea, Erik Brynjolfsson, Alex Pentland, Jiaxin Pei
链接: https://arxiv.org/abs/2604.22750v1
完整摘要: The wide adoption of AI agents in complex human workflows is driving rapid growth in LLM token consumption. When agents are deployed on tasks that require a significant amount of tokens, three questions naturally arise: (1) Where do AI agents spend the tokens? (2) Which models are more token-efficient? and (3) Can agents predict their token usage before task execution? In this paper, we present the first systematic study of token consumption patterns in agentic coding tasks. We analyze trajectories from eight frontier LLMs on SWE-bench Verified and evaluate models' ability to predict their own token costs before task execution. We find that: (1) agentic tasks are uniquely expensive, consuming 1000x more tokens than code reasoning and code chat, with input tokens rather than output tokens driving the overall cost; (2) token usage is highly variable and inherently stochastic: runs on the same task can differ by up to 30x in total tokens, and higher token usage does not translate into higher accuracy; instead, accuracy often peaks at intermediate cost and saturates at higher costs; (3) models vary substantially in token efficiency: on the same tasks, Kimi-K2 and Claude-Sonnet-4.5, on average, consume over 1.5 million more tokens than GPT-5; (4) task difficulty rated by human experts only weakly aligns with actual token costs, revealing a fundamental gap between human-perceived complexity and the computational effort agents actually expend; and (5) frontier models fail to accurately predict their own token usage (with weak-to-moderate correlations, up to 0.39) and systematically underestimate real token costs. Our study offers new insights into the economics of AI agents and can inspire future research in this direction.
匹配关键词: foundation model
---

[ACADEMIC - ARXIV]
标题: Representational Harms in LLM-Generated Narratives Against Global Majority Nationalities
作者: Ilana Nguyen, Harini Suresh, Thema Monroe-White, Evan Shieh
链接: https://arxiv.org/abs/2604.22749v1
完整摘要: Large language models (LLMs) are increasingly used for text generation tasks from everyday use to high-stakes enterprise and government applications, including simulated interviews with asylum seekers. While many works highlight the new potential applications of LLMs, there are risks of LLMs encoding and perpetuating harmful biases about non-dominant communities across the globe. To better evaluate and mitigate such harms, more research examining how LLMs portray diverse individuals is needed. In this work, we study how national origin identities are portrayed by widely-adopted LLMs in response to open-ended narrative generation prompts. Our findings demonstrate the presence of persistent representational harms by national origin, including harmful stereotypes, erasure, and one-dimensional portrayals of Global Majority identities. Minoritized national identities are simultaneously underrepresented in power-neutral stories and overrepresented in subordinated character portrayals, which are over fifty times more likely to appear than dominant portrayals. The degree of harm is amplified when US nationality cues (e.g., ``American'') are present in input prompts. Notably, we find that the harms we identify cannot be explained away via sycophancy, as US-centric biases persist even when replacing US nationality cues with non-US national identities in the prompts. Based on our findings, we call for further exploration of cultural harms in LLMs through methodologies that center Global Majority perspectives and challenge the uncritical adoption of US-based LLMs for the classification, surveillance, and misrepresentation of the majority of our planet.
匹配关键词: foundation model
---

[ACADEMIC - ARXIV]
标题: Agentic World Modeling: Foundations, Capabilities, Laws, and Beyond
作者: Meng Chu, Xuan Billy Zhang, Kevin Qinghong Lin, Lingdong Kong, Jize Zhang, Teng Tu, Weijian Ma, Ziqi Huang, Senqiao Yang, Wei Huang, Yeying Jin, Zhefan Rao, Jinhui Ye, Xinyu Lin, Xichen Zhang, Qisheng Hu, Shuai Yang, Leyang Shen, Wei Chow, Yifei Dong, Fengyi Wu, Quanyu Long, Bin Xia, Shaozuo Yu, Mingkang Zhu, Wenhu Zhang, Jiehui Huang, Haokun Gui, Haoxuan Che, Long Chen, Qifeng Chen, Wenxuan Zhang, Wenya Wang, Xiaojuan Qi, Yang Deng, Yanwei Li, Mike Zheng Shou, Zhi-Qi Cheng, See-Kiong Ng, Ziwei Liu, Philip Torr, Jiaya Jia
链接: https://arxiv.org/abs/2604.22748v1
完整摘要: As AI systems move from generating text to accomplishing goals through sustained interaction, the ability to model environment dynamics becomes a central bottleneck. Agents that manipulate objects, navigate software, coordinate with others, or design experiments require predictive environment models, yet the term world model carries different meanings across research communities. We introduce a "levels x laws" taxonomy organized along two axes. The first defines three capability levels: L1 Predictor, which learns one-step local transition operators; L2 Simulator, which composes them into multi-step, action-conditioned rollouts that respect domain laws; and L3 Evolver, which autonomously revises its own model when predictions fail against new evidence. The second identifies four governing-law regimes: physical, digital, social, and scientific. These regimes determine what constraints a world model must satisfy and where it is most likely to fail. Using this framework, we synthesize over 400 works and summarize more than 100 representative systems spanning model-based reinforcement learning, video generation, web and GUI agents, multi-agent social simulation, and AI-driven scientific discovery. We analyze methods, failure modes, and evaluation practices across level-regime pairs, propose decision-centric evaluation principles and a minimal reproducible evaluation package, and outline architectural guidance, open problems, and governance challenges. The resulting roadmap connects previously isolated communities and charts a path from passive next-step prediction toward world models that can simulate, and ultimately reshape, the environments in which agents operate.
匹配关键词: foundation model
---

[ACADEMIC - ARXIV]
标题: Relaxation-Informed Training of Neural Network Surrogate Models
作者: Calvin Tsay
链接: https://arxiv.org/abs/2604.22746v1
完整摘要: ReLU neural networks trained as surrogate models can be embedded exactly in mixed-integer linear programs (MILPs), enabling global optimization over the learned function. The tractability of the resulting MILP depends on structural properties of the network, i.e., the number of binary variables in associated formulations and the tightness of the continuous LP relaxation. These properties are determined during training, yet standard training objectives (prediction loss with classical weight regularization) offer no mechanism to directly control them. This work studies training regularizers that directly target downstream MILP tractability. Specifically, we propose simple bound-based regularizers that penalize the big-M constants of MILP formulations and/or the number of unstable neurons. Moreover, we introduce an LP relaxation gap regularizer that explicitly penalizes the per-sample gap of the continuous relaxation at training points. We derive its associated gradient and provide an implementation from LP dual variables without custom automatic differentiation tools. We show that combining the above regularizers can approximate the full total derivative of the LP gap with respect to the network parameters, capturing both direct and indirect sensitivities. Experiments on non-convex benchmark functions and a two-stage stochastic programming problem with quantile neural network surrogates demonstrate that the proposed regularizers can reduce MILP solve times by up to four orders of magnitude relative to an unregularized baseline, while maintaining competitive surrogate model accuracy.
匹配关键词: foundation model
---

[ACADEMIC - ARXIV]
标题: Inter-Stance: A Dyadic Multimodal Corpus for Conversational Stance Analysis
作者: Xiang Zhang, Xiaotian Li, Taoyue Wang, Nan Bi, Xin Zhou, Cody Zhou, Zoie Wang, Andrew Yang, Yuming Su, Jeff Cohn, Qiang Ji, Lijun Yin
链接: https://arxiv.org/abs/2604.22739v1
完整摘要: Social interactions dominate our perceptions of the world and shape our daily behavior by attaching social meaning to acts as simple and spontaneous as gestures, facial expressions, voice, and speech. People mimic and otherwise respond to each other's postures, facial expressions, mannerisms, and other verbal and nonverbal behavior, and form appraisals or evaluations in the process. Yet, no publicly-available dataset includes multimodal recordings and self-report measures of multiple persons in social interaction. Dyadic recordings and annotation are lacking. We present a new data corpus of multimodal dyadic interaction (45 dyads, 90 persons) that includes synchronized multi-modality behavior (2D face video, 3D face geometry, thermal spectrum dynamics, voice and speech behavior, physiology (PPG, EDA, heart-rate, blood pressure, and respiration), and self-reported affect of all participants in a communicative interaction scenario. Two types of dyads are included: persons with shared past history and strangers. Annotations include social signals, agreement, disagreement, and neutral stance. With a potent emotion induction, these multimodal data will enable novel modeling of multimodal interpersonal behavior. We present extensive experiments to evaluate multimodal dyadic communication of dyads with and without interpersonal history, and their affect. This new database will make multimodal modeling of social interaction never possible before. The dataset includes 20TB of multimodal data to share with the research community.
匹配关键词: foundation model
---

[ACADEMIC - ARXIV]
标题: Spend Less, Fit Better: Budget-Efficient Scaling Law Fitting via Active Experiment Selection
作者: Sijie Li, Shanda Li, Haowei Lin, Weiwei Sun, Ameet Talwalkar, Yiming Yang
链接: https://arxiv.org/abs/2604.22753v1
完整摘要: Scaling laws are used to plan multi-million-dollar training runs, but fitting those laws can itself cost millions. In modern large-scale workflows, assembling a sufficiently informative set of pilot experiments is already a major budget-allocation problem rather than a routine preprocessing step. We formulate scaling-law fitting as budget-aware sequential experimental design: given a finite pool of runnable experiments with heterogeneous costs, choose which runs to execute so as to maximize extrapolation accuracy in a high-cost target region. We then propose an uncertainty-aware method for sequentially allocating experimental budget toward the runs most useful for target-region extrapolation. Across a diverse benchmark of scaling-law tasks, our method consistently outperforms classical design-based baselines, and often approaches the performance of fitting on the full experimental set while using only about 10% of the total training budget. Our code is available at https://github.com/PlanarG/active-sl.
匹配关键词: scaling law
---

[ACADEMIC - ARXIV]
标题: Agentic World Modeling: Foundations, Capabilities, Laws, and Beyond
作者: Meng Chu, Xuan Billy Zhang, Kevin Qinghong Lin, Lingdong Kong, Jize Zhang, Teng Tu, Weijian Ma, Ziqi Huang, Senqiao Yang, Wei Huang, Yeying Jin, Zhefan Rao, Jinhui Ye, Xinyu Lin, Xichen Zhang, Qisheng Hu, Shuai Yang, Leyang Shen, Wei Chow, Yifei Dong, Fengyi Wu, Quanyu Long, Bin Xia, Shaozuo Yu, Mingkang Zhu, Wenhu Zhang, Jiehui Huang, Haokun Gui, Haoxuan Che, Long Chen, Qifeng Chen, Wenxuan Zhang, Wenya Wang, Xiaojuan Qi, Yang Deng, Yanwei Li, Mike Zheng Shou, Zhi-Qi Cheng, See-Kiong Ng, Ziwei Liu, Philip Torr, Jiaya Jia
链接: https://arxiv.org/abs/2604.22748v1
完整摘要: As AI systems move from generating text to accomplishing goals through sustained interaction, the ability to model environment dynamics becomes a central bottleneck. Agents that manipulate objects, navigate software, coordinate with others, or design experiments require predictive environment models, yet the term world model carries different meanings across research communities. We introduce a "levels x laws" taxonomy organized along two axes. The first defines three capability levels: L1 Predictor, which learns one-step local transition operators; L2 Simulator, which composes them into multi-step, action-conditioned rollouts that respect domain laws; and L3 Evolver, which autonomously revises its own model when predictions fail against new evidence. The second identifies four governing-law regimes: physical, digital, social, and scientific. These regimes determine what constraints a world model must satisfy and where it is most likely to fail. Using this framework, we synthesize over 400 works and summarize more than 100 representative systems spanning model-based reinforcement learning, video generation, web and GUI agents, multi-agent social simulation, and AI-driven scientific discovery. We analyze methods, failure modes, and evaluation practices across level-regime pairs, propose decision-centric evaluation principles and a minimal reproducible evaluation package, and outline architectural guidance, open problems, and governance challenges. The resulting roadmap connects previously isolated communities and charts a path from passive next-step prediction toward world models that can simulate, and ultimately reshape, the environments in which agents operate.
匹配关键词: scaling law
---

[ACADEMIC - ARXIV]
标题: Aligning Dense Retrievers with LLM Utility via DistillationAligning Dense Retrievers with LLM Utility via Distillation
作者: Rajinder Sandhu, Di Mu, Cheng Chang, Md Shahriar Tasjid, Himanshu Rai, Maksims Volkovs, Ga Wu
链接: https://arxiv.org/abs/2604.22722v1
完整摘要: Dense vector retrieval is the practical backbone of Retrieval- Augmented Generation (RAG), but similarity search can suffer from precision limitations. Conversely, utility-based approaches leveraging LLM re-ranking often achieve superior performance but are computationally prohibitive and prone to noise inherent in perplexity estimation. We propose Utility-Aligned Embeddings (UAE), a framework designed to merge these advantages into a practical, high-performance retrieval method. We formulate retrieval as a distribution matching problem, training a bi-encoder to imitate a utility distribution derived from perplexity reduction using a Utility-Modulated InfoNCE objective. This approach injects graded utility signals directly into the embedding space without requiring test-time LLM inference. On the QASPER benchmark, UAE improves retrieval Recall@1 by 30.59%, MAP by 30.16% and Token F1 by 17.3% over the strong semantic baseline BGE-Base. Crucially, UAE is over 180x faster than the efficient LLM re-ranking methods preserving competitive performance, demonstrating that aligning retrieval with generative utility yields reliable contexts at scale.
匹配关键词: scaling law
---

[ACADEMIC - ARXIV]
标题: ATRS: Adaptive Trajectory Re-splitting via a Shared Neural Policy for Parallel Optimization
作者: Jiajun Yu, Guodong Liu, Li Wang, Pengxiang Zhou, Wentao Liu, Yin He, Chao Xu, Fei Gao, Yanjun Cao
链接: https://arxiv.org/abs/2604.22715v1
完整摘要: Parallel trajectory optimization via the Alternating Direction Method of Multipliers (ADMM) has emerged as a scalable approach to long-horizon motion planning. However, existing frameworks typically decompose the problem into parallel subproblems based on a predefined fixed structure. Such structural rigidity often causes optimization stagnation in highly constrained regions, where a few lagging subproblems delay global convergence. A natural remedy is to adaptively re-split these stagnating segments online. Yet, deciding when, where, and how to split exceeds the capability of rule-based heuristics. To this end, we propose ATRS, a novel framework that embeds a shared Deep Reinforcement Learning policy into the parallel ADMM loop. We formulate this adaptive adjustment as a Multi-Agent Shared-Policy Markov Decision Process, where all trajectory segments act as homogeneous agents and share a unified neural policy network. This parameter-sharing architecture endows the system with size invariance, enabling it to handle dynamically changing segment counts during re-splitting and generalize to arbitrary trajectory lengths. Furthermore, our formulation inherently supports zero-shot generalization to unseen environments, as our network relies solely on the internal states of the numerical solver rather than on the geometric features of the environment. To ensure solver stability, a Confidence-Based Election mechanism selects only the most stagnating segment for re-splitting at each step. Extensive simulations demonstrate that ATRS accelerates convergence, reducing the number of iterations by up to 26.0% and the computation time by up to 19.1%. Real-world experiments further confirm its applicability to both large-scale offline global planning and real-time onboard replanning within 35 ms per cycle, with no sim-to-real degradation.
匹配关键词: scaling law
---

[ACADEMIC - ARXIV]
标题: Thinking Without Words: Efficient Latent Reasoning with Abstract Chain-of-Thought
作者: Keshav Ramji, Tahira Naseem, Ramón Fernandez Astudillo
链接: https://arxiv.org/abs/2604.22709v1
完整摘要: While long, explicit chains-of-thought (CoT) have proven effective on complex reasoning tasks, they are costly to generate during inference. Non-verbal reasoning methods have emerged with shorter generation lengths by leveraging continuous representations, yet their performance lags behind verbalized CoT. We propose $\textbf{Abstract Chain-of-Thought}$, a discrete latent reasoning post-training mechanism in which the language model produces a short sequence of tokens from a reserved vocabulary in lieu of a natural language CoT, before generating a response. To make previously unseen ''abstract'' tokens useful, we introduce a policy iteration-style warm-up loop that alternates between (i.) bottlenecking from a verbal CoT via masking and performing supervised fine-tuning, and (ii.) self-distillation by training the model to generate abstract tokens from the prompt alone via constrained decoding with the codebook. After warm-up, we optimize the generation of abstract sequences with warm-started reinforcement learning under constrained decoding. Abstract-CoT achieves up to $11.6\times$ fewer reasoning tokens while demonstrating comparable performance across mathematical reasoning, instruction-following, and multi-hop reasoning, and generalizes across language model families. We also find an emergent power law distribution over the abstract vocabulary, akin to those seen in natural language, that evolves across the training phases. Our findings highlight the potential for post-training latent reasoning mechanisms that enable efficient inference through a learned abstract reasoning language.
匹配关键词: scaling law
---

[ACADEMIC - ARXIV]
标题: How Do AI Agents Spend Your Money? Analyzing and Predicting Token Consumption in Agentic Coding Tasks
作者: Longju Bai, Zhemin Huang, Xingyao Wang, Jiao Sun, Rada Mihalcea, Erik Brynjolfsson, Alex Pentland, Jiaxin Pei
链接: https://arxiv.org/abs/2604.22750v1
完整摘要: The wide adoption of AI agents in complex human workflows is driving rapid growth in LLM token consumption. When agents are deployed on tasks that require a significant amount of tokens, three questions naturally arise: (1) Where do AI agents spend the tokens? (2) Which models are more token-efficient? and (3) Can agents predict their token usage before task execution? In this paper, we present the first systematic study of token consumption patterns in agentic coding tasks. We analyze trajectories from eight frontier LLMs on SWE-bench Verified and evaluate models' ability to predict their own token costs before task execution. We find that: (1) agentic tasks are uniquely expensive, consuming 1000x more tokens than code reasoning and code chat, with input tokens rather than output tokens driving the overall cost; (2) token usage is highly variable and inherently stochastic: runs on the same task can differ by up to 30x in total tokens, and higher token usage does not translate into higher accuracy; instead, accuracy often peaks at intermediate cost and saturates at higher costs; (3) models vary substantially in token efficiency: on the same tasks, Kimi-K2 and Claude-Sonnet-4.5, on average, consume over 1.5 million more tokens than GPT-5; (4) task difficulty rated by human experts only weakly aligns with actual token costs, revealing a fundamental gap between human-perceived complexity and the computational effort agents actually expend; and (5) frontier models fail to accurately predict their own token usage (with weak-to-moderate correlations, up to 0.39) and systematically underestimate real token costs. Our study offers new insights into the economics of AI agents and can inspire future research in this direction.
匹配关键词: language model
---

[ACADEMIC - ARXIV]
标题: Representational Harms in LLM-Generated Narratives Against Global Majority Nationalities
作者: Ilana Nguyen, Harini Suresh, Thema Monroe-White, Evan Shieh
链接: https://arxiv.org/abs/2604.22749v1
完整摘要: Large language models (LLMs) are increasingly used for text generation tasks from everyday use to high-stakes enterprise and government applications, including simulated interviews with asylum seekers. While many works highlight the new potential applications of LLMs, there are risks of LLMs encoding and perpetuating harmful biases about non-dominant communities across the globe. To better evaluate and mitigate such harms, more research examining how LLMs portray diverse individuals is needed. In this work, we study how national origin identities are portrayed by widely-adopted LLMs in response to open-ended narrative generation prompts. Our findings demonstrate the presence of persistent representational harms by national origin, including harmful stereotypes, erasure, and one-dimensional portrayals of Global Majority identities. Minoritized national identities are simultaneously underrepresented in power-neutral stories and overrepresented in subordinated character portrayals, which are over fifty times more likely to appear than dominant portrayals. The degree of harm is amplified when US nationality cues (e.g., ``American'') are present in input prompts. Notably, we find that the harms we identify cannot be explained away via sycophancy, as US-centric biases persist even when replacing US nationality cues with non-US national identities in the prompts. Based on our findings, we call for further exploration of cultural harms in LLMs through methodologies that center Global Majority perspectives and challenge the uncritical adoption of US-based LLMs for the classification, surveillance, and misrepresentation of the majority of our planet.
匹配关键词: language model
---

[ACADEMIC - ARXIV]
标题: Agentic World Modeling: Foundations, Capabilities, Laws, and Beyond
作者: Meng Chu, Xuan Billy Zhang, Kevin Qinghong Lin, Lingdong Kong, Jize Zhang, Teng Tu, Weijian Ma, Ziqi Huang, Senqiao Yang, Wei Huang, Yeying Jin, Zhefan Rao, Jinhui Ye, Xinyu Lin, Xichen Zhang, Qisheng Hu, Shuai Yang, Leyang Shen, Wei Chow, Yifei Dong, Fengyi Wu, Quanyu Long, Bin Xia, Shaozuo Yu, Mingkang Zhu, Wenhu Zhang, Jiehui Huang, Haokun Gui, Haoxuan Che, Long Chen, Qifeng Chen, Wenxuan Zhang, Wenya Wang, Xiaojuan Qi, Yang Deng, Yanwei Li, Mike Zheng Shou, Zhi-Qi Cheng, See-Kiong Ng, Ziwei Liu, Philip Torr, Jiaya Jia
链接: https://arxiv.org/abs/2604.22748v1
完整摘要: As AI systems move from generating text to accomplishing goals through sustained interaction, the ability to model environment dynamics becomes a central bottleneck. Agents that manipulate objects, navigate software, coordinate with others, or design experiments require predictive environment models, yet the term world model carries different meanings across research communities. We introduce a "levels x laws" taxonomy organized along two axes. The first defines three capability levels: L1 Predictor, which learns one-step local transition operators; L2 Simulator, which composes them into multi-step, action-conditioned rollouts that respect domain laws; and L3 Evolver, which autonomously revises its own model when predictions fail against new evidence. The second identifies four governing-law regimes: physical, digital, social, and scientific. These regimes determine what constraints a world model must satisfy and where it is most likely to fail. Using this framework, we synthesize over 400 works and summarize more than 100 representative systems spanning model-based reinforcement learning, video generation, web and GUI agents, multi-agent social simulation, and AI-driven scientific discovery. We analyze methods, failure modes, and evaluation practices across level-regime pairs, propose decision-centric evaluation principles and a minimal reproducible evaluation package, and outline architectural guidance, open problems, and governance challenges. The resulting roadmap connects previously isolated communities and charts a path from passive next-step prediction toward world models that can simulate, and ultimately reshape, the environments in which agents operate.
匹配关键词: language model
---

[ACADEMIC - ARXIV]
标题: Relaxation-Informed Training of Neural Network Surrogate Models
作者: Calvin Tsay
链接: https://arxiv.org/abs/2604.22746v1
完整摘要: ReLU neural networks trained as surrogate models can be embedded exactly in mixed-integer linear programs (MILPs), enabling global optimization over the learned function. The tractability of the resulting MILP depends on structural properties of the network, i.e., the number of binary variables in associated formulations and the tightness of the continuous LP relaxation. These properties are determined during training, yet standard training objectives (prediction loss with classical weight regularization) offer no mechanism to directly control them. This work studies training regularizers that directly target downstream MILP tractability. Specifically, we propose simple bound-based regularizers that penalize the big-M constants of MILP formulations and/or the number of unstable neurons. Moreover, we introduce an LP relaxation gap regularizer that explicitly penalizes the per-sample gap of the continuous relaxation at training points. We derive its associated gradient and provide an implementation from LP dual variables without custom automatic differentiation tools. We show that combining the above regularizers can approximate the full total derivative of the LP gap with respect to the network parameters, capturing both direct and indirect sensitivities. Experiments on non-convex benchmark functions and a two-stage stochastic programming problem with quantile neural network surrogates demonstrate that the proposed regularizers can reduce MILP solve times by up to four orders of magnitude relative to an unregularized baseline, while maintaining competitive surrogate model accuracy.
匹配关键词: language model
---

[ACADEMIC - ARXIV]
标题: Inter-Stance: A Dyadic Multimodal Corpus for Conversational Stance Analysis
作者: Xiang Zhang, Xiaotian Li, Taoyue Wang, Nan Bi, Xin Zhou, Cody Zhou, Zoie Wang, Andrew Yang, Yuming Su, Jeff Cohn, Qiang Ji, Lijun Yin
链接: https://arxiv.org/abs/2604.22739v1
完整摘要: Social interactions dominate our perceptions of the world and shape our daily behavior by attaching social meaning to acts as simple and spontaneous as gestures, facial expressions, voice, and speech. People mimic and otherwise respond to each other's postures, facial expressions, mannerisms, and other verbal and nonverbal behavior, and form appraisals or evaluations in the process. Yet, no publicly-available dataset includes multimodal recordings and self-report measures of multiple persons in social interaction. Dyadic recordings and annotation are lacking. We present a new data corpus of multimodal dyadic interaction (45 dyads, 90 persons) that includes synchronized multi-modality behavior (2D face video, 3D face geometry, thermal spectrum dynamics, voice and speech behavior, physiology (PPG, EDA, heart-rate, blood pressure, and respiration), and self-reported affect of all participants in a communicative interaction scenario. Two types of dyads are included: persons with shared past history and strangers. Annotations include social signals, agreement, disagreement, and neutral stance. With a potent emotion induction, these multimodal data will enable novel modeling of multimodal interpersonal behavior. We present extensive experiments to evaluate multimodal dyadic communication of dyads with and without interpersonal history, and their affect. This new database will make multimodal modeling of social interaction never possible before. The dataset includes 20TB of multimodal data to share with the research community.
匹配关键词: language model
---

[ACADEMIC - ARXIV]
标题: Agentic World Modeling: Foundations, Capabilities, Laws, and Beyond
作者: Meng Chu, Xuan Billy Zhang, Kevin Qinghong Lin, Lingdong Kong, Jize Zhang, Teng Tu, Weijian Ma, Ziqi Huang, Senqiao Yang, Wei Huang, Yeying Jin, Zhefan Rao, Jinhui Ye, Xinyu Lin, Xichen Zhang, Qisheng Hu, Shuai Yang, Leyang Shen, Wei Chow, Yifei Dong, Fengyi Wu, Quanyu Long, Bin Xia, Shaozuo Yu, Mingkang Zhu, Wenhu Zhang, Jiehui Huang, Haokun Gui, Haoxuan Che, Long Chen, Qifeng Chen, Wenxuan Zhang, Wenya Wang, Xiaojuan Qi, Yang Deng, Yanwei Li, Mike Zheng Shou, Zhi-Qi Cheng, See-Kiong Ng, Ziwei Liu, Philip Torr, Jiaya Jia
链接: https://arxiv.org/abs/2604.22748v1
完整摘要: As AI systems move from generating text to accomplishing goals through sustained interaction, the ability to model environment dynamics becomes a central bottleneck. Agents that manipulate objects, navigate software, coordinate with others, or design experiments require predictive environment models, yet the term world model carries different meanings across research communities. We introduce a "levels x laws" taxonomy organized along two axes. The first defines three capability levels: L1 Predictor, which learns one-step local transition operators; L2 Simulator, which composes them into multi-step, action-conditioned rollouts that respect domain laws; and L3 Evolver, which autonomously revises its own model when predictions fail against new evidence. The second identifies four governing-law regimes: physical, digital, social, and scientific. These regimes determine what constraints a world model must satisfy and where it is most likely to fail. Using this framework, we synthesize over 400 works and summarize more than 100 representative systems spanning model-based reinforcement learning, video generation, web and GUI agents, multi-agent social simulation, and AI-driven scientific discovery. We analyze methods, failure modes, and evaluation practices across level-regime pairs, propose decision-centric evaluation principles and a minimal reproducible evaluation package, and outline architectural guidance, open problems, and governance challenges. The resulting roadmap connects previously isolated communities and charts a path from passive next-step prediction toward world models that can simulate, and ultimately reshape, the environments in which agents operate.
匹配关键词: transformer architecture
---

[ACADEMIC - ARXIV]
标题: Neural Recovery of Historical Lexical Structure in Bantu Languages from Modern Data
作者: Hillary Mutisya, John Mugane
链接: https://arxiv.org/abs/2604.22730v1
完整摘要: We investigate whether neural models trained exclusively on modern morphological data can recover cross-lingual lexical structure consistent with historical reconstruction. Using BantuMorph v7, a transformer over Bantu morphological paradigms, we analyze 14 Eastern and Southern Bantu languages, extract encoder embeddings for their noun and verb lemmas, and identify 728 noun and 1,525 verb cognate candidates shared across 5+ languages. Evaluating these candidates against established historical resources-the Bantu Lexical Reconstructions database (BLR3; 4,786 reconstructed Proto-Bantu forms) and the ASJP basic vocabulary-we confirm 10 of the top 11 noun candidates (90.9%) align with previously reconstructed Proto-Bantu forms, including *-ntU 'person' (8 languages), *gombe 'cow' (9 languages), and *mUn (9 languages). Extending to verbs, 12 verb cognates align with reconstructed Proto-Bantu roots, including *-bon- 'see' and *-jIm- 'stand', each attested across wide geographic ranges. Cross-model validation using an independent translation model (NLLB-600M) confirms these patterns: both models recover cognate clusters and phylogenetic groupings consistent with established Guthrie-zone classifications (p 0.83 cosine similarity across languages (within-class > between-class, p < 10^-9). Our dataset is restricted to Eastern and Southern Bantu, so we interpret these results as recovering shared Bantu lexical structure consistent with Proto-Bantu rather than definitively distinguishing Proto-Bantu retentions from later regional innovations.
匹配关键词: transformer architecture
---

[ACADEMIC - ARXIV]
标题: ATRS: Adaptive Trajectory Re-splitting via a Shared Neural Policy for Parallel Optimization
作者: Jiajun Yu, Guodong Liu, Li Wang, Pengxiang Zhou, Wentao Liu, Yin He, Chao Xu, Fei Gao, Yanjun Cao
链接: https://arxiv.org/abs/2604.22715v1
完整摘要: Parallel trajectory optimization via the Alternating Direction Method of Multipliers (ADMM) has emerged as a scalable approach to long-horizon motion planning. However, existing frameworks typically decompose the problem into parallel subproblems based on a predefined fixed structure. Such structural rigidity often causes optimization stagnation in highly constrained regions, where a few lagging subproblems delay global convergence. A natural remedy is to adaptively re-split these stagnating segments online. Yet, deciding when, where, and how to split exceeds the capability of rule-based heuristics. To this end, we propose ATRS, a novel framework that embeds a shared Deep Reinforcement Learning policy into the parallel ADMM loop. We formulate this adaptive adjustment as a Multi-Agent Shared-Policy Markov Decision Process, where all trajectory segments act as homogeneous agents and share a unified neural policy network. This parameter-sharing architecture endows the system with size invariance, enabling it to handle dynamically changing segment counts during re-splitting and generalize to arbitrary trajectory lengths. Furthermore, our formulation inherently supports zero-shot generalization to unseen environments, as our network relies solely on the internal states of the numerical solver rather than on the geometric features of the environment. To ensure solver stability, a Confidence-Based Election mechanism selects only the most stagnating segment for re-splitting at each step. Extensive simulations demonstrate that ATRS accelerates convergence, reducing the number of iterations by up to 26.0% and the computation time by up to 19.1%. Real-world experiments further confirm its applicability to both large-scale offline global planning and real-time onboard replanning within 35 ms per cycle, with no sim-to-real degradation.
匹配关键词: transformer architecture
---

[ACADEMIC - ARXIV]
标题: A Non-Invasive Alternative to RFID: Self-Sufficient 3D Identification of Group-Housed Livestock
作者: Shiva Paudel, TsungCheng Tsai, Dongyi Wang
链接: https://arxiv.org/abs/2604.22657v1
完整摘要: Accurate identification of individual farm animals in group-housed environments is a cornerstone of precision livestock management. However, current industry standards rely heavily on Radio Frequency Identification (RFID) ear tags, which are invasive, prone to loss, and restricted by the spatial limitations of antenna fields. In this paper, we propose a non-intrusive, vision-based identification system leveraging 3D point cloud data captured within a commercial electronic feeding station (EFS). Departing from traditional supervised frame-level inference, we introduce the Temporal Adaptive Recognition Architecture (TARA), a self-sufficient, semi-supervised framework designed to maintain identity consistency over time. TARA employs a dynamic recalibration mechanism that updates individual identity profiles to account for morphological changes in the livestock. To facilitate training in label-scarce environments, we utilize a visit-level majority voting strategy to generate high-fidelity pseudo-labels from raw temporal sequences. Experimental results on a group housed sow dataset collected from an operational commercial barn demonstrate that our approach achieves 100% identification accuracy at the visit level. These results suggest that vision-based 3D point cloud analysis offers a robust, superior alternative to RFID-based systems, paving the way for fully autonomous individual animal monitoring.
匹配关键词: transformer architecture
---

[ACADEMIC - ARXIV]
标题: Adversarial Malware Generation in Linux ELF Binaries via Semantic-Preserving Transformations
作者: Lukáš Hrdonka, Martin Jureček
链接: https://arxiv.org/abs/2604.22639v1
完整摘要: Malware development and detection have undergone significant changes in recent years as modern concepts, such as machine learning, have been used for both adversarial attacks and defense. Despite intensive research on Windows Portable Executable (PE) files, there is minimal work on Linux Executable and Linkable Format (ELF). In this work, we summarize the academic papers submitted in this field and develop a new adversarial malware generator for the ELF format. Using a variety of metrics, we thoroughly evaluated our generator and achieved an Evasion Rate of 67.74 % while changing the confidence of the malware detector by -0.50 in the mean case for the dataset used. In our approach, we chose MalConv as the target classifier. Using this classifier, we found that the most successful modifications used strings typical of benign files as a data source. We conducted a variety of experiments and concluded that the target classifier appears sensitive to strings at any location within the executable file.
匹配关键词: transformer architecture
---

[ACADEMIC - ARXIV]
标题: How Do AI Agents Spend Your Money? Analyzing and Predicting Token Consumption in Agentic Coding Tasks
作者: Longju Bai, Zhemin Huang, Xingyao Wang, Jiao Sun, Rada Mihalcea, Erik Brynjolfsson, Alex Pentland, Jiaxin Pei
链接: https://arxiv.org/abs/2604.22750v1
完整摘要: The wide adoption of AI agents in complex human workflows is driving rapid growth in LLM token consumption. When agents are deployed on tasks that require a significant amount of tokens, three questions naturally arise: (1) Where do AI agents spend the tokens? (2) Which models are more token-efficient? and (3) Can agents predict their token usage before task execution? In this paper, we present the first systematic study of token consumption patterns in agentic coding tasks. We analyze trajectories from eight frontier LLMs on SWE-bench Verified and evaluate models' ability to predict their own token costs before task execution. We find that: (1) agentic tasks are uniquely expensive, consuming 1000x more tokens than code reasoning and code chat, with input tokens rather than output tokens driving the overall cost; (2) token usage is highly variable and inherently stochastic: runs on the same task can differ by up to 30x in total tokens, and higher token usage does not translate into higher accuracy; instead, accuracy often peaks at intermediate cost and saturates at higher costs; (3) models vary substantially in token efficiency: on the same tasks, Kimi-K2 and Claude-Sonnet-4.5, on average, consume over 1.5 million more tokens than GPT-5; (4) task difficulty rated by human experts only weakly aligns with actual token costs, revealing a fundamental gap between human-perceived complexity and the computational effort agents actually expend; and (5) frontier models fail to accurately predict their own token usage (with weak-to-moderate correlations, up to 0.39) and systematically underestimate real token costs. Our study offers new insights into the economics of AI agents and can inspire future research in this direction.
匹配关键词: mixture of experts
---

[ACADEMIC - ARXIV]
标题: SS3D: End2End Self-Supervised 3D from Web Videos
作者: Marwane Hariat, Gianni Franchi, David Filliat, Antoine Manzanera
链接: https://arxiv.org/abs/2604.22686v1
完整摘要: We present SS3D, a web-scale SfM-based self-supervision pretraining pipeline for feed-forward 3D estimation from monocular video. Our model jointly predicts depth, ego-motion, and intrinsics in a single forward pass and is trained/evaluated as a coherent end-to-end 3D estimator. To stabilize joint learning, we use an intrinsics-first two-stage schedule and a unified single-checkpoint evaluation protocol. Scaling SfM self-supervision to unconstrained web video is challenging due to weak multi-view observability and strong corpus heterogeneity; we address these with a multi-view signal proxy (MVS) used for filtering and curriculum sampling, and with expert training distilled into a single student. Pretraining on YouTube-8M (~100M frames after filtering) yields strong cross-domain zero-shot transfer and improved fine-tuning performance over prior self-supervised baselines. We release the pretrained checkpoint and code.
匹配关键词: mixture of experts
---

[ACADEMIC - ARXIV]
标题: Mixed Membership sub-Gaussian Models
作者: Huan Qing
链接: https://arxiv.org/abs/2604.22633v1
完整摘要: The Gaussian mixture model is widely used in unsupervised learning, owing to its simplicity and interpretability. However, a fundamental limitation of the classical Gaussian mixture model is that it forces each observation to belong to exactly one component. In many practical applications, such as genetics, social network analysis, and text mining, an observation may naturally belong to multiple components or exhibit partial membership in several latent components. To overcome this limitation, we propose the mixed membership sub-Gaussian model, which extends the classical Gaussian mixture framework by allowing each observation to belong to multiple components. This model inherits the interpretability of the classical Gaussian mixture model while offering greater flexibility for capturing complex overlapping structures. We develop an efficient spectral algorithm to estimate the mixed membership of each individual observation, and under mild separation conditions on the component centres, we prove that the estimation error of the per-individual membership vector can be made arbitrarily small with high probability. To our knowledge, this is the first work to provide a computationally efficient estimator with such a vanishing-error guarantee for a mixed-membership extension of the Gaussian mixture model. Extensive experimental studies demonstrate that our method outperforms existing approaches that ignore mixed memberships.
匹配关键词: mixture of experts
---

[ACADEMIC - ARXIV]
标题: QDTraj: Exploration of Diverse Trajectory Primitives for Articulated Objects Robotic Manipulation
作者: Mathilde Kappel, Mahdi Khoramshahi, Louis Annabi, Faiz Ben Amar, Stéphane Doncieux
链接: https://arxiv.org/abs/2604.22551v1
完整摘要: Thanks to the latest advances in learning and robotics, domestic robots are beginning to enter homes, aiming to execute household chores autonomously. However, robots still struggle to perform autonomous manipulation tasks in open-ended environments. In this context, this paper presents a method that enables a robot to manipulate a wide spectrum of articulated objects. In this paper, we automatically generate different robot low-level trajectory primitives to manipulate given object articulations. A very important point when it comes to generating expert trajectories is to consider the diversity of solutions to achieve the same goal. Indeed, knowing diverse low-level primitives to accomplish the same task enables the robot to choose the optimal solution in its real-world environment, with live constraints and unexpected changes. To do so, we propose a method based on Quality-Diversity algorithms that leverages sparse reward exploration in order to generate a set of diverse and high-performing trajectory primitives for a given manipulation task. We validated our method, QDTraj, by generating diverse trajectories in simulation and deploying them in the real world. QDTraj generates at least 5 times more diverse trajectories for both hinge and slider activation tasks, outperforming the other methods we compared against. We assessed the generalization of our method over 30 articulations of the PartNetMobility articulated object dataset, with an average of 704 different trajectories by task. Code is publicly available at: https://kappel.web.isir.upmc.fr/trajectory_primitive_website
匹配关键词: mixture of experts
---

[ACADEMIC - ARXIV]
标题: Aggregate vs. Personalized Judges in Business Idea Evaluation: Evidence from Expert Disagreement
作者: Wataru Hirota, Tomoki Taniguchi, Tomoko Ohkuma, Kosuke Takahashi, Takahiro Omi, Kosuke Arima, Takuto Asakura, Chung-Chi Chen, Tatsuya Ishigaki
链接: https://arxiv.org/abs/2604.22517v1
完整摘要: Evaluating LLM-generated business ideas is often harder to scale than generating them. Unlike standard NLP benchmarks, business idea evaluation relies on multi-dimensional criteria such as feasibility, novelty, differentiation, user need, and market size, and expert judgments often disagree. This paper studies a methodological question raised by such disagreement: should an automatic judge approximate an aggregate consensus, or model evaluators individually? We introduce PBIG-DATA, a dataset of approximately 3,000 individual scores across 300 patent-grounded product ideas, provided by domain experts on six business-oriented dimensions: specificity, technical validity, innovativeness, competitive advantage, need validity, and market size. Analyses show substantial expert disagreement on fine-grained ordinal scores, while agreement is higher under coarse selection, suggesting structured heterogeneity rather than random noise. We then compare three judge configurations: a rubric-only zero-shot judge, an aggregate judge conditioned on mixed evaluator histories, and a personalized judge conditioned on the target evaluator's scoring history. Across dimensions and model sizes, personalized judges align more closely with the corresponding evaluator than aggregate judges, and evaluator agreement correlates with similarity of judge-generated reasoning only under personalized conditioning. These results indicate that pooled labels can be a fragile target in pluralistic evaluation settings and motivate evaluator-conditioned judge designs for business idea assessment.
匹配关键词: mixture of experts
---

[ACADEMIC - ARXIV]
标题: Inter-Stance: A Dyadic Multimodal Corpus for Conversational Stance Analysis
作者: Xiang Zhang, Xiaotian Li, Taoyue Wang, Nan Bi, Xin Zhou, Cody Zhou, Zoie Wang, Andrew Yang, Yuming Su, Jeff Cohn, Qiang Ji, Lijun Yin
链接: https://arxiv.org/abs/2604.22739v1
完整摘要: Social interactions dominate our perceptions of the world and shape our daily behavior by attaching social meaning to acts as simple and spontaneous as gestures, facial expressions, voice, and speech. People mimic and otherwise respond to each other's postures, facial expressions, mannerisms, and other verbal and nonverbal behavior, and form appraisals or evaluations in the process. Yet, no publicly-available dataset includes multimodal recordings and self-report measures of multiple persons in social interaction. Dyadic recordings and annotation are lacking. We present a new data corpus of multimodal dyadic interaction (45 dyads, 90 persons) that includes synchronized multi-modality behavior (2D face video, 3D face geometry, thermal spectrum dynamics, voice and speech behavior, physiology (PPG, EDA, heart-rate, blood pressure, and respiration), and self-reported affect of all participants in a communicative interaction scenario. Two types of dyads are included: persons with shared past history and strangers. Annotations include social signals, agreement, disagreement, and neutral stance. With a potent emotion induction, these multimodal data will enable novel modeling of multimodal interpersonal behavior. We present extensive experiments to evaluate multimodal dyadic communication of dyads with and without interpersonal history, and their affect. This new database will make multimodal modeling of social interaction never possible before. The dataset includes 20TB of multimodal data to share with the research community.
匹配关键词: multimodal
---

[ACADEMIC - ARXIV]
标题: BERAG: Bayesian Ensemble Retrieval-Augmented Generation for Knowledge-based Visual Question Answering
作者: Jinghong Chen, Jingbiao Mei, Guangyu Yang, Bill Byrne
链接: https://arxiv.org/abs/2604.22678v1
完整摘要: A common approach to question answering with retrieval-augmented generation (RAG) is to concatenate documents into a single context and pass it to a language model to generate an answer. While simple, this strategy can obscure the contribution of individual documents, making attribution difficult and contributing to the ``lost-in-the-middle'' effect, where relevant information in long contexts is overlooked. Concatenation also scales poorly: computational cost grows quadratically with context length, a problem that becomes especially severe when the context includes visual data, as in visual question answering. Attempts to mitigate these issues by limiting context length can further restrict performance by preventing models from benefiting from the improved recall offered by deeper retrieval. We propose Bayesian Ensemble Retrieval-Augmented Generation (BERAG), along with Bayesian Ensemble Fine-Tuning (BEFT), as a RAG framework in which language models are conditioned on individual retrieved documents rather than a single combined context. BERAG treats document posterior probabilities as ensemble weights and updates them token by token using Bayes' rule during generation. This approach enables probabilistic re-ranking, parallel memory usage, and clear attribution of document contribution, making it well-suited for large document collections. We evaluate BERAG and BEFT primarily on knowledge-based visual question answering tasks, where models must reason over long, imperfect retrieval lists. The results show substantial improvements over standard RAG, including strong gains on Document Visual Question Answering and multimodal needle-in-a-haystack benchmarks. We also demonstrate that BERAG mitigates the ``lost-in-the-middle'' effect. The document posterior can be used to detect insufficient grounding and trigger deflection, while document pruning enables faster decoding than standard RAG.
匹配关键词: multimodal
---

[ACADEMIC - ARXIV]
标题: SpikingBrain2.0: Brain-Inspired Foundation Models for Efficient Long-Context and Cross-Platform Inference
作者: Yuqi Pan, Jinghao Zhuang, Yupeng Feng, Fangzhi Zhong, Siyu Ding, Xuerui Qiu, Shaowei Gu, Bohan Sun, Zhiyong Qin, Yibo Zhong, Lingtao Ouyang, Kun Yang, Zehao Liu, Yuhong Chou, Shurong Wang, Anjie Hu, Han Xu, Bo Xu, Guoqi Li
链接: https://arxiv.org/abs/2604.22575v1
完整摘要: Scaling context length is reshaping large-model development, yet full-attention Transformers suffer from prohibitive computation and inference bottlenecks at long sequences. A key challenge is to design foundation models that maintain performance and long-context efficiency with minimal training overhead. We introduce SpikingBrain2.0 (SpB2.0), a 5B model that advances both architecture and training efficiency of its predecessor. Our contributions are two-fold. (1) Architectural Innovation: We propose Dual-Space Sparse Attention (DSSA), an inter-layer hybrid of Sparse Softmax Attention (MoBA) and Sparse Linear Attention (SSE), achieving an improved performance-efficiency trade-off for long-context modeling. SpB2.0 further supports dual quantization paths: INT8-Spiking coding enables sparse event-driven computation, while FP8 coding accelerates inference on modern GPUs. (2) Enhanced Training Strategy: We develop an optimized Transformer-to-Hybrid (T2H) pipeline with dual conversion paths for LLMs and VLMs using curated open-source data. Empirically, SpB2.0-5B and SpB2.0-VL-5B recover most of the base Transformer (Qwen3-4B) capability with under 7k A100 GPU hours. SpB2.0 achieves a 10.13x TTFT speedup at 4M context and supports over 10M tokens on 8 A100 GPUs under vLLM, where full-attention models exceed memory limits. It also demonstrates strong cross-platform compatibility, enabling FP8 GPU inference (2.52x speedup at 250k) and efficient neuromorphic execution (64.31% sparsity, with 70.6% and 46.5% area and power reduction at 500MHz). Overall, SpikingBrain2.0 provides a practical pathway for lightweight, multimodal, spiking foundation models, highlighting the potential of combining brain-inspired mechanisms with efficient architectures for resource-constrained and edge scenarios.
匹配关键词: multimodal
---

[ACADEMIC - ARXIV]
标题: SOLAR-RL: Semi-Online Long-horizon Assignment Reinforcement Learning
作者: Jichao Wang, Liuyang Bian, Yufeng Zhou, Han Xiao, Yue Pan, Guozhi Wang, Hao Wang, Zhaoxiong Wang, Yafei Wen, Xiaoxin Chen, Shuai Ren, Lingfang Zeng
链接: https://arxiv.org/abs/2604.22558v1
完整摘要: As Multimodal Large Language Models (MLLMs) mature, GUI agents are evolving from static interactions to complex navigation. While Reinforcement Learning (RL) has emerged as a promising paradigm for training MLLM agents on dynamic GUI tasks, its effective application faces a dilemma. Standard Offline RL often relies on static step-level data, neglecting global trajectory semantics such as task completion and execution quality. Conversely, Online RL captures the long-term dynamics but suffers from high interaction costs and potential environmental instability. To bridge this gap, we propose SOLAR-RL (Semi-Online Long-horizon Assignment Reinforcement Learning). Instead of relying solely on expensive online interactions, our framework integrates global trajectory insights directly into the offline learning process. Specifically, we reconstruct diverse rollout candidates from static data, detect the first failure point using per-step validity signals, and retroactively assign dense step-level rewards with target-aligned shaping to reflect trajectory-level execution quality, effectively simulating online feedback without interaction costs. Extensive experiments demonstrate that SOLAR-RL significantly improves long-horizon task completion rates and robustness compared to strong baselines, offering a sample-efficient solution for autonomous GUI navigation.
匹配关键词: multimodal
---

[ACADEMIC - ARXIV]
标题: CGC: Compositional Grounded Contrast for Fine-Grained Multi-Image Understanding
作者: Lihao Zheng, Zhenwei Shao, Yu Zhou, Yan Yang, Xintian Shen, Jiawei Chen, Hao Ma, Tao Wei
链接: https://arxiv.org/abs/2604.22498v1
完整摘要: Although Multimodal Large Language Models (MLLMs) have advanced rapidly, they still face notable challenges in fine-grained multi-image understanding, often exhibiting spatial hallucination, attention leakage, and failures in object constancy. In addition, existing approaches typically rely on expensive human annotations or large-scale chain-of-thought (CoT) data generation. We propose Compositional Grounded Contrast (abbr. CGC), a low-cost full framework for boosting fine-grained multi-image understanding of MLLMs. Built on existing single-image grounding annotations, CGC constructs compositional multi-image training instances through Inter-Image Contrast and Intra-Image Contrast, which introduce semantically decoupled distractor contexts for cross-image discrimination and correlated cross-view samples for object constancy, respectively. CGC further introduces a Rule-Based Spatial Reward within the GRPO framework to improve source-image attribution, spatial alignment, and structured output validity under a Think-before-Grounding paradigm. Experiments show that CGC achieves state-of-the-art results on fine-grained multi-image benchmarks, including MIG-Bench and VLM2-Bench. The learned multi-image understanding capability also transfers to broader multimodal understanding and reasoning tasks, yielding consistent gains over the Qwen3-VL-8B base model on MathVista (+2.90), MuirBench (+2.88), MMStar (+1.93), MMMU (+1.77), and BLINK (+1.69).
匹配关键词: multimodal
---

[ACADEMIC - ARXIV]
标题: How Do AI Agents Spend Your Money? Analyzing and Predicting Token Consumption in Agentic Coding Tasks
作者: Longju Bai, Zhemin Huang, Xingyao Wang, Jiao Sun, Rada Mihalcea, Erik Brynjolfsson, Alex Pentland, Jiaxin Pei
链接: https://arxiv.org/abs/2604.22750v1
完整摘要: The wide adoption of AI agents in complex human workflows is driving rapid growth in LLM token consumption. When agents are deployed on tasks that require a significant amount of tokens, three questions naturally arise: (1) Where do AI agents spend the tokens? (2) Which models are more token-efficient? and (3) Can agents predict their token usage before task execution? In this paper, we present the first systematic study of token consumption patterns in agentic coding tasks. We analyze trajectories from eight frontier LLMs on SWE-bench Verified and evaluate models' ability to predict their own token costs before task execution. We find that: (1) agentic tasks are uniquely expensive, consuming 1000x more tokens than code reasoning and code chat, with input tokens rather than output tokens driving the overall cost; (2) token usage is highly variable and inherently stochastic: runs on the same task can differ by up to 30x in total tokens, and higher token usage does not translate into higher accuracy; instead, accuracy often peaks at intermediate cost and saturates at higher costs; (3) models vary substantially in token efficiency: on the same tasks, Kimi-K2 and Claude-Sonnet-4.5, on average, consume over 1.5 million more tokens than GPT-5; (4) task difficulty rated by human experts only weakly aligns with actual token costs, revealing a fundamental gap between human-perceived complexity and the computational effort agents actually expend; and (5) frontier models fail to accurately predict their own token usage (with weak-to-moderate correlations, up to 0.39) and systematically underestimate real token costs. Our study offers new insights into the economics of AI agents and can inspire future research in this direction.
匹配关键词: vision language model
---

[ACADEMIC - ARXIV]
标题: Representational Harms in LLM-Generated Narratives Against Global Majority Nationalities
作者: Ilana Nguyen, Harini Suresh, Thema Monroe-White, Evan Shieh
链接: https://arxiv.org/abs/2604.22749v1
完整摘要: Large language models (LLMs) are increasingly used for text generation tasks from everyday use to high-stakes enterprise and government applications, including simulated interviews with asylum seekers. While many works highlight the new potential applications of LLMs, there are risks of LLMs encoding and perpetuating harmful biases about non-dominant communities across the globe. To better evaluate and mitigate such harms, more research examining how LLMs portray diverse individuals is needed. In this work, we study how national origin identities are portrayed by widely-adopted LLMs in response to open-ended narrative generation prompts. Our findings demonstrate the presence of persistent representational harms by national origin, including harmful stereotypes, erasure, and one-dimensional portrayals of Global Majority identities. Minoritized national identities are simultaneously underrepresented in power-neutral stories and overrepresented in subordinated character portrayals, which are over fifty times more likely to appear than dominant portrayals. The degree of harm is amplified when US nationality cues (e.g., ``American'') are present in input prompts. Notably, we find that the harms we identify cannot be explained away via sycophancy, as US-centric biases persist even when replacing US nationality cues with non-US national identities in the prompts. Based on our findings, we call for further exploration of cultural harms in LLMs through methodologies that center Global Majority perspectives and challenge the uncritical adoption of US-based LLMs for the classification, surveillance, and misrepresentation of the majority of our planet.
匹配关键词: vision language model
---

[ACADEMIC - ARXIV]
标题: Agentic World Modeling: Foundations, Capabilities, Laws, and Beyond
作者: Meng Chu, Xuan Billy Zhang, Kevin Qinghong Lin, Lingdong Kong, Jize Zhang, Teng Tu, Weijian Ma, Ziqi Huang, Senqiao Yang, Wei Huang, Yeying Jin, Zhefan Rao, Jinhui Ye, Xinyu Lin, Xichen Zhang, Qisheng Hu, Shuai Yang, Leyang Shen, Wei Chow, Yifei Dong, Fengyi Wu, Quanyu Long, Bin Xia, Shaozuo Yu, Mingkang Zhu, Wenhu Zhang, Jiehui Huang, Haokun Gui, Haoxuan Che, Long Chen, Qifeng Chen, Wenxuan Zhang, Wenya Wang, Xiaojuan Qi, Yang Deng, Yanwei Li, Mike Zheng Shou, Zhi-Qi Cheng, See-Kiong Ng, Ziwei Liu, Philip Torr, Jiaya Jia
链接: https://arxiv.org/abs/2604.22748v1
完整摘要: As AI systems move from generating text to accomplishing goals through sustained interaction, the ability to model environment dynamics becomes a central bottleneck. Agents that manipulate objects, navigate software, coordinate with others, or design experiments require predictive environment models, yet the term world model carries different meanings across research communities. We introduce a "levels x laws" taxonomy organized along two axes. The first defines three capability levels: L1 Predictor, which learns one-step local transition operators; L2 Simulator, which composes them into multi-step, action-conditioned rollouts that respect domain laws; and L3 Evolver, which autonomously revises its own model when predictions fail against new evidence. The second identifies four governing-law regimes: physical, digital, social, and scientific. These regimes determine what constraints a world model must satisfy and where it is most likely to fail. Using this framework, we synthesize over 400 works and summarize more than 100 representative systems spanning model-based reinforcement learning, video generation, web and GUI agents, multi-agent social simulation, and AI-driven scientific discovery. We analyze methods, failure modes, and evaluation practices across level-regime pairs, propose decision-centric evaluation principles and a minimal reproducible evaluation package, and outline architectural guidance, open problems, and governance challenges. The resulting roadmap connects previously isolated communities and charts a path from passive next-step prediction toward world models that can simulate, and ultimately reshape, the environments in which agents operate.
匹配关键词: vision language model
---

[ACADEMIC - ARXIV]
标题: Relaxation-Informed Training of Neural Network Surrogate Models
作者: Calvin Tsay
链接: https://arxiv.org/abs/2604.22746v1
完整摘要: ReLU neural networks trained as surrogate models can be embedded exactly in mixed-integer linear programs (MILPs), enabling global optimization over the learned function. The tractability of the resulting MILP depends on structural properties of the network, i.e., the number of binary variables in associated formulations and the tightness of the continuous LP relaxation. These properties are determined during training, yet standard training objectives (prediction loss with classical weight regularization) offer no mechanism to directly control them. This work studies training regularizers that directly target downstream MILP tractability. Specifically, we propose simple bound-based regularizers that penalize the big-M constants of MILP formulations and/or the number of unstable neurons. Moreover, we introduce an LP relaxation gap regularizer that explicitly penalizes the per-sample gap of the continuous relaxation at training points. We derive its associated gradient and provide an implementation from LP dual variables without custom automatic differentiation tools. We show that combining the above regularizers can approximate the full total derivative of the LP gap with respect to the network parameters, capturing both direct and indirect sensitivities. Experiments on non-convex benchmark functions and a two-stage stochastic programming problem with quantile neural network surrogates demonstrate that the proposed regularizers can reduce MILP solve times by up to four orders of magnitude relative to an unregularized baseline, while maintaining competitive surrogate model accuracy.
匹配关键词: vision language model
---

[ACADEMIC - ARXIV]
标题: Inter-Stance: A Dyadic Multimodal Corpus for Conversational Stance Analysis
作者: Xiang Zhang, Xiaotian Li, Taoyue Wang, Nan Bi, Xin Zhou, Cody Zhou, Zoie Wang, Andrew Yang, Yuming Su, Jeff Cohn, Qiang Ji, Lijun Yin
链接: https://arxiv.org/abs/2604.22739v1
完整摘要: Social interactions dominate our perceptions of the world and shape our daily behavior by attaching social meaning to acts as simple and spontaneous as gestures, facial expressions, voice, and speech. People mimic and otherwise respond to each other's postures, facial expressions, mannerisms, and other verbal and nonverbal behavior, and form appraisals or evaluations in the process. Yet, no publicly-available dataset includes multimodal recordings and self-report measures of multiple persons in social interaction. Dyadic recordings and annotation are lacking. We present a new data corpus of multimodal dyadic interaction (45 dyads, 90 persons) that includes synchronized multi-modality behavior (2D face video, 3D face geometry, thermal spectrum dynamics, voice and speech behavior, physiology (PPG, EDA, heart-rate, blood pressure, and respiration), and self-reported affect of all participants in a communicative interaction scenario. Two types of dyads are included: persons with shared past history and strangers. Annotations include social signals, agreement, disagreement, and neutral stance. With a potent emotion induction, these multimodal data will enable novel modeling of multimodal interpersonal behavior. We present extensive experiments to evaluate multimodal dyadic communication of dyads with and without interpersonal history, and their affect. This new database will make multimodal modeling of social interaction never possible before. The dataset includes 20TB of multimodal data to share with the research community.
匹配关键词: vision language model
---

[ACADEMIC - ARXIV]
标题: SpikingBrain2.0: Brain-Inspired Foundation Models for Efficient Long-Context and Cross-Platform Inference
作者: Yuqi Pan, Jinghao Zhuang, Yupeng Feng, Fangzhi Zhong, Siyu Ding, Xuerui Qiu, Shaowei Gu, Bohan Sun, Zhiyong Qin, Yibo Zhong, Lingtao Ouyang, Kun Yang, Zehao Liu, Yuhong Chou, Shurong Wang, Anjie Hu, Han Xu, Bo Xu, Guoqi Li
链接: https://arxiv.org/abs/2604.22575v1
完整摘要: Scaling context length is reshaping large-model development, yet full-attention Transformers suffer from prohibitive computation and inference bottlenecks at long sequences. A key challenge is to design foundation models that maintain performance and long-context efficiency with minimal training overhead. We introduce SpikingBrain2.0 (SpB2.0), a 5B model that advances both architecture and training efficiency of its predecessor. Our contributions are two-fold. (1) Architectural Innovation: We propose Dual-Space Sparse Attention (DSSA), an inter-layer hybrid of Sparse Softmax Attention (MoBA) and Sparse Linear Attention (SSE), achieving an improved performance-efficiency trade-off for long-context modeling. SpB2.0 further supports dual quantization paths: INT8-Spiking coding enables sparse event-driven computation, while FP8 coding accelerates inference on modern GPUs. (2) Enhanced Training Strategy: We develop an optimized Transformer-to-Hybrid (T2H) pipeline with dual conversion paths for LLMs and VLMs using curated open-source data. Empirically, SpB2.0-5B and SpB2.0-VL-5B recover most of the base Transformer (Qwen3-4B) capability with under 7k A100 GPU hours. SpB2.0 achieves a 10.13x TTFT speedup at 4M context and supports over 10M tokens on 8 A100 GPUs under vLLM, where full-attention models exceed memory limits. It also demonstrates strong cross-platform compatibility, enabling FP8 GPU inference (2.52x speedup at 250k) and efficient neuromorphic execution (64.31% sparsity, with 70.6% and 46.5% area and power reduction at 500MHz). Overall, SpikingBrain2.0 provides a practical pathway for lightweight, multimodal, spiking foundation models, highlighting the potential of combining brain-inspired mechanisms with efficient architectures for resource-constrained and edge scenarios.
匹配关键词: VLM
---

[ACADEMIC - ARXIV]
标题: Cross-Stage Coherence in Hierarchical Driving VQA: Explicit Baselines and Learned Gated Context Projectors
作者: Gautam Kumar Jain, Carsten Markgraf, Julian Stähler
链接: https://arxiv.org/abs/2604.22560v1
完整摘要: Graph Visual Question Answering (GVQA) for autonomous driving organizes reasoning into ordered stages, namely Perception, Prediction, and Planning, where planning decisions should remain consistent with the model's own perception. We present a comparative study of cross-stage context passing on DriveLM-nuScenes using two complementary mechanisms. The explicit variant evaluates three prompt-based conditioning strategies on a domain-adapted 4B VLM (Mini-InternVL2-4B-DA-DriveLM) without additional training, reducing NLI contradiction by up to 42.6% and establishing a strong zero-training baseline. The implicit variant introduces gated context projectors, which extract a hidden-state vector from one stage and inject a normalized, gated projection into the next stage's input embeddings. These projectors are jointly trained with stage-specific QLoRA adapters on a general-purpose 8B VLM (InternVL3-8B-Instruct) while updating only approximately 0.5% of parameters. The implicit variant achieves a statistically significant 34% reduction in planning-stage NLI contradiction (bootstrap 95% CIs, p < 0.05) and increases cross-stage entailment by 50%, evaluated with a multilingual NLI classifier to account for mixed-language outputs. Planning language quality also improves (CIDEr +30.3%), but lexical overlap and structural consistency degrade due to the absence of driving-domain pretraining. Since the two variants use different base models, we present them as complementary case studies: explicit context passing provides a strong training-free baseline for surface consistency, while implicit gated projection delivers significant planning-stage semantic gains, suggesting domain adaptation as a plausible next ingredient for full-spectrum improvement.
匹配关键词: VLM
---

[ACADEMIC - ARXIV]
标题: Contrastive Semantic Projection: Faithful Neuron Labeling with Contrastive Examples
作者: Oussama Bouanani, Jim Berend, Wojciech Samek, Sebastian Lapuschkin, Maximilian Dreyer
链接: https://arxiv.org/abs/2604.22477v1
完整摘要: Neuron labeling assigns textual descriptions to internal units of deep networks. Existing approaches typically rely on highly activating examples, often yielding broad or misleading labels by focusing on dominant but incidental visual factors. Prior work such as FALCON introduced contrastive examples -- inputs that are semantically similar to activating examples but elicit low activations -- to sharpen explanations, but it primarily addresses subspace-level interpretability rather than scalable neuron-level labeling. We revisit contrastive explanations for neuron-level labeling in two stages: (1) candidate label generation with vision language models (VLMs) and (2) label assignment with CLIP-like encoders. First, we show that providing contrastive image sets to VLMs yields candidate labels that are more specific and more faithful. Second, we introduce Contrastive Semantic Projection (CSP), an extension of SemanticLens that incorporates contrastive examples directly into its CLIP-based scoring and selection pipeline. Across extensive experiments and a case study on melanoma detection, contrastive labeling improves both faithfulness and semantic granularity over state-of-the-art baselines. Our results demonstrate that contrastive examples are a simple yet powerful and currently underutilized component of neuron labeling and analysis pipelines.
匹配关键词: VLM
---

[ACADEMIC - ARXIV]
标题: SpaMEM: Benchmarking Dynamic Spatial Reasoning via Perception-Memory Integration in Embodied Environments
作者: Chih-Ting Liao, Xi Xiao, Chunlei Meng, Zhangquan Chen, Yitong Qiao, Weilin Zhou, Tianyang Wang, Xu Zheng, Xin Cao
链接: https://arxiv.org/abs/2604.22409v1
完整摘要: Multimodal large language models (MLLMs) have advanced static visual--spatial reasoning, yet they often fail to preserve long-horizon spatial coherence in embodied settings where beliefs must be continuously revised from egocentric observations under environmental change. We introduce SpaMEM (Spatial Memory from Action Sequences), a large-scale diagnostic benchmark that isolates the mechanics of spatial belief evolution via action-conditioned scene transformations (spawn, place, remove) over long interaction horizons. SpaMEM is built on a physically grounded dataset with 10,601,392 high-fidelity images across four modalities (RGB, depth, instance, semantic segmentation), collected from 25,000+ interaction sequences in 1,000 procedurally generated houses. We formalize embodied spatial reasoning as a three-level hierarchy with 15 diagnostic tasks: Level 1 measures atomic spatial perception from single observations; Level 2 probes temporal reasoning with oracle textual state histories to factor out perceptual noise; and Level 3 requires end-to-end belief maintenance from raw visual streams under the same task dimensions. We further evaluate both short-term (step-wise) updates and long-term (episodic) reconstruction. Benchmarking representative open-source VLM families reveals a consistent stacked bottleneck: coordinate-consistent grounding remains a hard ceiling, and the sharp collapse from Level 2 to Level 3 exposes a pronounced symbolic scaffolding dependency, where models succeed with text-based bookkeeping but struggle to sustain robust visual memory. SpaMEM provides a granular diagnostic standard and motivates explicit mechanisms for state representation, belief revision, and long-horizon episodic integration.
匹配关键词: VLM
---

[ACADEMIC - ARXIV]
标题: OccDirector: Language-Guided Behavior and Interaction Generation in 4D Occupancy Space
作者: Zhuding Liang, Tianyi Yan, Dubing Chen, Jiasen Zheng, Huan Zheng, Cheng-zhong Xu, Yida Wang, Kun Zhan, Jianbing Shen
链接: https://arxiv.org/abs/2604.22240v1
完整摘要: Generative world models increasingly rely on 4D occupancy for realistic autonomous driving simulation. However, existing generation frameworks depend on rigid geometric conditions (e.g., explicit trajectories) or simplistic attribute-level text, failing to orchestrate complex, sequential multi-agent interactions. To address this semantic-spatiotemporal gap, we propose OccDirector, a pioneering framework that generates 4D occupancy dynamics conditioned solely on natural language. Operating as a ``scenario director'', OccDirector maps natural language scripts into physically plausible voxel dynamics without requiring geometric priors. Technically, it employs a VLM-driven Spatio-Temporal MMDiT equipped with a history-prefix anchoring strategy to ensure long-horizon interaction consistency. Furthermore, we introduce OccInteract-85k, a novel dataset uniquely annotated with multi-level language instructions: ranging from static layouts to intricate multi-agent behaviors, alongside a novel VLM-based evaluation benchmark. Extensive experiments demonstrate that OccDirector achieves state-of-the-art generation quality and unprecedented instruction-following capabilities, successfully shifting the paradigm from appearance synthesis to language-driven behavior orchestration.
匹配关键词: VLM
---

[ACADEMIC - ARXIV]
标题: Representational Harms in LLM-Generated Narratives Against Global Majority Nationalities
作者: Ilana Nguyen, Harini Suresh, Thema Monroe-White, Evan Shieh
链接: https://arxiv.org/abs/2604.22749v1
完整摘要: Large language models (LLMs) are increasingly used for text generation tasks from everyday use to high-stakes enterprise and government applications, including simulated interviews with asylum seekers. While many works highlight the new potential applications of LLMs, there are risks of LLMs encoding and perpetuating harmful biases about non-dominant communities across the globe. To better evaluate and mitigate such harms, more research examining how LLMs portray diverse individuals is needed. In this work, we study how national origin identities are portrayed by widely-adopted LLMs in response to open-ended narrative generation prompts. Our findings demonstrate the presence of persistent representational harms by national origin, including harmful stereotypes, erasure, and one-dimensional portrayals of Global Majority identities. Minoritized national identities are simultaneously underrepresented in power-neutral stories and overrepresented in subordinated character portrayals, which are over fifty times more likely to appear than dominant portrayals. The degree of harm is amplified when US nationality cues (e.g., ``American'') are present in input prompts. Notably, we find that the harms we identify cannot be explained away via sycophancy, as US-centric biases persist even when replacing US nationality cues with non-US national identities in the prompts. Based on our findings, we call for further exploration of cultural harms in LLMs through methodologies that center Global Majority perspectives and challenge the uncritical adoption of US-based LLMs for the classification, surveillance, and misrepresentation of the majority of our planet.
匹配关键词: image generation
---

[ACADEMIC - ARXIV]
标题: Agentic World Modeling: Foundations, Capabilities, Laws, and Beyond
作者: Meng Chu, Xuan Billy Zhang, Kevin Qinghong Lin, Lingdong Kong, Jize Zhang, Teng Tu, Weijian Ma, Ziqi Huang, Senqiao Yang, Wei Huang, Yeying Jin, Zhefan Rao, Jinhui Ye, Xinyu Lin, Xichen Zhang, Qisheng Hu, Shuai Yang, Leyang Shen, Wei Chow, Yifei Dong, Fengyi Wu, Quanyu Long, Bin Xia, Shaozuo Yu, Mingkang Zhu, Wenhu Zhang, Jiehui Huang, Haokun Gui, Haoxuan Che, Long Chen, Qifeng Chen, Wenxuan Zhang, Wenya Wang, Xiaojuan Qi, Yang Deng, Yanwei Li, Mike Zheng Shou, Zhi-Qi Cheng, See-Kiong Ng, Ziwei Liu, Philip Torr, Jiaya Jia
链接: https://arxiv.org/abs/2604.22748v1
完整摘要: As AI systems move from generating text to accomplishing goals through sustained interaction, the ability to model environment dynamics becomes a central bottleneck. Agents that manipulate objects, navigate software, coordinate with others, or design experiments require predictive environment models, yet the term world model carries different meanings across research communities. We introduce a "levels x laws" taxonomy organized along two axes. The first defines three capability levels: L1 Predictor, which learns one-step local transition operators; L2 Simulator, which composes them into multi-step, action-conditioned rollouts that respect domain laws; and L3 Evolver, which autonomously revises its own model when predictions fail against new evidence. The second identifies four governing-law regimes: physical, digital, social, and scientific. These regimes determine what constraints a world model must satisfy and where it is most likely to fail. Using this framework, we synthesize over 400 works and summarize more than 100 representative systems spanning model-based reinforcement learning, video generation, web and GUI agents, multi-agent social simulation, and AI-driven scientific discovery. We analyze methods, failure modes, and evaluation practices across level-regime pairs, propose decision-centric evaluation principles and a minimal reproducible evaluation package, and outline architectural guidance, open problems, and governance challenges. The resulting roadmap connects previously isolated communities and charts a path from passive next-step prediction toward world models that can simulate, and ultimately reshape, the environments in which agents operate.
匹配关键词: image generation
---

[ACADEMIC - ARXIV]
标题: GCImOpt: Learning efficient goal-conditioned policies by imitating optimal trajectories
作者: Jon Goikoetxea, Jesús F. Palacián
链接: https://arxiv.org/abs/2604.22724v1
完整摘要: Imitation learning is a well-established approach for machine-learning-based control. However, its applicability depends on having access to demonstrations, which are often expensive to collect and/or suboptimal for solving the task. In this work, we present GCImOpt, an approach to learn efficient goal-conditioned policies by training on datasets generated by trajectory optimization. Our approach for dataset generation is computationally efficient, can generate thousands of optimal trajectories in minutes on a laptop computer, and produces high-quality demonstrations. Further, by means of a data augmentation scheme that treats intermediate states as goals, we are able to increase the training dataset size by an order of magnitude. Using our generated datasets, we train goal-conditioned neural network policies that can control the system towards arbitrary goals. To demonstrate the generality of our approach, we generate datasets and then train policies for various control tasks, namely cart-pole stabilization, planar and three-dimensional quadcopter stabilization, and point reaching using a 6-DoF robot arm. We show that our trained policies can achieve high success rates and near-optimal control profiles, all while being small (less than 80,000 neural network parameters) and fast enough (up to more than 6,000 times faster than a trajectory optimization solver) that they could be deployed onboard resource-constrained controllers. We provide videos, code, datasets and pre-trained policies under a free software license; see our project website https://jongoiko.github.io/gcimopt/.
匹配关键词: image generation
---

[ACADEMIC - ARXIV]
标题: Aligning Dense Retrievers with LLM Utility via DistillationAligning Dense Retrievers with LLM Utility via Distillation
作者: Rajinder Sandhu, Di Mu, Cheng Chang, Md Shahriar Tasjid, Himanshu Rai, Maksims Volkovs, Ga Wu
链接: https://arxiv.org/abs/2604.22722v1
完整摘要: Dense vector retrieval is the practical backbone of Retrieval- Augmented Generation (RAG), but similarity search can suffer from precision limitations. Conversely, utility-based approaches leveraging LLM re-ranking often achieve superior performance but are computationally prohibitive and prone to noise inherent in perplexity estimation. We propose Utility-Aligned Embeddings (UAE), a framework designed to merge these advantages into a practical, high-performance retrieval method. We formulate retrieval as a distribution matching problem, training a bi-encoder to imitate a utility distribution derived from perplexity reduction using a Utility-Modulated InfoNCE objective. This approach injects graded utility signals directly into the embedding space without requiring test-time LLM inference. On the QASPER benchmark, UAE improves retrieval Recall@1 by 30.59%, MAP by 30.16% and Token F1 by 17.3% over the strong semantic baseline BGE-Base. Crucially, UAE is over 180x faster than the efficient LLM re-ranking methods preserving competitive performance, demonstrating that aligning retrieval with generative utility yields reliable contexts at scale.
匹配关键词: image generation
---

[ACADEMIC - ARXIV]
标题: ATRS: Adaptive Trajectory Re-splitting via a Shared Neural Policy for Parallel Optimization
作者: Jiajun Yu, Guodong Liu, Li Wang, Pengxiang Zhou, Wentao Liu, Yin He, Chao Xu, Fei Gao, Yanjun Cao
链接: https://arxiv.org/abs/2604.22715v1
完整摘要: Parallel trajectory optimization via the Alternating Direction Method of Multipliers (ADMM) has emerged as a scalable approach to long-horizon motion planning. However, existing frameworks typically decompose the problem into parallel subproblems based on a predefined fixed structure. Such structural rigidity often causes optimization stagnation in highly constrained regions, where a few lagging subproblems delay global convergence. A natural remedy is to adaptively re-split these stagnating segments online. Yet, deciding when, where, and how to split exceeds the capability of rule-based heuristics. To this end, we propose ATRS, a novel framework that embeds a shared Deep Reinforcement Learning policy into the parallel ADMM loop. We formulate this adaptive adjustment as a Multi-Agent Shared-Policy Markov Decision Process, where all trajectory segments act as homogeneous agents and share a unified neural policy network. This parameter-sharing architecture endows the system with size invariance, enabling it to handle dynamically changing segment counts during re-splitting and generalize to arbitrary trajectory lengths. Furthermore, our formulation inherently supports zero-shot generalization to unseen environments, as our network relies solely on the internal states of the numerical solver rather than on the geometric features of the environment. To ensure solver stability, a Confidence-Based Election mechanism selects only the most stagnating segment for re-splitting at each step. Extensive simulations demonstrate that ATRS accelerates convergence, reducing the number of iterations by up to 26.0% and the computation time by up to 19.1%. Real-world experiments further confirm its applicability to both large-scale offline global planning and real-time onboard replanning within 35 ms per cycle, with no sim-to-real degradation.
匹配关键词: image generation
---

[ACADEMIC - ARXIV]
标题: Representational Harms in LLM-Generated Narratives Against Global Majority Nationalities
作者: Ilana Nguyen, Harini Suresh, Thema Monroe-White, Evan Shieh
链接: https://arxiv.org/abs/2604.22749v1
完整摘要: Large language models (LLMs) are increasingly used for text generation tasks from everyday use to high-stakes enterprise and government applications, including simulated interviews with asylum seekers. While many works highlight the new potential applications of LLMs, there are risks of LLMs encoding and perpetuating harmful biases about non-dominant communities across the globe. To better evaluate and mitigate such harms, more research examining how LLMs portray diverse individuals is needed. In this work, we study how national origin identities are portrayed by widely-adopted LLMs in response to open-ended narrative generation prompts. Our findings demonstrate the presence of persistent representational harms by national origin, including harmful stereotypes, erasure, and one-dimensional portrayals of Global Majority identities. Minoritized national identities are simultaneously underrepresented in power-neutral stories and overrepresented in subordinated character portrayals, which are over fifty times more likely to appear than dominant portrayals. The degree of harm is amplified when US nationality cues (e.g., ``American'') are present in input prompts. Notably, we find that the harms we identify cannot be explained away via sycophancy, as US-centric biases persist even when replacing US nationality cues with non-US national identities in the prompts. Based on our findings, we call for further exploration of cultural harms in LLMs through methodologies that center Global Majority perspectives and challenge the uncritical adoption of US-based LLMs for the classification, surveillance, and misrepresentation of the majority of our planet.
匹配关键词: video generation
---

[ACADEMIC - ARXIV]
标题: Agentic World Modeling: Foundations, Capabilities, Laws, and Beyond
作者: Meng Chu, Xuan Billy Zhang, Kevin Qinghong Lin, Lingdong Kong, Jize Zhang, Teng Tu, Weijian Ma, Ziqi Huang, Senqiao Yang, Wei Huang, Yeying Jin, Zhefan Rao, Jinhui Ye, Xinyu Lin, Xichen Zhang, Qisheng Hu, Shuai Yang, Leyang Shen, Wei Chow, Yifei Dong, Fengyi Wu, Quanyu Long, Bin Xia, Shaozuo Yu, Mingkang Zhu, Wenhu Zhang, Jiehui Huang, Haokun Gui, Haoxuan Che, Long Chen, Qifeng Chen, Wenxuan Zhang, Wenya Wang, Xiaojuan Qi, Yang Deng, Yanwei Li, Mike Zheng Shou, Zhi-Qi Cheng, See-Kiong Ng, Ziwei Liu, Philip Torr, Jiaya Jia
链接: https://arxiv.org/abs/2604.22748v1
完整摘要: As AI systems move from generating text to accomplishing goals through sustained interaction, the ability to model environment dynamics becomes a central bottleneck. Agents that manipulate objects, navigate software, coordinate with others, or design experiments require predictive environment models, yet the term world model carries different meanings across research communities. We introduce a "levels x laws" taxonomy organized along two axes. The first defines three capability levels: L1 Predictor, which learns one-step local transition operators; L2 Simulator, which composes them into multi-step, action-conditioned rollouts that respect domain laws; and L3 Evolver, which autonomously revises its own model when predictions fail against new evidence. The second identifies four governing-law regimes: physical, digital, social, and scientific. These regimes determine what constraints a world model must satisfy and where it is most likely to fail. Using this framework, we synthesize over 400 works and summarize more than 100 representative systems spanning model-based reinforcement learning, video generation, web and GUI agents, multi-agent social simulation, and AI-driven scientific discovery. We analyze methods, failure modes, and evaluation practices across level-regime pairs, propose decision-centric evaluation principles and a minimal reproducible evaluation package, and outline architectural guidance, open problems, and governance challenges. The resulting roadmap connects previously isolated communities and charts a path from passive next-step prediction toward world models that can simulate, and ultimately reshape, the environments in which agents operate.
匹配关键词: video generation
---

[ACADEMIC - ARXIV]
标题: Inter-Stance: A Dyadic Multimodal Corpus for Conversational Stance Analysis
作者: Xiang Zhang, Xiaotian Li, Taoyue Wang, Nan Bi, Xin Zhou, Cody Zhou, Zoie Wang, Andrew Yang, Yuming Su, Jeff Cohn, Qiang Ji, Lijun Yin
链接: https://arxiv.org/abs/2604.22739v1
完整摘要: Social interactions dominate our perceptions of the world and shape our daily behavior by attaching social meaning to acts as simple and spontaneous as gestures, facial expressions, voice, and speech. People mimic and otherwise respond to each other's postures, facial expressions, mannerisms, and other verbal and nonverbal behavior, and form appraisals or evaluations in the process. Yet, no publicly-available dataset includes multimodal recordings and self-report measures of multiple persons in social interaction. Dyadic recordings and annotation are lacking. We present a new data corpus of multimodal dyadic interaction (45 dyads, 90 persons) that includes synchronized multi-modality behavior (2D face video, 3D face geometry, thermal spectrum dynamics, voice and speech behavior, physiology (PPG, EDA, heart-rate, blood pressure, and respiration), and self-reported affect of all participants in a communicative interaction scenario. Two types of dyads are included: persons with shared past history and strangers. Annotations include social signals, agreement, disagreement, and neutral stance. With a potent emotion induction, these multimodal data will enable novel modeling of multimodal interpersonal behavior. We present extensive experiments to evaluate multimodal dyadic communication of dyads with and without interpersonal history, and their affect. This new database will make multimodal modeling of social interaction never possible before. The dataset includes 20TB of multimodal data to share with the research community.
匹配关键词: video generation
---

[ACADEMIC - ARXIV]
标题: GCImOpt: Learning efficient goal-conditioned policies by imitating optimal trajectories
作者: Jon Goikoetxea, Jesús F. Palacián
链接: https://arxiv.org/abs/2604.22724v1
完整摘要: Imitation learning is a well-established approach for machine-learning-based control. However, its applicability depends on having access to demonstrations, which are often expensive to collect and/or suboptimal for solving the task. In this work, we present GCImOpt, an approach to learn efficient goal-conditioned policies by training on datasets generated by trajectory optimization. Our approach for dataset generation is computationally efficient, can generate thousands of optimal trajectories in minutes on a laptop computer, and produces high-quality demonstrations. Further, by means of a data augmentation scheme that treats intermediate states as goals, we are able to increase the training dataset size by an order of magnitude. Using our generated datasets, we train goal-conditioned neural network policies that can control the system towards arbitrary goals. To demonstrate the generality of our approach, we generate datasets and then train policies for various control tasks, namely cart-pole stabilization, planar and three-dimensional quadcopter stabilization, and point reaching using a 6-DoF robot arm. We show that our trained policies can achieve high success rates and near-optimal control profiles, all while being small (less than 80,000 neural network parameters) and fast enough (up to more than 6,000 times faster than a trajectory optimization solver) that they could be deployed onboard resource-constrained controllers. We provide videos, code, datasets and pre-trained policies under a free software license; see our project website https://jongoiko.github.io/gcimopt/.
匹配关键词: video generation
---

[ACADEMIC - ARXIV]
标题: Aligning Dense Retrievers with LLM Utility via DistillationAligning Dense Retrievers with LLM Utility via Distillation
作者: Rajinder Sandhu, Di Mu, Cheng Chang, Md Shahriar Tasjid, Himanshu Rai, Maksims Volkovs, Ga Wu
链接: https://arxiv.org/abs/2604.22722v1
完整摘要: Dense vector retrieval is the practical backbone of Retrieval- Augmented Generation (RAG), but similarity search can suffer from precision limitations. Conversely, utility-based approaches leveraging LLM re-ranking often achieve superior performance but are computationally prohibitive and prone to noise inherent in perplexity estimation. We propose Utility-Aligned Embeddings (UAE), a framework designed to merge these advantages into a practical, high-performance retrieval method. We formulate retrieval as a distribution matching problem, training a bi-encoder to imitate a utility distribution derived from perplexity reduction using a Utility-Modulated InfoNCE objective. This approach injects graded utility signals directly into the embedding space without requiring test-time LLM inference. On the QASPER benchmark, UAE improves retrieval Recall@1 by 30.59%, MAP by 30.16% and Token F1 by 17.3% over the strong semantic baseline BGE-Base. Crucially, UAE is over 180x faster than the efficient LLM re-ranking methods preserving competitive performance, demonstrating that aligning retrieval with generative utility yields reliable contexts at scale.
匹配关键词: video generation
---

[ACADEMIC - ARXIV]
标题: How Do AI Agents Spend Your Money? Analyzing and Predicting Token Consumption in Agentic Coding Tasks
作者: Longju Bai, Zhemin Huang, Xingyao Wang, Jiao Sun, Rada Mihalcea, Erik Brynjolfsson, Alex Pentland, Jiaxin Pei
链接: https://arxiv.org/abs/2604.22750v1
完整摘要: The wide adoption of AI agents in complex human workflows is driving rapid growth in LLM token consumption. When agents are deployed on tasks that require a significant amount of tokens, three questions naturally arise: (1) Where do AI agents spend the tokens? (2) Which models are more token-efficient? and (3) Can agents predict their token usage before task execution? In this paper, we present the first systematic study of token consumption patterns in agentic coding tasks. We analyze trajectories from eight frontier LLMs on SWE-bench Verified and evaluate models' ability to predict their own token costs before task execution. We find that: (1) agentic tasks are uniquely expensive, consuming 1000x more tokens than code reasoning and code chat, with input tokens rather than output tokens driving the overall cost; (2) token usage is highly variable and inherently stochastic: runs on the same task can differ by up to 30x in total tokens, and higher token usage does not translate into higher accuracy; instead, accuracy often peaks at intermediate cost and saturates at higher costs; (3) models vary substantially in token efficiency: on the same tasks, Kimi-K2 and Claude-Sonnet-4.5, on average, consume over 1.5 million more tokens than GPT-5; (4) task difficulty rated by human experts only weakly aligns with actual token costs, revealing a fundamental gap between human-perceived complexity and the computational effort agents actually expend; and (5) frontier models fail to accurately predict their own token usage (with weak-to-moderate correlations, up to 0.39) and systematically underestimate real token costs. Our study offers new insights into the economics of AI agents and can inspire future research in this direction.
匹配关键词: visual reasoning
---

[ACADEMIC - ARXIV]
标题: Thinking Without Words: Efficient Latent Reasoning with Abstract Chain-of-Thought
作者: Keshav Ramji, Tahira Naseem, Ramón Fernandez Astudillo
链接: https://arxiv.org/abs/2604.22709v1
完整摘要: While long, explicit chains-of-thought (CoT) have proven effective on complex reasoning tasks, they are costly to generate during inference. Non-verbal reasoning methods have emerged with shorter generation lengths by leveraging continuous representations, yet their performance lags behind verbalized CoT. We propose $\textbf{Abstract Chain-of-Thought}$, a discrete latent reasoning post-training mechanism in which the language model produces a short sequence of tokens from a reserved vocabulary in lieu of a natural language CoT, before generating a response. To make previously unseen ''abstract'' tokens useful, we introduce a policy iteration-style warm-up loop that alternates between (i.) bottlenecking from a verbal CoT via masking and performing supervised fine-tuning, and (ii.) self-distillation by training the model to generate abstract tokens from the prompt alone via constrained decoding with the codebook. After warm-up, we optimize the generation of abstract sequences with warm-started reinforcement learning under constrained decoding. Abstract-CoT achieves up to $11.6\times$ fewer reasoning tokens while demonstrating comparable performance across mathematical reasoning, instruction-following, and multi-hop reasoning, and generalizes across language model families. We also find an emergent power law distribution over the abstract vocabulary, akin to those seen in natural language, that evolves across the training phases. Our findings highlight the potential for post-training latent reasoning mechanisms that enable efficient inference through a learned abstract reasoning language.
匹配关键词: visual reasoning
---

[ACADEMIC - ARXIV]
标题: BERAG: Bayesian Ensemble Retrieval-Augmented Generation for Knowledge-based Visual Question Answering
作者: Jinghong Chen, Jingbiao Mei, Guangyu Yang, Bill Byrne
链接: https://arxiv.org/abs/2604.22678v1
完整摘要: A common approach to question answering with retrieval-augmented generation (RAG) is to concatenate documents into a single context and pass it to a language model to generate an answer. While simple, this strategy can obscure the contribution of individual documents, making attribution difficult and contributing to the ``lost-in-the-middle'' effect, where relevant information in long contexts is overlooked. Concatenation also scales poorly: computational cost grows quadratically with context length, a problem that becomes especially severe when the context includes visual data, as in visual question answering. Attempts to mitigate these issues by limiting context length can further restrict performance by preventing models from benefiting from the improved recall offered by deeper retrieval. We propose Bayesian Ensemble Retrieval-Augmented Generation (BERAG), along with Bayesian Ensemble Fine-Tuning (BEFT), as a RAG framework in which language models are conditioned on individual retrieved documents rather than a single combined context. BERAG treats document posterior probabilities as ensemble weights and updates them token by token using Bayes' rule during generation. This approach enables probabilistic re-ranking, parallel memory usage, and clear attribution of document contribution, making it well-suited for large document collections. We evaluate BERAG and BEFT primarily on knowledge-based visual question answering tasks, where models must reason over long, imperfect retrieval lists. The results show substantial improvements over standard RAG, including strong gains on Document Visual Question Answering and multimodal needle-in-a-haystack benchmarks. We also demonstrate that BERAG mitigates the ``lost-in-the-middle'' effect. The document posterior can be used to detect insufficient grounding and trigger deflection, while document pruning enables faster decoding than standard RAG.
匹配关键词: visual reasoning
---

[ACADEMIC - ARXIV]
标题: Structure-Guided Diffusion Model for EEG-Based Visual Cognition Reconstruction
作者: Yongxiang Lian, Yueyang Cang, Pingge Hu, Yuchen He, Li Shi
链接: https://arxiv.org/abs/2604.22649v1
完整摘要: Objective: Decoding visual information from electroencephalography (EEG) is an important problem in neuroscience and brain-computer interface (BCI) research. Existing methods are largely restricted to natural images and categorical representations, with limited capacity to capture structural features and to differentiate objective perception from subjective cognition. We propose a Structure-Guided Diffusion Model (SGDM) that incorporates explicit structural information for EEG-based visual reconstruction. Approach: SGDM is evaluated on the Kilogram abstract visual object dataset and the THINGS natural image dataset using a two-stage generative mechanism. The framework combines a structurally supervised variational autoencoder with a spatiotemporal EEG encoder aligned to a visual embedding space via contrastive learning. Structural information is integrated into a diffusion model through ControlNet to guide image generation from EEG features. Results: SGDM outperforms existing methods on both abstract and natural image datasets. Reconstructed images achieve higher fidelity in low-level visual features and semantic representations, indicating improved decoding accuracy and strong generalization across diverse visual domains. Spatiotemporal analysis of EEG signals further reveals hierarchical structural encoding patterns, consistent with the neural dynamics of visual cognition. Significance: These findings validate the effectiveness of SGDM in capturing explicit structural geometry and generating images with high fidelity to individual cognitive representations. By enabling decoding of complex visual content from EEG signals, the framework extends neural decoding beyond low-dimensional or categorical outputs. This supports BCIs with increased degrees of freedom for intention decoding and more flexible brain-to-machine communication.
匹配关键词: visual reasoning
---

[ACADEMIC - ARXIV]
标题: GazeVLA: Learning Human Intention for Robotic Manipulation
作者: Chengyang Li, Kaiyi Xiong, Yuan Xu, Lei Qian, Yizhou Wang, Wentao Zhu
链接: https://arxiv.org/abs/2604.22615v1
完整摘要: Embodied foundation models have achieved significant breakthroughs in robotic manipulation, yet they still depend heavily on large-scale robot demonstrations. Although recent works have explored leveraging human data to alleviate this dependency, effectively extracting transferable knowledge remains a significant challenge due to the inherent embodiment gap between human and robot. We argue that the intention underlying human actions can serve as a powerful intermediate representation for bridging this gap. In this paper, we introduce a novel framework that explicitly learns and transfers human intention to facilitate robotic manipulation. Specifically, we model intention through gaze, as it naturally precedes physical actions and serves as an observable proxy for human intent. Our model is first pretrained on a large-scale egocentric human dataset to capture human intention and its synergy with action, followed by finetuning on a small set of robot and human data. During inference, the model adopts a Chain-of-Thought reasoning paradigm, sequentially predicting intention before executing the action. Extensive evaluations in simulation and real-world settings, across long-horizon and fine-grained tasks, and under few-shot and robustness benchmarks, show that our method consistently outperforms strong baselines, generalizes better, and achieves state-of-the-art performance.
匹配关键词: visual reasoning
---

[ACADEMIC - ARXIV]
标题: How Do AI Agents Spend Your Money? Analyzing and Predicting Token Consumption in Agentic Coding Tasks
作者: Longju Bai, Zhemin Huang, Xingyao Wang, Jiao Sun, Rada Mihalcea, Erik Brynjolfsson, Alex Pentland, Jiaxin Pei
链接: https://arxiv.org/abs/2604.22750v1
完整摘要: The wide adoption of AI agents in complex human workflows is driving rapid growth in LLM token consumption. When agents are deployed on tasks that require a significant amount of tokens, three questions naturally arise: (1) Where do AI agents spend the tokens? (2) Which models are more token-efficient? and (3) Can agents predict their token usage before task execution? In this paper, we present the first systematic study of token consumption patterns in agentic coding tasks. We analyze trajectories from eight frontier LLMs on SWE-bench Verified and evaluate models' ability to predict their own token costs before task execution. We find that: (1) agentic tasks are uniquely expensive, consuming 1000x more tokens than code reasoning and code chat, with input tokens rather than output tokens driving the overall cost; (2) token usage is highly variable and inherently stochastic: runs on the same task can differ by up to 30x in total tokens, and higher token usage does not translate into higher accuracy; instead, accuracy often peaks at intermediate cost and saturates at higher costs; (3) models vary substantially in token efficiency: on the same tasks, Kimi-K2 and Claude-Sonnet-4.5, on average, consume over 1.5 million more tokens than GPT-5; (4) task difficulty rated by human experts only weakly aligns with actual token costs, revealing a fundamental gap between human-perceived complexity and the computational effort agents actually expend; and (5) frontier models fail to accurately predict their own token usage (with weak-to-moderate correlations, up to 0.39) and systematically underestimate real token costs. Our study offers new insights into the economics of AI agents and can inspire future research in this direction.
匹配关键词: diffusion model
---

[ACADEMIC - ARXIV]
标题: Representational Harms in LLM-Generated Narratives Against Global Majority Nationalities
作者: Ilana Nguyen, Harini Suresh, Thema Monroe-White, Evan Shieh
链接: https://arxiv.org/abs/2604.22749v1
完整摘要: Large language models (LLMs) are increasingly used for text generation tasks from everyday use to high-stakes enterprise and government applications, including simulated interviews with asylum seekers. While many works highlight the new potential applications of LLMs, there are risks of LLMs encoding and perpetuating harmful biases about non-dominant communities across the globe. To better evaluate and mitigate such harms, more research examining how LLMs portray diverse individuals is needed. In this work, we study how national origin identities are portrayed by widely-adopted LLMs in response to open-ended narrative generation prompts. Our findings demonstrate the presence of persistent representational harms by national origin, including harmful stereotypes, erasure, and one-dimensional portrayals of Global Majority identities. Minoritized national identities are simultaneously underrepresented in power-neutral stories and overrepresented in subordinated character portrayals, which are over fifty times more likely to appear than dominant portrayals. The degree of harm is amplified when US nationality cues (e.g., ``American'') are present in input prompts. Notably, we find that the harms we identify cannot be explained away via sycophancy, as US-centric biases persist even when replacing US nationality cues with non-US national identities in the prompts. Based on our findings, we call for further exploration of cultural harms in LLMs through methodologies that center Global Majority perspectives and challenge the uncritical adoption of US-based LLMs for the classification, surveillance, and misrepresentation of the majority of our planet.
匹配关键词: diffusion model
---

[ACADEMIC - ARXIV]
标题: Agentic World Modeling: Foundations, Capabilities, Laws, and Beyond
作者: Meng Chu, Xuan Billy Zhang, Kevin Qinghong Lin, Lingdong Kong, Jize Zhang, Teng Tu, Weijian Ma, Ziqi Huang, Senqiao Yang, Wei Huang, Yeying Jin, Zhefan Rao, Jinhui Ye, Xinyu Lin, Xichen Zhang, Qisheng Hu, Shuai Yang, Leyang Shen, Wei Chow, Yifei Dong, Fengyi Wu, Quanyu Long, Bin Xia, Shaozuo Yu, Mingkang Zhu, Wenhu Zhang, Jiehui Huang, Haokun Gui, Haoxuan Che, Long Chen, Qifeng Chen, Wenxuan Zhang, Wenya Wang, Xiaojuan Qi, Yang Deng, Yanwei Li, Mike Zheng Shou, Zhi-Qi Cheng, See-Kiong Ng, Ziwei Liu, Philip Torr, Jiaya Jia
链接: https://arxiv.org/abs/2604.22748v1
完整摘要: As AI systems move from generating text to accomplishing goals through sustained interaction, the ability to model environment dynamics becomes a central bottleneck. Agents that manipulate objects, navigate software, coordinate with others, or design experiments require predictive environment models, yet the term world model carries different meanings across research communities. We introduce a "levels x laws" taxonomy organized along two axes. The first defines three capability levels: L1 Predictor, which learns one-step local transition operators; L2 Simulator, which composes them into multi-step, action-conditioned rollouts that respect domain laws; and L3 Evolver, which autonomously revises its own model when predictions fail against new evidence. The second identifies four governing-law regimes: physical, digital, social, and scientific. These regimes determine what constraints a world model must satisfy and where it is most likely to fail. Using this framework, we synthesize over 400 works and summarize more than 100 representative systems spanning model-based reinforcement learning, video generation, web and GUI agents, multi-agent social simulation, and AI-driven scientific discovery. We analyze methods, failure modes, and evaluation practices across level-regime pairs, propose decision-centric evaluation principles and a minimal reproducible evaluation package, and outline architectural guidance, open problems, and governance challenges. The resulting roadmap connects previously isolated communities and charts a path from passive next-step prediction toward world models that can simulate, and ultimately reshape, the environments in which agents operate.
匹配关键词: diffusion model
---

[ACADEMIC - ARXIV]
标题: Relaxation-Informed Training of Neural Network Surrogate Models
作者: Calvin Tsay
链接: https://arxiv.org/abs/2604.22746v1
完整摘要: ReLU neural networks trained as surrogate models can be embedded exactly in mixed-integer linear programs (MILPs), enabling global optimization over the learned function. The tractability of the resulting MILP depends on structural properties of the network, i.e., the number of binary variables in associated formulations and the tightness of the continuous LP relaxation. These properties are determined during training, yet standard training objectives (prediction loss with classical weight regularization) offer no mechanism to directly control them. This work studies training regularizers that directly target downstream MILP tractability. Specifically, we propose simple bound-based regularizers that penalize the big-M constants of MILP formulations and/or the number of unstable neurons. Moreover, we introduce an LP relaxation gap regularizer that explicitly penalizes the per-sample gap of the continuous relaxation at training points. We derive its associated gradient and provide an implementation from LP dual variables without custom automatic differentiation tools. We show that combining the above regularizers can approximate the full total derivative of the LP gap with respect to the network parameters, capturing both direct and indirect sensitivities. Experiments on non-convex benchmark functions and a two-stage stochastic programming problem with quantile neural network surrogates demonstrate that the proposed regularizers can reduce MILP solve times by up to four orders of magnitude relative to an unregularized baseline, while maintaining competitive surrogate model accuracy.
匹配关键词: diffusion model
---

[ACADEMIC - ARXIV]
标题: Inter-Stance: A Dyadic Multimodal Corpus for Conversational Stance Analysis
作者: Xiang Zhang, Xiaotian Li, Taoyue Wang, Nan Bi, Xin Zhou, Cody Zhou, Zoie Wang, Andrew Yang, Yuming Su, Jeff Cohn, Qiang Ji, Lijun Yin
链接: https://arxiv.org/abs/2604.22739v1
完整摘要: Social interactions dominate our perceptions of the world and shape our daily behavior by attaching social meaning to acts as simple and spontaneous as gestures, facial expressions, voice, and speech. People mimic and otherwise respond to each other's postures, facial expressions, mannerisms, and other verbal and nonverbal behavior, and form appraisals or evaluations in the process. Yet, no publicly-available dataset includes multimodal recordings and self-report measures of multiple persons in social interaction. Dyadic recordings and annotation are lacking. We present a new data corpus of multimodal dyadic interaction (45 dyads, 90 persons) that includes synchronized multi-modality behavior (2D face video, 3D face geometry, thermal spectrum dynamics, voice and speech behavior, physiology (PPG, EDA, heart-rate, blood pressure, and respiration), and self-reported affect of all participants in a communicative interaction scenario. Two types of dyads are included: persons with shared past history and strangers. Annotations include social signals, agreement, disagreement, and neutral stance. With a potent emotion induction, these multimodal data will enable novel modeling of multimodal interpersonal behavior. We present extensive experiments to evaluate multimodal dyadic communication of dyads with and without interpersonal history, and their affect. This new database will make multimodal modeling of social interaction never possible before. The dataset includes 20TB of multimodal data to share with the research community.
匹配关键词: diffusion model
---

[ACADEMIC - ARXIV]
标题: Inter-Stance: A Dyadic Multimodal Corpus for Conversational Stance Analysis
作者: Xiang Zhang, Xiaotian Li, Taoyue Wang, Nan Bi, Xin Zhou, Cody Zhou, Zoie Wang, Andrew Yang, Yuming Su, Jeff Cohn, Qiang Ji, Lijun Yin
链接: https://arxiv.org/abs/2604.22739v1
完整摘要: Social interactions dominate our perceptions of the world and shape our daily behavior by attaching social meaning to acts as simple and spontaneous as gestures, facial expressions, voice, and speech. People mimic and otherwise respond to each other's postures, facial expressions, mannerisms, and other verbal and nonverbal behavior, and form appraisals or evaluations in the process. Yet, no publicly-available dataset includes multimodal recordings and self-report measures of multiple persons in social interaction. Dyadic recordings and annotation are lacking. We present a new data corpus of multimodal dyadic interaction (45 dyads, 90 persons) that includes synchronized multi-modality behavior (2D face video, 3D face geometry, thermal spectrum dynamics, voice and speech behavior, physiology (PPG, EDA, heart-rate, blood pressure, and respiration), and self-reported affect of all participants in a communicative interaction scenario. Two types of dyads are included: persons with shared past history and strangers. Annotations include social signals, agreement, disagreement, and neutral stance. With a potent emotion induction, these multimodal data will enable novel modeling of multimodal interpersonal behavior. We present extensive experiments to evaluate multimodal dyadic communication of dyads with and without interpersonal history, and their affect. This new database will make multimodal modeling of social interaction never possible before. The dataset includes 20TB of multimodal data to share with the research community.
匹配关键词: speech synthesis
---

[ACADEMIC - ARXIV]
标题: PASR: Pose-Aware 3D Shape Retrieval from Occluded Single Views
作者: Jiaxin Shi, Guofeng Zhang, Wufei Ma, Naifu Liang, Adam Kortylewski, Alan Vuile
链接: https://arxiv.org/abs/2604.22658v1
完整摘要: Single-view 3D shape retrieval is a fundamental yet challenging task that is increasingly important with the growth of available 3D data. Existing approaches largely fall into two categories: those using contrastive learning to map point cloud features into existing vision-language spaces and those that learn a common embedding space for 2D images and 3D shapes. However, these feed-forward, holistic alignments are often difficult to interpret, which in turn limits their robustness and generalization to real-world applications. To address this problem, we propose Pose-Aware 3D Shape Retrieval (PASR), a framework that formulates retrieval as a feature-level analysis-by-synthesis problem by distilling knowledge from a 2D foundation model (DINOv3) into a 3D encoder. By aligning pose-conditioned 3D projections with 2D feature maps, our method bridges the gap between real-world images and synthetic meshes. During inference, PASR performs a test-time optimization via analysis-by-synthesis, jointly searching for the shape and pose that best reconstruct the patch-level feature map of the input image. This synthesis-based optimization is inherently robust to partial occlusion and sensitive to fine-grained geometric details. PASR substantially outperforms existing methods on both clean and occluded 3D shape retrieval datasets by a wide margin. Additionally, PASR demonstrates strong multi-task capabilities, achieving robust shape retrieval, competitive pose estimation, and accurate category classification within a single framework.
匹配关键词: speech synthesis
---

[ACADEMIC - ARXIV]
标题: Identifying and typifying demographic unfairness in phoneme-level embeddings of self-supervised speech recognition models
作者: Felix Herron, Solange Rossato, Alexandre Allauzen, François Portet
链接: https://arxiv.org/abs/2604.22631v1
完整摘要: Modern automatic speech recognition (ASR) systems have been observed to function better for certain speaker groups (SGs) than others, despite recent gains in overall performance. One potential impediment to progress towards fairer ASR is a more nuanced understanding of the types of modeling errors that speech encoder models make, and in particular the difference between the structure of embeddings for high-performance and low-performance SGs. This paper proposes a framework typifying two types of error that can occur in modeling phonemes in ASR systems: random error/high variance in phoneme embedding, vs systematic error/embedding bias. We find that training phoneme classification probes only on a single, typically disadvantaged SG, sometimes improves performance for that SG, which is evidence for the existence of SG-level bias in phoneme embeddings. On the other hand, we find that speakers and SGs with higher levels of phoneme variance are the same as those with worse phoneme prediction accuracy. We conclude that both types of error are present in phoneme embeddings and both are candidate causes for SG-level unfairness in ASR, though random error is likely a greater hindrance to fairness than systematic error. Furthermore, we find that finetuning encoder models using a fairness-enhancing algorithm (domain enhancing and adversarial training) changes neither the benefits of in-domain phoneme classification probe training, nor measured levels of random embedding error.
匹配关键词: speech synthesis
---

[ACADEMIC - ARXIV]
标题: RedVLA: Physical Red Teaming for Vision-Language-Action Models
作者: Yuhao Zhang, Borong Zhang, Jiaming Fan, Jiachen Shen, Yishuai Cai, Yaodong Yang, Jiaming Ji
链接: https://arxiv.org/abs/2604.22591v1
完整摘要: The real-world deployment of Vision-Language-Action (VLA) models remains limited by the risk of unpredictable and irreversible physical harm. However, we currently lack effective mechanisms to proactively detect these physical safety risks before deployment. To address this gap, we propose \textbf{RedVLA}, the first red teaming framework for physical safety in VLA models. We systematically uncover unsafe behaviors through a two-stage process: (I) \textbf{Risk Scenario Synthesis} constructs a valid and task-feasible initial risk scene. Specifically, it identifies critical interaction regions from benign trajectories and positions the risk factor within these regions, aiming to entangle it with the VLA's execution flow and elicit a target unsafe behavior. (II) \textbf{Risk Amplification} ensures stable elicitation across heterogeneous models. It iteratively refines the risk factor state through gradient-free optimization guided by trajectory features. Experiments on six representative VLA models show that RedVLA uncovers diverse unsafe behaviors and achieves the ASR up to 95.5\% within 10 optimization iterations. To mitigate these risks, we further propose SimpleVLA-Guard, a lightweight safety guard built from RedVLA-generated data. Our data, assets, and code are available \href{https://redvla.github.io}{here}.
匹配关键词: speech synthesis
---

[ACADEMIC - ARXIV]
标题: DM-ASR: Diarization-aware Multi-speaker ASR with Large Language Models
作者: Li Li, Ming Cheng, Weixin Zhu, Yannan Wang, Juan Liu, Ming Li
链接: https://arxiv.org/abs/2604.22467v1
完整摘要: Multi-speaker automatic speech recognition (ASR) aims to transcribe conversational speech involving multiple speakers, requiring the model to capture not only what was said, but also who said it and sometimes when it was spoken. Recent Speech-LLM approaches have shown the potential of unified modeling for this task, but jointly learning speaker attribution, temporal structure, and lexical recognition remains difficult and data-intensive. At the current stage, leveraging reliable speaker diarization as an explicit structural prior provides a practical and efficient way to simplify this task. To effectively exploit such priors, we propose DM-ASR, a diarization-aware multi-speaker ASR framework that reformulates the task as a multi-turn dialogue generation process. Given an audio chunk and diarization results, DM-ASR decomposes transcription into a sequence of speaker- and time-conditioned queries, each corresponding to one speaker in one time segment. This formulation converts multi-speaker recognition into a series of structured sub-tasks, explicitly decoupling speaker-temporal structure from linguistic content and enabling effective integration of diarization cues with the reasoning capability of large language models. We further introduce an optional word-level timestamp prediction mechanism that interleaves word and timestamp tokens, yielding richer structured outputs and better transcription quality. Our analysis shows that diarization systems provide more reliable speaker identities and segment-level boundaries, while LLMs excel at modeling linguistic content and long-range dependencies, demonstrating their complementary strengths. Experiments on Mandarin and English benchmarks show that the proposed approach achieves strong performance with relatively small models and training data, while remaining competitive with or outperforming existing unified approaches.
匹配关键词: speech synthesis
---

[ACADEMIC - ARXIV]
标题: TTS-PRISM: A Perceptual Reasoning and Interpretable Speech Model for Fine-Grained Diagnosis
作者: Xi Wang, Jie Wang, Xingchen Song, Baijun Song, Jingran Xie, Jiahe Shao, Zijian Lin, Di Wu, Meng Meng, Jian Luan, Zhiyong Wu
链接: https://arxiv.org/abs/2604.22225v1
完整摘要: While generative text-to-speech (TTS) models approach human-level quality, monolithic metrics fail to diagnose fine-grained acoustic artifacts or explain perceptual collapse. To address this, we propose TTS-PRISM, a multi-dimensional diagnostic framework for Mandarin. First, we establish a 12-dimensional schema spanning stability to advanced expressiveness. Second, we design a targeted synthesis pipeline with adversarial perturbations and expert anchors to build a high-quality diagnostic dataset. Third, schema-driven instruction tuning embeds explicit scoring criteria and reasoning into an efficient end-to-end model. Experiments on a 1,600-sample Gold Test Set show TTS-PRISM outperforms generalist models in human alignment. Profiling six TTS paradigms establishes intuitive diagnostic flags that reveal fine-grained capability differences. TTS-PRISM is open-source, with code and checkpoints at https://github.com/xiaomi-research/tts-prism.
匹配关键词: TTS
---

[ACADEMIC - ARXIV]
标题: UniSonate: A Unified Model for Speech, Music, and Sound Effect Generation with Text Instructions
作者: Chunyu Qiang, Xiaopeng Wang, Kang Yin, Yuzhe Liang, Yuxin Guo, Teng Ma, Ziyu Zhang, Tianrui Wang, Cheng Gong, Yushen Chen, Ruibo Fu, Chen Zhang, Longbiao Wang, Jianwu Dang
链接: https://arxiv.org/abs/2604.22209v1
完整摘要: Generative audio modeling has largely been fragmented into specialized tasks, text-to-speech (TTS), text-to-music (TTM), and text-to-audio (TTA), each operating under heterogeneous control paradigms. Unifying these modalities remains a fundamental challenge due to the intrinsic dissonance between structured semantic representations (speech/music) and unstructured acoustic textures (sound effects). In this paper, we introduce UniSonate, a unified flow-matching framework capable of synthesizing speech, music, and sound effects through a standardized, reference-free natural language instruction interface. To reconcile structural disparities, we propose a novel dynamic token injection mechanism that projects unstructured environmental sounds into a structured temporal latent space, enabling precise duration control within a phoneme-driven Multimodal Diffusion Transformer (MM-DiT). Coupled with a multi-stage curriculum learning strategy, this approach effectively mitigates cross-modal optimization conflicts. Extensive experiments demonstrate that UniSonate achieves state-of-the-art performance in instruction-based TTS (WER 1.47%) and TTM (SongEval Coherence 3.18), while maintaining competitive fidelity in TTA. Crucially, we observe positive transfer, where joint training on diverse audio data significantly enhances structural coherence and prosodic expressiveness compared to single-task baselines. Audio samples are available at https://qiangchunyu.github.io/UniSonate/.
匹配关键词: TTS
---

[ACADEMIC - ARXIV]
标题: Preferences of a Voice-First Nation: Large-Scale Pairwise Evaluation and Preference Analysis for TTS in Indian Languages
作者: Srija Anand, Ashwin Sankar, Ishvinder Sethi, Aaditya Pareek, Kartik Rajput, Gaurav Yadav, Nikhil Narasimhan, Adish Pandya, Deepon Halder, Mohammed Safi Ur Rahman Khan, Praveen S, Shobhit Banga, Mitesh M Khapra
链接: https://arxiv.org/abs/2604.21481v1
完整摘要: Crowdsourced pairwise evaluation has emerged as a scalable approach for assessing foundation models. However, applying it to Text to Speech(TTS) introduces high variance due to linguistic diversity and multidimensional nature of speech perception. We present a controlled multidimensional pairwise evaluation framework for multilingual TTS that combines linguistic control with perceptually grounded annotation. Using 5K+ native and code-mixed sentences across 10 Indic languages, we evaluate 7 state-of-the-art TTS systems and collect over 120K pairwise comparisons from over 1900 native raters. In addition to overall preference, raters provide judgments across 6 perceptual dimensions: intelligibility, expressiveness, voice quality, liveliness, noise, and hallucinations. Using Bradley-Terry modeling, we construct a multilingual leaderboard, interpret human preference using SHAP analysis and analyze leaderboard reliability alongside model strengths and trade-offs across perceptual dimensions.
匹配关键词: TTS
---

[ACADEMIC - ARXIV]
标题: Text-To-Speech with Chain-of-Details: modeling temporal dynamics in speech generation
作者: Jianbo Ma, Richard Cartwright
链接: https://arxiv.org/abs/2604.19330v1
完整摘要: Recent advances in Text-To-Speech (TTS) synthesis have seen the popularity of multi-stage approaches that first predict semantic tokens and then generate acoustic tokens. In this paper, we extend the coarse-to-fine generation paradigm to the temporal domain and introduce Chain-of-Details (CoD), a novel framework that explicitly models temporal coarse-to-fine dynamics in speech generation using a cascaded architecture. Our method progressively refines temporal details across multiple stages, with each stage targeting a specific temporal granularity. All temporal detail predictions are performed using a shared decoder, enabling efficient parameter utilization across different temporal resolutions. Notably, we observe that the lowest detail level naturally performs phonetic planning without the need for an explicit phoneme duration predictor. We evaluate our method on several datasets and compare it against several baselines. Experimental results show that CoD achieves competitive performance with significantly fewer parameters than existing approaches. Our findings demonstrate that explicit modeling of temporal dynamics with the CoD framework leads to more natural speech synthesis.
匹配关键词: TTS
---

[ACADEMIC - ARXIV]
标题: MINT-Bench: A Comprehensive Multilingual Benchmark for Instruction-Following Text-to-Speech
作者: Huakang Chen, Jingbin Hu, Liumeng Xue, Qirui Zhan, Wenhao Li, Guobin Ma, Hanke Xie, Dake Guo, Linhan Ma, Yuepeng Jiang, Bengu Wu, Pengyuan Xie, Chuan Xie, Qiang Zhang, Lei Xie
链接: https://arxiv.org/abs/2604.17958v1
完整摘要: Instruction-following text-to-speech (TTS) has emerged as an important capability for controllable and expressive speech generation, yet its evaluation remains underdeveloped due to limited benchmark coverage, weak diagnostic granularity, and insufficient multilingual support. We present \textbf{MINT-Bench}, a comprehensive multilingual benchmark for instruction-following TTS. MINT-Bench is built upon a hierarchical multi-axis taxonomy, a scalable multi-stage data construction pipeline, and a hierarchical hybrid evaluation protocol that jointly assesses content consistency, instruction following, and perceptual quality. Experiments across ten languages show that current systems remain far from solved: frontier commercial systems lead overall, while leading open-source models become highly competitive and can even outperform commercial counterparts in localized settings such as Chinese. The benchmark further reveals that harder compositional and paralinguistic controls remain major bottlenecks for current systems. We release MINT-Bench together with the data construction and evaluation toolkit to support future research on controllable, multilingual, and diagnostically grounded TTS evaluation. The leaderboard and demo are available at https://longwaytog0.github.io/MINT-Bench/
匹配关键词: TTS
---

[ACADEMIC - ARXIV]
标题: Identifying and typifying demographic unfairness in phoneme-level embeddings of self-supervised speech recognition models
作者: Felix Herron, Solange Rossato, Alexandre Allauzen, François Portet
链接: https://arxiv.org/abs/2604.22631v1
完整摘要: Modern automatic speech recognition (ASR) systems have been observed to function better for certain speaker groups (SGs) than others, despite recent gains in overall performance. One potential impediment to progress towards fairer ASR is a more nuanced understanding of the types of modeling errors that speech encoder models make, and in particular the difference between the structure of embeddings for high-performance and low-performance SGs. This paper proposes a framework typifying two types of error that can occur in modeling phonemes in ASR systems: random error/high variance in phoneme embedding, vs systematic error/embedding bias. We find that training phoneme classification probes only on a single, typically disadvantaged SG, sometimes improves performance for that SG, which is evidence for the existence of SG-level bias in phoneme embeddings. On the other hand, we find that speakers and SGs with higher levels of phoneme variance are the same as those with worse phoneme prediction accuracy. We conclude that both types of error are present in phoneme embeddings and both are candidate causes for SG-level unfairness in ASR, though random error is likely a greater hindrance to fairness than systematic error. Furthermore, we find that finetuning encoder models using a fairness-enhancing algorithm (domain enhancing and adversarial training) changes neither the benefits of in-domain phoneme classification probe training, nor measured levels of random embedding error.
匹配关键词: ASR
---

[ACADEMIC - ARXIV]
标题: RedVLA: Physical Red Teaming for Vision-Language-Action Models
作者: Yuhao Zhang, Borong Zhang, Jiaming Fan, Jiachen Shen, Yishuai Cai, Yaodong Yang, Jiaming Ji
链接: https://arxiv.org/abs/2604.22591v1
完整摘要: The real-world deployment of Vision-Language-Action (VLA) models remains limited by the risk of unpredictable and irreversible physical harm. However, we currently lack effective mechanisms to proactively detect these physical safety risks before deployment. To address this gap, we propose \textbf{RedVLA}, the first red teaming framework for physical safety in VLA models. We systematically uncover unsafe behaviors through a two-stage process: (I) \textbf{Risk Scenario Synthesis} constructs a valid and task-feasible initial risk scene. Specifically, it identifies critical interaction regions from benign trajectories and positions the risk factor within these regions, aiming to entangle it with the VLA's execution flow and elicit a target unsafe behavior. (II) \textbf{Risk Amplification} ensures stable elicitation across heterogeneous models. It iteratively refines the risk factor state through gradient-free optimization guided by trajectory features. Experiments on six representative VLA models show that RedVLA uncovers diverse unsafe behaviors and achieves the ASR up to 95.5\% within 10 optimization iterations. To mitigate these risks, we further propose SimpleVLA-Guard, a lightweight safety guard built from RedVLA-generated data. Our data, assets, and code are available \href{https://redvla.github.io}{here}.
匹配关键词: ASR
---

[ACADEMIC - ARXIV]
标题: DM-ASR: Diarization-aware Multi-speaker ASR with Large Language Models
作者: Li Li, Ming Cheng, Weixin Zhu, Yannan Wang, Juan Liu, Ming Li
链接: https://arxiv.org/abs/2604.22467v1
完整摘要: Multi-speaker automatic speech recognition (ASR) aims to transcribe conversational speech involving multiple speakers, requiring the model to capture not only what was said, but also who said it and sometimes when it was spoken. Recent Speech-LLM approaches have shown the potential of unified modeling for this task, but jointly learning speaker attribution, temporal structure, and lexical recognition remains difficult and data-intensive. At the current stage, leveraging reliable speaker diarization as an explicit structural prior provides a practical and efficient way to simplify this task. To effectively exploit such priors, we propose DM-ASR, a diarization-aware multi-speaker ASR framework that reformulates the task as a multi-turn dialogue generation process. Given an audio chunk and diarization results, DM-ASR decomposes transcription into a sequence of speaker- and time-conditioned queries, each corresponding to one speaker in one time segment. This formulation converts multi-speaker recognition into a series of structured sub-tasks, explicitly decoupling speaker-temporal structure from linguistic content and enabling effective integration of diarization cues with the reasoning capability of large language models. We further introduce an optional word-level timestamp prediction mechanism that interleaves word and timestamp tokens, yielding richer structured outputs and better transcription quality. Our analysis shows that diarization systems provide more reliable speaker identities and segment-level boundaries, while LLMs excel at modeling linguistic content and long-range dependencies, demonstrating their complementary strengths. Experiments on Mandarin and English benchmarks show that the proposed approach achieves strong performance with relatively small models and training data, while remaining competitive with or outperforming existing unified approaches.
匹配关键词: ASR
---

[ACADEMIC - ARXIV]
标题: Beyond Acoustic Sparsity and Linguistic Bias: A Prompt-Free Paradigm for Mispronunciation Detection and Diagnosis
作者: Haopeng Geng, Longfei Yang, Xi Chen, Haitong Sun, Daisuke Saito, Nobuaki Minematsu
链接: https://arxiv.org/abs/2604.22133v1
完整摘要: Mispronunciation Detection and Diagnosis (MDD) requires modeling fine-grained acoustic deviations. However, current ASR-derived MDD systems often face inherent limitations. In particular, CTC-based models favor sequence-level alignments that neglect transient mispronunciation cues, while explicit canonical priors bias predictions toward intended targets. To address these bottlenecks, we propose a prompt-free framework decoupling acoustic fidelity from canonical guidance. First, we introduce CROTTC, an acoustic model enforcing monotonic, frame-level alignment to accurately capture pronunciation deviations. Second, we implicitly inject mispronunciation information via the IF strategy under the knowledge transfer principle. Experiments show CROTTC-IF achieves a 71.77% F1-score on L2-ARCTIC and 71.70% F1-score on the Iqra'Eval2 leaderboard. With empirical analysis, we demonstrate that decoupling acoustics from explicit priors provides highly robust MDD.
匹配关键词: ASR
---

[ACADEMIC - ARXIV]
标题: Evaluation of Automatic Speech Recognition Using Generative Large Language Models
作者: Thibault Bañeras-Roux, Shashi Kumar, Driss Khalil, Sergio Burdisso, Petr Motlicek, Shiran Liu, Mickael Rouvier, Jane Wottawa, Richard Dufour
链接: https://arxiv.org/abs/2604.21928v1
完整摘要: Automatic Speech Recognition (ASR) is traditionally evaluated using Word Error Rate (WER), a metric that is insensitive to meaning. Embedding-based semantic metrics are better correlated with human perception, but decoder-based Large Language Models (LLMs) remain underexplored for this task. This paper evaluates their relevance through three approaches: (1) selecting the best hypothesis between two candidates, (2) computing semantic distance using generative embeddings, and (3) qualitative classification of errors. On the HATS dataset, the best LLMs achieve 92--94\% agreement with human annotators for hypothesis selection, compared to 63\% for WER, also outperforming semantic metrics. Embeddings from decoder-based LLMs show performance comparable to encoder models. Finally, LLMs offer a promising direction for interpretable and semantic ASR evaluation.
匹配关键词: ASR
---

[ACADEMIC - ARXIV]
标题: Inter-Stance: A Dyadic Multimodal Corpus for Conversational Stance Analysis
作者: Xiang Zhang, Xiaotian Li, Taoyue Wang, Nan Bi, Xin Zhou, Cody Zhou, Zoie Wang, Andrew Yang, Yuming Su, Jeff Cohn, Qiang Ji, Lijun Yin
链接: https://arxiv.org/abs/2604.22739v1
完整摘要: Social interactions dominate our perceptions of the world and shape our daily behavior by attaching social meaning to acts as simple and spontaneous as gestures, facial expressions, voice, and speech. People mimic and otherwise respond to each other's postures, facial expressions, mannerisms, and other verbal and nonverbal behavior, and form appraisals or evaluations in the process. Yet, no publicly-available dataset includes multimodal recordings and self-report measures of multiple persons in social interaction. Dyadic recordings and annotation are lacking. We present a new data corpus of multimodal dyadic interaction (45 dyads, 90 persons) that includes synchronized multi-modality behavior (2D face video, 3D face geometry, thermal spectrum dynamics, voice and speech behavior, physiology (PPG, EDA, heart-rate, blood pressure, and respiration), and self-reported affect of all participants in a communicative interaction scenario. Two types of dyads are included: persons with shared past history and strangers. Annotations include social signals, agreement, disagreement, and neutral stance. With a potent emotion induction, these multimodal data will enable novel modeling of multimodal interpersonal behavior. We present extensive experiments to evaluate multimodal dyadic communication of dyads with and without interpersonal history, and their affect. This new database will make multimodal modeling of social interaction never possible before. The dataset includes 20TB of multimodal data to share with the research community.
匹配关键词: speech recognition
---

[ACADEMIC - ARXIV]
标题: Long-tail Internet photo reconstruction
作者: Yuan Li, Yuanbo Xiangli, Hadar Averbuch-Elor, Noah Snavely, Ruojin Cai
链接: https://arxiv.org/abs/2604.22714v1
完整摘要: Internet photo collections exhibit an extremely long-tailed distribution: a few famous landmarks are densely photographed and easily reconstructed in 3D, while most real-world sites are represented with sparse, noisy, uneven imagery beyond the capabilities of both classical and learned 3D methods. We believe that tackling this long-tail regime represents one of the next frontiers for 3D foundation models. Although reliable ground-truth 3D supervision from sparse scenes is challenging to acquire, we observe that it can be effectively simulated by sampling sparse subsets from well-reconstructed Internet landmarks. To this end, we introduce MegaDepth-X, a large dataset of 3D reconstructions with clean, dense depth, together with a strategy for sampling sets of training images that mimic camera distributions in long-tail scenes. Finetuning 3D foundation models with these components yields robust reconstructions under extreme sparsity, and also enables more reliable reconstruction in symmetric and repetitive scenes, while preserving generalization to standard, dense 3D benchmark datasets.
匹配关键词: speech recognition
---

[ACADEMIC - ARXIV]
标题: Generative Modeling of Neurodegenerative Brain Anatomy with 4D Longitudinal Diffusion Model
作者: Nivetha Jayakumar, Swakshar Deb, Bahram Jafrasteh, Qingyu Zhao, Miaomiao Zhang
链接: https://arxiv.org/abs/2604.22700v1
完整摘要: Understanding and predicting the progression of neurodegenerative diseases remains a major challenge in medical AI, with significant implications for early diagnosis, disease monitoring, and treatment planning. However, most available longitudinal neuroimaging datasets are temporally sparse with a few follow-up scans per subject. This scarcity of temporal data limits our ability to model and accurately capture the continuous anatomical changes related to disease progression in individual subjects. To address this problem, we propose a novel 4D (3DxT) diffusion-based generative framework that effectively models and synthesizes longitudinal brain anatomy over time, conditioned on available clinical variables such as health status, age, sex, and other relevant factors. Moreover, while most current approaches focus on manipulating image intensity or texture, our method explicitly learns the data distribution of topology-preserving spatiotemporal deformations to effectively capture the geometric changes of brain structures over time. This design enables the realistic generation of future anatomical states and the reconstruction of anatomically consistent disease trajectories, providing a more faithful representation of longitudinal brain changes. We validate our model through both synthetic sequence generation and downstream longitudinal disease classification, as well as brain segmentation. Experiments on two large-scale longitudinal neuroimage datasets demonstrate that our method outperforms state-of-the-art baselines in generating anatomically accurate, temporally consistent, and clinically meaningful brain trajectories. Our code is available on Github.
匹配关键词: speech recognition
---

[ACADEMIC - ARXIV]
标题: SS3D: End2End Self-Supervised 3D from Web Videos
作者: Marwane Hariat, Gianni Franchi, David Filliat, Antoine Manzanera
链接: https://arxiv.org/abs/2604.22686v1
完整摘要: We present SS3D, a web-scale SfM-based self-supervision pretraining pipeline for feed-forward 3D estimation from monocular video. Our model jointly predicts depth, ego-motion, and intrinsics in a single forward pass and is trained/evaluated as a coherent end-to-end 3D estimator. To stabilize joint learning, we use an intrinsics-first two-stage schedule and a unified single-checkpoint evaluation protocol. Scaling SfM self-supervision to unconstrained web video is challenging due to weak multi-view observability and strong corpus heterogeneity; we address these with a multi-view signal proxy (MVS) used for filtering and curriculum sampling, and with expert training distilled into a single student. Pretraining on YouTube-8M (~100M frames after filtering) yields strong cross-domain zero-shot transfer and improved fine-tuning performance over prior self-supervised baselines. We release the pretrained checkpoint and code.
匹配关键词: speech recognition
---

[ACADEMIC - ARXIV]
标题: PASR: Pose-Aware 3D Shape Retrieval from Occluded Single Views
作者: Jiaxin Shi, Guofeng Zhang, Wufei Ma, Naifu Liang, Adam Kortylewski, Alan Vuile
链接: https://arxiv.org/abs/2604.22658v1
完整摘要: Single-view 3D shape retrieval is a fundamental yet challenging task that is increasingly important with the growth of available 3D data. Existing approaches largely fall into two categories: those using contrastive learning to map point cloud features into existing vision-language spaces and those that learn a common embedding space for 2D images and 3D shapes. However, these feed-forward, holistic alignments are often difficult to interpret, which in turn limits their robustness and generalization to real-world applications. To address this problem, we propose Pose-Aware 3D Shape Retrieval (PASR), a framework that formulates retrieval as a feature-level analysis-by-synthesis problem by distilling knowledge from a 2D foundation model (DINOv3) into a 3D encoder. By aligning pose-conditioned 3D projections with 2D feature maps, our method bridges the gap between real-world images and synthetic meshes. During inference, PASR performs a test-time optimization via analysis-by-synthesis, jointly searching for the shape and pose that best reconstruct the patch-level feature map of the input image. This synthesis-based optimization is inherently robust to partial occlusion and sensitive to fine-grained geometric details. PASR substantially outperforms existing methods on both clean and occluded 3D shape retrieval datasets by a wide margin. Additionally, PASR demonstrates strong multi-task capabilities, achieving robust shape retrieval, competitive pose estimation, and accurate category classification within a single framework.
匹配关键词: speech recognition
---

[ACADEMIC - ARXIV]
标题: How Do AI Agents Spend Your Money? Analyzing and Predicting Token Consumption in Agentic Coding Tasks
作者: Longju Bai, Zhemin Huang, Xingyao Wang, Jiao Sun, Rada Mihalcea, Erik Brynjolfsson, Alex Pentland, Jiaxin Pei
链接: https://arxiv.org/abs/2604.22750v1
完整摘要: The wide adoption of AI agents in complex human workflows is driving rapid growth in LLM token consumption. When agents are deployed on tasks that require a significant amount of tokens, three questions naturally arise: (1) Where do AI agents spend the tokens? (2) Which models are more token-efficient? and (3) Can agents predict their token usage before task execution? In this paper, we present the first systematic study of token consumption patterns in agentic coding tasks. We analyze trajectories from eight frontier LLMs on SWE-bench Verified and evaluate models' ability to predict their own token costs before task execution. We find that: (1) agentic tasks are uniquely expensive, consuming 1000x more tokens than code reasoning and code chat, with input tokens rather than output tokens driving the overall cost; (2) token usage is highly variable and inherently stochastic: runs on the same task can differ by up to 30x in total tokens, and higher token usage does not translate into higher accuracy; instead, accuracy often peaks at intermediate cost and saturates at higher costs; (3) models vary substantially in token efficiency: on the same tasks, Kimi-K2 and Claude-Sonnet-4.5, on average, consume over 1.5 million more tokens than GPT-5; (4) task difficulty rated by human experts only weakly aligns with actual token costs, revealing a fundamental gap between human-perceived complexity and the computational effort agents actually expend; and (5) frontier models fail to accurately predict their own token usage (with weak-to-moderate correlations, up to 0.39) and systematically underestimate real token costs. Our study offers new insights into the economics of AI agents and can inspire future research in this direction.
匹配关键词: audio language model
---

[ACADEMIC - ARXIV]
标题: Representational Harms in LLM-Generated Narratives Against Global Majority Nationalities
作者: Ilana Nguyen, Harini Suresh, Thema Monroe-White, Evan Shieh
链接: https://arxiv.org/abs/2604.22749v1
完整摘要: Large language models (LLMs) are increasingly used for text generation tasks from everyday use to high-stakes enterprise and government applications, including simulated interviews with asylum seekers. While many works highlight the new potential applications of LLMs, there are risks of LLMs encoding and perpetuating harmful biases about non-dominant communities across the globe. To better evaluate and mitigate such harms, more research examining how LLMs portray diverse individuals is needed. In this work, we study how national origin identities are portrayed by widely-adopted LLMs in response to open-ended narrative generation prompts. Our findings demonstrate the presence of persistent representational harms by national origin, including harmful stereotypes, erasure, and one-dimensional portrayals of Global Majority identities. Minoritized national identities are simultaneously underrepresented in power-neutral stories and overrepresented in subordinated character portrayals, which are over fifty times more likely to appear than dominant portrayals. The degree of harm is amplified when US nationality cues (e.g., ``American'') are present in input prompts. Notably, we find that the harms we identify cannot be explained away via sycophancy, as US-centric biases persist even when replacing US nationality cues with non-US national identities in the prompts. Based on our findings, we call for further exploration of cultural harms in LLMs through methodologies that center Global Majority perspectives and challenge the uncritical adoption of US-based LLMs for the classification, surveillance, and misrepresentation of the majority of our planet.
匹配关键词: audio language model
---

[ACADEMIC - ARXIV]
标题: Agentic World Modeling: Foundations, Capabilities, Laws, and Beyond
作者: Meng Chu, Xuan Billy Zhang, Kevin Qinghong Lin, Lingdong Kong, Jize Zhang, Teng Tu, Weijian Ma, Ziqi Huang, Senqiao Yang, Wei Huang, Yeying Jin, Zhefan Rao, Jinhui Ye, Xinyu Lin, Xichen Zhang, Qisheng Hu, Shuai Yang, Leyang Shen, Wei Chow, Yifei Dong, Fengyi Wu, Quanyu Long, Bin Xia, Shaozuo Yu, Mingkang Zhu, Wenhu Zhang, Jiehui Huang, Haokun Gui, Haoxuan Che, Long Chen, Qifeng Chen, Wenxuan Zhang, Wenya Wang, Xiaojuan Qi, Yang Deng, Yanwei Li, Mike Zheng Shou, Zhi-Qi Cheng, See-Kiong Ng, Ziwei Liu, Philip Torr, Jiaya Jia
链接: https://arxiv.org/abs/2604.22748v1
完整摘要: As AI systems move from generating text to accomplishing goals through sustained interaction, the ability to model environment dynamics becomes a central bottleneck. Agents that manipulate objects, navigate software, coordinate with others, or design experiments require predictive environment models, yet the term world model carries different meanings across research communities. We introduce a "levels x laws" taxonomy organized along two axes. The first defines three capability levels: L1 Predictor, which learns one-step local transition operators; L2 Simulator, which composes them into multi-step, action-conditioned rollouts that respect domain laws; and L3 Evolver, which autonomously revises its own model when predictions fail against new evidence. The second identifies four governing-law regimes: physical, digital, social, and scientific. These regimes determine what constraints a world model must satisfy and where it is most likely to fail. Using this framework, we synthesize over 400 works and summarize more than 100 representative systems spanning model-based reinforcement learning, video generation, web and GUI agents, multi-agent social simulation, and AI-driven scientific discovery. We analyze methods, failure modes, and evaluation practices across level-regime pairs, propose decision-centric evaluation principles and a minimal reproducible evaluation package, and outline architectural guidance, open problems, and governance challenges. The resulting roadmap connects previously isolated communities and charts a path from passive next-step prediction toward world models that can simulate, and ultimately reshape, the environments in which agents operate.
匹配关键词: audio language model
---

[ACADEMIC - ARXIV]
标题: Relaxation-Informed Training of Neural Network Surrogate Models
作者: Calvin Tsay
链接: https://arxiv.org/abs/2604.22746v1
完整摘要: ReLU neural networks trained as surrogate models can be embedded exactly in mixed-integer linear programs (MILPs), enabling global optimization over the learned function. The tractability of the resulting MILP depends on structural properties of the network, i.e., the number of binary variables in associated formulations and the tightness of the continuous LP relaxation. These properties are determined during training, yet standard training objectives (prediction loss with classical weight regularization) offer no mechanism to directly control them. This work studies training regularizers that directly target downstream MILP tractability. Specifically, we propose simple bound-based regularizers that penalize the big-M constants of MILP formulations and/or the number of unstable neurons. Moreover, we introduce an LP relaxation gap regularizer that explicitly penalizes the per-sample gap of the continuous relaxation at training points. We derive its associated gradient and provide an implementation from LP dual variables without custom automatic differentiation tools. We show that combining the above regularizers can approximate the full total derivative of the LP gap with respect to the network parameters, capturing both direct and indirect sensitivities. Experiments on non-convex benchmark functions and a two-stage stochastic programming problem with quantile neural network surrogates demonstrate that the proposed regularizers can reduce MILP solve times by up to four orders of magnitude relative to an unregularized baseline, while maintaining competitive surrogate model accuracy.
匹配关键词: audio language model
---

[ACADEMIC - ARXIV]
标题: Inter-Stance: A Dyadic Multimodal Corpus for Conversational Stance Analysis
作者: Xiang Zhang, Xiaotian Li, Taoyue Wang, Nan Bi, Xin Zhou, Cody Zhou, Zoie Wang, Andrew Yang, Yuming Su, Jeff Cohn, Qiang Ji, Lijun Yin
链接: https://arxiv.org/abs/2604.22739v1
完整摘要: Social interactions dominate our perceptions of the world and shape our daily behavior by attaching social meaning to acts as simple and spontaneous as gestures, facial expressions, voice, and speech. People mimic and otherwise respond to each other's postures, facial expressions, mannerisms, and other verbal and nonverbal behavior, and form appraisals or evaluations in the process. Yet, no publicly-available dataset includes multimodal recordings and self-report measures of multiple persons in social interaction. Dyadic recordings and annotation are lacking. We present a new data corpus of multimodal dyadic interaction (45 dyads, 90 persons) that includes synchronized multi-modality behavior (2D face video, 3D face geometry, thermal spectrum dynamics, voice and speech behavior, physiology (PPG, EDA, heart-rate, blood pressure, and respiration), and self-reported affect of all participants in a communicative interaction scenario. Two types of dyads are included: persons with shared past history and strangers. Annotations include social signals, agreement, disagreement, and neutral stance. With a potent emotion induction, these multimodal data will enable novel modeling of multimodal interpersonal behavior. We present extensive experiments to evaluate multimodal dyadic communication of dyads with and without interpersonal history, and their affect. This new database will make multimodal modeling of social interaction never possible before. The dataset includes 20TB of multimodal data to share with the research community.
匹配关键词: audio language model
---

[ACADEMIC - ARXIV]
标题: Representational Harms in LLM-Generated Narratives Against Global Majority Nationalities
作者: Ilana Nguyen, Harini Suresh, Thema Monroe-White, Evan Shieh
链接: https://arxiv.org/abs/2604.22749v1
完整摘要: Large language models (LLMs) are increasingly used for text generation tasks from everyday use to high-stakes enterprise and government applications, including simulated interviews with asylum seekers. While many works highlight the new potential applications of LLMs, there are risks of LLMs encoding and perpetuating harmful biases about non-dominant communities across the globe. To better evaluate and mitigate such harms, more research examining how LLMs portray diverse individuals is needed. In this work, we study how national origin identities are portrayed by widely-adopted LLMs in response to open-ended narrative generation prompts. Our findings demonstrate the presence of persistent representational harms by national origin, including harmful stereotypes, erasure, and one-dimensional portrayals of Global Majority identities. Minoritized national identities are simultaneously underrepresented in power-neutral stories and overrepresented in subordinated character portrayals, which are over fifty times more likely to appear than dominant portrayals. The degree of harm is amplified when US nationality cues (e.g., ``American'') are present in input prompts. Notably, we find that the harms we identify cannot be explained away via sycophancy, as US-centric biases persist even when replacing US nationality cues with non-US national identities in the prompts. Based on our findings, we call for further exploration of cultural harms in LLMs through methodologies that center Global Majority perspectives and challenge the uncritical adoption of US-based LLMs for the classification, surveillance, and misrepresentation of the majority of our planet.
匹配关键词: voice generation
---

[ACADEMIC - ARXIV]
标题: Agentic World Modeling: Foundations, Capabilities, Laws, and Beyond
作者: Meng Chu, Xuan Billy Zhang, Kevin Qinghong Lin, Lingdong Kong, Jize Zhang, Teng Tu, Weijian Ma, Ziqi Huang, Senqiao Yang, Wei Huang, Yeying Jin, Zhefan Rao, Jinhui Ye, Xinyu Lin, Xichen Zhang, Qisheng Hu, Shuai Yang, Leyang Shen, Wei Chow, Yifei Dong, Fengyi Wu, Quanyu Long, Bin Xia, Shaozuo Yu, Mingkang Zhu, Wenhu Zhang, Jiehui Huang, Haokun Gui, Haoxuan Che, Long Chen, Qifeng Chen, Wenxuan Zhang, Wenya Wang, Xiaojuan Qi, Yang Deng, Yanwei Li, Mike Zheng Shou, Zhi-Qi Cheng, See-Kiong Ng, Ziwei Liu, Philip Torr, Jiaya Jia
链接: https://arxiv.org/abs/2604.22748v1
完整摘要: As AI systems move from generating text to accomplishing goals through sustained interaction, the ability to model environment dynamics becomes a central bottleneck. Agents that manipulate objects, navigate software, coordinate with others, or design experiments require predictive environment models, yet the term world model carries different meanings across research communities. We introduce a "levels x laws" taxonomy organized along two axes. The first defines three capability levels: L1 Predictor, which learns one-step local transition operators; L2 Simulator, which composes them into multi-step, action-conditioned rollouts that respect domain laws; and L3 Evolver, which autonomously revises its own model when predictions fail against new evidence. The second identifies four governing-law regimes: physical, digital, social, and scientific. These regimes determine what constraints a world model must satisfy and where it is most likely to fail. Using this framework, we synthesize over 400 works and summarize more than 100 representative systems spanning model-based reinforcement learning, video generation, web and GUI agents, multi-agent social simulation, and AI-driven scientific discovery. We analyze methods, failure modes, and evaluation practices across level-regime pairs, propose decision-centric evaluation principles and a minimal reproducible evaluation package, and outline architectural guidance, open problems, and governance challenges. The resulting roadmap connects previously isolated communities and charts a path from passive next-step prediction toward world models that can simulate, and ultimately reshape, the environments in which agents operate.
匹配关键词: voice generation
---

[ACADEMIC - ARXIV]
标题: Inter-Stance: A Dyadic Multimodal Corpus for Conversational Stance Analysis
作者: Xiang Zhang, Xiaotian Li, Taoyue Wang, Nan Bi, Xin Zhou, Cody Zhou, Zoie Wang, Andrew Yang, Yuming Su, Jeff Cohn, Qiang Ji, Lijun Yin
链接: https://arxiv.org/abs/2604.22739v1
完整摘要: Social interactions dominate our perceptions of the world and shape our daily behavior by attaching social meaning to acts as simple and spontaneous as gestures, facial expressions, voice, and speech. People mimic and otherwise respond to each other's postures, facial expressions, mannerisms, and other verbal and nonverbal behavior, and form appraisals or evaluations in the process. Yet, no publicly-available dataset includes multimodal recordings and self-report measures of multiple persons in social interaction. Dyadic recordings and annotation are lacking. We present a new data corpus of multimodal dyadic interaction (45 dyads, 90 persons) that includes synchronized multi-modality behavior (2D face video, 3D face geometry, thermal spectrum dynamics, voice and speech behavior, physiology (PPG, EDA, heart-rate, blood pressure, and respiration), and self-reported affect of all participants in a communicative interaction scenario. Two types of dyads are included: persons with shared past history and strangers. Annotations include social signals, agreement, disagreement, and neutral stance. With a potent emotion induction, these multimodal data will enable novel modeling of multimodal interpersonal behavior. We present extensive experiments to evaluate multimodal dyadic communication of dyads with and without interpersonal history, and their affect. This new database will make multimodal modeling of social interaction never possible before. The dataset includes 20TB of multimodal data to share with the research community.
匹配关键词: voice generation
---

[ACADEMIC - ARXIV]
标题: GCImOpt: Learning efficient goal-conditioned policies by imitating optimal trajectories
作者: Jon Goikoetxea, Jesús F. Palacián
链接: https://arxiv.org/abs/2604.22724v1
完整摘要: Imitation learning is a well-established approach for machine-learning-based control. However, its applicability depends on having access to demonstrations, which are often expensive to collect and/or suboptimal for solving the task. In this work, we present GCImOpt, an approach to learn efficient goal-conditioned policies by training on datasets generated by trajectory optimization. Our approach for dataset generation is computationally efficient, can generate thousands of optimal trajectories in minutes on a laptop computer, and produces high-quality demonstrations. Further, by means of a data augmentation scheme that treats intermediate states as goals, we are able to increase the training dataset size by an order of magnitude. Using our generated datasets, we train goal-conditioned neural network policies that can control the system towards arbitrary goals. To demonstrate the generality of our approach, we generate datasets and then train policies for various control tasks, namely cart-pole stabilization, planar and three-dimensional quadcopter stabilization, and point reaching using a 6-DoF robot arm. We show that our trained policies can achieve high success rates and near-optimal control profiles, all while being small (less than 80,000 neural network parameters) and fast enough (up to more than 6,000 times faster than a trajectory optimization solver) that they could be deployed onboard resource-constrained controllers. We provide videos, code, datasets and pre-trained policies under a free software license; see our project website https://jongoiko.github.io/gcimopt/.
匹配关键词: voice generation
---

[ACADEMIC - ARXIV]
标题: Aligning Dense Retrievers with LLM Utility via DistillationAligning Dense Retrievers with LLM Utility via Distillation
作者: Rajinder Sandhu, Di Mu, Cheng Chang, Md Shahriar Tasjid, Himanshu Rai, Maksims Volkovs, Ga Wu
链接: https://arxiv.org/abs/2604.22722v1
完整摘要: Dense vector retrieval is the practical backbone of Retrieval- Augmented Generation (RAG), but similarity search can suffer from precision limitations. Conversely, utility-based approaches leveraging LLM re-ranking often achieve superior performance but are computationally prohibitive and prone to noise inherent in perplexity estimation. We propose Utility-Aligned Embeddings (UAE), a framework designed to merge these advantages into a practical, high-performance retrieval method. We formulate retrieval as a distribution matching problem, training a bi-encoder to imitate a utility distribution derived from perplexity reduction using a Utility-Modulated InfoNCE objective. This approach injects graded utility signals directly into the embedding space without requiring test-time LLM inference. On the QASPER benchmark, UAE improves retrieval Recall@1 by 30.59%, MAP by 30.16% and Token F1 by 17.3% over the strong semantic baseline BGE-Base. Crucially, UAE is over 180x faster than the efficient LLM re-ranking methods preserving competitive performance, demonstrating that aligning retrieval with generative utility yields reliable contexts at scale.
匹配关键词: voice generation
---

[ACADEMIC - ARXIV]
标题: How Do AI Agents Spend Your Money? Analyzing and Predicting Token Consumption in Agentic Coding Tasks
作者: Longju Bai, Zhemin Huang, Xingyao Wang, Jiao Sun, Rada Mihalcea, Erik Brynjolfsson, Alex Pentland, Jiaxin Pei
链接: https://arxiv.org/abs/2604.22750v1
完整摘要: The wide adoption of AI agents in complex human workflows is driving rapid growth in LLM token consumption. When agents are deployed on tasks that require a significant amount of tokens, three questions naturally arise: (1) Where do AI agents spend the tokens? (2) Which models are more token-efficient? and (3) Can agents predict their token usage before task execution? In this paper, we present the first systematic study of token consumption patterns in agentic coding tasks. We analyze trajectories from eight frontier LLMs on SWE-bench Verified and evaluate models' ability to predict their own token costs before task execution. We find that: (1) agentic tasks are uniquely expensive, consuming 1000x more tokens than code reasoning and code chat, with input tokens rather than output tokens driving the overall cost; (2) token usage is highly variable and inherently stochastic: runs on the same task can differ by up to 30x in total tokens, and higher token usage does not translate into higher accuracy; instead, accuracy often peaks at intermediate cost and saturates at higher costs; (3) models vary substantially in token efficiency: on the same tasks, Kimi-K2 and Claude-Sonnet-4.5, on average, consume over 1.5 million more tokens than GPT-5; (4) task difficulty rated by human experts only weakly aligns with actual token costs, revealing a fundamental gap between human-perceived complexity and the computational effort agents actually expend; and (5) frontier models fail to accurately predict their own token usage (with weak-to-moderate correlations, up to 0.39) and systematically underestimate real token costs. Our study offers new insights into the economics of AI agents and can inspire future research in this direction.
匹配关键词: embodied AI
---

[ACADEMIC - ARXIV]
标题: Agentic World Modeling: Foundations, Capabilities, Laws, and Beyond
作者: Meng Chu, Xuan Billy Zhang, Kevin Qinghong Lin, Lingdong Kong, Jize Zhang, Teng Tu, Weijian Ma, Ziqi Huang, Senqiao Yang, Wei Huang, Yeying Jin, Zhefan Rao, Jinhui Ye, Xinyu Lin, Xichen Zhang, Qisheng Hu, Shuai Yang, Leyang Shen, Wei Chow, Yifei Dong, Fengyi Wu, Quanyu Long, Bin Xia, Shaozuo Yu, Mingkang Zhu, Wenhu Zhang, Jiehui Huang, Haokun Gui, Haoxuan Che, Long Chen, Qifeng Chen, Wenxuan Zhang, Wenya Wang, Xiaojuan Qi, Yang Deng, Yanwei Li, Mike Zheng Shou, Zhi-Qi Cheng, See-Kiong Ng, Ziwei Liu, Philip Torr, Jiaya Jia
链接: https://arxiv.org/abs/2604.22748v1
完整摘要: As AI systems move from generating text to accomplishing goals through sustained interaction, the ability to model environment dynamics becomes a central bottleneck. Agents that manipulate objects, navigate software, coordinate with others, or design experiments require predictive environment models, yet the term world model carries different meanings across research communities. We introduce a "levels x laws" taxonomy organized along two axes. The first defines three capability levels: L1 Predictor, which learns one-step local transition operators; L2 Simulator, which composes them into multi-step, action-conditioned rollouts that respect domain laws; and L3 Evolver, which autonomously revises its own model when predictions fail against new evidence. The second identifies four governing-law regimes: physical, digital, social, and scientific. These regimes determine what constraints a world model must satisfy and where it is most likely to fail. Using this framework, we synthesize over 400 works and summarize more than 100 representative systems spanning model-based reinforcement learning, video generation, web and GUI agents, multi-agent social simulation, and AI-driven scientific discovery. We analyze methods, failure modes, and evaluation practices across level-regime pairs, propose decision-centric evaluation principles and a minimal reproducible evaluation package, and outline architectural guidance, open problems, and governance challenges. The resulting roadmap connects previously isolated communities and charts a path from passive next-step prediction toward world models that can simulate, and ultimately reshape, the environments in which agents operate.
匹配关键词: embodied AI
---

[ACADEMIC - ARXIV]
标题: Generative Modeling of Neurodegenerative Brain Anatomy with 4D Longitudinal Diffusion Model
作者: Nivetha Jayakumar, Swakshar Deb, Bahram Jafrasteh, Qingyu Zhao, Miaomiao Zhang
链接: https://arxiv.org/abs/2604.22700v1
完整摘要: Understanding and predicting the progression of neurodegenerative diseases remains a major challenge in medical AI, with significant implications for early diagnosis, disease monitoring, and treatment planning. However, most available longitudinal neuroimaging datasets are temporally sparse with a few follow-up scans per subject. This scarcity of temporal data limits our ability to model and accurately capture the continuous anatomical changes related to disease progression in individual subjects. To address this problem, we propose a novel 4D (3DxT) diffusion-based generative framework that effectively models and synthesizes longitudinal brain anatomy over time, conditioned on available clinical variables such as health status, age, sex, and other relevant factors. Moreover, while most current approaches focus on manipulating image intensity or texture, our method explicitly learns the data distribution of topology-preserving spatiotemporal deformations to effectively capture the geometric changes of brain structures over time. This design enables the realistic generation of future anatomical states and the reconstruction of anatomically consistent disease trajectories, providing a more faithful representation of longitudinal brain changes. We validate our model through both synthetic sequence generation and downstream longitudinal disease classification, as well as brain segmentation. Experiments on two large-scale longitudinal neuroimage datasets demonstrate that our method outperforms state-of-the-art baselines in generating anatomically accurate, temporally consistent, and clinically meaningful brain trajectories. Our code is available on Github.
匹配关键词: embodied AI
---

[ACADEMIC - ARXIV]
标题: How Supply Chain Dependencies Complicate Bias Measurement and Accountability Attribution in AI Hiring Applications
作者: Gauri Sharma, Maryam Molamohammadi
链接: https://arxiv.org/abs/2604.22679v1
完整摘要: The increasing adoption of AI systems in hiring has raised concerns about algorithmic bias and accountability, prompting regulatory responses including the EU AI Act, NYC Local Law 144, and Colorado's AI Act. While existing research examines bias through technical or regulatory lenses, both perspectives overlook a fundamental challenge: modern AI hiring systems operate within complex supply chains where responsibility fragments across data vendors, model developers, platform providers, and deploying organizations. This paper investigates how these dependency chains complicate bias evaluation and accountability attribution. Drawing on literature review and regulatory analysis, we demonstrate that fragmented responsibilities create two critical problems. First, bias emerges from component interactions rather than isolated elements, yet proprietary configurations prevent integrated evaluation. A resume parser may function without bias independently but contribute to discrimination when integrated with specific ranking algorithms and filtering thresholds. Second, information asymmetries mean deploying organizations bear legal responsibility without technical visibility into vendor-supplied algorithms, while vendors control implementations without meaningful disclosure requirements. Each stakeholder may believe they are compliant; nevertheless, the integrated system may produce biased outcomes. Analysis of implementation ambiguities reveals these challenges in practice. We propose multi-layered interventions including system-level audits, vendor guidelines, continuous monitoring mechanisms, and documentation across dependency chains. Our findings reveal that effective governance requires coordinated action across technical, organizational, and regulatory domains to establish meaningful accountability in distributed development environments.
匹配关键词: embodied AI
---

[ACADEMIC - ARXIV]
标题: Rethinking XAI Evaluation: A Human-Centered Audit of Shapley Benchmarks in High-Stakes Settings
作者: Inês Oliveira e Silva, Sérgio Jesus, Iker Perez, Rita P. Ribeiro, Carlos Soares, Hugo Ferreira, Pedro Bizarro
链接: https://arxiv.org/abs/2604.22662v1
完整摘要: Shapley values are a cornerstone of explainable AI, yet their proliferation into competing formulations has created a fragmented landscape with little consensus on practical deployment. While theoretical differences are well-documented, evaluation remains reliant on quantitative proxies whose alignment with human utility is unverified. In this work, we use a unified amortized framework to isolate semantic differences between eight Shapley variants under the low-latency constraints of operational risk workflows. We conduct a large-scale empirical evaluation across four risk datasets and a realistic fraud-detection environment involving professional analysts and 3,735 case reviews. Our results reveal a fundamental misalignment: standard quantitative metrics, such as sparsity and faithfulness, are decoupled from human-perceived clarity and decision utility. Furthermore, while no formulation improved objective analyst performance, explanations consistently increased decision confidence, signaling a critical risk of automation bias in high-stakes settings. These findings suggest that current evaluation proxies are insufficient for predicting downstream human impact, and we provide evidence-based guidance for selecting formulations and metrics in operational decision systems.
匹配关键词: embodied AI
---

[ACADEMIC - ARXIV]
标题: GCImOpt: Learning efficient goal-conditioned policies by imitating optimal trajectories
作者: Jon Goikoetxea, Jesús F. Palacián
链接: https://arxiv.org/abs/2604.22724v1
完整摘要: Imitation learning is a well-established approach for machine-learning-based control. However, its applicability depends on having access to demonstrations, which are often expensive to collect and/or suboptimal for solving the task. In this work, we present GCImOpt, an approach to learn efficient goal-conditioned policies by training on datasets generated by trajectory optimization. Our approach for dataset generation is computationally efficient, can generate thousands of optimal trajectories in minutes on a laptop computer, and produces high-quality demonstrations. Further, by means of a data augmentation scheme that treats intermediate states as goals, we are able to increase the training dataset size by an order of magnitude. Using our generated datasets, we train goal-conditioned neural network policies that can control the system towards arbitrary goals. To demonstrate the generality of our approach, we generate datasets and then train policies for various control tasks, namely cart-pole stabilization, planar and three-dimensional quadcopter stabilization, and point reaching using a 6-DoF robot arm. We show that our trained policies can achieve high success rates and near-optimal control profiles, all while being small (less than 80,000 neural network parameters) and fast enough (up to more than 6,000 times faster than a trajectory optimization solver) that they could be deployed onboard resource-constrained controllers. We provide videos, code, datasets and pre-trained policies under a free software license; see our project website https://jongoiko.github.io/gcimopt/.
匹配关键词: robotics
---

[ACADEMIC - ARXIV]
标题: ATRS: Adaptive Trajectory Re-splitting via a Shared Neural Policy for Parallel Optimization
作者: Jiajun Yu, Guodong Liu, Li Wang, Pengxiang Zhou, Wentao Liu, Yin He, Chao Xu, Fei Gao, Yanjun Cao
链接: https://arxiv.org/abs/2604.22715v1
完整摘要: Parallel trajectory optimization via the Alternating Direction Method of Multipliers (ADMM) has emerged as a scalable approach to long-horizon motion planning. However, existing frameworks typically decompose the problem into parallel subproblems based on a predefined fixed structure. Such structural rigidity often causes optimization stagnation in highly constrained regions, where a few lagging subproblems delay global convergence. A natural remedy is to adaptively re-split these stagnating segments online. Yet, deciding when, where, and how to split exceeds the capability of rule-based heuristics. To this end, we propose ATRS, a novel framework that embeds a shared Deep Reinforcement Learning policy into the parallel ADMM loop. We formulate this adaptive adjustment as a Multi-Agent Shared-Policy Markov Decision Process, where all trajectory segments act as homogeneous agents and share a unified neural policy network. This parameter-sharing architecture endows the system with size invariance, enabling it to handle dynamically changing segment counts during re-splitting and generalize to arbitrary trajectory lengths. Furthermore, our formulation inherently supports zero-shot generalization to unseen environments, as our network relies solely on the internal states of the numerical solver rather than on the geometric features of the environment. To ensure solver stability, a Confidence-Based Election mechanism selects only the most stagnating segment for re-splitting at each step. Extensive simulations demonstrate that ATRS accelerates convergence, reducing the number of iterations by up to 26.0% and the computation time by up to 19.1%. Real-world experiments further confirm its applicability to both large-scale offline global planning and real-time onboard replanning within 35 ms per cycle, with no sim-to-real degradation.
匹配关键词: robotics
---

[ACADEMIC - ARXIV]
标题: GazeVLA: Learning Human Intention for Robotic Manipulation
作者: Chengyang Li, Kaiyi Xiong, Yuan Xu, Lei Qian, Yizhou Wang, Wentao Zhu
链接: https://arxiv.org/abs/2604.22615v1
完整摘要: Embodied foundation models have achieved significant breakthroughs in robotic manipulation, yet they still depend heavily on large-scale robot demonstrations. Although recent works have explored leveraging human data to alleviate this dependency, effectively extracting transferable knowledge remains a significant challenge due to the inherent embodiment gap between human and robot. We argue that the intention underlying human actions can serve as a powerful intermediate representation for bridging this gap. In this paper, we introduce a novel framework that explicitly learns and transfers human intention to facilitate robotic manipulation. Specifically, we model intention through gaze, as it naturally precedes physical actions and serves as an observable proxy for human intent. Our model is first pretrained on a large-scale egocentric human dataset to capture human intention and its synergy with action, followed by finetuning on a small set of robot and human data. During inference, the model adopts a Chain-of-Thought reasoning paradigm, sequentially predicting intention before executing the action. Extensive evaluations in simulation and real-world settings, across long-horizon and fine-grained tasks, and under few-shot and robustness benchmarks, show that our method consistently outperforms strong baselines, generalizes better, and achieves state-of-the-art performance.
匹配关键词: robotics
---

[ACADEMIC - ARXIV]
标题: RedVLA: Physical Red Teaming for Vision-Language-Action Models
作者: Yuhao Zhang, Borong Zhang, Jiaming Fan, Jiachen Shen, Yishuai Cai, Yaodong Yang, Jiaming Ji
链接: https://arxiv.org/abs/2604.22591v1
完整摘要: The real-world deployment of Vision-Language-Action (VLA) models remains limited by the risk of unpredictable and irreversible physical harm. However, we currently lack effective mechanisms to proactively detect these physical safety risks before deployment. To address this gap, we propose \textbf{RedVLA}, the first red teaming framework for physical safety in VLA models. We systematically uncover unsafe behaviors through a two-stage process: (I) \textbf{Risk Scenario Synthesis} constructs a valid and task-feasible initial risk scene. Specifically, it identifies critical interaction regions from benign trajectories and positions the risk factor within these regions, aiming to entangle it with the VLA's execution flow and elicit a target unsafe behavior. (II) \textbf{Risk Amplification} ensures stable elicitation across heterogeneous models. It iteratively refines the risk factor state through gradient-free optimization guided by trajectory features. Experiments on six representative VLA models show that RedVLA uncovers diverse unsafe behaviors and achieves the ASR up to 95.5\% within 10 optimization iterations. To mitigate these risks, we further propose SimpleVLA-Guard, a lightweight safety guard built from RedVLA-generated data. Our data, assets, and code are available \href{https://redvla.github.io}{here}.
匹配关键词: robotics
---

[ACADEMIC - ARXIV]
标题: QDTraj: Exploration of Diverse Trajectory Primitives for Articulated Objects Robotic Manipulation
作者: Mathilde Kappel, Mahdi Khoramshahi, Louis Annabi, Faiz Ben Amar, Stéphane Doncieux
链接: https://arxiv.org/abs/2604.22551v1
完整摘要: Thanks to the latest advances in learning and robotics, domestic robots are beginning to enter homes, aiming to execute household chores autonomously. However, robots still struggle to perform autonomous manipulation tasks in open-ended environments. In this context, this paper presents a method that enables a robot to manipulate a wide spectrum of articulated objects. In this paper, we automatically generate different robot low-level trajectory primitives to manipulate given object articulations. A very important point when it comes to generating expert trajectories is to consider the diversity of solutions to achieve the same goal. Indeed, knowing diverse low-level primitives to accomplish the same task enables the robot to choose the optimal solution in its real-world environment, with live constraints and unexpected changes. To do so, we propose a method based on Quality-Diversity algorithms that leverages sparse reward exploration in order to generate a set of diverse and high-performing trajectory primitives for a given manipulation task. We validated our method, QDTraj, by generating diverse trajectories in simulation and deploying them in the real world. QDTraj generates at least 5 times more diverse trajectories for both hinge and slider activation tasks, outperforming the other methods we compared against. We assessed the generalization of our method over 30 articulations of the PartNetMobility articulated object dataset, with an average of 704 different trajectories by task. Code is publicly available at: https://kappel.web.isir.upmc.fr/trajectory_primitive_website
匹配关键词: robotics
---

[ACADEMIC - ARXIV]
标题: GCImOpt: Learning efficient goal-conditioned policies by imitating optimal trajectories
作者: Jon Goikoetxea, Jesús F. Palacián
链接: https://arxiv.org/abs/2604.22724v1
完整摘要: Imitation learning is a well-established approach for machine-learning-based control. However, its applicability depends on having access to demonstrations, which are often expensive to collect and/or suboptimal for solving the task. In this work, we present GCImOpt, an approach to learn efficient goal-conditioned policies by training on datasets generated by trajectory optimization. Our approach for dataset generation is computationally efficient, can generate thousands of optimal trajectories in minutes on a laptop computer, and produces high-quality demonstrations. Further, by means of a data augmentation scheme that treats intermediate states as goals, we are able to increase the training dataset size by an order of magnitude. Using our generated datasets, we train goal-conditioned neural network policies that can control the system towards arbitrary goals. To demonstrate the generality of our approach, we generate datasets and then train policies for various control tasks, namely cart-pole stabilization, planar and three-dimensional quadcopter stabilization, and point reaching using a 6-DoF robot arm. We show that our trained policies can achieve high success rates and near-optimal control profiles, all while being small (less than 80,000 neural network parameters) and fast enough (up to more than 6,000 times faster than a trajectory optimization solver) that they could be deployed onboard resource-constrained controllers. We provide videos, code, datasets and pre-trained policies under a free software license; see our project website https://jongoiko.github.io/gcimopt/.
匹配关键词: humanoid robot
---

[ACADEMIC - ARXIV]
标题: GazeVLA: Learning Human Intention for Robotic Manipulation
作者: Chengyang Li, Kaiyi Xiong, Yuan Xu, Lei Qian, Yizhou Wang, Wentao Zhu
链接: https://arxiv.org/abs/2604.22615v1
完整摘要: Embodied foundation models have achieved significant breakthroughs in robotic manipulation, yet they still depend heavily on large-scale robot demonstrations. Although recent works have explored leveraging human data to alleviate this dependency, effectively extracting transferable knowledge remains a significant challenge due to the inherent embodiment gap between human and robot. We argue that the intention underlying human actions can serve as a powerful intermediate representation for bridging this gap. In this paper, we introduce a novel framework that explicitly learns and transfers human intention to facilitate robotic manipulation. Specifically, we model intention through gaze, as it naturally precedes physical actions and serves as an observable proxy for human intent. Our model is first pretrained on a large-scale egocentric human dataset to capture human intention and its synergy with action, followed by finetuning on a small set of robot and human data. During inference, the model adopts a Chain-of-Thought reasoning paradigm, sequentially predicting intention before executing the action. Extensive evaluations in simulation and real-world settings, across long-horizon and fine-grained tasks, and under few-shot and robustness benchmarks, show that our method consistently outperforms strong baselines, generalizes better, and achieves state-of-the-art performance.
匹配关键词: humanoid robot
---

[ACADEMIC - ARXIV]
标题: QDTraj: Exploration of Diverse Trajectory Primitives for Articulated Objects Robotic Manipulation
作者: Mathilde Kappel, Mahdi Khoramshahi, Louis Annabi, Faiz Ben Amar, Stéphane Doncieux
链接: https://arxiv.org/abs/2604.22551v1
完整摘要: Thanks to the latest advances in learning and robotics, domestic robots are beginning to enter homes, aiming to execute household chores autonomously. However, robots still struggle to perform autonomous manipulation tasks in open-ended environments. In this context, this paper presents a method that enables a robot to manipulate a wide spectrum of articulated objects. In this paper, we automatically generate different robot low-level trajectory primitives to manipulate given object articulations. A very important point when it comes to generating expert trajectories is to consider the diversity of solutions to achieve the same goal. Indeed, knowing diverse low-level primitives to accomplish the same task enables the robot to choose the optimal solution in its real-world environment, with live constraints and unexpected changes. To do so, we propose a method based on Quality-Diversity algorithms that leverages sparse reward exploration in order to generate a set of diverse and high-performing trajectory primitives for a given manipulation task. We validated our method, QDTraj, by generating diverse trajectories in simulation and deploying them in the real world. QDTraj generates at least 5 times more diverse trajectories for both hinge and slider activation tasks, outperforming the other methods we compared against. We assessed the generalization of our method over 30 articulations of the PartNetMobility articulated object dataset, with an average of 704 different trajectories by task. Code is publicly available at: https://kappel.web.isir.upmc.fr/trajectory_primitive_website
匹配关键词: humanoid robot
---

[ACADEMIC - ARXIV]
标题: Decoding High-Dimensional Finger Motion from EMG Using Riemannian Features and RNNs
作者: Martin Colot, Cédric Simar, Guy Cheron, Ana Maria Cebolla Alvarez, Gianluca Bontempi
链接: https://arxiv.org/abs/2604.22499v1
完整摘要: Continuous estimation of high-dimensional finger kinematics from forearm surface electromyography (EMG) could enable natural control for hand prostheses, AR/XR interfaces, and teleoperation. However, the complexity of human hand gestures and the entanglement of forearm muscles make accurate recognition intrinsically challenging. Existing approaches typically reduce task complexity by relying on classification-based machine learning, limiting the controllable degrees of freedom and compromising on natural interaction. We present an end-to-end framework for continuous EMG-to-kinematics regression using only consumer-grade hardware. The framework combines an 8-channel EMG armband, a single webcam, and an automatic synchronization procedure, enabling the collection of the EMG Finger-Kinematics dataset (EMG-FK), a 10-h dataset of synchronized EMG and 15 finger joint angles from 20 participants performing rich, unconstrained right-hand motions. We also introduce the Temporal Riemannian Regressor (TRR), a lightweight GRU-based model that uses sequences of multi-band Riemannian covariance features to decode finger motion. Across EMG-FK and the public emg2pose benchmark, TRR outperforms state-of-the-art methods in both intra- and cross-subject evaluation. On EMG-FK, it reaches an average absolute error of $9.79 °\pm 1.48$ in intra-subject and $16.71 °\pm 3.97$ in cross-subject. Finally, we demonstrate real-time deployment on a Raspberry Pi 5 and intuitive control of a robotic hand; TRR runs at nearly 10 predictions/s and is roughly an order of magnitude faster than state-of-the-art approaches. Together, these contributions lower the barrier to reproducible, real-time EMG-based decoding of high-dimensional finger motion, and pave the way toward more natural and intuitive control of embedded EMG-based systems.
匹配关键词: humanoid robot
---

[ACADEMIC - ARXIV]
标题: Adaptive vs. Static Robot-to-Human Handover: A Study on Orientation and Approach Direction
作者: Federico Biagi, Dario Onfiani, Simone Silenzi, Cristina Iani, Luigi Biagiotti
链接: https://arxiv.org/abs/2604.22378v1
完整摘要: Robot-to-human handovers often rely on static, open-loop strategies (or, at best, approaches that adapt only the position), which generally do not consider how the object will be grasped by the human, thus requiring the user to adapt. This work presents a novel adaptive framework that dynamically adjusts the object's delivery pose in real time based on the user's hand pose and the intended downstream task. By integrating AI-based hand pose estimation with smooth, kinematically constrained trajectories, the system ensures a safe approach and an optimal handover orientation. A comprehensive user study compares the proposed adaptive approach against a static baseline across multiple tasks, evaluating both subjective metrics (NASA-TLX, Human-Robot Trust Scale) and objective physiological data (blink rate measured via wearable eye-trackers). The results demonstrate that dynamic alignment significantly reduces users' cognitive workload and physiological stress, while increasing perceived trust in the robot's reliability. These findings highlight the potential of task- and pose-aware systems for enabling fluid and ergonomic human-robot collaboration.
匹配关键词: humanoid robot
---

[ACADEMIC - ARXIV]
标题: Agentic World Modeling: Foundations, Capabilities, Laws, and Beyond
作者: Meng Chu, Xuan Billy Zhang, Kevin Qinghong Lin, Lingdong Kong, Jize Zhang, Teng Tu, Weijian Ma, Ziqi Huang, Senqiao Yang, Wei Huang, Yeying Jin, Zhefan Rao, Jinhui Ye, Xinyu Lin, Xichen Zhang, Qisheng Hu, Shuai Yang, Leyang Shen, Wei Chow, Yifei Dong, Fengyi Wu, Quanyu Long, Bin Xia, Shaozuo Yu, Mingkang Zhu, Wenhu Zhang, Jiehui Huang, Haokun Gui, Haoxuan Che, Long Chen, Qifeng Chen, Wenxuan Zhang, Wenya Wang, Xiaojuan Qi, Yang Deng, Yanwei Li, Mike Zheng Shou, Zhi-Qi Cheng, See-Kiong Ng, Ziwei Liu, Philip Torr, Jiaya Jia
链接: https://arxiv.org/abs/2604.22748v1
完整摘要: As AI systems move from generating text to accomplishing goals through sustained interaction, the ability to model environment dynamics becomes a central bottleneck. Agents that manipulate objects, navigate software, coordinate with others, or design experiments require predictive environment models, yet the term world model carries different meanings across research communities. We introduce a "levels x laws" taxonomy organized along two axes. The first defines three capability levels: L1 Predictor, which learns one-step local transition operators; L2 Simulator, which composes them into multi-step, action-conditioned rollouts that respect domain laws; and L3 Evolver, which autonomously revises its own model when predictions fail against new evidence. The second identifies four governing-law regimes: physical, digital, social, and scientific. These regimes determine what constraints a world model must satisfy and where it is most likely to fail. Using this framework, we synthesize over 400 works and summarize more than 100 representative systems spanning model-based reinforcement learning, video generation, web and GUI agents, multi-agent social simulation, and AI-driven scientific discovery. We analyze methods, failure modes, and evaluation practices across level-regime pairs, propose decision-centric evaluation principles and a minimal reproducible evaluation package, and outline architectural guidance, open problems, and governance challenges. The resulting roadmap connects previously isolated communities and charts a path from passive next-step prediction toward world models that can simulate, and ultimately reshape, the environments in which agents operate.
匹配关键词: manipulation
---

[ACADEMIC - ARXIV]
标题: Generative Modeling of Neurodegenerative Brain Anatomy with 4D Longitudinal Diffusion Model
作者: Nivetha Jayakumar, Swakshar Deb, Bahram Jafrasteh, Qingyu Zhao, Miaomiao Zhang
链接: https://arxiv.org/abs/2604.22700v1
完整摘要: Understanding and predicting the progression of neurodegenerative diseases remains a major challenge in medical AI, with significant implications for early diagnosis, disease monitoring, and treatment planning. However, most available longitudinal neuroimaging datasets are temporally sparse with a few follow-up scans per subject. This scarcity of temporal data limits our ability to model and accurately capture the continuous anatomical changes related to disease progression in individual subjects. To address this problem, we propose a novel 4D (3DxT) diffusion-based generative framework that effectively models and synthesizes longitudinal brain anatomy over time, conditioned on available clinical variables such as health status, age, sex, and other relevant factors. Moreover, while most current approaches focus on manipulating image intensity or texture, our method explicitly learns the data distribution of topology-preserving spatiotemporal deformations to effectively capture the geometric changes of brain structures over time. This design enables the realistic generation of future anatomical states and the reconstruction of anatomically consistent disease trajectories, providing a more faithful representation of longitudinal brain changes. We validate our model through both synthetic sequence generation and downstream longitudinal disease classification, as well as brain segmentation. Experiments on two large-scale longitudinal neuroimage datasets demonstrate that our method outperforms state-of-the-art baselines in generating anatomically accurate, temporally consistent, and clinically meaningful brain trajectories. Our code is available on Github.
匹配关键词: manipulation
---

[ACADEMIC - ARXIV]
标题: GazeVLA: Learning Human Intention for Robotic Manipulation
作者: Chengyang Li, Kaiyi Xiong, Yuan Xu, Lei Qian, Yizhou Wang, Wentao Zhu
链接: https://arxiv.org/abs/2604.22615v1
完整摘要: Embodied foundation models have achieved significant breakthroughs in robotic manipulation, yet they still depend heavily on large-scale robot demonstrations. Although recent works have explored leveraging human data to alleviate this dependency, effectively extracting transferable knowledge remains a significant challenge due to the inherent embodiment gap between human and robot. We argue that the intention underlying human actions can serve as a powerful intermediate representation for bridging this gap. In this paper, we introduce a novel framework that explicitly learns and transfers human intention to facilitate robotic manipulation. Specifically, we model intention through gaze, as it naturally precedes physical actions and serves as an observable proxy for human intent. Our model is first pretrained on a large-scale egocentric human dataset to capture human intention and its synergy with action, followed by finetuning on a small set of robot and human data. During inference, the model adopts a Chain-of-Thought reasoning paradigm, sequentially predicting intention before executing the action. Extensive evaluations in simulation and real-world settings, across long-horizon and fine-grained tasks, and under few-shot and robustness benchmarks, show that our method consistently outperforms strong baselines, generalizes better, and achieves state-of-the-art performance.
匹配关键词: manipulation
---

[ACADEMIC - ARXIV]
标题: Data-Free Contribution Estimation in Federated Learning using Gradient von Neumann Entropy
作者: Asim Ukaye, Mubarak Abdu-Aguye, Nurbek Tastan, Karthik Nandakumar
链接: https://arxiv.org/abs/2604.22562v1
完整摘要: Client contribution estimation in Federated Learning is necessary for identifying clients' importance and for providing fair rewards. Current methods often rely on server-side validation data or self-reported client information, which can compromise privacy or be susceptible to manipulation. We introduce a data-free signal based on the matrix von Neumann (spectral) entropy of the final-layer updates, which measures the diversity of the information contributed. We instantiate two practical schemes: (i) SpectralFed, which uses normalized entropy as aggregation weights, and (ii) SpectralFuse, which fuses entropy with class-specific alignment via a rank-adaptive Kalman filter for per-round stability. Across CIFAR-10/100 and the naturally partitioned FEMNIST and FedISIC benchmarks, entropy-derived scores show a consistently high correlation with standalone client accuracy under diverse non-IID regimes - without validation data or client metadata. We compare our results with data-free contribution estimation baselines and show that spectral entropy serves as a useful indicator of client contribution.
匹配关键词: manipulation
---

[ACADEMIC - ARXIV]
标题: QDTraj: Exploration of Diverse Trajectory Primitives for Articulated Objects Robotic Manipulation
作者: Mathilde Kappel, Mahdi Khoramshahi, Louis Annabi, Faiz Ben Amar, Stéphane Doncieux
链接: https://arxiv.org/abs/2604.22551v1
完整摘要: Thanks to the latest advances in learning and robotics, domestic robots are beginning to enter homes, aiming to execute household chores autonomously. However, robots still struggle to perform autonomous manipulation tasks in open-ended environments. In this context, this paper presents a method that enables a robot to manipulate a wide spectrum of articulated objects. In this paper, we automatically generate different robot low-level trajectory primitives to manipulate given object articulations. A very important point when it comes to generating expert trajectories is to consider the diversity of solutions to achieve the same goal. Indeed, knowing diverse low-level primitives to accomplish the same task enables the robot to choose the optimal solution in its real-world environment, with live constraints and unexpected changes. To do so, we propose a method based on Quality-Diversity algorithms that leverages sparse reward exploration in order to generate a set of diverse and high-performing trajectory primitives for a given manipulation task. We validated our method, QDTraj, by generating diverse trajectories in simulation and deploying them in the real world. QDTraj generates at least 5 times more diverse trajectories for both hinge and slider activation tasks, outperforming the other methods we compared against. We assessed the generalization of our method over 30 articulations of the PartNetMobility articulated object dataset, with an average of 704 different trajectories by task. Code is publicly available at: https://kappel.web.isir.upmc.fr/trajectory_primitive_website
匹配关键词: manipulation
---

[ACADEMIC - ARXIV]
标题: ATRS: Adaptive Trajectory Re-splitting via a Shared Neural Policy for Parallel Optimization
作者: Jiajun Yu, Guodong Liu, Li Wang, Pengxiang Zhou, Wentao Liu, Yin He, Chao Xu, Fei Gao, Yanjun Cao
链接: https://arxiv.org/abs/2604.22715v1
完整摘要: Parallel trajectory optimization via the Alternating Direction Method of Multipliers (ADMM) has emerged as a scalable approach to long-horizon motion planning. However, existing frameworks typically decompose the problem into parallel subproblems based on a predefined fixed structure. Such structural rigidity often causes optimization stagnation in highly constrained regions, where a few lagging subproblems delay global convergence. A natural remedy is to adaptively re-split these stagnating segments online. Yet, deciding when, where, and how to split exceeds the capability of rule-based heuristics. To this end, we propose ATRS, a novel framework that embeds a shared Deep Reinforcement Learning policy into the parallel ADMM loop. We formulate this adaptive adjustment as a Multi-Agent Shared-Policy Markov Decision Process, where all trajectory segments act as homogeneous agents and share a unified neural policy network. This parameter-sharing architecture endows the system with size invariance, enabling it to handle dynamically changing segment counts during re-splitting and generalize to arbitrary trajectory lengths. Furthermore, our formulation inherently supports zero-shot generalization to unseen environments, as our network relies solely on the internal states of the numerical solver rather than on the geometric features of the environment. To ensure solver stability, a Confidence-Based Election mechanism selects only the most stagnating segment for re-splitting at each step. Extensive simulations demonstrate that ATRS accelerates convergence, reducing the number of iterations by up to 26.0% and the computation time by up to 19.1%. Real-world experiments further confirm its applicability to both large-scale offline global planning and real-time onboard replanning within 35 ms per cycle, with no sim-to-real degradation.
匹配关键词: sim-to-real
---

[ACADEMIC - ARXIV]
标题: Information-Theoretic Geometry Optimization and Physics-Aware Learning for Calibration-Free Magnetic Localization
作者: Wenxuan Xie, Yuelin Zhang, Qingpeng Ding, Jianghua Chen, Jiewen Tan, Jiwei Shan, Shing Shin Cheng
链接: https://arxiv.org/abs/2604.22526v1
完整摘要: Wireless localization of permanent magnets enables occlusion-free guidance for medical interventions, yet its practical accuracy is fundamentally limited by two coupled challenges: the poor observability of conventional planar sensor arrays and the simulation-to-reality (Sim-to-Real) gap of learning-based estimators. To address these issues, this article presents a unified framework that combines information-theoretic sensor geometry optimization with physics-aware deep learning. First, a rigorous Fisher Information Matrix (FIM)-based evaluation framework is established to quantify geometry-induced observability limitations. The results show that a staggered split-array topology provides a substantially stronger observability foundation for localization while remaining compatible with practical external deployment. Second, building on this optimized sensing configuration, we propose Phy-GAANet, a calibration-free estimator trained entirely on hardware-aware synthetic data. By incorporating Physics-Informed Features (PIF) for saturation modeling and Geometry-Aware Attention (GAA) for preserving cross-layer vector structure, the network effectively bridges the Sim-to-Real gap. Extensive real-world experiments demonstrate state-of-the-art performance, achieving a position error of 1.84 mm and an orientation error of 3.18 degrees at a refresh rate exceeding 270 Hz. The proposed method consistently outperforms classical Levenberg--Marquardt solvers and generic convolutional baselines, particularly in suppressing catastrophic outliers and maintaining robustness in challenging near-field boundary regions. Beyond the proposed network, the FIM-guided analysis also provides a framework for sensor geometry design in magnetic localization systems under practical deployment constraints.
匹配关键词: sim-to-real
---

[ACADEMIC - ARXIV]
标题: Mochi: Aligning Pre-training and Inference for Efficient Graph Foundation Models via Meta-Learning
作者: João Mattos, Arlei Silva
链接: https://arxiv.org/abs/2604.22031v1
完整摘要: We propose Mochi, a Graph Foundation Model that addresses task unification and training efficiency by adopting a meta-learning based training framework. Prior models pre-train with reconstruction-based objectives such as link prediction, and assume that the resulting representations can be aligned with downstream tasks through a separate unification step such as class prototypes. We demonstrate through synthetic and real-world experiments that this procedure, while simple and intuitive, has limitations that directly affect downstream task performance. To address these limitations, Mochi pre-trains on few-shot episodes that mirror the downstream evaluation protocol, aligning the training objective with inference rather than relying on a post-hoc unification step. We show that Mochi, along with its more powerful variant Mochi++, achieves competitive or superior performance compared to existing Graph Foundation Models across 25 real-world graph datasets spanning node classification, link prediction, and graph classification, while requiring 8$\sim$27 times less training time than the strongest baseline.
匹配关键词: sim-to-real
---

[ACADEMIC - ARXIV]
标题: Do MLLMs Understand Pointing? Benchmarking and Enhancing Referential Reasoning in Egocentric Vision
作者: Chentao Li, Zirui Gao, Mingze Gao, Yinglian Ren, Jianjiang Feng, Jie Zhou
链接: https://arxiv.org/abs/2604.21461v1
完整摘要: Egocentric AI agents, such as smart glasses, rely on pointing gestures to resolve referential ambiguities in natural language commands. However, despite advancements in Multimodal Large Language Models (MLLMs), current systems often fail to precisely ground the spatial semantics of pointing. Instead, they rely on spurious correlations with visual proximity or object saliency, a phenomenon we term "Referential Hallucination." To address this gap, we introduce EgoPoint-Bench, a comprehensive question-answering benchmark designed to evaluate and enhance multimodal pointing reasoning in egocentric views. Comprising over 11k high-fidelity simulated and real-world samples, the benchmark spans five evaluation dimensions and three levels of referential complexity. Extensive experiments demonstrate that while state-of-the-art proprietary and open-source models struggle with egocentric pointing, models fine-tuned on our synthetic data achieve significant performance gains and robust sim-to-real generalization. This work highlights the importance of spatially aware supervision and offers a scalable path toward precise egocentric AI assistants. Project page: https://guyyyug.github.io/EgoPoint-Bench/
匹配关键词: sim-to-real
---

[ACADEMIC - ARXIV]
标题: Listen and Chant Before You Read: The Ladder of Beauty in LM Pre-Training
作者: Yoshinori Nomura
链接: https://arxiv.org/abs/2604.21265v1
完整摘要: We show that pre-training a Transformer on music before language significantly accelerates language acquisition. Using piano performances (MAESTRO dataset), a developmental pipeline -- music $\to$ poetry $\to$ prose -- yields a $17.5\%$ perplexity improvement over random initialization ($p < 0.001$, 5 seeds), with music and poetry improving orthogonal model components (internal computation and embeddings, respectively). Convergence tests confirm that this is not a transient head start: at $d\!=\!64$, multi-seed validation (5 seeds) shows a persistent 5.5\% gap at plateau ($p = 0.017$), with the pipeline converging faster and to a lower loss in every run. Real music matches the transfer ceiling of synthetic patterns with one-third the data, and scaling experiments reveal that optimal pre-training data volume shifts with model capacity ($-3\% \to +3\% \to +6\%$ advantage of larger datasets from $d\!=\!16$ to $d\!=\!64$). Across the scales we study ($d\!\in\!\{16,32,64\}$, up to ${\sim}400$K parameters), these results suggest a capacity-dependent data curation principle and indicate that structured human creative outputs can provide an efficient pre-training substrate for small language models; stronger conclusions at modern pre-training scale will require substantially larger experiments.
匹配关键词: sim-to-real
---

[ACADEMIC - ARXIV]
标题: How Do AI Agents Spend Your Money? Analyzing and Predicting Token Consumption in Agentic Coding Tasks
作者: Longju Bai, Zhemin Huang, Xingyao Wang, Jiao Sun, Rada Mihalcea, Erik Brynjolfsson, Alex Pentland, Jiaxin Pei
链接: https://arxiv.org/abs/2604.22750v1
完整摘要: The wide adoption of AI agents in complex human workflows is driving rapid growth in LLM token consumption. When agents are deployed on tasks that require a significant amount of tokens, three questions naturally arise: (1) Where do AI agents spend the tokens? (2) Which models are more token-efficient? and (3) Can agents predict their token usage before task execution? In this paper, we present the first systematic study of token consumption patterns in agentic coding tasks. We analyze trajectories from eight frontier LLMs on SWE-bench Verified and evaluate models' ability to predict their own token costs before task execution. We find that: (1) agentic tasks are uniquely expensive, consuming 1000x more tokens than code reasoning and code chat, with input tokens rather than output tokens driving the overall cost; (2) token usage is highly variable and inherently stochastic: runs on the same task can differ by up to 30x in total tokens, and higher token usage does not translate into higher accuracy; instead, accuracy often peaks at intermediate cost and saturates at higher costs; (3) models vary substantially in token efficiency: on the same tasks, Kimi-K2 and Claude-Sonnet-4.5, on average, consume over 1.5 million more tokens than GPT-5; (4) task difficulty rated by human experts only weakly aligns with actual token costs, revealing a fundamental gap between human-perceived complexity and the computational effort agents actually expend; and (5) frontier models fail to accurately predict their own token usage (with weak-to-moderate correlations, up to 0.39) and systematically underestimate real token costs. Our study offers new insights into the economics of AI agents and can inspire future research in this direction.
匹配关键词: world model
---

[ACADEMIC - ARXIV]
标题: Representational Harms in LLM-Generated Narratives Against Global Majority Nationalities
作者: Ilana Nguyen, Harini Suresh, Thema Monroe-White, Evan Shieh
链接: https://arxiv.org/abs/2604.22749v1
完整摘要: Large language models (LLMs) are increasingly used for text generation tasks from everyday use to high-stakes enterprise and government applications, including simulated interviews with asylum seekers. While many works highlight the new potential applications of LLMs, there are risks of LLMs encoding and perpetuating harmful biases about non-dominant communities across the globe. To better evaluate and mitigate such harms, more research examining how LLMs portray diverse individuals is needed. In this work, we study how national origin identities are portrayed by widely-adopted LLMs in response to open-ended narrative generation prompts. Our findings demonstrate the presence of persistent representational harms by national origin, including harmful stereotypes, erasure, and one-dimensional portrayals of Global Majority identities. Minoritized national identities are simultaneously underrepresented in power-neutral stories and overrepresented in subordinated character portrayals, which are over fifty times more likely to appear than dominant portrayals. The degree of harm is amplified when US nationality cues (e.g., ``American'') are present in input prompts. Notably, we find that the harms we identify cannot be explained away via sycophancy, as US-centric biases persist even when replacing US nationality cues with non-US national identities in the prompts. Based on our findings, we call for further exploration of cultural harms in LLMs through methodologies that center Global Majority perspectives and challenge the uncritical adoption of US-based LLMs for the classification, surveillance, and misrepresentation of the majority of our planet.
匹配关键词: world model
---

[ACADEMIC - ARXIV]
标题: Agentic World Modeling: Foundations, Capabilities, Laws, and Beyond
作者: Meng Chu, Xuan Billy Zhang, Kevin Qinghong Lin, Lingdong Kong, Jize Zhang, Teng Tu, Weijian Ma, Ziqi Huang, Senqiao Yang, Wei Huang, Yeying Jin, Zhefan Rao, Jinhui Ye, Xinyu Lin, Xichen Zhang, Qisheng Hu, Shuai Yang, Leyang Shen, Wei Chow, Yifei Dong, Fengyi Wu, Quanyu Long, Bin Xia, Shaozuo Yu, Mingkang Zhu, Wenhu Zhang, Jiehui Huang, Haokun Gui, Haoxuan Che, Long Chen, Qifeng Chen, Wenxuan Zhang, Wenya Wang, Xiaojuan Qi, Yang Deng, Yanwei Li, Mike Zheng Shou, Zhi-Qi Cheng, See-Kiong Ng, Ziwei Liu, Philip Torr, Jiaya Jia
链接: https://arxiv.org/abs/2604.22748v1
完整摘要: As AI systems move from generating text to accomplishing goals through sustained interaction, the ability to model environment dynamics becomes a central bottleneck. Agents that manipulate objects, navigate software, coordinate with others, or design experiments require predictive environment models, yet the term world model carries different meanings across research communities. We introduce a "levels x laws" taxonomy organized along two axes. The first defines three capability levels: L1 Predictor, which learns one-step local transition operators; L2 Simulator, which composes them into multi-step, action-conditioned rollouts that respect domain laws; and L3 Evolver, which autonomously revises its own model when predictions fail against new evidence. The second identifies four governing-law regimes: physical, digital, social, and scientific. These regimes determine what constraints a world model must satisfy and where it is most likely to fail. Using this framework, we synthesize over 400 works and summarize more than 100 representative systems spanning model-based reinforcement learning, video generation, web and GUI agents, multi-agent social simulation, and AI-driven scientific discovery. We analyze methods, failure modes, and evaluation practices across level-regime pairs, propose decision-centric evaluation principles and a minimal reproducible evaluation package, and outline architectural guidance, open problems, and governance challenges. The resulting roadmap connects previously isolated communities and charts a path from passive next-step prediction toward world models that can simulate, and ultimately reshape, the environments in which agents operate.
匹配关键词: world model
---

[ACADEMIC - ARXIV]
标题: Relaxation-Informed Training of Neural Network Surrogate Models
作者: Calvin Tsay
链接: https://arxiv.org/abs/2604.22746v1
完整摘要: ReLU neural networks trained as surrogate models can be embedded exactly in mixed-integer linear programs (MILPs), enabling global optimization over the learned function. The tractability of the resulting MILP depends on structural properties of the network, i.e., the number of binary variables in associated formulations and the tightness of the continuous LP relaxation. These properties are determined during training, yet standard training objectives (prediction loss with classical weight regularization) offer no mechanism to directly control them. This work studies training regularizers that directly target downstream MILP tractability. Specifically, we propose simple bound-based regularizers that penalize the big-M constants of MILP formulations and/or the number of unstable neurons. Moreover, we introduce an LP relaxation gap regularizer that explicitly penalizes the per-sample gap of the continuous relaxation at training points. We derive its associated gradient and provide an implementation from LP dual variables without custom automatic differentiation tools. We show that combining the above regularizers can approximate the full total derivative of the LP gap with respect to the network parameters, capturing both direct and indirect sensitivities. Experiments on non-convex benchmark functions and a two-stage stochastic programming problem with quantile neural network surrogates demonstrate that the proposed regularizers can reduce MILP solve times by up to four orders of magnitude relative to an unregularized baseline, while maintaining competitive surrogate model accuracy.
匹配关键词: world model
---

[ACADEMIC - ARXIV]
标题: Inter-Stance: A Dyadic Multimodal Corpus for Conversational Stance Analysis
作者: Xiang Zhang, Xiaotian Li, Taoyue Wang, Nan Bi, Xin Zhou, Cody Zhou, Zoie Wang, Andrew Yang, Yuming Su, Jeff Cohn, Qiang Ji, Lijun Yin
链接: https://arxiv.org/abs/2604.22739v1
完整摘要: Social interactions dominate our perceptions of the world and shape our daily behavior by attaching social meaning to acts as simple and spontaneous as gestures, facial expressions, voice, and speech. People mimic and otherwise respond to each other's postures, facial expressions, mannerisms, and other verbal and nonverbal behavior, and form appraisals or evaluations in the process. Yet, no publicly-available dataset includes multimodal recordings and self-report measures of multiple persons in social interaction. Dyadic recordings and annotation are lacking. We present a new data corpus of multimodal dyadic interaction (45 dyads, 90 persons) that includes synchronized multi-modality behavior (2D face video, 3D face geometry, thermal spectrum dynamics, voice and speech behavior, physiology (PPG, EDA, heart-rate, blood pressure, and respiration), and self-reported affect of all participants in a communicative interaction scenario. Two types of dyads are included: persons with shared past history and strangers. Annotations include social signals, agreement, disagreement, and neutral stance. With a potent emotion induction, these multimodal data will enable novel modeling of multimodal interpersonal behavior. We present extensive experiments to evaluate multimodal dyadic communication of dyads with and without interpersonal history, and their affect. This new database will make multimodal modeling of social interaction never possible before. The dataset includes 20TB of multimodal data to share with the research community.
匹配关键词: world model
---

[ACADEMIC - ARXIV]
标题: How Do AI Agents Spend Your Money? Analyzing and Predicting Token Consumption in Agentic Coding Tasks
作者: Longju Bai, Zhemin Huang, Xingyao Wang, Jiao Sun, Rada Mihalcea, Erik Brynjolfsson, Alex Pentland, Jiaxin Pei
链接: https://arxiv.org/abs/2604.22750v1
完整摘要: The wide adoption of AI agents in complex human workflows is driving rapid growth in LLM token consumption. When agents are deployed on tasks that require a significant amount of tokens, three questions naturally arise: (1) Where do AI agents spend the tokens? (2) Which models are more token-efficient? and (3) Can agents predict their token usage before task execution? In this paper, we present the first systematic study of token consumption patterns in agentic coding tasks. We analyze trajectories from eight frontier LLMs on SWE-bench Verified and evaluate models' ability to predict their own token costs before task execution. We find that: (1) agentic tasks are uniquely expensive, consuming 1000x more tokens than code reasoning and code chat, with input tokens rather than output tokens driving the overall cost; (2) token usage is highly variable and inherently stochastic: runs on the same task can differ by up to 30x in total tokens, and higher token usage does not translate into higher accuracy; instead, accuracy often peaks at intermediate cost and saturates at higher costs; (3) models vary substantially in token efficiency: on the same tasks, Kimi-K2 and Claude-Sonnet-4.5, on average, consume over 1.5 million more tokens than GPT-5; (4) task difficulty rated by human experts only weakly aligns with actual token costs, revealing a fundamental gap between human-perceived complexity and the computational effort agents actually expend; and (5) frontier models fail to accurately predict their own token usage (with weak-to-moderate correlations, up to 0.39) and systematically underestimate real token costs. Our study offers new insights into the economics of AI agents and can inspire future research in this direction.
匹配关键词: agent
---

[ACADEMIC - ARXIV]
标题: Agentic World Modeling: Foundations, Capabilities, Laws, and Beyond
作者: Meng Chu, Xuan Billy Zhang, Kevin Qinghong Lin, Lingdong Kong, Jize Zhang, Teng Tu, Weijian Ma, Ziqi Huang, Senqiao Yang, Wei Huang, Yeying Jin, Zhefan Rao, Jinhui Ye, Xinyu Lin, Xichen Zhang, Qisheng Hu, Shuai Yang, Leyang Shen, Wei Chow, Yifei Dong, Fengyi Wu, Quanyu Long, Bin Xia, Shaozuo Yu, Mingkang Zhu, Wenhu Zhang, Jiehui Huang, Haokun Gui, Haoxuan Che, Long Chen, Qifeng Chen, Wenxuan Zhang, Wenya Wang, Xiaojuan Qi, Yang Deng, Yanwei Li, Mike Zheng Shou, Zhi-Qi Cheng, See-Kiong Ng, Ziwei Liu, Philip Torr, Jiaya Jia
链接: https://arxiv.org/abs/2604.22748v1
完整摘要: As AI systems move from generating text to accomplishing goals through sustained interaction, the ability to model environment dynamics becomes a central bottleneck. Agents that manipulate objects, navigate software, coordinate with others, or design experiments require predictive environment models, yet the term world model carries different meanings across research communities. We introduce a "levels x laws" taxonomy organized along two axes. The first defines three capability levels: L1 Predictor, which learns one-step local transition operators; L2 Simulator, which composes them into multi-step, action-conditioned rollouts that respect domain laws; and L3 Evolver, which autonomously revises its own model when predictions fail against new evidence. The second identifies four governing-law regimes: physical, digital, social, and scientific. These regimes determine what constraints a world model must satisfy and where it is most likely to fail. Using this framework, we synthesize over 400 works and summarize more than 100 representative systems spanning model-based reinforcement learning, video generation, web and GUI agents, multi-agent social simulation, and AI-driven scientific discovery. We analyze methods, failure modes, and evaluation practices across level-regime pairs, propose decision-centric evaluation principles and a minimal reproducible evaluation package, and outline architectural guidance, open problems, and governance challenges. The resulting roadmap connects previously isolated communities and charts a path from passive next-step prediction toward world models that can simulate, and ultimately reshape, the environments in which agents operate.
匹配关键词: agent
---

[ACADEMIC - ARXIV]
标题: ATRS: Adaptive Trajectory Re-splitting via a Shared Neural Policy for Parallel Optimization
作者: Jiajun Yu, Guodong Liu, Li Wang, Pengxiang Zhou, Wentao Liu, Yin He, Chao Xu, Fei Gao, Yanjun Cao
链接: https://arxiv.org/abs/2604.22715v1
完整摘要: Parallel trajectory optimization via the Alternating Direction Method of Multipliers (ADMM) has emerged as a scalable approach to long-horizon motion planning. However, existing frameworks typically decompose the problem into parallel subproblems based on a predefined fixed structure. Such structural rigidity often causes optimization stagnation in highly constrained regions, where a few lagging subproblems delay global convergence. A natural remedy is to adaptively re-split these stagnating segments online. Yet, deciding when, where, and how to split exceeds the capability of rule-based heuristics. To this end, we propose ATRS, a novel framework that embeds a shared Deep Reinforcement Learning policy into the parallel ADMM loop. We formulate this adaptive adjustment as a Multi-Agent Shared-Policy Markov Decision Process, where all trajectory segments act as homogeneous agents and share a unified neural policy network. This parameter-sharing architecture endows the system with size invariance, enabling it to handle dynamically changing segment counts during re-splitting and generalize to arbitrary trajectory lengths. Furthermore, our formulation inherently supports zero-shot generalization to unseen environments, as our network relies solely on the internal states of the numerical solver rather than on the geometric features of the environment. To ensure solver stability, a Confidence-Based Election mechanism selects only the most stagnating segment for re-splitting at each step. Extensive simulations demonstrate that ATRS accelerates convergence, reducing the number of iterations by up to 26.0% and the computation time by up to 19.1%. Real-world experiments further confirm its applicability to both large-scale offline global planning and real-time onboard replanning within 35 ms per cycle, with no sim-to-real degradation.
匹配关键词: agent
---

[ACADEMIC - ARXIV]
标题: QuantClaw: Precision Where It Matters for OpenClaw
作者: Manyi Zhang, Ji-Fu Li, Zhongao Sun, Xiaohao Liu, Zhenhua Dong, Xianzhi Yu, Haoli Bai, Xiaobo Xia
链接: https://arxiv.org/abs/2604.22577v1
完整摘要: Autonomous agent systems such as OpenClaw introduce significant efficiency challenges due to long-context inputs and multi-turn reasoning. This results in prohibitively high computational and monetary costs in real-world development. While quantization is a standard approach for reducing cost and latency, its impact on agent performance in realistic scenarios remains unclear. In this work, we analyze quantization sensitivity across diverse complex workflows over OpenClaw, and show that precision requirements are highly task-dependent. Based on this observation, we propose QuantClaw, a plug-and-play precision routing plugin that dynamically assigns precision according to task characteristics. QuantClaw routes lightweight tasks to lower-cost configurations while preserving higher precision for demanding workloads, saving cost and accelerating inference without increasing user complexity. Experiments show that our QuantClaw maintains or improves task performance while reducing both latency and computational cost. Across a range of agent tasks, it achieves up to 21.4% cost savings and 15.7% latency reduction on GLM-5 (FP8 baseline). These results highlight the benefit of treating precision as a dynamic resource in agent systems.
匹配关键词: agent
---

[ACADEMIC - ARXIV]
标题: SOLAR-RL: Semi-Online Long-horizon Assignment Reinforcement Learning
作者: Jichao Wang, Liuyang Bian, Yufeng Zhou, Han Xiao, Yue Pan, Guozhi Wang, Hao Wang, Zhaoxiong Wang, Yafei Wen, Xiaoxin Chen, Shuai Ren, Lingfang Zeng
链接: https://arxiv.org/abs/2604.22558v1
完整摘要: As Multimodal Large Language Models (MLLMs) mature, GUI agents are evolving from static interactions to complex navigation. While Reinforcement Learning (RL) has emerged as a promising paradigm for training MLLM agents on dynamic GUI tasks, its effective application faces a dilemma. Standard Offline RL often relies on static step-level data, neglecting global trajectory semantics such as task completion and execution quality. Conversely, Online RL captures the long-term dynamics but suffers from high interaction costs and potential environmental instability. To bridge this gap, we propose SOLAR-RL (Semi-Online Long-horizon Assignment Reinforcement Learning). Instead of relying solely on expensive online interactions, our framework integrates global trajectory insights directly into the offline learning process. Specifically, we reconstruct diverse rollout candidates from static data, detect the first failure point using per-step validity signals, and retroactively assign dense step-level rewards with target-aligned shaping to reflect trajectory-level execution quality, effectively simulating online feedback without interaction costs. Extensive experiments demonstrate that SOLAR-RL significantly improves long-horizon task completion rates and robustness compared to strong baselines, offering a sample-efficient solution for autonomous GUI navigation.
匹配关键词: agent
---

