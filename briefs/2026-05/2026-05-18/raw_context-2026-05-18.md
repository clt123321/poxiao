# 破晓 PoXiao — 原始数据 (Raw Context)
生成时间: 2026-05-18 06:29 UTC
================================================================================

[RSS:Reddit LocalLLaMA (社区共识)]
M5 vs DGX Spark vs Strix Halo vs RTX 6000
https://www.reddit.com/r/LocalLLaMA/comments/1tfzsd6/m5_vs_dgx_spark_vs_strix_halo_vs_rtx_6000/
Hey guys, super simple. There have been a lot of online debates about the new M5 Macs vs DGX Sparks vs Strix Halo vs dedicated GPUs etc. So I put them all in a room with good power and cooling and ran everything in parallel with standardized tests for the past 3 days, and published everything to a r
---

[RSS:Reddit LocalLLaMA (社区共识)]
"Generate a photorealistic realtime render of a human face with webGL" (Qwen3.5-122B-A10B UD-Q3_K_XL)
https://www.reddit.com/r/LocalLLaMA/comments/1tg2muq/generate_a_photorealistic_realtime_render_of_a/
&#32; submitted by &#32; /u/_TheWolfOfWalmart_ [link] &#32; [comments]
---

[RSS:Reddit LocalLLaMA (社区共识)]
I hope that someday we will have a 124B Gemma.
https://www.reddit.com/r/LocalLLaMA/comments/1tfv8li/i_hope_that_someday_we_will_have_a_124b_gemma/
&#32; submitted by &#32; /u/cgs019283 [link] &#32; [comments]
---

[RSS:Reddit LocalLLaMA (社区共识)]
May 2026 updated chart of strix halo mini pc size chart
https://www.reddit.com/r/LocalLLaMA/comments/1tg6sgn/may_2026_updated_chart_of_strix_halo_mini_pc_size/
https://gist.github.com/RexYuan/3fc27edcd12475e496eb20946f8c8485 &#32; submitted by &#32; /u/rexyuan [link] &#32; [comments]
---

[RSS:Reddit LocalLLaMA (社区共识)]
llama: avoid copying logits during prompt decode in MTP by am17an · Pull Request #23198 · ggml-org/llama.cpp
https://www.reddit.com/r/LocalLLaMA/comments/1tft1il/llama_avoid_copying_logits_during_prompt_decode/
time to update your llama.cpp -&gt; improved prompt processing speed &#32; submitted by &#32; /u/jacek2023 [link] &#32; [comments]
---

[RSS:Reddit LocalLLaMA (社区共识)]
85 GPU-hours comparing 5 abliteration methods on Qwen3.6-27B: benchmarks, safety, weight forensics - Abliterlitics
https://www.reddit.com/r/LocalLLaMA/comments/1tfmocw/85_gpuhours_comparing_5_abliteration_methods_on/
I've been building Abliterlitics , an open-source abliteration forensics toolkit. The idea is straightforward: take the same base model, compare the different abliteration techniques others have applied, then measure what actually changed using benchmarks, safety evaluation, distribution shift, and 
---

[RSS:Reddit LocalLLaMA (社区共识)]
Apple silicon costs more than OpenRouter: an analysis
https://www.reddit.com/r/LocalLLaMA/comments/1tg0y2h/apple_silicon_costs_more_than_openrouter_an/
I am not the author. My two cents: I'm not suggesting we don't all know local AI is expensive, at least for now. The math gets interesting if OpenRouter providers are burning investor cash and it runs out, or we take into account hardware we use for other purposes, or privacy is a primary motivation
---

[RSS:Reddit LocalLLaMA (社区共识)]
The power of structured workflows and small local models
https://www.reddit.com/r/LocalLLaMA/comments/1tftaaa/the_power_of_structured_workflows_and_small_local/
A month ago, I experimented with a very basic home-rolled agent loop with a handful of tools and found it worked surprisingly well in spite of how crude it was: https://www.reddit.com/r/LocalLLaMA/comments/1sl7f8e/homerolled_loop_agent_is_surprisingly_effective/ Later, I wrote about how I addictive 
---

[RSS:Reddit LocalLLaMA (社区共识)]
Gemma-4-Gembrain-31B-it-uncensored-heretic Is Out Now, a Merge of Multiple Gemma 4 31B it Finetunes Designed to Boost Logical and Lateral Thinking for Improved Adherence, Increased Swipe Variety and Enhanced Creative Prose, With KLD of 0.0186 and 13/100 Refusals!
https://www.reddit.com/r/LocalLLaMA/comments/1tg7s7j/gemma4gembrain31bituncensoredheretic_is_out_now_a/
Provided in both Safetensors and GGUFs. Safetensors: llmfan46/Gemma-4-Gembrain-31B-it-uncensored-heretic: https://huggingface.co/llmfan46/Gemma-4-Gembrain-31B-it-uncensored-heretic GGUFs: llmfan46/Gemma-4-Gembrain-31B-it-uncensored-heretic-GGUF: https://huggingface.co/llmfan46/Gemma-4-Gembrain-31B-i
---

[RSS:Reddit LocalLLaMA (社区共识)]
Benchmarking vLLM vs SGLang vs llama.cpp on a mixed Blackwell/Ada cluster
https://www.reddit.com/r/LocalLLaMA/comments/1tg4mw0/benchmarking_vllm_vs_sglang_vs_llamacpp_on_a/
I have been running some benchmarks on a heterogeneous 7-GPU cluster to see how different inference engines handle long context prefill using pipeline parallelism. My setup consists of a mix of Blackwell and Ada cards: one RTX PRO 6000 96GB, one PRO 5000 48GB, two 5090 32GB, and three modded 4090 48
---

[RSS:Reddit LocalLLaMA (社区共识)]
Dual GPU llama.cpp speedup
https://www.reddit.com/r/LocalLLaMA/comments/1tflngz/dual_gpu_llamacpp_speedup/
Llama.cpp has an issue with &quot;--split-mode tensor&quot;, you'll get great results but it only supports non-quantized KV caches, for this very reason a lot of people decide to go with a healthy sized KV cache and ignore tensor parallelism. &nbsp; I've had a stab at fixing the issue here - https:/
---

[RSS:Reddit LocalLLaMA (社区共识)]
Testing llama.cpp MTP support on Qwen3.6 - RTX 5090
https://www.reddit.com/r/LocalLLaMA/comments/1tfgxc8/testing_llamacpp_mtp_support_on_qwen36_rtx_5090/
Setup: - RTX 5090, 32 GB, Linux - Built llama.cpp from 4f13cb7 (the official ghcr.io/ggml-org/llama.cpp:server-cuda image hasn't picked up the merge yet as of writing — had to docker build from source with CUDA_DOCKER_ARCH=120) - Unsloth's Qwen3.6-27B-MTP-GGUF Q5_K_M and Qwen3.6-35B-A3B-MTP-GGUF UD-
---

[RSS:Reddit LocalLLaMA (社区共识)]
ROCm 7.13 nightly adds strix halo optimizations
https://www.reddit.com/r/LocalLLaMA/comments/1tftg09/rocm_713_nightly_adds_strix_halo_optimizations/
https://www.phoronix.com/news/ROCm-7.13-Released Quote: ...new optimizations for Ryzen AI Max 300 &quot;Strix Halo&quot; and the ROCprof Trace Decoder is now open-source...&lt;snip&gt;... Those rolling from source can grab the ROCm 7.13 Tech Preview via TheRock on GitHub . https://rocm.docs.amd.com/
---

[RSS:Reddit LocalLLaMA (社区共识)]
Benchmarking the new b9200 update: Optimizing Qwen 3.6 27B mtp for Hermes Agent on a single RTX 3090
https://www.reddit.com/r/LocalLLaMA/comments/1tg6j9u/benchmarking_the_new_b9200_update_optimizing_qwen/
UPDATED (POST b9200) Okay, here is the updated version using the new Qwen 3.6 27B mtp gguf from Unsloth, running it as the backend for the hermes agent. While dialing it in, I noticed that the currently recommended Unsloth mtp flags actually bottleneck performance and tank draft acceptance rates for
---

[RSS:Reddit LocalLLaMA (社区共识)]
MTP experiences on 7900xtx?
https://www.reddit.com/r/LocalLLaMA/comments/1tg25fz/mtp_experiences_on_7900xtx/
Hi! I have been using Qwen3.6 35B A3B happily the past few weeks, and I wanted to try out Qwn3.6 27B with the new fancy MTP speculative draft! These are my settings currently: llama-server \ -m $HOME/Documents/ML/Qwen3.6-27B-Q4_K_M.gguf \ -c 64000 \ -ngl 65 \ --parallel 1 \ -t 8 \ --jinja \ --host 0
---

[RSS:Reddit LocalLLaMA (社区共识)]
Moving from Composer 2/Kimi 2.6 to Qwen3.6:35b-a3b
https://www.reddit.com/r/LocalLLaMA/comments/1tfxah9/moving_from_composer_2kimi_26_to_qwen3635ba3b/
I can't believe it, but I'm able to do my daily software development work on this model. We have a 500-700k line of code enterprise software suite that I'm devving for 60 hours a week. I've been hunting for a cursor replacement for a little bit now, and was previously toying with Kimi 2.6 and deepse
---

[RSS:Reddit LocalLLaMA (社区共识)]
Pushing the limit: minimax m2.7 q8_0 128k on 2x3090, 256GB DDR4
https://www.reddit.com/r/LocalLLaMA/comments/1tg37t6/pushing_the_limit_minimax_m27_q8_0_128k_on_2x3090/
CPU is just a secondhand 10900x. Using 128k context, unquantized kv cache. Model is at q8_0 to mitigate some weird behavior I was seeing at lower quants. Speed is very slow at around 50tps pp, 10tps tg, but usable for coding agent workflows. Anybody else running MoE models in this size class on rela
---

[RSS:Reddit LocalLLaMA (社区共识)]
Developers who use local AI - Q4_0 vs Q8_0 KV quant?
https://www.reddit.com/r/LocalLLaMA/comments/1tfqfvt/developers_who_use_local_ai_q4_0_vs_q8_0_kv_quant/
I'd love to hear from developers who use big context windows if they notice a difference? Obviously I would love to cut the KV cache VRAM requirement in half, but I'm worried about quality especially when we enter into 50k+ context territory. I don't really need a full study, just wondering, anecdot
---

[RSS:Reddit LocalLLaMA (社区共识)]
Any good MOE ~60B models? I have 64GB vram
https://www.reddit.com/r/LocalLLaMA/comments/1tfzmpq/any_good_moe_60b_models_i_have_64gb_vram/
I have a build with 2 x MI50 32GBs and 64 gigs of DDR4 (bought before rampocolypse for ~630 USD total, I’m not rich) and I’m not gonna upgrade it for a long while. Are there any good MOE models that are around 60B in parameters so I can make use of all the VRAM? I feel like I’m stuck in a weird spot
---

[RSS:Reddit LocalLLaMA (社区共识)]
b9200 released - potential mtp pp increase
https://www.reddit.com/r/LocalLLaMA/comments/1tg5r5p/b9200_released_potential_mtp_pp_increase/
testing in progress ...we all need an increase in pp 😆 https://github.com/ggml-org/llama.cpp/releases/tag/b9200 u/am17an am17an commented 13 hours ago • Overview Avoid copying the logits for every token in the batch when doing prompt processing for MTP since it only requires the pre-norm. This reduc
---

[RSS:Reddit LocalLLaMA (社区共识)]
MTP for Qwen3.6-35B-A3B on 6GB VRAM laptop: not worth it
https://www.reddit.com/r/LocalLLaMA/comments/1tfq683/mtp_for_qwen3635ba3b_on_6gb_vram_laptop_not_worth/
I have an Asus gaming laptop from 2021 that I bought used for 500€ last year. I wanted to see if the recently merged MTP support in llama.cpp is worth using on such a VRAM constrained device for the Qwen3.6-35B-A3B model. So I did some experiments to measure performance with and without MTP. TL;DR: 
---

[RSS:Reddit LocalLLaMA (社区共识)]
Jackrong/Qwopus3.5-9B-Coder-GGUF · Hugging Face
https://www.reddit.com/r/LocalLLaMA/comments/1tfin40/jackrongqwopus359bcodergguf_hugging_face/
Qwopus3.5-9B-coder is specially optimized and fine-tuned for high-performance 🤖 Agentic Coding, complex Tool Calling, and logical reasoning. 💡 Why the 9B Dense Model? We believe that the 9B dense architecture represents the perfect &quot;sweet spot&quot; for large language models. It runs seamlessly
---

[RSS:Reddit LocalLLaMA (社区共识)]
FlashLM v9.7
https://www.reddit.com/r/LocalLLaMA/comments/1tg8j0l/flashlm_v97/
Back with an update. Some of you saw v10 FSP, the one where I found that Future Sentence Prediction gave a 2.5x PPL improvement. Well, I've run 20+ more experiments since then trying to get the model to actually understand what it's saying. Spoiler: lower PPL does not mean more coherent. Quick clari
---

[RSS:Reddit LocalLLaMA (社区共识)]
Grafting vision onto text models for fun and profit.
https://www.reddit.com/r/LocalLLaMA/comments/1tg0me5/grafting_vision_onto_text_models_for_fun_and/
So as we know.. llama.cpp separates the vision or other multimedia from the main weights. Conversely, trained model capabilities might be removed at release. What if there was a way to put them back? Mistral has now released both pixtral and medium vision encoders. The tokenizers of past models cont
---

[RSS:Reddit MachineLearning (学术风向)]
Slop is making me feel disconnected from AI Research [D]
https://www.reddit.com/r/MachineLearning/comments/1tfv0vh/slop_is_making_me_feel_disconnected_from_ai/
Hello everyone. This is just a small rant on my part. I’m relatively young, a final year undergrad, and I’ve been interested in AI researcher since I was in high school. Over that period of time I feel there has been a significant shift in the landscape regarding the culture surrounding the research
---

[RSS:Reddit MachineLearning (学术风向)]
Program misleading high school students into paying to perform academic misconduct in ML Research [D]
https://www.reddit.com/r/MachineLearning/comments/1tfh2s9/program_misleading_high_school_students_into/
I was browsing OpenReview and I came accross this person called Kevin Zhu https://openreview.net/profile?id=~Kevin_Zhu3 , lets say I was impressed when I saw 158 publications and 468 coauthors, and out of curiosity I searched up his afflication ( https://algoverseairesearch.org/ ) Turns out it is a 
---

[RSS:Reddit MachineLearning (学术风向)]
Recent Developments in LLM Architectures: KV Sharing, mHC, and Compressed Attention [P]
https://www.reddit.com/r/MachineLearning/comments/1tfpvod/recent_developments_in_llm_architectures_kv/
&#32; submitted by &#32; /u/seraschka [link] &#32; [comments]
---

[RSS:Reddit MachineLearning (学术风向)]
Would a new result in pre-print be considered by reviewers? [D]
https://www.reddit.com/r/MachineLearning/comments/1tg7qq3/would_a_new_result_in_preprint_be_considered_by/
So I have a bit of a weird question; suppose you were reviewing a paper. The paper is otherwise ok, but you notice that the authors left a giant elephant in the room unaddressed, either experiment wise or theoretical result wise. But then you become curious and you look up the paper to see if there 
---

[RSS:Reddit MachineLearning (学术风向)]
#1 on memory benchmark LongMemEval with Gemini Flash, not Pro [R]
https://www.reddit.com/r/MachineLearning/comments/1tfwd69/1_on_memory_benchmark_longmemeval_with_gemini/
Disclosure: first author. Evaluation of an experimental memory retrieval system against LongMemEval (Wang et al., 2024). Figured the results might be of interest here, particularly the deliberate use of a smaller answering model to isolate retrieval quality from model capability. 96.4% at top-50 wit
---

[RSS:Reddit MachineLearning (学术风向)]
How are you handling training data when public datasets don't match your use case? [D]
https://www.reddit.com/r/MachineLearning/comments/1tg45fz/how_are_you_handling_training_data_when_public/
Public datasets on HF or Kaggle can sometimes be too generic, wrong domain, wrong schema, outdated, or just not enough volume to generalize properly. Collecting real-world proprietary data takes months. What do people actually do? From what I have seen, the options tend to be: - Ship with what you h
---

[RSS:Reddit MachineLearning (学术风向)]
ML lead vs PM on eval-methodology layer independence. who's actually right here? [D]
https://www.reddit.com/r/MachineLearning/comments/1tfkgbx/ml_lead_vs_pm_on_evalmethodology_layer/
got into an argument with our ML lead at 11pm yesterday about an eval methodology a PM had built off a framework she learned at an AI PM cohort. shes claiming a layered defense framework, hes saying the layers are statistically conditioned and her independence claim is wrong. they both have a point.
---

[RSS:Reddit Jobs & Careers (职场动态)]
New grad at Meta. Scared of layoffs. Not getting any callbacks
https://www.reddit.com/r/cscareerquestions/comments/1tfzk5s/new_grad_at_meta_scared_of_layoffs_not_getting/
I have 5 SWE internships, graduated last year, and been at Meta for almost a year as a SWE new grad. I was not a returning intern. None of my internships were at FAANG or FAANG+. I also had new grad offers last year from Robinhood, Amazon, Capital One, and a return offer from one of my internships. 
---

[RSS:Reddit Jobs & Careers (职场动态)]
Sankey Diagram of my Job Search, Full Stack SWE II with ~4 YOE
https://www.reddit.com/r/cscareerquestions/comments/1tfvcpn/sankey_diagram_of_my_job_search_full_stack_swe_ii/
https://imgur.com/a/X1EFMO1 I wanted to share my experience with job searching earlier this year. I'm a full stack (backend leaning) software engineer with almost 4 YOE at a Fortune 100 company in the US. I started applying for jobs in January of this year, and I mostly shotgun applied, only tailori
---

[RSS:Reddit Jobs & Careers (职场动态)]
Have you encountered actual "good" codebases for applications with a decent amount of complexity?
https://www.reddit.com/r/cscareerquestions/comments/1tfygrt/have_you_encountered_actual_good_codebases_for/
When I mean &quot;good&quot; I am not just referring to &quot;clean code&quot;. I mean codebases that are genuinely easy to understand and modify. The type of codebase where you aren't nervous to add new features or remove old ones. Code bases that don't require arcane tribal knowledge. But the key 
---

[RSS:Reddit Jobs & Careers (职场动态)]
Have you noticed an uptick in recruiter messages the last few months?
https://www.reddit.com/r/cscareerquestions/comments/1tfpyf8/have_you_noticed_an_uptick_in_recruiter_messages/
In 2022 I got like 2 messages per week from recruiters. In 2025 it was one message every 3 week and mostly from Indian consulting firms. Inhouse recruters where maybe 2 for all of 2025. The last two months I have gotten like 8 inhouse recruiters messaging me. Even if the role aren't a perfect fit th
---

[RSS:Reddit Jobs & Careers (职场动态)]
Career advice (I can’t stand the fear mongers)
https://www.reddit.com/r/cscareerquestions/comments/1tfoq9g/career_advice_i_cant_stand_the_fear_mongers/
I’m about to get my bachelor degree in Computer science but i want to pursue a Masters degree fo specializing in one field. The problem is i can’t decide. EVERY single field i look into, all i keep hearing is “Entry lvl jobs are GONE” “AI took over” “Unless you’re graduating from a world class unive
---

[RSS:Reddit Jobs & Careers (职场动态)]
I'm not happy about this one task at work, is there anything I can do about it without affecting my role?
https://www.reddit.com/r/cscareerquestions/comments/1tg5v45/im_not_happy_about_this_one_task_at_work_is_there/
I’m on an engineering team and started a few years ago. Early on, I didn’t have much work, so another teammate and I started helping a senior coworker with a task that isn’t really a part of our main responsibilies (it's part of his, not ours, we just needed something to do). About a year and a half
---

[RSS:Reddit Jobs & Careers (职场动态)]
I am battling perception from being made an example of and I am close to giving up on tech
https://www.reddit.com/r/cscareerquestions/comments/1tfy1w5/i_am_battling_perception_from_being_made_an/
I’ve worked in the tech industry for 12 years, I’ve switched disciplines, worked in mobile, back-end, data, security, infrastructure, and I’ve worked up to staff positions in smaller companies. I often worked at companies on an extended project basis but once the project concluded, I would move on. 
---

[RSS:Reddit Jobs & Careers (职场动态)]
Dilemma about switching jobs
https://www.reddit.com/r/cscareerquestions/comments/1tg6y68/dilemma_about_switching_jobs/
I’ve been at my current company for 6y. 7 YOE overall as a backend engineer in Big Tech. Lately, I’ve been re-orged into a new team. The architects associated with that project/team are extremely frustrating (not technically sound, make you second guess design proposals, political etc.). My new mana
---

[RSS:Reddit Jobs & Careers (职场动态)]
Do projects still matter right now for this market?
https://www.reddit.com/r/cscareerquestions/comments/1tg7h8t/do_projects_still_matter_right_now_for_this_market/
I’m basically getting back into the market or at least trying to and I’m planning to do a project and just asked gemini what would be a good realistic project to build to re-learn and also showcase like my abilities. This what it said - The project is an enterprise-grade backend system built with Sp
---

[RSS:Reddit Jobs & Careers (职场动态)]
Anyone else notice the job market (very slowly) getting better?
https://www.reddit.com/r/cscareerquestions/comments/1tfyouh/anyone_else_notice_the_job_market_very_slowly/
While it’s still not great right now, I have been noticing that it’s definitely better than where it was last summer. I’ve noticed more of my class of 2025 peers finding jobs and postings are showing some signs of life. This isn’t just blindly following the Indeed data too, my local networking event
---

[RSS:Reddit Jobs & Careers (职场动态)]
Anthropic Safety Fellowship
https://www.reddit.com/r/cscareerquestions/comments/1tfyir1/anthropic_safety_fellowship/
Has anyone interviewed for the Anthropic safety fellowship? I am interviewing and have a few questions about the topic of the final interview. Any help would be greatly appreciated. &#32; submitted by &#32; /u/Old_Location_9895 [link] &#32; [comments]
---

[RSS:Reddit Jobs & Careers (职场动态)]
2nd Year college Dillema
https://www.reddit.com/r/cscareerquestions/comments/1tg3jw5/2nd_year_college_dillema/
Too confused about skills to develop and what to leave. I have learnt basic SPRING BOOT (Crud &amp; auth) for college exams. I want to explore further but seniors say I should go for MERN stack as it has better returns. I dont want ai to replace me so I am interested in devOps, here again I am confu
---

[RSS:Reddit Jobs & Careers (职场动态)]
Anyone work at Toyota at Plano? How is it?
https://www.reddit.com/r/cscareerquestions/comments/1tg37p6/anyone_work_at_toyota_at_plano_how_is_it/
How is the campus there. I am considering an offer from there and I am just curious to know how the culture and how the campus is. &#32; submitted by &#32; /u/SruLunCa [link] &#32; [comments]
---

[RSS:Reddit Jobs & Careers (职场动态)]
Just graduated, how can I maximize my job search and standout?
https://www.reddit.com/r/cscareerquestions/comments/1tg2n6q/just_graduated_how_can_i_maximize_my_job_search/
Graduated last week and have been applying to full time / internship positions for months and gotten nowhere. Now that the clock is ticking I just really want to make the most of my applications and work I put in towards getting a job, or see what kind of projects I should make in my free time to bo
---

[RSS:Reddit Jobs & Careers (职场动态)]
CS Career Path Advice. (Software Systems Engineering?)
https://www.reddit.com/r/cscareerquestions/comments/1tg0q6t/cs_career_path_advice_software_systems_engineering/
Hey y'all, CS student #482938243 here. I was hoping some of you could give me some advice for how to move forward in my career so that I can ultimately get a job that I enjoy. I'm a rising senior studying Computer Science with a minor in math. I enjoy the logical and puzzle-solving part of programmi
---

[RSS:Reddit Jobs & Careers (职场动态)]
How can I gain skills needed for industry during a postdoc?
https://www.reddit.com/r/cscareerquestions/comments/1tfohvm/how_can_i_gain_skills_needed_for_industry_during/
I recently finished a PhD in deep reinforcement learning, during which I did only one internship (I have other internships from many years ago also). I wanted to go into industry ideally as a research scientist, research engineer, or data scientist that focuses on deep learning. I interviewed with 1
---

[RSS:Reddit Jobs & Careers (职场动态)]
Contract vs. full-time W2?
https://www.reddit.com/r/cscareerquestions/comments/1tg0a8x/contract_vs_fulltime_w2/
I've just started my career as a consultant with a small firm and have been on my first contract for about 3 months now. The contract was set for 3 months and now the company is asking me if I'd be interested in staying with them full-time. The firm is owned by a previous professor of mine who would
---

[RSS:Reddit Jobs & Careers (职场动态)]
Besides the jobs crash of this decade, what was the worst year for you career wise?
https://www.reddit.com/r/cscareerquestions/comments/1tfeb5c/besides_the_jobs_crash_of_this_decade_what_was/
2015 was a particularly difficult year for me. I had 4 years of experience already, but that's when I first started noticing interviews getting very tough. Not a single job offer that year. &#32; submitted by &#32; /u/superide [link] &#32; [comments]
---

[RSS:Reddit Jobs & Careers (职场动态)]
25 for college too late ?
https://www.reddit.com/r/cscareerquestions/comments/1tfyl2h/25_for_college_too_late/
I completed all the general education courses 3 years ago but then stopped because of mental health issues. I was thinking to return to college and finish a degree, but I don’t know which one. My college offers: Computer science Biomedical science Accounting and Finance International Business or Bus
---

[RSS:Reddit Jobs & Careers (职场动态)]
Confused Junior
https://www.reddit.com/r/cscareerquestions/comments/1tfwrpg/confused_junior/
I'm sure this post has been made a million times just today so if it gets taken down so be it. But I'm about to start my actual classes after coming from a CC. I'm just confused on what to do in the sense of actually progressing. In terms of internships (I know I'm not going to sniff employment for 
---

[RSS:Reddit Jobs & Careers (职场动态)]
Cisco vs Crusoe Offer Comparison
https://www.reddit.com/r/cscareerquestions/comments/1tfj7p7/cisco_vs_crusoe_offer_comparison/
I am a SWE with 3 YOE in a mid-size company in US, and I recently got offers from Cisco and Crusoe. Cisco salary is higher with real RSUs, but I'm hesitated as Cisco has layoff culture and the tech stack that I'm going to work on is extremely niche. If I decide to jump again in the future, very few 
---

[HACKERNEWS]
GenCAD
https://gencad.github.io/
Score: 129 | Comments: 26
---

[HACKERNEWS]
I turned a $80 RK3562 Android tablet into a Debian Linux workstation
https://github.com/tech4bot/rk3562deb
Score: 266 | Comments: 124
---

[HACKERNEWS]
Prolog Coding Horror
https://www.metalevel.at/prolog/horror
Score: 62 | Comments: 23
---

[HACKERNEWS]
Two EA-18 fighter jets collide at Mountain Home airshow, pilots ejected safely
https://idahonews.com/news/local/two-f-18-fighter-jets-have-crashed-during-an-airshow-at-mountain-home-air-force-base
Score: 108 | Comments: 88
---

[HACKERNEWS]
Show HN: Semble – Code search for agents that uses 98% fewer tokens than grep
https://github.com/MinishLab/semble
Score: 185 | Comments: 48
---

[HACKERNEWS]
VoIP brings back old-fashioned pay phones to rural Vermont (2025)
https://spectrum.ieee.org/payphone-voip
Score: 116 | Comments: 36
---

[HACKERNEWS]
CUDA Books
https://github.com/alternbits/awesome-cuda-books
Score: 133 | Comments: 27
---

[HACKERNEWS]
The History of ThinkPad: From IBM’s Bento Box to Lenovo’s AI Workstations
https://www.jdhodges.com/blog/thinkpad-history/
Score: 57 | Comments: 30
---

[HACKERNEWS]
Design posters showcasing your country's electrical grid
https://github.com/open-energy-transition/grid2poster
Score: 62 | Comments: 16
---

[HACKERNEWS]
I don't think AI will make your processes go faster
https://frederickvanbrabant.com/blog/2026-05-15-i-dont-think-ai-will-make-your-processes-go-faster/
Score: 502 | Comments: 356
---

[HACKERNEWS]
Fabricked: Misconfiguring Infinity Fabric to Break AMD SEV-SNP
https://xca-attacks.github.io/fabricked/
Score: 27 | Comments: 16
---

[HACKERNEWS]
Trials on veterans suggest ibogaine could provide a new treatment for PTSD
https://www.bbc.com/future/article/20260514-how-hallucinogenic-ibogaine-helps-veterans-overcome-ptsd
Score: 82 | Comments: 89
---

[ACADEMIC - ARXIV]
标题: IVGT: Implicit Visual Geometry Transformer for Neural Scene Representation
作者: Yuqi Wu, Tianyu Hu, Wenzhao Zheng, Yuanhui Huang, Haowen Sun, Jie Zhou, Jiwen Lu
链接: https://arxiv.org/abs/2605.16258v1
完整摘要: Reconstructing coherent 3D geometry and appearance from unposed multi-view images is a fundamental yet challenging problem in computer vision. Most existing visual geometry foundation models predict explicit geometry by regressing pixel-aligned pointmaps, often suffering from redundancy and limited geometric continuity. We propose IVGT, an Implicit Visual Geometry Transformer that implicitly models continuous and coherent geometry from pose-free multi-view images. This formulation learns a continuous neural scene representation in a canonical coordinate system and supports continuous spatial queries at any 3D positions, retrieving local features to predict signed distance (SDF) values and colors using lightweight decoders. It allows direct extraction of continuous and coherent surface geometry, enabling rendering of RGB images, depth maps, and surface normal maps from arbitrary viewpoints. We train IVGT via multi-dataset joint optimization with 2D supervision and 3D geometric regularization. IVGT demonstrates generalization across scenes and achieves strong performance on various tasks, including mesh and point cloud reconstruction, novel view synthesis, depth and surface normal estimation, and camera pose estimation.
匹配关键词: video synthesis
---

[ACADEMIC - ARXIV]
标题: Evaluating Design Video Generation: Metrics for Compositional Fidelity
作者: Adrienne Deganutti, Dingning Cao, Jaejung Seol, Elad Hirsch, Purvanshi Mehta
链接: https://arxiv.org/abs/2605.16223v1
完整摘要: Generative video models are increasingly used in design animation tasks, yet no standardized evaluation framework exists for this domain. Unlike natural video generation, design animation imposes structured constraints: specific components shall animate with prescribed motion types, directions, speed and timing, while non-animated regions must remain stable and layout structure must be preserved. This paper provides a fully automated evaluation framework organized across four dimensions: layout fidelity, motion correctness, temporal quality, and content fidelity. This eliminates the reliance on subjective human evaluation and establishes a common basis for benchmarking progress in the field.
匹配关键词: video synthesis
---

[ACADEMIC - ARXIV]
标题: Property-Guided LLM Program Synthesis for Planning
作者: Augusto B. Corrêa, André G. Pereira, Jendrik Seipp
链接: https://arxiv.org/abs/2605.16142v1
完整摘要: LLMs have shown impressive success in program synthesis, discovering programs that surpass prior solutions. However, these approaches rely on simple numeric scores to signal program quality, such as the value of the solution or the number of passed tests. Because a score offers no guidance on why a program failed, the system must generate and evaluate many candidates hoping some succeed, increasing LLM inference and evaluation costs. We study a different approach: property-guided LLM program synthesis. Instead of scoring programs after evaluation, we check whether a candidate satisfies a formally defined property. When the property is violated, we stop the evaluation early and provide the LLM with a concrete counterexample showing exactly how the program failed. This feedback drastically reduces both the number of program generations and the evaluation cost, and can guide the LLM to generate stronger programs. We evaluate this approach on PDDL planning domains, asking the LLM to synthesize direct heuristic functions: every state reachable by strictly improving transitions has a strictly improving successor. A heuristic with this property leads hill-climbing algorithm directly to a goal state. A counterexample-guided repair loop generates one candidate program, checks the property over a training set, and returns the first case that violates the property. We evaluate our approach on ten planning domains with an out-of-distribution test set. The synthesized heuristics are effectively direct on virtually all test tasks, and compared to the best prior generation method our approach generates seven times fewer programs per domain on average, solves more tasks without using search, and requires several orders of magnitude less computation to evaluate candidates. Whenever a problem admits a verifiable property, property-guided LLM synthesis can reduce cost and improve program quality.
匹配关键词: video synthesis
---

[ACADEMIC - ARXIV]
标题: Surrogate Neural Architecture Codesign Package (SNAC-Pack)
作者: Jason Weitz, Dmitri Demler, Benjamin Hawks, Aaron Wang, Nhan Tran, Javier Duarte
链接: https://arxiv.org/abs/2605.16138v1
完整摘要: Neural architecture search (NAS) is a powerful approach for automating model design, but existing methods often optimize for accuracy alone or rely on proxy metrics such as bit operations (BOPs) that correlate poorly with hardware cost. This gap is particularly large for FPGA deployment, where cost is dominated by a multi-dimensional budget of lookup tables, DSPs, flip-flops, BRAM, and latency. We present the Surrogate Neural Architecture Codesign Package (SNAC-Pack), an open-source AutoML framework for hardware-aware neural architecture codesign and end-to-end FPGA deployment. SNAC-Pack runs a multi-objective global search with Optuna and NSGA-II, loading trials to a shared SQLite store that enables parallel workers across compute nodes. A hardware surrogate model outputs per-trial resource and latency estimates, avoiding the synthesis cost that would otherwise dominate the search loop. A local search stage then applies quantization-aware training (QAT) together with iterative magnitude pruning in a combined compression loop, after which the final model is synthesized to FPGA firmware via the hls4ml Python library. A YAML configuration and an optional agentic frontend let users run the pipeline on new datasets without modifying the framework. We demonstrate SNAC-Pack on jet classification at the Large Hadron Collider and superconducting qubit readout, discovering compact architectures that match or exceed strong baselines on the task metric while reducing FPGA resource utilization and, in the qubit readout case, reducing the design space exploration process from months of manual fine-tuning to hours of automated search.
匹配关键词: video synthesis
---

[ACADEMIC - ARXIV]
标题: GenShield: Unified Detection and Artifact Correction for AI-Generated Images
作者: Zhipei Xu, Xuanyu Zhang, Youmin Xu, Qing Huang, Shen Chen, Taiping Yao, Shouhong Ding, Jian Zhang
链接: https://arxiv.org/abs/2605.16122v1
完整摘要: Diffusion-based image synthesis has made AI-generated images (AIGI) increasingly photorealistic, raising urgent concerns about authenticity in applications such as misinformation detection, digital forensics, and content moderation. Despite the substantial advances in AIGI detection, how to correct detected AI-generated images with visible artifacts and restore realistic appearance remains largely underexplored. Moreover, few existing work has established the connection between AIGI detection and artifact correction. To fill this gap, we propose GenShield, a unified autoregressive framework that jointly performs explainable AIGI detection and controllable artifact correction in a closed loop from diagnosis to restoration, revealing a mutually reinforcing relationship between these two tasks. We further introduce a Visual Chain-of-Thought based curriculum learning strategy that enables self-explained, multi-step ``diagnose-then-repair'' correction with an explicit stopping criterion. A high-quality dataset with large-scale ``artifact-restored'' pairs is also constructed alongside a unified evaluation pipeline. Extensive experiments on our correction benchmark and mainstream AIGI detection benchmarks demonstrate state-of-the-art performance and strong generalization of our method. The code is available at https://github.com/zhipeixu/GenShield.
匹配关键词: video synthesis
---

[ACADEMIC - ARXIV]
标题: Evaluating Design Video Generation: Metrics for Compositional Fidelity
作者: Adrienne Deganutti, Dingning Cao, Jaejung Seol, Elad Hirsch, Purvanshi Mehta
链接: https://arxiv.org/abs/2605.16223v1
完整摘要: Generative video models are increasingly used in design animation tasks, yet no standardized evaluation framework exists for this domain. Unlike natural video generation, design animation imposes structured constraints: specific components shall animate with prescribed motion types, directions, speed and timing, while non-animated regions must remain stable and layout structure must be preserved. This paper provides a fully automated evaluation framework organized across four dimensions: layout fidelity, motion correctness, temporal quality, and content fidelity. This eliminates the reliance on subjective human evaluation and establishes a common basis for benchmarking progress in the field.
匹配关键词: video understanding
---

[ACADEMIC - ARXIV]
标题: MAgSeg: Segmentation of Agricultural Landscapes in High-Resolution Satellite Imagery using Multimodal Large Language Models
作者: Piyush Tiwary, Utkarsh Ahuja, Depanshu Sani, Aishwarya Jayagopal, Sagar Gubbi, Subhashini Venugopalan, Alok Talekar, Vaibhav Rajan
链接: https://arxiv.org/abs/2605.16179v1
完整摘要: Agricultural landscape segmentation in the Global South is challenging as it is characterized by fragmented plots, high intra-class variance, and a scarcity of labeled training data. Recent advances in segmentation have been made by Multimodal Large Language Models (MLLMs). However, current approaches encounter critical context length bottlenecks and a domain alignment gap in understanding satellite features. We address these limitations through MAgSeg, a novel, decoder-free MLLM segmentation approach. MAgSeg is an architecturally efficient approach that enables standard MLLMs to perform segmentation of complex smallholder agricultural landscapes from high-resolution satellite imagery, without requiring auxiliary vision decoders. We introduce a novel instruction tuning data format designed to enable scalable fine-tuning and post-training on high resolution satellite imagery, which enables MAgSeg to learn from the global context of the image while generating text tokens for only a patch within the image. Extensive evaluations on datasets spanning three countries in the Global South demonstrate that MAgSeg significantly outperforms state-of-the-art MLLM baselines, offering a scalable solution to map smallholder agricultural environments.
匹配关键词: video understanding
---

[ACADEMIC - ARXIV]
标题: Second-Order Multi-Level Variance Correction for Modality Competition in Multimodal Models
作者: Yishun Lu, Wes Armour
链接: https://arxiv.org/abs/2605.16165v1
完整摘要: Autoregressive next-token training offers a unified formulation for image generation and text understanding, but it also creates strong modality competition that destabilizes optimization and limits large-batch scaling. We show that first-order optimizers such as AdamW are vulnerable to cross-modality gradient heterogeneity, while second-order preconditioning, particularly SOAP, provides a more stable basis for multimodal alignment. Building on this insight, we propose \emph{ML-FOP-SOAP}, a second-order optimization framework with Multi-Level Variance Correction. Our Fisher-Orthogonal Projection suppresses variance-induced modality conflicts, reducing the trade-off between visual generation and textual understanding. To make this practical under large gradient accumulation, we introduce a hierarchical folding strategy that captures fine-grained variance with low micro-step overhead. Experiments on Janus and Emu3 show consistent gains across both modalities and stable training at batch size 8192. Compared with AdamW, our method improves sample efficiency by up to $1.4\times$ and accelerates wall-clock training by up to $1.5\times$, offering a robust optimizer for scaling multimodal foundation models.
匹配关键词: video understanding
---

[ACADEMIC - ARXIV]
标题: Entropic Auto-Encoding via Implicit Free-Energy Minimization
作者: Hazhir Aliahmadi, Irina Babayan, Greg van Anders
链接: https://arxiv.org/abs/2605.16164v1
完整摘要: Despite their ubiquity, variational autoencoders (VAEs) inherently suffer from posterior collapse, a failure mode in which latent variables are effectively ignored. This failure arises because explicit prior imposition drives optimization toward loss landscape regions corresponding to uninformative latent representations. Here, we introduce Entropic Autoencoders (EAEs), a framework in which reconstruction loss is the only explicit objective, and entropy generates the latent variables' prior implicitly through a free energy-minimizing ensemble of encoders. This ensemble biases learning toward high-volume regions of near-optimal solutions, while decoder updates direct the search trajectories toward informative latent representations. We demonstrate that EAEs mitigate posterior collapse by learning non-Gaussian, multimodal latent distributions that yield diverse, data-consistent generations and preserve different forms of underlying structure in the data. As a proof-of-concept, we show that an EAE captures a superposition of the known low-dimensional dynamics of a reaction-diffusion process. Then, we show that an EAE identifies implicit categorical distinctions in MNIST latent representations, and displays a hierarchical understanding of facial structure on the CelebA dataset, from an "all-human" face to individual-dependent features.
匹配关键词: video understanding
---

[ACADEMIC - ARXIV]
标题: Centralized vs Decentralized Federated Learning: A trade-off performance analysis
作者: Chaimaa Medjadji, Guilain Leduc, Sylvain Kubler, Yves Le Traon
链接: https://arxiv.org/abs/2605.16089v1
完整摘要: Federated Learning (FL) has emerged as a promising paradigm for collaborative model training across distributed edge devices while preserving data privacy especially with the huge increase amount of data due to the adoption of technologies which contributes to the growing number of IoT devices. Storing this amount of data centrally is challenging due to issues like limited communication, privacy, and regulations. FL can be Centralized (CFL), Decentralized (DFL), and Semi-decentralized (SDFL). Choosing the right FL architecture depends on the application's needs. However, very few research studies have experimentally compared these three types of architectures to not only understand the respective strengths and limitations, but also trade-offs between different performance indicators. This paper overcome this lack of analysis, conducting experimental analyses using the Fedstellar simulator, MNIST dataset, and MLP classifier.
匹配关键词: video understanding
---

[ACADEMIC - ARXIV]
标题: Prospective multi-pathogen disease forecasting using autonomous LLM-guided tree search
作者: Sarah Martinson, Michael P. Brenner, Martyna Plomecka, Brian P. Williams, Nicholas G. Reich, Zahra Shamsi
链接: https://arxiv.org/abs/2605.16238v1
完整摘要: Probabilistic forecasting of infectious diseases is crucial for public health but relies on labor-intensive manual model curation by expert modeling teams. This bespoke development bottlenecks scalability to granular geographic resolutions or emerging pathogens. Here, we present an autonomous system using Large Language Model (LLM)-guided tree search to iteratively generate, evaluate, and optimize executable forecasting software. In a fully prospective, real-time evaluation during the 2025-2026 US respiratory season, the system autonomously discovered methodologically diverse models for influenza, COVID-19, and respiratory syncytial virus (RSV). Aggregating these machine-generated models yielded an ensemble that consistently matched or outperformed the gold-standard, human-curated Centers for Disease Control and Prevention (CDC) hub ensembles out-of-sample. The system successfully navigated data-scarce "cold start" scenarios for RSV. Moreover, controlled retrospective ablations revealed that optimizing log-scale distance metrics prevents reward hacking, while an automated judge-in-the-loop ensures structural fidelity to complex scientific theories. By autonomously translating epidemiological theory into accurate, transparent code, this framework overcomes the modeling labor bottleneck, enabling rapid deployment of expert-level disease forecasting at unprecedented scales.
匹配关键词: temporal consistency
---

[ACADEMIC - ARXIV]
标题: Evaluating Design Video Generation: Metrics for Compositional Fidelity
作者: Adrienne Deganutti, Dingning Cao, Jaejung Seol, Elad Hirsch, Purvanshi Mehta
链接: https://arxiv.org/abs/2605.16223v1
完整摘要: Generative video models are increasingly used in design animation tasks, yet no standardized evaluation framework exists for this domain. Unlike natural video generation, design animation imposes structured constraints: specific components shall animate with prescribed motion types, directions, speed and timing, while non-animated regions must remain stable and layout structure must be preserved. This paper provides a fully automated evaluation framework organized across four dimensions: layout fidelity, motion correctness, temporal quality, and content fidelity. This eliminates the reliance on subjective human evaluation and establishes a common basis for benchmarking progress in the field.
匹配关键词: temporal consistency
---

[ACADEMIC - ARXIV]
标题: Hypothesis-driven construction of mesoscopic dynamics
作者: Zhuoyuan Li, Aiqing Zhu, Qianxiao Li
链接: https://arxiv.org/abs/2605.16211v1
完整摘要: Traditional scientific modeling typically begins with fixed, instance-wise effective equations and then carries out equation-specific analysis and computation, a procedure that becomes exceptionally challenging in complex applications such as multiscale systems. We propose an alternative paradigm by learning mesoscopic dynamics within a mathematically constrained hypothesis class. Building upon a generalized Onsager principle, we introduce a unified framework encompassing both dissipative and conservative mesoscopic dynamics. We establish uniform and a priori theoretical guarantees, including global well-posedness, asymptotic stability, unique factorization identifiability, and discrete energy dissipation, applicable to all spatio-temporal evolution equations within this hypothesis class prior to all learning stages. Data from each problem instance is then used to guide the identification of members within our hypothesis class, giving rise to accurate, robust and interpretable dynamical models. We empirically validate this framework on both data from continuum PDE models as a check, and on data arising from microscopic chain models for which exact meso-scale models are unknown. The proposed approach not only acts as an effective dynamics learner, but also offers vital interpretable diagnostics of the underlying physics.
匹配关键词: temporal consistency
---

[ACADEMIC - ARXIV]
标题: Formal Methods Meet LLMs: Auditing, Monitoring, and Intervention for Compliance of Advanced AI Systems
作者: Parand A. Alamdari, Toryn Q. Klassen, Sheila A. McIlraith
链接: https://arxiv.org/abs/2605.16198v1
完整摘要: We examine one particular dimension of AI governance: how to monitor and audit AI-enabled products and services throughout the AI development lifecycle, from pre-deployment testing to post-deployment auditing. Combining principles from formal methods with SoTA machine learning, we propose techniques that enable AI-enabled product and service developers, as well as third party AI developers and evaluators, to perform offline auditing and online (runtime) monitoring of product-specific (temporally extended) behavioral constraints such as safety constraints, norms, rules and regulations with respect to black-box advanced AI systems, notably LLMs. We further provide practical techniques for predictive monitoring, such as sampling-based methods, and we introduce intervening monitors that act at runtime to preempt and potentially mitigate predicted violations. Experimental results show that by exploiting the formal syntax and semantics of Linear Temporal Logic (LTL), our proposed auditing and monitoring techniques are superior to LLM baseline methods in detecting violations of temporally extended behavioral constraints; with our approach, even small-model labelers match or exceed frontier LLM judges. Our predictive and intervening monitors significantly reduce the violation rates of LLM-based agents while largely preserving task performance. We further show through controlled experiments that LLMs' temporal reasoning shows a pronounced degradation in accuracy with increasing event distance, number of constraints, and number of propositions.
匹配关键词: temporal consistency
---

[ACADEMIC - ARXIV]
标题: Imitation learning for clinical decision support in pediatric ECMO
作者: Fateme Golivand, Michael Skinner, Saurabh Mathur, Ameet Soni, Phillip Reeder, Kristian Kersting, Lakshmi Raman, Sriraam Natarajan
链接: https://arxiv.org/abs/2605.16175v1
完整摘要: Pediatric critical care is a dynamic, high-stakes process involving constant monitoring and adjustments in life-saving treatments. Modeling these interventions is crucial for effective decision support. To address the challenges of high complexity and data scarcity in pediatric Extracorporeal Membrane Oxygenation (ECMO), we frame clinical decision-making as learning to act from trajectories, i.e., imitation learning that learns action models from observational data, with a key feature that actions are not directly observed. We consider TabPFN, a recent transformer-based approach for tabular data, and traditional baselines including XGBoost and Multi-Layer Perceptrons(MLPs) on real-world pediatric ECMO data to learn the action models. We find that the TabPFN-based approach consistently outperforms these classical baselines, supporting its use as a strong clinician-behavior baseline for pediatric ECMO decision support.
匹配关键词: temporal consistency
---

[ACADEMIC - ARXIV]
标题: AI-Mediated Communication Can Steer Collective Opinion
作者: Stratis Tsirtsis, Kai Rawal, Chris Russell, Brent Mittelstadt, Sandra Wachter
链接: https://arxiv.org/abs/2605.16245v1
完整摘要: Generative artificial intelligence (AI) is increasingly integrated into the online platforms where humans exchange opinions; large language models (LLMs) now polish users' posts on LinkedIn and provide context for content shared on X. While prior work has shown that AI can express biased opinions and shape individuals' opinions during human-AI interactions, less attention has been paid to its influence on collective opinion formation when mediating human-to-human communication. We address this gap via a combination of empirical and theoretical analyses. We show empirically that LLMs from multiple popular families introduce directional biases when instructed to edit human-written texts on contested topics, for example, nudging texts in favor of gun control and against atheism. Building on this observation, we introduce a mathematical model of opinion dynamics in which an AI system sits between users on a social network, transforming the opinions they express and perceive. By analytically characterizing the equilibrium of this model and performing simulations on real social network data, we show that biases introduced by AI in human-to-human communication can be amplified through the network and shift collective opinion in their direction. In light of these findings, we investigate whether such biases are controllable by online platforms. We audit the "Explain this post" feature on X and find evidence of pro-life bias in Grok's outputs on abortion-related content, which we trace back to specific design choices. We conclude with a discussion of the broader implications of our findings in relation to ongoing legislative efforts in the European Union.
匹配关键词: video LLM
---

[ACADEMIC - ARXIV]
标题: Prospective multi-pathogen disease forecasting using autonomous LLM-guided tree search
作者: Sarah Martinson, Michael P. Brenner, Martyna Plomecka, Brian P. Williams, Nicholas G. Reich, Zahra Shamsi
链接: https://arxiv.org/abs/2605.16238v1
完整摘要: Probabilistic forecasting of infectious diseases is crucial for public health but relies on labor-intensive manual model curation by expert modeling teams. This bespoke development bottlenecks scalability to granular geographic resolutions or emerging pathogens. Here, we present an autonomous system using Large Language Model (LLM)-guided tree search to iteratively generate, evaluate, and optimize executable forecasting software. In a fully prospective, real-time evaluation during the 2025-2026 US respiratory season, the system autonomously discovered methodologically diverse models for influenza, COVID-19, and respiratory syncytial virus (RSV). Aggregating these machine-generated models yielded an ensemble that consistently matched or outperformed the gold-standard, human-curated Centers for Disease Control and Prevention (CDC) hub ensembles out-of-sample. The system successfully navigated data-scarce "cold start" scenarios for RSV. Moreover, controlled retrospective ablations revealed that optimizing log-scale distance metrics prevents reward hacking, while an automated judge-in-the-loop ensures structural fidelity to complex scientific theories. By autonomously translating epidemiological theory into accurate, transparent code, this framework overcomes the modeling labor bottleneck, enabling rapid deployment of expert-level disease forecasting at unprecedented scales.
匹配关键词: video LLM
---

[ACADEMIC - ARXIV]
标题: FORGE: Self-Evolving Agent Memory With No Weight Updates via Population Broadcast
作者: Igor Bogdanov, Chung-Horng Lung, Thomas Kunz, Jie Gao, Adrian Taylor, Marzia Zaman
链接: https://arxiv.org/abs/2605.16233v1
完整摘要: Can LLM agents improve decision-making through self-generated memory without gradient updates? We propose FORGE (Failure-Optimized Reflective Graduation and Evolution), a staged, population-based protocol that evolves prompt-injected natural-language memory for hierarchical ReAct agents. FORGE wraps a Reflexion-style inner loop, where a dedicated reflection agent (using the same underlying LLM, no distillation from a stronger model) converts failed trajectories into reusable knowledge artifacts: textual heuristics (Rules), few-shot demonstrations (Examples), or both (Mixed), with an outer loop that propagates the best-performing instance's memory to the population between stages and freezes converged instances via a graduation criterion. We evaluate on CybORG CAGE-2, a stochastic network-defense POMDP at a 30-step horizon against the B-line attacker, where all four tested LLM families (Gemini-2.5-Flash-Lite, Grok-4-Fast, Llama-4-Maverick, Qwen3-235B) exhibit strongly negative, heavy-tailed zero-shot rewards. Compared against both a zero-shot baseline and a Reflexion baseline (isolated single-stream learning), FORGE improves average evaluation return by 1.7-7.7$\times$ over zero-shot and by 29-72% over Reflexion in all 12 model-representation conditions, reducing major-failure rates (below $-100$) to as low as $\sim$1%. We find that (1) population broadcast is critical mechanism, with a no-graduation ablation confirming that broadcast carries the performance gains while graduation primarily saves compute; (2) Examples achieves the strongest returns for three of four models, Rules offers the best cost-reliability profile with $\sim$40% fewer tokens; and (3) weaker baseline models benefit disproportionately, suggesting FORGE may mitigate capability gaps rather than amplify strong models. All evidence is confined to CAGE-2 B-line; cross-family findings are directional evidence.
匹配关键词: video LLM
---

[ACADEMIC - ARXIV]
标题: Evaluating Design Video Generation: Metrics for Compositional Fidelity
作者: Adrienne Deganutti, Dingning Cao, Jaejung Seol, Elad Hirsch, Purvanshi Mehta
链接: https://arxiv.org/abs/2605.16223v1
完整摘要: Generative video models are increasingly used in design animation tasks, yet no standardized evaluation framework exists for this domain. Unlike natural video generation, design animation imposes structured constraints: specific components shall animate with prescribed motion types, directions, speed and timing, while non-animated regions must remain stable and layout structure must be preserved. This paper provides a fully automated evaluation framework organized across four dimensions: layout fidelity, motion correctness, temporal quality, and content fidelity. This eliminates the reliance on subjective human evaluation and establishes a common basis for benchmarking progress in the field.
匹配关键词: video LLM
---

[ACADEMIC - ARXIV]
标题: Fully Open Meditron: An Auditable Pipeline for Clinical LLMs
作者: Xavier Theimer-Lienhard, Mushtaha El-Amin, Fay Elhassan, Sahaj Vaidya, Victor Cartier-Negadi, David Sasu, Lars Klein, Mary-Anne Hartley
链接: https://arxiv.org/abs/2605.16215v1
完整摘要: Clinical decision support systems (CDSS) require scrutable, auditable pipelines that enable rigorous, reproducible validation. Yet current LLM-based CDSS remain largely opaque. Most "open" models are open-weight only, releasing parameters while withholding the data provenance, curation procedures, and generation pipelines that determine model behavior. Fully Open (FO) models, which expose the complete training stack end-to-end, do not currently exist in medicine. We introduce Fully Open Meditron, the first fully open pipeline for building LLM-CDSS, comprising a clinician-audited training corpus, a reproducible data construction and training framework, and a use-aligned evaluation protocol. The corpus unifies eight public medical QA datasets into a normalized conversational format and expands coverage with three clinician-vetted synthetic extensions: exam-style QA, guideline-grounded QA derived from 46,469 clinical practice guidelines, and clinical vignettes. The pipeline enforces system-wide decontamination, gold-label resampling of teacher generations, and end-to-end validation by a four-physician panel. We evaluate using an LLM-as-a-judge protocol over expert-written clinical vignettes, calibrated against 204 human raters. We apply the recipe to five FO base models (Apertus-70B/8B-Instruct, OLMo-2-32B-SFT, EuroLLM-22B/9B-Instruct). All MeditronFO variants are preferred over their bases. Apertus-70B-MeditronFO improves +6.6 points over its base (47.2% to 53.8%) on aggregate medical benchmarks, establishing a new FO SoTA. Gemma-3-27B-MeditronFO is preferred over MedGemma in 58.6% of LLM-as-a-judge comparisons and outperforms it on HealthBench (58% vs 55.9%). These results show that fully open pipelines can achieve state-of-the-art domain-specific performance without sacrificing auditability or reproducibility.
匹配关键词: video LLM
---

[ACADEMIC - ARXIV]
标题: An Algebraic Exposition of the Theory of Dyadic Morality
作者: Kush R. Varshney
链接: https://arxiv.org/abs/2605.16153v1
完整摘要: This paper provides an algebraic exposition of the theory of dyadic morality (TDM), a psychological model of moral judgment grounded in a simple two-node template: an intentional agent causing harm to a vulnerable patient. We formalize TDM using structural causal modeling (SCM) notation and identify three psychological operators (typecasting operator, completion operator, and valence-dependent inference mechanism) that extend standard SCM to capture how people compute moral judgments under constraints. We address scalability challenges arising from TDM's dyadic limitation, showing how moral cognition compresses multi-node scenarios through node collapse and sequential processing. Drawing on this algebraic framework, we demonstrate concrete applications to AI policy design: detecting conflicting obligations, structuring helpfulness policies to preserve user agency, and designing post-failure communication as causal interventions. Finally, we recommend scoped, contextual measurement of mind perception over universal averaging to operationalize the theory empirically. This algebraic formalization enables neurosymbolic AI systems to compute morality in a way that is both mathematically rigorous and faithful to human moral cognition.
匹配关键词: multi-agent
---

[ACADEMIC - ARXIV]
标题: Surrogate Neural Architecture Codesign Package (SNAC-Pack)
作者: Jason Weitz, Dmitri Demler, Benjamin Hawks, Aaron Wang, Nhan Tran, Javier Duarte
链接: https://arxiv.org/abs/2605.16138v1
完整摘要: Neural architecture search (NAS) is a powerful approach for automating model design, but existing methods often optimize for accuracy alone or rely on proxy metrics such as bit operations (BOPs) that correlate poorly with hardware cost. This gap is particularly large for FPGA deployment, where cost is dominated by a multi-dimensional budget of lookup tables, DSPs, flip-flops, BRAM, and latency. We present the Surrogate Neural Architecture Codesign Package (SNAC-Pack), an open-source AutoML framework for hardware-aware neural architecture codesign and end-to-end FPGA deployment. SNAC-Pack runs a multi-objective global search with Optuna and NSGA-II, loading trials to a shared SQLite store that enables parallel workers across compute nodes. A hardware surrogate model outputs per-trial resource and latency estimates, avoiding the synthesis cost that would otherwise dominate the search loop. A local search stage then applies quantization-aware training (QAT) together with iterative magnitude pruning in a combined compression loop, after which the final model is synthesized to FPGA firmware via the hls4ml Python library. A YAML configuration and an optional agentic frontend let users run the pipeline on new datasets without modifying the framework. We demonstrate SNAC-Pack on jet classification at the Large Hadron Collider and superconducting qubit readout, discovering compact architectures that match or exceed strong baselines on the task metric while reducing FPGA resource utilization and, in the qubit readout case, reducing the design space exploration process from months of manual fine-tuning to hours of automated search.
匹配关键词: multi-agent
---

[ACADEMIC - ARXIV]
标题: RoadmapBench: Evaluating Long-Horizon Agentic Software Development Across Version Upgrades
作者: Xinbo Xu, Ruihan Yang, Haiyang Shen, Wendong Xu, Bofei Gao, Ruoyu Wu, Kean Shi, Weichu Xie, Xuanzhong Chen, Ming Wu, Jason Zeng, Michael Heinrich, Elvis Zhang, Liang Chen, Kuan Li, Baobao Chang
链接: https://arxiv.org/abs/2605.15846v1
完整摘要: Coding agents are increasingly deployed in real software development, where a single version iteration requires months of coordinated work across many files. However, most existing benchmarks focus predominantly on single-issue bug fixes from Python repositories, with coarse pass/fail evaluation outcomes, and thus fail to capture long-horizon, multi-target development at real engineering scale. To address this gap, we present RoadmapBench, a benchmark of 115 long-horizon coding tasks grounded in real open-source version upgrades across 17 repositories and 5 programming languages. Each task places the agent on a source-version code snapshot and provides a multi-target roadmap instruction requiring it to implement the functionality introduced in the target version, with a median modification of 3,700 lines across 51 files. We conduct a systematic evaluation on thirteen frontier models and find that even the strongest, Claude-Opus-4.7, resolves only 39.1% of tasks, while the weakest achieves merely 5.2%, in stark contrast to existing bug-fix benchmarks, suggesting that long-horizon software development remains a largely unsolved problem.
匹配关键词: multi-agent
---

[ACADEMIC - ARXIV]
标题: BootstrapAgent: Distilling Repository Setup into Reusable Agent Knowledge
作者: Sihan Fu, Oucheng Liu, Shiyuan Wang, Jin Shi, Chengkun Wei
链接: https://arxiv.org/abs/2605.15815v1
完整摘要: Code agents increasingly help developers work with unfamiliar repositories, but every such task depends on a costly prerequisite: bootstrapping the repository into a usable development state. This process requires substantial trial-and-error exploration, yet the resulting knowledge--resolved dependencies, repair strategies--stays trapped in a single conversation, unavailable to future agents. We therefore formulate repository bootstrapping as a reusable startup knowledge problem and introduce BootstrapAgent, a multi-agent framework that distills the heuristics discovered during bootstrap exploration into a persistent, verifiable, agent-consumable .bootstrap contract. Through evidence extraction, structured planning, deterministic Docker-based verification, and trace-driven repair, BootstrapAgent generates a contract covering environment setup, diagnostic checks, minimal verification, and accumulated repair knowledge. We further propose warm repair with clean replay to accelerate iterative debugging without sacrificing cold-start reproducibility, and a delta repair with sanity check to prevent reward hacking. Experiments on three benchmarks show that BootstrapAgent achieves a 92.9% success rate, outperforming the baseline by over 10% while reducing downstream agent token usage by 25.9% and build time by 22.3%. Our code is available at https://github.com/Vossera/BootstrapAgent.
匹配关键词: multi-agent
---

[ACADEMIC - ARXIV]
标题: From Gridworlds to Warehouses: Adapting Lightweight One-shot Multi-Agent Pathfinding for AGVs
作者: Hiroki Nagai, Keisuke Okumura
链接: https://arxiv.org/abs/2605.15799v1
完整摘要: Multi-agent pathfinding (MAPF) under one-shot planning is a core component of warehouse automation, yet classical formulations typically assume four-connected 2D grids with unit-time moves in four directions. To fill reality gaps while still being trackable with discrete combinatorial search, this work proposes a more practical counterpart tailored to differential-drive AGVs. We term this multi-agent warehouse pathfinding (MAWPF), featured with four constraints: (i) agent actions are restricted to straight motion and in-place rotation; (ii) rotations require multi-step costs; (iii) acceleration and deceleration are considered, and; (iv) follower collisions are prohibited to prevent rear-end crashes. To solve MAWPF efficiently, we adapt representative suboptimal MAPF algorithms-PP, LNS2, PIBT, and LaCAM-and conduct comprehensive benchmarking. Our experiments reveal that PP and LNS2 struggle to solve instances with many agents, while PIBT-based approaches achieve preferable scalability with increased solution cost. We believe that these constitute an important step toward adapting classical gridworld MAPF to operational warehouse setups.
匹配关键词: multi-agent
---

[ACADEMIC - ARXIV]
标题: IVGT: Implicit Visual Geometry Transformer for Neural Scene Representation
作者: Yuqi Wu, Tianyu Hu, Wenzhao Zheng, Yuanhui Huang, Haowen Sun, Jie Zhou, Jiwen Lu
链接: https://arxiv.org/abs/2605.16258v1
完整摘要: Reconstructing coherent 3D geometry and appearance from unposed multi-view images is a fundamental yet challenging problem in computer vision. Most existing visual geometry foundation models predict explicit geometry by regressing pixel-aligned pointmaps, often suffering from redundancy and limited geometric continuity. We propose IVGT, an Implicit Visual Geometry Transformer that implicitly models continuous and coherent geometry from pose-free multi-view images. This formulation learns a continuous neural scene representation in a canonical coordinate system and supports continuous spatial queries at any 3D positions, retrieving local features to predict signed distance (SDF) values and colors using lightweight decoders. It allows direct extraction of continuous and coherent surface geometry, enabling rendering of RGB images, depth maps, and surface normal maps from arbitrary viewpoints. We train IVGT via multi-dataset joint optimization with 2D supervision and 3D geometric regularization. IVGT demonstrates generalization across scenes and achieves strong performance on various tasks, including mesh and point cloud reconstruction, novel view synthesis, depth and surface normal estimation, and camera pose estimation.
匹配关键词: agent coordination
---

[ACADEMIC - ARXIV]
标题: DexJoCo: A Benchmark and Toolkit for Task-Oriented Dexterous Manipulation on MuJoCo
作者: Hanwen Wang, Weizhi Zhao, Xiangyu Wang, Siyuan Huang, He Lin, Boyuan Zheng, Rongtao Xu, Gang Wang, Yao Mu, He Wang, Lue Fan, Hongsheng Li, Zhaoxiang Zhang, Tieniu Tan
链接: https://arxiv.org/abs/2605.16257v1
完整摘要: Achieving human-level manipulation requires dexterous robotic hands capable of complex object interactions. Advancing such capabilities further demands standardized benchmarks for systematic evaluation. However, existing dexterous benchmarks lack tasks that reflect the unique manipulation capabilities of dexterous hands over parallel grippers, as well as comprehensive evaluation pipelines. In this paper, we present DexJoCo, a benchmark and toolkit for task-oriented dexterous manipulation, comprising 11 functionally grounded tasks that evaluate tool-use, bimanual coordination, long-horizon execution, and reasoning. We develop a low-cost data collection system and collect 1.1K trajectories across these tasks, with support for domain randomization to assess robustness. We benchmark modern models under diverse settings, including visual and dynamics randomization, multi-task training, and action-head adaptation. Through extensive empirical analysis, we identify several important insights and common limitations of current policies in dexterous manipulation, highlighting key challenges for future research in dexterous hand robot learning. Project page available at: https://dexjoco.github.io
匹配关键词: agent coordination
---

[ACADEMIC - ARXIV]
标题: A Generative AI Framework for Intelligent Utility Billing CO 2 Analytics and Sustainable Resource Optimisation
作者: Pavan Manjunath, Thomas Pruefer
链接: https://arxiv.org/abs/2605.16250v1
完整摘要: Distribution utilities are now expected to deliver bills that customers can actually read attach a defensible carbon number to every kWh sold and schedule load against grid stress and emissions constraints We propose an end-to-end framework that unifies four production-grade capabilities under one architectural roof a generative-AI agent that drafts each customers natural-language billing statement from structured numeric inputs under a constrained decoding policy a transformer-based forecaster that supplies the day-ahead consumption estimate with calibrated quantile bands
匹配关键词: agent coordination
---

[ACADEMIC - ARXIV]
标题: FORGE: Self-Evolving Agent Memory With No Weight Updates via Population Broadcast
作者: Igor Bogdanov, Chung-Horng Lung, Thomas Kunz, Jie Gao, Adrian Taylor, Marzia Zaman
链接: https://arxiv.org/abs/2605.16233v1
完整摘要: Can LLM agents improve decision-making through self-generated memory without gradient updates? We propose FORGE (Failure-Optimized Reflective Graduation and Evolution), a staged, population-based protocol that evolves prompt-injected natural-language memory for hierarchical ReAct agents. FORGE wraps a Reflexion-style inner loop, where a dedicated reflection agent (using the same underlying LLM, no distillation from a stronger model) converts failed trajectories into reusable knowledge artifacts: textual heuristics (Rules), few-shot demonstrations (Examples), or both (Mixed), with an outer loop that propagates the best-performing instance's memory to the population between stages and freezes converged instances via a graduation criterion. We evaluate on CybORG CAGE-2, a stochastic network-defense POMDP at a 30-step horizon against the B-line attacker, where all four tested LLM families (Gemini-2.5-Flash-Lite, Grok-4-Fast, Llama-4-Maverick, Qwen3-235B) exhibit strongly negative, heavy-tailed zero-shot rewards. Compared against both a zero-shot baseline and a Reflexion baseline (isolated single-stream learning), FORGE improves average evaluation return by 1.7-7.7$\times$ over zero-shot and by 29-72% over Reflexion in all 12 model-representation conditions, reducing major-failure rates (below $-100$) to as low as $\sim$1%. We find that (1) population broadcast is critical mechanism, with a no-graduation ablation confirming that broadcast carries the performance gains while graduation primarily saves compute; (2) Examples achieves the strongest returns for three of four models, Rules offers the best cost-reliability profile with $\sim$40% fewer tokens; and (3) weaker baseline models benefit disproportionately, suggesting FORGE may mitigate capability gaps rather than amplify strong models. All evidence is confined to CAGE-2 B-line; cross-family findings are directional evidence.
匹配关键词: agent coordination
---

[ACADEMIC - ARXIV]
标题: Universal Magnetic Structure Prediction from Atomic Coordinates with Near-Experimental Accuracy
作者: Abhijatmedhi Chotrattanapituk, Ryotaro Okabe, Eunbi Rha, Mariya Al-Hinai, Eugene Jiang, Daniel Pajerowski, Yongqiang Cheng, Joshua J. Turner, Mingda Li
链接: https://arxiv.org/abs/2605.16230v1
完整摘要: Magnetic order is a fundamental property of materials, governing collective behavior and enabling a broad range of functionalities. Yet magnetic structure remains difficult to determine: experiments are costly and specialized, while first-principles methods often struggle with the noncollinear and incommensurate orders found in real materials. Here we introduce magnetic structure network (MSN), an E(3) equivariant graph neural network that predicts both collinear and non-collinear magnetic structures directly from atomic crystal structures, trained directly on experimentally determined structures from MAGNDATA. By proposing the primitive modulated structure representation (PMSR), we are able to encode commensurate and incommensurate structures in a unified way without symmetry assumptions. The model achieves strong performance across all modulation components and reconstructs experimental magnetic structures with high fidelity. Our approach provides a scalable framework for rapid magnetic structure prediction and opens a route to data-driven discovery of magnetic materials.
匹配关键词: agent coordination
---

[ACADEMIC - ARXIV]
标题: A Generative AI Framework for Intelligent Utility Billing CO 2 Analytics and Sustainable Resource Optimisation
作者: Pavan Manjunath, Thomas Pruefer
链接: https://arxiv.org/abs/2605.16250v1
完整摘要: Distribution utilities are now expected to deliver bills that customers can actually read attach a defensible carbon number to every kWh sold and schedule load against grid stress and emissions constraints We propose an end-to-end framework that unifies four production-grade capabilities under one architectural roof a generative-AI agent that drafts each customers natural-language billing statement from structured numeric inputs under a constrained decoding policy a transformer-based forecaster that supplies the day-ahead consumption estimate with calibrated quantile bands
匹配关键词: decentralized agent
---

[ACADEMIC - ARXIV]
标题: FORGE: Self-Evolving Agent Memory With No Weight Updates via Population Broadcast
作者: Igor Bogdanov, Chung-Horng Lung, Thomas Kunz, Jie Gao, Adrian Taylor, Marzia Zaman
链接: https://arxiv.org/abs/2605.16233v1
完整摘要: Can LLM agents improve decision-making through self-generated memory without gradient updates? We propose FORGE (Failure-Optimized Reflective Graduation and Evolution), a staged, population-based protocol that evolves prompt-injected natural-language memory for hierarchical ReAct agents. FORGE wraps a Reflexion-style inner loop, where a dedicated reflection agent (using the same underlying LLM, no distillation from a stronger model) converts failed trajectories into reusable knowledge artifacts: textual heuristics (Rules), few-shot demonstrations (Examples), or both (Mixed), with an outer loop that propagates the best-performing instance's memory to the population between stages and freezes converged instances via a graduation criterion. We evaluate on CybORG CAGE-2, a stochastic network-defense POMDP at a 30-step horizon against the B-line attacker, where all four tested LLM families (Gemini-2.5-Flash-Lite, Grok-4-Fast, Llama-4-Maverick, Qwen3-235B) exhibit strongly negative, heavy-tailed zero-shot rewards. Compared against both a zero-shot baseline and a Reflexion baseline (isolated single-stream learning), FORGE improves average evaluation return by 1.7-7.7$\times$ over zero-shot and by 29-72% over Reflexion in all 12 model-representation conditions, reducing major-failure rates (below $-100$) to as low as $\sim$1%. We find that (1) population broadcast is critical mechanism, with a no-graduation ablation confirming that broadcast carries the performance gains while graduation primarily saves compute; (2) Examples achieves the strongest returns for three of four models, Rules offers the best cost-reliability profile with $\sim$40% fewer tokens; and (3) weaker baseline models benefit disproportionately, suggesting FORGE may mitigate capability gaps rather than amplify strong models. All evidence is confined to CAGE-2 B-line; cross-family findings are directional evidence.
匹配关键词: decentralized agent
---

[ACADEMIC - ARXIV]
标题: Argus: Evidence Assembly for Scalable Deep Research Agents
作者: Zhen Zhang, Liangcai Su, Zhuo Chen, Xiang Lin, Haotian Xu, Simon Shaolei Du, Kaiyu Yang, Bo An, Lidong Bing, Xinyu Wang
链接: https://arxiv.org/abs/2605.16217v1
完整摘要: Deep research agents have achieved remarkable progress on complex information seeking tasks. Even long ReAct style rollouts explore only a single trajectory, while recent state of the art systems scale inference time compute via parallel search and aggregation. Yet deep research answers are composed of complementary pieces of evidence, which parallel rollouts often duplicate rather than complete, yielding diminishing returns while pushing the aggregation context toward the model's limit. We propose Argus, an agentic system in which a Searcher and a Navigator cooperate to treat deep research as assembling a jigsaw from complementary evidence pieces, rather than brute forcing the whole answer in parallel. The Searcher collects evidence traces for a given sub-query through ReAct-style interaction. The Navigator maintains a shared evidence graph, verifying which pieces are still missing, dispatching Searchers to gather them, and reasoning over the completed graph to produce a source-traced final answer. We train the Navigator with reinforcement learning to verify, dispatch, and synthesize, while independently training the Searcher to remain a standard ReAct agent. The resulting Navigator supports rollouts with a single Searcher or many in parallel without retraining. With both Searcher and Navigator built on a 35B-A3B MoE backbone, Argus gains 5.5 points with a single Searcher and 12.7 points with 8 parallel Searchers, averaged over eight benchmarks. With 64 Searchers it reaches 86.2 on BrowseComp, surpassing every proprietary agent we benchmark, while the Navigator's reasoning context stays under 21.5K tokens.
匹配关键词: decentralized agent
---

[ACADEMIC - ARXIV]
标题: Confirming Correct, Missing the Rest: LLM Tutoring Agents Struggle Where Feedback Matters Most
作者: Tahreem Yasir, Wenbo Li, Sam Gilson, Sutapa Dey Tithi, Xiaoyi Tian, Tiffany Barnes
链接: https://arxiv.org/abs/2605.16207v1
完整摘要: Effective tutoring requires distinguishing optimal, valid but suboptimal, and incorrect student solutions, a distinction central to intelligent tutoring systems (ITS) but untested for LLM-based tutors. As LLMs are increasingly explored as conversational complements to ITS, evaluating their diagnostic precision is essential. We present a benchmark of seven LLM feedback agents in propositional logic using knowledge-graph-derived ground truth across 10,836 solution--feedback pairs and three feedback conditions. Models achieved near-ceiling performance on optimal steps but systematically over-rejected valid but suboptimal reasoning and over-validated incorrect solutions, precisely where adaptive tutoring matters most. These failures persisted across models regardless of solution context, suggesting architectural rather than informational limits. Moreover, accurate diagnosis did not reliably produce pedagogically actionable feedback, revealing a gap between diagnostic judgment and instructional effectiveness. Our findings suggest that LLMs are better suited for hybrid architectures where KG-grounded models handle diagnosis while LLMs support open-ended scaffolding and dialogue.
匹配关键词: decentralized agent
---

[ACADEMIC - ARXIV]
标题: Context, Reasoning, and Hierarchy: A Cost-Performance Study of Compound LLM Agent Design in an Adversarial POMDP
作者: Igor Bogdanov, Chung-Horng Lung, Thomas Kunz, Jie Gao, Adrian Taylor, Marzia Zaman
链接: https://arxiv.org/abs/2605.16205v1
完整摘要: Deploying compound LLM agents in adversarial, partially observable sequential environments requires navigating several design dimensions: (1) what the agent sees, (2) how it reasons, and (3) how tasks are decomposed across components. Yet practitioners lack guidance on which design choices improve performance versus merely increase inference costs. We present a controlled study of compound LLM agent design in CybORG CAGE-2, a cyber defense environment modeled as a Partially Observable Markov Decision Process (POMDP). Reward is non-positive, so all configurations operate in a failure-mitigation mode. Our evaluation spans five model families, six models, and twelve configurations (3,475 episodes) with token-level cost accounting. We vary context representation (raw observations vs. a deterministic state-tracking layer with compressed history), deliberation (self-questioning, self-critique, and self-improvement tools, with optional chain-of-thought prompting), and hierarchical decomposition (monolithic ReAct vs. delegation to specialized sub-agents). We find that: (1) Programmatic state abstraction delivers the largest returns per token spent (RPTS), improving mean return by up to 76% over raw observations. (2) Distributing deliberation tools across a hierarchy degrades performance relative to hierarchy alone for all five model families, reaching up to 3.4$\times$ worse mean return while using 1.8-2.7$\times$ more tokens. We call this destructive pattern a deliberation cascade. (3) Hierarchical decomposition without deliberation achieves the best absolute performance for most models, and context engineering is generally more cost-effective than deliberation. These findings suggest a design principle for structured adversarial POMDPs: invest in programmatic infrastructure and clean task decomposition rather than deeper per-agent reasoning, as these strategies can interfere when combined.
匹配关键词: decentralized agent
---

[ACADEMIC - ARXIV]
标题: IVGT: Implicit Visual Geometry Transformer for Neural Scene Representation
作者: Yuqi Wu, Tianyu Hu, Wenzhao Zheng, Yuanhui Huang, Haowen Sun, Jie Zhou, Jiwen Lu
链接: https://arxiv.org/abs/2605.16258v1
完整摘要: Reconstructing coherent 3D geometry and appearance from unposed multi-view images is a fundamental yet challenging problem in computer vision. Most existing visual geometry foundation models predict explicit geometry by regressing pixel-aligned pointmaps, often suffering from redundancy and limited geometric continuity. We propose IVGT, an Implicit Visual Geometry Transformer that implicitly models continuous and coherent geometry from pose-free multi-view images. This formulation learns a continuous neural scene representation in a canonical coordinate system and supports continuous spatial queries at any 3D positions, retrieving local features to predict signed distance (SDF) values and colors using lightweight decoders. It allows direct extraction of continuous and coherent surface geometry, enabling rendering of RGB images, depth maps, and surface normal maps from arbitrary viewpoints. We train IVGT via multi-dataset joint optimization with 2D supervision and 3D geometric regularization. IVGT demonstrates generalization across scenes and achieves strong performance on various tasks, including mesh and point cloud reconstruction, novel view synthesis, depth and surface normal estimation, and camera pose estimation.
匹配关键词: test-time compute
---

[ACADEMIC - ARXIV]
标题: Designing Datacenter Power Delivery Hierarchies for the AI Era
作者: Grant Wilkins, Fiodar Kazhamiaka, Alok Gautam Kumbhare, Chaojie Zhang, Ricardo Bianchini
链接: https://arxiv.org/abs/2605.16255v1
完整摘要: Demand for AI accelerators is rapidly increasing rack power density, with projections approaching 1MW per deployment by 2027. This poses a major challenge for datacenter power delivery designers. As power densities increase, a datacenter designed for a different target density may strand power, i.e., may be unable to use all the power that its delivery hierarchy has provisioned. Designs must remain efficient over long datacenter lifetimes and multiple hardware generations. Power utilization is particularly important as grid power capacity is a scarce resource in the AI era. Designing an efficient power delivery hierarchy for the long run is difficult because rack placement feasibility, workload impact, and cost depend jointly on electrical topology, deployment granularity, placement policy, power oversubscription, and workload mix. Moreover, each of these factors evolve over time, have inter-dependencies across multiple resource dimensions, and generally do not lend themselves to closed-form analysis. To address this challenge, we develop a framework for evaluating datacenter power delivery designs using throughput, power, and cost metrics over realistic arrival, oversubscription, and decommissioning sequences. The framework combines projection models for GPU, compute, and storage deployments with operational factors grounded in production data from Microsoft Azure. Our results show that multi-resource stranding materially changes deployable capacity, effective capital expenditure, and delivered performance, and quantify how rising density from rack- and pod-scale AI systems shapes these outcomes. For AI datacenter design, the relevant planning objective is not installed megawatts, but deployable capacity over time.
匹配关键词: test-time compute
---

[ACADEMIC - ARXIV]
标题: Real-time Speech Restoration using Data Prediction Mean Flows
作者: Sebastian Braun
链接: https://arxiv.org/abs/2605.16251v1
完整摘要: Generative models are capable to address difficult problems with non-unique solutions like bandwidth extension and gap filling, removing highly non-linear artifacts from codecs, clipping and distortion, as opposed to removing linear additive components like noise and reverb. While large offline processing models have shown impressive results, these tasks have not been solved with real-time capable models with low latency and compute. We propose a few-step flow matching model using Data Prediction Mean Flows in combination with suitable novel low-latency architecture to make flow matching models an attractive choice under theses constraints. Compared to state-of-the-art, our proposed mean flow model uses 120x less compute and introduces no algorithmic latency other than the STFT, while achieving similar audio quality.
匹配关键词: test-time compute
---

[ACADEMIC - ARXIV]
标题: Offline Semantic Guidance for Efficient Vision-Language-Action Policy Distillation
作者: Jin Shi, Brady Zhang, Yishun Lu
链接: https://arxiv.org/abs/2605.16241v1
完整摘要: Billion-parameter Vision-Language-Action (VLA) policies have recently shown impressive performance in robotic manipulation, yet their size and inference cost remain major obstacles for real-time closed-loop control. We introduce \textbf{VLA-AD}, a distillation framework that uses a Vision-Language Model as an offline semantic supervisor to transfer large VLA teachers into lightweight student policies. Instead of relying only on low-level action imitation, VLA-AD augments teacher-provided 7-DoF action targets with high-level semantic guidance, including task phase anchors and multi-frame operating-direction descriptions. These auxiliary signals are used only during training: at test time, the student policy runs independently, with neither the VLA teacher nor the VLM required. We evaluate VLA-AD on three LIBERO benchmark suites. Using OpenVLA-7B as the teacher, our method produces a 158M-parameter student, yielding a $44\times$ reduction in model size while matching the teacher with only a $0.27\%$ average relative gap. The resulting policy runs at 12.5 Hz on an RTX 4090, achieving a $3.28\times$ inference speedup over OpenVLA-7B. We further show that the same semantic distillation pipeline generalizes to a different $π_{0.5}$-4B teacher, where the student outperforms the teacher on two suites and remains within $0.53\%$ on \texttt{libero\_goal}. Additional analysis indicates that phase-level supervision and multi-frame directional cues make the student less sensitive to noisy teacher actions, such as erroneous high-frequency gripper changes. Overall, VLA-AD demonstrates that offline semantic guidance from VLMs can substantially improve the efficiency, robustness, and deployability of VLA policy distillation.
匹配关键词: test-time compute
---

[ACADEMIC - ARXIV]
标题: FORGE: Self-Evolving Agent Memory With No Weight Updates via Population Broadcast
作者: Igor Bogdanov, Chung-Horng Lung, Thomas Kunz, Jie Gao, Adrian Taylor, Marzia Zaman
链接: https://arxiv.org/abs/2605.16233v1
完整摘要: Can LLM agents improve decision-making through self-generated memory without gradient updates? We propose FORGE (Failure-Optimized Reflective Graduation and Evolution), a staged, population-based protocol that evolves prompt-injected natural-language memory for hierarchical ReAct agents. FORGE wraps a Reflexion-style inner loop, where a dedicated reflection agent (using the same underlying LLM, no distillation from a stronger model) converts failed trajectories into reusable knowledge artifacts: textual heuristics (Rules), few-shot demonstrations (Examples), or both (Mixed), with an outer loop that propagates the best-performing instance's memory to the population between stages and freezes converged instances via a graduation criterion. We evaluate on CybORG CAGE-2, a stochastic network-defense POMDP at a 30-step horizon against the B-line attacker, where all four tested LLM families (Gemini-2.5-Flash-Lite, Grok-4-Fast, Llama-4-Maverick, Qwen3-235B) exhibit strongly negative, heavy-tailed zero-shot rewards. Compared against both a zero-shot baseline and a Reflexion baseline (isolated single-stream learning), FORGE improves average evaluation return by 1.7-7.7$\times$ over zero-shot and by 29-72% over Reflexion in all 12 model-representation conditions, reducing major-failure rates (below $-100$) to as low as $\sim$1%. We find that (1) population broadcast is critical mechanism, with a no-graduation ablation confirming that broadcast carries the performance gains while graduation primarily saves compute; (2) Examples achieves the strongest returns for three of four models, Rules offers the best cost-reliability profile with $\sim$40% fewer tokens; and (3) weaker baseline models benefit disproportionately, suggesting FORGE may mitigate capability gaps rather than amplify strong models. All evidence is confined to CAGE-2 B-line; cross-family findings are directional evidence.
匹配关键词: test-time compute
---

[ACADEMIC - ARXIV]
标题: DebiasRAG: A Tuning-Free Path to Fair Generation in Large Language Models through Retrieval-Augmented Generation
作者: Rui Chu, Bingyin Zhao, Thanh Quoc Hung Le, Duy Cao Hoang, Huawei Lin, Ping Li, Weijie Zhao, Khoa D Doan, Yingjie Lao
链接: https://arxiv.org/abs/2605.16113v1
完整摘要: Large language models (LLMs) have achieved unprecedented success due to their exceptional generative capabilities. However, because they depend on knowledge encapsulated from training corpora, they may produce hallucinations, stereotypes, and socially biased content. In particular, LLMs are prone to prejudiced responses involving race, gender, and age, which are collectively referred to as social biases. Prior studies have used fine-tuning and prompt engineering to mitigate such biases in LLMs, but these methods require additional training resources or domain knowledge to design the framework. Moreover, they may degrade the original capabilities of LLMs and often overlook the need for dynamic debiasing contexts for fairer inference. In this paper, we propose DebiasRAG, a novel tuning-free and dynamic query-specific debiasing framework based on retrieval-augmented generation (RAG). DebiasRAG improves fairness while preserving the intrinsic properties of LLMs, such as representation ability. DebiasRAG consists of three stages: (1) query-specific debiasing candidate generation; (2) context candidate pool construction; and (3) gradient-updated debiasing-guided context piece reranking. First, DebiasRAG leverages self-diagnosed bias contexts relevant to the query through regular retrieval, where the bias contexts are prepared offline by the DebiasRAG provider. Given the query-specific bias contexts, DebiasRAG reversely produces debiasing contexts, which are provided as additional fairness constraints for LLM outputs. Second, a regular RAG retrieval process produces query-related contexts from the regular RAG document database, such as a chunked Wikipedia dataset.
匹配关键词: self-consistency
---

[ACADEMIC - ARXIV]
标题: Learning Sim-Grounded Policies for Bimanual Rope Manipulation from Human Teleoperation Data
作者: Gina Wigginghaus, Tim Missal, Berk Guler, Simon Manschitz, Jan Peters
链接: https://arxiv.org/abs/2605.16043v1
完整摘要: Deformable Linear Objects (DLOs) such as ropes and cables are widely encountered in both household and industrial applications, yet remain challenging to manipulate due to their infinite-dimensional configuration space and frequent self-occlusion. Imitation learning from teleoperation offers a practical path to bimanual DLO manipulation, but its scalability is limited by human effort, making the choice of observation space critical for generalization from small datasets. In this study, we investigate whether the lack of generalization in egocentric visual policies for the knot-untangling task stems from the observation space itself, rather than from the policy architecture or data scale. We compare two Action Chunking with Transformers policies trained on the same bimanual teleoperation data: a vision-based policy conditioned on two egocentric RGB streams from wrist-mounted cameras, and a state-based policy conditioned on the DLO's 3D particle state, extracted from an initial observation via multi-view fusion and evolved in a particle-based eXtended Position-Based Dynamics simulation. Evaluated open-loop on an unseen rope configuration, the state-based policy outperforms its visual counterpart with a 30.8% reduction in L1 error when predicting the initial grasp-and-pull action, quantifying the observability gap between pixels and physics-consistent state, and pointing toward more data-efficient robot learning for the DLO manipulation task from limited human demonstrations.
匹配关键词: self-consistency
---

[ACADEMIC - ARXIV]
标题: Agentic Discovery of Neural Architectures: AIRA-Compose and AIRA-Design
作者: Alberto Pepe, Chien-Yu Lin, Despoina Magka, Bilge Acun, Yannan Nellie Wu, Anton Protopopov, Carole-Jean Wu, Yoram Bachrach
链接: https://arxiv.org/abs/2605.15871v1
完整摘要: Toward recursive self-improvement, we investigate LLM agents autonomously designing foundation models beyond standard Transformers. We introduce a dual-framework approach: AIRA-Compose for high-level architecture search, and AIRA-Design for low-level mechanistic implementation. AIRA-Compose uses 11 agents to explore fundamental computational primitives under a 24-hour budget. Agents evaluate million-parameter candidates, extrapolating top designs to 350M, 1B, and 3B scales. This yields 14 architectures across two families: AIRAformers (Transformer-based) and AIRAhybrids (Transformer-Mamba). Pre-trained at 1B scale, these consistently outperform Llama 3.2 and Composer-found baselines. On downstream tasks, AIRAformer-D and AIRAhybrid-D improve accuracy by 2.4% and 3.8% over Llama 3.2. Furthermore, AIRA-Compose finds models with highly efficient scaling frontiers: AIRAformer-C scales 54% and 71% faster than Llama 3.2 and Composer's best Transformer, while AIRAhybrid-C outscales Nemotron-2 by 23% and Composer's best hybrid by 37%. AIRA-Design tasks 20 agents with writing novel attention mechanisms for long-range dependencies and high-performing training scripts. On the Long Range Arena benchmark, agent-designed architectures reach within 2.3% and 2.6% of human state-of-the-art on document matching and text classification. On the Autoresearch benchmark, Greedy Opus 4.5 achieves 0.968 validation bits-per-byte under a fixed time budget, surpassing the published minimum. Together, these frameworks show AI agents can autonomously discover architectures and algorithmic optimizations matching or surpassing hand-designed baselines. This establishes a powerful paradigm for discovering next-generation foundation models, marking a clear step toward recursive self-improvement.
匹配关键词: self-consistency
---

[ACADEMIC - ARXIV]
标题: Cross-Modal Registration Between 3D and 2D Fingerprints via Pose-Aware Unwrapping and Point-Cloud Fusion
作者: Xiongjun Guan, Jianjiang Feng, Jie Zhou
链接: https://arxiv.org/abs/2605.15796v1
完整摘要: Three-dimensional (3D) fingerprints preserve global finger geometry and local ridge structure while avoiding contact-induced deformation, but they remain difficult to integrate with legacy two-dimensional (2D) fingerprint systems. This paper addresses the intermediate stage between 3D acquisition and cross-modal matching, and presents a unified framework for 3D fingerprint preprocessing and registration across contactless and contact-based 2D modalities. The framework combines four components: 1) a nonparametric visualization and unwrapping method that converts a 3D fingerprint point cloud into a rolled-equivalent 2D representation without relying on a global finger-shape model; 2) a point-cloud fusion pipeline that registers and mosaics multiple partial 3D captures into a more complete fingerprint model; 3) an ellipse-based pose normalization method for canonical finger alignment; and 4) a pose-aware cross-modal registration strategy that improves compatibility between 3D fingerprints and both contactless and contact-based 2D fingerprints. Experiments on a self-collected multimodal fingerprint database containing 150 fingers show that the proposed framework achieves ridge-level 3D registration accuracy, robust pose estimation, and consistent gains in 2D compatibility. In particular, the 3D fusion error is concentrated around 0.09 mm, contactless 2D--3D registration reaches ridge-scale projection accuracy, and pose-aware unwrapping improves genuine matching scores relative to generic 3D unwrapping. These results support the use of 3D fingerprints as an effective geometric bridge across heterogeneous fingerprint modalities.
匹配关键词: self-consistency
---

[ACADEMIC - ARXIV]
标题: Reversing the Flow: Generation-to-Understanding Synergy in Large Multimodal Models
作者: Yujun Tong, Dongliang Chang, Zijin Yin, Xintong Liu, Yuanchen Fang, Zhanyu Ma
链接: https://arxiv.org/abs/2605.15792v1
完整摘要: The long-standing goal of multimodal AI is to build unified models in which visual understanding and visual generation mutually enhance one another. Despite recent works such as BAGEL, BLIP3o achieves remarkable progress; In practice, however, this unification remains one-directional: understanding routinely guides generation, yet how and why generation can support understanding is rarely investigated. We revisit this asymmetry and propose Generation-to-Understanding (G2U) synergy, where visual generation becomes an explicit intermediate reasoning step. Our framework enables a model to perform controlled generative acts, such as detail enhancement, context expansion or structural visualisation, to produce self-generated visual thoughts, which are then fed back into the model to refine perception without retraining or external tools. Through a comprehensive evaluation on twelve benchmarks, this reversed information flow consistently improves multimodal understanding. We show that generative fidelity bounds perceptual gain and that distinct families of edit prompts govern transfer efficiency. We further analyse whether models can decide what to imagine. While they can produce plausible edits, these self-generated visual thoughts lack stable task alignment, revealing that current large multimodal models fall short of true self-reflection. This work exposes a missing mechanism in unified cognition and suggests that imagination is not the end of understanding but its beginning.
匹配关键词: self-consistency
---

[ACADEMIC - ARXIV]
标题: Real-time Speech Restoration using Data Prediction Mean Flows
作者: Sebastian Braun
链接: https://arxiv.org/abs/2605.16251v1
完整摘要: Generative models are capable to address difficult problems with non-unique solutions like bandwidth extension and gap filling, removing highly non-linear artifacts from codecs, clipping and distortion, as opposed to removing linear additive components like noise and reverb. While large offline processing models have shown impressive results, these tasks have not been solved with real-time capable models with low latency and compute. We propose a few-step flow matching model using Data Prediction Mean Flows in combination with suitable novel low-latency architecture to make flow matching models an attractive choice under theses constraints. Compared to state-of-the-art, our proposed mean flow model uses 120x less compute and introduces no algorithmic latency other than the STFT, while achieving similar audio quality.
匹配关键词: process reward
---

[ACADEMIC - ARXIV]
标题: Prospective multi-pathogen disease forecasting using autonomous LLM-guided tree search
作者: Sarah Martinson, Michael P. Brenner, Martyna Plomecka, Brian P. Williams, Nicholas G. Reich, Zahra Shamsi
链接: https://arxiv.org/abs/2605.16238v1
完整摘要: Probabilistic forecasting of infectious diseases is crucial for public health but relies on labor-intensive manual model curation by expert modeling teams. This bespoke development bottlenecks scalability to granular geographic resolutions or emerging pathogens. Here, we present an autonomous system using Large Language Model (LLM)-guided tree search to iteratively generate, evaluate, and optimize executable forecasting software. In a fully prospective, real-time evaluation during the 2025-2026 US respiratory season, the system autonomously discovered methodologically diverse models for influenza, COVID-19, and respiratory syncytial virus (RSV). Aggregating these machine-generated models yielded an ensemble that consistently matched or outperformed the gold-standard, human-curated Centers for Disease Control and Prevention (CDC) hub ensembles out-of-sample. The system successfully navigated data-scarce "cold start" scenarios for RSV. Moreover, controlled retrospective ablations revealed that optimizing log-scale distance metrics prevents reward hacking, while an automated judge-in-the-loop ensures structural fidelity to complex scientific theories. By autonomously translating epidemiological theory into accurate, transparent code, this framework overcomes the modeling labor bottleneck, enabling rapid deployment of expert-level disease forecasting at unprecedented scales.
匹配关键词: process reward
---

[ACADEMIC - ARXIV]
标题: FORGE: Self-Evolving Agent Memory With No Weight Updates via Population Broadcast
作者: Igor Bogdanov, Chung-Horng Lung, Thomas Kunz, Jie Gao, Adrian Taylor, Marzia Zaman
链接: https://arxiv.org/abs/2605.16233v1
完整摘要: Can LLM agents improve decision-making through self-generated memory without gradient updates? We propose FORGE (Failure-Optimized Reflective Graduation and Evolution), a staged, population-based protocol that evolves prompt-injected natural-language memory for hierarchical ReAct agents. FORGE wraps a Reflexion-style inner loop, where a dedicated reflection agent (using the same underlying LLM, no distillation from a stronger model) converts failed trajectories into reusable knowledge artifacts: textual heuristics (Rules), few-shot demonstrations (Examples), or both (Mixed), with an outer loop that propagates the best-performing instance's memory to the population between stages and freezes converged instances via a graduation criterion. We evaluate on CybORG CAGE-2, a stochastic network-defense POMDP at a 30-step horizon against the B-line attacker, where all four tested LLM families (Gemini-2.5-Flash-Lite, Grok-4-Fast, Llama-4-Maverick, Qwen3-235B) exhibit strongly negative, heavy-tailed zero-shot rewards. Compared against both a zero-shot baseline and a Reflexion baseline (isolated single-stream learning), FORGE improves average evaluation return by 1.7-7.7$\times$ over zero-shot and by 29-72% over Reflexion in all 12 model-representation conditions, reducing major-failure rates (below $-100$) to as low as $\sim$1%. We find that (1) population broadcast is critical mechanism, with a no-graduation ablation confirming that broadcast carries the performance gains while graduation primarily saves compute; (2) Examples achieves the strongest returns for three of four models, Rules offers the best cost-reliability profile with $\sim$40% fewer tokens; and (3) weaker baseline models benefit disproportionately, suggesting FORGE may mitigate capability gaps rather than amplify strong models. All evidence is confined to CAGE-2 B-line; cross-family findings are directional evidence.
匹配关键词: process reward
---

[ACADEMIC - ARXIV]
标题: Artificial Aphasias in Lesioned Language Models
作者: Nathan Roll, Jill Kries, Laura Gwilliams, Cory Shain
链接: https://arxiv.org/abs/2605.16222v1
完整摘要: Aphasias, selective language impairments which can arise from brain damage, reveal the functional organization of human language by providing causal links between affected brain regions and specific symptom profiles. Drawing on this literature, we introduce an aphasia-inspired technique to characterize the emergent functional organization of language models (LMs). We ``lesion'' (zero-out) model parameters and measure the effects of this intervention against clinical aphasia symptoms, as diagnosed by the Text Aphasia Battery (TAB). When applied to 112,426 outputs from five 1B-scale LMs, the full range of evaluated symptoms surface, but in distributions largely distinct from those of humans. Our method uncovers broad symptom-profile differences between attention components (query, key, value, output) and feed-forward components (up, gate, down), with weaker evidence for differences among components within the same mechanism. We also find an effect of depth, where lesions in early layers disproportionately cause syntactic and semantic symptoms while late-middle layers yield higher rates of phonological and fluency deficits. Although some LM lesions induce quantitatively more similar profiles to some human aphasia types than others, qualitative differences in symptom patterns between LMs and humans suggest that aphasia syndromes are heavily influenced by the details of learning and processing rather than being a domain-invariant consequence of disrupted language processing.
匹配关键词: process reward
---

[ACADEMIC - ARXIV]
标题: Context, Reasoning, and Hierarchy: A Cost-Performance Study of Compound LLM Agent Design in an Adversarial POMDP
作者: Igor Bogdanov, Chung-Horng Lung, Thomas Kunz, Jie Gao, Adrian Taylor, Marzia Zaman
链接: https://arxiv.org/abs/2605.16205v1
完整摘要: Deploying compound LLM agents in adversarial, partially observable sequential environments requires navigating several design dimensions: (1) what the agent sees, (2) how it reasons, and (3) how tasks are decomposed across components. Yet practitioners lack guidance on which design choices improve performance versus merely increase inference costs. We present a controlled study of compound LLM agent design in CybORG CAGE-2, a cyber defense environment modeled as a Partially Observable Markov Decision Process (POMDP). Reward is non-positive, so all configurations operate in a failure-mitigation mode. Our evaluation spans five model families, six models, and twelve configurations (3,475 episodes) with token-level cost accounting. We vary context representation (raw observations vs. a deterministic state-tracking layer with compressed history), deliberation (self-questioning, self-critique, and self-improvement tools, with optional chain-of-thought prompting), and hierarchical decomposition (monolithic ReAct vs. delegation to specialized sub-agents). We find that: (1) Programmatic state abstraction delivers the largest returns per token spent (RPTS), improving mean return by up to 76% over raw observations. (2) Distributing deliberation tools across a hierarchy degrades performance relative to hierarchy alone for all five model families, reaching up to 3.4$\times$ worse mean return while using 1.8-2.7$\times$ more tokens. We call this destructive pattern a deliberation cascade. (3) Hierarchical decomposition without deliberation achieves the best absolute performance for most models, and context engineering is generally more cost-effective than deliberation. These findings suggest a design principle for structured adversarial POMDPs: invest in programmatic infrastructure and clean task decomposition rather than deeper per-agent reasoning, as these strategies can interfere when combined.
匹配关键词: process reward
---

[ACADEMIC - ARXIV]
标题: Layer Equivalence Is Not a Property of Layers Alone: How You Test Redundancy Changes What You Find
作者: Gabriel Garcia
链接: https://arxiv.org/abs/2605.16234v1
完整摘要: When researchers ask whether two transformer layers are "equivalent" for compression, they often conflate distinct tests. Replacement asks whether one layer's map can substitute for another's in place; interchange asks whether two layers approximately commute when their positions are swapped. Both are output-grounded swap-KL probes, but they need not agree: on pretrained transformers the protocol gap can change which layers look safe to prune by several-fold under the same evaluator, especially when replacement distances are high. We measure both protocols across checkpoints and architectures. On a Pythia training trajectory (410M and 1.4B), the replacement-interchange gap grows from initialization to convergence. Under one matched WikiText-2 contract at 8B scale, Qwen3-8B enters a divergent regime: interchange-guided removal is several-fold safer than replacement-guided at the same layer budgets, while Llama-3.1-8B ties the two protocols for pruning cost even though interchange KL is lower, showing metric gaps need not map one-to-one to removal. Before layer removal or merging, score both swap-KLs on the target checkpoint; the diagnostic requires only unlabeled forward passes.
匹配关键词: pretraining
---

[ACADEMIC - ARXIV]
标题: Multi-Fidelity Flow Matching: Cascaded Refinement of PDE Solutions
作者: Sipeng Chen, Junliang Liu, Hewei Tang, Shibo Li
链接: https://arxiv.org/abs/2605.16118v1
完整摘要: The source distribution in conditional flow matching is a design parameter that can be calibrated to data, not a default isotropic prior. We exploit this in Multi-Fidelity Flow Matching (MFFM), a cascade refinement framework for parametric PDE solutions: the source is calibrated to the empirical low-to-high-fidelity residual scale with local Gaussian-blur correlation, and the velocity network is conditioned on the low-fidelity solution. Conditioning makes the residual refinement problem substantially easier than unconditional field generation, while residual-calibrated source noise improves the flow-matching training geometry. A multi-resolution cascade applies the same construction independently between adjacent fidelities. After level-wise flow-matching pretraining, we fine-tune the composed cascade end-to-end with a deterministic one-step rollout, which makes one velocity evaluation per cascade level the optimized operating point at inference. The result is a learned analog of multigrid refinement that reaches the finest grid in $L$ deterministic network evaluations per query. We validate MFFM on eight benchmarks: two super-resolution problems and six spatiotemporal forecasting tasks from PDEBench, The Well, and the FNO Navier--Stokes dataset.
匹配关键词: pretraining
---

[ACADEMIC - ARXIV]
标题: Multi-level Self-supervised Pretraining on Compositional Hierarchical Graph for Molecular Property Prediction
作者: Xiayu Liu, Zhengyi Lu, Hou-biao Li
链接: https://arxiv.org/abs/2605.16088v1
完整摘要: Self-supervised pretraining on molecular graphs has emerged as a promising approach for molecular property prediction, yet most existing methods operate at a single structural granularity and treat bond information as auxiliary edge attributes rather than as an independent semantic layer. In this work, we propose MolCHG, a multi-level self-supervised pretraining framework built upon a novel Compositional Hierarchical Graph that organizes molecular structure into four types of nodes across three semantic levels. By introducing a bond graph that operates in parallel with the atom graph, our architecture elevates bond-level information to independently evolving node representations, enabling fragment nodes to aggregate atom-level and bond-level semantics on an equal footing. We design three level-specific pretraining objectives: an atom-bond cross-view contrastive task that aligns the atom-view and bond-view representations within each fragment, a fragment-level functional group prediction task to inject domain-relevant chemical knowledge, and graph-level structure prediction tasks to encode global molecular topology. Experiments on nine MoleculeNet benchmarks demonstrate that MolCHG achieves the best performance on seven datasets across both classification and regression tasks, remaining competitive with the strongest baselines on the rest. Ablation studies further confirm that the multi-level supervision signals are complementary and that each component contributes to the overall performance.
匹配关键词: pretraining
---

[ACADEMIC - ARXIV]
标题: ITGPT: Generative Pretraining on Irregular Timeseries
作者: Antoine Honoré, Ming Xiao
链接: https://arxiv.org/abs/2605.16069v1
完整摘要: Timeseries regression models often struggle to leverage large volumes of labeled multimodal data, particularly when the data are irregularly sampled or contain missing values. This is common in domains like healthcare and predictive maintenance, where data are collected from unreliable sources, and labeling requires expert knowledge or costly equipments. Transformer-based large language models have proven effective on structured data such as text through self-supervised learning (SSL) and generative pretraining (GPT) frameworks. However, such models lack the flexibility to efficiently process irregularly sampled multimodal timeseries data. In this paper, we introduce ITGPT, an attention-based architecture designed for handling multimodal, irregularly sampled timeseries by allowing training with both SSL losses and GPT-like objectives. We evaluate its performance on a healthcare task with the TIHM dataset, and a predictive maintenance task with the CompX dataset. Our results demonstrate that ITGPT achieves state-of-the-art performance without requiring resampling, feature fusion or explicit data imputation. Furthermore, when labels are scarce, ITGPT effectively leverages unlabeled data through SSL and GPT training, outperforming the purely supervised approach. This represents an important step towards efficiently using large and unstructured timeseries datasets for practical inference tasks.
匹配关键词: pretraining
---

[ACADEMIC - ARXIV]
标题: Health-Conditioned Vision-Language-Action Models for Malfunction-Aware Robot Control
作者: Hüseyin Arslan, Özgür Erkent
链接: https://arxiv.org/abs/2605.16056v1
完整摘要: Research on Vision Language Action (VLA) models has been increasing rapidly in recent years. Although some of them focus on detecting, preventing, and recovering from task failures, they usually don't deal with adapting to robot's physical failures. In real-life scenarios, most robots face physical degradations in various ways such as joint degradation, actuator failure, or weak gripper. We introduce malfunction-aware (health-conditioned) VLA that takes a health vector as an input that gives information about robots' joints' operation angle and torque capability, and adapts its predictions to complete the tasks with the degraded joints. To achieve this, we inject a Health Projector module to the VLA-Adapter architecture and train it on malfunction robot data we collected on the LIBERO environment [1]. We collect 128 teleoperated episodes on Libero-Spatial tasks. Our results show that, with a very lightweight addition, the model can learn to operate successfully with different configurations of degraded joints which the default pretrained VLA-Adapter's Libero-Spatial-Pro model cannot. The code and dataset will be available soon at https://github.com/h-arslan/health-aware-vla
匹配关键词: pretraining
---

[ACADEMIC - ARXIV]
标题: IVGT: Implicit Visual Geometry Transformer for Neural Scene Representation
作者: Yuqi Wu, Tianyu Hu, Wenzhao Zheng, Yuanhui Huang, Haowen Sun, Jie Zhou, Jiwen Lu
链接: https://arxiv.org/abs/2605.16258v1
完整摘要: Reconstructing coherent 3D geometry and appearance from unposed multi-view images is a fundamental yet challenging problem in computer vision. Most existing visual geometry foundation models predict explicit geometry by regressing pixel-aligned pointmaps, often suffering from redundancy and limited geometric continuity. We propose IVGT, an Implicit Visual Geometry Transformer that implicitly models continuous and coherent geometry from pose-free multi-view images. This formulation learns a continuous neural scene representation in a canonical coordinate system and supports continuous spatial queries at any 3D positions, retrieving local features to predict signed distance (SDF) values and colors using lightweight decoders. It allows direct extraction of continuous and coherent surface geometry, enabling rendering of RGB images, depth maps, and surface normal maps from arbitrary viewpoints. We train IVGT via multi-dataset joint optimization with 2D supervision and 3D geometric regularization. IVGT demonstrates generalization across scenes and achieves strong performance on various tasks, including mesh and point cloud reconstruction, novel view synthesis, depth and surface normal estimation, and camera pose estimation.
匹配关键词: foundation model
---

[ACADEMIC - ARXIV]
标题: DexJoCo: A Benchmark and Toolkit for Task-Oriented Dexterous Manipulation on MuJoCo
作者: Hanwen Wang, Weizhi Zhao, Xiangyu Wang, Siyuan Huang, He Lin, Boyuan Zheng, Rongtao Xu, Gang Wang, Yao Mu, He Wang, Lue Fan, Hongsheng Li, Zhaoxiang Zhang, Tieniu Tan
链接: https://arxiv.org/abs/2605.16257v1
完整摘要: Achieving human-level manipulation requires dexterous robotic hands capable of complex object interactions. Advancing such capabilities further demands standardized benchmarks for systematic evaluation. However, existing dexterous benchmarks lack tasks that reflect the unique manipulation capabilities of dexterous hands over parallel grippers, as well as comprehensive evaluation pipelines. In this paper, we present DexJoCo, a benchmark and toolkit for task-oriented dexterous manipulation, comprising 11 functionally grounded tasks that evaluate tool-use, bimanual coordination, long-horizon execution, and reasoning. We develop a low-cost data collection system and collect 1.1K trajectories across these tasks, with support for domain randomization to assess robustness. We benchmark modern models under diverse settings, including visual and dynamics randomization, multi-task training, and action-head adaptation. Through extensive empirical analysis, we identify several important insights and common limitations of current policies in dexterous manipulation, highlighting key challenges for future research in dexterous hand robot learning. Project page available at: https://dexjoco.github.io
匹配关键词: foundation model
---

[ACADEMIC - ARXIV]
标题: Designing Datacenter Power Delivery Hierarchies for the AI Era
作者: Grant Wilkins, Fiodar Kazhamiaka, Alok Gautam Kumbhare, Chaojie Zhang, Ricardo Bianchini
链接: https://arxiv.org/abs/2605.16255v1
完整摘要: Demand for AI accelerators is rapidly increasing rack power density, with projections approaching 1MW per deployment by 2027. This poses a major challenge for datacenter power delivery designers. As power densities increase, a datacenter designed for a different target density may strand power, i.e., may be unable to use all the power that its delivery hierarchy has provisioned. Designs must remain efficient over long datacenter lifetimes and multiple hardware generations. Power utilization is particularly important as grid power capacity is a scarce resource in the AI era. Designing an efficient power delivery hierarchy for the long run is difficult because rack placement feasibility, workload impact, and cost depend jointly on electrical topology, deployment granularity, placement policy, power oversubscription, and workload mix. Moreover, each of these factors evolve over time, have inter-dependencies across multiple resource dimensions, and generally do not lend themselves to closed-form analysis. To address this challenge, we develop a framework for evaluating datacenter power delivery designs using throughput, power, and cost metrics over realistic arrival, oversubscription, and decommissioning sequences. The framework combines projection models for GPU, compute, and storage deployments with operational factors grounded in production data from Microsoft Azure. Our results show that multi-resource stranding materially changes deployable capacity, effective capital expenditure, and delivered performance, and quantify how rising density from rack- and pod-scale AI systems shapes these outcomes. For AI datacenter design, the relevant planning objective is not installed megawatts, but deployable capacity over time.
匹配关键词: foundation model
---

[ACADEMIC - ARXIV]
标题: Real-time Speech Restoration using Data Prediction Mean Flows
作者: Sebastian Braun
链接: https://arxiv.org/abs/2605.16251v1
完整摘要: Generative models are capable to address difficult problems with non-unique solutions like bandwidth extension and gap filling, removing highly non-linear artifacts from codecs, clipping and distortion, as opposed to removing linear additive components like noise and reverb. While large offline processing models have shown impressive results, these tasks have not been solved with real-time capable models with low latency and compute. We propose a few-step flow matching model using Data Prediction Mean Flows in combination with suitable novel low-latency architecture to make flow matching models an attractive choice under theses constraints. Compared to state-of-the-art, our proposed mean flow model uses 120x less compute and introduces no algorithmic latency other than the STFT, while achieving similar audio quality.
匹配关键词: foundation model
---

[ACADEMIC - ARXIV]
标题: AI-Mediated Communication Can Steer Collective Opinion
作者: Stratis Tsirtsis, Kai Rawal, Chris Russell, Brent Mittelstadt, Sandra Wachter
链接: https://arxiv.org/abs/2605.16245v1
完整摘要: Generative artificial intelligence (AI) is increasingly integrated into the online platforms where humans exchange opinions; large language models (LLMs) now polish users' posts on LinkedIn and provide context for content shared on X. While prior work has shown that AI can express biased opinions and shape individuals' opinions during human-AI interactions, less attention has been paid to its influence on collective opinion formation when mediating human-to-human communication. We address this gap via a combination of empirical and theoretical analyses. We show empirically that LLMs from multiple popular families introduce directional biases when instructed to edit human-written texts on contested topics, for example, nudging texts in favor of gun control and against atheism. Building on this observation, we introduce a mathematical model of opinion dynamics in which an AI system sits between users on a social network, transforming the opinions they express and perceive. By analytically characterizing the equilibrium of this model and performing simulations on real social network data, we show that biases introduced by AI in human-to-human communication can be amplified through the network and shift collective opinion in their direction. In light of these findings, we investigate whether such biases are controllable by online platforms. We audit the "Explain this post" feature on X and find evidence of pro-life bias in Grok's outputs on abortion-related content, which we trace back to specific design choices. We conclude with a discussion of the broader implications of our findings in relation to ongoing legislative efforts in the European Union.
匹配关键词: foundation model
---

[ACADEMIC - ARXIV]
标题: Designing Datacenter Power Delivery Hierarchies for the AI Era
作者: Grant Wilkins, Fiodar Kazhamiaka, Alok Gautam Kumbhare, Chaojie Zhang, Ricardo Bianchini
链接: https://arxiv.org/abs/2605.16255v1
完整摘要: Demand for AI accelerators is rapidly increasing rack power density, with projections approaching 1MW per deployment by 2027. This poses a major challenge for datacenter power delivery designers. As power densities increase, a datacenter designed for a different target density may strand power, i.e., may be unable to use all the power that its delivery hierarchy has provisioned. Designs must remain efficient over long datacenter lifetimes and multiple hardware generations. Power utilization is particularly important as grid power capacity is a scarce resource in the AI era. Designing an efficient power delivery hierarchy for the long run is difficult because rack placement feasibility, workload impact, and cost depend jointly on electrical topology, deployment granularity, placement policy, power oversubscription, and workload mix. Moreover, each of these factors evolve over time, have inter-dependencies across multiple resource dimensions, and generally do not lend themselves to closed-form analysis. To address this challenge, we develop a framework for evaluating datacenter power delivery designs using throughput, power, and cost metrics over realistic arrival, oversubscription, and decommissioning sequences. The framework combines projection models for GPU, compute, and storage deployments with operational factors grounded in production data from Microsoft Azure. Our results show that multi-resource stranding materially changes deployable capacity, effective capital expenditure, and delivered performance, and quantify how rising density from rack- and pod-scale AI systems shapes these outcomes. For AI datacenter design, the relevant planning objective is not installed megawatts, but deployable capacity over time.
匹配关键词: scaling law
---

[ACADEMIC - ARXIV]
标题: Prospective multi-pathogen disease forecasting using autonomous LLM-guided tree search
作者: Sarah Martinson, Michael P. Brenner, Martyna Plomecka, Brian P. Williams, Nicholas G. Reich, Zahra Shamsi
链接: https://arxiv.org/abs/2605.16238v1
完整摘要: Probabilistic forecasting of infectious diseases is crucial for public health but relies on labor-intensive manual model curation by expert modeling teams. This bespoke development bottlenecks scalability to granular geographic resolutions or emerging pathogens. Here, we present an autonomous system using Large Language Model (LLM)-guided tree search to iteratively generate, evaluate, and optimize executable forecasting software. In a fully prospective, real-time evaluation during the 2025-2026 US respiratory season, the system autonomously discovered methodologically diverse models for influenza, COVID-19, and respiratory syncytial virus (RSV). Aggregating these machine-generated models yielded an ensemble that consistently matched or outperformed the gold-standard, human-curated Centers for Disease Control and Prevention (CDC) hub ensembles out-of-sample. The system successfully navigated data-scarce "cold start" scenarios for RSV. Moreover, controlled retrospective ablations revealed that optimizing log-scale distance metrics prevents reward hacking, while an automated judge-in-the-loop ensures structural fidelity to complex scientific theories. By autonomously translating epidemiological theory into accurate, transparent code, this framework overcomes the modeling labor bottleneck, enabling rapid deployment of expert-level disease forecasting at unprecedented scales.
匹配关键词: scaling law
---

[ACADEMIC - ARXIV]
标题: Layer Equivalence Is Not a Property of Layers Alone: How You Test Redundancy Changes What You Find
作者: Gabriel Garcia
链接: https://arxiv.org/abs/2605.16234v1
完整摘要: When researchers ask whether two transformer layers are "equivalent" for compression, they often conflate distinct tests. Replacement asks whether one layer's map can substitute for another's in place; interchange asks whether two layers approximately commute when their positions are swapped. Both are output-grounded swap-KL probes, but they need not agree: on pretrained transformers the protocol gap can change which layers look safe to prune by several-fold under the same evaluator, especially when replacement distances are high. We measure both protocols across checkpoints and architectures. On a Pythia training trajectory (410M and 1.4B), the replacement-interchange gap grows from initialization to convergence. Under one matched WikiText-2 contract at 8B scale, Qwen3-8B enters a divergent regime: interchange-guided removal is several-fold safer than replacement-guided at the same layer budgets, while Llama-3.1-8B ties the two protocols for pruning cost even though interchange KL is lower, showing metric gaps need not map one-to-one to removal. Before layer removal or merging, score both swap-KLs on the target checkpoint; the diagnostic requires only unlabeled forward passes.
匹配关键词: scaling law
---

[ACADEMIC - ARXIV]
标题: Artificial Aphasias in Lesioned Language Models
作者: Nathan Roll, Jill Kries, Laura Gwilliams, Cory Shain
链接: https://arxiv.org/abs/2605.16222v1
完整摘要: Aphasias, selective language impairments which can arise from brain damage, reveal the functional organization of human language by providing causal links between affected brain regions and specific symptom profiles. Drawing on this literature, we introduce an aphasia-inspired technique to characterize the emergent functional organization of language models (LMs). We ``lesion'' (zero-out) model parameters and measure the effects of this intervention against clinical aphasia symptoms, as diagnosed by the Text Aphasia Battery (TAB). When applied to 112,426 outputs from five 1B-scale LMs, the full range of evaluated symptoms surface, but in distributions largely distinct from those of humans. Our method uncovers broad symptom-profile differences between attention components (query, key, value, output) and feed-forward components (up, gate, down), with weaker evidence for differences among components within the same mechanism. We also find an effect of depth, where lesions in early layers disproportionately cause syntactic and semantic symptoms while late-middle layers yield higher rates of phonological and fluency deficits. Although some LM lesions induce quantitatively more similar profiles to some human aphasia types than others, qualitative differences in symptom patterns between LMs and humans suggest that aphasia syndromes are heavily influenced by the details of learning and processing rather than being a domain-invariant consequence of disrupted language processing.
匹配关键词: scaling law
---

[ACADEMIC - ARXIV]
标题: The Privacy Price of Tail-Risk Learning: Effective Tail Sample Size in Differentially Private CVaR Optimization
作者: El Mustapha Mansouri
链接: https://arxiv.org/abs/2605.16219v1
完整摘要: Differential privacy changes the effective sample size governing CVaR learning. For tail mass $τ$, the privacy-relevant sample size is not $n$, but $nτ$; equivalently, the effective private tail sample size is $εnτ$. Private CVaR excess risk decomposes into ordinary tail-risk statistical error and a privacy price. This decomposition is complete for scalar estimation and finite classes: scalar estimation has rate $Θ(B \min\{1,(nτ)^{-1/2}+(εnτ)^{-1}\})$, and finite classes of size $M$ have rate $Θ(B \min\{1,\sqrt{\log(2M)/(nτ)}+\log(2M)/(εnτ)\})$. These complete rates hold under pure DP, and their lower bounds extend to approximate DP in the stated small-$δ$ regimes. For convex Lipschitz learning, modular upper and lower reductions show that the CVaR-specific privacy term necessarily scales as $1/(εnτ)$, with dimension dependence inherited from private stochastic convex optimization. Together, these results identify ordinary private learning on $Θ(nτ)$ informative tail records as the canonical hard subproblem inside private CVaR learning.
匹配关键词: scaling law
---

[ACADEMIC - ARXIV]
标题: IVGT: Implicit Visual Geometry Transformer for Neural Scene Representation
作者: Yuqi Wu, Tianyu Hu, Wenzhao Zheng, Yuanhui Huang, Haowen Sun, Jie Zhou, Jiwen Lu
链接: https://arxiv.org/abs/2605.16258v1
完整摘要: Reconstructing coherent 3D geometry and appearance from unposed multi-view images is a fundamental yet challenging problem in computer vision. Most existing visual geometry foundation models predict explicit geometry by regressing pixel-aligned pointmaps, often suffering from redundancy and limited geometric continuity. We propose IVGT, an Implicit Visual Geometry Transformer that implicitly models continuous and coherent geometry from pose-free multi-view images. This formulation learns a continuous neural scene representation in a canonical coordinate system and supports continuous spatial queries at any 3D positions, retrieving local features to predict signed distance (SDF) values and colors using lightweight decoders. It allows direct extraction of continuous and coherent surface geometry, enabling rendering of RGB images, depth maps, and surface normal maps from arbitrary viewpoints. We train IVGT via multi-dataset joint optimization with 2D supervision and 3D geometric regularization. IVGT demonstrates generalization across scenes and achieves strong performance on various tasks, including mesh and point cloud reconstruction, novel view synthesis, depth and surface normal estimation, and camera pose estimation.
匹配关键词: language model
---

[ACADEMIC - ARXIV]
标题: DexJoCo: A Benchmark and Toolkit for Task-Oriented Dexterous Manipulation on MuJoCo
作者: Hanwen Wang, Weizhi Zhao, Xiangyu Wang, Siyuan Huang, He Lin, Boyuan Zheng, Rongtao Xu, Gang Wang, Yao Mu, He Wang, Lue Fan, Hongsheng Li, Zhaoxiang Zhang, Tieniu Tan
链接: https://arxiv.org/abs/2605.16257v1
完整摘要: Achieving human-level manipulation requires dexterous robotic hands capable of complex object interactions. Advancing such capabilities further demands standardized benchmarks for systematic evaluation. However, existing dexterous benchmarks lack tasks that reflect the unique manipulation capabilities of dexterous hands over parallel grippers, as well as comprehensive evaluation pipelines. In this paper, we present DexJoCo, a benchmark and toolkit for task-oriented dexterous manipulation, comprising 11 functionally grounded tasks that evaluate tool-use, bimanual coordination, long-horizon execution, and reasoning. We develop a low-cost data collection system and collect 1.1K trajectories across these tasks, with support for domain randomization to assess robustness. We benchmark modern models under diverse settings, including visual and dynamics randomization, multi-task training, and action-head adaptation. Through extensive empirical analysis, we identify several important insights and common limitations of current policies in dexterous manipulation, highlighting key challenges for future research in dexterous hand robot learning. Project page available at: https://dexjoco.github.io
匹配关键词: language model
---

[ACADEMIC - ARXIV]
标题: Designing Datacenter Power Delivery Hierarchies for the AI Era
作者: Grant Wilkins, Fiodar Kazhamiaka, Alok Gautam Kumbhare, Chaojie Zhang, Ricardo Bianchini
链接: https://arxiv.org/abs/2605.16255v1
完整摘要: Demand for AI accelerators is rapidly increasing rack power density, with projections approaching 1MW per deployment by 2027. This poses a major challenge for datacenter power delivery designers. As power densities increase, a datacenter designed for a different target density may strand power, i.e., may be unable to use all the power that its delivery hierarchy has provisioned. Designs must remain efficient over long datacenter lifetimes and multiple hardware generations. Power utilization is particularly important as grid power capacity is a scarce resource in the AI era. Designing an efficient power delivery hierarchy for the long run is difficult because rack placement feasibility, workload impact, and cost depend jointly on electrical topology, deployment granularity, placement policy, power oversubscription, and workload mix. Moreover, each of these factors evolve over time, have inter-dependencies across multiple resource dimensions, and generally do not lend themselves to closed-form analysis. To address this challenge, we develop a framework for evaluating datacenter power delivery designs using throughput, power, and cost metrics over realistic arrival, oversubscription, and decommissioning sequences. The framework combines projection models for GPU, compute, and storage deployments with operational factors grounded in production data from Microsoft Azure. Our results show that multi-resource stranding materially changes deployable capacity, effective capital expenditure, and delivered performance, and quantify how rising density from rack- and pod-scale AI systems shapes these outcomes. For AI datacenter design, the relevant planning objective is not installed megawatts, but deployable capacity over time.
匹配关键词: language model
---

[ACADEMIC - ARXIV]
标题: Real-time Speech Restoration using Data Prediction Mean Flows
作者: Sebastian Braun
链接: https://arxiv.org/abs/2605.16251v1
完整摘要: Generative models are capable to address difficult problems with non-unique solutions like bandwidth extension and gap filling, removing highly non-linear artifacts from codecs, clipping and distortion, as opposed to removing linear additive components like noise and reverb. While large offline processing models have shown impressive results, these tasks have not been solved with real-time capable models with low latency and compute. We propose a few-step flow matching model using Data Prediction Mean Flows in combination with suitable novel low-latency architecture to make flow matching models an attractive choice under theses constraints. Compared to state-of-the-art, our proposed mean flow model uses 120x less compute and introduces no algorithmic latency other than the STFT, while achieving similar audio quality.
匹配关键词: language model
---

[ACADEMIC - ARXIV]
标题: A Generative AI Framework for Intelligent Utility Billing CO 2 Analytics and Sustainable Resource Optimisation
作者: Pavan Manjunath, Thomas Pruefer
链接: https://arxiv.org/abs/2605.16250v1
完整摘要: Distribution utilities are now expected to deliver bills that customers can actually read attach a defensible carbon number to every kWh sold and schedule load against grid stress and emissions constraints We propose an end-to-end framework that unifies four production-grade capabilities under one architectural roof a generative-AI agent that drafts each customers natural-language billing statement from structured numeric inputs under a constrained decoding policy a transformer-based forecaster that supplies the day-ahead consumption estimate with calibrated quantile bands
匹配关键词: language model
---

[ACADEMIC - ARXIV]
标题: Prospective multi-pathogen disease forecasting using autonomous LLM-guided tree search
作者: Sarah Martinson, Michael P. Brenner, Martyna Plomecka, Brian P. Williams, Nicholas G. Reich, Zahra Shamsi
链接: https://arxiv.org/abs/2605.16238v1
完整摘要: Probabilistic forecasting of infectious diseases is crucial for public health but relies on labor-intensive manual model curation by expert modeling teams. This bespoke development bottlenecks scalability to granular geographic resolutions or emerging pathogens. Here, we present an autonomous system using Large Language Model (LLM)-guided tree search to iteratively generate, evaluate, and optimize executable forecasting software. In a fully prospective, real-time evaluation during the 2025-2026 US respiratory season, the system autonomously discovered methodologically diverse models for influenza, COVID-19, and respiratory syncytial virus (RSV). Aggregating these machine-generated models yielded an ensemble that consistently matched or outperformed the gold-standard, human-curated Centers for Disease Control and Prevention (CDC) hub ensembles out-of-sample. The system successfully navigated data-scarce "cold start" scenarios for RSV. Moreover, controlled retrospective ablations revealed that optimizing log-scale distance metrics prevents reward hacking, while an automated judge-in-the-loop ensures structural fidelity to complex scientific theories. By autonomously translating epidemiological theory into accurate, transparent code, this framework overcomes the modeling labor bottleneck, enabling rapid deployment of expert-level disease forecasting at unprecedented scales.
匹配关键词: mixture of experts
---

[ACADEMIC - ARXIV]
标题: Fully Open Meditron: An Auditable Pipeline for Clinical LLMs
作者: Xavier Theimer-Lienhard, Mushtaha El-Amin, Fay Elhassan, Sahaj Vaidya, Victor Cartier-Negadi, David Sasu, Lars Klein, Mary-Anne Hartley
链接: https://arxiv.org/abs/2605.16215v1
完整摘要: Clinical decision support systems (CDSS) require scrutable, auditable pipelines that enable rigorous, reproducible validation. Yet current LLM-based CDSS remain largely opaque. Most "open" models are open-weight only, releasing parameters while withholding the data provenance, curation procedures, and generation pipelines that determine model behavior. Fully Open (FO) models, which expose the complete training stack end-to-end, do not currently exist in medicine. We introduce Fully Open Meditron, the first fully open pipeline for building LLM-CDSS, comprising a clinician-audited training corpus, a reproducible data construction and training framework, and a use-aligned evaluation protocol. The corpus unifies eight public medical QA datasets into a normalized conversational format and expands coverage with three clinician-vetted synthetic extensions: exam-style QA, guideline-grounded QA derived from 46,469 clinical practice guidelines, and clinical vignettes. The pipeline enforces system-wide decontamination, gold-label resampling of teacher generations, and end-to-end validation by a four-physician panel. We evaluate using an LLM-as-a-judge protocol over expert-written clinical vignettes, calibrated against 204 human raters. We apply the recipe to five FO base models (Apertus-70B/8B-Instruct, OLMo-2-32B-SFT, EuroLLM-22B/9B-Instruct). All MeditronFO variants are preferred over their bases. Apertus-70B-MeditronFO improves +6.6 points over its base (47.2% to 53.8%) on aggregate medical benchmarks, establishing a new FO SoTA. Gemma-3-27B-MeditronFO is preferred over MedGemma in 58.6% of LLM-as-a-judge comparisons and outperforms it on HealthBench (58% vs 55.9%). These results show that fully open pipelines can achieve state-of-the-art domain-specific performance without sacrificing auditability or reproducibility.
匹配关键词: mixture of experts
---

[ACADEMIC - ARXIV]
标题: BAPR: Bayesian amnesic piecewise-robust reinforcement learning for non-stationary continuous control
作者: Yifan Zhang, Liang Zheng
链接: https://arxiv.org/abs/2605.16170v1
完整摘要: Real-world control systems frequently operate under \emph{piecewise stationary} conditions, where dynamics remain stable for extended periods before undergoing abrupt regime changes. Standard robust RL methods face a fundamental dilemma: a globally conservative policy wastes performance during stable periods, while a locally adaptive policy risks catastrophic failure when the regime changes undetected. We propose \textbf{BAPR} (Bayesian Amnesic Piecewise-Robust SAC), which unifies Bayesian Online Change Detection (BOCD) with robust ensemble RL. The BAPR operator -- a convex combination of mode-conditional Bellman operators weighted by a frozen belief distribution -- is a $γ$-contraction. A complementary counterexample, machine-verified in Lean~4, establishes a \emph{sharp boundary}: when beliefs depend on the Q-function, the contraction factor becomes $γ+ λΔ$ (where $Δ$ is the mode reward gap), and contraction fails exactly when $γ+ λΔ\geq 1$. We derive a \emph{component-wise} formal error budget for the abstract operator -- every component machine-verified -- bounding post-switch recovery; the budget applies to the abstract mode-mixture operator and inherits to the implemented shared-critic algorithm only through the frozen-parameter design intuition. All results are formally verified with no \texttt{sorry} (1,145 lines across 3 Lean~4 files, 22 machine-verified theorems). BOCD drives an adaptive conservatism mechanism: the policy becomes maximally conservative after detected change-points and smoothly relaxes as confidence grows, with detection delay $O(\log(1/δ))$. A context-conditioning module trained via RMDM loss provides mode-aware representations from simulator-provided mode IDs at training time and requires no mode labels at deployment.
匹配关键词: mixture of experts
---

[ACADEMIC - ARXIV]
标题: MIND: Decoupling Model-Induced Label Noise via Latent Manifold Disentanglement
作者: Dayong Ren
链接: https://arxiv.org/abs/2605.16081v1
完整摘要: The paradigm of learning from automatic annotations driven by pre-trained experts and Foundation Models dominates data-hungry applications. However, it introduces a critical challenge: model-induced label noise. Unlike stochastic noise in classical robust learning, this noise stems from annotator inductive biases, manifesting as systematic errors tightly coupled with local feature manifolds. Existing methods relying on global transition matrices underfit these structural patterns, while learning instance-specific matrices remains mathematically intractable. We propose Model-Induced Noise Decoupling (MIND), a theoretically grounded framework addressing this dilemma. We demonstrate that the high-dimensional noise manifold can be decoupled into tractable, subspace-dependent components via Latent Manifold Disentanglement. Specifically, our Latent Decoupling Estimator (LDE) dynamically projects samples into latent structural clusters with consistent error modes, facilitating noise identifiability without ground-truth anchor points. To rigorously evaluate robustness, we adopt a hierarchical protocol: moving from controlled noise on CIFAR-100 to a structural stress test on large-scale real-world 3D datasets (S3DIS, ScanNet), where error patterns explicitly couple with geometric manifolds. Empirically, MIND significantly outperforms state-of-the-art methods on these complex benchmarks and effectively corrects zero-shot hallucinations from Vision-Language Models (e.g., OpenSeg), highlighting its potential as a robust distillation framework for Foundation Models.
匹配关键词: mixture of experts
---

[ACADEMIC - ARXIV]
标题: ITGPT: Generative Pretraining on Irregular Timeseries
作者: Antoine Honoré, Ming Xiao
链接: https://arxiv.org/abs/2605.16069v1
完整摘要: Timeseries regression models often struggle to leverage large volumes of labeled multimodal data, particularly when the data are irregularly sampled or contain missing values. This is common in domains like healthcare and predictive maintenance, where data are collected from unreliable sources, and labeling requires expert knowledge or costly equipments. Transformer-based large language models have proven effective on structured data such as text through self-supervised learning (SSL) and generative pretraining (GPT) frameworks. However, such models lack the flexibility to efficiently process irregularly sampled multimodal timeseries data. In this paper, we introduce ITGPT, an attention-based architecture designed for handling multimodal, irregularly sampled timeseries by allowing training with both SSL losses and GPT-like objectives. We evaluate its performance on a healthcare task with the TIHM dataset, and a predictive maintenance task with the CompX dataset. Our results demonstrate that ITGPT achieves state-of-the-art performance without requiring resampling, feature fusion or explicit data imputation. Furthermore, when labels are scarce, ITGPT effectively leverages unlabeled data through SSL and GPT training, outperforming the purely supervised approach. This represents an important step towards efficiently using large and unstructured timeseries datasets for practical inference tasks.
匹配关键词: mixture of experts
---

[ACADEMIC - ARXIV]
标题: IVGT: Implicit Visual Geometry Transformer for Neural Scene Representation
作者: Yuqi Wu, Tianyu Hu, Wenzhao Zheng, Yuanhui Huang, Haowen Sun, Jie Zhou, Jiwen Lu
链接: https://arxiv.org/abs/2605.16258v1
完整摘要: Reconstructing coherent 3D geometry and appearance from unposed multi-view images is a fundamental yet challenging problem in computer vision. Most existing visual geometry foundation models predict explicit geometry by regressing pixel-aligned pointmaps, often suffering from redundancy and limited geometric continuity. We propose IVGT, an Implicit Visual Geometry Transformer that implicitly models continuous and coherent geometry from pose-free multi-view images. This formulation learns a continuous neural scene representation in a canonical coordinate system and supports continuous spatial queries at any 3D positions, retrieving local features to predict signed distance (SDF) values and colors using lightweight decoders. It allows direct extraction of continuous and coherent surface geometry, enabling rendering of RGB images, depth maps, and surface normal maps from arbitrary viewpoints. We train IVGT via multi-dataset joint optimization with 2D supervision and 3D geometric regularization. IVGT demonstrates generalization across scenes and achieves strong performance on various tasks, including mesh and point cloud reconstruction, novel view synthesis, depth and surface normal estimation, and camera pose estimation.
匹配关键词: transformer architecture
---

[ACADEMIC - ARXIV]
标题: Real-time Speech Restoration using Data Prediction Mean Flows
作者: Sebastian Braun
链接: https://arxiv.org/abs/2605.16251v1
完整摘要: Generative models are capable to address difficult problems with non-unique solutions like bandwidth extension and gap filling, removing highly non-linear artifacts from codecs, clipping and distortion, as opposed to removing linear additive components like noise and reverb. While large offline processing models have shown impressive results, these tasks have not been solved with real-time capable models with low latency and compute. We propose a few-step flow matching model using Data Prediction Mean Flows in combination with suitable novel low-latency architecture to make flow matching models an attractive choice under theses constraints. Compared to state-of-the-art, our proposed mean flow model uses 120x less compute and introduces no algorithmic latency other than the STFT, while achieving similar audio quality.
匹配关键词: transformer architecture
---

[ACADEMIC - ARXIV]
标题: A Generative AI Framework for Intelligent Utility Billing CO 2 Analytics and Sustainable Resource Optimisation
作者: Pavan Manjunath, Thomas Pruefer
链接: https://arxiv.org/abs/2605.16250v1
完整摘要: Distribution utilities are now expected to deliver bills that customers can actually read attach a defensible carbon number to every kWh sold and schedule load against grid stress and emissions constraints We propose an end-to-end framework that unifies four production-grade capabilities under one architectural roof a generative-AI agent that drafts each customers natural-language billing statement from structured numeric inputs under a constrained decoding policy a transformer-based forecaster that supplies the day-ahead consumption estimate with calibrated quantile bands
匹配关键词: transformer architecture
---

[ACADEMIC - ARXIV]
标题: AI-Mediated Communication Can Steer Collective Opinion
作者: Stratis Tsirtsis, Kai Rawal, Chris Russell, Brent Mittelstadt, Sandra Wachter
链接: https://arxiv.org/abs/2605.16245v1
完整摘要: Generative artificial intelligence (AI) is increasingly integrated into the online platforms where humans exchange opinions; large language models (LLMs) now polish users' posts on LinkedIn and provide context for content shared on X. While prior work has shown that AI can express biased opinions and shape individuals' opinions during human-AI interactions, less attention has been paid to its influence on collective opinion formation when mediating human-to-human communication. We address this gap via a combination of empirical and theoretical analyses. We show empirically that LLMs from multiple popular families introduce directional biases when instructed to edit human-written texts on contested topics, for example, nudging texts in favor of gun control and against atheism. Building on this observation, we introduce a mathematical model of opinion dynamics in which an AI system sits between users on a social network, transforming the opinions they express and perceive. By analytically characterizing the equilibrium of this model and performing simulations on real social network data, we show that biases introduced by AI in human-to-human communication can be amplified through the network and shift collective opinion in their direction. In light of these findings, we investigate whether such biases are controllable by online platforms. We audit the "Explain this post" feature on X and find evidence of pro-life bias in Grok's outputs on abortion-related content, which we trace back to specific design choices. We conclude with a discussion of the broader implications of our findings in relation to ongoing legislative efforts in the European Union.
匹配关键词: transformer architecture
---

[ACADEMIC - ARXIV]
标题: Dynamics-Level Watermarking of Flow Matching Models with Random Codes
作者: Shuchan Wang
链接: https://arxiv.org/abs/2605.16239v1
完整摘要: We introduce a dynamics-level approach to watermarking generative models. Rather than embedding signals into model weights or outputs, we embed the watermark directly into the learned continuous dynamics -- the velocity field of a flow matching model. We formulate this as random coding over a continuous channel: a key-dependent perturbation is added during training, and the message is recovered at detection time from black-box queries. The perturbation is designed to leave the generated distribution unchanged. Experiments on MNIST and CIFAR-10 across different architectures confirm reliable message recovery, preserved generation quality, and chance-level decoding accuracy without the secret key.
匹配关键词: transformer architecture
---

[ACADEMIC - ARXIV]
标题: MAgSeg: Segmentation of Agricultural Landscapes in High-Resolution Satellite Imagery using Multimodal Large Language Models
作者: Piyush Tiwary, Utkarsh Ahuja, Depanshu Sani, Aishwarya Jayagopal, Sagar Gubbi, Subhashini Venugopalan, Alok Talekar, Vaibhav Rajan
链接: https://arxiv.org/abs/2605.16179v1
完整摘要: Agricultural landscape segmentation in the Global South is challenging as it is characterized by fragmented plots, high intra-class variance, and a scarcity of labeled training data. Recent advances in segmentation have been made by Multimodal Large Language Models (MLLMs). However, current approaches encounter critical context length bottlenecks and a domain alignment gap in understanding satellite features. We address these limitations through MAgSeg, a novel, decoder-free MLLM segmentation approach. MAgSeg is an architecturally efficient approach that enables standard MLLMs to perform segmentation of complex smallholder agricultural landscapes from high-resolution satellite imagery, without requiring auxiliary vision decoders. We introduce a novel instruction tuning data format designed to enable scalable fine-tuning and post-training on high resolution satellite imagery, which enables MAgSeg to learn from the global context of the image while generating text tokens for only a patch within the image. Extensive evaluations on datasets spanning three countries in the Global South demonstrate that MAgSeg significantly outperforms state-of-the-art MLLM baselines, offering a scalable solution to map smallholder agricultural environments.
匹配关键词: post-training
---

[ACADEMIC - ARXIV]
标题: BAPR: Bayesian amnesic piecewise-robust reinforcement learning for non-stationary continuous control
作者: Yifan Zhang, Liang Zheng
链接: https://arxiv.org/abs/2605.16170v1
完整摘要: Real-world control systems frequently operate under \emph{piecewise stationary} conditions, where dynamics remain stable for extended periods before undergoing abrupt regime changes. Standard robust RL methods face a fundamental dilemma: a globally conservative policy wastes performance during stable periods, while a locally adaptive policy risks catastrophic failure when the regime changes undetected. We propose \textbf{BAPR} (Bayesian Amnesic Piecewise-Robust SAC), which unifies Bayesian Online Change Detection (BOCD) with robust ensemble RL. The BAPR operator -- a convex combination of mode-conditional Bellman operators weighted by a frozen belief distribution -- is a $γ$-contraction. A complementary counterexample, machine-verified in Lean~4, establishes a \emph{sharp boundary}: when beliefs depend on the Q-function, the contraction factor becomes $γ+ λΔ$ (where $Δ$ is the mode reward gap), and contraction fails exactly when $γ+ λΔ\geq 1$. We derive a \emph{component-wise} formal error budget for the abstract operator -- every component machine-verified -- bounding post-switch recovery; the budget applies to the abstract mode-mixture operator and inherits to the implemented shared-critic algorithm only through the frozen-parameter design intuition. All results are formally verified with no \texttt{sorry} (1,145 lines across 3 Lean~4 files, 22 machine-verified theorems). BOCD drives an adaptive conservatism mechanism: the policy becomes maximally conservative after detected change-points and smoothly relaxes as confidence grows, with detection delay $O(\log(1/δ))$. A context-conditioning module trained via RMDM loss provides mode-aware representations from simulator-provided mode IDs at training time and requires no mode labels at deployment.
匹配关键词: post-training
---

[ACADEMIC - ARXIV]
标题: Learn Where Outcomes Diverge: Efficient VLA RL via Probabilistic Chunk Masking
作者: Vaidehi Bagaria, Nikshep Grampurohit, Pulkit Verma
链接: https://arxiv.org/abs/2605.16154v1
完整摘要: Reinforcement learning (RL) allows vision-language-action (VLA) policies to generalize beyond their training distribution by optimizing directly for task success, but post-training is computationally expensive. A natural response has been to speed rollout collection through faster simulators and world models. In GRPO-based VLA RL, we find that the dominant cost lies elsewhere: gradient computation accounts for approximately 78% of wall-clock time per step in our runs, while rollout collection accounts for only 21%. Gradient cost dominates because much of this computation is spent on phases that contribute little to learning. GRPO's learning signal is driven by advantage variance: only phases where successful and failed rollouts diverge produce learning signal. However, GRPO assigns the same advantage to every chunk in a rollout. As a result, actor-update compute is spent uniformly across the trajectory, including phases the policy already handles after pre-training and supervised fine-tuning. This paper presents Probabilistic Chunk Masking (PCM), a drop-in modification to GRPO that allocates gradient computation to a small, probabilistically selected subset of chunks per trajectory. PCM scores semantic phases using success-failure action variance, a rollout-derived proxy for per-phase gradient variance, and samples a fixed chunk budget with online-updated phase-level keep probabilities. We formalize per-phase gradient variance as the quantity determines where gradient computation is useful and show that success-failure action variance provides a measurable proxy for it. PCM requires no reward model or learned critic. On three LIBERO benchmarks, PCM matches the final success rate of standard GRPO while achieving 2.38 times wall-clock speedup, 4.8 times faster gradient updates, and 60% lower peak activation memory, while backpropagating through fewer than 20% of trajectory chunks.
匹配关键词: post-training
---

[ACADEMIC - ARXIV]
标题: Not All Tasks Quantize Equally: Fisher-Guided Quantization for Visual Geometry Transformer
作者: Yipu Zhang, Jintao Cheng, Weilun Feng, Jiehao Luo, Chuanguang Yang, Zhulin An, Yongjun Xu, Wei Zhang
链接: https://arxiv.org/abs/2605.15828v1
完整摘要: Feed-forward 3D reconstruction models, represented by Visual Geometry Grounded Transformer (VGGT), jointly predict multiple visual geometry tasks such as depth estimation, camera pose prediction, and point cloud reconstruction in a single forward pass. They have been widely adopted in 3D vision applications, but their billion-scale parameters bring substantial memory and computation overhead, posing challenges for on-device deployment. Post-Training Quantization (PTQ) is an effective technique to reduce this overhead. Existing PTQ methods for feed-forward 3D models mainly focus on handling heavy-tailed activation distributions and constructing diverse calibration datasets. However, we observe that feed-forward 3D models predict multiple geometric attributes through a shared backbone, where different transformer blocks and hidden channels contribute distinctly to each task, resulting in substantially different sensitivities to quantization errors across tasks, blocks, and channels. Consequently, treating all tasks equally over-emphasizes insensitive tasks and causes significant accuracy loss on the sensitive ones. To address this issue, we propose Fisher-Guided Quantization (FGQ) for feed-forward 3D reconstruction models. Specifically, FGQ uses the diagonal Fisher information matrix to quantify the different sensitivities across tasks, blocks, and channels, and incorporates these sensitivities into the Learnable Affine Transformation during calibration to better preserve the channels and blocks most critical to each task. Extensive experiments across camera pose estimation, point map reconstruction, and depth estimation show that FGQ consistently outperforms state-of-the-art quantization baselines on VGGT, achieving up to 39% relative improvement under the 4-bit quantization.
匹配关键词: post-training
---

[ACADEMIC - ARXIV]
标题: IO-SVD: Input-Output Whitened SVD for Adaptive-Rank LLM Compression
作者: Ali Abbasi, Chayne Thrash, Haoran Qin, Hamed Pirsiavash, Soheil Kolouri
链接: https://arxiv.org/abs/2605.15626v1
完整摘要: Large language models deliver strong performance across language and reasoning tasks, but their storage and compute costs remain major barriers to deployment in resource-constrained and latency-sensitive settings. SVD-based post-training compression offers a hardware-agnostic way to reduce model size and improve inference efficiency through low-rank factorization. However, existing methods often rely on input-only whitening spaces, homogeneous rank allocation, or loss-agnostic allocation heuristics, limiting their ability to preserve model quality under aggressive compression. We propose Input-Output Whitened SVD (IO-SVD), a post-training compression method that forms a KL-aware double-sided whitening space for model weights. Using a second-order expansion of the KL loss over the top-K token probabilities, IO-SVD constructs an output-side metric that captures predictive sensitivity, while input whitening captures activation statistics. We further introduce an efficient heterogeneous rank-allocation strategy that scores whitened singular components using first-order calibration loss estimates and prunes the least sensitive components under a global budget. Inspired by prior work that combines SVD truncation with quantization, we improve hybrid SVD-quantization compression through loss-aware remapping, which selects low-rank factor rows for 8-bit quantization based on the predicted loss change incurred by quantizing them. Extensive experiments across diverse LLM and VLM families, and inference-time analysis shows that IO-SVD compresses LLMs with minimal performance degradation while delivering practical inference speedups. Code is available at https://github.com/mint-vu/IO-SVD.git
匹配关键词: post-training
---

[ACADEMIC - ARXIV]
标题: MAgSeg: Segmentation of Agricultural Landscapes in High-Resolution Satellite Imagery using Multimodal Large Language Models
作者: Piyush Tiwary, Utkarsh Ahuja, Depanshu Sani, Aishwarya Jayagopal, Sagar Gubbi, Subhashini Venugopalan, Alok Talekar, Vaibhav Rajan
链接: https://arxiv.org/abs/2605.16179v1
完整摘要: Agricultural landscape segmentation in the Global South is challenging as it is characterized by fragmented plots, high intra-class variance, and a scarcity of labeled training data. Recent advances in segmentation have been made by Multimodal Large Language Models (MLLMs). However, current approaches encounter critical context length bottlenecks and a domain alignment gap in understanding satellite features. We address these limitations through MAgSeg, a novel, decoder-free MLLM segmentation approach. MAgSeg is an architecturally efficient approach that enables standard MLLMs to perform segmentation of complex smallholder agricultural landscapes from high-resolution satellite imagery, without requiring auxiliary vision decoders. We introduce a novel instruction tuning data format designed to enable scalable fine-tuning and post-training on high resolution satellite imagery, which enables MAgSeg to learn from the global context of the image while generating text tokens for only a patch within the image. Extensive evaluations on datasets spanning three countries in the Global South demonstrate that MAgSeg significantly outperforms state-of-the-art MLLM baselines, offering a scalable solution to map smallholder agricultural environments.
匹配关键词: fine-tuning
---

[ACADEMIC - ARXIV]
标题: Res$^2$CLIP: Few-Shot Generalist Anomaly Detection with Residual-to-Residual Alignment
作者: Xinyue Liu, Jianyuan Wang, Biao Leng, Shuo Zhang
链接: https://arxiv.org/abs/2605.16171v1
完整摘要: Few-shot Generalist Anomaly Detection requires models to generalize to novel categories without retraining, posing significant challenges in real-world scenarios with scarce samples and rapidly changing categories. Existing CLIP-based methods face two major challenges: coarse-grained unified text prompts struggle to adapt to fine-grained foreground-background differences, causing cross-granularity mismatch; and fine-tuning on auxiliary datasets disrupts CLIP's inherent open-world generalization due to domain shift, leading to cross-category generalization degradation. To address these, we propose to shift multimodal alignment entirely into a unified residual space, where residual representations naturally eliminate fine-grained normal feature differences across regions and class-specific biases, simultaneously resolving both problems. Based on this insight, Res$^2$CLIP, the first residual-to-residual alignment framework that symmetrically bridges visual and text modalities within CLIP's residual space, is designed. The framework is developed from a residual perspective into three branches: a text prompt-based branch, a visual prompt-based branch, and a novel residual-to-residual alignment branch. All learnable optimizations are constrained within the residual domain, and the residual alignment optimization objectives are designed to force the model to focus on relative anomaly deviations rather than optimizing class-specific features. Experiments on multiple datasets demonstrate the effectiveness of our architecture. The code is available at https://github.com/hito2448/Res2CLIP.
匹配关键词: fine-tuning
---

[ACADEMIC - ARXIV]
标题: Learn Where Outcomes Diverge: Efficient VLA RL via Probabilistic Chunk Masking
作者: Vaidehi Bagaria, Nikshep Grampurohit, Pulkit Verma
链接: https://arxiv.org/abs/2605.16154v1
完整摘要: Reinforcement learning (RL) allows vision-language-action (VLA) policies to generalize beyond their training distribution by optimizing directly for task success, but post-training is computationally expensive. A natural response has been to speed rollout collection through faster simulators and world models. In GRPO-based VLA RL, we find that the dominant cost lies elsewhere: gradient computation accounts for approximately 78% of wall-clock time per step in our runs, while rollout collection accounts for only 21%. Gradient cost dominates because much of this computation is spent on phases that contribute little to learning. GRPO's learning signal is driven by advantage variance: only phases where successful and failed rollouts diverge produce learning signal. However, GRPO assigns the same advantage to every chunk in a rollout. As a result, actor-update compute is spent uniformly across the trajectory, including phases the policy already handles after pre-training and supervised fine-tuning. This paper presents Probabilistic Chunk Masking (PCM), a drop-in modification to GRPO that allocates gradient computation to a small, probabilistically selected subset of chunks per trajectory. PCM scores semantic phases using success-failure action variance, a rollout-derived proxy for per-phase gradient variance, and samples a fixed chunk budget with online-updated phase-level keep probabilities. We formalize per-phase gradient variance as the quantity determines where gradient computation is useful and show that success-failure action variance provides a measurable proxy for it. PCM requires no reward model or learned critic. On three LIBERO benchmarks, PCM matches the final success rate of standard GRPO while achieving 2.38 times wall-clock speedup, 4.8 times faster gradient updates, and 60% lower peak activation memory, while backpropagating through fewer than 20% of trajectory chunks.
匹配关键词: fine-tuning
---

[ACADEMIC - ARXIV]
标题: Surrogate Neural Architecture Codesign Package (SNAC-Pack)
作者: Jason Weitz, Dmitri Demler, Benjamin Hawks, Aaron Wang, Nhan Tran, Javier Duarte
链接: https://arxiv.org/abs/2605.16138v1
完整摘要: Neural architecture search (NAS) is a powerful approach for automating model design, but existing methods often optimize for accuracy alone or rely on proxy metrics such as bit operations (BOPs) that correlate poorly with hardware cost. This gap is particularly large for FPGA deployment, where cost is dominated by a multi-dimensional budget of lookup tables, DSPs, flip-flops, BRAM, and latency. We present the Surrogate Neural Architecture Codesign Package (SNAC-Pack), an open-source AutoML framework for hardware-aware neural architecture codesign and end-to-end FPGA deployment. SNAC-Pack runs a multi-objective global search with Optuna and NSGA-II, loading trials to a shared SQLite store that enables parallel workers across compute nodes. A hardware surrogate model outputs per-trial resource and latency estimates, avoiding the synthesis cost that would otherwise dominate the search loop. A local search stage then applies quantization-aware training (QAT) together with iterative magnitude pruning in a combined compression loop, after which the final model is synthesized to FPGA firmware via the hls4ml Python library. A YAML configuration and an optional agentic frontend let users run the pipeline on new datasets without modifying the framework. We demonstrate SNAC-Pack on jet classification at the Large Hadron Collider and superconducting qubit readout, discovering compact architectures that match or exceed strong baselines on the task metric while reducing FPGA resource utilization and, in the qubit readout case, reducing the design space exploration process from months of manual fine-tuning to hours of automated search.
匹配关键词: fine-tuning
---

[ACADEMIC - ARXIV]
标题: STABLE: Simulation-Ready Tabletop Layout Generation via a Semantics-Physics Dual System
作者: Zhen Luo, Yixuan Yang, Xudong Xu, Jinkun Hao, Zhaoyang Lyu, Feng Zheng, Jiangmiao Pang, Yanwei Fu
链接: https://arxiv.org/abs/2605.16137v1
完整摘要: Generating simulation-ready tabletop scenes from task instructions is an intriguing and promising research direction in the field of Embodied AI. However, existing task-to-scene generation methods rely exclusively on large language models (LLMs) to predict scene layouts, inevitably yielding object collisions or floating due to LLMs' inherent limitations in 3D spatial reasoning. In this paper, we present STABLE, a semantics-physics dual-system tailored for simulation-ready tabletop scene generation. STABLE consists of two complementary modules: (i) a Semantic Reasoner, a fine-tuned LLM trained on a structured tabletop scene dataset to generate coarse layouts from input task instructions, and (ii) a Physics Corrector, a physics-aware flow-based denoising model that outputs pose updates to refine layouts, which ensures the physical plausibility of scenes while preserves semantic alignment with task instructions. STABLE adopts a progressive generation paradigm: by alternating between the Semantic Reasoner and Physics Corrector, it incrementally expands the scene from task-critical objects to background objects. Experiments demonstrate that STABLE successfully generates simulation-ready tabletop scenes that strictly conform to task instructions and significantly enhances the physical validity of scenes over prior art.
匹配关键词: fine-tuning
---

[ACADEMIC - ARXIV]
标题: Fully Open Meditron: An Auditable Pipeline for Clinical LLMs
作者: Xavier Theimer-Lienhard, Mushtaha El-Amin, Fay Elhassan, Sahaj Vaidya, Victor Cartier-Negadi, David Sasu, Lars Klein, Mary-Anne Hartley
链接: https://arxiv.org/abs/2605.16215v1
完整摘要: Clinical decision support systems (CDSS) require scrutable, auditable pipelines that enable rigorous, reproducible validation. Yet current LLM-based CDSS remain largely opaque. Most "open" models are open-weight only, releasing parameters while withholding the data provenance, curation procedures, and generation pipelines that determine model behavior. Fully Open (FO) models, which expose the complete training stack end-to-end, do not currently exist in medicine. We introduce Fully Open Meditron, the first fully open pipeline for building LLM-CDSS, comprising a clinician-audited training corpus, a reproducible data construction and training framework, and a use-aligned evaluation protocol. The corpus unifies eight public medical QA datasets into a normalized conversational format and expands coverage with three clinician-vetted synthetic extensions: exam-style QA, guideline-grounded QA derived from 46,469 clinical practice guidelines, and clinical vignettes. The pipeline enforces system-wide decontamination, gold-label resampling of teacher generations, and end-to-end validation by a four-physician panel. We evaluate using an LLM-as-a-judge protocol over expert-written clinical vignettes, calibrated against 204 human raters. We apply the recipe to five FO base models (Apertus-70B/8B-Instruct, OLMo-2-32B-SFT, EuroLLM-22B/9B-Instruct). All MeditronFO variants are preferred over their bases. Apertus-70B-MeditronFO improves +6.6 points over its base (47.2% to 53.8%) on aggregate medical benchmarks, establishing a new FO SoTA. Gemma-3-27B-MeditronFO is preferred over MedGemma in 58.6% of LLM-as-a-judge comparisons and outperforms it on HealthBench (58% vs 55.9%). These results show that fully open pipelines can achieve state-of-the-art domain-specific performance without sacrificing auditability or reproducibility.
匹配关键词: SFT
---

[ACADEMIC - ARXIV]
标题: ATLAS: Agentic or Latent Visual Reasoning? One Word is Enough for Both
作者: Ziyu Guo, Rain Liu, Xinyan Chen, Pheng-Ann Heng
链接: https://arxiv.org/abs/2605.15198v1
完整摘要: Visual reasoning, often interleaved with intermediate visual states, has emerged as a promising direction in the field. A straightforward approach is to directly generate images via unified models during reasoning, but this is computationally expensive and architecturally non-trivial. Recent alternatives include agentic reasoning through code or tool calls, and latent reasoning with learnable hidden embeddings. However, agentic methods incur context-switching latency from external execution, while latent methods lack task generalization and are difficult to train with autoregressive parallelization. To combine their strengths while mitigating their limitations, we propose ATLAS, a framework in which a single discrete 'word', termed as a functional token, serves both as an agentic operation and a latent visual reasoning unit. Each functional token is associated with an internalized visual operation, yet requires no visual supervision and remains a standard token in the tokenizer vocabulary, which can be generated via next-token prediction. This design avoids verbose intermediate visual content generation, while preserving compatibility with the vanilla scalable SFT and RL training, without architectural or methodological modifications. To further address the sparsity of functional tokens during RL, we introduce Latent-Anchored GRPO (LA-GRPO), which stabilizes the training by anchoring functional tokens with a statically weighted auxiliary objective, providing stronger gradient updates. Extensive experiments and analyses demonstrate that ATLAS achieves superior performance on challenging benchmarks while maintaining clear interpretability. We hope ATLAS offers a new paradigm inspiring future visual reasoning research.
匹配关键词: SFT
---

[ACADEMIC - ARXIV]
标题: Orchard: An Open-Source Agentic Modeling Framework
作者: Baolin Peng, Wenlin Yao, Qianhui Wu, Hao Cheng, Xiao Yu, Rui Yang, Tao Ge, Alessandrio Sordoni, Xingdi Yuan, Yelong Shen, Pengcheng He, Tong Zhang, Zhou Yu, Jianfeng Gao
链接: https://arxiv.org/abs/2605.15040v1
完整摘要: Agentic modeling aims to transform LLMs into autonomous agents capable of solving complex tasks through planning, reasoning, tool use, and multi-turn interaction with environments. Despite major investment, open research remains constrained by infrastructure and training gaps. Many high-performing systems rely on proprietary codebases, models, or services, while most open-source frameworks focus on orchestration and evaluation rather than scalable agent training. We present Orchard, an open-source framework for scalable agentic modeling. At its core is Orchard Env, a lightweight environment service providing reusable primitives for sandbox lifecycle management across task domains, agent harnesses, and pipeline stages. On top of Orchard Env, we build three agentic modeling recipes. Orchard-SWE targets coding agents. We distill 107K trajectories from MiniMax-M2.5 and Qwen3.5-397B, introduce credit-assignment SFT to learn from productive segments of unresolved trajectories, and apply Balanced Adaptive Rollout for RL. Starting from Qwen3-30B-A3B-Thinking, Orchard-SWE achieves 64.3% on SWE-bench Verified after SFT and 67.5% after SFT+RL, setting a new state of the art among open-source models of comparable size. Orchard-GUI trains a 4B vision-language computer-use agent using only 0.4K distilled trajectories and 2.2K open-ended tasks. It achieves 74.1%, 67.0%, and 64.0% success rates on WebVoyager, Online-Mind2Web, and DeepShop, respectively, making it the strongest open-source model while remaining competitive with proprietary systems. Orchard-Claw targets personal assistant agents. Trained with only 0.2K synthetic tasks, it achieves 59.6% pass@3 on Claw-Eval and 73.9% when paired with a stronger ZeroClaw harness. Collectively, these results show that a lightweight, open, harness-agnostic environment layer enables reusable agentic data, training recipes, and evaluations across domains.
匹配关键词: SFT
---

[ACADEMIC - ARXIV]
标题: Boosting Reinforcement Learning with Verifiable Rewards via Randomly Selected Few-Shot Guidance
作者: Kai Yan, Alexander G. Schwing, Yu-Xiong Wang
链接: https://arxiv.org/abs/2605.15012v1
完整摘要: Reinforcement Learning with Verifiable Rewards (RLVR) has achieved great success in developing Large Language Models (LLMs) with chain-of-thought rollouts for many tasks such as math and coding. Nevertheless, RLVR struggles with sample efficiency on difficult problems where correct rollouts are hard to generate. Prior works propose to address this issue via demonstration-guided RLVR, i.e., to conduct Supervised FineTuning (SFT) when RL fails; however, SFT often requires a lot of data, which can be expensive to acquire. In this paper, we propose FEST, a FEw-ShoT demonstration-guided RLVR algorithm. It attains compelling results with only 128 demonstrations randomly selected from an SFT dataset. We find that three components are vital for the success: supervised signal, on-policy signal, and decaying weights on the few-shot SFT dataset to prevent overfitting from multiple-epoch training. On several benchmarks, FEST outperforms baselines with magnitudes less SFT data, even matching their performance with full dataset.
匹配关键词: SFT
---

[ACADEMIC - ARXIV]
标题: InfoSFT: Learn More and Forget Less with Information-Aware Token Weighting
作者: Mahdi Sabbaghi, George Pappas, Adel Javanmard, Hamed Hassani
链接: https://arxiv.org/abs/2605.14967v1
完整摘要: Supervised fine-tuning (SFT) provides the standard approach for teaching LLMs new behaviors from offline expert demonstrations. However, standard SFT uniformly fits all samples -- including those with low likelihood under the base model -- which can disproportionately drive training updates toward overfitting specific samples rather than learning the target behavior. Moreover, adapting to these unlikely samples induces substantial policy shifts that degrade prior capabilities. Existing methods mitigate this by filtering, regenerating, or down-weighting low-likelihood data. In doing so, they often suppress precisely the novel behaviors the base model has yet to learn. We propose InfoSFT, a principled weighting scheme for the SFT objective that concentrates learning signals on maximally informative, medium-confidence tokens -- those neither overly familiar to the base model nor too unlikely to cause instability. Requiring only a one-line modification to the standard token-wise loss, InfoSFT demonstrably improves generalization over vanilla SFT and likelihood-weighted baselines across math, code, and chain-of-thought tasks with diverse model families, while better preserving pre-existing capabilities.
匹配关键词: SFT
---

[ACADEMIC - ARXIV]
标题: AI-Mediated Communication Can Steer Collective Opinion
作者: Stratis Tsirtsis, Kai Rawal, Chris Russell, Brent Mittelstadt, Sandra Wachter
链接: https://arxiv.org/abs/2605.16245v1
完整摘要: Generative artificial intelligence (AI) is increasingly integrated into the online platforms where humans exchange opinions; large language models (LLMs) now polish users' posts on LinkedIn and provide context for content shared on X. While prior work has shown that AI can express biased opinions and shape individuals' opinions during human-AI interactions, less attention has been paid to its influence on collective opinion formation when mediating human-to-human communication. We address this gap via a combination of empirical and theoretical analyses. We show empirically that LLMs from multiple popular families introduce directional biases when instructed to edit human-written texts on contested topics, for example, nudging texts in favor of gun control and against atheism. Building on this observation, we introduce a mathematical model of opinion dynamics in which an AI system sits between users on a social network, transforming the opinions they express and perceive. By analytically characterizing the equilibrium of this model and performing simulations on real social network data, we show that biases introduced by AI in human-to-human communication can be amplified through the network and shift collective opinion in their direction. In light of these findings, we investigate whether such biases are controllable by online platforms. We audit the "Explain this post" feature on X and find evidence of pro-life bias in Grok's outputs on abortion-related content, which we trace back to specific design choices. We conclude with a discussion of the broader implications of our findings in relation to ongoing legislative efforts in the European Union.
匹配关键词: instruction tuning
---

[ACADEMIC - ARXIV]
标题: Fully Open Meditron: An Auditable Pipeline for Clinical LLMs
作者: Xavier Theimer-Lienhard, Mushtaha El-Amin, Fay Elhassan, Sahaj Vaidya, Victor Cartier-Negadi, David Sasu, Lars Klein, Mary-Anne Hartley
链接: https://arxiv.org/abs/2605.16215v1
完整摘要: Clinical decision support systems (CDSS) require scrutable, auditable pipelines that enable rigorous, reproducible validation. Yet current LLM-based CDSS remain largely opaque. Most "open" models are open-weight only, releasing parameters while withholding the data provenance, curation procedures, and generation pipelines that determine model behavior. Fully Open (FO) models, which expose the complete training stack end-to-end, do not currently exist in medicine. We introduce Fully Open Meditron, the first fully open pipeline for building LLM-CDSS, comprising a clinician-audited training corpus, a reproducible data construction and training framework, and a use-aligned evaluation protocol. The corpus unifies eight public medical QA datasets into a normalized conversational format and expands coverage with three clinician-vetted synthetic extensions: exam-style QA, guideline-grounded QA derived from 46,469 clinical practice guidelines, and clinical vignettes. The pipeline enforces system-wide decontamination, gold-label resampling of teacher generations, and end-to-end validation by a four-physician panel. We evaluate using an LLM-as-a-judge protocol over expert-written clinical vignettes, calibrated against 204 human raters. We apply the recipe to five FO base models (Apertus-70B/8B-Instruct, OLMo-2-32B-SFT, EuroLLM-22B/9B-Instruct). All MeditronFO variants are preferred over their bases. Apertus-70B-MeditronFO improves +6.6 points over its base (47.2% to 53.8%) on aggregate medical benchmarks, establishing a new FO SoTA. Gemma-3-27B-MeditronFO is preferred over MedGemma in 58.6% of LLM-as-a-judge comparisons and outperforms it on HealthBench (58% vs 55.9%). These results show that fully open pipelines can achieve state-of-the-art domain-specific performance without sacrificing auditability or reproducibility.
匹配关键词: instruction tuning
---

[ACADEMIC - ARXIV]
标题: Confirming Correct, Missing the Rest: LLM Tutoring Agents Struggle Where Feedback Matters Most
作者: Tahreem Yasir, Wenbo Li, Sam Gilson, Sutapa Dey Tithi, Xiaoyi Tian, Tiffany Barnes
链接: https://arxiv.org/abs/2605.16207v1
完整摘要: Effective tutoring requires distinguishing optimal, valid but suboptimal, and incorrect student solutions, a distinction central to intelligent tutoring systems (ITS) but untested for LLM-based tutors. As LLMs are increasingly explored as conversational complements to ITS, evaluating their diagnostic precision is essential. We present a benchmark of seven LLM feedback agents in propositional logic using knowledge-graph-derived ground truth across 10,836 solution--feedback pairs and three feedback conditions. Models achieved near-ceiling performance on optimal steps but systematically over-rejected valid but suboptimal reasoning and over-validated incorrect solutions, precisely where adaptive tutoring matters most. These failures persisted across models regardless of solution context, suggesting architectural rather than informational limits. Moreover, accurate diagnosis did not reliably produce pedagogically actionable feedback, revealing a gap between diagnostic judgment and instructional effectiveness. Our findings suggest that LLMs are better suited for hybrid architectures where KG-grounded models handle diagnosis while LLMs support open-ended scaffolding and dialogue.
匹配关键词: instruction tuning
---

[ACADEMIC - ARXIV]
标题: MAgSeg: Segmentation of Agricultural Landscapes in High-Resolution Satellite Imagery using Multimodal Large Language Models
作者: Piyush Tiwary, Utkarsh Ahuja, Depanshu Sani, Aishwarya Jayagopal, Sagar Gubbi, Subhashini Venugopalan, Alok Talekar, Vaibhav Rajan
链接: https://arxiv.org/abs/2605.16179v1
完整摘要: Agricultural landscape segmentation in the Global South is challenging as it is characterized by fragmented plots, high intra-class variance, and a scarcity of labeled training data. Recent advances in segmentation have been made by Multimodal Large Language Models (MLLMs). However, current approaches encounter critical context length bottlenecks and a domain alignment gap in understanding satellite features. We address these limitations through MAgSeg, a novel, decoder-free MLLM segmentation approach. MAgSeg is an architecturally efficient approach that enables standard MLLMs to perform segmentation of complex smallholder agricultural landscapes from high-resolution satellite imagery, without requiring auxiliary vision decoders. We introduce a novel instruction tuning data format designed to enable scalable fine-tuning and post-training on high resolution satellite imagery, which enables MAgSeg to learn from the global context of the image while generating text tokens for only a patch within the image. Extensive evaluations on datasets spanning three countries in the Global South demonstrate that MAgSeg significantly outperforms state-of-the-art MLLM baselines, offering a scalable solution to map smallholder agricultural environments.
匹配关键词: instruction tuning
---

[ACADEMIC - ARXIV]
标题: Res$^2$CLIP: Few-Shot Generalist Anomaly Detection with Residual-to-Residual Alignment
作者: Xinyue Liu, Jianyuan Wang, Biao Leng, Shuo Zhang
链接: https://arxiv.org/abs/2605.16171v1
完整摘要: Few-shot Generalist Anomaly Detection requires models to generalize to novel categories without retraining, posing significant challenges in real-world scenarios with scarce samples and rapidly changing categories. Existing CLIP-based methods face two major challenges: coarse-grained unified text prompts struggle to adapt to fine-grained foreground-background differences, causing cross-granularity mismatch; and fine-tuning on auxiliary datasets disrupts CLIP's inherent open-world generalization due to domain shift, leading to cross-category generalization degradation. To address these, we propose to shift multimodal alignment entirely into a unified residual space, where residual representations naturally eliminate fine-grained normal feature differences across regions and class-specific biases, simultaneously resolving both problems. Based on this insight, Res$^2$CLIP, the first residual-to-residual alignment framework that symmetrically bridges visual and text modalities within CLIP's residual space, is designed. The framework is developed from a residual perspective into three branches: a text prompt-based branch, a visual prompt-based branch, and a novel residual-to-residual alignment branch. All learnable optimizations are constrained within the residual domain, and the residual alignment optimization objectives are designed to force the model to focus on relative anomaly deviations rather than optimizing class-specific features. Experiments on multiple datasets demonstrate the effectiveness of our architecture. The code is available at https://github.com/hito2448/Res2CLIP.
匹配关键词: instruction tuning
---

[ACADEMIC - ARXIV]
标题: Designing Datacenter Power Delivery Hierarchies for the AI Era
作者: Grant Wilkins, Fiodar Kazhamiaka, Alok Gautam Kumbhare, Chaojie Zhang, Ricardo Bianchini
链接: https://arxiv.org/abs/2605.16255v1
完整摘要: Demand for AI accelerators is rapidly increasing rack power density, with projections approaching 1MW per deployment by 2027. This poses a major challenge for datacenter power delivery designers. As power densities increase, a datacenter designed for a different target density may strand power, i.e., may be unable to use all the power that its delivery hierarchy has provisioned. Designs must remain efficient over long datacenter lifetimes and multiple hardware generations. Power utilization is particularly important as grid power capacity is a scarce resource in the AI era. Designing an efficient power delivery hierarchy for the long run is difficult because rack placement feasibility, workload impact, and cost depend jointly on electrical topology, deployment granularity, placement policy, power oversubscription, and workload mix. Moreover, each of these factors evolve over time, have inter-dependencies across multiple resource dimensions, and generally do not lend themselves to closed-form analysis. To address this challenge, we develop a framework for evaluating datacenter power delivery designs using throughput, power, and cost metrics over realistic arrival, oversubscription, and decommissioning sequences. The framework combines projection models for GPU, compute, and storage deployments with operational factors grounded in production data from Microsoft Azure. Our results show that multi-resource stranding materially changes deployable capacity, effective capital expenditure, and delivered performance, and quantify how rising density from rack- and pod-scale AI systems shapes these outcomes. For AI datacenter design, the relevant planning objective is not installed megawatts, but deployable capacity over time.
匹配关键词: AI scientist
---

[ACADEMIC - ARXIV]
标题: A Generative AI Framework for Intelligent Utility Billing CO 2 Analytics and Sustainable Resource Optimisation
作者: Pavan Manjunath, Thomas Pruefer
链接: https://arxiv.org/abs/2605.16250v1
完整摘要: Distribution utilities are now expected to deliver bills that customers can actually read attach a defensible carbon number to every kWh sold and schedule load against grid stress and emissions constraints We propose an end-to-end framework that unifies four production-grade capabilities under one architectural roof a generative-AI agent that drafts each customers natural-language billing statement from structured numeric inputs under a constrained decoding policy a transformer-based forecaster that supplies the day-ahead consumption estimate with calibrated quantile bands
匹配关键词: AI scientist
---

[ACADEMIC - ARXIV]
标题: AI-Mediated Communication Can Steer Collective Opinion
作者: Stratis Tsirtsis, Kai Rawal, Chris Russell, Brent Mittelstadt, Sandra Wachter
链接: https://arxiv.org/abs/2605.16245v1
完整摘要: Generative artificial intelligence (AI) is increasingly integrated into the online platforms where humans exchange opinions; large language models (LLMs) now polish users' posts on LinkedIn and provide context for content shared on X. While prior work has shown that AI can express biased opinions and shape individuals' opinions during human-AI interactions, less attention has been paid to its influence on collective opinion formation when mediating human-to-human communication. We address this gap via a combination of empirical and theoretical analyses. We show empirically that LLMs from multiple popular families introduce directional biases when instructed to edit human-written texts on contested topics, for example, nudging texts in favor of gun control and against atheism. Building on this observation, we introduce a mathematical model of opinion dynamics in which an AI system sits between users on a social network, transforming the opinions they express and perceive. By analytically characterizing the equilibrium of this model and performing simulations on real social network data, we show that biases introduced by AI in human-to-human communication can be amplified through the network and shift collective opinion in their direction. In light of these findings, we investigate whether such biases are controllable by online platforms. We audit the "Explain this post" feature on X and find evidence of pro-life bias in Grok's outputs on abortion-related content, which we trace back to specific design choices. We conclude with a discussion of the broader implications of our findings in relation to ongoing legislative efforts in the European Union.
匹配关键词: AI scientist
---

[ACADEMIC - ARXIV]
标题: A Unified Generative-AI Framework for Smart Energy Infrastructure: Intelligent Gas Distribution, Utility Billing, Carbon Analytics, and Quantum-Inspired Optimisation
作者: Pavan Manjunath, Thomas pruefer
链接: https://arxiv.org/abs/2605.16232v1
完整摘要: The accelerating convergence of smart metering, generative artificial intelligence, and quantum-inspired combinatorial optimisation is reshaping how energy utilities manage physical infrastructure, customer engagement, and environmental accountability
匹配关键词: AI scientist
---

[ACADEMIC - ARXIV]
标题: Formal Methods Meet LLMs: Auditing, Monitoring, and Intervention for Compliance of Advanced AI Systems
作者: Parand A. Alamdari, Toryn Q. Klassen, Sheila A. McIlraith
链接: https://arxiv.org/abs/2605.16198v1
完整摘要: We examine one particular dimension of AI governance: how to monitor and audit AI-enabled products and services throughout the AI development lifecycle, from pre-deployment testing to post-deployment auditing. Combining principles from formal methods with SoTA machine learning, we propose techniques that enable AI-enabled product and service developers, as well as third party AI developers and evaluators, to perform offline auditing and online (runtime) monitoring of product-specific (temporally extended) behavioral constraints such as safety constraints, norms, rules and regulations with respect to black-box advanced AI systems, notably LLMs. We further provide practical techniques for predictive monitoring, such as sampling-based methods, and we introduce intervening monitors that act at runtime to preempt and potentially mitigate predicted violations. Experimental results show that by exploiting the formal syntax and semantics of Linear Temporal Logic (LTL), our proposed auditing and monitoring techniques are superior to LLM baseline methods in detecting violations of temporally extended behavioral constraints; with our approach, even small-model labelers match or exceed frontier LLM judges. Our predictive and intervening monitors significantly reduce the violation rates of LLM-based agents while largely preserving task performance. We further show through controlled experiments that LLMs' temporal reasoning shows a pronounced degradation in accuracy with increasing event distance, number of constraints, and number of propositions.
匹配关键词: AI scientist
---

[ACADEMIC - ARXIV]
标题: DexJoCo: A Benchmark and Toolkit for Task-Oriented Dexterous Manipulation on MuJoCo
作者: Hanwen Wang, Weizhi Zhao, Xiangyu Wang, Siyuan Huang, He Lin, Boyuan Zheng, Rongtao Xu, Gang Wang, Yao Mu, He Wang, Lue Fan, Hongsheng Li, Zhaoxiang Zhang, Tieniu Tan
链接: https://arxiv.org/abs/2605.16257v1
完整摘要: Achieving human-level manipulation requires dexterous robotic hands capable of complex object interactions. Advancing such capabilities further demands standardized benchmarks for systematic evaluation. However, existing dexterous benchmarks lack tasks that reflect the unique manipulation capabilities of dexterous hands over parallel grippers, as well as comprehensive evaluation pipelines. In this paper, we present DexJoCo, a benchmark and toolkit for task-oriented dexterous manipulation, comprising 11 functionally grounded tasks that evaluate tool-use, bimanual coordination, long-horizon execution, and reasoning. We develop a low-cost data collection system and collect 1.1K trajectories across these tasks, with support for domain randomization to assess robustness. We benchmark modern models under diverse settings, including visual and dynamics randomization, multi-task training, and action-head adaptation. Through extensive empirical analysis, we identify several important insights and common limitations of current policies in dexterous manipulation, highlighting key challenges for future research in dexterous hand robot learning. Project page available at: https://dexjoco.github.io
匹配关键词: automated research
---

[ACADEMIC - ARXIV]
标题: Prospective multi-pathogen disease forecasting using autonomous LLM-guided tree search
作者: Sarah Martinson, Michael P. Brenner, Martyna Plomecka, Brian P. Williams, Nicholas G. Reich, Zahra Shamsi
链接: https://arxiv.org/abs/2605.16238v1
完整摘要: Probabilistic forecasting of infectious diseases is crucial for public health but relies on labor-intensive manual model curation by expert modeling teams. This bespoke development bottlenecks scalability to granular geographic resolutions or emerging pathogens. Here, we present an autonomous system using Large Language Model (LLM)-guided tree search to iteratively generate, evaluate, and optimize executable forecasting software. In a fully prospective, real-time evaluation during the 2025-2026 US respiratory season, the system autonomously discovered methodologically diverse models for influenza, COVID-19, and respiratory syncytial virus (RSV). Aggregating these machine-generated models yielded an ensemble that consistently matched or outperformed the gold-standard, human-curated Centers for Disease Control and Prevention (CDC) hub ensembles out-of-sample. The system successfully navigated data-scarce "cold start" scenarios for RSV. Moreover, controlled retrospective ablations revealed that optimizing log-scale distance metrics prevents reward hacking, while an automated judge-in-the-loop ensures structural fidelity to complex scientific theories. By autonomously translating epidemiological theory into accurate, transparent code, this framework overcomes the modeling labor bottleneck, enabling rapid deployment of expert-level disease forecasting at unprecedented scales.
匹配关键词: automated research
---

[ACADEMIC - ARXIV]
标题: Layer Equivalence Is Not a Property of Layers Alone: How You Test Redundancy Changes What You Find
作者: Gabriel Garcia
链接: https://arxiv.org/abs/2605.16234v1
完整摘要: When researchers ask whether two transformer layers are "equivalent" for compression, they often conflate distinct tests. Replacement asks whether one layer's map can substitute for another's in place; interchange asks whether two layers approximately commute when their positions are swapped. Both are output-grounded swap-KL probes, but they need not agree: on pretrained transformers the protocol gap can change which layers look safe to prune by several-fold under the same evaluator, especially when replacement distances are high. We measure both protocols across checkpoints and architectures. On a Pythia training trajectory (410M and 1.4B), the replacement-interchange gap grows from initialization to convergence. Under one matched WikiText-2 contract at 8B scale, Qwen3-8B enters a divergent regime: interchange-guided removal is several-fold safer than replacement-guided at the same layer budgets, while Llama-3.1-8B ties the two protocols for pruning cost even though interchange KL is lower, showing metric gaps need not map one-to-one to removal. Before layer removal or merging, score both swap-KLs on the target checkpoint; the diagnostic requires only unlabeled forward passes.
匹配关键词: automated research
---

[ACADEMIC - ARXIV]
标题: Evaluating Design Video Generation: Metrics for Compositional Fidelity
作者: Adrienne Deganutti, Dingning Cao, Jaejung Seol, Elad Hirsch, Purvanshi Mehta
链接: https://arxiv.org/abs/2605.16223v1
完整摘要: Generative video models are increasingly used in design animation tasks, yet no standardized evaluation framework exists for this domain. Unlike natural video generation, design animation imposes structured constraints: specific components shall animate with prescribed motion types, directions, speed and timing, while non-animated regions must remain stable and layout structure must be preserved. This paper provides a fully automated evaluation framework organized across four dimensions: layout fidelity, motion correctness, temporal quality, and content fidelity. This eliminates the reliance on subjective human evaluation and establishes a common basis for benchmarking progress in the field.
匹配关键词: automated research
---

[ACADEMIC - ARXIV]
标题: Argus: Evidence Assembly for Scalable Deep Research Agents
作者: Zhen Zhang, Liangcai Su, Zhuo Chen, Xiang Lin, Haotian Xu, Simon Shaolei Du, Kaiyu Yang, Bo An, Lidong Bing, Xinyu Wang
链接: https://arxiv.org/abs/2605.16217v1
完整摘要: Deep research agents have achieved remarkable progress on complex information seeking tasks. Even long ReAct style rollouts explore only a single trajectory, while recent state of the art systems scale inference time compute via parallel search and aggregation. Yet deep research answers are composed of complementary pieces of evidence, which parallel rollouts often duplicate rather than complete, yielding diminishing returns while pushing the aggregation context toward the model's limit. We propose Argus, an agentic system in which a Searcher and a Navigator cooperate to treat deep research as assembling a jigsaw from complementary evidence pieces, rather than brute forcing the whole answer in parallel. The Searcher collects evidence traces for a given sub-query through ReAct-style interaction. The Navigator maintains a shared evidence graph, verifying which pieces are still missing, dispatching Searchers to gather them, and reasoning over the completed graph to produce a source-traced final answer. We train the Navigator with reinforcement learning to verify, dispatch, and synthesize, while independently training the Searcher to remain a standard ReAct agent. The resulting Navigator supports rollouts with a single Searcher or many in parallel without retraining. With both Searcher and Navigator built on a 35B-A3B MoE backbone, Argus gains 5.5 points with a single Searcher and 12.7 points with 8 parallel Searchers, averaged over eight benchmarks. With 64 Searchers it reaches 86.2 on BrowseComp, surpassing every proprietary agent we benchmark, while the Navigator's reasoning context stays under 21.5K tokens.
匹配关键词: automated research
---

[ACADEMIC - ARXIV]
标题: Prospective multi-pathogen disease forecasting using autonomous LLM-guided tree search
作者: Sarah Martinson, Michael P. Brenner, Martyna Plomecka, Brian P. Williams, Nicholas G. Reich, Zahra Shamsi
链接: https://arxiv.org/abs/2605.16238v1
完整摘要: Probabilistic forecasting of infectious diseases is crucial for public health but relies on labor-intensive manual model curation by expert modeling teams. This bespoke development bottlenecks scalability to granular geographic resolutions or emerging pathogens. Here, we present an autonomous system using Large Language Model (LLM)-guided tree search to iteratively generate, evaluate, and optimize executable forecasting software. In a fully prospective, real-time evaluation during the 2025-2026 US respiratory season, the system autonomously discovered methodologically diverse models for influenza, COVID-19, and respiratory syncytial virus (RSV). Aggregating these machine-generated models yielded an ensemble that consistently matched or outperformed the gold-standard, human-curated Centers for Disease Control and Prevention (CDC) hub ensembles out-of-sample. The system successfully navigated data-scarce "cold start" scenarios for RSV. Moreover, controlled retrospective ablations revealed that optimizing log-scale distance metrics prevents reward hacking, while an automated judge-in-the-loop ensures structural fidelity to complex scientific theories. By autonomously translating epidemiological theory into accurate, transparent code, this framework overcomes the modeling labor bottleneck, enabling rapid deployment of expert-level disease forecasting at unprecedented scales.
匹配关键词: scientific discovery
---

[ACADEMIC - ARXIV]
标题: Universal Magnetic Structure Prediction from Atomic Coordinates with Near-Experimental Accuracy
作者: Abhijatmedhi Chotrattanapituk, Ryotaro Okabe, Eunbi Rha, Mariya Al-Hinai, Eugene Jiang, Daniel Pajerowski, Yongqiang Cheng, Joshua J. Turner, Mingda Li
链接: https://arxiv.org/abs/2605.16230v1
完整摘要: Magnetic order is a fundamental property of materials, governing collective behavior and enabling a broad range of functionalities. Yet magnetic structure remains difficult to determine: experiments are costly and specialized, while first-principles methods often struggle with the noncollinear and incommensurate orders found in real materials. Here we introduce magnetic structure network (MSN), an E(3) equivariant graph neural network that predicts both collinear and non-collinear magnetic structures directly from atomic crystal structures, trained directly on experimentally determined structures from MAGNDATA. By proposing the primitive modulated structure representation (PMSR), we are able to encode commensurate and incommensurate structures in a unified way without symmetry assumptions. The model achieves strong performance across all modulation components and reconstructs experimental magnetic structures with high fidelity. Our approach provides a scalable framework for rapid magnetic structure prediction and opens a route to data-driven discovery of magnetic materials.
匹配关键词: scientific discovery
---

[ACADEMIC - ARXIV]
标题: Hypothesis-driven construction of mesoscopic dynamics
作者: Zhuoyuan Li, Aiqing Zhu, Qianxiao Li
链接: https://arxiv.org/abs/2605.16211v1
完整摘要: Traditional scientific modeling typically begins with fixed, instance-wise effective equations and then carries out equation-specific analysis and computation, a procedure that becomes exceptionally challenging in complex applications such as multiscale systems. We propose an alternative paradigm by learning mesoscopic dynamics within a mathematically constrained hypothesis class. Building upon a generalized Onsager principle, we introduce a unified framework encompassing both dissipative and conservative mesoscopic dynamics. We establish uniform and a priori theoretical guarantees, including global well-posedness, asymptotic stability, unique factorization identifiability, and discrete energy dissipation, applicable to all spatio-temporal evolution equations within this hypothesis class prior to all learning stages. Data from each problem instance is then used to guide the identification of members within our hypothesis class, giving rise to accurate, robust and interpretable dynamical models. We empirically validate this framework on both data from continuum PDE models as a check, and on data arising from microscopic chain models for which exact meso-scale models are unknown. The proposed approach not only acts as an effective dynamics learner, but also offers vital interpretable diagnostics of the underlying physics.
匹配关键词: scientific discovery
---

[ACADEMIC - ARXIV]
标题: Optimized Three-Dimensional Photovoltaic Structures with LLM guided Tree Search
作者: Michael P. Brenner, Lizzie Dorfman, John C. Platt
链接: https://arxiv.org/abs/2605.16191v1
完整摘要: We present a case study for how AI coding systems can be used to generate novel scientific hypotheses. We combine a generic coding agent (Google's AntiGravity) with an LLM-driven tree search algorithm (Empirical Research Assistance / ERA) to autonomously generate high-efficiency three-dimensional photovoltaic (3DPV) structures that overcome losses limiting flat solar panels at mid-latitudes. These structures operate by presenting favorable angles to the sun throughout the day, and for illustrative purposes we focus on optimizing performance for a single solar day. Our workflow begins by using AntiGravity to reproduce calculations \cite{bernardi2012solar} showing that 3DPV can have energy densities much higher than stationary flat PV panels. We use these initial designs as the starting point for large scale tree search, where we seek improved solutions and score them for their diurnal yield. The initial tree search leads to nominally more efficient solutions, yet they are caused by algorithmic reward hacking, arising from non-physical design features such as structurally levitating disconnected tiers and exploitations of the discretizations in the optics solver. To counteract this, we develop a workflow where the coding agent iteratively patches the physics engine with constraints to eliminate reward hacking. With reward-hacking eliminated, ERA discovers a series of designs with various constraints and improved performance, including optimal designs with different fixed collector areas, optimizing zenith tracking and avoiding self shadowing. Combining coding agents with tree search (ERA) provides a powerful platform for scientific discovery, for problems whose solutions can be empirically evaluated with a score function.
匹配关键词: scientific discovery
---

[ACADEMIC - ARXIV]
标题: ShopGym: An Integrated Framework for Realistic Simulation and Scalable Benchmarking of E-Commerce Web Agents
作者: Chinmay Savadikar, Mingyu Zhao, Yuanzheng Zhu, Han Li, Shuang Xie, Alberto Castelo, Tianfu Wu, Lingyun Wang
链接: https://arxiv.org/abs/2605.16116v1
完整摘要: Developing and evaluating e-commerce web agents requires environments that preserve meaningful task structure while enabling controllable, reproducible, and scalable scientific comparison. Existing methodologies force a tradeoff: live storefronts provide realism but are non-stationary, difficult to inspect, and irreproducible, while hand-built sandbox benchmarks provide control but cover only a narrow range of layouts, catalogs, policies, and interaction patterns. We argue that the core bottleneck is methodological: the field lacks a scalable way to construct evaluation settings that are simultaneously realistic, diverse, controllable, inspectable, and reproducible. We introduce ShopGym, an integrated framework for realistic simulation and scalable benchmarking of e-commerce web agents. ShopGym is a framework for constructing e-commerce simulation environments and grounded benchmark tasks. Its simulation layer, ShopArena, converts live seed storefronts into self-contained sandbox shops through anonymized shop specifications and a staged, validated generation process. On top of these simulated storefronts, ShopGuru synthesizes benchmark tasks across seven skill categories, grounding each task in the shop's catalog, navigation structure, policies, and interaction affordances. Together, ShopArena and ShopGuru produce self-contained, resettable, inspectable, and stable evaluation artifacts that preserve structural properties and agent-evaluation signals relevant to shopping tasks. We validate the framework through graph-based structural analysis and agent-based behavioral evaluation with 224 generated tasks across six sandbox shops: three constructed with synthetic data and three with real data. Our results show that the synthetic shops preserve key structural properties of live storefronts, with agent performance on synthetic shops positively correlated with performance on live storefronts.
匹配关键词: scientific discovery
---

[ACADEMIC - ARXIV]
标题: IVGT: Implicit Visual Geometry Transformer for Neural Scene Representation
作者: Yuqi Wu, Tianyu Hu, Wenzhao Zheng, Yuanhui Huang, Haowen Sun, Jie Zhou, Jiwen Lu
链接: https://arxiv.org/abs/2605.16258v1
完整摘要: Reconstructing coherent 3D geometry and appearance from unposed multi-view images is a fundamental yet challenging problem in computer vision. Most existing visual geometry foundation models predict explicit geometry by regressing pixel-aligned pointmaps, often suffering from redundancy and limited geometric continuity. We propose IVGT, an Implicit Visual Geometry Transformer that implicitly models continuous and coherent geometry from pose-free multi-view images. This formulation learns a continuous neural scene representation in a canonical coordinate system and supports continuous spatial queries at any 3D positions, retrieving local features to predict signed distance (SDF) values and colors using lightweight decoders. It allows direct extraction of continuous and coherent surface geometry, enabling rendering of RGB images, depth maps, and surface normal maps from arbitrary viewpoints. We train IVGT via multi-dataset joint optimization with 2D supervision and 3D geometric regularization. IVGT demonstrates generalization across scenes and achieves strong performance on various tasks, including mesh and point cloud reconstruction, novel view synthesis, depth and surface normal estimation, and camera pose estimation.
匹配关键词: hypothesis generation
---

[ACADEMIC - ARXIV]
标题: Designing Datacenter Power Delivery Hierarchies for the AI Era
作者: Grant Wilkins, Fiodar Kazhamiaka, Alok Gautam Kumbhare, Chaojie Zhang, Ricardo Bianchini
链接: https://arxiv.org/abs/2605.16255v1
完整摘要: Demand for AI accelerators is rapidly increasing rack power density, with projections approaching 1MW per deployment by 2027. This poses a major challenge for datacenter power delivery designers. As power densities increase, a datacenter designed for a different target density may strand power, i.e., may be unable to use all the power that its delivery hierarchy has provisioned. Designs must remain efficient over long datacenter lifetimes and multiple hardware generations. Power utilization is particularly important as grid power capacity is a scarce resource in the AI era. Designing an efficient power delivery hierarchy for the long run is difficult because rack placement feasibility, workload impact, and cost depend jointly on electrical topology, deployment granularity, placement policy, power oversubscription, and workload mix. Moreover, each of these factors evolve over time, have inter-dependencies across multiple resource dimensions, and generally do not lend themselves to closed-form analysis. To address this challenge, we develop a framework for evaluating datacenter power delivery designs using throughput, power, and cost metrics over realistic arrival, oversubscription, and decommissioning sequences. The framework combines projection models for GPU, compute, and storage deployments with operational factors grounded in production data from Microsoft Azure. Our results show that multi-resource stranding materially changes deployable capacity, effective capital expenditure, and delivered performance, and quantify how rising density from rack- and pod-scale AI systems shapes these outcomes. For AI datacenter design, the relevant planning objective is not installed megawatts, but deployable capacity over time.
匹配关键词: hypothesis generation
---

[ACADEMIC - ARXIV]
标题: Real-time Speech Restoration using Data Prediction Mean Flows
作者: Sebastian Braun
链接: https://arxiv.org/abs/2605.16251v1
完整摘要: Generative models are capable to address difficult problems with non-unique solutions like bandwidth extension and gap filling, removing highly non-linear artifacts from codecs, clipping and distortion, as opposed to removing linear additive components like noise and reverb. While large offline processing models have shown impressive results, these tasks have not been solved with real-time capable models with low latency and compute. We propose a few-step flow matching model using Data Prediction Mean Flows in combination with suitable novel low-latency architecture to make flow matching models an attractive choice under theses constraints. Compared to state-of-the-art, our proposed mean flow model uses 120x less compute and introduces no algorithmic latency other than the STFT, while achieving similar audio quality.
匹配关键词: hypothesis generation
---

[ACADEMIC - ARXIV]
标题: A Generative AI Framework for Intelligent Utility Billing CO 2 Analytics and Sustainable Resource Optimisation
作者: Pavan Manjunath, Thomas Pruefer
链接: https://arxiv.org/abs/2605.16250v1
完整摘要: Distribution utilities are now expected to deliver bills that customers can actually read attach a defensible carbon number to every kWh sold and schedule load against grid stress and emissions constraints We propose an end-to-end framework that unifies four production-grade capabilities under one architectural roof a generative-AI agent that drafts each customers natural-language billing statement from structured numeric inputs under a constrained decoding policy a transformer-based forecaster that supplies the day-ahead consumption estimate with calibrated quantile bands
匹配关键词: hypothesis generation
---

[ACADEMIC - ARXIV]
标题: AI-Mediated Communication Can Steer Collective Opinion
作者: Stratis Tsirtsis, Kai Rawal, Chris Russell, Brent Mittelstadt, Sandra Wachter
链接: https://arxiv.org/abs/2605.16245v1
完整摘要: Generative artificial intelligence (AI) is increasingly integrated into the online platforms where humans exchange opinions; large language models (LLMs) now polish users' posts on LinkedIn and provide context for content shared on X. While prior work has shown that AI can express biased opinions and shape individuals' opinions during human-AI interactions, less attention has been paid to its influence on collective opinion formation when mediating human-to-human communication. We address this gap via a combination of empirical and theoretical analyses. We show empirically that LLMs from multiple popular families introduce directional biases when instructed to edit human-written texts on contested topics, for example, nudging texts in favor of gun control and against atheism. Building on this observation, we introduce a mathematical model of opinion dynamics in which an AI system sits between users on a social network, transforming the opinions they express and perceive. By analytically characterizing the equilibrium of this model and performing simulations on real social network data, we show that biases introduced by AI in human-to-human communication can be amplified through the network and shift collective opinion in their direction. In light of these findings, we investigate whether such biases are controllable by online platforms. We audit the "Explain this post" feature on X and find evidence of pro-life bias in Grok's outputs on abortion-related content, which we trace back to specific design choices. We conclude with a discussion of the broader implications of our findings in relation to ongoing legislative efforts in the European Union.
匹配关键词: hypothesis generation
---

[ACADEMIC - ARXIV]
标题: Dynamics-Level Watermarking of Flow Matching Models with Random Codes
作者: Shuchan Wang
链接: https://arxiv.org/abs/2605.16239v1
完整摘要: We introduce a dynamics-level approach to watermarking generative models. Rather than embedding signals into model weights or outputs, we embed the watermark directly into the learned continuous dynamics -- the velocity field of a flow matching model. We formulate this as random coding over a continuous channel: a key-dependent perturbation is added during training, and the message is recovered at detection time from black-box queries. The perturbation is designed to leave the generated distribution unchanged. Experiments on MNIST and CIFAR-10 across different architectures confirm reliable message recovery, preserved generation quality, and chance-level decoding accuracy without the secret key.
匹配关键词: autonomous experiment
---

[ACADEMIC - ARXIV]
标题: Prospective multi-pathogen disease forecasting using autonomous LLM-guided tree search
作者: Sarah Martinson, Michael P. Brenner, Martyna Plomecka, Brian P. Williams, Nicholas G. Reich, Zahra Shamsi
链接: https://arxiv.org/abs/2605.16238v1
完整摘要: Probabilistic forecasting of infectious diseases is crucial for public health but relies on labor-intensive manual model curation by expert modeling teams. This bespoke development bottlenecks scalability to granular geographic resolutions or emerging pathogens. Here, we present an autonomous system using Large Language Model (LLM)-guided tree search to iteratively generate, evaluate, and optimize executable forecasting software. In a fully prospective, real-time evaluation during the 2025-2026 US respiratory season, the system autonomously discovered methodologically diverse models for influenza, COVID-19, and respiratory syncytial virus (RSV). Aggregating these machine-generated models yielded an ensemble that consistently matched or outperformed the gold-standard, human-curated Centers for Disease Control and Prevention (CDC) hub ensembles out-of-sample. The system successfully navigated data-scarce "cold start" scenarios for RSV. Moreover, controlled retrospective ablations revealed that optimizing log-scale distance metrics prevents reward hacking, while an automated judge-in-the-loop ensures structural fidelity to complex scientific theories. By autonomously translating epidemiological theory into accurate, transparent code, this framework overcomes the modeling labor bottleneck, enabling rapid deployment of expert-level disease forecasting at unprecedented scales.
匹配关键词: autonomous experiment
---

[ACADEMIC - ARXIV]
标题: Universal Magnetic Structure Prediction from Atomic Coordinates with Near-Experimental Accuracy
作者: Abhijatmedhi Chotrattanapituk, Ryotaro Okabe, Eunbi Rha, Mariya Al-Hinai, Eugene Jiang, Daniel Pajerowski, Yongqiang Cheng, Joshua J. Turner, Mingda Li
链接: https://arxiv.org/abs/2605.16230v1
完整摘要: Magnetic order is a fundamental property of materials, governing collective behavior and enabling a broad range of functionalities. Yet magnetic structure remains difficult to determine: experiments are costly and specialized, while first-principles methods often struggle with the noncollinear and incommensurate orders found in real materials. Here we introduce magnetic structure network (MSN), an E(3) equivariant graph neural network that predicts both collinear and non-collinear magnetic structures directly from atomic crystal structures, trained directly on experimentally determined structures from MAGNDATA. By proposing the primitive modulated structure representation (PMSR), we are able to encode commensurate and incommensurate structures in a unified way without symmetry assumptions. The model achieves strong performance across all modulation components and reconstructs experimental magnetic structures with high fidelity. Our approach provides a scalable framework for rapid magnetic structure prediction and opens a route to data-driven discovery of magnetic materials.
匹配关键词: autonomous experiment
---

[ACADEMIC - ARXIV]
标题: A Scalable Nonparametric Continuous-Time Survival Model through Numerical Quadrature
作者: Chaeyeon Lee, Sehwan Kim, Hyungrok Do
链接: https://arxiv.org/abs/2605.16208v1
完整摘要: Flexible continuous-time survival modeling is critical for capturing complex time-varying hazard dynamics in high-dimensional data; however, training such models remains challenging due to the intractable integral required for likelihood estimation. We introduce QSurv, a scalable deep learning framework that enables nonparametric continuous-time modeling without relying on time discretization or restrictive distributional assumptions. We propose a training objective based on Gauss-Legendre numerical quadrature, which approximates the cumulative hazard with high-order accuracy while facilitating efficient end-to-end training via standard backpropagation. Furthermore, to effectively capture non-stationary hazard dynamics in complex architectures, we introduce time-conditioned low-rank adaptation, a mechanism that conditions general neural backbones on time by dynamically modulating weights via low-rank updates. We provide theoretical analysis establishing approximation error bounds for cumulative-hazard evaluation. Comprehensive experiments across synthetic benchmarks, large-scale real-world tabular datasets, and high-dimensional medical imaging tasks demonstrate that QSurv achieves competitive predictive performance with advantages in instantaneous hazard function estimation, enabling more interpretable characterization of time-varying risk patterns.
匹配关键词: autonomous experiment
---

[ACADEMIC - ARXIV]
标题: Formal Methods Meet LLMs: Auditing, Monitoring, and Intervention for Compliance of Advanced AI Systems
作者: Parand A. Alamdari, Toryn Q. Klassen, Sheila A. McIlraith
链接: https://arxiv.org/abs/2605.16198v1
完整摘要: We examine one particular dimension of AI governance: how to monitor and audit AI-enabled products and services throughout the AI development lifecycle, from pre-deployment testing to post-deployment auditing. Combining principles from formal methods with SoTA machine learning, we propose techniques that enable AI-enabled product and service developers, as well as third party AI developers and evaluators, to perform offline auditing and online (runtime) monitoring of product-specific (temporally extended) behavioral constraints such as safety constraints, norms, rules and regulations with respect to black-box advanced AI systems, notably LLMs. We further provide practical techniques for predictive monitoring, such as sampling-based methods, and we introduce intervening monitors that act at runtime to preempt and potentially mitigate predicted violations. Experimental results show that by exploiting the formal syntax and semantics of Linear Temporal Logic (LTL), our proposed auditing and monitoring techniques are superior to LLM baseline methods in detecting violations of temporally extended behavioral constraints; with our approach, even small-model labelers match or exceed frontier LLM judges. Our predictive and intervening monitors significantly reduce the violation rates of LLM-based agents while largely preserving task performance. We further show through controlled experiments that LLMs' temporal reasoning shows a pronounced degradation in accuracy with increasing event distance, number of constraints, and number of propositions.
匹配关键词: autonomous experiment
---

[ACADEMIC - ARXIV]
标题: Prospective multi-pathogen disease forecasting using autonomous LLM-guided tree search
作者: Sarah Martinson, Michael P. Brenner, Martyna Plomecka, Brian P. Williams, Nicholas G. Reich, Zahra Shamsi
链接: https://arxiv.org/abs/2605.16238v1
完整摘要: Probabilistic forecasting of infectious diseases is crucial for public health but relies on labor-intensive manual model curation by expert modeling teams. This bespoke development bottlenecks scalability to granular geographic resolutions or emerging pathogens. Here, we present an autonomous system using Large Language Model (LLM)-guided tree search to iteratively generate, evaluate, and optimize executable forecasting software. In a fully prospective, real-time evaluation during the 2025-2026 US respiratory season, the system autonomously discovered methodologically diverse models for influenza, COVID-19, and respiratory syncytial virus (RSV). Aggregating these machine-generated models yielded an ensemble that consistently matched or outperformed the gold-standard, human-curated Centers for Disease Control and Prevention (CDC) hub ensembles out-of-sample. The system successfully navigated data-scarce "cold start" scenarios for RSV. Moreover, controlled retrospective ablations revealed that optimizing log-scale distance metrics prevents reward hacking, while an automated judge-in-the-loop ensures structural fidelity to complex scientific theories. By autonomously translating epidemiological theory into accurate, transparent code, this framework overcomes the modeling labor bottleneck, enabling rapid deployment of expert-level disease forecasting at unprecedented scales.
匹配关键词: lab automation
---

[ACADEMIC - ARXIV]
标题: Evaluating Design Video Generation: Metrics for Compositional Fidelity
作者: Adrienne Deganutti, Dingning Cao, Jaejung Seol, Elad Hirsch, Purvanshi Mehta
链接: https://arxiv.org/abs/2605.16223v1
完整摘要: Generative video models are increasingly used in design animation tasks, yet no standardized evaluation framework exists for this domain. Unlike natural video generation, design animation imposes structured constraints: specific components shall animate with prescribed motion types, directions, speed and timing, while non-animated regions must remain stable and layout structure must be preserved. This paper provides a fully automated evaluation framework organized across four dimensions: layout fidelity, motion correctness, temporal quality, and content fidelity. This eliminates the reliance on subjective human evaluation and establishes a common basis for benchmarking progress in the field.
匹配关键词: lab automation
---

[ACADEMIC - ARXIV]
标题: Surrogate Neural Architecture Codesign Package (SNAC-Pack)
作者: Jason Weitz, Dmitri Demler, Benjamin Hawks, Aaron Wang, Nhan Tran, Javier Duarte
链接: https://arxiv.org/abs/2605.16138v1
完整摘要: Neural architecture search (NAS) is a powerful approach for automating model design, but existing methods often optimize for accuracy alone or rely on proxy metrics such as bit operations (BOPs) that correlate poorly with hardware cost. This gap is particularly large for FPGA deployment, where cost is dominated by a multi-dimensional budget of lookup tables, DSPs, flip-flops, BRAM, and latency. We present the Surrogate Neural Architecture Codesign Package (SNAC-Pack), an open-source AutoML framework for hardware-aware neural architecture codesign and end-to-end FPGA deployment. SNAC-Pack runs a multi-objective global search with Optuna and NSGA-II, loading trials to a shared SQLite store that enables parallel workers across compute nodes. A hardware surrogate model outputs per-trial resource and latency estimates, avoiding the synthesis cost that would otherwise dominate the search loop. A local search stage then applies quantization-aware training (QAT) together with iterative magnitude pruning in a combined compression loop, after which the final model is synthesized to FPGA firmware via the hls4ml Python library. A YAML configuration and an optional agentic frontend let users run the pipeline on new datasets without modifying the framework. We demonstrate SNAC-Pack on jet classification at the Large Hadron Collider and superconducting qubit readout, discovering compact architectures that match or exceed strong baselines on the task metric while reducing FPGA resource utilization and, in the qubit readout case, reducing the design space exploration process from months of manual fine-tuning to hours of automated search.
匹配关键词: lab automation
---

[ACADEMIC - ARXIV]
标题: VideoSeeker: Incentivizing Instance-level Video Understanding via Native Agentic Tool Invocation
作者: Yiming Zhao, Yu Zeng, Wenxuan Huang, Zhen Fang, Qing Miao, Qisheng Su, Jiawei Zhao, Jiayin Cai, Lin Chen, Zehui Chen, Yukun Qi, Yao Hu, Xiaolong Jiang, Feng Zhao
链接: https://arxiv.org/abs/2605.16079v1
完整摘要: Large Vision-Language Models (LVLMs) have shown significant progress in video understanding, yet they face substantial challenges in tasks requiring precise spatiotemporal localization at the instance level. Existing methods primarily rely on text prompts for human-model interaction, but these prompts struggle to provide precise spatial and temporal references, resulting in poor user experience. Furthermore, current approaches typically decouple visual perception from language reasoning, centering reasoning around language rather than visual content, which limits the model's ability to proactively perceive fine-grained visual evidence. To address these challenges, we propose VideoSeeker, a novel paradigm for instance-level video understanding through visual prompts. VideoSeeker seamlessly integrates agentic reasoning with instance-level video understanding tasks, enabling the model to proactively perceive and retrieve relevant video segments on demand. We construct a four-stage fully automated data synthesis pipeline to efficiently generate large-scale, high-quality instance-level video data. We internalize tool-calling and proactive perception capabilities into the model via cold-start supervision and RL training, building a powerful video understanding model. Experiments demonstrate that our model achieves an average improvement of +13.7% over baselines on instance-level video understanding tasks, surpassing powerful closed-source models such as GPT-4o and Gemini-2.5-Pro, while also showing effective transferability on general video understanding benchmarks. The relevant datasets and code will be released publicly.
匹配关键词: lab automation
---

[ACADEMIC - ARXIV]
标题: AgriMind: An Ensemble Deep Learning Framework for Multi-Class Plant Disease Classification
作者: Salma Hoque Talukdar Koli, Fahima Haque Talukder Jely
链接: https://arxiv.org/abs/2605.16076v1
完整摘要: Plant disease detection is still largely manual in Bangladesh, where extension workers eyeball leaf samples across millions of smallholdings. We built AgriMind to automate this: an ensemble of ResNet50, EfficientNet-B0, and DenseNet121 trained on 20,638 PlantVillage images across 15 pepper, potato, and tomato disease classes. Transfer learning with frozen ImageNet backbones and 10 epochs of head-only training keeps the pipeline lightweight. Individual models hit 96--97% on the held-out test set, but averaging their softmax outputs pushes the ensemble to 99.23% -- a two-thirds cut in error rate. We tried biasing the average toward the best validation model; it backfired. Dropping any single model also hurt. Pepper and potato classify perfectly; tomato, with ten visually similar classes, still reaches 99.01%. On an NVIDIA T4 GPU the full ensemble runs at 53 FPS. Whether that translates to real-time mobile use depends on TensorFlow Lite optimization -- work we have not yet completed.
匹配关键词: lab automation
---

[ACADEMIC - ARXIV]
标题: IVGT: Implicit Visual Geometry Transformer for Neural Scene Representation
作者: Yuqi Wu, Tianyu Hu, Wenzhao Zheng, Yuanhui Huang, Haowen Sun, Jie Zhou, Jiwen Lu
链接: https://arxiv.org/abs/2605.16258v1
完整摘要: Reconstructing coherent 3D geometry and appearance from unposed multi-view images is a fundamental yet challenging problem in computer vision. Most existing visual geometry foundation models predict explicit geometry by regressing pixel-aligned pointmaps, often suffering from redundancy and limited geometric continuity. We propose IVGT, an Implicit Visual Geometry Transformer that implicitly models continuous and coherent geometry from pose-free multi-view images. This formulation learns a continuous neural scene representation in a canonical coordinate system and supports continuous spatial queries at any 3D positions, retrieving local features to predict signed distance (SDF) values and colors using lightweight decoders. It allows direct extraction of continuous and coherent surface geometry, enabling rendering of RGB images, depth maps, and surface normal maps from arbitrary viewpoints. We train IVGT via multi-dataset joint optimization with 2D supervision and 3D geometric regularization. IVGT demonstrates generalization across scenes and achieves strong performance on various tasks, including mesh and point cloud reconstruction, novel view synthesis, depth and surface normal estimation, and camera pose estimation.
匹配关键词: AI for science
---

[ACADEMIC - ARXIV]
标题: DexJoCo: A Benchmark and Toolkit for Task-Oriented Dexterous Manipulation on MuJoCo
作者: Hanwen Wang, Weizhi Zhao, Xiangyu Wang, Siyuan Huang, He Lin, Boyuan Zheng, Rongtao Xu, Gang Wang, Yao Mu, He Wang, Lue Fan, Hongsheng Li, Zhaoxiang Zhang, Tieniu Tan
链接: https://arxiv.org/abs/2605.16257v1
完整摘要: Achieving human-level manipulation requires dexterous robotic hands capable of complex object interactions. Advancing such capabilities further demands standardized benchmarks for systematic evaluation. However, existing dexterous benchmarks lack tasks that reflect the unique manipulation capabilities of dexterous hands over parallel grippers, as well as comprehensive evaluation pipelines. In this paper, we present DexJoCo, a benchmark and toolkit for task-oriented dexterous manipulation, comprising 11 functionally grounded tasks that evaluate tool-use, bimanual coordination, long-horizon execution, and reasoning. We develop a low-cost data collection system and collect 1.1K trajectories across these tasks, with support for domain randomization to assess robustness. We benchmark modern models under diverse settings, including visual and dynamics randomization, multi-task training, and action-head adaptation. Through extensive empirical analysis, we identify several important insights and common limitations of current policies in dexterous manipulation, highlighting key challenges for future research in dexterous hand robot learning. Project page available at: https://dexjoco.github.io
匹配关键词: AI for science
---

[ACADEMIC - ARXIV]
标题: Designing Datacenter Power Delivery Hierarchies for the AI Era
作者: Grant Wilkins, Fiodar Kazhamiaka, Alok Gautam Kumbhare, Chaojie Zhang, Ricardo Bianchini
链接: https://arxiv.org/abs/2605.16255v1
完整摘要: Demand for AI accelerators is rapidly increasing rack power density, with projections approaching 1MW per deployment by 2027. This poses a major challenge for datacenter power delivery designers. As power densities increase, a datacenter designed for a different target density may strand power, i.e., may be unable to use all the power that its delivery hierarchy has provisioned. Designs must remain efficient over long datacenter lifetimes and multiple hardware generations. Power utilization is particularly important as grid power capacity is a scarce resource in the AI era. Designing an efficient power delivery hierarchy for the long run is difficult because rack placement feasibility, workload impact, and cost depend jointly on electrical topology, deployment granularity, placement policy, power oversubscription, and workload mix. Moreover, each of these factors evolve over time, have inter-dependencies across multiple resource dimensions, and generally do not lend themselves to closed-form analysis. To address this challenge, we develop a framework for evaluating datacenter power delivery designs using throughput, power, and cost metrics over realistic arrival, oversubscription, and decommissioning sequences. The framework combines projection models for GPU, compute, and storage deployments with operational factors grounded in production data from Microsoft Azure. Our results show that multi-resource stranding materially changes deployable capacity, effective capital expenditure, and delivered performance, and quantify how rising density from rack- and pod-scale AI systems shapes these outcomes. For AI datacenter design, the relevant planning objective is not installed megawatts, but deployable capacity over time.
匹配关键词: AI for science
---

[ACADEMIC - ARXIV]
标题: Real-time Speech Restoration using Data Prediction Mean Flows
作者: Sebastian Braun
链接: https://arxiv.org/abs/2605.16251v1
完整摘要: Generative models are capable to address difficult problems with non-unique solutions like bandwidth extension and gap filling, removing highly non-linear artifacts from codecs, clipping and distortion, as opposed to removing linear additive components like noise and reverb. While large offline processing models have shown impressive results, these tasks have not been solved with real-time capable models with low latency and compute. We propose a few-step flow matching model using Data Prediction Mean Flows in combination with suitable novel low-latency architecture to make flow matching models an attractive choice under theses constraints. Compared to state-of-the-art, our proposed mean flow model uses 120x less compute and introduces no algorithmic latency other than the STFT, while achieving similar audio quality.
匹配关键词: AI for science
---

[ACADEMIC - ARXIV]
标题: A Generative AI Framework for Intelligent Utility Billing CO 2 Analytics and Sustainable Resource Optimisation
作者: Pavan Manjunath, Thomas Pruefer
链接: https://arxiv.org/abs/2605.16250v1
完整摘要: Distribution utilities are now expected to deliver bills that customers can actually read attach a defensible carbon number to every kWh sold and schedule load against grid stress and emissions constraints We propose an end-to-end framework that unifies four production-grade capabilities under one architectural roof a generative-AI agent that drafts each customers natural-language billing statement from structured numeric inputs under a constrained decoding policy a transformer-based forecaster that supplies the day-ahead consumption estimate with calibrated quantile bands
匹配关键词: AI for science
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
标题: DeepLog: A Software Framework for Modular Neurosymbolic AI
作者: Robin Manhaeve, Stefano Colamonaco, Vincent Derkinderen, Rik Adriaensen, Lucas Van Praet, Luc De Raedt, Giuseppe Marra
链接: https://arxiv.org/abs/2605.10279v1
完整摘要: DeepLog is an operational neurosymbolic framework that unifies logic and deep learning within standard PyTorch workflows. While existing neurosymbolic systems focus on a particular paradigm and semantics, DeepLog serves as a universal backend that can emulate many systems in the neurosymbolic alphabet soup. By treating diverse neurosymbolic languages as high-level specifications, the DeepLog software automatically compiles them into optimized arithmetic circuits. This design lowers the barrier for machine learning practitioners by treating logic as composable modules, while providing neurosymbolic developers with a shared, high-performance basis for prototyping new integration strategies. The code is available here: https://github.com/ML-KULeuven/deeplog
匹配关键词: PyTorch
---

[ACADEMIC - ARXIV]
标题: Monocular Biomechanical Tracking of Fingers with Inverse Kinematics to Foundation Models
作者: R. James Cotton, Pouyan Firouzabadi, Wendy Murray
链接: https://arxiv.org/abs/2605.09258v1
完整摘要: Accurate hand and finger tracking from video has significant clinical applications for monitoring activities of daily living and measuring range of motion, yet monocular video approaches for obtaining hand biomechanics remain under-developed. We present a method that combines the SAM 3D Body foundation model with inverse kinematics optimization in a full-body biomechanical model to extract anatomically-constrained finger joint angles from single-view video. We port SAM 3D Body from PyTorch to JAX for integration with MuJoCo-MJX, enabling GPU-accelerated optimization, and develop a novel mapping between the Momentum Human Rig (MHR) outputs and biomechanical model markers. Validation against 8-camera multiview reconstruction on 4,590 frames from 7 participants performing a variety of hand poses and object manipulation tasks shows finger joint angle errors of approximately 10 degrees and hand position errors of approximately 6 mm, after Procrustes alignment. Results were consistent across camera viewpoints and robust to different methods for producing reference values from multiview video. This work extends monocular biomechanical analysis to detailed finger tracking, expanding access to quantitative characterization of hand movement from readily available video.
匹配关键词: PyTorch
---

[ACADEMIC - ARXIV]
标题: Single-Thread JPEG Decoder Benchmarks Mis-Evaluate ML Data Loaders
作者: Vladimir Iglovikov
链接: https://arxiv.org/abs/2605.08731v1
完整摘要: JPEG decode is routine ML infrastructure, but Python decoder choices are often justified by single-process, single-thread microbenchmarks. We audit this evaluation assumption with twelve Python-accessible JPEG decode paths on five matched 16 vCPU Google Cloud CPUs: Intel Emerald Rapids, AMD Zen 4, AMD Zen 5, ARM Neoverse V2, and ARM Neoverse N1. ImageNet validation is the workload, not a new dataset contribution: each run decodes the full 50,000-image split from memory and reports single-thread throughput for all decoders, PyTorch DataLoader throughput for eligible decoders at worker counts {0,2,4,8}, and decoder skip behavior. The evaluation protocol changes the supported conclusion. On Neoverse V2, imageio is ninth in single-thread throughput yet lands in the top DataLoader tier with torchvision; on Zen 4, torchvision rises from seventh single-thread to the top measured DataLoader tier; on Neoverse N1, imagecodecs is the single-thread leader but fourth at peak DataLoader throughput. We also find that worker-count conclusions differ between Zen 4 and Zen 5, TensorFlow has a large single-thread ARM penalty, and strict libjpeg-turbo-family wrappers reject the same rare ImageNet JPEG. For PyTorch DataLoader workloads, torchvision and simplejpeg form the strongest measured zero-skip tier: torchvision has the highest mean normalized throughput, while simplejpeg has the highest minimum. OpenCV remains a robust general-purpose fallback above 90% of the platform-local winner on every tested CPU. We release raw JSON, generated tables/figures, and an executable local/cloud benchmark framework.
匹配关键词: PyTorch
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
标题: MDN: Parallelizing Stepwise Momentum for Delta Linear Attention
作者: Yulong Huang, Xiang Liu, Hongxiang Huang, Xiaopeng Lin, Zunchang Liu, Xiaowen Chu, Zeke Xie, Bojun Cheng
链接: https://arxiv.org/abs/2605.05838v1
完整摘要: Linear Attention (LA) offers a promising paradigm for scaling large language models (LLMs) to long sequences by avoiding the quadratic complexity of self-attention. Recent LA models such as Mamba2 and GDN interpret linear recurrences as closed-form online stochastic gradient descent (SGD), but naive SGD updates suffer from rapid information decay and suboptimal convergence in optimization. While momentum-based optimizers provide a natural remedy, they pose challenges in simultaneously achieving training efficiency and effectiveness. To address this, we develop a chunkwise parallel algorithm for LA with a stepwise momentum rule by geometrically reordering the update coefficients. Further, from a dynamical systems perspective, we analyze the momentum-based recurrence as a second-order system that introduces complex conjugate eigenvalues. This analysis guides the design of stable gating constraints. The resulting model, Momentum DeltaNet (MDN), leverages Triton kernels to achieve comparable training throughput with competitive linear models such as Mamba2 and KDA. Extensive experiments on the 400M and 1.3B parameter models demonstrate consistent performance improvements over strong baselines, including Transformers, Mamba2 and GDN, across diverse downstream evaluation benchmarks. Code: https://github.com/HuuYuLong/MomentumDeltaNet .
匹配关键词: Triton
---

[ACADEMIC - ARXIV]
标题: KernelBenchX: A Comprehensive Benchmark for Evaluating LLM-Generated GPU Kernels
作者: Han Wang, Jintao Zhang, Kai Jiang, Haoxu Wang, Jianfei Chen, Jun Zhu
链接: https://arxiv.org/abs/2605.04956v2
完整摘要: LLM-based Triton kernel generation has attracted significant interest, yet a fundamental empirical question remains unanswered: where does this capability break down, and why? We present KernelBenchX, a benchmark designed to answer this question through category-aware evaluation of correctness and hardware efficiency across 176 tasks in 15 categories. Our systematic comparison of five representative methods yields three main findings. First, task structure determines correctness more than method design. Category explains nearly three times more variance in semantic correctness than method (9.4% vs 3.3% explained deviance), and 72% of Fusion tasks fail across all five methods while Math tasks are solved consistently. Second, iterative refinement improves correctness, but not performance. Across GEAK iterations, compile rate rises from 52.3% to 68.8% while average speedup declines from $1.58\times$ to $1.44\times$; newly rescued kernels consistently underperform persistently correct ones ($1.16\times$ vs $1.58\times$ speedup in round~0$\to$1). Third, correctness does not imply efficiency. 46.6% of correct kernels are slower than the PyTorch eager baseline, and cross-hardware speedup variance reaches $21.4\times$. Besides, quantization remains completely unsolved (0/30 successes) despite non-trivial compilation rates, revealing systematic misunderstanding of numerical computation contracts rather than surface-level syntax errors. These findings suggest that future progress depends on handling global coordination, explicitly modeling numerical precision, and incorporating hardware efficiency into generation. The code is available at https://github.com/BonnieW05/KernelBenchX
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
标题: An Interpretable Latency Model for Speculative Decoding in LLM Serving
作者: Linghao Kong, Megan Flynn, Michael Peng, Nir Shavit, Mark Kurtz, Alexandre Marques
链接: https://arxiv.org/abs/2605.15051v1
完整摘要: Speculative decoding (SD) accelerates large language model (LLM) inference by using a smaller draft model to propose multiple tokens that are verified by a larger target model in parallel. While prior work demonstrates substantial speedups in isolated or fixed-batch settings, the behavior of SD in production serving systems remains poorly understood: request load varies over time, and effective batch size emerges from the serving system rather than being directly controlled or observed. In this work, we develop a simple and interpretable latency model for SD in LLM serving. We infer effective batch size from request rate using Little's Law and decompose per-request demand into load-independent and load-dependent components for prefill, drafting, and verification. We validate our model using extensive measurements from vLLM across verifier and drafter model sizes, prefill and decode lengths, request rates, draft lengths, and acceptance probabilities. The model accurately describes observed latency, explains why speedups often diminish as server load increases, and characterizes how draft length, acceptance rate, and verifier-drafter size shape latency across serving conditions, with implications for configuring SD in deployed systems. We further show how the framework extends to mixture of experts models, where sparse expert activation changes the effective service costs across load regimes. Together, our results provide a structured framework for understanding SD in real LLM serving systems.
匹配关键词: vLLM
---

[ACADEMIC - ARXIV]
标题: XFP: Quality-Targeted Adaptive Codebook Quantization with Sparse Outlier Separation for LLM Inference
作者: Thomas Witt
链接: https://arxiv.org/abs/2605.14844v1
完整摘要: We introduce XFP, a dynamic weight quantizer for LLM inference that inverts the conventional workflow: the operator specifies reconstruction quality floors on per-channel cosine similarity (one strict floor for attention and shared experts, one lazy floor for routed-expert MoE); XFP determines codebook size, outlier budget, and packing per layer automatically -- no Hessian, no calibration data, no manual bit-width selection. Each weight matrix is decomposed into a sparse fp16 outlier residual and a dense sub-byte index tensor into a per-group learned codebook. Two storage modes share one auto-select frontend and one fused decode kernel: V2 (per-channel Lloyd) and V2a (shared library of L=32 codebooks per layer). On Qwen3.5-122B-A10B under V2, XFP reaches 138 tok/s single-stream decode on workstation hardware (RTX PRO 6000 Blackwell, TP=2) at 94.49% GSM8K strict-match (3 seeds, n=3957), and is 49% faster than Marlin INT4 at TP=1. For models that do not fit in the target memory envelope, we present the H-Process: a quality-driven iteration over the two cosine thresholds that finds the operating point at which the model just fits while still producing sensible output. Three constraints define its search space: the operator-set thresholds, an OOM boundary at quantize-on-load, and a garbage boundary in generation (cosine similarity steers; benches verify). On Qwen3.5-397B-A17B (512 routed experts/layer), the H-Process fits the full expert population into 2x96 GB at ~3.4 effective bits and delivers 100.9 tok/s long-output decode at 66.72% GSM8K strict-match on the full 1319-problem set (single seed at submission; multi-seed evaluation in progress), exceeding INT4 with routed-expert pruning on memory, throughput, and accuracy simultaneously.
匹配关键词: vLLM
---

[ACADEMIC - ARXIV]
标题: BEAM: Binary Expert Activation Masking for Dynamic Routing in MoE
作者: Juntong Wu, Jialiang Cheng, Qishen Yin, Yue Dai, Yuliang Yan, Fuyu Lv, Ou Dan, Li Yuan
链接: https://arxiv.org/abs/2605.14438v1
完整摘要: Mixture-of-Experts (MoE) architectures enhance the efficiency of large language models by activating only a subset of experts per token. However, standard MoE employs a fixed Top-K routing strategy, leading to redundant computation and suboptimal inference latency. Existing acceleration methods either require costly retraining with architectural changes or suffer from severe performance drop at high sparsity due to train-inference mismatch. To address these limitations, we propose BEAM (Binary Expert Activation Masking), a novel method that learns token-adaptive expert selection via trainable binary masks. With a straight-through estimator and an auxiliary regularization loss, BEAM induces dynamic expert sparsity through end-to-end training while maintaining model capability. We further implement an efficient custom CUDA kernel for BEAM, ensuring seamless integration with the vLLM inference framework. Experiments show that BEAM retains over 98\% of the original model's performance while reducing MoE layer FLOPs by up to 85\%, achieving up to 2.5$\times$ faster decoding and 1.4$\times$ higher throughput, demonstrating its effectiveness as a practical, plug-and-play solution for efficient MoE inference.
匹配关键词: vLLM
---

[ACADEMIC - ARXIV]
标题: PreFT: Prefill-only finetuning for efficient inference
作者: Andrew Lanpouthakoun, Aryaman Arora, Zhengxuan Wu, Dhruv Pai, Ben Keigwin, Dan Jurafsky, Christopher Potts
链接: https://arxiv.org/abs/2605.14217v1
完整摘要: Large language models can now be personalised efficiently at scale using parameter efficient finetuning methods (PEFTs), but serving user-specific PEFTs harms throughput, even with specialised kernels and memory management techniques. This is because, theoretically and empirically, a mismatch exists between prefill (processing a large number of tokens at once) and decode (generating a single token autoregressively): the latter has far lower throughput when serving multiple adapters. Rather than optimising performance relative to parameter count, for efficient multi-adapter serving, we instead ought to optimise performance relative to serving throughput. We therefore propose PreFT (Prefill-only Finetuning), wherein we only apply the adapter to prefill tokens and discard it afterwards. PreFT significantly increases throughput with minimal effect on performance. We develop and release an efficient implementation of two prefill-only PEFTs, LoRA and ReFT, on the vLLM inference engine. We first show that serving multi-user PreFTs is more efficient than traditional PEFTs ($1.9\times$ the throughput when serving $512$ adapters on Llama 3.1 70B). Then, we compare the performance of prefill-only vs. all-token adapters on a variety of supervised finetuning and reinforcement learning tasks with LMs at varying scales. On SFT, we observe that the evaluation loss of PreFTs is higher than PEFTs, but can be compensated by increasing rank with nearly no reduction in throughput. On RL, we consistently find that PreFTs approach parity with standard PEFTs. Together, this work validates prefill-only adaptation of LLMs as a more favourable accuracy-throughput tradeoff than existing PEFTs for personalised serving.
匹配关键词: vLLM
---

[ACADEMIC - ARXIV]
标题: Attention Once Is All You Need: Efficient Streaming Inference with Stateful Transformers
作者: Victor Norgren
链接: https://arxiv.org/abs/2605.13784v1
完整摘要: Conventional transformer inference engines are request-driven, paying an O(n) prefill cost on every query. In streaming workloads, where data arrives continuously and queries probe an ever-growing context, this cost is prohibitive. We introduce a data-driven computational model centred on stateful sessions: a persistent KV cache advanced incrementally as new data arrives, so prefill is moved off the critical path and query latency becomes O(|q|), independent of accumulated context size. Building on this, Flash Queries reclaim idle GPU cycles between data arrivals to pre-evaluate registered questions and return cached answers before the user asks, a pattern that is structurally impossible in stateless engines because they discard intermediate state between requests. A multi-tenant continuous-batching scheduler with cell-budget admission and prefix-aware grouped prefill lets dozens of stateful sessions coexist on a single GPU while preserving full quadratic self-attention. On streaming market-data benchmarks the reference implementation achieves up to 5.9x speedup over conventional inference engines (vLLM, SGLang, TensorRT-LLM, llama.cpp), holding query latency constant as accumulated context grows.
匹配关键词: vLLM
---

[ACADEMIC - ARXIV]
标题: Attention Once Is All You Need: Efficient Streaming Inference with Stateful Transformers
作者: Victor Norgren
链接: https://arxiv.org/abs/2605.13784v1
完整摘要: Conventional transformer inference engines are request-driven, paying an O(n) prefill cost on every query. In streaming workloads, where data arrives continuously and queries probe an ever-growing context, this cost is prohibitive. We introduce a data-driven computational model centred on stateful sessions: a persistent KV cache advanced incrementally as new data arrives, so prefill is moved off the critical path and query latency becomes O(|q|), independent of accumulated context size. Building on this, Flash Queries reclaim idle GPU cycles between data arrivals to pre-evaluate registered questions and return cached answers before the user asks, a pattern that is structurally impossible in stateless engines because they discard intermediate state between requests. A multi-tenant continuous-batching scheduler with cell-budget admission and prefix-aware grouped prefill lets dozens of stateful sessions coexist on a single GPU while preserving full quadratic self-attention. On streaming market-data benchmarks the reference implementation achieves up to 5.9x speedup over conventional inference engines (vLLM, SGLang, TensorRT-LLM, llama.cpp), holding query latency constant as accumulated context grows.
匹配关键词: TensorRT
---

[ACADEMIC - ARXIV]
标题: Ada-MK: Adaptive MegaKernel Optimization via Automated DAG-based Search for LLM Inference
作者: Wenxin Dong, Mingqing Hu, Guanghui Yu, Qiang Fu, Peng Xu, Hui Xu, Yue Xing, Xuewu Jiao, Shuanglong Li, Lin Liu
链接: https://arxiv.org/abs/2605.11581v1
完整摘要: When large language models (LLMs) serve real-time inference in commercial online advertising systems, end-to-end latency must be strictly bounded to the millisecond range. Yet every token generated during the decode phase triggers thousands of kernel launches, and kernel launch overhead alone can account for 14.6% of end-to-end inference time. MegaKernel eliminates launch overhead and inter-operator HBM round-trips by fusing multiple operators into a single persistent kernel. However, existing MegaKernel implementations face a fundamental tension between portability and efficiency on resource-constrained GPUs such as NVIDIA Ada: hand-tuned solutions are tightly coupled to specific architectures and lack portability, while auto-compiled approaches introduce runtime dynamic scheduling whose branch penalties are unacceptable in latency-critical settings. We observe that under a fixed deployment configuration, the optimal execution path of a MegaKernel is uniquely determined, and runtime dynamic decision-making can be entirely hoisted to compile time. Building on this insight, we propose Ada-MK: (1) a three-dimensional shared-memory constraint model combined with K-dimension splitting that reduces peak shared memory usage by 50%; (2) MLIR-based fine-grained DAG offline search that solidifies the optimal execution path, completely eliminating runtime branching; and (3) a heterogeneous hybrid inference engine that embeds MegaKernel as a plugin into TensorRT-LLM, combining high-throughput Prefill with low-latency Decode. On an NVIDIA L20, Ada-MK improves single-batch throughput by up to 23.6% over vanilla TensorRT-LLM and 50.2% over vLLM, achieving positive gains across all tested scenarios--the first industrial deployment of MegaKernel in a commercial online advertising system.
匹配关键词: TensorRT
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
标题: DualKV: Shared-Prompt Flash Attention for Efficient RL Training with Large Rollouts and Long Contexts
作者: Jiading Gai, Shuai Zhang, Xiang Song, Bernie Wang, George Karypis
链接: https://arxiv.org/abs/2605.15422v1
完整摘要: Modern RL post-training methods such as GRPO and DAPO train on $N$ response sequences of $R$ tokens sampled from a shared prompt of $P$ tokens, but standard FlashAttention replicates all $P$ prompt tokens $N$ times across both forward and backward passes -- duplicating compute and memory on identical hidden states. In large-rollout, long-context RL training ($N{\geq}16$, $P{\geq}8\text{K}$), this redundancy dominates the policy update cost. We observe that in decoder-only models, causal masking makes prompt representations invariant across sequences at every layer, so all per-token operations (norms, projections, MLP) and attention can process the prompt once -- a property not yet exploited at the kernel level for training. We propose \textbf{DualKV}, the first FlashAttention kernel variant that eliminates shared-prompt replication during RL training, via (1)~fused CUDA forward and backward kernels that iterate over two disjoint KV regions -- shared context and per-sequence response -- in a single kernel launch, and (2)~a data-pipeline redesign in veRL that repacks $N(P{+}R)$ tokens into $P{+}NR$ tokens per micro-batch, extending the token reduction from attention to the entire model by a factor $ρ= N(P{+}R)/(P{+}NR)$. DualKV is mathematically equivalent to standard attention and introduces no approximation. On Qwen3-8B GRPO training with 8$\times$H100 GPUs ($N{=}32$, 8K-context), DualKV achieves $1.63$--$2.09\times$ policy-update speedup, enables $2\times$ larger micro-batches, and raises MFU from $36\%$ to $76\%$. Similar gains hold for DAPO ($2.47\times$ speedup, $77\%$ MFU). At 30B MoE scale on 16$\times$H100, DualKV achieves $3.82\times$ policy-update and $3.38\times$ end-to-end step speedup over FlashAttention (which requires 4-way Ulysses sequence parallelism to avoid OOM).
匹配关键词: CUDA
---

[ACADEMIC - ARXIV]
标题: BEAM: Binary Expert Activation Masking for Dynamic Routing in MoE
作者: Juntong Wu, Jialiang Cheng, Qishen Yin, Yue Dai, Yuliang Yan, Fuyu Lv, Ou Dan, Li Yuan
链接: https://arxiv.org/abs/2605.14438v1
完整摘要: Mixture-of-Experts (MoE) architectures enhance the efficiency of large language models by activating only a subset of experts per token. However, standard MoE employs a fixed Top-K routing strategy, leading to redundant computation and suboptimal inference latency. Existing acceleration methods either require costly retraining with architectural changes or suffer from severe performance drop at high sparsity due to train-inference mismatch. To address these limitations, we propose BEAM (Binary Expert Activation Masking), a novel method that learns token-adaptive expert selection via trainable binary masks. With a straight-through estimator and an auxiliary regularization loss, BEAM induces dynamic expert sparsity through end-to-end training while maintaining model capability. We further implement an efficient custom CUDA kernel for BEAM, ensuring seamless integration with the vLLM inference framework. Experiments show that BEAM retains over 98\% of the original model's performance while reducing MoE layer FLOPs by up to 85\%, achieving up to 2.5$\times$ faster decoding and 1.4$\times$ higher throughput, demonstrating its effectiveness as a practical, plug-and-play solution for efficient MoE inference.
匹配关键词: CUDA
---

[ACADEMIC - ARXIV]
标题: Hierarchical Transformer Preconditioning for Interactive Physics Simulation
作者: Carl Osborne, Minghao Guo, Crystal Owens, Wojciech Matusik
链接: https://arxiv.org/abs/2605.13343v2
完整摘要: Neural preconditioners for real-time physics simulation offer promising data-driven priors, but they often fail to capture long-range couplings efficiently because they inherit local message passing or sparse-operator access patterns. We introduce the Hierarchical Transformer Preconditioner, a neural preconditioner anchored to a weak-admissibility H-matrix partition. The partition provides a multiscale structural prior (dense diagonal leaves plus coarsening off-diagonal tiles) that enables full-graph approximate-inverse computation with O(N) scaling at fixed block sizes. The network models the inverse through low-rank far-field factors and uses highway connections (axial buffers plus a global summary token) to propagate context across transformer depth. At each PCG iteration, preconditioner application reduces to batched dense GEMMs with regular memory access. The key training contribution is a cosine-Hutchinson probe objective that learns the action of MA on convergence-critical spectral subspaces, optimizing angular alignment of MAz with z rather than forcing eigenvalue clusters to a prescribed location. This removes unnecessary spectral-placement constraints from SAI-style objectives and improves conditioning on irregular spectra. Because both inference and apply are dense, dependency-free tensor programs, the full solve loop is captured as a single CUDA Graph. On stiff multiphase Poisson systems (up to 100:1 density contrast, N = 1,024-16,384), the solver runs from ~143 to ~21 fps. At N = 8,192, it reaches 17.9 ms/frame, with 2.2x speedup over GPU Jacobi, ~28x over GPU IC/DILU (AMGX multicolor_dilu), and 2.7x over neural SPAI retrained per scale on the same benchmark.
匹配关键词: CUDA
---

[ACADEMIC - ARXIV]
标题: SCALAR: A Neurosymbolic Framework for Automated Conjecture and Reasoning in Quantum Circuit Analysis
作者: Sean Feeney, Pooja Rao, Andreas Klappenecker, Reuben Tate, Yuri Alexeev, Stefano Mensa, Elica Kyoseva, Stephan Eidenbenz
链接: https://arxiv.org/abs/2605.10327v1
完整摘要: In this paper, we present SCALAR (Symbolic Conjecture and LLM-Assisted Reasoning), a neurosymbolic framework for automated conjecture generation in quantum circuit analysis built on top of the CUDA-Q open source framework. The system integrates quantum simulation, symbolic conjecture generation, and LLM-based interpretation. We evaluate SCALAR on 82 MaxCut instances from the MQLib benchmark dataset and extend the analysis to 2,000 randomly generated graphs across four topologies: regular, Erdos-Renyi, Barabasi-Albert, and Watts-Strogatz. The framework generates conjectured bounds relating optimal QAOA parameters to graph invariants, including known relationships such as periodicity constraints on the phase separation parameter $γ$. SCALAR also recovers previously reported parameter transfer phenomena across structurally similar instances. Additionally, the system identifies correlations between graph structural features and optimization landscape properties, which we characterize through invariant-based descriptors. Using CUDA-Q tensor network simulator, we scale experiments to instances of up to 77 qubits. We discuss the accuracy, generality, and limitations of the generated conjectures, including sensitivity to graph class and quantum circuit depth.
匹配关键词: CUDA
---

[ACADEMIC - ARXIV]
标题: Non-Monotonic Latency in Apple MPS Decoding: KV Cache Interactions and Execution Regimes
作者: Willy Fitra Hendria
链接: https://arxiv.org/abs/2605.08913v2
完整摘要: Autoregressive inference is typically assumed to scale predictably with decoding length, with latency increasing smoothly as generated sequence length grows. In this work, we identify unexpected non-monotonic latency behavior in the Apple MPS backend, where latency changes abruptly across nearby decoding configurations during transformer decoding. Using multiple model families (GPT-2, BLOOM, and OPT), we observe latency spikes of up to 21x within specific decoding-budget intervals, followed by recovery at neighboring configurations. Controlled experiments show that these anomalies originate primarily during the decode phase rather than prefill, are not explained by memory pressure alone, and remain absent on CPU and NVIDIA CUDA backends under identical conditions. We further show that key-value (KV) cache interacts strongly with these pathological execution regimes: KV caching remains beneficial overall, but its practical speedup collapses sharply within anomalous configurations, while cache-disabled decoding still exhibits residual non-monotonic behavior. These findings suggest that autoregressive decoding on MPS enters discrete execution regimes that are not captured by coarse-grained benchmarking, highlighting the importance of hardware-aware evaluation for long-context inference.
匹配关键词: CUDA
---

[ACADEMIC - ARXIV]
标题: IVGT: Implicit Visual Geometry Transformer for Neural Scene Representation
作者: Yuqi Wu, Tianyu Hu, Wenzhao Zheng, Yuanhui Huang, Haowen Sun, Jie Zhou, Jiwen Lu
链接: https://arxiv.org/abs/2605.16258v1
完整摘要: Reconstructing coherent 3D geometry and appearance from unposed multi-view images is a fundamental yet challenging problem in computer vision. Most existing visual geometry foundation models predict explicit geometry by regressing pixel-aligned pointmaps, often suffering from redundancy and limited geometric continuity. We propose IVGT, an Implicit Visual Geometry Transformer that implicitly models continuous and coherent geometry from pose-free multi-view images. This formulation learns a continuous neural scene representation in a canonical coordinate system and supports continuous spatial queries at any 3D positions, retrieving local features to predict signed distance (SDF) values and colors using lightweight decoders. It allows direct extraction of continuous and coherent surface geometry, enabling rendering of RGB images, depth maps, and surface normal maps from arbitrary viewpoints. We train IVGT via multi-dataset joint optimization with 2D supervision and 3D geometric regularization. IVGT demonstrates generalization across scenes and achieves strong performance on various tasks, including mesh and point cloud reconstruction, novel view synthesis, depth and surface normal estimation, and camera pose estimation.
匹配关键词: distributed training
---

[ACADEMIC - ARXIV]
标题: DexJoCo: A Benchmark and Toolkit for Task-Oriented Dexterous Manipulation on MuJoCo
作者: Hanwen Wang, Weizhi Zhao, Xiangyu Wang, Siyuan Huang, He Lin, Boyuan Zheng, Rongtao Xu, Gang Wang, Yao Mu, He Wang, Lue Fan, Hongsheng Li, Zhaoxiang Zhang, Tieniu Tan
链接: https://arxiv.org/abs/2605.16257v1
完整摘要: Achieving human-level manipulation requires dexterous robotic hands capable of complex object interactions. Advancing such capabilities further demands standardized benchmarks for systematic evaluation. However, existing dexterous benchmarks lack tasks that reflect the unique manipulation capabilities of dexterous hands over parallel grippers, as well as comprehensive evaluation pipelines. In this paper, we present DexJoCo, a benchmark and toolkit for task-oriented dexterous manipulation, comprising 11 functionally grounded tasks that evaluate tool-use, bimanual coordination, long-horizon execution, and reasoning. We develop a low-cost data collection system and collect 1.1K trajectories across these tasks, with support for domain randomization to assess robustness. We benchmark modern models under diverse settings, including visual and dynamics randomization, multi-task training, and action-head adaptation. Through extensive empirical analysis, we identify several important insights and common limitations of current policies in dexterous manipulation, highlighting key challenges for future research in dexterous hand robot learning. Project page available at: https://dexjoco.github.io
匹配关键词: distributed training
---

[ACADEMIC - ARXIV]
标题: Designing Datacenter Power Delivery Hierarchies for the AI Era
作者: Grant Wilkins, Fiodar Kazhamiaka, Alok Gautam Kumbhare, Chaojie Zhang, Ricardo Bianchini
链接: https://arxiv.org/abs/2605.16255v1
完整摘要: Demand for AI accelerators is rapidly increasing rack power density, with projections approaching 1MW per deployment by 2027. This poses a major challenge for datacenter power delivery designers. As power densities increase, a datacenter designed for a different target density may strand power, i.e., may be unable to use all the power that its delivery hierarchy has provisioned. Designs must remain efficient over long datacenter lifetimes and multiple hardware generations. Power utilization is particularly important as grid power capacity is a scarce resource in the AI era. Designing an efficient power delivery hierarchy for the long run is difficult because rack placement feasibility, workload impact, and cost depend jointly on electrical topology, deployment granularity, placement policy, power oversubscription, and workload mix. Moreover, each of these factors evolve over time, have inter-dependencies across multiple resource dimensions, and generally do not lend themselves to closed-form analysis. To address this challenge, we develop a framework for evaluating datacenter power delivery designs using throughput, power, and cost metrics over realistic arrival, oversubscription, and decommissioning sequences. The framework combines projection models for GPU, compute, and storage deployments with operational factors grounded in production data from Microsoft Azure. Our results show that multi-resource stranding materially changes deployable capacity, effective capital expenditure, and delivered performance, and quantify how rising density from rack- and pod-scale AI systems shapes these outcomes. For AI datacenter design, the relevant planning objective is not installed megawatts, but deployable capacity over time.
匹配关键词: distributed training
---

[ACADEMIC - ARXIV]
标题: A Generative AI Framework for Intelligent Utility Billing CO 2 Analytics and Sustainable Resource Optimisation
作者: Pavan Manjunath, Thomas Pruefer
链接: https://arxiv.org/abs/2605.16250v1
完整摘要: Distribution utilities are now expected to deliver bills that customers can actually read attach a defensible carbon number to every kWh sold and schedule load against grid stress and emissions constraints We propose an end-to-end framework that unifies four production-grade capabilities under one architectural roof a generative-AI agent that drafts each customers natural-language billing statement from structured numeric inputs under a constrained decoding policy a transformer-based forecaster that supplies the day-ahead consumption estimate with calibrated quantile bands
匹配关键词: distributed training
---

[ACADEMIC - ARXIV]
标题: Offline Semantic Guidance for Efficient Vision-Language-Action Policy Distillation
作者: Jin Shi, Brady Zhang, Yishun Lu
链接: https://arxiv.org/abs/2605.16241v1
完整摘要: Billion-parameter Vision-Language-Action (VLA) policies have recently shown impressive performance in robotic manipulation, yet their size and inference cost remain major obstacles for real-time closed-loop control. We introduce \textbf{VLA-AD}, a distillation framework that uses a Vision-Language Model as an offline semantic supervisor to transfer large VLA teachers into lightweight student policies. Instead of relying only on low-level action imitation, VLA-AD augments teacher-provided 7-DoF action targets with high-level semantic guidance, including task phase anchors and multi-frame operating-direction descriptions. These auxiliary signals are used only during training: at test time, the student policy runs independently, with neither the VLA teacher nor the VLM required. We evaluate VLA-AD on three LIBERO benchmark suites. Using OpenVLA-7B as the teacher, our method produces a 158M-parameter student, yielding a $44\times$ reduction in model size while matching the teacher with only a $0.27\%$ average relative gap. The resulting policy runs at 12.5 Hz on an RTX 4090, achieving a $3.28\times$ inference speedup over OpenVLA-7B. We further show that the same semantic distillation pipeline generalizes to a different $π_{0.5}$-4B teacher, where the student outperforms the teacher on two suites and remains within $0.53\%$ on \texttt{libero\_goal}. Additional analysis indicates that phase-level supervision and multi-frame directional cues make the student less sensitive to noisy teacher actions, such as erroneous high-frequency gripper changes. Overall, VLA-AD demonstrates that offline semantic guidance from VLMs can substantially improve the efficiency, robustness, and deployability of VLA policy distillation.
匹配关键词: distributed training
---

[ACADEMIC - ARXIV]
标题: IVGT: Implicit Visual Geometry Transformer for Neural Scene Representation
作者: Yuqi Wu, Tianyu Hu, Wenzhao Zheng, Yuanhui Huang, Haowen Sun, Jie Zhou, Jiwen Lu
链接: https://arxiv.org/abs/2605.16258v1
完整摘要: Reconstructing coherent 3D geometry and appearance from unposed multi-view images is a fundamental yet challenging problem in computer vision. Most existing visual geometry foundation models predict explicit geometry by regressing pixel-aligned pointmaps, often suffering from redundancy and limited geometric continuity. We propose IVGT, an Implicit Visual Geometry Transformer that implicitly models continuous and coherent geometry from pose-free multi-view images. This formulation learns a continuous neural scene representation in a canonical coordinate system and supports continuous spatial queries at any 3D positions, retrieving local features to predict signed distance (SDF) values and colors using lightweight decoders. It allows direct extraction of continuous and coherent surface geometry, enabling rendering of RGB images, depth maps, and surface normal maps from arbitrary viewpoints. We train IVGT via multi-dataset joint optimization with 2D supervision and 3D geometric regularization. IVGT demonstrates generalization across scenes and achieves strong performance on various tasks, including mesh and point cloud reconstruction, novel view synthesis, depth and surface normal estimation, and camera pose estimation.
匹配关键词: GPU optimization
---

[ACADEMIC - ARXIV]
标题: Designing Datacenter Power Delivery Hierarchies for the AI Era
作者: Grant Wilkins, Fiodar Kazhamiaka, Alok Gautam Kumbhare, Chaojie Zhang, Ricardo Bianchini
链接: https://arxiv.org/abs/2605.16255v1
完整摘要: Demand for AI accelerators is rapidly increasing rack power density, with projections approaching 1MW per deployment by 2027. This poses a major challenge for datacenter power delivery designers. As power densities increase, a datacenter designed for a different target density may strand power, i.e., may be unable to use all the power that its delivery hierarchy has provisioned. Designs must remain efficient over long datacenter lifetimes and multiple hardware generations. Power utilization is particularly important as grid power capacity is a scarce resource in the AI era. Designing an efficient power delivery hierarchy for the long run is difficult because rack placement feasibility, workload impact, and cost depend jointly on electrical topology, deployment granularity, placement policy, power oversubscription, and workload mix. Moreover, each of these factors evolve over time, have inter-dependencies across multiple resource dimensions, and generally do not lend themselves to closed-form analysis. To address this challenge, we develop a framework for evaluating datacenter power delivery designs using throughput, power, and cost metrics over realistic arrival, oversubscription, and decommissioning sequences. The framework combines projection models for GPU, compute, and storage deployments with operational factors grounded in production data from Microsoft Azure. Our results show that multi-resource stranding materially changes deployable capacity, effective capital expenditure, and delivered performance, and quantify how rising density from rack- and pod-scale AI systems shapes these outcomes. For AI datacenter design, the relevant planning objective is not installed megawatts, but deployable capacity over time.
匹配关键词: GPU optimization
---

[ACADEMIC - ARXIV]
标题: Prospective multi-pathogen disease forecasting using autonomous LLM-guided tree search
作者: Sarah Martinson, Michael P. Brenner, Martyna Plomecka, Brian P. Williams, Nicholas G. Reich, Zahra Shamsi
链接: https://arxiv.org/abs/2605.16238v1
完整摘要: Probabilistic forecasting of infectious diseases is crucial for public health but relies on labor-intensive manual model curation by expert modeling teams. This bespoke development bottlenecks scalability to granular geographic resolutions or emerging pathogens. Here, we present an autonomous system using Large Language Model (LLM)-guided tree search to iteratively generate, evaluate, and optimize executable forecasting software. In a fully prospective, real-time evaluation during the 2025-2026 US respiratory season, the system autonomously discovered methodologically diverse models for influenza, COVID-19, and respiratory syncytial virus (RSV). Aggregating these machine-generated models yielded an ensemble that consistently matched or outperformed the gold-standard, human-curated Centers for Disease Control and Prevention (CDC) hub ensembles out-of-sample. The system successfully navigated data-scarce "cold start" scenarios for RSV. Moreover, controlled retrospective ablations revealed that optimizing log-scale distance metrics prevents reward hacking, while an automated judge-in-the-loop ensures structural fidelity to complex scientific theories. By autonomously translating epidemiological theory into accurate, transparent code, this framework overcomes the modeling labor bottleneck, enabling rapid deployment of expert-level disease forecasting at unprecedented scales.
匹配关键词: GPU optimization
---

[ACADEMIC - ARXIV]
标题: FORGE: Self-Evolving Agent Memory With No Weight Updates via Population Broadcast
作者: Igor Bogdanov, Chung-Horng Lung, Thomas Kunz, Jie Gao, Adrian Taylor, Marzia Zaman
链接: https://arxiv.org/abs/2605.16233v1
完整摘要: Can LLM agents improve decision-making through self-generated memory without gradient updates? We propose FORGE (Failure-Optimized Reflective Graduation and Evolution), a staged, population-based protocol that evolves prompt-injected natural-language memory for hierarchical ReAct agents. FORGE wraps a Reflexion-style inner loop, where a dedicated reflection agent (using the same underlying LLM, no distillation from a stronger model) converts failed trajectories into reusable knowledge artifacts: textual heuristics (Rules), few-shot demonstrations (Examples), or both (Mixed), with an outer loop that propagates the best-performing instance's memory to the population between stages and freezes converged instances via a graduation criterion. We evaluate on CybORG CAGE-2, a stochastic network-defense POMDP at a 30-step horizon against the B-line attacker, where all four tested LLM families (Gemini-2.5-Flash-Lite, Grok-4-Fast, Llama-4-Maverick, Qwen3-235B) exhibit strongly negative, heavy-tailed zero-shot rewards. Compared against both a zero-shot baseline and a Reflexion baseline (isolated single-stream learning), FORGE improves average evaluation return by 1.7-7.7$\times$ over zero-shot and by 29-72% over Reflexion in all 12 model-representation conditions, reducing major-failure rates (below $-100$) to as low as $\sim$1%. We find that (1) population broadcast is critical mechanism, with a no-graduation ablation confirming that broadcast carries the performance gains while graduation primarily saves compute; (2) Examples achieves the strongest returns for three of four models, Rules offers the best cost-reliability profile with $\sim$40% fewer tokens; and (3) weaker baseline models benefit disproportionately, suggesting FORGE may mitigate capability gaps rather than amplify strong models. All evidence is confined to CAGE-2 B-line; cross-family findings are directional evidence.
匹配关键词: GPU optimization
---

[ACADEMIC - ARXIV]
标题: The Privacy Price of Tail-Risk Learning: Effective Tail Sample Size in Differentially Private CVaR Optimization
作者: El Mustapha Mansouri
链接: https://arxiv.org/abs/2605.16219v1
完整摘要: Differential privacy changes the effective sample size governing CVaR learning. For tail mass $τ$, the privacy-relevant sample size is not $n$, but $nτ$; equivalently, the effective private tail sample size is $εnτ$. Private CVaR excess risk decomposes into ordinary tail-risk statistical error and a privacy price. This decomposition is complete for scalar estimation and finite classes: scalar estimation has rate $Θ(B \min\{1,(nτ)^{-1/2}+(εnτ)^{-1}\})$, and finite classes of size $M$ have rate $Θ(B \min\{1,\sqrt{\log(2M)/(nτ)}+\log(2M)/(εnτ)\})$. These complete rates hold under pure DP, and their lower bounds extend to approximate DP in the stated small-$δ$ regimes. For convex Lipschitz learning, modular upper and lower reductions show that the CVaR-specific privacy term necessarily scales as $1/(εnτ)$, with dimension dependence inherited from private stochastic convex optimization. Together, these results identify ordinary private learning on $Θ(nτ)$ informative tail records as the canonical hard subproblem inside private CVaR learning.
匹配关键词: GPU optimization
---

[ACADEMIC - ARXIV]
标题: Multi-level Self-supervised Pretraining on Compositional Hierarchical Graph for Molecular Property Prediction
作者: Xiayu Liu, Zhengyi Lu, Hou-biao Li
链接: https://arxiv.org/abs/2605.16088v1
完整摘要: Self-supervised pretraining on molecular graphs has emerged as a promising approach for molecular property prediction, yet most existing methods operate at a single structural granularity and treat bond information as auxiliary edge attributes rather than as an independent semantic layer. In this work, we propose MolCHG, a multi-level self-supervised pretraining framework built upon a novel Compositional Hierarchical Graph that organizes molecular structure into four types of nodes across three semantic levels. By introducing a bond graph that operates in parallel with the atom graph, our architecture elevates bond-level information to independently evolving node representations, enabling fragment nodes to aggregate atom-level and bond-level semantics on an equal footing. We design three level-specific pretraining objectives: an atom-bond cross-view contrastive task that aligns the atom-view and bond-view representations within each fragment, a fragment-level functional group prediction task to inject domain-relevant chemical knowledge, and graph-level structure prediction tasks to encode global molecular topology. Experiments on nine MoleculeNet benchmarks demonstrate that MolCHG achieves the best performance on seven datasets across both classification and regression tasks, remaining competitive with the strongest baselines on the rest. Ablation studies further confirm that the multi-level supervision signals are complementary and that each component contributes to the overall performance.
匹配关键词: self-supervised
---

[ACADEMIC - ARXIV]
标题: ITGPT: Generative Pretraining on Irregular Timeseries
作者: Antoine Honoré, Ming Xiao
链接: https://arxiv.org/abs/2605.16069v1
完整摘要: Timeseries regression models often struggle to leverage large volumes of labeled multimodal data, particularly when the data are irregularly sampled or contain missing values. This is common in domains like healthcare and predictive maintenance, where data are collected from unreliable sources, and labeling requires expert knowledge or costly equipments. Transformer-based large language models have proven effective on structured data such as text through self-supervised learning (SSL) and generative pretraining (GPT) frameworks. However, such models lack the flexibility to efficiently process irregularly sampled multimodal timeseries data. In this paper, we introduce ITGPT, an attention-based architecture designed for handling multimodal, irregularly sampled timeseries by allowing training with both SSL losses and GPT-like objectives. We evaluate its performance on a healthcare task with the TIHM dataset, and a predictive maintenance task with the CompX dataset. Our results demonstrate that ITGPT achieves state-of-the-art performance without requiring resampling, feature fusion or explicit data imputation. Furthermore, when labels are scarce, ITGPT effectively leverages unlabeled data through SSL and GPT training, outperforming the purely supervised approach. This represents an important step towards efficiently using large and unstructured timeseries datasets for practical inference tasks.
匹配关键词: self-supervised
---

[ACADEMIC - ARXIV]
标题: SOLAR: Self-supervised Joint Learning for Symmetric Multimodal Retrieval
作者: Wenjie Yang, Hang Yu, Yuyu Guo, Peng Di
链接: https://arxiv.org/abs/2605.15868v1
完整摘要: In this work, we address the critical yet underexplored challenge of symmetric multimodal-to-multimodal (MM2MM) retrieval, where queries and contexts are interchangeable. Existing universal multimodal retrieval works struggle with this task, as they are constrained by the labeled asymmetric datasets used. We produce SOLAR (Self-supervised jOint LeArning for symmetric multimodal Retrieval), a novel two-stage self-supervised framework that leverages readily available unlabeled web-scale image-text pairs. Based on the observation that both semantic alignment and discrepancies exist between two modalities, in the first stage, we learn the intersection mask of image-text pair, allowing us to align intersection while preserving semantic of difference. In the second stage, the learned mask is further utilized to construct positive and hardnegative samples via masking different parts of image/text, which enable us to conduct self-supervised multimodal embedding learning. Complementing this framework, we present a new benchmark featuring high-quality human-verified positive and hard-negative pairs to evaluate symmetric MM2MM retrieval under realistic conditions, as well as the corresponding pipeline. Extensive experiments against ten SOTA methods show SOLAR surpasses the strongest supervised VLM by 7.08 points on this benchmark, with over 50x fewer model parameters and a 5x smaller embedding dimension. Code and benchmark will be available soon.
匹配关键词: self-supervised
---

[ACADEMIC - ARXIV]
标题: Structure Abstraction and Generalization in a Hippocampal-Entorhinal Inspired World Model
作者: Tianqiu Zhang, Muyang Lyu, Xiao Liu, Si Wu
链接: https://arxiv.org/abs/2605.15733v1
完整摘要: Humans abstract experiences into structured representations to facilitate pattern inference and knowledge transfer. While the hippocampal-entorhinal (HPC-MEC) circuit is known to represent both spatial and conceptual spaces, the mechanisms for concurrently extracting abstract structures from continuous, high-dimensional dynamics remain poorly understood. We propose a brain-inspired hierarchical model that simultaneously infers latent transitions and constructs a predictive visual world model. Our architecture employs an inverse model for structural extraction alongside an HPC-MEC coupling model that dissociates relational structures (MEC) from integrated episodic scenes (HPC). Using primitive transformation dynamics as a benchmark, we demonstrate the model's capacity for structural abstraction. By leveraging velocity-driven path integration, the framework enables robust prediction and structural reuse across diverse contexts, thereby achieving structural generalization. This work provides a novel computational framework for understanding how brain-inspired, self-supervised learning of world models facilitates the acquisition of reusable abstract knowledge.
匹配关键词: self-supervised
---

[ACADEMIC - ARXIV]
标题: DiLA: Disentangled Latent Action World Models
作者: Tianqiu Zhang, Muyang Lyu, Yufan Zhang, Fang Fang, Si Wu
链接: https://arxiv.org/abs/2605.15725v1
完整摘要: Latent Action Models (LAMs) enable the learning of world models from unlabeled video by inferring abstract actions between consecutive frames. However, LAMs face a fundamental trade-off between action abstraction and generation fidelity. Existing methods typically circumvent this issue by using two-stage training with pre-trained world models or by limiting predictions to optical flow. In this paper, we introduce DiLA, a novel Disentangled Latent Action world model that aims to resolve this trade-off via content-structure disentanglement. Our key insight is that disentanglement and latent action learning are co-evolving: the predictive bottleneck inherent in latent action learning serves as a driving force for disentanglement, compelling the model to distill spatial layouts into the structure pathway while offloading visual details to a separate content pathway for generation. This synergy yields a continuous, semantically structured latent action space without compromising generative quality. DiLA achieves superior results in video generation quality, action transfer, visual planning, and manifold interpretability. These findings establish DiLA as a unified framework that simultaneously achieves high-level action abstraction and high-fidelity generation, advancing the frontier of self-supervised world model learning.
匹配关键词: self-supervised
---

[ACADEMIC - ARXIV]
标题: IVGT: Implicit Visual Geometry Transformer for Neural Scene Representation
作者: Yuqi Wu, Tianyu Hu, Wenzhao Zheng, Yuanhui Huang, Haowen Sun, Jie Zhou, Jiwen Lu
链接: https://arxiv.org/abs/2605.16258v1
完整摘要: Reconstructing coherent 3D geometry and appearance from unposed multi-view images is a fundamental yet challenging problem in computer vision. Most existing visual geometry foundation models predict explicit geometry by regressing pixel-aligned pointmaps, often suffering from redundancy and limited geometric continuity. We propose IVGT, an Implicit Visual Geometry Transformer that implicitly models continuous and coherent geometry from pose-free multi-view images. This formulation learns a continuous neural scene representation in a canonical coordinate system and supports continuous spatial queries at any 3D positions, retrieving local features to predict signed distance (SDF) values and colors using lightweight decoders. It allows direct extraction of continuous and coherent surface geometry, enabling rendering of RGB images, depth maps, and surface normal maps from arbitrary viewpoints. We train IVGT via multi-dataset joint optimization with 2D supervision and 3D geometric regularization. IVGT demonstrates generalization across scenes and achieves strong performance on various tasks, including mesh and point cloud reconstruction, novel view synthesis, depth and surface normal estimation, and camera pose estimation.
匹配关键词: contrastive learning
---

[ACADEMIC - ARXIV]
标题: DexJoCo: A Benchmark and Toolkit for Task-Oriented Dexterous Manipulation on MuJoCo
作者: Hanwen Wang, Weizhi Zhao, Xiangyu Wang, Siyuan Huang, He Lin, Boyuan Zheng, Rongtao Xu, Gang Wang, Yao Mu, He Wang, Lue Fan, Hongsheng Li, Zhaoxiang Zhang, Tieniu Tan
链接: https://arxiv.org/abs/2605.16257v1
完整摘要: Achieving human-level manipulation requires dexterous robotic hands capable of complex object interactions. Advancing such capabilities further demands standardized benchmarks for systematic evaluation. However, existing dexterous benchmarks lack tasks that reflect the unique manipulation capabilities of dexterous hands over parallel grippers, as well as comprehensive evaluation pipelines. In this paper, we present DexJoCo, a benchmark and toolkit for task-oriented dexterous manipulation, comprising 11 functionally grounded tasks that evaluate tool-use, bimanual coordination, long-horizon execution, and reasoning. We develop a low-cost data collection system and collect 1.1K trajectories across these tasks, with support for domain randomization to assess robustness. We benchmark modern models under diverse settings, including visual and dynamics randomization, multi-task training, and action-head adaptation. Through extensive empirical analysis, we identify several important insights and common limitations of current policies in dexterous manipulation, highlighting key challenges for future research in dexterous hand robot learning. Project page available at: https://dexjoco.github.io
匹配关键词: contrastive learning
---

[ACADEMIC - ARXIV]
标题: A Generative AI Framework for Intelligent Utility Billing CO 2 Analytics and Sustainable Resource Optimisation
作者: Pavan Manjunath, Thomas Pruefer
链接: https://arxiv.org/abs/2605.16250v1
完整摘要: Distribution utilities are now expected to deliver bills that customers can actually read attach a defensible carbon number to every kWh sold and schedule load against grid stress and emissions constraints We propose an end-to-end framework that unifies four production-grade capabilities under one architectural roof a generative-AI agent that drafts each customers natural-language billing statement from structured numeric inputs under a constrained decoding policy a transformer-based forecaster that supplies the day-ahead consumption estimate with calibrated quantile bands
匹配关键词: contrastive learning
---

[ACADEMIC - ARXIV]
标题: AI-Mediated Communication Can Steer Collective Opinion
作者: Stratis Tsirtsis, Kai Rawal, Chris Russell, Brent Mittelstadt, Sandra Wachter
链接: https://arxiv.org/abs/2605.16245v1
完整摘要: Generative artificial intelligence (AI) is increasingly integrated into the online platforms where humans exchange opinions; large language models (LLMs) now polish users' posts on LinkedIn and provide context for content shared on X. While prior work has shown that AI can express biased opinions and shape individuals' opinions during human-AI interactions, less attention has been paid to its influence on collective opinion formation when mediating human-to-human communication. We address this gap via a combination of empirical and theoretical analyses. We show empirically that LLMs from multiple popular families introduce directional biases when instructed to edit human-written texts on contested topics, for example, nudging texts in favor of gun control and against atheism. Building on this observation, we introduce a mathematical model of opinion dynamics in which an AI system sits between users on a social network, transforming the opinions they express and perceive. By analytically characterizing the equilibrium of this model and performing simulations on real social network data, we show that biases introduced by AI in human-to-human communication can be amplified through the network and shift collective opinion in their direction. In light of these findings, we investigate whether such biases are controllable by online platforms. We audit the "Explain this post" feature on X and find evidence of pro-life bias in Grok's outputs on abortion-related content, which we trace back to specific design choices. We conclude with a discussion of the broader implications of our findings in relation to ongoing legislative efforts in the European Union.
匹配关键词: contrastive learning
---

[ACADEMIC - ARXIV]
标题: Dynamics-Level Watermarking of Flow Matching Models with Random Codes
作者: Shuchan Wang
链接: https://arxiv.org/abs/2605.16239v1
完整摘要: We introduce a dynamics-level approach to watermarking generative models. Rather than embedding signals into model weights or outputs, we embed the watermark directly into the learned continuous dynamics -- the velocity field of a flow matching model. We formulate this as random coding over a continuous channel: a key-dependent perturbation is added during training, and the message is recovered at detection time from black-box queries. The perturbation is designed to leave the generated distribution unchanged. Experiments on MNIST and CIFAR-10 across different architectures confirm reliable message recovery, preserved generation quality, and chance-level decoding accuracy without the secret key.
匹配关键词: contrastive learning
---

[ACADEMIC - ARXIV]
标题: IVGT: Implicit Visual Geometry Transformer for Neural Scene Representation
作者: Yuqi Wu, Tianyu Hu, Wenzhao Zheng, Yuanhui Huang, Haowen Sun, Jie Zhou, Jiwen Lu
链接: https://arxiv.org/abs/2605.16258v1
完整摘要: Reconstructing coherent 3D geometry and appearance from unposed multi-view images is a fundamental yet challenging problem in computer vision. Most existing visual geometry foundation models predict explicit geometry by regressing pixel-aligned pointmaps, often suffering from redundancy and limited geometric continuity. We propose IVGT, an Implicit Visual Geometry Transformer that implicitly models continuous and coherent geometry from pose-free multi-view images. This formulation learns a continuous neural scene representation in a canonical coordinate system and supports continuous spatial queries at any 3D positions, retrieving local features to predict signed distance (SDF) values and colors using lightweight decoders. It allows direct extraction of continuous and coherent surface geometry, enabling rendering of RGB images, depth maps, and surface normal maps from arbitrary viewpoints. We train IVGT via multi-dataset joint optimization with 2D supervision and 3D geometric regularization. IVGT demonstrates generalization across scenes and achieves strong performance on various tasks, including mesh and point cloud reconstruction, novel view synthesis, depth and surface normal estimation, and camera pose estimation.
匹配关键词: representation learning
---

[ACADEMIC - ARXIV]
标题: DexJoCo: A Benchmark and Toolkit for Task-Oriented Dexterous Manipulation on MuJoCo
作者: Hanwen Wang, Weizhi Zhao, Xiangyu Wang, Siyuan Huang, He Lin, Boyuan Zheng, Rongtao Xu, Gang Wang, Yao Mu, He Wang, Lue Fan, Hongsheng Li, Zhaoxiang Zhang, Tieniu Tan
链接: https://arxiv.org/abs/2605.16257v1
完整摘要: Achieving human-level manipulation requires dexterous robotic hands capable of complex object interactions. Advancing such capabilities further demands standardized benchmarks for systematic evaluation. However, existing dexterous benchmarks lack tasks that reflect the unique manipulation capabilities of dexterous hands over parallel grippers, as well as comprehensive evaluation pipelines. In this paper, we present DexJoCo, a benchmark and toolkit for task-oriented dexterous manipulation, comprising 11 functionally grounded tasks that evaluate tool-use, bimanual coordination, long-horizon execution, and reasoning. We develop a low-cost data collection system and collect 1.1K trajectories across these tasks, with support for domain randomization to assess robustness. We benchmark modern models under diverse settings, including visual and dynamics randomization, multi-task training, and action-head adaptation. Through extensive empirical analysis, we identify several important insights and common limitations of current policies in dexterous manipulation, highlighting key challenges for future research in dexterous hand robot learning. Project page available at: https://dexjoco.github.io
匹配关键词: representation learning
---

[ACADEMIC - ARXIV]
标题: A Generative AI Framework for Intelligent Utility Billing CO 2 Analytics and Sustainable Resource Optimisation
作者: Pavan Manjunath, Thomas Pruefer
链接: https://arxiv.org/abs/2605.16250v1
完整摘要: Distribution utilities are now expected to deliver bills that customers can actually read attach a defensible carbon number to every kWh sold and schedule load against grid stress and emissions constraints We propose an end-to-end framework that unifies four production-grade capabilities under one architectural roof a generative-AI agent that drafts each customers natural-language billing statement from structured numeric inputs under a constrained decoding policy a transformer-based forecaster that supplies the day-ahead consumption estimate with calibrated quantile bands
匹配关键词: representation learning
---

[ACADEMIC - ARXIV]
标题: AI-Mediated Communication Can Steer Collective Opinion
作者: Stratis Tsirtsis, Kai Rawal, Chris Russell, Brent Mittelstadt, Sandra Wachter
链接: https://arxiv.org/abs/2605.16245v1
完整摘要: Generative artificial intelligence (AI) is increasingly integrated into the online platforms where humans exchange opinions; large language models (LLMs) now polish users' posts on LinkedIn and provide context for content shared on X. While prior work has shown that AI can express biased opinions and shape individuals' opinions during human-AI interactions, less attention has been paid to its influence on collective opinion formation when mediating human-to-human communication. We address this gap via a combination of empirical and theoretical analyses. We show empirically that LLMs from multiple popular families introduce directional biases when instructed to edit human-written texts on contested topics, for example, nudging texts in favor of gun control and against atheism. Building on this observation, we introduce a mathematical model of opinion dynamics in which an AI system sits between users on a social network, transforming the opinions they express and perceive. By analytically characterizing the equilibrium of this model and performing simulations on real social network data, we show that biases introduced by AI in human-to-human communication can be amplified through the network and shift collective opinion in their direction. In light of these findings, we investigate whether such biases are controllable by online platforms. We audit the "Explain this post" feature on X and find evidence of pro-life bias in Grok's outputs on abortion-related content, which we trace back to specific design choices. We conclude with a discussion of the broader implications of our findings in relation to ongoing legislative efforts in the European Union.
匹配关键词: representation learning
---

[ACADEMIC - ARXIV]
标题: Dynamics-Level Watermarking of Flow Matching Models with Random Codes
作者: Shuchan Wang
链接: https://arxiv.org/abs/2605.16239v1
完整摘要: We introduce a dynamics-level approach to watermarking generative models. Rather than embedding signals into model weights or outputs, we embed the watermark directly into the learned continuous dynamics -- the velocity field of a flow matching model. We formulate this as random coding over a continuous channel: a key-dependent perturbation is added during training, and the message is recovered at detection time from black-box queries. The perturbation is designed to leave the generated distribution unchanged. Experiments on MNIST and CIFAR-10 across different architectures confirm reliable message recovery, preserved generation quality, and chance-level decoding accuracy without the secret key.
匹配关键词: representation learning
---

[ACADEMIC - ARXIV]
标题: IVGT: Implicit Visual Geometry Transformer for Neural Scene Representation
作者: Yuqi Wu, Tianyu Hu, Wenzhao Zheng, Yuanhui Huang, Haowen Sun, Jie Zhou, Jiwen Lu
链接: https://arxiv.org/abs/2605.16258v1
完整摘要: Reconstructing coherent 3D geometry and appearance from unposed multi-view images is a fundamental yet challenging problem in computer vision. Most existing visual geometry foundation models predict explicit geometry by regressing pixel-aligned pointmaps, often suffering from redundancy and limited geometric continuity. We propose IVGT, an Implicit Visual Geometry Transformer that implicitly models continuous and coherent geometry from pose-free multi-view images. This formulation learns a continuous neural scene representation in a canonical coordinate system and supports continuous spatial queries at any 3D positions, retrieving local features to predict signed distance (SDF) values and colors using lightweight decoders. It allows direct extraction of continuous and coherent surface geometry, enabling rendering of RGB images, depth maps, and surface normal maps from arbitrary viewpoints. We train IVGT via multi-dataset joint optimization with 2D supervision and 3D geometric regularization. IVGT demonstrates generalization across scenes and achieves strong performance on various tasks, including mesh and point cloud reconstruction, novel view synthesis, depth and surface normal estimation, and camera pose estimation.
匹配关键词: masked language model
---

[ACADEMIC - ARXIV]
标题: DexJoCo: A Benchmark and Toolkit for Task-Oriented Dexterous Manipulation on MuJoCo
作者: Hanwen Wang, Weizhi Zhao, Xiangyu Wang, Siyuan Huang, He Lin, Boyuan Zheng, Rongtao Xu, Gang Wang, Yao Mu, He Wang, Lue Fan, Hongsheng Li, Zhaoxiang Zhang, Tieniu Tan
链接: https://arxiv.org/abs/2605.16257v1
完整摘要: Achieving human-level manipulation requires dexterous robotic hands capable of complex object interactions. Advancing such capabilities further demands standardized benchmarks for systematic evaluation. However, existing dexterous benchmarks lack tasks that reflect the unique manipulation capabilities of dexterous hands over parallel grippers, as well as comprehensive evaluation pipelines. In this paper, we present DexJoCo, a benchmark and toolkit for task-oriented dexterous manipulation, comprising 11 functionally grounded tasks that evaluate tool-use, bimanual coordination, long-horizon execution, and reasoning. We develop a low-cost data collection system and collect 1.1K trajectories across these tasks, with support for domain randomization to assess robustness. We benchmark modern models under diverse settings, including visual and dynamics randomization, multi-task training, and action-head adaptation. Through extensive empirical analysis, we identify several important insights and common limitations of current policies in dexterous manipulation, highlighting key challenges for future research in dexterous hand robot learning. Project page available at: https://dexjoco.github.io
匹配关键词: masked language model
---

[ACADEMIC - ARXIV]
标题: Designing Datacenter Power Delivery Hierarchies for the AI Era
作者: Grant Wilkins, Fiodar Kazhamiaka, Alok Gautam Kumbhare, Chaojie Zhang, Ricardo Bianchini
链接: https://arxiv.org/abs/2605.16255v1
完整摘要: Demand for AI accelerators is rapidly increasing rack power density, with projections approaching 1MW per deployment by 2027. This poses a major challenge for datacenter power delivery designers. As power densities increase, a datacenter designed for a different target density may strand power, i.e., may be unable to use all the power that its delivery hierarchy has provisioned. Designs must remain efficient over long datacenter lifetimes and multiple hardware generations. Power utilization is particularly important as grid power capacity is a scarce resource in the AI era. Designing an efficient power delivery hierarchy for the long run is difficult because rack placement feasibility, workload impact, and cost depend jointly on electrical topology, deployment granularity, placement policy, power oversubscription, and workload mix. Moreover, each of these factors evolve over time, have inter-dependencies across multiple resource dimensions, and generally do not lend themselves to closed-form analysis. To address this challenge, we develop a framework for evaluating datacenter power delivery designs using throughput, power, and cost metrics over realistic arrival, oversubscription, and decommissioning sequences. The framework combines projection models for GPU, compute, and storage deployments with operational factors grounded in production data from Microsoft Azure. Our results show that multi-resource stranding materially changes deployable capacity, effective capital expenditure, and delivered performance, and quantify how rising density from rack- and pod-scale AI systems shapes these outcomes. For AI datacenter design, the relevant planning objective is not installed megawatts, but deployable capacity over time.
匹配关键词: masked language model
---

[ACADEMIC - ARXIV]
标题: Real-time Speech Restoration using Data Prediction Mean Flows
作者: Sebastian Braun
链接: https://arxiv.org/abs/2605.16251v1
完整摘要: Generative models are capable to address difficult problems with non-unique solutions like bandwidth extension and gap filling, removing highly non-linear artifacts from codecs, clipping and distortion, as opposed to removing linear additive components like noise and reverb. While large offline processing models have shown impressive results, these tasks have not been solved with real-time capable models with low latency and compute. We propose a few-step flow matching model using Data Prediction Mean Flows in combination with suitable novel low-latency architecture to make flow matching models an attractive choice under theses constraints. Compared to state-of-the-art, our proposed mean flow model uses 120x less compute and introduces no algorithmic latency other than the STFT, while achieving similar audio quality.
匹配关键词: masked language model
---

[ACADEMIC - ARXIV]
标题: A Generative AI Framework for Intelligent Utility Billing CO 2 Analytics and Sustainable Resource Optimisation
作者: Pavan Manjunath, Thomas Pruefer
链接: https://arxiv.org/abs/2605.16250v1
完整摘要: Distribution utilities are now expected to deliver bills that customers can actually read attach a defensible carbon number to every kWh sold and schedule load against grid stress and emissions constraints We propose an end-to-end framework that unifies four production-grade capabilities under one architectural roof a generative-AI agent that drafts each customers natural-language billing statement from structured numeric inputs under a constrained decoding policy a transformer-based forecaster that supplies the day-ahead consumption estimate with calibrated quantile bands
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
标题: A Cross-Modal Prompt Injection Attack against Large Vision-Language Models with Image-Only Perturbation
作者: Hao Yang, Zhuo Ma, Yang Liu, Yilong Yang, Guancheng Wang, JianFeng Ma
链接: https://arxiv.org/abs/2605.16090v1
完整摘要: Large vision-language models (LVLMs) have emerged as a powerful paradigm for multimodal intelligence, but their growing deployment also expands the attack surface of prompt injection. Despite this growing concern, existing attacks still suffer from a critical limitation: the injected prompt for one modality only steers the model's interpretation of that singular input. Alternatively, these attacks remain multimodal but fail to achieve cross-modal prompt perturbation. To bridge this gap, we introduce a novel cross-modal prompt injection attack CrossMPI, which can steer the model's interpretation of both textual and visual inputs via image-only prompt injection. Our design is underpinned by the following key breakthroughs. First, we turn the focus of the injected prompt perturbation optimization from the visual embedding space (typically with only $10^5$ parameters) to the model hidden state space (for multimodal information integration and with $10^7$ parameters). Then, two strategies are adopted to mitigate the optimization challenges posed by the larger parameter space. To constrain the optimized model parameter space, we introduce a layer selection strategy that identifies the layers most critical to multimodal integration. Interestingly, deviating from the past experience, our analysis reveals that the optimal layers for LVLM prompt perturbation reside in the middle of the model rather than the last. To constrain the image perturbation space, we propose a new distance-decremental perturbation budget assignment strategy that allocates budgets decrementally as the pixel distance to semantic-critical regions increases. Extensive experiments across multiple LVLMs and datasets show that our method significantly outperforms baseline approaches.
匹配关键词: MAE
---

[ACADEMIC - ARXIV]
标题: From Flat Language Labels to Typological Priors: Structured Language Conditioning for Multilingual Speech-to-Speech Translation
作者: Yu Pan, Yang Hou, Xiongfei Wu, Liang Zhang, Yves Le Traon, Lei Ma, Jianjun Zhao
链接: https://arxiv.org/abs/2605.16026v1
完整摘要: Compositional speech-to-speech translation (S2ST) systems built upon speech large language models (SpeechLLMs) have recently shown promising performance. However, existing S2ST systems often either neglect source-language information or encode it through a language-as-label paradigm, representing each source language as an independent flat embedding. Such a design overlooks systematic linguistic structure shared across languages, which may limit data-efficient multilingual adaptation when supervised S2ST data are scarce. To address this issue, we propose S2ST-Omni 2, a many-to-one compositional S2ST framework that systematically reformulates multilingual language conditioning from flat language labels to structured typological priors. Specifically, S2ST-Omni 2 revisits language conditioning at three levels: typology-informed hierarchical language encoding for structured source-language representation, dynamically-gated language-aware Dual-CTC for content-adaptive acoustic modulation, and typology-aware LLM prompting for decoder-side linguistic guidance. Experiments on CVSS-C show that S2ST-Omni 2 achieves superior average performance among representative S2ST approaches across BLEU, COMET, ASR-BLEU, and BLASER 2.0 under the adopted evaluation protocol. Ablation studies indicate that the proposed representation-level, acoustic-level, and decoding-level strategies provide complementary benefits. Moreover, controlled data-budget analyses and a Japanese-to-English evaluation using only approximately 3 hours of supervised training data suggest that explicit typological priors provide useful inductive biases for data-efficient multilingual S2ST.
匹配关键词: MAE
---

[ACADEMIC - ARXIV]
标题: Towards Generalization of Block Attention via Automatic Segmentation and Block Distillation
作者: Shuaiyi Li, Zhisong Zhang, Yan Wang, Lei Zhu, Dongyang Ma, Chenlong Deng, Yang Deng, Wai Lam
链接: https://arxiv.org/abs/2605.15913v1
完整摘要: Block attention, which processes the input as separate blocks that cannot attend to one another, offers significant potential to improve KV cache reuse in long-context scenarios such as Retrieval-Augmented Generation (RAG). However, its broader application is hindered by two key challenges: the difficulty of segmenting input text into meaningful, self-contained blocks, and the inefficiency of existing block fine-tuning methods that risk degrading performance. To address these, we first construct SemanticSeg, a large and diverse semantic segmentation dataset containing over 30k instances across 16 categories-including books, code, web text, and conversations with text lengths ranging from 2k to 32k. Using this dataset, we train a lightweight segmenter to automatically partition text into human-instinct-aligned blocks with controllable granularity. Second, we propose block distillation, a training framework that is more efficient than block fine-tuning, which uses a frozen full-attention teacher model to guide the block-attention student. This framework integrates three novel components: block sink tokens to mitigate information loss at block boundaries, block dropout to leverage training signals from all blocks, and token-level loss weighting to focus learning on block-attention-sensitive tokens. Experiments across multiple models and benchmarks demonstrate that our segmenter outperforms heuristic and statistical baselines, and block distillation achieves near-full-attention performance under block attention, establishing a practical and scalable pathway for deploying block attention.
匹配关键词: MAE
---

[ACADEMIC - ARXIV]
标题: Are VLMs Seeing or Just Saying? Uncovering the Illusion of Visual Re-examination
作者: Chufan Shi, Cheng Yang, Yaokang Wu, Linhao Jin, Bo Shui, Taylor Berg-Kirkpatrick, Xuezhe Ma
链接: https://arxiv.org/abs/2605.15864v1
完整摘要: Vision-Language Models (VLMs) often produce self-reflective statements like "let me check the figure again" during reasoning. Do such statements trigger genuine visual re-examination, or are they merely learned textual patterns? We investigate this via VisualSwap, an image-swap probing framework: after a model reasons over an image, we replace it with a visually similar but semantically different one and test whether the model notices. We introduce VS-Bench, 800 image pairs curated from MathVista, MathVerse, MathVision, and MMMU-Pro. Experiments on Qwen3-VL, Kimi-VL, and ERNIE-VL reveal a striking failure: models overwhelmingly miss the swap, with accuracy dropping by up to 60%. Counterintuitively, thinking models are nearly 3x more vulnerable than their instructed counterparts, and scaling offers no mitigation. Multi-turn user instructions restore visual grounding, but self-generated reflective statements during continuous generation do not. Attention analysis explains why: user instructions substantially elevate attention to visual tokens, whereas self-reflection does not. Current VLMs tend to say rather than actually see when claiming to perform visual re-examination. Our code and dataset are available at the project page: https://visualswap.github.io
匹配关键词: MAE
---

[ACADEMIC - ARXIV]
标题: Modeling Music as a Time-Frequency Image: A 2D Tokenizer for Music Generation
作者: Yuqing Cheng, Xingyu Ma, Guochen Yu, Xiaotao Gu
链接: https://arxiv.org/abs/2605.15831v1
完整摘要: Autoregressive music generation depends strongly on the audio tokenizer. Existing high-fidelity codecs often use residual multi-codebook quantization, which preserves reconstruction quality but complicates language modeling after sequence flattening, as the residual hierarchy imposes strong sequential dependencies and can amplify error accumulation. We propose BandTok, a generation-oriented 2D Mel-spectrogram tokenizer that represents each frame with Mel-frequency band tokens from a single shared codebook. This design yields a physically interpretable time-frequency token grid with a more independent token structure, making it better suited for autoregressive modeling. BandTok improves reconstruction with a multi-scale PatchGAN objective and EMA codebook updates. We further introduce an autoregressive language model with 2D Rotary Position Embedding (2D RoPE) to preserve temporal and frequency-band structure during generation. Experiments show that BandTok improves over residual-codebook tokenizers and achieves strong results in a data-limited setting. The source code and generation demos for this work are publicly available.
匹配关键词: MAE
---

[ACADEMIC - ARXIV]
标题: IVGT: Implicit Visual Geometry Transformer for Neural Scene Representation
作者: Yuqi Wu, Tianyu Hu, Wenzhao Zheng, Yuanhui Huang, Haowen Sun, Jie Zhou, Jiwen Lu
链接: https://arxiv.org/abs/2605.16258v1
完整摘要: Reconstructing coherent 3D geometry and appearance from unposed multi-view images is a fundamental yet challenging problem in computer vision. Most existing visual geometry foundation models predict explicit geometry by regressing pixel-aligned pointmaps, often suffering from redundancy and limited geometric continuity. We propose IVGT, an Implicit Visual Geometry Transformer that implicitly models continuous and coherent geometry from pose-free multi-view images. This formulation learns a continuous neural scene representation in a canonical coordinate system and supports continuous spatial queries at any 3D positions, retrieving local features to predict signed distance (SDF) values and colors using lightweight decoders. It allows direct extraction of continuous and coherent surface geometry, enabling rendering of RGB images, depth maps, and surface normal maps from arbitrary viewpoints. We train IVGT via multi-dataset joint optimization with 2D supervision and 3D geometric regularization. IVGT demonstrates generalization across scenes and achieves strong performance on various tasks, including mesh and point cloud reconstruction, novel view synthesis, depth and surface normal estimation, and camera pose estimation.
匹配关键词: generative model
---

[ACADEMIC - ARXIV]
标题: DexJoCo: A Benchmark and Toolkit for Task-Oriented Dexterous Manipulation on MuJoCo
作者: Hanwen Wang, Weizhi Zhao, Xiangyu Wang, Siyuan Huang, He Lin, Boyuan Zheng, Rongtao Xu, Gang Wang, Yao Mu, He Wang, Lue Fan, Hongsheng Li, Zhaoxiang Zhang, Tieniu Tan
链接: https://arxiv.org/abs/2605.16257v1
完整摘要: Achieving human-level manipulation requires dexterous robotic hands capable of complex object interactions. Advancing such capabilities further demands standardized benchmarks for systematic evaluation. However, existing dexterous benchmarks lack tasks that reflect the unique manipulation capabilities of dexterous hands over parallel grippers, as well as comprehensive evaluation pipelines. In this paper, we present DexJoCo, a benchmark and toolkit for task-oriented dexterous manipulation, comprising 11 functionally grounded tasks that evaluate tool-use, bimanual coordination, long-horizon execution, and reasoning. We develop a low-cost data collection system and collect 1.1K trajectories across these tasks, with support for domain randomization to assess robustness. We benchmark modern models under diverse settings, including visual and dynamics randomization, multi-task training, and action-head adaptation. Through extensive empirical analysis, we identify several important insights and common limitations of current policies in dexterous manipulation, highlighting key challenges for future research in dexterous hand robot learning. Project page available at: https://dexjoco.github.io
匹配关键词: generative model
---

[ACADEMIC - ARXIV]
标题: Designing Datacenter Power Delivery Hierarchies for the AI Era
作者: Grant Wilkins, Fiodar Kazhamiaka, Alok Gautam Kumbhare, Chaojie Zhang, Ricardo Bianchini
链接: https://arxiv.org/abs/2605.16255v1
完整摘要: Demand for AI accelerators is rapidly increasing rack power density, with projections approaching 1MW per deployment by 2027. This poses a major challenge for datacenter power delivery designers. As power densities increase, a datacenter designed for a different target density may strand power, i.e., may be unable to use all the power that its delivery hierarchy has provisioned. Designs must remain efficient over long datacenter lifetimes and multiple hardware generations. Power utilization is particularly important as grid power capacity is a scarce resource in the AI era. Designing an efficient power delivery hierarchy for the long run is difficult because rack placement feasibility, workload impact, and cost depend jointly on electrical topology, deployment granularity, placement policy, power oversubscription, and workload mix. Moreover, each of these factors evolve over time, have inter-dependencies across multiple resource dimensions, and generally do not lend themselves to closed-form analysis. To address this challenge, we develop a framework for evaluating datacenter power delivery designs using throughput, power, and cost metrics over realistic arrival, oversubscription, and decommissioning sequences. The framework combines projection models for GPU, compute, and storage deployments with operational factors grounded in production data from Microsoft Azure. Our results show that multi-resource stranding materially changes deployable capacity, effective capital expenditure, and delivered performance, and quantify how rising density from rack- and pod-scale AI systems shapes these outcomes. For AI datacenter design, the relevant planning objective is not installed megawatts, but deployable capacity over time.
匹配关键词: generative model
---

[ACADEMIC - ARXIV]
标题: Real-time Speech Restoration using Data Prediction Mean Flows
作者: Sebastian Braun
链接: https://arxiv.org/abs/2605.16251v1
完整摘要: Generative models are capable to address difficult problems with non-unique solutions like bandwidth extension and gap filling, removing highly non-linear artifacts from codecs, clipping and distortion, as opposed to removing linear additive components like noise and reverb. While large offline processing models have shown impressive results, these tasks have not been solved with real-time capable models with low latency and compute. We propose a few-step flow matching model using Data Prediction Mean Flows in combination with suitable novel low-latency architecture to make flow matching models an attractive choice under theses constraints. Compared to state-of-the-art, our proposed mean flow model uses 120x less compute and introduces no algorithmic latency other than the STFT, while achieving similar audio quality.
匹配关键词: generative model
---

[ACADEMIC - ARXIV]
标题: A Generative AI Framework for Intelligent Utility Billing CO 2 Analytics and Sustainable Resource Optimisation
作者: Pavan Manjunath, Thomas Pruefer
链接: https://arxiv.org/abs/2605.16250v1
完整摘要: Distribution utilities are now expected to deliver bills that customers can actually read attach a defensible carbon number to every kWh sold and schedule load against grid stress and emissions constraints We propose an end-to-end framework that unifies four production-grade capabilities under one architectural roof a generative-AI agent that drafts each customers natural-language billing statement from structured numeric inputs under a constrained decoding policy a transformer-based forecaster that supplies the day-ahead consumption estimate with calibrated quantile bands
匹配关键词: generative model
---

[ACADEMIC - ARXIV]
标题: IVGT: Implicit Visual Geometry Transformer for Neural Scene Representation
作者: Yuqi Wu, Tianyu Hu, Wenzhao Zheng, Yuanhui Huang, Haowen Sun, Jie Zhou, Jiwen Lu
链接: https://arxiv.org/abs/2605.16258v1
完整摘要: Reconstructing coherent 3D geometry and appearance from unposed multi-view images is a fundamental yet challenging problem in computer vision. Most existing visual geometry foundation models predict explicit geometry by regressing pixel-aligned pointmaps, often suffering from redundancy and limited geometric continuity. We propose IVGT, an Implicit Visual Geometry Transformer that implicitly models continuous and coherent geometry from pose-free multi-view images. This formulation learns a continuous neural scene representation in a canonical coordinate system and supports continuous spatial queries at any 3D positions, retrieving local features to predict signed distance (SDF) values and colors using lightweight decoders. It allows direct extraction of continuous and coherent surface geometry, enabling rendering of RGB images, depth maps, and surface normal maps from arbitrary viewpoints. We train IVGT via multi-dataset joint optimization with 2D supervision and 3D geometric regularization. IVGT demonstrates generalization across scenes and achieves strong performance on various tasks, including mesh and point cloud reconstruction, novel view synthesis, depth and surface normal estimation, and camera pose estimation.
匹配关键词: diffusion model
---

[ACADEMIC - ARXIV]
标题: DexJoCo: A Benchmark and Toolkit for Task-Oriented Dexterous Manipulation on MuJoCo
作者: Hanwen Wang, Weizhi Zhao, Xiangyu Wang, Siyuan Huang, He Lin, Boyuan Zheng, Rongtao Xu, Gang Wang, Yao Mu, He Wang, Lue Fan, Hongsheng Li, Zhaoxiang Zhang, Tieniu Tan
链接: https://arxiv.org/abs/2605.16257v1
完整摘要: Achieving human-level manipulation requires dexterous robotic hands capable of complex object interactions. Advancing such capabilities further demands standardized benchmarks for systematic evaluation. However, existing dexterous benchmarks lack tasks that reflect the unique manipulation capabilities of dexterous hands over parallel grippers, as well as comprehensive evaluation pipelines. In this paper, we present DexJoCo, a benchmark and toolkit for task-oriented dexterous manipulation, comprising 11 functionally grounded tasks that evaluate tool-use, bimanual coordination, long-horizon execution, and reasoning. We develop a low-cost data collection system and collect 1.1K trajectories across these tasks, with support for domain randomization to assess robustness. We benchmark modern models under diverse settings, including visual and dynamics randomization, multi-task training, and action-head adaptation. Through extensive empirical analysis, we identify several important insights and common limitations of current policies in dexterous manipulation, highlighting key challenges for future research in dexterous hand robot learning. Project page available at: https://dexjoco.github.io
匹配关键词: diffusion model
---

[ACADEMIC - ARXIV]
标题: Designing Datacenter Power Delivery Hierarchies for the AI Era
作者: Grant Wilkins, Fiodar Kazhamiaka, Alok Gautam Kumbhare, Chaojie Zhang, Ricardo Bianchini
链接: https://arxiv.org/abs/2605.16255v1
完整摘要: Demand for AI accelerators is rapidly increasing rack power density, with projections approaching 1MW per deployment by 2027. This poses a major challenge for datacenter power delivery designers. As power densities increase, a datacenter designed for a different target density may strand power, i.e., may be unable to use all the power that its delivery hierarchy has provisioned. Designs must remain efficient over long datacenter lifetimes and multiple hardware generations. Power utilization is particularly important as grid power capacity is a scarce resource in the AI era. Designing an efficient power delivery hierarchy for the long run is difficult because rack placement feasibility, workload impact, and cost depend jointly on electrical topology, deployment granularity, placement policy, power oversubscription, and workload mix. Moreover, each of these factors evolve over time, have inter-dependencies across multiple resource dimensions, and generally do not lend themselves to closed-form analysis. To address this challenge, we develop a framework for evaluating datacenter power delivery designs using throughput, power, and cost metrics over realistic arrival, oversubscription, and decommissioning sequences. The framework combines projection models for GPU, compute, and storage deployments with operational factors grounded in production data from Microsoft Azure. Our results show that multi-resource stranding materially changes deployable capacity, effective capital expenditure, and delivered performance, and quantify how rising density from rack- and pod-scale AI systems shapes these outcomes. For AI datacenter design, the relevant planning objective is not installed megawatts, but deployable capacity over time.
匹配关键词: diffusion model
---

[ACADEMIC - ARXIV]
标题: Real-time Speech Restoration using Data Prediction Mean Flows
作者: Sebastian Braun
链接: https://arxiv.org/abs/2605.16251v1
完整摘要: Generative models are capable to address difficult problems with non-unique solutions like bandwidth extension and gap filling, removing highly non-linear artifacts from codecs, clipping and distortion, as opposed to removing linear additive components like noise and reverb. While large offline processing models have shown impressive results, these tasks have not been solved with real-time capable models with low latency and compute. We propose a few-step flow matching model using Data Prediction Mean Flows in combination with suitable novel low-latency architecture to make flow matching models an attractive choice under theses constraints. Compared to state-of-the-art, our proposed mean flow model uses 120x less compute and introduces no algorithmic latency other than the STFT, while achieving similar audio quality.
匹配关键词: diffusion model
---

[ACADEMIC - ARXIV]
标题: AI-Mediated Communication Can Steer Collective Opinion
作者: Stratis Tsirtsis, Kai Rawal, Chris Russell, Brent Mittelstadt, Sandra Wachter
链接: https://arxiv.org/abs/2605.16245v1
完整摘要: Generative artificial intelligence (AI) is increasingly integrated into the online platforms where humans exchange opinions; large language models (LLMs) now polish users' posts on LinkedIn and provide context for content shared on X. While prior work has shown that AI can express biased opinions and shape individuals' opinions during human-AI interactions, less attention has been paid to its influence on collective opinion formation when mediating human-to-human communication. We address this gap via a combination of empirical and theoretical analyses. We show empirically that LLMs from multiple popular families introduce directional biases when instructed to edit human-written texts on contested topics, for example, nudging texts in favor of gun control and against atheism. Building on this observation, we introduce a mathematical model of opinion dynamics in which an AI system sits between users on a social network, transforming the opinions they express and perceive. By analytically characterizing the equilibrium of this model and performing simulations on real social network data, we show that biases introduced by AI in human-to-human communication can be amplified through the network and shift collective opinion in their direction. In light of these findings, we investigate whether such biases are controllable by online platforms. We audit the "Explain this post" feature on X and find evidence of pro-life bias in Grok's outputs on abortion-related content, which we trace back to specific design choices. We conclude with a discussion of the broader implications of our findings in relation to ongoing legislative efforts in the European Union.
匹配关键词: diffusion model
---

[ACADEMIC - ARXIV]
标题: When and Why Adversarial Training Improves PINNs: A Neural Tangent Kernel Perspective
作者: Yuan-dong Cao, Chi Chiu SO, Jun-Min Wang, He Wang
链接: https://arxiv.org/abs/2605.15959v1
完整摘要: Physics-informed neural networks (PINNs) are powerful surrogates for differential equations but are notoriously difficult to train due to spectral bias, stiffness, and poor accuracy on high-frequency or multiscale solutions. Adversarial training based on generative adversarial networks (GANs) has recently gained surprisingly strong empirical results in improving training, but the underlying mechanisms remain elusive. To this end, we propose a new analysis framework for adversarially trained PINNs, based on the key observation of how the discriminator in GANs can influence the training dynamics of PINNs. The framework first provides a much needed theoretical grounding to why and when adversarial training is effective in PINNs, then presents a unified analysis of GANs variants in such training, and finally leads to a new, practical, efficient training algorithm for PINNs. Empirical results demonstrate that our method can significantly reduce the pathology of PINNs training, thereby providing better models with superior performances, often several magnitudes more accurate than alternative methods.
匹配关键词: GAN
---

[ACADEMIC - ARXIV]
标题: Can Visual Mamba Improve AI-Generated Image Detection? An In-Depth Investigation
作者: Mamadou Keita, Wassim Hamidouche, Hessen Bougueffa Eutamene, Abdelmalik Taleb-Ahmed, Xianxun Zhu, Abdenour Hadid
链接: https://arxiv.org/abs/2605.14799v1
完整摘要: In recent years, computer vision has witnessed remarkable progress, fueled by the development of innovative architectures such as Convolutional Neural Networks (CNNs), Generative Adversarial Networks (GANs), diffusion-based architectures, Vision Transformers (ViTs), and, more recently, Vision-Language Models (VLMs). This progress has undeniably contributed to creating increasingly realistic and diverse visual content. However, such advancements in image generation also raise concerns about potential misuse in areas such as misinformation, identity theft, and threats to privacy and security. In parallel, Mamba-based architectures have emerged as versatile tools for a range of image analysis tasks, including classification, segmentation, medical imaging, object detection, and image restoration, in this rapidly evolving field. However, their potential for identifying AI-generated images remains relatively unexplored compared to established techniques. This study provides a systematic evaluation and comparative analysis of Vision Mamba models for AI-generated image detection. We benchmark multiple Vision Mamba variants against representative CNNs, ViTs, and VLM-based detectors across diverse datasets and synthetic image sources, focusing on key metrics such as accuracy, efficiency, and generalizability across diverse image types and generative models. Through this comprehensive analysis, we aim to elucidate Vision Mamba's strengths and limitations relative to established methodologies in terms of applicability, accuracy, and efficiency in detecting AI-generated images. Overall, our findings highlight both the promise and current limitations of Vision Mamba as a component in systems designed to distinguish authentic from AI-generated visual content. This research is crucial for enhancing detection in an age where distinguishing between real and AI-generated content is a major challenge.
匹配关键词: GAN
---

[ACADEMIC - ARXIV]
标题: Beyond What to Select: A Plug-and-play Oscillatory Data-Volume Scheduling for Efficient Model Training
作者: Suorong Yang, Hanqi Zhu, Hai Gan, Fangjian Su, Guang Li, Furao Shen, Soujanya Poria
链接: https://arxiv.org/abs/2605.14773v1
完整摘要: Data selection accelerates training by identifying representative training data while preserving model performance. However, existing methods mainly focus on designing sample-importance criteria, i.e., deciding what to select, while typically fixing the selected data volume as the target ratio throughout training. Thus, they are often dynamic in sample identity but static in data volume. In this work, we revisit data selection from an optimization perspective and show that selected-data training induces an implicit regularization effect modulated by the instantaneous selection ratio. This reveals a key trade-off: lower ratios amplify selection-induced regularization, whereas higher ratios preserve data coverage and optimization fidelity. Motivated by this insight, we propose PODS, a Plug-and-play Oscillatory Data-volume Scheduling framework. Rather than introducing another sample-scoring metric, PODS serves as a lightweight module that dynamically schedules how much data to select over training. Under the target selection ratio, PODS alternates between low-ratio regularization phases and high-ratio recovery phases to exploit selection-induced regularization without sacrificing optimization stability. With its lightweight, ratio-level, and task-agnostic design, PODS is compatible with existing static and dynamic selection methods and broadly applicable across training paradigms. Experiments across various datasets, architectures, and tasks show that PODS consistently improves the efficiency-generalization trade-off, e.g., reducing ImageNet-1k training cost by 50% with improved accuracy and accelerating LLM instruction tuning by over 2x without performance degradation.
匹配关键词: GAN
---

[ACADEMIC - ARXIV]
标题: Reduce the Artifacts Bias for More Generalizable AI-Generated Image Detection
作者: Yiheng Li, Yang Yang, Zichang Tan, Gao Li, Zhen Lei, Wenhao Wang
链接: https://arxiv.org/abs/2605.14486v1
完整摘要: As the misuse of AI-generated images grows, generalizable image detection techniques are urgently needed. Recent state-of-the-art (SOTA) methods adopt aligned training datasets to reduce content, size, and format biases, empowering models to capture robust forgery cues. A common strategy is to employ reconstruction techniques, e.g., VAE and DDIM, which show remarkable results in diffusion-based methods. However, such reconstruction-based approaches typically introduce limited and homogeneous artifacts, which cannot fully capture diverse generative patterns, such as GAN-based methods. To complement reconstruction-based fake images with aligned yet diverse artifact patterns, we propose a GAN-based upsampling approach that mimics GAN-generated fake patterns while preserving content, size, and format alignment. This naturally results in two aligned but distinct types of fake images. However, due to the domain shift between reconstruction-based and upsampling-based fake images, direct mixed training causes suboptimal results, where one domain disrupts feature learning of the other. Accordingly, we propose a Separate Expert Fusion (SEF) framework to extract complementary artifact information and reduce inter-domain interference. We first train domain-specific experts via LoRA adaptation on a frozen foundational model, then conduct decoupled fusion with a gating network to adaptively combine expert features while retaining their specialized knowledge. Rather than merely benefiting GAN-generated image detection, this design introduces diverse and complementary artifact patterns that enable SEF to learn a more robust decision boundary and improve generalization across broader generative methods. Extensive experiments demonstrate that our method yields strong results across 13 diverse benchmarks. Codes are released at: https://github.com/liyih/SEF_AIGC_detection.
匹配关键词: GAN
---

[ACADEMIC - ARXIV]
标题: Smooth Multi-Policy Causal Effect Estimation in Longitudinal Settings
作者: Wenxin Chen, Weishen Pan, Kyra Gan, Fei Wang
链接: https://arxiv.org/abs/2605.14284v1
完整摘要: Comparative evaluation of multiple dynamic treatment policies is essential for healthcare and policy decisions, yet conventional longitudinal causal inference methods estimate each in isolation, preventing information sharing across counterfactuals. We demonstrate that this separate estimation paradigm induces a structurally uncontrolled second-order bias, inflating finite-sample variance even after standard debiasing with longitudinal targeted maximum likelihood estimation(LTMLE). To address this, we propose a policy-aware reparameterization of Iterative Conditional Expectation (ICE) Q-functions that enables joint estimation through shared representations. We implement this approach in the Policy-Encoded Q Network (PEQ-Net), an architecture centered on a shared policy encoder. The encoder is trained using kernel mean embeddings, ensuring that the learned representation space reflects population-level policy dissimilarities. After applying an LTMLE correction step, we prove this design imposes a structural constraint on the second-order remainder, thereby stabilizing finite-sample variance. Experiments on semi-synthetic datasets demonstrate that PEQ-Net consistently outperforms existing ICE-based methods, achieving substantial reductions in root-mean-square error, particularly when evaluating closely related policies.
匹配关键词: GAN
---

[ACADEMIC - ARXIV]
标题: Entropic Auto-Encoding via Implicit Free-Energy Minimization
作者: Hazhir Aliahmadi, Irina Babayan, Greg van Anders
链接: https://arxiv.org/abs/2605.16164v1
完整摘要: Despite their ubiquity, variational autoencoders (VAEs) inherently suffer from posterior collapse, a failure mode in which latent variables are effectively ignored. This failure arises because explicit prior imposition drives optimization toward loss landscape regions corresponding to uninformative latent representations. Here, we introduce Entropic Autoencoders (EAEs), a framework in which reconstruction loss is the only explicit objective, and entropy generates the latent variables' prior implicitly through a free energy-minimizing ensemble of encoders. This ensemble biases learning toward high-volume regions of near-optimal solutions, while decoder updates direct the search trajectories toward informative latent representations. We demonstrate that EAEs mitigate posterior collapse by learning non-Gaussian, multimodal latent distributions that yield diverse, data-consistent generations and preserve different forms of underlying structure in the data. As a proof-of-concept, we show that an EAE captures a superposition of the known low-dimensional dynamics of a reaction-diffusion process. Then, we show that an EAE identifies implicit categorical distinctions in MNIST latent representations, and displays a hierarchical understanding of facial structure on the CelebA dataset, from an "all-human" face to individual-dependent features.
匹配关键词: VAE
---

[ACADEMIC - ARXIV]
标题: Entropy-Based Characterisation of the Polarised Regime in Latent Variable Models
作者: Peter Clapham, Lisa Bonheme, Marek Grzes
链接: https://arxiv.org/abs/2605.15965v1
完整摘要: Variational Autoencoders (VAEs) often exhibit a polarised regime in which latent variables separate into active, passive, and mixed subsets. Existing criteria for identifying active dimensions depend on a Gaussian prior, limiting their applicability to variational models and specific priors. We propose a simple information-theoretic classification of the polarised regime based on the entropy of the mean representation. We show theoretically how this entropy couples to KL minimisation through entropy--variance bounds, and we relate the resulting criterion to Bonheme's active/passive conditions. We also clarify a key limitation: entropy of the mean alone cannot reliably distinguish active from mixed dimensions without additional signals from the variance representation. Empirically, we evaluate the entropy criterion on $β$-VAEs, identifiable VAEs, Least-Volume Autoencoders, and L2-regularised autoencoders, and find that it consistently recovers a polarised regime when such a regime is present across the model classes studied. Finally, we show that passive dimensions can yield small but consistent improvements on downstream tasks when latent codes are appropriately normalised, suggesting that collapse is often a matter of scale rather than absolute information removal.
匹配关键词: VAE
---

[ACADEMIC - ARXIV]
标题: HyperDiT: Hyper-Connected Transformers for High-Fidelity Pixel-Space Diffusion
作者: Yu He, Lichen Ma, Zipeng Guo, Xinyuan Shan, Jingling Fu, Dong Chen, Junshi Huang, Yan Li
链接: https://arxiv.org/abs/2605.15741v1
完整摘要: Pixel-space diffusion models bypass the reconstruction bottleneck of Variational Autoencoders (VAEs) but face a fundamental "granularity dilemma": capturing global semantics favors large patch scales, while generating high-fidelity details demands fine-grained inputs. To address this issue, we propose HyperDiT, a unified framework establishing Hyper-Connected Cross-Scale Interactions to bridge the semantic and pixel manifold. Diverging from injecting semantics by AdaLN, HyperDiT utilizes Cross-Attention mechanisms, enabling fine-grained tokens to query multi-level semantic anchors globally. To resolve the spatial mismatch during multi-scale interactions, we introduce Scale-Aware Rotary Position Embedding (SA-RoPE) to ensure precise geometric alignment among tokens of varying patch sizes. Furthermore, we incorporate Registers to learn the dense semantics from a pretrained Visual Foundation Model (VFM), effectively reducing generation hallucination and artifacts. Extensive experiments demonstrate that HyperDiT achieves state-of-the-art (SoTA) FID of $\mathbf{1.56}$ on ImageNet $256\times256$ directly within the pixel space. By combining the fine-grained stream with semantic guidance, HyperDiT offers a superior paradigm for high-fidelity pixel generation.
匹配关键词: VAE
---

[ACADEMIC - ARXIV]
标题: ElasticDiT: Efficient Diffusion Transformers via Elastic Architecture and Sparse Attention for High-Resolution Image Generation on Mobile Devices
作者: Kunpeng Du, Haizhen Xie, Sen Lu, Lei Yu, Binglei Bao, Huaao Tang, Chuntao Liu, Hao Wu, Yang Zhao, Zhicai Huang, Heyuan Gao, Zhijun Tu, Jie Hu, Xinghao Chen
链接: https://arxiv.org/abs/2605.15684v1
完整摘要: The Diffusion Transformer (DiT) architecture is the state-of-the-art paradigm for high-fidelity image generation, underpinning models like Stable Diffusion-3 and FLUX.1. However, deploying these models on resource-constrained mobile devices entails prohibitive computational and memory overhead. While efficiency-driven approaches like Linear-DiT and static pruning alleviate bottlenecks, they often incur quality degradation. Unlike cloud environments, mobile constraints require a single-model paradigm that dynamically balances fidelity and latency. We introduce ElasticDiT, which achieves this dynamic trade-off by adjusting spatial compression ratios and DiT block depths. By integrating Shift Sparse Block Attention (SSBA) and a Tiny DWT-Distilled VAE (T-DVAE), ElasticDiT reduces inference latency and memory footprint while maintaining image quality. Experiments confirm that ElasticDiT effectively covers a wide range of fidelity-latency trade-offs within a single set of parameters. By jointly adjusting compression and depth, a single ElasticDiT model can be reconfigured on-the-fly to outperform task-specific baselines. Specifically, our flex lite variant achieves an HPS of 32.87, surpassing the Flux model, while maintaining competitive quality at 84.16 percent average sparsity through SSBA. Furthermore, the plug-and-play T-DVAE provides SD3-level reconstruction with only 1/8x the computational cost of standard VAEs, and Flow-GRPO boosts semantic alignment (GenEval: 66.93 to 73.62). These results demonstrate that ElasticDiT offers a versatile, hardware-adaptive solution that eliminates the need for multiple specialized models, providing a promising path for future high-resolution image generation on mobile devices.
匹配关键词: VAE
---

[ACADEMIC - ARXIV]
标题: RefDecoder: Enhancing Visual Generation with Conditional Video Decoding
作者: Xiang Fan, Yuheng Wang, Bohan Fang, Zhongzheng Ren, Ranjay Krishna
链接: https://arxiv.org/abs/2605.15196v1
完整摘要: Video generation powers a vast array of downstream applications. However, while the de facto standard, i.e., latent diffusion models, typically employ heavily conditioned denoising networks, their decoders often remain unconditional. We observe that this architectural asymmetry leads to significant loss of detail and inconsistency relative to the input image. To address this, we argue that the decoder requires equal conditioning to preserve structural integrity. We introduce RefDecoder, a reference-conditioned video VAE decoder by injecting high-fidelity reference image signal directly into the decoding process via reference attention. Specifically, a lightweight image encoder maps the reference frame into the detail-rich high-dimensional tokens, which are co-processed with the denoised video latent tokens at each decoder up-sampling stage. We demonstrate consistent improvements across several distinct decoder backbones (e.g., Wan 2.1 and VideoVAE+), achieving up to +2.1dB PSNR over the unconditional baselines on the Inter4K, WebVid, and Large Motion reconstruction benchmarks. Notably, RefDecoder can be directly swapped into existing video generation systems without additional fine-tuning, and we report across-the-board improvements in subject consistency, background consistency, and overall quality scores on the VBench I2V benchmark. Beyond I2V, RefDecoder generalizes well to a wide range of visual generation tasks such as style transfer and video editing refinement.
匹配关键词: VAE
---

[ACADEMIC - ARXIV]
标题: Second-Order Multi-Level Variance Correction for Modality Competition in Multimodal Models
作者: Yishun Lu, Wes Armour
链接: https://arxiv.org/abs/2605.16165v1
完整摘要: Autoregressive next-token training offers a unified formulation for image generation and text understanding, but it also creates strong modality competition that destabilizes optimization and limits large-batch scaling. We show that first-order optimizers such as AdamW are vulnerable to cross-modality gradient heterogeneity, while second-order preconditioning, particularly SOAP, provides a more stable basis for multimodal alignment. Building on this insight, we propose \emph{ML-FOP-SOAP}, a second-order optimization framework with Multi-Level Variance Correction. Our Fisher-Orthogonal Projection suppresses variance-induced modality conflicts, reducing the trade-off between visual generation and textual understanding. To make this practical under large gradient accumulation, we introduce a hierarchical folding strategy that captures fine-grained variance with low micro-step overhead. Experiments on Janus and Emu3 show consistent gains across both modalities and stable training at batch size 8192. Compared with AdamW, our method improves sample efficiency by up to $1.4\times$ and accelerates wall-clock training by up to $1.5\times$, offering a robust optimizer for scaling multimodal foundation models.
匹配关键词: autoregressive
---

[ACADEMIC - ARXIV]
标题: GenShield: Unified Detection and Artifact Correction for AI-Generated Images
作者: Zhipei Xu, Xuanyu Zhang, Youmin Xu, Qing Huang, Shen Chen, Taiping Yao, Shouhong Ding, Jian Zhang
链接: https://arxiv.org/abs/2605.16122v1
完整摘要: Diffusion-based image synthesis has made AI-generated images (AIGI) increasingly photorealistic, raising urgent concerns about authenticity in applications such as misinformation detection, digital forensics, and content moderation. Despite the substantial advances in AIGI detection, how to correct detected AI-generated images with visible artifacts and restore realistic appearance remains largely underexplored. Moreover, few existing work has established the connection between AIGI detection and artifact correction. To fill this gap, we propose GenShield, a unified autoregressive framework that jointly performs explainable AIGI detection and controllable artifact correction in a closed loop from diagnosis to restoration, revealing a mutually reinforcing relationship between these two tasks. We further introduce a Visual Chain-of-Thought based curriculum learning strategy that enables self-explained, multi-step ``diagnose-then-repair'' correction with an explicit stopping criterion. A high-quality dataset with large-scale ``artifact-restored'' pairs is also constructed alongside a unified evaluation pipeline. Extensive experiments on our correction benchmark and mainstream AIGI detection benchmarks demonstrate state-of-the-art performance and strong generalization of our method. The code is available at https://github.com/zhipeixu/GenShield.
匹配关键词: autoregressive
---

[ACADEMIC - ARXIV]
标题: Variational Autoregressive Networks with probability priors
作者: Piotr Białas, Piotr Korcyl, Tomasz Stebel, Dawid Zapolski
链接: https://arxiv.org/abs/2605.16020v1
完整摘要: Monte Carlo methods are essential across diverse scientific fields, yet their efficiency is frequently hampered by critical slowing down-a sharp increase in autocorrelation times near phase transitions. Although deep learning approaches, such as neural-network-based samplers, have been proposed to alleviate this issue, they face another serious problem: the difficulty of training the models. This difficulty partially stems from the overly general nature of original machine-learning architectures, which often ignore underlying physical symmetries and force networks to relearn them from scratch. In this paper, we demonstrate that incorporating physical priors into the model significantly enhances performance. Building upon existing strategies that integrate spin-spin interactions, we propose a framework that utilizes a prior probability distribution as a starting point for training. Our results for the Ising model, as well as for the Edwards-Anderson spin glass model, suggest that moving away from `blank slate' models in favor of physics-informed priors reduces the training burden and facilitates the simulation of larger system sizes in discrete spin models.
匹配关键词: autoregressive
---

[ACADEMIC - ARXIV]
标题: Echo-Forcing: A Scene Memory Framework for Interactive Long Video Generation
作者: Mingqiang Wu, Weilun Feng, Zhefeng Zhang, Haotong Qin, Yuqi Li, Guoxin Fan, Xiaokun Liu, Zhulin An, Libo Huang, Yongjun Xu, Chuanguang Yang
链接: https://arxiv.org/abs/2605.16003v1
完整摘要: Autoregressive video diffusion models enable open-ended generation through local attention and KV caching. However, existing training-free long-video optimization methods mainly focus on stable extension under a single prompt, making them difficult to handle interactive scenarios involving prompt switching, old scene forgetting, and historical scene recall. We identify the core bottleneck as the functional entanglement of historical KV states: stable anchors and recent dynamics are handled by the same cache policy, leading to outdated background contamination, delayed response to new prompts, and loss of long-range memory. To address this issue, we propose Echo-Forcing, a training-free scene memory framework specifically designed for interactive long video generation with three core mechanisms: (1) Hierarchical Temporal Memory, which decouples stable anchors, compressed history, and recent windows under relative RoPE; (2) Scene Recall Frames, which compresses historical scenes into spatially structured KV representations to support long-term recall; and (3) Difference-aware Memory Decay, which adaptively forgets conflicting tokens according to the discrepancy between old and new scenes. Based on these designs, Echo-Forcing uniformly supports smooth transitions, hard cuts, and long-range scene recall under a bounded cache budget. Extensive evaluations on VBench-Long further demonstrate that Echo-Forcing achieves the best overall performance in both long-video generation and interactive video generation settings. Our code is released in https://github.com/mingqiangWu/Echo-Forcing
匹配关键词: autoregressive
---

[ACADEMIC - ARXIV]
标题: Segmentation, Detection and Explanation: A Unified Framework for CT Appearance Reasoning
作者: Yuyuan Liu, Can Peng, Yingyu Yang, Qianye Yang, Cheng Ouyang, J. Alison Noble
链接: https://arxiv.org/abs/2605.15997v1
完整摘要: Recent progress in deep learning has significantly advanced CT image analysis, particularly for segmentation tasks. However, these advances are largely confined to image-level pattern recognition, with most methods lacking explicit anatomical or contextual reasoning. Large vision-language models introduce linguistic context into image analysis, yet most approaches typically focus on a single task, which is insufficient for clinical workflow analysis that requires multiple fine-grained types of analysis, such as anatomy detection and segmentation. In this paper, we propose a unified autoregressive framework that integrates language-guided visual reasoning into CT interpretation. Our method introduces task-routing tokens that trigger detection and segmentation heads conditioned on the hidden states of a large vision-language model, enabling coherent generation of visual outputs (e.g., masks and bounding boxes) and textual reasonings. To progressively enhance localisation accuracy and semantic clarity, we further design a "closer-look" mechanism that allows the model to perform progressive coarse-to-fine visits to regions of interest under refined fields of view. To support model training and evaluation, we curated a new multimodal CT dataset containing pixel-wise masks, bounding boxes, spatial prompts, and structured descriptions for visual objects constructed through an AI-assisted annotation process with human verification. Experiments on public benchmarks demonstrate consistent improvements over the SoTA, achieving up to 1.0% Dice on BTCV and 1.7% Dice on MosMed+, while additionally providing appearance reasoning outputs. The code and dataset will be available.
匹配关键词: autoregressive
---

[ACADEMIC - ARXIV]
标题: Designing Datacenter Power Delivery Hierarchies for the AI Era
作者: Grant Wilkins, Fiodar Kazhamiaka, Alok Gautam Kumbhare, Chaojie Zhang, Ricardo Bianchini
链接: https://arxiv.org/abs/2605.16255v1
完整摘要: Demand for AI accelerators is rapidly increasing rack power density, with projections approaching 1MW per deployment by 2027. This poses a major challenge for datacenter power delivery designers. As power densities increase, a datacenter designed for a different target density may strand power, i.e., may be unable to use all the power that its delivery hierarchy has provisioned. Designs must remain efficient over long datacenter lifetimes and multiple hardware generations. Power utilization is particularly important as grid power capacity is a scarce resource in the AI era. Designing an efficient power delivery hierarchy for the long run is difficult because rack placement feasibility, workload impact, and cost depend jointly on electrical topology, deployment granularity, placement policy, power oversubscription, and workload mix. Moreover, each of these factors evolve over time, have inter-dependencies across multiple resource dimensions, and generally do not lend themselves to closed-form analysis. To address this challenge, we develop a framework for evaluating datacenter power delivery designs using throughput, power, and cost metrics over realistic arrival, oversubscription, and decommissioning sequences. The framework combines projection models for GPU, compute, and storage deployments with operational factors grounded in production data from Microsoft Azure. Our results show that multi-resource stranding materially changes deployable capacity, effective capital expenditure, and delivered performance, and quantify how rising density from rack- and pod-scale AI systems shapes these outcomes. For AI datacenter design, the relevant planning objective is not installed megawatts, but deployable capacity over time.
匹配关键词: embodied AI
---

[ACADEMIC - ARXIV]
标题: A Generative AI Framework for Intelligent Utility Billing CO 2 Analytics and Sustainable Resource Optimisation
作者: Pavan Manjunath, Thomas Pruefer
链接: https://arxiv.org/abs/2605.16250v1
完整摘要: Distribution utilities are now expected to deliver bills that customers can actually read attach a defensible carbon number to every kWh sold and schedule load against grid stress and emissions constraints We propose an end-to-end framework that unifies four production-grade capabilities under one architectural roof a generative-AI agent that drafts each customers natural-language billing statement from structured numeric inputs under a constrained decoding policy a transformer-based forecaster that supplies the day-ahead consumption estimate with calibrated quantile bands
匹配关键词: embodied AI
---

[ACADEMIC - ARXIV]
标题: AI-Mediated Communication Can Steer Collective Opinion
作者: Stratis Tsirtsis, Kai Rawal, Chris Russell, Brent Mittelstadt, Sandra Wachter
链接: https://arxiv.org/abs/2605.16245v1
完整摘要: Generative artificial intelligence (AI) is increasingly integrated into the online platforms where humans exchange opinions; large language models (LLMs) now polish users' posts on LinkedIn and provide context for content shared on X. While prior work has shown that AI can express biased opinions and shape individuals' opinions during human-AI interactions, less attention has been paid to its influence on collective opinion formation when mediating human-to-human communication. We address this gap via a combination of empirical and theoretical analyses. We show empirically that LLMs from multiple popular families introduce directional biases when instructed to edit human-written texts on contested topics, for example, nudging texts in favor of gun control and against atheism. Building on this observation, we introduce a mathematical model of opinion dynamics in which an AI system sits between users on a social network, transforming the opinions they express and perceive. By analytically characterizing the equilibrium of this model and performing simulations on real social network data, we show that biases introduced by AI in human-to-human communication can be amplified through the network and shift collective opinion in their direction. In light of these findings, we investigate whether such biases are controllable by online platforms. We audit the "Explain this post" feature on X and find evidence of pro-life bias in Grok's outputs on abortion-related content, which we trace back to specific design choices. We conclude with a discussion of the broader implications of our findings in relation to ongoing legislative efforts in the European Union.
匹配关键词: embodied AI
---

[ACADEMIC - ARXIV]
标题: A Unified Generative-AI Framework for Smart Energy Infrastructure: Intelligent Gas Distribution, Utility Billing, Carbon Analytics, and Quantum-Inspired Optimisation
作者: Pavan Manjunath, Thomas pruefer
链接: https://arxiv.org/abs/2605.16232v1
完整摘要: The accelerating convergence of smart metering, generative artificial intelligence, and quantum-inspired combinatorial optimisation is reshaping how energy utilities manage physical infrastructure, customer engagement, and environmental accountability
匹配关键词: embodied AI
---

[ACADEMIC - ARXIV]
标题: Formal Methods Meet LLMs: Auditing, Monitoring, and Intervention for Compliance of Advanced AI Systems
作者: Parand A. Alamdari, Toryn Q. Klassen, Sheila A. McIlraith
链接: https://arxiv.org/abs/2605.16198v1
完整摘要: We examine one particular dimension of AI governance: how to monitor and audit AI-enabled products and services throughout the AI development lifecycle, from pre-deployment testing to post-deployment auditing. Combining principles from formal methods with SoTA machine learning, we propose techniques that enable AI-enabled product and service developers, as well as third party AI developers and evaluators, to perform offline auditing and online (runtime) monitoring of product-specific (temporally extended) behavioral constraints such as safety constraints, norms, rules and regulations with respect to black-box advanced AI systems, notably LLMs. We further provide practical techniques for predictive monitoring, such as sampling-based methods, and we introduce intervening monitors that act at runtime to preempt and potentially mitigate predicted violations. Experimental results show that by exploiting the formal syntax and semantics of Linear Temporal Logic (LTL), our proposed auditing and monitoring techniques are superior to LLM baseline methods in detecting violations of temporally extended behavioral constraints; with our approach, even small-model labelers match or exceed frontier LLM judges. Our predictive and intervening monitors significantly reduce the violation rates of LLM-based agents while largely preserving task performance. We further show through controlled experiments that LLMs' temporal reasoning shows a pronounced degradation in accuracy with increasing event distance, number of constraints, and number of propositions.
匹配关键词: embodied AI
---

[ACADEMIC - ARXIV]
标题: IVGT: Implicit Visual Geometry Transformer for Neural Scene Representation
作者: Yuqi Wu, Tianyu Hu, Wenzhao Zheng, Yuanhui Huang, Haowen Sun, Jie Zhou, Jiwen Lu
链接: https://arxiv.org/abs/2605.16258v1
完整摘要: Reconstructing coherent 3D geometry and appearance from unposed multi-view images is a fundamental yet challenging problem in computer vision. Most existing visual geometry foundation models predict explicit geometry by regressing pixel-aligned pointmaps, often suffering from redundancy and limited geometric continuity. We propose IVGT, an Implicit Visual Geometry Transformer that implicitly models continuous and coherent geometry from pose-free multi-view images. This formulation learns a continuous neural scene representation in a canonical coordinate system and supports continuous spatial queries at any 3D positions, retrieving local features to predict signed distance (SDF) values and colors using lightweight decoders. It allows direct extraction of continuous and coherent surface geometry, enabling rendering of RGB images, depth maps, and surface normal maps from arbitrary viewpoints. We train IVGT via multi-dataset joint optimization with 2D supervision and 3D geometric regularization. IVGT demonstrates generalization across scenes and achieves strong performance on various tasks, including mesh and point cloud reconstruction, novel view synthesis, depth and surface normal estimation, and camera pose estimation.
匹配关键词: robotics
---

[ACADEMIC - ARXIV]
标题: DexJoCo: A Benchmark and Toolkit for Task-Oriented Dexterous Manipulation on MuJoCo
作者: Hanwen Wang, Weizhi Zhao, Xiangyu Wang, Siyuan Huang, He Lin, Boyuan Zheng, Rongtao Xu, Gang Wang, Yao Mu, He Wang, Lue Fan, Hongsheng Li, Zhaoxiang Zhang, Tieniu Tan
链接: https://arxiv.org/abs/2605.16257v1
完整摘要: Achieving human-level manipulation requires dexterous robotic hands capable of complex object interactions. Advancing such capabilities further demands standardized benchmarks for systematic evaluation. However, existing dexterous benchmarks lack tasks that reflect the unique manipulation capabilities of dexterous hands over parallel grippers, as well as comprehensive evaluation pipelines. In this paper, we present DexJoCo, a benchmark and toolkit for task-oriented dexterous manipulation, comprising 11 functionally grounded tasks that evaluate tool-use, bimanual coordination, long-horizon execution, and reasoning. We develop a low-cost data collection system and collect 1.1K trajectories across these tasks, with support for domain randomization to assess robustness. We benchmark modern models under diverse settings, including visual and dynamics randomization, multi-task training, and action-head adaptation. Through extensive empirical analysis, we identify several important insights and common limitations of current policies in dexterous manipulation, highlighting key challenges for future research in dexterous hand robot learning. Project page available at: https://dexjoco.github.io
匹配关键词: robotics
---

[ACADEMIC - ARXIV]
标题: Offline Semantic Guidance for Efficient Vision-Language-Action Policy Distillation
作者: Jin Shi, Brady Zhang, Yishun Lu
链接: https://arxiv.org/abs/2605.16241v1
完整摘要: Billion-parameter Vision-Language-Action (VLA) policies have recently shown impressive performance in robotic manipulation, yet their size and inference cost remain major obstacles for real-time closed-loop control. We introduce \textbf{VLA-AD}, a distillation framework that uses a Vision-Language Model as an offline semantic supervisor to transfer large VLA teachers into lightweight student policies. Instead of relying only on low-level action imitation, VLA-AD augments teacher-provided 7-DoF action targets with high-level semantic guidance, including task phase anchors and multi-frame operating-direction descriptions. These auxiliary signals are used only during training: at test time, the student policy runs independently, with neither the VLA teacher nor the VLM required. We evaluate VLA-AD on three LIBERO benchmark suites. Using OpenVLA-7B as the teacher, our method produces a 158M-parameter student, yielding a $44\times$ reduction in model size while matching the teacher with only a $0.27\%$ average relative gap. The resulting policy runs at 12.5 Hz on an RTX 4090, achieving a $3.28\times$ inference speedup over OpenVLA-7B. We further show that the same semantic distillation pipeline generalizes to a different $π_{0.5}$-4B teacher, where the student outperforms the teacher on two suites and remains within $0.53\%$ on \texttt{libero\_goal}. Additional analysis indicates that phase-level supervision and multi-frame directional cues make the student less sensitive to noisy teacher actions, such as erroneous high-frequency gripper changes. Overall, VLA-AD demonstrates that offline semantic guidance from VLMs can substantially improve the efficiency, robustness, and deployability of VLA policy distillation.
匹配关键词: robotics
---

[ACADEMIC - ARXIV]
标题: Learn Where Outcomes Diverge: Efficient VLA RL via Probabilistic Chunk Masking
作者: Vaidehi Bagaria, Nikshep Grampurohit, Pulkit Verma
链接: https://arxiv.org/abs/2605.16154v1
完整摘要: Reinforcement learning (RL) allows vision-language-action (VLA) policies to generalize beyond their training distribution by optimizing directly for task success, but post-training is computationally expensive. A natural response has been to speed rollout collection through faster simulators and world models. In GRPO-based VLA RL, we find that the dominant cost lies elsewhere: gradient computation accounts for approximately 78% of wall-clock time per step in our runs, while rollout collection accounts for only 21%. Gradient cost dominates because much of this computation is spent on phases that contribute little to learning. GRPO's learning signal is driven by advantage variance: only phases where successful and failed rollouts diverge produce learning signal. However, GRPO assigns the same advantage to every chunk in a rollout. As a result, actor-update compute is spent uniformly across the trajectory, including phases the policy already handles after pre-training and supervised fine-tuning. This paper presents Probabilistic Chunk Masking (PCM), a drop-in modification to GRPO that allocates gradient computation to a small, probabilistically selected subset of chunks per trajectory. PCM scores semantic phases using success-failure action variance, a rollout-derived proxy for per-phase gradient variance, and samples a fixed chunk budget with online-updated phase-level keep probabilities. We formalize per-phase gradient variance as the quantity determines where gradient computation is useful and show that success-failure action variance provides a measurable proxy for it. PCM requires no reward model or learned critic. On three LIBERO benchmarks, PCM matches the final success rate of standard GRPO while achieving 2.38 times wall-clock speedup, 4.8 times faster gradient updates, and 60% lower peak activation memory, while backpropagating through fewer than 20% of trajectory chunks.
匹配关键词: robotics
---

[ACADEMIC - ARXIV]
标题: STABLE: Simulation-Ready Tabletop Layout Generation via a Semantics-Physics Dual System
作者: Zhen Luo, Yixuan Yang, Xudong Xu, Jinkun Hao, Zhaoyang Lyu, Feng Zheng, Jiangmiao Pang, Yanwei Fu
链接: https://arxiv.org/abs/2605.16137v1
完整摘要: Generating simulation-ready tabletop scenes from task instructions is an intriguing and promising research direction in the field of Embodied AI. However, existing task-to-scene generation methods rely exclusively on large language models (LLMs) to predict scene layouts, inevitably yielding object collisions or floating due to LLMs' inherent limitations in 3D spatial reasoning. In this paper, we present STABLE, a semantics-physics dual-system tailored for simulation-ready tabletop scene generation. STABLE consists of two complementary modules: (i) a Semantic Reasoner, a fine-tuned LLM trained on a structured tabletop scene dataset to generate coarse layouts from input task instructions, and (ii) a Physics Corrector, a physics-aware flow-based denoising model that outputs pose updates to refine layouts, which ensures the physical plausibility of scenes while preserves semantic alignment with task instructions. STABLE adopts a progressive generation paradigm: by alternating between the Semantic Reasoner and Physics Corrector, it incrementally expands the scene from task-critical objects to background objects. Experiments demonstrate that STABLE successfully generates simulation-ready tabletop scenes that strictly conform to task instructions and significantly enhances the physical validity of scenes over prior art.
匹配关键词: robotics
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
标题: NavRL++: A System-Level Framework for Improving Sim-to-Real Transfer in Reinforcement Learning-Based Robot Navigation
作者: Zhefan Xu, Hanyu Jin, Kenji Shimada
链接: https://arxiv.org/abs/2605.15559v1
完整摘要: Recent years have witnessed significant progress in autonomous navigation using reinforcement learning. However, existing approaches largely emphasize reinforcement learning framework design, such as input representations, action spaces, and reward functions, while providing limited analysis of sim-to-real transfer and insufficient insight into how training strategies affect real-world deployment performance. To bridge this gap, we not only introduce an effective RL framework but also present a complete training and deployment pipeline, along with a systematic empirical study that disentangles the key factors affecting sim-to-real transfer in reinforcement learning-based navigation, including sensor noise, perception failures, system latency, and control response. Building on insights from this analysis, we introduce perturbation-aware fine-tuning, a post-training adaptation strategy that improves transfer robustness by explicitly accounting for empirically identified domain discrepancies. To further mitigate perception degradation and enhance control smoothness in real-world deployment, we propose a Transformer-based temporal reasoning policy that leverages short-horizon observation for navigation control. We quantitatively evaluate how individual sim-to-real perturbations and training design choices impact navigation performance across environments. Experimental results demonstrate that the proposed training strategy and policy architecture outperform learning-based baselines in both static and dynamic environments, while achieving performance comparable to optimization-based planners in static settings. We validate our approach through real-world deployment on multiple robotic platforms, including aerial and legged robots, across navigation-centric tasks such as exploration and inspection, demonstrating zero-shot sim-to-real transfer.
匹配关键词: sim-to-real
---

[ACADEMIC - ARXIV]
标题: Multimodal Object Detection Under Sparse Forest-Canopy Occlusion
作者: Nitik Jain, Mangal Kothari
链接: https://arxiv.org/abs/2605.15326v1
完整摘要: Reliable detection of humans beneath forest canopy remains a difficult remote-sensing challenge due to sparse, structured, and viewpoint-dependent occlusion. This paper presents a multimodal proof-of-concept pipeline that integrates three complementary approaches: (i) experimental evaluation of LiDAR returns through vegetation to assess the feasibility of active sensing, (ii) visible--thermal image fusion using a multi-scale transform and sparse-representation framework to enhance human saliency, and (iii) synthetic-aperture image formation via Airborne Optical Sectioning (AOS) to suppress canopy clutter. A YOLOv5 detector is fine-tuned on the Teledyne FLIR thermal dataset and evaluated on thermal and fused imagery. Results show that the tested terrestrial LiDAR configuration provides limited penetration for object-level detection, while visible--thermal fusion improves target visibility in low-contrast scenes and AOS enhances ground-plane detection in synthetic forest imagery. The fine-tuned YOLOv5 achieves a mean average precision of $\sim$0.83 on the top three FLIR classes. These findings establish an initial baseline for UAV-deployable search-and-rescue and surveillance systems operating in forested environments, and motivate future work on dedicated forest datasets and real-time multimodal integration.
匹配关键词: sim-to-real
---

[ACADEMIC - ARXIV]
标题: Causal Forcing++: Scalable Few-Step Autoregressive Diffusion Distillation for Real-Time Interactive Video Generation
作者: Min Zhao, Hongzhou Zhu, Kaiwen Zheng, Zihan Zhou, Bokai Yan, Xinyuan Li, Xiao Yang, Chongxuan Li, Jun Zhu
链接: https://arxiv.org/abs/2605.15141v1
完整摘要: Real-time interactive video generation requires low-latency, streaming, and controllable rollout. Existing autoregressive (AR) diffusion distillation methods have achieved strong results in the chunk-wise 4-step regime by distilling bidirectional base models into few-step AR students, but they remain limited by coarse response granularity and non-negligible sampling latency. In this paper, we study a more aggressive setting: frame-wise autoregression with only 1--2 sampling steps. In this regime, we identify the initialization of a few-step AR student as the key bottleneck: existing strategies are either target-misaligned, incapable of few-step generation, or too costly to scale. We propose \textbf{Causal Forcing++}, a principled and scalable pipeline that uses \emph{causal consistency distillation} (causal CD) for few-step AR initialization. The core idea is that causal CD learns the same AR-conditional flow map as causal ODE distillation, but obtains supervision from a single online teacher ODE step between adjacent timesteps, avoiding the need to precompute and store full PF-ODE trajectories. This makes the initialization both more efficient and easier to optimize. The resulting pipeline, \ours, surpasses the SOTA 4-step chunk-wise Causal Forcing under the \textit{\textbf{frame-wise 2-step setting}} by 0.1 in VBench Total, 0.3 in VBench Quality, and 0.335 in VisionReward, while reducing first-frame latency by 50\% and Stage 2 training cost by $\sim$$4\times$. We further extend the pipeline to action-conditioned world model generation in the spirit of Genie3. Project Page: https://github.com/thu-ml/Causal-Forcing and https://github.com/shengshu-ai/minWM .
匹配关键词: sim-to-real
---

[ACADEMIC - ARXIV]
标题: IVGT: Implicit Visual Geometry Transformer for Neural Scene Representation
作者: Yuqi Wu, Tianyu Hu, Wenzhao Zheng, Yuanhui Huang, Haowen Sun, Jie Zhou, Jiwen Lu
链接: https://arxiv.org/abs/2605.16258v1
完整摘要: Reconstructing coherent 3D geometry and appearance from unposed multi-view images is a fundamental yet challenging problem in computer vision. Most existing visual geometry foundation models predict explicit geometry by regressing pixel-aligned pointmaps, often suffering from redundancy and limited geometric continuity. We propose IVGT, an Implicit Visual Geometry Transformer that implicitly models continuous and coherent geometry from pose-free multi-view images. This formulation learns a continuous neural scene representation in a canonical coordinate system and supports continuous spatial queries at any 3D positions, retrieving local features to predict signed distance (SDF) values and colors using lightweight decoders. It allows direct extraction of continuous and coherent surface geometry, enabling rendering of RGB images, depth maps, and surface normal maps from arbitrary viewpoints. We train IVGT via multi-dataset joint optimization with 2D supervision and 3D geometric regularization. IVGT demonstrates generalization across scenes and achieves strong performance on various tasks, including mesh and point cloud reconstruction, novel view synthesis, depth and surface normal estimation, and camera pose estimation.
匹配关键词: speech synthesis
---

[ACADEMIC - ARXIV]
标题: Real-time Speech Restoration using Data Prediction Mean Flows
作者: Sebastian Braun
链接: https://arxiv.org/abs/2605.16251v1
完整摘要: Generative models are capable to address difficult problems with non-unique solutions like bandwidth extension and gap filling, removing highly non-linear artifacts from codecs, clipping and distortion, as opposed to removing linear additive components like noise and reverb. While large offline processing models have shown impressive results, these tasks have not been solved with real-time capable models with low latency and compute. We propose a few-step flow matching model using Data Prediction Mean Flows in combination with suitable novel low-latency architecture to make flow matching models an attractive choice under theses constraints. Compared to state-of-the-art, our proposed mean flow model uses 120x less compute and introduces no algorithmic latency other than the STFT, while achieving similar audio quality.
匹配关键词: speech synthesis
---

[ACADEMIC - ARXIV]
标题: Property-Guided LLM Program Synthesis for Planning
作者: Augusto B. Corrêa, André G. Pereira, Jendrik Seipp
链接: https://arxiv.org/abs/2605.16142v1
完整摘要: LLMs have shown impressive success in program synthesis, discovering programs that surpass prior solutions. However, these approaches rely on simple numeric scores to signal program quality, such as the value of the solution or the number of passed tests. Because a score offers no guidance on why a program failed, the system must generate and evaluate many candidates hoping some succeed, increasing LLM inference and evaluation costs. We study a different approach: property-guided LLM program synthesis. Instead of scoring programs after evaluation, we check whether a candidate satisfies a formally defined property. When the property is violated, we stop the evaluation early and provide the LLM with a concrete counterexample showing exactly how the program failed. This feedback drastically reduces both the number of program generations and the evaluation cost, and can guide the LLM to generate stronger programs. We evaluate this approach on PDDL planning domains, asking the LLM to synthesize direct heuristic functions: every state reachable by strictly improving transitions has a strictly improving successor. A heuristic with this property leads hill-climbing algorithm directly to a goal state. A counterexample-guided repair loop generates one candidate program, checks the property over a training set, and returns the first case that violates the property. We evaluate our approach on ten planning domains with an out-of-distribution test set. The synthesized heuristics are effectively direct on virtually all test tasks, and compared to the best prior generation method our approach generates seven times fewer programs per domain on average, solves more tasks without using search, and requires several orders of magnitude less computation to evaluate candidates. Whenever a problem admits a verifiable property, property-guided LLM synthesis can reduce cost and improve program quality.
匹配关键词: speech synthesis
---

[ACADEMIC - ARXIV]
标题: Surrogate Neural Architecture Codesign Package (SNAC-Pack)
作者: Jason Weitz, Dmitri Demler, Benjamin Hawks, Aaron Wang, Nhan Tran, Javier Duarte
链接: https://arxiv.org/abs/2605.16138v1
完整摘要: Neural architecture search (NAS) is a powerful approach for automating model design, but existing methods often optimize for accuracy alone or rely on proxy metrics such as bit operations (BOPs) that correlate poorly with hardware cost. This gap is particularly large for FPGA deployment, where cost is dominated by a multi-dimensional budget of lookup tables, DSPs, flip-flops, BRAM, and latency. We present the Surrogate Neural Architecture Codesign Package (SNAC-Pack), an open-source AutoML framework for hardware-aware neural architecture codesign and end-to-end FPGA deployment. SNAC-Pack runs a multi-objective global search with Optuna and NSGA-II, loading trials to a shared SQLite store that enables parallel workers across compute nodes. A hardware surrogate model outputs per-trial resource and latency estimates, avoiding the synthesis cost that would otherwise dominate the search loop. A local search stage then applies quantization-aware training (QAT) together with iterative magnitude pruning in a combined compression loop, after which the final model is synthesized to FPGA firmware via the hls4ml Python library. A YAML configuration and an optional agentic frontend let users run the pipeline on new datasets without modifying the framework. We demonstrate SNAC-Pack on jet classification at the Large Hadron Collider and superconducting qubit readout, discovering compact architectures that match or exceed strong baselines on the task metric while reducing FPGA resource utilization and, in the qubit readout case, reducing the design space exploration process from months of manual fine-tuning to hours of automated search.
匹配关键词: speech synthesis
---

[ACADEMIC - ARXIV]
标题: GenShield: Unified Detection and Artifact Correction for AI-Generated Images
作者: Zhipei Xu, Xuanyu Zhang, Youmin Xu, Qing Huang, Shen Chen, Taiping Yao, Shouhong Ding, Jian Zhang
链接: https://arxiv.org/abs/2605.16122v1
完整摘要: Diffusion-based image synthesis has made AI-generated images (AIGI) increasingly photorealistic, raising urgent concerns about authenticity in applications such as misinformation detection, digital forensics, and content moderation. Despite the substantial advances in AIGI detection, how to correct detected AI-generated images with visible artifacts and restore realistic appearance remains largely underexplored. Moreover, few existing work has established the connection between AIGI detection and artifact correction. To fill this gap, we propose GenShield, a unified autoregressive framework that jointly performs explainable AIGI detection and controllable artifact correction in a closed loop from diagnosis to restoration, revealing a mutually reinforcing relationship between these two tasks. We further introduce a Visual Chain-of-Thought based curriculum learning strategy that enables self-explained, multi-step ``diagnose-then-repair'' correction with an explicit stopping criterion. A high-quality dataset with large-scale ``artifact-restored'' pairs is also constructed alongside a unified evaluation pipeline. Extensive experiments on our correction benchmark and mainstream AIGI detection benchmarks demonstrate state-of-the-art performance and strong generalization of our method. The code is available at https://github.com/zhipeixu/GenShield.
匹配关键词: speech synthesis
---

[ACADEMIC - ARXIV]
标题: Improving Automatic Speech Recognition for Speakers Treated for Oral Cancer using Data Augmentation and LLM Error Correction
作者: Hidde Folkertsma, Thomas Tienkamp, Sebastiaan de Visscher, Max Witjes, Rob van Son, Jiapan Guo, Bence Mark Halpern
链接: https://arxiv.org/abs/2605.15854v1
完整摘要: In recent years, the performance of automatic speech recognition (ASR) systems has made considerable progress. Unfortunately, for people with speech impairments, such as people treated for oral cancer (OC), ASR performance is still lagging behind. The scarcity and variability of OC speech data makes development of ASR models for this type of speech difficult. In this work, we use data augmentation and large language model (LLM) error correction to mitigate this problem. We apply various augmentation techniques on a corpus of Dutch oral cancer speech to create synthetic data, and evaluate their effect on ASR performance. We finetune Whisper and Massively Multilingual Speech (MMS) models for each augmentation technique and observe, on average, an 8% relative decrease in Word Error Rate (WER) when including data created using text-to-speech (TTS). When employing LLMs for error correction, we see a further 21.4-26.2% relative decrease in WER for finetuned ASR models and a 10.0% relative decrease for non-finetuned models. Overall, we achieve a 40% relative WER decrease for Whisper and a 50% relative WER decrease for MMS, indicating that a combination of data augmentation and LLM correction is a viable strategy for the recognition of OC speech.
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
标题: Beyond Explained Variance: A Cautionary Tale of PCA
作者: Gionni Marchetti
链接: https://arxiv.org/abs/2605.13520v1
完整摘要: We address shortcomings of principal component analysis (PCA) for visualizing high-dimensional data lying on a nonlinear low-dimensional manifold via two-dimensional scatterplots, focusing on a fossil teeth dataset from the early mammalian insectivore Kuehneotherium. While the PCA scatterplot reported by Jolliffe and Cadima (Philosophical Transactions of the Royal Society A, 2016) shows clustering in the region where PC2 < 0, our analysis based on t-SNE and persistent homology (PH) reveals a ring-like structure with no evident clustering and intrinsic dimensionality equal to one. We further propose a generative probabilistic-geometric model in which the data are sampled uniformly from a unit circle. Under this model, pairwise cosine distances follow an arcsine distribution, in qualitative agreement with the observed U-shaped distribution, thereby independently supporting the analysis based on tt t-SNE and persistent homology.
匹配关键词: TTS
---

[ACADEMIC - ARXIV]
标题: PoDAR: Power-Disentangled Audio Representation for Generative Modeling
作者: Alejandro Luebs, Mithilesh Vaidya, Ishaan Kumar, Sumukh Badam, Stephen W. Bailey, Matthew Bendel, Jose Sotelo, Xingzhe He
链接: https://arxiv.org/abs/2605.10084v1
完整摘要: The performance of audio latent diffusion models is primarily governed by generator expressivity and the modelability of the underlying latent space. While recent research has focused primarily on the former, as well as improving the reconstruction fidelity of audio codecs, we demonstrate that latent modelability can be significantly improved through explicit factor disentanglement. We present PoDAR (Power-Disentangled Audio Representation), a framework that utilizes a randomized power augmentation and latent consistency objective to decouple signal power from invariant semantic content. This factorization makes the latent space easier to model, which both accelerates the convergence of downstream generative models and improves final overall performance. When applied to a Stable Audio 1.0 VAE with an F5-TTS generator, PoDAR achieves about a $2\times$ acceleration in convergence to match baseline performance, while increasing final speaker similarity by 0.055 and UTMOS by 0.22 on the LibriSpeech-PC dataset. Furthermore, isolating power into dedicated channels enables the application of CFG exclusively to power-invariant content, effectively extending the stable guidance regime to higher scales.
匹配关键词: TTS
---

[ACADEMIC - ARXIV]
标题: Kinetic-Optimal Scheduling with Moment Correction for Metric-Induced Discrete Flow Matching in Zero-Shot Text-to-Speech
作者: Dong Yang, Yiyi Cai, Haoyu Zhang, Yuki Saito, Hiroshi Saruwatari
链接: https://arxiv.org/abs/2605.09386v1
完整摘要: Metric-induced discrete flow matching (MI-DFM) exploits token-latent geometry for discrete generation, but its practical use is limited by two issues: heuristic schedulers requiring hyperparameter search, and finite-step path-tracking error from its first-order continuous-time Markov chain (CTMC) solver. We address both issues. First, we derive a kinetic-optimal scheduler for prescribed scalar-parameterized probability paths, and instantiate it for MI-DFM as a training-free numerical schedule that traverses the path at constant Fisher-Rao speed. Second, we introduce a finite-step moment correction that adjusts the jump probability while preserving the CTMC jump destination distribution. We validate the resulting method, GibbsTTS, on codec-based zero-shot text-to-speech (TTS). Under controlled comparisons with a unified architecture and large-scale dataset, GibbsTTS achieves the best objective naturalness and is preferred in subjective evaluations over masked discrete generative baselines. Additionally, in comparison with the evaluated state-of-the-art TTS systems, GibbsTTS shows strong speaker similarity, achieving the highest similarity on three of four test sets and ranking second on the fourth. Project page: https://ydqmkkx.github.io/GibbsTTSProject
匹配关键词: TTS
---

[ACADEMIC - ARXIV]
标题: From Flat Language Labels to Typological Priors: Structured Language Conditioning for Multilingual Speech-to-Speech Translation
作者: Yu Pan, Yang Hou, Xiongfei Wu, Liang Zhang, Yves Le Traon, Lei Ma, Jianjun Zhao
链接: https://arxiv.org/abs/2605.16026v1
完整摘要: Compositional speech-to-speech translation (S2ST) systems built upon speech large language models (SpeechLLMs) have recently shown promising performance. However, existing S2ST systems often either neglect source-language information or encode it through a language-as-label paradigm, representing each source language as an independent flat embedding. Such a design overlooks systematic linguistic structure shared across languages, which may limit data-efficient multilingual adaptation when supervised S2ST data are scarce. To address this issue, we propose S2ST-Omni 2, a many-to-one compositional S2ST framework that systematically reformulates multilingual language conditioning from flat language labels to structured typological priors. Specifically, S2ST-Omni 2 revisits language conditioning at three levels: typology-informed hierarchical language encoding for structured source-language representation, dynamically-gated language-aware Dual-CTC for content-adaptive acoustic modulation, and typology-aware LLM prompting for decoder-side linguistic guidance. Experiments on CVSS-C show that S2ST-Omni 2 achieves superior average performance among representative S2ST approaches across BLEU, COMET, ASR-BLEU, and BLASER 2.0 under the adopted evaluation protocol. Ablation studies indicate that the proposed representation-level, acoustic-level, and decoding-level strategies provide complementary benefits. Moreover, controlled data-budget analyses and a Japanese-to-English evaluation using only approximately 3 hours of supervised training data suggest that explicit typological priors provide useful inductive biases for data-efficient multilingual S2ST.
匹配关键词: ASR
---

[ACADEMIC - ARXIV]
标题: Improving Automatic Speech Recognition for Speakers Treated for Oral Cancer using Data Augmentation and LLM Error Correction
作者: Hidde Folkertsma, Thomas Tienkamp, Sebastiaan de Visscher, Max Witjes, Rob van Son, Jiapan Guo, Bence Mark Halpern
链接: https://arxiv.org/abs/2605.15854v1
完整摘要: In recent years, the performance of automatic speech recognition (ASR) systems has made considerable progress. Unfortunately, for people with speech impairments, such as people treated for oral cancer (OC), ASR performance is still lagging behind. The scarcity and variability of OC speech data makes development of ASR models for this type of speech difficult. In this work, we use data augmentation and large language model (LLM) error correction to mitigate this problem. We apply various augmentation techniques on a corpus of Dutch oral cancer speech to create synthetic data, and evaluate their effect on ASR performance. We finetune Whisper and Massively Multilingual Speech (MMS) models for each augmentation technique and observe, on average, an 8% relative decrease in Word Error Rate (WER) when including data created using text-to-speech (TTS). When employing LLMs for error correction, we see a further 21.4-26.2% relative decrease in WER for finetuned ASR models and a 10.0% relative decrease for non-finetuned models. Overall, we achieve a 40% relative WER decrease for Whisper and a 50% relative WER decrease for MMS, indicating that a combination of data augmentation and LLM correction is a viable strategy for the recognition of OC speech.
匹配关键词: ASR
---

[ACADEMIC - ARXIV]
标题: Mind the Gap: Impact of Synthetic Conversational Data on Multi-Talker ASR and Speaker Diarization
作者: Alexander Polok, Ivan Medennikov, Jan Černocký, Shinji Watanabe, Lukáš Burget, Samuele Cornell
链接: https://arxiv.org/abs/2605.15442v1
完整摘要: Recent breakthroughs in multi-talker ASR (MT-ASR) and speaker diarization (SD) rely on synthetic data to mitigate the scarcity of large-scale conversational recordings, yet the impact of specific simulation choices remains poorly understood. To mind the gap between simulated mixtures and real-world interactions, we present a study of synthetic data generation for leading MT-ASR (DiCoW) and SD (Sortformer) systems. By introducing FastMSS, a highly efficient open-source simulator, we analyze turn-taking dynamics, source domain, acoustic augmentation, and data mixing strategies. Our findings reveal that optimal simulation recipes are highly task-dependent: increasing speech overlap benefits ASR but degrades diarization. Furthermore, broad source diversity consistently outperforms exact domain matching. Ultimately, synthetic-only training approaches real-data baselines, and combining simulated data with real recordings yields substantial gains over real-only training across both tasks.
匹配关键词: ASR
---

[ACADEMIC - ARXIV]
标题: nASR: An End-to-End Trainable Neural Layer for Channel-Level EEG Artifact Subspace Reconstruction in Real-Time BCI
作者: Shantanu Sarkar, Jose L. Contreras-Vidal
链接: https://arxiv.org/abs/2605.14941v1
完整摘要: Electroencephalogram (EEG) signals are highly susceptible to artifacts, resulting in a low signal-to-noise ratio which makes extraction of meaningful neural information challenging. Artifact Subspace Reconstruction (ASR) is one of the most widely used artifact filtering techniques in EEG-based BCI applications, owing to its real-time applicability. ASR reconstructs artifact-free signals by operating in Principal Component (PC) space within sliding windows. However, ASR performance is critically sensitive to its threshold parameter - an incorrect threshold risks removing task-relevant neural features alongside artifacts. Furthermore, since PCs are linear combinations of all channels, subspace reconstruction in PC space may alter the underlying data structure, potentially discarding essential neural information. To address these limitations, we propose nASR, a novel end-to-end trainable Keras layer that jointly optimizes artifact rejection and downstream decoding. nASR introduces two trainable threshold parameters: K, which governs artifact detection in PC variance space, and L, which quantifies eigen-spread to pinpoint the primary artifact--contributing channels, enabling selective channel-level reconstruction that preserves clean channel information. An ablation study comprising five model variants (m01 - m05), evaluated across two subjects from the BCI Competition IV Dataset 1, confirms that nASR variants consistently outperform traditional ASR on test classification metrics, while achieving a 6-8x reduction in inference time, making nASR a strong candidate for real-time BCI applications demanding both low latency and high decoding performance.
匹配关键词: ASR
---

[ACADEMIC - ARXIV]
标题: A Calculus-Based Framework for Determining Vocabulary Size in End-to-End ASR
作者: Sunil Kumar Kopparapu
链接: https://arxiv.org/abs/2605.14427v1
完整摘要: In hybrid automatic speech recognition (ASR) systems, the vocabulary size is unambiguous, typically determined by the number of phones, bi-phones, or tri-phones present in the language. In contrast, end-to-end ASR systems derive their vocabulary, often referred to as tokens from the text corpus used for training. The choice and, more importantly, the size of this vocabulary is a critical hyper-parameter in training end-to-end ASR systems. Tokenization algorithms such as Byte Pair Encoding (BPE), WordPiece, and Unigram Language Model (ULM) use the vocabulary size as an input hyper-parameter to generate the sub-words employed during ASR training. Popular toolkits like ESPNet provide a fixed vocabulary size in their training recipes, but there is little documentation or discussion in the literature regarding how these values are determined. Recent work [1] has formalized an approach to identify the vocabulary size best suited for end-to-end ASR, introducing a cost function framework that treats the tokenization process as a black box. In this paper, we build upon that foundation by curve fitting the training data and using the principle of first and second derivative tests in calculus to formally estimate the vocabulary size hyper-parameter. We demonstrate the utility and usefulness of our approach by applying it on a standard Librispeech corpus and show that the optimal choice of vocabulary size hyper-parameter improves the performance of the ASR. The main contribution of this paper in formalizing an approach to identify the vocabulary size best suited for training an end-to-end ASR system.
匹配关键词: ASR
---

[ACADEMIC - ARXIV]
标题: Hierarchical Image Tokenization for Multi-Scale Image Super Resolution
作者: Isma Hadji, Enrique Sanchez, Adrian Bulat, Brais Martinez, Georgios Tzimiropoulos
链接: https://arxiv.org/abs/2605.14891v1
完整摘要: We introduce a multi-scale Image Super Resolution (ISR) method building on recent advances in Visual Auto-Regressive (VAR) modeling. VAR models break image tokenization into additive, gradually increasing scales, using Residual Quantization (RQ), an approach that aligns perfectly with our target ISR task. Previous works taking advantage of this synergy suffer from two main shortcomings. First, due to the limitations in RQ, they only generate images at a predefined fixed scale, failing to map intermediate outputs to the corresponding image scales. They also rely on large backbones or a large corpus of annotated data to achieve better performance. To address both shortcomings, we introduce two novel components to the VAR training for ISR, aiming at increasing its flexibility and reducing its complexity. In particular, we introduce a) a \textbf{Hierarchical Image Tokenization (HIT)} approach that progressively represents images at different scales while enforcing token overlap across scales, and b) a \textbf{Direct Preference Optimization (DPO) regularization term} that, relying solely on the (LR,HR) pair, encourages the transformer to produce the latter over the former. Our proposed HIT acts as a strong inductive bias for the VAR training, resulting in a small model (300M params vs 1B params of VARSR), that achieves state-of-the-art results without external training data, and that delivers multi-scale outputs with a single forward pass.
匹配关键词: DPO
---

[ACADEMIC - ARXIV]
标题: PRISM-X: Experiments on Personalised Fine-Tuning with Human and Simulated Users
作者: Hannah Rose Kirk, Liu Leqi, Fanzhi Zeng, Henry Davidson, Bertie Vidgen, Christopher Summerfield, Scott A. Hale
链接: https://arxiv.org/abs/2605.13307v1
完整摘要: Personalisation is a standard feature of conversational AI systems used by millions; yet, the efficacy of personalisation methods is often evaluated in academic research using simulated users rather than real people. This raises questions about how users and their simulated counterparts differ in interaction patterns and judgements, as well as whether personalisation is best achieved through context-based prompting or weight-based fine-tuning. Here, in a large-scale within-subject experiment, we re-recruit 530 participants from 52 countries two years after they gave their preferences in the PRISM dataset (Kirk et al., 2024) to evaluate personalised and non-personalised language models in blinded multi-turn conversations. We find preference fine-tuning (P-DPO, Li et al., 2024) significantly outperforms both a generic model and personalised prompting but adapting to individual preference data yields marginal gains over training on pooled preferences from a diverse population. Beyond length biases, fine-tuning amplifies sycophancy and relationship-seeking behaviours that people reward in short-term evaluations but which may introduce deleterious long-term consequences. Replicating this within-subject experiment with simulated users recovers aggregate model hierarchies but simulators perform far below human self-consistency baselines for individual judgements, discuss different topics, exhibit amplified position biases, and produce feedback dynamics that diverge from humans.
匹配关键词: DPO
---

[ACADEMIC - ARXIV]
标题: DocAtlas: Multilingual Document Understanding Across 80+ Languages
作者: Ahmed Heakl, Youssef Mohamed, Abdullah Sohail, Rania Elbadry, Ahmed Nassar, Peter W. J. Staar, Fahad Shahbaz Khan, Imran Razzak, Salman Khan
链接: https://arxiv.org/abs/2605.12623v1
完整摘要: Multilingual document understanding remains limited for low-resource languages due to scarce training data and model-based annotation pipelines that perpetuate existing biases. We introduce DocAtlas, a framework that constructs high-fidelity OCR datasets and benchmarks covering 82 languages and 9 evaluation tasks. Our dual pipelines, differential rendering of native DOCX documents and synthetic LaTeX-based generation for right-to-left scripts produce precise structural annotations in a unified DocTag format encoding layout, text, and component types, without learned models for core annotation. Evaluating 16 state-of-the-art models reveals persistent gaps in low-resource scripts. We show that Direct Preference Optimization (DPO) using rendering-derived ground truth as positive signal achieves stable multilingual adaptation, improving both in-domain (+1.9%) and out-of-domain (+1.8%) accuracy without measurable base-language degradation, where supervised fine-tuning degrades out-of-domain performance by up to 21%. Our best variant, DocAtlas-DeepSeek, improves +1.7% over the strongest baseline.
匹配关键词: DPO
---

[ACADEMIC - ARXIV]
标题: TokenRatio: Principled Token-Level Preference Optimization via Ratio Matching
作者: Truong Nguyen, Tien-Phat Nguyen, Linh Ngo Van, Duy Minh Ho Nguyen, Khoa D. Doan, Trung Le
链接: https://arxiv.org/abs/2605.12288v2
完整摘要: Direct Preference Optimization (DPO) is a widely used RL-free method for aligning language models from pairwise preferences, but it models preferences over full sequences even though generation is driven by per-token decisions. Existing token-level extensions typically decompose a sequence-level Bradley-Terry objective across timesteps, leaving per-prefix (state-wise) optimality implicit. We study how to recover token-level preference optimality using only standard sequence-level pairwise comparisons. We introduce Token-level Bregman Preference Optimization (TBPO), which posits a token-level Bradley-Terry preference model over next-token actions conditioned on the prefix, and derive a Bregman-divergence density-ratio matching objective that generalizes the logistic/DPO loss while preserving the optimal policy induced by the token-level model and maintaining DPO-like simplicity. We introduce two instantiations: TBPO-Q, which explicitly learns a lightweight state baseline, and TBPO-A, which removes the baseline through advantage normalization. Across instruction following, helpfulness/harmlessness, and summarization benchmarks, TBPO improves alignment quality and training stability and increases output diversity relative to strong sequence-level and token-level baselines.
匹配关键词: DPO
---

[ACADEMIC - ARXIV]
标题: SyncDPO: Enhancing Temporal Synchronization in Video-Audio Joint Generation via Preference Learning
作者: Xin Cheng, Xihua Wang, Ying Ba, Yuyue Wang, Kaisi Guan, Yinbo Wang, Wenpu Li, Ruihua Song
链接: https://arxiv.org/abs/2605.12179v1
完整摘要: Recent advancements in video-audio joint generation have achieved remarkable success in semantic correspondence. However, achieving precise temporal synchronization, which requires fine-grained alignment between audio events and their visual triggers, remains a challenging problem. The post-training method for joint generation is largely dominated by Supervised Fine-Tuning, but the commonly used Mean Squared Error loss provides insufficient penalties for subtle temporal misalignments. Direct Preference Optimization offers an alternative by introducing explicit misaligned counterparts to better improve temporal sensitivity. In this paper we propose a post-training framework SyncDPO, leveraging DPO to improve the temporal sensitivity of V-A joint generation. Conventional DPO pipelines typically depend on costly sampling-and-ranking procedures to construct preference pairs, resulting in substantial computational cost. To improve efficiency, we introduce a suite of on-the-fly rule-based negative construction strategies that distort temporal structures without incurring additional annotation or sampling. We demonstrate that the temporal alignment capability can be effectively reinforced by providing explicit negative supervision through temporally distorted V-A pairs. Accordingly, we implement a curriculum learning strategy that progressively increases the difficulty of negative samples, transitioning from coarse misalignment to subtle inconsistencies. Extensive objective and subjective experiments across four diverse benchmarks, ranging from ambient sound videos to human speech videos, demonstrate that SyncDPO significantly outperforms other methods in improving model's temporal alignment capability. It also demonstrates superior generalization on out-of-distribution benchmark by capturing intrinsic motion-sound dynamics. Demo and code is available in https://syncdpo.github.io/syncdpo/.
匹配关键词: DPO
---

[ACADEMIC - ARXIV]
标题: Designing Datacenter Power Delivery Hierarchies for the AI Era
作者: Grant Wilkins, Fiodar Kazhamiaka, Alok Gautam Kumbhare, Chaojie Zhang, Ricardo Bianchini
链接: https://arxiv.org/abs/2605.16255v1
完整摘要: Demand for AI accelerators is rapidly increasing rack power density, with projections approaching 1MW per deployment by 2027. This poses a major challenge for datacenter power delivery designers. As power densities increase, a datacenter designed for a different target density may strand power, i.e., may be unable to use all the power that its delivery hierarchy has provisioned. Designs must remain efficient over long datacenter lifetimes and multiple hardware generations. Power utilization is particularly important as grid power capacity is a scarce resource in the AI era. Designing an efficient power delivery hierarchy for the long run is difficult because rack placement feasibility, workload impact, and cost depend jointly on electrical topology, deployment granularity, placement policy, power oversubscription, and workload mix. Moreover, each of these factors evolve over time, have inter-dependencies across multiple resource dimensions, and generally do not lend themselves to closed-form analysis. To address this challenge, we develop a framework for evaluating datacenter power delivery designs using throughput, power, and cost metrics over realistic arrival, oversubscription, and decommissioning sequences. The framework combines projection models for GPU, compute, and storage deployments with operational factors grounded in production data from Microsoft Azure. Our results show that multi-resource stranding materially changes deployable capacity, effective capital expenditure, and delivered performance, and quantify how rising density from rack- and pod-scale AI systems shapes these outcomes. For AI datacenter design, the relevant planning objective is not installed megawatts, but deployable capacity over time.
匹配关键词: constitutional AI
---

[ACADEMIC - ARXIV]
标题: A Generative AI Framework for Intelligent Utility Billing CO 2 Analytics and Sustainable Resource Optimisation
作者: Pavan Manjunath, Thomas Pruefer
链接: https://arxiv.org/abs/2605.16250v1
完整摘要: Distribution utilities are now expected to deliver bills that customers can actually read attach a defensible carbon number to every kWh sold and schedule load against grid stress and emissions constraints We propose an end-to-end framework that unifies four production-grade capabilities under one architectural roof a generative-AI agent that drafts each customers natural-language billing statement from structured numeric inputs under a constrained decoding policy a transformer-based forecaster that supplies the day-ahead consumption estimate with calibrated quantile bands
匹配关键词: constitutional AI
---

[ACADEMIC - ARXIV]
标题: AI-Mediated Communication Can Steer Collective Opinion
作者: Stratis Tsirtsis, Kai Rawal, Chris Russell, Brent Mittelstadt, Sandra Wachter
链接: https://arxiv.org/abs/2605.16245v1
完整摘要: Generative artificial intelligence (AI) is increasingly integrated into the online platforms where humans exchange opinions; large language models (LLMs) now polish users' posts on LinkedIn and provide context for content shared on X. While prior work has shown that AI can express biased opinions and shape individuals' opinions during human-AI interactions, less attention has been paid to its influence on collective opinion formation when mediating human-to-human communication. We address this gap via a combination of empirical and theoretical analyses. We show empirically that LLMs from multiple popular families introduce directional biases when instructed to edit human-written texts on contested topics, for example, nudging texts in favor of gun control and against atheism. Building on this observation, we introduce a mathematical model of opinion dynamics in which an AI system sits between users on a social network, transforming the opinions they express and perceive. By analytically characterizing the equilibrium of this model and performing simulations on real social network data, we show that biases introduced by AI in human-to-human communication can be amplified through the network and shift collective opinion in their direction. In light of these findings, we investigate whether such biases are controllable by online platforms. We audit the "Explain this post" feature on X and find evidence of pro-life bias in Grok's outputs on abortion-related content, which we trace back to specific design choices. We conclude with a discussion of the broader implications of our findings in relation to ongoing legislative efforts in the European Union.
匹配关键词: constitutional AI
---

[ACADEMIC - ARXIV]
标题: A Unified Generative-AI Framework for Smart Energy Infrastructure: Intelligent Gas Distribution, Utility Billing, Carbon Analytics, and Quantum-Inspired Optimisation
作者: Pavan Manjunath, Thomas pruefer
链接: https://arxiv.org/abs/2605.16232v1
完整摘要: The accelerating convergence of smart metering, generative artificial intelligence, and quantum-inspired combinatorial optimisation is reshaping how energy utilities manage physical infrastructure, customer engagement, and environmental accountability
匹配关键词: constitutional AI
---

[ACADEMIC - ARXIV]
标题: Formal Methods Meet LLMs: Auditing, Monitoring, and Intervention for Compliance of Advanced AI Systems
作者: Parand A. Alamdari, Toryn Q. Klassen, Sheila A. McIlraith
链接: https://arxiv.org/abs/2605.16198v1
完整摘要: We examine one particular dimension of AI governance: how to monitor and audit AI-enabled products and services throughout the AI development lifecycle, from pre-deployment testing to post-deployment auditing. Combining principles from formal methods with SoTA machine learning, we propose techniques that enable AI-enabled product and service developers, as well as third party AI developers and evaluators, to perform offline auditing and online (runtime) monitoring of product-specific (temporally extended) behavioral constraints such as safety constraints, norms, rules and regulations with respect to black-box advanced AI systems, notably LLMs. We further provide practical techniques for predictive monitoring, such as sampling-based methods, and we introduce intervening monitors that act at runtime to preempt and potentially mitigate predicted violations. Experimental results show that by exploiting the formal syntax and semantics of Linear Temporal Logic (LTL), our proposed auditing and monitoring techniques are superior to LLM baseline methods in detecting violations of temporally extended behavioral constraints; with our approach, even small-model labelers match or exceed frontier LLM judges. Our predictive and intervening monitors significantly reduce the violation rates of LLM-based agents while largely preserving task performance. We further show through controlled experiments that LLMs' temporal reasoning shows a pronounced degradation in accuracy with increasing event distance, number of constraints, and number of propositions.
匹配关键词: constitutional AI
---

[ACADEMIC - ARXIV]
标题: DebiasRAG: A Tuning-Free Path to Fair Generation in Large Language Models through Retrieval-Augmented Generation
作者: Rui Chu, Bingyin Zhao, Thanh Quoc Hung Le, Duy Cao Hoang, Huawei Lin, Ping Li, Weijie Zhao, Khoa D Doan, Yingjie Lao
链接: https://arxiv.org/abs/2605.16113v1
完整摘要: Large language models (LLMs) have achieved unprecedented success due to their exceptional generative capabilities. However, because they depend on knowledge encapsulated from training corpora, they may produce hallucinations, stereotypes, and socially biased content. In particular, LLMs are prone to prejudiced responses involving race, gender, and age, which are collectively referred to as social biases. Prior studies have used fine-tuning and prompt engineering to mitigate such biases in LLMs, but these methods require additional training resources or domain knowledge to design the framework. Moreover, they may degrade the original capabilities of LLMs and often overlook the need for dynamic debiasing contexts for fairer inference. In this paper, we propose DebiasRAG, a novel tuning-free and dynamic query-specific debiasing framework based on retrieval-augmented generation (RAG). DebiasRAG improves fairness while preserving the intrinsic properties of LLMs, such as representation ability. DebiasRAG consists of three stages: (1) query-specific debiasing candidate generation; (2) context candidate pool construction; and (3) gradient-updated debiasing-guided context piece reranking. First, DebiasRAG leverages self-diagnosed bias contexts relevant to the query through regular retrieval, where the bias contexts are prepared offline by the DebiasRAG provider. Given the query-specific bias contexts, DebiasRAG reversely produces debiasing contexts, which are provided as additional fairness constraints for LLM outputs. Second, a regular RAG retrieval process produces query-related contexts from the regular RAG document database, such as a chunked Wikipedia dataset.
匹配关键词: RAG
---

[ACADEMIC - ARXIV]
标题: Towards Generalization of Block Attention via Automatic Segmentation and Block Distillation
作者: Shuaiyi Li, Zhisong Zhang, Yan Wang, Lei Zhu, Dongyang Ma, Chenlong Deng, Yang Deng, Wai Lam
链接: https://arxiv.org/abs/2605.15913v1
完整摘要: Block attention, which processes the input as separate blocks that cannot attend to one another, offers significant potential to improve KV cache reuse in long-context scenarios such as Retrieval-Augmented Generation (RAG). However, its broader application is hindered by two key challenges: the difficulty of segmenting input text into meaningful, self-contained blocks, and the inefficiency of existing block fine-tuning methods that risk degrading performance. To address these, we first construct SemanticSeg, a large and diverse semantic segmentation dataset containing over 30k instances across 16 categories-including books, code, web text, and conversations with text lengths ranging from 2k to 32k. Using this dataset, we train a lightweight segmenter to automatically partition text into human-instinct-aligned blocks with controllable granularity. Second, we propose block distillation, a training framework that is more efficient than block fine-tuning, which uses a frozen full-attention teacher model to guide the block-attention student. This framework integrates three novel components: block sink tokens to mitigate information loss at block boundaries, block dropout to leverage training signals from all blocks, and token-level loss weighting to focus learning on block-attention-sensitive tokens. Experiments across multiple models and benchmarks demonstrate that our segmenter outperforms heuristic and statistical baselines, and block distillation achieves near-full-attention performance under block attention, establishing a practical and scalable pathway for deploying block attention.
匹配关键词: RAG
---

[ACADEMIC - ARXIV]
标题: Retrieval-Augmented Large Language Models for Schema-Constrained Clinical Information Extraction
作者: A H M Rezaul Karim, Ozlem Uzuner
链接: https://arxiv.org/abs/2605.15467v1
完整摘要: Conversational nurse-patient transcripts contain actionable observations, but converting these transcripts into structured representations at scale remains challenging. Documentation burden is substantial, with prior studies showing clinicians spend large portions of their workday on documentation and related desk work rather than direct patient care. MEDIQA-SYNUR focuses on observation extraction from conversational nurse-patient transcripts, requiring systems to normalize these narratives into a predefined schema with value-type constraints. We propose a modular retrieval-augmented generation (RAG) pipeline that uses the training set as an exemplar corpus, combines schema-constrained prompting (full schema vs. pruned candidate schema), deterministic schema-based postprocessing, and a second-pass audit, with two LLM backbones: Llama-4-Scout-17B-16E-Instruct and GPT-5.2 with corresponding embedding models for RAG. Our best configuration uses GPT-5.2 with full schema, RAG, and a second-pass auditing, achieving 80.36% F1 score. Overall, our results show that RAG consistently improves performance, while the optimal degree of schema constraint depends on the model, and second-pass auditing yields modest additional gains by correcting residual schema-adherence errors.
匹配关键词: RAG
---

[ACADEMIC - ARXIV]
标题: Eskwai for Students: Generative AI Assistant for Legal Education in Ghana
作者: George Boateng, Philemon Badu, Patrick Agyeman-Budu, Samuel Ansah, Evans Atompoya, Evan Igwilo, Lord Baah, Frederick Abu-Bonsrah, Victor Wumbor-Apin Kumbol
链接: https://arxiv.org/abs/2605.15380v1
完整摘要: Recent advances in generative AI have shown their potential to be leveraged for legal education. Yet, work on the development and deployment of such systems for legal education in the Global South is limited. In this work, we developed Eskwai for Students, a generative AI assistant to help law students with their legal education. Eskwai for Students is a retrieval augmented generation (RAG) system that provides answers to a wide range of legal questions for law students grounded in a curated database of over 12K case laws and 1.4K legislation in Ghana. We deployed Eskwai for Students in a longitudinal study of 30 months (2.5 years) used by 3.1K law students in Ghana who made 32K queries. We evaluated the helpfulness of our AI, and provided insight into the kinds of queries law students submit to this generative AI tool, which raises some ethical concerns. This work contributes to an understanding of how law students in the Global South are using generative AI for their studies and the ways it could be leveraged responsibly to advance legal education.
匹配关键词: RAG
---

[ACADEMIC - ARXIV]
标题: Is Grep All You Need? How Agent Harnesses Reshape Agentic Search
作者: Sahil Sen, Akhil Kasturi, Elias Lumer, Anmol Gulati, Vamse Kumar Subbiah
链接: https://arxiv.org/abs/2605.15184v1
完整摘要: Recent advances in Large Language Model (LLM) agents have enabled complex agentic workflows where models autonomously retrieve information, call tools, and reason over large corpora to complete tasks on behalf of users. Despite the growing adoption of retrieval-augmented generation (RAG) in agentic search systems, existing literature lacks a systematic comparison of how retrieval strategy choice interacts with agent architecture and tool-calling paradigm. Important practical dimensions, including how tool outputs are presented to the model and how performance changes when searches must cope with more irrelevant surrounding text, remain under-explored in agent loops. This paper reports an empirical study organized into two experiments. Experiment 1 compares grep and vector retrieval on a 116-question sample from LongMemEval, using a custom agent harness (Chronos) and provider-native CLI harnesses (Claude Code, Codex, and Gemini CLI), for both inline tool results and file-based tool results that the model reads separately. Experiment 2 compares grep-only and vector-only retrieval while progressively mixing in additional unrelated conversation history, so that each query is embedded in more distracting material alongside the passages that matter. Across Chronos and the provider CLIs, grep generally yields higher accuracy than vector retrieval in our comparisons in experiment 1; at the same time, overall scores still depend strongly on which harness and tool-calling style is used, even when the underlying conversation data are the same.
匹配关键词: RAG
---

[ACADEMIC - ARXIV]
标题: IVGT: Implicit Visual Geometry Transformer for Neural Scene Representation
作者: Yuqi Wu, Tianyu Hu, Wenzhao Zheng, Yuanhui Huang, Haowen Sun, Jie Zhou, Jiwen Lu
链接: https://arxiv.org/abs/2605.16258v1
完整摘要: Reconstructing coherent 3D geometry and appearance from unposed multi-view images is a fundamental yet challenging problem in computer vision. Most existing visual geometry foundation models predict explicit geometry by regressing pixel-aligned pointmaps, often suffering from redundancy and limited geometric continuity. We propose IVGT, an Implicit Visual Geometry Transformer that implicitly models continuous and coherent geometry from pose-free multi-view images. This formulation learns a continuous neural scene representation in a canonical coordinate system and supports continuous spatial queries at any 3D positions, retrieving local features to predict signed distance (SDF) values and colors using lightweight decoders. It allows direct extraction of continuous and coherent surface geometry, enabling rendering of RGB images, depth maps, and surface normal maps from arbitrary viewpoints. We train IVGT via multi-dataset joint optimization with 2D supervision and 3D geometric regularization. IVGT demonstrates generalization across scenes and achieves strong performance on various tasks, including mesh and point cloud reconstruction, novel view synthesis, depth and surface normal estimation, and camera pose estimation.
匹配关键词: code generation
---

[ACADEMIC - ARXIV]
标题: Designing Datacenter Power Delivery Hierarchies for the AI Era
作者: Grant Wilkins, Fiodar Kazhamiaka, Alok Gautam Kumbhare, Chaojie Zhang, Ricardo Bianchini
链接: https://arxiv.org/abs/2605.16255v1
完整摘要: Demand for AI accelerators is rapidly increasing rack power density, with projections approaching 1MW per deployment by 2027. This poses a major challenge for datacenter power delivery designers. As power densities increase, a datacenter designed for a different target density may strand power, i.e., may be unable to use all the power that its delivery hierarchy has provisioned. Designs must remain efficient over long datacenter lifetimes and multiple hardware generations. Power utilization is particularly important as grid power capacity is a scarce resource in the AI era. Designing an efficient power delivery hierarchy for the long run is difficult because rack placement feasibility, workload impact, and cost depend jointly on electrical topology, deployment granularity, placement policy, power oversubscription, and workload mix. Moreover, each of these factors evolve over time, have inter-dependencies across multiple resource dimensions, and generally do not lend themselves to closed-form analysis. To address this challenge, we develop a framework for evaluating datacenter power delivery designs using throughput, power, and cost metrics over realistic arrival, oversubscription, and decommissioning sequences. The framework combines projection models for GPU, compute, and storage deployments with operational factors grounded in production data from Microsoft Azure. Our results show that multi-resource stranding materially changes deployable capacity, effective capital expenditure, and delivered performance, and quantify how rising density from rack- and pod-scale AI systems shapes these outcomes. For AI datacenter design, the relevant planning objective is not installed megawatts, but deployable capacity over time.
匹配关键词: code generation
---

[ACADEMIC - ARXIV]
标题: Real-time Speech Restoration using Data Prediction Mean Flows
作者: Sebastian Braun
链接: https://arxiv.org/abs/2605.16251v1
完整摘要: Generative models are capable to address difficult problems with non-unique solutions like bandwidth extension and gap filling, removing highly non-linear artifacts from codecs, clipping and distortion, as opposed to removing linear additive components like noise and reverb. While large offline processing models have shown impressive results, these tasks have not been solved with real-time capable models with low latency and compute. We propose a few-step flow matching model using Data Prediction Mean Flows in combination with suitable novel low-latency architecture to make flow matching models an attractive choice under theses constraints. Compared to state-of-the-art, our proposed mean flow model uses 120x less compute and introduces no algorithmic latency other than the STFT, while achieving similar audio quality.
匹配关键词: code generation
---

[ACADEMIC - ARXIV]
标题: A Generative AI Framework for Intelligent Utility Billing CO 2 Analytics and Sustainable Resource Optimisation
作者: Pavan Manjunath, Thomas Pruefer
链接: https://arxiv.org/abs/2605.16250v1
完整摘要: Distribution utilities are now expected to deliver bills that customers can actually read attach a defensible carbon number to every kWh sold and schedule load against grid stress and emissions constraints We propose an end-to-end framework that unifies four production-grade capabilities under one architectural roof a generative-AI agent that drafts each customers natural-language billing statement from structured numeric inputs under a constrained decoding policy a transformer-based forecaster that supplies the day-ahead consumption estimate with calibrated quantile bands
匹配关键词: code generation
---

[ACADEMIC - ARXIV]
标题: AI-Mediated Communication Can Steer Collective Opinion
作者: Stratis Tsirtsis, Kai Rawal, Chris Russell, Brent Mittelstadt, Sandra Wachter
链接: https://arxiv.org/abs/2605.16245v1
完整摘要: Generative artificial intelligence (AI) is increasingly integrated into the online platforms where humans exchange opinions; large language models (LLMs) now polish users' posts on LinkedIn and provide context for content shared on X. While prior work has shown that AI can express biased opinions and shape individuals' opinions during human-AI interactions, less attention has been paid to its influence on collective opinion formation when mediating human-to-human communication. We address this gap via a combination of empirical and theoretical analyses. We show empirically that LLMs from multiple popular families introduce directional biases when instructed to edit human-written texts on contested topics, for example, nudging texts in favor of gun control and against atheism. Building on this observation, we introduce a mathematical model of opinion dynamics in which an AI system sits between users on a social network, transforming the opinions they express and perceive. By analytically characterizing the equilibrium of this model and performing simulations on real social network data, we show that biases introduced by AI in human-to-human communication can be amplified through the network and shift collective opinion in their direction. In light of these findings, we investigate whether such biases are controllable by online platforms. We audit the "Explain this post" feature on X and find evidence of pro-life bias in Grok's outputs on abortion-related content, which we trace back to specific design choices. We conclude with a discussion of the broader implications of our findings in relation to ongoing legislative efforts in the European Union.
匹配关键词: code generation
---

[ACADEMIC - ARXIV]
标题: DexJoCo: A Benchmark and Toolkit for Task-Oriented Dexterous Manipulation on MuJoCo
作者: Hanwen Wang, Weizhi Zhao, Xiangyu Wang, Siyuan Huang, He Lin, Boyuan Zheng, Rongtao Xu, Gang Wang, Yao Mu, He Wang, Lue Fan, Hongsheng Li, Zhaoxiang Zhang, Tieniu Tan
链接: https://arxiv.org/abs/2605.16257v1
完整摘要: Achieving human-level manipulation requires dexterous robotic hands capable of complex object interactions. Advancing such capabilities further demands standardized benchmarks for systematic evaluation. However, existing dexterous benchmarks lack tasks that reflect the unique manipulation capabilities of dexterous hands over parallel grippers, as well as comprehensive evaluation pipelines. In this paper, we present DexJoCo, a benchmark and toolkit for task-oriented dexterous manipulation, comprising 11 functionally grounded tasks that evaluate tool-use, bimanual coordination, long-horizon execution, and reasoning. We develop a low-cost data collection system and collect 1.1K trajectories across these tasks, with support for domain randomization to assess robustness. We benchmark modern models under diverse settings, including visual and dynamics randomization, multi-task training, and action-head adaptation. Through extensive empirical analysis, we identify several important insights and common limitations of current policies in dexterous manipulation, highlighting key challenges for future research in dexterous hand robot learning. Project page available at: https://dexjoco.github.io
匹配关键词: benchmark
---

[ACADEMIC - ARXIV]
标题: Offline Semantic Guidance for Efficient Vision-Language-Action Policy Distillation
作者: Jin Shi, Brady Zhang, Yishun Lu
链接: https://arxiv.org/abs/2605.16241v1
完整摘要: Billion-parameter Vision-Language-Action (VLA) policies have recently shown impressive performance in robotic manipulation, yet their size and inference cost remain major obstacles for real-time closed-loop control. We introduce \textbf{VLA-AD}, a distillation framework that uses a Vision-Language Model as an offline semantic supervisor to transfer large VLA teachers into lightweight student policies. Instead of relying only on low-level action imitation, VLA-AD augments teacher-provided 7-DoF action targets with high-level semantic guidance, including task phase anchors and multi-frame operating-direction descriptions. These auxiliary signals are used only during training: at test time, the student policy runs independently, with neither the VLA teacher nor the VLM required. We evaluate VLA-AD on three LIBERO benchmark suites. Using OpenVLA-7B as the teacher, our method produces a 158M-parameter student, yielding a $44\times$ reduction in model size while matching the teacher with only a $0.27\%$ average relative gap. The resulting policy runs at 12.5 Hz on an RTX 4090, achieving a $3.28\times$ inference speedup over OpenVLA-7B. We further show that the same semantic distillation pipeline generalizes to a different $π_{0.5}$-4B teacher, where the student outperforms the teacher on two suites and remains within $0.53\%$ on \texttt{libero\_goal}. Additional analysis indicates that phase-level supervision and multi-frame directional cues make the student less sensitive to noisy teacher actions, such as erroneous high-frequency gripper changes. Overall, VLA-AD demonstrates that offline semantic guidance from VLMs can substantially improve the efficiency, robustness, and deployability of VLA policy distillation.
匹配关键词: benchmark
---

[ACADEMIC - ARXIV]
标题: Evaluating Design Video Generation: Metrics for Compositional Fidelity
作者: Adrienne Deganutti, Dingning Cao, Jaejung Seol, Elad Hirsch, Purvanshi Mehta
链接: https://arxiv.org/abs/2605.16223v1
完整摘要: Generative video models are increasingly used in design animation tasks, yet no standardized evaluation framework exists for this domain. Unlike natural video generation, design animation imposes structured constraints: specific components shall animate with prescribed motion types, directions, speed and timing, while non-animated regions must remain stable and layout structure must be preserved. This paper provides a fully automated evaluation framework organized across four dimensions: layout fidelity, motion correctness, temporal quality, and content fidelity. This eliminates the reliance on subjective human evaluation and establishes a common basis for benchmarking progress in the field.
匹配关键词: benchmark
---

[ACADEMIC - ARXIV]
标题: Argus: Evidence Assembly for Scalable Deep Research Agents
作者: Zhen Zhang, Liangcai Su, Zhuo Chen, Xiang Lin, Haotian Xu, Simon Shaolei Du, Kaiyu Yang, Bo An, Lidong Bing, Xinyu Wang
链接: https://arxiv.org/abs/2605.16217v1
完整摘要: Deep research agents have achieved remarkable progress on complex information seeking tasks. Even long ReAct style rollouts explore only a single trajectory, while recent state of the art systems scale inference time compute via parallel search and aggregation. Yet deep research answers are composed of complementary pieces of evidence, which parallel rollouts often duplicate rather than complete, yielding diminishing returns while pushing the aggregation context toward the model's limit. We propose Argus, an agentic system in which a Searcher and a Navigator cooperate to treat deep research as assembling a jigsaw from complementary evidence pieces, rather than brute forcing the whole answer in parallel. The Searcher collects evidence traces for a given sub-query through ReAct-style interaction. The Navigator maintains a shared evidence graph, verifying which pieces are still missing, dispatching Searchers to gather them, and reasoning over the completed graph to produce a source-traced final answer. We train the Navigator with reinforcement learning to verify, dispatch, and synthesize, while independently training the Searcher to remain a standard ReAct agent. The resulting Navigator supports rollouts with a single Searcher or many in parallel without retraining. With both Searcher and Navigator built on a 35B-A3B MoE backbone, Argus gains 5.5 points with a single Searcher and 12.7 points with 8 parallel Searchers, averaged over eight benchmarks. With 64 Searchers it reaches 86.2 on BrowseComp, surpassing every proprietary agent we benchmark, while the Navigator's reasoning context stays under 21.5K tokens.
匹配关键词: benchmark
---

[ACADEMIC - ARXIV]
标题: Fully Open Meditron: An Auditable Pipeline for Clinical LLMs
作者: Xavier Theimer-Lienhard, Mushtaha El-Amin, Fay Elhassan, Sahaj Vaidya, Victor Cartier-Negadi, David Sasu, Lars Klein, Mary-Anne Hartley
链接: https://arxiv.org/abs/2605.16215v1
完整摘要: Clinical decision support systems (CDSS) require scrutable, auditable pipelines that enable rigorous, reproducible validation. Yet current LLM-based CDSS remain largely opaque. Most "open" models are open-weight only, releasing parameters while withholding the data provenance, curation procedures, and generation pipelines that determine model behavior. Fully Open (FO) models, which expose the complete training stack end-to-end, do not currently exist in medicine. We introduce Fully Open Meditron, the first fully open pipeline for building LLM-CDSS, comprising a clinician-audited training corpus, a reproducible data construction and training framework, and a use-aligned evaluation protocol. The corpus unifies eight public medical QA datasets into a normalized conversational format and expands coverage with three clinician-vetted synthetic extensions: exam-style QA, guideline-grounded QA derived from 46,469 clinical practice guidelines, and clinical vignettes. The pipeline enforces system-wide decontamination, gold-label resampling of teacher generations, and end-to-end validation by a four-physician panel. We evaluate using an LLM-as-a-judge protocol over expert-written clinical vignettes, calibrated against 204 human raters. We apply the recipe to five FO base models (Apertus-70B/8B-Instruct, OLMo-2-32B-SFT, EuroLLM-22B/9B-Instruct). All MeditronFO variants are preferred over their bases. Apertus-70B-MeditronFO improves +6.6 points over its base (47.2% to 53.8%) on aggregate medical benchmarks, establishing a new FO SoTA. Gemma-3-27B-MeditronFO is preferred over MedGemma in 58.6% of LLM-as-a-judge comparisons and outperforms it on HealthBench (58% vs 55.9%). These results show that fully open pipelines can achieve state-of-the-art domain-specific performance without sacrificing auditability or reproducibility.
匹配关键词: benchmark
---

[ACADEMIC - ARXIV]
标题: Formal Methods Meet LLMs: Auditing, Monitoring, and Intervention for Compliance of Advanced AI Systems
作者: Parand A. Alamdari, Toryn Q. Klassen, Sheila A. McIlraith
链接: https://arxiv.org/abs/2605.16198v1
完整摘要: We examine one particular dimension of AI governance: how to monitor and audit AI-enabled products and services throughout the AI development lifecycle, from pre-deployment testing to post-deployment auditing. Combining principles from formal methods with SoTA machine learning, we propose techniques that enable AI-enabled product and service developers, as well as third party AI developers and evaluators, to perform offline auditing and online (runtime) monitoring of product-specific (temporally extended) behavioral constraints such as safety constraints, norms, rules and regulations with respect to black-box advanced AI systems, notably LLMs. We further provide practical techniques for predictive monitoring, such as sampling-based methods, and we introduce intervening monitors that act at runtime to preempt and potentially mitigate predicted violations. Experimental results show that by exploiting the formal syntax and semantics of Linear Temporal Logic (LTL), our proposed auditing and monitoring techniques are superior to LLM baseline methods in detecting violations of temporally extended behavioral constraints; with our approach, even small-model labelers match or exceed frontier LLM judges. Our predictive and intervening monitors significantly reduce the violation rates of LLM-based agents while largely preserving task performance. We further show through controlled experiments that LLMs' temporal reasoning shows a pronounced degradation in accuracy with increasing event distance, number of constraints, and number of propositions.
匹配关键词: safety
---

[ACADEMIC - ARXIV]
标题: Towards Trustworthy and Explainable AI for Perception Models: From Concept to Prototype Vehicle Deployment
作者: Till Beemelmanns, Shayan Sharifi, Manas Mehrotra, Ayushman Choudhuri, Lutz Eckstein
链接: https://arxiv.org/abs/2605.16087v1
完整摘要: Deep Neural Networks have become the dominant solution for Autonomous Driving perception, but their opacity conflicts with emerging Trustworthy AI guidelines and complicates safety assurance, debugging, and human oversight. While theoretical frameworks for safe and Explainable AI (XAI) exist, concrete implementations of Trustworthy AI for 3D scene understanding remain scarce. We address this gap by proposing a Trustworthy AI perception module that is remarkably robust, integrates faithful explainability, and calibrated uncertainty estimates. Building on a transformer-based detector, we derive explanation from the attention mechanism at inference time and validate their faithfulness using perturbation-based consistency tests. We further integrate an uncertainty estimation and calibration module, and apply robustness-enhancing training methods. Experiments show faithful saliency behavior, improved robustness, and well-calibrated uncertainty estimates. Finally, we deploy these Trustworthy AI elements in a prototype vehicle and provide an XAI Interface that visualizes documentation artifacts, model uncertainty state, and saliency maps, demonstrating the feasibility of trustworthy perception monitoring in real time. Supplementary materials are available at https://tillbeemelmanns.github.io/trustworthy_ai/ .
匹配关键词: safety
---

[ACADEMIC - ARXIV]
标题: SAFE Quantum Machine Learning with Variational Quantum Classifiers
作者: Ying Chen, Paolo Giudici, Vasily Kolesnikov, Paolo Recchia
链接: https://arxiv.org/abs/2605.16067v1
完整摘要: We propose a variational quantum classifier operating on high dimensional deep representations via amplitude encoding, stabilized by a learnable classical pre encoding layer.By combining normalized amplitude embeddings with bounded quantum observables, the resulting model induces a structured and smooth hypothesis class with controlled sensitivity to input variations. Model reliability is assessed using SAFE-AI metrics derived from the Cramer von Mises divergence, enabling consistent evaluation across accuracy, robustness, and explainability dimensions. Empirical results show that the proposed quantum model provides competitive predictive performance compared with strong classical baselines while exhibiting a more balanced SAFE reliability profile, with improved robustness to noise and stability under structured feature removal. These findings suggest that variational quantum circuits offer a principled mechanism for stability oriented SAFE learning in safety critical settings.
匹配关键词: safety
---

[ACADEMIC - ARXIV]
标题: Constrained MPC-Based Motion Planning for Morphing Quadrotors in Ultra-Narrow Passages under Limited Perception
作者: Harsh Modi, Xiao Liang, Minghui Zheng
链接: https://arxiv.org/abs/2605.15999v1
完整摘要: This paper introduces a motion planning framework to plan morphology and trajectory for morphing quadrotors under extremely constrained environments. We develop a novel obstacle avoidance cost function for nonlinear model predictive control (MPC) that enables navigation through extremely narrow gaps under limited perception from a 2D LiDAR. Classical artificial potential field-based costs typically have a high cost in narrow passages, artificially blocking the navigable path. In contrast, we propose a smooth exponential obstacle cost that preserves low traversal cost within narrow gaps while maintaining strong collision avoidance behavior. The formulation avoids hard activation thresholds and introduces a cost reduction factor to reduce the cost within narrow passages. Direct use of 2D LiDAR measurements in MPC allows navigation around arbitrarily shaped obstacles. The method is embedded within an acados-based nonlinear MPC framework. Simulation and experimental results demonstrate successful traversal of narrow corridors where typical repulsive cost functions would fail. The approach provides a computationally efficient and practical solution for navigating through tight spaces while maintaining safety from the obstacles. While we are implementing the framework on the morphing quadrotors, the cost function formulation is general-purpose for any mobile robot application, and is not limited to the morphing quadrotors. The implementation code is available at \href{https://github.com/harshjmodi1996/morphocopter_mpc}{Github Repo} and a short video is available at \href{https://zh.engr.tamu.edu/wp-content/uploads/sites/310/2026/03/MPC_MorphoCopter_video.mp4}{Video Link}.
匹配关键词: safety
---

[ACADEMIC - ARXIV]
标题: OHP-RL: Online Human Preference as Guidance in Reinforcement Learning for Robot Manipulation
作者: Yunyang Mo, Jian Li, Qiwei Wu, Yihang Kang, Renjing Xu
链接: https://arxiv.org/abs/2605.15971v1
完整摘要: While reinforcement learning (RL) enables robots to acquire skills autonomously, its real-world deployment is severely limited by inefficient and unsafe exploration. Human-in-the-loop interventions offer a practical solution, yet existing methods typically exploit these interventions as auxiliary training signals, without fully capturing the richer information they provide about when and how autonomy should be guided. Human interventions often encode relative preferences over behavior under safety and task constraints, rather than prescribing exact actions to imitate. Motivated by this perspective, we propose Online Human Preference as Guidance in Reinforcement Learning (OHP-RL), a framework that leverages human interventions as preference information to guide policy learning. OHP-RL introduces a state-dependent preference gate that adaptively regulates when and to what extent human interventions should shape policy learning. This design enables the agent to benefit from intermittent and imperfect human feedback while preserving autonomous exploration and stable policy optimization. We evaluate OHP-RL on three challenging real-world contact-rich manipulation tasks on a Franka robot. Across all tasks, OHP-RL consistently achieves strong success rates, faster convergence, and substantially lower human intervention effort than prior approaches. Moreover, the learned policies exhibit more stable and human-aligned behavior throughout training.
匹配关键词: safety
---

