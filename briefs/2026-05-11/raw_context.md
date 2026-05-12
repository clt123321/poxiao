# 破晓 PoXiao — 原始数据 (Raw Context)
生成时间: 2026-05-11 06:55 UTC
================================================================================

[RSS:Reddit LocalLLaMA (社区共识)]
Getting a feel for how fast X tokens/second really is.
https://www.reddit.com/r/LocalLLaMA/comments/1t99upf/getting_a_feel_for_how_fast_x_tokenssecond_really/
I love following all your adventures with local LLM setups. Quality and size of the models are important, but so is performance. Numbers don't really convey the experienced speed well, however. If someone claims they run Qwen 3.6-27B at 21 tokens/second, how fast is that? Is 10 tokens/second unusabl
---

[RSS:Reddit LocalLLaMA (社区共识)]
I Think I Spent Way Too Much Time Messing with Local LLMs
https://www.reddit.com/r/LocalLLaMA/comments/1t9jyfu/i_think_i_spent_way_too_much_time_messing_with/
Guys, I'm hearing coil whine in my sleep. Help /s &#32; submitted by &#32; /u/MrChilliBalls [link] &#32; [comments]
---

[RSS:Reddit LocalLLaMA (社区共识)]
Running Qwen3.6 35b a3b on 8gb vram and 32gb ram ~190k context
https://www.reddit.com/r/LocalLLaMA/comments/1t9eo83/running_qwen36_35b_a3b_on_8gb_vram_and_32gb_ram/
If anyone is looking for a good high-speed setup with ~190k context, this config has been working insanely well for me. I’m using my laptop as a server over Tailscale. Installed Linux on it and running: - Qwen3.6 35B A3B - RTX 4060 8GB VRAM - 32GB DDR5 5600MHz RAM - Q5 quant models Current models te
---

[RSS:Reddit LocalLLaMA (社区共识)]
MTP benchmark results: the nature of the generative task dictates whether you will benefit (coding) or get slower inference (creative) from speculative inference. No other factor comes close.
https://www.reddit.com/r/LocalLLaMA/comments/1t9gcar/mtp_benchmark_results_the_nature_of_the/
I recently published MTP quants of Qwen 3.6 27B and I was suprised by the reports here on reddit, and on HF, of users who were experiencing worst speed with speculative inference than without. This did not match what I was seeing, but when I tried to reproduce their exact usage, it confirmed what th
---

[RSS:Reddit LocalLLaMA (社区共识)]
Switched from OpenCode to Pi - What Settings/Plugins would you recommend?
https://www.reddit.com/r/LocalLLaMA/comments/1t9fta2/switched_from_opencode_to_pi_what_settingsplugins/
Hey, so I just switched from OpenCode to Pi. Main reason was just the speed and the &quot;bloated&quot; system instructions in OpenCode. Also, for some reason OpenCode seemed to hang right when I loaded a model in. However, I do really like the idea of Planning and Build mode as I don't need to worr
---

[RSS:Reddit LocalLLaMA (社区共识)]
I have DeepSeek V4 Pro at home
https://www.reddit.com/r/LocalLLaMA/comments/1t94ito/i_have_deepseek_v4_pro_at_home/
Just wanted to share that I used u/LegacyRemaster slightly modified (Q4_K_M conversion support) DeepSeek V4 CUDA repo (based on u/antirez work ) to convert and run Q4_K_M DeepSeek V4 Pro on my Epyc workstation (Genoa 9374F, 12 x 96GB RAM, single RTX PRO 6000 Max-Q) and it worked right from the start
---

[RSS:Reddit LocalLLaMA (社区共识)]
DeepSeek-V4-Flash W4A16+FP8 with MTP self-speculation: 85 tok/s @ 524k on 2× RTX PRO 6000 Max-Q
https://www.reddit.com/r/LocalLLaMA/comments/1t9em98/deepseekv4flash_w4a16fp8_with_mtp_selfspeculation/
TL;DR : DeepSeek-V4-Flash running at 85.52 tok/s @ 524k ctx and ~111 tok/s @ 128k single-stream on 2× RTX PRO 6000 Max-Q pasta-paul's DeepSeek-V4-Flash-W4A16-FP8 quant is great, but its MTP head silently gets stripped at load time (HF transformers has it in _keys_to_ignore_on_load_unexpected ), so -
---

[RSS:Reddit LocalLLaMA (社区共识)]
Anybody else noticing how good gemma-4-26b-a4b is with one-shotting three.js?
https://www.reddit.com/r/LocalLLaMA/comments/1t9cle9/anybody_else_noticing_how_good_gemma426ba4b_is/
I wrote up this little python app to cycle through a bunch of prompts like this: Single HTML file using three.js from CDN. A central rotating MeshNormalMaterial torus knot. Place a bright Sprite (AdditiveBlending, soft circular canvas texture) at a position projected to screen, and 6 smaller sprites
---

[RSS:Reddit LocalLLaMA (社区共识)]
Ran some Llama.cpp RPC test to see if its worth it. And if 10Gbe needed.
https://www.reddit.com/r/LocalLLaMA/comments/1t9lbcm/ran_some_llamacpp_rpc_test_to_see_if_its_worth_it/
Let me first say I am not doing anything with parallelism so these benchmarks and tests are not for you. That said if your hobbyist like me that is left wondering if can I use the GPUs my other PCs then I have some answers and but I'm still learning. There is probably a better config for Llama.cpp b
---

[RSS:Reddit LocalLLaMA (社区共识)]
Hello from 10KM high! - Thanks to Qwen 3.6 35b a3b!
https://www.reddit.com/r/LocalLLaMA/comments/1t92hff/hello_from_10km_high_thanks_to_qwen_36_35b_a3b/
Typing this on a cramped flight, but I was having issues connecting to the plane's wifi on my ubuntu laptop, when it was effortless on my phone. The issue I was having was the Laptop WiFi connected to the plane wifi network, but captive portal wouldn't load. Turns out systemd-resolved was using Dock
---

[RSS:Reddit LocalLLaMA (社区共识)]
Sharing "cull" : my open-source dataset tool for image scraping & classification & captioning pipeline
https://www.reddit.com/r/LocalLLaMA/comments/1t9jub0/sharing_cull_my_opensource_dataset_tool_for_image/
I open-sourced a tool I built and am maintaining called Cull . It’s a machine curation engine for AI image datasets, the kind of work that eats hours every time you want to train a LoRA, build a reference library, or just classify an archive that isn’t a 100,000-file mess. What it does, end to end S
---

[RSS:Reddit LocalLLaMA (社区共识)]
As of today, what's the *most stable* model to run on a 32Gb RAM Mac w/ 256k context?
https://www.reddit.com/r/LocalLLaMA/comments/1t9p4oe/as_of_today_whats_the_most_stable_model_to_run_on/
Hey everyone, I've been playing around with Gemma4 and Qwen3.6 on my 32Gb Macbook Pro M2 Max since their release but I'm struggling at finding: The best software to run it (oMLX, llama.cpp, ...) The best model + quant to pick The best settings for agentic workflows I have tried literal hundreds of s
---

[RSS:Reddit LocalLLaMA (社区共识)]
I built an open source hyperparameter search tool for diffusion fine-tunes- pick the winner based on scoring
https://www.reddit.com/r/LocalLLaMA/comments/1t9k8gy/i_built_an_open_source_hyperparameter_search_tool/
I kept running the same loop: train a LoRA, look at the samples, decide it’s “fine”, change three things at once, train again, then when a new dataset needs training, all the parameters previously need to be reviewed again. So I built something to take the hassle out of this. It’s called Bracket . Y
---

[RSS:Reddit LocalLLaMA (社区共识)]
NCCL-Free Tensor Parallelism on Dual Blackwell PCIe llama.cpp b9095 released!
https://www.reddit.com/r/LocalLLaMA/comments/1t96l6r/ncclfree_tensor_parallelism_on_dual_blackwell/
b9095 finally makes -sm tensor work on dual consumer Blackwell PCIe GPUs without NCCL If youre on dual Blackwell gpus this look like it could be big. I'll have my own results for 2x5060ti asap &#32; submitted by &#32; /u/Bulky-Priority6824 [link] &#32; [comments]
---

[RSS:Reddit LocalLLaMA (社区共识)]
Is HIPfire worth it for Strix Halo?
https://www.reddit.com/r/LocalLLaMA/comments/1t9gmyq/is_hipfire_worth_it_for_strix_halo/
Did anyone evaluate HIPfire for long context sizes (100k+) and quality, for Strix Halo? It apparently promises large performance increase over llama.cpp and the like. What TPS performance and quality did you get? &#32; submitted by &#32; /u/ivoras [link] &#32; [comments]
---

[RSS:Reddit LocalLLaMA (社区共识)]
Do you use subscriptions beside Local LLM?
https://www.reddit.com/r/LocalLLaMA/comments/1t9n09x/do_you_use_subscriptions_beside_local_llm/
For me I do, my graphics card is “old” GTX 1080, it is from 2016 or 2017, forgot when already, when they released it, the Nvidia Guy went on stage talking about the Pascal Architecture like they invented teleportation or something, and we all ran to give him our thousand dollars :) So, I am still wa
---

[RSS:Reddit LocalLLaMA (社区共识)]
Speeding up local LLM for usable coding agent
https://www.reddit.com/r/LocalLLaMA/comments/1t96kfh/speeding_up_local_llm_for_usable_coding_agent/
TL;DR: Qwen 3.6 35B-A3B (Q4_K_M) is running slow at around 9 t/s with 72% filled context (36147 tokens window) and a total response time of 77s including prefill and token generation. Ran this using LM Studio on Windows with the attached image settings, on a 5060 Ti (16GB VRAM) + 32GB system RAM. I 
---

[RSS:Reddit LocalLLaMA (社区共识)]
DS4
https://www.reddit.com/r/LocalLLaMA/comments/1t95k73/ds4/
The developer that created Redis, Salvatore Sanfilippo, has released a new project on GitHub named DS4. https://github.com/antirez/ds4/ The TL;DR on this one is getting DeepSeek V4 Flash running with a 1M context windows on Mac Metal hardware. Some novel techniques going on. A few hours ago he poste
---

[RSS:Reddit LocalLLaMA (社区共识)]
OpenClaw + oMLX shows 0 cached tokens, but Hermes uses cache fine with the same local model, what am I missing?
https://www.reddit.com/r/LocalLLaMA/comments/1t9rlkc/openclaw_omlx_shows_0_cached_tokens_but_hermes/
Hey everyone, I’m trying to debug a weird prompt cache issue with OpenClaw + oMLX, and I’d appreciate help from anyone running local agents on MLX/oMLX. The short version is this: I’m running oMLX v0.3.8 on my Mac, serving: Qwen3.6-35B-A3B-RotorQuant-MLX-4bit OpenClaw runs in Docker on my NAS and co
---

[RSS:Reddit LocalLLaMA (社区共识)]
Has anyone bought a 3080 20GB mod recently?
https://www.reddit.com/r/LocalLLaMA/comments/1t92h41/has_anyone_bought_a_3080_20gb_mod_recently/
I think it would suit my needs perfectly, but I'm scared of getting scammed on Alibaba so looking for some sellers who have delivered. Follow-up question for those who have the card, how well does it run Qwen 3.6 27B? &#32; submitted by &#32; /u/quickreactor [link] &#32; [comments]
---

[RSS:Reddit LocalLLaMA (社区共识)]
Is there any image2image model better than Qwen-Image-Edit-2511 and of comparable size?
https://www.reddit.com/r/LocalLLaMA/comments/1t9i65e/is_there_any_image2image_model_better_than/
I've tried with FLUX.2-9B but was not really better and FLUX.2-dev is too big. Any (tested) suggestions are most welcome. &#32; submitted by &#32; /u/HumanDrone8721 [link] &#32; [comments]
---

[RSS:Reddit MachineLearning (学术风向)]
PhD students in ML, how many hours on average do you work? [D]
https://www.reddit.com/r/MachineLearning/comments/1t9mwqy/phd_students_in_ml_how_many_hours_on_average_do/
I generally work around 9–10 hours a day, but not contiguously. I can usually carve out a dedicated chunk of time in the morning, take lab or project meetings in the afternoon, and block out around 6–8 PM for commute, exercise, socializing, and dinner. I also get more work done in the evening, since
---

[RSS:Reddit MachineLearning (学术风向)]
Signals: finding the most informative agent traces without LLM judges [R]
https://www.reddit.com/r/MachineLearning/comments/1t9d3et/signals_finding_the_most_informative_agent_traces/
Hello Peeps Salman, Shuguang and Adil here from Katanemo Labs (a DigitalOcean company). Wanted to introduce our latest research on agentic systems called Signals. If you've been building agents, you've probably noticed that there are far too many agent traces/trajectories to review one by one, and u
---

[RSS:Reddit MachineLearning (学术风向)]
Any implementations similar to D4RT? [D]
https://www.reddit.com/r/MachineLearning/comments/1t95gc6/any_implementations_similar_to_d4rt_d/
Deepmind released a paper on D4RT at the start of this year which crucially enabled a “4D” understanding of the world via structure from motion and generating: 1. Point cloud reconstruction from 2D videos (not static scenes) 2. Camera pose estimation You could pass in a video of a dog walking on a b
---

[RSS:Reddit MachineLearning (学术风向)]
Parax v0.7: Parametric Modeling in JAX [P]
https://www.reddit.com/r/MachineLearning/comments/1t929x3/parax_v07_parametric_modeling_in_jax_p/
Hi everyone! Parax is a library for &quot;Parametric modeling&quot; in JAX, attempting to bridge the approach between pure JAX PyTrees, and more object-orientated modeling approaches (e.g. using Equinox ). v0.7 has been released, featuring a more polished API as well as some detailed examples in the
---

[RSS:Reddit MachineLearning (学术风向)]
Why is human LLM annotation so expensive? [D]
https://www.reddit.com/r/MachineLearning/comments/1t9nc40/why_is_human_llm_annotation_so_expensive_d/
Scale AI and similar services charge a lot for annotation. MTurk is cheap but the quality is horrible for anything requiring real domain understanding. For small teams that need a few thousand labeled examples to calibrate their evals or fine tune a model, there seems to be no good middle ground. Ho
---

[RSS:Reddit MachineLearning (学术风向)]
"colss" a math-style expression evaluator for NumPy arrays [P]
https://www.reddit.com/r/MachineLearning/comments/1t8zja2/colss_a_mathstyle_expression_evaluator_for_numpy/
Built a small Python library called &quot;colss&quot; that lets you write NumPy expressions using a shorter, more mathematical syntax. Built using C++, OpenMP, pybind11, ExprTk, and NumPy. Github: https://github.com/SivaPA08/colss Example: a = np.array([1,2,3,4]) b = np.array([4,5,6,7]) c = 2 res = 
---

[RSS:Reddit Jobs & Careers (职场动态)]
How much will you miss traditional programming?
https://www.reddit.com/r/cscareerquestions/comments/1t97tv2/how_much_will_you_miss_traditional_programming/
I already miss it dearly. Saw a lot of people saying they love AI cause they don't have to type syntax anymore but I really struggle with the new workflow. Maybe it's cause I'm ADHD, but agentic coding just lets me wander off and get distracted from the actual problem. I used to be able to zone the 
---

[RSS:Reddit Jobs & Careers (职场动态)]
Accepted an offer at AMZN. How do I excel and what am I getting myself into?
https://www.reddit.com/r/cscareerquestions/comments/1t9gtf0/accepted_an_offer_at_amzn_how_do_i_excel_and_what/
Starting in a month in Amazon retail. Obviously everyone's heard of Amazon horror stories but my last job wasn't exactly a walk in the park either and Amazon pays better. Plus it's a great resume builder. Is making it to the one year mark a real concern here? Are there more layoffs actually coming? 
---

[RSS:Reddit Jobs & Careers (职场动态)]
Anyone experience as code clean up specialist?
https://www.reddit.com/r/cscareerquestions/comments/1t9f8qp/anyone_experience_as_code_clean_up_specialist/
So I applied at this company and they have new way of developing structures. On one side you got vibe code engineers, which often used to be business analyst without technical background who are developing new features and products from zero. And then you have so called code clean up specialist who 
---

[RSS:Reddit Jobs & Careers (职场动态)]
Been coasting in my career for the past few years, looking to make some changes
https://www.reddit.com/r/cscareerquestions/comments/1t9bnvb/been_coasting_in_my_career_for_the_past_few_years/
I've been at my current job for just over 5 years, still my first job since getting my CS degree (in 2020). I haven't been learning anything new or advancing my skills at my job in the past few years, so I'm looking to get a certification to improve my resume and find something better. I don't reall
---

[RSS:Reddit Jobs & Careers (职场动态)]
should I restudy discrete math?
https://www.reddit.com/r/cscareerquestions/comments/1t9f4p0/should_i_restudy_discrete_math/
so I did terrible in my semester of discrete mathematics and i cheated through SOME of the problem sets, and still did terrible on the final. Since discrete math is basically the foundations of problem solving in computer science, should I relearn it? this is also a question of how valuable it is to
---

[RSS:Reddit Jobs & Careers (职场动态)]
Anyone have any thoughts on this new Masters of Generative AI program?
https://www.reddit.com/r/cscareerquestions/comments/1t9ibls/anyone_have_any_thoughts_on_this_new_masters_of/
https://sps.cuny.edu/academics/graduate/master-of-science-in-generative-ai &#32; submitted by &#32; /u/rasputin1 [link] &#32; [comments]
---

[RSS:Reddit Jobs & Careers (职场动态)]
Got Rejected From an Unpaid “Internship” That Was Basically a Founding Engineer Role
https://www.reddit.com/r/cscareerquestions/comments/1t99cce/got_rejected_from_an_unpaid_internship_that_was/
I got rejected from an unpaid internship today and I genuinely don’t know whether I should feel bad about it or relieved. The role itself already sounded insane. They basically wanted someone to deploy and maintain their AI model/product, develop features for the application, handle AWS/cloud infras
---

[RSS:Reddit Jobs & Careers (职场动态)]
Lower Tier SWE vs. Big Tech Non-SWE
https://www.reddit.com/r/cscareerquestions/comments/1t96raj/lower_tier_swe_vs_big_tech_nonswe/
Hey everyone, just a quick question. Im currently very early into my career as a new grad. Im torn between 2 types of offers: 1) SWE positions (AI agent, backend, etc) at companies like SAP, Boeing, and what not 2) Tech Consulting positions (Proserve, Solutions Engineer) at companies like AWS, Micro
---

[RSS:Reddit Jobs & Careers (职场动态)]
Is it bad to do 3 interships at one company?
https://www.reddit.com/r/cscareerquestions/comments/1t9edcn/is_it_bad_to_do_3_interships_at_one_company/
I’m graduating this summer having completed three data internships at one company (F125), with a return offer for January 2027. The first internship was a low-impact data analytics role, and the second was a high-impact data engineering role. After my second internship, I got comfortable and decided
---

[RSS:Reddit Jobs & Careers (职场动态)]
Linkedin network usefulness when looking for a new job
https://www.reddit.com/r/cscareerquestions/comments/1t9e5c6/linkedin_network_usefulness_when_looking_for_a/
There have been multiple posts recently stating that network/ex-colleagues have been mostly useless. Now I am not talking about close connections aka family/friends, but folks you worked with in the same company, who at least have heard your name (or with whom you have common reputable connections) 
---

[RSS:Reddit Jobs & Careers (职场动态)]
How to grow in a company as an introvert?
https://www.reddit.com/r/cscareerquestions/comments/1t8xrxt/how_to_grow_in_a_company_as_an_introvert/
I’m very introverted and work 100% remote as an SDET whereas most of my company works onsite. Recently I’ve been tasked with leading some initiatives around AI tools and have found it very unnatural to showcase what I’m working on and get my name out there in my org. I’m more comfortable putting my 
---

[RSS:Reddit Jobs & Careers (职场动态)]
Resources for learning
https://www.reddit.com/r/cscareerquestions/comments/1t9msqx/resources_for_learning/
I want to start using my early time of the day of work reading tech news or articles or anything (and make it a habit) that would broaden my overall engineering knowledge. Looking for some good source whether it's to do with AI engineering, system design, business side of engineering etc, just anyth
---

[RSS:Reddit Jobs & Careers (职场动态)]
DSA Prep for Fall internships
https://www.reddit.com/r/cscareerquestions/comments/1t9lczv/dsa_prep_for_fall_internships/
Hello CS people, I am trying to prepare for fall internship OAs and interviews. I have mainly been doing some LeetCode problems, and I do know the basics of DSA, but I feel like I really need a more structured course to help me solidify the fundamentals. I am never able to solve the medium/hard prob
---

[RSS:Reddit Jobs & Careers (职场动态)]
I need some career advice.
https://www.reddit.com/r/cscareerquestions/comments/1t98axi/i_need_some_career_advice/
I need some career advice. I am currently working for a startup and have 6 months of work experience. I have realised that I was able to do most of the tasks with the help of AI. But I lacked in areas when it comes to planning to implement a product. Should I just keep focusing on backend developmen
---

[RSS:Reddit Jobs & Careers (职场动态)]
Is this a CSS Codility test?
https://www.reddit.com/r/cscareerquestions/comments/1t9acaj/is_this_a_css_codility_test/
I'm on a selection process and the next step is a Codility test. I clicked on the link and I saw this: You can write your solution(s) in CSS, PHP, php or txt*.* the availability of the programming languages depends on the task, and in some tasks the choice of programming languages might be limited. 
---

[RSS:Reddit Jobs & Careers (职场动态)]
Book recommendations for someone who doesn't know where to start
https://www.reddit.com/r/cscareerquestions/comments/1t9kh3j/book_recommendations_for_someone_who_doesnt_know/
I am a 9th grader, and I am so interested in the field of computer science. The problem is, I don't know where to start. There are so many different careers, topics, and fields, and I want to start exploring them this summer. I know how to program in HTML, CSS, a bit of python and C++, but I want to
---

[HACKERNEWS]
Hardware Attestation as Monopoly Enabler
https://grapheneos.social/@GrapheneOS/116550899908879585
Score: 1039 | Comments: 368
---

[HACKERNEWS]
Local AI needs to be the norm
https://unix.foo/posts/local-ai-needs-to-be-norm/
Score: 724 | Comments: 340
---

[HACKERNEWS]
I'm going back to writing code by hand
https://blog.k10s.dev/im-going-back-to-writing-code-by-hand/
Score: 116 | Comments: 49
---

[HACKERNEWS]
Running local models on an M4 with 24GB memory
https://jola.dev/posts/running-local-models-on-m4
Score: 162 | Comments: 59
---

[HACKERNEWS]
The Greatest Shot in Television: James Burke Had One Chance to Nail This Scene
https://www.openculture.com/2024/10/the-greatest-shot-in-television.html
Score: 30 | Comments: 6
---

[HACKERNEWS]
Incident Report: CVE-2024-YIKES
https://nesbitt.io/2026/02/03/incident-report-cve-2024-yikes.html
Score: 437 | Comments: 109
---

[HACKERNEWS]
Obsidian plugin was abused to deploy a remote access trojan
https://cyber.netsecops.io/articles/obsidian-plugin-abused-in-campaign-to-deploy-phantom-pulse-rat/
Score: 111 | Comments: 62
---

[HACKERNEWS]
An AI coding agent, used to write code, needs to reduce your maintenance costs
https://www.jamesshore.com/v2/blog/2026/you-need-ai-that-reduces-your-maintenance-costs
Score: 68 | Comments: 10
---

[HACKERNEWS]
Ask HN: What are you working on? (May 2026)
https://news.ycombinator.com/item?id=48085993
Score: 152 | Comments: 526
---

[HACKERNEWS]
Traces Of Humanity
https://tracesofhumanity.org/hello-world/
Score: 134 | Comments: 19
---

[HACKERNEWS]
Maryland citizens hit with $2B power grid upgrade for out-of-state AI
https://www.tomshardware.com/tech-industry/artificial-intelligence/maryland-citizens-slapped-with-usd2-billion-grid-upgrade-bill-for-out-of-state-ai-data-centers-state-complains-to-federal-energy-regulators-says-additional-cost-breaks-ratepayer-protection-pledge-promises
Score: 184 | Comments: 94
---

[HACKERNEWS]
How Fast Does Claude, Acting as a User Space IP Stack, Respond to Pings?
https://dunkels.com/adam/claude-user-space-ip-stack-ping/
Score: 23 | Comments: 4
---

[HACKERNEWS]
PS3 Emulator Devs Politely Ask That People Stop Flooding It with AI PRs
https://kotaku.com/playstation-3-emulator-devs-politely-ask-that-people-stop-flooding-it-with-ai-code-pull-requests-2000694656
Score: 108 | Comments: 74
---

[GITHUB]
vllm-project/vllm released v0.20.2
https://github.com/vllm-project/vllm/releases/tag/v0.20.2
Author: khluu
# vLLM v0.20.2 ## Highlights This release features 6 commits from 6 contributors (0 new)! This is a small patch release with bug fixes for DeepSeek V4, gpt-oss, and Qwen3-VL ### Bug Fixes * **DeepSeek V4 sparse attention**: Re-enable the persistent topk path on Hopper and ensure the memset kernel ru
---

[ACADEMIC - ARXIV]
标题: The Memory Curse: How Expanded Recall Erodes Cooperative Intent in LLM Agents
作者: Jiayuan Liu, Tianqin Li, Shiyi Du, Xin Luo, Haoxuan Zeng, Emanuel Tewolde, Tai Sing Lee, Tonghan Wang, Carl Kingsford, Vincent Conitzer
链接: https://arxiv.org/abs/2605.08060v1
完整摘要: Context window expansion is often treated as a straightforward capability upgrade for LLMs, but we find it systematically fails in multi-agent social dilemmas. Across 7 LLMs and 4 games over 500 rounds, expanding accessible history degrades cooperation in 18 of 28 model--game settings, a pattern we term the memory curse. We isolate the underlying mechanism through three analyses. First, lexical analysis of 378,000 reasoning traces associates this breakdown with eroding forward-looking intent rather than rising paranoia. We validate this using targeted fine-tuning as a cognitive probe: a LoRA adapter trained exclusively on forward-looking traces mitigates the decay and transfers zero-shot to distinct games. Second, memory sanitization holds prompt length fixed while replacing visible history with synthetic cooperative records, which restores cooperation substantially, proving the trigger is memory content, not length alone. Finally, ablating explicit Chain-of-Thought reasoning often reduces the collapse, showing that deliberation paradoxically amplifies the memory curse. Together, these results recast memory as an active determinant of multi-agent behavior: longer recall can either destabilize or support cooperation depending on the reasoning patterns it elicits.
匹配关键词: chain-of-thought
---

[ACADEMIC - ARXIV]
标题: Abductive Reasoning with Probabilistic Commonsense
作者: Joseph Cotnareanu, Chiara Roverato, Han Zhou, Didier Chetelat, Yingxue Zhang, Mark Coates
链接: https://arxiv.org/abs/2605.08011v1
完整摘要: Recent efforts to improve the reasoning abilities of Large Language Models (LLMs) have focused on integrating formal logic solvers within neurosymbolic frameworks. A key challenge is that formal solvers lack commonsense world knowledge, preventing them from making reasoning steps that humans find obvious. Prior methods address this by using LLMs to supply missing commonsense assumptions, but these approaches implicitly assume universal agreement on such commonsense facts. In reality, commonsense beliefs vary across individuals. We propose a probabilistic framework for abductive commonsense reasoning that explicitly models this variation, aiming to determine whether most people would judge a statement as true or false. We introduce Probabilistic Abductive CommonSense (PACS), a novel algorithm that uses an LLM and a formal solver to sample proofs as observations of individuals' distinct commonsense beliefs, and aggregates conclusions across these samples. Empirically, PACS outperforms chain-of-thought reasoning, prior neurosymbolic methods, and search-based approaches across multiple benchmarks.
匹配关键词: chain-of-thought
---

[ACADEMIC - ARXIV]
标题: Video Understanding Reward Modeling: A Robust Benchmark and Performant Reward Models
作者: Yuancheng Wei, Linli Yao, Lei Li, Haojie Zhang, Hao Zhou, Fandong Meng, Xu Sun
链接: https://arxiv.org/abs/2605.07872v1
完整摘要: Multimodal reward models have advanced substantially in text and image domains, yet progress in video understanding reward modeling remains severely limited by the lack of robust evaluation benchmarks and high-quality preference data. To address this, we propose a unified framework spanning benchmark design, data construction, and reward model training. We introduce Video Understanding Reward Bench (VURB), a benchmark featuring 2,100 preference pairs with long chain-of-thought reasoning traces (averaging 1,143 tokens) and majority voting evaluation across general, long, and reasoning-oriented video tasks. We further construct Video Understanding Preference Dataset (VUP-35K) via a fully automated pipeline, providing large-scale high-quality supervision for video reward training. Building on the data, we train VideoDRM and VideoGRM, a discriminative and a generative reward model, both achieving state-of-the-art performance on VURB and VideoRewardBench. Further analysis confirms that VUP-35K enhances both reward performance and model reasoning capability, while VideoDRM and VideoGRM yield significant gains under best-of-$N$ test-time scaling.
匹配关键词: chain-of-thought
---

[ACADEMIC - ARXIV]
标题: Tracing Uncertainty in Language Model "Reasoning"
作者: Nils Grünefeld, Bertram Højer, Philipp Mondorf, Barbara Plank, Anna Rogers, Christian Hardmeier, Stefan Heinrich, Jes Frellsen
链接: https://arxiv.org/abs/2605.07776v1
完整摘要: Language model (LM) "reasoning", commonly described as Chain-of-Thought or test-time scaling, often improves benchmark performance, but the dynamics underlying this process remain poorly understood. We study these dynamics through the lens of uncertainty quantification by treating the "reasoning" traces, the intermediate token sequences generated by LMs, as evolving model states. We summarize each trace by an uncertainty trace profile: a small set of features describing the shape of the uncertainty signal over its trace, such as its slope and linearity. We find that across five LMs evaluated on GSM8K and ProntoQA, these profiles predict whether a trace yields a correct final answer with AUROC up to 0.807, improving markedly on recent related work. We reach AUROC 0.801 using only the first few hundred tokens of full traces, suggesting that errors can be detected early in the generation. A detailed comparison of correct and incorrect traces further reveals qualitatively distinct uncertainty profiles, with correct traces showing a steeper and less linear decline in uncertainty. Together, the results suggest that our method, grounded in decision-making under uncertainty, provides a principled lens for studying the generative process underlying LM "reasoning".
匹配关键词: chain-of-thought
---

[ACADEMIC - ARXIV]
标题: The Coupling Tax: How Shared Token Budgets Undermine Visible Chain-of-Thought Under Fixed Output Limits
作者: Wenhua Nie, Junlin Liu, Jianan Wu, Zijie Meng, Yilong Fan, Zhang Zijian, Haoran Zheng, Jyh-Shing Roger Jang
链接: https://arxiv.org/abs/2605.07686v1
完整摘要: Chain-of-thought reasoning is often treated as a monotone way to improve language-model accuracy by letting a model think longer. We identify a countervailing effect, the coupling tax: when reasoning traces and final answers share one output-token budget, long traces can crowd out the answer they are meant to support. Across GSM8K, MATH-500, and five BIG-Bench Hard tasks with Qwen3 models at three scales, non-thinking mode matches or outperforms thinking mode on GSM8K and MATH-500 at every budget up to 2048 tokens, while harder tasks shift the crossover to larger budgets. We derive a truncation-waste decomposition, $\mathrm{Acc}_{\mathrm{think}}(b)=α_c F_L(b)+α_t(1-F_L(b))$, that predicts this crossover from chain-length and accuracy statistics and explains inverse scaling within the Qwen family. A DeepSeek-R1-Distill-Llama-8B replication shows the same pattern under a different thinking interface. As a mitigation, split-budget generation decouples reasoning and answer budgets; on full MATH-500, IRIS reaches 74.0% accuracy, a strengthened extraction variant reaches 78.8%, and a fixed non-oracle SC+IRIS gate reaches 83.6%. The results show that test-time reasoning should be evaluated as a budget-allocation problem, not only as a question of whether longer traces are available.
匹配关键词: chain-of-thought
---

[ACADEMIC - ARXIV]
标题: LLMs Improving LLMs: Agentic Discovery for Test-Time Scaling
作者: Tong Zheng, Haolin Liu, Chengsong Huang, Huiwen Bao, Sheng Zhang, Rui Liu, Runpeng Dai, Ruibo Chen, Chenxi Liu, Tianyi Xiong, Xidong Wu, Hongming Zhang, Heng Huang
链接: https://arxiv.org/abs/2605.08083v1
完整摘要: Test-time scaling (TTS) has become an effective approach for improving large language model performance by allocating additional computation during inference. However, existing TTS strategies are largely hand-crafted: researchers manually design reasoning patterns and tune heuristics by intuition, leaving much of the computation-allocation space unexplored. We propose an environment-driven framework, AutoTTS, that changes what researchers design: from individual TTS heuristics to environments where TTS strategies can be discovered automatically. The key to AutoTTS lies in environment construction: the discovery environment must make the control space tractable and provide cheap, frequent feedback for TTS search. As a concrete instantiation, we formulate width--depth TTS as controller synthesis over pre-collected reasoning trajectories and probe signals, where controllers decide when to branch, continue, probe, prune, or stop and can be evaluated cheaply without repeated LLM calls. We further introduce beta parameterization to make the search tractable and fine-grained execution trace feedback to improve discovery efficiency by helping the agent diagnose why a TTS program fails. Experiments on mathematical reasoning benchmarks show that the discovered strategies improve the overall accuracy--cost tradeoff over strong manually designed baselines. The discovered strategies generalize to held-out benchmarks and model scales, while the entire discovery costs only $39.9 and 160 minutes. Our data, and code will be open-source at https://github.com/zhengkid/AutoTTS.
匹配关键词: test-time compute
---

[ACADEMIC - ARXIV]
标题: Zero-Shot Imagined Speech Decoding via Imagined-to-Listened MEG Mapping
作者: Maryam Maghsoudi, Shihab Shamma
链接: https://arxiv.org/abs/2605.08075v1
完整摘要: Decoding imagined speech from non-invasive brain recordings is challenging because imagined datasets are scarce and difficult to align temporally across subjects and sessions In this work, we propose a new approach to the decoding of imagined speech that leverages the richer and more reliably labeled recordings during listening to speech. We collected paired listened and imagined MEG recordings to rhythmic melodic and spoken stimuli from trained musicians. Using trained musicians helped improve temporal alignment across conditions. We then developed a three-stage decoding pipeline that revealed consistent and meaningful relationships between neural activity evoked by imagining and listening to the same stimuli. First, we trained six linear and neural models to map imagined MEG responses to listened responses. We evaluated these models against a null baseline from unseen subjects to validate that the predicted-listening responses preserve stimulus-specific information. In the second stage, we trained a contrastive word decoder exclusively on the listened MEG responses, and evaluated it using four embedding strategies including semantic, acoustic, and phonetic representations. In the third stage, we process the imagined MEG responses from held-out subjects through the mapping pipeline to compute the corresponding listening responses that are then decoded by the listened decoder. Using rank-based analysis, we show that the imagined words are decodable significantly above chance. We shall report here the results of a proof-of-concept implementation to decode imagined speech, where all evaluations are performed on held-out subjects. We also demonstrate that performance improves with training data size, suggesting that this approach is scalable and can directly be made applicable to realistic brain-computer interface scenarios.
匹配关键词: test-time compute
---

[ACADEMIC - ARXIV]
标题: GRAPHLCP: Structure-Aware Localized Conformal Prediction on Graphs
作者: Peyman Baghershahi, Fangxin Wang, Debmalya Mandal, Sourav Medya
链接: https://arxiv.org/abs/2605.08074v1
完整摘要: Conformal prediction (CP) provides a distribution-free approach to uncertainty quantification with finite-sample guarantees. However, applying CP to graph neural networks (GNNs) remains challenging as the combinatorial nature of graphs often leads to insufficiently certain predictions and indiscriminative embeddings. Existing methods primarily rely on embedding-space proximity for localization, which can be unreliable for graphs and yield inefficient prediction sets. We propose GRAPHLCP, a proximity-based localized CP framework that explicitly incorporates graph topology and inter-node dependencies into localization and weighting. Our approach introduces a feature-aware densification step to mitigate locality bias in sparse graphs, followed by a Personalized PageRank-based kernel computation to model structural proximity. This enables topology-dependent anchor sampling and calibration weighting that captures both local and long-range dependencies. Extensive experiments on several regression and classification datasets demonstrate that GRAPHLCP guarantees marginal coverage with finite samples while efficiently attaining favorable test conditional coverage across various conditioning scenarios.
匹配关键词: test-time compute
---

[ACADEMIC - ARXIV]
标题: EmambaIR: Efficient Visual State Space Model for Event-guided Image Reconstruction
作者: Wei Yu, Yunhang Qian
链接: https://arxiv.org/abs/2605.08073v1
完整摘要: Recent event-based image reconstruction methods predominantly rely on Convolutional Neural Networks (CNNs) and Vision Transformers (ViTs) to process complementary event information. However, these architectures face fundamental limitations: CNNs often fail to capture global feature correlations, whereas ViTs incur quadratic computational complexity (e.g., $O(n^2)$), hindering their application in high-resolution scenarios. To address these bottlenecks, we introduce EmambaIR, an Efficient visual State Space Model designed for image reconstruction using spatially sparse and temporally continuous event streams. Our framework introduces two key components: the cross-modal Top-k Sparse Attention Module (TSAM) and the Gated State-Space Module (GSSM). TSAM efficiently performs pixel-level top-k sparse attention to guide cross-modal interactions, yielding rich yet sparse fusion features. Subsequently, GSSM utilizes a nonlinear gated unit to enhance the temporal representation of vanilla linear-complexity ($O(n)$) SSMs, effectively capturing global contextual dependencies without the typical computational overhead. Extensive experiments on six datasets across three diverse image reconstruction tasks - motion deblurring, deraining, and High Dynamic Range (HDR) enhancement - demonstrate that EmambaIR significantly outperforms state-of-the-art methods while offering substantial reductions in memory consumption and computational cost. The source code and data are publicly available at: https://github.com/YunhangWickert/EmambaIR
匹配关键词: test-time compute
---

[ACADEMIC - ARXIV]
标题: A Note on Non-Negative $L_1$-Approximating Polynomials
作者: Jane H. Lee, Anay Mehrotra, Manolis Zampetakis
链接: https://arxiv.org/abs/2605.08072v1
完整摘要: $L_1$-Approximating polynomials, i.e., polynomials that approximate indicator functions in $L_1$-norm under certain distributions, are widely used in computational learning theory. We study the existence of \textit{non-negative} $L_1$-approximating polynomials with respect to Gaussian distributions. This is a stronger requirement than $L_1$-approximation but weaker than sandwiching polynomials (which themselves have many applications). These non-negative approximating polynomials have recently found uses in smoothed learning from positive-only examples. In this short note, we prove that every class of sets with Gaussian surface area (GSA) at most $Γ$ under the standard Gaussian admits degree-$k$ non-negative polynomials that $\eps$-approximate its indicator functions in $L_1$-norm, for $k=\tilde{O}(Γ^2/\varepsilon^2)$. Equivalently, finite GSA implies $L_1$-approximation with the stronger pointwise guarantee that the approximating polynomial has range contained in $[0,\infty)$. Up to a constant-factor, this matches the degree of the best currently known Gaussian $L_1$-approximation degree bound without the non-negativity constraint.
匹配关键词: test-time compute
---

[ACADEMIC - ARXIV]
标题: Normalizing Trajectory Models
作者: Jiatao Gu, Tianrong Chen, Ying Shen, David Berthelot, Shuangfei Zhai, Josh Susskind
链接: https://arxiv.org/abs/2605.08078v1
完整摘要: Diffusion-based models decompose sampling into many small Gaussian denoising steps -- an assumption that breaks down when generation is compressed to a few coarse transitions. Existing few-step methods address this through distillation, consistency training, or adversarial objectives, but sacrifice the likelihood framework in the process. We introduce Normalizing Trajectory Models (NTM), which models each reverse step as an expressive conditional normalizing flow with exact likelihood training. Architecturally, NTM combines shallow invertible blocks within each step with a deep parallel predictor across the trajectory, forming an end-to-end network trainable from scratch or initializable from pretrained flow-matching models. Its exact trajectory likelihood further enables self-distillation: a lightweight denoiser trained on the model's own score produces high-quality samples in four steps. On text-to-image benchmarks, NTM matches or outperforms strong image generation baselines in just four sampling steps while uniquely retaining exact likelihood over the generative trajectory.
匹配关键词: self-consistency
---

[ACADEMIC - ARXIV]
标题: VecCISC: Improving Confidence-Informed Self-Consistency with Reasoning Trace Clustering and Candidate Answer Selection
作者: James Petullo, Sonny George, Dylan Cashman, Nianwen Xue
链接: https://arxiv.org/abs/2605.08070v1
完整摘要: A standard technique for scaling inference-time reasoning is Self-Consistency, whereby multiple candidate answers are sampled from an LLM and the most common answer is selected. More recently, it has been shown that weighted majority voting (e.g. Confidence-Informed Self Consistency (CISC)), which assigns a confidence value to each candidate answer and chooses the answer with the largest accumulated score, tends to be more accurate on a wide range of popular benchmarks. In practice, weighted majority voting necessitates calling a critic LLM on each candidate's reasoning trace to produce the answer's confidence score. This secondary series of LLM calls greatly increases the overhead and cost of weighted majority voting, despite its potential performance benefits. To reduce this expense, we propose VecCISC, a lightweight, adaptive framework that uses a measure of semantic similarity to filter reasoning traces that are semantically equivalent to others, degenerate, or hallucinated, thus decreasing the number of candidate answers that must be evaluated by the critic. To ensure adequate experimental thoroughness, we evaluate VecCISC on five challenging, widely-adopted datasets spanning the domains of mathematics, chemistry, biology, commonsense reasoning, and the humanities. Our results demonstrate that VecCISC reduces the total token usage by 47%, while maintaining or exceeding the accuracy of CISC.
匹配关键词: self-consistency
---

[ACADEMIC - ARXIV]
标题: GRASP -- Graph-Based Anomaly Detection Through Self-Supervised Classification
作者: Robin Buchta, Carsten Kleiner, Felix Heine, Gabi Dreo Rodosek
链接: https://arxiv.org/abs/2605.07812v1
完整摘要: Advanced persistent threat (APT) attacks remain difficult to detect due to their stealth, adaptability, and use of legitimate system components. Provenance-based intrusion detection systems (PIDS) offer a promising defense by capturing detailed relationships between system components and actions. However, current PIDS rely on predefined or subset-determined thresholds, which limit detection stability and the ability to detect any anomalous behavior in general. Furthermore, related work often neglects the role of process executables, which describe system activity by interacting through a process with files, network components, and other processes. We introduce GRASP, a PIDS based on masked self-supervised classification. GRASP masks the executable information of processes and learns to infer it from their two-hop provenance graph neighborhood, marking misclassified processes as anomalies. It captures behavior patterns for the learned executables without thresholding, making it robust against interference and unknown activities. Evaluations on the DARPA TC and OpTC datasets demonstrate that GRASP consistently detects anomalous behavior, including known attack-related activities, outperforming existing systems. Our PIDS identifies all documented attacks on datasets where the behavior of executables is learnable. In addition, compared to existing systems, GRASP uncovers potentially malicious anomalous behavior not labeled as an attack in the documentation.
匹配关键词: self-consistency
---

[ACADEMIC - ARXIV]
标题: Beyond Confidence: Rethinking Self-Assessments for Performance Prediction in LLMs
作者: Sree Bhattacharyya, Samarth Khanna, Leona Chen, Lucas Craig, Tharun Dilliraj, James Z. Wang
链接: https://arxiv.org/abs/2605.07806v1
完整摘要: Large Language Models (LLMs) are increasingly used in settings where reliable self-assessment is critical. Assessing model reliability has evolved from using probabilistic correctness estimates to, more recently, eliciting verbalized confidence. Confidence, however, has been shown to be an inconsistent and overoptimistic predictor of model correctness. Drawing on cognitive appraisal theory, a framework from human psychology that decomposes self-evaluation into multiple components, we propose a multidimensional perspective on model self-assessment. We elicit six appraisal-based dimensions of self-assessment, alongside confidence, and evaluate their utility for predicting model failure across 12 LLMs and 38 tasks spanning eight domains. We find that competence-related appraisal dimensions, particularly effort and ability, consistently match or outperform confidence across most settings. Effort additionally yields less overoptimistic estimates that remain stable across model sizes. In contrast, affective dimensions provide marginally predictive signals. Furthermore, the most informative dimension varies systematically with task characteristics: effort is most predictive for reasoning-intensive tasks, while ability and confidence dominate on retrieval-oriented tasks. Broadly, our findings indicate that structured multidimensional self-assessment is a promising approach to improving the reliability and safety of language model deployment across diverse real-world settings.
匹配关键词: self-consistency
---

[ACADEMIC - ARXIV]
标题: NoiseGate: Learning Per-Latent Timestep Schedules as Information Gating in World Action Models
作者: Wen Huang, Haoran Sun, Yongjian Guo, Yunxuan Ma, Haoran Li, Jing Long, Zhouying Mo, Zhong Guan, Yucheng Guo, Shuai Di, Junwu Xiong
链接: https://arxiv.org/abs/2605.07794v1
完整摘要: World Action Models (WAMs) are an emerging family of policies that tie robot action generation to future-observation modeling. In this work, we focus on the joint video--action modeling paradigm, where actions and imagined future observations are co-generated along a shared denoising or flow trajectory, so that perception, prediction, and control are coupled within one generative process. Existing WAMs typically realize this paradigm with a Mixture-of-Transformers (MoT), where video and action tokens interact through shared self-attention. This architecture can in principle assign a separate timestep $t_f$ to each predicted latent frame, yet current systems collapse this degree of freedom onto a single shared scalar $t$. Under the noise-as-masking view of Diffusion Forcing, this shared schedule imposes the unjustified prior that every predicted latent is equally reliable for action generation. We instead view the per-latent schedule as a \emph{learnable information-gating policy}: by changing a latent frame's noise level, the policy modulates the reliability of its Key/Value contribution to the action tokens. We propose \textbf{NoiseGate}, which combines independent per-latent timestep sampling during backbone training, a lightweight Gating Policy Network that emits per-latent time increments during denoising, and task-reward optimization that trains the schedule policy without hand-crafted shape priors. Built on a joint video--action MoT backbone, NoiseGate delivers consistent gains on diverse RoboTwin random-scene manipulation tasks.
匹配关键词: self-consistency
---

[ACADEMIC - ARXIV]
标题: Normalizing Trajectory Models
作者: Jiatao Gu, Tianrong Chen, Ying Shen, David Berthelot, Shuangfei Zhai, Josh Susskind
链接: https://arxiv.org/abs/2605.08078v1
完整摘要: Diffusion-based models decompose sampling into many small Gaussian denoising steps -- an assumption that breaks down when generation is compressed to a few coarse transitions. Existing few-step methods address this through distillation, consistency training, or adversarial objectives, but sacrifice the likelihood framework in the process. We introduce Normalizing Trajectory Models (NTM), which models each reverse step as an expressive conditional normalizing flow with exact likelihood training. Architecturally, NTM combines shallow invertible blocks within each step with a deep parallel predictor across the trajectory, forming an end-to-end network trainable from scratch or initializable from pretrained flow-matching models. Its exact trajectory likelihood further enables self-distillation: a lightweight denoiser trained on the model's own score produces high-quality samples in four steps. On text-to-image benchmarks, NTM matches or outperforms strong image generation baselines in just four sampling steps while uniquely retaining exact likelihood over the generative trajectory.
匹配关键词: process reward
---

[ACADEMIC - ARXIV]
标题: Zero-Shot Imagined Speech Decoding via Imagined-to-Listened MEG Mapping
作者: Maryam Maghsoudi, Shihab Shamma
链接: https://arxiv.org/abs/2605.08075v1
完整摘要: Decoding imagined speech from non-invasive brain recordings is challenging because imagined datasets are scarce and difficult to align temporally across subjects and sessions In this work, we propose a new approach to the decoding of imagined speech that leverages the richer and more reliably labeled recordings during listening to speech. We collected paired listened and imagined MEG recordings to rhythmic melodic and spoken stimuli from trained musicians. Using trained musicians helped improve temporal alignment across conditions. We then developed a three-stage decoding pipeline that revealed consistent and meaningful relationships between neural activity evoked by imagining and listening to the same stimuli. First, we trained six linear and neural models to map imagined MEG responses to listened responses. We evaluated these models against a null baseline from unseen subjects to validate that the predicted-listening responses preserve stimulus-specific information. In the second stage, we trained a contrastive word decoder exclusively on the listened MEG responses, and evaluated it using four embedding strategies including semantic, acoustic, and phonetic representations. In the third stage, we process the imagined MEG responses from held-out subjects through the mapping pipeline to compute the corresponding listening responses that are then decoded by the listened decoder. Using rank-based analysis, we show that the imagined words are decodable significantly above chance. We shall report here the results of a proof-of-concept implementation to decode imagined speech, where all evaluations are performed on held-out subjects. We also demonstrate that performance improves with training data size, suggesting that this approach is scalable and can directly be made applicable to realistic brain-computer interface scenarios.
匹配关键词: process reward
---

[ACADEMIC - ARXIV]
标题: EmambaIR: Efficient Visual State Space Model for Event-guided Image Reconstruction
作者: Wei Yu, Yunhang Qian
链接: https://arxiv.org/abs/2605.08073v1
完整摘要: Recent event-based image reconstruction methods predominantly rely on Convolutional Neural Networks (CNNs) and Vision Transformers (ViTs) to process complementary event information. However, these architectures face fundamental limitations: CNNs often fail to capture global feature correlations, whereas ViTs incur quadratic computational complexity (e.g., $O(n^2)$), hindering their application in high-resolution scenarios. To address these bottlenecks, we introduce EmambaIR, an Efficient visual State Space Model designed for image reconstruction using spatially sparse and temporally continuous event streams. Our framework introduces two key components: the cross-modal Top-k Sparse Attention Module (TSAM) and the Gated State-Space Module (GSSM). TSAM efficiently performs pixel-level top-k sparse attention to guide cross-modal interactions, yielding rich yet sparse fusion features. Subsequently, GSSM utilizes a nonlinear gated unit to enhance the temporal representation of vanilla linear-complexity ($O(n)$) SSMs, effectively capturing global contextual dependencies without the typical computational overhead. Extensive experiments on six datasets across three diverse image reconstruction tasks - motion deblurring, deraining, and High Dynamic Range (HDR) enhancement - demonstrate that EmambaIR significantly outperforms state-of-the-art methods while offering substantial reductions in memory consumption and computational cost. The source code and data are publicly available at: https://github.com/YunhangWickert/EmambaIR
匹配关键词: process reward
---

[ACADEMIC - ARXIV]
标题: Flow-OPD: On-Policy Distillation for Flow Matching Models
作者: Zhen Fang, Wenxuan Huang, Yu Zeng, Yiming Zhao, Shuang Chen, Kaituo Feng, Yunlong Lin, Lin Chen, Zehui Chen, Shaosheng Cao, Feng Zhao
链接: https://arxiv.org/abs/2605.08063v1
完整摘要: Existing Flow Matching (FM) text-to-image models suffer from two critical bottlenecks under multi-task alignment: the reward sparsity induced by scalar-valued rewards, and the gradient interference arising from jointly optimizing heterogeneous objectives, which together give rise to a 'seesaw effect' of competing metrics and pervasive reward hacking. Inspired by the success of On-Policy Distillation (OPD) in the large language model community, we propose Flow-OPD, the first unified post-training framework that integrates on-policy distillation into Flow Matching models. Flow-OPD adopts a two-stage alignment strategy: it first cultivates domain-specialized teacher models via single-reward GRPO fine-tuning, allowing each expert to reach its performance ceiling in isolation; it then establishes a robust initial policy through a Flow-based Cold-Start scheme and seamlessly consolidates heterogeneous expertise into a single student via a three-step orchestration of on-policy sampling, task-routing labeling, and dense trajectory-level supervision. We further introduce Manifold Anchor Regularization (MAR), which leverages a task-agnostic teacher to provide full-data supervision that anchors generation to a high-quality manifold, effectively mitigating the aesthetic degradation commonly observed in purely RL-driven alignment. Built upon Stable Diffusion 3.5 Medium, Flow-OPD raises the GenEval score from 63 to 92 and the OCR accuracy from 59 to 94, yielding an overall improvement of roughly 10 points over vanilla GRPO, while preserving image fidelity and human-preference alignment and exhibiting an emergent 'teacher-surpassing' effect. These results establish Flow-OPD as a scalable alignment paradigm for building generalist text-to-image models.
匹配关键词: process reward
---

[ACADEMIC - ARXIV]
标题: Rubric-Grounded RL: Structured Judge Rewards for Generalizable Reasoning
作者: Manish Bhattarai, Ismael Boureima, Nishath Rajiv Ranasinghe, Scott Pakin, Dan O'Malley
链接: https://arxiv.org/abs/2605.08061v1
完整摘要: We argue that decomposing reward into weighted, verifiable criteria and using an LLM judge to score them provides a partial-credit optimization signal: instead of a binary outcome or a single holistic score, each response is graded along multiple task-specific criteria. We formalize \emph{rubric-grounded reinforcement learning (RL)}: a framework in which the policy is optimized against a structured, multi-criterion reward produced by a frozen LLM judge that conditions on auxiliary grounding the policy never sees. We instantiate the framework by deriving rubrics from an Office of Scientific and Technical Information (OSTI)-derived corpus of roughly 100,000 scientific and technical documents and training Llama-3.1-8B-Instruct with Group Relative Policy Optimization (GRPO). With GRPO-based training, the model achieves $71.7\%$ normalized reward on held-out rubric evaluation. The GRPO-tuned policy also improves over the base model on four reasoning benchmarks not derived from the training corpus -- GSM8K, MATH, GPQA Main, and GPQA Diamond. These results provide evidence that structured, document-grounded rewards can improve held-out rubric performance and induce transferable reasoning behaviors beyond the corpus used to construct the training environment.
匹配关键词: process reward
---

[ACADEMIC - ARXIV]
标题: Normalizing Trajectory Models
作者: Jiatao Gu, Tianrong Chen, Ying Shen, David Berthelot, Shuangfei Zhai, Josh Susskind
链接: https://arxiv.org/abs/2605.08078v1
完整摘要: Diffusion-based models decompose sampling into many small Gaussian denoising steps -- an assumption that breaks down when generation is compressed to a few coarse transitions. Existing few-step methods address this through distillation, consistency training, or adversarial objectives, but sacrifice the likelihood framework in the process. We introduce Normalizing Trajectory Models (NTM), which models each reverse step as an expressive conditional normalizing flow with exact likelihood training. Architecturally, NTM combines shallow invertible blocks within each step with a deep parallel predictor across the trajectory, forming an end-to-end network trainable from scratch or initializable from pretrained flow-matching models. Its exact trajectory likelihood further enables self-distillation: a lightweight denoiser trained on the model's own score produces high-quality samples in four steps. On text-to-image benchmarks, NTM matches or outperforms strong image generation baselines in just four sampling steps while uniquely retaining exact likelihood over the generative trajectory.
匹配关键词: pretraining
---

[ACADEMIC - ARXIV]
标题: PET-Adapter: Test-Time Domain Adaptation for Full and Limited-Angle PET Image Reconstruction
作者: Rüveyda Yilmaz, Yuli Wu, Johannes Stegmaier, Volkmar Schulz
链接: https://arxiv.org/abs/2605.08030v1
完整摘要: Positron Emission Tomography (PET) image reconstruction is inherently challenged by Poisson noise and physical degradation factors, which are further exacerbated in limited-angle acquisitions. While deep learning methods demonstrate promising performance, their generalization to unseen clinical data distributions remains limited without extensive retraining. We propose PET-Adapter, a test-time domain adaptation framework for generative PET reconstruction models pretrained solely on phantom data. Our method enables adaptation to clinical datasets with varying anatomies, tracers, and scanner configurations without requiring paired ground truth. PET-Adapter introduces layer-wise low-rank anatomical conditioning during adaptation and Ordered Subset Expectation Maximization-based warm-starting that initializes the generation from physics-informed reconstructions, reducing diffusion steps from 50 to 2 without compromising quality. Experiments across multiple clinical datasets demonstrate superior 3D reconstruction performance in both full-angle and limited-angle settings, highlighting the clinical feasibility and computational efficiency of the proposed approach.
匹配关键词: pretraining
---

[ACADEMIC - ARXIV]
标题: STARFlow2: Bridging Language Models and Normalizing Flows for Unified Multimodal Generation
作者: Ying Shen, Tianrong Chen, Yuan Gao, Yizhe Zhang, Yuyang Wang, Miguel Ángel Bautista, Shuangfei Zhai, Joshua M. Susskind, Jiatao Gu
链接: https://arxiv.org/abs/2605.08029v1
完整摘要: Deep generative models have advanced rapidly across text and vision, motivating unified multimodal systems that can understand, reason over, and generate interleaved text-image sequences. Most existing approaches combine autoregressive language modeling with diffusion-based image generators, inheriting a structural mismatch between causal text generation and iterative visual denoising. We observe that autoregressive normalizing flows are autoregressive Transformers--sharing the same causal mask, KV-cache mechanism, and left-to-right structure as LLMs--making them the most natural paradigm for true unified multimodal generation. We present STARFlow2, built on the Pretzel architecture that vertically interleaves a pretrained VLM stream with a TarFlow stream via residual skip connections, both operating under the same causal mask. Combined with a deep-shallow flow design and a unified FAE latent space, STARFlow2 enables cache-friendly interleaved generation where both text and visual outputs directly enter the KV-cache without re-encoding. Experiments demonstrate strong performance across image generation and multimodal understanding benchmarks, validating autoregressive flows as a viable foundation for unified multimodal modeling.
匹配关键词: pretraining
---

[ACADEMIC - ARXIV]
标题: Rethinking Dense Optical Flow without Test-Time Scaling
作者: Praroop Chanda, Suryansh Kumar
链接: https://arxiv.org/abs/2605.08000v1
完整摘要: Recent progress in dense optical flow has been driven by increasingly complex architectures and multi-step refinement for test-time scaling. While these approaches achieve strong benchmark performance, they also require substantial computation during inference. This raises a fundamental question: Is scaling test-time computation the only way to improve dense optical flow accuracy? We argue that it is not. Instead, powerful visual semantic and geometric priors encoded in modern foundation models can reduce, if not overcome, the need for computationally expensive iterative refinement at test-time. In this paper, we present a framework that estimates dense optical flow in a single forward pass, leveraging pretrained foundation representations, while avoiding iterative refinement and additional inference-time computation, thus offering an alternative to test-time scaling. Our method extracts visual semantic features from a frozen DINO-v2 backbone and combines them with geometric cues from a monocular depth foundation model. We fuse these complementary priors into a unified representation and apply a global matching formulation to estimate dense correspondences without recurrent updates or test-time optimization. Despite avoiding iterative refinement, our approach achieves strong cross-dataset generalization across challenging benchmarks. On Sintel Final, we obtain 2.81 EPE without refinement, significantly improving over state-of-the-art (SOTA) SEA-RAFT under comparable training conditions and outperforming RAFT, GMFlow (without refinement), and recent FlowSeek in the same setting. These results suggest that strong foundation priors can substitute for test-time scaling, offering a computationally efficient alternative to refinement-heavy pipelines.
匹配关键词: pretraining
---

[ACADEMIC - ARXIV]
标题: Tool Calling is Linearly Readable and Steerable in Language Models
作者: Zekun Wu, Ze Wang, Seonglae Cho, Yufei Yang, Adriano Koshiyama, Sahan Bulathwela, Maria Perez-Ortiz
链接: https://arxiv.org/abs/2605.07990v1
完整摘要: When a tool-calling agent picks the wrong tool, the failure is invisible until execution: the email gets sent, the meeting gets missed. Probing 12 instruction-tuned models across Gemma 3, Qwen 3, Qwen 2.5, and Llama 3.1 (270M to 27B), we find the identity of the chosen tool is linearly readable and steerable inside the model. Adding the mean-difference between two tools' average internal activations switches which tool the model selects at 77-100% accuracy on name-only single-turn prompts (93-100% at 4B+), and the JSON arguments that follow autoregressively match the new tool's schema, so flipping the name is enough. The same per-tool means also flag likely errors before they happen: on Gemma 3 12B and 27B, queries where the gap between the top-1 and top-2 tool is smallest produce 14-21x more wrong calls than queries with the largest gap. The causal effect concentrates along one direction, the row of the output layer that produces the target tool's first token: a unit vector along it at matched magnitude already reaches 93-100%, while what is left over leaves the choice almost untouched. Activation patching localises this to a small set of mid- and late-layer attention heads, and a within-topic probe across 14 same-domain $τ$-bench airline tools reaches top-1 61-89% across five 4B-14B models, ruling out the reading that we are just moving the model along a topic axis. Even base models encode the right tool before they can emit it: cosine readout from the internal state recovers 69-82% on BFCL while base generation reaches only 2-10%, suggesting pretraining forms the representation and instruction tuning later wires it to the output. We measure tool identity selection and JSON schema correctness in single-turn fixed-menu settings; multi-turn agentic transfer is more fragile and is discussed in Limitations.
匹配关键词: pretraining
---

[ACADEMIC - ARXIV]
标题: LLMs Improving LLMs: Agentic Discovery for Test-Time Scaling
作者: Tong Zheng, Haolin Liu, Chengsong Huang, Huiwen Bao, Sheng Zhang, Rui Liu, Runpeng Dai, Ruibo Chen, Chenxi Liu, Tianyi Xiong, Xidong Wu, Hongming Zhang, Heng Huang
链接: https://arxiv.org/abs/2605.08083v1
完整摘要: Test-time scaling (TTS) has become an effective approach for improving large language model performance by allocating additional computation during inference. However, existing TTS strategies are largely hand-crafted: researchers manually design reasoning patterns and tune heuristics by intuition, leaving much of the computation-allocation space unexplored. We propose an environment-driven framework, AutoTTS, that changes what researchers design: from individual TTS heuristics to environments where TTS strategies can be discovered automatically. The key to AutoTTS lies in environment construction: the discovery environment must make the control space tractable and provide cheap, frequent feedback for TTS search. As a concrete instantiation, we formulate width--depth TTS as controller synthesis over pre-collected reasoning trajectories and probe signals, where controllers decide when to branch, continue, probe, prune, or stop and can be evaluated cheaply without repeated LLM calls. We further introduce beta parameterization to make the search tractable and fine-grained execution trace feedback to improve discovery efficiency by helping the agent diagnose why a TTS program fails. Experiments on mathematical reasoning benchmarks show that the discovered strategies improve the overall accuracy--cost tradeoff over strong manually designed baselines. The discovered strategies generalize to held-out benchmarks and model scales, while the entire discovery costs only $39.9 and 160 minutes. Our data, and code will be open-source at https://github.com/zhengkid/AutoTTS.
匹配关键词: foundation model
---

[ACADEMIC - ARXIV]
标题: Normalizing Trajectory Models
作者: Jiatao Gu, Tianrong Chen, Ying Shen, David Berthelot, Shuangfei Zhai, Josh Susskind
链接: https://arxiv.org/abs/2605.08078v1
完整摘要: Diffusion-based models decompose sampling into many small Gaussian denoising steps -- an assumption that breaks down when generation is compressed to a few coarse transitions. Existing few-step methods address this through distillation, consistency training, or adversarial objectives, but sacrifice the likelihood framework in the process. We introduce Normalizing Trajectory Models (NTM), which models each reverse step as an expressive conditional normalizing flow with exact likelihood training. Architecturally, NTM combines shallow invertible blocks within each step with a deep parallel predictor across the trajectory, forming an end-to-end network trainable from scratch or initializable from pretrained flow-matching models. Its exact trajectory likelihood further enables self-distillation: a lightweight denoiser trained on the model's own score produces high-quality samples in four steps. On text-to-image benchmarks, NTM matches or outperforms strong image generation baselines in just four sampling steps while uniquely retaining exact likelihood over the generative trajectory.
匹配关键词: foundation model
---

[ACADEMIC - ARXIV]
标题: Zero-Shot Imagined Speech Decoding via Imagined-to-Listened MEG Mapping
作者: Maryam Maghsoudi, Shihab Shamma
链接: https://arxiv.org/abs/2605.08075v1
完整摘要: Decoding imagined speech from non-invasive brain recordings is challenging because imagined datasets are scarce and difficult to align temporally across subjects and sessions In this work, we propose a new approach to the decoding of imagined speech that leverages the richer and more reliably labeled recordings during listening to speech. We collected paired listened and imagined MEG recordings to rhythmic melodic and spoken stimuli from trained musicians. Using trained musicians helped improve temporal alignment across conditions. We then developed a three-stage decoding pipeline that revealed consistent and meaningful relationships between neural activity evoked by imagining and listening to the same stimuli. First, we trained six linear and neural models to map imagined MEG responses to listened responses. We evaluated these models against a null baseline from unseen subjects to validate that the predicted-listening responses preserve stimulus-specific information. In the second stage, we trained a contrastive word decoder exclusively on the listened MEG responses, and evaluated it using four embedding strategies including semantic, acoustic, and phonetic representations. In the third stage, we process the imagined MEG responses from held-out subjects through the mapping pipeline to compute the corresponding listening responses that are then decoded by the listened decoder. Using rank-based analysis, we show that the imagined words are decodable significantly above chance. We shall report here the results of a proof-of-concept implementation to decode imagined speech, where all evaluations are performed on held-out subjects. We also demonstrate that performance improves with training data size, suggesting that this approach is scalable and can directly be made applicable to realistic brain-computer interface scenarios.
匹配关键词: foundation model
---

[ACADEMIC - ARXIV]
标题: GRAPHLCP: Structure-Aware Localized Conformal Prediction on Graphs
作者: Peyman Baghershahi, Fangxin Wang, Debmalya Mandal, Sourav Medya
链接: https://arxiv.org/abs/2605.08074v1
完整摘要: Conformal prediction (CP) provides a distribution-free approach to uncertainty quantification with finite-sample guarantees. However, applying CP to graph neural networks (GNNs) remains challenging as the combinatorial nature of graphs often leads to insufficiently certain predictions and indiscriminative embeddings. Existing methods primarily rely on embedding-space proximity for localization, which can be unreliable for graphs and yield inefficient prediction sets. We propose GRAPHLCP, a proximity-based localized CP framework that explicitly incorporates graph topology and inter-node dependencies into localization and weighting. Our approach introduces a feature-aware densification step to mitigate locality bias in sparse graphs, followed by a Personalized PageRank-based kernel computation to model structural proximity. This enables topology-dependent anchor sampling and calibration weighting that captures both local and long-range dependencies. Extensive experiments on several regression and classification datasets demonstrate that GRAPHLCP guarantees marginal coverage with finite samples while efficiently attaining favorable test conditional coverage across various conditioning scenarios.
匹配关键词: foundation model
---

[ACADEMIC - ARXIV]
标题: EmambaIR: Efficient Visual State Space Model for Event-guided Image Reconstruction
作者: Wei Yu, Yunhang Qian
链接: https://arxiv.org/abs/2605.08073v1
完整摘要: Recent event-based image reconstruction methods predominantly rely on Convolutional Neural Networks (CNNs) and Vision Transformers (ViTs) to process complementary event information. However, these architectures face fundamental limitations: CNNs often fail to capture global feature correlations, whereas ViTs incur quadratic computational complexity (e.g., $O(n^2)$), hindering their application in high-resolution scenarios. To address these bottlenecks, we introduce EmambaIR, an Efficient visual State Space Model designed for image reconstruction using spatially sparse and temporally continuous event streams. Our framework introduces two key components: the cross-modal Top-k Sparse Attention Module (TSAM) and the Gated State-Space Module (GSSM). TSAM efficiently performs pixel-level top-k sparse attention to guide cross-modal interactions, yielding rich yet sparse fusion features. Subsequently, GSSM utilizes a nonlinear gated unit to enhance the temporal representation of vanilla linear-complexity ($O(n)$) SSMs, effectively capturing global contextual dependencies without the typical computational overhead. Extensive experiments on six datasets across three diverse image reconstruction tasks - motion deblurring, deraining, and High Dynamic Range (HDR) enhancement - demonstrate that EmambaIR significantly outperforms state-of-the-art methods while offering substantial reductions in memory consumption and computational cost. The source code and data are publicly available at: https://github.com/YunhangWickert/EmambaIR
匹配关键词: foundation model
---

[ACADEMIC - ARXIV]
标题: 123D: Unifying Multi-Modal Autonomous Driving Data at Scale
作者: Daniel Dauner, Valentin Charraut, Bastian Berle, Tianyu Li, Long Nguyen, Jiabao Wang, Changhui Jing, Maximilian Igl, Holger Caesar, Boris Ivanovic, Yiyi Liao, Andreas Geiger, Kashyap Chitta
链接: https://arxiv.org/abs/2605.08084v1
完整摘要: The pursuit of autonomous driving has produced one of the richest sensor data collections in all of robotics. However, its scale and diversity remain largely untapped. Each dataset adopts different 2D and 3D modalities, such as cameras, lidar, ego states, annotations, traffic lights, and HD maps, with different rates and synchronization schemes. They come in fragmented formats requiring complex dependencies that cannot natively coexist in the same development environment. Further, major inconsistencies in annotation conventions prevent training or measuring generalization across multiple datasets. We present 123D, an open-source framework that unifies such multi-modal driving data through a single API. To handle synchronization, we store each modality as an independent timestamped event stream with no prescribed rate, enabling synchronous or asynchronous access across arbitrary datasets. Using 123D, we consolidate eight real-world driving datasets spanning 3,300 hours and 90,000 kilometers, together with a synthetic dataset with configurable collection scripts, and provide tools for data analysis and visualization. We conduct a systematic study comparing annotation statistics and assessing each dataset's pose and calibration accuracy. Further, we showcase two applications 123D enables: cross-dataset 3D object detection transfer and reinforcement learning for planning, and offer recommendations for future directions. Code and documentation are available at https://github.com/kesai-labs/py123d.
匹配关键词: scaling law
---

[ACADEMIC - ARXIV]
标题: LLMs Improving LLMs: Agentic Discovery for Test-Time Scaling
作者: Tong Zheng, Haolin Liu, Chengsong Huang, Huiwen Bao, Sheng Zhang, Rui Liu, Runpeng Dai, Ruibo Chen, Chenxi Liu, Tianyi Xiong, Xidong Wu, Hongming Zhang, Heng Huang
链接: https://arxiv.org/abs/2605.08083v1
完整摘要: Test-time scaling (TTS) has become an effective approach for improving large language model performance by allocating additional computation during inference. However, existing TTS strategies are largely hand-crafted: researchers manually design reasoning patterns and tune heuristics by intuition, leaving much of the computation-allocation space unexplored. We propose an environment-driven framework, AutoTTS, that changes what researchers design: from individual TTS heuristics to environments where TTS strategies can be discovered automatically. The key to AutoTTS lies in environment construction: the discovery environment must make the control space tractable and provide cheap, frequent feedback for TTS search. As a concrete instantiation, we formulate width--depth TTS as controller synthesis over pre-collected reasoning trajectories and probe signals, where controllers decide when to branch, continue, probe, prune, or stop and can be evaluated cheaply without repeated LLM calls. We further introduce beta parameterization to make the search tractable and fine-grained execution trace feedback to improve discovery efficiency by helping the agent diagnose why a TTS program fails. Experiments on mathematical reasoning benchmarks show that the discovered strategies improve the overall accuracy--cost tradeoff over strong manually designed baselines. The discovered strategies generalize to held-out benchmarks and model scales, while the entire discovery costs only $39.9 and 160 minutes. Our data, and code will be open-source at https://github.com/zhengkid/AutoTTS.
匹配关键词: scaling law
---

[ACADEMIC - ARXIV]
标题: VecCISC: Improving Confidence-Informed Self-Consistency with Reasoning Trace Clustering and Candidate Answer Selection
作者: James Petullo, Sonny George, Dylan Cashman, Nianwen Xue
链接: https://arxiv.org/abs/2605.08070v1
完整摘要: A standard technique for scaling inference-time reasoning is Self-Consistency, whereby multiple candidate answers are sampled from an LLM and the most common answer is selected. More recently, it has been shown that weighted majority voting (e.g. Confidence-Informed Self Consistency (CISC)), which assigns a confidence value to each candidate answer and chooses the answer with the largest accumulated score, tends to be more accurate on a wide range of popular benchmarks. In practice, weighted majority voting necessitates calling a critic LLM on each candidate's reasoning trace to produce the answer's confidence score. This secondary series of LLM calls greatly increases the overhead and cost of weighted majority voting, despite its potential performance benefits. To reduce this expense, we propose VecCISC, a lightweight, adaptive framework that uses a measure of semantic similarity to filter reasoning traces that are semantically equivalent to others, degenerate, or hallucinated, thus decreasing the number of candidate answers that must be evaluated by the critic. To ensure adequate experimental thoroughness, we evaluate VecCISC on five challenging, widely-adopted datasets spanning the domains of mathematics, chemistry, biology, commonsense reasoning, and the humanities. Our results demonstrate that VecCISC reduces the total token usage by 47%, while maintaining or exceeding the accuracy of CISC.
匹配关键词: scaling law
---

[ACADEMIC - ARXIV]
标题: CA-SQL: Complexity-Aware Inference Time Reasoning for Text-to-SQL via Exploration and Compute Budget Allocation
作者: James Petullo, Nianwen Xue
链接: https://arxiv.org/abs/2605.08057v1
完整摘要: While recent advancements in inference-time learning have improved LLM reasoning on Text-to-SQL tasks, current solutions still struggle to perform well on the most challenging tasks in the Bird-Bench (BIRD) benchmark. This is due to inadequate solution space exploration, which is necessary to uncover promising candidate queries that can be further refined to produce the correct output. To address this challenge, we introduce CA-SQL, a novel Text-to-SQL pipeline that utilizes the estimated difficulty of a task to dynamically scale the breadth of the exploration for generating solution candidates. In addition, we use a custom prompt seeding method, based on principles of evolutionary search, to further elicit exploratory behavior from the base LLM and a novel voting method to select the best candidate solution at the end of the search. Experiments demonstrate that our solution achieves a state-of-the-art score of 51.72% on the "challenging" tier of BIRD development set problems, using only GPT-4o-mini, out-performing other in-context learning approaches, even those that leverage larger models. Overall, our method attains a competitive 61.06% execution accuracy and 68.77% Soft F1 score on the BIRD development dataset.
匹配关键词: scaling law
---

[ACADEMIC - ARXIV]
标题: Reinforcement Learning for Exponential Utility: Algorithms and Convergence in Discounted MDPs
作者: Gugan Thoppe, L. A. Prashanth, Ankur Naskar, Sanjay Bhat
链接: https://arxiv.org/abs/2605.08053v1
完整摘要: Reinforcement learning (RL) for exponential-utility optimization in discounted Markov decision processes (MDPs) lacks principled value-based algorithms. We address this gap in the fixed risk-aversion setting. Building on the Bellman-type equation for exponential utility studied in \cite{porteus1975optimality}, we derive two Q-value-style extensions and show that the associated operators are contractions in the $L_\infty$ and sup-log/Thompson metrics, respectively. We characterize their fixed points and prove that the induced greedy stationary policy is optimal for the exponential-utility objective among stationary policies. These structural results lead to two model-free algorithms: a two-timescale Q-learning--style algorithm, for which we establish almost-sure convergence and provide finite-time convergence rates via timescale separation, and a one-timescale algorithm governed by a sublinear power-law operator. Since the latter does not admit a global contraction in standard metrics, we prove its convergence using delicate arguments based on local Lipschitzness, monotonicity, homogeneity, and Dini derivatives, and provide a scalar finite-time analysis that highlights the challenges in obtaining convergence rates in the vector case. Our work provides a foundation for value-based RL under exponential-utility objectives.
匹配关键词: scaling law
---

[ACADEMIC - ARXIV]
标题: LLMs Improving LLMs: Agentic Discovery for Test-Time Scaling
作者: Tong Zheng, Haolin Liu, Chengsong Huang, Huiwen Bao, Sheng Zhang, Rui Liu, Runpeng Dai, Ruibo Chen, Chenxi Liu, Tianyi Xiong, Xidong Wu, Hongming Zhang, Heng Huang
链接: https://arxiv.org/abs/2605.08083v1
完整摘要: Test-time scaling (TTS) has become an effective approach for improving large language model performance by allocating additional computation during inference. However, existing TTS strategies are largely hand-crafted: researchers manually design reasoning patterns and tune heuristics by intuition, leaving much of the computation-allocation space unexplored. We propose an environment-driven framework, AutoTTS, that changes what researchers design: from individual TTS heuristics to environments where TTS strategies can be discovered automatically. The key to AutoTTS lies in environment construction: the discovery environment must make the control space tractable and provide cheap, frequent feedback for TTS search. As a concrete instantiation, we formulate width--depth TTS as controller synthesis over pre-collected reasoning trajectories and probe signals, where controllers decide when to branch, continue, probe, prune, or stop and can be evaluated cheaply without repeated LLM calls. We further introduce beta parameterization to make the search tractable and fine-grained execution trace feedback to improve discovery efficiency by helping the agent diagnose why a TTS program fails. Experiments on mathematical reasoning benchmarks show that the discovered strategies improve the overall accuracy--cost tradeoff over strong manually designed baselines. The discovered strategies generalize to held-out benchmarks and model scales, while the entire discovery costs only $39.9 and 160 minutes. Our data, and code will be open-source at https://github.com/zhengkid/AutoTTS.
匹配关键词: language model
---

[ACADEMIC - ARXIV]
标题: Normalizing Trajectory Models
作者: Jiatao Gu, Tianrong Chen, Ying Shen, David Berthelot, Shuangfei Zhai, Josh Susskind
链接: https://arxiv.org/abs/2605.08078v1
完整摘要: Diffusion-based models decompose sampling into many small Gaussian denoising steps -- an assumption that breaks down when generation is compressed to a few coarse transitions. Existing few-step methods address this through distillation, consistency training, or adversarial objectives, but sacrifice the likelihood framework in the process. We introduce Normalizing Trajectory Models (NTM), which models each reverse step as an expressive conditional normalizing flow with exact likelihood training. Architecturally, NTM combines shallow invertible blocks within each step with a deep parallel predictor across the trajectory, forming an end-to-end network trainable from scratch or initializable from pretrained flow-matching models. Its exact trajectory likelihood further enables self-distillation: a lightweight denoiser trained on the model's own score produces high-quality samples in four steps. On text-to-image benchmarks, NTM matches or outperforms strong image generation baselines in just four sampling steps while uniquely retaining exact likelihood over the generative trajectory.
匹配关键词: language model
---

[ACADEMIC - ARXIV]
标题: Conformal Path Reasoning: Trustworthy Knowledge Graph Question Answering via Path-Level Calibration
作者: Shuhang Lin, Chuhao Zhou, Xiao Lin, Zihan Dong, Kuan Lu, Zhencan Peng, Jie Yin, Dimitris N. Metaxas
链接: https://arxiv.org/abs/2605.08077v1
完整摘要: Knowledge Graph Question Answering (KGQA) has shown promise for grounded and interpretable reasoning, yet existing approaches often fail to provide reliable coverage guarantees over retrieved answers. While Conformal Prediction (CP) offers a principled framework for producing prediction sets with statistical guarantees, prior methods suffer from critical limitations in both calibration validity and score discriminability, resulting in violated coverage guarantees and excessively large prediction sets. To address these pitfalls, we propose Conformal Path Reasoning (CPR), a trustworthy KGQA framework with two key innovations. First, we perform query-level conformal calibration over path-level scores, preserving the exchangeability while generating path prediction sets. Second, we introduce the Residual Conformal Value Network (RCVNet), a lightweight module trained via PUCT-guided exploration to learn discriminative path-level nonconformity scores. Experiments on benchmarks show that CPR significantly improves the Empirical Coverage Rate by 34% while reducing average prediction set size by 40% compared to conformal baselines. These results validate the efficacy of CPR in satisfying coverage guarantees with substantially more compact answer sets.
匹配关键词: language model
---

[ACADEMIC - ARXIV]
标题: Zero-Shot Imagined Speech Decoding via Imagined-to-Listened MEG Mapping
作者: Maryam Maghsoudi, Shihab Shamma
链接: https://arxiv.org/abs/2605.08075v1
完整摘要: Decoding imagined speech from non-invasive brain recordings is challenging because imagined datasets are scarce and difficult to align temporally across subjects and sessions In this work, we propose a new approach to the decoding of imagined speech that leverages the richer and more reliably labeled recordings during listening to speech. We collected paired listened and imagined MEG recordings to rhythmic melodic and spoken stimuli from trained musicians. Using trained musicians helped improve temporal alignment across conditions. We then developed a three-stage decoding pipeline that revealed consistent and meaningful relationships between neural activity evoked by imagining and listening to the same stimuli. First, we trained six linear and neural models to map imagined MEG responses to listened responses. We evaluated these models against a null baseline from unseen subjects to validate that the predicted-listening responses preserve stimulus-specific information. In the second stage, we trained a contrastive word decoder exclusively on the listened MEG responses, and evaluated it using four embedding strategies including semantic, acoustic, and phonetic representations. In the third stage, we process the imagined MEG responses from held-out subjects through the mapping pipeline to compute the corresponding listening responses that are then decoded by the listened decoder. Using rank-based analysis, we show that the imagined words are decodable significantly above chance. We shall report here the results of a proof-of-concept implementation to decode imagined speech, where all evaluations are performed on held-out subjects. We also demonstrate that performance improves with training data size, suggesting that this approach is scalable and can directly be made applicable to realistic brain-computer interface scenarios.
匹配关键词: language model
---

[ACADEMIC - ARXIV]
标题: GRAPHLCP: Structure-Aware Localized Conformal Prediction on Graphs
作者: Peyman Baghershahi, Fangxin Wang, Debmalya Mandal, Sourav Medya
链接: https://arxiv.org/abs/2605.08074v1
完整摘要: Conformal prediction (CP) provides a distribution-free approach to uncertainty quantification with finite-sample guarantees. However, applying CP to graph neural networks (GNNs) remains challenging as the combinatorial nature of graphs often leads to insufficiently certain predictions and indiscriminative embeddings. Existing methods primarily rely on embedding-space proximity for localization, which can be unreliable for graphs and yield inefficient prediction sets. We propose GRAPHLCP, a proximity-based localized CP framework that explicitly incorporates graph topology and inter-node dependencies into localization and weighting. Our approach introduces a feature-aware densification step to mitigate locality bias in sparse graphs, followed by a Personalized PageRank-based kernel computation to model structural proximity. This enables topology-dependent anchor sampling and calibration weighting that captures both local and long-range dependencies. Extensive experiments on several regression and classification datasets demonstrate that GRAPHLCP guarantees marginal coverage with finite samples while efficiently attaining favorable test conditional coverage across various conditioning scenarios.
匹配关键词: language model
---

[ACADEMIC - ARXIV]
标题: Flow-OPD: On-Policy Distillation for Flow Matching Models
作者: Zhen Fang, Wenxuan Huang, Yu Zeng, Yiming Zhao, Shuang Chen, Kaituo Feng, Yunlong Lin, Lin Chen, Zehui Chen, Shaosheng Cao, Feng Zhao
链接: https://arxiv.org/abs/2605.08063v1
完整摘要: Existing Flow Matching (FM) text-to-image models suffer from two critical bottlenecks under multi-task alignment: the reward sparsity induced by scalar-valued rewards, and the gradient interference arising from jointly optimizing heterogeneous objectives, which together give rise to a 'seesaw effect' of competing metrics and pervasive reward hacking. Inspired by the success of On-Policy Distillation (OPD) in the large language model community, we propose Flow-OPD, the first unified post-training framework that integrates on-policy distillation into Flow Matching models. Flow-OPD adopts a two-stage alignment strategy: it first cultivates domain-specialized teacher models via single-reward GRPO fine-tuning, allowing each expert to reach its performance ceiling in isolation; it then establishes a robust initial policy through a Flow-based Cold-Start scheme and seamlessly consolidates heterogeneous expertise into a single student via a three-step orchestration of on-policy sampling, task-routing labeling, and dense trajectory-level supervision. We further introduce Manifold Anchor Regularization (MAR), which leverages a task-agnostic teacher to provide full-data supervision that anchors generation to a high-quality manifold, effectively mitigating the aesthetic degradation commonly observed in purely RL-driven alignment. Built upon Stable Diffusion 3.5 Medium, Flow-OPD raises the GenEval score from 63 to 92 and the OCR accuracy from 59 to 94, yielding an overall improvement of roughly 10 points over vanilla GRPO, while preserving image fidelity and human-preference alignment and exhibiting an emergent 'teacher-surpassing' effect. These results establish Flow-OPD as a scalable alignment paradigm for building generalist text-to-image models.
匹配关键词: mixture of experts
---

[ACADEMIC - ARXIV]
标题: MPD$^2$-Router: Mask-aware Multi-expert Prior-regularized Dual-head Deferral Router in Glaucoma Screening and Diagnosis
作者: Wenxin Zhan
链接: https://arxiv.org/abs/2605.08024v1
完整摘要: Learning-to-defer (L2D) can make glaucoma screening safer by routing difficult/uncertain cases to humans, yet standard formulations overlook expert availability, heterogeneous readers behavior, workload imbalance, asymmetric diagnostic harm, case difficulty from morphology and deployment shift. We introduce MPD$^2$-Router, a mask-aware multi-expert deferral framework that recasts ophthalmic triage as constrained human--AI routing: whether to defer and to which available expert. It couples a dual-head deferral/allocation policy with mask-aware Gumbel--sigmoid gating that strictly enforces per-sample availability, and fuses uncertainty, morphology, image-quality, and OOD signals. Training uses an asymmetric cost-sensitive objective with an augmented-Lagrangian deferral budget, a group-specific distribution prior, and a rank-majorization JS regularizer that jointly prevent expert collapse without forcing uniform allocation. Across three cross-national glaucoma cohorts (REFUGE, CHAKSU, ORIGA) with a frozen REFUGE-trained backbone, MPD$^2$-Router substantially lowers clinical cost and improves MCC over AI-only at a moderate deferral rate. It is Pareto-optimal in F1--MCC--cost, robust under cross-domain shift, and yields balanced expert utilization.
匹配关键词: mixture of experts
---

[ACADEMIC - ARXIV]
标题: Towards Apples to Apples for AI Evaluations: From Real-World Use Cases to Evaluation Scenarios
作者: Yee-Yin Choong, Kristen Greene, Alice Qian, Meryem Marasli, Ziqi Yang, Sophia Chen, Laura Dabbish, Anand Rao, Hong Shen
链接: https://arxiv.org/abs/2605.07986v1
完整摘要: AI measurement science has a wide variety of methodologies and measurements for comparing AI systems, resulting in what often appear to be "apples-to-oranges" comparisons across AI evaluations. To move toward "apples-to-apples" comparisons in real-world AI evaluations, this work advocates for methodological transparency in evaluation scenarios, operational grounding, and human-centered design (HCD) principles. We propose a repeatable process for transforming high-level use cases to detailed scenarios by eliciting use cases from subject matter experts (SMEs) via a structured AI Use Case Worksheet with six key elements: use case, sector, user (direct and indirect), intended outcomes, expected impacts (positive and negative), and KPIs and metrics. We demonstrate utility of the worksheet and process in the U.S. financial services sector. This paper reports on example high-level AI use cases identified by financial services sector SMEs: cyber defense enablement, developer productivity, financial crime aggregation, suspicious activity report (SAR) filing, credit memo generation, and internal call center support. These AI use cases provided are illustrative of the process and not exhaustive. Central to our work is a three-stage expansion pipeline combining LLM prompting with human reviews to generate 107 scenarios from those use cases elicited from SMEs. This process integrates iterative human reviews at every juncture to ensure operational grounding: for scenario titles and descriptions; for core scenario elements like users, benefits and risks, and metrics; and for scenario narratives and evaluation objectives. Human checkpoints ensure scenarios remain reflective of real-world usage and human needs. We describe a validation rubric to assess scenario quality. By defining key scenario components, this work supports a more consistent and meaningful paradigm for human-centered AI evaluations.
匹配关键词: mixture of experts
---

[ACADEMIC - ARXIV]
标题: When Diffusion Model Can Ignore Dimension: An Entropy-Based Theory
作者: Ahmad Aghapour, Erhan Bayraktar
链接: https://arxiv.org/abs/2605.07969v1
完整摘要: Diffusion models perform remarkably well on high-dimensional data such as images, often using only a modest number of reverse-time steps. Despite this practical success, existing convergence theory does not fully explain why such samplers remain efficient in high dimensions. Many prior KL guarantees bound the discretization error in terms of the ambient dimension, while other improved results replace this dependence using intrinsic-dimensional or geometric structure assumptions. In this work, we develop an alternative information-theoretic perspective on diffusion sampler convergence. We prove that, for Gaussian mixture targets, the discretization error is controlled by the Shannon entropy of the latent mixture component rather than by the ambient dimension. Consequently, the leading step complexity scales linearly with latent entropy and depends only logarithmically on the second moment of the data. Our analysis also extends to discrete target distributions, where the relevant complexity is the entropy of the target rather than the dimension of the embedding space. These results suggest that diffusion sampling can remain efficient in high-dimensional spaces when the data distribution admits a compact latent representation, as is widely believed to be the case for natural images.
匹配关键词: mixture of experts
---

[ACADEMIC - ARXIV]
标题: Asymptotically Log-Optimal Bayes-Assisted Confidence Sequences for Bounded Means
作者: Valentin Kilian, Stefano Cortinovis, François Caron
链接: https://arxiv.org/abs/2605.07964v1
完整摘要: Confidence sequences based on test martingales provide time-uniform uncertainty quantification for the mean of bounded IID observations without parametric distributional assumptions. Their practical efficiency, however, depends strongly on the choice of martingale updates, and many existing constructions do not exploit prior information about plausible data-generating distributions or mean values. We propose a Bayes-assisted framework that uses a Bayesian working predictive model to adaptively construct confidence sequences.For each candidate mean and time point, the predictive distribution selects, among valid one-step martingale factors, the update maximising predictive expected log-growth; validity is therefore preserved even when the prior or working model is misspecified. We prove that if the predictive distribution is Wasserstein-consistent, the resulting procedure is asymptotically log-optimal, matching the per-sample log-growth of an oracle procedure with access to the true distribution. We instantiate the framework using robust predictives based on Dirichlet-process mixtures and Bayesian exponentially tilted empirical likelihood. Experiments on synthetic data, sequential best-arm identification for LLM evaluation, and prediction-powered inference show that informative priors can substantially reduce confidence-sequence width and sampling effort while retaining anytime-valid coverage.
匹配关键词: mixture of experts
---

[ACADEMIC - ARXIV]
标题: LLMs Improving LLMs: Agentic Discovery for Test-Time Scaling
作者: Tong Zheng, Haolin Liu, Chengsong Huang, Huiwen Bao, Sheng Zhang, Rui Liu, Runpeng Dai, Ruibo Chen, Chenxi Liu, Tianyi Xiong, Xidong Wu, Hongming Zhang, Heng Huang
链接: https://arxiv.org/abs/2605.08083v1
完整摘要: Test-time scaling (TTS) has become an effective approach for improving large language model performance by allocating additional computation during inference. However, existing TTS strategies are largely hand-crafted: researchers manually design reasoning patterns and tune heuristics by intuition, leaving much of the computation-allocation space unexplored. We propose an environment-driven framework, AutoTTS, that changes what researchers design: from individual TTS heuristics to environments where TTS strategies can be discovered automatically. The key to AutoTTS lies in environment construction: the discovery environment must make the control space tractable and provide cheap, frequent feedback for TTS search. As a concrete instantiation, we formulate width--depth TTS as controller synthesis over pre-collected reasoning trajectories and probe signals, where controllers decide when to branch, continue, probe, prune, or stop and can be evaluated cheaply without repeated LLM calls. We further introduce beta parameterization to make the search tractable and fine-grained execution trace feedback to improve discovery efficiency by helping the agent diagnose why a TTS program fails. Experiments on mathematical reasoning benchmarks show that the discovered strategies improve the overall accuracy--cost tradeoff over strong manually designed baselines. The discovered strategies generalize to held-out benchmarks and model scales, while the entire discovery costs only $39.9 and 160 minutes. Our data, and code will be open-source at https://github.com/zhengkid/AutoTTS.
匹配关键词: automated research
---

[ACADEMIC - ARXIV]
标题: Proxy3D: Efficient 3D Representations for Vision-Language Models via Semantic Clustering and Alignment
作者: Jerry Jiang, Haowen Sun, Denis Gudovskiy, Yohei Nakata, Tomoyuki Okuno, Kurt Keutzer, Wenzhao Zheng
链接: https://arxiv.org/abs/2605.08064v1
完整摘要: Spatial intelligence in vision-language models (VLMs) attracts research interest with the practical demand to reason in the 3D world.Despite promising results, most existing methods follow the conventional 2D pipeline in VLMs and use pixel-aligned representations for the vision modality. However, correspondence-based models with implicit 3D scene understanding often fail to achieve spatial consistency, and representation-based models with 3D geometric priors lack efficiency in vision sequence serialization. To address this, we propose a Proxy3D method with compact yet comprehensive 3D proxy representations for the vision modality. Given only video frames as input, we employ semantic and geometric encoders to extract scene features and then perform their semantic-aware clustering to obtain a set of proxies in the 3D space. For representation alignment, we further curate the SpaceSpan dataset and apply multi-stage training to adopt the proposed 3D proxy representations with the VLM. When using shorter sequences for vision information, our method achieves competitive or state-of-the-art performance in 3D visual question answering, visual grounding and general spatial intelligence benchmarks.
匹配关键词: automated research
---

[ACADEMIC - ARXIV]
标题: Adaptive Domain Decomposition Physics-Informed Neural Networks for Traffic State Estimation with Sparse Sensor Data
作者: Eunhan Ka, Ludovic Leclercq, Satish V. Ukkusuri
链接: https://arxiv.org/abs/2605.08028v1
完整摘要: Traffic state estimation from sparse fixed sensors is challenging because physics-informed neural networks (PINNs) tend to over-smooth the shockwaves admitted by the Lighthill-Whitham-Richards (LWR) model. This study proposes Adaptive Domain Decomposition Physics-Informed Neural Networks (ADD-PINN), a two-stage residual-guided framework for LWR-based offline speed-field reconstruction. A coarse global PINN is first trained; its spatial residual profile is then used to place subdomain boundaries and initialize child subnetworks in a decomposition-enabled mode, while a data-driven shock indicator can retain a single-domain fallback when localized evidence of transition is weak. The primary offline I-24 MOTION evaluation spans five days, five sensor configurations, and ten seeds per configuration, yielding 1,500 runs in total. Against neural and physics-informed baselines, ADD-PINN attains the lowest relative L2 error in 18 of 25 configurations and in 14 of 15 sparse-sensing cases, while training 2.4 times faster than the extended PINN (XPINN) baseline. An ablation study supports spatial-only decomposition as an effective default for fixed-sensor traffic reconstruction in the evaluated settings. Supplementary Next Generation Simulation (NGSIM) experiments serve as a negative control: the shock indicator suppresses decomposition in all 50 runs, and the default single-domain fallback ranks first across all sensor configurations. These results support residual-guided spatial decomposition as an effective PINN-family design for offline reconstruction when sparse fixed sensing coincides with localized transition regions.
匹配关键词: automated research
---

[ACADEMIC - ARXIV]
标题: TRAS: An Interactive Software for Tracing Tree Ring Cross Sections
作者: Henry Marichal, Diego Passarella, Gregory Randall
链接: https://arxiv.org/abs/2605.08025v1
完整摘要: Tree ring marking remains a key step in dendrometry and dendrochronology, but it is often performed manually, making the process time-consuming, subjective, and difficult to scale to large image datasets. We present the Tree Ring Analyzer Suite (TRAS), an open-source graphical software for automatic delineation, manual correction, and measurement of tree rings in wood cross-sectional images. TRAS integrates three complementary detection algorithms: the classical image-processing method CS-TRD and two deep-learning approaches, DeepCS-TRD and INBD. The interface allows users to refine automatic detections, remove false positives, and manually add missing rings. It also computes dendrochronological metrics such as earlywood and latewood areas, ring perimeter, equivalent ring width, and custom path-based ring-width measurements. TRAS was evaluated on 18 expertly annotated Pinus taeda L. cross-section images. DeepCS-TRD achieved the best automatic detection performance, with an F-score of 81.0% and precision of 86.4%. Automatic detection reduced the required manual correction effort to approximately 20% of ring boundaries. For one-dimensional ring-width measurements, TRAS showed excellent agreement with CooRecorder ($r > 0.99$). Common detection errors, such as jump propagation or false positives near knots, were easily corrected through the postprocessing interface. TRAS provides a flexible and reproducible solution for tree-ring analysis on Windows, macOS, and Linux. Code is available at the https://hmarichal93.github.io/tras.
匹配关键词: automated research
---

[ACADEMIC - ARXIV]
标题: AgentEscapeBench: Evaluating Out-of-Domain Tool-Grounded Reasoning in LLM Agents
作者: Zhengkang Guo, Yiyang Li, Lin Qiu, Xiaohua Wang, Jingwen Xv, Dongyu Ru, Xiaoyu Li, Xiaoqing Zheng, Xuezhi Cao, Xunliang Cai
链接: https://arxiv.org/abs/2605.07926v1
完整摘要: As LLM-based agents increasingly rely on external tools, it is important to evaluate their ability to sustain tool-grounded reasoning beyond familiar workflows and short-range interactions. We introduce AgentEscapeBench, an escape-room-style benchmark that tests whether agents can infer, execute, and revise novel tool-use procedures under explicit long-range dependency constraints. Each task defines a directed acyclic dependency graph over tools and items, requiring agents to invoke real external functions, track hidden state revealed incrementally, propagate intermediate results, and submit a deterministically verifiable final answer. AgentEscapeBench includes 270 instances across five difficulty tiers and supports fully automated evaluation. Experiments with sixteen LLM agents and human participants show that performance drops sharply as dependency depth increases: humans decline from 98.3% success at difficulty-5 to 80.0% at difficulty-25, while the best model drops from 90.0% to 60.0%. Trajectory analysis attributes model failures mainly to breakdowns in long-range state tracking, clue adherence, and intermediate-result propagation. These findings suggest that current agents can often handle local tool use but still struggle with deep contextual dependencies. We hope AgentEscapeBench can serve as a diagnostic testbed for measuring current agent capabilities and informing future training efforts toward more robust general-purpose reasoning, action, and adaptation.
匹配关键词: automated research
---

[ACADEMIC - ARXIV]
标题: LLMs Improving LLMs: Agentic Discovery for Test-Time Scaling
作者: Tong Zheng, Haolin Liu, Chengsong Huang, Huiwen Bao, Sheng Zhang, Rui Liu, Runpeng Dai, Ruibo Chen, Chenxi Liu, Tianyi Xiong, Xidong Wu, Hongming Zhang, Heng Huang
链接: https://arxiv.org/abs/2605.08083v1
完整摘要: Test-time scaling (TTS) has become an effective approach for improving large language model performance by allocating additional computation during inference. However, existing TTS strategies are largely hand-crafted: researchers manually design reasoning patterns and tune heuristics by intuition, leaving much of the computation-allocation space unexplored. We propose an environment-driven framework, AutoTTS, that changes what researchers design: from individual TTS heuristics to environments where TTS strategies can be discovered automatically. The key to AutoTTS lies in environment construction: the discovery environment must make the control space tractable and provide cheap, frequent feedback for TTS search. As a concrete instantiation, we formulate width--depth TTS as controller synthesis over pre-collected reasoning trajectories and probe signals, where controllers decide when to branch, continue, probe, prune, or stop and can be evaluated cheaply without repeated LLM calls. We further introduce beta parameterization to make the search tractable and fine-grained execution trace feedback to improve discovery efficiency by helping the agent diagnose why a TTS program fails. Experiments on mathematical reasoning benchmarks show that the discovered strategies improve the overall accuracy--cost tradeoff over strong manually designed baselines. The discovered strategies generalize to held-out benchmarks and model scales, while the entire discovery costs only $39.9 and 160 minutes. Our data, and code will be open-source at https://github.com/zhengkid/AutoTTS.
匹配关键词: scientific discovery
---

[ACADEMIC - ARXIV]
标题: Rubric-Grounded RL: Structured Judge Rewards for Generalizable Reasoning
作者: Manish Bhattarai, Ismael Boureima, Nishath Rajiv Ranasinghe, Scott Pakin, Dan O'Malley
链接: https://arxiv.org/abs/2605.08061v1
完整摘要: We argue that decomposing reward into weighted, verifiable criteria and using an LLM judge to score them provides a partial-credit optimization signal: instead of a binary outcome or a single holistic score, each response is graded along multiple task-specific criteria. We formalize \emph{rubric-grounded reinforcement learning (RL)}: a framework in which the policy is optimized against a structured, multi-criterion reward produced by a frozen LLM judge that conditions on auxiliary grounding the policy never sees. We instantiate the framework by deriving rubrics from an Office of Scientific and Technical Information (OSTI)-derived corpus of roughly 100,000 scientific and technical documents and training Llama-3.1-8B-Instruct with Group Relative Policy Optimization (GRPO). With GRPO-based training, the model achieves $71.7\%$ normalized reward on held-out rubric evaluation. The GRPO-tuned policy also improves over the base model on four reasoning benchmarks not derived from the training corpus -- GSM8K, MATH, GPQA Main, and GPQA Diamond. These results provide evidence that structured, document-grounded rewards can improve held-out rubric performance and induce transferable reasoning behaviors beyond the corpus used to construct the training environment.
匹配关键词: scientific discovery
---

[ACADEMIC - ARXIV]
标题: Reason to Play: Behavioral and Brain Alignment Between Frontier LRMs and Human Game Learners
作者: Botos Csaba, Sreejan Kumar, Austin Tudor David Andrews, Laurence Hunt, Chris Summerfield, Joshua B. Tenenbaum, Rui Ponte Costa, Marcelo G. Mattar, Momchil Tomov
链接: https://arxiv.org/abs/2605.08019v1
完整摘要: Humans rapidly learn abstract knowledge when encountering novel environments and flexibly deploy this knowledge to guide efficient and intelligent action. Can modern AI systems learn and plan in a similar way? We study this question using a dataset of complex human gameplay with concurrent fMRI recordings, in which participants learn novel video games that require rule discovery, hypothesis revision, and multi-step planning. We jointly evaluate models by their ability to play the games, match human learning behavior, and predict brain activity during the same task, comparing a suite of frontier Large Reasoning Models (LRMs) against model-free and model-based deep reinforcement learning agents and a Bayesian theory-based agent. We find that frontier LRMs most closely match human behavioral patterns during game discovery and predict brain activity an order of magnitude better than both reinforcement learning alternatives across cortical and subcortical regions, with effects robust to permutation controls. Through targeted manipulations, we further show that brain alignment reflects the model's in-context representation of the game state rather than its downstream planning or reasoning. Our results establish LRMs as compelling computational accounts of human learning and decision making in complex, naturalistic environments. Project page with interactive replays: https://botcs.github.io/reason-to-play/
匹配关键词: scientific discovery
---

[ACADEMIC - ARXIV]
标题: It Just Takes Two: Scaling Amortized Inference to Large Sets
作者: Antoine Wehenkel, Michael Kagan, Lukas Heinrich, Chris Pollard
链接: https://arxiv.org/abs/2605.07972v1
完整摘要: Neural posterior estimation has emerged as a powerful tool for amortized inference, with growing adoption across scientific and applied domains. In many of these applications, the conditioning variable is a set of observations whose elements depend not only on the target but also on unknown factors shared across the set. Optimal inference therefore requires treating the set jointly, which in turn requires training the estimator at the deployment set size -- a regime where memory and compute quickly become prohibitive. We introduce a simple, theoretically grounded strategy that decouples representation learning from posterior modeling. Our method trains a mean-pool Deep Set on sets of size at most two, producing an encoder that generalizes to arbitrary set sizes. The inference head is then finetuned on pre-aggregated embeddings, making training cost essentially independent of the deployment set size N. Across scalar, image, multi-view 3D, molecular, and high-dimensional conditional generation benchmarks with N in the thousands, our approach matches or outperforms standard baselines at a fraction of the compute.
匹配关键词: scientific discovery
---

[ACADEMIC - ARXIV]
标题: BeeVe: Unsupervised Acoustic State Discovery in Honey Bee Buzzing
作者: Hamze Hammami, Nidhal Abdulaziz
链接: https://arxiv.org/abs/2605.07903v1
完整摘要: Discovering structure in biological signals without supervision is a fundamental problem in computational intelligence, yet existing bioacoustic methods assume vocal production models or predefined semantic units, leaving non-vocal species poorly served. This work introduces BeeVe, an unsupervised framework for acoustic state discovery in collective honey bee buzzing. BeeVe uses the self-supervised Patchout Spectrogram Transformer (PaSST) as a frozen feature extractor, then trains a Vector-Quantized Variational Autoencoder (VQ-VAE) without labels on those embeddings, learning a finite discrete codebook of acoustic tokens directly from unlabelled hive audio. No labels, pretext tasks, or contrastive objectives are used at any stage. Post-hoc evaluation against known queen status reveals that the learned tokens separate queenright and queenless conditions with Jensen-Shannon Divergence values between 0.609 and 0.688, and that the queenless condition further decomposes into three internally coherent sub-states stable across experiments with different codebook sizes and random seeds. Token transition analysis confirms non-random sequential structure (p << 0.001) across all experiments. Generalisation to unseen recordings preserves both token overlap (Jaccard = 0.947) and global manifold topology. These results demonstrate that unsupervised discrete codebook learning can recover repeatable acoustic structure from a non-vocal biological signal without annotation, opening a path toward non-invasive acoustic hive health monitoring.
匹配关键词: scientific discovery
---

[ACADEMIC - ARXIV]
标题: 123D: Unifying Multi-Modal Autonomous Driving Data at Scale
作者: Daniel Dauner, Valentin Charraut, Bastian Berle, Tianyu Li, Long Nguyen, Jiabao Wang, Changhui Jing, Maximilian Igl, Holger Caesar, Boris Ivanovic, Yiyi Liao, Andreas Geiger, Kashyap Chitta
链接: https://arxiv.org/abs/2605.08084v1
完整摘要: The pursuit of autonomous driving has produced one of the richest sensor data collections in all of robotics. However, its scale and diversity remain largely untapped. Each dataset adopts different 2D and 3D modalities, such as cameras, lidar, ego states, annotations, traffic lights, and HD maps, with different rates and synchronization schemes. They come in fragmented formats requiring complex dependencies that cannot natively coexist in the same development environment. Further, major inconsistencies in annotation conventions prevent training or measuring generalization across multiple datasets. We present 123D, an open-source framework that unifies such multi-modal driving data through a single API. To handle synchronization, we store each modality as an independent timestamped event stream with no prescribed rate, enabling synchronous or asynchronous access across arbitrary datasets. Using 123D, we consolidate eight real-world driving datasets spanning 3,300 hours and 90,000 kilometers, together with a synthetic dataset with configurable collection scripts, and provide tools for data analysis and visualization. We conduct a systematic study comparing annotation statistics and assessing each dataset's pose and calibration accuracy. Further, we showcase two applications 123D enables: cross-dataset 3D object detection transfer and reinforcement learning for planning, and offer recommendations for future directions. Code and documentation are available at https://github.com/kesai-labs/py123d.
匹配关键词: hypothesis generation
---

[ACADEMIC - ARXIV]
标题: LLMs Improving LLMs: Agentic Discovery for Test-Time Scaling
作者: Tong Zheng, Haolin Liu, Chengsong Huang, Huiwen Bao, Sheng Zhang, Rui Liu, Runpeng Dai, Ruibo Chen, Chenxi Liu, Tianyi Xiong, Xidong Wu, Hongming Zhang, Heng Huang
链接: https://arxiv.org/abs/2605.08083v1
完整摘要: Test-time scaling (TTS) has become an effective approach for improving large language model performance by allocating additional computation during inference. However, existing TTS strategies are largely hand-crafted: researchers manually design reasoning patterns and tune heuristics by intuition, leaving much of the computation-allocation space unexplored. We propose an environment-driven framework, AutoTTS, that changes what researchers design: from individual TTS heuristics to environments where TTS strategies can be discovered automatically. The key to AutoTTS lies in environment construction: the discovery environment must make the control space tractable and provide cheap, frequent feedback for TTS search. As a concrete instantiation, we formulate width--depth TTS as controller synthesis over pre-collected reasoning trajectories and probe signals, where controllers decide when to branch, continue, probe, prune, or stop and can be evaluated cheaply without repeated LLM calls. We further introduce beta parameterization to make the search tractable and fine-grained execution trace feedback to improve discovery efficiency by helping the agent diagnose why a TTS program fails. Experiments on mathematical reasoning benchmarks show that the discovered strategies improve the overall accuracy--cost tradeoff over strong manually designed baselines. The discovered strategies generalize to held-out benchmarks and model scales, while the entire discovery costs only $39.9 and 160 minutes. Our data, and code will be open-source at https://github.com/zhengkid/AutoTTS.
匹配关键词: hypothesis generation
---

[ACADEMIC - ARXIV]
标题: Normalizing Trajectory Models
作者: Jiatao Gu, Tianrong Chen, Ying Shen, David Berthelot, Shuangfei Zhai, Josh Susskind
链接: https://arxiv.org/abs/2605.08078v1
完整摘要: Diffusion-based models decompose sampling into many small Gaussian denoising steps -- an assumption that breaks down when generation is compressed to a few coarse transitions. Existing few-step methods address this through distillation, consistency training, or adversarial objectives, but sacrifice the likelihood framework in the process. We introduce Normalizing Trajectory Models (NTM), which models each reverse step as an expressive conditional normalizing flow with exact likelihood training. Architecturally, NTM combines shallow invertible blocks within each step with a deep parallel predictor across the trajectory, forming an end-to-end network trainable from scratch or initializable from pretrained flow-matching models. Its exact trajectory likelihood further enables self-distillation: a lightweight denoiser trained on the model's own score produces high-quality samples in four steps. On text-to-image benchmarks, NTM matches or outperforms strong image generation baselines in just four sampling steps while uniquely retaining exact likelihood over the generative trajectory.
匹配关键词: hypothesis generation
---

[ACADEMIC - ARXIV]
标题: Conformal Path Reasoning: Trustworthy Knowledge Graph Question Answering via Path-Level Calibration
作者: Shuhang Lin, Chuhao Zhou, Xiao Lin, Zihan Dong, Kuan Lu, Zhencan Peng, Jie Yin, Dimitris N. Metaxas
链接: https://arxiv.org/abs/2605.08077v1
完整摘要: Knowledge Graph Question Answering (KGQA) has shown promise for grounded and interpretable reasoning, yet existing approaches often fail to provide reliable coverage guarantees over retrieved answers. While Conformal Prediction (CP) offers a principled framework for producing prediction sets with statistical guarantees, prior methods suffer from critical limitations in both calibration validity and score discriminability, resulting in violated coverage guarantees and excessively large prediction sets. To address these pitfalls, we propose Conformal Path Reasoning (CPR), a trustworthy KGQA framework with two key innovations. First, we perform query-level conformal calibration over path-level scores, preserving the exchangeability while generating path prediction sets. Second, we introduce the Residual Conformal Value Network (RCVNet), a lightweight module trained via PUCT-guided exploration to learn discriminative path-level nonconformity scores. Experiments on benchmarks show that CPR significantly improves the Empirical Coverage Rate by 34% while reducing average prediction set size by 40% compared to conformal baselines. These results validate the efficacy of CPR in satisfying coverage guarantees with substantially more compact answer sets.
匹配关键词: hypothesis generation
---

[ACADEMIC - ARXIV]
标题: Proxy3D: Efficient 3D Representations for Vision-Language Models via Semantic Clustering and Alignment
作者: Jerry Jiang, Haowen Sun, Denis Gudovskiy, Yohei Nakata, Tomoyuki Okuno, Kurt Keutzer, Wenzhao Zheng
链接: https://arxiv.org/abs/2605.08064v1
完整摘要: Spatial intelligence in vision-language models (VLMs) attracts research interest with the practical demand to reason in the 3D world.Despite promising results, most existing methods follow the conventional 2D pipeline in VLMs and use pixel-aligned representations for the vision modality. However, correspondence-based models with implicit 3D scene understanding often fail to achieve spatial consistency, and representation-based models with 3D geometric priors lack efficiency in vision sequence serialization. To address this, we propose a Proxy3D method with compact yet comprehensive 3D proxy representations for the vision modality. Given only video frames as input, we employ semantic and geometric encoders to extract scene features and then perform their semantic-aware clustering to obtain a set of proxies in the 3D space. For representation alignment, we further curate the SpaceSpan dataset and apply multi-stage training to adopt the proposed 3D proxy representations with the VLM. When using shorter sequences for vision information, our method achieves competitive or state-of-the-art performance in 3D visual question answering, visual grounding and general spatial intelligence benchmarks.
匹配关键词: hypothesis generation
---

[ACADEMIC - ARXIV]
标题: 123D: Unifying Multi-Modal Autonomous Driving Data at Scale
作者: Daniel Dauner, Valentin Charraut, Bastian Berle, Tianyu Li, Long Nguyen, Jiabao Wang, Changhui Jing, Maximilian Igl, Holger Caesar, Boris Ivanovic, Yiyi Liao, Andreas Geiger, Kashyap Chitta
链接: https://arxiv.org/abs/2605.08084v1
完整摘要: The pursuit of autonomous driving has produced one of the richest sensor data collections in all of robotics. However, its scale and diversity remain largely untapped. Each dataset adopts different 2D and 3D modalities, such as cameras, lidar, ego states, annotations, traffic lights, and HD maps, with different rates and synchronization schemes. They come in fragmented formats requiring complex dependencies that cannot natively coexist in the same development environment. Further, major inconsistencies in annotation conventions prevent training or measuring generalization across multiple datasets. We present 123D, an open-source framework that unifies such multi-modal driving data through a single API. To handle synchronization, we store each modality as an independent timestamped event stream with no prescribed rate, enabling synchronous or asynchronous access across arbitrary datasets. Using 123D, we consolidate eight real-world driving datasets spanning 3,300 hours and 90,000 kilometers, together with a synthetic dataset with configurable collection scripts, and provide tools for data analysis and visualization. We conduct a systematic study comparing annotation statistics and assessing each dataset's pose and calibration accuracy. Further, we showcase two applications 123D enables: cross-dataset 3D object detection transfer and reinforcement learning for planning, and offer recommendations for future directions. Code and documentation are available at https://github.com/kesai-labs/py123d.
匹配关键词: autonomous experiment
---

[ACADEMIC - ARXIV]
标题: LLMs Improving LLMs: Agentic Discovery for Test-Time Scaling
作者: Tong Zheng, Haolin Liu, Chengsong Huang, Huiwen Bao, Sheng Zhang, Rui Liu, Runpeng Dai, Ruibo Chen, Chenxi Liu, Tianyi Xiong, Xidong Wu, Hongming Zhang, Heng Huang
链接: https://arxiv.org/abs/2605.08083v1
完整摘要: Test-time scaling (TTS) has become an effective approach for improving large language model performance by allocating additional computation during inference. However, existing TTS strategies are largely hand-crafted: researchers manually design reasoning patterns and tune heuristics by intuition, leaving much of the computation-allocation space unexplored. We propose an environment-driven framework, AutoTTS, that changes what researchers design: from individual TTS heuristics to environments where TTS strategies can be discovered automatically. The key to AutoTTS lies in environment construction: the discovery environment must make the control space tractable and provide cheap, frequent feedback for TTS search. As a concrete instantiation, we formulate width--depth TTS as controller synthesis over pre-collected reasoning trajectories and probe signals, where controllers decide when to branch, continue, probe, prune, or stop and can be evaluated cheaply without repeated LLM calls. We further introduce beta parameterization to make the search tractable and fine-grained execution trace feedback to improve discovery efficiency by helping the agent diagnose why a TTS program fails. Experiments on mathematical reasoning benchmarks show that the discovered strategies improve the overall accuracy--cost tradeoff over strong manually designed baselines. The discovered strategies generalize to held-out benchmarks and model scales, while the entire discovery costs only $39.9 and 160 minutes. Our data, and code will be open-source at https://github.com/zhengkid/AutoTTS.
匹配关键词: autonomous experiment
---

[ACADEMIC - ARXIV]
标题: Conformal Path Reasoning: Trustworthy Knowledge Graph Question Answering via Path-Level Calibration
作者: Shuhang Lin, Chuhao Zhou, Xiao Lin, Zihan Dong, Kuan Lu, Zhencan Peng, Jie Yin, Dimitris N. Metaxas
链接: https://arxiv.org/abs/2605.08077v1
完整摘要: Knowledge Graph Question Answering (KGQA) has shown promise for grounded and interpretable reasoning, yet existing approaches often fail to provide reliable coverage guarantees over retrieved answers. While Conformal Prediction (CP) offers a principled framework for producing prediction sets with statistical guarantees, prior methods suffer from critical limitations in both calibration validity and score discriminability, resulting in violated coverage guarantees and excessively large prediction sets. To address these pitfalls, we propose Conformal Path Reasoning (CPR), a trustworthy KGQA framework with two key innovations. First, we perform query-level conformal calibration over path-level scores, preserving the exchangeability while generating path prediction sets. Second, we introduce the Residual Conformal Value Network (RCVNet), a lightweight module trained via PUCT-guided exploration to learn discriminative path-level nonconformity scores. Experiments on benchmarks show that CPR significantly improves the Empirical Coverage Rate by 34% while reducing average prediction set size by 40% compared to conformal baselines. These results validate the efficacy of CPR in satisfying coverage guarantees with substantially more compact answer sets.
匹配关键词: autonomous experiment
---

[ACADEMIC - ARXIV]
标题: GRAPHLCP: Structure-Aware Localized Conformal Prediction on Graphs
作者: Peyman Baghershahi, Fangxin Wang, Debmalya Mandal, Sourav Medya
链接: https://arxiv.org/abs/2605.08074v1
完整摘要: Conformal prediction (CP) provides a distribution-free approach to uncertainty quantification with finite-sample guarantees. However, applying CP to graph neural networks (GNNs) remains challenging as the combinatorial nature of graphs often leads to insufficiently certain predictions and indiscriminative embeddings. Existing methods primarily rely on embedding-space proximity for localization, which can be unreliable for graphs and yield inefficient prediction sets. We propose GRAPHLCP, a proximity-based localized CP framework that explicitly incorporates graph topology and inter-node dependencies into localization and weighting. Our approach introduces a feature-aware densification step to mitigate locality bias in sparse graphs, followed by a Personalized PageRank-based kernel computation to model structural proximity. This enables topology-dependent anchor sampling and calibration weighting that captures both local and long-range dependencies. Extensive experiments on several regression and classification datasets demonstrate that GRAPHLCP guarantees marginal coverage with finite samples while efficiently attaining favorable test conditional coverage across various conditioning scenarios.
匹配关键词: autonomous experiment
---

[ACADEMIC - ARXIV]
标题: EmambaIR: Efficient Visual State Space Model for Event-guided Image Reconstruction
作者: Wei Yu, Yunhang Qian
链接: https://arxiv.org/abs/2605.08073v1
完整摘要: Recent event-based image reconstruction methods predominantly rely on Convolutional Neural Networks (CNNs) and Vision Transformers (ViTs) to process complementary event information. However, these architectures face fundamental limitations: CNNs often fail to capture global feature correlations, whereas ViTs incur quadratic computational complexity (e.g., $O(n^2)$), hindering their application in high-resolution scenarios. To address these bottlenecks, we introduce EmambaIR, an Efficient visual State Space Model designed for image reconstruction using spatially sparse and temporally continuous event streams. Our framework introduces two key components: the cross-modal Top-k Sparse Attention Module (TSAM) and the Gated State-Space Module (GSSM). TSAM efficiently performs pixel-level top-k sparse attention to guide cross-modal interactions, yielding rich yet sparse fusion features. Subsequently, GSSM utilizes a nonlinear gated unit to enhance the temporal representation of vanilla linear-complexity ($O(n)$) SSMs, effectively capturing global contextual dependencies without the typical computational overhead. Extensive experiments on six datasets across three diverse image reconstruction tasks - motion deblurring, deraining, and High Dynamic Range (HDR) enhancement - demonstrate that EmambaIR significantly outperforms state-of-the-art methods while offering substantial reductions in memory consumption and computational cost. The source code and data are publicly available at: https://github.com/YunhangWickert/EmambaIR
匹配关键词: autonomous experiment
---

[ACADEMIC - ARXIV]
标题: 123D: Unifying Multi-Modal Autonomous Driving Data at Scale
作者: Daniel Dauner, Valentin Charraut, Bastian Berle, Tianyu Li, Long Nguyen, Jiabao Wang, Changhui Jing, Maximilian Igl, Holger Caesar, Boris Ivanovic, Yiyi Liao, Andreas Geiger, Kashyap Chitta
链接: https://arxiv.org/abs/2605.08084v1
完整摘要: The pursuit of autonomous driving has produced one of the richest sensor data collections in all of robotics. However, its scale and diversity remain largely untapped. Each dataset adopts different 2D and 3D modalities, such as cameras, lidar, ego states, annotations, traffic lights, and HD maps, with different rates and synchronization schemes. They come in fragmented formats requiring complex dependencies that cannot natively coexist in the same development environment. Further, major inconsistencies in annotation conventions prevent training or measuring generalization across multiple datasets. We present 123D, an open-source framework that unifies such multi-modal driving data through a single API. To handle synchronization, we store each modality as an independent timestamped event stream with no prescribed rate, enabling synchronous or asynchronous access across arbitrary datasets. Using 123D, we consolidate eight real-world driving datasets spanning 3,300 hours and 90,000 kilometers, together with a synthetic dataset with configurable collection scripts, and provide tools for data analysis and visualization. We conduct a systematic study comparing annotation statistics and assessing each dataset's pose and calibration accuracy. Further, we showcase two applications 123D enables: cross-dataset 3D object detection transfer and reinforcement learning for planning, and offer recommendations for future directions. Code and documentation are available at https://github.com/kesai-labs/py123d.
匹配关键词: lab automation
---

[ACADEMIC - ARXIV]
标题: TimeLesSeg: Unified Contrast-Agnostic Cross-Sectional and Longitudinal MS Lesion Segmentation via a Stochastic Generative Model
作者: Vicent Caselles-Ballester, Eloy Martínez-Heras, Giuseppe Pontillo, Zoe Mendelsohn, Elena M. Marrón, Juan Luis García Fernández, Laia Subirats, Jon Stutters, Jeremy Chataway, Frederik Barkhof, Sara Llufriu, Ferran Prados
链接: https://arxiv.org/abs/2605.07955v1
完整摘要: Multiple sclerosis (MS) expresses substantial clinical and radiological heterogeneity, which poses significant challenges for automatic lesion segmentation. The current deep learning-based SOTA is highly susceptible to changes in both distribution, e.g., changes in scanner; as well as the structure of inputs, evident in the current divide between cross-sectional and longitudinal approaches. We introduce TimeLesSeg, a unified contrast-agnostic framework designed to segment MS lesions regardless of the presence of a temporal dimension in its inputs, with a single convolutional neural network. Our approach models pathological priors through lesion masks, which are processed together with the current scan. Cross-sectional processing is enabled by exposing the model to training cases where no prior information is available, which are modeled with an empty mask, allowing it to operate seamlessly in both scenarios. To overcome the scarcity and inconsistency of longitudinal datasets, we propose a novel generative pipeline in which patterns of lesion evolution are simulated by stochastically deforming each individual lesion with morphological operations, producing realistic prior timepoints. In parallel, we achieve contrast agnosticism through Gaussian mixture model-based domain randomization, enabling the network to experience a wide spectrum of intensity profiles. Results on three publicly available and two in-house datasets show that TimeLesSeg outperforms the contrast-agnostic state of the art on single-modality inputs across overlap- and distance-based metrics. In longitudinal processing, our method outperforms SAMSEG, and captures lesion load dynamics more accurately than both the former and LST-AI. All source code related to the development of TimeLesSeg is available at https://github.com/NeuroADaS-Lab/TimeLesSeg.
匹配关键词: lab automation
---

[ACADEMIC - ARXIV]
标题: AgentEscapeBench: Evaluating Out-of-Domain Tool-Grounded Reasoning in LLM Agents
作者: Zhengkang Guo, Yiyang Li, Lin Qiu, Xiaohua Wang, Jingwen Xv, Dongyu Ru, Xiaoyu Li, Xiaoqing Zheng, Xuezhi Cao, Xunliang Cai
链接: https://arxiv.org/abs/2605.07926v1
完整摘要: As LLM-based agents increasingly rely on external tools, it is important to evaluate their ability to sustain tool-grounded reasoning beyond familiar workflows and short-range interactions. We introduce AgentEscapeBench, an escape-room-style benchmark that tests whether agents can infer, execute, and revise novel tool-use procedures under explicit long-range dependency constraints. Each task defines a directed acyclic dependency graph over tools and items, requiring agents to invoke real external functions, track hidden state revealed incrementally, propagate intermediate results, and submit a deterministically verifiable final answer. AgentEscapeBench includes 270 instances across five difficulty tiers and supports fully automated evaluation. Experiments with sixteen LLM agents and human participants show that performance drops sharply as dependency depth increases: humans decline from 98.3% success at difficulty-5 to 80.0% at difficulty-25, while the best model drops from 90.0% to 60.0%. Trajectory analysis attributes model failures mainly to breakdowns in long-range state tracking, clue adherence, and intermediate-result propagation. These findings suggest that current agents can often handle local tool use but still struggle with deep contextual dependencies. We hope AgentEscapeBench can serve as a diagnostic testbed for measuring current agent capabilities and informing future training efforts toward more robust general-purpose reasoning, action, and adaptation.
匹配关键词: lab automation
---

[ACADEMIC - ARXIV]
标题: Video Understanding Reward Modeling: A Robust Benchmark and Performant Reward Models
作者: Yuancheng Wei, Linli Yao, Lei Li, Haojie Zhang, Hao Zhou, Fandong Meng, Xu Sun
链接: https://arxiv.org/abs/2605.07872v1
完整摘要: Multimodal reward models have advanced substantially in text and image domains, yet progress in video understanding reward modeling remains severely limited by the lack of robust evaluation benchmarks and high-quality preference data. To address this, we propose a unified framework spanning benchmark design, data construction, and reward model training. We introduce Video Understanding Reward Bench (VURB), a benchmark featuring 2,100 preference pairs with long chain-of-thought reasoning traces (averaging 1,143 tokens) and majority voting evaluation across general, long, and reasoning-oriented video tasks. We further construct Video Understanding Preference Dataset (VUP-35K) via a fully automated pipeline, providing large-scale high-quality supervision for video reward training. Building on the data, we train VideoDRM and VideoGRM, a discriminative and a generative reward model, both achieving state-of-the-art performance on VURB and VideoRewardBench. Further analysis confirms that VUP-35K enhances both reward performance and model reasoning capability, while VideoDRM and VideoGRM yield significant gains under best-of-$N$ test-time scaling.
匹配关键词: lab automation
---

[ACADEMIC - ARXIV]
标题: Many-to-Many Multi-Agent Pickup and Delivery
作者: Ethan Schneider, Jingkai Chen, Tianyi Gu, Kunlei Lian, Seth Hutchinson, Sonia Chernova
链接: https://arxiv.org/abs/2605.07835v1
完整摘要: Multi-robot systems in automated warehouses must manage continuous streams of pickup-and-delivery tasks while ensuring efficiency and safety. Prior work on Multi-Agent Pickup-and-Delivery (MAPD) has largely focused on the one-to-one variant, where each task has a fixed pickup and delivery location. In contrast, real warehouses often present many-to-many MAPD scenarios, where items, tracked by stock keeping unit (SKU) identifiers, can be retrieved from or stored at multiple locations, resulting in an NP-hard four-dimensional assignment problem. To solve the many-to-many MAPD problem, we contribute our algorithm: Many-to-Many Multi-Agent Pickup and Delivery (M2M). We experiment with two variants of our algorithm: one that minimizes estimated task durations (M2M), and one which incorporates SKU distribution into the objective function (M2M-wSKU). Simulation results over 8-hour warehouse operations show that our method consistently matches or outperforms prior state of the art, with M2M completing up to 22,000 more tasks on average across different environments and warehouse inventory densities.
匹配关键词: lab automation
---

[ACADEMIC - ARXIV]
标题: 123D: Unifying Multi-Modal Autonomous Driving Data at Scale
作者: Daniel Dauner, Valentin Charraut, Bastian Berle, Tianyu Li, Long Nguyen, Jiabao Wang, Changhui Jing, Maximilian Igl, Holger Caesar, Boris Ivanovic, Yiyi Liao, Andreas Geiger, Kashyap Chitta
链接: https://arxiv.org/abs/2605.08084v1
完整摘要: The pursuit of autonomous driving has produced one of the richest sensor data collections in all of robotics. However, its scale and diversity remain largely untapped. Each dataset adopts different 2D and 3D modalities, such as cameras, lidar, ego states, annotations, traffic lights, and HD maps, with different rates and synchronization schemes. They come in fragmented formats requiring complex dependencies that cannot natively coexist in the same development environment. Further, major inconsistencies in annotation conventions prevent training or measuring generalization across multiple datasets. We present 123D, an open-source framework that unifies such multi-modal driving data through a single API. To handle synchronization, we store each modality as an independent timestamped event stream with no prescribed rate, enabling synchronous or asynchronous access across arbitrary datasets. Using 123D, we consolidate eight real-world driving datasets spanning 3,300 hours and 90,000 kilometers, together with a synthetic dataset with configurable collection scripts, and provide tools for data analysis and visualization. We conduct a systematic study comparing annotation statistics and assessing each dataset's pose and calibration accuracy. Further, we showcase two applications 123D enables: cross-dataset 3D object detection transfer and reinforcement learning for planning, and offer recommendations for future directions. Code and documentation are available at https://github.com/kesai-labs/py123d.
匹配关键词: AI for science
---

[ACADEMIC - ARXIV]
标题: LLMs Improving LLMs: Agentic Discovery for Test-Time Scaling
作者: Tong Zheng, Haolin Liu, Chengsong Huang, Huiwen Bao, Sheng Zhang, Rui Liu, Runpeng Dai, Ruibo Chen, Chenxi Liu, Tianyi Xiong, Xidong Wu, Hongming Zhang, Heng Huang
链接: https://arxiv.org/abs/2605.08083v1
完整摘要: Test-time scaling (TTS) has become an effective approach for improving large language model performance by allocating additional computation during inference. However, existing TTS strategies are largely hand-crafted: researchers manually design reasoning patterns and tune heuristics by intuition, leaving much of the computation-allocation space unexplored. We propose an environment-driven framework, AutoTTS, that changes what researchers design: from individual TTS heuristics to environments where TTS strategies can be discovered automatically. The key to AutoTTS lies in environment construction: the discovery environment must make the control space tractable and provide cheap, frequent feedback for TTS search. As a concrete instantiation, we formulate width--depth TTS as controller synthesis over pre-collected reasoning trajectories and probe signals, where controllers decide when to branch, continue, probe, prune, or stop and can be evaluated cheaply without repeated LLM calls. We further introduce beta parameterization to make the search tractable and fine-grained execution trace feedback to improve discovery efficiency by helping the agent diagnose why a TTS program fails. Experiments on mathematical reasoning benchmarks show that the discovered strategies improve the overall accuracy--cost tradeoff over strong manually designed baselines. The discovered strategies generalize to held-out benchmarks and model scales, while the entire discovery costs only $39.9 and 160 minutes. Our data, and code will be open-source at https://github.com/zhengkid/AutoTTS.
匹配关键词: AI for science
---

[ACADEMIC - ARXIV]
标题: Normalizing Trajectory Models
作者: Jiatao Gu, Tianrong Chen, Ying Shen, David Berthelot, Shuangfei Zhai, Josh Susskind
链接: https://arxiv.org/abs/2605.08078v1
完整摘要: Diffusion-based models decompose sampling into many small Gaussian denoising steps -- an assumption that breaks down when generation is compressed to a few coarse transitions. Existing few-step methods address this through distillation, consistency training, or adversarial objectives, but sacrifice the likelihood framework in the process. We introduce Normalizing Trajectory Models (NTM), which models each reverse step as an expressive conditional normalizing flow with exact likelihood training. Architecturally, NTM combines shallow invertible blocks within each step with a deep parallel predictor across the trajectory, forming an end-to-end network trainable from scratch or initializable from pretrained flow-matching models. Its exact trajectory likelihood further enables self-distillation: a lightweight denoiser trained on the model's own score produces high-quality samples in four steps. On text-to-image benchmarks, NTM matches or outperforms strong image generation baselines in just four sampling steps while uniquely retaining exact likelihood over the generative trajectory.
匹配关键词: AI for science
---

[ACADEMIC - ARXIV]
标题: Conformal Path Reasoning: Trustworthy Knowledge Graph Question Answering via Path-Level Calibration
作者: Shuhang Lin, Chuhao Zhou, Xiao Lin, Zihan Dong, Kuan Lu, Zhencan Peng, Jie Yin, Dimitris N. Metaxas
链接: https://arxiv.org/abs/2605.08077v1
完整摘要: Knowledge Graph Question Answering (KGQA) has shown promise for grounded and interpretable reasoning, yet existing approaches often fail to provide reliable coverage guarantees over retrieved answers. While Conformal Prediction (CP) offers a principled framework for producing prediction sets with statistical guarantees, prior methods suffer from critical limitations in both calibration validity and score discriminability, resulting in violated coverage guarantees and excessively large prediction sets. To address these pitfalls, we propose Conformal Path Reasoning (CPR), a trustworthy KGQA framework with two key innovations. First, we perform query-level conformal calibration over path-level scores, preserving the exchangeability while generating path prediction sets. Second, we introduce the Residual Conformal Value Network (RCVNet), a lightweight module trained via PUCT-guided exploration to learn discriminative path-level nonconformity scores. Experiments on benchmarks show that CPR significantly improves the Empirical Coverage Rate by 34% while reducing average prediction set size by 40% compared to conformal baselines. These results validate the efficacy of CPR in satisfying coverage guarantees with substantially more compact answer sets.
匹配关键词: AI for science
---

[ACADEMIC - ARXIV]
标题: Zero-Shot Imagined Speech Decoding via Imagined-to-Listened MEG Mapping
作者: Maryam Maghsoudi, Shihab Shamma
链接: https://arxiv.org/abs/2605.08075v1
完整摘要: Decoding imagined speech from non-invasive brain recordings is challenging because imagined datasets are scarce and difficult to align temporally across subjects and sessions In this work, we propose a new approach to the decoding of imagined speech that leverages the richer and more reliably labeled recordings during listening to speech. We collected paired listened and imagined MEG recordings to rhythmic melodic and spoken stimuli from trained musicians. Using trained musicians helped improve temporal alignment across conditions. We then developed a three-stage decoding pipeline that revealed consistent and meaningful relationships between neural activity evoked by imagining and listening to the same stimuli. First, we trained six linear and neural models to map imagined MEG responses to listened responses. We evaluated these models against a null baseline from unseen subjects to validate that the predicted-listening responses preserve stimulus-specific information. In the second stage, we trained a contrastive word decoder exclusively on the listened MEG responses, and evaluated it using four embedding strategies including semantic, acoustic, and phonetic representations. In the third stage, we process the imagined MEG responses from held-out subjects through the mapping pipeline to compute the corresponding listening responses that are then decoded by the listened decoder. Using rank-based analysis, we show that the imagined words are decodable significantly above chance. We shall report here the results of a proof-of-concept implementation to decode imagined speech, where all evaluations are performed on held-out subjects. We also demonstrate that performance improves with training data size, suggesting that this approach is scalable and can directly be made applicable to realistic brain-computer interface scenarios.
匹配关键词: AI for science
---

[ACADEMIC - ARXIV]
标题: bispectrum: Selective $G$-Bispectra Made Practical
作者: Johan Mathe, Adele Myers, Simon Mataigne, Nina Miolane
链接: https://arxiv.org/abs/2605.07270v1
完整摘要: Many machine learning tasks are invariant under the action of a group $G$ of transformations: signal classification can be invariant under translations, image classification under 2D rotations, and spherical-image classification under 3D rotations. The $G$-bispectrum is a principled complete invariant of a signal (retaining all all signal's information up to the group action) with proven benefits in machine learning and as a pooling layer in deep networks. However, its deployment has been hampered by high computational cost and a patchwork of group-specific implementations. We present bispectrum, an open-source, fully unit-tested PyTorch library that implements selective $G$-bispectra for seven different group actions, as differentiable modules that can be directly incorporated into machine learning pipelines and deep learning architectures. For finite groups $G$, selectivity reduces the computational cost from $O(|G|^2)$ to $O(|G|)$. For planar rotations, we leverage the disk bispectrum. For spherical 3D rotations, we introduce an augmented selective bispectrum at band-limit $L$ which reduces the cost from $O(L^3)$ to $Θ(L^2)$ coefficients. We profile the entire library (for which we implemented various compute optimizations), showing that it delivers near-exact $G$-invariance with its selective $G$-bispectra computed in sub-millisecond time on GPU (up to commonly used bandlimits). We evaluate the benefits of incorporating $G$-bispectra as pooling layers into deep learning architectures on three classical benchmark datasets --comparing against norm pooling, gated pooling, Fourier-ELU pooling, max pooling, and (non-equivariant) data-augmented convolutional baselines. Results show that $G$-bispectra consistently outperform alternatives in the low-data, moderate-capacity regime.
匹配关键词: PyTorch
---

[ACADEMIC - ARXIV]
标题: Litespark Inference on Consumer CPUs: Custom SIMD Kernels for Ternary Neural Networks
作者: Nii Osae Osae Dade, Tony Morri, Moinul Hossain Rahat, Sayandip Pal
链接: https://arxiv.org/abs/2605.06485v1
完整摘要: Large language models (LLMs) have transformed artificial intelligence, but their computational requirements remain prohibitive for most users. Standard inference demands expensive datacenter GPUs or cloud API access, leaving over one billion personal computers underutilized for AI workloads. Ternary models offer a path forward: their weights are constrained to {-1, 0, +1}, theoretically eliminating the need for floating-point multiplication. However, existing frameworks fail to exploit this structure, treating ternary models as dense floating-point networks. We address this gap with custom SIMD kernels that replace matrix multiplication with simple addition and subtraction operations, targeting the integer dot product instructions available on modern CPUs. Our implementation, Litespark-Inference, is pip-installable and integrates directly with Hugging-Face, achieving 9.2x faster time-to-first-token, 52x higher throughput, and 14x memory reduction compared to standard PyTorch inference on Apple Silicon, with similar speedups on Intel and AMD processors.
匹配关键词: PyTorch
---

[ACADEMIC - ARXIV]
标题: CuBridge: An LLM-Based Framework for Understanding and Reconstructing High-Performance Attention Kernels
作者: Xing Ma, Yangjie Zhou, Wu Sun, Zihan Liu, Jingwen Leng, Yun Lin, Shixuan Sun, Minyi Guo, Jin Song Dong
链接: https://arxiv.org/abs/2605.05023v1
完整摘要: Efficient CUDA implementations of attention mechanisms are critical to modern deep learning systems, yet supporting diverse and evolving attention variants remains challenging. Existing frameworks and compilers trade performance for flexibility, while expert-written kernels achieve high efficiency but are difficult to adapt. Recent work explores large language models (LLMs) for GPU kernel generation, but prior studies report unstable correctness and significant performance gaps for complex operators such as attention. We present CuBridge, an LLM-based framework that adapts expert-written attention kernels through a structured lift-transfer-lower workflow. CuBridge starts from expert-written CUDA attention kernels and lifts them into an executable intermediate representation that makes execution orchestration explicit while abstracting low-level CUDA syntax. Given a user-provided PyTorch specification, CuBridge generates and verifies a target IR program, then reconstructs optimized CUDA code via reference-guided lowering. Across diverse attention variants and GPU platforms, CuBridge consistently produces correct kernels and substantially outperforms general frameworks, compiler-based approaches, and prior LLM-based methods.
匹配关键词: PyTorch
---

[ACADEMIC - ARXIV]
标题: KernelBench-X: A Comprehensive Benchmark for Evaluating LLM-Generated GPU Kernels
作者: Han Wang, Jintao Zhang, Kai Jiang, Haoxu Wang, Jianfei Chen, Jun Zhu
链接: https://arxiv.org/abs/2605.04956v1
完整摘要: LLM-based Triton kernel generation has attracted significant interest, yet a fundamental empirical question remains unanswered: where does this capability break down, and why? We present KernelBench-X, a benchmark designed to answer this question through category-aware evaluation of correctness and hardware efficiency across 176 tasks in 15 categories. Our systematic comparison of five representative methods yields three main findings. First, task structure determines correctness more than method design. Category explains nearly three times more variance in semantic correctness than method (9.4% vs 3.3% explained deviance), and 72% of Fusion tasks fail across all five methods while Math tasks are solved consistently. Second, iterative refinement improves correctness, but not performance. Across GEAK iterations, compile rate rises from 52.3% to 68.8% while average speedup declines from $1.58\times$ to $1.44\times$; newly rescued kernels consistently underperform persistently correct ones ($1.16\times$ vs $1.58\times$ speedup in round~0$\to$1). Third, correctness does not imply efficiency. 46.6% of correct kernels are slower than the PyTorch eager baseline, and cross-hardware speedup variance reaches $21.4\times$. Besides, quantization remains completely unsolved (0/30 successes) despite non-trivial compilation rates, revealing systematic misunderstanding of numerical computation contracts rather than surface-level syntax errors. These findings suggest that future progress depends on handling global coordination, explicitly modeling numerical precision, and incorporating hardware efficiency into generation. The code is available at https://github.com/BonnieW05/KernelBenchX
匹配关键词: PyTorch
---

[ACADEMIC - ARXIV]
标题: 3D Human Face Reconstruction with 3DMM face model from RGB image
作者: Zhangnan Jiang, Zichen Yang
链接: https://arxiv.org/abs/2605.03996v1
完整摘要: Nowadays as convolution neural networks demonstrate its powerful problem-solving ability in the area of image processing, efforts have been made to reconstruct detailed face shapes from 2D face images or videos. However, to make the full use of CNN, a large number of labeled data is required to train the network. Coarse morphable face model has been used to synthesize labeled data. However, it is hard for coarse morphable face models to generate photo-realistic data with detail such as wrinkles. In this project, we present a pipeline that reconstructs a human face 3D model from a single RGB image. The pipeline includes face detection, landmark detection, regression of 3DMM model parameters, and soft rendering. Mentor: Zhipeng Fan (Email: zf606@nyu.edu) Code Repository: https://github.com/SeVEnMY/3d-face- reconstruction Code Reference: https://github.com/sicxu/Deep3DFaceRecon pytorch
匹配关键词: PyTorch
---

[ACADEMIC - ARXIV]
标题: MDN: Parallelizing Stepwise Momentum for Delta Linear Attention
作者: Yulong Huang, Xiang Liu, Hongxiang Huang, Xiaopeng Lin, Zunchang Liu, Xiaowen Chu, Zeke Xie, Bojun Cheng
链接: https://arxiv.org/abs/2605.05838v1
完整摘要: Linear Attention (LA) offers a promising paradigm for scaling large language models (LLMs) to long sequences by avoiding the quadratic complexity of self-attention. Recent LA models such as Mamba2 and GDN interpret linear recurrences as closed-form online stochastic gradient descent (SGD), but naive SGD updates suffer from rapid information decay and suboptimal convergence in optimization. While momentum-based optimizers provide a natural remedy, they pose challenges in simultaneously achieving training efficiency and effectiveness. To address this, we develop a chunkwise parallel algorithm for LA with a stepwise momentum rule by geometrically reordering the update coefficients. Further, from a dynamical systems perspective, we analyze the momentum-based recurrence as a second-order system that introduces complex conjugate eigenvalues. This analysis guides the design of stable gating constraints. The resulting model, Momentum DeltaNet (MDN), leverages Triton kernels to achieve comparable training throughput with competitive linear models such as Mamba2 and KDA. Extensive experiments on the 400M and 1.3B parameter models demonstrate consistent performance improvements over strong baselines, including Transformers, Mamba2 and GDN, across diverse downstream evaluation benchmarks. Code: https://github.com/HuuYuLong/MomentumDeltaNet .
匹配关键词: Triton
---

[ACADEMIC - ARXIV]
标题: KernelBench-X: A Comprehensive Benchmark for Evaluating LLM-Generated GPU Kernels
作者: Han Wang, Jintao Zhang, Kai Jiang, Haoxu Wang, Jianfei Chen, Jun Zhu
链接: https://arxiv.org/abs/2605.04956v1
完整摘要: LLM-based Triton kernel generation has attracted significant interest, yet a fundamental empirical question remains unanswered: where does this capability break down, and why? We present KernelBench-X, a benchmark designed to answer this question through category-aware evaluation of correctness and hardware efficiency across 176 tasks in 15 categories. Our systematic comparison of five representative methods yields three main findings. First, task structure determines correctness more than method design. Category explains nearly three times more variance in semantic correctness than method (9.4% vs 3.3% explained deviance), and 72% of Fusion tasks fail across all five methods while Math tasks are solved consistently. Second, iterative refinement improves correctness, but not performance. Across GEAK iterations, compile rate rises from 52.3% to 68.8% while average speedup declines from $1.58\times$ to $1.44\times$; newly rescued kernels consistently underperform persistently correct ones ($1.16\times$ vs $1.58\times$ speedup in round~0$\to$1). Third, correctness does not imply efficiency. 46.6% of correct kernels are slower than the PyTorch eager baseline, and cross-hardware speedup variance reaches $21.4\times$. Besides, quantization remains completely unsolved (0/30 successes) despite non-trivial compilation rates, revealing systematic misunderstanding of numerical computation contracts rather than surface-level syntax errors. These findings suggest that future progress depends on handling global coordination, explicitly modeling numerical precision, and incorporating hardware efficiency into generation. The code is available at https://github.com/BonnieW05/KernelBenchX
匹配关键词: Triton
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
标题: Discrete Elastic Ribbons: A Unified Discrete Differential Geometry Framework for One-Dimensional Energy Models
作者: Shivam Kumar Panda, M Khalid Jawed
链接: https://arxiv.org/abs/2605.05529v1
完整摘要: Elastic ribbons, slender structures whose length ($L$), width ($W$), and thickness ($b$) satisfy $L \gg W \gg b$, exhibit mechanical behaviors intermediate between one-dimensional rods ($L \gg W, b$) and two-dimensional plates ($L, W \gg b$). In quadratic Kirchhoff-type rod-based frameworks, such as Discrete Elastic Rods (DER), the governing equilibrium equations are independent of width, and therefore these models cannot capture width-dependent mechanical effects. Reduced centerline-based ribbon models attempt to capture width dependence via coupled bending-twisting energies. However, their relative accuracy remain unclear due to the absence of a unified simulation framework. In this work, we formulate a framework grounded in discrete differential geometry where the energy is expressed as functions of coupled bending-twisting strain measures along the centerline, rather than a linear sum of quadratic bending and twisting energies in DER. We derive analytical gradients and Hessians of the energy that enable implicit time integration. Within this unified setting, we compare five ribbon models: Kirchhoff, Sadowsky, Wunderlich, Sano, and Audoly. As a benchmark, a straight ribbon is longitudinally constrained into a pre-buckled arch and subjected to transverse displacement, inducing a supercritical pitchfork bifurcation. Predicted bifurcation thresholds are compared against shell-based finite element simulations, with the Sano model providing the closest agreement in capturing width-dependent shifts. Our high-performance JAX-based implementation achieves $\mathcal{O}(N)$ per-iteration cost and also confirms that Sano model introduces negligible per-iteration overhead relative to standard DER.
匹配关键词: JAX
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
标题: UniPrefill: Universal Long-Context Prefill Acceleration via Block-wise Dynamic Sparsification
作者: Qihang Fan, Huaibo Huang, Zhiying Wu, Bingning Wang, Ran He
链接: https://arxiv.org/abs/2605.06221v1
完整摘要: As large language models (LLMs) continue to advance rapidly, they are becoming increasingly capable while simultaneously demanding ever-longer context lengths. To improve the inference efficiency of long-context processing, several novel low-complexity hybrid architectures have recently been proposed, effectively alleviating the computational burden of long-context inference. However, existing research on long-context prefill acceleration remains predominantly focused on sparse attention mechanisms, which achieve their maximum speedup only on full-attention models. When transferred to emerging architectures--such as linear/full attention hybrids or sliding window/full attention hybrids--these prefill acceleration approaches suffer significant performance degradation. Furthermore, such methods are generally incompatible with continuous batching, making them difficult to integrate into modern inference engines such as vLLM. To this end, we propose UniPrefill, a prefill acceleration framework applicable to virtually any model architecture, which directly accelerates the model's computation at the token level. We further implement UniPrefill as a continuous batching operator and extend vLLM's scheduling strategy to natively support prefill-decode co-processing and tensor parallel for UniPrefill, enabling its seamless integration into vLLM. UniPrefill achieves up to 2.1x speedup in Time-To-First-Token (TTFT), with the acceleration becoming increasingly pronounced as the number of concurrent requests grows.
匹配关键词: vLLM
---

[ACADEMIC - ARXIV]
标题: VibeServe: Can AI Agents Build Bespoke LLM Serving Systems?
作者: Keisuke Kamahori, Shihang Li, Simon Peter, Baris Kasikci
链接: https://arxiv.org/abs/2605.06068v1
完整摘要: For years, we have built LLM serving systems like any other critical infrastructure: a single general-purpose stack, hand-tuned over many engineer-years, meant to support every model and workload. In this paper, we take the opposite bet: a multi-agent loop that automatically synthesizes bespoke serving systems for different usage scenarios. We propose VibeServe, the first agentic loop that generates entire LLM serving stacks end-to-end. VibeServe uses an outer loop to plan and track the search over system designs, and an inner loop to implement candidates, check correctness, and measure performance on the target benchmark. In the standard deployment setting, where existing stacks are highly optimized, VibeServe remains competitive with vLLM, showing that generation-time specialization need not come at the cost of performance. More interestingly, in non-standard scenarios, VibeServe outperforms existing systems by exploiting opportunities that generic systems miss in six scenarios involving non-standard model architectures, workload knowledge, and hardware-specific optimizations. Together, these results suggest a different point in the design space for infrastructure software: generation-time specialization rather than runtime generality. Code is available at https://github.com/uw-syfi/vibe-serve.
匹配关键词: vLLM
---

[ACADEMIC - ARXIV]
标题: Requests of a Feather Must Flock Together: Batch Size vs. Prefix Homogeneity in LLM Inference
作者: Saksham Rathi, Preeti, Mythili Vutukuru
链接: https://arxiv.org/abs/2605.06046v1
完整摘要: Auto-regressive token generation in large language models is memory-bound because it requires "attending to" key and value tensors (KV cache) of all previous tokens. Prior work aims to improve the efficiency of this decode process by batching multiple requests together, and maximizing batch size subject to GPU memory constraints. The key observation of our work is that with prefix-sharing workloads, smaller, prefix-homogeneous batches -- where all requests share a common prefix -- can achieve higher decode throughput than larger, heterogeneous batches, due to better spatial and temporal locality during KV cache accesses. However, prefix-aware schedulers in state-of-the-art inference engines maximize prefix reuse within a batch only to reduce KV cache memory footprint, but do not stop batch formation at smaller homogeneous batches that could have performed better. Further, we show that shared prefix detection in existing schedulers relies on radix-tree traversals, incurring substantial CPU overhead that is often comparable to GPU execution time. This paper presents Feather, a prefix-aware scheduler that uses reinforcement learning (RL) to learn the optimal tradeoff between batch size and prefix homogeneity. We also introduce Chunked Hash Tree (CHT), a lightweight data structure that enables fast prefix detection and efficient request selection for the RL scheduler, avoiding expensive tree traversals. We integrate Feather into vLLM and SGLang, and our evaluation shows that Feather achieves 2--10$\times$ higher end-to-end throughput as compared to existing schedulers, while doing no worse than the status quo when the workload does not have enough prefix sharing. Feather achieves these gains by reducing the total number of KV cache accesses, surpassing the performance of prefix-aware attention kernels that have the same goal.
匹配关键词: vLLM
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
标题: On-Orbit Real-Time Wildfire Detection Under On-Board Constraints
作者: Matthias Rötzer, Veronika Pörtge, Martin Ickerott, Jayendra Praveen Kumar Chorapalli, Dimitri Scheftelowitsch, Max Bereczky, Dmitry Rashkovetsky, Sai Manoj Appalla, Julia Gottfriedsen
链接: https://arxiv.org/abs/2605.06273v1
完整摘要: We present a deployed system for on-orbit wildfire detection aboard a nine-satellite commercial thermal infrared constellation, operating under demanding joint constraints: sub-megabyte model footprint, sub-150 ms per-batch TensorRT FP16 inference on an NVIDIA Jetson Xavier NX, and an end-to-end alert pipeline targeting under 10 minutes from satellite overpass to fire event communication. The system operates on uncalibrated mid-wave infrared (MWIR) single-band imagery at 200 m ground sampling distance, where fires frequently appear as sub-pixel or single-pixel thermal anomalies under extreme class imbalance -- challenges not addressed by the contextual thermal-thresholding pipelines (MODIS, VIIRS) that currently dominate operational fire monitoring. We present an empirical study of lightweight dense representation learning for this regime using a proprietary nine-satellite MWIR dataset. We compare dense masked autoencoding (DenseMAE) and a hybrid DenseMAE+EMA (exponential moving average) distillation variant, and evaluate representations via linear probing and full-distribution pixel-level average precision (AP) under extreme class imbalance. DenseMAE pretraining enables compact downstream models on the latency-accuracy Pareto frontier: our fastest SSL-pretrained model achieves 0.640 test AP and 0.69 event-level Fire-F1 with 65.34 ms latency per batch and a 0.52 MB engine, without pruning or compression. The best configuration reaches 0.699 AP and 0.744 Fire-F1 below 1 MB, outperforming a supervised baseline (0.650 AP) under comparable constraints.
匹配关键词: TensorRT
---

[ACADEMIC - ARXIV]
标题: AgriKD: Cross-Architecture Knowledge Distillation for Efficient Leaf Disease Classification
作者: Minh-Dung Le, Minh-Duc Hoang, Hoang-Vu Truong, Thi-Thu-Hong Phan
链接: https://arxiv.org/abs/2605.01355v2
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
标题: CuBridge: An LLM-Based Framework for Understanding and Reconstructing High-Performance Attention Kernels
作者: Xing Ma, Yangjie Zhou, Wu Sun, Zihan Liu, Jingwen Leng, Yun Lin, Shixuan Sun, Minyi Guo, Jin Song Dong
链接: https://arxiv.org/abs/2605.05023v1
完整摘要: Efficient CUDA implementations of attention mechanisms are critical to modern deep learning systems, yet supporting diverse and evolving attention variants remains challenging. Existing frameworks and compilers trade performance for flexibility, while expert-written kernels achieve high efficiency but are difficult to adapt. Recent work explores large language models (LLMs) for GPU kernel generation, but prior studies report unstable correctness and significant performance gaps for complex operators such as attention. We present CuBridge, an LLM-based framework that adapts expert-written attention kernels through a structured lift-transfer-lower workflow. CuBridge starts from expert-written CUDA attention kernels and lifts them into an executable intermediate representation that makes execution orchestration explicit while abstracting low-level CUDA syntax. Given a user-provided PyTorch specification, CuBridge generates and verifies a target IR program, then reconstructs optimized CUDA code via reference-guided lowering. Across diverse attention variants and GPU platforms, CuBridge consistently produces correct kernels and substantially outperforms general frameworks, compiler-based approaches, and prior LLM-based methods.
匹配关键词: CUDA
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
链接: https://arxiv.org/abs/2604.26799v2
完整摘要: 3D Gaussian Splatting (3DGS) achieves high-quality novel view synthesis with real-time rendering, but its storage cost remains prohibitive for practical deployment. Existing post-training compression methods still rely on many coupled hyperparameters across pruning, transformation, quantization, and entropy coding, making it difficult to control the final compressed size and fully exploit the rate-distortion trade-off. We propose MesonGS++, a size-aware post-training codec for 3D Gaussian compression. On the codec side, MesonGS++ combines joint importance-based pruning, octree geometry coding, attribute transformation, selective vector quantization for higher-degree spherical harmonics, and group-wise mixed-precision quantization with entropy coding. On the configuration side, it treats the reserve ratio and bit-width allocation as the dominant rate-distortion knobs and jointly optimizes them under a target storage budget via discrete sampling and 0--1 integer linear programming. We further propose a linear size estimator and a CUDA parallel quantization operator to accelerate the hyperparameter searching process. Extensive experiments show that MesonGS++ achieves over 34$\times$ compression while preserving rendering fidelity, outperforming state-of-the-art post-training methods and accurately meeting target size budgets. Remarkably, without any training, MesonGS++ can even surpass the PSNR of vanilla 3DGS at a 20$\times$ compression rate on the Stump scene. Our code is available at https://github.com/mmlab-sigs/mesongs_plus
匹配关键词: CUDA
---

[ACADEMIC - ARXIV]
标题: 123D: Unifying Multi-Modal Autonomous Driving Data at Scale
作者: Daniel Dauner, Valentin Charraut, Bastian Berle, Tianyu Li, Long Nguyen, Jiabao Wang, Changhui Jing, Maximilian Igl, Holger Caesar, Boris Ivanovic, Yiyi Liao, Andreas Geiger, Kashyap Chitta
链接: https://arxiv.org/abs/2605.08084v1
完整摘要: The pursuit of autonomous driving has produced one of the richest sensor data collections in all of robotics. However, its scale and diversity remain largely untapped. Each dataset adopts different 2D and 3D modalities, such as cameras, lidar, ego states, annotations, traffic lights, and HD maps, with different rates and synchronization schemes. They come in fragmented formats requiring complex dependencies that cannot natively coexist in the same development environment. Further, major inconsistencies in annotation conventions prevent training or measuring generalization across multiple datasets. We present 123D, an open-source framework that unifies such multi-modal driving data through a single API. To handle synchronization, we store each modality as an independent timestamped event stream with no prescribed rate, enabling synchronous or asynchronous access across arbitrary datasets. Using 123D, we consolidate eight real-world driving datasets spanning 3,300 hours and 90,000 kilometers, together with a synthetic dataset with configurable collection scripts, and provide tools for data analysis and visualization. We conduct a systematic study comparing annotation statistics and assessing each dataset's pose and calibration accuracy. Further, we showcase two applications 123D enables: cross-dataset 3D object detection transfer and reinforcement learning for planning, and offer recommendations for future directions. Code and documentation are available at https://github.com/kesai-labs/py123d.
匹配关键词: distributed training
---

[ACADEMIC - ARXIV]
标题: Normalizing Trajectory Models
作者: Jiatao Gu, Tianrong Chen, Ying Shen, David Berthelot, Shuangfei Zhai, Josh Susskind
链接: https://arxiv.org/abs/2605.08078v1
完整摘要: Diffusion-based models decompose sampling into many small Gaussian denoising steps -- an assumption that breaks down when generation is compressed to a few coarse transitions. Existing few-step methods address this through distillation, consistency training, or adversarial objectives, but sacrifice the likelihood framework in the process. We introduce Normalizing Trajectory Models (NTM), which models each reverse step as an expressive conditional normalizing flow with exact likelihood training. Architecturally, NTM combines shallow invertible blocks within each step with a deep parallel predictor across the trajectory, forming an end-to-end network trainable from scratch or initializable from pretrained flow-matching models. Its exact trajectory likelihood further enables self-distillation: a lightweight denoiser trained on the model's own score produces high-quality samples in four steps. On text-to-image benchmarks, NTM matches or outperforms strong image generation baselines in just four sampling steps while uniquely retaining exact likelihood over the generative trajectory.
匹配关键词: distributed training
---

[ACADEMIC - ARXIV]
标题: Conformal Path Reasoning: Trustworthy Knowledge Graph Question Answering via Path-Level Calibration
作者: Shuhang Lin, Chuhao Zhou, Xiao Lin, Zihan Dong, Kuan Lu, Zhencan Peng, Jie Yin, Dimitris N. Metaxas
链接: https://arxiv.org/abs/2605.08077v1
完整摘要: Knowledge Graph Question Answering (KGQA) has shown promise for grounded and interpretable reasoning, yet existing approaches often fail to provide reliable coverage guarantees over retrieved answers. While Conformal Prediction (CP) offers a principled framework for producing prediction sets with statistical guarantees, prior methods suffer from critical limitations in both calibration validity and score discriminability, resulting in violated coverage guarantees and excessively large prediction sets. To address these pitfalls, we propose Conformal Path Reasoning (CPR), a trustworthy KGQA framework with two key innovations. First, we perform query-level conformal calibration over path-level scores, preserving the exchangeability while generating path prediction sets. Second, we introduce the Residual Conformal Value Network (RCVNet), a lightweight module trained via PUCT-guided exploration to learn discriminative path-level nonconformity scores. Experiments on benchmarks show that CPR significantly improves the Empirical Coverage Rate by 34% while reducing average prediction set size by 40% compared to conformal baselines. These results validate the efficacy of CPR in satisfying coverage guarantees with substantially more compact answer sets.
匹配关键词: distributed training
---

[ACADEMIC - ARXIV]
标题: Zero-Shot Imagined Speech Decoding via Imagined-to-Listened MEG Mapping
作者: Maryam Maghsoudi, Shihab Shamma
链接: https://arxiv.org/abs/2605.08075v1
完整摘要: Decoding imagined speech from non-invasive brain recordings is challenging because imagined datasets are scarce and difficult to align temporally across subjects and sessions In this work, we propose a new approach to the decoding of imagined speech that leverages the richer and more reliably labeled recordings during listening to speech. We collected paired listened and imagined MEG recordings to rhythmic melodic and spoken stimuli from trained musicians. Using trained musicians helped improve temporal alignment across conditions. We then developed a three-stage decoding pipeline that revealed consistent and meaningful relationships between neural activity evoked by imagining and listening to the same stimuli. First, we trained six linear and neural models to map imagined MEG responses to listened responses. We evaluated these models against a null baseline from unseen subjects to validate that the predicted-listening responses preserve stimulus-specific information. In the second stage, we trained a contrastive word decoder exclusively on the listened MEG responses, and evaluated it using four embedding strategies including semantic, acoustic, and phonetic representations. In the third stage, we process the imagined MEG responses from held-out subjects through the mapping pipeline to compute the corresponding listening responses that are then decoded by the listened decoder. Using rank-based analysis, we show that the imagined words are decodable significantly above chance. We shall report here the results of a proof-of-concept implementation to decode imagined speech, where all evaluations are performed on held-out subjects. We also demonstrate that performance improves with training data size, suggesting that this approach is scalable and can directly be made applicable to realistic brain-computer interface scenarios.
匹配关键词: distributed training
---

[ACADEMIC - ARXIV]
标题: GRAPHLCP: Structure-Aware Localized Conformal Prediction on Graphs
作者: Peyman Baghershahi, Fangxin Wang, Debmalya Mandal, Sourav Medya
链接: https://arxiv.org/abs/2605.08074v1
完整摘要: Conformal prediction (CP) provides a distribution-free approach to uncertainty quantification with finite-sample guarantees. However, applying CP to graph neural networks (GNNs) remains challenging as the combinatorial nature of graphs often leads to insufficiently certain predictions and indiscriminative embeddings. Existing methods primarily rely on embedding-space proximity for localization, which can be unreliable for graphs and yield inefficient prediction sets. We propose GRAPHLCP, a proximity-based localized CP framework that explicitly incorporates graph topology and inter-node dependencies into localization and weighting. Our approach introduces a feature-aware densification step to mitigate locality bias in sparse graphs, followed by a Personalized PageRank-based kernel computation to model structural proximity. This enables topology-dependent anchor sampling and calibration weighting that captures both local and long-range dependencies. Extensive experiments on several regression and classification datasets demonstrate that GRAPHLCP guarantees marginal coverage with finite samples while efficiently attaining favorable test conditional coverage across various conditioning scenarios.
匹配关键词: distributed training
---

[ACADEMIC - ARXIV]
标题: Flow-OPD: On-Policy Distillation for Flow Matching Models
作者: Zhen Fang, Wenxuan Huang, Yu Zeng, Yiming Zhao, Shuang Chen, Kaituo Feng, Yunlong Lin, Lin Chen, Zehui Chen, Shaosheng Cao, Feng Zhao
链接: https://arxiv.org/abs/2605.08063v1
完整摘要: Existing Flow Matching (FM) text-to-image models suffer from two critical bottlenecks under multi-task alignment: the reward sparsity induced by scalar-valued rewards, and the gradient interference arising from jointly optimizing heterogeneous objectives, which together give rise to a 'seesaw effect' of competing metrics and pervasive reward hacking. Inspired by the success of On-Policy Distillation (OPD) in the large language model community, we propose Flow-OPD, the first unified post-training framework that integrates on-policy distillation into Flow Matching models. Flow-OPD adopts a two-stage alignment strategy: it first cultivates domain-specialized teacher models via single-reward GRPO fine-tuning, allowing each expert to reach its performance ceiling in isolation; it then establishes a robust initial policy through a Flow-based Cold-Start scheme and seamlessly consolidates heterogeneous expertise into a single student via a three-step orchestration of on-policy sampling, task-routing labeling, and dense trajectory-level supervision. We further introduce Manifold Anchor Regularization (MAR), which leverages a task-agnostic teacher to provide full-data supervision that anchors generation to a high-quality manifold, effectively mitigating the aesthetic degradation commonly observed in purely RL-driven alignment. Built upon Stable Diffusion 3.5 Medium, Flow-OPD raises the GenEval score from 63 to 92 and the OCR accuracy from 59 to 94, yielding an overall improvement of roughly 10 points over vanilla GRPO, while preserving image fidelity and human-preference alignment and exhibiting an emergent 'teacher-surpassing' effect. These results establish Flow-OPD as a scalable alignment paradigm for building generalist text-to-image models.
匹配关键词: GPU optimization
---

[ACADEMIC - ARXIV]
标题: Rubric-Grounded RL: Structured Judge Rewards for Generalizable Reasoning
作者: Manish Bhattarai, Ismael Boureima, Nishath Rajiv Ranasinghe, Scott Pakin, Dan O'Malley
链接: https://arxiv.org/abs/2605.08061v1
完整摘要: We argue that decomposing reward into weighted, verifiable criteria and using an LLM judge to score them provides a partial-credit optimization signal: instead of a binary outcome or a single holistic score, each response is graded along multiple task-specific criteria. We formalize \emph{rubric-grounded reinforcement learning (RL)}: a framework in which the policy is optimized against a structured, multi-criterion reward produced by a frozen LLM judge that conditions on auxiliary grounding the policy never sees. We instantiate the framework by deriving rubrics from an Office of Scientific and Technical Information (OSTI)-derived corpus of roughly 100,000 scientific and technical documents and training Llama-3.1-8B-Instruct with Group Relative Policy Optimization (GRPO). With GRPO-based training, the model achieves $71.7\%$ normalized reward on held-out rubric evaluation. The GRPO-tuned policy also improves over the base model on four reasoning benchmarks not derived from the training corpus -- GSM8K, MATH, GPQA Main, and GPQA Diamond. These results provide evidence that structured, document-grounded rewards can improve held-out rubric performance and induce transferable reasoning behaviors beyond the corpus used to construct the training environment.
匹配关键词: GPU optimization
---

[ACADEMIC - ARXIV]
标题: Towards Highly-Constrained Human Motion Generation with Retrieval-Guided Diffusion Noise Optimization
作者: Hanchao Liu, Fang-Lue Zhang, Shining Zhang, Tai-Jiang Mu, Shi-Min Hu
链接: https://arxiv.org/abs/2605.08054v1
完整摘要: Generating human motion that satisfies customized zero-shot goal functions, enabling applications such as controllable character animation and behavior synthesis for virtual agents, is a critical capability. While current approaches handle many unseen constraints, they fail on tasks with very challenging spatiotemporal restrictions, such as severe spatial obstacles or specified numbers of walking steps. To equip motion generators for these highly constrained tasks, we present a retrieval-guided method built on the training-free diffusion noise optimization framework. The key idea is to search within large motion datasets for guidance that can potentially satisfy difficult constraints. We introduce relational task parsing to group target constraints and identify the difficult ones to be handled by retrieved reference. A better initialization for diffusion noise is then obtained via a reward-guided mask that combines random noise with retrieved noise. By optimizing diffusion noise from this improved initialization, we successfully solve highly constrained generation tasks. By leveraging LLM for relational task parsing, the whole framework is further enabled to automatically reason for what to retrieve, improving the intelligence of moving agents under a training-free optimization scheme.
匹配关键词: GPU optimization
---

[ACADEMIC - ARXIV]
标题: Reinforcement Learning for Exponential Utility: Algorithms and Convergence in Discounted MDPs
作者: Gugan Thoppe, L. A. Prashanth, Ankur Naskar, Sanjay Bhat
链接: https://arxiv.org/abs/2605.08053v1
完整摘要: Reinforcement learning (RL) for exponential-utility optimization in discounted Markov decision processes (MDPs) lacks principled value-based algorithms. We address this gap in the fixed risk-aversion setting. Building on the Bellman-type equation for exponential utility studied in \cite{porteus1975optimality}, we derive two Q-value-style extensions and show that the associated operators are contractions in the $L_\infty$ and sup-log/Thompson metrics, respectively. We characterize their fixed points and prove that the induced greedy stationary policy is optimal for the exponential-utility objective among stationary policies. These structural results lead to two model-free algorithms: a two-timescale Q-learning--style algorithm, for which we establish almost-sure convergence and provide finite-time convergence rates via timescale separation, and a one-timescale algorithm governed by a sublinear power-law operator. Since the latter does not admit a global contraction in standard metrics, we prove its convergence using delicate arguments based on local Lipschitzness, monotonicity, homogeneity, and Dini derivatives, and provide a scalar finite-time analysis that highlights the challenges in obtaining convergence rates in the vector case. Our work provides a foundation for value-based RL under exponential-utility objectives.
匹配关键词: GPU optimization
---

[ACADEMIC - ARXIV]
标题: Accurate and Efficient Statistical Testing for Word Semantic Breadth
作者: Yo Ehara
链接: https://arxiv.org/abs/2605.08048v1
完整摘要: Measuring the breadth of a word's meaning, or its spread across contexts, has become feasible with contextualized token embeddings. A word type can be represented as a cloud of token vectors, with dispersion-based statistics serving as proxies for contextual diversity (Nagata and Tanaka-Ishii, ACL2025). These measurements are useful for deciding appropriate sense distinctions when constructing thesauri and domain-specific dictionaries. However, when comparing the breadth of two word types, naive hypothesis testing on dispersion can be misleading: differences in semantic direction can masquerade as dispersion differences, inflating Type-I error and yielding "statistically significant" outcomes even when there is no true breadth difference. This is problematic because significance testing should distinguish genuine effects from incidental fluctuations in small-difference regimes. We propose a Householder-aligned permutation test to isolate dispersion differences from directional differences. Our method applies a single Householder reflection to align the mean directions of the two word types and then performs a permutation test on the aligned token clouds, yielding calibrated, non-parametric p-values. For practicality, we introduce a GPU-oriented implementation that batches permutations and linear algebra operations. Empirically, our alignment reduced Type-I error by 32.5% while preserving sensitivity to genuine breadth differences, and achieved a 23x speedup over the CPU baseline.
匹配关键词: GPU optimization
---

[ACADEMIC - ARXIV]
标题: Rebalancing gradient to improve self-supervised co-training of depth, odometry and optical flow predictions
作者: Marwane Hariat, Antoine Manzanera, David Filliat
链接: https://arxiv.org/abs/2605.07945v1
完整摘要: We present CoopNet, an approach that improves the cooperation of co-trained networks by dynamically adapting the apportionment of gradient, to ensure equitable learning progress. It is applied to motion-aware self-supervised prediction of depth maps, by introducing a new hybrid loss, based on a distribution model of photo-metric reconstruction errors made by, on the one hand the depth + odometry paired networks, and on the other hand the optical flow network. This model essentially assumes that the pixels from moving objects (that must be discarded for training depth and odometry), correspond to those where the two reconstructions strongly disagree. We justify this model by theoretical considerations and experimental evidences. A comparative evaluation on KITTI and CityScapes datasets shows that CoopNet improves or is comparable to the state-of-the-art in depth, odometry and optical flow predictions.
匹配关键词: self-supervised
---

[ACADEMIC - ARXIV]
标题: BeeVe: Unsupervised Acoustic State Discovery in Honey Bee Buzzing
作者: Hamze Hammami, Nidhal Abdulaziz
链接: https://arxiv.org/abs/2605.07903v1
完整摘要: Discovering structure in biological signals without supervision is a fundamental problem in computational intelligence, yet existing bioacoustic methods assume vocal production models or predefined semantic units, leaving non-vocal species poorly served. This work introduces BeeVe, an unsupervised framework for acoustic state discovery in collective honey bee buzzing. BeeVe uses the self-supervised Patchout Spectrogram Transformer (PaSST) as a frozen feature extractor, then trains a Vector-Quantized Variational Autoencoder (VQ-VAE) without labels on those embeddings, learning a finite discrete codebook of acoustic tokens directly from unlabelled hive audio. No labels, pretext tasks, or contrastive objectives are used at any stage. Post-hoc evaluation against known queen status reveals that the learned tokens separate queenright and queenless conditions with Jensen-Shannon Divergence values between 0.609 and 0.688, and that the queenless condition further decomposes into three internally coherent sub-states stable across experiments with different codebook sizes and random seeds. Token transition analysis confirms non-random sequential structure (p << 0.001) across all experiments. Generalisation to unseen recordings preserves both token overlap (Jaccard = 0.947) and global manifold topology. These results demonstrate that unsupervised discrete codebook learning can recover repeatable acoustic structure from a non-vocal biological signal without annotation, opening a path toward non-invasive acoustic hive health monitoring.
匹配关键词: self-supervised
---

[ACADEMIC - ARXIV]
标题: GRASP -- Graph-Based Anomaly Detection Through Self-Supervised Classification
作者: Robin Buchta, Carsten Kleiner, Felix Heine, Gabi Dreo Rodosek
链接: https://arxiv.org/abs/2605.07812v1
完整摘要: Advanced persistent threat (APT) attacks remain difficult to detect due to their stealth, adaptability, and use of legitimate system components. Provenance-based intrusion detection systems (PIDS) offer a promising defense by capturing detailed relationships between system components and actions. However, current PIDS rely on predefined or subset-determined thresholds, which limit detection stability and the ability to detect any anomalous behavior in general. Furthermore, related work often neglects the role of process executables, which describe system activity by interacting through a process with files, network components, and other processes. We introduce GRASP, a PIDS based on masked self-supervised classification. GRASP masks the executable information of processes and learns to infer it from their two-hop provenance graph neighborhood, marking misclassified processes as anomalies. It captures behavior patterns for the learned executables without thresholding, making it robust against interference and unknown activities. Evaluations on the DARPA TC and OpTC datasets demonstrate that GRASP consistently detects anomalous behavior, including known attack-related activities, outperforming existing systems. Our PIDS identifies all documented attacks on datasets where the behavior of executables is learnable. In addition, compared to existing systems, GRASP uncovers potentially malicious anomalous behavior not labeled as an attack in the documentation.
匹配关键词: self-supervised
---

[ACADEMIC - ARXIV]
标题: When Losses Align: Gradient-Based Composite Loss Weighting for Efficient Pretraining
作者: Ivan Karpukhin, Andrey Savchenko
链接: https://arxiv.org/abs/2605.07756v1
完整摘要: Modern deep models are often pretrained on large-scale data with missing labels using composite objectives, where the relative weights of multiple loss terms act as hyperparameters. Tuning these weights with random search or Bayesian optimization is computationally expensive, as it requires many independent training runs. To address this, we propose a gradient-based bilevel method that learns pretraining loss weights online by aligning the composite pretraining gradient with a downstream objective. By exploiting the structure of the loss, the method avoids the multiple backward passes typically required by truncated backpropagation through the full model, reducing the overhead of hyperparameter tuning to approximately 30% above a single training run. We evaluate the approach on event-sequence modeling and self-supervised computer vision, where it matches or improves upon carefully tuned baselines while substantially reducing the cost of hyperparameter tuning compared to random or Bayesian search.
匹配关键词: self-supervised
---

[ACADEMIC - ARXIV]
标题: Aquatic Neuromorphic Optical Flow
作者: Pei Zhang, Yunkai Liang, Kaiqiang Wang
链接: https://arxiv.org/abs/2605.07653v1
完整摘要: Underwater environments impose severe constraints on conventional imaging systems and demand solutions that balance high-quality sensing with strict resource efficiency. While emerging event cameras offer a promising alternative, their potential in aquatic scenarios remains largely unexplored. Through the lens of neuromorphic vision, this work pioneers the investigation of motion fields that serve as key media for agile underwater perception. Built upon spiking neural networks, we introduce a self-supervised framework to estimate per-pixel optical flow from asynchronous event streams, elegantly bypassing the long-standing bottleneck of underwater data scarcity. Extensive evaluations demonstrate that our method achieves competitive visual and quantitative results against leading techniques while operating with superior computational efficiency. By bridging neuromorphic sensing and aquatic intelligence, this work opens new frontiers for lightweight, real-time, and low-cost perception on resource-constrained underwater edge platforms.
匹配关键词: self-supervised
---

[ACADEMIC - ARXIV]
标题: 123D: Unifying Multi-Modal Autonomous Driving Data at Scale
作者: Daniel Dauner, Valentin Charraut, Bastian Berle, Tianyu Li, Long Nguyen, Jiabao Wang, Changhui Jing, Maximilian Igl, Holger Caesar, Boris Ivanovic, Yiyi Liao, Andreas Geiger, Kashyap Chitta
链接: https://arxiv.org/abs/2605.08084v1
完整摘要: The pursuit of autonomous driving has produced one of the richest sensor data collections in all of robotics. However, its scale and diversity remain largely untapped. Each dataset adopts different 2D and 3D modalities, such as cameras, lidar, ego states, annotations, traffic lights, and HD maps, with different rates and synchronization schemes. They come in fragmented formats requiring complex dependencies that cannot natively coexist in the same development environment. Further, major inconsistencies in annotation conventions prevent training or measuring generalization across multiple datasets. We present 123D, an open-source framework that unifies such multi-modal driving data through a single API. To handle synchronization, we store each modality as an independent timestamped event stream with no prescribed rate, enabling synchronous or asynchronous access across arbitrary datasets. Using 123D, we consolidate eight real-world driving datasets spanning 3,300 hours and 90,000 kilometers, together with a synthetic dataset with configurable collection scripts, and provide tools for data analysis and visualization. We conduct a systematic study comparing annotation statistics and assessing each dataset's pose and calibration accuracy. Further, we showcase two applications 123D enables: cross-dataset 3D object detection transfer and reinforcement learning for planning, and offer recommendations for future directions. Code and documentation are available at https://github.com/kesai-labs/py123d.
匹配关键词: contrastive learning
---

[ACADEMIC - ARXIV]
标题: Normalizing Trajectory Models
作者: Jiatao Gu, Tianrong Chen, Ying Shen, David Berthelot, Shuangfei Zhai, Josh Susskind
链接: https://arxiv.org/abs/2605.08078v1
完整摘要: Diffusion-based models decompose sampling into many small Gaussian denoising steps -- an assumption that breaks down when generation is compressed to a few coarse transitions. Existing few-step methods address this through distillation, consistency training, or adversarial objectives, but sacrifice the likelihood framework in the process. We introduce Normalizing Trajectory Models (NTM), which models each reverse step as an expressive conditional normalizing flow with exact likelihood training. Architecturally, NTM combines shallow invertible blocks within each step with a deep parallel predictor across the trajectory, forming an end-to-end network trainable from scratch or initializable from pretrained flow-matching models. Its exact trajectory likelihood further enables self-distillation: a lightweight denoiser trained on the model's own score produces high-quality samples in four steps. On text-to-image benchmarks, NTM matches or outperforms strong image generation baselines in just four sampling steps while uniquely retaining exact likelihood over the generative trajectory.
匹配关键词: contrastive learning
---

[ACADEMIC - ARXIV]
标题: Conformal Path Reasoning: Trustworthy Knowledge Graph Question Answering via Path-Level Calibration
作者: Shuhang Lin, Chuhao Zhou, Xiao Lin, Zihan Dong, Kuan Lu, Zhencan Peng, Jie Yin, Dimitris N. Metaxas
链接: https://arxiv.org/abs/2605.08077v1
完整摘要: Knowledge Graph Question Answering (KGQA) has shown promise for grounded and interpretable reasoning, yet existing approaches often fail to provide reliable coverage guarantees over retrieved answers. While Conformal Prediction (CP) offers a principled framework for producing prediction sets with statistical guarantees, prior methods suffer from critical limitations in both calibration validity and score discriminability, resulting in violated coverage guarantees and excessively large prediction sets. To address these pitfalls, we propose Conformal Path Reasoning (CPR), a trustworthy KGQA framework with two key innovations. First, we perform query-level conformal calibration over path-level scores, preserving the exchangeability while generating path prediction sets. Second, we introduce the Residual Conformal Value Network (RCVNet), a lightweight module trained via PUCT-guided exploration to learn discriminative path-level nonconformity scores. Experiments on benchmarks show that CPR significantly improves the Empirical Coverage Rate by 34% while reducing average prediction set size by 40% compared to conformal baselines. These results validate the efficacy of CPR in satisfying coverage guarantees with substantially more compact answer sets.
匹配关键词: contrastive learning
---

[ACADEMIC - ARXIV]
标题: Zero-Shot Imagined Speech Decoding via Imagined-to-Listened MEG Mapping
作者: Maryam Maghsoudi, Shihab Shamma
链接: https://arxiv.org/abs/2605.08075v1
完整摘要: Decoding imagined speech from non-invasive brain recordings is challenging because imagined datasets are scarce and difficult to align temporally across subjects and sessions In this work, we propose a new approach to the decoding of imagined speech that leverages the richer and more reliably labeled recordings during listening to speech. We collected paired listened and imagined MEG recordings to rhythmic melodic and spoken stimuli from trained musicians. Using trained musicians helped improve temporal alignment across conditions. We then developed a three-stage decoding pipeline that revealed consistent and meaningful relationships between neural activity evoked by imagining and listening to the same stimuli. First, we trained six linear and neural models to map imagined MEG responses to listened responses. We evaluated these models against a null baseline from unseen subjects to validate that the predicted-listening responses preserve stimulus-specific information. In the second stage, we trained a contrastive word decoder exclusively on the listened MEG responses, and evaluated it using four embedding strategies including semantic, acoustic, and phonetic representations. In the third stage, we process the imagined MEG responses from held-out subjects through the mapping pipeline to compute the corresponding listening responses that are then decoded by the listened decoder. Using rank-based analysis, we show that the imagined words are decodable significantly above chance. We shall report here the results of a proof-of-concept implementation to decode imagined speech, where all evaluations are performed on held-out subjects. We also demonstrate that performance improves with training data size, suggesting that this approach is scalable and can directly be made applicable to realistic brain-computer interface scenarios.
匹配关键词: contrastive learning
---

[ACADEMIC - ARXIV]
标题: GRAPHLCP: Structure-Aware Localized Conformal Prediction on Graphs
作者: Peyman Baghershahi, Fangxin Wang, Debmalya Mandal, Sourav Medya
链接: https://arxiv.org/abs/2605.08074v1
完整摘要: Conformal prediction (CP) provides a distribution-free approach to uncertainty quantification with finite-sample guarantees. However, applying CP to graph neural networks (GNNs) remains challenging as the combinatorial nature of graphs often leads to insufficiently certain predictions and indiscriminative embeddings. Existing methods primarily rely on embedding-space proximity for localization, which can be unreliable for graphs and yield inefficient prediction sets. We propose GRAPHLCP, a proximity-based localized CP framework that explicitly incorporates graph topology and inter-node dependencies into localization and weighting. Our approach introduces a feature-aware densification step to mitigate locality bias in sparse graphs, followed by a Personalized PageRank-based kernel computation to model structural proximity. This enables topology-dependent anchor sampling and calibration weighting that captures both local and long-range dependencies. Extensive experiments on several regression and classification datasets demonstrate that GRAPHLCP guarantees marginal coverage with finite samples while efficiently attaining favorable test conditional coverage across various conditioning scenarios.
匹配关键词: contrastive learning
---

[ACADEMIC - ARXIV]
标题: 123D: Unifying Multi-Modal Autonomous Driving Data at Scale
作者: Daniel Dauner, Valentin Charraut, Bastian Berle, Tianyu Li, Long Nguyen, Jiabao Wang, Changhui Jing, Maximilian Igl, Holger Caesar, Boris Ivanovic, Yiyi Liao, Andreas Geiger, Kashyap Chitta
链接: https://arxiv.org/abs/2605.08084v1
完整摘要: The pursuit of autonomous driving has produced one of the richest sensor data collections in all of robotics. However, its scale and diversity remain largely untapped. Each dataset adopts different 2D and 3D modalities, such as cameras, lidar, ego states, annotations, traffic lights, and HD maps, with different rates and synchronization schemes. They come in fragmented formats requiring complex dependencies that cannot natively coexist in the same development environment. Further, major inconsistencies in annotation conventions prevent training or measuring generalization across multiple datasets. We present 123D, an open-source framework that unifies such multi-modal driving data through a single API. To handle synchronization, we store each modality as an independent timestamped event stream with no prescribed rate, enabling synchronous or asynchronous access across arbitrary datasets. Using 123D, we consolidate eight real-world driving datasets spanning 3,300 hours and 90,000 kilometers, together with a synthetic dataset with configurable collection scripts, and provide tools for data analysis and visualization. We conduct a systematic study comparing annotation statistics and assessing each dataset's pose and calibration accuracy. Further, we showcase two applications 123D enables: cross-dataset 3D object detection transfer and reinforcement learning for planning, and offer recommendations for future directions. Code and documentation are available at https://github.com/kesai-labs/py123d.
匹配关键词: representation learning
---

[ACADEMIC - ARXIV]
标题: Normalizing Trajectory Models
作者: Jiatao Gu, Tianrong Chen, Ying Shen, David Berthelot, Shuangfei Zhai, Josh Susskind
链接: https://arxiv.org/abs/2605.08078v1
完整摘要: Diffusion-based models decompose sampling into many small Gaussian denoising steps -- an assumption that breaks down when generation is compressed to a few coarse transitions. Existing few-step methods address this through distillation, consistency training, or adversarial objectives, but sacrifice the likelihood framework in the process. We introduce Normalizing Trajectory Models (NTM), which models each reverse step as an expressive conditional normalizing flow with exact likelihood training. Architecturally, NTM combines shallow invertible blocks within each step with a deep parallel predictor across the trajectory, forming an end-to-end network trainable from scratch or initializable from pretrained flow-matching models. Its exact trajectory likelihood further enables self-distillation: a lightweight denoiser trained on the model's own score produces high-quality samples in four steps. On text-to-image benchmarks, NTM matches or outperforms strong image generation baselines in just four sampling steps while uniquely retaining exact likelihood over the generative trajectory.
匹配关键词: representation learning
---

[ACADEMIC - ARXIV]
标题: Conformal Path Reasoning: Trustworthy Knowledge Graph Question Answering via Path-Level Calibration
作者: Shuhang Lin, Chuhao Zhou, Xiao Lin, Zihan Dong, Kuan Lu, Zhencan Peng, Jie Yin, Dimitris N. Metaxas
链接: https://arxiv.org/abs/2605.08077v1
完整摘要: Knowledge Graph Question Answering (KGQA) has shown promise for grounded and interpretable reasoning, yet existing approaches often fail to provide reliable coverage guarantees over retrieved answers. While Conformal Prediction (CP) offers a principled framework for producing prediction sets with statistical guarantees, prior methods suffer from critical limitations in both calibration validity and score discriminability, resulting in violated coverage guarantees and excessively large prediction sets. To address these pitfalls, we propose Conformal Path Reasoning (CPR), a trustworthy KGQA framework with two key innovations. First, we perform query-level conformal calibration over path-level scores, preserving the exchangeability while generating path prediction sets. Second, we introduce the Residual Conformal Value Network (RCVNet), a lightweight module trained via PUCT-guided exploration to learn discriminative path-level nonconformity scores. Experiments on benchmarks show that CPR significantly improves the Empirical Coverage Rate by 34% while reducing average prediction set size by 40% compared to conformal baselines. These results validate the efficacy of CPR in satisfying coverage guarantees with substantially more compact answer sets.
匹配关键词: representation learning
---

[ACADEMIC - ARXIV]
标题: Zero-Shot Imagined Speech Decoding via Imagined-to-Listened MEG Mapping
作者: Maryam Maghsoudi, Shihab Shamma
链接: https://arxiv.org/abs/2605.08075v1
完整摘要: Decoding imagined speech from non-invasive brain recordings is challenging because imagined datasets are scarce and difficult to align temporally across subjects and sessions In this work, we propose a new approach to the decoding of imagined speech that leverages the richer and more reliably labeled recordings during listening to speech. We collected paired listened and imagined MEG recordings to rhythmic melodic and spoken stimuli from trained musicians. Using trained musicians helped improve temporal alignment across conditions. We then developed a three-stage decoding pipeline that revealed consistent and meaningful relationships between neural activity evoked by imagining and listening to the same stimuli. First, we trained six linear and neural models to map imagined MEG responses to listened responses. We evaluated these models against a null baseline from unseen subjects to validate that the predicted-listening responses preserve stimulus-specific information. In the second stage, we trained a contrastive word decoder exclusively on the listened MEG responses, and evaluated it using four embedding strategies including semantic, acoustic, and phonetic representations. In the third stage, we process the imagined MEG responses from held-out subjects through the mapping pipeline to compute the corresponding listening responses that are then decoded by the listened decoder. Using rank-based analysis, we show that the imagined words are decodable significantly above chance. We shall report here the results of a proof-of-concept implementation to decode imagined speech, where all evaluations are performed on held-out subjects. We also demonstrate that performance improves with training data size, suggesting that this approach is scalable and can directly be made applicable to realistic brain-computer interface scenarios.
匹配关键词: representation learning
---

[ACADEMIC - ARXIV]
标题: GRAPHLCP: Structure-Aware Localized Conformal Prediction on Graphs
作者: Peyman Baghershahi, Fangxin Wang, Debmalya Mandal, Sourav Medya
链接: https://arxiv.org/abs/2605.08074v1
完整摘要: Conformal prediction (CP) provides a distribution-free approach to uncertainty quantification with finite-sample guarantees. However, applying CP to graph neural networks (GNNs) remains challenging as the combinatorial nature of graphs often leads to insufficiently certain predictions and indiscriminative embeddings. Existing methods primarily rely on embedding-space proximity for localization, which can be unreliable for graphs and yield inefficient prediction sets. We propose GRAPHLCP, a proximity-based localized CP framework that explicitly incorporates graph topology and inter-node dependencies into localization and weighting. Our approach introduces a feature-aware densification step to mitigate locality bias in sparse graphs, followed by a Personalized PageRank-based kernel computation to model structural proximity. This enables topology-dependent anchor sampling and calibration weighting that captures both local and long-range dependencies. Extensive experiments on several regression and classification datasets demonstrate that GRAPHLCP guarantees marginal coverage with finite samples while efficiently attaining favorable test conditional coverage across various conditioning scenarios.
匹配关键词: representation learning
---

[ACADEMIC - ARXIV]
标题: LLMs Improving LLMs: Agentic Discovery for Test-Time Scaling
作者: Tong Zheng, Haolin Liu, Chengsong Huang, Huiwen Bao, Sheng Zhang, Rui Liu, Runpeng Dai, Ruibo Chen, Chenxi Liu, Tianyi Xiong, Xidong Wu, Hongming Zhang, Heng Huang
链接: https://arxiv.org/abs/2605.08083v1
完整摘要: Test-time scaling (TTS) has become an effective approach for improving large language model performance by allocating additional computation during inference. However, existing TTS strategies are largely hand-crafted: researchers manually design reasoning patterns and tune heuristics by intuition, leaving much of the computation-allocation space unexplored. We propose an environment-driven framework, AutoTTS, that changes what researchers design: from individual TTS heuristics to environments where TTS strategies can be discovered automatically. The key to AutoTTS lies in environment construction: the discovery environment must make the control space tractable and provide cheap, frequent feedback for TTS search. As a concrete instantiation, we formulate width--depth TTS as controller synthesis over pre-collected reasoning trajectories and probe signals, where controllers decide when to branch, continue, probe, prune, or stop and can be evaluated cheaply without repeated LLM calls. We further introduce beta parameterization to make the search tractable and fine-grained execution trace feedback to improve discovery efficiency by helping the agent diagnose why a TTS program fails. Experiments on mathematical reasoning benchmarks show that the discovered strategies improve the overall accuracy--cost tradeoff over strong manually designed baselines. The discovered strategies generalize to held-out benchmarks and model scales, while the entire discovery costs only $39.9 and 160 minutes. Our data, and code will be open-source at https://github.com/zhengkid/AutoTTS.
匹配关键词: masked language model
---

[ACADEMIC - ARXIV]
标题: Normalizing Trajectory Models
作者: Jiatao Gu, Tianrong Chen, Ying Shen, David Berthelot, Shuangfei Zhai, Josh Susskind
链接: https://arxiv.org/abs/2605.08078v1
完整摘要: Diffusion-based models decompose sampling into many small Gaussian denoising steps -- an assumption that breaks down when generation is compressed to a few coarse transitions. Existing few-step methods address this through distillation, consistency training, or adversarial objectives, but sacrifice the likelihood framework in the process. We introduce Normalizing Trajectory Models (NTM), which models each reverse step as an expressive conditional normalizing flow with exact likelihood training. Architecturally, NTM combines shallow invertible blocks within each step with a deep parallel predictor across the trajectory, forming an end-to-end network trainable from scratch or initializable from pretrained flow-matching models. Its exact trajectory likelihood further enables self-distillation: a lightweight denoiser trained on the model's own score produces high-quality samples in four steps. On text-to-image benchmarks, NTM matches or outperforms strong image generation baselines in just four sampling steps while uniquely retaining exact likelihood over the generative trajectory.
匹配关键词: masked language model
---

[ACADEMIC - ARXIV]
标题: Conformal Path Reasoning: Trustworthy Knowledge Graph Question Answering via Path-Level Calibration
作者: Shuhang Lin, Chuhao Zhou, Xiao Lin, Zihan Dong, Kuan Lu, Zhencan Peng, Jie Yin, Dimitris N. Metaxas
链接: https://arxiv.org/abs/2605.08077v1
完整摘要: Knowledge Graph Question Answering (KGQA) has shown promise for grounded and interpretable reasoning, yet existing approaches often fail to provide reliable coverage guarantees over retrieved answers. While Conformal Prediction (CP) offers a principled framework for producing prediction sets with statistical guarantees, prior methods suffer from critical limitations in both calibration validity and score discriminability, resulting in violated coverage guarantees and excessively large prediction sets. To address these pitfalls, we propose Conformal Path Reasoning (CPR), a trustworthy KGQA framework with two key innovations. First, we perform query-level conformal calibration over path-level scores, preserving the exchangeability while generating path prediction sets. Second, we introduce the Residual Conformal Value Network (RCVNet), a lightweight module trained via PUCT-guided exploration to learn discriminative path-level nonconformity scores. Experiments on benchmarks show that CPR significantly improves the Empirical Coverage Rate by 34% while reducing average prediction set size by 40% compared to conformal baselines. These results validate the efficacy of CPR in satisfying coverage guarantees with substantially more compact answer sets.
匹配关键词: masked language model
---

[ACADEMIC - ARXIV]
标题: Zero-Shot Imagined Speech Decoding via Imagined-to-Listened MEG Mapping
作者: Maryam Maghsoudi, Shihab Shamma
链接: https://arxiv.org/abs/2605.08075v1
完整摘要: Decoding imagined speech from non-invasive brain recordings is challenging because imagined datasets are scarce and difficult to align temporally across subjects and sessions In this work, we propose a new approach to the decoding of imagined speech that leverages the richer and more reliably labeled recordings during listening to speech. We collected paired listened and imagined MEG recordings to rhythmic melodic and spoken stimuli from trained musicians. Using trained musicians helped improve temporal alignment across conditions. We then developed a three-stage decoding pipeline that revealed consistent and meaningful relationships between neural activity evoked by imagining and listening to the same stimuli. First, we trained six linear and neural models to map imagined MEG responses to listened responses. We evaluated these models against a null baseline from unseen subjects to validate that the predicted-listening responses preserve stimulus-specific information. In the second stage, we trained a contrastive word decoder exclusively on the listened MEG responses, and evaluated it using four embedding strategies including semantic, acoustic, and phonetic representations. In the third stage, we process the imagined MEG responses from held-out subjects through the mapping pipeline to compute the corresponding listening responses that are then decoded by the listened decoder. Using rank-based analysis, we show that the imagined words are decodable significantly above chance. We shall report here the results of a proof-of-concept implementation to decode imagined speech, where all evaluations are performed on held-out subjects. We also demonstrate that performance improves with training data size, suggesting that this approach is scalable and can directly be made applicable to realistic brain-computer interface scenarios.
匹配关键词: masked language model
---

[ACADEMIC - ARXIV]
标题: GRAPHLCP: Structure-Aware Localized Conformal Prediction on Graphs
作者: Peyman Baghershahi, Fangxin Wang, Debmalya Mandal, Sourav Medya
链接: https://arxiv.org/abs/2605.08074v1
完整摘要: Conformal prediction (CP) provides a distribution-free approach to uncertainty quantification with finite-sample guarantees. However, applying CP to graph neural networks (GNNs) remains challenging as the combinatorial nature of graphs often leads to insufficiently certain predictions and indiscriminative embeddings. Existing methods primarily rely on embedding-space proximity for localization, which can be unreliable for graphs and yield inefficient prediction sets. We propose GRAPHLCP, a proximity-based localized CP framework that explicitly incorporates graph topology and inter-node dependencies into localization and weighting. Our approach introduces a feature-aware densification step to mitigate locality bias in sparse graphs, followed by a Personalized PageRank-based kernel computation to model structural proximity. This enables topology-dependent anchor sampling and calibration weighting that captures both local and long-range dependencies. Extensive experiments on several regression and classification datasets demonstrate that GRAPHLCP guarantees marginal coverage with finite samples while efficiently attaining favorable test conditional coverage across various conditioning scenarios.
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
标题: SCOPE: Structured Decomposition and Conditional Skill Orchestration for Complex Image Generation
作者: Tianfei Ren, Zhipeng Yan, Yiming Zhao, Zhen Fang, Yu Zeng, Guohui Zhang, Hang Xu, Xiaoxiao Ma, Shiting Huang, Ke Xu, Wenxuan Huang, Lionel Z. Wang, Lin Chen, Zehui Chen, Jie Huang, Feng Zhao
链接: https://arxiv.org/abs/2605.08043v1
完整摘要: While text-to-image models have made strong progress in visual fidelity, faithfully realizing complex visual intents remains challenging because many requirements must be tracked across grounding, generation, and verification. We refer to these requirements as semantic commitments and formalize their lifecycle discontinuity as the Conceptual Rift, where commitments may be locally resolved or checked but fail to remain identifiable as the same operational units throughout the generation lifecycle. To address this, we propose SCOPE, a specification-guided skill orchestration framework that maintains semantic commitments in an evolving structured specification and conditionally invokes retrieval, reasoning, and repair skills around unresolved or violated commitments. To evaluate commitment-level intent realization, we introduce Gen-Arena, a human-annotated benchmark with entity- and constraint-level specifications, together with Entity-Gated Intent Pass Rate (EGIP), a strict entity-first pass criterion. SCOPE substantially outperforms all evaluated baselines on Gen-Arena, achieving 0.60 EGIP, and further achieves strong results on WISE-V (0.907) and MindBench (0.61), demonstrating the effectiveness of persistent commitment tracking for complex image generation.
匹配关键词: MAE
---

[ACADEMIC - ARXIV]
标题: Object Hallucination-Free Reinforcement Unlearning for Vision-Language Models
作者: Kaidi Jia, Yujie Lin, Chengyi Yang, Jiayao Ma, Jinsong Su
链接: https://arxiv.org/abs/2605.08031v1
完整摘要: Vision-language models (VLMs) raise growing concerns about privacy, copyright, and bias, motivating machine unlearning to remove sensitive knowledge. However, existing methods primarily fine-tune the language decoder, leading to superficial forgetting that fails to erase underlying visual representations and often introduces object hallucination. We propose HFRU, a reinforcement unlearning framework that operates on the vision encoder for deep semantic removal. Our two-stage approach combines alignment disruption with GRPO-based optimization using a composite reward, including an abstraction reward that encourages semantically valid substitutions and mitigates hallucinations. Experiments on object recognition and face identity tasks show that HFRU achieves over 98% forgetting and retention performance, while introducing negligible object hallucination, significantly outperforming prior methods.Our code and implementation details are available at https://github.com/XMUDeepLIT/HFRU.
匹配关键词: MAE
---

[ACADEMIC - ARXIV]
标题: Where's the Plan? Locating Latent Planning in Language Models with Lightweight Mechanistic Interventions
作者: Nicole Ma, Nick Rui
链接: https://arxiv.org/abs/2605.07984v1
完整摘要: We study planning site formation in language models -- where internal representations of structurally-constrained future tokens form during the forward pass, and whether they causally drive generation. Using rhyming-couplet completion as a clean test of forward-looking constraint, we apply two lightweight methods (linear probing and activation patching) across Qwen3, Gemma-3, and Llama-3 at more than ten scales. Probing shows that future-rhyme information is linearly decodable at the line boundary, with signal that strengthens with scale in all three families. Activation patching reveals that only Gemma-3-27B causally relies on this encoding, exhibiting a handoff in which the causal driver migrates from the rhyme word to the line boundary around layer 30. Every other model we test conditions on the rhyme word throughout generation, with near-zero causal effect at the line boundary despite strong probe signal. We localize the Gemma-3-27B handoff to five attention heads through two-stage path patching that recover ~90% of the rhyme-routing capacity at the newline.
匹配关键词: MAE
---

[ACADEMIC - ARXIV]
标题: Delta-Adapter: Scalable Exemplar-Based Image Editing with Single-Pair Supervision
作者: Jiacheng Chen, Songze Li, Han Fu, Baoquan Zhao, Wei Liu, Yanyan Liang, Li Qing, Xudong Mao
链接: https://arxiv.org/abs/2605.07940v1
完整摘要: Exemplar-based image editing applies a transformation defined by a source-target image pair to a new query image. Existing methods rely on a pair-of-pairs supervision paradigm, requiring two image pairs sharing the same edit semantics to learn the target transformation. This constraint makes training data difficult to curate at scale and limits generalization across diverse edit types. We propose Delta-Adapter, a method that learns transferable editing semantics under single-pair supervision, requiring no textual guidance. Rather than directly exposing the exemplar pair to the model, we leverage a pre-trained vision encoder to extract a semantic delta that encodes the visual transformation between the two images. This semantic delta is injected into a pre-trained image editing model via a Perceiver-based adapter. Since the target image is never directly visible to the model, it can serve as the prediction target, enabling single-pair supervision without requiring additional exemplar pairs. This formulation allows us to leverage existing large-scale editing datasets for training. To further promote faithful transformation transfer, we introduce a semantic delta consistency loss that aligns the semantic change of the generated output with the ground-truth semantic delta extracted from the exemplar pair. Extensive experiments demonstrate that Delta-Adapter consistently improves both editing accuracy and content consistency over four strong baselines on seen editing tasks, while also generalizing more effectively to unseen editing tasks. Code will be available at https://delta-adapter.github.io.
匹配关键词: MAE
---

[ACADEMIC - ARXIV]
标题: One Token Per Frame: Reconsidering Visual Bandwidth in World Models for VLA Policy
作者: Zuojin Tang, Shengchao Yuan, Xiaoxin Bai, Zhiyuan Jin, De Ma, Gang Pan, Bin Liu
链接: https://arxiv.org/abs/2605.07931v1
完整摘要: Vision-language-action (VLA) models increasingly rely on auxiliary world modules to plan over long horizons, yet how such modules should be parameterized on top of a pretrained VLA remains an open design question. Existing world-model-augmented VLAs typically pass the per-frame visual stream into the world module at high visual bandwidth and treat its rollout as a side product of action prediction; under a constrained adaptation budget on a frozen backbone, this leaves both the per-frame representation and the latent action coupling under-examined. We introduce OneWM-VLA, which compresses each view into a single semantic token per frame through an Adaptive Attention Pooling, and produces the resulting latent stream and the action trajectory under a single flow-matching objective rather than connecting them through a separate decoder. Empirically, we find that per-frame visual bandwidth can be reduced to a single token without compromising long-horizon performance under our setup. Trained with 14.71M LoRA parameters on a $π_0$ (2B) backbone, OneWM-VLA improves the average success rate from 47.9% to 61.3% on MetaWorld~MT50, reaches 95.6% on LIBERO-Long (vs.85.2% for $π_0$), and reaches 60.0% on the long-horizon deformable task Fold Cloth on a real Piper arm (vs.20.0% for $π_0$).
匹配关键词: MAE
---

[ACADEMIC - ARXIV]
标题: 123D: Unifying Multi-Modal Autonomous Driving Data at Scale
作者: Daniel Dauner, Valentin Charraut, Bastian Berle, Tianyu Li, Long Nguyen, Jiabao Wang, Changhui Jing, Maximilian Igl, Holger Caesar, Boris Ivanovic, Yiyi Liao, Andreas Geiger, Kashyap Chitta
链接: https://arxiv.org/abs/2605.08084v1
完整摘要: The pursuit of autonomous driving has produced one of the richest sensor data collections in all of robotics. However, its scale and diversity remain largely untapped. Each dataset adopts different 2D and 3D modalities, such as cameras, lidar, ego states, annotations, traffic lights, and HD maps, with different rates and synchronization schemes. They come in fragmented formats requiring complex dependencies that cannot natively coexist in the same development environment. Further, major inconsistencies in annotation conventions prevent training or measuring generalization across multiple datasets. We present 123D, an open-source framework that unifies such multi-modal driving data through a single API. To handle synchronization, we store each modality as an independent timestamped event stream with no prescribed rate, enabling synchronous or asynchronous access across arbitrary datasets. Using 123D, we consolidate eight real-world driving datasets spanning 3,300 hours and 90,000 kilometers, together with a synthetic dataset with configurable collection scripts, and provide tools for data analysis and visualization. We conduct a systematic study comparing annotation statistics and assessing each dataset's pose and calibration accuracy. Further, we showcase two applications 123D enables: cross-dataset 3D object detection transfer and reinforcement learning for planning, and offer recommendations for future directions. Code and documentation are available at https://github.com/kesai-labs/py123d.
匹配关键词: generative model
---

[ACADEMIC - ARXIV]
标题: LLMs Improving LLMs: Agentic Discovery for Test-Time Scaling
作者: Tong Zheng, Haolin Liu, Chengsong Huang, Huiwen Bao, Sheng Zhang, Rui Liu, Runpeng Dai, Ruibo Chen, Chenxi Liu, Tianyi Xiong, Xidong Wu, Hongming Zhang, Heng Huang
链接: https://arxiv.org/abs/2605.08083v1
完整摘要: Test-time scaling (TTS) has become an effective approach for improving large language model performance by allocating additional computation during inference. However, existing TTS strategies are largely hand-crafted: researchers manually design reasoning patterns and tune heuristics by intuition, leaving much of the computation-allocation space unexplored. We propose an environment-driven framework, AutoTTS, that changes what researchers design: from individual TTS heuristics to environments where TTS strategies can be discovered automatically. The key to AutoTTS lies in environment construction: the discovery environment must make the control space tractable and provide cheap, frequent feedback for TTS search. As a concrete instantiation, we formulate width--depth TTS as controller synthesis over pre-collected reasoning trajectories and probe signals, where controllers decide when to branch, continue, probe, prune, or stop and can be evaluated cheaply without repeated LLM calls. We further introduce beta parameterization to make the search tractable and fine-grained execution trace feedback to improve discovery efficiency by helping the agent diagnose why a TTS program fails. Experiments on mathematical reasoning benchmarks show that the discovered strategies improve the overall accuracy--cost tradeoff over strong manually designed baselines. The discovered strategies generalize to held-out benchmarks and model scales, while the entire discovery costs only $39.9 and 160 minutes. Our data, and code will be open-source at https://github.com/zhengkid/AutoTTS.
匹配关键词: generative model
---

[ACADEMIC - ARXIV]
标题: Normalizing Trajectory Models
作者: Jiatao Gu, Tianrong Chen, Ying Shen, David Berthelot, Shuangfei Zhai, Josh Susskind
链接: https://arxiv.org/abs/2605.08078v1
完整摘要: Diffusion-based models decompose sampling into many small Gaussian denoising steps -- an assumption that breaks down when generation is compressed to a few coarse transitions. Existing few-step methods address this through distillation, consistency training, or adversarial objectives, but sacrifice the likelihood framework in the process. We introduce Normalizing Trajectory Models (NTM), which models each reverse step as an expressive conditional normalizing flow with exact likelihood training. Architecturally, NTM combines shallow invertible blocks within each step with a deep parallel predictor across the trajectory, forming an end-to-end network trainable from scratch or initializable from pretrained flow-matching models. Its exact trajectory likelihood further enables self-distillation: a lightweight denoiser trained on the model's own score produces high-quality samples in four steps. On text-to-image benchmarks, NTM matches or outperforms strong image generation baselines in just four sampling steps while uniquely retaining exact likelihood over the generative trajectory.
匹配关键词: generative model
---

[ACADEMIC - ARXIV]
标题: Conformal Path Reasoning: Trustworthy Knowledge Graph Question Answering via Path-Level Calibration
作者: Shuhang Lin, Chuhao Zhou, Xiao Lin, Zihan Dong, Kuan Lu, Zhencan Peng, Jie Yin, Dimitris N. Metaxas
链接: https://arxiv.org/abs/2605.08077v1
完整摘要: Knowledge Graph Question Answering (KGQA) has shown promise for grounded and interpretable reasoning, yet existing approaches often fail to provide reliable coverage guarantees over retrieved answers. While Conformal Prediction (CP) offers a principled framework for producing prediction sets with statistical guarantees, prior methods suffer from critical limitations in both calibration validity and score discriminability, resulting in violated coverage guarantees and excessively large prediction sets. To address these pitfalls, we propose Conformal Path Reasoning (CPR), a trustworthy KGQA framework with two key innovations. First, we perform query-level conformal calibration over path-level scores, preserving the exchangeability while generating path prediction sets. Second, we introduce the Residual Conformal Value Network (RCVNet), a lightweight module trained via PUCT-guided exploration to learn discriminative path-level nonconformity scores. Experiments on benchmarks show that CPR significantly improves the Empirical Coverage Rate by 34% while reducing average prediction set size by 40% compared to conformal baselines. These results validate the efficacy of CPR in satisfying coverage guarantees with substantially more compact answer sets.
匹配关键词: generative model
---

[ACADEMIC - ARXIV]
标题: Zero-Shot Imagined Speech Decoding via Imagined-to-Listened MEG Mapping
作者: Maryam Maghsoudi, Shihab Shamma
链接: https://arxiv.org/abs/2605.08075v1
完整摘要: Decoding imagined speech from non-invasive brain recordings is challenging because imagined datasets are scarce and difficult to align temporally across subjects and sessions In this work, we propose a new approach to the decoding of imagined speech that leverages the richer and more reliably labeled recordings during listening to speech. We collected paired listened and imagined MEG recordings to rhythmic melodic and spoken stimuli from trained musicians. Using trained musicians helped improve temporal alignment across conditions. We then developed a three-stage decoding pipeline that revealed consistent and meaningful relationships between neural activity evoked by imagining and listening to the same stimuli. First, we trained six linear and neural models to map imagined MEG responses to listened responses. We evaluated these models against a null baseline from unseen subjects to validate that the predicted-listening responses preserve stimulus-specific information. In the second stage, we trained a contrastive word decoder exclusively on the listened MEG responses, and evaluated it using four embedding strategies including semantic, acoustic, and phonetic representations. In the third stage, we process the imagined MEG responses from held-out subjects through the mapping pipeline to compute the corresponding listening responses that are then decoded by the listened decoder. Using rank-based analysis, we show that the imagined words are decodable significantly above chance. We shall report here the results of a proof-of-concept implementation to decode imagined speech, where all evaluations are performed on held-out subjects. We also demonstrate that performance improves with training data size, suggesting that this approach is scalable and can directly be made applicable to realistic brain-computer interface scenarios.
匹配关键词: generative model
---

[ACADEMIC - ARXIV]
标题: LLMs Improving LLMs: Agentic Discovery for Test-Time Scaling
作者: Tong Zheng, Haolin Liu, Chengsong Huang, Huiwen Bao, Sheng Zhang, Rui Liu, Runpeng Dai, Ruibo Chen, Chenxi Liu, Tianyi Xiong, Xidong Wu, Hongming Zhang, Heng Huang
链接: https://arxiv.org/abs/2605.08083v1
完整摘要: Test-time scaling (TTS) has become an effective approach for improving large language model performance by allocating additional computation during inference. However, existing TTS strategies are largely hand-crafted: researchers manually design reasoning patterns and tune heuristics by intuition, leaving much of the computation-allocation space unexplored. We propose an environment-driven framework, AutoTTS, that changes what researchers design: from individual TTS heuristics to environments where TTS strategies can be discovered automatically. The key to AutoTTS lies in environment construction: the discovery environment must make the control space tractable and provide cheap, frequent feedback for TTS search. As a concrete instantiation, we formulate width--depth TTS as controller synthesis over pre-collected reasoning trajectories and probe signals, where controllers decide when to branch, continue, probe, prune, or stop and can be evaluated cheaply without repeated LLM calls. We further introduce beta parameterization to make the search tractable and fine-grained execution trace feedback to improve discovery efficiency by helping the agent diagnose why a TTS program fails. Experiments on mathematical reasoning benchmarks show that the discovered strategies improve the overall accuracy--cost tradeoff over strong manually designed baselines. The discovered strategies generalize to held-out benchmarks and model scales, while the entire discovery costs only $39.9 and 160 minutes. Our data, and code will be open-source at https://github.com/zhengkid/AutoTTS.
匹配关键词: diffusion model
---

[ACADEMIC - ARXIV]
标题: Normalizing Trajectory Models
作者: Jiatao Gu, Tianrong Chen, Ying Shen, David Berthelot, Shuangfei Zhai, Josh Susskind
链接: https://arxiv.org/abs/2605.08078v1
完整摘要: Diffusion-based models decompose sampling into many small Gaussian denoising steps -- an assumption that breaks down when generation is compressed to a few coarse transitions. Existing few-step methods address this through distillation, consistency training, or adversarial objectives, but sacrifice the likelihood framework in the process. We introduce Normalizing Trajectory Models (NTM), which models each reverse step as an expressive conditional normalizing flow with exact likelihood training. Architecturally, NTM combines shallow invertible blocks within each step with a deep parallel predictor across the trajectory, forming an end-to-end network trainable from scratch or initializable from pretrained flow-matching models. Its exact trajectory likelihood further enables self-distillation: a lightweight denoiser trained on the model's own score produces high-quality samples in four steps. On text-to-image benchmarks, NTM matches or outperforms strong image generation baselines in just four sampling steps while uniquely retaining exact likelihood over the generative trajectory.
匹配关键词: diffusion model
---

[ACADEMIC - ARXIV]
标题: Zero-Shot Imagined Speech Decoding via Imagined-to-Listened MEG Mapping
作者: Maryam Maghsoudi, Shihab Shamma
链接: https://arxiv.org/abs/2605.08075v1
完整摘要: Decoding imagined speech from non-invasive brain recordings is challenging because imagined datasets are scarce and difficult to align temporally across subjects and sessions In this work, we propose a new approach to the decoding of imagined speech that leverages the richer and more reliably labeled recordings during listening to speech. We collected paired listened and imagined MEG recordings to rhythmic melodic and spoken stimuli from trained musicians. Using trained musicians helped improve temporal alignment across conditions. We then developed a three-stage decoding pipeline that revealed consistent and meaningful relationships between neural activity evoked by imagining and listening to the same stimuli. First, we trained six linear and neural models to map imagined MEG responses to listened responses. We evaluated these models against a null baseline from unseen subjects to validate that the predicted-listening responses preserve stimulus-specific information. In the second stage, we trained a contrastive word decoder exclusively on the listened MEG responses, and evaluated it using four embedding strategies including semantic, acoustic, and phonetic representations. In the third stage, we process the imagined MEG responses from held-out subjects through the mapping pipeline to compute the corresponding listening responses that are then decoded by the listened decoder. Using rank-based analysis, we show that the imagined words are decodable significantly above chance. We shall report here the results of a proof-of-concept implementation to decode imagined speech, where all evaluations are performed on held-out subjects. We also demonstrate that performance improves with training data size, suggesting that this approach is scalable and can directly be made applicable to realistic brain-computer interface scenarios.
匹配关键词: diffusion model
---

[ACADEMIC - ARXIV]
标题: GRAPHLCP: Structure-Aware Localized Conformal Prediction on Graphs
作者: Peyman Baghershahi, Fangxin Wang, Debmalya Mandal, Sourav Medya
链接: https://arxiv.org/abs/2605.08074v1
完整摘要: Conformal prediction (CP) provides a distribution-free approach to uncertainty quantification with finite-sample guarantees. However, applying CP to graph neural networks (GNNs) remains challenging as the combinatorial nature of graphs often leads to insufficiently certain predictions and indiscriminative embeddings. Existing methods primarily rely on embedding-space proximity for localization, which can be unreliable for graphs and yield inefficient prediction sets. We propose GRAPHLCP, a proximity-based localized CP framework that explicitly incorporates graph topology and inter-node dependencies into localization and weighting. Our approach introduces a feature-aware densification step to mitigate locality bias in sparse graphs, followed by a Personalized PageRank-based kernel computation to model structural proximity. This enables topology-dependent anchor sampling and calibration weighting that captures both local and long-range dependencies. Extensive experiments on several regression and classification datasets demonstrate that GRAPHLCP guarantees marginal coverage with finite samples while efficiently attaining favorable test conditional coverage across various conditioning scenarios.
匹配关键词: diffusion model
---

[ACADEMIC - ARXIV]
标题: EmambaIR: Efficient Visual State Space Model for Event-guided Image Reconstruction
作者: Wei Yu, Yunhang Qian
链接: https://arxiv.org/abs/2605.08073v1
完整摘要: Recent event-based image reconstruction methods predominantly rely on Convolutional Neural Networks (CNNs) and Vision Transformers (ViTs) to process complementary event information. However, these architectures face fundamental limitations: CNNs often fail to capture global feature correlations, whereas ViTs incur quadratic computational complexity (e.g., $O(n^2)$), hindering their application in high-resolution scenarios. To address these bottlenecks, we introduce EmambaIR, an Efficient visual State Space Model designed for image reconstruction using spatially sparse and temporally continuous event streams. Our framework introduces two key components: the cross-modal Top-k Sparse Attention Module (TSAM) and the Gated State-Space Module (GSSM). TSAM efficiently performs pixel-level top-k sparse attention to guide cross-modal interactions, yielding rich yet sparse fusion features. Subsequently, GSSM utilizes a nonlinear gated unit to enhance the temporal representation of vanilla linear-complexity ($O(n)$) SSMs, effectively capturing global contextual dependencies without the typical computational overhead. Extensive experiments on six datasets across three diverse image reconstruction tasks - motion deblurring, deraining, and High Dynamic Range (HDR) enhancement - demonstrate that EmambaIR significantly outperforms state-of-the-art methods while offering substantial reductions in memory consumption and computational cost. The source code and data are publicly available at: https://github.com/YunhangWickert/EmambaIR
匹配关键词: diffusion model
---

[ACADEMIC - ARXIV]
标题: On the Tradeoffs of On-Device Generative Models in Federated Predictive Maintenance Systems
作者: Usevalad Milasheuski, Piero Baraldi, Enrico Zio, Stefano Savazzi
链接: https://arxiv.org/abs/2605.07860v1
完整摘要: Federated Learning (FL) has emerged as a promising paradigm for preserving client data ownership and control over distributed Internet of Things (IoT) environments. While discriminative models dominate most FL use cases, recent advances in generative models -- such as Variational Autoencoders (VAE), Generative Adversarial Networks (GAN), and Diffusion Models (DM) -- offer new opportunities for unsupervised anomaly detection in time series analysis, with relevant applications in predictive maintenance (PdM) in critical industrial infrastructures. In this work, we present a comprehensive analysis of VAEs, GANs, and DMs in the context of federated PdM. We analyze their performance and communication overhead under both full and partial federation setups, where only subsets of model components are shared. Building on this analysis, the paper proposes a novel taxonomy for federated generative models that formalizes partial component sharing as a principled mechanism for model personalization. Our experiments over a real-world time series dataset reveal distinct trade-offs in model utility, stability, and scalability, especially in heterogeneous and bandwidth-constrained FL settings. For the evaluated GAN-based configurations, full federation improves training stability relative to independent local training, although the model remains less robust than the VAE- and DDPM-based alternatives. For DMs, however, partial federation -- especially decoder sharing -- can outperform full federation in bandwidth-constrained, non-IID settings.
匹配关键词: GAN
---

[ACADEMIC - ARXIV]
标题: Retrieve, Integrate, and Synthesize: Spatial-Semantic Grounded Latent Visual Reasoning
作者: Jin Cui, Xinyue Long, Xunyong Zhang, Yadong Zhang, Chuanchang Su, Jingye Gan, Boran Zhao, Pengju Ren
链接: https://arxiv.org/abs/2605.07106v1
完整摘要: Multimodal Large Language Models (MLLMs) have made remarkable progress on vision-language reasoning, yet most methods still compress visual evidence into discrete textual thoughts, creating an information bottleneck for fine-grained perception. Recent latent visual reasoning methods attempt to reason in continuous hidden states, but we find that they suffer from insufficient manifold compatibility: latent trajectories drift away from pretrained reasoning circuits, collapse into instance-agnostic patterns, and are often bypassed during answer generation. To address these issues, we propose RIS (Retrieve, Integrate, and Synthesize), a spatial-semantic grounded framework that develops latent reasoning as a compatible extension of pretrained MLLM computation. We first construct a step-wise grounded reasoning dataset with bounding boxes and region-specific semantic descriptions. Built on this supervision, RIS anchors latent tokens to both spatial and semantic evidence, enforces their causal role through a progressive attention bottleneck, and introduces short language transition tokens to bridge synthesized latent states back to vocabulary-aligned decoding. Experiments on V*, HRBench4K, HRBench8K, MMVP, and BLINK show consistent improvements over closed/open-source and latent reasoning baselines. Further analyses demonstrate that RIS learns diverse, interpretable, and progressively integrated latent trajectories, offering a practical path toward faithful internal visual reasoning in MLLMs.
匹配关键词: GAN
---

[ACADEMIC - ARXIV]
标题: Decoupling Semantics and Fingerprints: A Universal Representation for AI-Generated Image Detection
作者: Zhiyuan Wang, Yanxiang Chen, Yuanzhi Yao, Yunfeng Diao
链接: https://arxiv.org/abs/2605.07074v1
完整摘要: Detecting AI-generated images across unseen architectures remains challenging, as existing models often overfit to generator-specific fingerprints and semantic content rather than learning universal forgery traces. We attribute this failure to feature entanglement: detectors learn these factors as a single entangled representation, where universal forgery traces are inextricably confounded with both generator-specific fingerprints and semantic content. Crucially, our spectral analysis reveals that this entanglement is avoidable: distinct generator-specific fingerprints (e.g., GAN stripes vs. Diffusion Model spots) occupy disjoint frequency subspaces and coexist as independent superpositions. Leveraging this physical orthogonality, we propose the Orthogonal Decomposition and Purification Network (ODP-Net) to structurally disentangle these factors. Specifically, ODP-Net employs (1) Instance-aware Orthogonal Decomposition to project features into mutually exclusive subspaces: universal forgery traces, generator-specific fingerprints, and semantic content; (2) Perturbation-based Purification to enforce semantic invariance via cross-sample feature injection; and (3) Manifold Alignment to bridge domain gaps. By explicitly decoupling universal forgery traces from generator-specific fingerprints and semantic content, ODP-Net achieves state-of-the-art performance on unseen architectures (e.g., Stable Diffusion 3), validating that structural disentanglement is key to generalization.
匹配关键词: GAN
---

[ACADEMIC - ARXIV]
标题: Integrating Causal DAGs in Deep RL: Activating Minimal Markovian States with Multi-Order Exposure
作者: Jiamin Xu, Jacqueline Maasch, Kyra Gan
链接: https://arxiv.org/abs/2605.07057v1
完整摘要: Online reinforcement learning (RL) relies on the Markov property for guaranteed performance, but real-world applications often lack well-defined states given raw observed variables. While causal RL has attracted growing interest, existing work typically assumes Markovian states are provided and focuses on using causality to accelerate learning, leaving a fundamental gap: \emph{given a longitudinal causal graph over observed variables, how does one construct MDP states that provably satisfy the Markov property?} We address this by providing a procedure that constructs a provably minimal state representation. In deep RL, we observe that the minimal representation alone empirically fails to improve performance, indicating that neural networks cannot directly exploit Markovian minimality. To address this, we propose \textbf{MOSE} (Multi-Order State Exposure), which feeds multi-order historical state constructions into the same $Q$-function. MOSE consistently outperforms both the minimal state construction and single-window policies on common benchmarks and synthetic datasets. Including the minimal representation alongside MOSE can further improve performance. Our results establish a core principle for causal deep RL: minimal sufficiency is not enough, and \emph{controlled redundancy} is necessary to unlock the benefit of causal state information.
匹配关键词: GAN
---

[ACADEMIC - ARXIV]
标题: LensVLM: Selective Context Expansion for Compressed Visual Representation of Text
作者: Roy Xie, Dan Friedman, Donghan Yu, Bowen Pan, Christopher Fifty, Jang-Hyun Kim, Xianzhi Du, Zhe Gan, Vivek Rathod, Bhuwan Dhingra
链接: https://arxiv.org/abs/2605.07019v1
完整摘要: Vision Language Models (VLMs) offer the exciting possibility of processing text as rendered images, bypassing the need for tokenizing the text into long token sequences. Since VLM image encoders map fixed-size images to a fixed number of visual tokens, varying rendering resolution provides a fine-grained compression knob. However, accuracy deteriorates quickly as compression increases: characters shrink below the vision encoder's effective resolution, making them indistinguishable. To address this, we propose LensVLM, an inference framework and post-training recipe that enables VLMs to scan compressed images, then selectively expand only the relevant images to their uncompressed form via learned tools. Building on Qwen3.5-9B-Base, LensVLM maintains accuracy comparable to the full-text upper bound at 4.3x effective compression and outperforms retrieval-based, text- and visual-compression baselines up to 10.1x effective compression across seven text QA benchmarks. LensVLM also generalizes to multimodal document and code understanding tasks, with the accuracy gain over baselines growing as compression increases. Our analysis validates this approach: training makes visual compression robust to rendering choices, and as compression grows the model increasingly relies on expanded content rather than unreliable visual reading. The analysis also yields practical tool-choice guidance: text expansion is preferable for rendered text, while high-resolution image expansion suits native documents whose layout cues carry task-relevant information.
匹配关键词: GAN
---

[ACADEMIC - ARXIV]
标题: BeeVe: Unsupervised Acoustic State Discovery in Honey Bee Buzzing
作者: Hamze Hammami, Nidhal Abdulaziz
链接: https://arxiv.org/abs/2605.07903v1
完整摘要: Discovering structure in biological signals without supervision is a fundamental problem in computational intelligence, yet existing bioacoustic methods assume vocal production models or predefined semantic units, leaving non-vocal species poorly served. This work introduces BeeVe, an unsupervised framework for acoustic state discovery in collective honey bee buzzing. BeeVe uses the self-supervised Patchout Spectrogram Transformer (PaSST) as a frozen feature extractor, then trains a Vector-Quantized Variational Autoencoder (VQ-VAE) without labels on those embeddings, learning a finite discrete codebook of acoustic tokens directly from unlabelled hive audio. No labels, pretext tasks, or contrastive objectives are used at any stage. Post-hoc evaluation against known queen status reveals that the learned tokens separate queenright and queenless conditions with Jensen-Shannon Divergence values between 0.609 and 0.688, and that the queenless condition further decomposes into three internally coherent sub-states stable across experiments with different codebook sizes and random seeds. Token transition analysis confirms non-random sequential structure (p << 0.001) across all experiments. Generalisation to unseen recordings preserves both token overlap (Jaccard = 0.947) and global manifold topology. These results demonstrate that unsupervised discrete codebook learning can recover repeatable acoustic structure from a non-vocal biological signal without annotation, opening a path toward non-invasive acoustic hive health monitoring.
匹配关键词: VAE
---

[ACADEMIC - ARXIV]
标题: On the Tradeoffs of On-Device Generative Models in Federated Predictive Maintenance Systems
作者: Usevalad Milasheuski, Piero Baraldi, Enrico Zio, Stefano Savazzi
链接: https://arxiv.org/abs/2605.07860v1
完整摘要: Federated Learning (FL) has emerged as a promising paradigm for preserving client data ownership and control over distributed Internet of Things (IoT) environments. While discriminative models dominate most FL use cases, recent advances in generative models -- such as Variational Autoencoders (VAE), Generative Adversarial Networks (GAN), and Diffusion Models (DM) -- offer new opportunities for unsupervised anomaly detection in time series analysis, with relevant applications in predictive maintenance (PdM) in critical industrial infrastructures. In this work, we present a comprehensive analysis of VAEs, GANs, and DMs in the context of federated PdM. We analyze their performance and communication overhead under both full and partial federation setups, where only subsets of model components are shared. Building on this analysis, the paper proposes a novel taxonomy for federated generative models that formalizes partial component sharing as a principled mechanism for model personalization. Our experiments over a real-world time series dataset reveal distinct trade-offs in model utility, stability, and scalability, especially in heterogeneous and bandwidth-constrained FL settings. For the evaluated GAN-based configurations, full federation improves training stability relative to independent local training, although the model remains less robust than the VAE- and DDPM-based alternatives. For DMs, however, partial federation -- especially decoder sharing -- can outperform full federation in bandwidth-constrained, non-IID settings.
匹配关键词: VAE
---

[ACADEMIC - ARXIV]
标题: TextLDM: Language Modeling with Continuous Latent Diffusion
作者: Jiaxiu Jiang, Jingjing Ren, Wenbo Li, Bo Wang, Haoze Sun, Yijun Yang, Jianhui Liu, Yanbing Zhang, Shenghe Zheng, Yuan Zhang, Haoyang Huang, Nan Duan, Wangmeng Zuo
链接: https://arxiv.org/abs/2605.07748v1
完整摘要: Diffusion Transformers (DiT) trained with flow matching in a VAE latent space have unified visual generation across images and videos. A natural next step toward a single architecture for both generation (visual synthesis) and understanding (text generation) is to apply this framework to language modeling. We propose TextLDM, which transfers the visual latent diffusion recipe to text generation with minimal architectural modification. A Transformer-based VAE maps discrete tokens to continuous latents, enhanced by Representation Alignment (REPA) with a frozen pretrained language model to produce representations effective for conditional denoising. A standard DiT then performs flow matching in this latent space, identical in architecture to its visual counterpart. The central challenge we address is obtaining high-quality continuous text representations: we find that reconstruction fidelity alone is insufficient, and that aligning latent features with a pretrained language model via REPA is critical for downstream generation quality. Trained from scratch on OpenWebText2, TextLDM substantially outperforms prior diffusion language models and matches GPT-2 under the same settings. Our results establish that the visual DiT recipe transfers effectively to language, taking a concrete step toward unified diffusion architectures for multimodal generation and understanding.
匹配关键词: VAE
---

[ACADEMIC - ARXIV]
标题: Task-Oriented Communication for Human Action Understanding via Edge-Cloud Co-Inference
作者: Jingyi Liu, Cheng Yuan, Lijun He, Jun Zhang, Jiawei Shao
链接: https://arxiv.org/abs/2605.07354v1
完整摘要: The expanding application of smart sensing has created a growing demand for the accurate understanding of human action at the network edge. Traditional approaches require massive video data to be transmitted from resource-constrained edge devices to powerful cloud servers, incurring prohibitive uplink bandwidth consumption and unacceptable latency while raising privacy concerns. To overcome these bottlenecks, we propose a task-oriented communication framework for human action understanding (TOAU) through edge-cloud collaboration. Our framework utilizes a monocular pose estimator to extract continuous joint coordinates from raw videos, followed by a vector quantized variational autoencoder (VQ-VAE) to convert these coordinates into discrete motion tokens. Consequently, only a compact sequence of codebook indices is transmitted over the network, consuming as few as 9 bits per frame and avoiding privacy leakages. At the cloud server, a lightweight projector aligns these motion tokens with the embedding space of a large vision-language model (VLM) to facilitate complex action understanding, which is trained with an efficient instruction tuning paradigm. Comprehensive evaluations on three benchmarks demonstrate that our TOAU system reduces the transmission payload to approximately 1\% and the system latency to around 20\% compared to video codec-based solutions, while delivering comparable action understanding accuracy.
匹配关键词: VAE
---

[ACADEMIC - ARXIV]
标题: PersonaGest: Personalized Co-Speech Gesture Generation with Semantic-Guided Hierarchical Motion Representation
作者: Junchuan Zhao, Qifan Liang, Ye Wang
链接: https://arxiv.org/abs/2605.07252v1
完整摘要: Co-speech gesture generation aims to synthesize realistic body movements that are semantically coherent with speech and faithful to a user-specified gestural style. Existing VQ-VAE based co-speech gesture generation methods improve generation quality but fail to encode semantic structure into the motion representation or explicitly disentangle content from style, limiting both semantic coherence and personalization fidelity. We present PersonaGest, a two-stage framework addressing both limitations. In the first stage, a semantic-guided RVQ-VAE disentangles motion content and gestural style within the residual quantization structure, where a Semantic-Aware Motion Codebook (SMoC) organizes the content codebook by gesture semantics and contrastive learning further enforces content-style separation. In the second stage, a Masked Generative Transformer generates content tokens via a semantic-aware re-masking strategy, followed by a cascade of Style Residual Transformers conditioned on a reference motion prompt for style control. Extensive experiments demonstrate state-of-the-art performance on objective metrics and perceptual user studies, with strong style consistency to the reference prompt. Our project page with demo videos is available at https://danny-nus.github.io/PersonaGest/
匹配关键词: VAE
---

[ACADEMIC - ARXIV]
标题: Fast Byte Latent Transformer
作者: Julie Kallini, Artidoro Pagnoni, Tomasz Limisiewicz, Gargi Ghosh, Luke Zettlemoyer, Christopher Potts, Xiaochuang Han, Srinivasan Iyer
链接: https://arxiv.org/abs/2605.08044v1
完整摘要: Recent byte-level language models (LMs) match the performance of token-level models without relying on subword vocabularies, yet their utility is limited by slow, byte-by-byte autoregressive generation. We address this bottleneck in the Byte Latent Transformer (BLT) through new training and generation techniques. First, we introduce BLT Diffusion (BLT-D), a new model and our fastest BLT variant, trained with an auxiliary block-wise diffusion objective alongside the standard next-byte prediction loss. This enables an inference procedure that generates multiple bytes in parallel per decoding step, substantially reducing the number of forward passes required to generate a sequence. Second, we propose two extensions inspired by speculative decoding that trade some of this speed for higher generation quality: BLT Self-speculation (BLT-S), in which BLT's local decoder continues generating past its normal patch boundaries to draft bytes, which are then verified with a single full-model forward pass; and BLT Diffusion+Verification (BLT-DV), which augments BLT-D with an autoregressive verification step after diffusion-based generation. All methods may achieve an estimated memory-bandwidth cost over 50% lower than BLT on generation tasks. Each approach offers its own unique advantages, together removing key barriers to the practical use of byte-level LMs.
匹配关键词: autoregressive
---

[ACADEMIC - ARXIV]
标题: STARFlow2: Bridging Language Models and Normalizing Flows for Unified Multimodal Generation
作者: Ying Shen, Tianrong Chen, Yuan Gao, Yizhe Zhang, Yuyang Wang, Miguel Ángel Bautista, Shuangfei Zhai, Joshua M. Susskind, Jiatao Gu
链接: https://arxiv.org/abs/2605.08029v1
完整摘要: Deep generative models have advanced rapidly across text and vision, motivating unified multimodal systems that can understand, reason over, and generate interleaved text-image sequences. Most existing approaches combine autoregressive language modeling with diffusion-based image generators, inheriting a structural mismatch between causal text generation and iterative visual denoising. We observe that autoregressive normalizing flows are autoregressive Transformers--sharing the same causal mask, KV-cache mechanism, and left-to-right structure as LLMs--making them the most natural paradigm for true unified multimodal generation. We present STARFlow2, built on the Pretzel architecture that vertically interleaves a pretrained VLM stream with a TarFlow stream via residual skip connections, both operating under the same causal mask. Combined with a deep-shallow flow design and a unified FAE latent space, STARFlow2 enables cache-friendly interleaved generation where both text and visual outputs directly enter the KV-cache without re-encoding. Experiments demonstrate strong performance across image generation and multimodal understanding benchmarks, validating autoregressive flows as a viable foundation for unified multimodal modeling.
匹配关键词: autoregressive
---

[ACADEMIC - ARXIV]
标题: Tool Calling is Linearly Readable and Steerable in Language Models
作者: Zekun Wu, Ze Wang, Seonglae Cho, Yufei Yang, Adriano Koshiyama, Sahan Bulathwela, Maria Perez-Ortiz
链接: https://arxiv.org/abs/2605.07990v1
完整摘要: When a tool-calling agent picks the wrong tool, the failure is invisible until execution: the email gets sent, the meeting gets missed. Probing 12 instruction-tuned models across Gemma 3, Qwen 3, Qwen 2.5, and Llama 3.1 (270M to 27B), we find the identity of the chosen tool is linearly readable and steerable inside the model. Adding the mean-difference between two tools' average internal activations switches which tool the model selects at 77-100% accuracy on name-only single-turn prompts (93-100% at 4B+), and the JSON arguments that follow autoregressively match the new tool's schema, so flipping the name is enough. The same per-tool means also flag likely errors before they happen: on Gemma 3 12B and 27B, queries where the gap between the top-1 and top-2 tool is smallest produce 14-21x more wrong calls than queries with the largest gap. The causal effect concentrates along one direction, the row of the output layer that produces the target tool's first token: a unit vector along it at matched magnitude already reaches 93-100%, while what is left over leaves the choice almost untouched. Activation patching localises this to a small set of mid- and late-layer attention heads, and a within-topic probe across 14 same-domain $τ$-bench airline tools reaches top-1 61-89% across five 4B-14B models, ruling out the reading that we are just moving the model along a topic axis. Even base models encode the right tool before they can emit it: cosine readout from the internal state recovers 69-82% on BFCL while base generation reaches only 2-10%, suggesting pretraining forms the representation and instruction tuning later wires it to the output. We measure tool identity selection and JSON schema correctness in single-turn fixed-menu settings; multi-turn agentic transfer is more fragile and is discussed in Limitations.
匹配关键词: autoregressive
---

[ACADEMIC - ARXIV]
标题: GLiGuard: Schema-Conditioned Classification for LLM Safeguard
作者: Urchade Zaratiana, Mary Newhauser, George Hurn-Maloney, Ash Lewis
链接: https://arxiv.org/abs/2605.07982v1
完整摘要: Ensuring safe, policy-compliant outputs from large language models requires real-time content moderation that can scale across multiple safety dimensions. However, state-of-the-art guardrail models rely on autoregressive decoders with 7B--27B parameters, reformulating what is fundamentally a classification problem as sequential text generation, a design choice that incurs high latency and scales poorly to multi-aspect evaluation. In this work, we introduce \textbf{GLiGuard}, a 0.3B-parameter schema-conditioned bidirectional encoder adapted from GLiNER2 for LLM content moderation. The key idea is to encode task definitions and label semantics directly into the input sequence as structured token schemas, enabling simultaneous evaluation of prompt safety, response safety, refusal detection, 14 fine-grained harm categories, and 11 jailbreak strategies in a single non-autoregressive forward pass. This schema-conditioned design lets supported task and label blocks be composed directly in the input schema at inference time. Across nine established safety benchmarks, GLiGuard achieves F1 scores competitive with 7B--27B decoder-based guards despite being 23--90$\times$ smaller, while delivering up to 16$\times$ higher throughput and 17$\times$ lower latency. These results suggest that compact bidirectional encoders can approach the accuracy of much larger guard models while drastically reducing inference cost. Code and models are available at https://github.com/fastino-ai/GLiGuard.
匹配关键词: autoregressive
---

[ACADEMIC - ARXIV]
标题: How to Train Your Latent Diffusion Language Model Jointly With the Latent Space
作者: Viacheslav Meshchaninov, Alexander Shabalin, Egor Chimbulatov, Nikita Gushchin, Ilya Koziev, Alexander Korotin, Dmitry Vetrov
链接: https://arxiv.org/abs/2605.07933v1
完整摘要: Latent diffusion models offer an attractive alternative to discrete diffusion for non-autoregressive text generation by operating on continuous text representations and denoising entire sequences in parallel. The major challenge in latent diffusion modeling is constructing a suitable latent space. In this work, we present the Latent Diffusion Language Model (LDLM), in which the latent encoder, diffusion model, and decoder are trained jointly. LDLM builds its latent space by reshaping the representations of a pre-trained language model with a trainable encoder, yielding latents that are easy to both denoise and decode into tokens. We show that naive joint training produces a low-quality diffusion model, and propose a simple training recipe consisting of an MSE decoder loss, diffusion-to-encoder warmup, adaptive timestep sampling, and decoder-input noise. Ablations show that each component substantially impacts generation performance. On OpenWebText and LM1B, LDLM achieves better generation performance than existing discrete and continuous diffusion language models while being $2{\text -}13\times$ faster, indicating that jointly learning the latent space is a key step toward making latent diffusion competitive for text generation.
匹配关键词: autoregressive
---

[ACADEMIC - ARXIV]
标题: Normalizing Trajectory Models
作者: Jiatao Gu, Tianrong Chen, Ying Shen, David Berthelot, Shuangfei Zhai, Josh Susskind
链接: https://arxiv.org/abs/2605.08078v1
完整摘要: Diffusion-based models decompose sampling into many small Gaussian denoising steps -- an assumption that breaks down when generation is compressed to a few coarse transitions. Existing few-step methods address this through distillation, consistency training, or adversarial objectives, but sacrifice the likelihood framework in the process. We introduce Normalizing Trajectory Models (NTM), which models each reverse step as an expressive conditional normalizing flow with exact likelihood training. Architecturally, NTM combines shallow invertible blocks within each step with a deep parallel predictor across the trajectory, forming an end-to-end network trainable from scratch or initializable from pretrained flow-matching models. Its exact trajectory likelihood further enables self-distillation: a lightweight denoiser trained on the model's own score produces high-quality samples in four steps. On text-to-image benchmarks, NTM matches or outperforms strong image generation baselines in just four sampling steps while uniquely retaining exact likelihood over the generative trajectory.
匹配关键词: latent diffusion
---

[ACADEMIC - ARXIV]
标题: Flow-OPD: On-Policy Distillation for Flow Matching Models
作者: Zhen Fang, Wenxuan Huang, Yu Zeng, Yiming Zhao, Shuang Chen, Kaituo Feng, Yunlong Lin, Lin Chen, Zehui Chen, Shaosheng Cao, Feng Zhao
链接: https://arxiv.org/abs/2605.08063v1
完整摘要: Existing Flow Matching (FM) text-to-image models suffer from two critical bottlenecks under multi-task alignment: the reward sparsity induced by scalar-valued rewards, and the gradient interference arising from jointly optimizing heterogeneous objectives, which together give rise to a 'seesaw effect' of competing metrics and pervasive reward hacking. Inspired by the success of On-Policy Distillation (OPD) in the large language model community, we propose Flow-OPD, the first unified post-training framework that integrates on-policy distillation into Flow Matching models. Flow-OPD adopts a two-stage alignment strategy: it first cultivates domain-specialized teacher models via single-reward GRPO fine-tuning, allowing each expert to reach its performance ceiling in isolation; it then establishes a robust initial policy through a Flow-based Cold-Start scheme and seamlessly consolidates heterogeneous expertise into a single student via a three-step orchestration of on-policy sampling, task-routing labeling, and dense trajectory-level supervision. We further introduce Manifold Anchor Regularization (MAR), which leverages a task-agnostic teacher to provide full-data supervision that anchors generation to a high-quality manifold, effectively mitigating the aesthetic degradation commonly observed in purely RL-driven alignment. Built upon Stable Diffusion 3.5 Medium, Flow-OPD raises the GenEval score from 63 to 92 and the OCR accuracy from 59 to 94, yielding an overall improvement of roughly 10 points over vanilla GRPO, while preserving image fidelity and human-preference alignment and exhibiting an emergent 'teacher-surpassing' effect. These results establish Flow-OPD as a scalable alignment paradigm for building generalist text-to-image models.
匹配关键词: latent diffusion
---

[ACADEMIC - ARXIV]
标题: Towards Highly-Constrained Human Motion Generation with Retrieval-Guided Diffusion Noise Optimization
作者: Hanchao Liu, Fang-Lue Zhang, Shining Zhang, Tai-Jiang Mu, Shi-Min Hu
链接: https://arxiv.org/abs/2605.08054v1
完整摘要: Generating human motion that satisfies customized zero-shot goal functions, enabling applications such as controllable character animation and behavior synthesis for virtual agents, is a critical capability. While current approaches handle many unseen constraints, they fail on tasks with very challenging spatiotemporal restrictions, such as severe spatial obstacles or specified numbers of walking steps. To equip motion generators for these highly constrained tasks, we present a retrieval-guided method built on the training-free diffusion noise optimization framework. The key idea is to search within large motion datasets for guidance that can potentially satisfy difficult constraints. We introduce relational task parsing to group target constraints and identify the difficult ones to be handled by retrieved reference. A better initialization for diffusion noise is then obtained via a reward-guided mask that combines random noise with retrieved noise. By optimizing diffusion noise from this improved initialization, we successfully solve highly constrained generation tasks. By leveraging LLM for relational task parsing, the whole framework is further enabled to automatically reason for what to retrieve, improving the intelligence of moving agents under a training-free optimization scheme.
匹配关键词: latent diffusion
---

[ACADEMIC - ARXIV]
标题: MoCoTalk: Multi-Conditional Diffusion with Adaptive Router for Controllable Talking Head Generation
作者: Xinyan Ye, Jiankang Deng, Abbas Edalat
链接: https://arxiv.org/abs/2605.08050v1
完整摘要: Talking-head generation requires joint modeling of identity, head pose, facial expression, and mouth dynamics. Existing methods typically address only a subset of these factors, and rely on fixed-weight or heuristic fusion when multiple conditions are involved. We present MoCoTalk, a multi-conditional video diffusion framework that unifies four complementary control signals: a reference image, facial keypoints, 3DMM-rendered shading meshes, and the corresponding speech audio. To resolve destructive interference among heterogeneous conditions, we introduce an Adaptive Multi-Condition Router that computes channel-wise, timestep-aware gating over the four condition streams, allowing the fusion strategy to vary with both feature subspace and noise level. To better capture speech-related facial dynamics, we design a Mouth-Augmented Shading Mesh, a 3DMM-based representation that decouples head motion, mouth motion, expression, and lighting. This design provides a temporally consistent geometric prior and allows flexible recombination of these attributes at inference. We further introduce a lip consistency loss to tighten audio-visual alignment. Extensive experiments show that MoCoTalk achieves state-of-the-art performance on the majority of structural, motion, and perceptual metrics, while offering attribute-level controllability that single-condition methods do not provide.
匹配关键词: latent diffusion
---

[ACADEMIC - ARXIV]
标题: Fast Byte Latent Transformer
作者: Julie Kallini, Artidoro Pagnoni, Tomasz Limisiewicz, Gargi Ghosh, Luke Zettlemoyer, Christopher Potts, Xiaochuang Han, Srinivasan Iyer
链接: https://arxiv.org/abs/2605.08044v1
完整摘要: Recent byte-level language models (LMs) match the performance of token-level models without relying on subword vocabularies, yet their utility is limited by slow, byte-by-byte autoregressive generation. We address this bottleneck in the Byte Latent Transformer (BLT) through new training and generation techniques. First, we introduce BLT Diffusion (BLT-D), a new model and our fastest BLT variant, trained with an auxiliary block-wise diffusion objective alongside the standard next-byte prediction loss. This enables an inference procedure that generates multiple bytes in parallel per decoding step, substantially reducing the number of forward passes required to generate a sequence. Second, we propose two extensions inspired by speculative decoding that trade some of this speed for higher generation quality: BLT Self-speculation (BLT-S), in which BLT's local decoder continues generating past its normal patch boundaries to draft bytes, which are then verified with a single full-model forward pass; and BLT Diffusion+Verification (BLT-DV), which augments BLT-D with an autoregressive verification step after diffusion-based generation. All methods may achieve an estimated memory-bandwidth cost over 50% lower than BLT on generation tasks. Each approach offers its own unique advantages, together removing key barriers to the practical use of byte-level LMs.
匹配关键词: latent diffusion
---

[ACADEMIC - ARXIV]
标题: STARFlow2: Bridging Language Models and Normalizing Flows for Unified Multimodal Generation
作者: Ying Shen, Tianrong Chen, Yuan Gao, Yizhe Zhang, Yuyang Wang, Miguel Ángel Bautista, Shuangfei Zhai, Joshua M. Susskind, Jiatao Gu
链接: https://arxiv.org/abs/2605.08029v1
完整摘要: Deep generative models have advanced rapidly across text and vision, motivating unified multimodal systems that can understand, reason over, and generate interleaved text-image sequences. Most existing approaches combine autoregressive language modeling with diffusion-based image generators, inheriting a structural mismatch between causal text generation and iterative visual denoising. We observe that autoregressive normalizing flows are autoregressive Transformers--sharing the same causal mask, KV-cache mechanism, and left-to-right structure as LLMs--making them the most natural paradigm for true unified multimodal generation. We present STARFlow2, built on the Pretzel architecture that vertically interleaves a pretrained VLM stream with a TarFlow stream via residual skip connections, both operating under the same causal mask. Combined with a deep-shallow flow design and a unified FAE latent space, STARFlow2 enables cache-friendly interleaved generation where both text and visual outputs directly enter the KV-cache without re-encoding. Experiments demonstrate strong performance across image generation and multimodal understanding benchmarks, validating autoregressive flows as a viable foundation for unified multimodal modeling.
匹配关键词: multimodal
---

[ACADEMIC - ARXIV]
标题: SphereVAD: Training-Free Video Anomaly Detection via Geodesic Inference on the Unit Hypersphere
作者: Chao Huang, Penfei Wei, Wei Wang, Jie Wen, Zhihua Wang, Li Shen, Wenqi Ren, Xiaochun Cao
链接: https://arxiv.org/abs/2605.08003v1
完整摘要: Video anomaly detection (VAD) aims to automatically identify events that deviate from normal patterns in untrimmed surveillance videos. Existing methods universally depend on large-scale annotations or task-specific training procedures, severely limiting their rapid deployment to novel scenes. We observe that intermediate-layer features of pre-trained multimodal large language models (MLLMs) already encode rich anomaly semantics, yet existing approaches rely on the language output pathway and fail to exploit the geometric discriminability latent in these representations. Based on this finding, we propose SphereVAD, a fully training-free, zero-shot VAD framework that recasts anomaly discrimination as von Mises-Fisher (vMF) likelihood-ratio geodesic inference on the unit hypersphere, unleashing latent discriminability through principled geometric reasoning rather than learning new representations. Specifically, SphereVAD first applies Frechet mean centering to unfold feature distributions and eliminate domain biases, then employs Holistic Scene Attention (HSA) to reinforce feature consistency using cross-video priors, and finally performs vMF-guided Spherical Geodesic Pulling (SGP) to align ambiguous segments with directional prototypes on the spherical manifold. This training-free pipeline requires only minimal synthetic images for calibration. SphereVAD establishes new state-of-the-art results among training-free approaches on three major benchmarks and remains competitive with fully supervised baselines. Code will be available upon acceptance.
匹配关键词: multimodal
---

[ACADEMIC - ARXIV]
标题: Video Understanding Reward Modeling: A Robust Benchmark and Performant Reward Models
作者: Yuancheng Wei, Linli Yao, Lei Li, Haojie Zhang, Hao Zhou, Fandong Meng, Xu Sun
链接: https://arxiv.org/abs/2605.07872v1
完整摘要: Multimodal reward models have advanced substantially in text and image domains, yet progress in video understanding reward modeling remains severely limited by the lack of robust evaluation benchmarks and high-quality preference data. To address this, we propose a unified framework spanning benchmark design, data construction, and reward model training. We introduce Video Understanding Reward Bench (VURB), a benchmark featuring 2,100 preference pairs with long chain-of-thought reasoning traces (averaging 1,143 tokens) and majority voting evaluation across general, long, and reasoning-oriented video tasks. We further construct Video Understanding Preference Dataset (VUP-35K) via a fully automated pipeline, providing large-scale high-quality supervision for video reward training. Building on the data, we train VideoDRM and VideoGRM, a discriminative and a generative reward model, both achieving state-of-the-art performance on VURB and VideoRewardBench. Further analysis confirms that VUP-35K enhances both reward performance and model reasoning capability, while VideoDRM and VideoGRM yield significant gains under best-of-$N$ test-time scaling.
匹配关键词: multimodal
---

[ACADEMIC - ARXIV]
标题: EyeCue: Driver Cognitive Distraction Detection via Gaze-Empowered Egocentric Video Understanding
作者: Lang Zhang, JinYi Yoon, Matthew Corbett, Abhijit Sarkar, Bo Ji
链接: https://arxiv.org/abs/2605.07859v1
完整摘要: Driver cognitive distraction is a major cause of road collisions and remains difficult to detect. Unlike manual or visual distraction, cognitive distraction is diverted by thoughts unrelated to driving, even when the driver appears visually attentive and exhibits no explicit physical movements. In this work, we propose EyeCue, a gaze-empowered egocentric video understanding framework, to detect driver cognitive distraction. A key insight is that cognitive distraction manifests in the interaction between eye gaze and visual context. To capture this interaction, EyeCue integrates eye gaze with egocentric video to enable context-aware modeling of the driver's attention over time. Furthermore, to tackle the limited scale and diversity of existing datasets, we introduce CogDrive, a comprehensive multi-scenario dataset that augments four existing driving datasets with cognitive distraction annotations. Through extensive evaluations on CogDrive, we show that EyeCue achieves the highest accuracy of 74.38%, outperforming 11 baselines from 6 model families by over 7%. Notably, EyeCue can achieve an accuracy of over 70% across various driving scenarios (different road types, times of day, and weather conditions) with strong generalizability. These results highlight the importance of modeling gaze-context interactions and the effectiveness of cross-modal interaction modeling for multimodal cognitive distraction detection. Our codes and CogDrive dataset resources are available at https://github.com/langzhang2000/EyeCue.
匹配关键词: multimodal
---

[ACADEMIC - ARXIV]
标题: Anisotropic Modality Align
作者: Xiaomin Yu, Yijiang Li, Yuhui Zhang, Hanzhen Zhao, Yue Yang, Hao Tang, Yue Song, Xiaobin Hu, Chengwei Qin, Shuicheng Yan, Hui Xiong
链接: https://arxiv.org/abs/2605.07825v1
完整摘要: Training multimodal large language models has long been limited by the scarcity of high-quality paired multimodal data. Recent studies show that the shared representation space of pretrained multimodal contrastive models can serve as a bridge, enabling models to perform multimodal training with unimodal data. However, the key premise of this paradigm remains insufficiently understood: can representations from different modalities be reliably interchanged? The core obstacle lies in the persistent Modality Gap in the shared space. In this work, we revisit the geometric nature of the modality gap. We find that modality representations already share compatible dominant semantic geometry. What truly hinders modality interchangeability is not a simple global shift, but an anisotropic residual structure concentrated along a small number of dominant directions. Based on this finding, we further propose the principle of anisotropic modality gap alignment: effective modality alignment should align with the target-modality distribution while preserving the semantic structure of the source modality. Guided by this principle, we propose an anisotropic geometric correction framework, AnisoAlign, for unpaired modality alignment. This framework leverages the internal geometric prior of the target modality and performs bounded correction on source-modality representations, thereby constructing substitute representations in the target modality. Experiments confirm its benefits in both geometric diagnostics and text-only MLLM training. Overall, this work recasts the modality gap from an empirical observation into a correctable, structured geometric phenomenon and provides a new representation alignment perspective for training multimodal models with unimodal data.
匹配关键词: multimodal
---

[ACADEMIC - ARXIV]
标题: 123D: Unifying Multi-Modal Autonomous Driving Data at Scale
作者: Daniel Dauner, Valentin Charraut, Bastian Berle, Tianyu Li, Long Nguyen, Jiabao Wang, Changhui Jing, Maximilian Igl, Holger Caesar, Boris Ivanovic, Yiyi Liao, Andreas Geiger, Kashyap Chitta
链接: https://arxiv.org/abs/2605.08084v1
完整摘要: The pursuit of autonomous driving has produced one of the richest sensor data collections in all of robotics. However, its scale and diversity remain largely untapped. Each dataset adopts different 2D and 3D modalities, such as cameras, lidar, ego states, annotations, traffic lights, and HD maps, with different rates and synchronization schemes. They come in fragmented formats requiring complex dependencies that cannot natively coexist in the same development environment. Further, major inconsistencies in annotation conventions prevent training or measuring generalization across multiple datasets. We present 123D, an open-source framework that unifies such multi-modal driving data through a single API. To handle synchronization, we store each modality as an independent timestamped event stream with no prescribed rate, enabling synchronous or asynchronous access across arbitrary datasets. Using 123D, we consolidate eight real-world driving datasets spanning 3,300 hours and 90,000 kilometers, together with a synthetic dataset with configurable collection scripts, and provide tools for data analysis and visualization. We conduct a systematic study comparing annotation statistics and assessing each dataset's pose and calibration accuracy. Further, we showcase two applications 123D enables: cross-dataset 3D object detection transfer and reinforcement learning for planning, and offer recommendations for future directions. Code and documentation are available at https://github.com/kesai-labs/py123d.
匹配关键词: vision language model
---

[ACADEMIC - ARXIV]
标题: LLMs Improving LLMs: Agentic Discovery for Test-Time Scaling
作者: Tong Zheng, Haolin Liu, Chengsong Huang, Huiwen Bao, Sheng Zhang, Rui Liu, Runpeng Dai, Ruibo Chen, Chenxi Liu, Tianyi Xiong, Xidong Wu, Hongming Zhang, Heng Huang
链接: https://arxiv.org/abs/2605.08083v1
完整摘要: Test-time scaling (TTS) has become an effective approach for improving large language model performance by allocating additional computation during inference. However, existing TTS strategies are largely hand-crafted: researchers manually design reasoning patterns and tune heuristics by intuition, leaving much of the computation-allocation space unexplored. We propose an environment-driven framework, AutoTTS, that changes what researchers design: from individual TTS heuristics to environments where TTS strategies can be discovered automatically. The key to AutoTTS lies in environment construction: the discovery environment must make the control space tractable and provide cheap, frequent feedback for TTS search. As a concrete instantiation, we formulate width--depth TTS as controller synthesis over pre-collected reasoning trajectories and probe signals, where controllers decide when to branch, continue, probe, prune, or stop and can be evaluated cheaply without repeated LLM calls. We further introduce beta parameterization to make the search tractable and fine-grained execution trace feedback to improve discovery efficiency by helping the agent diagnose why a TTS program fails. Experiments on mathematical reasoning benchmarks show that the discovered strategies improve the overall accuracy--cost tradeoff over strong manually designed baselines. The discovered strategies generalize to held-out benchmarks and model scales, while the entire discovery costs only $39.9 and 160 minutes. Our data, and code will be open-source at https://github.com/zhengkid/AutoTTS.
匹配关键词: vision language model
---

[ACADEMIC - ARXIV]
标题: Normalizing Trajectory Models
作者: Jiatao Gu, Tianrong Chen, Ying Shen, David Berthelot, Shuangfei Zhai, Josh Susskind
链接: https://arxiv.org/abs/2605.08078v1
完整摘要: Diffusion-based models decompose sampling into many small Gaussian denoising steps -- an assumption that breaks down when generation is compressed to a few coarse transitions. Existing few-step methods address this through distillation, consistency training, or adversarial objectives, but sacrifice the likelihood framework in the process. We introduce Normalizing Trajectory Models (NTM), which models each reverse step as an expressive conditional normalizing flow with exact likelihood training. Architecturally, NTM combines shallow invertible blocks within each step with a deep parallel predictor across the trajectory, forming an end-to-end network trainable from scratch or initializable from pretrained flow-matching models. Its exact trajectory likelihood further enables self-distillation: a lightweight denoiser trained on the model's own score produces high-quality samples in four steps. On text-to-image benchmarks, NTM matches or outperforms strong image generation baselines in just four sampling steps while uniquely retaining exact likelihood over the generative trajectory.
匹配关键词: vision language model
---

[ACADEMIC - ARXIV]
标题: Conformal Path Reasoning: Trustworthy Knowledge Graph Question Answering via Path-Level Calibration
作者: Shuhang Lin, Chuhao Zhou, Xiao Lin, Zihan Dong, Kuan Lu, Zhencan Peng, Jie Yin, Dimitris N. Metaxas
链接: https://arxiv.org/abs/2605.08077v1
完整摘要: Knowledge Graph Question Answering (KGQA) has shown promise for grounded and interpretable reasoning, yet existing approaches often fail to provide reliable coverage guarantees over retrieved answers. While Conformal Prediction (CP) offers a principled framework for producing prediction sets with statistical guarantees, prior methods suffer from critical limitations in both calibration validity and score discriminability, resulting in violated coverage guarantees and excessively large prediction sets. To address these pitfalls, we propose Conformal Path Reasoning (CPR), a trustworthy KGQA framework with two key innovations. First, we perform query-level conformal calibration over path-level scores, preserving the exchangeability while generating path prediction sets. Second, we introduce the Residual Conformal Value Network (RCVNet), a lightweight module trained via PUCT-guided exploration to learn discriminative path-level nonconformity scores. Experiments on benchmarks show that CPR significantly improves the Empirical Coverage Rate by 34% while reducing average prediction set size by 40% compared to conformal baselines. These results validate the efficacy of CPR in satisfying coverage guarantees with substantially more compact answer sets.
匹配关键词: vision language model
---

[ACADEMIC - ARXIV]
标题: Zero-Shot Imagined Speech Decoding via Imagined-to-Listened MEG Mapping
作者: Maryam Maghsoudi, Shihab Shamma
链接: https://arxiv.org/abs/2605.08075v1
完整摘要: Decoding imagined speech from non-invasive brain recordings is challenging because imagined datasets are scarce and difficult to align temporally across subjects and sessions In this work, we propose a new approach to the decoding of imagined speech that leverages the richer and more reliably labeled recordings during listening to speech. We collected paired listened and imagined MEG recordings to rhythmic melodic and spoken stimuli from trained musicians. Using trained musicians helped improve temporal alignment across conditions. We then developed a three-stage decoding pipeline that revealed consistent and meaningful relationships between neural activity evoked by imagining and listening to the same stimuli. First, we trained six linear and neural models to map imagined MEG responses to listened responses. We evaluated these models against a null baseline from unseen subjects to validate that the predicted-listening responses preserve stimulus-specific information. In the second stage, we trained a contrastive word decoder exclusively on the listened MEG responses, and evaluated it using four embedding strategies including semantic, acoustic, and phonetic representations. In the third stage, we process the imagined MEG responses from held-out subjects through the mapping pipeline to compute the corresponding listening responses that are then decoded by the listened decoder. Using rank-based analysis, we show that the imagined words are decodable significantly above chance. We shall report here the results of a proof-of-concept implementation to decode imagined speech, where all evaluations are performed on held-out subjects. We also demonstrate that performance improves with training data size, suggesting that this approach is scalable and can directly be made applicable to realistic brain-computer interface scenarios.
匹配关键词: vision language model
---

[ACADEMIC - ARXIV]
标题: Proxy3D: Efficient 3D Representations for Vision-Language Models via Semantic Clustering and Alignment
作者: Jerry Jiang, Haowen Sun, Denis Gudovskiy, Yohei Nakata, Tomoyuki Okuno, Kurt Keutzer, Wenzhao Zheng
链接: https://arxiv.org/abs/2605.08064v1
完整摘要: Spatial intelligence in vision-language models (VLMs) attracts research interest with the practical demand to reason in the 3D world.Despite promising results, most existing methods follow the conventional 2D pipeline in VLMs and use pixel-aligned representations for the vision modality. However, correspondence-based models with implicit 3D scene understanding often fail to achieve spatial consistency, and representation-based models with 3D geometric priors lack efficiency in vision sequence serialization. To address this, we propose a Proxy3D method with compact yet comprehensive 3D proxy representations for the vision modality. Given only video frames as input, we employ semantic and geometric encoders to extract scene features and then perform their semantic-aware clustering to obtain a set of proxies in the 3D space. For representation alignment, we further curate the SpaceSpan dataset and apply multi-stage training to adopt the proposed 3D proxy representations with the VLM. When using shorter sequences for vision information, our method achieves competitive or state-of-the-art performance in 3D visual question answering, visual grounding and general spatial intelligence benchmarks.
匹配关键词: VLM
---

[ACADEMIC - ARXIV]
标题: Object Hallucination-Free Reinforcement Unlearning for Vision-Language Models
作者: Kaidi Jia, Yujie Lin, Chengyi Yang, Jiayao Ma, Jinsong Su
链接: https://arxiv.org/abs/2605.08031v1
完整摘要: Vision-language models (VLMs) raise growing concerns about privacy, copyright, and bias, motivating machine unlearning to remove sensitive knowledge. However, existing methods primarily fine-tune the language decoder, leading to superficial forgetting that fails to erase underlying visual representations and often introduces object hallucination. We propose HFRU, a reinforcement unlearning framework that operates on the vision encoder for deep semantic removal. Our two-stage approach combines alignment disruption with GRPO-based optimization using a composite reward, including an abstraction reward that encourages semantically valid substitutions and mitigates hallucinations. Experiments on object recognition and face identity tasks show that HFRU achieves over 98% forgetting and retention performance, while introducing negligible object hallucination, significantly outperforming prior methods.Our code and implementation details are available at https://github.com/XMUDeepLIT/HFRU.
匹配关键词: VLM
---

[ACADEMIC - ARXIV]
标题: STARFlow2: Bridging Language Models and Normalizing Flows for Unified Multimodal Generation
作者: Ying Shen, Tianrong Chen, Yuan Gao, Yizhe Zhang, Yuyang Wang, Miguel Ángel Bautista, Shuangfei Zhai, Joshua M. Susskind, Jiatao Gu
链接: https://arxiv.org/abs/2605.08029v1
完整摘要: Deep generative models have advanced rapidly across text and vision, motivating unified multimodal systems that can understand, reason over, and generate interleaved text-image sequences. Most existing approaches combine autoregressive language modeling with diffusion-based image generators, inheriting a structural mismatch between causal text generation and iterative visual denoising. We observe that autoregressive normalizing flows are autoregressive Transformers--sharing the same causal mask, KV-cache mechanism, and left-to-right structure as LLMs--making them the most natural paradigm for true unified multimodal generation. We present STARFlow2, built on the Pretzel architecture that vertically interleaves a pretrained VLM stream with a TarFlow stream via residual skip connections, both operating under the same causal mask. Combined with a deep-shallow flow design and a unified FAE latent space, STARFlow2 enables cache-friendly interleaved generation where both text and visual outputs directly enter the KV-cache without re-encoding. Experiments demonstrate strong performance across image generation and multimodal understanding benchmarks, validating autoregressive flows as a viable foundation for unified multimodal modeling.
匹配关键词: VLM
---

[ACADEMIC - ARXIV]
标题: MedVIGIL: Evaluating Trustworthy Medical VLMs Under Broken Visual Evidence
作者: Hanqi Jiang, Junhao Chen, Yi Pan, Lifeng Chen, Weihang You, Haozhen Gong, Ruiyu Yan, Jinglei Lv, Lin Zhao, Hui Ren, Quanzheng Li, Tianming Liu, Xiang Li
链接: https://arxiv.org/abs/2605.07919v1
完整摘要: Medical vision--language models (VLMs) are usually evaluated on intact image--question pairs, but trustworthy clinical use requires a stronger property: a model must recognise when the evidential basis for an answer has failed. We study this through silent failures under perturbed evidence, where a vision-required medical question is paired with a false premise, wording perturbation, knowledge-only rewrite, or ROI-corrupted image, yet the model returns a fluent non-refusal answer. We introduce medvigil, a 300-case evaluation suite drawn from four public medical VQA sources, supervised end to end by four board-certified radiologists: every gold answer, refusal option, candidate-answer set, paraphrase, false-premise trap, ROI box, and clinical risk tier is clinician-authored. Two attending radiologists annotate every case in parallel, a senior radiologist consolidates the released manifest, and a separate fourth radiologist independent of construction answers every probe to provide the human reference baseline. The release contains 2{,}556 MCQ probes, 240 counterfactual triplets, physician-adjudicated risk-tier and answerability flags, ROI boxes, and a paired open-ended variant. We report seven correctness-conditioned audit metrics that summarise into the medvigil Composite Score (MCS), and audit 16 vision-capable models plus two text-only baselines. The independent radiologist scores MCS 83.3 at silent-failure rate 5.8%, leaving a 14.1-point composite headroom above the strongest audited model (Claude Opus 4.7 at 69.2). The benchmark and evaluation harness are publicly released.
匹配关键词: VLM
---

[ACADEMIC - ARXIV]
标题: GazeVLM: Active Vision via Internal Attention Control for Multimodal Reasoning
作者: Brown Ebouky, Gabriele Carrino, Niccolo Avogaro, Christoph Studer, Andrea Bartezzaghi, Mattia Rigotti
链接: https://arxiv.org/abs/2605.07817v1
完整摘要: Human visual reasoning is governed by active vision, a process where metacognitive control drives top-down goal-directed attention, dynamically routing foveal focus toward task-relevant details while maintaining peripheral awareness of the global scene. In contrast, modern Vision-Language Models (VLMs) process visual information passively, relying on the static accumulation of massive token contexts that dilute spatial reasoning and induce linguistic hallucinations. Here we propose the following paradigm shift: GazeVLM, a multimodal architecture that internalizes this metacognitive oversight over its deployment of attention resources directly into the reasoning loop. By empowering the VLM to autonomously generate gaze tokens ($\texttt{ }$), GazeVLM establishes a top-down control mechanism over its own causal attention mask. The model dynamically dictates its focal intent, triggering a continuous suppression bias that dampens irrelevant visual features, implementing spatial selective attention and simulating foveal fixation. Once local reasoning concludes, the bias lifts, seamlessly restoring the global view. This architecture enables the model to fluidly transition between global spatial awareness and localized focal reasoning without relying on external agentic contraptions like cropping tools, or inflating the context window with additional visual tokens derived from localized visual patches. Trained with a bespoke Group Relative Policy Optimization (GRPO) procedure that rewards valid grounding, our 4B-parameter GazeVLM delivers strong high-resolution multimodal reasoning performance, surpassing state-of-the-art VLMs in its parameter class by nearly 4% and agentic multimodal pipelines built around thinking with images by more than 5% on HRBench-4k and HRBench-8k.
匹配关键词: VLM
---

[ACADEMIC - ARXIV]
标题: 123D: Unifying Multi-Modal Autonomous Driving Data at Scale
作者: Daniel Dauner, Valentin Charraut, Bastian Berle, Tianyu Li, Long Nguyen, Jiabao Wang, Changhui Jing, Maximilian Igl, Holger Caesar, Boris Ivanovic, Yiyi Liao, Andreas Geiger, Kashyap Chitta
链接: https://arxiv.org/abs/2605.08084v1
完整摘要: The pursuit of autonomous driving has produced one of the richest sensor data collections in all of robotics. However, its scale and diversity remain largely untapped. Each dataset adopts different 2D and 3D modalities, such as cameras, lidar, ego states, annotations, traffic lights, and HD maps, with different rates and synchronization schemes. They come in fragmented formats requiring complex dependencies that cannot natively coexist in the same development environment. Further, major inconsistencies in annotation conventions prevent training or measuring generalization across multiple datasets. We present 123D, an open-source framework that unifies such multi-modal driving data through a single API. To handle synchronization, we store each modality as an independent timestamped event stream with no prescribed rate, enabling synchronous or asynchronous access across arbitrary datasets. Using 123D, we consolidate eight real-world driving datasets spanning 3,300 hours and 90,000 kilometers, together with a synthetic dataset with configurable collection scripts, and provide tools for data analysis and visualization. We conduct a systematic study comparing annotation statistics and assessing each dataset's pose and calibration accuracy. Further, we showcase two applications 123D enables: cross-dataset 3D object detection transfer and reinforcement learning for planning, and offer recommendations for future directions. Code and documentation are available at https://github.com/kesai-labs/py123d.
匹配关键词: image generation
---

[ACADEMIC - ARXIV]
标题: LLMs Improving LLMs: Agentic Discovery for Test-Time Scaling
作者: Tong Zheng, Haolin Liu, Chengsong Huang, Huiwen Bao, Sheng Zhang, Rui Liu, Runpeng Dai, Ruibo Chen, Chenxi Liu, Tianyi Xiong, Xidong Wu, Hongming Zhang, Heng Huang
链接: https://arxiv.org/abs/2605.08083v1
完整摘要: Test-time scaling (TTS) has become an effective approach for improving large language model performance by allocating additional computation during inference. However, existing TTS strategies are largely hand-crafted: researchers manually design reasoning patterns and tune heuristics by intuition, leaving much of the computation-allocation space unexplored. We propose an environment-driven framework, AutoTTS, that changes what researchers design: from individual TTS heuristics to environments where TTS strategies can be discovered automatically. The key to AutoTTS lies in environment construction: the discovery environment must make the control space tractable and provide cheap, frequent feedback for TTS search. As a concrete instantiation, we formulate width--depth TTS as controller synthesis over pre-collected reasoning trajectories and probe signals, where controllers decide when to branch, continue, probe, prune, or stop and can be evaluated cheaply without repeated LLM calls. We further introduce beta parameterization to make the search tractable and fine-grained execution trace feedback to improve discovery efficiency by helping the agent diagnose why a TTS program fails. Experiments on mathematical reasoning benchmarks show that the discovered strategies improve the overall accuracy--cost tradeoff over strong manually designed baselines. The discovered strategies generalize to held-out benchmarks and model scales, while the entire discovery costs only $39.9 and 160 minutes. Our data, and code will be open-source at https://github.com/zhengkid/AutoTTS.
匹配关键词: image generation
---

[ACADEMIC - ARXIV]
标题: Normalizing Trajectory Models
作者: Jiatao Gu, Tianrong Chen, Ying Shen, David Berthelot, Shuangfei Zhai, Josh Susskind
链接: https://arxiv.org/abs/2605.08078v1
完整摘要: Diffusion-based models decompose sampling into many small Gaussian denoising steps -- an assumption that breaks down when generation is compressed to a few coarse transitions. Existing few-step methods address this through distillation, consistency training, or adversarial objectives, but sacrifice the likelihood framework in the process. We introduce Normalizing Trajectory Models (NTM), which models each reverse step as an expressive conditional normalizing flow with exact likelihood training. Architecturally, NTM combines shallow invertible blocks within each step with a deep parallel predictor across the trajectory, forming an end-to-end network trainable from scratch or initializable from pretrained flow-matching models. Its exact trajectory likelihood further enables self-distillation: a lightweight denoiser trained on the model's own score produces high-quality samples in four steps. On text-to-image benchmarks, NTM matches or outperforms strong image generation baselines in just four sampling steps while uniquely retaining exact likelihood over the generative trajectory.
匹配关键词: image generation
---

[ACADEMIC - ARXIV]
标题: Conformal Path Reasoning: Trustworthy Knowledge Graph Question Answering via Path-Level Calibration
作者: Shuhang Lin, Chuhao Zhou, Xiao Lin, Zihan Dong, Kuan Lu, Zhencan Peng, Jie Yin, Dimitris N. Metaxas
链接: https://arxiv.org/abs/2605.08077v1
完整摘要: Knowledge Graph Question Answering (KGQA) has shown promise for grounded and interpretable reasoning, yet existing approaches often fail to provide reliable coverage guarantees over retrieved answers. While Conformal Prediction (CP) offers a principled framework for producing prediction sets with statistical guarantees, prior methods suffer from critical limitations in both calibration validity and score discriminability, resulting in violated coverage guarantees and excessively large prediction sets. To address these pitfalls, we propose Conformal Path Reasoning (CPR), a trustworthy KGQA framework with two key innovations. First, we perform query-level conformal calibration over path-level scores, preserving the exchangeability while generating path prediction sets. Second, we introduce the Residual Conformal Value Network (RCVNet), a lightweight module trained via PUCT-guided exploration to learn discriminative path-level nonconformity scores. Experiments on benchmarks show that CPR significantly improves the Empirical Coverage Rate by 34% while reducing average prediction set size by 40% compared to conformal baselines. These results validate the efficacy of CPR in satisfying coverage guarantees with substantially more compact answer sets.
匹配关键词: image generation
---

[ACADEMIC - ARXIV]
标题: EmambaIR: Efficient Visual State Space Model for Event-guided Image Reconstruction
作者: Wei Yu, Yunhang Qian
链接: https://arxiv.org/abs/2605.08073v1
完整摘要: Recent event-based image reconstruction methods predominantly rely on Convolutional Neural Networks (CNNs) and Vision Transformers (ViTs) to process complementary event information. However, these architectures face fundamental limitations: CNNs often fail to capture global feature correlations, whereas ViTs incur quadratic computational complexity (e.g., $O(n^2)$), hindering their application in high-resolution scenarios. To address these bottlenecks, we introduce EmambaIR, an Efficient visual State Space Model designed for image reconstruction using spatially sparse and temporally continuous event streams. Our framework introduces two key components: the cross-modal Top-k Sparse Attention Module (TSAM) and the Gated State-Space Module (GSSM). TSAM efficiently performs pixel-level top-k sparse attention to guide cross-modal interactions, yielding rich yet sparse fusion features. Subsequently, GSSM utilizes a nonlinear gated unit to enhance the temporal representation of vanilla linear-complexity ($O(n)$) SSMs, effectively capturing global contextual dependencies without the typical computational overhead. Extensive experiments on six datasets across three diverse image reconstruction tasks - motion deblurring, deraining, and High Dynamic Range (HDR) enhancement - demonstrate that EmambaIR significantly outperforms state-of-the-art methods while offering substantial reductions in memory consumption and computational cost. The source code and data are publicly available at: https://github.com/YunhangWickert/EmambaIR
匹配关键词: image generation
---

[ACADEMIC - ARXIV]
标题: 123D: Unifying Multi-Modal Autonomous Driving Data at Scale
作者: Daniel Dauner, Valentin Charraut, Bastian Berle, Tianyu Li, Long Nguyen, Jiabao Wang, Changhui Jing, Maximilian Igl, Holger Caesar, Boris Ivanovic, Yiyi Liao, Andreas Geiger, Kashyap Chitta
链接: https://arxiv.org/abs/2605.08084v1
完整摘要: The pursuit of autonomous driving has produced one of the richest sensor data collections in all of robotics. However, its scale and diversity remain largely untapped. Each dataset adopts different 2D and 3D modalities, such as cameras, lidar, ego states, annotations, traffic lights, and HD maps, with different rates and synchronization schemes. They come in fragmented formats requiring complex dependencies that cannot natively coexist in the same development environment. Further, major inconsistencies in annotation conventions prevent training or measuring generalization across multiple datasets. We present 123D, an open-source framework that unifies such multi-modal driving data through a single API. To handle synchronization, we store each modality as an independent timestamped event stream with no prescribed rate, enabling synchronous or asynchronous access across arbitrary datasets. Using 123D, we consolidate eight real-world driving datasets spanning 3,300 hours and 90,000 kilometers, together with a synthetic dataset with configurable collection scripts, and provide tools for data analysis and visualization. We conduct a systematic study comparing annotation statistics and assessing each dataset's pose and calibration accuracy. Further, we showcase two applications 123D enables: cross-dataset 3D object detection transfer and reinforcement learning for planning, and offer recommendations for future directions. Code and documentation are available at https://github.com/kesai-labs/py123d.
匹配关键词: video generation
---

[ACADEMIC - ARXIV]
标题: LLMs Improving LLMs: Agentic Discovery for Test-Time Scaling
作者: Tong Zheng, Haolin Liu, Chengsong Huang, Huiwen Bao, Sheng Zhang, Rui Liu, Runpeng Dai, Ruibo Chen, Chenxi Liu, Tianyi Xiong, Xidong Wu, Hongming Zhang, Heng Huang
链接: https://arxiv.org/abs/2605.08083v1
完整摘要: Test-time scaling (TTS) has become an effective approach for improving large language model performance by allocating additional computation during inference. However, existing TTS strategies are largely hand-crafted: researchers manually design reasoning patterns and tune heuristics by intuition, leaving much of the computation-allocation space unexplored. We propose an environment-driven framework, AutoTTS, that changes what researchers design: from individual TTS heuristics to environments where TTS strategies can be discovered automatically. The key to AutoTTS lies in environment construction: the discovery environment must make the control space tractable and provide cheap, frequent feedback for TTS search. As a concrete instantiation, we formulate width--depth TTS as controller synthesis over pre-collected reasoning trajectories and probe signals, where controllers decide when to branch, continue, probe, prune, or stop and can be evaluated cheaply without repeated LLM calls. We further introduce beta parameterization to make the search tractable and fine-grained execution trace feedback to improve discovery efficiency by helping the agent diagnose why a TTS program fails. Experiments on mathematical reasoning benchmarks show that the discovered strategies improve the overall accuracy--cost tradeoff over strong manually designed baselines. The discovered strategies generalize to held-out benchmarks and model scales, while the entire discovery costs only $39.9 and 160 minutes. Our data, and code will be open-source at https://github.com/zhengkid/AutoTTS.
匹配关键词: video generation
---

[ACADEMIC - ARXIV]
标题: Normalizing Trajectory Models
作者: Jiatao Gu, Tianrong Chen, Ying Shen, David Berthelot, Shuangfei Zhai, Josh Susskind
链接: https://arxiv.org/abs/2605.08078v1
完整摘要: Diffusion-based models decompose sampling into many small Gaussian denoising steps -- an assumption that breaks down when generation is compressed to a few coarse transitions. Existing few-step methods address this through distillation, consistency training, or adversarial objectives, but sacrifice the likelihood framework in the process. We introduce Normalizing Trajectory Models (NTM), which models each reverse step as an expressive conditional normalizing flow with exact likelihood training. Architecturally, NTM combines shallow invertible blocks within each step with a deep parallel predictor across the trajectory, forming an end-to-end network trainable from scratch or initializable from pretrained flow-matching models. Its exact trajectory likelihood further enables self-distillation: a lightweight denoiser trained on the model's own score produces high-quality samples in four steps. On text-to-image benchmarks, NTM matches or outperforms strong image generation baselines in just four sampling steps while uniquely retaining exact likelihood over the generative trajectory.
匹配关键词: video generation
---

[ACADEMIC - ARXIV]
标题: Conformal Path Reasoning: Trustworthy Knowledge Graph Question Answering via Path-Level Calibration
作者: Shuhang Lin, Chuhao Zhou, Xiao Lin, Zihan Dong, Kuan Lu, Zhencan Peng, Jie Yin, Dimitris N. Metaxas
链接: https://arxiv.org/abs/2605.08077v1
完整摘要: Knowledge Graph Question Answering (KGQA) has shown promise for grounded and interpretable reasoning, yet existing approaches often fail to provide reliable coverage guarantees over retrieved answers. While Conformal Prediction (CP) offers a principled framework for producing prediction sets with statistical guarantees, prior methods suffer from critical limitations in both calibration validity and score discriminability, resulting in violated coverage guarantees and excessively large prediction sets. To address these pitfalls, we propose Conformal Path Reasoning (CPR), a trustworthy KGQA framework with two key innovations. First, we perform query-level conformal calibration over path-level scores, preserving the exchangeability while generating path prediction sets. Second, we introduce the Residual Conformal Value Network (RCVNet), a lightweight module trained via PUCT-guided exploration to learn discriminative path-level nonconformity scores. Experiments on benchmarks show that CPR significantly improves the Empirical Coverage Rate by 34% while reducing average prediction set size by 40% compared to conformal baselines. These results validate the efficacy of CPR in satisfying coverage guarantees with substantially more compact answer sets.
匹配关键词: video generation
---

[ACADEMIC - ARXIV]
标题: Proxy3D: Efficient 3D Representations for Vision-Language Models via Semantic Clustering and Alignment
作者: Jerry Jiang, Haowen Sun, Denis Gudovskiy, Yohei Nakata, Tomoyuki Okuno, Kurt Keutzer, Wenzhao Zheng
链接: https://arxiv.org/abs/2605.08064v1
完整摘要: Spatial intelligence in vision-language models (VLMs) attracts research interest with the practical demand to reason in the 3D world.Despite promising results, most existing methods follow the conventional 2D pipeline in VLMs and use pixel-aligned representations for the vision modality. However, correspondence-based models with implicit 3D scene understanding often fail to achieve spatial consistency, and representation-based models with 3D geometric priors lack efficiency in vision sequence serialization. To address this, we propose a Proxy3D method with compact yet comprehensive 3D proxy representations for the vision modality. Given only video frames as input, we employ semantic and geometric encoders to extract scene features and then perform their semantic-aware clustering to obtain a set of proxies in the 3D space. For representation alignment, we further curate the SpaceSpan dataset and apply multi-stage training to adopt the proposed 3D proxy representations with the VLM. When using shorter sequences for vision information, our method achieves competitive or state-of-the-art performance in 3D visual question answering, visual grounding and general spatial intelligence benchmarks.
匹配关键词: video generation
---

[ACADEMIC - ARXIV]
标题: 123D: Unifying Multi-Modal Autonomous Driving Data at Scale
作者: Daniel Dauner, Valentin Charraut, Bastian Berle, Tianyu Li, Long Nguyen, Jiabao Wang, Changhui Jing, Maximilian Igl, Holger Caesar, Boris Ivanovic, Yiyi Liao, Andreas Geiger, Kashyap Chitta
链接: https://arxiv.org/abs/2605.08084v1
完整摘要: The pursuit of autonomous driving has produced one of the richest sensor data collections in all of robotics. However, its scale and diversity remain largely untapped. Each dataset adopts different 2D and 3D modalities, such as cameras, lidar, ego states, annotations, traffic lights, and HD maps, with different rates and synchronization schemes. They come in fragmented formats requiring complex dependencies that cannot natively coexist in the same development environment. Further, major inconsistencies in annotation conventions prevent training or measuring generalization across multiple datasets. We present 123D, an open-source framework that unifies such multi-modal driving data through a single API. To handle synchronization, we store each modality as an independent timestamped event stream with no prescribed rate, enabling synchronous or asynchronous access across arbitrary datasets. Using 123D, we consolidate eight real-world driving datasets spanning 3,300 hours and 90,000 kilometers, together with a synthetic dataset with configurable collection scripts, and provide tools for data analysis and visualization. We conduct a systematic study comparing annotation statistics and assessing each dataset's pose and calibration accuracy. Further, we showcase two applications 123D enables: cross-dataset 3D object detection transfer and reinforcement learning for planning, and offer recommendations for future directions. Code and documentation are available at https://github.com/kesai-labs/py123d.
匹配关键词: visual reasoning
---

[ACADEMIC - ARXIV]
标题: LLMs Improving LLMs: Agentic Discovery for Test-Time Scaling
作者: Tong Zheng, Haolin Liu, Chengsong Huang, Huiwen Bao, Sheng Zhang, Rui Liu, Runpeng Dai, Ruibo Chen, Chenxi Liu, Tianyi Xiong, Xidong Wu, Hongming Zhang, Heng Huang
链接: https://arxiv.org/abs/2605.08083v1
完整摘要: Test-time scaling (TTS) has become an effective approach for improving large language model performance by allocating additional computation during inference. However, existing TTS strategies are largely hand-crafted: researchers manually design reasoning patterns and tune heuristics by intuition, leaving much of the computation-allocation space unexplored. We propose an environment-driven framework, AutoTTS, that changes what researchers design: from individual TTS heuristics to environments where TTS strategies can be discovered automatically. The key to AutoTTS lies in environment construction: the discovery environment must make the control space tractable and provide cheap, frequent feedback for TTS search. As a concrete instantiation, we formulate width--depth TTS as controller synthesis over pre-collected reasoning trajectories and probe signals, where controllers decide when to branch, continue, probe, prune, or stop and can be evaluated cheaply without repeated LLM calls. We further introduce beta parameterization to make the search tractable and fine-grained execution trace feedback to improve discovery efficiency by helping the agent diagnose why a TTS program fails. Experiments on mathematical reasoning benchmarks show that the discovered strategies improve the overall accuracy--cost tradeoff over strong manually designed baselines. The discovered strategies generalize to held-out benchmarks and model scales, while the entire discovery costs only $39.9 and 160 minutes. Our data, and code will be open-source at https://github.com/zhengkid/AutoTTS.
匹配关键词: visual reasoning
---

[ACADEMIC - ARXIV]
标题: Conformal Path Reasoning: Trustworthy Knowledge Graph Question Answering via Path-Level Calibration
作者: Shuhang Lin, Chuhao Zhou, Xiao Lin, Zihan Dong, Kuan Lu, Zhencan Peng, Jie Yin, Dimitris N. Metaxas
链接: https://arxiv.org/abs/2605.08077v1
完整摘要: Knowledge Graph Question Answering (KGQA) has shown promise for grounded and interpretable reasoning, yet existing approaches often fail to provide reliable coverage guarantees over retrieved answers. While Conformal Prediction (CP) offers a principled framework for producing prediction sets with statistical guarantees, prior methods suffer from critical limitations in both calibration validity and score discriminability, resulting in violated coverage guarantees and excessively large prediction sets. To address these pitfalls, we propose Conformal Path Reasoning (CPR), a trustworthy KGQA framework with two key innovations. First, we perform query-level conformal calibration over path-level scores, preserving the exchangeability while generating path prediction sets. Second, we introduce the Residual Conformal Value Network (RCVNet), a lightweight module trained via PUCT-guided exploration to learn discriminative path-level nonconformity scores. Experiments on benchmarks show that CPR significantly improves the Empirical Coverage Rate by 34% while reducing average prediction set size by 40% compared to conformal baselines. These results validate the efficacy of CPR in satisfying coverage guarantees with substantially more compact answer sets.
匹配关键词: visual reasoning
---

[ACADEMIC - ARXIV]
标题: EmambaIR: Efficient Visual State Space Model for Event-guided Image Reconstruction
作者: Wei Yu, Yunhang Qian
链接: https://arxiv.org/abs/2605.08073v1
完整摘要: Recent event-based image reconstruction methods predominantly rely on Convolutional Neural Networks (CNNs) and Vision Transformers (ViTs) to process complementary event information. However, these architectures face fundamental limitations: CNNs often fail to capture global feature correlations, whereas ViTs incur quadratic computational complexity (e.g., $O(n^2)$), hindering their application in high-resolution scenarios. To address these bottlenecks, we introduce EmambaIR, an Efficient visual State Space Model designed for image reconstruction using spatially sparse and temporally continuous event streams. Our framework introduces two key components: the cross-modal Top-k Sparse Attention Module (TSAM) and the Gated State-Space Module (GSSM). TSAM efficiently performs pixel-level top-k sparse attention to guide cross-modal interactions, yielding rich yet sparse fusion features. Subsequently, GSSM utilizes a nonlinear gated unit to enhance the temporal representation of vanilla linear-complexity ($O(n)$) SSMs, effectively capturing global contextual dependencies without the typical computational overhead. Extensive experiments on six datasets across three diverse image reconstruction tasks - motion deblurring, deraining, and High Dynamic Range (HDR) enhancement - demonstrate that EmambaIR significantly outperforms state-of-the-art methods while offering substantial reductions in memory consumption and computational cost. The source code and data are publicly available at: https://github.com/YunhangWickert/EmambaIR
匹配关键词: visual reasoning
---

[ACADEMIC - ARXIV]
标题: VecCISC: Improving Confidence-Informed Self-Consistency with Reasoning Trace Clustering and Candidate Answer Selection
作者: James Petullo, Sonny George, Dylan Cashman, Nianwen Xue
链接: https://arxiv.org/abs/2605.08070v1
完整摘要: A standard technique for scaling inference-time reasoning is Self-Consistency, whereby multiple candidate answers are sampled from an LLM and the most common answer is selected. More recently, it has been shown that weighted majority voting (e.g. Confidence-Informed Self Consistency (CISC)), which assigns a confidence value to each candidate answer and chooses the answer with the largest accumulated score, tends to be more accurate on a wide range of popular benchmarks. In practice, weighted majority voting necessitates calling a critic LLM on each candidate's reasoning trace to produce the answer's confidence score. This secondary series of LLM calls greatly increases the overhead and cost of weighted majority voting, despite its potential performance benefits. To reduce this expense, we propose VecCISC, a lightweight, adaptive framework that uses a measure of semantic similarity to filter reasoning traces that are semantically equivalent to others, degenerate, or hallucinated, thus decreasing the number of candidate answers that must be evaluated by the critic. To ensure adequate experimental thoroughness, we evaluate VecCISC on five challenging, widely-adopted datasets spanning the domains of mathematics, chemistry, biology, commonsense reasoning, and the humanities. Our results demonstrate that VecCISC reduces the total token usage by 47%, while maintaining or exceeding the accuracy of CISC.
匹配关键词: visual reasoning
---

[ACADEMIC - ARXIV]
标题: MPD$^2$-Router: Mask-aware Multi-expert Prior-regularized Dual-head Deferral Router in Glaucoma Screening and Diagnosis
作者: Wenxin Zhan
链接: https://arxiv.org/abs/2605.08024v1
完整摘要: Learning-to-defer (L2D) can make glaucoma screening safer by routing difficult/uncertain cases to humans, yet standard formulations overlook expert availability, heterogeneous readers behavior, workload imbalance, asymmetric diagnostic harm, case difficulty from morphology and deployment shift. We introduce MPD$^2$-Router, a mask-aware multi-expert deferral framework that recasts ophthalmic triage as constrained human--AI routing: whether to defer and to which available expert. It couples a dual-head deferral/allocation policy with mask-aware Gumbel--sigmoid gating that strictly enforces per-sample availability, and fuses uncertainty, morphology, image-quality, and OOD signals. Training uses an asymmetric cost-sensitive objective with an augmented-Lagrangian deferral budget, a group-specific distribution prior, and a rank-majorization JS regularizer that jointly prevent expert collapse without forcing uniform allocation. Across three cross-national glaucoma cohorts (REFUGE, CHAKSU, ORIGA) with a frozen REFUGE-trained backbone, MPD$^2$-Router substantially lowers clinical cost and improves MCC over AI-only at a moderate deferral rate. It is Pareto-optimal in F1--MCC--cost, robust under cross-domain shift, and yields balanced expert utilization.
匹配关键词: embodied AI
---

[ACADEMIC - ARXIV]
标题: Active Embodiment Identification with Reinforcement Learning for Legged Robots
作者: Nico Bohlinger, Jan Peters
链接: https://arxiv.org/abs/2605.08020v1
完整摘要: We present an active embodiment identification method for legged robots that jointly learns information-seeking behavior and explicit embodiment prediction. Using a history-augmented URMA architecture, the method infers joint-level and global embodiment parameters through interaction with the environment in simulation across different morphologies.
匹配关键词: embodied AI
---

[ACADEMIC - ARXIV]
标题: Reason to Play: Behavioral and Brain Alignment Between Frontier LRMs and Human Game Learners
作者: Botos Csaba, Sreejan Kumar, Austin Tudor David Andrews, Laurence Hunt, Chris Summerfield, Joshua B. Tenenbaum, Rui Ponte Costa, Marcelo G. Mattar, Momchil Tomov
链接: https://arxiv.org/abs/2605.08019v1
完整摘要: Humans rapidly learn abstract knowledge when encountering novel environments and flexibly deploy this knowledge to guide efficient and intelligent action. Can modern AI systems learn and plan in a similar way? We study this question using a dataset of complex human gameplay with concurrent fMRI recordings, in which participants learn novel video games that require rule discovery, hypothesis revision, and multi-step planning. We jointly evaluate models by their ability to play the games, match human learning behavior, and predict brain activity during the same task, comparing a suite of frontier Large Reasoning Models (LRMs) against model-free and model-based deep reinforcement learning agents and a Bayesian theory-based agent. We find that frontier LRMs most closely match human behavioral patterns during game discovery and predict brain activity an order of magnitude better than both reinforcement learning alternatives across cortical and subcortical regions, with effects robust to permutation controls. Through targeted manipulations, we further show that brain alignment reflects the model's in-context representation of the game state rather than its downstream planning or reasoning. Our results establish LRMs as compelling computational accounts of human learning and decision making in complex, naturalistic environments. Project page with interactive replays: https://botcs.github.io/reason-to-play/
匹配关键词: embodied AI
---

[ACADEMIC - ARXIV]
标题: Towards Apples to Apples for AI Evaluations: From Real-World Use Cases to Evaluation Scenarios
作者: Yee-Yin Choong, Kristen Greene, Alice Qian, Meryem Marasli, Ziqi Yang, Sophia Chen, Laura Dabbish, Anand Rao, Hong Shen
链接: https://arxiv.org/abs/2605.07986v1
完整摘要: AI measurement science has a wide variety of methodologies and measurements for comparing AI systems, resulting in what often appear to be "apples-to-oranges" comparisons across AI evaluations. To move toward "apples-to-apples" comparisons in real-world AI evaluations, this work advocates for methodological transparency in evaluation scenarios, operational grounding, and human-centered design (HCD) principles. We propose a repeatable process for transforming high-level use cases to detailed scenarios by eliciting use cases from subject matter experts (SMEs) via a structured AI Use Case Worksheet with six key elements: use case, sector, user (direct and indirect), intended outcomes, expected impacts (positive and negative), and KPIs and metrics. We demonstrate utility of the worksheet and process in the U.S. financial services sector. This paper reports on example high-level AI use cases identified by financial services sector SMEs: cyber defense enablement, developer productivity, financial crime aggregation, suspicious activity report (SAR) filing, credit memo generation, and internal call center support. These AI use cases provided are illustrative of the process and not exhaustive. Central to our work is a three-stage expansion pipeline combining LLM prompting with human reviews to generate 107 scenarios from those use cases elicited from SMEs. This process integrates iterative human reviews at every juncture to ensure operational grounding: for scenario titles and descriptions; for core scenario elements like users, benefits and risks, and metrics; and for scenario narratives and evaluation objectives. Human checkpoints ensure scenarios remain reflective of real-world usage and human needs. We describe a validation rubric to assess scenario quality. By defining key scenario components, this work supports a more consistent and meaningful paradigm for human-centered AI evaluations.
匹配关键词: embodied AI
---

[ACADEMIC - ARXIV]
标题: GLiGuard: Schema-Conditioned Classification for LLM Safeguard
作者: Urchade Zaratiana, Mary Newhauser, George Hurn-Maloney, Ash Lewis
链接: https://arxiv.org/abs/2605.07982v1
完整摘要: Ensuring safe, policy-compliant outputs from large language models requires real-time content moderation that can scale across multiple safety dimensions. However, state-of-the-art guardrail models rely on autoregressive decoders with 7B--27B parameters, reformulating what is fundamentally a classification problem as sequential text generation, a design choice that incurs high latency and scales poorly to multi-aspect evaluation. In this work, we introduce \textbf{GLiGuard}, a 0.3B-parameter schema-conditioned bidirectional encoder adapted from GLiNER2 for LLM content moderation. The key idea is to encode task definitions and label semantics directly into the input sequence as structured token schemas, enabling simultaneous evaluation of prompt safety, response safety, refusal detection, 14 fine-grained harm categories, and 11 jailbreak strategies in a single non-autoregressive forward pass. This schema-conditioned design lets supported task and label blocks be composed directly in the input schema at inference time. Across nine established safety benchmarks, GLiGuard achieves F1 scores competitive with 7B--27B decoder-based guards despite being 23--90$\times$ smaller, while delivering up to 16$\times$ higher throughput and 17$\times$ lower latency. These results suggest that compact bidirectional encoders can approach the accuracy of much larger guard models while drastically reducing inference cost. Code and models are available at https://github.com/fastino-ai/GLiGuard.
匹配关键词: embodied AI
---

[ACADEMIC - ARXIV]
标题: 123D: Unifying Multi-Modal Autonomous Driving Data at Scale
作者: Daniel Dauner, Valentin Charraut, Bastian Berle, Tianyu Li, Long Nguyen, Jiabao Wang, Changhui Jing, Maximilian Igl, Holger Caesar, Boris Ivanovic, Yiyi Liao, Andreas Geiger, Kashyap Chitta
链接: https://arxiv.org/abs/2605.08084v1
完整摘要: The pursuit of autonomous driving has produced one of the richest sensor data collections in all of robotics. However, its scale and diversity remain largely untapped. Each dataset adopts different 2D and 3D modalities, such as cameras, lidar, ego states, annotations, traffic lights, and HD maps, with different rates and synchronization schemes. They come in fragmented formats requiring complex dependencies that cannot natively coexist in the same development environment. Further, major inconsistencies in annotation conventions prevent training or measuring generalization across multiple datasets. We present 123D, an open-source framework that unifies such multi-modal driving data through a single API. To handle synchronization, we store each modality as an independent timestamped event stream with no prescribed rate, enabling synchronous or asynchronous access across arbitrary datasets. Using 123D, we consolidate eight real-world driving datasets spanning 3,300 hours and 90,000 kilometers, together with a synthetic dataset with configurable collection scripts, and provide tools for data analysis and visualization. We conduct a systematic study comparing annotation statistics and assessing each dataset's pose and calibration accuracy. Further, we showcase two applications 123D enables: cross-dataset 3D object detection transfer and reinforcement learning for planning, and offer recommendations for future directions. Code and documentation are available at https://github.com/kesai-labs/py123d.
匹配关键词: robotics
---

[ACADEMIC - ARXIV]
标题: 6D Pose Estimation via Keypoint Heatmap Regression with RGB-D Residual Neural Networks
作者: Ismail Aljosevic, Amir Masoud Almasi, Ana Parovic, Ashkan Shafiei
链接: https://arxiv.org/abs/2605.08059v1
完整摘要: In this paper, we propose a modular framework for 6D pose estimation based on keypoint heatmap regression. Our approach combines YOLOv10m for object detection with a ResNet18-based network that predicts 2D heatmaps from RGB images. Keypoints extracted from these heatmaps are used to estimate the 6D object pose via the PnP RANSAC algorithm. We compare different keypoint selection strategies to assess their impact on pose accuracy. Additionally, we extend the baseline by incorporating depth data using a cross-fusion architecture, which enables interaction between RGB and depth features at multiple stages. We further explore general training improvements, such as experimenting with activation functions and learning rate scheduling strategies to improve model performance. Our best RGB-only model achieved a mean ADD-based accuracy of 84.50%, while the RGB-D fusion model reached 92.41% on the LINEMOD dataset. The code is available at https://github.com/ameermasood/HeatNet.
匹配关键词: robotics
---

[ACADEMIC - ARXIV]
标题: Active Embodiment Identification with Reinforcement Learning for Legged Robots
作者: Nico Bohlinger, Jan Peters
链接: https://arxiv.org/abs/2605.08020v1
完整摘要: We present an active embodiment identification method for legged robots that jointly learns information-seeking behavior and explicit embodiment prediction. Using a history-augmented URMA architecture, the method infers joint-level and global embodiment parameters through interaction with the environment in simulation across different morphologies.
匹配关键词: robotics
---

[ACADEMIC - ARXIV]
标题: Evaluation of an Actuated Spine in Agile Quadruped Locomotion
作者: Nico Bohlinger, Piotr Kicki, Davide Tateo, Krzysztof Walas, Jan Peters
链接: https://arxiv.org/abs/2605.07988v1
完整摘要: The spine plays a crucial role in the dynamic locomotion of quadrupedal animals, improving the stability, speed, and efficiency of their gait, especially for fast-paced and highly agile movements. Therefore, the spine is also a promising and natural way to extend the capabilities of quadruped robots. This paper empirically investigates the benefits of an actuated spine for learning agile quadruped locomotion. We evaluate whether the use of the spine brings benefits in terms of high-speed running, climbing stairs, climbing high-angle slopes, hurdling, and crawling scenarios. We conducted an empirical study in MuJoCo simulation using the Silver Badger robot from MAB Robotics with an actuated 1-DOF spine in the sagittal plane. The obtained results show that the use of the spine provides the robot with increased agility and allows it to overcome higher stairs, steeper slopes, higher obstacles, and smaller passages.
匹配关键词: robotics
---

[ACADEMIC - ARXIV]
标题: TAVIS: A Benchmark for Egocentric Active Vision and Anticipatory Gaze in Imitation Learning
作者: Giacomo Spigler
链接: https://arxiv.org/abs/2605.07943v1
完整摘要: Active vision -- where a policy controls its own gaze during manipulation -- has emerged as a key capability for imitation learning, with multiple independent systems demonstrating its benefits in the past year. Yet there is no shared benchmark to compare approaches or quantify what active vision contributes, on which task types, and under what conditions. We introduce TAVIS, evaluation infrastructure for active-vision imitation learning, with two complementary task suites -- TAVIS-Head (5 tasks, global search via pan/tilt necks) and TAVIS-Hands (3 tasks, local occlusion via wrist cameras) -- on two humanoid torso embodiments (GR1T2, Reachy2), built on IsaacLab. TAVIS provides three evaluation primitives: a paired headcam-vs-fixedcam protocol on identical demonstrations; GALT (Gaze-Action Lead Time), a novel metric grounded in cognitive science and HRI that quantifies anticipatory gaze in learned policies; and procedural ID/OOD splits. Baseline experiments with Diffusion Policy and $π_0$ reveal that (i) active-vision generally helps, but benefits are task-conditional rather than uniform; (ii) multi-task policies degrade sharply under controlled distribution shifts on both suites; and (iii) imitation alone yields anticipatory gaze, with median lead times comparable to the human teleoperator reference. Code, evaluation scripts, demonstrations (LeRobot v3.0; ~2200 episodes) and trained baselines are released at https://github.com/spiglerg/tavis and https://huggingface.co/tavis-benchmark.
匹配关键词: robotics
---

[ACADEMIC - ARXIV]
标题: 123D: Unifying Multi-Modal Autonomous Driving Data at Scale
作者: Daniel Dauner, Valentin Charraut, Bastian Berle, Tianyu Li, Long Nguyen, Jiabao Wang, Changhui Jing, Maximilian Igl, Holger Caesar, Boris Ivanovic, Yiyi Liao, Andreas Geiger, Kashyap Chitta
链接: https://arxiv.org/abs/2605.08084v1
完整摘要: The pursuit of autonomous driving has produced one of the richest sensor data collections in all of robotics. However, its scale and diversity remain largely untapped. Each dataset adopts different 2D and 3D modalities, such as cameras, lidar, ego states, annotations, traffic lights, and HD maps, with different rates and synchronization schemes. They come in fragmented formats requiring complex dependencies that cannot natively coexist in the same development environment. Further, major inconsistencies in annotation conventions prevent training or measuring generalization across multiple datasets. We present 123D, an open-source framework that unifies such multi-modal driving data through a single API. To handle synchronization, we store each modality as an independent timestamped event stream with no prescribed rate, enabling synchronous or asynchronous access across arbitrary datasets. Using 123D, we consolidate eight real-world driving datasets spanning 3,300 hours and 90,000 kilometers, together with a synthetic dataset with configurable collection scripts, and provide tools for data analysis and visualization. We conduct a systematic study comparing annotation statistics and assessing each dataset's pose and calibration accuracy. Further, we showcase two applications 123D enables: cross-dataset 3D object detection transfer and reinforcement learning for planning, and offer recommendations for future directions. Code and documentation are available at https://github.com/kesai-labs/py123d.
匹配关键词: humanoid robot
---

[ACADEMIC - ARXIV]
标题: Active Embodiment Identification with Reinforcement Learning for Legged Robots
作者: Nico Bohlinger, Jan Peters
链接: https://arxiv.org/abs/2605.08020v1
完整摘要: We present an active embodiment identification method for legged robots that jointly learns information-seeking behavior and explicit embodiment prediction. Using a history-augmented URMA architecture, the method infers joint-level and global embodiment parameters through interaction with the environment in simulation across different morphologies.
匹配关键词: humanoid robot
---

[ACADEMIC - ARXIV]
标题: Evaluation of an Actuated Spine in Agile Quadruped Locomotion
作者: Nico Bohlinger, Piotr Kicki, Davide Tateo, Krzysztof Walas, Jan Peters
链接: https://arxiv.org/abs/2605.07988v1
完整摘要: The spine plays a crucial role in the dynamic locomotion of quadrupedal animals, improving the stability, speed, and efficiency of their gait, especially for fast-paced and highly agile movements. Therefore, the spine is also a promising and natural way to extend the capabilities of quadruped robots. This paper empirically investigates the benefits of an actuated spine for learning agile quadruped locomotion. We evaluate whether the use of the spine brings benefits in terms of high-speed running, climbing stairs, climbing high-angle slopes, hurdling, and crawling scenarios. We conducted an empirical study in MuJoCo simulation using the Silver Badger robot from MAB Robotics with an actuated 1-DOF spine in the sagittal plane. The obtained results show that the use of the spine provides the robot with increased agility and allows it to overcome higher stairs, steeper slopes, higher obstacles, and smaller passages.
匹配关键词: humanoid robot
---

[ACADEMIC - ARXIV]
标题: TAVIS: A Benchmark for Egocentric Active Vision and Anticipatory Gaze in Imitation Learning
作者: Giacomo Spigler
链接: https://arxiv.org/abs/2605.07943v1
完整摘要: Active vision -- where a policy controls its own gaze during manipulation -- has emerged as a key capability for imitation learning, with multiple independent systems demonstrating its benefits in the past year. Yet there is no shared benchmark to compare approaches or quantify what active vision contributes, on which task types, and under what conditions. We introduce TAVIS, evaluation infrastructure for active-vision imitation learning, with two complementary task suites -- TAVIS-Head (5 tasks, global search via pan/tilt necks) and TAVIS-Hands (3 tasks, local occlusion via wrist cameras) -- on two humanoid torso embodiments (GR1T2, Reachy2), built on IsaacLab. TAVIS provides three evaluation primitives: a paired headcam-vs-fixedcam protocol on identical demonstrations; GALT (Gaze-Action Lead Time), a novel metric grounded in cognitive science and HRI that quantifies anticipatory gaze in learned policies; and procedural ID/OOD splits. Baseline experiments with Diffusion Policy and $π_0$ reveal that (i) active-vision generally helps, but benefits are task-conditional rather than uniform; (ii) multi-task policies degrade sharply under controlled distribution shifts on both suites; and (iii) imitation alone yields anticipatory gaze, with median lead times comparable to the human teleoperator reference. Code, evaluation scripts, demonstrations (LeRobot v3.0; ~2200 episodes) and trained baselines are released at https://github.com/spiglerg/tavis and https://huggingface.co/tavis-benchmark.
匹配关键词: humanoid robot
---

[ACADEMIC - ARXIV]
标题: Melding LLM and temporal logic for reliable human-swarm collaboration in complex scenarios
作者: Junfeng Chen, Yuxiao Zhu, An Zhuo, Xintong Zhang, Shuo Zhang, Guanghui Wen, Xiwang Dong, Meng Guo, Zhongkui Li
链接: https://arxiv.org/abs/2605.07877v1
完整摘要: Robot swarms promise scalable assistance in complex and hazardous environments. Task planning lies at the core of human-swarm collaboration, translating the operator's intent into coordinated swarm actions and helping determine when validation or intervention is required during execution. In long-horizon missions under dynamic scenarios, however, reliable task planning becomes difficult to maintain: emerging events and changing conditions demand continual adaptation, and sustained operator oversight imposes substantial cognitive burden. Existing LLM-based planning tools can support plan generation, yet they remain susceptible to invalid task orderings and infeasible robot actions, resulting in frequent manual adjustment. Here we introduce a neuro-symbolic framework for long-horizon human-swarm collaboration that tightly melds verifiable task planning with context-grounded LLM reasoning. We formalize mission goals and operational rules as temporal logic formulas and admissible task orderings as task automata. Conditioned on these formal constraints and live perceptual context, LLMs generate executable subtask sequences that satisfy mission rules and remain grounded in the current scene. An uncertainty-aware scheduler then assigns subtasks across the heterogeneous swarm to maximize parallelisms while remaining resilient to disruptions. An event-triggered interaction protocol further limits operator involvement to sparse, high-level confirmation and guidance. Deployment on a heterogeneous robotic fleet yields similar results while remaining robust to hardware-specific actuation and communication uncertainties. Together, these results support a formal and scalable paradigm for reliable and low-overhead human-swarm collaboration in dynamic environments
匹配关键词: humanoid robot
---

[ACADEMIC - ARXIV]
标题: Reason to Play: Behavioral and Brain Alignment Between Frontier LRMs and Human Game Learners
作者: Botos Csaba, Sreejan Kumar, Austin Tudor David Andrews, Laurence Hunt, Chris Summerfield, Joshua B. Tenenbaum, Rui Ponte Costa, Marcelo G. Mattar, Momchil Tomov
链接: https://arxiv.org/abs/2605.08019v1
完整摘要: Humans rapidly learn abstract knowledge when encountering novel environments and flexibly deploy this knowledge to guide efficient and intelligent action. Can modern AI systems learn and plan in a similar way? We study this question using a dataset of complex human gameplay with concurrent fMRI recordings, in which participants learn novel video games that require rule discovery, hypothesis revision, and multi-step planning. We jointly evaluate models by their ability to play the games, match human learning behavior, and predict brain activity during the same task, comparing a suite of frontier Large Reasoning Models (LRMs) against model-free and model-based deep reinforcement learning agents and a Bayesian theory-based agent. We find that frontier LRMs most closely match human behavioral patterns during game discovery and predict brain activity an order of magnitude better than both reinforcement learning alternatives across cortical and subcortical regions, with effects robust to permutation controls. Through targeted manipulations, we further show that brain alignment reflects the model's in-context representation of the game state rather than its downstream planning or reasoning. Our results establish LRMs as compelling computational accounts of human learning and decision making in complex, naturalistic environments. Project page with interactive replays: https://botcs.github.io/reason-to-play/
匹配关键词: manipulation
---

[ACADEMIC - ARXIV]
标题: Graph Representation Learning Augmented Model Manipulation on Federated Fine-Tuning of LLMs
作者: Hanlin Cai, Kai Li, Houtianfu Wang, Haofan Dong, Yichen Li, Falko Dressler, Ozgur B. Akan
链接: https://arxiv.org/abs/2605.07961v1
完整摘要: Federated fine-tuning (FFT) has emerged as a privacy-preserving paradigm for collaboratively adapting large language models (LLMs). Built upon federated learning, FFT enables distributed agents to jointly refine a shared pretrained LLM by aggregating local LLM updates without sharing local raw data. However, FFT-based LLMs remain vulnerable to model manipulation threats, in which adversarial participants upload manipulated LLM updates that corrupt the aggregation process and degrade the performance of the global LLM. In this paper, we propose an Augmented Model maniPulation (AugMP) strategy against FFT-based LLMs. Specifically, we design a novel graph representation learning framework that captures feature correlations among benign LLM updates to guide the generation of malicious updates. To enhance manipulation effectiveness and stealthiness, we develop an iterative manipulation algorithm based on an augmented Lagrangian dual formulation. Through this formulation, malicious updates are optimized to embed adversarial objectives while preserving benign-like parameter characteristics. Experimental results across multiple LLM backbones demonstrate that the AugMP strategy achieves the strongest manipulation performance among all competing baselines, reducing the global LLM accuracy by up to 26% and degrading the average accuracy of local LLM agents by up to 22%. Meanwhile, AugMP maintains high statistical and geometric consistency with benign updates, enabling it to evade conventional distance- and similarity-based defense methods.
匹配关键词: manipulation
---

[ACADEMIC - ARXIV]
标题: TAVIS: A Benchmark for Egocentric Active Vision and Anticipatory Gaze in Imitation Learning
作者: Giacomo Spigler
链接: https://arxiv.org/abs/2605.07943v1
完整摘要: Active vision -- where a policy controls its own gaze during manipulation -- has emerged as a key capability for imitation learning, with multiple independent systems demonstrating its benefits in the past year. Yet there is no shared benchmark to compare approaches or quantify what active vision contributes, on which task types, and under what conditions. We introduce TAVIS, evaluation infrastructure for active-vision imitation learning, with two complementary task suites -- TAVIS-Head (5 tasks, global search via pan/tilt necks) and TAVIS-Hands (3 tasks, local occlusion via wrist cameras) -- on two humanoid torso embodiments (GR1T2, Reachy2), built on IsaacLab. TAVIS provides three evaluation primitives: a paired headcam-vs-fixedcam protocol on identical demonstrations; GALT (Gaze-Action Lead Time), a novel metric grounded in cognitive science and HRI that quantifies anticipatory gaze in learned policies; and procedural ID/OOD splits. Baseline experiments with Diffusion Policy and $π_0$ reveal that (i) active-vision generally helps, but benefits are task-conditional rather than uniform; (ii) multi-task policies degrade sharply under controlled distribution shifts on both suites; and (iii) imitation alone yields anticipatory gaze, with median lead times comparable to the human teleoperator reference. Code, evaluation scripts, demonstrations (LeRobot v3.0; ~2200 episodes) and trained baselines are released at https://github.com/spiglerg/tavis and https://huggingface.co/tavis-benchmark.
匹配关键词: manipulation
---

[ACADEMIC - ARXIV]
标题: NoiseGate: Learning Per-Latent Timestep Schedules as Information Gating in World Action Models
作者: Wen Huang, Haoran Sun, Yongjian Guo, Yunxuan Ma, Haoran Li, Jing Long, Zhouying Mo, Zhong Guan, Yucheng Guo, Shuai Di, Junwu Xiong
链接: https://arxiv.org/abs/2605.07794v1
完整摘要: World Action Models (WAMs) are an emerging family of policies that tie robot action generation to future-observation modeling. In this work, we focus on the joint video--action modeling paradigm, where actions and imagined future observations are co-generated along a shared denoising or flow trajectory, so that perception, prediction, and control are coupled within one generative process. Existing WAMs typically realize this paradigm with a Mixture-of-Transformers (MoT), where video and action tokens interact through shared self-attention. This architecture can in principle assign a separate timestep $t_f$ to each predicted latent frame, yet current systems collapse this degree of freedom onto a single shared scalar $t$. Under the noise-as-masking view of Diffusion Forcing, this shared schedule imposes the unjustified prior that every predicted latent is equally reliable for action generation. We instead view the per-latent schedule as a \emph{learnable information-gating policy}: by changing a latent frame's noise level, the policy modulates the reliability of its Key/Value contribution to the action tokens. We propose \textbf{NoiseGate}, which combines independent per-latent timestep sampling during backbone training, a lightweight Gating Policy Network that emits per-latent time increments during denoising, and task-reward optimization that trains the schedule policy without hand-crafted shape priors. Built on a joint video--action MoT backbone, NoiseGate delivers consistent gains on diverse RoboTwin random-scene manipulation tasks.
匹配关键词: manipulation
---

[ACADEMIC - ARXIV]
标题: Drifting Field Policy: A One-Step Generative Policy via Wasserstein Gradient Flow
作者: Juil Koo, Mingue Park, Jiwon Choi, Yunhong Min, Minhyuk Sung
链接: https://arxiv.org/abs/2605.07727v1
完整摘要: We propose Drifting Field Policy (DFP), a non-ODE one-step generative policy built on the drifting model paradigm. We frame the policy update as a reverse-KL Wasserstein-2 gradient flow toward a soft target policy, so that each DFP update corresponds to a gradient step in probability space. By construction, this gradient is decomposed into an ascent toward higher action-value regions and a score matching with the anchor policy as a trust region. We further derive a simple, tractable surrogate of the otherwise intractable update loss, akin to behavior cloning on top-K critic-selected actions. We find empirically that this mechanism uniquely benefits the drifting backbone owing to its non-ODE parameterization. With one-step inference, DFP achieves state-of-the-art performance on several manipulation tasks across Robomimic and OGBench, outperforming ODE-based policies.
匹配关键词: manipulation
---

[ACADEMIC - ARXIV]
标题: PhySPRING: Structure-Preserving Reduction of Physics-Informed Twins via GNN
作者: Yixiong Jing, Xingyuan Chen, Guangming Wang, Olaf Wysocki, Haibing Wu, Brian Sheil
链接: https://arxiv.org/abs/2605.07687v1
完整摘要: Physics-based digital twins aim to predict the dynamics of real-world objects under interaction, enabling real-to-sim-to-real applications in robotics. Current approaches reconstruct such twins as explicit physical models (such as spring-mass systems) to predict the dynamics, but the resulting models often inherit the resolution of the visual reconstruction rather than being reduced to the physical complexity required to reproduce task-relevant dynamics. This mismatch introduces redundant topology, making repeated forward-dynamics rollouts unnecessarily expensive. To address this challenge, we present PhySPRING, an fully differentiable GNN-based method to reduce complexity in spring--mass digital twins. PhySPRING jointly learns a hierarchy of coarsened graph topologies and their mechanical parameters from observations. At each reduction level, PhySPRING merges nodes with similar learned dynamic responses to optimize the topology, while maintaining every reduced layer as an explicit spring--mass system. On the PhysTwin benchmark, PhySPRING improves dense reconstruction and prediction accuracy over PhysTwin, while reduced models retain stable physical and visual fidelity with up to a 2.30 times speed-up. We further demonstrate the effectiveness of PhySPRING in a Real2Sim robot policy-evaluation pipeline, where the reduced models are substituted zero-shot into ACT and $π_0$ evaluations, maintaining comparable manipulation success rates across downsampling levels while improving action-sampling effectiveness. Together, PhySPRING enables efficient and structure-preserving spring--mass reduction without sacrificing fidelity or robotic utility.
匹配关键词: sim-to-real
---

[ACADEMIC - ARXIV]
标题: Toward Visually Realistic Simulation: A Benchmark for Evaluating Robot Manipulation in Simulation
作者: Yixin Zhu, Zixiong Wang, Jian Yang, Jin Xie, Jingyi Yu, Jiayuan Gu, Beibei Wang
链接: https://arxiv.org/abs/2605.06311v1
完整摘要: Reliable simulation evaluation of robot manipulation policies serves as a high-fidelity proxy for real-world performance. Although existing benchmarks cover a wide range of task categories, they lack visual realism, creating a large domain gap between simulation and reality. This undermines the reliability of simulation-based evaluation in predicting real-world performance. To mitigate the sim-to-real visual gap, we conduct a systematic analysis to isolate the effects of lighting and material. Our results show that these factors play a critical role in geometric reasoning and spatial grounding, yet are largely overlooked in existing benchmarks. Motivated by the analysis, we propose VISER, a visually realistic benchmark for evaluating robot manipulation in simulation. VISER features a high-fidelity dataset of over 1,000 3D assets with physically-based rendering (PBR) materials, along with 3D scenes created from these assets through curated layouts or generation. To this end, we propose an automated pipeline leveraging Multi-modal Large Language Models (MLLMs) for material-aware part segmentation and material retrieval, enabling scalable generation of physically plausible assets. Building on the high-fidelity 3D asset dataset, we construct diverse evaluation tasks, such as grasping, placing, and long-horizon tasks, enabling scalable and reproducible assessment of Vision-Language-Action (VLA) models. Our benchmark shows a strong correlation between simulation and real-world performance, achieving an average Pearson correlation coefficient of 0.92 across different policies.
匹配关键词: sim-to-real
---

[ACADEMIC - ARXIV]
标题: DexSynRefine: Synthesizing and Refining Human-Object Interaction Motion for Physically Feasible Dexterous Robot Actions
作者: Hyesung Lee, Hyunwoo Jung, Si-Hwan Heo, Sungwook Yang
链接: https://arxiv.org/abs/2605.05925v1
完整摘要: Learning dexterous manipulation from human-object interaction (HOI) data is a scalable alternative to teleoperation, but HOI demonstrations are sparse and provide only kinematic motion that is not directly executable under embodiment mismatch and contact-rich dynamics. We present DexSynRefine, a framework with three coupled components: HOI-MMFP, a task- and object-initial-state-conditioned extension of motion manifold primitives that synthesizes coordinated hand-object trajectories from sparse HOI demonstrations; a task-space residual RL policy that physically grounds the synthesized reference while inheriting its kinematic structure; and a contact-and-dynamics adaptation module that enables sim-to-real transfer from proprioceptive history. Across five dexterous manipulation tasks spanning pick-and-place, tool use, and object reorientation, our task-space residual policy outperforms prior action-representation baselines in simulations and transfers to a real robot on all five tasks, improving over kinematic retargeting by 50-70 percentage points.
匹配关键词: sim-to-real
---

[ACADEMIC - ARXIV]
标题: Beyond Retrieval: A Multitask Benchmark and Model for Code Search
作者: Siqiao Xue, Zihan Liao, Jin Qin, Ziyin Zhang, Yixiang Mu, Fan Zhou, Hang Yu
链接: https://arxiv.org/abs/2605.04615v2
完整摘要: Code search has usually been evaluated as first-stage retrieval, even though production systems rely on broader pipelines with reranking and developer-style queries. Existing benchmarks also suffer from data contamination, label noise, and degenerate binary relevance. In this paper, we introduce \textsc{CoREB}, a contamination-limited, multitask \underline{co}de \underline{r}etrieval and r\underline{e}ranking \underline{b}enchmark, together with a fine-tuned code reranker, that goes beyond retrieval to cover the full code search pipeline. \textsc{CoREB} is built from counterfactually rewritten LiveCodeBench problems in five programming languages and delivered as timed releases with graded relevance judgments. We benchmark eleven embedding models and five rerankers across three tasks: text-to-code, code-to-text, and code-to-code. Our experiments reveal that: \circone code-specialised embeddings dominate code-to-code retrieval (${\sim}2{\times}$ over general encoders), yet no single model wins all three tasks; \circtwo short keyword queries, the format closest to real developer search, collapse every model to near-zero nDCG@10; \circthree off-the-shelf rerankers are task-asymmetric, with a 12-point swing on code-to-code and no baseline net-positive across all tasks; \circfour our fine-tuned \textsc{CoREB-Reranker} is the first to achieve consistent gains across all three tasks. The data and model are released.
匹配关键词: sim-to-real
---

[ACADEMIC - ARXIV]
标题: SigLoMa: Learning Open-World Quadrupedal Loco-Manipulation from Ego-Centric Vision
作者: Shiyi Chen, Haiyi Liu, Mingye Yang, Jiaqi Zhang, Debing Zhang
链接: https://arxiv.org/abs/2605.03846v1
完整摘要: Designing an open-world quadrupedal loco-manipulation system is highly challenging. Traditional reinforcement learning frameworks utilizing exteroception often suffer from extreme sample inefficiency and massive sim-to-real gaps. Furthermore, the inherent latency of visual tracking fundamentally conflicts with the high-frequency demands of precise floating-base control. Consequently, existing systems lean heavily on expensive external motion capture and off-board computation. To eliminate these dependencies, we present SigLoMa, a fully onboard, ego-centric vision-based pick-and-place framework. At the core of SigLoMa is the introduction of Sigma Points, a lightweight geometric representation for exteroception that guarantees high scalability and native sim-to-real alignment. To bridge the frequency divide between slow perception and fast control, we design an ego-centric Kalman Filter to provide robust, high-rate state estimation. On the learning front, we alleviate sample inefficiency via an Active Sampling Curriculum guided by Hint Poses, and tackle the robot's structural visual blind spots using temporal encoding coupled with simulated random-walk drift. Real-world experiments validate that, relying solely on a 5Hz (200 ms latency) open-vocabulary detector, SigLoMa successfully executes dynamic loco-manipulation across multiple tasks, achieving performance comparable to expert human teleoperation.
匹配关键词: sim-to-real
---

[ACADEMIC - ARXIV]
标题: 123D: Unifying Multi-Modal Autonomous Driving Data at Scale
作者: Daniel Dauner, Valentin Charraut, Bastian Berle, Tianyu Li, Long Nguyen, Jiabao Wang, Changhui Jing, Maximilian Igl, Holger Caesar, Boris Ivanovic, Yiyi Liao, Andreas Geiger, Kashyap Chitta
链接: https://arxiv.org/abs/2605.08084v1
完整摘要: The pursuit of autonomous driving has produced one of the richest sensor data collections in all of robotics. However, its scale and diversity remain largely untapped. Each dataset adopts different 2D and 3D modalities, such as cameras, lidar, ego states, annotations, traffic lights, and HD maps, with different rates and synchronization schemes. They come in fragmented formats requiring complex dependencies that cannot natively coexist in the same development environment. Further, major inconsistencies in annotation conventions prevent training or measuring generalization across multiple datasets. We present 123D, an open-source framework that unifies such multi-modal driving data through a single API. To handle synchronization, we store each modality as an independent timestamped event stream with no prescribed rate, enabling synchronous or asynchronous access across arbitrary datasets. Using 123D, we consolidate eight real-world driving datasets spanning 3,300 hours and 90,000 kilometers, together with a synthetic dataset with configurable collection scripts, and provide tools for data analysis and visualization. We conduct a systematic study comparing annotation statistics and assessing each dataset's pose and calibration accuracy. Further, we showcase two applications 123D enables: cross-dataset 3D object detection transfer and reinforcement learning for planning, and offer recommendations for future directions. Code and documentation are available at https://github.com/kesai-labs/py123d.
匹配关键词: world model
---

[ACADEMIC - ARXIV]
标题: LLMs Improving LLMs: Agentic Discovery for Test-Time Scaling
作者: Tong Zheng, Haolin Liu, Chengsong Huang, Huiwen Bao, Sheng Zhang, Rui Liu, Runpeng Dai, Ruibo Chen, Chenxi Liu, Tianyi Xiong, Xidong Wu, Hongming Zhang, Heng Huang
链接: https://arxiv.org/abs/2605.08083v1
完整摘要: Test-time scaling (TTS) has become an effective approach for improving large language model performance by allocating additional computation during inference. However, existing TTS strategies are largely hand-crafted: researchers manually design reasoning patterns and tune heuristics by intuition, leaving much of the computation-allocation space unexplored. We propose an environment-driven framework, AutoTTS, that changes what researchers design: from individual TTS heuristics to environments where TTS strategies can be discovered automatically. The key to AutoTTS lies in environment construction: the discovery environment must make the control space tractable and provide cheap, frequent feedback for TTS search. As a concrete instantiation, we formulate width--depth TTS as controller synthesis over pre-collected reasoning trajectories and probe signals, where controllers decide when to branch, continue, probe, prune, or stop and can be evaluated cheaply without repeated LLM calls. We further introduce beta parameterization to make the search tractable and fine-grained execution trace feedback to improve discovery efficiency by helping the agent diagnose why a TTS program fails. Experiments on mathematical reasoning benchmarks show that the discovered strategies improve the overall accuracy--cost tradeoff over strong manually designed baselines. The discovered strategies generalize to held-out benchmarks and model scales, while the entire discovery costs only $39.9 and 160 minutes. Our data, and code will be open-source at https://github.com/zhengkid/AutoTTS.
匹配关键词: world model
---

[ACADEMIC - ARXIV]
标题: Normalizing Trajectory Models
作者: Jiatao Gu, Tianrong Chen, Ying Shen, David Berthelot, Shuangfei Zhai, Josh Susskind
链接: https://arxiv.org/abs/2605.08078v1
完整摘要: Diffusion-based models decompose sampling into many small Gaussian denoising steps -- an assumption that breaks down when generation is compressed to a few coarse transitions. Existing few-step methods address this through distillation, consistency training, or adversarial objectives, but sacrifice the likelihood framework in the process. We introduce Normalizing Trajectory Models (NTM), which models each reverse step as an expressive conditional normalizing flow with exact likelihood training. Architecturally, NTM combines shallow invertible blocks within each step with a deep parallel predictor across the trajectory, forming an end-to-end network trainable from scratch or initializable from pretrained flow-matching models. Its exact trajectory likelihood further enables self-distillation: a lightweight denoiser trained on the model's own score produces high-quality samples in four steps. On text-to-image benchmarks, NTM matches or outperforms strong image generation baselines in just four sampling steps while uniquely retaining exact likelihood over the generative trajectory.
匹配关键词: world model
---

[ACADEMIC - ARXIV]
标题: Zero-Shot Imagined Speech Decoding via Imagined-to-Listened MEG Mapping
作者: Maryam Maghsoudi, Shihab Shamma
链接: https://arxiv.org/abs/2605.08075v1
完整摘要: Decoding imagined speech from non-invasive brain recordings is challenging because imagined datasets are scarce and difficult to align temporally across subjects and sessions In this work, we propose a new approach to the decoding of imagined speech that leverages the richer and more reliably labeled recordings during listening to speech. We collected paired listened and imagined MEG recordings to rhythmic melodic and spoken stimuli from trained musicians. Using trained musicians helped improve temporal alignment across conditions. We then developed a three-stage decoding pipeline that revealed consistent and meaningful relationships between neural activity evoked by imagining and listening to the same stimuli. First, we trained six linear and neural models to map imagined MEG responses to listened responses. We evaluated these models against a null baseline from unseen subjects to validate that the predicted-listening responses preserve stimulus-specific information. In the second stage, we trained a contrastive word decoder exclusively on the listened MEG responses, and evaluated it using four embedding strategies including semantic, acoustic, and phonetic representations. In the third stage, we process the imagined MEG responses from held-out subjects through the mapping pipeline to compute the corresponding listening responses that are then decoded by the listened decoder. Using rank-based analysis, we show that the imagined words are decodable significantly above chance. We shall report here the results of a proof-of-concept implementation to decode imagined speech, where all evaluations are performed on held-out subjects. We also demonstrate that performance improves with training data size, suggesting that this approach is scalable and can directly be made applicable to realistic brain-computer interface scenarios.
匹配关键词: world model
---

[ACADEMIC - ARXIV]
标题: GRAPHLCP: Structure-Aware Localized Conformal Prediction on Graphs
作者: Peyman Baghershahi, Fangxin Wang, Debmalya Mandal, Sourav Medya
链接: https://arxiv.org/abs/2605.08074v1
完整摘要: Conformal prediction (CP) provides a distribution-free approach to uncertainty quantification with finite-sample guarantees. However, applying CP to graph neural networks (GNNs) remains challenging as the combinatorial nature of graphs often leads to insufficiently certain predictions and indiscriminative embeddings. Existing methods primarily rely on embedding-space proximity for localization, which can be unreliable for graphs and yield inefficient prediction sets. We propose GRAPHLCP, a proximity-based localized CP framework that explicitly incorporates graph topology and inter-node dependencies into localization and weighting. Our approach introduces a feature-aware densification step to mitigate locality bias in sparse graphs, followed by a Personalized PageRank-based kernel computation to model structural proximity. This enables topology-dependent anchor sampling and calibration weighting that captures both local and long-range dependencies. Extensive experiments on several regression and classification datasets demonstrate that GRAPHLCP guarantees marginal coverage with finite samples while efficiently attaining favorable test conditional coverage across various conditioning scenarios.
匹配关键词: world model
---

[ACADEMIC - ARXIV]
标题: LLMs Improving LLMs: Agentic Discovery for Test-Time Scaling
作者: Tong Zheng, Haolin Liu, Chengsong Huang, Huiwen Bao, Sheng Zhang, Rui Liu, Runpeng Dai, Ruibo Chen, Chenxi Liu, Tianyi Xiong, Xidong Wu, Hongming Zhang, Heng Huang
链接: https://arxiv.org/abs/2605.08083v1
完整摘要: Test-time scaling (TTS) has become an effective approach for improving large language model performance by allocating additional computation during inference. However, existing TTS strategies are largely hand-crafted: researchers manually design reasoning patterns and tune heuristics by intuition, leaving much of the computation-allocation space unexplored. We propose an environment-driven framework, AutoTTS, that changes what researchers design: from individual TTS heuristics to environments where TTS strategies can be discovered automatically. The key to AutoTTS lies in environment construction: the discovery environment must make the control space tractable and provide cheap, frequent feedback for TTS search. As a concrete instantiation, we formulate width--depth TTS as controller synthesis over pre-collected reasoning trajectories and probe signals, where controllers decide when to branch, continue, probe, prune, or stop and can be evaluated cheaply without repeated LLM calls. We further introduce beta parameterization to make the search tractable and fine-grained execution trace feedback to improve discovery efficiency by helping the agent diagnose why a TTS program fails. Experiments on mathematical reasoning benchmarks show that the discovered strategies improve the overall accuracy--cost tradeoff over strong manually designed baselines. The discovered strategies generalize to held-out benchmarks and model scales, while the entire discovery costs only $39.9 and 160 minutes. Our data, and code will be open-source at https://github.com/zhengkid/AutoTTS.
匹配关键词: speech synthesis
---

[ACADEMIC - ARXIV]
标题: Zero-Shot Imagined Speech Decoding via Imagined-to-Listened MEG Mapping
作者: Maryam Maghsoudi, Shihab Shamma
链接: https://arxiv.org/abs/2605.08075v1
完整摘要: Decoding imagined speech from non-invasive brain recordings is challenging because imagined datasets are scarce and difficult to align temporally across subjects and sessions In this work, we propose a new approach to the decoding of imagined speech that leverages the richer and more reliably labeled recordings during listening to speech. We collected paired listened and imagined MEG recordings to rhythmic melodic and spoken stimuli from trained musicians. Using trained musicians helped improve temporal alignment across conditions. We then developed a three-stage decoding pipeline that revealed consistent and meaningful relationships between neural activity evoked by imagining and listening to the same stimuli. First, we trained six linear and neural models to map imagined MEG responses to listened responses. We evaluated these models against a null baseline from unseen subjects to validate that the predicted-listening responses preserve stimulus-specific information. In the second stage, we trained a contrastive word decoder exclusively on the listened MEG responses, and evaluated it using four embedding strategies including semantic, acoustic, and phonetic representations. In the third stage, we process the imagined MEG responses from held-out subjects through the mapping pipeline to compute the corresponding listening responses that are then decoded by the listened decoder. Using rank-based analysis, we show that the imagined words are decodable significantly above chance. We shall report here the results of a proof-of-concept implementation to decode imagined speech, where all evaluations are performed on held-out subjects. We also demonstrate that performance improves with training data size, suggesting that this approach is scalable and can directly be made applicable to realistic brain-computer interface scenarios.
匹配关键词: speech synthesis
---

[ACADEMIC - ARXIV]
标题: Towards Highly-Constrained Human Motion Generation with Retrieval-Guided Diffusion Noise Optimization
作者: Hanchao Liu, Fang-Lue Zhang, Shining Zhang, Tai-Jiang Mu, Shi-Min Hu
链接: https://arxiv.org/abs/2605.08054v1
完整摘要: Generating human motion that satisfies customized zero-shot goal functions, enabling applications such as controllable character animation and behavior synthesis for virtual agents, is a critical capability. While current approaches handle many unseen constraints, they fail on tasks with very challenging spatiotemporal restrictions, such as severe spatial obstacles or specified numbers of walking steps. To equip motion generators for these highly constrained tasks, we present a retrieval-guided method built on the training-free diffusion noise optimization framework. The key idea is to search within large motion datasets for guidance that can potentially satisfy difficult constraints. We introduce relational task parsing to group target constraints and identify the difficult ones to be handled by retrieved reference. A better initialization for diffusion noise is then obtained via a reward-guided mask that combines random noise with retrieved noise. By optimizing diffusion noise from this improved initialization, we successfully solve highly constrained generation tasks. By leveraging LLM for relational task parsing, the whole framework is further enabled to automatically reason for what to retrieve, improving the intelligence of moving agents under a training-free optimization scheme.
匹配关键词: speech synthesis
---

[ACADEMIC - ARXIV]
标题: MoCoTalk: Multi-Conditional Diffusion with Adaptive Router for Controllable Talking Head Generation
作者: Xinyan Ye, Jiankang Deng, Abbas Edalat
链接: https://arxiv.org/abs/2605.08050v1
完整摘要: Talking-head generation requires joint modeling of identity, head pose, facial expression, and mouth dynamics. Existing methods typically address only a subset of these factors, and rely on fixed-weight or heuristic fusion when multiple conditions are involved. We present MoCoTalk, a multi-conditional video diffusion framework that unifies four complementary control signals: a reference image, facial keypoints, 3DMM-rendered shading meshes, and the corresponding speech audio. To resolve destructive interference among heterogeneous conditions, we introduce an Adaptive Multi-Condition Router that computes channel-wise, timestep-aware gating over the four condition streams, allowing the fusion strategy to vary with both feature subspace and noise level. To better capture speech-related facial dynamics, we design a Mouth-Augmented Shading Mesh, a 3DMM-based representation that decouples head motion, mouth motion, expression, and lighting. This design provides a temporally consistent geometric prior and allows flexible recombination of these attributes at inference. We further introduce a lip consistency loss to tighten audio-visual alignment. Extensive experiments show that MoCoTalk achieves state-of-the-art performance on the majority of structural, motion, and perceptual metrics, while offering attribute-level controllability that single-condition methods do not provide.
匹配关键词: speech synthesis
---

[ACADEMIC - ARXIV]
标题: Beyond Pairs: Your Language Model is Secretly Optimizing a Preference Graph
作者: Ning Liu, Chuanneng Sun, Kristina Klinkner, Shervin Malmasi
链接: https://arxiv.org/abs/2605.08037v1
完整摘要: Direct Preference Optimization (DPO) aligns language models using pairwise preference comparisons, offering a simple and effective alternative to Reinforcement Learning (RL) from human feedback. However, in many practical settings, training data consists of multiple rollouts per prompt, inducing rich preference structure that pairwise DPO fails to exploit. Collapsing such data into independent pairs discards transitivity, introduces redundant or conflicting supervision, and can lead to unstable optimization. We propose Graph Direct Preference Optimization (GraphDPO), a principled generalization of DPO that operates over directed acyclic preference graphs induced by rollout rankings. GraphDPO encodes dominance relations as edges and optimizes a graph-structured Plackett--Luce-inspired objective that aggregates supervision over graph neighborhoods, enforcing transitivity while recovering standard DPO as a special case. To handle discrete or sparse signals, we introduce an equivalence-class construction where responses with identical preferences form graph layers, and intra-layer edges contribute zero loss, preventing spurious gradients. Despite leveraging full graph structure, GraphDPO maintains linear per-prompt complexity via efficient log-sum-exp aggregation. We further incorporate optional ground-truth anchoring by inserting verified solutions as dominant nodes and applying an annealed schedule that stabilizes early training while gradually relaxing oracle supervision. Experiments on reasoning and program synthesis tasks demonstrate superior performance, suggesting that graph-structured preference modeling is a scalable and robust alternative to pairwise and listwise alignment objectives.
匹配关键词: speech synthesis
---

[ACADEMIC - ARXIV]
标题: LLMs Improving LLMs: Agentic Discovery for Test-Time Scaling
作者: Tong Zheng, Haolin Liu, Chengsong Huang, Huiwen Bao, Sheng Zhang, Rui Liu, Runpeng Dai, Ruibo Chen, Chenxi Liu, Tianyi Xiong, Xidong Wu, Hongming Zhang, Heng Huang
链接: https://arxiv.org/abs/2605.08083v1
完整摘要: Test-time scaling (TTS) has become an effective approach for improving large language model performance by allocating additional computation during inference. However, existing TTS strategies are largely hand-crafted: researchers manually design reasoning patterns and tune heuristics by intuition, leaving much of the computation-allocation space unexplored. We propose an environment-driven framework, AutoTTS, that changes what researchers design: from individual TTS heuristics to environments where TTS strategies can be discovered automatically. The key to AutoTTS lies in environment construction: the discovery environment must make the control space tractable and provide cheap, frequent feedback for TTS search. As a concrete instantiation, we formulate width--depth TTS as controller synthesis over pre-collected reasoning trajectories and probe signals, where controllers decide when to branch, continue, probe, prune, or stop and can be evaluated cheaply without repeated LLM calls. We further introduce beta parameterization to make the search tractable and fine-grained execution trace feedback to improve discovery efficiency by helping the agent diagnose why a TTS program fails. Experiments on mathematical reasoning benchmarks show that the discovered strategies improve the overall accuracy--cost tradeoff over strong manually designed baselines. The discovered strategies generalize to held-out benchmarks and model scales, while the entire discovery costs only $39.9 and 160 minutes. Our data, and code will be open-source at https://github.com/zhengkid/AutoTTS.
匹配关键词: TTS
---

[ACADEMIC - ARXIV]
标题: WavCube: Unifying Speech Representation for Understanding and Generation via Semantic-Acoustic Joint Modeling
作者: Guanrou Yang, Tian Tan, Qian Chen, Zhikang Niu, Yakun Song, Ziyang Ma, Yushen Chen, Zeyu Xie, Tianrui Wang, Yifan Yang, Wenxi Chen, Qi Chen, Wenrui Liu, Shan Yang, Xie Chen
链接: https://arxiv.org/abs/2605.06407v1
完整摘要: Integrating speech understanding and generation is a pivotal step toward building unified speech models. However, the different representations required for these two tasks currently pose significant compatibility challenges. Typically, semantics-oriented features are learned from self-supervised learning (SSL), and acoustic-oriented features from reconstruction. Such fragmented representations hinder the realization of truly unified speech systems. We present WavCube, a compact continuous latent derived from an SSL speech encoder that simultaneously supports speech understanding, reconstruction, and generation. WavCube employs a two-stage training scheme. Stage 1 trains a semantic bottleneck to filter off-manifold redundancy that makes raw SSL features intractable for diffusion. Stage 2 injects fine-grained acoustic details via end-to-end reconstruction, while a semantic anchoring loss ensures the representation remains grounded within its original semantic manifold. Comprehensive experiments show that WavCube closely approaches WavLM performance on SUPERB despite an 8x dimensional compression, attains reconstruction quality on par with existing acoustic representations, delivers state-of-the-art zero-shot TTS performance with markedly faster training convergence, and excels in speech enhancement, separation, and voice conversion tasks on the SUPERB-SG benchmark. Systematic ablations reveal that WavCube's two-stage recipe resolves two intrinsic flaws of SSL features for generative modeling, paving the way for future unified speech systems. Codes and checkpoints are available at https://github.com/yanghaha0908/WavCube.
匹配关键词: TTS
---

[ACADEMIC - ARXIV]
标题: X-Voice: Enabling Everyone to Speak 30 Languages via Zero-Shot Cross-Lingual Voice Cloning
作者: Rixi Xu, Qingyu Liu, Haitao Li, Yushen Chen, Zhikang Niu, Yunting Yang, Jian Zhao, Ke Li, Berrak Sisman, Qinyuan Cheng, Xipeng Qiu, Kai Yu, Xie Chen
链接: https://arxiv.org/abs/2605.05611v1
完整摘要: In this paper, we present X-Voice, a 0.4B multilingual zero-shot voice cloning model that clones arbitrary voices and enables everyone to speak 30 languages. X-Voice is trained on a 420K-hour multilingual corpus using the International Phonetic Alphabet (IPA) as a unified representation. To eliminate the reliance on prompt text without complex preprocessing like forced alignment, we design a two-stage training paradigm. In Stage 1, we establish X-Voice$_{\text{s1}}$ through standard conditional flow-matching training and use it to synthesize 10K hours of speaker-consistent segments as audio prompts. In Stage 2, we fine-tune on these audio pairs with prompt text masked to derive X-Voice$_{\text{s2}}$, which enables zero-shot voice cloning without requiring transcripts of audio prompts. Architecturally, we extend F5-TTS by implementing a dual-level injection of language identifiers and decoupling and scheduling of Classifier-Free Guidance to facilitate multilingual speech synthesis. Subjective and objective evaluation results demonstrate that X-Voice outperforms existing flow-matching based multilingual systems like LEMAS-TTS and achieves zero-shot cross-lingual cloning capabilities comparable to billion-scale models such as Qwen3-TTS. To facilitate research transparency and community advancement, we open-source all related resources.
匹配关键词: TTS
---

[ACADEMIC - ARXIV]
标题: BitCal-TTS: Bit-Calibrated Test-Time Scaling for Quantized Reasoning Models
作者: Sai Babu Patarlapalli, Surya Teja Avvaru
链接: https://arxiv.org/abs/2605.05561v1
完整摘要: Post-training quantization makes large reasoning models practical under tight memory and latency budgets, but it can distort the online signals that drive adaptive test-time compute allocation. Under a fixed cap on the number of newly generated tokens, miscalibrated confidence can lead to harmful early halting: the model may surface a plausible final line while the underlying reasoning is still wrong, or the controller may stop before the trace has stabilized. We study this interaction for greedy 4-bit inference and propose BitCal-TTS, a lightweight runtime controller that combines (i) inexpensive online proxies for token-level uncertainty and reasoning-trace stability, (ii) a bit-conditioned confidence rescaling that is conservative at low nominal precision, and (iii) a bit-aware post-marker confirmation horizon designed for GSM8K-style structured outputs. The method requires no fine-tuning of the base model and integrates with standard Hugging Face 4-bit inference using forward hooks for logits and last-layer hidden states. On small evaluation shards of GSM8K with Qwen2.5 Instruct models, BitCal-TTS improves exact-match accuracy over a non-bit-aware adaptive baseline at the 7B and 14B scales while preserving substantial token savings relative to fixed-budget decoding. At a token cap of B=512, on the evaluation shards we report (N=54 for 7B and N=35 for 14B; not the full GSM8K test set), accuracy gains are +3.7 points (7B) and +2.8 points (14B), with the premature-stop rate falling from 14.8% to 11.1% on 7B and from 17.1% to 11.4% on 14B. We report Wilson 95% confidence intervals throughout and explicitly discuss the limited statistical power of the partial-shard comparisons. We release code and figure-generation scripts to support full reproduction.
匹配关键词: TTS
---

[ACADEMIC - ARXIV]
标题: Stream-T1: Test-Time Scaling for Streaming Video Generation
作者: Yijing Tu, Shaojin Wu, Mengqi Huang, Wenchuan Wang, Yuxin Wang, Chunxiao Liu, Zhendong Mao
链接: https://arxiv.org/abs/2605.04461v1
完整摘要: While Test-Time Scaling (TTS) offers a promising direction to enhance video generation without the surging costs of training, current test-time video generation methods based on diffusion models suffer from exorbitant candidate exploration costs and lack temporal guidance. To address these structural bottlenecks, we propose shifting the focus to streaming video generation. We identify that its chunk-level synthesis and few denoising steps are intrinsically suited for TTS, significantly lowering computational overhead while enabling fine-grained temporal control. Driven by this insight, we introduced Stream-T1, a pioneering comprehensive TTS framework exclusively tailored for streaming video generation. Specifically, Stream-T1 is composed of three units: (1) Stream -Scaled Noise Propagation, which actively refines the initial latent noise of the generating chunk using historically proven, high-quality previous chunk noise, effectively establishes temporal dependency and utilizing the historical Gaussian prior to guide the current generation; (2) Stream -Scaled Reward Pruning, which comprehensively evaluates generated candidates to strike an optimal balance between local spatial aesthetics and global temporal coherence by integrating immediate short-term assessments with sliding-window-based long-term evaluations; (3) Stream-Scaled Memory Sinking, which dynamically routes the context evicted from KV-cache into distinct updating pathways guided by the reward feedback, ensuring that previously generated visual information effectively anchors and guides the subsequent video stream. Evaluated on both 5s and 30s comprehensive video benchmarks, Stream-T1 demonstrates profound superiority, significantly improving temporal consistency, motion smoothness, and frame-level visual quality.
匹配关键词: TTS
---

[ACADEMIC - ARXIV]
标题: CSR: Infinite-Horizon Real-Time Policies with Massive Cached State Representations
作者: Robin Karlsson, Go Suzui
链接: https://arxiv.org/abs/2605.07325v1
完整摘要: Deploying massive large language models (LLMs) as continuous cognitive engines for robotics is bottlenecked by the time-to-first-token (TTFT) latency required to process extensive state histories. Existing solutions like RAG or sliding windows compromise global context or incur prohibitive re-computation costs. We formalize the optimal task structure for minimizing latency and theoretically prove that prefix stability, incremental extensibility, and asynchronous state reconciliation are necessary conditions for real-time performance. Building on these proofs, we introduce the Cached State Representation (CSR) framework as the practical instantiation of these properties, ensuring optimal KV-cache reuse. To sustain these properties over infinite horizons, we further propose an Asynchronous State Reconciliation (ASR) algorithm that offloads state memory eviction to a parallel computational resource to eliminate latency spikes. On a physical robot wirelessly connected to an on-premise GPU server, CSR achieves a 26-fold latency reduction (14.67s to 0.56s) for 120K token contexts with a 235B parameter model compared to a standard baseline. On an embodied AI benchmark, we achieve SOTA recall (0.836 vs. 0.459) while maintaining RAG-level latency. ASR is validated to sustain bounded, spike-free TTFT over 10 eviction cycles in continuous real-world operation. Together, CSR and ASR enable massive LLMs to function as continuously operating, high-frequency (> 2 Hz) embodied policies.
匹配关键词: ASR
---

[ACADEMIC - ARXIV]
标题: Beyond Single Ground Truth: Reference Monism as Epistemic Injustice in ASR Evaluation
作者: Anna Seo Gyeong Choi, Maria Teleki, James Caverlee, Miguel del Rio, Corey Miller, Hoon Choi
链接: https://arxiv.org/abs/2605.07084v1
完整摘要: Automatic speech recognition (ASR) evaluation compares system output to ground truth transcripts, with Word Error Rate (WER) quantifying the distance between them. But ground truth transcripts are not discovered - they are produced by human annotators following conventions that encode normative assumptions about which speech features matter. Different conventions (verbatim, non-verbatim, legal) produce different transcripts of identical speech and judge the same ASR output differently. This paper argues that reference monism - enforcing a single transcription convention as ground truth - commits epistemic injustice. Speakers with aphasia, whose speech includes clinically meaningful disfluencies, are systematically disadvantaged when evaluated against "clean" references that treat those disfluencies as errors. The harm is not merely differential performance, but that evaluative infrastructure lacks interpretive resources to recognize their contributions as legitimate. We develop a philosophical framework introducing the hermeneutical gap, formalize Epistemic Injustice Distance (EID) to measure reference monism's cost, and demonstrate empirically using AphasiaBank that WER varies depending on which convention defines ground truth. We propose WER-Range: reporting performance across legitimate conventions rather than assuming a single correct answer.
匹配关键词: ASR
---

[ACADEMIC - ARXIV]
标题: Beyond Task Success: Measuring Workflow Fidelity in LLM-Based Agentic Payment Systems
作者: Donghao Huang, Joon Kiat Chua, Zhaoxia Wang
链接: https://arxiv.org/abs/2605.06457v1
完整摘要: LLM-based multi-agent systems are increasingly deployed for payment workflows, yet prevailing metrics, Task Success Rate (TSR) and Agent Handoff F1-Score (HF1), capture only final outcomes or unordered routing decisions. We introduce the Agentic Success Rate (ASR), a trajectory-fidelity metric that compares observed and expected agent execution sequences at the transition level, decomposing performance into Transition Recall and Transition Precision. Applied to the Hierarchical Multi-Agent System for Payments (HMASP) across 18 LLMs and 90,000 task instances, ASR reveals that 10 of 18 models systematically skip a confirmation checkpoint during payment checkout, a deviation invisible to both TSR and HF1, while 8 models enforce the checkpoint perfectly. Notably, GPT-4.1 exhibits hidden workflow shortcuts despite achieving perfect TSR and HF1, while GPT-5.2 achieves perfect ASR. Prompt refinements and deterministic routing guards guided by ASR diagnostics yield substantial TSR improvements, with gains up to +93.8 percentage points for previously struggling models, demonstrating that trajectory-level evaluation is essential in regulated domains.
匹配关键词: ASR
---

[ACADEMIC - ARXIV]
标题: XL-SafetyBench: A Country-Grounded Cross-Cultural Benchmark for LLM Safety and Cultural Sensitivity
作者: Dasol Choi, Eugenia Kim, Jaewon Noh, Sang Seo, Eunmi Kim, Myunggyo Oh, Yunjin Park, Brigitta Jesica Kartono, Josef Pichlmeier, Helena Berndt, Sai Krishna Mendu, Glenn Johannes Tungka, Özlem Gökçe, Suresh Gehlot, Katherine Pratt, Amanda Minnich, Haon Park
链接: https://arxiv.org/abs/2605.05662v1
完整摘要: Current LLM safety benchmarks are predominantly English-centric and often rely on translation, failing to capture country-specific harms. Moreover, they rarely evaluate a model's ability to detect culturally embedded sensitivities as distinct from universal harms. We introduce XL-SafetyBench. a suite of 5,500 test cases across 10 country-language pairs, comprising a Jailbreak Benchmark of country-grounded adversarial prompts and a Cultural Benchmark where local sensitivities are embedded within innocuous requests. Each item is constructed via a multi-stage pipeline that combines LLM-assisted discovery, automated validation gates, and dual independent native-speaker annotators per country. To distinguish principled refusal from comprehension failure, we evaluate Attack Success Rate (ASR) alongside two complementary metrics we introduce: Neutral-Safe Rate (NSR) and Cultural Sensitivity Rate (CSR). Evaluating 10 frontier and 27 local LLMs reveals two key findings. First, jailbreak robustness and cultural awareness do not show a coupled relationship among frontier models, so a composite safety score obscures per-axis variation. Second, local models exhibit a near-linear ASR-NSR trade-off (r = -0.81), indicating that their apparent safety reflects generation failure rather than genuine alignment. XL-SafetyBench enables more nuanced, cross-cultural safety evaluation in the multilingual era.
匹配关键词: ASR
---

[ACADEMIC - ARXIV]
标题: Sparse Tokens Suffice: Jailbreaking Audio Language Models via Token-Aware Gradient Optimization
作者: Zheng Fang, Xiaosen Wang, Shenyi Zhang, Shaokang Wang, Zhijin Ge
链接: https://arxiv.org/abs/2605.04700v1
完整摘要: Jailbreak attacks on audio language models (ALMs) optimize audio perturbations to elicit unsafe generations, and they typically update the entire waveform densely throughout optimization. In this work, we investigate the necessity of such dense optimization by analyzing the structure of token-aligned gradients in ALMs. We find that gradient energy is highly non-uniform across audio tokens, indicating that only a small subset of token-aligned audio regions dominates the optimization signal. Motivated by this observation, we propose Token-Aware Gradient Optimization (TAGO), which enables sparse jailbreak optimization by retaining only waveform gradients aligned with audio tokens that have high gradient energy, while masking the remaining gradients at each iteration. Across three ALMs, TAGO outperforms baselines, and substantial sparsification preserves strong attack success rates (e.g. on Qwen3-Omni, $\mathrm{ASR}_{l}$ remains at 86% with a token retention ratio of 0.25, compared to 87% with full token retention). These results demonstrate that dense waveform updates are largely redundant, and we advocate that future audio jailbreak and safety alignment research should further leverage this heterogeneous token-level gradient structure.
匹配关键词: ASR
---

[ACADEMIC - ARXIV]
标题: LLMs Improving LLMs: Agentic Discovery for Test-Time Scaling
作者: Tong Zheng, Haolin Liu, Chengsong Huang, Huiwen Bao, Sheng Zhang, Rui Liu, Runpeng Dai, Ruibo Chen, Chenxi Liu, Tianyi Xiong, Xidong Wu, Hongming Zhang, Heng Huang
链接: https://arxiv.org/abs/2605.08083v1
完整摘要: Test-time scaling (TTS) has become an effective approach for improving large language model performance by allocating additional computation during inference. However, existing TTS strategies are largely hand-crafted: researchers manually design reasoning patterns and tune heuristics by intuition, leaving much of the computation-allocation space unexplored. We propose an environment-driven framework, AutoTTS, that changes what researchers design: from individual TTS heuristics to environments where TTS strategies can be discovered automatically. The key to AutoTTS lies in environment construction: the discovery environment must make the control space tractable and provide cheap, frequent feedback for TTS search. As a concrete instantiation, we formulate width--depth TTS as controller synthesis over pre-collected reasoning trajectories and probe signals, where controllers decide when to branch, continue, probe, prune, or stop and can be evaluated cheaply without repeated LLM calls. We further introduce beta parameterization to make the search tractable and fine-grained execution trace feedback to improve discovery efficiency by helping the agent diagnose why a TTS program fails. Experiments on mathematical reasoning benchmarks show that the discovered strategies improve the overall accuracy--cost tradeoff over strong manually designed baselines. The discovered strategies generalize to held-out benchmarks and model scales, while the entire discovery costs only $39.9 and 160 minutes. Our data, and code will be open-source at https://github.com/zhengkid/AutoTTS.
匹配关键词: audio language model
---

[ACADEMIC - ARXIV]
标题: Normalizing Trajectory Models
作者: Jiatao Gu, Tianrong Chen, Ying Shen, David Berthelot, Shuangfei Zhai, Josh Susskind
链接: https://arxiv.org/abs/2605.08078v1
完整摘要: Diffusion-based models decompose sampling into many small Gaussian denoising steps -- an assumption that breaks down when generation is compressed to a few coarse transitions. Existing few-step methods address this through distillation, consistency training, or adversarial objectives, but sacrifice the likelihood framework in the process. We introduce Normalizing Trajectory Models (NTM), which models each reverse step as an expressive conditional normalizing flow with exact likelihood training. Architecturally, NTM combines shallow invertible blocks within each step with a deep parallel predictor across the trajectory, forming an end-to-end network trainable from scratch or initializable from pretrained flow-matching models. Its exact trajectory likelihood further enables self-distillation: a lightweight denoiser trained on the model's own score produces high-quality samples in four steps. On text-to-image benchmarks, NTM matches or outperforms strong image generation baselines in just four sampling steps while uniquely retaining exact likelihood over the generative trajectory.
匹配关键词: audio language model
---

[ACADEMIC - ARXIV]
标题: Conformal Path Reasoning: Trustworthy Knowledge Graph Question Answering via Path-Level Calibration
作者: Shuhang Lin, Chuhao Zhou, Xiao Lin, Zihan Dong, Kuan Lu, Zhencan Peng, Jie Yin, Dimitris N. Metaxas
链接: https://arxiv.org/abs/2605.08077v1
完整摘要: Knowledge Graph Question Answering (KGQA) has shown promise for grounded and interpretable reasoning, yet existing approaches often fail to provide reliable coverage guarantees over retrieved answers. While Conformal Prediction (CP) offers a principled framework for producing prediction sets with statistical guarantees, prior methods suffer from critical limitations in both calibration validity and score discriminability, resulting in violated coverage guarantees and excessively large prediction sets. To address these pitfalls, we propose Conformal Path Reasoning (CPR), a trustworthy KGQA framework with two key innovations. First, we perform query-level conformal calibration over path-level scores, preserving the exchangeability while generating path prediction sets. Second, we introduce the Residual Conformal Value Network (RCVNet), a lightweight module trained via PUCT-guided exploration to learn discriminative path-level nonconformity scores. Experiments on benchmarks show that CPR significantly improves the Empirical Coverage Rate by 34% while reducing average prediction set size by 40% compared to conformal baselines. These results validate the efficacy of CPR in satisfying coverage guarantees with substantially more compact answer sets.
匹配关键词: audio language model
---

[ACADEMIC - ARXIV]
标题: Zero-Shot Imagined Speech Decoding via Imagined-to-Listened MEG Mapping
作者: Maryam Maghsoudi, Shihab Shamma
链接: https://arxiv.org/abs/2605.08075v1
完整摘要: Decoding imagined speech from non-invasive brain recordings is challenging because imagined datasets are scarce and difficult to align temporally across subjects and sessions In this work, we propose a new approach to the decoding of imagined speech that leverages the richer and more reliably labeled recordings during listening to speech. We collected paired listened and imagined MEG recordings to rhythmic melodic and spoken stimuli from trained musicians. Using trained musicians helped improve temporal alignment across conditions. We then developed a three-stage decoding pipeline that revealed consistent and meaningful relationships between neural activity evoked by imagining and listening to the same stimuli. First, we trained six linear and neural models to map imagined MEG responses to listened responses. We evaluated these models against a null baseline from unseen subjects to validate that the predicted-listening responses preserve stimulus-specific information. In the second stage, we trained a contrastive word decoder exclusively on the listened MEG responses, and evaluated it using four embedding strategies including semantic, acoustic, and phonetic representations. In the third stage, we process the imagined MEG responses from held-out subjects through the mapping pipeline to compute the corresponding listening responses that are then decoded by the listened decoder. Using rank-based analysis, we show that the imagined words are decodable significantly above chance. We shall report here the results of a proof-of-concept implementation to decode imagined speech, where all evaluations are performed on held-out subjects. We also demonstrate that performance improves with training data size, suggesting that this approach is scalable and can directly be made applicable to realistic brain-computer interface scenarios.
匹配关键词: audio language model
---

[ACADEMIC - ARXIV]
标题: GRAPHLCP: Structure-Aware Localized Conformal Prediction on Graphs
作者: Peyman Baghershahi, Fangxin Wang, Debmalya Mandal, Sourav Medya
链接: https://arxiv.org/abs/2605.08074v1
完整摘要: Conformal prediction (CP) provides a distribution-free approach to uncertainty quantification with finite-sample guarantees. However, applying CP to graph neural networks (GNNs) remains challenging as the combinatorial nature of graphs often leads to insufficiently certain predictions and indiscriminative embeddings. Existing methods primarily rely on embedding-space proximity for localization, which can be unreliable for graphs and yield inefficient prediction sets. We propose GRAPHLCP, a proximity-based localized CP framework that explicitly incorporates graph topology and inter-node dependencies into localization and weighting. Our approach introduces a feature-aware densification step to mitigate locality bias in sparse graphs, followed by a Personalized PageRank-based kernel computation to model structural proximity. This enables topology-dependent anchor sampling and calibration weighting that captures both local and long-range dependencies. Extensive experiments on several regression and classification datasets demonstrate that GRAPHLCP guarantees marginal coverage with finite samples while efficiently attaining favorable test conditional coverage across various conditioning scenarios.
匹配关键词: audio language model
---

[ACADEMIC - ARXIV]
标题: STARFlow2: Bridging Language Models and Normalizing Flows for Unified Multimodal Generation
作者: Ying Shen, Tianrong Chen, Yuan Gao, Yizhe Zhang, Yuyang Wang, Miguel Ángel Bautista, Shuangfei Zhai, Joshua M. Susskind, Jiatao Gu
链接: https://arxiv.org/abs/2605.08029v1
完整摘要: Deep generative models have advanced rapidly across text and vision, motivating unified multimodal systems that can understand, reason over, and generate interleaved text-image sequences. Most existing approaches combine autoregressive language modeling with diffusion-based image generators, inheriting a structural mismatch between causal text generation and iterative visual denoising. We observe that autoregressive normalizing flows are autoregressive Transformers--sharing the same causal mask, KV-cache mechanism, and left-to-right structure as LLMs--making them the most natural paradigm for true unified multimodal generation. We present STARFlow2, built on the Pretzel architecture that vertically interleaves a pretrained VLM stream with a TarFlow stream via residual skip connections, both operating under the same causal mask. Combined with a deep-shallow flow design and a unified FAE latent space, STARFlow2 enables cache-friendly interleaved generation where both text and visual outputs directly enter the KV-cache without re-encoding. Experiments demonstrate strong performance across image generation and multimodal understanding benchmarks, validating autoregressive flows as a viable foundation for unified multimodal modeling.
匹配关键词: KV cache
---

[ACADEMIC - ARXIV]
标题: Semantic-Aware Adaptive Visual Memory for Streaming Video Understanding
作者: Hang Wu, Sherin Mary Mathews, Yujun Cai, Ming-Hsuan Yang, Yiwei Wang
链接: https://arxiv.org/abs/2605.07897v1
完整摘要: Online streaming video understanding requires models to process continuous visual inputs and respond to user queries in real time, where the unbounded stream and unpredictable query timing turn memory management into a central challenge. Existing methods typically compress visual tokens via visual similarity heuristics, or augment compression with KV-cache-level retrieval. However, compression decisions rarely incorporate semantic signals, and retrieval is often added after compression is finalized, making the two stages hard to coordinate. We present SAVEMem, a training-free dual-stage framework that brings semantic awareness into memory generation and lets the retrieval scope adapt per query. In Stage~1, SAVEMem builds a three-tier streaming memory online under a constant memory budget. A fixed pseudo-question bank provides a lightweight semantic prior, so that long-term retention is shaped by semantic salience rather than visual similarity alone. In Stage~2, SAVEMem performs query-aware retrieval over this memory. An anchor-conditioned recency gate adapts the retrieval scope from short-term to mid- and long-term memory based on whether the query targets the present or the distant past. Within this scope, late interaction between query and memory tokens selects candidate frames for answering. Applied to Qwen2.5-VL without training, SAVEMem improves the OVO-Bench overall score from 52.27 to 62.69 and yields consistent gains on StreamingBench and ODV-Bench, while reducing peak GPU memory by 48\% at 128 frames over the backbone.
匹配关键词: KV cache
---

[ACADEMIC - ARXIV]
标题: Memory-Efficient Looped Transformer: Decoupling Compute from Memory in Looped Language Models
作者: Victor Conchello Vendrell, Arnau Padres Masdemont, Niccolò Grillo, Jordi Ros-Giralt, Arash Behboodi, Fabio Valerio Massoli
链接: https://arxiv.org/abs/2605.07721v1
完整摘要: Recurrent LLM architectures have emerged as a promising approach for improving reasoning, as they enable multi-step computation in the embedding space without generating intermediate tokens. Models such as Ouro perform reasoning by iteratively updating internal representations while retaining a standard Key-Value (KV) cache across iterations, causing memory consumption to grow linearly with reasoning depth. Consequently, increasing the number of reasoning iterations can lead to prohibitive memory usage, limiting the practical scalability of such architectures. In this work, we propose Memory-Efficient Looped Transformer (MELT), a novel architecture that decouples reasoning depth from memory consumption. Instead of using a standard KV cache per layer and loop, MELT maintains a single KV cache per layer that is shared across reasoning loops. This cache is updated over time via a learnable gating mechanism. To enable stable and efficient training under this architecture, we propose to train MELT using chunk-wise training in a two phase procedure: interpolated transition, followed by attention-aligned distillation, both from the LoopLM starting model to MELT. Empirically, we show that MELT models fine-tuned from pretrained Ouro parameters outperform standard LLMs of comparable size, while maintaining a memory footprint comparable to those models and dramatically smaller than Ouro's. Overall, MELT achieves constant-memory iterative reasoning without sacrificing LoopLM performance, using only a lightweight post-training procedure.
匹配关键词: KV cache
---

[ACADEMIC - ARXIV]
标题: An Efficient Hybrid Sparse Attention with CPU-GPU Parallelism for Long-Context Inference
作者: Feiyu Yao, Zhixiong Niu, Xiaqing Li, Yongqiang Xiong, Juan Fang, Qian Wang
链接: https://arxiv.org/abs/2605.07719v1
完整摘要: Long-context inference increasingly operates over CPU-resident KV caches, either because decoding-time KV states exceed GPU memory capacity or because disaggregated prefill-decode systems place KV data in host memory. Although block-sparse attention reduces attention cost in this setting, sparsity alone is insufficient for end-to-end efficiency. GPU-only designs remain constrained by PCIe bandwidth and metadata memory overhead, while CPU-GPU hybrid designs still suffer from substantial GPU idle time and bottlenecks in CPU-side top-k selection and sparse attention computation. Fluxion is built on three key insights: output-aware KV budgeting, head-specific and granularity-aware sparse configuration, and cross-device coordinated execution for sparse attention over CPU-resident KV caches. Guided by these insights, Fluxion combines a lightweight head-property predictor, a granularity-budget selector, and a priority-based scheduler to jointly optimize budget allocation, sparse configuration, and CPU-GPU execution overlap. This co-design enables hybrid sparse attention to achieve both accuracy and system efficiency in long-context inference. Across 2 models, 3 benchmarks, and 40 tasks, Fluxion preserves quality well -- the worst average degradation is only -0.26 relative to FULL, while delivering 1.5$\times$-3.7$\times$ speedup over the strongest fixed sparse hybrid baseline, whose KV budget is only 0.05.
匹配关键词: KV cache
---

[ACADEMIC - ARXIV]
标题: Stochastic Transition-Map Distillation for Fast Probabilistic Inference
作者: George Rapakoulias, Peter Garud, Lingjiong Zhu, Panagiotis Tsiotras
链接: https://arxiv.org/abs/2605.07661v1
完整摘要: Diffusion models achieve strong generation quality, diversity, and distribution coverage, but their performance often comes with expensive inference. In this work, we propose Stochastic Transition-Map Distillation (STMD), a teacher-free framework for accelerating diffusion model inference while preserving probabilistic sample generation. In contrast to score-based diffusion models, whose denoising parametrization models the mean of the posterior distribution, STMD distills the full transition map associated with the sampling stochastic differential equation (SDE). We parameterize these SDE transitions with a conditional Mean Flow model, yielding a one- or few-step stochastic sampler that retains the transition structure of the underlying diffusion process. This perspective is especially useful for downstream tasks that require stochastic inference, such as diffusion posterior sampling, inverse problems, and energy-based fine-tuning. Compared to recent distillation methods, STMD requires no pretrained teacher, bi-level optimization, or trajectory simulation and caching, enabling efficient and scalable training. We derive convergence bounds for our method in the Wasserstein distance, providing a strong theoretical foundation for our approach, and validate STMD on various image generation examples on the MNIST, CIFAR-10, and CelebA datasets.
匹配关键词: KV cache
---

[ACADEMIC - ARXIV]
标题: BeeVe: Unsupervised Acoustic State Discovery in Honey Bee Buzzing
作者: Hamze Hammami, Nidhal Abdulaziz
链接: https://arxiv.org/abs/2605.07903v1
完整摘要: Discovering structure in biological signals without supervision is a fundamental problem in computational intelligence, yet existing bioacoustic methods assume vocal production models or predefined semantic units, leaving non-vocal species poorly served. This work introduces BeeVe, an unsupervised framework for acoustic state discovery in collective honey bee buzzing. BeeVe uses the self-supervised Patchout Spectrogram Transformer (PaSST) as a frozen feature extractor, then trains a Vector-Quantized Variational Autoencoder (VQ-VAE) without labels on those embeddings, learning a finite discrete codebook of acoustic tokens directly from unlabelled hive audio. No labels, pretext tasks, or contrastive objectives are used at any stage. Post-hoc evaluation against known queen status reveals that the learned tokens separate queenright and queenless conditions with Jensen-Shannon Divergence values between 0.609 and 0.688, and that the queenless condition further decomposes into three internally coherent sub-states stable across experiments with different codebook sizes and random seeds. Token transition analysis confirms non-random sequential structure (p << 0.001) across all experiments. Generalisation to unseen recordings preserves both token overlap (Jaccard = 0.947) and global manifold topology. These results demonstrate that unsupervised discrete codebook learning can recover repeatable acoustic structure from a non-vocal biological signal without annotation, opening a path toward non-invasive acoustic hive health monitoring.
匹配关键词: quantization
---

[ACADEMIC - ARXIV]
标题: Measuring and Mitigating the Distributional Gap Between Real and Simulated User Behaviors
作者: Shuhaib Mehri, Philippe Laban, Sumuk Shashidhar, Marwa Abdulhai, Sergey Levine, Michel Galley, Dilek Hakkani-Tür
链接: https://arxiv.org/abs/2605.07847v1
完整摘要: As user simulators are increasingly used for interactive training and evaluation of AI assistants, it is essential that they represent the diverse behaviors of real users. While existing works train user simulators to generate human-like responses, whether they capture the broad and heterogeneous distribution of real user behaviors remains an open question. In this work, we introduce a method to measure the distributional gap between real and simulated user behaviors, validated through a human study and ablations. Given a dataset of real and simulated conversations, our method extracts representations of user behavior from each conversation, quantizes them into discrete distributions via clustering, then computes divergence metrics. We provide the first systematic evaluation of 24 LLM-based user simulators on coding and writing tasks, and reveal a large distributional gap from real users that varies across model families, scales, and behavioral facets. Pairwise comparisons show that most simulators behave similarly, while a few stand apart. Combining behaviorally complementary simulators brings the resulting distribution closer to real users compared to either simulator on its own. Finally, a TF-IDF analysis of the clusters surfaces interpretable patterns of behaviors that simulators capture, miss, and hallucinate.
匹配关键词: quantization
---

[ACADEMIC - ARXIV]
标题: Approximation-Free Differentiable Oblique Decision Trees
作者: Subrat Prasad Panda, Blaise Genest, Arvind Easwaran
链接: https://arxiv.org/abs/2605.07837v1
完整摘要: Decision Trees (DTs) are widely used in safety-critical domains such as medical diagnosis, valued for their interpretability and effectiveness on tabular data. However, training accurate oblique DTs is challenging due to complex optimization landscapes and overfitting risks, particularly in regression. Recent advances have introduced differentiable formulations that enable gradient-based training and joint optimization of decision boundaries and leaf regressors. Yet, existing approaches typically rely on approximations, either through probabilistic softening of boundaries (soft DTs) or quantized gradients such as the Straight-Through Estimator (STE). To overcome these limitations, we propose DTSemNet, a novel, semantically equivalent, and invertible representation of hard oblique DTs as neural networks. DTSemNet enables end-to-end training with standard gradient descent, eliminating the need for approximations in both classification and regression. While classification aligns naturally with this formulation, regression remains challenging due to the joint optimization of internal nodes and leaf regressors. To address this, we analyze the limitations of STE and introduce an annealed Top-k method that provides accurate gradient signals without approximation. Extensive experiments on classification and regression benchmarks show that DTSemNet-trained oblique DTs outperform state-of-the-art differentiable DTs. Furthermore, we demonstrate that DTSemNet can serve as programmatic DT policies in reinforcement learning environments, thereby broadening their applicability.
匹配关键词: quantization
---

[ACADEMIC - ARXIV]
标题: CommandSwarm: Safety-Aware Natural Language-to-Behavior-Tree Generation for Robotic Swarms
作者: Mohammed Majid, Amjad Yousef Majid
链接: https://arxiv.org/abs/2605.07764v1
完整摘要: Natural-language interfaces can make swarm robotics more accessible to non-expert operators, but they must translate ambiguous user intent into executable swarm behaviors without unsupported actions, malformed programs, or unsafe plans. This paper presents CommandSwarm, a safety-aware language-to-behavior-tree pipeline for generating XML behavior trees (BTs) from speech or text commands. The system combines multilingual translation, command-level safety filtering, constrained prompting, a LoRA-adapted large language model (LLM), and deterministic parser validation against a whitelist of executable swarm primitives. We evaluate eleven open 6.7B--14B parameter LLMs, all using 4-bit quantization, on representative swarm-control scenarios under zero-shot, one-shot, and two-shot prompting. Falcon3-Instruct-10B and Mistral-7B-v3 are the strongest prompt-engineered candidates, reaching BLEU scores above 0.60 and high syntactic validity in few-shot settings. LoRA adaptation of Falcon3-Instruct-10B on a 2,063-example synthetic instruction--BT corpus improves zero-shot BLEU from 0.267 to 0.663, ROUGE-L from 0.366 to 0.692, and parser-accepted syntactic validity from 0% to 72%. Translation experiments further show that SeamlessM4T v2-large and EuroLLM-9B provide the best quality-latency trade-offs for the multilingual front end. The results indicate that compact, quantized, domain-adapted LLMs can generate useful swarm BTs when embedded in a validated systems pipeline. They also show that parser acceptance and safety filtering remain necessary execution gates; generation quality alone is not sufficient for autonomous deployment.
匹配关键词: quantization
---

[ACADEMIC - ARXIV]
标题: Task-Oriented Communication for Human Action Understanding via Edge-Cloud Co-Inference
作者: Jingyi Liu, Cheng Yuan, Lijun He, Jun Zhang, Jiawei Shao
链接: https://arxiv.org/abs/2605.07354v1
完整摘要: The expanding application of smart sensing has created a growing demand for the accurate understanding of human action at the network edge. Traditional approaches require massive video data to be transmitted from resource-constrained edge devices to powerful cloud servers, incurring prohibitive uplink bandwidth consumption and unacceptable latency while raising privacy concerns. To overcome these bottlenecks, we propose a task-oriented communication framework for human action understanding (TOAU) through edge-cloud collaboration. Our framework utilizes a monocular pose estimator to extract continuous joint coordinates from raw videos, followed by a vector quantized variational autoencoder (VQ-VAE) to convert these coordinates into discrete motion tokens. Consequently, only a compact sequence of codebook indices is transmitted over the network, consuming as few as 9 bits per frame and avoiding privacy leakages. At the cloud server, a lightweight projector aligns these motion tokens with the embedding space of a large vision-language model (VLM) to facilitate complex action understanding, which is trained with an efficient instruction tuning paradigm. Comprehensive evaluations on three benchmarks demonstrate that our TOAU system reduces the transmission payload to approximately 1\% and the system latency to around 20\% compared to video codec-based solutions, while delivering comparable action understanding accuracy.
匹配关键词: quantization
---

[ACADEMIC - ARXIV]
标题: Zero-Shot Imagined Speech Decoding via Imagined-to-Listened MEG Mapping
作者: Maryam Maghsoudi, Shihab Shamma
链接: https://arxiv.org/abs/2605.08075v1
完整摘要: Decoding imagined speech from non-invasive brain recordings is challenging because imagined datasets are scarce and difficult to align temporally across subjects and sessions In this work, we propose a new approach to the decoding of imagined speech that leverages the richer and more reliably labeled recordings during listening to speech. We collected paired listened and imagined MEG recordings to rhythmic melodic and spoken stimuli from trained musicians. Using trained musicians helped improve temporal alignment across conditions. We then developed a three-stage decoding pipeline that revealed consistent and meaningful relationships between neural activity evoked by imagining and listening to the same stimuli. First, we trained six linear and neural models to map imagined MEG responses to listened responses. We evaluated these models against a null baseline from unseen subjects to validate that the predicted-listening responses preserve stimulus-specific information. In the second stage, we trained a contrastive word decoder exclusively on the listened MEG responses, and evaluated it using four embedding strategies including semantic, acoustic, and phonetic representations. In the third stage, we process the imagined MEG responses from held-out subjects through the mapping pipeline to compute the corresponding listening responses that are then decoded by the listened decoder. Using rank-based analysis, we show that the imagined words are decodable significantly above chance. We shall report here the results of a proof-of-concept implementation to decode imagined speech, where all evaluations are performed on held-out subjects. We also demonstrate that performance improves with training data size, suggesting that this approach is scalable and can directly be made applicable to realistic brain-computer interface scenarios.
匹配关键词: speculative decoding
---

[ACADEMIC - ARXIV]
标题: Fast Byte Latent Transformer
作者: Julie Kallini, Artidoro Pagnoni, Tomasz Limisiewicz, Gargi Ghosh, Luke Zettlemoyer, Christopher Potts, Xiaochuang Han, Srinivasan Iyer
链接: https://arxiv.org/abs/2605.08044v1
完整摘要: Recent byte-level language models (LMs) match the performance of token-level models without relying on subword vocabularies, yet their utility is limited by slow, byte-by-byte autoregressive generation. We address this bottleneck in the Byte Latent Transformer (BLT) through new training and generation techniques. First, we introduce BLT Diffusion (BLT-D), a new model and our fastest BLT variant, trained with an auxiliary block-wise diffusion objective alongside the standard next-byte prediction loss. This enables an inference procedure that generates multiple bytes in parallel per decoding step, substantially reducing the number of forward passes required to generate a sequence. Second, we propose two extensions inspired by speculative decoding that trade some of this speed for higher generation quality: BLT Self-speculation (BLT-S), in which BLT's local decoder continues generating past its normal patch boundaries to draft bytes, which are then verified with a single full-model forward pass; and BLT Diffusion+Verification (BLT-DV), which augments BLT-D with an autoregressive verification step after diffusion-based generation. All methods may achieve an estimated memory-bandwidth cost over 50% lower than BLT on generation tasks. Each approach offers its own unique advantages, together removing key barriers to the practical use of byte-level LMs.
匹配关键词: speculative decoding
---

[ACADEMIC - ARXIV]
标题: Object Hallucination-Free Reinforcement Unlearning for Vision-Language Models
作者: Kaidi Jia, Yujie Lin, Chengyi Yang, Jiayao Ma, Jinsong Su
链接: https://arxiv.org/abs/2605.08031v1
完整摘要: Vision-language models (VLMs) raise growing concerns about privacy, copyright, and bias, motivating machine unlearning to remove sensitive knowledge. However, existing methods primarily fine-tune the language decoder, leading to superficial forgetting that fails to erase underlying visual representations and often introduces object hallucination. We propose HFRU, a reinforcement unlearning framework that operates on the vision encoder for deep semantic removal. Our two-stage approach combines alignment disruption with GRPO-based optimization using a composite reward, including an abstraction reward that encourages semantically valid substitutions and mitigates hallucinations. Experiments on object recognition and face identity tasks show that HFRU achieves over 98% forgetting and retention performance, while introducing negligible object hallucination, significantly outperforming prior methods.Our code and implementation details are available at https://github.com/XMUDeepLIT/HFRU.
匹配关键词: speculative decoding
---

[ACADEMIC - ARXIV]
标题: Where's the Plan? Locating Latent Planning in Language Models with Lightweight Mechanistic Interventions
作者: Nicole Ma, Nick Rui
链接: https://arxiv.org/abs/2605.07984v1
完整摘要: We study planning site formation in language models -- where internal representations of structurally-constrained future tokens form during the forward pass, and whether they causally drive generation. Using rhyming-couplet completion as a clean test of forward-looking constraint, we apply two lightweight methods (linear probing and activation patching) across Qwen3, Gemma-3, and Llama-3 at more than ten scales. Probing shows that future-rhyme information is linearly decodable at the line boundary, with signal that strengthens with scale in all three families. Activation patching reveals that only Gemma-3-27B causally relies on this encoding, exhibiting a handoff in which the causal driver migrates from the rhyme word to the line boundary around layer 30. Every other model we test conditions on the rhyme word throughout generation, with near-zero causal effect at the line boundary despite strong probe signal. We localize the Gemma-3-27B handoff to five attention heads through two-stage path patching that recover ~90% of the rhyme-routing capacity at the newline.
匹配关键词: speculative decoding
---

[ACADEMIC - ARXIV]
标题: GLiGuard: Schema-Conditioned Classification for LLM Safeguard
作者: Urchade Zaratiana, Mary Newhauser, George Hurn-Maloney, Ash Lewis
链接: https://arxiv.org/abs/2605.07982v1
完整摘要: Ensuring safe, policy-compliant outputs from large language models requires real-time content moderation that can scale across multiple safety dimensions. However, state-of-the-art guardrail models rely on autoregressive decoders with 7B--27B parameters, reformulating what is fundamentally a classification problem as sequential text generation, a design choice that incurs high latency and scales poorly to multi-aspect evaluation. In this work, we introduce \textbf{GLiGuard}, a 0.3B-parameter schema-conditioned bidirectional encoder adapted from GLiNER2 for LLM content moderation. The key idea is to encode task definitions and label semantics directly into the input sequence as structured token schemas, enabling simultaneous evaluation of prompt safety, response safety, refusal detection, 14 fine-grained harm categories, and 11 jailbreak strategies in a single non-autoregressive forward pass. This schema-conditioned design lets supported task and label blocks be composed directly in the input schema at inference time. Across nine established safety benchmarks, GLiGuard achieves F1 scores competitive with 7B--27B decoder-based guards despite being 23--90$\times$ smaller, while delivering up to 16$\times$ higher throughput and 17$\times$ lower latency. These results suggest that compact bidirectional encoders can approach the accuracy of much larger guard models while drastically reducing inference cost. Code and models are available at https://github.com/fastino-ai/GLiGuard.
匹配关键词: speculative decoding
---

[ACADEMIC - ARXIV]
标题: GRAPHLCP: Structure-Aware Localized Conformal Prediction on Graphs
作者: Peyman Baghershahi, Fangxin Wang, Debmalya Mandal, Sourav Medya
链接: https://arxiv.org/abs/2605.08074v1
完整摘要: Conformal prediction (CP) provides a distribution-free approach to uncertainty quantification with finite-sample guarantees. However, applying CP to graph neural networks (GNNs) remains challenging as the combinatorial nature of graphs often leads to insufficiently certain predictions and indiscriminative embeddings. Existing methods primarily rely on embedding-space proximity for localization, which can be unreliable for graphs and yield inefficient prediction sets. We propose GRAPHLCP, a proximity-based localized CP framework that explicitly incorporates graph topology and inter-node dependencies into localization and weighting. Our approach introduces a feature-aware densification step to mitigate locality bias in sparse graphs, followed by a Personalized PageRank-based kernel computation to model structural proximity. This enables topology-dependent anchor sampling and calibration weighting that captures both local and long-range dependencies. Extensive experiments on several regression and classification datasets demonstrate that GRAPHLCP guarantees marginal coverage with finite samples while efficiently attaining favorable test conditional coverage across various conditioning scenarios.
匹配关键词: kernel optimization
---

[ACADEMIC - ARXIV]
标题: Flow-OPD: On-Policy Distillation for Flow Matching Models
作者: Zhen Fang, Wenxuan Huang, Yu Zeng, Yiming Zhao, Shuang Chen, Kaituo Feng, Yunlong Lin, Lin Chen, Zehui Chen, Shaosheng Cao, Feng Zhao
链接: https://arxiv.org/abs/2605.08063v1
完整摘要: Existing Flow Matching (FM) text-to-image models suffer from two critical bottlenecks under multi-task alignment: the reward sparsity induced by scalar-valued rewards, and the gradient interference arising from jointly optimizing heterogeneous objectives, which together give rise to a 'seesaw effect' of competing metrics and pervasive reward hacking. Inspired by the success of On-Policy Distillation (OPD) in the large language model community, we propose Flow-OPD, the first unified post-training framework that integrates on-policy distillation into Flow Matching models. Flow-OPD adopts a two-stage alignment strategy: it first cultivates domain-specialized teacher models via single-reward GRPO fine-tuning, allowing each expert to reach its performance ceiling in isolation; it then establishes a robust initial policy through a Flow-based Cold-Start scheme and seamlessly consolidates heterogeneous expertise into a single student via a three-step orchestration of on-policy sampling, task-routing labeling, and dense trajectory-level supervision. We further introduce Manifold Anchor Regularization (MAR), which leverages a task-agnostic teacher to provide full-data supervision that anchors generation to a high-quality manifold, effectively mitigating the aesthetic degradation commonly observed in purely RL-driven alignment. Built upon Stable Diffusion 3.5 Medium, Flow-OPD raises the GenEval score from 63 to 92 and the OCR accuracy from 59 to 94, yielding an overall improvement of roughly 10 points over vanilla GRPO, while preserving image fidelity and human-preference alignment and exhibiting an emergent 'teacher-surpassing' effect. These results establish Flow-OPD as a scalable alignment paradigm for building generalist text-to-image models.
匹配关键词: kernel optimization
---

[ACADEMIC - ARXIV]
标题: Rubric-Grounded RL: Structured Judge Rewards for Generalizable Reasoning
作者: Manish Bhattarai, Ismael Boureima, Nishath Rajiv Ranasinghe, Scott Pakin, Dan O'Malley
链接: https://arxiv.org/abs/2605.08061v1
完整摘要: We argue that decomposing reward into weighted, verifiable criteria and using an LLM judge to score them provides a partial-credit optimization signal: instead of a binary outcome or a single holistic score, each response is graded along multiple task-specific criteria. We formalize \emph{rubric-grounded reinforcement learning (RL)}: a framework in which the policy is optimized against a structured, multi-criterion reward produced by a frozen LLM judge that conditions on auxiliary grounding the policy never sees. We instantiate the framework by deriving rubrics from an Office of Scientific and Technical Information (OSTI)-derived corpus of roughly 100,000 scientific and technical documents and training Llama-3.1-8B-Instruct with Group Relative Policy Optimization (GRPO). With GRPO-based training, the model achieves $71.7\%$ normalized reward on held-out rubric evaluation. The GRPO-tuned policy also improves over the base model on four reasoning benchmarks not derived from the training corpus -- GSM8K, MATH, GPQA Main, and GPQA Diamond. These results provide evidence that structured, document-grounded rewards can improve held-out rubric performance and induce transferable reasoning behaviors beyond the corpus used to construct the training environment.
匹配关键词: kernel optimization
---

[ACADEMIC - ARXIV]
标题: Towards Highly-Constrained Human Motion Generation with Retrieval-Guided Diffusion Noise Optimization
作者: Hanchao Liu, Fang-Lue Zhang, Shining Zhang, Tai-Jiang Mu, Shi-Min Hu
链接: https://arxiv.org/abs/2605.08054v1
完整摘要: Generating human motion that satisfies customized zero-shot goal functions, enabling applications such as controllable character animation and behavior synthesis for virtual agents, is a critical capability. While current approaches handle many unseen constraints, they fail on tasks with very challenging spatiotemporal restrictions, such as severe spatial obstacles or specified numbers of walking steps. To equip motion generators for these highly constrained tasks, we present a retrieval-guided method built on the training-free diffusion noise optimization framework. The key idea is to search within large motion datasets for guidance that can potentially satisfy difficult constraints. We introduce relational task parsing to group target constraints and identify the difficult ones to be handled by retrieved reference. A better initialization for diffusion noise is then obtained via a reward-guided mask that combines random noise with retrieved noise. By optimizing diffusion noise from this improved initialization, we successfully solve highly constrained generation tasks. By leveraging LLM for relational task parsing, the whole framework is further enabled to automatically reason for what to retrieve, improving the intelligence of moving agents under a training-free optimization scheme.
匹配关键词: kernel optimization
---

[ACADEMIC - ARXIV]
标题: Reinforcement Learning for Exponential Utility: Algorithms and Convergence in Discounted MDPs
作者: Gugan Thoppe, L. A. Prashanth, Ankur Naskar, Sanjay Bhat
链接: https://arxiv.org/abs/2605.08053v1
完整摘要: Reinforcement learning (RL) for exponential-utility optimization in discounted Markov decision processes (MDPs) lacks principled value-based algorithms. We address this gap in the fixed risk-aversion setting. Building on the Bellman-type equation for exponential utility studied in \cite{porteus1975optimality}, we derive two Q-value-style extensions and show that the associated operators are contractions in the $L_\infty$ and sup-log/Thompson metrics, respectively. We characterize their fixed points and prove that the induced greedy stationary policy is optimal for the exponential-utility objective among stationary policies. These structural results lead to two model-free algorithms: a two-timescale Q-learning--style algorithm, for which we establish almost-sure convergence and provide finite-time convergence rates via timescale separation, and a one-timescale algorithm governed by a sublinear power-law operator. Since the latter does not admit a global contraction in standard metrics, we prove its convergence using delicate arguments based on local Lipschitzness, monotonicity, homogeneity, and Dini derivatives, and provide a scalar finite-time analysis that highlights the challenges in obtaining convergence rates in the vector case. Our work provides a foundation for value-based RL under exponential-utility objectives.
匹配关键词: kernel optimization
---

[ACADEMIC - ARXIV]
标题: LLMs Improving LLMs: Agentic Discovery for Test-Time Scaling
作者: Tong Zheng, Haolin Liu, Chengsong Huang, Huiwen Bao, Sheng Zhang, Rui Liu, Runpeng Dai, Ruibo Chen, Chenxi Liu, Tianyi Xiong, Xidong Wu, Hongming Zhang, Heng Huang
链接: https://arxiv.org/abs/2605.08083v1
完整摘要: Test-time scaling (TTS) has become an effective approach for improving large language model performance by allocating additional computation during inference. However, existing TTS strategies are largely hand-crafted: researchers manually design reasoning patterns and tune heuristics by intuition, leaving much of the computation-allocation space unexplored. We propose an environment-driven framework, AutoTTS, that changes what researchers design: from individual TTS heuristics to environments where TTS strategies can be discovered automatically. The key to AutoTTS lies in environment construction: the discovery environment must make the control space tractable and provide cheap, frequent feedback for TTS search. As a concrete instantiation, we formulate width--depth TTS as controller synthesis over pre-collected reasoning trajectories and probe signals, where controllers decide when to branch, continue, probe, prune, or stop and can be evaluated cheaply without repeated LLM calls. We further introduce beta parameterization to make the search tractable and fine-grained execution trace feedback to improve discovery efficiency by helping the agent diagnose why a TTS program fails. Experiments on mathematical reasoning benchmarks show that the discovered strategies improve the overall accuracy--cost tradeoff over strong manually designed baselines. The discovered strategies generalize to held-out benchmarks and model scales, while the entire discovery costs only $39.9 and 160 minutes. Our data, and code will be open-source at https://github.com/zhengkid/AutoTTS.
匹配关键词: memory efficiency
---

[ACADEMIC - ARXIV]
标题: GRAPHLCP: Structure-Aware Localized Conformal Prediction on Graphs
作者: Peyman Baghershahi, Fangxin Wang, Debmalya Mandal, Sourav Medya
链接: https://arxiv.org/abs/2605.08074v1
完整摘要: Conformal prediction (CP) provides a distribution-free approach to uncertainty quantification with finite-sample guarantees. However, applying CP to graph neural networks (GNNs) remains challenging as the combinatorial nature of graphs often leads to insufficiently certain predictions and indiscriminative embeddings. Existing methods primarily rely on embedding-space proximity for localization, which can be unreliable for graphs and yield inefficient prediction sets. We propose GRAPHLCP, a proximity-based localized CP framework that explicitly incorporates graph topology and inter-node dependencies into localization and weighting. Our approach introduces a feature-aware densification step to mitigate locality bias in sparse graphs, followed by a Personalized PageRank-based kernel computation to model structural proximity. This enables topology-dependent anchor sampling and calibration weighting that captures both local and long-range dependencies. Extensive experiments on several regression and classification datasets demonstrate that GRAPHLCP guarantees marginal coverage with finite samples while efficiently attaining favorable test conditional coverage across various conditioning scenarios.
匹配关键词: memory efficiency
---

[ACADEMIC - ARXIV]
标题: EmambaIR: Efficient Visual State Space Model for Event-guided Image Reconstruction
作者: Wei Yu, Yunhang Qian
链接: https://arxiv.org/abs/2605.08073v1
完整摘要: Recent event-based image reconstruction methods predominantly rely on Convolutional Neural Networks (CNNs) and Vision Transformers (ViTs) to process complementary event information. However, these architectures face fundamental limitations: CNNs often fail to capture global feature correlations, whereas ViTs incur quadratic computational complexity (e.g., $O(n^2)$), hindering their application in high-resolution scenarios. To address these bottlenecks, we introduce EmambaIR, an Efficient visual State Space Model designed for image reconstruction using spatially sparse and temporally continuous event streams. Our framework introduces two key components: the cross-modal Top-k Sparse Attention Module (TSAM) and the Gated State-Space Module (GSSM). TSAM efficiently performs pixel-level top-k sparse attention to guide cross-modal interactions, yielding rich yet sparse fusion features. Subsequently, GSSM utilizes a nonlinear gated unit to enhance the temporal representation of vanilla linear-complexity ($O(n)$) SSMs, effectively capturing global contextual dependencies without the typical computational overhead. Extensive experiments on six datasets across three diverse image reconstruction tasks - motion deblurring, deraining, and High Dynamic Range (HDR) enhancement - demonstrate that EmambaIR significantly outperforms state-of-the-art methods while offering substantial reductions in memory consumption and computational cost. The source code and data are publicly available at: https://github.com/YunhangWickert/EmambaIR
匹配关键词: memory efficiency
---

[ACADEMIC - ARXIV]
标题: Proxy3D: Efficient 3D Representations for Vision-Language Models via Semantic Clustering and Alignment
作者: Jerry Jiang, Haowen Sun, Denis Gudovskiy, Yohei Nakata, Tomoyuki Okuno, Kurt Keutzer, Wenzhao Zheng
链接: https://arxiv.org/abs/2605.08064v1
完整摘要: Spatial intelligence in vision-language models (VLMs) attracts research interest with the practical demand to reason in the 3D world.Despite promising results, most existing methods follow the conventional 2D pipeline in VLMs and use pixel-aligned representations for the vision modality. However, correspondence-based models with implicit 3D scene understanding often fail to achieve spatial consistency, and representation-based models with 3D geometric priors lack efficiency in vision sequence serialization. To address this, we propose a Proxy3D method with compact yet comprehensive 3D proxy representations for the vision modality. Given only video frames as input, we employ semantic and geometric encoders to extract scene features and then perform their semantic-aware clustering to obtain a set of proxies in the 3D space. For representation alignment, we further curate the SpaceSpan dataset and apply multi-stage training to adopt the proposed 3D proxy representations with the VLM. When using shorter sequences for vision information, our method achieves competitive or state-of-the-art performance in 3D visual question answering, visual grounding and general spatial intelligence benchmarks.
匹配关键词: memory efficiency
---

[ACADEMIC - ARXIV]
标题: The Memory Curse: How Expanded Recall Erodes Cooperative Intent in LLM Agents
作者: Jiayuan Liu, Tianqin Li, Shiyi Du, Xin Luo, Haoxuan Zeng, Emanuel Tewolde, Tai Sing Lee, Tonghan Wang, Carl Kingsford, Vincent Conitzer
链接: https://arxiv.org/abs/2605.08060v1
完整摘要: Context window expansion is often treated as a straightforward capability upgrade for LLMs, but we find it systematically fails in multi-agent social dilemmas. Across 7 LLMs and 4 games over 500 rounds, expanding accessible history degrades cooperation in 18 of 28 model--game settings, a pattern we term the memory curse. We isolate the underlying mechanism through three analyses. First, lexical analysis of 378,000 reasoning traces associates this breakdown with eroding forward-looking intent rather than rising paranoia. We validate this using targeted fine-tuning as a cognitive probe: a LoRA adapter trained exclusively on forward-looking traces mitigates the decay and transfers zero-shot to distinct games. Second, memory sanitization holds prompt length fixed while replacing visible history with synthetic cooperative records, which restores cooperation substantially, proving the trigger is memory content, not length alone. Finally, ablating explicit Chain-of-Thought reasoning often reduces the collapse, showing that deliberation paradoxically amplifies the memory curse. Together, these results recast memory as an active determinant of multi-agent behavior: longer recall can either destabilize or support cooperation depending on the reasoning patterns it elicits.
匹配关键词: memory efficiency
---

[ACADEMIC - ARXIV]
标题: LLMs Improving LLMs: Agentic Discovery for Test-Time Scaling
作者: Tong Zheng, Haolin Liu, Chengsong Huang, Huiwen Bao, Sheng Zhang, Rui Liu, Runpeng Dai, Ruibo Chen, Chenxi Liu, Tianyi Xiong, Xidong Wu, Hongming Zhang, Heng Huang
链接: https://arxiv.org/abs/2605.08083v1
完整摘要: Test-time scaling (TTS) has become an effective approach for improving large language model performance by allocating additional computation during inference. However, existing TTS strategies are largely hand-crafted: researchers manually design reasoning patterns and tune heuristics by intuition, leaving much of the computation-allocation space unexplored. We propose an environment-driven framework, AutoTTS, that changes what researchers design: from individual TTS heuristics to environments where TTS strategies can be discovered automatically. The key to AutoTTS lies in environment construction: the discovery environment must make the control space tractable and provide cheap, frequent feedback for TTS search. As a concrete instantiation, we formulate width--depth TTS as controller synthesis over pre-collected reasoning trajectories and probe signals, where controllers decide when to branch, continue, probe, prune, or stop and can be evaluated cheaply without repeated LLM calls. We further introduce beta parameterization to make the search tractable and fine-grained execution trace feedback to improve discovery efficiency by helping the agent diagnose why a TTS program fails. Experiments on mathematical reasoning benchmarks show that the discovered strategies improve the overall accuracy--cost tradeoff over strong manually designed baselines. The discovered strategies generalize to held-out benchmarks and model scales, while the entire discovery costs only $39.9 and 160 minutes. Our data, and code will be open-source at https://github.com/zhengkid/AutoTTS.
匹配关键词: agent
---

[ACADEMIC - ARXIV]
标题: The Memory Curse: How Expanded Recall Erodes Cooperative Intent in LLM Agents
作者: Jiayuan Liu, Tianqin Li, Shiyi Du, Xin Luo, Haoxuan Zeng, Emanuel Tewolde, Tai Sing Lee, Tonghan Wang, Carl Kingsford, Vincent Conitzer
链接: https://arxiv.org/abs/2605.08060v1
完整摘要: Context window expansion is often treated as a straightforward capability upgrade for LLMs, but we find it systematically fails in multi-agent social dilemmas. Across 7 LLMs and 4 games over 500 rounds, expanding accessible history degrades cooperation in 18 of 28 model--game settings, a pattern we term the memory curse. We isolate the underlying mechanism through three analyses. First, lexical analysis of 378,000 reasoning traces associates this breakdown with eroding forward-looking intent rather than rising paranoia. We validate this using targeted fine-tuning as a cognitive probe: a LoRA adapter trained exclusively on forward-looking traces mitigates the decay and transfers zero-shot to distinct games. Second, memory sanitization holds prompt length fixed while replacing visible history with synthetic cooperative records, which restores cooperation substantially, proving the trigger is memory content, not length alone. Finally, ablating explicit Chain-of-Thought reasoning often reduces the collapse, showing that deliberation paradoxically amplifies the memory curse. Together, these results recast memory as an active determinant of multi-agent behavior: longer recall can either destabilize or support cooperation depending on the reasoning patterns it elicits.
匹配关键词: agent
---

[ACADEMIC - ARXIV]
标题: Towards Highly-Constrained Human Motion Generation with Retrieval-Guided Diffusion Noise Optimization
作者: Hanchao Liu, Fang-Lue Zhang, Shining Zhang, Tai-Jiang Mu, Shi-Min Hu
链接: https://arxiv.org/abs/2605.08054v1
完整摘要: Generating human motion that satisfies customized zero-shot goal functions, enabling applications such as controllable character animation and behavior synthesis for virtual agents, is a critical capability. While current approaches handle many unseen constraints, they fail on tasks with very challenging spatiotemporal restrictions, such as severe spatial obstacles or specified numbers of walking steps. To equip motion generators for these highly constrained tasks, we present a retrieval-guided method built on the training-free diffusion noise optimization framework. The key idea is to search within large motion datasets for guidance that can potentially satisfy difficult constraints. We introduce relational task parsing to group target constraints and identify the difficult ones to be handled by retrieved reference. A better initialization for diffusion noise is then obtained via a reward-guided mask that combines random noise with retrieved noise. By optimizing diffusion noise from this improved initialization, we successfully solve highly constrained generation tasks. By leveraging LLM for relational task parsing, the whole framework is further enabled to automatically reason for what to retrieve, improving the intelligence of moving agents under a training-free optimization scheme.
匹配关键词: agent
---

[ACADEMIC - ARXIV]
标题: Reason to Play: Behavioral and Brain Alignment Between Frontier LRMs and Human Game Learners
作者: Botos Csaba, Sreejan Kumar, Austin Tudor David Andrews, Laurence Hunt, Chris Summerfield, Joshua B. Tenenbaum, Rui Ponte Costa, Marcelo G. Mattar, Momchil Tomov
链接: https://arxiv.org/abs/2605.08019v1
完整摘要: Humans rapidly learn abstract knowledge when encountering novel environments and flexibly deploy this knowledge to guide efficient and intelligent action. Can modern AI systems learn and plan in a similar way? We study this question using a dataset of complex human gameplay with concurrent fMRI recordings, in which participants learn novel video games that require rule discovery, hypothesis revision, and multi-step planning. We jointly evaluate models by their ability to play the games, match human learning behavior, and predict brain activity during the same task, comparing a suite of frontier Large Reasoning Models (LRMs) against model-free and model-based deep reinforcement learning agents and a Bayesian theory-based agent. We find that frontier LRMs most closely match human behavioral patterns during game discovery and predict brain activity an order of magnitude better than both reinforcement learning alternatives across cortical and subcortical regions, with effects robust to permutation controls. Through targeted manipulations, we further show that brain alignment reflects the model's in-context representation of the game state rather than its downstream planning or reasoning. Our results establish LRMs as compelling computational accounts of human learning and decision making in complex, naturalistic environments. Project page with interactive replays: https://botcs.github.io/reason-to-play/
匹配关键词: agent
---

[ACADEMIC - ARXIV]
标题: Learning CLI Agents with Structured Action Credit under Selective Observation
作者: Haoyang Su, Ying Wen
链接: https://arxiv.org/abs/2605.08013v1
完整摘要: Command line interface (CLI) agents are emerging as a practical paradigm for agent-computer interaction over evolving filesystems, executable command line programs, and online execution feedback. Recent work has used reinforcement learning (RL) to learn these interaction abilities from verifiable task feedback, yet few methods exploit the native structured attributes of CLI actions as learning signals. Beyond this underused action structure, CLI learning also couples two bottlenecks for coding agents. First, the agent must identify task-relevant evidence in a large codebase from partial observations. Second, sparse terminal rewards must be assigned to the actions that shape a long multi-turn trajectory. We study these bottlenecks through shell-driven information extraction and file editing tasks. For selective observation, we introduce $σ$-Reveal, an inference-time mechanism that selects token-budgeted context for the same CLI. For credit assignment, we propose Action Advantage Assignment ($\mathrm{A}^3$), a native agentic RL method that preserves the algorithmic complexity of standard agentic RL. $\mathrm{A}^3$ constructs turn-level advantages from episode-level relative feedback, abstract syntax tree (AST) based action sub-chain residuals, and tree-level trajectory margins. To further evaluate this problem setting, we construct ShellOps, a verifiable dataset suite covering CLI tasks in repository environments.
匹配关键词: agent
---

[ACADEMIC - ARXIV]
标题: 123D: Unifying Multi-Modal Autonomous Driving Data at Scale
作者: Daniel Dauner, Valentin Charraut, Bastian Berle, Tianyu Li, Long Nguyen, Jiabao Wang, Changhui Jing, Maximilian Igl, Holger Caesar, Boris Ivanovic, Yiyi Liao, Andreas Geiger, Kashyap Chitta
链接: https://arxiv.org/abs/2605.08084v1
完整摘要: The pursuit of autonomous driving has produced one of the richest sensor data collections in all of robotics. However, its scale and diversity remain largely untapped. Each dataset adopts different 2D and 3D modalities, such as cameras, lidar, ego states, annotations, traffic lights, and HD maps, with different rates and synchronization schemes. They come in fragmented formats requiring complex dependencies that cannot natively coexist in the same development environment. Further, major inconsistencies in annotation conventions prevent training or measuring generalization across multiple datasets. We present 123D, an open-source framework that unifies such multi-modal driving data through a single API. To handle synchronization, we store each modality as an independent timestamped event stream with no prescribed rate, enabling synchronous or asynchronous access across arbitrary datasets. Using 123D, we consolidate eight real-world driving datasets spanning 3,300 hours and 90,000 kilometers, together with a synthetic dataset with configurable collection scripts, and provide tools for data analysis and visualization. We conduct a systematic study comparing annotation statistics and assessing each dataset's pose and calibration accuracy. Further, we showcase two applications 123D enables: cross-dataset 3D object detection transfer and reinforcement learning for planning, and offer recommendations for future directions. Code and documentation are available at https://github.com/kesai-labs/py123d.
匹配关键词: tool use
---

[ACADEMIC - ARXIV]
标题: Zero-Shot Imagined Speech Decoding via Imagined-to-Listened MEG Mapping
作者: Maryam Maghsoudi, Shihab Shamma
链接: https://arxiv.org/abs/2605.08075v1
完整摘要: Decoding imagined speech from non-invasive brain recordings is challenging because imagined datasets are scarce and difficult to align temporally across subjects and sessions In this work, we propose a new approach to the decoding of imagined speech that leverages the richer and more reliably labeled recordings during listening to speech. We collected paired listened and imagined MEG recordings to rhythmic melodic and spoken stimuli from trained musicians. Using trained musicians helped improve temporal alignment across conditions. We then developed a three-stage decoding pipeline that revealed consistent and meaningful relationships between neural activity evoked by imagining and listening to the same stimuli. First, we trained six linear and neural models to map imagined MEG responses to listened responses. We evaluated these models against a null baseline from unseen subjects to validate that the predicted-listening responses preserve stimulus-specific information. In the second stage, we trained a contrastive word decoder exclusively on the listened MEG responses, and evaluated it using four embedding strategies including semantic, acoustic, and phonetic representations. In the third stage, we process the imagined MEG responses from held-out subjects through the mapping pipeline to compute the corresponding listening responses that are then decoded by the listened decoder. Using rank-based analysis, we show that the imagined words are decodable significantly above chance. We shall report here the results of a proof-of-concept implementation to decode imagined speech, where all evaluations are performed on held-out subjects. We also demonstrate that performance improves with training data size, suggesting that this approach is scalable and can directly be made applicable to realistic brain-computer interface scenarios.
匹配关键词: tool use
---

[ACADEMIC - ARXIV]
标题: EmambaIR: Efficient Visual State Space Model for Event-guided Image Reconstruction
作者: Wei Yu, Yunhang Qian
链接: https://arxiv.org/abs/2605.08073v1
完整摘要: Recent event-based image reconstruction methods predominantly rely on Convolutional Neural Networks (CNNs) and Vision Transformers (ViTs) to process complementary event information. However, these architectures face fundamental limitations: CNNs often fail to capture global feature correlations, whereas ViTs incur quadratic computational complexity (e.g., $O(n^2)$), hindering their application in high-resolution scenarios. To address these bottlenecks, we introduce EmambaIR, an Efficient visual State Space Model designed for image reconstruction using spatially sparse and temporally continuous event streams. Our framework introduces two key components: the cross-modal Top-k Sparse Attention Module (TSAM) and the Gated State-Space Module (GSSM). TSAM efficiently performs pixel-level top-k sparse attention to guide cross-modal interactions, yielding rich yet sparse fusion features. Subsequently, GSSM utilizes a nonlinear gated unit to enhance the temporal representation of vanilla linear-complexity ($O(n)$) SSMs, effectively capturing global contextual dependencies without the typical computational overhead. Extensive experiments on six datasets across three diverse image reconstruction tasks - motion deblurring, deraining, and High Dynamic Range (HDR) enhancement - demonstrate that EmambaIR significantly outperforms state-of-the-art methods while offering substantial reductions in memory consumption and computational cost. The source code and data are publicly available at: https://github.com/YunhangWickert/EmambaIR
匹配关键词: tool use
---

[ACADEMIC - ARXIV]
标题: A Note on Non-Negative $L_1$-Approximating Polynomials
作者: Jane H. Lee, Anay Mehrotra, Manolis Zampetakis
链接: https://arxiv.org/abs/2605.08072v1
完整摘要: $L_1$-Approximating polynomials, i.e., polynomials that approximate indicator functions in $L_1$-norm under certain distributions, are widely used in computational learning theory. We study the existence of \textit{non-negative} $L_1$-approximating polynomials with respect to Gaussian distributions. This is a stronger requirement than $L_1$-approximation but weaker than sandwiching polynomials (which themselves have many applications). These non-negative approximating polynomials have recently found uses in smoothed learning from positive-only examples. In this short note, we prove that every class of sets with Gaussian surface area (GSA) at most $Γ$ under the standard Gaussian admits degree-$k$ non-negative polynomials that $\eps$-approximate its indicator functions in $L_1$-norm, for $k=\tilde{O}(Γ^2/\varepsilon^2)$. Equivalently, finite GSA implies $L_1$-approximation with the stronger pointwise guarantee that the approximating polynomial has range contained in $[0,\infty)$. Up to a constant-factor, this matches the degree of the best currently known Gaussian $L_1$-approximation degree bound without the non-negativity constraint.
匹配关键词: tool use
---

[ACADEMIC - ARXIV]
标题: VecCISC: Improving Confidence-Informed Self-Consistency with Reasoning Trace Clustering and Candidate Answer Selection
作者: James Petullo, Sonny George, Dylan Cashman, Nianwen Xue
链接: https://arxiv.org/abs/2605.08070v1
完整摘要: A standard technique for scaling inference-time reasoning is Self-Consistency, whereby multiple candidate answers are sampled from an LLM and the most common answer is selected. More recently, it has been shown that weighted majority voting (e.g. Confidence-Informed Self Consistency (CISC)), which assigns a confidence value to each candidate answer and chooses the answer with the largest accumulated score, tends to be more accurate on a wide range of popular benchmarks. In practice, weighted majority voting necessitates calling a critic LLM on each candidate's reasoning trace to produce the answer's confidence score. This secondary series of LLM calls greatly increases the overhead and cost of weighted majority voting, despite its potential performance benefits. To reduce this expense, we propose VecCISC, a lightweight, adaptive framework that uses a measure of semantic similarity to filter reasoning traces that are semantically equivalent to others, degenerate, or hallucinated, thus decreasing the number of candidate answers that must be evaluated by the critic. To ensure adequate experimental thoroughness, we evaluate VecCISC on five challenging, widely-adopted datasets spanning the domains of mathematics, chemistry, biology, commonsense reasoning, and the humanities. Our results demonstrate that VecCISC reduces the total token usage by 47%, while maintaining or exceeding the accuracy of CISC.
匹配关键词: tool use
---

[ACADEMIC - ARXIV]
标题: 123D: Unifying Multi-Modal Autonomous Driving Data at Scale
作者: Daniel Dauner, Valentin Charraut, Bastian Berle, Tianyu Li, Long Nguyen, Jiabao Wang, Changhui Jing, Maximilian Igl, Holger Caesar, Boris Ivanovic, Yiyi Liao, Andreas Geiger, Kashyap Chitta
链接: https://arxiv.org/abs/2605.08084v1
完整摘要: The pursuit of autonomous driving has produced one of the richest sensor data collections in all of robotics. However, its scale and diversity remain largely untapped. Each dataset adopts different 2D and 3D modalities, such as cameras, lidar, ego states, annotations, traffic lights, and HD maps, with different rates and synchronization schemes. They come in fragmented formats requiring complex dependencies that cannot natively coexist in the same development environment. Further, major inconsistencies in annotation conventions prevent training or measuring generalization across multiple datasets. We present 123D, an open-source framework that unifies such multi-modal driving data through a single API. To handle synchronization, we store each modality as an independent timestamped event stream with no prescribed rate, enabling synchronous or asynchronous access across arbitrary datasets. Using 123D, we consolidate eight real-world driving datasets spanning 3,300 hours and 90,000 kilometers, together with a synthetic dataset with configurable collection scripts, and provide tools for data analysis and visualization. We conduct a systematic study comparing annotation statistics and assessing each dataset's pose and calibration accuracy. Further, we showcase two applications 123D enables: cross-dataset 3D object detection transfer and reinforcement learning for planning, and offer recommendations for future directions. Code and documentation are available at https://github.com/kesai-labs/py123d.
匹配关键词: planning
---

[ACADEMIC - ARXIV]
标题: PropSplat: Map-Free RF Field Reconstruction via 3D Gaussian Propagation Splatting
作者: William Bjorndahl, Maninder Pal Singh, Farhad Nouri, Joseph Camp
链接: https://arxiv.org/abs/2605.08035v1
完整摘要: Building a site-specific propagation model typically requires either ray-tracing over detailed 3D maps or dense measurement campaigns. Both approaches are expensive and often infeasible for rapid deployments where geographic data is unavailable or outdated. We present PropSplat, a map-free propagation modeling method that reconstructs radio frequency (RF) fields using 3D anisotropic Gaussian primitives. Each Gaussian encodes a scalar path loss offset relative to an explicit baseline path loss model with a learnable path loss exponent. Gaussians are initialized along observed transmitter--receiver paths and optimized end-to-end to learn the propagation environment without external information like floor plans, terrain databases, or clutter data. We evaluate PropSplat against wireless radiance field methods NeRF$^2$, GSRF, and WRF-GS+ on two real-world datasets. On large-scale outdoor drive-tests spanning multiple topographical regions at six sub-6 GHz frequencies, PropSplat achieves 5.38 dB RMSE when training measurements are spaced 300m apart and outperforms WRF-GS+ (5.87 dB), GSRF (7.46 dB), and NeRF$^2$ (14.76 dB). On indoor Bluetooth Low Energy measurements, PropSplat achieves 0.19m mean localization error, an order of magnitude better than NeRF$^2$ (1.84m), while achieving near-identical received signal strength prediction accuracy. These results show that accurate site-specific propagation reconstruction is achievable from sparse RF-native measurements. The need for geographic data as a prerequisite for scalable RF environment modeling is reduced.
匹配关键词: planning
---

[ACADEMIC - ARXIV]
标题: Reason to Play: Behavioral and Brain Alignment Between Frontier LRMs and Human Game Learners
作者: Botos Csaba, Sreejan Kumar, Austin Tudor David Andrews, Laurence Hunt, Chris Summerfield, Joshua B. Tenenbaum, Rui Ponte Costa, Marcelo G. Mattar, Momchil Tomov
链接: https://arxiv.org/abs/2605.08019v1
完整摘要: Humans rapidly learn abstract knowledge when encountering novel environments and flexibly deploy this knowledge to guide efficient and intelligent action. Can modern AI systems learn and plan in a similar way? We study this question using a dataset of complex human gameplay with concurrent fMRI recordings, in which participants learn novel video games that require rule discovery, hypothesis revision, and multi-step planning. We jointly evaluate models by their ability to play the games, match human learning behavior, and predict brain activity during the same task, comparing a suite of frontier Large Reasoning Models (LRMs) against model-free and model-based deep reinforcement learning agents and a Bayesian theory-based agent. We find that frontier LRMs most closely match human behavioral patterns during game discovery and predict brain activity an order of magnitude better than both reinforcement learning alternatives across cortical and subcortical regions, with effects robust to permutation controls. Through targeted manipulations, we further show that brain alignment reflects the model's in-context representation of the game state rather than its downstream planning or reasoning. Our results establish LRMs as compelling computational accounts of human learning and decision making in complex, naturalistic environments. Project page with interactive replays: https://botcs.github.io/reason-to-play/
匹配关键词: planning
---

[ACADEMIC - ARXIV]
标题: Where's the Plan? Locating Latent Planning in Language Models with Lightweight Mechanistic Interventions
作者: Nicole Ma, Nick Rui
链接: https://arxiv.org/abs/2605.07984v1
完整摘要: We study planning site formation in language models -- where internal representations of structurally-constrained future tokens form during the forward pass, and whether they causally drive generation. Using rhyming-couplet completion as a clean test of forward-looking constraint, we apply two lightweight methods (linear probing and activation patching) across Qwen3, Gemma-3, and Llama-3 at more than ten scales. Probing shows that future-rhyme information is linearly decodable at the line boundary, with signal that strengthens with scale in all three families. Activation patching reveals that only Gemma-3-27B causally relies on this encoding, exhibiting a handoff in which the causal driver migrates from the rhyme word to the line boundary around layer 30. Every other model we test conditions on the rhyme word throughout generation, with near-zero causal effect at the line boundary despite strong probe signal. We localize the Gemma-3-27B handoff to five attention heads through two-stage path patching that recover ~90% of the rhyme-routing capacity at the newline.
匹配关键词: planning
---

[ACADEMIC - ARXIV]
标题: One Token Per Frame: Reconsidering Visual Bandwidth in World Models for VLA Policy
作者: Zuojin Tang, Shengchao Yuan, Xiaoxin Bai, Zhiyuan Jin, De Ma, Gang Pan, Bin Liu
链接: https://arxiv.org/abs/2605.07931v1
完整摘要: Vision-language-action (VLA) models increasingly rely on auxiliary world modules to plan over long horizons, yet how such modules should be parameterized on top of a pretrained VLA remains an open design question. Existing world-model-augmented VLAs typically pass the per-frame visual stream into the world module at high visual bandwidth and treat its rollout as a side product of action prediction; under a constrained adaptation budget on a frozen backbone, this leaves both the per-frame representation and the latent action coupling under-examined. We introduce OneWM-VLA, which compresses each view into a single semantic token per frame through an Adaptive Attention Pooling, and produces the resulting latent stream and the action trajectory under a single flow-matching objective rather than connecting them through a separate decoder. Empirically, we find that per-frame visual bandwidth can be reduced to a single token without compromising long-horizon performance under our setup. Trained with 14.71M LoRA parameters on a $π_0$ (2B) backbone, OneWM-VLA improves the average success rate from 47.9% to 61.3% on MetaWorld~MT50, reaches 95.6% on LIBERO-Long (vs.85.2% for $π_0$), and reaches 60.0% on the long-horizon deformable task Fold Cloth on a real Piper arm (vs.20.0% for $π_0$).
匹配关键词: planning
---

