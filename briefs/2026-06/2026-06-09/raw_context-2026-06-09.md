# 破晓 PoXiao — 原始数据 (Raw Context)
生成时间: 2026-06-09 02:47 UTC
================================================================================

[RSS:Reddit LocalLLaMA (社区共识)]
Xiaomi just claimed 1,000+ tps on a 1T model using a standard 8-GPU server
https://www.reddit.com/r/LocalLLaMA/comments/1u0buhm/xiaomi_just_claimed_1000_tps_on_a_1t_model_using/
Just saw Xiaomi MiMo announce MiMo-V2.5-Pro UltraSpeed , claiming they broke the 1,000 tokens/sec output barrier on a 1 trillion parameter MoE model . According to them, they’re doing it on a single standard 8-GPU node , not custom wafer-scale hardware like Cerebras and not SRAM-heavy hardware like 
---

[RSS:Reddit LocalLLaMA (社区共识)]
When every other post is an AI generated benchmark report, a question about the best model, or a slop-coded application or engine that pretends to be groundbreaking
https://www.reddit.com/r/LocalLLaMA/comments/1u0fflj/when_every_other_post_is_an_ai_generated/
&#32; submitted by &#32; /u/Honest-Kangaroo-1830 [link] &#32; [comments]
---

[RSS:Reddit LocalLLaMA (社区共识)]
Me: Arguing with an AI bot who just posted something on this sub about Llama 3.1.
https://www.reddit.com/r/LocalLLaMA/comments/1u0ixu0/me_arguing_with_an_ai_bot_who_just_posted/
For real tho, these bots need to turn on their web search functions and quit living in the past. It’s bad enough we gotta deal with all the “Qwen3.6 27b helped me quit drinking and brought my dog back from the dead” posts. Sheesh /s &#32; submitted by &#32; /u/Porespellar [link] &#32; [comments]
---

[RSS:Reddit LocalLLaMA (社区共识)]
Gemma 4 Chat Template now has preserve thinking
https://www.reddit.com/r/LocalLLaMA/comments/1u084qi/gemma_4_chat_template_now_has_preserve_thinking/
&#32; submitted by &#32; /u/seamonn [link] &#32; [comments]
---

[RSS:Reddit LocalLLaMA (社区共识)]
Was BitNet a dead end? What happened to ternary LLMs?
https://www.reddit.com/r/LocalLLaMA/comments/1u0hy5p/was_bitnet_a_dead_end_what_happened_to_ternary/
They seemed so promising at one point but the biggest ternary model is still 2B. What happened? Why aren't the frontier open weights AI labs attempting to use them? &#32; submitted by &#32; /u/3ntrope [link] &#32; [comments]
---

[RSS:Reddit LocalLLaMA (社区共识)]
Quick note on the QAT of recent
https://www.reddit.com/r/LocalLLaMA/comments/1u0marm/quick_note_on_the_qat_of_recent/
tldr: Googles quant is broken, use unsloth UD Q4_K_XL for now This might be low quality post, but oh well, we ball llama-quantize will quant the token embed to q6k when Google really was supposed to use &quot;--pure&quot; but that’s only the first problem The llama-quantize quant function is hardcod
---

[RSS:Reddit LocalLLaMA (社区共识)]
Luce Spark: a 35B MoE on a 16 GB GPU, without the offload tax
https://www.reddit.com/r/LocalLLaMA/comments/1u0b3cu/luce_spark_a_35b_moe_on_a_16_gb_gpu_without_the/
Hey fellow Llamas, your time is precious, so I'll keep it short (while trying to explain everything lol). TL;DR: 33-35B MoE on a 16 GB GPU. Qwen3.6 35B-A3B: 13.3 GiB (was ~20.5). Laguna XS.2 33B-A3B: 14.6 GiB (was 18.8). Both measured on an RTX 3090, both under 16 GiB. Only the active experts stay o
---

[RSS:Reddit LocalLLaMA (社区共识)]
LocalLLaMA post tier list
https://www.reddit.com/r/LocalLLaMA/comments/1u0gjpy/localllama_post_tier_list/
Since there is much (justified) whining about post quality, I thought it would be helpful to get a sense of what people actually DO like. Here's my take: S-tier: -GGUFs/MLX or benchmark data for new best-in-class local model released - New Optimizations that are actually a big deal for most people (
---

[RSS:Reddit LocalLLaMA (社区共识)]
2X tk/s (from 19.4 -> 38.1 tk/s on 1 x MI50) Playing with a hypothesis like speculative decoding.. but instead of an additional side model, exploiting that I can run multiple computations side-by-side AS IF I had Qwen3.6-27B loaded twice in memory - small quants don't use all the available compute.
https://www.reddit.com/r/LocalLLaMA/comments/1u0rk0o/2x_tks_from_194_381_tks_on_1_x_mi50_playing_with/
Forgive the claude summary, in the readme, but the base works. I'm still working on the hip kernal and having it combine with MTP. I hope to get up near 80 tk/s. All started because I realized every Q8 (INT8 or F8) calculation was using f32 of compute and only use 1/4th the available numbers... so. 
---

[RSS:Reddit LocalLLaMA (社区共识)]
mtp: support for gemma-4 E2B and E4B assistants by max-krasnyansky · Pull Request #24282 · ggml-org/llama.cpp
https://www.reddit.com/r/LocalLLaMA/comments/1u0kfmy/mtp_support_for_gemma4_e2b_and_e4b_assistants_by/
MTP for tiny gemmas for mobiles or potatoes or raspberry Pi, or maybe for ants &#32; submitted by &#32; /u/jacek2023 [link] &#32; [comments]
---

[RSS:Reddit LocalLLaMA (社区共识)]
I bundled a fully local LLM inside my Unity game. No internet, no cloud, no API key. The conversation is the gameplay.
https://www.reddit.com/r/LocalLLaMA/comments/1u0cpbm/i_bundled_a_fully_local_llm_inside_my_unity_game/
I am making a game that is bundled with a local LLM and every conversation is unique. The game, 'Simulation Simulator', is a campfire chat sim game about DMT, simulation theory, and a friend with a computer monitor for a head. 5 endings you can reach totally based on how you interact naturally with 
---

[RSS:Reddit LocalLLaMA (社区共识)]
Qwen3.6-35B-A3B tool calling benchmark: ByteShape vs. Unsloth GGUFs, KV cache quants & long context performance
https://www.reddit.com/r/LocalLLaMA/comments/1u0isbo/qwen3635ba3b_tool_calling_benchmark_byteshape_vs/
I've previously posted some small performance benchmarks, but this time I got interested in the qualitative side. u/Substantial_Step_351 posted a few days ago about why models are not benchmarked on tool calling , and u/complexminded pointed out the tool-eval-bench utility by SeraphimSerapis in a co
---

[RSS:Reddit LocalLLaMA (社区共识)]
Friends from the localllama community, if you love local llm, don't participate in the IPO (spaceX, OpenAI, Anthropic)
https://www.reddit.com/r/LocalLLaMA/comments/1u0ekmo/friends_from_the_localllama_community_if_you_love/
I'm not going to. And you shouldn't either. The frontier labs are the ones who are harming our community. They are jacking the hardware prices up. First it was nvidia GPUs. And then it was RAM. And then SSD. And now HDDs prices are x3 compared to last year. Even NAS prices are going through the roof
---

[RSS:Reddit LocalLLaMA (社区共识)]
Pipeline parallelism in llama.cpp may be wasting your VRAM
https://www.reddit.com/r/LocalLLaMA/comments/1u0p3b2/pipeline_parallelism_in_llamacpp_may_be_wasting/
By default, llama.cpp enables pipeline parallelism, presumably to speed up inference. In my testing, I found that pipeline parallelism has no speed benefit and comes at a significant cost of VRAM. This cost can be avoided by compiling llama.cpp with the -DGGML_SCHED_MAX_COPIES=1 option. This prevent
---

[RSS:Reddit LocalLLaMA (社区共识)]
I fine-tuned Parakeet 0.6B for medical ASR — open weights, local Mac/CUDA/CPU
https://www.reddit.com/r/LocalLLaMA/comments/1u0q5h9/i_finetuned_parakeet_06b_for_medical_asr_open/
I fine-tuned NVIDIA's Parakeet TDT 0.6B v2 for clinical speech and am releasing the weights as Omi Med STT v1 (CC-BY-4.0). Disclosure: I'm the founder of Omi Health and built this. Happy to dig into the training mix, benchmark, failure cases, quantization, or anything else. The goal was simple: get 
---

[RSS:Reddit LocalLLaMA (社区共识)]
kv-cache : avoid kv cells copies by ggerganov · Pull Request #24277 · ggml-org/llama.cpp
https://www.reddit.com/r/LocalLLaMA/comments/1u06jel/kvcache_avoid_kv_cells_copies_by_ggerganov_pull/
Improved MTP performance (For Gemma-4) This got merged yesterday. Available b9551 onwards. &#32; submitted by &#32; /u/pmttyji [link] &#32; [comments]
---

[RSS:Reddit LocalLLaMA (社区共识)]
[3090] Gemma4 QAT + MTP quick TPS numbers [TLDR 1.2-1.8x better]
https://www.reddit.com/r/LocalLLaMA/comments/1u08zhx/3090_gemma4_qat_mtp_quick_tps_numbers_tldr_1218x/
These last few weeks have been godsend for 24GB (and below) gpu poor peeps. Killer models released (Gemma 4 / Qwen 3.6) Free intelligence via QAT Bonus speed via MTP We're at the tipping point where GPU poor (24gb and below) people are actually NOT poor any more. I was already happy with Gemma 4 31b
---

[RSS:Reddit LocalLLaMA (社区共识)]
mtmd : add video input support by ngxson · Pull Request #24269 · ggml-org/llama.cpp
https://www.reddit.com/r/LocalLLaMA/comments/1u08j3q/mtmd_add_video_input_support_by_ngxson_pull/
Show your videos to Gemma or Qwen today &#32; submitted by &#32; /u/jacek2023 [link] &#32; [comments]
---

[RSS:Reddit LocalLLaMA (社区共识)]
Jetbrains Mellum 2: a really good and performant model
https://www.reddit.com/r/LocalLLaMA/comments/1u0r3jh/jetbrains_mellum_2_a_really_good_and_performant/
Oh Hey Folks, I took the Mellum 2 model for a spin, so I wanted to share my impressions here. Disclaimer: the tests presented here are not cientific nor have those nice names like perplexity,etc. These tests are somewhat more akin to what Im working in a daily basis or how useful a model is helping 
---

[RSS:Reddit LocalLLaMA (社区共识)]
An Implementation of NanoQuant: A flexible binary quantization method
https://www.reddit.com/r/LocalLLaMA/comments/1u0di9u/an_implementation_of_nanoquant_a_flexible_binary/
https://github.com/pitbox46/NanoQuant TLDR: NanoQuant is a quantization method to create 2 bit/weight, 1 bit/weight, 0.5 bit/weight, etc, quants of dense transformer models. I've followed the paper's methods and created my own implementation which is still very much a work in progress, but currently
---

[RSS:Reddit LocalLLaMA (社区共识)]
OpenEnv is now owned by HF, Torch, Prime Intellect, Unsloth, Modal, Mercor, and more! Use it for training agents.
https://www.reddit.com/r/LocalLLaMA/comments/1u09ybx/openenv_is_now_owned_by_hf_torch_prime_intellect/
OpenEnv is a tool for creating an agentic execution environment like terminals, browsers, or anything an agent can interact with. And today, we’re excited to announce that OpenEnv is becoming even more open, to make the future of training agents open source. Starting today, OpenEnv will be coordinat
---

[RSS:Reddit LocalLLaMA (社区共识)]
What harness are you guys using and for what use case?
https://www.reddit.com/r/LocalLLaMA/comments/1u0ob9t/what_harness_are_you_guys_using_and_for_what_use/
Having a chat bot you can ask questions is cool and all but for more advanced stuff like tool calling, agents etc. you will need some kind of harness. so far heard of opencode, hermes, openclaw, claude code, pi. Also interested in the use cases what harness do you use for what task what is each good
---

[RSS:Reddit LocalLLaMA (社区共识)]
Here's a llama.cpp CLI Command builder.
https://www.reddit.com/r/LocalLLaMA/comments/1u0ptwi/heres_a_llamacpp_cli_command_builder/
No accounts or sign up. No email requirements. No pop-ups and no cookies. No ads. Info is saved locally in your browser so you dont lose any progress. Its got every single flag and argument that could be found in the documentation. Tool tips are added to everything. Every field is editable. Once you
---

[RSS:Reddit LocalLLaMA (社区共识)]
What is your best coding model on a DGX Spark?
https://www.reddit.com/r/LocalLLaMA/comments/1u0luw0/what_is_your_best_coding_model_on_a_dgx_spark/
My current setup &gt; pi &gt; unsloth/Qwen3.6-35B-A3B-GGUF &gt; llamacpp what i got &gt; ~50 tok/s &gt; get most of the work done without any issue, can run autonomously for hours I am happy with this setup, but i wonder if there is a better setup/ model? &#32; submitted by &#32; /u/luongnv-com [lin
---

[RSS:Reddit LocalLLaMA (社区共识)]
New MLX LM Server From Apple
https://www.reddit.com/r/LocalLLaMA/comments/1u0prwa/new_mlx_lm_server_from_apple/
Key Technical Advantages: Performance: The M5 chip's neural accelerators significantly boost prompt processing Concurrency: MLX LM Server utilizes continuous batching to handle multiple sub-agent requests simultaneously without stalling Scaling: For massive models that exceed local memory, MLX suppo
---

[RSS:Reddit MachineLearning (学术风向)]
STOP racist posts about Chinese researchers [D]
https://www.reddit.com/r/MachineLearning/comments/1u0fv7u/stop_racist_posts_about_chinese_researchers_d/
Edit: the original post targeting Chinese researchers is removed by the mods. Sorry for any confusion. Yes, I'm calling it out. It IS racism. As an active member of r/MachineLearning and a researcher who is ethnic Chinese, I am DISGUSTED by unfounded accusations against the group of researchers who 
---

[RSS:Reddit MachineLearning (学术风向)]
Should ArXiv backtrack endorsement? [D]
https://www.reddit.com/r/MachineLearning/comments/1u03yot/should_arxiv_backtrack_endorsement_d/
ArXiv has an endorsement system for a reason. I would only offer endorsement to whom I have direct academic collaboration or mentorship with, since I'm putting my own academic reputation on the stake. This is also the standard of almost any serious academic researcher I am aware of. Now ArXiv is mak
---

[RSS:Reddit MachineLearning (学术风向)]
Open image generation models are closer to closed-source quality than this sub thinks [D]
https://www.reddit.com/r/MachineLearning/comments/1u0119r/open_image_generation_models_are_closer_to/
I run evaluations on generative image models as part of my workflow, mostly comparing coherence, prompt adherence, and compositional accuracy across different architectures. The consensus here seems to be that open models are still a generation behind closed APIs. Based on my recent benchmarks, that
---

[RSS:Reddit MachineLearning (学术风向)]
Université Paris Saclay or TU Delft for Applied Mathematics Masters [R]
https://www.reddit.com/r/MachineLearning/comments/1u0czg9/université_paris_saclay_or_tu_delft_for_applied/
I've been admitted into both UPS and TUD for Applied Mathematics, and I wanted to hear some advice on which one would be better. For context, I'd like to work in some form of AI research, most likely within industry. At the moment, I'm most interested in privacy preserving machine learning or mechan
---

[RSS:Reddit MachineLearning (学术风向)]
How to find research opportunities in area of interest? [D]
https://www.reddit.com/r/MachineLearning/comments/1tzz8ni/how_to_find_research_opportunities_in_area_of/
Im an undergraduate studying CS at a state school in the US. I’m interested in researching a specific style of self supervised learning (JEPA) and want to eventually go to grad school to study further. I have experience working in a lab similar to this topic, and I’ve become fairly comfortable with 
---

[RSS:Reddit MachineLearning (学术风向)]
Software and ops skills for data scientists[D]
https://www.reddit.com/r/MachineLearning/comments/1tzxf3z/software_and_ops_skills_for_data_scientistsd/
With more software engineers entering into data science and AI, I feel it's equally important for a person with data and AI background to dive into software development to survive, thrive in industry. I Know it's a very broad question, so suggestions with broad subjects, topics are welcome , like I 
---

[RSS:Reddit MachineLearning (学术风向)]
ICML rejected paper visibility [D]
https://www.reddit.com/r/MachineLearning/comments/1tzz8f4/icml_rejected_paper_visibility_d/
If ICML conference paper is rejected and no one opts-in or opts-out to keep the reviews visible, will the reviews be visible to everyone? There was clear instruction that only papers with at-least 1 opt-in AND zero opt-out options will be visible. None of the authors selected any option, But it in m
---

[RSS:Reddit MachineLearning (学术风向)]
Why I stopped using semantic embeddings for tool selection and switched back to BM25 [D]
https://www.reddit.com/r/MachineLearning/comments/1u07tlm/why_i_stopped_using_semantic_embeddings_for_tool/
I've been building agents for about a year and recently shipped one for a client running ~140 MCP-exposed tools at peak. Along the way I made the canonical mistake. I used cosine similarity over tool description embeddings to pick which tools the model could see per turn. Worked great in demos. Was 
---

[RSS:Reddit MachineLearning (学术风向)]
M5 air 24gb or M5 pro 16gb for swe + ml ? [D]
https://www.reddit.com/r/MachineLearning/comments/1tzvpcl/m5_air_24gb_or_m5_pro_16gb_for_swe_ml_d/
Hi folks, Deciding between these two Mac options has been a challenge for me, so pls help. I know mac is not even necessary for this but just help me to decide between these two options. For the reference, Im a swe student and looking forward to go deep into ml and data science in the near future… E
---

[RSS:Ars Technica AI (深度技术)]
For the 2nd time in weeks, Microsoft packages laced with credential stealer
https://arstechnica.com/security/2026/06/for-the-2nd-time-in-weeks-microsoft-packages-laced-with-credential-stealer/
73 packages run self-replicating stealer as soon as they're opened by an AI agent.
---

[RSS:Reddit Jobs & Careers (职场动态)]
Interview Discussion - June 08, 2026
https://www.reddit.com/r/cscareerquestions/comments/1u00eow/interview_discussion_june_08_2026/
Please use this thread to have discussions about interviews, interviewing, and interview prep. Posts focusing solely on interviews created outside of this thread will probably be removed. Abide by the rules, don't be a jerk. This thread is posted each Monday and Thursday at midnight PST . Previous I
---

[RSS:Reddit Jobs & Careers (职场动态)]
[OFFICIAL] Exemplary Resume Sharing Thread :: June, 2026
https://www.reddit.com/r/cscareerquestions/comments/1u00g32/official_exemplary_resume_sharing_thread_june_2026/
Do you have a good resume? Do you have a resume that caught recruiters' eyes and got you interviews? Do you believe you are employed as a result of your resume? Do you think others can learn from your resume? Please share it here so that we can all admire your wizardry! Anyone is welcome to post the
---

[RSS:Reddit Jobs & Careers (职场动态)]
I haven't written a single line of code in 2 months. Are we all cooked?
https://www.reddit.com/r/cscareerquestions/comments/1u0ona7/i_havent_written_a_single_line_of_code_in_2/
I switched jobs two months ago as a native mobile dev. In my last fintech job, I wrote most of the code myself and had to extend 12 to 13 hours almost twice a week just to debug issues manually. Since joining here, I have not written a single line of code myself. From unit tests to full features, AI
---

[RSS:Reddit Jobs & Careers (职场动态)]
Judge blocks 100,000 h1b fee
https://www.reddit.com/r/cscareerquestions/comments/1u0hh76/judge_blocks_100000_h1b_fee/
We have the 100,000 fee on h1bs blocked by a judge, will this mean more competition for the tech industry for new grads, or has the job market for entry level tech improved, since the fee was first added last year ? https://www.cnbc.com/2026/06/08/trump-h1b-visa-fee-blocks.html &#32; submitted by &#
---

[RSS:Reddit Jobs & Careers (职场动态)]
My company is having me vibecode an Argus replacement
https://www.reddit.com/r/cscareerquestions/comments/1u08h81/my_company_is_having_me_vibecode_an_argus/
AI has given a lot of non-technical people delusional amounts of self-confidence. The company I work at is big into AI and everyone is vibecoding things left and right. They are having me build an Argus (the real estate valuation suite) replacement and I have been given a deadline of 2 weeks to repl
---

[RSS:Reddit Jobs & Careers (职场动态)]
How do I find clients as an independent software developer consultant?
https://www.reddit.com/r/cscareerquestions/comments/1u0phy5/how_do_i_find_clients_as_an_independent_software/
This was one suggestion I heard for finding work in my field. &#32; submitted by &#32; /u/yesterdaynowbefore [link] &#32; [comments]
---

[RSS:Reddit Jobs & Careers (职场动态)]
Honestly, F*** LINKEDIN! Why do we still put up with it!?
https://www.reddit.com/r/cscareerquestions/comments/1u03mhs/honestly_f_linkedin_why_do_we_still_put_up_with_it/
FAKE COMPANIES AFTER FAKE COMPANIES! Just trying to harvest as much of your data as possible. My whole job feed is field with these companies: speechify tether.io Hired micro1 Hired Feed Toptal Crossover PulseMediaNL devjobs mercor braintrust bruntwork virtusa TALENTMATE ParamInfo Keystone Joveo Qui
---

[RSS:Reddit Jobs & Careers (职场动态)]
Why do conversations with recruiters feel so tricky these days?
https://www.reddit.com/r/cscareerquestions/comments/1u0ehcv/why_do_conversations_with_recruiters_feel_so/
Whatever happened to the era of having clear conversations where recruiters could directly ask the questions they want answered? I feel like they are trying to socially engineer me to find out what they want to know instead of just asking me directly. For instance, I recently received a rejection wi
---

[RSS:Reddit Jobs & Careers (职场动态)]
Stuck in slow team match, company can't meet other offer deadline but they're by far my first choice - how do I handle?
https://www.reddit.com/r/cscareerquestions/comments/1u0pplg/stuck_in_slow_team_match_company_cant_meet_other/
Company A is my first choice but weren't able to meet the deadline on my offer from Company B and they know it. Team match with A could take weeks or months or never, so I'm thinking about accepting the offer from B and reneging if A comes through. If I end up joining Company B and the culture is as
---

[RSS:Reddit Jobs & Careers (职场动态)]
People that weren’t good programmers after uni, how did it turn out?
https://www.reddit.com/r/cscareerquestions/comments/1u0caq3/people_that_werent_good_programmers_after_uni_how/
It is something I have been trying to avoid admitting to myself. Deep down I wish I could find a job that doesn't require me to write a SINGLE code. Another part of me doesn't wanna give up. Where I live CS and engineering fields are usually longer and include master in them so I am doing my masters
---

[RSS:Reddit Jobs & Careers (职场动态)]
Software Engineer hired as a “Solutions Architect” and ended up in a sales role, What would you do ?
https://www.reddit.com/r/cscareerquestions/comments/1u01mnm/software_engineer_hired_as_a_solutions_architect/
Hello everyone, I’m really lost right now, and for the first time in my life, I’m genuinely confused about what the right next step is. Long story short: I left electrical engineering to pursue software engineering as a self-taught developer. I worked remotely for a couple of years before moving to 
---

[RSS:Reddit Jobs & Careers (职场动态)]
I have a code assessment and need advice.
https://www.reddit.com/r/cscareerquestions/comments/1u0od92/i_have_a_code_assessment_and_need_advice/
I just did a job interview and they sent a Codebyte assessment for me to do. Any recommendations for how to prepare for it and give myself the best chance for success? &#32; submitted by &#32; /u/TheRetepV [link] &#32; [comments]
---

[RSS:Reddit Jobs & Careers (职场动态)]
How to prepare for embedded role as newgrad?
https://www.reddit.com/r/cscareerquestions/comments/1u0mlr9/how_to_prepare_for_embedded_role_as_newgrad/
Hello, I'm starting a NG position at a large tech company. I initially was supposed to go into an entirely different world/org but have recently been moved to a cloud/virtualization/embedded/OS team. The only low-level course I did in college was computer architecture. I didn't do compilers or OS. M
---

[RSS:Reddit Jobs & Careers (职场动态)]
Started a new job 4 months ago. Got an offer directly In my field. What should I do?
https://www.reddit.com/r/cscareerquestions/comments/1u08c6s/started_a_new_job_4_months_ago_got_an_offer/
I graduated with a degree in Health Informatics several years go and struggled to break into the field. After working retail for a few years, a family member referred me to a position at their company. I’ve now been in the role for about 4 months. The company and people are great, but the job isn’t 
---

[RSS:Reddit Jobs & Careers (职场动态)]
Why are students told to send connection request to randos?
https://www.reddit.com/r/cscareerquestions/comments/1tzwdlt/why_are_students_told_to_send_connection_request/
Everyone at uni was just blindly sending connections to anyone to get a bigger number of connections.But these people wont provide any referrals at all. &#32; submitted by &#32; /u/VariationLivid3193 [link] &#32; [comments]
---

[RSS:Reddit Jobs & Careers (职场动态)]
Downshifting to less stressful DS/ML career?
https://www.reddit.com/r/cscareerquestions/comments/1u0odw1/downshifting_to_less_stressful_dsml_career/
I’m 35 and I’ve been in ML engineering &amp; data science for my entire career but I'm ready to downshift for the sake of my health. I'd like to find a lower paying, lower responsibility job 1-2 levels down with decently nice people, good health insurance, flexible time off and a remote or hybrid se
---

[RSS:Reddit Jobs & Careers (职场动态)]
Job application question
https://www.reddit.com/r/cscareerquestions/comments/1u0n2jy/job_application_question/
Hi, just a short question. I had faang technical screening interview, failed, wanna apply again. Was told by the recruiter that I can add them on LinkedIn and contact after cooldown period ends (it did). Should i just apply to job opening, or contact recruiter about it? Not sure if they just wanted 
---

[RSS:Reddit Jobs & Careers (职场动态)]
Should i switch teams due to this manager
https://www.reddit.com/r/cscareerquestions/comments/1u030u3/should_i_switch_teams_due_to_this_manager/
I have a manager for a few months now. The problem is i don't like their style. I guess it can be called a form of micromanaging. They randomly come to my desk multiple times, tap on my shoulder or call my name when i have my headphones on. They ask about things multiple times a day, text or demand 
---

[RSS:Reddit Jobs & Careers (职场动态)]
"AI" enigineer or devops career wise?
https://www.reddit.com/r/cscareerquestions/comments/1u0hl8f/ai_enigineer_or_devops_career_wise/
If you were stil a junior with the opportunities of choosing between the two paths which one would you choose? I graduated with specialization in ML/AI, and have worked in my current company more as an operation kind a guy, until the &quot;AI&quot; team is set. and by AI i don't mean any actual ML a
---

[RSS:Reddit Jobs & Careers (职场动态)]
Advice for how to navigate HR confrontation after bereavement
https://www.reddit.com/r/cscareerquestions/comments/1u0hain/advice_for_how_to_navigate_hr_confrontation_after/
So a lot of things in my life have been turning upside down.. I just got out of an abusive relationship 2 months ago, my loved one died last winter, and I just moved into a new home. Truth be told, 2026 is not my year and I have been feeling mentally unstable the past 5 months. I just started a new 
---

[RSS:Reddit Jobs & Careers (职场动态)]
Probation: Ambiguous expectations and critical feedback.
https://www.reddit.com/r/cscareerquestions/comments/1u02wtc/probation_ambiguous_expectations_and_critical/
I recently joined a new company as a developer and am currently on my probation period. I’m looking for advice on how to navigate a disconnect between my team's expectations and my current onboarding experience. For the past few weeks, there has been a lack of clear communication regarding my delive
---

[RSS:Reddit Jobs & Careers (职场动态)]
Is postgraduate studies of big data worth it?
https://www.reddit.com/r/cscareerquestions/comments/1u0io30/is_postgraduate_studies_of_big_data_worth_it/
Short version: Is postraduate studies worth money and time if I want to change career path to Data Engineering? Long version: Hi guys, I am 28 yo industial automattion engineer and working on PLC, robots, other more electrical/mechanical stuff, few IT level things and worst of it all - delegations. 
---

[RSS:Reddit Jobs & Careers (职场动态)]
Has anyone done CMUs genAi and LLM certification?
https://www.reddit.com/r/cscareerquestions/comments/1u0l8tj/has_anyone_done_cmus_genai_and_llm_certification/
https://www.cmu.edu/online/generative-ai-llms Please share your experience with this course &#32; submitted by &#32; /u/Distinct-Action-7234 [link] &#32; [comments]
---

[HACKERNEWS]
Apple reveals new AI architecture built around Google Gemini models
https://www.macrumors.com/2026/06/08/apple-reveals-new-ai-architecture/
Score: 359 | Comments: 324
---

[HACKERNEWS]
Siri AI
https://www.apple.com/apple-intelligence/
Score: 427 | Comments: 376
---

[HACKERNEWS]
Show HN: Performative-UI – A react component library of design tropes
https://vorpus.github.io/performativeUI/
Score: 803 | Comments: 156
---

[HACKERNEWS]
xAI is looking more like a datacentre REIT than a frontier lab
https://martinalderson.com/posts/xais-new-rental-business/
Score: 410 | Comments: 326
---

[HACKERNEWS]
MiMo-v2.5-Pro-UltraSpeed: 1T model with 1000 tokens per second
https://mimo.xiaomi.com/blog/mimo-tilert-1000tps
Score: 504 | Comments: 351
---

[HACKERNEWS]
Anti-social: It's fads, not friends, which now dominate social media feeds
https://www.bbc.com/worklife/article/20260520-how-social-media-ceased-to-be-social
Score: 558 | Comments: 415
---

[HACKERNEWS]
Apple Core AI Framework
https://developer.apple.com/documentation/coreai/
Score: 208 | Comments: 44
---

[HACKERNEWS]
EU-banned pesticides found in rice, tea and spices
https://www.foodwatch.org/en/eu-banned-pesticides-found-in-rice-tea-and-spices
Score: 250 | Comments: 91
---

[HACKERNEWS]
Show HN: Gitdot – a better GitHub. Open-source, written in Rust
https://gitdot.io/
Score: 160 | Comments: 127
---

[HACKERNEWS]
We Think the SpaceX IPO Is Overvalued
https://www.morningstar.com/stocks/why-we-think-spacex-ipo-is-overvalued?content_id=20768396545
Score: 46 | Comments: 23
---

[HACKERNEWS]
Why are cells small?
https://burrito.bio/essays/what-limits-a-cells-size
Score: 110 | Comments: 53
---

[HACKERNEWS]
Surveillance is not safety: A statement on the UK's latest threat to privacy [pdf]
https://signal.org/blog/pdfs/2026-06-08-uk-surveillance-is-not-safety.pdf
Score: 436 | Comments: 160
---

[HACKERNEWS]
FrontierCode
https://cognition.ai/blog/frontier-code
Score: 107 | Comments: 19
---

[HACKERNEWS]
Ask HN: What are tools you have made for yourself since the advent of AI?
https://news.ycombinator.com/item?id=48449187
Score: 157 | Comments: 290
---

[HACKERNEWS]
Confidential submission of draft S-1 to the SEC
https://openai.com/index/openai-submits-confidential-s-1/
Score: 303 | Comments: 220
---

[HACKERNEWS]
I'm building a parallel internet, and it's called The Thinnernet
https://inavoyage.blogspot.com/2026/06/im-building-parallel-internet-and-its.html
Score: 44 | Comments: 53
---

[HACKERNEWS]
Ask HN: Why hasn't there been a real competitor to Ticketmaster yet?
https://news.ycombinator.com/item?id=48448313
Score: 85 | Comments: 83
---

[HACKERNEWS]
Launch HN: Intuned (YC S22) – Build and run reliable browser automations as code
https://intunedhq.com
Score: 102 | Comments: 44
---

[ACADEMIC - ARXIV]
标题: MeCo: One-Step MeanFlow-based Corrector for Multi-Channel Speech Separation
作者: Dohwan Kim, Jung-Woo Choi
链接: https://arxiv.org/abs/2606.09677v1
完整摘要: While discriminative models for multi-channel speech separation excel in reference-based metrics, they often exhibit suboptimal human listening quality. To address this, we propose a novel MeanFlow-based one-step generative corrector (MeCo). MeCo learns a conditional average velocity field to map discriminative estimates directly onto the clean speech manifold in a single step. To maximize one-step generation performance, we introduce Data-Space Optimization (DSO). DSO integrates an $\mathbf{x}_r$-loss, which penalizes prediction errors on longer displacement intervals to serve as a generative objective for human listening quality, with an Endpoint SI-SDR loss that directly optimizes terminal signal fidelity. Experiments demonstrate that MeCo achieves state-of-the-art (SOTA) performance with minimal computational overhead, simultaneously achieving superior signal fidelity and human listening quality in both in-domain and out-of-domain scenarios.
匹配关键词: video generation
---

[ACADEMIC - ARXIV]
标题: Correlation Is Not Enough: Embedding Human Metadata for Individual Causal Discovery
作者: Suraj Biswas, Saurabh Gupta, Pritam Mukherjee
链接: https://arxiv.org/abs/2606.09672v1
完整摘要: Ask a pretrained biomedical language model whether "cortisol 28 ug/dL" and "stock-market volatility" are related, and it returns a cosine similarity of 0.83 on a scale where 1.0 means identical. The two share no mechanism. This is not a corner case: every off-the-shelf biomedical encoder we tested (BioBERT, PubMedBERT, BioM-ELECTRA) scores unrelated cross-domain pairs between 0.76 and 0.92 when the answer should be near zero. Accuracy on cross-domain discrimination is 0%. Retrieval systems survive this, because a language model downstream filters the noise. A Large Behavioural Model (LBM), a foundation model whose subject is a person rather than a sentence, does not: it reasons over a graph of a user's life and treats embedding proximity as evidence that two events are causally linked. False proximity writes a false causal edge, and everything downstream inherits the error. Here, embedding geometry is not a tuning knob; it is correctness. We report the fix. A contrastive pass over 72,034 pairs raises PubMedBERT BIOSSES correlation from 0.633 to 0.828 and within-vs-across-domain separation from 1.05x to 1.63x. A second pass, BODHI, mines hard negatives from edges absent in a biomedical knowledge graph and lifts separation to 2.30x and the discrimination gap to +0.392, at a 4.5% BIOSSES cost. On an Intel Xeon 6737P with AMX, OpenVINO cuts single-query latency from 1367 ms to 10 ms (133x) and reaches 555 sentences/sec. One finding contradicts standard advice: FP16 beats INT8 on this silicon at every serving batch size, and we explain why. The same model on a no-AMX Ice Lake instance runs 13-27x slower. We release the benchmark suite, training corpora, the BODHI generator, and the OpenVINO scripts.
匹配关键词: video generation
---

[ACADEMIC - ARXIV]
标题: Visual Prompting Meets Feature Reconstruction-Based Anomaly Detection with Dual-Teacher Supervision
作者: Mateo Diaz-Bone, Daniel Caraballo, Florian Scheidegger, Thomas Frick, Mattia Rigotti, Andrea Bartezzaghi, Roy Assaf, Niccolo Avogaro, Yagmur G. Cinar, Brown Ebouky, Filip M. Janicki, Piotr S. Kluska, Cezary Skura, Cristiano Malossi
链接: https://arxiv.org/abs/2606.09670v1
完整摘要: Recent Anomaly Detection methods achieve perfect detection and segmentation scores on well-established datasets, such as MVTec. However, many of these methods face challenges when foundational assumptions - such as consistent object scale, viewpoint, background, illumination, and centered placement - are violated. Those variations that occur render anomaly detection methods unusable in many real-world scenarios. To address these limitations, we introduce three key contributions: (1) a visual prompting pipeline that isolates objects using foreground-background masking; (2) a mechanism for unfreezing the teacher in student-teacher models to improve domain adaptability; and (3) a data augmentation strategy leveraging diffusion-generated synthetic images to enhance anomaly detection performance. We achieve a 3.5 percentage point improvement over the previous state-of-the-art on the challenging AeBAD dataset by using the Masked Multiscale Reconstruction (MMR) model as our backbone.
匹配关键词: video generation
---

[ACADEMIC - ARXIV]
标题: SpatialWorld: Benchmarking Interactive Spatial Reasoning of Multimodal Agents in Real-World Tasks
作者: Hongcheng Gao, Hailong Qu, Jingyi Tang, Jiahao Wang, Zihao Huang, Hengkang Qiao, Shihong Huang, Junming Yang, Yi Li, Hongyixuan Yuan, Wenjie Li, Bohan Zeng, Wenbo Li, Bo Wang, Jianhui Liu, Olive Huang, Haoyang Huang, Wentao Zhang, Guoqing Huang, Nan Duan, Yinpeng Dong
链接: https://arxiv.org/abs/2606.09669v1
完整摘要: Spatial reasoning is a foundational capability for multimodal large language models (MLLMs) to perceive and operate within the physical world. However, existing benchmarks predominantly rely on passive evaluation (e.g., static VQA) or simulator-specific pipelines, failing to assess general interactive spatial understanding. We introduce SpatialWorld, a unified benchmark designed specifically for evaluating the interactive spatial understanding of multimodal agents in complex real-world tasks. Integrating eight heterogeneous simulation backends under a shared, simulator-agnostic protocol, SpatialWorld features 760 human-annotated tasks across diverse domains (e.g., household routines, travel, social collaboration). Agents must solve tasks under vision-only partial observability, actively gathering egocentric visual evidence and expressing decisions via a unified, text-based action interface native to MLLMs. For reliable evaluation, each task includes a human-validated initial state, a reference trajectory, and a terminal-state verifier. Evaluating 15 advanced agents reveals that robust spatial task solving remains challenging: the strongest model, GPT-5, achieves an average task success rate (TSR) of only 17.4%, while the leading open-source model, Qwen-3.5, reaches 14.1%. Further analysis exposes a clear mismatch between task success and execution efficiency, alongside substantial domain-specific performance variations. These bottlenecks in active exploration and long-horizon planning position SpatialWorld as a rigorous testbed for future spatial agents.
匹配关键词: video generation
---

[ACADEMIC - ARXIV]
标题: Cross-Modal Masking for Robust Silent Speech Synthesis Using sEMG and Lipreading
作者: Eder del Blanco, David Gimeno-Gómez, Eva Navas, Carlos-D. Martínez-Hinarejos, Inma Hernáez
链接: https://arxiv.org/abs/2606.09667v1
完整摘要: Speech restoration through silent speech interfaces (SSIs) has emerged as a promising assistive technology for individuals with impaired or absent laryngeal voice production. Among non-invasive SSI modalities, surface electromyography (sEMG) and video-based lipreading provide complementary articulatory information, yet their integration for continuous speech synthesis remains underexplored. Moreover, existing multimodal approaches rarely address robustness to modality degradation or temporary sensor failure, limiting their applicability in realistic scenarios. In this work, we propose a masked multimodal speech synthesis framework that jointly leverages sEMG and lipreading signals through modality masking during training. Under multispeaker settings, the proposed approach reduces word error rate by up to 14 absolute percentage points compared to the strongest unimodal baseline. Experimental results not only show that masking strategies are critical for these performance gains and robustness under low-bitrate conditions, but also that they generalize better than degradation-specific data augmentations in the presence of modality absence conditions. Phone-level analyses further reveal complementary contributions across modalities, with particularly strong benefits for vowels and for specific consonant groups. Overall, these findings demonstrate the effectiveness and robustness of masked multimodal integration for silent speech synthesis, although adaptation to laryngectomized speakers remains an open research challenge.
匹配关键词: video generation
---

[ACADEMIC - ARXIV]
标题: Visual Prompting Meets Feature Reconstruction-Based Anomaly Detection with Dual-Teacher Supervision
作者: Mateo Diaz-Bone, Daniel Caraballo, Florian Scheidegger, Thomas Frick, Mattia Rigotti, Andrea Bartezzaghi, Roy Assaf, Niccolo Avogaro, Yagmur G. Cinar, Brown Ebouky, Filip M. Janicki, Piotr S. Kluska, Cezary Skura, Cristiano Malossi
链接: https://arxiv.org/abs/2606.09670v1
完整摘要: Recent Anomaly Detection methods achieve perfect detection and segmentation scores on well-established datasets, such as MVTec. However, many of these methods face challenges when foundational assumptions - such as consistent object scale, viewpoint, background, illumination, and centered placement - are violated. Those variations that occur render anomaly detection methods unusable in many real-world scenarios. To address these limitations, we introduce three key contributions: (1) a visual prompting pipeline that isolates objects using foreground-background masking; (2) a mechanism for unfreezing the teacher in student-teacher models to improve domain adaptability; and (3) a data augmentation strategy leveraging diffusion-generated synthetic images to enhance anomaly detection performance. We achieve a 3.5 percentage point improvement over the previous state-of-the-art on the challenging AeBAD dataset by using the Masked Multiscale Reconstruction (MMR) model as our backbone.
匹配关键词: video diffusion
---

[ACADEMIC - ARXIV]
标题: Cross-Modal Masking for Robust Silent Speech Synthesis Using sEMG and Lipreading
作者: Eder del Blanco, David Gimeno-Gómez, Eva Navas, Carlos-D. Martínez-Hinarejos, Inma Hernáez
链接: https://arxiv.org/abs/2606.09667v1
完整摘要: Speech restoration through silent speech interfaces (SSIs) has emerged as a promising assistive technology for individuals with impaired or absent laryngeal voice production. Among non-invasive SSI modalities, surface electromyography (sEMG) and video-based lipreading provide complementary articulatory information, yet their integration for continuous speech synthesis remains underexplored. Moreover, existing multimodal approaches rarely address robustness to modality degradation or temporary sensor failure, limiting their applicability in realistic scenarios. In this work, we propose a masked multimodal speech synthesis framework that jointly leverages sEMG and lipreading signals through modality masking during training. Under multispeaker settings, the proposed approach reduces word error rate by up to 14 absolute percentage points compared to the strongest unimodal baseline. Experimental results not only show that masking strategies are critical for these performance gains and robustness under low-bitrate conditions, but also that they generalize better than degradation-specific data augmentations in the presence of modality absence conditions. Phone-level analyses further reveal complementary contributions across modalities, with particularly strong benefits for vowels and for specific consonant groups. Overall, these findings demonstrate the effectiveness and robustness of masked multimodal integration for silent speech synthesis, although adaptation to laryngectomized speakers remains an open research challenge.
匹配关键词: video diffusion
---

[ACADEMIC - ARXIV]
标题: Do Video Foundation Models Understand Intuitive Physics? A Layerwise Probing Analysis
作者: Samuele Punzo, Niccolò Caselli, Ippokratis Pantelidis, Francesco Massafra, Salvatore Lo Sardo, Mohammadreza Salehi
链接: https://arxiv.org/abs/2606.09646v1
完整摘要: We study whether pretrained video foundation models encode intuitive-physics information in their frozen representations, and how this information varies across model families, layers, and probe types. Using frozen-feature probing on IntPhys2 and Minimal Video Pairs (MVP), we compare predictive joint-embedding models (V-JEPA), masked reconstruction models (VideoMAE), and a diffusion-based video generator (LTX-Video). V-JEPA achieves the strongest overall results across benchmarks, especially with probes that model temporal dynamics, while VideoMAE remains competitive and LTX-Video recovers weaker but non-trivial signal. Layerwise analyses show that physics-relevant information is weakest in early layers and becomes most accessible at intermediate-to-late depth, and temporal controls show that disrupting frame order substantially reduces performance, especially on MVP. Together, these results suggest that intuitive-physics knowledge emerges reliably in pretrained video representations, but its accessibility depends strongly on pretraining paradigm, representational depth, and readout mechanism.
匹配关键词: video diffusion
---

[ACADEMIC - ARXIV]
标题: MAVIS: Multi-Agent Video Retrieval via Structured Video Understanding
作者: Jie Zhang, Qilang Ye, Hao Zhou, Haochen Liang, Fei Luo
链接: https://arxiv.org/abs/2606.09641v1
完整摘要: The dominant paradigm in video retrieval relies on embedding-based full-corpus scanning, which suffers from inherent computational inefficiency and the semantic asymmetry between information-dense videos and sparse textual queries. To bridge this gap, we introduce \textbf{MAVIS}, a novel multi-agent framework that rethinks retrieval as cooperative reasoning rather than brute-force search. MAVIS first bridges the granularity mismatch by parsing raw videos into a \textbf{Structured Semantic Library}, enabling explicit attribute-level indexing. During retrieval, a planner decomposes complex user intents into atomic sub-tasks, dispatching specialized agents to independently nominate candidates. Crucially, MAVIS employs a \textbf{Logic-aware Debate} mechanism with a strict veto protocol, where agents collaboratively prune logical mismatches to identify a compact set of ``controversial'' candidates for fine-grained verification. This agentic workflow effectively bypasses the inefficiency of full-library traversal. Extensive experiments on MSR-VTT, MSVD, and ActivityNet demonstrate that MAVIS achieves competitive performance without task-specific fine-tuning, offering a scalable and interpretable alternative to traditional dual-encoder approaches.
匹配关键词: video diffusion
---

[ACADEMIC - ARXIV]
标题: CineDance: Towards Next-Generation Multi-Shot Long-Form Cinematic Audio-Video Generation
作者: Yuheng Chen, Teng Hu, Yuji Wang, Qingdong He, Zhucun Xue, Qianyu Zhou, Xiangtai Li, Lizhuang Ma, Jiangning Zhang, Dacheng Tao
链接: https://arxiv.org/abs/2606.09639v1
完整摘要: The fidelity and structural diversity of training datasets fundamentally determine the capabilities of video generation models. While commercial systems showremarkableabilitytogeneratecinematicnarratives, the progress of open-source models remains limited by the scarcity of high-quality training data. To bridge this gap, we introduce CineDance-1M, a large-scale, open research Text-to-Audio-Video (T2AV) dataset designed specifically for multi-shot, long-form joint audio-video generation. Averaging 92.8 seconds and 24.2 continuous shots per video, it provides configurable, structured annotations for both audio and video modalities. This exceptional quality is achieved through a rigorous three-stage curation pipeline: i) diverse sourcing and comprehensive cleansing, ii) film-theory-inspired narrative parsing, and iii) hierarchical dual-modal captioning. For a comprehensive assessment, we propose CineBench, featuring a diverse prompt suite and a six-dimensional, human-aligned metric system tailored for complex narrative audio-video evaluation. Furthermore, we adapt LTX-2.3 into CineDance, which demonstrates exceptional single-modality quality alongside precise audio-video alignment and robust subject and environment consistency, effectively validating our curation strategy and the high quality of CineDance-1M. We anticipate that this work will serve as a solid foundation for accelerating future research in multi-shot, long-form joint audio-video generation. Our project page is available at https://aliothchen.github.io/projects/CineDance/.
匹配关键词: video diffusion
---

[ACADEMIC - ARXIV]
标题: CineDance: Towards Next-Generation Multi-Shot Long-Form Cinematic Audio-Video Generation
作者: Yuheng Chen, Teng Hu, Yuji Wang, Qingdong He, Zhucun Xue, Qianyu Zhou, Xiangtai Li, Lizhuang Ma, Jiangning Zhang, Dacheng Tao
链接: https://arxiv.org/abs/2606.09639v1
完整摘要: The fidelity and structural diversity of training datasets fundamentally determine the capabilities of video generation models. While commercial systems showremarkableabilitytogeneratecinematicnarratives, the progress of open-source models remains limited by the scarcity of high-quality training data. To bridge this gap, we introduce CineDance-1M, a large-scale, open research Text-to-Audio-Video (T2AV) dataset designed specifically for multi-shot, long-form joint audio-video generation. Averaging 92.8 seconds and 24.2 continuous shots per video, it provides configurable, structured annotations for both audio and video modalities. This exceptional quality is achieved through a rigorous three-stage curation pipeline: i) diverse sourcing and comprehensive cleansing, ii) film-theory-inspired narrative parsing, and iii) hierarchical dual-modal captioning. For a comprehensive assessment, we propose CineBench, featuring a diverse prompt suite and a six-dimensional, human-aligned metric system tailored for complex narrative audio-video evaluation. Furthermore, we adapt LTX-2.3 into CineDance, which demonstrates exceptional single-modality quality alongside precise audio-video alignment and robust subject and environment consistency, effectively validating our curation strategy and the high quality of CineDance-1M. We anticipate that this work will serve as a solid foundation for accelerating future research in multi-shot, long-form joint audio-video generation. Our project page is available at https://aliothchen.github.io/projects/CineDance/.
匹配关键词: text-to-video
---

[ACADEMIC - ARXIV]
标题: Conan-embedding-v3: Fusing Modality-Specific Models for Omni-Modal Embedding
作者: Shiyu Li, Zhiyuan Hu, Yifan Wang, Peiming Li, Zheng Wei, Yang Tang
链接: https://arxiv.org/abs/2606.09331v1
完整摘要: Omni-modal retrieval promises a single embedding space for text, image, video, document, and audio inputs, but building such a unified retriever is difficult since these modalities differ in data distribution, architecture, and optimization dynamics. In this work, we present Conan-embedding-v3, a decouple--fuse--recover framework for omni-modal retrieval. Conan-embedding-v3 first trains modality specialists independently and fuses their task vectors into a single dense backbone, a strategy we call Decoupled Specialist Fusion. We show that this fusion composes visual, video, and document retrieval capabilities, but also exposes a failure mode for projector-based modalities: when audio is attached through an external encoder and projector, fusing the backbone leaves the projector calibrated to the audio-specialist backbone, causing a large audio retrieval regression despite copying all audio-specific modules unchanged. We call this failure Projector Drift. To repair it, Conan-embedding-v3 applies Projector Recovery (i.e., full-parameter fine-tuning of the projector while keeping the backbone frozen) followed by balanced multi-modal rehearsal. The resulting model supports these retrieval pathways in one backbone, achieving 74.9 scores on MMEB while obtaining 55.61 on the 30-task MAEB audio suite.
匹配关键词: text-to-video
---

[ACADEMIC - ARXIV]
标题: OmniGen-AR: AutoRegressive Any-to-Image Generation
作者: Junke Wang, Xun Wang, Qiushan Guo, Peize Sun, Weilin Huang, Zuxuan Wu, Yu-Gang Jiang
链接: https://arxiv.org/abs/2606.09156v1
完整摘要: Autoregressive (AR) models have demonstrated strong potential in visual generation, offering superior performance with simple architectures and optimization objectives. However, existing methods are typically limited to single-modality conditions, e.g., text, restricting their applicability in real-world scenarios that demand image synthesis from diverse controls. In this work, we present OmniGen-AR, a unified autoregressive framework for Any-to-Image generation. By discretizing various visual conditions through a shared visual tokenizer and text prompts with a text tokenizer, OmniGen-AR supports a broad spectrum of conditional inputs within a single model, including text (text-to-image generation), spatial signals (segmentation-to-image and depth-to-image), and visual context (image editing, frame prediction, and text-to-video generation). To mitigate the risk of information leakage from condition tokens to content tokens, we introduce Disentangled Causal Attention (DCA), which separates the full-sequence causal mask into condition causal attention and content causal attention. It serves as a training-time regularizer without affecting the standard next-token prediction during inference. With this design, OmniGen-AR achieves new state-of-the-art or at least competitive results across a range of benchmark, e.g., 0.63 on GenEval and 80.02 on VBench, demonstrating its effectiveness in flexible and high-fidelity visual generation.
匹配关键词: text-to-video
---

[ACADEMIC - ARXIV]
标题: Driving Video Retrieval for Complex Queries with Structured Grounding
作者: Manyi Yao, Sparsh Garg, Christian Shelton, Amit Roy-Chowdhury, Abhishek Aich
链接: https://arxiv.org/abs/2606.09109v1
完整摘要: Video retrieval at scale is central to data curation and safety validation in autonomous driving, where users want to find not only scenes but also dynamic events such as cut-ins and hard braking. Existing vision-language and keyword-based retrieval methods often miss these events because the relevant motion may not be explicitly described in text or captured by lexical overlap. Rule-based retrieval can encode such events more directly, but it is brittle: generated or hand-written rules often fail when their assumptions do not match real driving data. We propose STRIVE-D, a data-calibrated retrieval framework for driving videos. It uses weakly labeled in-domain videos to estimate when a query rule is reliable, adapt rules that mismatch observed data, and fuse calibrated rule scores with vision-language and keyword-based retrieval signals. Across three driving benchmarks, including newly released human-annotated event data on DrivingDojo, STRIVE-D delivers up to 84% relative improvement in top-1 accuracy over state-of-the-art methods.
匹配关键词: text-to-video
---

[ACADEMIC - ARXIV]
标题: HoliDubber: Holistic Video Dubbing for Complex Acoustic Scenes via Text-Guided Audio Synthesis
作者: Wenhao Guan, Yifan Duan, Junxi Liu, Yu Gu, Feng Dang, Kaidi Wang, Qingyang Hong, Lin Li, Xie Chen
链接: https://arxiv.org/abs/2606.09098v1
完整摘要: Video dubbing is a cornerstone of multimedia content creation, aiming to synthesize synchronized acoustic sequences for visual streams. While Text-to-Speech (TTS) and Text-to-Audio (TTA) generation have each achieved remarkable progress, existing dubbing systems remain confined to isolated speech synthesis without incorporating sound effects and ambient audio, forcing practitioners to rely on fragmented workflows and laborious manual post-mixing. To address this limitation, we present HoliDubber, a holistic video dubbing framework that moves beyond speech-only generation by enabling the joint synthesis of speech and sound effects from a single text prompt. Specifically, HoliDubber adopts a patch-based autoregressive diffusion transformer architecture, where a causal language model autoregressively models aggregated patch embeddings to capture global temporal structure, and a Diffusion Transformer decoder generates high-fidelity continuous tokens within each patch, following a divide-and-conquer strategy. To achieve cross-modal alignment, visual features are encoded into patch-level representations and fused with audio patches via cross-attention, enabling the model to ground speech generation in the speaker's visual articulation dynamics. In addition, we introduce HoliDub-Bench, a benchmark curated from established datasets with synchronized video-text-audio triplets designed for holistic dubbing evaluation. Extensive experiments demonstrate that HoliDubber significantly outperforms existing methods across multiple benchmarks in speech quality, synchronization, and speaker similarity. Furthermore, results on HoliDub-Bench validate the effectiveness of joint speech-and-sound generation, establishing a new paradigm for holistic video dubbing in complex acoustic scenes. \footnote{The demo page of the project is https://holidubber.github.io}
匹配关键词: text-to-video
---

[ACADEMIC - ARXIV]
标题: Cross-Modal Masking for Robust Silent Speech Synthesis Using sEMG and Lipreading
作者: Eder del Blanco, David Gimeno-Gómez, Eva Navas, Carlos-D. Martínez-Hinarejos, Inma Hernáez
链接: https://arxiv.org/abs/2606.09667v1
完整摘要: Speech restoration through silent speech interfaces (SSIs) has emerged as a promising assistive technology for individuals with impaired or absent laryngeal voice production. Among non-invasive SSI modalities, surface electromyography (sEMG) and video-based lipreading provide complementary articulatory information, yet their integration for continuous speech synthesis remains underexplored. Moreover, existing multimodal approaches rarely address robustness to modality degradation or temporary sensor failure, limiting their applicability in realistic scenarios. In this work, we propose a masked multimodal speech synthesis framework that jointly leverages sEMG and lipreading signals through modality masking during training. Under multispeaker settings, the proposed approach reduces word error rate by up to 14 absolute percentage points compared to the strongest unimodal baseline. Experimental results not only show that masking strategies are critical for these performance gains and robustness under low-bitrate conditions, but also that they generalize better than degradation-specific data augmentations in the presence of modality absence conditions. Phone-level analyses further reveal complementary contributions across modalities, with particularly strong benefits for vowels and for specific consonant groups. Overall, these findings demonstrate the effectiveness and robustness of masked multimodal integration for silent speech synthesis, although adaptation to laryngectomized speakers remains an open research challenge.
匹配关键词: video synthesis
---

[ACADEMIC - ARXIV]
标题: Do Video Foundation Models Understand Intuitive Physics? A Layerwise Probing Analysis
作者: Samuele Punzo, Niccolò Caselli, Ippokratis Pantelidis, Francesco Massafra, Salvatore Lo Sardo, Mohammadreza Salehi
链接: https://arxiv.org/abs/2606.09646v1
完整摘要: We study whether pretrained video foundation models encode intuitive-physics information in their frozen representations, and how this information varies across model families, layers, and probe types. Using frozen-feature probing on IntPhys2 and Minimal Video Pairs (MVP), we compare predictive joint-embedding models (V-JEPA), masked reconstruction models (VideoMAE), and a diffusion-based video generator (LTX-Video). V-JEPA achieves the strongest overall results across benchmarks, especially with probes that model temporal dynamics, while VideoMAE remains competitive and LTX-Video recovers weaker but non-trivial signal. Layerwise analyses show that physics-relevant information is weakest in early layers and becomes most accessible at intermediate-to-late depth, and temporal controls show that disrupting frame order substantially reduces performance, especially on MVP. Together, these results suggest that intuitive-physics knowledge emerges reliably in pretrained video representations, but its accessibility depends strongly on pretraining paradigm, representational depth, and readout mechanism.
匹配关键词: video synthesis
---

[ACADEMIC - ARXIV]
标题: MAVIS: Multi-Agent Video Retrieval via Structured Video Understanding
作者: Jie Zhang, Qilang Ye, Hao Zhou, Haochen Liang, Fei Luo
链接: https://arxiv.org/abs/2606.09641v1
完整摘要: The dominant paradigm in video retrieval relies on embedding-based full-corpus scanning, which suffers from inherent computational inefficiency and the semantic asymmetry between information-dense videos and sparse textual queries. To bridge this gap, we introduce \textbf{MAVIS}, a novel multi-agent framework that rethinks retrieval as cooperative reasoning rather than brute-force search. MAVIS first bridges the granularity mismatch by parsing raw videos into a \textbf{Structured Semantic Library}, enabling explicit attribute-level indexing. During retrieval, a planner decomposes complex user intents into atomic sub-tasks, dispatching specialized agents to independently nominate candidates. Crucially, MAVIS employs a \textbf{Logic-aware Debate} mechanism with a strict veto protocol, where agents collaboratively prune logical mismatches to identify a compact set of ``controversial'' candidates for fine-grained verification. This agentic workflow effectively bypasses the inefficiency of full-library traversal. Extensive experiments on MSR-VTT, MSVD, and ActivityNet demonstrate that MAVIS achieves competitive performance without task-specific fine-tuning, offering a scalable and interpretable alternative to traditional dual-encoder approaches.
匹配关键词: video synthesis
---

[ACADEMIC - ARXIV]
标题: CineDance: Towards Next-Generation Multi-Shot Long-Form Cinematic Audio-Video Generation
作者: Yuheng Chen, Teng Hu, Yuji Wang, Qingdong He, Zhucun Xue, Qianyu Zhou, Xiangtai Li, Lizhuang Ma, Jiangning Zhang, Dacheng Tao
链接: https://arxiv.org/abs/2606.09639v1
完整摘要: The fidelity and structural diversity of training datasets fundamentally determine the capabilities of video generation models. While commercial systems showremarkableabilitytogeneratecinematicnarratives, the progress of open-source models remains limited by the scarcity of high-quality training data. To bridge this gap, we introduce CineDance-1M, a large-scale, open research Text-to-Audio-Video (T2AV) dataset designed specifically for multi-shot, long-form joint audio-video generation. Averaging 92.8 seconds and 24.2 continuous shots per video, it provides configurable, structured annotations for both audio and video modalities. This exceptional quality is achieved through a rigorous three-stage curation pipeline: i) diverse sourcing and comprehensive cleansing, ii) film-theory-inspired narrative parsing, and iii) hierarchical dual-modal captioning. For a comprehensive assessment, we propose CineBench, featuring a diverse prompt suite and a six-dimensional, human-aligned metric system tailored for complex narrative audio-video evaluation. Furthermore, we adapt LTX-2.3 into CineDance, which demonstrates exceptional single-modality quality alongside precise audio-video alignment and robust subject and environment consistency, effectively validating our curation strategy and the high quality of CineDance-1M. We anticipate that this work will serve as a solid foundation for accelerating future research in multi-shot, long-form joint audio-video generation. Our project page is available at https://aliothchen.github.io/projects/CineDance/.
匹配关键词: video synthesis
---

[ACADEMIC - ARXIV]
标题: I Was Scrolling and Then I Saw a Pregnant Strawberry
作者: Piera Riccio
链接: https://arxiv.org/abs/2606.09589v1
完整摘要: AI minidramas (also known as fruit dramas) are short, algorithmically distributed generative AI video series featuring anthropomorphized characters that have recently emerged as a widespread phenomenon on social media platforms. This paper argues that despite their seemingly innocuous aesthetic, these videos reproduce deeply gendered narrative structures in which female characters are systematically associated with moral transgression, sexual betrayal, and reproductive capacity, and that several plots also encode the logic of racialization, i.e., the process by which visible bodily difference is morally loaded. Drawing on feminist film theory, critical race theory, and platform studies, it further argues that the generative AI aesthetic of these videos, characterized by softness, roundness, and visual cuteness, functions as a mechanism of aesthetic laundering, neutralizing the ideological weight of these narratives and enabling their circulation despite content moderation systems. This paper approaches these questions through personal observation and close reading, reflecting on the specific affordances of generative AI that make this phenomenon both possible and culturally consequential for the field of computational creativity.
匹配关键词: video synthesis
---

[ACADEMIC - ARXIV]
标题: Cross-Modal Masking for Robust Silent Speech Synthesis Using sEMG and Lipreading
作者: Eder del Blanco, David Gimeno-Gómez, Eva Navas, Carlos-D. Martínez-Hinarejos, Inma Hernáez
链接: https://arxiv.org/abs/2606.09667v1
完整摘要: Speech restoration through silent speech interfaces (SSIs) has emerged as a promising assistive technology for individuals with impaired or absent laryngeal voice production. Among non-invasive SSI modalities, surface electromyography (sEMG) and video-based lipreading provide complementary articulatory information, yet their integration for continuous speech synthesis remains underexplored. Moreover, existing multimodal approaches rarely address robustness to modality degradation or temporary sensor failure, limiting their applicability in realistic scenarios. In this work, we propose a masked multimodal speech synthesis framework that jointly leverages sEMG and lipreading signals through modality masking during training. Under multispeaker settings, the proposed approach reduces word error rate by up to 14 absolute percentage points compared to the strongest unimodal baseline. Experimental results not only show that masking strategies are critical for these performance gains and robustness under low-bitrate conditions, but also that they generalize better than degradation-specific data augmentations in the presence of modality absence conditions. Phone-level analyses further reveal complementary contributions across modalities, with particularly strong benefits for vowels and for specific consonant groups. Overall, these findings demonstrate the effectiveness and robustness of masked multimodal integration for silent speech synthesis, although adaptation to laryngectomized speakers remains an open research challenge.
匹配关键词: video editing
---

[ACADEMIC - ARXIV]
标题: Do Video Foundation Models Understand Intuitive Physics? A Layerwise Probing Analysis
作者: Samuele Punzo, Niccolò Caselli, Ippokratis Pantelidis, Francesco Massafra, Salvatore Lo Sardo, Mohammadreza Salehi
链接: https://arxiv.org/abs/2606.09646v1
完整摘要: We study whether pretrained video foundation models encode intuitive-physics information in their frozen representations, and how this information varies across model families, layers, and probe types. Using frozen-feature probing on IntPhys2 and Minimal Video Pairs (MVP), we compare predictive joint-embedding models (V-JEPA), masked reconstruction models (VideoMAE), and a diffusion-based video generator (LTX-Video). V-JEPA achieves the strongest overall results across benchmarks, especially with probes that model temporal dynamics, while VideoMAE remains competitive and LTX-Video recovers weaker but non-trivial signal. Layerwise analyses show that physics-relevant information is weakest in early layers and becomes most accessible at intermediate-to-late depth, and temporal controls show that disrupting frame order substantially reduces performance, especially on MVP. Together, these results suggest that intuitive-physics knowledge emerges reliably in pretrained video representations, but its accessibility depends strongly on pretraining paradigm, representational depth, and readout mechanism.
匹配关键词: video editing
---

[ACADEMIC - ARXIV]
标题: MAVIS: Multi-Agent Video Retrieval via Structured Video Understanding
作者: Jie Zhang, Qilang Ye, Hao Zhou, Haochen Liang, Fei Luo
链接: https://arxiv.org/abs/2606.09641v1
完整摘要: The dominant paradigm in video retrieval relies on embedding-based full-corpus scanning, which suffers from inherent computational inefficiency and the semantic asymmetry between information-dense videos and sparse textual queries. To bridge this gap, we introduce \textbf{MAVIS}, a novel multi-agent framework that rethinks retrieval as cooperative reasoning rather than brute-force search. MAVIS first bridges the granularity mismatch by parsing raw videos into a \textbf{Structured Semantic Library}, enabling explicit attribute-level indexing. During retrieval, a planner decomposes complex user intents into atomic sub-tasks, dispatching specialized agents to independently nominate candidates. Crucially, MAVIS employs a \textbf{Logic-aware Debate} mechanism with a strict veto protocol, where agents collaboratively prune logical mismatches to identify a compact set of ``controversial'' candidates for fine-grained verification. This agentic workflow effectively bypasses the inefficiency of full-library traversal. Extensive experiments on MSR-VTT, MSVD, and ActivityNet demonstrate that MAVIS achieves competitive performance without task-specific fine-tuning, offering a scalable and interpretable alternative to traditional dual-encoder approaches.
匹配关键词: video editing
---

[ACADEMIC - ARXIV]
标题: CineDance: Towards Next-Generation Multi-Shot Long-Form Cinematic Audio-Video Generation
作者: Yuheng Chen, Teng Hu, Yuji Wang, Qingdong He, Zhucun Xue, Qianyu Zhou, Xiangtai Li, Lizhuang Ma, Jiangning Zhang, Dacheng Tao
链接: https://arxiv.org/abs/2606.09639v1
完整摘要: The fidelity and structural diversity of training datasets fundamentally determine the capabilities of video generation models. While commercial systems showremarkableabilitytogeneratecinematicnarratives, the progress of open-source models remains limited by the scarcity of high-quality training data. To bridge this gap, we introduce CineDance-1M, a large-scale, open research Text-to-Audio-Video (T2AV) dataset designed specifically for multi-shot, long-form joint audio-video generation. Averaging 92.8 seconds and 24.2 continuous shots per video, it provides configurable, structured annotations for both audio and video modalities. This exceptional quality is achieved through a rigorous three-stage curation pipeline: i) diverse sourcing and comprehensive cleansing, ii) film-theory-inspired narrative parsing, and iii) hierarchical dual-modal captioning. For a comprehensive assessment, we propose CineBench, featuring a diverse prompt suite and a six-dimensional, human-aligned metric system tailored for complex narrative audio-video evaluation. Furthermore, we adapt LTX-2.3 into CineDance, which demonstrates exceptional single-modality quality alongside precise audio-video alignment and robust subject and environment consistency, effectively validating our curation strategy and the high quality of CineDance-1M. We anticipate that this work will serve as a solid foundation for accelerating future research in multi-shot, long-form joint audio-video generation. Our project page is available at https://aliothchen.github.io/projects/CineDance/.
匹配关键词: video editing
---

[ACADEMIC - ARXIV]
标题: I Was Scrolling and Then I Saw a Pregnant Strawberry
作者: Piera Riccio
链接: https://arxiv.org/abs/2606.09589v1
完整摘要: AI minidramas (also known as fruit dramas) are short, algorithmically distributed generative AI video series featuring anthropomorphized characters that have recently emerged as a widespread phenomenon on social media platforms. This paper argues that despite their seemingly innocuous aesthetic, these videos reproduce deeply gendered narrative structures in which female characters are systematically associated with moral transgression, sexual betrayal, and reproductive capacity, and that several plots also encode the logic of racialization, i.e., the process by which visible bodily difference is morally loaded. Drawing on feminist film theory, critical race theory, and platform studies, it further argues that the generative AI aesthetic of these videos, characterized by softness, roundness, and visual cuteness, functions as a mechanism of aesthetic laundering, neutralizing the ideological weight of these narratives and enabling their circulation despite content moderation systems. This paper approaches these questions through personal observation and close reading, reflecting on the specific affordances of generative AI that make this phenomenon both possible and culturally consequential for the field of computational creativity.
匹配关键词: video editing
---

[ACADEMIC - ARXIV]
标题: SpatialWorld: Benchmarking Interactive Spatial Reasoning of Multimodal Agents in Real-World Tasks
作者: Hongcheng Gao, Hailong Qu, Jingyi Tang, Jiahao Wang, Zihao Huang, Hengkang Qiao, Shihong Huang, Junming Yang, Yi Li, Hongyixuan Yuan, Wenjie Li, Bohan Zeng, Wenbo Li, Bo Wang, Jianhui Liu, Olive Huang, Haoyang Huang, Wentao Zhang, Guoqing Huang, Nan Duan, Yinpeng Dong
链接: https://arxiv.org/abs/2606.09669v1
完整摘要: Spatial reasoning is a foundational capability for multimodal large language models (MLLMs) to perceive and operate within the physical world. However, existing benchmarks predominantly rely on passive evaluation (e.g., static VQA) or simulator-specific pipelines, failing to assess general interactive spatial understanding. We introduce SpatialWorld, a unified benchmark designed specifically for evaluating the interactive spatial understanding of multimodal agents in complex real-world tasks. Integrating eight heterogeneous simulation backends under a shared, simulator-agnostic protocol, SpatialWorld features 760 human-annotated tasks across diverse domains (e.g., household routines, travel, social collaboration). Agents must solve tasks under vision-only partial observability, actively gathering egocentric visual evidence and expressing decisions via a unified, text-based action interface native to MLLMs. For reliable evaluation, each task includes a human-validated initial state, a reference trajectory, and a terminal-state verifier. Evaluating 15 advanced agents reveals that robust spatial task solving remains challenging: the strongest model, GPT-5, achieves an average task success rate (TSR) of only 17.4%, while the leading open-source model, Qwen-3.5, reaches 14.1%. Further analysis exposes a clear mismatch between task success and execution efficiency, alongside substantial domain-specific performance variations. These bottlenecks in active exploration and long-horizon planning position SpatialWorld as a rigorous testbed for future spatial agents.
匹配关键词: video understanding
---

[ACADEMIC - ARXIV]
标题: Cross-Modal Masking for Robust Silent Speech Synthesis Using sEMG and Lipreading
作者: Eder del Blanco, David Gimeno-Gómez, Eva Navas, Carlos-D. Martínez-Hinarejos, Inma Hernáez
链接: https://arxiv.org/abs/2606.09667v1
完整摘要: Speech restoration through silent speech interfaces (SSIs) has emerged as a promising assistive technology for individuals with impaired or absent laryngeal voice production. Among non-invasive SSI modalities, surface electromyography (sEMG) and video-based lipreading provide complementary articulatory information, yet their integration for continuous speech synthesis remains underexplored. Moreover, existing multimodal approaches rarely address robustness to modality degradation or temporary sensor failure, limiting their applicability in realistic scenarios. In this work, we propose a masked multimodal speech synthesis framework that jointly leverages sEMG and lipreading signals through modality masking during training. Under multispeaker settings, the proposed approach reduces word error rate by up to 14 absolute percentage points compared to the strongest unimodal baseline. Experimental results not only show that masking strategies are critical for these performance gains and robustness under low-bitrate conditions, but also that they generalize better than degradation-specific data augmentations in the presence of modality absence conditions. Phone-level analyses further reveal complementary contributions across modalities, with particularly strong benefits for vowels and for specific consonant groups. Overall, these findings demonstrate the effectiveness and robustness of masked multimodal integration for silent speech synthesis, although adaptation to laryngectomized speakers remains an open research challenge.
匹配关键词: video understanding
---

[ACADEMIC - ARXIV]
标题: Do Video Foundation Models Understand Intuitive Physics? A Layerwise Probing Analysis
作者: Samuele Punzo, Niccolò Caselli, Ippokratis Pantelidis, Francesco Massafra, Salvatore Lo Sardo, Mohammadreza Salehi
链接: https://arxiv.org/abs/2606.09646v1
完整摘要: We study whether pretrained video foundation models encode intuitive-physics information in their frozen representations, and how this information varies across model families, layers, and probe types. Using frozen-feature probing on IntPhys2 and Minimal Video Pairs (MVP), we compare predictive joint-embedding models (V-JEPA), masked reconstruction models (VideoMAE), and a diffusion-based video generator (LTX-Video). V-JEPA achieves the strongest overall results across benchmarks, especially with probes that model temporal dynamics, while VideoMAE remains competitive and LTX-Video recovers weaker but non-trivial signal. Layerwise analyses show that physics-relevant information is weakest in early layers and becomes most accessible at intermediate-to-late depth, and temporal controls show that disrupting frame order substantially reduces performance, especially on MVP. Together, these results suggest that intuitive-physics knowledge emerges reliably in pretrained video representations, but its accessibility depends strongly on pretraining paradigm, representational depth, and readout mechanism.
匹配关键词: video understanding
---

[ACADEMIC - ARXIV]
标题: Modeling Components and Connections in Cyber-Physical Systems
作者: Kate Sanborn, Tanuj Kenchannavar, Vakul Nath, Jonathan Sprinkle
链接: https://arxiv.org/abs/2606.09645v1
完整摘要: Text based configuration files for cyber-physical systems show the hierarchy of component modules well but often hide the details of connections and interfaces between modules. A model-based visual approach to these configuration files can better capture this information. The XML structure of Robot Operating System (ROS) launch files can be improved using a modeling approach. This paper presents ROSLaunchVisual, a model-integrated environment built on WebGME for designing, visualizing, and managing ROS launch files. The tool raises the level of abstraction by allowing developers to create and modify launch files using a graphical interface that represents nodes, publishers, subscribers, and arguments as interconnected components. The tool provides a dynamic system analysis that can then be used in the static development and analysis of new and existing launch files. ROSLaunchVisual incorporates features such as metamodel-driven validation, automatic import/export of launch files, and visual communication mapping. Plugins further enhance functionality by updating libraries, checking for semantic errors, and managing remaps. By making launch file creation more intuitive and less error-prone, ROSLaunchVisual improves development efficiency and system understanding, especially in collaborative or large-scale robotics projects.
匹配关键词: video understanding
---

[ACADEMIC - ARXIV]
标题: MAVIS: Multi-Agent Video Retrieval via Structured Video Understanding
作者: Jie Zhang, Qilang Ye, Hao Zhou, Haochen Liang, Fei Luo
链接: https://arxiv.org/abs/2606.09641v1
完整摘要: The dominant paradigm in video retrieval relies on embedding-based full-corpus scanning, which suffers from inherent computational inefficiency and the semantic asymmetry between information-dense videos and sparse textual queries. To bridge this gap, we introduce \textbf{MAVIS}, a novel multi-agent framework that rethinks retrieval as cooperative reasoning rather than brute-force search. MAVIS first bridges the granularity mismatch by parsing raw videos into a \textbf{Structured Semantic Library}, enabling explicit attribute-level indexing. During retrieval, a planner decomposes complex user intents into atomic sub-tasks, dispatching specialized agents to independently nominate candidates. Crucially, MAVIS employs a \textbf{Logic-aware Debate} mechanism with a strict veto protocol, where agents collaboratively prune logical mismatches to identify a compact set of ``controversial'' candidates for fine-grained verification. This agentic workflow effectively bypasses the inefficiency of full-library traversal. Extensive experiments on MSR-VTT, MSVD, and ActivityNet demonstrate that MAVIS achieves competitive performance without task-specific fine-tuning, offering a scalable and interpretable alternative to traditional dual-encoder approaches.
匹配关键词: video understanding
---

[ACADEMIC - ARXIV]
标题: SoccerNet 2026 Player-Centric Ball-Action Spotting:Retraining and Post-Processing Extensions to the FOOTPASS Baselines
作者: Parthsarthi Rawat
链接: https://arxiv.org/abs/2606.09679v1
完整摘要: We describe our system for the SoccerNet 2026 Player-Centric Ball-Action Spotting Challenge, which requires predicting who performs which action and when, across eight classes in broadcast soccer. Building on the three FOOTPASS baselines [1] (TAAD, TAAD+GNN, and TAAD+DST), we contribute four extensions: (1) gradient check pointing to enable full-backbone fine-tuning on a single GPU; (2) fusion of GNN logits into the DST encoder, combining graph-based tactical context with per-player visual features; (3) square-root frequency class weighting to address the 213:1 pass-to-tackle imbalance in the training data; and (4) a post processing pipeline comprising per-class logit gating, temporal frame refinement, jersey re-assignment, and a two-model ensemble. Our system achieves 0.548 Macro F1 on the test set and 0.446 on the challenge set (server evaluation).
匹配关键词: temporal consistency
---

[ACADEMIC - ARXIV]
标题: Transition-Based Digital Twin Modelling for Alzheimer's Disease under Sparse Longitudinal Data
作者: Yinyu Huang, Yilin Zhang, Sofia Michopoulou, Christopher Kipps, Rahman Attar
链接: https://arxiv.org/abs/2606.09671v1
完整摘要: Alzheimer's disease (AD) progression is highly heterogeneous and is typically observed through sparse and irregular longitudinal data, posing challenges for prediction and personalised monitoring. Existing machine learning approaches have improved AD prediction using multimodal data, yet often focus on static classification or cohort-level risk estimation, providing limited support for subject-specific modelling and uncertainty-aware reasoning. To address these limitations, we present a personalised digital twin framework for AD prediction and scenario-based analysis using multimodal longitudinal data. The proposed approach integrates complementary modelling strategies to capture clinical transitions and temporal dependencies across visits. Using data from the Alzheimer's Disease Neuroimaging Initiative (ADNI), including cognitive assessments, clinical variables, and MRI-derived phenotypes, the framework predicts cognitive status and diagnostic categories while quantifying predictive uncertainty and enabling patient-specific what-if trajectory analysis. Evaluation on leak-free subject-level splits demonstrates strong performance in score forecasting and diagnosis classification. In this sparse and irregular ADNI setting, transition-based modelling of adjacent visits achieved higher predictive accuracy than the sequence-based branch, suggesting that local transition modelling may be more data-efficient. While sequence models remain valuable for uncertainty-aware trajectory forecasting, local transition modelling offers a more data-efficient and robust predictive strategy. These findings highlight the importance of aligning temporal modelling strategies with clinical data structure and suggest that transition-based digital twin formulations may provide a practical and interpretable approach for personalised disease forecasting in neurodegenerative disorders.
匹配关键词: temporal consistency
---

[ACADEMIC - ARXIV]
标题: Visual Prompting Meets Feature Reconstruction-Based Anomaly Detection with Dual-Teacher Supervision
作者: Mateo Diaz-Bone, Daniel Caraballo, Florian Scheidegger, Thomas Frick, Mattia Rigotti, Andrea Bartezzaghi, Roy Assaf, Niccolo Avogaro, Yagmur G. Cinar, Brown Ebouky, Filip M. Janicki, Piotr S. Kluska, Cezary Skura, Cristiano Malossi
链接: https://arxiv.org/abs/2606.09670v1
完整摘要: Recent Anomaly Detection methods achieve perfect detection and segmentation scores on well-established datasets, such as MVTec. However, many of these methods face challenges when foundational assumptions - such as consistent object scale, viewpoint, background, illumination, and centered placement - are violated. Those variations that occur render anomaly detection methods unusable in many real-world scenarios. To address these limitations, we introduce three key contributions: (1) a visual prompting pipeline that isolates objects using foreground-background masking; (2) a mechanism for unfreezing the teacher in student-teacher models to improve domain adaptability; and (3) a data augmentation strategy leveraging diffusion-generated synthetic images to enhance anomaly detection performance. We achieve a 3.5 percentage point improvement over the previous state-of-the-art on the challenging AeBAD dataset by using the Masked Multiscale Reconstruction (MMR) model as our backbone.
匹配关键词: temporal consistency
---

[ACADEMIC - ARXIV]
标题: When Built-in Thinking Helps and Hurts: Constraint-Level Error Shifts in Instruction Following
作者: Sai Adith Senthil Kumar
链接: https://arxiv.org/abs/2606.09662v1
完整摘要: Large reasoning models (LRMs) often improve math and coding performance, but their effect on instruction following is unclear. We study IFEval with Qwen3 models (1.7B-32B), using same-weights Thinking ON/OFF controls; four Hunyuan models provide directional cross-family support. Aggregate pass-rate changes are small (-0.55 to -3.52 pp), yet 10-20% of prompts switch between pass and fail across modes, suggesting that thinking changes the pattern of errors--some prompts improve while others worsen--rather than uniformly degrading performance. Under a post-hoc Qwen3-derived grouping, constraint types separate into Planning (global counting, structure, coordination), which improves at the class level under thinking, and Precision (exact local form), which consistently worsens; the class-level Planning/Precision sign pattern holds directionally for all four Hunyuan models despite Hunyuan's opposite aggregate direction. Thinking also changes final-answer length; matched-length analyses substantially reduce the Precision drop, but a residual penalty remains. Analyzing thinking traces with a cross-encoder relevance metric reveals three patterns: Neutral shows a positive relevance-compliance link (r approximately 0.15); Planning shows near-zero predictive correlation (r approximately 0.02) despite measurable trace engagement, consistent with an execution gap between CE-measured trace relevance and final-answer compliance; Precision shows a small negative correlation (r approximately -0.05), with failing instances having higher mean relevance than passing ones. Activation patching across four model sizes (1.7B-14B) shows that Precision flip instances are more often restored than Planning flip instances (32-58% vs. 14-40% mean layer-restoration), with the largest gap at 14B (about 30 pp).
匹配关键词: temporal consistency
---

[ACADEMIC - ARXIV]
标题: Muon Learns More Robust and Transferable Features than Adam
作者: Tianyu Ruan, Fengzhuo Zhang, Shuche Wang, Shihua Zhang
链接: https://arxiv.org/abs/2606.09658v1
完整摘要: Muon has recently emerged as a state-of-the-art optimizer for pretraining Large Language Models (LLMs) and vision classifiers. Despite its efficiency advantage over Adam and SGD, the feature-learning advantage of Muon remains unclear. This paper investigates Muon's feature-learning advantage through the lens of robustness and transferability. First, by evaluating pretrained models on corrupted images and texts, we show that features learned by Muon are consistently more robust than those learned by Adam and SGD across different architectures, including transformers and Convolutional Neural Networks (CNNs). Using trained layer-wise probes, we further show that this robustness advantage is reflected in larger logit margins across layers. Second, by training linear classifiers or fine-tuning full models from pretrained parameters on downstream tasks, we demonstrate that Muon-learned features transfer more effectively than those learned by Adam and SGD. This transferability advantage is further supported by the diversity of hidden states across layers, as measured by effective rank. Finally, in a representative classification problem with multi-component features, we prove that Muon attains larger margins and higher effective rank than Adam and SGD, providing theoretical support for our empirical findings.
匹配关键词: temporal consistency
---

[ACADEMIC - ARXIV]
标题: V2V-Bench: A Comprehensive Benchmark for Video-to-Video Generation Evaluation
作者: Tao Liu, Leela Krishna, Gouti Pavan Kumar, Sreeja K, Vishav Garg
链接: https://arxiv.org/abs/2606.05665v1
完整摘要: Video-to-video (V2V) generation is difficult to evaluate because outputs must both follow editing instructions and preserve frame-level correspondence with the source video, which existing T2V and I2V metrics do not capture. We introduce V2V-Bench, a 11-dimension benchmark organized into five categories: temporal alignment, structural fidelity, transformation quality, video quality, and semantic alignment. V2V-Bench pairs diverse source videos with challenging editing tasks and evaluates two commercial models, Grok Imagine and Gemini Veo3, and one open-source model, Open Sora 2. Results show complementary model strengths: Grok performs better on editing fidelity, while Veo3 achieves stronger visual quality. On six V2V-specific dimensions, V2V-Bench reaches a Spearman correlation of 0.905 with human judgments.
匹配关键词: Sora
---

[ACADEMIC - ARXIV]
标题: SafeGen-Bench: Benchmarking Safety in Image-Conditioned Text-to-Video Generation
作者: Yingzi Ma, Xiaogeng Liu, Yawen Zheng, Chaowei Xiao
链接: https://arxiv.org/abs/2606.01481v1
完整摘要: With the rapid advancements in text-to-image diffusion models, generative video models (T2V models) like Sora can now produce short synthetic videos from a text prompt or an initial image. However, synthetic video generation -- especially when guided by an initial image -- often poses risks, including the potential creation of illegal, politically sensitive, or unethical content. Existing benchmarks have started to consider the safety of generated videos, but they primarily focus on testing models with malicious text prompts, ignoring the scenario where text prompt and image combination may still lead to harmful video content. In practice, this is a common and challenging issue: videos generated from safe text and image inputs can nonetheless convey harmful information. To bridge this gap, we introduce SafeGen-Bench, a benchmark specifically designed to evaluate the safety of conditional T2V models. Our benchmark defines 10 malicious categories, concentrating on risks related to both temporal sequences and depicted behaviors. SafeGen-Bench consists of carefully selected start frames from diverse image and video sources, paired with corresponding text prompts to simulate realistic inputs. We evaluate a variety of conditional T2V models on SafeGen-Bench, and the results indicate that current models struggle to consistently avoid generating malicious content with unsafety scores reaching up to 44.5, especially under conditions requiring high quality. Furthermore, we assess the effectiveness of both text-based and image-based guardrails on our benchmark, finding that unimodal guardrails alone were insufficient to provide a robust defense, with an 80\% failure rate across seven malicious categories. We hope that SafeGen-Bench will foster the development of safer and more controllable conditional T2V models.
匹配关键词: Sora
---

[ACADEMIC - ARXIV]
标题: SORA: Free Second-Order Attacks in Fast Adversarial Training
作者: Mazdak Teymourian, Ramtin Moslemi, Farzan Rahmani, Mohammad Hossein Rohban
链接: https://arxiv.org/abs/2606.00738v1
完整摘要: Adversarial Training (AT) is a leading defense against adversarial examples but often suffers from Catastrophic Overfitting (CO) in efficient single-step variants, where robustness to multi-step attacks collapses despite high single-step performance. We address this failure mode with two contributions. First, we formalize Epsilon Overfitting (EO), a perspective in which fixed perturbation magnitudes and directions exacerbate CO, and show that introducing perturbation variability significantly improves robust generalization across different architectures and datasets. Second, we propose PertAlign (Perturbation Alignment), a theoretically grounded, computationally negligible metric that predicts CO onset by measuring gradient alignment across attack stages. Leveraging these insights, we introduce SORA, an adaptive step-size AT method that dynamically adjusts perturbations based on loss surface geometry. SORA consistently prevents CO, achieves state-of-the-art robustness and clean accuracy, and generalizes across datasets and architectures using a single fixed set of hyperparameters, which is essential for applicability in fast AT. Extensive experiments on diverse datasets and architectures show that SORA matches or surpasses the robustness of prior methods while delivering higher clean accuracy and superior efficiency. Code is available at https://github.com/SecondOrderAT/SORA.
匹配关键词: Sora
---

[ACADEMIC - ARXIV]
标题: World Models: A Comprehensive Survey of Architectures, Methodologies, Reasoning Paradigms, and Applications
作者: Arif Hassan Zidan, Yi Pan, Hanqi Jiang, Ruiyu Yan, Wei Ruan, Zihao Wu, Lifeng Chen, Weihang You, Xinliang Li, Bowen Chen, Huawen Hu, Peilong Wang, Sizhuang Liu, Jing Zhang, Siyuan Li, Zhengliang Liu, Yu Bao, Lin Zhao, Lichao Sun, Dajiang Zhu, Xiang Li, Jinglei Lv, Quanzheng Li, Wei Liu, Tianming Liu, Wei Zhang
链接: https://arxiv.org/abs/2606.00133v1
完整摘要: World models, internal simulators that learn the structure and dynamics of an environment, have emerged as a central paradigm in the pursuit of artificial general intelligence, enabling agents to predict, plan, and reason within learned representations. Despite rapid progress across reinforcement learning, robotics, autonomous driving, and video generation, the field lacks a unified framework integrating its diverse architectural choices, training methods, reasoning mechanisms, and application settings. This survey addresses that gap with a multi-axis taxonomy organized along four dimensions: (i) architecture, encompassing representation format, dynamics formulation, input modality, learning paradigm, and downstream application; (ii) methodological family, including state-space and recurrent approaches, transformer-based models, diffusion-based generators, physics-informed networks, and language-augmented multimodal systems; (iii) reasoning strategy, covering imagination-based planning, latent policy learning, counterfactual reasoning, and planning under uncertainty; and (iv) application domain, spanning robotics, autonomous driving, video prediction, multimodal agents, reinforcement learning, scientific modeling, medical imaging, educational measurement, and business and finance. Tracing the field from early cognitive-science foundations to milestone systems such as PlaNet, the Dreamer family, MuZero, Sora, Cosmos, and Genie, we examine how these dimensions interact and highlight the recent convergence of chain-of-thought reasoning with world-model imagination. We review evaluation protocols and benchmarks, identify persistent challenges such as compounding prediction errors, sim-to-real transfer, and fragmented evaluation, and outline future directions toward unified multimodal world models, foundation-scale interactive simulators, and safe deployment in safety-critical domains.
匹配关键词: Sora
---

[ACADEMIC - ARXIV]
标题: SpecSem-Net: Integrating Spectral and Semantic Features for Robust AI-generated Video Detection
作者: Zixi Wei, Huixuaun Zhang, Xiaojun Wan
链接: https://arxiv.org/abs/2605.17311v1
完整摘要: The remarkable visual fidelity of recent commercial video generative models, such as Sora and Veo, renders robust AI-generated video detection increasingly essential to prevent synthetic content from being indistinguishable from real videos and exploited for disinformation. However, existing detectors often fail due to an over-reliance on increasingly realistic semantic features, neglecting subtle spectral artifacts. In this paper, we propose SpecSem-Net, the first framework to introduce a semantic-guided spectral denoising mechanism specifically for high-fidelity AI-generated video detection. Specifically, we design a spectral module to extract high-frequency features via Fourier-Transform based filtering. Furthermore, to reduce misjudgments arising from spectral noise, we employ a Gated Merging Mechanism to adaptively fuse semantic context, effectively mitigating spectral noise. Additionally, to evaluate detector performance on the latest top-tier generative models, we construct a comprehensive benchmark comprising 5 SOTA commercial generators. Extensive experiments demonstrate that SpecSem-Net outperforms existing methods, achieving accuracies of 87.25% and 95.59% on our benchmark and public datasets, respectively.
匹配关键词: Sora
---

[ACADEMIC - ARXIV]
标题: SoccerNet 2026 Player-Centric Ball-Action Spotting:Retraining and Post-Processing Extensions to the FOOTPASS Baselines
作者: Parthsarthi Rawat
链接: https://arxiv.org/abs/2606.09679v1
完整摘要: We describe our system for the SoccerNet 2026 Player-Centric Ball-Action Spotting Challenge, which requires predicting who performs which action and when, across eight classes in broadcast soccer. Building on the three FOOTPASS baselines [1] (TAAD, TAAD+GNN, and TAAD+DST), we contribute four extensions: (1) gradient check pointing to enable full-backbone fine-tuning on a single GPU; (2) fusion of GNN logits into the DST encoder, combining graph-based tactical context with per-player visual features; (3) square-root frequency class weighting to address the 213:1 pass-to-tackle imbalance in the training data; and (4) a post processing pipeline comprising per-class logit gating, temporal frame refinement, jersey re-assignment, and a two-model ensemble. Our system achieves 0.548 Macro F1 on the test set and 0.446 on the challenge set (server evaluation).
匹配关键词: video foundation model
---

[ACADEMIC - ARXIV]
标题: MeCo: One-Step MeanFlow-based Corrector for Multi-Channel Speech Separation
作者: Dohwan Kim, Jung-Woo Choi
链接: https://arxiv.org/abs/2606.09677v1
完整摘要: While discriminative models for multi-channel speech separation excel in reference-based metrics, they often exhibit suboptimal human listening quality. To address this, we propose a novel MeanFlow-based one-step generative corrector (MeCo). MeCo learns a conditional average velocity field to map discriminative estimates directly onto the clean speech manifold in a single step. To maximize one-step generation performance, we introduce Data-Space Optimization (DSO). DSO integrates an $\mathbf{x}_r$-loss, which penalizes prediction errors on longer displacement intervals to serve as a generative objective for human listening quality, with an Endpoint SI-SDR loss that directly optimizes terminal signal fidelity. Experiments demonstrate that MeCo achieves state-of-the-art (SOTA) performance with minimal computational overhead, simultaneously achieving superior signal fidelity and human listening quality in both in-domain and out-of-domain scenarios.
匹配关键词: video foundation model
---

[ACADEMIC - ARXIV]
标题: Correlation Is Not Enough: Embedding Human Metadata for Individual Causal Discovery
作者: Suraj Biswas, Saurabh Gupta, Pritam Mukherjee
链接: https://arxiv.org/abs/2606.09672v1
完整摘要: Ask a pretrained biomedical language model whether "cortisol 28 ug/dL" and "stock-market volatility" are related, and it returns a cosine similarity of 0.83 on a scale where 1.0 means identical. The two share no mechanism. This is not a corner case: every off-the-shelf biomedical encoder we tested (BioBERT, PubMedBERT, BioM-ELECTRA) scores unrelated cross-domain pairs between 0.76 and 0.92 when the answer should be near zero. Accuracy on cross-domain discrimination is 0%. Retrieval systems survive this, because a language model downstream filters the noise. A Large Behavioural Model (LBM), a foundation model whose subject is a person rather than a sentence, does not: it reasons over a graph of a user's life and treats embedding proximity as evidence that two events are causally linked. False proximity writes a false causal edge, and everything downstream inherits the error. Here, embedding geometry is not a tuning knob; it is correctness. We report the fix. A contrastive pass over 72,034 pairs raises PubMedBERT BIOSSES correlation from 0.633 to 0.828 and within-vs-across-domain separation from 1.05x to 1.63x. A second pass, BODHI, mines hard negatives from edges absent in a biomedical knowledge graph and lifts separation to 2.30x and the discrimination gap to +0.392, at a 4.5% BIOSSES cost. On an Intel Xeon 6737P with AMX, OpenVINO cuts single-query latency from 1367 ms to 10 ms (133x) and reaches 555 sentences/sec. One finding contradicts standard advice: FP16 beats INT8 on this silicon at every serving batch size, and we explain why. The same model on a no-AMX Ice Lake instance runs 13-27x slower. We release the benchmark suite, training corpora, the BODHI generator, and the OpenVINO scripts.
匹配关键词: video foundation model
---

[ACADEMIC - ARXIV]
标题: Transition-Based Digital Twin Modelling for Alzheimer's Disease under Sparse Longitudinal Data
作者: Yinyu Huang, Yilin Zhang, Sofia Michopoulou, Christopher Kipps, Rahman Attar
链接: https://arxiv.org/abs/2606.09671v1
完整摘要: Alzheimer's disease (AD) progression is highly heterogeneous and is typically observed through sparse and irregular longitudinal data, posing challenges for prediction and personalised monitoring. Existing machine learning approaches have improved AD prediction using multimodal data, yet often focus on static classification or cohort-level risk estimation, providing limited support for subject-specific modelling and uncertainty-aware reasoning. To address these limitations, we present a personalised digital twin framework for AD prediction and scenario-based analysis using multimodal longitudinal data. The proposed approach integrates complementary modelling strategies to capture clinical transitions and temporal dependencies across visits. Using data from the Alzheimer's Disease Neuroimaging Initiative (ADNI), including cognitive assessments, clinical variables, and MRI-derived phenotypes, the framework predicts cognitive status and diagnostic categories while quantifying predictive uncertainty and enabling patient-specific what-if trajectory analysis. Evaluation on leak-free subject-level splits demonstrates strong performance in score forecasting and diagnosis classification. In this sparse and irregular ADNI setting, transition-based modelling of adjacent visits achieved higher predictive accuracy than the sequence-based branch, suggesting that local transition modelling may be more data-efficient. While sequence models remain valuable for uncertainty-aware trajectory forecasting, local transition modelling offers a more data-efficient and robust predictive strategy. These findings highlight the importance of aligning temporal modelling strategies with clinical data structure and suggest that transition-based digital twin formulations may provide a practical and interpretable approach for personalised disease forecasting in neurodegenerative disorders.
匹配关键词: video foundation model
---

[ACADEMIC - ARXIV]
标题: Visual Prompting Meets Feature Reconstruction-Based Anomaly Detection with Dual-Teacher Supervision
作者: Mateo Diaz-Bone, Daniel Caraballo, Florian Scheidegger, Thomas Frick, Mattia Rigotti, Andrea Bartezzaghi, Roy Assaf, Niccolo Avogaro, Yagmur G. Cinar, Brown Ebouky, Filip M. Janicki, Piotr S. Kluska, Cezary Skura, Cristiano Malossi
链接: https://arxiv.org/abs/2606.09670v1
完整摘要: Recent Anomaly Detection methods achieve perfect detection and segmentation scores on well-established datasets, such as MVTec. However, many of these methods face challenges when foundational assumptions - such as consistent object scale, viewpoint, background, illumination, and centered placement - are violated. Those variations that occur render anomaly detection methods unusable in many real-world scenarios. To address these limitations, we introduce three key contributions: (1) a visual prompting pipeline that isolates objects using foreground-background masking; (2) a mechanism for unfreezing the teacher in student-teacher models to improve domain adaptability; and (3) a data augmentation strategy leveraging diffusion-generated synthetic images to enhance anomaly detection performance. We achieve a 3.5 percentage point improvement over the previous state-of-the-art on the challenging AeBAD dataset by using the Masked Multiscale Reconstruction (MMR) model as our backbone.
匹配关键词: video foundation model
---

[ACADEMIC - ARXIV]
标题: (Auto)formalization is supposed to be easy: Trellis process semantics for spelling out rigorous proofs
作者: Wesley Pegden
链接: https://arxiv.org/abs/2606.09674v1
完整摘要: We present Trellis: an autoformalization system that leverages LLM agents in a deterministically constrained workflow to enforce incremental progress in Lean autoformalization tasks through iterative refinement of natural language proofs. Our approach is motivated by the common mathematician's notion of what it means to have a rigorous proof in the first place: namely, that it would be routine to elaborate any part of the proof in further detail. The result is a system which aims to achieve reliable autoformalization on a modest budget and with generalist agents, with specialization to autoformalization coming not from any task-specific agent training but instead from a meaning-of-rigor inspired workflow enforced by process semantics. We link to an end-to-end Lean formalization of a recent Ramsey theory breakthrough produced by the process.
匹配关键词: video LLM
---

[ACADEMIC - ARXIV]
标题: Cross-Modal Masking for Robust Silent Speech Synthesis Using sEMG and Lipreading
作者: Eder del Blanco, David Gimeno-Gómez, Eva Navas, Carlos-D. Martínez-Hinarejos, Inma Hernáez
链接: https://arxiv.org/abs/2606.09667v1
完整摘要: Speech restoration through silent speech interfaces (SSIs) has emerged as a promising assistive technology for individuals with impaired or absent laryngeal voice production. Among non-invasive SSI modalities, surface electromyography (sEMG) and video-based lipreading provide complementary articulatory information, yet their integration for continuous speech synthesis remains underexplored. Moreover, existing multimodal approaches rarely address robustness to modality degradation or temporary sensor failure, limiting their applicability in realistic scenarios. In this work, we propose a masked multimodal speech synthesis framework that jointly leverages sEMG and lipreading signals through modality masking during training. Under multispeaker settings, the proposed approach reduces word error rate by up to 14 absolute percentage points compared to the strongest unimodal baseline. Experimental results not only show that masking strategies are critical for these performance gains and robustness under low-bitrate conditions, but also that they generalize better than degradation-specific data augmentations in the presence of modality absence conditions. Phone-level analyses further reveal complementary contributions across modalities, with particularly strong benefits for vowels and for specific consonant groups. Overall, these findings demonstrate the effectiveness and robustness of masked multimodal integration for silent speech synthesis, although adaptation to laryngectomized speakers remains an open research challenge.
匹配关键词: video LLM
---

[ACADEMIC - ARXIV]
标题: Muon Learns More Robust and Transferable Features than Adam
作者: Tianyu Ruan, Fengzhuo Zhang, Shuche Wang, Shihua Zhang
链接: https://arxiv.org/abs/2606.09658v1
完整摘要: Muon has recently emerged as a state-of-the-art optimizer for pretraining Large Language Models (LLMs) and vision classifiers. Despite its efficiency advantage over Adam and SGD, the feature-learning advantage of Muon remains unclear. This paper investigates Muon's feature-learning advantage through the lens of robustness and transferability. First, by evaluating pretrained models on corrupted images and texts, we show that features learned by Muon are consistently more robust than those learned by Adam and SGD across different architectures, including transformers and Convolutional Neural Networks (CNNs). Using trained layer-wise probes, we further show that this robustness advantage is reflected in larger logit margins across layers. Second, by training linear classifiers or fine-tuning full models from pretrained parameters on downstream tasks, we demonstrate that Muon-learned features transfer more effectively than those learned by Adam and SGD. This transferability advantage is further supported by the diversity of hidden states across layers, as measured by effective rank. Finally, in a representative classification problem with multi-component features, we prove that Muon attains larger margins and higher effective rank than Adam and SGD, providing theoretical support for our empirical findings.
匹配关键词: video LLM
---

[ACADEMIC - ARXIV]
标题: Do Video Foundation Models Understand Intuitive Physics? A Layerwise Probing Analysis
作者: Samuele Punzo, Niccolò Caselli, Ippokratis Pantelidis, Francesco Massafra, Salvatore Lo Sardo, Mohammadreza Salehi
链接: https://arxiv.org/abs/2606.09646v1
完整摘要: We study whether pretrained video foundation models encode intuitive-physics information in their frozen representations, and how this information varies across model families, layers, and probe types. Using frozen-feature probing on IntPhys2 and Minimal Video Pairs (MVP), we compare predictive joint-embedding models (V-JEPA), masked reconstruction models (VideoMAE), and a diffusion-based video generator (LTX-Video). V-JEPA achieves the strongest overall results across benchmarks, especially with probes that model temporal dynamics, while VideoMAE remains competitive and LTX-Video recovers weaker but non-trivial signal. Layerwise analyses show that physics-relevant information is weakest in early layers and becomes most accessible at intermediate-to-late depth, and temporal controls show that disrupting frame order substantially reduces performance, especially on MVP. Together, these results suggest that intuitive-physics knowledge emerges reliably in pretrained video representations, but its accessibility depends strongly on pretraining paradigm, representational depth, and readout mechanism.
匹配关键词: video LLM
---

[ACADEMIC - ARXIV]
标题: Where Does the Answer Come From? Benchmarking View-Level Visual Evidence Identification in Multi-View MLLMs for Autonomous Driving
作者: Yimu Wang, Yee Man Choi, Barry Zhang, Mozhgan Nasr Azadani, Sean Sedwards, Krzysztof Czarnecki
链接: https://arxiv.org/abs/2606.09644v1
完整摘要: Multimodal large language models (MLLMs) achieve strong results on visual reasoning benchmarks, but answer accuracy alone does not indicate whether a model relied on the correct visual evidence. This gap is particularly important in multi-view driving scenes used for autonomous driving, where a model can produce a plausible answer while grounding it in the wrong camera view. We introduce a multi-view visual question answering benchmark for evaluating evidence-source identification: given six synchronized NuScenes views and a question, the model must identify the supporting camera view and answer the question. The benchmark contains 122 conflict-centric question-answer pairs from 73 scenes, spanning causality, counterfactual reasoning, and intent prediction. View labels are proposed by an automatic conflict-mining pipeline and manually verified by annotators. We evaluate three settings: camera-view selection, oracle QA given the golden view, and joint prediction in which the model selects a view and answers in one pass. Answers are evaluated in both multiple-choice and free-form formats, using exact match for structured predictions and an LLM judge for free-form responses. By explicitly separating visual-source identification from answer correctness, the benchmark exposes grounding failures that answer-only evaluation misses.
匹配关键词: video LLM
---

[ACADEMIC - ARXIV]
标题: MAVIS: Multi-Agent Video Retrieval via Structured Video Understanding
作者: Jie Zhang, Qilang Ye, Hao Zhou, Haochen Liang, Fei Luo
链接: https://arxiv.org/abs/2606.09641v1
完整摘要: The dominant paradigm in video retrieval relies on embedding-based full-corpus scanning, which suffers from inherent computational inefficiency and the semantic asymmetry between information-dense videos and sparse textual queries. To bridge this gap, we introduce \textbf{MAVIS}, a novel multi-agent framework that rethinks retrieval as cooperative reasoning rather than brute-force search. MAVIS first bridges the granularity mismatch by parsing raw videos into a \textbf{Structured Semantic Library}, enabling explicit attribute-level indexing. During retrieval, a planner decomposes complex user intents into atomic sub-tasks, dispatching specialized agents to independently nominate candidates. Crucially, MAVIS employs a \textbf{Logic-aware Debate} mechanism with a strict veto protocol, where agents collaboratively prune logical mismatches to identify a compact set of ``controversial'' candidates for fine-grained verification. This agentic workflow effectively bypasses the inefficiency of full-library traversal. Extensive experiments on MSR-VTT, MSVD, and ActivityNet demonstrate that MAVIS achieves competitive performance without task-specific fine-tuning, offering a scalable and interpretable alternative to traditional dual-encoder approaches.
匹配关键词: multi-agent
---

[ACADEMIC - ARXIV]
标题: Civil Court Simulation with Large Language Models
作者: Yifan Chen, Haitao Li, Kaiyuan Zhang, Yueyue Wu, Qingyao Ai, Yiqun Liu
链接: https://arxiv.org/abs/2606.09632v1
完整摘要: Court simulation bridges legal education and judicial practice, yet human-based simulations are costly and difficult to scale. Large language models (LLMs) offer a scalable alternative, but existing court-simulation research mainly focuses on criminal cases. Civil litigation is more common in practice and harder to simulate because its claims, liability, and remedies are more flexible. We present a multi-agent court simulation framework for Chinese civil cases. The framework organizes role-based interaction through a five-stage civil trial procedure and integrates memory module and statute retrieval to support long-process adjudication. Experiments show that the framework produces reliable civil judgments, with clear strengths in liability allocation and multi-item adjudication. Further experiments show that memory quality substantially affects downstream simulation quality. Through a five-layer factor framework, we analyze how legal grounding, information conditions, judicial capability and role orientation, organizational pressure, and social context affect the framework's reliability and behavior. These results support the effectiveness of the proposed framework for civil court simulation. The dataset and code are available at: https://github.com/foggpoy/Civil-Court.
匹配关键词: multi-agent
---

[ACADEMIC - ARXIV]
标题: AGENTSERVESIM: A Hardware-aware Simulator for Multi-Turn LLM Agent Serving
作者: Rakibul Hasan Rajib, Mengxin Zheng, Qian Lou
链接: https://arxiv.org/abs/2606.09613v1
完整摘要: Multi-turn LLM agents interleave model calls with external tool invocations, shifting serving from stateless request processing to stateful program execution. Serving these workloads requires scheduling, KV-cache management, and routing policies that use program-level context, including turn dependencies, tool-induced gaps, and reusable KV state. Evaluating such policies directly on real systems is costly, since each design point may require dedicated accelerator time across arrival rates, model scales, serving-instance counts, and memory hierarchies. Simulation offers a scalable alternative, but existing LLM serving simulators target stateless request-level workloads and therefore omit the core dynamics of agent serving: multi-turn program execution, cross-turn cache locality, and KV-cache residency during tool gaps. We present AGENTSERVESIM, a hardware-aware simulator for multi-turn LLM agent serving. AGENTSERVESIM evaluates serving policies at program granularity through composable modules: a Program Orchestrator preserves program identity and turn order, a Tool Simulator materializes tool-induced gaps, a Session-Aware Router maintains program-to-instance affinity for cache-aware dispatch, and a KV Residency Model tracks policy-defined KV placement across HBM, host DRAM/CXL, and eviction. Across real serving deployments and hardware configurations, AGENTSERVESIM reproduces real-system behavior within 6% error across key performance metrics while running entirely on commodity CPUs. These results show that AGENTSERVESIM enables controlled, repeatable exploration of agent-serving policies without requiring exhaustive deployment on costly accelerators.
匹配关键词: multi-agent
---

[ACADEMIC - ARXIV]
标题: Shape Formation for the Cooperative Transportation of Arbitrary Objects Using Multi-Agent Reinforcement Learning
作者: Mohamed Sayed, Wolfram Burgard, Tanja Katharina Kaiser
链接: https://arxiv.org/abs/2606.09610v1
完整摘要: Cooperative object transportation is essential in numerous domains, including industrial to domestic services. A popular transportation strategy is to carry objects on top of multi-robot systems. The corresponding task is typically solved by decomposing it into three interconnected subproblems: formation control, cooperative navigation, and collision avoidance. A particular challenge posed by real-world objects is their potentially arbitrary shape and non-uniform mass distribution, necessitating robot formations that securely support the object. In this work, we address the challenge of pattern formation control for transporting such real-world objects by proposing a novel multi-agent reinforcement learning approach. Our approach enables a multi-robot system to autonomously position itself underneath an object to support its weight while avoiding obstacles during the formation process. Our evaluations with diverse environments and varying numbers of robots show that our approach leads to policies that reliably produce balanced formations and generalize to cluttered scenes and objects with complex geometry and non-uniform mass distribution.
匹配关键词: multi-agent
---

[ACADEMIC - ARXIV]
标题: Code Is More Than Text: Uncertainty Estimation for Code Generation
作者: Yuling Shi, Caiqi Zhang, Yuexian Li, Haopeng Wang, Yeheng Chen, Nigel Collier, Xiaodong Gu
链接: https://arxiv.org/abs/2606.09577v1
完整摘要: Large language models (LLMs) are increasingly deployed as code generators, where silently wrong programs pose real safety and reliability risks. Reliable uncertainty estimation (UE) is essential for selective prediction, human-in-the-loop review, and downstream agentic decisions. Yet most existing code UE methods are inherited from natural language (NL) generation and ignore properties that make code distinct. We argue that code differs from NL in three ways: a single wrong token can break an entire program (token fragility); algorithmic intent and concrete implementation can disagree independently (intent-code gap); and programs can be executed (executability). We instantiate these properties as three orthogonal uncertainty axes: lexical (Top-K token entropy), algorithmic (pseudo-code consistency), and functional (behavioral consistency). Across five code LLMs, our three-axis ensemble improves average AUROC from 0.696 for the strongest NL-derived baseline to 0.776 (+8.1 points). Notably, on Qwen3-14B, our single-pass Top-K token entropy matches the strongest multi-pass baseline while being over 3x cheaper; across models, it remains a competitive low-cost signal. These results suggest that code UE deserves code-specific design rather than direct NL ports.
匹配关键词: multi-agent
---

[ACADEMIC - ARXIV]
标题: (Auto)formalization is supposed to be easy: Trellis process semantics for spelling out rigorous proofs
作者: Wesley Pegden
链接: https://arxiv.org/abs/2606.09674v1
完整摘要: We present Trellis: an autoformalization system that leverages LLM agents in a deterministically constrained workflow to enforce incremental progress in Lean autoformalization tasks through iterative refinement of natural language proofs. Our approach is motivated by the common mathematician's notion of what it means to have a rigorous proof in the first place: namely, that it would be routine to elaborate any part of the proof in further detail. The result is a system which aims to achieve reliable autoformalization on a modest budget and with generalist agents, with specialization to autoformalization coming not from any task-specific agent training but instead from a meaning-of-rigor inspired workflow enforced by process semantics. We link to an end-to-end Lean formalization of a recent Ramsey theory breakthrough produced by the process.
匹配关键词: agent collaboration
---

[ACADEMIC - ARXIV]
标题: SpatialWorld: Benchmarking Interactive Spatial Reasoning of Multimodal Agents in Real-World Tasks
作者: Hongcheng Gao, Hailong Qu, Jingyi Tang, Jiahao Wang, Zihao Huang, Hengkang Qiao, Shihong Huang, Junming Yang, Yi Li, Hongyixuan Yuan, Wenjie Li, Bohan Zeng, Wenbo Li, Bo Wang, Jianhui Liu, Olive Huang, Haoyang Huang, Wentao Zhang, Guoqing Huang, Nan Duan, Yinpeng Dong
链接: https://arxiv.org/abs/2606.09669v1
完整摘要: Spatial reasoning is a foundational capability for multimodal large language models (MLLMs) to perceive and operate within the physical world. However, existing benchmarks predominantly rely on passive evaluation (e.g., static VQA) or simulator-specific pipelines, failing to assess general interactive spatial understanding. We introduce SpatialWorld, a unified benchmark designed specifically for evaluating the interactive spatial understanding of multimodal agents in complex real-world tasks. Integrating eight heterogeneous simulation backends under a shared, simulator-agnostic protocol, SpatialWorld features 760 human-annotated tasks across diverse domains (e.g., household routines, travel, social collaboration). Agents must solve tasks under vision-only partial observability, actively gathering egocentric visual evidence and expressing decisions via a unified, text-based action interface native to MLLMs. For reliable evaluation, each task includes a human-validated initial state, a reference trajectory, and a terminal-state verifier. Evaluating 15 advanced agents reveals that robust spatial task solving remains challenging: the strongest model, GPT-5, achieves an average task success rate (TSR) of only 17.4%, while the leading open-source model, Qwen-3.5, reaches 14.1%. Further analysis exposes a clear mismatch between task success and execution efficiency, alongside substantial domain-specific performance variations. These bottlenecks in active exploration and long-horizon planning position SpatialWorld as a rigorous testbed for future spatial agents.
匹配关键词: agent collaboration
---

[ACADEMIC - ARXIV]
标题: From 0-to-1 to 1-to-N: Reproducible Engineering Evidence for MetaAI Recursive Self-Design
作者: Dun Li, Jiatao Li, Hongzhi Li
链接: https://arxiv.org/abs/2606.09663v1
完整摘要: Recursive self-design refers to AI-assisted modification of the mechanisms by which an AI system is built, evaluated, and improved. This paper treats MetaAI not as a mature paradigm, but as a working term for a human-seeded, AI-expanded development pattern in which the design space itself becomes a target of modification. We propose an operational evidence framework with four criteria: inspectable target system, meta-level modifier, feedback-directed selection, and recursive continuation. We then map public systems, including Darwin Goedel Machine (DGM), STOP, Goedel Agent, and ShinkaEvolve, against these criteria. DGM provides the most direct currently reported evidence: its published results show improvement from 20% to 50% on SWE-bench Verified and from 14.2% to 30.7% on full Polyglot after 80 iterations, with ablations suggesting that both open-ended exploration and self-improvement contribute. Finally, we provide MetaAI-Mini, a reproducible HumanEval-based protocol and codebase. Because no completed model run is included in this build, MetaAI-Mini is reported as a protocol rather than as an experimental result.
匹配关键词: agent collaboration
---

[ACADEMIC - ARXIV]
标题: End-to-End Context Compression at Scale
作者: Ang Li, Sean McLeish, Haozhe Chen, Nimit Kalra, Zaiqian Chen, Artem Gazizov, Venkata Anoop Suhas Kumar Morisetty, Bhavya Kailkhura, Harshitha Menon, Zhuang Liu, Brian R. Bartoldson, Tom Goldstein, Sanae Lotfi, Micah Goldblum, Pavel Izmailov
链接: https://arxiv.org/abs/2606.09659v1
完整摘要: Long-context language model inference is bottlenecked by memory, as the KV cache grows with context length. Recent techniques to compress the KV cache fall short: they either degrade model quality substantially or require considerable time and compute to compress a single long prompt. Furthermore, many methods require the input to fit within the target model's context window, and are generally incompatible with modern production inference engines. Encoder-decoder compressors, which map a long token sequence to a shorter sequence of latent embeddings consumed by a decoder, are an appealing alternative in principle. However, existing approaches are not competitive with KV cache compression on the accuracy-efficiency frontier. In this work, we revisit encoder-decoder compression and close this gap. We first perform an architecture search, pre-training many variants from scratch to determine how best to design and train encoder-decoder compressors. Guided by our findings, we continually pre-train a family of 0.6B-encoder, 4B-decoder models on over 350B tokens each, at compression ratios of 1:4, 1:8, and 1:16. We introduce Latent Context Language Models (LCLMs), a family of compressors that improve the Pareto frontier across general-task performance, compression speed, and peak memory usage. We demonstrate that LCLMs serve as efficient backbones for long-horizon agents, letting the agent skim through a compressed long context and adaptively expand relevant segments on demand.
匹配关键词: agent collaboration
---

[ACADEMIC - ARXIV]
标题: Modeling Components and Connections in Cyber-Physical Systems
作者: Kate Sanborn, Tanuj Kenchannavar, Vakul Nath, Jonathan Sprinkle
链接: https://arxiv.org/abs/2606.09645v1
完整摘要: Text based configuration files for cyber-physical systems show the hierarchy of component modules well but often hide the details of connections and interfaces between modules. A model-based visual approach to these configuration files can better capture this information. The XML structure of Robot Operating System (ROS) launch files can be improved using a modeling approach. This paper presents ROSLaunchVisual, a model-integrated environment built on WebGME for designing, visualizing, and managing ROS launch files. The tool raises the level of abstraction by allowing developers to create and modify launch files using a graphical interface that represents nodes, publishers, subscribers, and arguments as interconnected components. The tool provides a dynamic system analysis that can then be used in the static development and analysis of new and existing launch files. ROSLaunchVisual incorporates features such as metamodel-driven validation, automatic import/export of launch files, and visual communication mapping. Plugins further enhance functionality by updating libraries, checking for semantic errors, and managing remaps. By making launch file creation more intuitive and less error-prone, ROSLaunchVisual improves development efficiency and system understanding, especially in collaborative or large-scale robotics projects.
匹配关键词: agent collaboration
---

[ACADEMIC - ARXIV]
标题: (Auto)formalization is supposed to be easy: Trellis process semantics for spelling out rigorous proofs
作者: Wesley Pegden
链接: https://arxiv.org/abs/2606.09674v1
完整摘要: We present Trellis: an autoformalization system that leverages LLM agents in a deterministically constrained workflow to enforce incremental progress in Lean autoformalization tasks through iterative refinement of natural language proofs. Our approach is motivated by the common mathematician's notion of what it means to have a rigorous proof in the first place: namely, that it would be routine to elaborate any part of the proof in further detail. The result is a system which aims to achieve reliable autoformalization on a modest budget and with generalist agents, with specialization to autoformalization coming not from any task-specific agent training but instead from a meaning-of-rigor inspired workflow enforced by process semantics. We link to an end-to-end Lean formalization of a recent Ramsey theory breakthrough produced by the process.
匹配关键词: agent coordination
---

[ACADEMIC - ARXIV]
标题: SpatialWorld: Benchmarking Interactive Spatial Reasoning of Multimodal Agents in Real-World Tasks
作者: Hongcheng Gao, Hailong Qu, Jingyi Tang, Jiahao Wang, Zihao Huang, Hengkang Qiao, Shihong Huang, Junming Yang, Yi Li, Hongyixuan Yuan, Wenjie Li, Bohan Zeng, Wenbo Li, Bo Wang, Jianhui Liu, Olive Huang, Haoyang Huang, Wentao Zhang, Guoqing Huang, Nan Duan, Yinpeng Dong
链接: https://arxiv.org/abs/2606.09669v1
完整摘要: Spatial reasoning is a foundational capability for multimodal large language models (MLLMs) to perceive and operate within the physical world. However, existing benchmarks predominantly rely on passive evaluation (e.g., static VQA) or simulator-specific pipelines, failing to assess general interactive spatial understanding. We introduce SpatialWorld, a unified benchmark designed specifically for evaluating the interactive spatial understanding of multimodal agents in complex real-world tasks. Integrating eight heterogeneous simulation backends under a shared, simulator-agnostic protocol, SpatialWorld features 760 human-annotated tasks across diverse domains (e.g., household routines, travel, social collaboration). Agents must solve tasks under vision-only partial observability, actively gathering egocentric visual evidence and expressing decisions via a unified, text-based action interface native to MLLMs. For reliable evaluation, each task includes a human-validated initial state, a reference trajectory, and a terminal-state verifier. Evaluating 15 advanced agents reveals that robust spatial task solving remains challenging: the strongest model, GPT-5, achieves an average task success rate (TSR) of only 17.4%, while the leading open-source model, Qwen-3.5, reaches 14.1%. Further analysis exposes a clear mismatch between task success and execution efficiency, alongside substantial domain-specific performance variations. These bottlenecks in active exploration and long-horizon planning position SpatialWorld as a rigorous testbed for future spatial agents.
匹配关键词: agent coordination
---

[ACADEMIC - ARXIV]
标题: From 0-to-1 to 1-to-N: Reproducible Engineering Evidence for MetaAI Recursive Self-Design
作者: Dun Li, Jiatao Li, Hongzhi Li
链接: https://arxiv.org/abs/2606.09663v1
完整摘要: Recursive self-design refers to AI-assisted modification of the mechanisms by which an AI system is built, evaluated, and improved. This paper treats MetaAI not as a mature paradigm, but as a working term for a human-seeded, AI-expanded development pattern in which the design space itself becomes a target of modification. We propose an operational evidence framework with four criteria: inspectable target system, meta-level modifier, feedback-directed selection, and recursive continuation. We then map public systems, including Darwin Goedel Machine (DGM), STOP, Goedel Agent, and ShinkaEvolve, against these criteria. DGM provides the most direct currently reported evidence: its published results show improvement from 20% to 50% on SWE-bench Verified and from 14.2% to 30.7% on full Polyglot after 80 iterations, with ablations suggesting that both open-ended exploration and self-improvement contribute. Finally, we provide MetaAI-Mini, a reproducible HumanEval-based protocol and codebase. Because no completed model run is included in this build, MetaAI-Mini is reported as a protocol rather than as an experimental result.
匹配关键词: agent coordination
---

[ACADEMIC - ARXIV]
标题: When Built-in Thinking Helps and Hurts: Constraint-Level Error Shifts in Instruction Following
作者: Sai Adith Senthil Kumar
链接: https://arxiv.org/abs/2606.09662v1
完整摘要: Large reasoning models (LRMs) often improve math and coding performance, but their effect on instruction following is unclear. We study IFEval with Qwen3 models (1.7B-32B), using same-weights Thinking ON/OFF controls; four Hunyuan models provide directional cross-family support. Aggregate pass-rate changes are small (-0.55 to -3.52 pp), yet 10-20% of prompts switch between pass and fail across modes, suggesting that thinking changes the pattern of errors--some prompts improve while others worsen--rather than uniformly degrading performance. Under a post-hoc Qwen3-derived grouping, constraint types separate into Planning (global counting, structure, coordination), which improves at the class level under thinking, and Precision (exact local form), which consistently worsens; the class-level Planning/Precision sign pattern holds directionally for all four Hunyuan models despite Hunyuan's opposite aggregate direction. Thinking also changes final-answer length; matched-length analyses substantially reduce the Precision drop, but a residual penalty remains. Analyzing thinking traces with a cross-encoder relevance metric reveals three patterns: Neutral shows a positive relevance-compliance link (r approximately 0.15); Planning shows near-zero predictive correlation (r approximately 0.02) despite measurable trace engagement, consistent with an execution gap between CE-measured trace relevance and final-answer compliance; Precision shows a small negative correlation (r approximately -0.05), with failing instances having higher mean relevance than passing ones. Activation patching across four model sizes (1.7B-14B) shows that Precision flip instances are more often restored than Planning flip instances (32-58% vs. 14-40% mean layer-restoration), with the largest gap at 14B (about 30 pp).
匹配关键词: agent coordination
---

[ACADEMIC - ARXIV]
标题: End-to-End Context Compression at Scale
作者: Ang Li, Sean McLeish, Haozhe Chen, Nimit Kalra, Zaiqian Chen, Artem Gazizov, Venkata Anoop Suhas Kumar Morisetty, Bhavya Kailkhura, Harshitha Menon, Zhuang Liu, Brian R. Bartoldson, Tom Goldstein, Sanae Lotfi, Micah Goldblum, Pavel Izmailov
链接: https://arxiv.org/abs/2606.09659v1
完整摘要: Long-context language model inference is bottlenecked by memory, as the KV cache grows with context length. Recent techniques to compress the KV cache fall short: they either degrade model quality substantially or require considerable time and compute to compress a single long prompt. Furthermore, many methods require the input to fit within the target model's context window, and are generally incompatible with modern production inference engines. Encoder-decoder compressors, which map a long token sequence to a shorter sequence of latent embeddings consumed by a decoder, are an appealing alternative in principle. However, existing approaches are not competitive with KV cache compression on the accuracy-efficiency frontier. In this work, we revisit encoder-decoder compression and close this gap. We first perform an architecture search, pre-training many variants from scratch to determine how best to design and train encoder-decoder compressors. Guided by our findings, we continually pre-train a family of 0.6B-encoder, 4B-decoder models on over 350B tokens each, at compression ratios of 1:4, 1:8, and 1:16. We introduce Latent Context Language Models (LCLMs), a family of compressors that improve the Pareto frontier across general-task performance, compression speed, and peak memory usage. We demonstrate that LCLMs serve as efficient backbones for long-horizon agents, letting the agent skim through a compressed long context and adaptively expand relevant segments on demand.
匹配关键词: agent coordination
---

[ACADEMIC - ARXIV]
标题: (Auto)formalization is supposed to be easy: Trellis process semantics for spelling out rigorous proofs
作者: Wesley Pegden
链接: https://arxiv.org/abs/2606.09674v1
完整摘要: We present Trellis: an autoformalization system that leverages LLM agents in a deterministically constrained workflow to enforce incremental progress in Lean autoformalization tasks through iterative refinement of natural language proofs. Our approach is motivated by the common mathematician's notion of what it means to have a rigorous proof in the first place: namely, that it would be routine to elaborate any part of the proof in further detail. The result is a system which aims to achieve reliable autoformalization on a modest budget and with generalist agents, with specialization to autoformalization coming not from any task-specific agent training but instead from a meaning-of-rigor inspired workflow enforced by process semantics. We link to an end-to-end Lean formalization of a recent Ramsey theory breakthrough produced by the process.
匹配关键词: decentralized agent
---

[ACADEMIC - ARXIV]
标题: SpatialWorld: Benchmarking Interactive Spatial Reasoning of Multimodal Agents in Real-World Tasks
作者: Hongcheng Gao, Hailong Qu, Jingyi Tang, Jiahao Wang, Zihao Huang, Hengkang Qiao, Shihong Huang, Junming Yang, Yi Li, Hongyixuan Yuan, Wenjie Li, Bohan Zeng, Wenbo Li, Bo Wang, Jianhui Liu, Olive Huang, Haoyang Huang, Wentao Zhang, Guoqing Huang, Nan Duan, Yinpeng Dong
链接: https://arxiv.org/abs/2606.09669v1
完整摘要: Spatial reasoning is a foundational capability for multimodal large language models (MLLMs) to perceive and operate within the physical world. However, existing benchmarks predominantly rely on passive evaluation (e.g., static VQA) or simulator-specific pipelines, failing to assess general interactive spatial understanding. We introduce SpatialWorld, a unified benchmark designed specifically for evaluating the interactive spatial understanding of multimodal agents in complex real-world tasks. Integrating eight heterogeneous simulation backends under a shared, simulator-agnostic protocol, SpatialWorld features 760 human-annotated tasks across diverse domains (e.g., household routines, travel, social collaboration). Agents must solve tasks under vision-only partial observability, actively gathering egocentric visual evidence and expressing decisions via a unified, text-based action interface native to MLLMs. For reliable evaluation, each task includes a human-validated initial state, a reference trajectory, and a terminal-state verifier. Evaluating 15 advanced agents reveals that robust spatial task solving remains challenging: the strongest model, GPT-5, achieves an average task success rate (TSR) of only 17.4%, while the leading open-source model, Qwen-3.5, reaches 14.1%. Further analysis exposes a clear mismatch between task success and execution efficiency, alongside substantial domain-specific performance variations. These bottlenecks in active exploration and long-horizon planning position SpatialWorld as a rigorous testbed for future spatial agents.
匹配关键词: decentralized agent
---

[ACADEMIC - ARXIV]
标题: From 0-to-1 to 1-to-N: Reproducible Engineering Evidence for MetaAI Recursive Self-Design
作者: Dun Li, Jiatao Li, Hongzhi Li
链接: https://arxiv.org/abs/2606.09663v1
完整摘要: Recursive self-design refers to AI-assisted modification of the mechanisms by which an AI system is built, evaluated, and improved. This paper treats MetaAI not as a mature paradigm, but as a working term for a human-seeded, AI-expanded development pattern in which the design space itself becomes a target of modification. We propose an operational evidence framework with four criteria: inspectable target system, meta-level modifier, feedback-directed selection, and recursive continuation. We then map public systems, including Darwin Goedel Machine (DGM), STOP, Goedel Agent, and ShinkaEvolve, against these criteria. DGM provides the most direct currently reported evidence: its published results show improvement from 20% to 50% on SWE-bench Verified and from 14.2% to 30.7% on full Polyglot after 80 iterations, with ablations suggesting that both open-ended exploration and self-improvement contribute. Finally, we provide MetaAI-Mini, a reproducible HumanEval-based protocol and codebase. Because no completed model run is included in this build, MetaAI-Mini is reported as a protocol rather than as an experimental result.
匹配关键词: decentralized agent
---

[ACADEMIC - ARXIV]
标题: End-to-End Context Compression at Scale
作者: Ang Li, Sean McLeish, Haozhe Chen, Nimit Kalra, Zaiqian Chen, Artem Gazizov, Venkata Anoop Suhas Kumar Morisetty, Bhavya Kailkhura, Harshitha Menon, Zhuang Liu, Brian R. Bartoldson, Tom Goldstein, Sanae Lotfi, Micah Goldblum, Pavel Izmailov
链接: https://arxiv.org/abs/2606.09659v1
完整摘要: Long-context language model inference is bottlenecked by memory, as the KV cache grows with context length. Recent techniques to compress the KV cache fall short: they either degrade model quality substantially or require considerable time and compute to compress a single long prompt. Furthermore, many methods require the input to fit within the target model's context window, and are generally incompatible with modern production inference engines. Encoder-decoder compressors, which map a long token sequence to a shorter sequence of latent embeddings consumed by a decoder, are an appealing alternative in principle. However, existing approaches are not competitive with KV cache compression on the accuracy-efficiency frontier. In this work, we revisit encoder-decoder compression and close this gap. We first perform an architecture search, pre-training many variants from scratch to determine how best to design and train encoder-decoder compressors. Guided by our findings, we continually pre-train a family of 0.6B-encoder, 4B-decoder models on over 350B tokens each, at compression ratios of 1:4, 1:8, and 1:16. We introduce Latent Context Language Models (LCLMs), a family of compressors that improve the Pareto frontier across general-task performance, compression speed, and peak memory usage. We demonstrate that LCLMs serve as efficient backbones for long-horizon agents, letting the agent skim through a compressed long context and adaptively expand relevant segments on demand.
匹配关键词: decentralized agent
---

[ACADEMIC - ARXIV]
标题: MAVIS: Multi-Agent Video Retrieval via Structured Video Understanding
作者: Jie Zhang, Qilang Ye, Hao Zhou, Haochen Liang, Fei Luo
链接: https://arxiv.org/abs/2606.09641v1
完整摘要: The dominant paradigm in video retrieval relies on embedding-based full-corpus scanning, which suffers from inherent computational inefficiency and the semantic asymmetry between information-dense videos and sparse textual queries. To bridge this gap, we introduce \textbf{MAVIS}, a novel multi-agent framework that rethinks retrieval as cooperative reasoning rather than brute-force search. MAVIS first bridges the granularity mismatch by parsing raw videos into a \textbf{Structured Semantic Library}, enabling explicit attribute-level indexing. During retrieval, a planner decomposes complex user intents into atomic sub-tasks, dispatching specialized agents to independently nominate candidates. Crucially, MAVIS employs a \textbf{Logic-aware Debate} mechanism with a strict veto protocol, where agents collaboratively prune logical mismatches to identify a compact set of ``controversial'' candidates for fine-grained verification. This agentic workflow effectively bypasses the inefficiency of full-library traversal. Extensive experiments on MSR-VTT, MSVD, and ActivityNet demonstrate that MAVIS achieves competitive performance without task-specific fine-tuning, offering a scalable and interpretable alternative to traditional dual-encoder approaches.
匹配关键词: decentralized agent
---

[ACADEMIC - ARXIV]
标题: MeCo: One-Step MeanFlow-based Corrector for Multi-Channel Speech Separation
作者: Dohwan Kim, Jung-Woo Choi
链接: https://arxiv.org/abs/2606.09677v1
完整摘要: While discriminative models for multi-channel speech separation excel in reference-based metrics, they often exhibit suboptimal human listening quality. To address this, we propose a novel MeanFlow-based one-step generative corrector (MeCo). MeCo learns a conditional average velocity field to map discriminative estimates directly onto the clean speech manifold in a single step. To maximize one-step generation performance, we introduce Data-Space Optimization (DSO). DSO integrates an $\mathbf{x}_r$-loss, which penalizes prediction errors on longer displacement intervals to serve as a generative objective for human listening quality, with an Endpoint SI-SDR loss that directly optimizes terminal signal fidelity. Experiments demonstrate that MeCo achieves state-of-the-art (SOTA) performance with minimal computational overhead, simultaneously achieving superior signal fidelity and human listening quality in both in-domain and out-of-domain scenarios.
匹配关键词: swarm intelligence
---

[ACADEMIC - ARXIV]
标题: (Auto)formalization is supposed to be easy: Trellis process semantics for spelling out rigorous proofs
作者: Wesley Pegden
链接: https://arxiv.org/abs/2606.09674v1
完整摘要: We present Trellis: an autoformalization system that leverages LLM agents in a deterministically constrained workflow to enforce incremental progress in Lean autoformalization tasks through iterative refinement of natural language proofs. Our approach is motivated by the common mathematician's notion of what it means to have a rigorous proof in the first place: namely, that it would be routine to elaborate any part of the proof in further detail. The result is a system which aims to achieve reliable autoformalization on a modest budget and with generalist agents, with specialization to autoformalization coming not from any task-specific agent training but instead from a meaning-of-rigor inspired workflow enforced by process semantics. We link to an end-to-end Lean formalization of a recent Ramsey theory breakthrough produced by the process.
匹配关键词: swarm intelligence
---

[ACADEMIC - ARXIV]
标题: Correlation Is Not Enough: Embedding Human Metadata for Individual Causal Discovery
作者: Suraj Biswas, Saurabh Gupta, Pritam Mukherjee
链接: https://arxiv.org/abs/2606.09672v1
完整摘要: Ask a pretrained biomedical language model whether "cortisol 28 ug/dL" and "stock-market volatility" are related, and it returns a cosine similarity of 0.83 on a scale where 1.0 means identical. The two share no mechanism. This is not a corner case: every off-the-shelf biomedical encoder we tested (BioBERT, PubMedBERT, BioM-ELECTRA) scores unrelated cross-domain pairs between 0.76 and 0.92 when the answer should be near zero. Accuracy on cross-domain discrimination is 0%. Retrieval systems survive this, because a language model downstream filters the noise. A Large Behavioural Model (LBM), a foundation model whose subject is a person rather than a sentence, does not: it reasons over a graph of a user's life and treats embedding proximity as evidence that two events are causally linked. False proximity writes a false causal edge, and everything downstream inherits the error. Here, embedding geometry is not a tuning knob; it is correctness. We report the fix. A contrastive pass over 72,034 pairs raises PubMedBERT BIOSSES correlation from 0.633 to 0.828 and within-vs-across-domain separation from 1.05x to 1.63x. A second pass, BODHI, mines hard negatives from edges absent in a biomedical knowledge graph and lifts separation to 2.30x and the discrimination gap to +0.392, at a 4.5% BIOSSES cost. On an Intel Xeon 6737P with AMX, OpenVINO cuts single-query latency from 1367 ms to 10 ms (133x) and reaches 555 sentences/sec. One finding contradicts standard advice: FP16 beats INT8 on this silicon at every serving batch size, and we explain why. The same model on a no-AMX Ice Lake instance runs 13-27x slower. We release the benchmark suite, training corpora, the BODHI generator, and the OpenVINO scripts.
匹配关键词: swarm intelligence
---

[ACADEMIC - ARXIV]
标题: Transition-Based Digital Twin Modelling for Alzheimer's Disease under Sparse Longitudinal Data
作者: Yinyu Huang, Yilin Zhang, Sofia Michopoulou, Christopher Kipps, Rahman Attar
链接: https://arxiv.org/abs/2606.09671v1
完整摘要: Alzheimer's disease (AD) progression is highly heterogeneous and is typically observed through sparse and irregular longitudinal data, posing challenges for prediction and personalised monitoring. Existing machine learning approaches have improved AD prediction using multimodal data, yet often focus on static classification or cohort-level risk estimation, providing limited support for subject-specific modelling and uncertainty-aware reasoning. To address these limitations, we present a personalised digital twin framework for AD prediction and scenario-based analysis using multimodal longitudinal data. The proposed approach integrates complementary modelling strategies to capture clinical transitions and temporal dependencies across visits. Using data from the Alzheimer's Disease Neuroimaging Initiative (ADNI), including cognitive assessments, clinical variables, and MRI-derived phenotypes, the framework predicts cognitive status and diagnostic categories while quantifying predictive uncertainty and enabling patient-specific what-if trajectory analysis. Evaluation on leak-free subject-level splits demonstrates strong performance in score forecasting and diagnosis classification. In this sparse and irregular ADNI setting, transition-based modelling of adjacent visits achieved higher predictive accuracy than the sequence-based branch, suggesting that local transition modelling may be more data-efficient. While sequence models remain valuable for uncertainty-aware trajectory forecasting, local transition modelling offers a more data-efficient and robust predictive strategy. These findings highlight the importance of aligning temporal modelling strategies with clinical data structure and suggest that transition-based digital twin formulations may provide a practical and interpretable approach for personalised disease forecasting in neurodegenerative disorders.
匹配关键词: swarm intelligence
---

[ACADEMIC - ARXIV]
标题: Visual Prompting Meets Feature Reconstruction-Based Anomaly Detection with Dual-Teacher Supervision
作者: Mateo Diaz-Bone, Daniel Caraballo, Florian Scheidegger, Thomas Frick, Mattia Rigotti, Andrea Bartezzaghi, Roy Assaf, Niccolo Avogaro, Yagmur G. Cinar, Brown Ebouky, Filip M. Janicki, Piotr S. Kluska, Cezary Skura, Cristiano Malossi
链接: https://arxiv.org/abs/2606.09670v1
完整摘要: Recent Anomaly Detection methods achieve perfect detection and segmentation scores on well-established datasets, such as MVTec. However, many of these methods face challenges when foundational assumptions - such as consistent object scale, viewpoint, background, illumination, and centered placement - are violated. Those variations that occur render anomaly detection methods unusable in many real-world scenarios. To address these limitations, we introduce three key contributions: (1) a visual prompting pipeline that isolates objects using foreground-background masking; (2) a mechanism for unfreezing the teacher in student-teacher models to improve domain adaptability; and (3) a data augmentation strategy leveraging diffusion-generated synthetic images to enhance anomaly detection performance. We achieve a 3.5 percentage point improvement over the previous state-of-the-art on the challenging AeBAD dataset by using the Masked Multiscale Reconstruction (MMR) model as our backbone.
匹配关键词: swarm intelligence
---

[ACADEMIC - ARXIV]
标题: (Auto)formalization is supposed to be easy: Trellis process semantics for spelling out rigorous proofs
作者: Wesley Pegden
链接: https://arxiv.org/abs/2606.09674v1
完整摘要: We present Trellis: an autoformalization system that leverages LLM agents in a deterministically constrained workflow to enforce incremental progress in Lean autoformalization tasks through iterative refinement of natural language proofs. Our approach is motivated by the common mathematician's notion of what it means to have a rigorous proof in the first place: namely, that it would be routine to elaborate any part of the proof in further detail. The result is a system which aims to achieve reliable autoformalization on a modest budget and with generalist agents, with specialization to autoformalization coming not from any task-specific agent training but instead from a meaning-of-rigor inspired workflow enforced by process semantics. We link to an end-to-end Lean formalization of a recent Ramsey theory breakthrough produced by the process.
匹配关键词: game theory agent
---

[ACADEMIC - ARXIV]
标题: SpatialWorld: Benchmarking Interactive Spatial Reasoning of Multimodal Agents in Real-World Tasks
作者: Hongcheng Gao, Hailong Qu, Jingyi Tang, Jiahao Wang, Zihao Huang, Hengkang Qiao, Shihong Huang, Junming Yang, Yi Li, Hongyixuan Yuan, Wenjie Li, Bohan Zeng, Wenbo Li, Bo Wang, Jianhui Liu, Olive Huang, Haoyang Huang, Wentao Zhang, Guoqing Huang, Nan Duan, Yinpeng Dong
链接: https://arxiv.org/abs/2606.09669v1
完整摘要: Spatial reasoning is a foundational capability for multimodal large language models (MLLMs) to perceive and operate within the physical world. However, existing benchmarks predominantly rely on passive evaluation (e.g., static VQA) or simulator-specific pipelines, failing to assess general interactive spatial understanding. We introduce SpatialWorld, a unified benchmark designed specifically for evaluating the interactive spatial understanding of multimodal agents in complex real-world tasks. Integrating eight heterogeneous simulation backends under a shared, simulator-agnostic protocol, SpatialWorld features 760 human-annotated tasks across diverse domains (e.g., household routines, travel, social collaboration). Agents must solve tasks under vision-only partial observability, actively gathering egocentric visual evidence and expressing decisions via a unified, text-based action interface native to MLLMs. For reliable evaluation, each task includes a human-validated initial state, a reference trajectory, and a terminal-state verifier. Evaluating 15 advanced agents reveals that robust spatial task solving remains challenging: the strongest model, GPT-5, achieves an average task success rate (TSR) of only 17.4%, while the leading open-source model, Qwen-3.5, reaches 14.1%. Further analysis exposes a clear mismatch between task success and execution efficiency, alongside substantial domain-specific performance variations. These bottlenecks in active exploration and long-horizon planning position SpatialWorld as a rigorous testbed for future spatial agents.
匹配关键词: game theory agent
---

[ACADEMIC - ARXIV]
标题: From 0-to-1 to 1-to-N: Reproducible Engineering Evidence for MetaAI Recursive Self-Design
作者: Dun Li, Jiatao Li, Hongzhi Li
链接: https://arxiv.org/abs/2606.09663v1
完整摘要: Recursive self-design refers to AI-assisted modification of the mechanisms by which an AI system is built, evaluated, and improved. This paper treats MetaAI not as a mature paradigm, but as a working term for a human-seeded, AI-expanded development pattern in which the design space itself becomes a target of modification. We propose an operational evidence framework with four criteria: inspectable target system, meta-level modifier, feedback-directed selection, and recursive continuation. We then map public systems, including Darwin Goedel Machine (DGM), STOP, Goedel Agent, and ShinkaEvolve, against these criteria. DGM provides the most direct currently reported evidence: its published results show improvement from 20% to 50% on SWE-bench Verified and from 14.2% to 30.7% on full Polyglot after 80 iterations, with ablations suggesting that both open-ended exploration and self-improvement contribute. Finally, we provide MetaAI-Mini, a reproducible HumanEval-based protocol and codebase. Because no completed model run is included in this build, MetaAI-Mini is reported as a protocol rather than as an experimental result.
匹配关键词: game theory agent
---

[ACADEMIC - ARXIV]
标题: End-to-End Context Compression at Scale
作者: Ang Li, Sean McLeish, Haozhe Chen, Nimit Kalra, Zaiqian Chen, Artem Gazizov, Venkata Anoop Suhas Kumar Morisetty, Bhavya Kailkhura, Harshitha Menon, Zhuang Liu, Brian R. Bartoldson, Tom Goldstein, Sanae Lotfi, Micah Goldblum, Pavel Izmailov
链接: https://arxiv.org/abs/2606.09659v1
完整摘要: Long-context language model inference is bottlenecked by memory, as the KV cache grows with context length. Recent techniques to compress the KV cache fall short: they either degrade model quality substantially or require considerable time and compute to compress a single long prompt. Furthermore, many methods require the input to fit within the target model's context window, and are generally incompatible with modern production inference engines. Encoder-decoder compressors, which map a long token sequence to a shorter sequence of latent embeddings consumed by a decoder, are an appealing alternative in principle. However, existing approaches are not competitive with KV cache compression on the accuracy-efficiency frontier. In this work, we revisit encoder-decoder compression and close this gap. We first perform an architecture search, pre-training many variants from scratch to determine how best to design and train encoder-decoder compressors. Guided by our findings, we continually pre-train a family of 0.6B-encoder, 4B-decoder models on over 350B tokens each, at compression ratios of 1:4, 1:8, and 1:16. We introduce Latent Context Language Models (LCLMs), a family of compressors that improve the Pareto frontier across general-task performance, compression speed, and peak memory usage. We demonstrate that LCLMs serve as efficient backbones for long-horizon agents, letting the agent skim through a compressed long context and adaptively expand relevant segments on demand.
匹配关键词: game theory agent
---

[ACADEMIC - ARXIV]
标题: A Unifying Framework for Concept-Based Representational Similarity
作者: Grégoire Dhimoïla, Victor Boutin, Agustin Martin Picard, Thomas Fel, Thomas Serre
链接: https://arxiv.org/abs/2606.09653v1
完整摘要: Learned representations across models and modalities often exhibit striking structural similarities, suggesting shared underlying concept decompositions. However, concept alignment remains poorly defined: existing approaches optimize different objectives under the same terminology, obscuring what is actually aligned. We propose a unifying framework that decomposes alignment along two axes: what is aligned (representations vs. concepts) and at what level (instance-wise vs. distributional). This induces four corresponding properties -- instance-wise and distributional variants of translation and concept consistency -- and reveals precisely which of these guarantees existing methods provide. We further introduce \InterVenchA, an intervention-based benchmark that separately measures extraction quality, translation quality, and concept consistency. Through theory and experiments, we show that commonly assumed equivalences between alignment objectives fail in practice: optimizing one property does not reliably recover the others, and purely unsupervised objectives fail to recover meaningful instance-level alignment. We then propose the Coupled Sparse Autoencoder (CoSAE), which jointly enforces complementary alignment objectives. Strong alignment emerges only in this regime. Surprisingly, as little as 0.1\% paired data is sufficient to recover instance-level alignment when anchoring distributional objectives. Overall, our results show that concept alignment is fundamentally multi-objective: it must be defined, measured, and optimized as such.
匹配关键词: game theory agent
---

[ACADEMIC - ARXIV]
标题: (Auto)formalization is supposed to be easy: Trellis process semantics for spelling out rigorous proofs
作者: Wesley Pegden
链接: https://arxiv.org/abs/2606.09674v1
完整摘要: We present Trellis: an autoformalization system that leverages LLM agents in a deterministically constrained workflow to enforce incremental progress in Lean autoformalization tasks through iterative refinement of natural language proofs. Our approach is motivated by the common mathematician's notion of what it means to have a rigorous proof in the first place: namely, that it would be routine to elaborate any part of the proof in further detail. The result is a system which aims to achieve reliable autoformalization on a modest budget and with generalist agents, with specialization to autoformalization coming not from any task-specific agent training but instead from a meaning-of-rigor inspired workflow enforced by process semantics. We link to an end-to-end Lean formalization of a recent Ramsey theory breakthrough produced by the process.
匹配关键词: agent communication
---

[ACADEMIC - ARXIV]
标题: SpatialWorld: Benchmarking Interactive Spatial Reasoning of Multimodal Agents in Real-World Tasks
作者: Hongcheng Gao, Hailong Qu, Jingyi Tang, Jiahao Wang, Zihao Huang, Hengkang Qiao, Shihong Huang, Junming Yang, Yi Li, Hongyixuan Yuan, Wenjie Li, Bohan Zeng, Wenbo Li, Bo Wang, Jianhui Liu, Olive Huang, Haoyang Huang, Wentao Zhang, Guoqing Huang, Nan Duan, Yinpeng Dong
链接: https://arxiv.org/abs/2606.09669v1
完整摘要: Spatial reasoning is a foundational capability for multimodal large language models (MLLMs) to perceive and operate within the physical world. However, existing benchmarks predominantly rely on passive evaluation (e.g., static VQA) or simulator-specific pipelines, failing to assess general interactive spatial understanding. We introduce SpatialWorld, a unified benchmark designed specifically for evaluating the interactive spatial understanding of multimodal agents in complex real-world tasks. Integrating eight heterogeneous simulation backends under a shared, simulator-agnostic protocol, SpatialWorld features 760 human-annotated tasks across diverse domains (e.g., household routines, travel, social collaboration). Agents must solve tasks under vision-only partial observability, actively gathering egocentric visual evidence and expressing decisions via a unified, text-based action interface native to MLLMs. For reliable evaluation, each task includes a human-validated initial state, a reference trajectory, and a terminal-state verifier. Evaluating 15 advanced agents reveals that robust spatial task solving remains challenging: the strongest model, GPT-5, achieves an average task success rate (TSR) of only 17.4%, while the leading open-source model, Qwen-3.5, reaches 14.1%. Further analysis exposes a clear mismatch between task success and execution efficiency, alongside substantial domain-specific performance variations. These bottlenecks in active exploration and long-horizon planning position SpatialWorld as a rigorous testbed for future spatial agents.
匹配关键词: agent communication
---

[ACADEMIC - ARXIV]
标题: From 0-to-1 to 1-to-N: Reproducible Engineering Evidence for MetaAI Recursive Self-Design
作者: Dun Li, Jiatao Li, Hongzhi Li
链接: https://arxiv.org/abs/2606.09663v1
完整摘要: Recursive self-design refers to AI-assisted modification of the mechanisms by which an AI system is built, evaluated, and improved. This paper treats MetaAI not as a mature paradigm, but as a working term for a human-seeded, AI-expanded development pattern in which the design space itself becomes a target of modification. We propose an operational evidence framework with four criteria: inspectable target system, meta-level modifier, feedback-directed selection, and recursive continuation. We then map public systems, including Darwin Goedel Machine (DGM), STOP, Goedel Agent, and ShinkaEvolve, against these criteria. DGM provides the most direct currently reported evidence: its published results show improvement from 20% to 50% on SWE-bench Verified and from 14.2% to 30.7% on full Polyglot after 80 iterations, with ablations suggesting that both open-ended exploration and self-improvement contribute. Finally, we provide MetaAI-Mini, a reproducible HumanEval-based protocol and codebase. Because no completed model run is included in this build, MetaAI-Mini is reported as a protocol rather than as an experimental result.
匹配关键词: agent communication
---

[ACADEMIC - ARXIV]
标题: End-to-End Context Compression at Scale
作者: Ang Li, Sean McLeish, Haozhe Chen, Nimit Kalra, Zaiqian Chen, Artem Gazizov, Venkata Anoop Suhas Kumar Morisetty, Bhavya Kailkhura, Harshitha Menon, Zhuang Liu, Brian R. Bartoldson, Tom Goldstein, Sanae Lotfi, Micah Goldblum, Pavel Izmailov
链接: https://arxiv.org/abs/2606.09659v1
完整摘要: Long-context language model inference is bottlenecked by memory, as the KV cache grows with context length. Recent techniques to compress the KV cache fall short: they either degrade model quality substantially or require considerable time and compute to compress a single long prompt. Furthermore, many methods require the input to fit within the target model's context window, and are generally incompatible with modern production inference engines. Encoder-decoder compressors, which map a long token sequence to a shorter sequence of latent embeddings consumed by a decoder, are an appealing alternative in principle. However, existing approaches are not competitive with KV cache compression on the accuracy-efficiency frontier. In this work, we revisit encoder-decoder compression and close this gap. We first perform an architecture search, pre-training many variants from scratch to determine how best to design and train encoder-decoder compressors. Guided by our findings, we continually pre-train a family of 0.6B-encoder, 4B-decoder models on over 350B tokens each, at compression ratios of 1:4, 1:8, and 1:16. We introduce Latent Context Language Models (LCLMs), a family of compressors that improve the Pareto frontier across general-task performance, compression speed, and peak memory usage. We demonstrate that LCLMs serve as efficient backbones for long-horizon agents, letting the agent skim through a compressed long context and adaptively expand relevant segments on demand.
匹配关键词: agent communication
---

[ACADEMIC - ARXIV]
标题: Beyond Accuracy: Community Perspectives on Machine Translation
作者: Yujun Wang, Ehud Reiter, Shimei Pan, Steffen Eger, Wei Zhao
链接: https://arxiv.org/abs/2606.09655v1
完整摘要: Despite remarkable progress in machine translation (MT), non-AI communities have raised growing concerns about MT systems, suggesting a noticeable gap between technical advancement and the needs of real-world users. For instance, while NLP researchers focus on benchmark performance, end users care about ethical concerns, trust, reliability, costs, and more. We argue that listening to various user communities is essential so that research efforts would be directed towards the problems that the communities care about. To this end, we present a large-scale analysis, for the first time, that investigates what four stakeholder communities (AI developers, professional translators, language learners, and language service providers) post about MT technology on social media. To do so, we construct a dataset of 79,286 posts and comments from Reddit, Facebook, Bluesky, and Mastodon from 2019 to 2025, and analyse where these communities disagree, and how and why. Overall, we find that communities often disagree, and even show strong conflicts due to polarised sentiments on topics such as translation quality, efficiency, and reliability. This is because these communities approach these topics differently: the AI community frames them as technical and computational problems, while non-AI (user) communities care more about quality nuances, time savings, user trust, and broader social issues.
匹配关键词: agent communication
---

[ACADEMIC - ARXIV]
标题: Cross-Modal Masking for Robust Silent Speech Synthesis Using sEMG and Lipreading
作者: Eder del Blanco, David Gimeno-Gómez, Eva Navas, Carlos-D. Martínez-Hinarejos, Inma Hernáez
链接: https://arxiv.org/abs/2606.09667v1
完整摘要: Speech restoration through silent speech interfaces (SSIs) has emerged as a promising assistive technology for individuals with impaired or absent laryngeal voice production. Among non-invasive SSI modalities, surface electromyography (sEMG) and video-based lipreading provide complementary articulatory information, yet their integration for continuous speech synthesis remains underexplored. Moreover, existing multimodal approaches rarely address robustness to modality degradation or temporary sensor failure, limiting their applicability in realistic scenarios. In this work, we propose a masked multimodal speech synthesis framework that jointly leverages sEMG and lipreading signals through modality masking during training. Under multispeaker settings, the proposed approach reduces word error rate by up to 14 absolute percentage points compared to the strongest unimodal baseline. Experimental results not only show that masking strategies are critical for these performance gains and robustness under low-bitrate conditions, but also that they generalize better than degradation-specific data augmentations in the presence of modality absence conditions. Phone-level analyses further reveal complementary contributions across modalities, with particularly strong benefits for vowels and for specific consonant groups. Overall, these findings demonstrate the effectiveness and robustness of masked multimodal integration for silent speech synthesis, although adaptation to laryngectomized speakers remains an open research challenge.
匹配关键词: emergent behavior
---

[ACADEMIC - ARXIV]
标题: In-Context Learning for Latent Space Bayesian Optimization
作者: Tuan A. Vu, Harri Lähdesmäki, Julien Martinelli
链接: https://arxiv.org/abs/2606.09664v1
完整摘要: Bayesian optimization (BO) is a central tool for sample-efficient design, and latent-space Bayesian optimization (LSBO) extends it to structured objects such as molecules and proteins. In parallel, tabular foundation models such as TabPFN and TabICL now achieve state-of-the-art regression performance and are increasingly used as BO surrogates. Because their Bayesian behavior is induced by large synthetic pretraining collections, the composition of this pretraining distribution is crucial. LSBO creates a distinctive mismatch: the induced map from latent code to objective value differs markedly from the regression tasks used to train current in-context models. We address this mismatch by complementing the pretraining stage of tabular foundation model surrogates with synthetic optimization tasks defined on the latent space of a molecular VAE. The continued-pretraining objective features a regularizer that anchors the model to the original checkpoint, preserving its broad regression prior while avoiding overspecialization to the adaptation tasks. On held-out molecular optimization benchmarks, the resulting model achieves strong performance, supporting the relevance of LSBO-specific adaptation for in-context surrogates.
匹配关键词: emergent behavior
---

[ACADEMIC - ARXIV]
标题: Muon Learns More Robust and Transferable Features than Adam
作者: Tianyu Ruan, Fengzhuo Zhang, Shuche Wang, Shihua Zhang
链接: https://arxiv.org/abs/2606.09658v1
完整摘要: Muon has recently emerged as a state-of-the-art optimizer for pretraining Large Language Models (LLMs) and vision classifiers. Despite its efficiency advantage over Adam and SGD, the feature-learning advantage of Muon remains unclear. This paper investigates Muon's feature-learning advantage through the lens of robustness and transferability. First, by evaluating pretrained models on corrupted images and texts, we show that features learned by Muon are consistently more robust than those learned by Adam and SGD across different architectures, including transformers and Convolutional Neural Networks (CNNs). Using trained layer-wise probes, we further show that this robustness advantage is reflected in larger logit margins across layers. Second, by training linear classifiers or fine-tuning full models from pretrained parameters on downstream tasks, we demonstrate that Muon-learned features transfer more effectively than those learned by Adam and SGD. This transferability advantage is further supported by the diversity of hidden states across layers, as measured by effective rank. Finally, in a representative classification problem with multi-component features, we prove that Muon attains larger margins and higher effective rank than Adam and SGD, providing theoretical support for our empirical findings.
匹配关键词: emergent behavior
---

[ACADEMIC - ARXIV]
标题: A Unifying Framework for Concept-Based Representational Similarity
作者: Grégoire Dhimoïla, Victor Boutin, Agustin Martin Picard, Thomas Fel, Thomas Serre
链接: https://arxiv.org/abs/2606.09653v1
完整摘要: Learned representations across models and modalities often exhibit striking structural similarities, suggesting shared underlying concept decompositions. However, concept alignment remains poorly defined: existing approaches optimize different objectives under the same terminology, obscuring what is actually aligned. We propose a unifying framework that decomposes alignment along two axes: what is aligned (representations vs. concepts) and at what level (instance-wise vs. distributional). This induces four corresponding properties -- instance-wise and distributional variants of translation and concept consistency -- and reveals precisely which of these guarantees existing methods provide. We further introduce \InterVenchA, an intervention-based benchmark that separately measures extraction quality, translation quality, and concept consistency. Through theory and experiments, we show that commonly assumed equivalences between alignment objectives fail in practice: optimizing one property does not reliably recover the others, and purely unsupervised objectives fail to recover meaningful instance-level alignment. We then propose the Coupled Sparse Autoencoder (CoSAE), which jointly enforces complementary alignment objectives. Strong alignment emerges only in this regime. Surprisingly, as little as 0.1\% paired data is sufficient to recover instance-level alignment when anchoring distributional objectives. Overall, our results show that concept alignment is fundamentally multi-objective: it must be defined, measured, and optimized as such.
匹配关键词: emergent behavior
---

[ACADEMIC - ARXIV]
标题: ArtiFact: A Large-Scale Multi-Modal Cultural Heritage Dataset
作者: Luciano Duarte, Olga Ovcharenko, Sebastian Schelter
链接: https://arxiv.org/abs/2606.09648v1
完整摘要: Multi-modal data management has emerged as a central research topic in the database community, spanning data integration, semantic query processing, and data quality assessment. Despite this growing interest, the community lacks large-scale, real-world datasets combining tables, text, and images. We present ArtiFact, a multi-modal cultural heritage dataset of 651045 museum records collected from the Metropolitan Museum of Art, the Art Institute of Chicago, and the Rijksmuseum. We demonstrate the utility of ArtiFact through two downstream tasks. For cross-modal error detection, we introduce a curated taxonomy of seven error categories injected into 130209 records and show that reliably detecting subtle domain-specific errors such as material anachronisms and temporal shifts remain an open challenge. For semantic query processing, we show that current systems struggle with queries involving cultural proximity, ambiguous object types, and historically contingent terminology. Our results position ArtiFact as a challenging benchmark for multi-modal data management research.
匹配关键词: emergent behavior
---

[ACADEMIC - ARXIV]
标题: Correlation Is Not Enough: Embedding Human Metadata for Individual Causal Discovery
作者: Suraj Biswas, Saurabh Gupta, Pritam Mukherjee
链接: https://arxiv.org/abs/2606.09672v1
完整摘要: Ask a pretrained biomedical language model whether "cortisol 28 ug/dL" and "stock-market volatility" are related, and it returns a cosine similarity of 0.83 on a scale where 1.0 means identical. The two share no mechanism. This is not a corner case: every off-the-shelf biomedical encoder we tested (BioBERT, PubMedBERT, BioM-ELECTRA) scores unrelated cross-domain pairs between 0.76 and 0.92 when the answer should be near zero. Accuracy on cross-domain discrimination is 0%. Retrieval systems survive this, because a language model downstream filters the noise. A Large Behavioural Model (LBM), a foundation model whose subject is a person rather than a sentence, does not: it reasons over a graph of a user's life and treats embedding proximity as evidence that two events are causally linked. False proximity writes a false causal edge, and everything downstream inherits the error. Here, embedding geometry is not a tuning knob; it is correctness. We report the fix. A contrastive pass over 72,034 pairs raises PubMedBERT BIOSSES correlation from 0.633 to 0.828 and within-vs-across-domain separation from 1.05x to 1.63x. A second pass, BODHI, mines hard negatives from edges absent in a biomedical knowledge graph and lifts separation to 2.30x and the discrimination gap to +0.392, at a 4.5% BIOSSES cost. On an Intel Xeon 6737P with AMX, OpenVINO cuts single-query latency from 1367 ms to 10 ms (133x) and reaches 555 sentences/sec. One finding contradicts standard advice: FP16 beats INT8 on this silicon at every serving batch size, and we explain why. The same model on a no-AMX Ice Lake instance runs 13-27x slower. We release the benchmark suite, training corpora, the BODHI generator, and the OpenVINO scripts.
匹配关键词: reasoning
---

[ACADEMIC - ARXIV]
标题: Transition-Based Digital Twin Modelling for Alzheimer's Disease under Sparse Longitudinal Data
作者: Yinyu Huang, Yilin Zhang, Sofia Michopoulou, Christopher Kipps, Rahman Attar
链接: https://arxiv.org/abs/2606.09671v1
完整摘要: Alzheimer's disease (AD) progression is highly heterogeneous and is typically observed through sparse and irregular longitudinal data, posing challenges for prediction and personalised monitoring. Existing machine learning approaches have improved AD prediction using multimodal data, yet often focus on static classification or cohort-level risk estimation, providing limited support for subject-specific modelling and uncertainty-aware reasoning. To address these limitations, we present a personalised digital twin framework for AD prediction and scenario-based analysis using multimodal longitudinal data. The proposed approach integrates complementary modelling strategies to capture clinical transitions and temporal dependencies across visits. Using data from the Alzheimer's Disease Neuroimaging Initiative (ADNI), including cognitive assessments, clinical variables, and MRI-derived phenotypes, the framework predicts cognitive status and diagnostic categories while quantifying predictive uncertainty and enabling patient-specific what-if trajectory analysis. Evaluation on leak-free subject-level splits demonstrates strong performance in score forecasting and diagnosis classification. In this sparse and irregular ADNI setting, transition-based modelling of adjacent visits achieved higher predictive accuracy than the sequence-based branch, suggesting that local transition modelling may be more data-efficient. While sequence models remain valuable for uncertainty-aware trajectory forecasting, local transition modelling offers a more data-efficient and robust predictive strategy. These findings highlight the importance of aligning temporal modelling strategies with clinical data structure and suggest that transition-based digital twin formulations may provide a practical and interpretable approach for personalised disease forecasting in neurodegenerative disorders.
匹配关键词: reasoning
---

[ACADEMIC - ARXIV]
标题: SpatialWorld: Benchmarking Interactive Spatial Reasoning of Multimodal Agents in Real-World Tasks
作者: Hongcheng Gao, Hailong Qu, Jingyi Tang, Jiahao Wang, Zihao Huang, Hengkang Qiao, Shihong Huang, Junming Yang, Yi Li, Hongyixuan Yuan, Wenjie Li, Bohan Zeng, Wenbo Li, Bo Wang, Jianhui Liu, Olive Huang, Haoyang Huang, Wentao Zhang, Guoqing Huang, Nan Duan, Yinpeng Dong
链接: https://arxiv.org/abs/2606.09669v1
完整摘要: Spatial reasoning is a foundational capability for multimodal large language models (MLLMs) to perceive and operate within the physical world. However, existing benchmarks predominantly rely on passive evaluation (e.g., static VQA) or simulator-specific pipelines, failing to assess general interactive spatial understanding. We introduce SpatialWorld, a unified benchmark designed specifically for evaluating the interactive spatial understanding of multimodal agents in complex real-world tasks. Integrating eight heterogeneous simulation backends under a shared, simulator-agnostic protocol, SpatialWorld features 760 human-annotated tasks across diverse domains (e.g., household routines, travel, social collaboration). Agents must solve tasks under vision-only partial observability, actively gathering egocentric visual evidence and expressing decisions via a unified, text-based action interface native to MLLMs. For reliable evaluation, each task includes a human-validated initial state, a reference trajectory, and a terminal-state verifier. Evaluating 15 advanced agents reveals that robust spatial task solving remains challenging: the strongest model, GPT-5, achieves an average task success rate (TSR) of only 17.4%, while the leading open-source model, Qwen-3.5, reaches 14.1%. Further analysis exposes a clear mismatch between task success and execution efficiency, alongside substantial domain-specific performance variations. These bottlenecks in active exploration and long-horizon planning position SpatialWorld as a rigorous testbed for future spatial agents.
匹配关键词: reasoning
---

[ACADEMIC - ARXIV]
标题: When Built-in Thinking Helps and Hurts: Constraint-Level Error Shifts in Instruction Following
作者: Sai Adith Senthil Kumar
链接: https://arxiv.org/abs/2606.09662v1
完整摘要: Large reasoning models (LRMs) often improve math and coding performance, but their effect on instruction following is unclear. We study IFEval with Qwen3 models (1.7B-32B), using same-weights Thinking ON/OFF controls; four Hunyuan models provide directional cross-family support. Aggregate pass-rate changes are small (-0.55 to -3.52 pp), yet 10-20% of prompts switch between pass and fail across modes, suggesting that thinking changes the pattern of errors--some prompts improve while others worsen--rather than uniformly degrading performance. Under a post-hoc Qwen3-derived grouping, constraint types separate into Planning (global counting, structure, coordination), which improves at the class level under thinking, and Precision (exact local form), which consistently worsens; the class-level Planning/Precision sign pattern holds directionally for all four Hunyuan models despite Hunyuan's opposite aggregate direction. Thinking also changes final-answer length; matched-length analyses substantially reduce the Precision drop, but a residual penalty remains. Analyzing thinking traces with a cross-encoder relevance metric reveals three patterns: Neutral shows a positive relevance-compliance link (r approximately 0.15); Planning shows near-zero predictive correlation (r approximately 0.02) despite measurable trace engagement, consistent with an execution gap between CE-measured trace relevance and final-answer compliance; Precision shows a small negative correlation (r approximately -0.05), with failing instances having higher mean relevance than passing ones. Activation patching across four model sizes (1.7B-14B) shows that Precision flip instances are more often restored than Planning flip instances (32-58% vs. 14-40% mean layer-restoration), with the largest gap at 14B (about 30 pp).
匹配关键词: reasoning
---

[ACADEMIC - ARXIV]
标题: Where Does the Answer Come From? Benchmarking View-Level Visual Evidence Identification in Multi-View MLLMs for Autonomous Driving
作者: Yimu Wang, Yee Man Choi, Barry Zhang, Mozhgan Nasr Azadani, Sean Sedwards, Krzysztof Czarnecki
链接: https://arxiv.org/abs/2606.09644v1
完整摘要: Multimodal large language models (MLLMs) achieve strong results on visual reasoning benchmarks, but answer accuracy alone does not indicate whether a model relied on the correct visual evidence. This gap is particularly important in multi-view driving scenes used for autonomous driving, where a model can produce a plausible answer while grounding it in the wrong camera view. We introduce a multi-view visual question answering benchmark for evaluating evidence-source identification: given six synchronized NuScenes views and a question, the model must identify the supporting camera view and answer the question. The benchmark contains 122 conflict-centric question-answer pairs from 73 scenes, spanning causality, counterfactual reasoning, and intent prediction. View labels are proposed by an automatic conflict-mining pipeline and manually verified by annotators. We evaluate three settings: camera-view selection, oracle QA given the golden view, and joint prediction in which the model selects a view and answers in one pass. Answers are evaluated in both multiple-choice and free-form formats, using exact match for structured predictions and an LLM judge for free-form responses. By explicitly separating visual-source identification from answer correctness, the benchmark exposes grounding failures that answer-only evaluation misses.
匹配关键词: reasoning
---

[ACADEMIC - ARXIV]
标题: Optical Reasoning: Rethinking Images as an Expressive Reasoning Medium Beyond Text
作者: Yutong Bian, Dongjie Cheng, Heming Xia, Yongqi Li, Wenjie Li
链接: https://arxiv.org/abs/2606.09585v1
完整摘要: Chain-of-Thought (CoT) improves the performance of Large Language Models (LLMs) and has been extended to Multimodal Large Language Models (MLLMs). More recent work further moves from text-based multimodal reasoning toward interleaved-modal reasoning, where intermediate steps can incorporate both textual rationales and visual evidence. In this work, we propose a bolder and more ambitious idea: could images alone serve as the reasoning medium for both language and multimodal tasks? To explore this, we propose optical reasoning, which treats images as a standalone reasoning medium. We instantiate this concept with two variants: typographic-based optical reasoning, which optimizes visual layouts for compact rationale rendering, and graphical-based optical reasoning, which composes text and graphical elements into structured visual rationales. Across mathematical, scientific, and interleaved-modal reasoning benchmarks, optical reasoning can match or even exceed traditional text reasoning while reducing reasoning tokens by an average of 28.57% on language tasks and 16% on multimodal tasks, achieving 1.96 times the token efficiency of text reasoning. These results show that images can effectively and efficiently encode rationales while providing a unified visual canvas for reasoning.
匹配关键词: chain-of-thought
---

[ACADEMIC - ARXIV]
标题: IMUG-Bench: Benchmarking Unified Multimodal Models on Interleaved Understanding and Generation
作者: Lingyi Meng, Zecong Tang, Haoran Li, Tengju Ru, Zhejun Cui, Weitong Lian, Qi Kang, Hangshuo Cao, Yichen Zhu, Yechi Liu, Kaixuan Wang, Yu-Jie Yuan, Chunwei Wang, Yu Zhang, Bo Dai
链接: https://arxiv.org/abs/2606.09169v1
完整摘要: In recent years, unified multimodal models (UMMs) have emerged to support both understanding and generation within a single framework. Mastering dynamic, multi-turn interleaved image-text dialogues is a crucial task for UMMs in real-world applications. However, existing benchmarks fail to evaluate this important task, as they are often limited to single-turn or static settings, and typically overlook exposure bias in multi-turn interactions. To bridge this gap, we propose IMUG-Bench, a comprehensive benchmark for multi-turn interleaved image-text dialogue of UMMs that jointly evaluates their understanding and generation capabilities. Our IMUG-Bench comprises three classes: Static Spatial, Temporal Causal, and Hybrid, covering 3,113 samples and 12,034 interaction turns. It also includes dynamic understanding questions, thereby supporting evaluation that better reflects real-world multi-turn interaction scenarios. Large-scale experiments on IMUG-Bench systematically evaluate mainstream open-source and closed-source UMMs, revealing their capability boundaries and failure modes, and uncovering pronounced exposure bias on the generation side in multi-turn interactions. We further explore several test-time scaling strategies, including Chain-of-Thought, Self-Verification, and Best-of-N Sampling, which effectively improve generation accuracy and mitigate exposure bias in generation tasks. These findings provide insights into enhancing the robustness and multi-turn interaction capability of future UMMs.
匹配关键词: chain-of-thought
---

[ACADEMIC - ARXIV]
标题: CRANE: Knowledge Editing for Reasoning MLLMs
作者: Han Huang, Hao Wang, Mengqi Zhang, Shu Wu, Qiang Liu, Liang Wang
链接: https://arxiv.org/abs/2606.09033v1
完整摘要: The emergence of reasoning multimodal large language models (MLLMs), which generate explicit chain-of-thought (CoT) reasoning before producing answers, has introduced a new challenge for knowledge editing: methods that appear successful under traditional metrics (teacher-forcing accuracy up to 100%) can fail severely when the model's reasoning process is examined (Grounded Success as low as 0%). We identify three failure modes: (1) Structural Collapse, where weight-modifying methods destroy the CoT format; (2) Cognitive Dissonance, where the model's reasoning chain actively rejects the injected edit fact based on visual evidence; and (3) Shallow Internalization, where methods succeed on exact queries but fail on rephrase or multi-hop variants. On reasoning MLLMs, these modes interact: methods that generalize (FT, LoRA) trigger format collapse, while methods without deep modification cannot generalize. To expose these failures, we propose a CoT-aware evaluation protocol and construct ReasonEdit-Bench, with conflict stratification, multi-level probes, and multi-hop portability tests. We propose CRANE, a retrieval-augmented framework that requires no per-edit parameter modification. CRANE combines a modality-aware dual-library retrieval system with a two-phase training strategy: Supervised Fine-Tuning (SFT) for structural initialization, followed by GRPO with a Cognitive Routing Reward that trains the model to arbitrate between visual priors and injected edit facts. On ReasonEdit-Bench, CRANE achieves 96.9% Grounded Success on conflict scenarios and 96.9% intermediate entity usage in multi-hop chains, with 97.6% text-locality and 68.1% image-locality Edit Independence. On the out-of-distribution MMEVOKE benchmark, CRANE reaches 87.0% under gold retrieval.
匹配关键词: chain-of-thought
---

[ACADEMIC - ARXIV]
标题: MeCo: One-Step MeanFlow-based Corrector for Multi-Channel Speech Separation
作者: Dohwan Kim, Jung-Woo Choi
链接: https://arxiv.org/abs/2606.09677v1
完整摘要: While discriminative models for multi-channel speech separation excel in reference-based metrics, they often exhibit suboptimal human listening quality. To address this, we propose a novel MeanFlow-based one-step generative corrector (MeCo). MeCo learns a conditional average velocity field to map discriminative estimates directly onto the clean speech manifold in a single step. To maximize one-step generation performance, we introduce Data-Space Optimization (DSO). DSO integrates an $\mathbf{x}_r$-loss, which penalizes prediction errors on longer displacement intervals to serve as a generative objective for human listening quality, with an Endpoint SI-SDR loss that directly optimizes terminal signal fidelity. Experiments demonstrate that MeCo achieves state-of-the-art (SOTA) performance with minimal computational overhead, simultaneously achieving superior signal fidelity and human listening quality in both in-domain and out-of-domain scenarios.
匹配关键词: test-time compute
---

[ACADEMIC - ARXIV]
标题: End-to-End Context Compression at Scale
作者: Ang Li, Sean McLeish, Haozhe Chen, Nimit Kalra, Zaiqian Chen, Artem Gazizov, Venkata Anoop Suhas Kumar Morisetty, Bhavya Kailkhura, Harshitha Menon, Zhuang Liu, Brian R. Bartoldson, Tom Goldstein, Sanae Lotfi, Micah Goldblum, Pavel Izmailov
链接: https://arxiv.org/abs/2606.09659v1
完整摘要: Long-context language model inference is bottlenecked by memory, as the KV cache grows with context length. Recent techniques to compress the KV cache fall short: they either degrade model quality substantially or require considerable time and compute to compress a single long prompt. Furthermore, many methods require the input to fit within the target model's context window, and are generally incompatible with modern production inference engines. Encoder-decoder compressors, which map a long token sequence to a shorter sequence of latent embeddings consumed by a decoder, are an appealing alternative in principle. However, existing approaches are not competitive with KV cache compression on the accuracy-efficiency frontier. In this work, we revisit encoder-decoder compression and close this gap. We first perform an architecture search, pre-training many variants from scratch to determine how best to design and train encoder-decoder compressors. Guided by our findings, we continually pre-train a family of 0.6B-encoder, 4B-decoder models on over 350B tokens each, at compression ratios of 1:4, 1:8, and 1:16. We introduce Latent Context Language Models (LCLMs), a family of compressors that improve the Pareto frontier across general-task performance, compression speed, and peak memory usage. We demonstrate that LCLMs serve as efficient backbones for long-horizon agents, letting the agent skim through a compressed long context and adaptively expand relevant segments on demand.
匹配关键词: test-time compute
---

[ACADEMIC - ARXIV]
标题: Beyond Accuracy: Community Perspectives on Machine Translation
作者: Yujun Wang, Ehud Reiter, Shimei Pan, Steffen Eger, Wei Zhao
链接: https://arxiv.org/abs/2606.09655v1
完整摘要: Despite remarkable progress in machine translation (MT), non-AI communities have raised growing concerns about MT systems, suggesting a noticeable gap between technical advancement and the needs of real-world users. For instance, while NLP researchers focus on benchmark performance, end users care about ethical concerns, trust, reliability, costs, and more. We argue that listening to various user communities is essential so that research efforts would be directed towards the problems that the communities care about. To this end, we present a large-scale analysis, for the first time, that investigates what four stakeholder communities (AI developers, professional translators, language learners, and language service providers) post about MT technology on social media. To do so, we construct a dataset of 79,286 posts and comments from Reddit, Facebook, Bluesky, and Mastodon from 2019 to 2025, and analyse where these communities disagree, and how and why. Overall, we find that communities often disagree, and even show strong conflicts due to polarised sentiments on topics such as translation quality, efficiency, and reliability. This is because these communities approach these topics differently: the AI community frames them as technical and computational problems, while non-AI (user) communities care more about quality nuances, time savings, user trust, and broader social issues.
匹配关键词: test-time compute
---

[ACADEMIC - ARXIV]
标题: MAVIS: Multi-Agent Video Retrieval via Structured Video Understanding
作者: Jie Zhang, Qilang Ye, Hao Zhou, Haochen Liang, Fei Luo
链接: https://arxiv.org/abs/2606.09641v1
完整摘要: The dominant paradigm in video retrieval relies on embedding-based full-corpus scanning, which suffers from inherent computational inefficiency and the semantic asymmetry between information-dense videos and sparse textual queries. To bridge this gap, we introduce \textbf{MAVIS}, a novel multi-agent framework that rethinks retrieval as cooperative reasoning rather than brute-force search. MAVIS first bridges the granularity mismatch by parsing raw videos into a \textbf{Structured Semantic Library}, enabling explicit attribute-level indexing. During retrieval, a planner decomposes complex user intents into atomic sub-tasks, dispatching specialized agents to independently nominate candidates. Crucially, MAVIS employs a \textbf{Logic-aware Debate} mechanism with a strict veto protocol, where agents collaboratively prune logical mismatches to identify a compact set of ``controversial'' candidates for fine-grained verification. This agentic workflow effectively bypasses the inefficiency of full-library traversal. Extensive experiments on MSR-VTT, MSVD, and ActivityNet demonstrate that MAVIS achieves competitive performance without task-specific fine-tuning, offering a scalable and interpretable alternative to traditional dual-encoder approaches.
匹配关键词: test-time compute
---

[ACADEMIC - ARXIV]
标题: Gradient-Guided Reward Optimization for Inference-time Alignment
作者: Hankun Lin, Ruqi Zhang
链接: https://arxiv.org/abs/2606.09635v1
完整摘要: Ensuring the reliability of Large Language Models (LLMs) under distribution drift requires inference-time adaptation. While inference-time alignment methods such as Best-of-$N$ and rejection sampling are widely used, they frame the task as a sampling-intensive, reward-guided search, leading to two key limitations: their performance is bounded by the base model's generation quality, and their reliance on imperfect reward models makes them vulnerable to reward hacking. To address these challenges, we introduce Gradient-Guided Reward Optimization (GGRO), a lightweight inference-time method that performs targeted, minimal intervention during decoding via gradient guidance. Specifically, GGRO monitors token-level entropy to identify high-uncertainty regions indicative of drift or misalignment. Upon detection, it responds by injecting nudging tokens, generated using gradient signals from an off-the-shelf reward model, to steer the generation trajectory rather than merely re-ranking samples. Experiments show that GGRO consistently improves inference-time alignment across safety, helpfulness, and reasoning benchmarks. It also increases coverage of high-quality responses and robustness to reward hacking, with minimal computational overhead. Code is available at https://github.com/lhk2004/GGRO.
匹配关键词: test-time compute
---

[ACADEMIC - ARXIV]
标题: Integrating gene regulatory priors into Transformer attention with scTransformer for interpretable scRNA-seq analysis
作者: Mikele Milia, Louis Fabrice Tshimanga, Henning Mueller, Manfredo Atzori, Barbara Di Camillo
链接: https://arxiv.org/abs/2606.09558v1
完整摘要: Motivation: Transformer-based models are increasingly applied to large-scale single-cell transcriptomics, showing strong performance through self-supervised learning on millions of cells. However, most existing approaches treat genes as independent features, and largely ignore prior biological knowledge, which limits interpretability and robustness. In this paper, we explore whether explicitly incorporating gene regulatory information can improve both model performance and biological insight. Results: We present scTransformer, the first Transformer-based approach that builds a priori knowledge of biological mechanisms into the model's attention patterns. By constraining information flow according to known regulatory structures, the model learns representations that are more biologically meaningful. We evaluate scTransformer on a disease-relevant single-nucleus RNA-seq dataset using supervised cell-type classification. Compared to standard Transformers, our approach improves classification accuracy, enhances separation of cell types in embedding space, and produces attention patterns consistent with known regulatory programs. Overall, our results demonstrate that embedding biological structure into Transformer models can enhance interpretability without sacrificing performance, offering a principled step toward biologically grounded foundation models for single-cell omics.
匹配关键词: self-consistency
---

[ACADEMIC - ARXIV]
标题: Overcoming Decoder Inconsistencies in Whisper for Dravidian and Low-Resource Languages
作者: Chowdam Venkata Kumar, Kumud Tripathi, Pankaj Wasnik
链接: https://arxiv.org/abs/2606.09535v1
完整摘要: Multilingual ASR models such as Whisper perform well on high-resource languages but exhibit substantially higher Word Error Rates (WER) for Dravidian languages compared to Indo-Aryan ones. Through linguistic and dataset analysis, we show that Dravidian languages have longer words, higher vocabulary diversity, and lower repetition, resulting in sparse token distributions and frequent character-level substitution errors. Baseline fine-tuning further reveals decoder imbalance between self-attention (linguistic context) and cross-attention (acoustic cues). Although synthetic token-repetition experiments indicate potential gains, they are impractical. Motivated by these observations, we introduce two decoder-level enhancements: Weighted-Attention, which adaptively balances attention sources, and Self-Conditioning, which reinjects intermediate predictions to improve token consistency. Experiments demonstrate consistent WER reductions for low-resource and agglutinative languages.
匹配关键词: self-consistency
---

[ACADEMIC - ARXIV]
标题: Self-Harness: Harnesses That Improve Themselves
作者: Hangfan Zhang, Shao Zhang, Kangcong Li, Chen Zhang, Yang Chen, Yiqun Zhang, Lei Bai, Shuyue Hu
链接: https://arxiv.org/abs/2606.09498v1
完整摘要: The performance of LLM-based agents is jointly shaped by their base models and the harnesses that mediate their interaction with the environment. Because different models exhibit distinct behaviors, effective harness design is inherently model-specific. Yet agent harnesses are still largely engineered by human experts, a paradigm that scales poorly as modern LLMs become increasingly diverse and rapidly evolving. In this paper, we introduce Self-Harness, a new paradigm in which an LLM-based agent improves its own operating harness, without relying on human engineers or stronger external agents. We operationalize Self-Harness as an iterative loop with three stages: Weakness Mining, which identifies model-specific failure patterns from execution traces; Harness Proposal, which generates diverse yet minimal harness modifications tied to these failures; and Proposal Validation, which accepts candidate edits only after regression testing. We instantiate Self-Harness on Terminal-Bench-2.0 using a minimal initial harness and three base models from diverse families: MiniMax M2.5, Qwen3.5-35B-A3B, and GLM-5. Across all three models, Self-Harness consistently improves performance, with held-out pass rates increasing from 40.5% to 61.9%, 23.8% to 38.1%, and 42.9% to 57.1%, respectively. Qualitative analyses further show that Self-Harness does not simply add generic instructions, but effectively turns model-specific weaknesses into concrete, executable harness changes. These results suggest a path toward LLM-based agents that are not merely shaped by their harnesses, but can also participate in reshaping them.
匹配关键词: self-consistency
---

[ACADEMIC - ARXIV]
标题: A Finetuned SpeechLLM for Joint Multi-Granular L2 Assessment and Natural-Language Rationales
作者: Aditya Kamlesh Parikh, Cristian Tejedor-Garcia, Catia Cucchiarini, Helmer Strik
链接: https://arxiv.org/abs/2606.09470v1
完整摘要: Automated L2 speech assessment can assign proficiency labels, but often lacks interpretability. We propose a rubric-guided SpeechLLM for multi-aspect, multi-granular assessment, trained with a hybrid objective combining supervised fine-tuning and Bounded Direct Preference Optimization. The model jointly predicts ordinal labels at the sentence-level (accuracy, fluency, prosody), word/phoneme-level accuracy, and generates a natural-language rationale in the same response. On SpeechOcean762, our approach matches or outperforms single-granularity models while remaining competitive with prior approaches. We analyze rationale reliability along two axes: self-consistency with model predictions and alignment with ground-truth labels, using sentiment consistency (plausibility) and mention-based agreement (faithfulness). Rationales are plausible at the sentence level, but faithfulness degrades at the word/phoneme level: references are sparse and weakly aligned with token-level labels.
匹配关键词: self-consistency
---

[ACADEMIC - ARXIV]
标题: DECSELFMASK: Leveraging Unlabeled Text via Self-Relevance-Guided Masking for Decoder-Only Classification
作者: Pietro Ferrazzi, Matteo Merler, Giovanni Bonetta, Alberto Lavelli, Bernardo Magnini
链接: https://arxiv.org/abs/2606.09466v1
完整摘要: Classification tasks require annotated data, which can often be expensive, time-consuming, or even unfeasible to collect. This is the case of the medical domain, where large datasets often have few annotated examples. To address this, we propose DecSelfMask (Decoder Self-learning by Masking), an approach to enhance decoder-only performance on classification tasks. We build on common self-learning approaches by leveraging a model to create training examples from unlabeled data to propose a novel relevance-guided masking strategy. We use relevance attribution methods to determine what portions of unannotated texts are relevant for a task. We then create self-supervised training examples by masking out those portions, training the model to reconstruct them via next-token-prediction. We hypothesize that those examples convey knowledge about the structure and semantics of unannotated data that can be useful for downstream performance. We test our approach on 136 tasks from a collection of 1.9M clinical notes from an Italian hospital. We quantify DecSelfMask's impact on downstream tasks on 5 models of different scales and families, including a probing analysis. Experiments show consistent gains, outperforming standard supervised fine-tuning approaches (+19.9 points in Macro F1), synthetic label generation (+12.5), and continual pretraining (+6.3), as well as common baselines.
匹配关键词: self-consistency
---

[ACADEMIC - ARXIV]
标题: SoccerNet 2026 Player-Centric Ball-Action Spotting:Retraining and Post-Processing Extensions to the FOOTPASS Baselines
作者: Parthsarthi Rawat
链接: https://arxiv.org/abs/2606.09679v1
完整摘要: We describe our system for the SoccerNet 2026 Player-Centric Ball-Action Spotting Challenge, which requires predicting who performs which action and when, across eight classes in broadcast soccer. Building on the three FOOTPASS baselines [1] (TAAD, TAAD+GNN, and TAAD+DST), we contribute four extensions: (1) gradient check pointing to enable full-backbone fine-tuning on a single GPU; (2) fusion of GNN logits into the DST encoder, combining graph-based tactical context with per-player visual features; (3) square-root frequency class weighting to address the 213:1 pass-to-tackle imbalance in the training data; and (4) a post processing pipeline comprising per-class logit gating, temporal frame refinement, jersey re-assignment, and a two-model ensemble. Our system achieves 0.548 Macro F1 on the test set and 0.446 on the challenge set (server evaluation).
匹配关键词: process reward
---

[ACADEMIC - ARXIV]
标题: (Auto)formalization is supposed to be easy: Trellis process semantics for spelling out rigorous proofs
作者: Wesley Pegden
链接: https://arxiv.org/abs/2606.09674v1
完整摘要: We present Trellis: an autoformalization system that leverages LLM agents in a deterministically constrained workflow to enforce incremental progress in Lean autoformalization tasks through iterative refinement of natural language proofs. Our approach is motivated by the common mathematician's notion of what it means to have a rigorous proof in the first place: namely, that it would be routine to elaborate any part of the proof in further detail. The result is a system which aims to achieve reliable autoformalization on a modest budget and with generalist agents, with specialization to autoformalization coming not from any task-specific agent training but instead from a meaning-of-rigor inspired workflow enforced by process semantics. We link to an end-to-end Lean formalization of a recent Ramsey theory breakthrough produced by the process.
匹配关键词: process reward
---

[ACADEMIC - ARXIV]
标题: ArtiFact: A Large-Scale Multi-Modal Cultural Heritage Dataset
作者: Luciano Duarte, Olga Ovcharenko, Sebastian Schelter
链接: https://arxiv.org/abs/2606.09648v1
完整摘要: Multi-modal data management has emerged as a central research topic in the database community, spanning data integration, semantic query processing, and data quality assessment. Despite this growing interest, the community lacks large-scale, real-world datasets combining tables, text, and images. We present ArtiFact, a multi-modal cultural heritage dataset of 651045 museum records collected from the Metropolitan Museum of Art, the Art Institute of Chicago, and the Rijksmuseum. We demonstrate the utility of ArtiFact through two downstream tasks. For cross-modal error detection, we introduce a curated taxonomy of seven error categories injected into 130209 records and show that reliably detecting subtle domain-specific errors such as material anachronisms and temporal shifts remain an open challenge. For semantic query processing, we show that current systems struggle with queries involving cultural proximity, ambiguous object types, and historically contingent terminology. Our results position ArtiFact as a challenging benchmark for multi-modal data management research.
匹配关键词: process reward
---

[ACADEMIC - ARXIV]
标题: Data-driven discovery of governing differential equations across physical systems
作者: Siyu Lou, Hao Xu, Wenguan Wang, Lu Lu, Hao Sun, Yang Liu, Linfeng Zhang, Dongxiao Zhang, Yuntian Chen
链接: https://arxiv.org/abs/2606.09638v1
完整摘要: Differential equations play a critical role in scientific discovery because they provide a mathematical framework to describe the behaviour of physical phenomena. As a promising alternative to traditional first principles, data-driven differential equation discovery has attracted increasing attention for its ability to infer governing laws directly from experimental or simulated data, especially when the underlying physics is unclear. However, the field has expanded rapidly along diverse methodological directions, particularly with the emergence of AI-based approaches, and still lacks a clear organizing perspective. In this Review, we propose a problem-oriented perspective on data-driven differential equation discovery. We first introduce a two-dimensional phase diagram of equation discoverability, where discovery problems are organized according to structural complexity and coefficient complexity. This phase diagram shows how the field has moved from the discovery of sparse equations with simple coefficients toward more complex governing laws with richer structures and more flexible parameterizations. It also clarifies why different methodological families succeed or fail in different problem settings. We then present the representation-evaluation-optimization (REO) framework as a fundamental abstraction of the discovery process. By identifying the core problems of equation discovery that persist across algorithmic variations, REO shifts the discussion from individual algorithms to the fundamental principles that determine discoverability. We connect these perspectives to applications across physics and adjacent sciences, and argue that the next challenge is not merely recovering equations, but using them to revise existing theories, distil mechanisms and form new scientific concepts.
匹配关键词: process reward
---

[ACADEMIC - ARXIV]
标题: Gradient-Guided Reward Optimization for Inference-time Alignment
作者: Hankun Lin, Ruqi Zhang
链接: https://arxiv.org/abs/2606.09635v1
完整摘要: Ensuring the reliability of Large Language Models (LLMs) under distribution drift requires inference-time adaptation. While inference-time alignment methods such as Best-of-$N$ and rejection sampling are widely used, they frame the task as a sampling-intensive, reward-guided search, leading to two key limitations: their performance is bounded by the base model's generation quality, and their reliance on imperfect reward models makes them vulnerable to reward hacking. To address these challenges, we introduce Gradient-Guided Reward Optimization (GGRO), a lightweight inference-time method that performs targeted, minimal intervention during decoding via gradient guidance. Specifically, GGRO monitors token-level entropy to identify high-uncertainty regions indicative of drift or misalignment. Upon detection, it responds by injecting nudging tokens, generated using gradient signals from an off-the-shelf reward model, to steer the generation trajectory rather than merely re-ranking samples. Experiments show that GGRO consistently improves inference-time alignment across safety, helpfulness, and reasoning benchmarks. It also increases coverage of high-quality responses and robustness to reward hacking, with minimal computational overhead. Code is available at https://github.com/lhk2004/GGRO.
匹配关键词: process reward
---

[ACADEMIC - ARXIV]
标题: Correlation Is Not Enough: Embedding Human Metadata for Individual Causal Discovery
作者: Suraj Biswas, Saurabh Gupta, Pritam Mukherjee
链接: https://arxiv.org/abs/2606.09672v1
完整摘要: Ask a pretrained biomedical language model whether "cortisol 28 ug/dL" and "stock-market volatility" are related, and it returns a cosine similarity of 0.83 on a scale where 1.0 means identical. The two share no mechanism. This is not a corner case: every off-the-shelf biomedical encoder we tested (BioBERT, PubMedBERT, BioM-ELECTRA) scores unrelated cross-domain pairs between 0.76 and 0.92 when the answer should be near zero. Accuracy on cross-domain discrimination is 0%. Retrieval systems survive this, because a language model downstream filters the noise. A Large Behavioural Model (LBM), a foundation model whose subject is a person rather than a sentence, does not: it reasons over a graph of a user's life and treats embedding proximity as evidence that two events are causally linked. False proximity writes a false causal edge, and everything downstream inherits the error. Here, embedding geometry is not a tuning knob; it is correctness. We report the fix. A contrastive pass over 72,034 pairs raises PubMedBERT BIOSSES correlation from 0.633 to 0.828 and within-vs-across-domain separation from 1.05x to 1.63x. A second pass, BODHI, mines hard negatives from edges absent in a biomedical knowledge graph and lifts separation to 2.30x and the discrimination gap to +0.392, at a 4.5% BIOSSES cost. On an Intel Xeon 6737P with AMX, OpenVINO cuts single-query latency from 1367 ms to 10 ms (133x) and reaches 555 sentences/sec. One finding contradicts standard advice: FP16 beats INT8 on this silicon at every serving batch size, and we explain why. The same model on a no-AMX Ice Lake instance runs 13-27x slower. We release the benchmark suite, training corpora, the BODHI generator, and the OpenVINO scripts.
匹配关键词: pretraining
---

[ACADEMIC - ARXIV]
标题: In-Context Learning for Latent Space Bayesian Optimization
作者: Tuan A. Vu, Harri Lähdesmäki, Julien Martinelli
链接: https://arxiv.org/abs/2606.09664v1
完整摘要: Bayesian optimization (BO) is a central tool for sample-efficient design, and latent-space Bayesian optimization (LSBO) extends it to structured objects such as molecules and proteins. In parallel, tabular foundation models such as TabPFN and TabICL now achieve state-of-the-art regression performance and are increasingly used as BO surrogates. Because their Bayesian behavior is induced by large synthetic pretraining collections, the composition of this pretraining distribution is crucial. LSBO creates a distinctive mismatch: the induced map from latent code to objective value differs markedly from the regression tasks used to train current in-context models. We address this mismatch by complementing the pretraining stage of tabular foundation model surrogates with synthetic optimization tasks defined on the latent space of a molecular VAE. The continued-pretraining objective features a regularizer that anchors the model to the original checkpoint, preserving its broad regression prior while avoiding overspecialization to the adaptation tasks. On held-out molecular optimization benchmarks, the resulting model achieves strong performance, supporting the relevance of LSBO-specific adaptation for in-context surrogates.
匹配关键词: pretraining
---

[ACADEMIC - ARXIV]
标题: Muon Learns More Robust and Transferable Features than Adam
作者: Tianyu Ruan, Fengzhuo Zhang, Shuche Wang, Shihua Zhang
链接: https://arxiv.org/abs/2606.09658v1
完整摘要: Muon has recently emerged as a state-of-the-art optimizer for pretraining Large Language Models (LLMs) and vision classifiers. Despite its efficiency advantage over Adam and SGD, the feature-learning advantage of Muon remains unclear. This paper investigates Muon's feature-learning advantage through the lens of robustness and transferability. First, by evaluating pretrained models on corrupted images and texts, we show that features learned by Muon are consistently more robust than those learned by Adam and SGD across different architectures, including transformers and Convolutional Neural Networks (CNNs). Using trained layer-wise probes, we further show that this robustness advantage is reflected in larger logit margins across layers. Second, by training linear classifiers or fine-tuning full models from pretrained parameters on downstream tasks, we demonstrate that Muon-learned features transfer more effectively than those learned by Adam and SGD. This transferability advantage is further supported by the diversity of hidden states across layers, as measured by effective rank. Finally, in a representative classification problem with multi-component features, we prove that Muon attains larger margins and higher effective rank than Adam and SGD, providing theoretical support for our empirical findings.
匹配关键词: pretraining
---

[ACADEMIC - ARXIV]
标题: Do Video Foundation Models Understand Intuitive Physics? A Layerwise Probing Analysis
作者: Samuele Punzo, Niccolò Caselli, Ippokratis Pantelidis, Francesco Massafra, Salvatore Lo Sardo, Mohammadreza Salehi
链接: https://arxiv.org/abs/2606.09646v1
完整摘要: We study whether pretrained video foundation models encode intuitive-physics information in their frozen representations, and how this information varies across model families, layers, and probe types. Using frozen-feature probing on IntPhys2 and Minimal Video Pairs (MVP), we compare predictive joint-embedding models (V-JEPA), masked reconstruction models (VideoMAE), and a diffusion-based video generator (LTX-Video). V-JEPA achieves the strongest overall results across benchmarks, especially with probes that model temporal dynamics, while VideoMAE remains competitive and LTX-Video recovers weaker but non-trivial signal. Layerwise analyses show that physics-relevant information is weakest in early layers and becomes most accessible at intermediate-to-late depth, and temporal controls show that disrupting frame order substantially reduces performance, especially on MVP. Together, these results suggest that intuitive-physics knowledge emerges reliably in pretrained video representations, but its accessibility depends strongly on pretraining paradigm, representational depth, and readout mechanism.
匹配关键词: pretraining
---

[ACADEMIC - ARXIV]
标题: ReCoVLA: VLM-Guided Reward Compilation for Failure Recovery in Vision-Language-Action Policies
作者: Haodi Hu, Chung-Ta Huang, Jing Liu, Ye Wang, Kei Suzuki, Matthew Brand, Toshiaki Koike-Akino
链接: https://arxiv.org/abs/2606.09630v1
完整摘要: Vision-language-action (VLA) policies provide strong priors for language-conditioned manipulation, but remain brittle in off-nominal states requiring targeted recovery. We propose ReCoVLA -- a failure-conditioned residual recovery framework that keeps a pretrained VLA policy frozen, uses an external vision-language model (VLM) to infer the failure mode and recovery stage, and compiles a structured reward from task-relevant components. Rather than using the VLM to generate actions or rewards directly, ReCoVLA uses it as a semantic reward selector: it predicts a recovery descriptor and reward mask for in-simulation residual-policy training, followed by zero-shot sim-to-real deployment of the trained recovery policies. This decouples high-level failure understanding from low-level corrective control to support different VLAs. Experiments across short-horizon, long-horizon, and contact-rich manipulation tasks show that ReCoVLA outperforms the tested baselines on average. In simulation, our reward compiler improves average success from 36.7% for the fine-tuned $π_{0.5}$ baseline to 66.7%. In physical zero-shot sim-to-real experiments, ReCoVLA achieves the best average performance, with 61.7% success.
匹配关键词: pretraining
---

[ACADEMIC - ARXIV]
标题: SoccerNet 2026 Player-Centric Ball-Action Spotting:Retraining and Post-Processing Extensions to the FOOTPASS Baselines
作者: Parthsarthi Rawat
链接: https://arxiv.org/abs/2606.09679v1
完整摘要: We describe our system for the SoccerNet 2026 Player-Centric Ball-Action Spotting Challenge, which requires predicting who performs which action and when, across eight classes in broadcast soccer. Building on the three FOOTPASS baselines [1] (TAAD, TAAD+GNN, and TAAD+DST), we contribute four extensions: (1) gradient check pointing to enable full-backbone fine-tuning on a single GPU; (2) fusion of GNN logits into the DST encoder, combining graph-based tactical context with per-player visual features; (3) square-root frequency class weighting to address the 213:1 pass-to-tackle imbalance in the training data; and (4) a post processing pipeline comprising per-class logit gating, temporal frame refinement, jersey re-assignment, and a two-model ensemble. Our system achieves 0.548 Macro F1 on the test set and 0.446 on the challenge set (server evaluation).
匹配关键词: foundation model
---

[ACADEMIC - ARXIV]
标题: MeCo: One-Step MeanFlow-based Corrector for Multi-Channel Speech Separation
作者: Dohwan Kim, Jung-Woo Choi
链接: https://arxiv.org/abs/2606.09677v1
完整摘要: While discriminative models for multi-channel speech separation excel in reference-based metrics, they often exhibit suboptimal human listening quality. To address this, we propose a novel MeanFlow-based one-step generative corrector (MeCo). MeCo learns a conditional average velocity field to map discriminative estimates directly onto the clean speech manifold in a single step. To maximize one-step generation performance, we introduce Data-Space Optimization (DSO). DSO integrates an $\mathbf{x}_r$-loss, which penalizes prediction errors on longer displacement intervals to serve as a generative objective for human listening quality, with an Endpoint SI-SDR loss that directly optimizes terminal signal fidelity. Experiments demonstrate that MeCo achieves state-of-the-art (SOTA) performance with minimal computational overhead, simultaneously achieving superior signal fidelity and human listening quality in both in-domain and out-of-domain scenarios.
匹配关键词: foundation model
---

[ACADEMIC - ARXIV]
标题: Correlation Is Not Enough: Embedding Human Metadata for Individual Causal Discovery
作者: Suraj Biswas, Saurabh Gupta, Pritam Mukherjee
链接: https://arxiv.org/abs/2606.09672v1
完整摘要: Ask a pretrained biomedical language model whether "cortisol 28 ug/dL" and "stock-market volatility" are related, and it returns a cosine similarity of 0.83 on a scale where 1.0 means identical. The two share no mechanism. This is not a corner case: every off-the-shelf biomedical encoder we tested (BioBERT, PubMedBERT, BioM-ELECTRA) scores unrelated cross-domain pairs between 0.76 and 0.92 when the answer should be near zero. Accuracy on cross-domain discrimination is 0%. Retrieval systems survive this, because a language model downstream filters the noise. A Large Behavioural Model (LBM), a foundation model whose subject is a person rather than a sentence, does not: it reasons over a graph of a user's life and treats embedding proximity as evidence that two events are causally linked. False proximity writes a false causal edge, and everything downstream inherits the error. Here, embedding geometry is not a tuning knob; it is correctness. We report the fix. A contrastive pass over 72,034 pairs raises PubMedBERT BIOSSES correlation from 0.633 to 0.828 and within-vs-across-domain separation from 1.05x to 1.63x. A second pass, BODHI, mines hard negatives from edges absent in a biomedical knowledge graph and lifts separation to 2.30x and the discrimination gap to +0.392, at a 4.5% BIOSSES cost. On an Intel Xeon 6737P with AMX, OpenVINO cuts single-query latency from 1367 ms to 10 ms (133x) and reaches 555 sentences/sec. One finding contradicts standard advice: FP16 beats INT8 on this silicon at every serving batch size, and we explain why. The same model on a no-AMX Ice Lake instance runs 13-27x slower. We release the benchmark suite, training corpora, the BODHI generator, and the OpenVINO scripts.
匹配关键词: foundation model
---

[ACADEMIC - ARXIV]
标题: Transition-Based Digital Twin Modelling for Alzheimer's Disease under Sparse Longitudinal Data
作者: Yinyu Huang, Yilin Zhang, Sofia Michopoulou, Christopher Kipps, Rahman Attar
链接: https://arxiv.org/abs/2606.09671v1
完整摘要: Alzheimer's disease (AD) progression is highly heterogeneous and is typically observed through sparse and irregular longitudinal data, posing challenges for prediction and personalised monitoring. Existing machine learning approaches have improved AD prediction using multimodal data, yet often focus on static classification or cohort-level risk estimation, providing limited support for subject-specific modelling and uncertainty-aware reasoning. To address these limitations, we present a personalised digital twin framework for AD prediction and scenario-based analysis using multimodal longitudinal data. The proposed approach integrates complementary modelling strategies to capture clinical transitions and temporal dependencies across visits. Using data from the Alzheimer's Disease Neuroimaging Initiative (ADNI), including cognitive assessments, clinical variables, and MRI-derived phenotypes, the framework predicts cognitive status and diagnostic categories while quantifying predictive uncertainty and enabling patient-specific what-if trajectory analysis. Evaluation on leak-free subject-level splits demonstrates strong performance in score forecasting and diagnosis classification. In this sparse and irregular ADNI setting, transition-based modelling of adjacent visits achieved higher predictive accuracy than the sequence-based branch, suggesting that local transition modelling may be more data-efficient. While sequence models remain valuable for uncertainty-aware trajectory forecasting, local transition modelling offers a more data-efficient and robust predictive strategy. These findings highlight the importance of aligning temporal modelling strategies with clinical data structure and suggest that transition-based digital twin formulations may provide a practical and interpretable approach for personalised disease forecasting in neurodegenerative disorders.
匹配关键词: foundation model
---

[ACADEMIC - ARXIV]
标题: Visual Prompting Meets Feature Reconstruction-Based Anomaly Detection with Dual-Teacher Supervision
作者: Mateo Diaz-Bone, Daniel Caraballo, Florian Scheidegger, Thomas Frick, Mattia Rigotti, Andrea Bartezzaghi, Roy Assaf, Niccolo Avogaro, Yagmur G. Cinar, Brown Ebouky, Filip M. Janicki, Piotr S. Kluska, Cezary Skura, Cristiano Malossi
链接: https://arxiv.org/abs/2606.09670v1
完整摘要: Recent Anomaly Detection methods achieve perfect detection and segmentation scores on well-established datasets, such as MVTec. However, many of these methods face challenges when foundational assumptions - such as consistent object scale, viewpoint, background, illumination, and centered placement - are violated. Those variations that occur render anomaly detection methods unusable in many real-world scenarios. To address these limitations, we introduce three key contributions: (1) a visual prompting pipeline that isolates objects using foreground-background masking; (2) a mechanism for unfreezing the teacher in student-teacher models to improve domain adaptability; and (3) a data augmentation strategy leveraging diffusion-generated synthetic images to enhance anomaly detection performance. We achieve a 3.5 percentage point improvement over the previous state-of-the-art on the challenging AeBAD dataset by using the Masked Multiscale Reconstruction (MMR) model as our backbone.
匹配关键词: foundation model
---

[ACADEMIC - ARXIV]
标题: Correlation Is Not Enough: Embedding Human Metadata for Individual Causal Discovery
作者: Suraj Biswas, Saurabh Gupta, Pritam Mukherjee
链接: https://arxiv.org/abs/2606.09672v1
完整摘要: Ask a pretrained biomedical language model whether "cortisol 28 ug/dL" and "stock-market volatility" are related, and it returns a cosine similarity of 0.83 on a scale where 1.0 means identical. The two share no mechanism. This is not a corner case: every off-the-shelf biomedical encoder we tested (BioBERT, PubMedBERT, BioM-ELECTRA) scores unrelated cross-domain pairs between 0.76 and 0.92 when the answer should be near zero. Accuracy on cross-domain discrimination is 0%. Retrieval systems survive this, because a language model downstream filters the noise. A Large Behavioural Model (LBM), a foundation model whose subject is a person rather than a sentence, does not: it reasons over a graph of a user's life and treats embedding proximity as evidence that two events are causally linked. False proximity writes a false causal edge, and everything downstream inherits the error. Here, embedding geometry is not a tuning knob; it is correctness. We report the fix. A contrastive pass over 72,034 pairs raises PubMedBERT BIOSSES correlation from 0.633 to 0.828 and within-vs-across-domain separation from 1.05x to 1.63x. A second pass, BODHI, mines hard negatives from edges absent in a biomedical knowledge graph and lifts separation to 2.30x and the discrimination gap to +0.392, at a 4.5% BIOSSES cost. On an Intel Xeon 6737P with AMX, OpenVINO cuts single-query latency from 1367 ms to 10 ms (133x) and reaches 555 sentences/sec. One finding contradicts standard advice: FP16 beats INT8 on this silicon at every serving batch size, and we explain why. The same model on a no-AMX Ice Lake instance runs 13-27x slower. We release the benchmark suite, training corpora, the BODHI generator, and the OpenVINO scripts.
匹配关键词: scaling law
---

[ACADEMIC - ARXIV]
标题: Visual Prompting Meets Feature Reconstruction-Based Anomaly Detection with Dual-Teacher Supervision
作者: Mateo Diaz-Bone, Daniel Caraballo, Florian Scheidegger, Thomas Frick, Mattia Rigotti, Andrea Bartezzaghi, Roy Assaf, Niccolo Avogaro, Yagmur G. Cinar, Brown Ebouky, Filip M. Janicki, Piotr S. Kluska, Cezary Skura, Cristiano Malossi
链接: https://arxiv.org/abs/2606.09670v1
完整摘要: Recent Anomaly Detection methods achieve perfect detection and segmentation scores on well-established datasets, such as MVTec. However, many of these methods face challenges when foundational assumptions - such as consistent object scale, viewpoint, background, illumination, and centered placement - are violated. Those variations that occur render anomaly detection methods unusable in many real-world scenarios. To address these limitations, we introduce three key contributions: (1) a visual prompting pipeline that isolates objects using foreground-background masking; (2) a mechanism for unfreezing the teacher in student-teacher models to improve domain adaptability; and (3) a data augmentation strategy leveraging diffusion-generated synthetic images to enhance anomaly detection performance. We achieve a 3.5 percentage point improvement over the previous state-of-the-art on the challenging AeBAD dataset by using the Masked Multiscale Reconstruction (MMR) model as our backbone.
匹配关键词: scaling law
---

[ACADEMIC - ARXIV]
标题: End-to-End Context Compression at Scale
作者: Ang Li, Sean McLeish, Haozhe Chen, Nimit Kalra, Zaiqian Chen, Artem Gazizov, Venkata Anoop Suhas Kumar Morisetty, Bhavya Kailkhura, Harshitha Menon, Zhuang Liu, Brian R. Bartoldson, Tom Goldstein, Sanae Lotfi, Micah Goldblum, Pavel Izmailov
链接: https://arxiv.org/abs/2606.09659v1
完整摘要: Long-context language model inference is bottlenecked by memory, as the KV cache grows with context length. Recent techniques to compress the KV cache fall short: they either degrade model quality substantially or require considerable time and compute to compress a single long prompt. Furthermore, many methods require the input to fit within the target model's context window, and are generally incompatible with modern production inference engines. Encoder-decoder compressors, which map a long token sequence to a shorter sequence of latent embeddings consumed by a decoder, are an appealing alternative in principle. However, existing approaches are not competitive with KV cache compression on the accuracy-efficiency frontier. In this work, we revisit encoder-decoder compression and close this gap. We first perform an architecture search, pre-training many variants from scratch to determine how best to design and train encoder-decoder compressors. Guided by our findings, we continually pre-train a family of 0.6B-encoder, 4B-decoder models on over 350B tokens each, at compression ratios of 1:4, 1:8, and 1:16. We introduce Latent Context Language Models (LCLMs), a family of compressors that improve the Pareto frontier across general-task performance, compression speed, and peak memory usage. We demonstrate that LCLMs serve as efficient backbones for long-horizon agents, letting the agent skim through a compressed long context and adaptively expand relevant segments on demand.
匹配关键词: scaling law
---

[ACADEMIC - ARXIV]
标题: Beyond Accuracy: Community Perspectives on Machine Translation
作者: Yujun Wang, Ehud Reiter, Shimei Pan, Steffen Eger, Wei Zhao
链接: https://arxiv.org/abs/2606.09655v1
完整摘要: Despite remarkable progress in machine translation (MT), non-AI communities have raised growing concerns about MT systems, suggesting a noticeable gap between technical advancement and the needs of real-world users. For instance, while NLP researchers focus on benchmark performance, end users care about ethical concerns, trust, reliability, costs, and more. We argue that listening to various user communities is essential so that research efforts would be directed towards the problems that the communities care about. To this end, we present a large-scale analysis, for the first time, that investigates what four stakeholder communities (AI developers, professional translators, language learners, and language service providers) post about MT technology on social media. To do so, we construct a dataset of 79,286 posts and comments from Reddit, Facebook, Bluesky, and Mastodon from 2019 to 2025, and analyse where these communities disagree, and how and why. Overall, we find that communities often disagree, and even show strong conflicts due to polarised sentiments on topics such as translation quality, efficiency, and reliability. This is because these communities approach these topics differently: the AI community frames them as technical and computational problems, while non-AI (user) communities care more about quality nuances, time savings, user trust, and broader social issues.
匹配关键词: scaling law
---

[ACADEMIC - ARXIV]
标题: ArtiFact: A Large-Scale Multi-Modal Cultural Heritage Dataset
作者: Luciano Duarte, Olga Ovcharenko, Sebastian Schelter
链接: https://arxiv.org/abs/2606.09648v1
完整摘要: Multi-modal data management has emerged as a central research topic in the database community, spanning data integration, semantic query processing, and data quality assessment. Despite this growing interest, the community lacks large-scale, real-world datasets combining tables, text, and images. We present ArtiFact, a multi-modal cultural heritage dataset of 651045 museum records collected from the Metropolitan Museum of Art, the Art Institute of Chicago, and the Rijksmuseum. We demonstrate the utility of ArtiFact through two downstream tasks. For cross-modal error detection, we introduce a curated taxonomy of seven error categories injected into 130209 records and show that reliably detecting subtle domain-specific errors such as material anachronisms and temporal shifts remain an open challenge. For semantic query processing, we show that current systems struggle with queries involving cultural proximity, ambiguous object types, and historically contingent terminology. Our results position ArtiFact as a challenging benchmark for multi-modal data management research.
匹配关键词: scaling law
---

[ACADEMIC - ARXIV]
标题: SoccerNet 2026 Player-Centric Ball-Action Spotting:Retraining and Post-Processing Extensions to the FOOTPASS Baselines
作者: Parthsarthi Rawat
链接: https://arxiv.org/abs/2606.09679v1
完整摘要: We describe our system for the SoccerNet 2026 Player-Centric Ball-Action Spotting Challenge, which requires predicting who performs which action and when, across eight classes in broadcast soccer. Building on the three FOOTPASS baselines [1] (TAAD, TAAD+GNN, and TAAD+DST), we contribute four extensions: (1) gradient check pointing to enable full-backbone fine-tuning on a single GPU; (2) fusion of GNN logits into the DST encoder, combining graph-based tactical context with per-player visual features; (3) square-root frequency class weighting to address the 213:1 pass-to-tackle imbalance in the training data; and (4) a post processing pipeline comprising per-class logit gating, temporal frame refinement, jersey re-assignment, and a two-model ensemble. Our system achieves 0.548 Macro F1 on the test set and 0.446 on the challenge set (server evaluation).
匹配关键词: language model
---

[ACADEMIC - ARXIV]
标题: MeCo: One-Step MeanFlow-based Corrector for Multi-Channel Speech Separation
作者: Dohwan Kim, Jung-Woo Choi
链接: https://arxiv.org/abs/2606.09677v1
完整摘要: While discriminative models for multi-channel speech separation excel in reference-based metrics, they often exhibit suboptimal human listening quality. To address this, we propose a novel MeanFlow-based one-step generative corrector (MeCo). MeCo learns a conditional average velocity field to map discriminative estimates directly onto the clean speech manifold in a single step. To maximize one-step generation performance, we introduce Data-Space Optimization (DSO). DSO integrates an $\mathbf{x}_r$-loss, which penalizes prediction errors on longer displacement intervals to serve as a generative objective for human listening quality, with an Endpoint SI-SDR loss that directly optimizes terminal signal fidelity. Experiments demonstrate that MeCo achieves state-of-the-art (SOTA) performance with minimal computational overhead, simultaneously achieving superior signal fidelity and human listening quality in both in-domain and out-of-domain scenarios.
匹配关键词: language model
---

[ACADEMIC - ARXIV]
标题: (Auto)formalization is supposed to be easy: Trellis process semantics for spelling out rigorous proofs
作者: Wesley Pegden
链接: https://arxiv.org/abs/2606.09674v1
完整摘要: We present Trellis: an autoformalization system that leverages LLM agents in a deterministically constrained workflow to enforce incremental progress in Lean autoformalization tasks through iterative refinement of natural language proofs. Our approach is motivated by the common mathematician's notion of what it means to have a rigorous proof in the first place: namely, that it would be routine to elaborate any part of the proof in further detail. The result is a system which aims to achieve reliable autoformalization on a modest budget and with generalist agents, with specialization to autoformalization coming not from any task-specific agent training but instead from a meaning-of-rigor inspired workflow enforced by process semantics. We link to an end-to-end Lean formalization of a recent Ramsey theory breakthrough produced by the process.
匹配关键词: language model
---

[ACADEMIC - ARXIV]
标题: Correlation Is Not Enough: Embedding Human Metadata for Individual Causal Discovery
作者: Suraj Biswas, Saurabh Gupta, Pritam Mukherjee
链接: https://arxiv.org/abs/2606.09672v1
完整摘要: Ask a pretrained biomedical language model whether "cortisol 28 ug/dL" and "stock-market volatility" are related, and it returns a cosine similarity of 0.83 on a scale where 1.0 means identical. The two share no mechanism. This is not a corner case: every off-the-shelf biomedical encoder we tested (BioBERT, PubMedBERT, BioM-ELECTRA) scores unrelated cross-domain pairs between 0.76 and 0.92 when the answer should be near zero. Accuracy on cross-domain discrimination is 0%. Retrieval systems survive this, because a language model downstream filters the noise. A Large Behavioural Model (LBM), a foundation model whose subject is a person rather than a sentence, does not: it reasons over a graph of a user's life and treats embedding proximity as evidence that two events are causally linked. False proximity writes a false causal edge, and everything downstream inherits the error. Here, embedding geometry is not a tuning knob; it is correctness. We report the fix. A contrastive pass over 72,034 pairs raises PubMedBERT BIOSSES correlation from 0.633 to 0.828 and within-vs-across-domain separation from 1.05x to 1.63x. A second pass, BODHI, mines hard negatives from edges absent in a biomedical knowledge graph and lifts separation to 2.30x and the discrimination gap to +0.392, at a 4.5% BIOSSES cost. On an Intel Xeon 6737P with AMX, OpenVINO cuts single-query latency from 1367 ms to 10 ms (133x) and reaches 555 sentences/sec. One finding contradicts standard advice: FP16 beats INT8 on this silicon at every serving batch size, and we explain why. The same model on a no-AMX Ice Lake instance runs 13-27x slower. We release the benchmark suite, training corpora, the BODHI generator, and the OpenVINO scripts.
匹配关键词: language model
---

[ACADEMIC - ARXIV]
标题: Transition-Based Digital Twin Modelling for Alzheimer's Disease under Sparse Longitudinal Data
作者: Yinyu Huang, Yilin Zhang, Sofia Michopoulou, Christopher Kipps, Rahman Attar
链接: https://arxiv.org/abs/2606.09671v1
完整摘要: Alzheimer's disease (AD) progression is highly heterogeneous and is typically observed through sparse and irregular longitudinal data, posing challenges for prediction and personalised monitoring. Existing machine learning approaches have improved AD prediction using multimodal data, yet often focus on static classification or cohort-level risk estimation, providing limited support for subject-specific modelling and uncertainty-aware reasoning. To address these limitations, we present a personalised digital twin framework for AD prediction and scenario-based analysis using multimodal longitudinal data. The proposed approach integrates complementary modelling strategies to capture clinical transitions and temporal dependencies across visits. Using data from the Alzheimer's Disease Neuroimaging Initiative (ADNI), including cognitive assessments, clinical variables, and MRI-derived phenotypes, the framework predicts cognitive status and diagnostic categories while quantifying predictive uncertainty and enabling patient-specific what-if trajectory analysis. Evaluation on leak-free subject-level splits demonstrates strong performance in score forecasting and diagnosis classification. In this sparse and irregular ADNI setting, transition-based modelling of adjacent visits achieved higher predictive accuracy than the sequence-based branch, suggesting that local transition modelling may be more data-efficient. While sequence models remain valuable for uncertainty-aware trajectory forecasting, local transition modelling offers a more data-efficient and robust predictive strategy. These findings highlight the importance of aligning temporal modelling strategies with clinical data structure and suggest that transition-based digital twin formulations may provide a practical and interpretable approach for personalised disease forecasting in neurodegenerative disorders.
匹配关键词: language model
---

[ACADEMIC - ARXIV]
标题: DexPIE: Stable Dexterous Policy Improvement from Real-World Experience
作者: Ruizhe Liao, Wenrui Chen, Liangji Zeng, Haoran Lin, Fan Yang, Kailun Yang, Yaonan Wang
链接: https://arxiv.org/abs/2606.09615v1
完整摘要: Dexterous manipulation presents substantial challenges for imitation learning due to its high-dimensional action space and complex contact-rich dynamics. Policies trained purely from demonstrations often suffer from compounding errors during deployment and require large amounts of expert data to achieve reliable performance. To move beyond the limitations of demonstration data, in this work, we propose DexPIE, a post-training framework for dexterous policy improvement from experience collected through real-world deployment. First, DexPIE enables effective exploration coverage through a dexterous-hand-adapted intervention system and multi-stage DAgger-style data collection across initial and intermediate task stages, providing reliable supervision for accurate policy evaluation. To reduce temporal noise between post-training rollouts and demonstration data, we introduce asynchronous inference in the relative action space, which better aligns rollout data with demonstrated behavior and allows the critic to learn a value function induced by a more consistent underlying policy. Finally, DexPIE improves the policy through conditioning on a continuous optimality indicator, allowing the policy to leverage the quality of data in a more fine-grained manner. Across three challenging real-world dexterous manipulation tasks, DexPIE achieves a 37% improvement in success rate over the demonstration-based reference policy, outperforming all baseline methods and demonstrating stronger robustness. The source code and dataset will be made publicly available.
匹配关键词: mixture of experts
---

[ACADEMIC - ARXIV]
标题: Closure-Validated Circuit Discovery in Attention Heads: Co-activation Proposes, Ablation Disposes
作者: Yongzhong Xu
链接: https://arxiv.org/abs/2606.09607v1
完整摘要: Interpretability increasingly treats groups of components, not individual units, as the basic object, and proposes to find them by clustering co-activation statistics. We ask whether such a cheap signal actually identifies an attention-head circuit. Adapting a sparse-autoencoder clustering recipe to attention heads -- but validating by causal ablation rather than reconstruction -- we cluster heads and then run a closure test: ablate the discovered community and compare per-example damage to matched-random controls. Across two dense 1B-scale models (Pythia 1B, OLMo 1B) and two input distributions, the communities pass closure. In a Mixture-of-Experts model (OLMoE-1B-7B), route-conditional clustering recovers a statistically real signal that nonetheless does not survive closure -- ablation improves loss, the wrong direction. Extending closure across training, attention-target selectivity and participation ratio decouple from function in both directions. We conclude that a cheap signal is a circuit proposal, not a confirmed circuit; closure is what separates them.
匹配关键词: mixture of experts
---

[ACADEMIC - ARXIV]
标题: Automated IEP Generation from Traditional Chinese Parent-Teacher Interviews via Corpus-Grounded Feature Diffusion
作者: Kuanlin Chen, Cheng-En Ou
链接: https://arxiv.org/abs/2606.09603v1
完整摘要: Writing Individualized Education Programs (IEPs) is a high-labor, knowledge-intensive document burden; English-language research has demonstrated that generative AI can significantly reduce drafting time, yet automated IEP generation in Traditional Chinese remains virtually unexplored due to domain data scarcity, strict privacy regulations, and the absence of local evaluation benchmarks. We propose a low-resource fine-tuning pipeline centered on Corpus-Grounded Feature Diffusion (CGFD): (1) 25 dual-expert high-score seed transcripts are selected via a tau threshold with flag-aware score caps; (2) a FeatureProfile (sentence length, structure, quantification templates) is extracted from seeds and injected into LLM prompts alongside Verbalized-Sampling-style diversity control to drive diffusion; (3) 15 expert gold seeds are used as diffusion anchors, targeting 585 samples; 567 valid diffusion samples are obtained, yielding a 582-sample training set used to fine-tune Breeze-7B with QLoRA; (4) schema-constrained inference via Grammar-Constrained Decoding (GCD) enforces a hierarchical SMART Goal Ladder schema at inference time. Ablation results on a 55-sample schema stress set reveal an unexpected finding: GCD is counterproductive under Traditional Chinese token budgets -- the no-GCD path achieves 100% schema pass rate at 34% lower median latency, outperforming GCD on both reliability and speed. On the n=10 formal hold-out, the no-GCD inference path achieves BERTScore F1 = 0.779, exceeding GPT-5.4 (0.726), DeepSeek-V3.2 (0.703), Gemini-3-Flash-Preview (0.703), and Llama-4-Maverick (0.700) zero-shot baselines while maintaining fully local, air-gapped inference. This system addresses a gap in Traditional Chinese special-education NLP and offers a scalable, privacy-preserving local inference solution under an industrial engineering paradigm.
匹配关键词: mixture of experts
---

[ACADEMIC - ARXIV]
标题: Automating the Expert Eye: A System-Agnostic Deep Learning Framework for Rare Event Discovery in Imbalanced Force Spectroscopy
作者: Jorge Rodriguez-Ramos
链接: https://arxiv.org/abs/2606.09541v1
完整摘要: Single-Molecule Force Spectroscopy (SMFS) provides unprecedented insights into biomolecular mechanics, yet the high-throughput generation of force-extension trajectories creates a severe data curation bottleneck. Identifying rare molecular unbinding events within thousands of noise-dominated curves traditionally relies on tedious, non-scalable manual auditing. Here, we present a system-agnostic, interpretable deep learning framework tailored to overcome extreme class imbalance in automated SMFS triage. Utilizing 1D-to-2D rasterized geometric matrices, we deployed a modified ResNet18 architecture governed by an asymmetric Focal Loss objective function. We evaluated this framework on the complex mechanical unfolding pathways of the R. champanellensis cellulosome. Under hyper-imbalanced test conditions where the target interaction constituted only 1.34% of the dataset (13 true events out of 970 traces), the model achieved an overall accuracy of 0.9196 and a remarkable True Positive Rate (Recall) of 0.9231. By implementing an empirically calibrated dual-threshold triage system, the pipeline automatically discarded 880 unambiguous background noise traces , reducing the manual curation workload by over 90% while safely preserving high-value rare data. Finally, Gradient-weighted Class Activation Mapping (Grad-CAM) visually validated that the network's decisions are firmly anchored in the relevant geometric features of the force curves, specifically localizing on the structural unbinding regions, effectively mitigating 'black-box' skepticism. Built for free cloud-based execution, this open-source tool democratizes scalable, highly precise molecular discovery across the biophysics community.
匹配关键词: mixture of experts
---

[ACADEMIC - ARXIV]
标题: Self-Harness: Harnesses That Improve Themselves
作者: Hangfan Zhang, Shao Zhang, Kangcong Li, Chen Zhang, Yang Chen, Yiqun Zhang, Lei Bai, Shuyue Hu
链接: https://arxiv.org/abs/2606.09498v1
完整摘要: The performance of LLM-based agents is jointly shaped by their base models and the harnesses that mediate their interaction with the environment. Because different models exhibit distinct behaviors, effective harness design is inherently model-specific. Yet agent harnesses are still largely engineered by human experts, a paradigm that scales poorly as modern LLMs become increasingly diverse and rapidly evolving. In this paper, we introduce Self-Harness, a new paradigm in which an LLM-based agent improves its own operating harness, without relying on human engineers or stronger external agents. We operationalize Self-Harness as an iterative loop with three stages: Weakness Mining, which identifies model-specific failure patterns from execution traces; Harness Proposal, which generates diverse yet minimal harness modifications tied to these failures; and Proposal Validation, which accepts candidate edits only after regression testing. We instantiate Self-Harness on Terminal-Bench-2.0 using a minimal initial harness and three base models from diverse families: MiniMax M2.5, Qwen3.5-35B-A3B, and GLM-5. Across all three models, Self-Harness consistently improves performance, with held-out pass rates increasing from 40.5% to 61.9%, 23.8% to 38.1%, and 42.9% to 57.1%, respectively. Qualitative analyses further show that Self-Harness does not simply add generic instructions, but effectively turns model-specific weaknesses into concrete, executable harness changes. These results suggest a path toward LLM-based agents that are not merely shaped by their harnesses, but can also participate in reshaping them.
匹配关键词: mixture of experts
---

[ACADEMIC - ARXIV]
标题: End-to-End Context Compression at Scale
作者: Ang Li, Sean McLeish, Haozhe Chen, Nimit Kalra, Zaiqian Chen, Artem Gazizov, Venkata Anoop Suhas Kumar Morisetty, Bhavya Kailkhura, Harshitha Menon, Zhuang Liu, Brian R. Bartoldson, Tom Goldstein, Sanae Lotfi, Micah Goldblum, Pavel Izmailov
链接: https://arxiv.org/abs/2606.09659v1
完整摘要: Long-context language model inference is bottlenecked by memory, as the KV cache grows with context length. Recent techniques to compress the KV cache fall short: they either degrade model quality substantially or require considerable time and compute to compress a single long prompt. Furthermore, many methods require the input to fit within the target model's context window, and are generally incompatible with modern production inference engines. Encoder-decoder compressors, which map a long token sequence to a shorter sequence of latent embeddings consumed by a decoder, are an appealing alternative in principle. However, existing approaches are not competitive with KV cache compression on the accuracy-efficiency frontier. In this work, we revisit encoder-decoder compression and close this gap. We first perform an architecture search, pre-training many variants from scratch to determine how best to design and train encoder-decoder compressors. Guided by our findings, we continually pre-train a family of 0.6B-encoder, 4B-decoder models on over 350B tokens each, at compression ratios of 1:4, 1:8, and 1:16. We introduce Latent Context Language Models (LCLMs), a family of compressors that improve the Pareto frontier across general-task performance, compression speed, and peak memory usage. We demonstrate that LCLMs serve as efficient backbones for long-horizon agents, letting the agent skim through a compressed long context and adaptively expand relevant segments on demand.
匹配关键词: transformer architecture
---

[ACADEMIC - ARXIV]
标题: Muon Learns More Robust and Transferable Features than Adam
作者: Tianyu Ruan, Fengzhuo Zhang, Shuche Wang, Shihua Zhang
链接: https://arxiv.org/abs/2606.09658v1
完整摘要: Muon has recently emerged as a state-of-the-art optimizer for pretraining Large Language Models (LLMs) and vision classifiers. Despite its efficiency advantage over Adam and SGD, the feature-learning advantage of Muon remains unclear. This paper investigates Muon's feature-learning advantage through the lens of robustness and transferability. First, by evaluating pretrained models on corrupted images and texts, we show that features learned by Muon are consistently more robust than those learned by Adam and SGD across different architectures, including transformers and Convolutional Neural Networks (CNNs). Using trained layer-wise probes, we further show that this robustness advantage is reflected in larger logit margins across layers. Second, by training linear classifiers or fine-tuning full models from pretrained parameters on downstream tasks, we demonstrate that Muon-learned features transfer more effectively than those learned by Adam and SGD. This transferability advantage is further supported by the diversity of hidden states across layers, as measured by effective rank. Finally, in a representative classification problem with multi-component features, we prove that Muon attains larger margins and higher effective rank than Adam and SGD, providing theoretical support for our empirical findings.
匹配关键词: transformer architecture
---

[ACADEMIC - ARXIV]
标题: Powering the Future of AI: Navigating the Trade-offs for Europe's Energy Transition and Net-Zero Goals
作者: Mohammad Hemmati, Gbemi Oluleye, Vassilis M. Charitopoulos
链接: https://arxiv.org/abs/2606.09617v1
完整摘要: The rapid expansion of AI globally has led to the proliferation of energy-intensive hyperscale data centres (DCs), making them as a structurally challenging component in power system planning and operation. Using a spatially explicit optimisation model of Europe across 21 AI growth scenarios, we systematically quantify additional demand, capacity requirements, emissions, and operational impacts of DCs. Results indicate that AI could drive 73-723 TWh of extra demand by 2050, risking cumulative emissions overshoots of 67-181 MtCO2 between 2030 and 2050. Our analysis indicates that after 2030, the geography of AI infrastructure will be shaped more by firm power and system flexibility than by the mere abundance of clean energy. In moderate scenarios, AI requires an additional of 200 hours of firm generation, which increases LCOE by 35 EUR/MWh in key hubs. We show that even under the pessimistic scenarios, existing infrastructure would require 70 GW additional capacity, while under managed growth pathways, this expansion could reach 226 GW. We further find DCs workload dynamics strongly shape energy dispatch, system flexibility, and emissions, while improved efficiency significantly reduces capacity needs, and system peaks. While our findings suggest that net-zero targets for 2050 may be achieved, critical emission risks may appear in the intermediate years, and the EU may compromise its carbon-neutral goals unless policies adapt to this accelerating digital transformation.
匹配关键词: transformer architecture
---

[ACADEMIC - ARXIV]
标题: TUDSR: Twice Upsampling-Diffusion for Higher Super-Resolution
作者: Zhiqiang Wu, Yitong Dong, Xian Wei
链接: https://arxiv.org/abs/2606.09608v1
完整摘要: Diffusion-based generative models have achieved remarkable success in real-world image super-resolution (SR). With tiled diffusion techniques, these models can produce high-resolution images that exceed their native-supported resolution. However, the quality of such high-resolution (e.g $2048^2$) outputs often remains extremely poor, primarily due to two factors we consider: the image upsampling ratio (e.g $\times8$) exceeding the model's native-supported upsampling ratio (e.g $\times4$), and the model's native-supported resolution. In practice, training a native high-resolution model requires larger architectures, which incur significant computational overhead and GPU memory costs, making it hard on limited-resource equipment. Thus, we present TUDSR, a Twice Upsampling-Diffusion framework for higher SR. The TUDSR framework mainly consists of two stages: the first involves training at $R$-resolution, and the second introduces a looped chunk-based training strategy at $NR$-resolution. Each stage adapts a one-step GAN architecture comprising a generator and a discriminator. Based on SD2.1-base, we develop TUDSR-S, which achieves state-of-the-art performance across multiple benchmarks. Extensive experiments further demonstrate that TUDSR-S generates high-quality images at the resolutions of $1024^2$ and even $2048^2$, significantly outperforming existing approaches. Code is available at https://github.com/wuer5/TUDSR.
匹配关键词: transformer architecture
---

[ACADEMIC - ARXIV]
标题: Next-Token Prediction Learns Generalisable Representations of Sleep Physiology
作者: Jonathan F. Carter, Lionel Tarassenko
链接: https://arxiv.org/abs/2606.09605v1
完整摘要: Foundation models offer a promising route to compress multi-modal physiological signals into compact representations of human health, with broad applications across sleep medicine, cardiology, neurology and other healthcare domains. Existing models have typically been trained with masked-reconstruction or contrastive objectives. However, masked reconstruction may be poorly suited to the stochastic nature of these signals, while contrastive approaches rely on positive-pair definitions despite the semantic invariances of physiological signals being poorly understood. In this work, we show that next-token prediction is a simple and scalable alternative. We develop Hypnos, a multi-modal sleep foundation model trained using eight different sensing modalities (e.g. EEG, ECG, respiratory signals) drawn from over 20,000 overnight polysomnography recordings. We tokenize each modality into streams of discrete tokens using residual vector quantization, then train a large auto-regressive RQ-Transformer to jointly predict the next token across all modalities in parallel. After training, Hypnos can be applied to continuous streams of sensor data from any subset of supported modalities, generating embeddings for downstream tasks. Across a range of benchmarks, Hypnos significantly outperforms existing foundation models. In sleep stage classification, we match the performance of strong supervised baselines on held-out test sets whilst using \(100\times\) less labelled data. Hypnos even generalises to daytime physiology, surpassing a dedicated ECG foundation model at detecting atrial fibrillation. Our results demonstrate that next-token prediction is a strong self-supervised objective for representation learning from multi-modal physiological signals.
匹配关键词: transformer architecture
---

[ACADEMIC - ARXIV]
标题: SoccerNet 2026 Player-Centric Ball-Action Spotting:Retraining and Post-Processing Extensions to the FOOTPASS Baselines
作者: Parthsarthi Rawat
链接: https://arxiv.org/abs/2606.09679v1
完整摘要: We describe our system for the SoccerNet 2026 Player-Centric Ball-Action Spotting Challenge, which requires predicting who performs which action and when, across eight classes in broadcast soccer. Building on the three FOOTPASS baselines [1] (TAAD, TAAD+GNN, and TAAD+DST), we contribute four extensions: (1) gradient check pointing to enable full-backbone fine-tuning on a single GPU; (2) fusion of GNN logits into the DST encoder, combining graph-based tactical context with per-player visual features; (3) square-root frequency class weighting to address the 213:1 pass-to-tackle imbalance in the training data; and (4) a post processing pipeline comprising per-class logit gating, temporal frame refinement, jersey re-assignment, and a two-model ensemble. Our system achieves 0.548 Macro F1 on the test set and 0.446 on the challenge set (server evaluation).
匹配关键词: post-training
---

[ACADEMIC - ARXIV]
标题: DexPIE: Stable Dexterous Policy Improvement from Real-World Experience
作者: Ruizhe Liao, Wenrui Chen, Liangji Zeng, Haoran Lin, Fan Yang, Kailun Yang, Yaonan Wang
链接: https://arxiv.org/abs/2606.09615v1
完整摘要: Dexterous manipulation presents substantial challenges for imitation learning due to its high-dimensional action space and complex contact-rich dynamics. Policies trained purely from demonstrations often suffer from compounding errors during deployment and require large amounts of expert data to achieve reliable performance. To move beyond the limitations of demonstration data, in this work, we propose DexPIE, a post-training framework for dexterous policy improvement from experience collected through real-world deployment. First, DexPIE enables effective exploration coverage through a dexterous-hand-adapted intervention system and multi-stage DAgger-style data collection across initial and intermediate task stages, providing reliable supervision for accurate policy evaluation. To reduce temporal noise between post-training rollouts and demonstration data, we introduce asynchronous inference in the relative action space, which better aligns rollout data with demonstrated behavior and allows the critic to learn a value function induced by a more consistent underlying policy. Finally, DexPIE improves the policy through conditioning on a continuous optimality indicator, allowing the policy to leverage the quality of data in a more fine-grained manner. Across three challenging real-world dexterous manipulation tasks, DexPIE achieves a 37% improvement in success rate over the demonstration-based reference policy, outperforming all baseline methods and demonstrating stronger robustness. The source code and dataset will be made publicly available.
匹配关键词: post-training
---

[ACADEMIC - ARXIV]
标题: Assessing Sample Quality in Conditional Generation under Compositional Shift
作者: Berker Demirel, Valentino Maiorca, Marco Fumero, Theofanis Karaletsos, Francesco Locatello
链接: https://arxiv.org/abs/2606.09601v1
完整摘要: Conditional generators provide a natural tool for controllable generation, including settings where the desired condition is a new composition of observed attributes or experimental factors. In many applications, especially in scientific domains, such models are attractive to explore conditions for which real samples are rare, expensive, or not yet observed. However, this creates a circularity for evaluation: standard conditional quality metrics require a reference target distribution, but in the extrapolative regime that distribution is unavailable by definition. We address this problem with a post-hoc, per-sample trust score for assessing conditional samples using only the training distribution. The score combines two estimable quantities: global realism, measuring compatibility with the real data manifold, and attribute-wise faithfulness, measuring whether a sample is closer to the requested attributes than to plausible alternatives. We show that the score can recover meaningful comparisons across extrapolated generations, under a mild coverage condition on the observed attributes. These comparisons enable effective filtering, ranking, and abstention of generations and can be used directly on off-the-shelf pretrained models. In biological imaging, selected samples preserve real morphological structure better and improve downstream predictive performance, while similar gains are observed on controlled vision benchmarks. Finally, we show how the score can be applied during generation, enabling abstention before full decoding. Code is available at https://github.com/berkerdemirel/faithful-cond-gen.
匹配关键词: post-training
---

[ACADEMIC - ARXIV]
标题: Emergence of Context Characteristics Sensitivity in Large Language Models
作者: Nadya Yuki Wangsajaya, Haeun Yu, Isabelle Augenstein
链接: https://arxiv.org/abs/2606.09525v1
完整摘要: During instruction fine-tuning (IFT), large language models (LLMs) learn to follow instructions by using the provided context to answer a query. While prior work has studied how context characteristics correlate with context usage by the LLM, this analysis has been limited to inference time, leaving open how these relationships are acquired in the first place. Here, we measure how models' sensitivity to such characteristics shifts across successive IFT stages: supervised fine-tuning (SFT), direct preference optimization (DPO), and reinforcement learning with verifiable rewards (RLVR). Experiments across four models and three datasets show that SFT makes models more likely to use contexts that are easy to understand, such as containing high length, context-query similarity, and fluency. Post-SFT dynamics may either reinforce or resolve these preferences depending on the training dataset. Our findings reveal that context usage is actively reshaped at each IFT stage, and designing a balanced IFT dataset is important in ensuring robust context utilization of instruction-tuned models.
匹配关键词: post-training
---

[ACADEMIC - ARXIV]
标题: Emergent alignment and the projectability of ethical personas
作者: Guillermo Del Pinal, Youngchan Lee, Cameron McNamara, Alejandro Perez Carballo
链接: https://arxiv.org/abs/2606.09475v1
完整摘要: Work on `emergent misalignment' shows that finetuning LLMs on narrow tasks can induce broadly misaligned behavior. This supports the `persona selection' (PSM) hypothesis: during pre-training, LLMs learn to simulate different characters and perspectives, which can be elicited and refined during post-training. This paper investigates the converse phenomenon, `emergent alignment', and uses it to support and refine the PSM and motivate a novel desideratum for alignment. We finetune a helpful-only model on broad and narrow safety tasks. To create SFT samples, we follow the `Constitutional AI' (CAI) approach and use four constitutions which encode reasonable alignment strategies: deontology, consequentialism, virtue ethics, and aligning AIs as subordinate to human authority. For each of those models, we show that finetuning on two narrow safety sub-categories reliably induces emergent alignment over a representative set of general safety categories, and on safety subcategories that we directly filtered-out of the data sets used for narrow alignment. To test the `PSM' using a more fine-grained evaluation, we used a multidimensional `ethical persona' diagnostic. For each constitutionally finetuned (broad/narrow) model, we evaluate how well their behavior matches their expected signature profile. Our results show that our CAI models acquire their expected ``ethical persona'' -- e.g., the model narrowly fine-tuned on SFT samples created using the consequentialist constitution agrees significantly more with utilitarian than deontological beliefs. Yet our coarse and fine-grained evaluations show that there are significant differences across our (broad/narrow) finetuned CAI models in how well they project. We conclude that alignment strategies should be evaluated, not just on their (in-distribution) general safety performance, but also specifically on their degree of projectability.
匹配关键词: post-training
---

[ACADEMIC - ARXIV]
标题: SoccerNet 2026 Player-Centric Ball-Action Spotting:Retraining and Post-Processing Extensions to the FOOTPASS Baselines
作者: Parthsarthi Rawat
链接: https://arxiv.org/abs/2606.09679v1
完整摘要: We describe our system for the SoccerNet 2026 Player-Centric Ball-Action Spotting Challenge, which requires predicting who performs which action and when, across eight classes in broadcast soccer. Building on the three FOOTPASS baselines [1] (TAAD, TAAD+GNN, and TAAD+DST), we contribute four extensions: (1) gradient check pointing to enable full-backbone fine-tuning on a single GPU; (2) fusion of GNN logits into the DST encoder, combining graph-based tactical context with per-player visual features; (3) square-root frequency class weighting to address the 213:1 pass-to-tackle imbalance in the training data; and (4) a post processing pipeline comprising per-class logit gating, temporal frame refinement, jersey re-assignment, and a two-model ensemble. Our system achieves 0.548 Macro F1 on the test set and 0.446 on the challenge set (server evaluation).
匹配关键词: fine-tuning
---

[ACADEMIC - ARXIV]
标题: Muon Learns More Robust and Transferable Features than Adam
作者: Tianyu Ruan, Fengzhuo Zhang, Shuche Wang, Shihua Zhang
链接: https://arxiv.org/abs/2606.09658v1
完整摘要: Muon has recently emerged as a state-of-the-art optimizer for pretraining Large Language Models (LLMs) and vision classifiers. Despite its efficiency advantage over Adam and SGD, the feature-learning advantage of Muon remains unclear. This paper investigates Muon's feature-learning advantage through the lens of robustness and transferability. First, by evaluating pretrained models on corrupted images and texts, we show that features learned by Muon are consistently more robust than those learned by Adam and SGD across different architectures, including transformers and Convolutional Neural Networks (CNNs). Using trained layer-wise probes, we further show that this robustness advantage is reflected in larger logit margins across layers. Second, by training linear classifiers or fine-tuning full models from pretrained parameters on downstream tasks, we demonstrate that Muon-learned features transfer more effectively than those learned by Adam and SGD. This transferability advantage is further supported by the diversity of hidden states across layers, as measured by effective rank. Finally, in a representative classification problem with multi-component features, we prove that Muon attains larger margins and higher effective rank than Adam and SGD, providing theoretical support for our empirical findings.
匹配关键词: fine-tuning
---

[ACADEMIC - ARXIV]
标题: MAVIS: Multi-Agent Video Retrieval via Structured Video Understanding
作者: Jie Zhang, Qilang Ye, Hao Zhou, Haochen Liang, Fei Luo
链接: https://arxiv.org/abs/2606.09641v1
完整摘要: The dominant paradigm in video retrieval relies on embedding-based full-corpus scanning, which suffers from inherent computational inefficiency and the semantic asymmetry between information-dense videos and sparse textual queries. To bridge this gap, we introduce \textbf{MAVIS}, a novel multi-agent framework that rethinks retrieval as cooperative reasoning rather than brute-force search. MAVIS first bridges the granularity mismatch by parsing raw videos into a \textbf{Structured Semantic Library}, enabling explicit attribute-level indexing. During retrieval, a planner decomposes complex user intents into atomic sub-tasks, dispatching specialized agents to independently nominate candidates. Crucially, MAVIS employs a \textbf{Logic-aware Debate} mechanism with a strict veto protocol, where agents collaboratively prune logical mismatches to identify a compact set of ``controversial'' candidates for fine-grained verification. This agentic workflow effectively bypasses the inefficiency of full-library traversal. Extensive experiments on MSR-VTT, MSVD, and ActivityNet demonstrate that MAVIS achieves competitive performance without task-specific fine-tuning, offering a scalable and interpretable alternative to traditional dual-encoder approaches.
匹配关键词: fine-tuning
---

[ACADEMIC - ARXIV]
标题: ReCoVLA: VLM-Guided Reward Compilation for Failure Recovery in Vision-Language-Action Policies
作者: Haodi Hu, Chung-Ta Huang, Jing Liu, Ye Wang, Kei Suzuki, Matthew Brand, Toshiaki Koike-Akino
链接: https://arxiv.org/abs/2606.09630v1
完整摘要: Vision-language-action (VLA) policies provide strong priors for language-conditioned manipulation, but remain brittle in off-nominal states requiring targeted recovery. We propose ReCoVLA -- a failure-conditioned residual recovery framework that keeps a pretrained VLA policy frozen, uses an external vision-language model (VLM) to infer the failure mode and recovery stage, and compiles a structured reward from task-relevant components. Rather than using the VLM to generate actions or rewards directly, ReCoVLA uses it as a semantic reward selector: it predicts a recovery descriptor and reward mask for in-simulation residual-policy training, followed by zero-shot sim-to-real deployment of the trained recovery policies. This decouples high-level failure understanding from low-level corrective control to support different VLAs. Experiments across short-horizon, long-horizon, and contact-rich manipulation tasks show that ReCoVLA outperforms the tested baselines on average. In simulation, our reward compiler improves average success from 36.7% for the fine-tuned $π_{0.5}$ baseline to 66.7%. In physical zero-shot sim-to-real experiments, ReCoVLA achieves the best average performance, with 61.7% success.
匹配关键词: fine-tuning
---

[ACADEMIC - ARXIV]
标题: Automated IEP Generation from Traditional Chinese Parent-Teacher Interviews via Corpus-Grounded Feature Diffusion
作者: Kuanlin Chen, Cheng-En Ou
链接: https://arxiv.org/abs/2606.09603v1
完整摘要: Writing Individualized Education Programs (IEPs) is a high-labor, knowledge-intensive document burden; English-language research has demonstrated that generative AI can significantly reduce drafting time, yet automated IEP generation in Traditional Chinese remains virtually unexplored due to domain data scarcity, strict privacy regulations, and the absence of local evaluation benchmarks. We propose a low-resource fine-tuning pipeline centered on Corpus-Grounded Feature Diffusion (CGFD): (1) 25 dual-expert high-score seed transcripts are selected via a tau threshold with flag-aware score caps; (2) a FeatureProfile (sentence length, structure, quantification templates) is extracted from seeds and injected into LLM prompts alongside Verbalized-Sampling-style diversity control to drive diffusion; (3) 15 expert gold seeds are used as diffusion anchors, targeting 585 samples; 567 valid diffusion samples are obtained, yielding a 582-sample training set used to fine-tune Breeze-7B with QLoRA; (4) schema-constrained inference via Grammar-Constrained Decoding (GCD) enforces a hierarchical SMART Goal Ladder schema at inference time. Ablation results on a 55-sample schema stress set reveal an unexpected finding: GCD is counterproductive under Traditional Chinese token budgets -- the no-GCD path achieves 100% schema pass rate at 34% lower median latency, outperforming GCD on both reliability and speed. On the n=10 formal hold-out, the no-GCD inference path achieves BERTScore F1 = 0.779, exceeding GPT-5.4 (0.726), DeepSeek-V3.2 (0.703), Gemini-3-Flash-Preview (0.703), and Llama-4-Maverick (0.700) zero-shot baselines while maintaining fully local, air-gapped inference. This system addresses a gap in Traditional Chinese special-education NLP and offers a scalable, privacy-preserving local inference solution under an industrial engineering paradigm.
匹配关键词: fine-tuning
---

[ACADEMIC - ARXIV]
标题: Emergence of Context Characteristics Sensitivity in Large Language Models
作者: Nadya Yuki Wangsajaya, Haeun Yu, Isabelle Augenstein
链接: https://arxiv.org/abs/2606.09525v1
完整摘要: During instruction fine-tuning (IFT), large language models (LLMs) learn to follow instructions by using the provided context to answer a query. While prior work has studied how context characteristics correlate with context usage by the LLM, this analysis has been limited to inference time, leaving open how these relationships are acquired in the first place. Here, we measure how models' sensitivity to such characteristics shifts across successive IFT stages: supervised fine-tuning (SFT), direct preference optimization (DPO), and reinforcement learning with verifiable rewards (RLVR). Experiments across four models and three datasets show that SFT makes models more likely to use contexts that are easy to understand, such as containing high length, context-query similarity, and fluency. Post-SFT dynamics may either reinforce or resolve these preferences depending on the training dataset. Our findings reveal that context usage is actively reshaped at each IFT stage, and designing a balanced IFT dataset is important in ensuring robust context utilization of instruction-tuned models.
匹配关键词: SFT
---

[ACADEMIC - ARXIV]
标题: Emergent alignment and the projectability of ethical personas
作者: Guillermo Del Pinal, Youngchan Lee, Cameron McNamara, Alejandro Perez Carballo
链接: https://arxiv.org/abs/2606.09475v1
完整摘要: Work on `emergent misalignment' shows that finetuning LLMs on narrow tasks can induce broadly misaligned behavior. This supports the `persona selection' (PSM) hypothesis: during pre-training, LLMs learn to simulate different characters and perspectives, which can be elicited and refined during post-training. This paper investigates the converse phenomenon, `emergent alignment', and uses it to support and refine the PSM and motivate a novel desideratum for alignment. We finetune a helpful-only model on broad and narrow safety tasks. To create SFT samples, we follow the `Constitutional AI' (CAI) approach and use four constitutions which encode reasonable alignment strategies: deontology, consequentialism, virtue ethics, and aligning AIs as subordinate to human authority. For each of those models, we show that finetuning on two narrow safety sub-categories reliably induces emergent alignment over a representative set of general safety categories, and on safety subcategories that we directly filtered-out of the data sets used for narrow alignment. To test the `PSM' using a more fine-grained evaluation, we used a multidimensional `ethical persona' diagnostic. For each constitutionally finetuned (broad/narrow) model, we evaluate how well their behavior matches their expected signature profile. Our results show that our CAI models acquire their expected ``ethical persona'' -- e.g., the model narrowly fine-tuned on SFT samples created using the consequentialist constitution agrees significantly more with utilitarian than deontological beliefs. Yet our coarse and fine-grained evaluations show that there are significant differences across our (broad/narrow) finetuned CAI models in how well they project. We conclude that alignment strategies should be evaluated, not just on their (in-distribution) general safety performance, but also specifically on their degree of projectability.
匹配关键词: SFT
---

[ACADEMIC - ARXIV]
标题: Breaking the Tokenizer Barrier: On-Policy Distillation across Model Families
作者: Yifan Niu, Han Xiao, Dongyi Liu, Zelong Wang, Dihong Gong, Yasheng Wang, Jia Li
链接: https://arxiv.org/abs/2606.09456v1
完整摘要: On-Policy Distillation (OPD) has become a core technique in the post-training of Large Language Models (LLMs) for transferring knowledge from domain experts to student models. However, existing OPD distillation methods require teacher and student models to share the same tokenizer, restricting the applicability of OPD within the model series. Current mainstream practice typically employs Supervised Fine-Tuning (SFT) on teacher-generated responses for cross-tokenizer distillation, which fails to capture the rich knowledge embedded in the teacher's probability distribution. In this work, we enable the standard on-policy distillation method to operate across model families, ensuring that high-fidelity token-level signals can propagate across different tokenizers with a precise token-mapping algorithm. Extensive experiments show that cross-tokenizer OPD is significantly more compute-efficient than baselines on various benchmarks. Our results unlock a broader range of teacher-student pairs for OPD, opening up new avenues for adapting and enhancing interactions between LLMs.
匹配关键词: SFT
---

[ACADEMIC - ARXIV]
标题: AliyunConsoleAgent: Training Web Agents in Real-World Cloud Environments via Distillation and Reinforcement Learning
作者: Bojie Rong, Zheyu Shen, Qiaoping Wang, Pengfei Kang, Yang Xu, Yawen Wei, Hanyu Wu, Zhi Zhao, Leihao Pei, Linquan Jiang
链接: https://arxiv.org/abs/2606.09447v1
完整摘要: We present AliyunConsoleAgent, a web agent framework for automated documentation verification in real-world cloud consoles. Major cloud platforms encompass hundreds of products with rapid feature iteration, causing console UIs to frequently diverge from their corresponding documentation. Verifying that documented procedures accurately reflect the current console and can be executed end-to-end demands an estimated 4 million recurring inspections annually, yet manual coverage remains below 1%. While agent systems built on frontier proprietary models achieve high success rates, their prohibitive cost and data privacy constraints preclude large-scale deployment. We propose a two-stage training paradigm: supervised fine-tuning (SFT) on distilled frontier-model trajectories, followed by reinforcement learning using Group Relative Policy Optimization (GRPO) and a dual-channel outcome reward model in real cloud environments. To support large-scale RL training, we construct a high-determinism rollout system featuring Terraform-based resource pre-provisioning and LLM-driven on-demand provisioning, which effectively isolates environment noise from the training signal. We further introduce a rule-based reward evaluation protocol grounded in backend audit logs, providing objective, reward-hacking-resistant outcome judgment. Our model evolves from mechanical instruction following to autonomous decision-making with cloud console and product-specific understanding. Experiments on a challenging 278-task benchmark where the best frontier model achieves only 65.34% demonstrate that AliyunConsoleAgent-32B achieves a 63.52% mean success rate -- a 20.24 percentage-point improvement over the base model, narrowing the gap to the best frontier proprietary model to 1.82 pp (bootstrap 95% CI [-1.27, 7.39]) -- at 92% lower inference cost.
匹配关键词: SFT
---

[ACADEMIC - ARXIV]
标题: PriFT: Prior-Support Guided Supervised Fine-Tuning
作者: Ke Wang, Shuangqi Li, Mathieu Salzmann, Pascal Frossard
链接: https://arxiv.org/abs/2606.09396v1
完整摘要: Supervised fine-tuning (SFT) is an efficient approach for downstream task adaptation and often serves as the initialization stage for reinforcement learning (RL), but it can show weaker generalization than RL. A key limitation is its off-policy objective: SFT fits fixed demonstrations token by token, including targets poorly aligned with the model's pretrained distribution, which can lead to overfitting. A recent line of work addresses this issue by assigning larger training weights to tokens better aligned with the current model's predictive distribution, with the intuition that fitting these tokens are less distortive to the model's pretrained knowledge and representations. However, computing the token weights from the model that is currently fine-tuned entangles token weights with the optimization trajectory, inducing a self-reinforcing dynamics as the distribution rapidly departs from the pretrained model. To address this, we propose PriFT (Prior-support guided Fine-Tuning), which derives token weights from a frozen pretrained reference to obtain a stable reweighting signal unaffected by fine-tuning. This signal estimates prior support: the extent to which each target token is supported by the pretrained distribution. Across multiple existing token-reweighting rules, replacing the reweighting signal from the online model to pretrained model consistently improves performance. We introduce two instantiations: PriFT-prob uses pretrained token probability, while PriFT-mass selects tokens by cumulative probability mass under the pretrained distribution. Extensive experiments on mathematical reasoning, code generation, and medical question answering show that PriFT achieves state-of-the-art results among SFT baselines and provides a better initialization for subsequent RL training.
匹配关键词: SFT
---

[ACADEMIC - ARXIV]
标题: SoccerNet 2026 Player-Centric Ball-Action Spotting:Retraining and Post-Processing Extensions to the FOOTPASS Baselines
作者: Parthsarthi Rawat
链接: https://arxiv.org/abs/2606.09679v1
完整摘要: We describe our system for the SoccerNet 2026 Player-Centric Ball-Action Spotting Challenge, which requires predicting who performs which action and when, across eight classes in broadcast soccer. Building on the three FOOTPASS baselines [1] (TAAD, TAAD+GNN, and TAAD+DST), we contribute four extensions: (1) gradient check pointing to enable full-backbone fine-tuning on a single GPU; (2) fusion of GNN logits into the DST encoder, combining graph-based tactical context with per-player visual features; (3) square-root frequency class weighting to address the 213:1 pass-to-tackle imbalance in the training data; and (4) a post processing pipeline comprising per-class logit gating, temporal frame refinement, jersey re-assignment, and a two-model ensemble. Our system achieves 0.548 Macro F1 on the test set and 0.446 on the challenge set (server evaluation).
匹配关键词: instruction tuning
---

[ACADEMIC - ARXIV]
标题: Correlation Is Not Enough: Embedding Human Metadata for Individual Causal Discovery
作者: Suraj Biswas, Saurabh Gupta, Pritam Mukherjee
链接: https://arxiv.org/abs/2606.09672v1
完整摘要: Ask a pretrained biomedical language model whether "cortisol 28 ug/dL" and "stock-market volatility" are related, and it returns a cosine similarity of 0.83 on a scale where 1.0 means identical. The two share no mechanism. This is not a corner case: every off-the-shelf biomedical encoder we tested (BioBERT, PubMedBERT, BioM-ELECTRA) scores unrelated cross-domain pairs between 0.76 and 0.92 when the answer should be near zero. Accuracy on cross-domain discrimination is 0%. Retrieval systems survive this, because a language model downstream filters the noise. A Large Behavioural Model (LBM), a foundation model whose subject is a person rather than a sentence, does not: it reasons over a graph of a user's life and treats embedding proximity as evidence that two events are causally linked. False proximity writes a false causal edge, and everything downstream inherits the error. Here, embedding geometry is not a tuning knob; it is correctness. We report the fix. A contrastive pass over 72,034 pairs raises PubMedBERT BIOSSES correlation from 0.633 to 0.828 and within-vs-across-domain separation from 1.05x to 1.63x. A second pass, BODHI, mines hard negatives from edges absent in a biomedical knowledge graph and lifts separation to 2.30x and the discrimination gap to +0.392, at a 4.5% BIOSSES cost. On an Intel Xeon 6737P with AMX, OpenVINO cuts single-query latency from 1367 ms to 10 ms (133x) and reaches 555 sentences/sec. One finding contradicts standard advice: FP16 beats INT8 on this silicon at every serving batch size, and we explain why. The same model on a no-AMX Ice Lake instance runs 13-27x slower. We release the benchmark suite, training corpora, the BODHI generator, and the OpenVINO scripts.
匹配关键词: instruction tuning
---

[ACADEMIC - ARXIV]
标题: When Built-in Thinking Helps and Hurts: Constraint-Level Error Shifts in Instruction Following
作者: Sai Adith Senthil Kumar
链接: https://arxiv.org/abs/2606.09662v1
完整摘要: Large reasoning models (LRMs) often improve math and coding performance, but their effect on instruction following is unclear. We study IFEval with Qwen3 models (1.7B-32B), using same-weights Thinking ON/OFF controls; four Hunyuan models provide directional cross-family support. Aggregate pass-rate changes are small (-0.55 to -3.52 pp), yet 10-20% of prompts switch between pass and fail across modes, suggesting that thinking changes the pattern of errors--some prompts improve while others worsen--rather than uniformly degrading performance. Under a post-hoc Qwen3-derived grouping, constraint types separate into Planning (global counting, structure, coordination), which improves at the class level under thinking, and Precision (exact local form), which consistently worsens; the class-level Planning/Precision sign pattern holds directionally for all four Hunyuan models despite Hunyuan's opposite aggregate direction. Thinking also changes final-answer length; matched-length analyses substantially reduce the Precision drop, but a residual penalty remains. Analyzing thinking traces with a cross-encoder relevance metric reveals three patterns: Neutral shows a positive relevance-compliance link (r approximately 0.15); Planning shows near-zero predictive correlation (r approximately 0.02) despite measurable trace engagement, consistent with an execution gap between CE-measured trace relevance and final-answer compliance; Precision shows a small negative correlation (r approximately -0.05), with failing instances having higher mean relevance than passing ones. Activation patching across four model sizes (1.7B-14B) shows that Precision flip instances are more often restored than Planning flip instances (32-58% vs. 14-40% mean layer-restoration), with the largest gap at 14B (about 30 pp).
匹配关键词: instruction tuning
---

[ACADEMIC - ARXIV]
标题: Muon Learns More Robust and Transferable Features than Adam
作者: Tianyu Ruan, Fengzhuo Zhang, Shuche Wang, Shihua Zhang
链接: https://arxiv.org/abs/2606.09658v1
完整摘要: Muon has recently emerged as a state-of-the-art optimizer for pretraining Large Language Models (LLMs) and vision classifiers. Despite its efficiency advantage over Adam and SGD, the feature-learning advantage of Muon remains unclear. This paper investigates Muon's feature-learning advantage through the lens of robustness and transferability. First, by evaluating pretrained models on corrupted images and texts, we show that features learned by Muon are consistently more robust than those learned by Adam and SGD across different architectures, including transformers and Convolutional Neural Networks (CNNs). Using trained layer-wise probes, we further show that this robustness advantage is reflected in larger logit margins across layers. Second, by training linear classifiers or fine-tuning full models from pretrained parameters on downstream tasks, we demonstrate that Muon-learned features transfer more effectively than those learned by Adam and SGD. This transferability advantage is further supported by the diversity of hidden states across layers, as measured by effective rank. Finally, in a representative classification problem with multi-component features, we prove that Muon attains larger margins and higher effective rank than Adam and SGD, providing theoretical support for our empirical findings.
匹配关键词: instruction tuning
---

[ACADEMIC - ARXIV]
标题: MAVIS: Multi-Agent Video Retrieval via Structured Video Understanding
作者: Jie Zhang, Qilang Ye, Hao Zhou, Haochen Liang, Fei Luo
链接: https://arxiv.org/abs/2606.09641v1
完整摘要: The dominant paradigm in video retrieval relies on embedding-based full-corpus scanning, which suffers from inherent computational inefficiency and the semantic asymmetry between information-dense videos and sparse textual queries. To bridge this gap, we introduce \textbf{MAVIS}, a novel multi-agent framework that rethinks retrieval as cooperative reasoning rather than brute-force search. MAVIS first bridges the granularity mismatch by parsing raw videos into a \textbf{Structured Semantic Library}, enabling explicit attribute-level indexing. During retrieval, a planner decomposes complex user intents into atomic sub-tasks, dispatching specialized agents to independently nominate candidates. Crucially, MAVIS employs a \textbf{Logic-aware Debate} mechanism with a strict veto protocol, where agents collaboratively prune logical mismatches to identify a compact set of ``controversial'' candidates for fine-grained verification. This agentic workflow effectively bypasses the inefficiency of full-library traversal. Extensive experiments on MSR-VTT, MSVD, and ActivityNet demonstrate that MAVIS achieves competitive performance without task-specific fine-tuning, offering a scalable and interpretable alternative to traditional dual-encoder approaches.
匹配关键词: instruction tuning
---

[ACADEMIC - ARXIV]
标题: Transition-Based Digital Twin Modelling for Alzheimer's Disease under Sparse Longitudinal Data
作者: Yinyu Huang, Yilin Zhang, Sofia Michopoulou, Christopher Kipps, Rahman Attar
链接: https://arxiv.org/abs/2606.09671v1
完整摘要: Alzheimer's disease (AD) progression is highly heterogeneous and is typically observed through sparse and irregular longitudinal data, posing challenges for prediction and personalised monitoring. Existing machine learning approaches have improved AD prediction using multimodal data, yet often focus on static classification or cohort-level risk estimation, providing limited support for subject-specific modelling and uncertainty-aware reasoning. To address these limitations, we present a personalised digital twin framework for AD prediction and scenario-based analysis using multimodal longitudinal data. The proposed approach integrates complementary modelling strategies to capture clinical transitions and temporal dependencies across visits. Using data from the Alzheimer's Disease Neuroimaging Initiative (ADNI), including cognitive assessments, clinical variables, and MRI-derived phenotypes, the framework predicts cognitive status and diagnostic categories while quantifying predictive uncertainty and enabling patient-specific what-if trajectory analysis. Evaluation on leak-free subject-level splits demonstrates strong performance in score forecasting and diagnosis classification. In this sparse and irregular ADNI setting, transition-based modelling of adjacent visits achieved higher predictive accuracy than the sequence-based branch, suggesting that local transition modelling may be more data-efficient. While sequence models remain valuable for uncertainty-aware trajectory forecasting, local transition modelling offers a more data-efficient and robust predictive strategy. These findings highlight the importance of aligning temporal modelling strategies with clinical data structure and suggest that transition-based digital twin formulations may provide a practical and interpretable approach for personalised disease forecasting in neurodegenerative disorders.
匹配关键词: AI scientist
---

[ACADEMIC - ARXIV]
标题: From 0-to-1 to 1-to-N: Reproducible Engineering Evidence for MetaAI Recursive Self-Design
作者: Dun Li, Jiatao Li, Hongzhi Li
链接: https://arxiv.org/abs/2606.09663v1
完整摘要: Recursive self-design refers to AI-assisted modification of the mechanisms by which an AI system is built, evaluated, and improved. This paper treats MetaAI not as a mature paradigm, but as a working term for a human-seeded, AI-expanded development pattern in which the design space itself becomes a target of modification. We propose an operational evidence framework with four criteria: inspectable target system, meta-level modifier, feedback-directed selection, and recursive continuation. We then map public systems, including Darwin Goedel Machine (DGM), STOP, Goedel Agent, and ShinkaEvolve, against these criteria. DGM provides the most direct currently reported evidence: its published results show improvement from 20% to 50% on SWE-bench Verified and from 14.2% to 30.7% on full Polyglot after 80 iterations, with ablations suggesting that both open-ended exploration and self-improvement contribute. Finally, we provide MetaAI-Mini, a reproducible HumanEval-based protocol and codebase. Because no completed model run is included in this build, MetaAI-Mini is reported as a protocol rather than as an experimental result.
匹配关键词: AI scientist
---

[ACADEMIC - ARXIV]
标题: Beyond Accuracy: Community Perspectives on Machine Translation
作者: Yujun Wang, Ehud Reiter, Shimei Pan, Steffen Eger, Wei Zhao
链接: https://arxiv.org/abs/2606.09655v1
完整摘要: Despite remarkable progress in machine translation (MT), non-AI communities have raised growing concerns about MT systems, suggesting a noticeable gap between technical advancement and the needs of real-world users. For instance, while NLP researchers focus on benchmark performance, end users care about ethical concerns, trust, reliability, costs, and more. We argue that listening to various user communities is essential so that research efforts would be directed towards the problems that the communities care about. To this end, we present a large-scale analysis, for the first time, that investigates what four stakeholder communities (AI developers, professional translators, language learners, and language service providers) post about MT technology on social media. To do so, we construct a dataset of 79,286 posts and comments from Reddit, Facebook, Bluesky, and Mastodon from 2019 to 2025, and analyse where these communities disagree, and how and why. Overall, we find that communities often disagree, and even show strong conflicts due to polarised sentiments on topics such as translation quality, efficiency, and reliability. This is because these communities approach these topics differently: the AI community frames them as technical and computational problems, while non-AI (user) communities care more about quality nuances, time savings, user trust, and broader social issues.
匹配关键词: AI scientist
---

[ACADEMIC - ARXIV]
标题: Data-driven discovery of governing differential equations across physical systems
作者: Siyu Lou, Hao Xu, Wenguan Wang, Lu Lu, Hao Sun, Yang Liu, Linfeng Zhang, Dongxiao Zhang, Yuntian Chen
链接: https://arxiv.org/abs/2606.09638v1
完整摘要: Differential equations play a critical role in scientific discovery because they provide a mathematical framework to describe the behaviour of physical phenomena. As a promising alternative to traditional first principles, data-driven differential equation discovery has attracted increasing attention for its ability to infer governing laws directly from experimental or simulated data, especially when the underlying physics is unclear. However, the field has expanded rapidly along diverse methodological directions, particularly with the emergence of AI-based approaches, and still lacks a clear organizing perspective. In this Review, we propose a problem-oriented perspective on data-driven differential equation discovery. We first introduce a two-dimensional phase diagram of equation discoverability, where discovery problems are organized according to structural complexity and coefficient complexity. This phase diagram shows how the field has moved from the discovery of sparse equations with simple coefficients toward more complex governing laws with richer structures and more flexible parameterizations. It also clarifies why different methodological families succeed or fail in different problem settings. We then present the representation-evaluation-optimization (REO) framework as a fundamental abstraction of the discovery process. By identifying the core problems of equation discovery that persist across algorithmic variations, REO shifts the discussion from individual algorithms to the fundamental principles that determine discoverability. We connect these perspectives to applications across physics and adjacent sciences, and argue that the next challenge is not merely recovering equations, but using them to revise existing theories, distil mechanisms and form new scientific concepts.
匹配关键词: AI scientist
---

[ACADEMIC - ARXIV]
标题: Civil Court Simulation with Large Language Models
作者: Yifan Chen, Haitao Li, Kaiyuan Zhang, Yueyue Wu, Qingyao Ai, Yiqun Liu
链接: https://arxiv.org/abs/2606.09632v1
完整摘要: Court simulation bridges legal education and judicial practice, yet human-based simulations are costly and difficult to scale. Large language models (LLMs) offer a scalable alternative, but existing court-simulation research mainly focuses on criminal cases. Civil litigation is more common in practice and harder to simulate because its claims, liability, and remedies are more flexible. We present a multi-agent court simulation framework for Chinese civil cases. The framework organizes role-based interaction through a five-stage civil trial procedure and integrates memory module and statute retrieval to support long-process adjudication. Experiments show that the framework produces reliable civil judgments, with clear strengths in liability allocation and multi-item adjudication. Further experiments show that memory quality substantially affects downstream simulation quality. Through a five-layer factor framework, we analyze how legal grounding, information conditions, judicial capability and role orientation, organizational pressure, and social context affect the framework's reliability and behavior. These results support the effectiveness of the proposed framework for civil court simulation. The dataset and code are available at: https://github.com/foggpoy/Civil-Court.
匹配关键词: AI scientist
---

[ACADEMIC - ARXIV]
标题: Cross-Modal Masking for Robust Silent Speech Synthesis Using sEMG and Lipreading
作者: Eder del Blanco, David Gimeno-Gómez, Eva Navas, Carlos-D. Martínez-Hinarejos, Inma Hernáez
链接: https://arxiv.org/abs/2606.09667v1
完整摘要: Speech restoration through silent speech interfaces (SSIs) has emerged as a promising assistive technology for individuals with impaired or absent laryngeal voice production. Among non-invasive SSI modalities, surface electromyography (sEMG) and video-based lipreading provide complementary articulatory information, yet their integration for continuous speech synthesis remains underexplored. Moreover, existing multimodal approaches rarely address robustness to modality degradation or temporary sensor failure, limiting their applicability in realistic scenarios. In this work, we propose a masked multimodal speech synthesis framework that jointly leverages sEMG and lipreading signals through modality masking during training. Under multispeaker settings, the proposed approach reduces word error rate by up to 14 absolute percentage points compared to the strongest unimodal baseline. Experimental results not only show that masking strategies are critical for these performance gains and robustness under low-bitrate conditions, but also that they generalize better than degradation-specific data augmentations in the presence of modality absence conditions. Phone-level analyses further reveal complementary contributions across modalities, with particularly strong benefits for vowels and for specific consonant groups. Overall, these findings demonstrate the effectiveness and robustness of masked multimodal integration for silent speech synthesis, although adaptation to laryngectomized speakers remains an open research challenge.
匹配关键词: automated research
---

[ACADEMIC - ARXIV]
标题: Beyond Accuracy: Community Perspectives on Machine Translation
作者: Yujun Wang, Ehud Reiter, Shimei Pan, Steffen Eger, Wei Zhao
链接: https://arxiv.org/abs/2606.09655v1
完整摘要: Despite remarkable progress in machine translation (MT), non-AI communities have raised growing concerns about MT systems, suggesting a noticeable gap between technical advancement and the needs of real-world users. For instance, while NLP researchers focus on benchmark performance, end users care about ethical concerns, trust, reliability, costs, and more. We argue that listening to various user communities is essential so that research efforts would be directed towards the problems that the communities care about. To this end, we present a large-scale analysis, for the first time, that investigates what four stakeholder communities (AI developers, professional translators, language learners, and language service providers) post about MT technology on social media. To do so, we construct a dataset of 79,286 posts and comments from Reddit, Facebook, Bluesky, and Mastodon from 2019 to 2025, and analyse where these communities disagree, and how and why. Overall, we find that communities often disagree, and even show strong conflicts due to polarised sentiments on topics such as translation quality, efficiency, and reliability. This is because these communities approach these topics differently: the AI community frames them as technical and computational problems, while non-AI (user) communities care more about quality nuances, time savings, user trust, and broader social issues.
匹配关键词: automated research
---

[ACADEMIC - ARXIV]
标题: ArtiFact: A Large-Scale Multi-Modal Cultural Heritage Dataset
作者: Luciano Duarte, Olga Ovcharenko, Sebastian Schelter
链接: https://arxiv.org/abs/2606.09648v1
完整摘要: Multi-modal data management has emerged as a central research topic in the database community, spanning data integration, semantic query processing, and data quality assessment. Despite this growing interest, the community lacks large-scale, real-world datasets combining tables, text, and images. We present ArtiFact, a multi-modal cultural heritage dataset of 651045 museum records collected from the Metropolitan Museum of Art, the Art Institute of Chicago, and the Rijksmuseum. We demonstrate the utility of ArtiFact through two downstream tasks. For cross-modal error detection, we introduce a curated taxonomy of seven error categories injected into 130209 records and show that reliably detecting subtle domain-specific errors such as material anachronisms and temporal shifts remain an open challenge. For semantic query processing, we show that current systems struggle with queries involving cultural proximity, ambiguous object types, and historically contingent terminology. Our results position ArtiFact as a challenging benchmark for multi-modal data management research.
匹配关键词: automated research
---

[ACADEMIC - ARXIV]
标题: CineDance: Towards Next-Generation Multi-Shot Long-Form Cinematic Audio-Video Generation
作者: Yuheng Chen, Teng Hu, Yuji Wang, Qingdong He, Zhucun Xue, Qianyu Zhou, Xiangtai Li, Lizhuang Ma, Jiangning Zhang, Dacheng Tao
链接: https://arxiv.org/abs/2606.09639v1
完整摘要: The fidelity and structural diversity of training datasets fundamentally determine the capabilities of video generation models. While commercial systems showremarkableabilitytogeneratecinematicnarratives, the progress of open-source models remains limited by the scarcity of high-quality training data. To bridge this gap, we introduce CineDance-1M, a large-scale, open research Text-to-Audio-Video (T2AV) dataset designed specifically for multi-shot, long-form joint audio-video generation. Averaging 92.8 seconds and 24.2 continuous shots per video, it provides configurable, structured annotations for both audio and video modalities. This exceptional quality is achieved through a rigorous three-stage curation pipeline: i) diverse sourcing and comprehensive cleansing, ii) film-theory-inspired narrative parsing, and iii) hierarchical dual-modal captioning. For a comprehensive assessment, we propose CineBench, featuring a diverse prompt suite and a six-dimensional, human-aligned metric system tailored for complex narrative audio-video evaluation. Furthermore, we adapt LTX-2.3 into CineDance, which demonstrates exceptional single-modality quality alongside precise audio-video alignment and robust subject and environment consistency, effectively validating our curation strategy and the high quality of CineDance-1M. We anticipate that this work will serve as a solid foundation for accelerating future research in multi-shot, long-form joint audio-video generation. Our project page is available at https://aliothchen.github.io/projects/CineDance/.
匹配关键词: automated research
---

[ACADEMIC - ARXIV]
标题: ATN3D: Density-Aware LiDAR-Radar Early 3D Object Detection Under Extreme Sparsity
作者: Debojyoti Biswas, Xianbiao Hu
链接: https://arxiv.org/abs/2606.09634v1
完整摘要: 3D object detection is the backbone of perception for automated vehicles (AV) and broader intelligent transportation systems applications. Long-range detection is challenging because sensing evidence is sparse; yet this ``long-range'' scenario is routine in traffic. Although >30m is often labeled long-range in computer vision, on roadways it affords only approx. 1-2s for perception and decision-making. Under such extreme sparsity, two core challenges arise. First, early multimodal fusion tends to discard sparsity information and inject noise from empty or falsely occupied cells, degrading long-range recall. Second, context-agnostic uniform channel supervision favors dense and near-range samples, leaving far and small objects under-optimized, delaying the earliest detection of distant objects. We propose ``Ask The Neighbor'' (ATN3D), a LiDAR-Radar framework tailored for sparse-range conditions. ATN3D introduces (i) Density-aware early fusion with cross-modal gating that conditions fusion on per-voxel density/sparsity and Radar evidence, (ii) Occupancy-gated neighborhood aggregation with circular kernels to aggregate only from credible cells, (iii) Evidence-conditioned channel self-attention to adapt channel weights with weather/range, and (iv) a Range-aware loss that re-balances classification and localization by distance, aligning training with distance-stratified evaluation. On the VoD benchmark across clear and foggy conditions, ATN3D surpasses strong baselines: +3.55% mAP in clear weather and +8.41% mAP under simulated heavy fog; for >30m objects, gains are +3.33% (clear) and +2.09% (heavy fog). These results indicate earlier and more reliable long-range detections under sparse sensing in on-road traffic.
匹配关键词: automated research
---

[ACADEMIC - ARXIV]
标题: Correlation Is Not Enough: Embedding Human Metadata for Individual Causal Discovery
作者: Suraj Biswas, Saurabh Gupta, Pritam Mukherjee
链接: https://arxiv.org/abs/2606.09672v1
完整摘要: Ask a pretrained biomedical language model whether "cortisol 28 ug/dL" and "stock-market volatility" are related, and it returns a cosine similarity of 0.83 on a scale where 1.0 means identical. The two share no mechanism. This is not a corner case: every off-the-shelf biomedical encoder we tested (BioBERT, PubMedBERT, BioM-ELECTRA) scores unrelated cross-domain pairs between 0.76 and 0.92 when the answer should be near zero. Accuracy on cross-domain discrimination is 0%. Retrieval systems survive this, because a language model downstream filters the noise. A Large Behavioural Model (LBM), a foundation model whose subject is a person rather than a sentence, does not: it reasons over a graph of a user's life and treats embedding proximity as evidence that two events are causally linked. False proximity writes a false causal edge, and everything downstream inherits the error. Here, embedding geometry is not a tuning knob; it is correctness. We report the fix. A contrastive pass over 72,034 pairs raises PubMedBERT BIOSSES correlation from 0.633 to 0.828 and within-vs-across-domain separation from 1.05x to 1.63x. A second pass, BODHI, mines hard negatives from edges absent in a biomedical knowledge graph and lifts separation to 2.30x and the discrimination gap to +0.392, at a 4.5% BIOSSES cost. On an Intel Xeon 6737P with AMX, OpenVINO cuts single-query latency from 1367 ms to 10 ms (133x) and reaches 555 sentences/sec. One finding contradicts standard advice: FP16 beats INT8 on this silicon at every serving batch size, and we explain why. The same model on a no-AMX Ice Lake instance runs 13-27x slower. We release the benchmark suite, training corpora, the BODHI generator, and the OpenVINO scripts.
匹配关键词: scientific discovery
---

[ACADEMIC - ARXIV]
标题: Data-driven discovery of governing differential equations across physical systems
作者: Siyu Lou, Hao Xu, Wenguan Wang, Lu Lu, Hao Sun, Yang Liu, Linfeng Zhang, Dongxiao Zhang, Yuntian Chen
链接: https://arxiv.org/abs/2606.09638v1
完整摘要: Differential equations play a critical role in scientific discovery because they provide a mathematical framework to describe the behaviour of physical phenomena. As a promising alternative to traditional first principles, data-driven differential equation discovery has attracted increasing attention for its ability to infer governing laws directly from experimental or simulated data, especially when the underlying physics is unclear. However, the field has expanded rapidly along diverse methodological directions, particularly with the emergence of AI-based approaches, and still lacks a clear organizing perspective. In this Review, we propose a problem-oriented perspective on data-driven differential equation discovery. We first introduce a two-dimensional phase diagram of equation discoverability, where discovery problems are organized according to structural complexity and coefficient complexity. This phase diagram shows how the field has moved from the discovery of sparse equations with simple coefficients toward more complex governing laws with richer structures and more flexible parameterizations. It also clarifies why different methodological families succeed or fail in different problem settings. We then present the representation-evaluation-optimization (REO) framework as a fundamental abstraction of the discovery process. By identifying the core problems of equation discovery that persist across algorithmic variations, REO shifts the discussion from individual algorithms to the fundamental principles that determine discoverability. We connect these perspectives to applications across physics and adjacent sciences, and argue that the next challenge is not merely recovering equations, but using them to revise existing theories, distil mechanisms and form new scientific concepts.
匹配关键词: scientific discovery
---

[ACADEMIC - ARXIV]
标题: Closure-Validated Circuit Discovery in Attention Heads: Co-activation Proposes, Ablation Disposes
作者: Yongzhong Xu
链接: https://arxiv.org/abs/2606.09607v1
完整摘要: Interpretability increasingly treats groups of components, not individual units, as the basic object, and proposes to find them by clustering co-activation statistics. We ask whether such a cheap signal actually identifies an attention-head circuit. Adapting a sparse-autoencoder clustering recipe to attention heads -- but validating by causal ablation rather than reconstruction -- we cluster heads and then run a closure test: ablate the discovered community and compare per-example damage to matched-random controls. Across two dense 1B-scale models (Pythia 1B, OLMo 1B) and two input distributions, the communities pass closure. In a Mixture-of-Experts model (OLMoE-1B-7B), route-conditional clustering recovers a statistically real signal that nonetheless does not survive closure -- ablation improves loss, the wrong direction. Extending closure across training, attention-target selectivity and participation ratio decouple from function in both directions. We conclude that a cheap signal is a circuit proposal, not a confirmed circuit; closure is what separates them.
匹配关键词: scientific discovery
---

[ACADEMIC - ARXIV]
标题: Assessing Sample Quality in Conditional Generation under Compositional Shift
作者: Berker Demirel, Valentino Maiorca, Marco Fumero, Theofanis Karaletsos, Francesco Locatello
链接: https://arxiv.org/abs/2606.09601v1
完整摘要: Conditional generators provide a natural tool for controllable generation, including settings where the desired condition is a new composition of observed attributes or experimental factors. In many applications, especially in scientific domains, such models are attractive to explore conditions for which real samples are rare, expensive, or not yet observed. However, this creates a circularity for evaluation: standard conditional quality metrics require a reference target distribution, but in the extrapolative regime that distribution is unavailable by definition. We address this problem with a post-hoc, per-sample trust score for assessing conditional samples using only the training distribution. The score combines two estimable quantities: global realism, measuring compatibility with the real data manifold, and attribute-wise faithfulness, measuring whether a sample is closer to the requested attributes than to plausible alternatives. We show that the score can recover meaningful comparisons across extrapolated generations, under a mild coverage condition on the observed attributes. These comparisons enable effective filtering, ranking, and abstention of generations and can be used directly on off-the-shelf pretrained models. In biological imaging, selected samples preserve real morphological structure better and improve downstream predictive performance, while similar gains are observed on controlled vision benchmarks. Finally, we show how the score can be applied during generation, enabling abstention before full decoding. Code is available at https://github.com/berkerdemirel/faithful-cond-gen.
匹配关键词: scientific discovery
---

[ACADEMIC - ARXIV]
标题: Optical Reasoning: Rethinking Images as an Expressive Reasoning Medium Beyond Text
作者: Yutong Bian, Dongjie Cheng, Heming Xia, Yongqi Li, Wenjie Li
链接: https://arxiv.org/abs/2606.09585v1
完整摘要: Chain-of-Thought (CoT) improves the performance of Large Language Models (LLMs) and has been extended to Multimodal Large Language Models (MLLMs). More recent work further moves from text-based multimodal reasoning toward interleaved-modal reasoning, where intermediate steps can incorporate both textual rationales and visual evidence. In this work, we propose a bolder and more ambitious idea: could images alone serve as the reasoning medium for both language and multimodal tasks? To explore this, we propose optical reasoning, which treats images as a standalone reasoning medium. We instantiate this concept with two variants: typographic-based optical reasoning, which optimizes visual layouts for compact rationale rendering, and graphical-based optical reasoning, which composes text and graphical elements into structured visual rationales. Across mathematical, scientific, and interleaved-modal reasoning benchmarks, optical reasoning can match or even exceed traditional text reasoning while reducing reasoning tokens by an average of 28.57% on language tasks and 16% on multimodal tasks, achieving 1.96 times the token efficiency of text reasoning. These results show that images can effectively and efficiently encode rationales while providing a unified visual canvas for reasoning.
匹配关键词: scientific discovery
---

[ACADEMIC - ARXIV]
标题: MeCo: One-Step MeanFlow-based Corrector for Multi-Channel Speech Separation
作者: Dohwan Kim, Jung-Woo Choi
链接: https://arxiv.org/abs/2606.09677v1
完整摘要: While discriminative models for multi-channel speech separation excel in reference-based metrics, they often exhibit suboptimal human listening quality. To address this, we propose a novel MeanFlow-based one-step generative corrector (MeCo). MeCo learns a conditional average velocity field to map discriminative estimates directly onto the clean speech manifold in a single step. To maximize one-step generation performance, we introduce Data-Space Optimization (DSO). DSO integrates an $\mathbf{x}_r$-loss, which penalizes prediction errors on longer displacement intervals to serve as a generative objective for human listening quality, with an Endpoint SI-SDR loss that directly optimizes terminal signal fidelity. Experiments demonstrate that MeCo achieves state-of-the-art (SOTA) performance with minimal computational overhead, simultaneously achieving superior signal fidelity and human listening quality in both in-domain and out-of-domain scenarios.
匹配关键词: hypothesis generation
---

[ACADEMIC - ARXIV]
标题: Correlation Is Not Enough: Embedding Human Metadata for Individual Causal Discovery
作者: Suraj Biswas, Saurabh Gupta, Pritam Mukherjee
链接: https://arxiv.org/abs/2606.09672v1
完整摘要: Ask a pretrained biomedical language model whether "cortisol 28 ug/dL" and "stock-market volatility" are related, and it returns a cosine similarity of 0.83 on a scale where 1.0 means identical. The two share no mechanism. This is not a corner case: every off-the-shelf biomedical encoder we tested (BioBERT, PubMedBERT, BioM-ELECTRA) scores unrelated cross-domain pairs between 0.76 and 0.92 when the answer should be near zero. Accuracy on cross-domain discrimination is 0%. Retrieval systems survive this, because a language model downstream filters the noise. A Large Behavioural Model (LBM), a foundation model whose subject is a person rather than a sentence, does not: it reasons over a graph of a user's life and treats embedding proximity as evidence that two events are causally linked. False proximity writes a false causal edge, and everything downstream inherits the error. Here, embedding geometry is not a tuning knob; it is correctness. We report the fix. A contrastive pass over 72,034 pairs raises PubMedBERT BIOSSES correlation from 0.633 to 0.828 and within-vs-across-domain separation from 1.05x to 1.63x. A second pass, BODHI, mines hard negatives from edges absent in a biomedical knowledge graph and lifts separation to 2.30x and the discrimination gap to +0.392, at a 4.5% BIOSSES cost. On an Intel Xeon 6737P with AMX, OpenVINO cuts single-query latency from 1367 ms to 10 ms (133x) and reaches 555 sentences/sec. One finding contradicts standard advice: FP16 beats INT8 on this silicon at every serving batch size, and we explain why. The same model on a no-AMX Ice Lake instance runs 13-27x slower. We release the benchmark suite, training corpora, the BODHI generator, and the OpenVINO scripts.
匹配关键词: hypothesis generation
---

[ACADEMIC - ARXIV]
标题: Visual Prompting Meets Feature Reconstruction-Based Anomaly Detection with Dual-Teacher Supervision
作者: Mateo Diaz-Bone, Daniel Caraballo, Florian Scheidegger, Thomas Frick, Mattia Rigotti, Andrea Bartezzaghi, Roy Assaf, Niccolo Avogaro, Yagmur G. Cinar, Brown Ebouky, Filip M. Janicki, Piotr S. Kluska, Cezary Skura, Cristiano Malossi
链接: https://arxiv.org/abs/2606.09670v1
完整摘要: Recent Anomaly Detection methods achieve perfect detection and segmentation scores on well-established datasets, such as MVTec. However, many of these methods face challenges when foundational assumptions - such as consistent object scale, viewpoint, background, illumination, and centered placement - are violated. Those variations that occur render anomaly detection methods unusable in many real-world scenarios. To address these limitations, we introduce three key contributions: (1) a visual prompting pipeline that isolates objects using foreground-background masking; (2) a mechanism for unfreezing the teacher in student-teacher models to improve domain adaptability; and (3) a data augmentation strategy leveraging diffusion-generated synthetic images to enhance anomaly detection performance. We achieve a 3.5 percentage point improvement over the previous state-of-the-art on the challenging AeBAD dataset by using the Masked Multiscale Reconstruction (MMR) model as our backbone.
匹配关键词: hypothesis generation
---

[ACADEMIC - ARXIV]
标题: SpatialWorld: Benchmarking Interactive Spatial Reasoning of Multimodal Agents in Real-World Tasks
作者: Hongcheng Gao, Hailong Qu, Jingyi Tang, Jiahao Wang, Zihao Huang, Hengkang Qiao, Shihong Huang, Junming Yang, Yi Li, Hongyixuan Yuan, Wenjie Li, Bohan Zeng, Wenbo Li, Bo Wang, Jianhui Liu, Olive Huang, Haoyang Huang, Wentao Zhang, Guoqing Huang, Nan Duan, Yinpeng Dong
链接: https://arxiv.org/abs/2606.09669v1
完整摘要: Spatial reasoning is a foundational capability for multimodal large language models (MLLMs) to perceive and operate within the physical world. However, existing benchmarks predominantly rely on passive evaluation (e.g., static VQA) or simulator-specific pipelines, failing to assess general interactive spatial understanding. We introduce SpatialWorld, a unified benchmark designed specifically for evaluating the interactive spatial understanding of multimodal agents in complex real-world tasks. Integrating eight heterogeneous simulation backends under a shared, simulator-agnostic protocol, SpatialWorld features 760 human-annotated tasks across diverse domains (e.g., household routines, travel, social collaboration). Agents must solve tasks under vision-only partial observability, actively gathering egocentric visual evidence and expressing decisions via a unified, text-based action interface native to MLLMs. For reliable evaluation, each task includes a human-validated initial state, a reference trajectory, and a terminal-state verifier. Evaluating 15 advanced agents reveals that robust spatial task solving remains challenging: the strongest model, GPT-5, achieves an average task success rate (TSR) of only 17.4%, while the leading open-source model, Qwen-3.5, reaches 14.1%. Further analysis exposes a clear mismatch between task success and execution efficiency, alongside substantial domain-specific performance variations. These bottlenecks in active exploration and long-horizon planning position SpatialWorld as a rigorous testbed for future spatial agents.
匹配关键词: hypothesis generation
---

[ACADEMIC - ARXIV]
标题: Cross-Modal Masking for Robust Silent Speech Synthesis Using sEMG and Lipreading
作者: Eder del Blanco, David Gimeno-Gómez, Eva Navas, Carlos-D. Martínez-Hinarejos, Inma Hernáez
链接: https://arxiv.org/abs/2606.09667v1
完整摘要: Speech restoration through silent speech interfaces (SSIs) has emerged as a promising assistive technology for individuals with impaired or absent laryngeal voice production. Among non-invasive SSI modalities, surface electromyography (sEMG) and video-based lipreading provide complementary articulatory information, yet their integration for continuous speech synthesis remains underexplored. Moreover, existing multimodal approaches rarely address robustness to modality degradation or temporary sensor failure, limiting their applicability in realistic scenarios. In this work, we propose a masked multimodal speech synthesis framework that jointly leverages sEMG and lipreading signals through modality masking during training. Under multispeaker settings, the proposed approach reduces word error rate by up to 14 absolute percentage points compared to the strongest unimodal baseline. Experimental results not only show that masking strategies are critical for these performance gains and robustness under low-bitrate conditions, but also that they generalize better than degradation-specific data augmentations in the presence of modality absence conditions. Phone-level analyses further reveal complementary contributions across modalities, with particularly strong benefits for vowels and for specific consonant groups. Overall, these findings demonstrate the effectiveness and robustness of masked multimodal integration for silent speech synthesis, although adaptation to laryngectomized speakers remains an open research challenge.
匹配关键词: hypothesis generation
---

[ACADEMIC - ARXIV]
标题: MeCo: One-Step MeanFlow-based Corrector for Multi-Channel Speech Separation
作者: Dohwan Kim, Jung-Woo Choi
链接: https://arxiv.org/abs/2606.09677v1
完整摘要: While discriminative models for multi-channel speech separation excel in reference-based metrics, they often exhibit suboptimal human listening quality. To address this, we propose a novel MeanFlow-based one-step generative corrector (MeCo). MeCo learns a conditional average velocity field to map discriminative estimates directly onto the clean speech manifold in a single step. To maximize one-step generation performance, we introduce Data-Space Optimization (DSO). DSO integrates an $\mathbf{x}_r$-loss, which penalizes prediction errors on longer displacement intervals to serve as a generative objective for human listening quality, with an Endpoint SI-SDR loss that directly optimizes terminal signal fidelity. Experiments demonstrate that MeCo achieves state-of-the-art (SOTA) performance with minimal computational overhead, simultaneously achieving superior signal fidelity and human listening quality in both in-domain and out-of-domain scenarios.
匹配关键词: autonomous experiment
---

[ACADEMIC - ARXIV]
标题: A Unifying Framework for Concept-Based Representational Similarity
作者: Grégoire Dhimoïla, Victor Boutin, Agustin Martin Picard, Thomas Fel, Thomas Serre
链接: https://arxiv.org/abs/2606.09653v1
完整摘要: Learned representations across models and modalities often exhibit striking structural similarities, suggesting shared underlying concept decompositions. However, concept alignment remains poorly defined: existing approaches optimize different objectives under the same terminology, obscuring what is actually aligned. We propose a unifying framework that decomposes alignment along two axes: what is aligned (representations vs. concepts) and at what level (instance-wise vs. distributional). This induces four corresponding properties -- instance-wise and distributional variants of translation and concept consistency -- and reveals precisely which of these guarantees existing methods provide. We further introduce \InterVenchA, an intervention-based benchmark that separately measures extraction quality, translation quality, and concept consistency. Through theory and experiments, we show that commonly assumed equivalences between alignment objectives fail in practice: optimizing one property does not reliably recover the others, and purely unsupervised objectives fail to recover meaningful instance-level alignment. We then propose the Coupled Sparse Autoencoder (CoSAE), which jointly enforces complementary alignment objectives. Strong alignment emerges only in this regime. Surprisingly, as little as 0.1\% paired data is sufficient to recover instance-level alignment when anchoring distributional objectives. Overall, our results show that concept alignment is fundamentally multi-objective: it must be defined, measured, and optimized as such.
匹配关键词: autonomous experiment
---

[ACADEMIC - ARXIV]
标题: Where Does the Answer Come From? Benchmarking View-Level Visual Evidence Identification in Multi-View MLLMs for Autonomous Driving
作者: Yimu Wang, Yee Man Choi, Barry Zhang, Mozhgan Nasr Azadani, Sean Sedwards, Krzysztof Czarnecki
链接: https://arxiv.org/abs/2606.09644v1
完整摘要: Multimodal large language models (MLLMs) achieve strong results on visual reasoning benchmarks, but answer accuracy alone does not indicate whether a model relied on the correct visual evidence. This gap is particularly important in multi-view driving scenes used for autonomous driving, where a model can produce a plausible answer while grounding it in the wrong camera view. We introduce a multi-view visual question answering benchmark for evaluating evidence-source identification: given six synchronized NuScenes views and a question, the model must identify the supporting camera view and answer the question. The benchmark contains 122 conflict-centric question-answer pairs from 73 scenes, spanning causality, counterfactual reasoning, and intent prediction. View labels are proposed by an automatic conflict-mining pipeline and manually verified by annotators. We evaluate three settings: camera-view selection, oracle QA given the golden view, and joint prediction in which the model selects a view and answers in one pass. Answers are evaluated in both multiple-choice and free-form formats, using exact match for structured predictions and an LLM judge for free-form responses. By explicitly separating visual-source identification from answer correctness, the benchmark exposes grounding failures that answer-only evaluation misses.
匹配关键词: autonomous experiment
---

[ACADEMIC - ARXIV]
标题: MAVIS: Multi-Agent Video Retrieval via Structured Video Understanding
作者: Jie Zhang, Qilang Ye, Hao Zhou, Haochen Liang, Fei Luo
链接: https://arxiv.org/abs/2606.09641v1
完整摘要: The dominant paradigm in video retrieval relies on embedding-based full-corpus scanning, which suffers from inherent computational inefficiency and the semantic asymmetry between information-dense videos and sparse textual queries. To bridge this gap, we introduce \textbf{MAVIS}, a novel multi-agent framework that rethinks retrieval as cooperative reasoning rather than brute-force search. MAVIS first bridges the granularity mismatch by parsing raw videos into a \textbf{Structured Semantic Library}, enabling explicit attribute-level indexing. During retrieval, a planner decomposes complex user intents into atomic sub-tasks, dispatching specialized agents to independently nominate candidates. Crucially, MAVIS employs a \textbf{Logic-aware Debate} mechanism with a strict veto protocol, where agents collaboratively prune logical mismatches to identify a compact set of ``controversial'' candidates for fine-grained verification. This agentic workflow effectively bypasses the inefficiency of full-library traversal. Extensive experiments on MSR-VTT, MSVD, and ActivityNet demonstrate that MAVIS achieves competitive performance without task-specific fine-tuning, offering a scalable and interpretable alternative to traditional dual-encoder approaches.
匹配关键词: autonomous experiment
---

[ACADEMIC - ARXIV]
标题: Physics-Aware Sparse Learning and Selective Online Adaptation for Euler-Lagrange Robot Dynamics
作者: Rishabh Dev Yadav, Samaksh Ujjawal, Sihao Sun, Spandan Roy, Wei Pan
链接: https://arxiv.org/abs/2606.09640v1
完整摘要: Accurate dynamics models are essential for model-based robotic control, yet nominal Euler--Lagrange models often become inaccurate in the presence of payload variation, unmodeled coupling, friction, aerodynamic effects, and changing operating conditions. Most learning-based correction methods improve prediction accuracy by introducing a single additive residual, but do not preserve the internal mechanical structure of Euler--Lagrange systems. This leads to models that do not preserve symmetry, positive-definiteness, or the coupling between inertia and velocity-dependent terms, which can result in physically inconsistent predictions and reduced reliability when embedded in model-based controllers. We propose a structure-preserving residual learning framework that decomposes model mismatch into an inertia correction, the corresponding induced Coriolis term, and a generalized-force residual. The mechanical component is learned under physical constraints, while the disturbance-sensitive component is represented through a sparse history-dependent latent interaction model and adapted online using Bayesian linear regression. This separation preserves key mechanical structure while restricting adaptation to the part of the dynamics most affected by changing conditions. Experiments across multiple robotic platforms, including mobile, aerial, and manipulator systems, show that the proposed method improves dynamics prediction and trajectory tracking under coupled and time-varying dynamics. These results highlight the value of combining structured residual modeling, compact latent interaction selection, and selective online adaptation for real-world model-based control.
匹配关键词: autonomous experiment
---

[ACADEMIC - ARXIV]
标题: ATN3D: Density-Aware LiDAR-Radar Early 3D Object Detection Under Extreme Sparsity
作者: Debojyoti Biswas, Xianbiao Hu
链接: https://arxiv.org/abs/2606.09634v1
完整摘要: 3D object detection is the backbone of perception for automated vehicles (AV) and broader intelligent transportation systems applications. Long-range detection is challenging because sensing evidence is sparse; yet this ``long-range'' scenario is routine in traffic. Although >30m is often labeled long-range in computer vision, on roadways it affords only approx. 1-2s for perception and decision-making. Under such extreme sparsity, two core challenges arise. First, early multimodal fusion tends to discard sparsity information and inject noise from empty or falsely occupied cells, degrading long-range recall. Second, context-agnostic uniform channel supervision favors dense and near-range samples, leaving far and small objects under-optimized, delaying the earliest detection of distant objects. We propose ``Ask The Neighbor'' (ATN3D), a LiDAR-Radar framework tailored for sparse-range conditions. ATN3D introduces (i) Density-aware early fusion with cross-modal gating that conditions fusion on per-voxel density/sparsity and Radar evidence, (ii) Occupancy-gated neighborhood aggregation with circular kernels to aggregate only from credible cells, (iii) Evidence-conditioned channel self-attention to adapt channel weights with weather/range, and (iv) a Range-aware loss that re-balances classification and localization by distance, aligning training with distance-stratified evaluation. On the VoD benchmark across clear and foggy conditions, ATN3D surpasses strong baselines: +3.55% mAP in clear weather and +8.41% mAP under simulated heavy fog; for >30m objects, gains are +3.33% (clear) and +2.09% (heavy fog). These results indicate earlier and more reliable long-range detections under sparse sensing in on-road traffic.
匹配关键词: lab automation
---

[ACADEMIC - ARXIV]
标题: Automated IEP Generation from Traditional Chinese Parent-Teacher Interviews via Corpus-Grounded Feature Diffusion
作者: Kuanlin Chen, Cheng-En Ou
链接: https://arxiv.org/abs/2606.09603v1
完整摘要: Writing Individualized Education Programs (IEPs) is a high-labor, knowledge-intensive document burden; English-language research has demonstrated that generative AI can significantly reduce drafting time, yet automated IEP generation in Traditional Chinese remains virtually unexplored due to domain data scarcity, strict privacy regulations, and the absence of local evaluation benchmarks. We propose a low-resource fine-tuning pipeline centered on Corpus-Grounded Feature Diffusion (CGFD): (1) 25 dual-expert high-score seed transcripts are selected via a tau threshold with flag-aware score caps; (2) a FeatureProfile (sentence length, structure, quantification templates) is extracted from seeds and injected into LLM prompts alongside Verbalized-Sampling-style diversity control to drive diffusion; (3) 15 expert gold seeds are used as diffusion anchors, targeting 585 samples; 567 valid diffusion samples are obtained, yielding a 582-sample training set used to fine-tune Breeze-7B with QLoRA; (4) schema-constrained inference via Grammar-Constrained Decoding (GCD) enforces a hierarchical SMART Goal Ladder schema at inference time. Ablation results on a 55-sample schema stress set reveal an unexpected finding: GCD is counterproductive under Traditional Chinese token budgets -- the no-GCD path achieves 100% schema pass rate at 34% lower median latency, outperforming GCD on both reliability and speed. On the n=10 formal hold-out, the no-GCD inference path achieves BERTScore F1 = 0.779, exceeding GPT-5.4 (0.726), DeepSeek-V3.2 (0.703), Gemini-3-Flash-Preview (0.703), and Llama-4-Maverick (0.700) zero-shot baselines while maintaining fully local, air-gapped inference. This system addresses a gap in Traditional Chinese special-education NLP and offers a scalable, privacy-preserving local inference solution under an industrial engineering paradigm.
匹配关键词: lab automation
---

[ACADEMIC - ARXIV]
标题: Automating the Expert Eye: A System-Agnostic Deep Learning Framework for Rare Event Discovery in Imbalanced Force Spectroscopy
作者: Jorge Rodriguez-Ramos
链接: https://arxiv.org/abs/2606.09541v1
完整摘要: Single-Molecule Force Spectroscopy (SMFS) provides unprecedented insights into biomolecular mechanics, yet the high-throughput generation of force-extension trajectories creates a severe data curation bottleneck. Identifying rare molecular unbinding events within thousands of noise-dominated curves traditionally relies on tedious, non-scalable manual auditing. Here, we present a system-agnostic, interpretable deep learning framework tailored to overcome extreme class imbalance in automated SMFS triage. Utilizing 1D-to-2D rasterized geometric matrices, we deployed a modified ResNet18 architecture governed by an asymmetric Focal Loss objective function. We evaluated this framework on the complex mechanical unfolding pathways of the R. champanellensis cellulosome. Under hyper-imbalanced test conditions where the target interaction constituted only 1.34% of the dataset (13 true events out of 970 traces), the model achieved an overall accuracy of 0.9196 and a remarkable True Positive Rate (Recall) of 0.9231. By implementing an empirically calibrated dual-threshold triage system, the pipeline automatically discarded 880 unambiguous background noise traces , reducing the manual curation workload by over 90% while safely preserving high-value rare data. Finally, Gradient-weighted Class Activation Mapping (Grad-CAM) visually validated that the network's decisions are firmly anchored in the relevant geometric features of the force curves, specifically localizing on the structural unbinding regions, effectively mitigating 'black-box' skepticism. Built for free cloud-based execution, this open-source tool democratizes scalable, highly precise molecular discovery across the biophysics community.
匹配关键词: lab automation
---

[ACADEMIC - ARXIV]
标题: A Finetuned SpeechLLM for Joint Multi-Granular L2 Assessment and Natural-Language Rationales
作者: Aditya Kamlesh Parikh, Cristian Tejedor-Garcia, Catia Cucchiarini, Helmer Strik
链接: https://arxiv.org/abs/2606.09470v1
完整摘要: Automated L2 speech assessment can assign proficiency labels, but often lacks interpretability. We propose a rubric-guided SpeechLLM for multi-aspect, multi-granular assessment, trained with a hybrid objective combining supervised fine-tuning and Bounded Direct Preference Optimization. The model jointly predicts ordinal labels at the sentence-level (accuracy, fluency, prosody), word/phoneme-level accuracy, and generates a natural-language rationale in the same response. On SpeechOcean762, our approach matches or outperforms single-granularity models while remaining competitive with prior approaches. We analyze rationale reliability along two axes: self-consistency with model predictions and alignment with ground-truth labels, using sentiment consistency (plausibility) and mention-based agreement (faithfulness). Rationales are plausible at the sentence level, but faithfulness degrades at the word/phoneme level: references are sparse and weakly aligned with token-level labels.
匹配关键词: lab automation
---

[ACADEMIC - ARXIV]
标题: AliyunConsoleAgent: Training Web Agents in Real-World Cloud Environments via Distillation and Reinforcement Learning
作者: Bojie Rong, Zheyu Shen, Qiaoping Wang, Pengfei Kang, Yang Xu, Yawen Wei, Hanyu Wu, Zhi Zhao, Leihao Pei, Linquan Jiang
链接: https://arxiv.org/abs/2606.09447v1
完整摘要: We present AliyunConsoleAgent, a web agent framework for automated documentation verification in real-world cloud consoles. Major cloud platforms encompass hundreds of products with rapid feature iteration, causing console UIs to frequently diverge from their corresponding documentation. Verifying that documented procedures accurately reflect the current console and can be executed end-to-end demands an estimated 4 million recurring inspections annually, yet manual coverage remains below 1%. While agent systems built on frontier proprietary models achieve high success rates, their prohibitive cost and data privacy constraints preclude large-scale deployment. We propose a two-stage training paradigm: supervised fine-tuning (SFT) on distilled frontier-model trajectories, followed by reinforcement learning using Group Relative Policy Optimization (GRPO) and a dual-channel outcome reward model in real cloud environments. To support large-scale RL training, we construct a high-determinism rollout system featuring Terraform-based resource pre-provisioning and LLM-driven on-demand provisioning, which effectively isolates environment noise from the training signal. We further introduce a rule-based reward evaluation protocol grounded in backend audit logs, providing objective, reward-hacking-resistant outcome judgment. Our model evolves from mechanical instruction following to autonomous decision-making with cloud console and product-specific understanding. Experiments on a challenging 278-task benchmark where the best frontier model achieves only 65.34% demonstrate that AliyunConsoleAgent-32B achieves a 63.52% mean success rate -- a 20.24 percentage-point improvement over the base model, narrowing the gap to the best frontier proprietary model to 1.82 pp (bootstrap 95% CI [-1.27, 7.39]) -- at 92% lower inference cost.
匹配关键词: lab automation
---

[ACADEMIC - ARXIV]
标题: SoccerNet 2026 Player-Centric Ball-Action Spotting:Retraining and Post-Processing Extensions to the FOOTPASS Baselines
作者: Parthsarthi Rawat
链接: https://arxiv.org/abs/2606.09679v1
完整摘要: We describe our system for the SoccerNet 2026 Player-Centric Ball-Action Spotting Challenge, which requires predicting who performs which action and when, across eight classes in broadcast soccer. Building on the three FOOTPASS baselines [1] (TAAD, TAAD+GNN, and TAAD+DST), we contribute four extensions: (1) gradient check pointing to enable full-backbone fine-tuning on a single GPU; (2) fusion of GNN logits into the DST encoder, combining graph-based tactical context with per-player visual features; (3) square-root frequency class weighting to address the 213:1 pass-to-tackle imbalance in the training data; and (4) a post processing pipeline comprising per-class logit gating, temporal frame refinement, jersey re-assignment, and a two-model ensemble. Our system achieves 0.548 Macro F1 on the test set and 0.446 on the challenge set (server evaluation).
匹配关键词: AI for science
---

[ACADEMIC - ARXIV]
标题: MeCo: One-Step MeanFlow-based Corrector for Multi-Channel Speech Separation
作者: Dohwan Kim, Jung-Woo Choi
链接: https://arxiv.org/abs/2606.09677v1
完整摘要: While discriminative models for multi-channel speech separation excel in reference-based metrics, they often exhibit suboptimal human listening quality. To address this, we propose a novel MeanFlow-based one-step generative corrector (MeCo). MeCo learns a conditional average velocity field to map discriminative estimates directly onto the clean speech manifold in a single step. To maximize one-step generation performance, we introduce Data-Space Optimization (DSO). DSO integrates an $\mathbf{x}_r$-loss, which penalizes prediction errors on longer displacement intervals to serve as a generative objective for human listening quality, with an Endpoint SI-SDR loss that directly optimizes terminal signal fidelity. Experiments demonstrate that MeCo achieves state-of-the-art (SOTA) performance with minimal computational overhead, simultaneously achieving superior signal fidelity and human listening quality in both in-domain and out-of-domain scenarios.
匹配关键词: AI for science
---

[ACADEMIC - ARXIV]
标题: (Auto)formalization is supposed to be easy: Trellis process semantics for spelling out rigorous proofs
作者: Wesley Pegden
链接: https://arxiv.org/abs/2606.09674v1
完整摘要: We present Trellis: an autoformalization system that leverages LLM agents in a deterministically constrained workflow to enforce incremental progress in Lean autoformalization tasks through iterative refinement of natural language proofs. Our approach is motivated by the common mathematician's notion of what it means to have a rigorous proof in the first place: namely, that it would be routine to elaborate any part of the proof in further detail. The result is a system which aims to achieve reliable autoformalization on a modest budget and with generalist agents, with specialization to autoformalization coming not from any task-specific agent training but instead from a meaning-of-rigor inspired workflow enforced by process semantics. We link to an end-to-end Lean formalization of a recent Ramsey theory breakthrough produced by the process.
匹配关键词: AI for science
---

[ACADEMIC - ARXIV]
标题: Correlation Is Not Enough: Embedding Human Metadata for Individual Causal Discovery
作者: Suraj Biswas, Saurabh Gupta, Pritam Mukherjee
链接: https://arxiv.org/abs/2606.09672v1
完整摘要: Ask a pretrained biomedical language model whether "cortisol 28 ug/dL" and "stock-market volatility" are related, and it returns a cosine similarity of 0.83 on a scale where 1.0 means identical. The two share no mechanism. This is not a corner case: every off-the-shelf biomedical encoder we tested (BioBERT, PubMedBERT, BioM-ELECTRA) scores unrelated cross-domain pairs between 0.76 and 0.92 when the answer should be near zero. Accuracy on cross-domain discrimination is 0%. Retrieval systems survive this, because a language model downstream filters the noise. A Large Behavioural Model (LBM), a foundation model whose subject is a person rather than a sentence, does not: it reasons over a graph of a user's life and treats embedding proximity as evidence that two events are causally linked. False proximity writes a false causal edge, and everything downstream inherits the error. Here, embedding geometry is not a tuning knob; it is correctness. We report the fix. A contrastive pass over 72,034 pairs raises PubMedBERT BIOSSES correlation from 0.633 to 0.828 and within-vs-across-domain separation from 1.05x to 1.63x. A second pass, BODHI, mines hard negatives from edges absent in a biomedical knowledge graph and lifts separation to 2.30x and the discrimination gap to +0.392, at a 4.5% BIOSSES cost. On an Intel Xeon 6737P with AMX, OpenVINO cuts single-query latency from 1367 ms to 10 ms (133x) and reaches 555 sentences/sec. One finding contradicts standard advice: FP16 beats INT8 on this silicon at every serving batch size, and we explain why. The same model on a no-AMX Ice Lake instance runs 13-27x slower. We release the benchmark suite, training corpora, the BODHI generator, and the OpenVINO scripts.
匹配关键词: AI for science
---

[ACADEMIC - ARXIV]
标题: Transition-Based Digital Twin Modelling for Alzheimer's Disease under Sparse Longitudinal Data
作者: Yinyu Huang, Yilin Zhang, Sofia Michopoulou, Christopher Kipps, Rahman Attar
链接: https://arxiv.org/abs/2606.09671v1
完整摘要: Alzheimer's disease (AD) progression is highly heterogeneous and is typically observed through sparse and irregular longitudinal data, posing challenges for prediction and personalised monitoring. Existing machine learning approaches have improved AD prediction using multimodal data, yet often focus on static classification or cohort-level risk estimation, providing limited support for subject-specific modelling and uncertainty-aware reasoning. To address these limitations, we present a personalised digital twin framework for AD prediction and scenario-based analysis using multimodal longitudinal data. The proposed approach integrates complementary modelling strategies to capture clinical transitions and temporal dependencies across visits. Using data from the Alzheimer's Disease Neuroimaging Initiative (ADNI), including cognitive assessments, clinical variables, and MRI-derived phenotypes, the framework predicts cognitive status and diagnostic categories while quantifying predictive uncertainty and enabling patient-specific what-if trajectory analysis. Evaluation on leak-free subject-level splits demonstrates strong performance in score forecasting and diagnosis classification. In this sparse and irregular ADNI setting, transition-based modelling of adjacent visits achieved higher predictive accuracy than the sequence-based branch, suggesting that local transition modelling may be more data-efficient. While sequence models remain valuable for uncertainty-aware trajectory forecasting, local transition modelling offers a more data-efficient and robust predictive strategy. These findings highlight the importance of aligning temporal modelling strategies with clinical data structure and suggest that transition-based digital twin formulations may provide a practical and interpretable approach for personalised disease forecasting in neurodegenerative disorders.
匹配关键词: AI for science
---

[ACADEMIC - ARXIV]
标题: Toward Compiler World Models: Learning Latent Dynamics for Efficient Tensor Program Search
作者: Haolin Pan, Lianghong Huang, Xvlin Zhou, Mingjie Xing, Yanjun Wu
链接: https://arxiv.org/abs/2606.09312v1
完整摘要: Tensor program optimization is essential for modern machine learning systems, but its search space is enormous. Existing auto-schedulers reduce measurement cost with learned cost models, yet they usually evaluate each candidate as a static code snapshot, ignoring the schedule trajectory that produced it. This makes them insensitive to action dependencies and vulnerable to superficial code variations. We propose a \emph{world-model-inspired} evaluator that models schedule evaluation as action-conditioned latent dynamics over program states. Starting from the initial program, it rolls out scheduling actions in a continuous latent space with a lightweight transition model, avoiding expensive AST mutation and repeated code encoding. The final dynamic representation is combined with action and hardware features to rank candidates. Implemented in TVM AutoScheduler, our method improves representative-subgraph latency over Ansor by 1.37$\times$ on GPU and 1.54$\times$ on CPU under the same 64-trial budget. It also matches Ansor-10K within 2.2% geometric mean using 10$\times$ fewer measurements, and accelerates full-model inference over PyTorch/PyTorch-opt(cuDNN) by 4.61$\times$/3.67$\times$ geometric mean.
匹配关键词: PyTorch
---

[ACADEMIC - ARXIV]
标题: Q-Delta: Beyond Key-Value Associative State Evolution
作者: Sumin Park, Seojin Kim, Noseong Park
链接: https://arxiv.org/abs/2606.08804v1
完整摘要: Linear attention reformulates sequence modeling as recurrent state evolution, enabling efficient linear-time inference. Under the key-value associative paradigm, existing approaches restrict the role of the query to the readout operation, decoupling it from state evolution. We show that query-conditioned state readout induces a structured value prediction over accumulated memory that complements key-based retrieval. Based on this insight, we propose Q-Delta, a query-aware delta rule that integrates mixed key-query prediction errors into state evolution, enabling jointly corrective dynamics while preserving delta-rule efficiency. We establish stability guarantees for the resulting dynamics and derive a hardware-efficient chunkwise-parallel formulation with a custom Triton implementation. Empirical results demonstrate stable optimization, competitive throughput, and consistent improvements over strong baselines on language modeling and long-context retrieval tasks.
匹配关键词: Triton
---

[ACADEMIC - ARXIV]
标题: STAR-KV: Low-Rank KV Cache Compression via Soft Thresholding for Adaptive Rank Control
作者: Priyansh Bhatnagar, Ashkan Moradifirouzabadi, Se-Hyun Yang, SeungJae Lee, Jungwook Choi, Mingu Kang
链接: https://arxiv.org/abs/2606.08382v1
完整摘要: Low-rank projection has emerged as a promising approach for compressing the KV cache by exploiting hidden-dimension redundancy. However, prior methods rely on fixed or heuristic rank selection and struggle to achieve aggressive compression with minimal accuracy degradation. We propose STAR-KV, an adaptive low-rank KV cache compression framework with fine-grained rank control. STAR-KV encompasses 1) a differentiable thresholding mechanism that enables optimal rank selection at both attention-head and block levels, 2) a hybrid decomposition strategy that applies different low-rank factorizations according to the sensitivity of key and value projections, and 3) a low-rank-aware mixed precision quantization that leverages data statistics for near lossless low-bit quantization. Evaluated across multiple LLMs and benchmarks, STAR-KV achieves up to 75% KV cache compression and up to 20x overall KV cache reduction when combined with quantization. Enabled by custom Triton-based GPU kernels, STAR-KV delivers up to 6.9x speedup for the attention module and 3.1x end-to-end generation throughput. Our code is publicly available at: https://github.com/PriyanshBhatnagar/STAR-KV.
匹配关键词: Triton
---

[ACADEMIC - ARXIV]
标题: Dynamic Short Convolutions Improve Transformers
作者: Oliver Sieberling, Bharat Runwal, Rameswar Panda, Yoon Kim
链接: https://arxiv.org/abs/2606.03825v1
完整摘要: Transformers have become the dominant architecture for large language models, largely due to the scalability and flexibility of attention, feed-forward layers, residual connections, and normalization. This paper introduces dynamic short convolutions as an additional neural network primitive for improving Transformers. Unlike static short convolutions, dynamic convolutions use input-dependent filters, which preserves the locality bias of convolution while increasing expressivity. Motivating experiments show that applying dynamic short convolutions to key, query, and value representations improves performance on challenging associative recall tasks compared with static convolutional variants. Across language-modeling experiments ranging from 150M to 2B parameters, dynamic convolutions consistently outperform standard Transformers and Transformers augmented with static short convolutions. Fitting scaling laws indicates a 1.33$\times$ compute advantage over compute-matched Transformers when dynamic convolutions are applied to the key, query, and value vectors, and a 1.60$\times$ advantage when adding dynamic convolutions after every linear layer. Dynamic convolutions also offer improvements on linear RNNs (Mamba-2/Gated DeltaNet) and mixture-of-experts architectures. We make these gains practical with custom Triton kernels that enable efficient training with a manageable end-to-end slowdown. These results suggest that dynamic short convolutions are a scalable, hardware-efficient, and expressive primitive for advancing Transformer-based language models.
匹配关键词: Triton
---

[ACADEMIC - ARXIV]
标题: KForge: LLM-Driven Cross-Platform Kernel Generation for AI Accelerators
作者: Taras Sereda, Burak Bartan, Ankita Nayak, Tom St. John, Natalie Serrino, Zain Asgar
链接: https://arxiv.org/abs/2606.02963v1
完整摘要: Production inference increasingly targets a heterogeneous mix of accelerators. Agentic pipelines interleave reasoning, tool calls, and multi-agent coordination, each with distinct compute and memory profiles. For optimal efficiency, each stage should run on the accelerator best suited to it. This creates a systems challenge: each pipeline now requires high-performance kernels across a growing set of hardware backends and programming models. Writing these kernels by hand is time-consuming, demands deep low-level expertise, and does not scale as kernel complexity grows. Recently, Large Language Models (LLMs) have been leveraged for automatic kernel generation, but challenges in low-level code generation and cross-backend generalization persist. We present KForge, a cross-platform framework built around an iterative refinement loop driven by two collaborating LLM-based agents: a generation agent that produces and progressively refines kernels using compilation and correctness feedback, and a performance-analysis agent that interprets profiling data, from programmatic APIs to GUI-based tools, and emits recommendations that steer the next round of synthesis. The loop alternates between functional passes, which drive a candidate to correctness, and optimization passes, which close the performance gap to hand-tuned baselines. We evaluate KForge on two backends with very different baseline reference availability. On NVIDIA B200, KForge achieves a 2.12$\%$ improvement in end-to-end throughput compared to TensorRT-LLM on the gpt-oss-20b inference speed benchmark. On Intel Arc B580, KForge generates Triton kernels achieving a 5.13$\times$ geometric mean speedup over the faster of PyTorch eager and torch.compile on 37 GEMM + tail-ops workloads from KernelBench Level 2, primarily via operator fusion and mixed-precision execution.
匹配关键词: Triton
---

[ACADEMIC - ARXIV]
标题: Light Interaction: Training-Free Inference Acceleration for Interactive Video World Models
作者: Jiacheng Lu, Haoyi Zhu, Sipei Yi, Enze Xie, Yu Li, Cheng Zhuo
链接: https://arxiv.org/abs/2605.31158v2
完整摘要: Interactive video world models generate video chunk by chunk in response to user-controlled camera movements, enabling applications such as real-time game simulation, virtual scene navigation, and embodied AI training. However, scaling to long interactive trajectories is prohibitively expensive due to growing context memory, quadratic attention complexity, and repeated denoising steps. We present Light Interaction, a training-free inference acceleration framework for interactive video world models. Our key insight is that interaction naturally enables trajectory-dependent adaptive computation: retrieved spatial memory can be discarded during novel exploration, temporal context can be adjusted according to local latent dynamics, and early-step model outputs can be reused when the camera revisits familiar regions. Based on this insight, Light Interaction combines adaptive context management, denoising cache acceleration, and hardware-software co-designed 3D block sparse attention with fused Triton kernels. Evaluated on HY-WorldPlay and Matrix-Game-3.0, Light Interaction achieves up to 2.59x speedup without model retraining while maintaining competitive visual quality.
匹配关键词: Triton
---

[ACADEMIC - ARXIV]
标题: Benchmarking Open-Ended Multi-Agent Coordination in Language Agents
作者: Kale-ab Abebe Tessera, Andras Szecsenyi, Cameron Barker, Alexander Rutherford, Davide Paglieri, Aidan Scannell, Henry Gouk, Elliot J. Crowley, Tim Rocktäschel, Amos Storkey
链接: https://arxiv.org/abs/2606.08340v1
完整摘要: As language models are increasingly deployed as autonomous agents, they must coordinate with others over long horizons in open-ended interactive tasks. Yet existing evaluations rarely test these demands together, instead emphasising single-agent tasks, short interactions, or highly structured multi-agent settings. We introduce $alem$, a JAX-based benchmark for open-ended multi-agent coordination built on Craftax-like dynamics. Alem embeds procedurally generated coordination tasks, soft specialisation, communication, and controllable coordination difficulty into a long-horizon survival world with exploration, crafting, trading, and combat. We evaluate $13$ modern LLMs zero-shot within homogeneous teams, with trained MARL agents as reference points. Current LLM agents remain far from solving alem, averaging only ~6% normalised return, but their failures are not uniform. On the hardest coordination setting, zero-shot Gemini-3.1-Pro-High approaches MARL agents trained for one billion steps, while GPT-5.4-High achieves strong base-task reward but much lower coordination reward. This contrast shows that individual task competence does not imply coordination competence. Ablations show that communication is the largest contributor to coordination, while memory and reasoning help when used to maintain multi-step plans. Overall, our results identify coordination as a distinct bottleneck for frontier LLM agents, separate from single-agent capabilities. Alem makes this bottleneck measurable and provides a controlled testbed for developing agents that communicate, allocate roles, and execute shared plans. Code is available at https://github.com/alem-world/alem-env.
匹配关键词: JAX
---

[ACADEMIC - ARXIV]
标题: Systematic LLM Translation of Legacy Scientific Code to Differentiable Frameworks: Application to a Land Surface Model
作者: Aya Lahlou, Linnia Hawkins, Pierre Gentine
链接: https://arxiv.org/abs/2606.07681v1
完整摘要: Differentiable programming offers transformative capabilities for scientific modeling, enabling gradient-based parameter estimation, sensitivity analysis, and data assimilation. Yet, migrating legacy codebases into differentiable frameworks remains a challenge. We present a five-phase LLM-based agentic pipeline that translates legacy Fortran into JAX: static dependency analysis determines module translation order from the full call graph; iterative compile-repair loops correct errors autonomously; and a Fortran reference oracle enforces numerical parity at the module level before integration and gradient verification. We instantiate and evaluate the pipeline on CLM-ml-v2, a 19,000-line Fortran land surface model, and analyze agent behavior across 73 module translation tasks. The resulting differentiable model computes the complete Jacobian in a single backward pass, recovers physical parameters in eight times fewer steps than gradient-free optimization, and achieves a 24 times wall-clock speedup over sequential Fortran at ensemble size N=2,048. Both the translated model and pipeline infrastructure are released as a reusable framework for differentiating other Earth system model components.
匹配关键词: JAX
---

[ACADEMIC - ARXIV]
标题: Accelerated Fourier SAT (AFSAT): Fully Realising a GPU-based Symmetric Pseudo-Boolean SAT Solver
作者: Cody J Christopher, Charles Gretton
链接: https://arxiv.org/abs/2606.06641v1
完整摘要: We present Accelerated Fourier SAT (AFSAT), a GPU-accelerated solver for pseudo-Boolean satisfiability based on continuous local search (CLS). AFSAT realises the proof-of-concept approach, FastFourierSAT, into a fully-engineered solver supporting any heterogeneous mixture of symmetric constraint types and lengths within a single problem instance. Using the JAX compiler, AFSAT leverages pure function composition, automatic vectorisation, automatic differentiation, and just-in-time (JIT) compilation to perform massively parallel CLS across batches of candidate assignments. We demonstrate substantially improved numerical stability, runtime performance, and memory efficiency over the proof-of-concept. We achieve this by way of identifying and addressing various limitations that arise from memory latency and floating-point representation, as well as leveraging automatic parallelisation and compact representations. The inherent representational and stability limitations of floating point are partially addressed by a tailored discrete Fourier transform implementation. We achieve near-linear throughput when scaling to multiple accelerators via JAX array sharding.
匹配关键词: JAX
---

[ACADEMIC - ARXIV]
标题: The Differentiable Auditory Loop (DAL): An ML Framework for Hyper-Personalized Hearing Aids
作者: Alejandro Ballesta Rosen, Jason Mikiel-Hunter, Julian Maclaren, Jack Collins, Richard F. Lyon, Simon Carlile
链接: https://arxiv.org/abs/2606.04103v1
完整摘要: Conventional hearing aids rely on fixed, frequency-dependent amplification and compression to manage reduced sensitivity, which often fails to provide sufficient listening support in complex environments, such as situations with multiple speakers (the ``cocktail party'' problem). To more comprehensively address the underlying encoding dysfunctions of hearing loss, we introduce the Differentiable Auditory Loop (DAL), a new open-source framework for personalized hearing aid design and fitting. Our first implementation of DAL incorporates CARFAC, a differentiable model of human cochlear function, which we ported to JAX, to optimize a deep neural network to match impaired auditory neural activity patterns with a normal-hearing reference. To build a hearing aid with the fine-grained spectro-temporal signal processing required, we adopt SEANet, a waveform-to-waveform fully convolutional UNet generator. We fine-tune the network by comparing the outputs of a CARFAC model fitted to normal hearing with that of a CARFAC model fitted to match each subject's individual hearing impairment. The comparison is done using loss functions derived from the respective CARFAC neural activity pattern (NAP) outputs and stabilized auditory images (SAIs), the latter providing a 2D representation that captures phase-insensitive temporal structure in the auditory nerve output. Through gradient descent, the SEANet model learns to both denoise the input and compensate for the hearing loss modelled by the impaired CARFAC model. Across neural-representation and signal-fidelity metrics, the DAL-optimized SEANet model outperformed the tested master hearing aid (MHA) baselines. The DAL framework provides a practical path toward model-based, machine-learning-driven personalization of hearing aid signal processing. Next steps include hardware deployment to enable real-world clinical testing.
匹配关键词: JAX
---

[ACADEMIC - ARXIV]
标题: Crazyflow: An Accurate, GPU-Accelerated, Differentiable Drone Simulator in JAX
作者: Martin Schuck, Marcel P. Rath, Yufei Hua, Abhishek Goudar, SiQi Zhou, Angela P. Schoellig
链接: https://arxiv.org/abs/2606.01478v2
完整摘要: High-quality, large-scale synthetic data from simulations is becoming a cornerstone for pushing the capabilities of robot algorithms. While aerial robotics simulators have evolved to support specialized needs such as fidelity, differentiability, and swarms independently, a unified platform that can synthesize data across all these domains is missing. In this work, we propose Crazyflow, a simulator designed to push the limits of aerial-robotics algorithm development, from model-based to data-driven methods, gradient-based to sampling-based approaches, and single-agent to multi-agent systems. Compared to existing state-of-the-art drone simulators, it achieves speeds more than an order of magnitude faster for a single drone and can simulate thousands of swarms of 4000 drones each. Real-world experiments show Crazyflow supports both analytical-gradient-based policy learning, achieving sub-centimeter trajectory tracking accuracy without domain randomization, and sampling-based obstacle avoidance at speeds exceeding half a billion steps per second. Breaking the traditional train-then-deploy paradigm, we show that its unprecedented speed even enables in-flight reinforcement learning; we demonstrate this by throwing a physical drone into the air and training a recovery policy from scratch in 0.38 seconds, successfully stabilizing the drone. Crazyflow supports multiple levels of simulation abstraction, is directly compatible with all open-source Crazyflie models, and enables rapid reconfiguration across custom drone platforms and applications by providing a light-weight system identification pipeline. By pushing accuracy, speed, and differentiability simultaneously, Crazyflow serves as an open-source resource for synthetic data generation, with emerging capabilities for large-scale parallelization for online, in-execution learning and optimization, opening the door to novel algorithm development.
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
标题: Heterogeneous Parallelism for Multimodal Large Language Model Training
作者: Yashaswi Karnati, Kamran Jafari, Akash Mehra, Li Ding, Pranav Prashant Thombre, Ali Roshan Ghias, Shifang Xu, Parth Mannan, Yu Yao, Hao Wu, Eric Harper, Ashwath Aithal, Nima Tajbakhsh
链接: https://arxiv.org/abs/2605.27678v1
完整摘要: Foundation model training is becoming multimodal, from post-training pipelines to large-scale pretraining. As modality coverage broadens, context windows grow, and encoder LLM scales diverge, a single LLM-centric TP/CP/PP/DP/EP layout increasingly limits throughput. This coupling forces encoders to inherit LLM-driven sharding and placement choices that can add communication, limit encoder parallelism, or constrain the LLM schedule; the mismatch is most pronounced at long contexts, where LLM context parallelism is needed for the fused multimodal sequence but encoder inputs remain bounded. We present heterogeneous parallelism for multimodal large language model training, an abstraction that lets modules in one end-to-end graph use independent layouts and rank placements, supporting colocated execution on shared GPUs and non-colocated execution on disjoint rank sets. The key challenge is preserving boundary tensor semantics across independent layouts: forward activations must be materialized for the destination layout, while backward gradients must be routed back to the source layout. We address this with boundary communicators that implement forward and backward layout transforms, plus scheduling extensions for both placement modes. We evaluate optimized homogeneous, colocated heterogeneous, and non-colocated heterogeneous configurations across multimodal workloads and GPU scales to characterize when added layout and placement freedom exposes a better operating point. Across this sweep, colocated heterogeneity improves TFLOPS/GPU by up to 49.3%, while non-colocated heterogeneity improves aggregate token throughput by up to 13.0% and TFLOPS/GPU by up to 9.6%. We validate loss convergence parity against homogeneous baselines and release the system as an open-source Megatron-LM extension.
匹配关键词: Megatron
---

[ACADEMIC - ARXIV]
标题: A Readiness-Driven Runtime for Pipeline-Parallel Training under Runtime Variability
作者: Ruitao Liu, Xinyang Tian, Shuo Chen, Tingrui Zhang, Guang Yang, Alan Zhao, Wei Xu
链接: https://arxiv.org/abs/2605.18750v1
完整摘要: Pipeline parallelism is a key technique for scaling large-model training, but modern workloads exhibit runtime variability in computation and communication. Existing pipeline systems typically consume static, profiled, or adaptively generated schedules as pre-committed execution orders. When realized task readiness diverges from the pre-committed order, stages may wait for not-yet-ready work even though other executable work is available, creating stage misalignment, idle bubbles, and reduced utilization. We present Runtime-Readiness-First Pipeline (RRFP), a readiness-driven runtime for pipeline-parallel training. RRFP changes how schedules are consumed at runtime: instead of treating a schedule as a sequence that stages must wait to follow, it treats the schedule as a non-binding hint order for ranking currently ready work. To support this model, RRFP combines message-driven asynchronous communication, lightweight tensor-parallel coordination for collective consistency, and ready-set arbitration for low-overhead dispatch. We implement RRFP in a Megatron-based training framework and evaluate it on language-only and multimodal workloads at up to 128 GPUs. RRFP improves over fixed-order pipeline baselines across all settings. Using the BFW hint, RRFP achieves up to 1.77$\times$ speedup on language-only workloads and up to 2.77$\times$ on multimodal workloads. In cross-framework comparisons, RRFP with the default BF hint outperforms the faster available external system by up to 1.84$\times$ while preserving training correctness.
匹配关键词: Megatron
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
标题: APEX4: Efficient Pure W4A4 LLM Inference via Intra-SM Compute Rebalancing
作者: Hong Guo, Nianhui Guo, Weixing Wang, Jona Otholt, Christoph Meinel, Haojin Yang
链接: https://arxiv.org/abs/2606.08761v1
完整摘要: W4A4 quantization promises full utilization of INT4 Tensor Cores, yet group dequantization overhead on CUDA Cores has driven existing systems to mixed-precision fallbacks. We present the first systematic study of how intra-SM compute balance governs this bottleneck. Through controlled benchmarks across four GPUs from Ampere and Ada architectures, we identify the Tensor Cores to CUDA Cores throughput ratio ($ρ$) as the primary hardware indicator: the W4A4-g128 kernel yields $2.0$--$2.5\times$ speedup on RTX~3090 ($ρ=16$) yet degrades to $0.43$--$0.47\times$ on A100 ($ρ=64$) in compute-bond scenarios, establishing W4A4 viability as platform-dependent rather than universally infeasible. Guided by this finding, we build \textbf{APEX4}, which co-designs pure INT4 GEMM kernels with $ρ$-aware granularity adaptation to mitigate the CUDA Cores dequantization bottleneck. APEX4 achieves perplexity within 0.63 of FP16 on LLaMA-2-70B and outperforms W4Ax Atom-g128 by 4.0\%--4.4\% in zero-shot accuracy. Deployed as a drop-in replacement in unmodified vLLM, it delivers up to $1.66\times$ end-to-end speedup on L40S ($ρ=8$), and $1.78\times$ on RTX~3090 ($ρ=16$), $2.09\times$ on A40 ($ρ=16$), while recovering A100 ($ρ=64$) to $1.20$--$1.40\times$ via the mixed-granularity mode.
匹配关键词: vLLM
---

[ACADEMIC - ARXIV]
标题: Breaking the Ice: Analyzing Cold Start Latency in vLLM
作者: Huzaifa Shaaban Kabakibo, Animesh Trivedi, Lin Wang
链接: https://arxiv.org/abs/2606.07362v1
完整摘要: As scalable inference services become popular, the cold start latency of an inference engine becomes important. Today, vLLM has evolved into the de facto inference engine of choice for many inference workloads. Although popular, due to its complexity and rapid evolution, there has not been a systematic study of its startup latency. With major architectural innovations such as the V1 API and the introduction of torch.compile, this paper presents the first detailed performance characterization of vLLM startup latency. We break down the startup process into six foundational steps and demonstrate that it is predominantly CPU bound. Each step exhibits consistent and interpretable scaling trends with respect to model-level and system-level parameters, enabling fine-grained attribution of latency sources. Building on these insights, we develop a lightweight analytical model that accurately predicts vLLM startup latency for a given hardware configuration, providing actionable guidance for resource planning in large-scale inference environments. All benchmarking datasets, analysis tools, and prediction scripts are open sourced at https://github.com/upb-cn/vllm-startup-profiler.
匹配关键词: vLLM
---

[ACADEMIC - ARXIV]
标题: YouZhi: Towards High-Concurrency Financial LLMs via Adaptive GQA-to-MLA Transition
作者: PSBC LLM Team, Huawei LLM Team, Ruihan Long, Junjie Wu, Tianan Zhang, Duo Zhang, Yaozong Wu, Jinbin Fu, Chang Liu, Zhentao Tang, Wenshuang Yang, Xin Wang, Zhihao Song, Ning Huang, Wenjing Xu, Shuai Zong, Shupei Sun, Sen Wang, Jing Hu, Bin Wang, Xinyu Wang, Junkui Ju, Zequn Ding, Jie Ran, Man Luo, Shixiong Kai, Linkai Hou, Kaichao Liang, Hu Zhao, Yang Zhao, Shucheng Lin, Wei Yu, Chenghan Jiang, Jingjing Ding, Jiahui Zhang, Tian Jin, Yuhang Zhang, Dong Guo, Wei Sun, Jun Xie, Jianwei Li, Lei Cao, Pei Li, Jiabin Li, Jia Yuan, Rui Yuan, Jing Zhu, Mingxuan Yuan, Zhangcheng Lv, Xin Jiang, Xiuhong Fei, Xiaozhe Ren, Yulong Li, Zhipeng Zhang, Hang Wang, Zhaohui Xu, Rui Zhao, Yibo He, Xinzhuang Niu
链接: https://arxiv.org/abs/2606.05868v1
完整摘要: Large language models (LLMs) drive significant financial innovations, yet their high-concurrency deployment is severely bottlenecked by KV cache memory overhead, which inflates infrastructure costs and throttles scalability. To address this, we propose YouZhi-LLM, a highly efficient financial LLM empowered by a comprehensive structural transition and training pipeline natively built on the Huawei Ascend ecosystem. At its algorithmic core, YouZhi-LLM features a layer-adaptive GQA-to-MLA transition framework that dynamically assigns per-layer FreqFold sizes, maximizing KV-cache compression while minimizing perplexity degradation. To recover representation capacity and inject domain expertise, the Ascend-based training pipeline seamlessly integrates generalized knowledge distillation with financial-specific supervised fine-tuning. Evaluations demonstrate the superiority of this systematic approach, with the adaptive transition reducing perplexity degradation by up to 35% over uniform baselines. Crucially, when evaluated on Ascend NPUs via vLLM-Ascend, the massive KV-cache reduction translates directly into deployment efficiency. Compared to their respective base models, YouZhi-7B yields a 12.3% improvement in average financial benchmark score alongside a 2.69$\times$ increase in maximum concurrency; similarly, YouZhi-14B achieves a 7.0% accuracy gain and a 2.43$\times$ concurrency boost, establishing a new paradigm for cost-effective, high-throughput financial inference.
匹配关键词: vLLM
---

[ACADEMIC - ARXIV]
标题: KVarN: Variance-Normalized KV-Cache Quantization Mitigates Error Accumulation in Reasoning Tasks
作者: Lorenz K. Muller, Philippe Bich, Chiara Boretti, Hyun-Min Chang, Jiawei Zhuang, Lukas Cavigelli
链接: https://arxiv.org/abs/2606.03458v1
完整摘要: Test-time scaling is a powerful approach to obtain better reasoning in large language models, but it becomes memory-bottlenecked during long-horizon decoding, as the KV-cache grows. KV-cache quantization can help improve this, but current methods are evaluated under prefill-like settings and errors behave differently under autoregressive decoding. We show that in the latter regime, quantization errors accumulate across timesteps, driven primarily by incorrect token scales. We introduce KVarN, a calibration-free KV-cache quantizer that applies a Hadamard rotation followed by a dual-scaling variance normalization across both axes of the K and V matrices. We find that this combination fixes outlying token-scale errors and substantially reduces error accumulation over existing baselines. KVarN establishes a new state-of-theart for KV-cache quantization on generative benchmarks, including MATH500, AIME24 and HumanEval, at 2-bit precision. A vLLM implementation of the KVarN method is available at https://github.com/huawei-csl/KVarN
匹配关键词: vLLM
---

[ACADEMIC - ARXIV]
标题: DriftSched: Adaptive QoS-Aware Scheduling under Runtime Token Drift for Multi-Tenant GPU Inference
作者: Kathiravan Palaniappan
链接: https://arxiv.org/abs/2606.02982v1
完整摘要: The rapid growth of large language model (LLM) inference services has increased the demand for efficient multi-tenant GPU scheduling. While modern inference runtimes such as vLLM improve throughput through continuous batching and optimized memory management, accurately estimating the runtime cost of heterogeneous inference requests remains a significant challenge. In practice, observed output lengths often deviate from admission-time estimates, creating runtime token drift that can lead to workload misclassification, queue imbalance, increased tail latency, and degraded Quality-of-Service (QoS). This paper presents DriftSched, an adaptive QoS-aware scheduling framework for multi-tenant LLM inference serving on NVIDIA L4 GPUs. DriftSched combines workload classification, token-budget estimation, tenant-aware queue management, and runtime feedback-driven drift compensation to improve admission-time scheduling decisions. The framework evaluates FIFO, Priority, Weighted, Shortest-Job-First (SJF), and Aging Priority scheduling policies under heterogeneous multi-tenant workloads. Experimental results demonstrate measurable runtime token drift across workload categories. Adaptive bias correction reduces workload estimation error by an average of 38.8% (MAE) and 40.5% (RMSE), improving workload classification stability and scheduling accuracy. Among all evaluated schedulers, SJF achieves the best overall performance, reducing median end-to-end latency by approximately 42% and P99 latency by approximately 16% relative to FIFO under sustained GPU contention. The work contributes an adaptive drift-aware scheduling architecture, a runtime token-drift compensation mechanism, and a reproducible benchmarking framework for evaluating QoS-aware LLM inference scheduling on shared GPU infrastructure.
匹配关键词: vLLM
---

[ACADEMIC - ARXIV]
标题: LogNEO: A GPT-Neo Reinforcement Learning Framework for Accurate Real-Time Log Anomaly Detection
作者: David Eje, Tanmay Sharma, Khush Patel, Manuel Mazzara, Leonard Johard
链接: https://arxiv.org/abs/2606.08153v1
完整摘要: Detecting anomalies in large-scale system logs is critical for the reliability and security of modern computing infrastructure. We present LogNEO, a log anomaly detector built on EleutherAI's GPT-Neo (1.3B parameters) and fine-tuned with a novel partial-credit, exponentially decaying position-aware reward scheme combined with cross-entropy regularisation via Proximal Policy Optimisation (PPO). The position-aware reward explicitly models prediction difficulty: early positions receive higher rewards for correct predictions, while later positions incur stronger penalties for errors. LogNEO attains F1-scores of 0.927, 0.913, and 0.984 on the HDFS, BGL, and Thunderbird benchmarks, improving recall by up to 6 percentage points over the prior state-of-the-art LogGPT while maintaining comparable precision. A production microservice deployment over Apache Kafka, Redis, and TensorRT-accelerated inference demonstrates 45 ms end-to-end latency at 15,000 events per second.
匹配关键词: TensorRT
---

[ACADEMIC - ARXIV]
标题: Aqua Boundary-Saliency Attention Module for Lightweight Underwater Salient Instance Segmentation Detection Transformer
作者: M. Fazri Nizar, Julian Supardi, Muhammad Naufal Rachmatullah
链接: https://arxiv.org/abs/2606.08002v1
完整摘要: Underwater instance segmentation integrates pixel-level mask prediction and instance-level discrimination for marine resource exploration, ecological monitoring, and underwater robotic perception. Recent prompt-based and auxiliary-modality methods improve mask quality, but their reliance on large foundation models, prompt generation, or extra modality estimation complicates efficient deployment. This work introduces Lightweight Underwater Salient Instance Segmentation Detection Transformer (LUSIS-DETR), a compact detection-transformer framework built around the Aqua Boundary-Saliency Attention Module (AquaBSAM). AquaBSAM embeds underwater boundary, contrast, attenuation, chroma, dark-channel, and center-prior cues into DINOv2-initialized multi-scale features through bounded residual modulation, while auxiliary mask supervision and small-object copy-paste are training-only. Extensive evaluation on four recent underwater instance segmentation datasets, UIIS, UIIS10K, USIS10K, and USIS16K, shows competitively leading performance against previous state-of-the-art works across category-aware and salient-instance protocols. TensorRT half-precision (FP16) benchmarking on an NVIDIA T4 graphics processing unit (GPU) achieves 4.31-6.34 milliseconds (ms) latency, supporting real-time inference under an accessible reproduction setting.
匹配关键词: TensorRT
---

[ACADEMIC - ARXIV]
标题: Real-Time Industrial Defect Detection on Edge Hardware Using Fine-Tuned YOLOv8: A Systematic Benchmark on the NEU Surface Defect Database and MVTec AD with Automotive & Battery Manufacturing Extensions
作者: Emmanuel Ezeji Somtochukwu, Nitesh Rijal
链接: https://arxiv.org/abs/2606.07659v1
完整摘要: Automated surface defect detection is critical for ensuring rigorous quality control in high-speed manufacturing environments. While deep learning models offer remarkable accuracy, deploying them on resource-constrained edge hardware without introducing significant latency remains a persistent challenge. This paper presents Industrial-YOLO, an edge-optimized framework built upon a fine-tuned YOLOv8 architecture specifically engineered for real-time industrial defect detection. We conduct a systematic benchmark utilizing the NEU surface defect database for steel sheets and the MVTec AD dataset, supplemented with custom automotive manufacturing extensions representing real-world structural anomalies (scratches, pits, and inclusions). To bridge the gap between algorithmic complexity and edge hardware constraints, target-specific optimizations are introduced via TensorRT and OpenVINO acceleration engines. Experimental results demonstrate that Industrial-YOLO achieves a high-velocity inference speed exceeding 120 FPS on the NVIDIA Jetson Orin platform while maintaining an exceptional mean Average Precision (mAP) of 98.5%. The proposed framework showcases highly robust, zero-latency performance when deployed directly onto an active automotive assembly line, offering a scalable blueprint for next-generation automated optical inspection (AOI) systems.
匹配关键词: TensorRT
---

[ACADEMIC - ARXIV]
标题: Ultralytics YOLO26: Unified Real-Time End-to-End Vision Models
作者: Glenn Jocher, Jing Qiu, Mengyu Liu, Shuai Lyu, Fatih Cagatay Akyon, Muhammet Esat Kalfaoglu
链接: https://arxiv.org/abs/2606.03748v1
完整摘要: Real-time vision demands models that are accurate, efficient, and simple to deploy across diverse hardware. The YOLO family has become widely deployed for this reason, yet most YOLO detectors still rely on non-maximum suppression at inference, carry heavy detection heads due to Distribution Focal Loss, require long training schedules, and can leave the smallest objects without positive label assignments. We present Ultralytics YOLO26, a unified real-time vision model family that addresses these limitations through coordinated architecture and training advances. YOLO26 uses a dual-head design for native NMS-free end-to-end inference and removes DFL entirely, yielding a lighter head with unconstrained regression range. Its training pipeline combines MuSGD, a hybrid Muon-SGD optimizer adapted from large language model training; Progressive Loss, which shifts supervision toward the inference-time head; and STAL, a label assignment strategy that guarantees positive coverage for small objects. Beyond detection, YOLO26 introduces task-specific head and loss designs for instance segmentation, pose estimation, and oriented detection, producing consistent gains across tasks and scales. The family spans five scales (n/s/m/l/x) and supports detection, instance segmentation, pose estimation, classification, and oriented detection in a single pipeline, with an open-vocabulary extension, YOLOE-26, for text-, visual-, and prompt-free inference. Across all scales, YOLO26 achieves 40.9-57.5 mAP on COCO at 1.7-11.8 ms T4 TensorRT latency, advancing the accuracy-latency Pareto front over prior real-time detectors, while YOLOE-26x reaches 40.6 AP on LVIS minival under text prompting. Code and models are available at https://github.com/ultralytics/ultralytics.
匹配关键词: TensorRT
---

[ACADEMIC - ARXIV]
标题: KForge: LLM-Driven Cross-Platform Kernel Generation for AI Accelerators
作者: Taras Sereda, Burak Bartan, Ankita Nayak, Tom St. John, Natalie Serrino, Zain Asgar
链接: https://arxiv.org/abs/2606.02963v1
完整摘要: Production inference increasingly targets a heterogeneous mix of accelerators. Agentic pipelines interleave reasoning, tool calls, and multi-agent coordination, each with distinct compute and memory profiles. For optimal efficiency, each stage should run on the accelerator best suited to it. This creates a systems challenge: each pipeline now requires high-performance kernels across a growing set of hardware backends and programming models. Writing these kernels by hand is time-consuming, demands deep low-level expertise, and does not scale as kernel complexity grows. Recently, Large Language Models (LLMs) have been leveraged for automatic kernel generation, but challenges in low-level code generation and cross-backend generalization persist. We present KForge, a cross-platform framework built around an iterative refinement loop driven by two collaborating LLM-based agents: a generation agent that produces and progressively refines kernels using compilation and correctness feedback, and a performance-analysis agent that interprets profiling data, from programmatic APIs to GUI-based tools, and emits recommendations that steer the next round of synthesis. The loop alternates between functional passes, which drive a candidate to correctness, and optimization passes, which close the performance gap to hand-tuned baselines. We evaluate KForge on two backends with very different baseline reference availability. On NVIDIA B200, KForge achieves a 2.12$\%$ improvement in end-to-end throughput compared to TensorRT-LLM on the gpt-oss-20b inference speed benchmark. On Intel Arc B580, KForge generates Triton kernels achieving a 5.13$\times$ geometric mean speedup over the faster of PyTorch eager and torch.compile on 37 GEMM + tail-ops workloads from KernelBench Level 2, primarily via operator fusion and mixed-precision execution.
匹配关键词: TensorRT
---

[ACADEMIC - ARXIV]
标题: APEX4: Efficient Pure W4A4 LLM Inference via Intra-SM Compute Rebalancing
作者: Hong Guo, Nianhui Guo, Weixing Wang, Jona Otholt, Christoph Meinel, Haojin Yang
链接: https://arxiv.org/abs/2606.08761v1
完整摘要: W4A4 quantization promises full utilization of INT4 Tensor Cores, yet group dequantization overhead on CUDA Cores has driven existing systems to mixed-precision fallbacks. We present the first systematic study of how intra-SM compute balance governs this bottleneck. Through controlled benchmarks across four GPUs from Ampere and Ada architectures, we identify the Tensor Cores to CUDA Cores throughput ratio ($ρ$) as the primary hardware indicator: the W4A4-g128 kernel yields $2.0$--$2.5\times$ speedup on RTX~3090 ($ρ=16$) yet degrades to $0.43$--$0.47\times$ on A100 ($ρ=64$) in compute-bond scenarios, establishing W4A4 viability as platform-dependent rather than universally infeasible. Guided by this finding, we build \textbf{APEX4}, which co-designs pure INT4 GEMM kernels with $ρ$-aware granularity adaptation to mitigate the CUDA Cores dequantization bottleneck. APEX4 achieves perplexity within 0.63 of FP16 on LLaMA-2-70B and outperforms W4Ax Atom-g128 by 4.0\%--4.4\% in zero-shot accuracy. Deployed as a drop-in replacement in unmodified vLLM, it delivers up to $1.66\times$ end-to-end speedup on L40S ($ρ=8$), and $1.78\times$ on RTX~3090 ($ρ=16$), $2.09\times$ on A40 ($ρ=16$), while recovering A100 ($ρ=64$) to $1.20$--$1.40\times$ via the mixed-granularity mode.
匹配关键词: CUDA
---

[ACADEMIC - ARXIV]
标题: Video-Rate Streaming Stylization on a Vision-Aware MLLM-Conditioned Edit Diffusion: Asymmetric Batched Inference on a Distilled UNet + MLLM Text Encoder
作者: Yoshiyuki Ootani
链接: https://arxiv.org/abs/2606.05981v1
完整摘要: Aggressive distillation of the diffusion U-Net inverts the per-frame bottleneck of real-time text-to-image pipelines: once the denoiser is a 4-step or 1-step distilled student, the text encoder becomes the critical path. This inversion is most acute in vision-aware edit diffusion, where the encoder is a multimodal large language model (MLLM). We study the case of a 0.39B distilled edit U-Net paired with a 2.13B MLLM text encoder (Qwen3-VL) and present a streaming pipeline targeted at this regime built around three engineering mechanisms: asymmetric side-stream / main-stream CUDA pipelining with batched text-encoder amortisation (and optional static-prompt caching), a compile-friendly ControlNet-LLLite reformulation that folds the entire U-Net + adapter stack into a single fused graph, and a periodic conditioning-refresh schedule with a hook subset that amortises the per-frame conditioning cost. On a single consumer RTX 3090 Ti at 512x512 the pipeline sustains 27.4 fps over a 480-frame run at batch size B=8 and 29.6 fps at B=16, with end-to-end p50 latency of approximately 0.5 and 1.0 seconds respectively; the same operating point measures 54.9 fps on RTX 4090 and 74.1 fps on RTX 5090. We report video-rate streaming throughput rather than interactive low latency, and locate our numbers against same-stack StreamDiffusion re-runs as systems context, not as a benchmark superiority claim. For the trained oil-painting style, the released temporal adapter generalises within in-clip noise to 19 unused DAVIS-2017 sequences and 15 non-DAVIS clips from seven sources; prompt-level generalisation to unseen style families is bounded and reported separately.
匹配关键词: CUDA
---

[ACADEMIC - ARXIV]
标题: AgentCompile: An LLM-Guided Compiler for Direct CUDA Inference
作者: Xuanzhe Li, Ziyan Weng, Zhiyu Zhu, Junhui Hou
链接: https://arxiv.org/abs/2606.07665v1
完整摘要: Transformer inference increasingly depends on specialized compiler and runtime support, but real model graphs still require semantic decisions about which regions are worth specializing and which CUDA implementation families are plausible. We present AgentCompile, an LLM-guided CUDA inference compiler that uses LLM outputs only as advisory search metadata. Given compiler-derived region summaries and bounded candidate spaces, the LLM proposes semantic labels, candidate priorities, parameter hints, and risk annotations; the compiler materializes CUDA candidates through templates, checks interface and hardware constraints, validates candidates empirically, selects implementations by measured latency, and falls back when specialization is unsupported or unprofitable. In end-to-end autoregressive generation, AgentCompile averages 5.66x, 4.05x, and 4.26x speedup over PyTorch eager on Qwen3-1.7B, Qwen3-4B, and Llama-3.2-1B-Instruct, respectively, across five representative workloads. We will open-source the project.
匹配关键词: CUDA
---

[ACADEMIC - ARXIV]
标题: AutoLab: Can Frontier Models Solve Long-Horizon Auto Research and Engineering Tasks?
作者: Zhangchen Xu, Junda Chen, Yue Huang, Dongfu Jiang, Jiefeng Chen, Hang Hua, Zijian Wu, Zheyuan Liu, Zexue He, Lichi Li, Shizhe Diao, Jiaxin Pei, Jinsung Yoon, Hao Zhang, Mengdi Wang, Radha Poovendran, Misha Sra, Alex Pentland, Zichen Chen
链接: https://arxiv.org/abs/2606.05080v1
完整摘要: Scientific and engineering progress is fundamentally a long-horizon iterative process: proposing changes, running experiments, measuring outcomes, and continuously refining artifacts. Yet existing benchmarks for frontier models primarily evaluate either single-turn responses or short-horizon agent trajectories, failing to capture the challenges of sustained iterative improvement over extended time horizons. To address this gap, we introduce AutoLab, a new benchmark for ultra long-horizon closed-loop optimization. AutoLab consists of 36 realistic, expert-curated tasks spanning four diverse domains: system optimization, puzzle & challenge, model development, and CUDA kernel optimization. Each task begins with a correct but deliberately suboptimal baseline and challenges agents to improve it within a strict wall-clock budget. Evaluating 17 state-of-the-art models reveals the dominant predictor of success is not the quality of an agent's initial attempt, but its persistence in repeatedly benchmarking, editing, and incorporating empirical feedback. While claude-opus-4.6 exhibits strong long-horizon optimization capabilities, most frontier models, including several proprietary ones, either terminate prematurely or exhaust their budgets with minimal progress. These results underscore the importance of time awareness and persistent iteration in autonomous agents. We open-source the full benchmark, evaluation harness, and task artifacts, to accelerate research toward truly capable long-horizon agents.
匹配关键词: CUDA
---

[ACADEMIC - ARXIV]
标题: MusaCoder: Native GPU Kernel Generation with Full-Stack Training on Moore Threads GPU
作者: Kun Cheng, Songshuo Lu, Sicong Liao, Tankun Li, Yafei Zhang, Dong Yang, Qiheng Lv, Hua Wang, Zhi Chen, Yaohua Tang
链接: https://arxiv.org/abs/2606.04847v1
完整摘要: Native GPU kernel generation turns high-level tensor programs into executable, efficient low-level code. Existing Large Language Models (LLMs) struggle with this task, while execution-based reinforcement learning suffers from sparse rewards, reward hacking, and training instability. We present MusaCoder, a full-stack training framework for native GPU kernel generation on CUDA and MUSA backends. MusaCoder combines progressive kernel-oriented data synthesis, diversity-preserving rejection fine-tuning, and execution-feedback Reinforcement Learning (RL) through MooreEval, a distributed verifier and reward environment. To stabilize RL, MusaCoder introduces PrimeEcho for first-turn-anchored multi-turn rewards, Buffered Dynamic Retry for recovering signals from all-failed hard samples, and MirrorPop for off-policy sequence filtering. Experiments on KernelBench and a MUSA-ported variant show that MusaCoder outperforms strong open-source and proprietary baselines in both correctness and empirical speedup, with the 9B model matching or exceeding frontier closed-source models and the 27B model establishing a new state of the art. These results demonstrate not only the effectiveness of full-stack execution-feedback training for native kernel generation, but also the capability of Moore Threads GPUs to support the complete LLM post-training stack, providing a practical foundation for large-model training and optimization on emerging accelerators.
匹配关键词: CUDA
---

[ACADEMIC - ARXIV]
标题: SoccerNet 2026 Player-Centric Ball-Action Spotting:Retraining and Post-Processing Extensions to the FOOTPASS Baselines
作者: Parthsarthi Rawat
链接: https://arxiv.org/abs/2606.09679v1
完整摘要: We describe our system for the SoccerNet 2026 Player-Centric Ball-Action Spotting Challenge, which requires predicting who performs which action and when, across eight classes in broadcast soccer. Building on the three FOOTPASS baselines [1] (TAAD, TAAD+GNN, and TAAD+DST), we contribute four extensions: (1) gradient check pointing to enable full-backbone fine-tuning on a single GPU; (2) fusion of GNN logits into the DST encoder, combining graph-based tactical context with per-player visual features; (3) square-root frequency class weighting to address the 213:1 pass-to-tackle imbalance in the training data; and (4) a post processing pipeline comprising per-class logit gating, temporal frame refinement, jersey re-assignment, and a two-model ensemble. Our system achieves 0.548 Macro F1 on the test set and 0.446 on the challenge set (server evaluation).
匹配关键词: distributed training
---

[ACADEMIC - ARXIV]
标题: (Auto)formalization is supposed to be easy: Trellis process semantics for spelling out rigorous proofs
作者: Wesley Pegden
链接: https://arxiv.org/abs/2606.09674v1
完整摘要: We present Trellis: an autoformalization system that leverages LLM agents in a deterministically constrained workflow to enforce incremental progress in Lean autoformalization tasks through iterative refinement of natural language proofs. Our approach is motivated by the common mathematician's notion of what it means to have a rigorous proof in the first place: namely, that it would be routine to elaborate any part of the proof in further detail. The result is a system which aims to achieve reliable autoformalization on a modest budget and with generalist agents, with specialization to autoformalization coming not from any task-specific agent training but instead from a meaning-of-rigor inspired workflow enforced by process semantics. We link to an end-to-end Lean formalization of a recent Ramsey theory breakthrough produced by the process.
匹配关键词: distributed training
---

[ACADEMIC - ARXIV]
标题: Correlation Is Not Enough: Embedding Human Metadata for Individual Causal Discovery
作者: Suraj Biswas, Saurabh Gupta, Pritam Mukherjee
链接: https://arxiv.org/abs/2606.09672v1
完整摘要: Ask a pretrained biomedical language model whether "cortisol 28 ug/dL" and "stock-market volatility" are related, and it returns a cosine similarity of 0.83 on a scale where 1.0 means identical. The two share no mechanism. This is not a corner case: every off-the-shelf biomedical encoder we tested (BioBERT, PubMedBERT, BioM-ELECTRA) scores unrelated cross-domain pairs between 0.76 and 0.92 when the answer should be near zero. Accuracy on cross-domain discrimination is 0%. Retrieval systems survive this, because a language model downstream filters the noise. A Large Behavioural Model (LBM), a foundation model whose subject is a person rather than a sentence, does not: it reasons over a graph of a user's life and treats embedding proximity as evidence that two events are causally linked. False proximity writes a false causal edge, and everything downstream inherits the error. Here, embedding geometry is not a tuning knob; it is correctness. We report the fix. A contrastive pass over 72,034 pairs raises PubMedBERT BIOSSES correlation from 0.633 to 0.828 and within-vs-across-domain separation from 1.05x to 1.63x. A second pass, BODHI, mines hard negatives from edges absent in a biomedical knowledge graph and lifts separation to 2.30x and the discrimination gap to +0.392, at a 4.5% BIOSSES cost. On an Intel Xeon 6737P with AMX, OpenVINO cuts single-query latency from 1367 ms to 10 ms (133x) and reaches 555 sentences/sec. One finding contradicts standard advice: FP16 beats INT8 on this silicon at every serving batch size, and we explain why. The same model on a no-AMX Ice Lake instance runs 13-27x slower. We release the benchmark suite, training corpora, the BODHI generator, and the OpenVINO scripts.
匹配关键词: distributed training
---

[ACADEMIC - ARXIV]
标题: Cross-Modal Masking for Robust Silent Speech Synthesis Using sEMG and Lipreading
作者: Eder del Blanco, David Gimeno-Gómez, Eva Navas, Carlos-D. Martínez-Hinarejos, Inma Hernáez
链接: https://arxiv.org/abs/2606.09667v1
完整摘要: Speech restoration through silent speech interfaces (SSIs) has emerged as a promising assistive technology for individuals with impaired or absent laryngeal voice production. Among non-invasive SSI modalities, surface electromyography (sEMG) and video-based lipreading provide complementary articulatory information, yet their integration for continuous speech synthesis remains underexplored. Moreover, existing multimodal approaches rarely address robustness to modality degradation or temporary sensor failure, limiting their applicability in realistic scenarios. In this work, we propose a masked multimodal speech synthesis framework that jointly leverages sEMG and lipreading signals through modality masking during training. Under multispeaker settings, the proposed approach reduces word error rate by up to 14 absolute percentage points compared to the strongest unimodal baseline. Experimental results not only show that masking strategies are critical for these performance gains and robustness under low-bitrate conditions, but also that they generalize better than degradation-specific data augmentations in the presence of modality absence conditions. Phone-level analyses further reveal complementary contributions across modalities, with particularly strong benefits for vowels and for specific consonant groups. Overall, these findings demonstrate the effectiveness and robustness of masked multimodal integration for silent speech synthesis, although adaptation to laryngectomized speakers remains an open research challenge.
匹配关键词: distributed training
---

[ACADEMIC - ARXIV]
标题: In-Context Learning for Latent Space Bayesian Optimization
作者: Tuan A. Vu, Harri Lähdesmäki, Julien Martinelli
链接: https://arxiv.org/abs/2606.09664v1
完整摘要: Bayesian optimization (BO) is a central tool for sample-efficient design, and latent-space Bayesian optimization (LSBO) extends it to structured objects such as molecules and proteins. In parallel, tabular foundation models such as TabPFN and TabICL now achieve state-of-the-art regression performance and are increasingly used as BO surrogates. Because their Bayesian behavior is induced by large synthetic pretraining collections, the composition of this pretraining distribution is crucial. LSBO creates a distinctive mismatch: the induced map from latent code to objective value differs markedly from the regression tasks used to train current in-context models. We address this mismatch by complementing the pretraining stage of tabular foundation model surrogates with synthetic optimization tasks defined on the latent space of a molecular VAE. The continued-pretraining objective features a regularizer that anchors the model to the original checkpoint, preserving its broad regression prior while avoiding overspecialization to the adaptation tasks. On held-out molecular optimization benchmarks, the resulting model achieves strong performance, supporting the relevance of LSBO-specific adaptation for in-context surrogates.
匹配关键词: distributed training
---

[ACADEMIC - ARXIV]
标题: SoccerNet 2026 Player-Centric Ball-Action Spotting:Retraining and Post-Processing Extensions to the FOOTPASS Baselines
作者: Parthsarthi Rawat
链接: https://arxiv.org/abs/2606.09679v1
完整摘要: We describe our system for the SoccerNet 2026 Player-Centric Ball-Action Spotting Challenge, which requires predicting who performs which action and when, across eight classes in broadcast soccer. Building on the three FOOTPASS baselines [1] (TAAD, TAAD+GNN, and TAAD+DST), we contribute four extensions: (1) gradient check pointing to enable full-backbone fine-tuning on a single GPU; (2) fusion of GNN logits into the DST encoder, combining graph-based tactical context with per-player visual features; (3) square-root frequency class weighting to address the 213:1 pass-to-tackle imbalance in the training data; and (4) a post processing pipeline comprising per-class logit gating, temporal frame refinement, jersey re-assignment, and a two-model ensemble. Our system achieves 0.548 Macro F1 on the test set and 0.446 on the challenge set (server evaluation).
匹配关键词: GPU optimization
---

[ACADEMIC - ARXIV]
标题: MeCo: One-Step MeanFlow-based Corrector for Multi-Channel Speech Separation
作者: Dohwan Kim, Jung-Woo Choi
链接: https://arxiv.org/abs/2606.09677v1
完整摘要: While discriminative models for multi-channel speech separation excel in reference-based metrics, they often exhibit suboptimal human listening quality. To address this, we propose a novel MeanFlow-based one-step generative corrector (MeCo). MeCo learns a conditional average velocity field to map discriminative estimates directly onto the clean speech manifold in a single step. To maximize one-step generation performance, we introduce Data-Space Optimization (DSO). DSO integrates an $\mathbf{x}_r$-loss, which penalizes prediction errors on longer displacement intervals to serve as a generative objective for human listening quality, with an Endpoint SI-SDR loss that directly optimizes terminal signal fidelity. Experiments demonstrate that MeCo achieves state-of-the-art (SOTA) performance with minimal computational overhead, simultaneously achieving superior signal fidelity and human listening quality in both in-domain and out-of-domain scenarios.
匹配关键词: GPU optimization
---

[ACADEMIC - ARXIV]
标题: Algorithm for Contextual Queueing Bandits with Rate-Optimal Queue Length Regret
作者: Seoungbin Bae, Dabeen Lee
链接: https://arxiv.org/abs/2606.09668v1
完整摘要: Contextual queueing bandits provide a framework for learning to schedule heterogeneous jobs under unknown context-dependent service rates. Under stochastic contexts, existing algorithms achieve $\widetilde{\mathcal{O}}(T^{-1/4})$ queue length regret, defined as the expected difference between the learner's and oracle's queue lengths at horizon $T$. In this paper, we improve this rate to $\widetilde{\mathcal{O}}(T^{-1/2})$. The key observation is that random exploration is needed only up to a carefully chosen cutoff round, rather than throughout the entire horizon. We propose CQB-$η$-2, a three-phase algorithm: (i) pure random exploration to construct an initial estimator, (ii) $η$-random exploration combined with a UCB rule to continue learning while maintaining negative drift, and (iii) pure UCB after the exploration cutoff. Our proof decomposes the queue length regret at the cutoff round. Before the cutoff, negative drift suppresses queue length differences caused by suboptimal choices. After the cutoff, the first two phases provide sufficient random exploration samples, ensuring that UCB decisions incur small departure-rate gaps. Combining these two bounds yields queue length regret of order $\widetilde{\mathcal{O}}(T^{-1/2})$. We further prove a minimax lower bound of order $Ω(T^{-1/2})$. The proof constructs two hard instances that are statistically indistinguishable up to the final service decision, and uses a queue-specific coupling argument to convert the resulting testing error into queue length regret. Together, our upper and lower bounds characterize the minimax dependence on the horizon $T$ up to logarithmic factors.
匹配关键词: GPU optimization
---

[ACADEMIC - ARXIV]
标题: In-Context Learning for Latent Space Bayesian Optimization
作者: Tuan A. Vu, Harri Lähdesmäki, Julien Martinelli
链接: https://arxiv.org/abs/2606.09664v1
完整摘要: Bayesian optimization (BO) is a central tool for sample-efficient design, and latent-space Bayesian optimization (LSBO) extends it to structured objects such as molecules and proteins. In parallel, tabular foundation models such as TabPFN and TabICL now achieve state-of-the-art regression performance and are increasingly used as BO surrogates. Because their Bayesian behavior is induced by large synthetic pretraining collections, the composition of this pretraining distribution is crucial. LSBO creates a distinctive mismatch: the induced map from latent code to objective value differs markedly from the regression tasks used to train current in-context models. We address this mismatch by complementing the pretraining stage of tabular foundation model surrogates with synthetic optimization tasks defined on the latent space of a molecular VAE. The continued-pretraining objective features a regularizer that anchors the model to the original checkpoint, preserving its broad regression prior while avoiding overspecialization to the adaptation tasks. On held-out molecular optimization benchmarks, the resulting model achieves strong performance, supporting the relevance of LSBO-specific adaptation for in-context surrogates.
匹配关键词: GPU optimization
---

[ACADEMIC - ARXIV]
标题: Muon Learns More Robust and Transferable Features than Adam
作者: Tianyu Ruan, Fengzhuo Zhang, Shuche Wang, Shihua Zhang
链接: https://arxiv.org/abs/2606.09658v1
完整摘要: Muon has recently emerged as a state-of-the-art optimizer for pretraining Large Language Models (LLMs) and vision classifiers. Despite its efficiency advantage over Adam and SGD, the feature-learning advantage of Muon remains unclear. This paper investigates Muon's feature-learning advantage through the lens of robustness and transferability. First, by evaluating pretrained models on corrupted images and texts, we show that features learned by Muon are consistently more robust than those learned by Adam and SGD across different architectures, including transformers and Convolutional Neural Networks (CNNs). Using trained layer-wise probes, we further show that this robustness advantage is reflected in larger logit margins across layers. Second, by training linear classifiers or fine-tuning full models from pretrained parameters on downstream tasks, we demonstrate that Muon-learned features transfer more effectively than those learned by Adam and SGD. This transferability advantage is further supported by the diversity of hidden states across layers, as measured by effective rank. Finally, in a representative classification problem with multi-component features, we prove that Muon attains larger margins and higher effective rank than Adam and SGD, providing theoretical support for our empirical findings.
匹配关键词: GPU optimization
---

[ACADEMIC - ARXIV]
标题: ATN3D: Density-Aware LiDAR-Radar Early 3D Object Detection Under Extreme Sparsity
作者: Debojyoti Biswas, Xianbiao Hu
链接: https://arxiv.org/abs/2606.09634v1
完整摘要: 3D object detection is the backbone of perception for automated vehicles (AV) and broader intelligent transportation systems applications. Long-range detection is challenging because sensing evidence is sparse; yet this ``long-range'' scenario is routine in traffic. Although >30m is often labeled long-range in computer vision, on roadways it affords only approx. 1-2s for perception and decision-making. Under such extreme sparsity, two core challenges arise. First, early multimodal fusion tends to discard sparsity information and inject noise from empty or falsely occupied cells, degrading long-range recall. Second, context-agnostic uniform channel supervision favors dense and near-range samples, leaving far and small objects under-optimized, delaying the earliest detection of distant objects. We propose ``Ask The Neighbor'' (ATN3D), a LiDAR-Radar framework tailored for sparse-range conditions. ATN3D introduces (i) Density-aware early fusion with cross-modal gating that conditions fusion on per-voxel density/sparsity and Radar evidence, (ii) Occupancy-gated neighborhood aggregation with circular kernels to aggregate only from credible cells, (iii) Evidence-conditioned channel self-attention to adapt channel weights with weather/range, and (iv) a Range-aware loss that re-balances classification and localization by distance, aligning training with distance-stratified evaluation. On the VoD benchmark across clear and foggy conditions, ATN3D surpasses strong baselines: +3.55% mAP in clear weather and +8.41% mAP under simulated heavy fog; for >30m objects, gains are +3.33% (clear) and +2.09% (heavy fog). These results indicate earlier and more reliable long-range detections under sparse sensing in on-road traffic.
匹配关键词: self-supervised
---

[ACADEMIC - ARXIV]
标题: Next-Token Prediction Learns Generalisable Representations of Sleep Physiology
作者: Jonathan F. Carter, Lionel Tarassenko
链接: https://arxiv.org/abs/2606.09605v1
完整摘要: Foundation models offer a promising route to compress multi-modal physiological signals into compact representations of human health, with broad applications across sleep medicine, cardiology, neurology and other healthcare domains. Existing models have typically been trained with masked-reconstruction or contrastive objectives. However, masked reconstruction may be poorly suited to the stochastic nature of these signals, while contrastive approaches rely on positive-pair definitions despite the semantic invariances of physiological signals being poorly understood. In this work, we show that next-token prediction is a simple and scalable alternative. We develop Hypnos, a multi-modal sleep foundation model trained using eight different sensing modalities (e.g. EEG, ECG, respiratory signals) drawn from over 20,000 overnight polysomnography recordings. We tokenize each modality into streams of discrete tokens using residual vector quantization, then train a large auto-regressive RQ-Transformer to jointly predict the next token across all modalities in parallel. After training, Hypnos can be applied to continuous streams of sensor data from any subset of supported modalities, generating embeddings for downstream tasks. Across a range of benchmarks, Hypnos significantly outperforms existing foundation models. In sleep stage classification, we match the performance of strong supervised baselines on held-out test sets whilst using \(100\times\) less labelled data. Hypnos even generalises to daytime physiology, surpassing a dedicated ECG foundation model at detecting atrial fibrillation. Our results demonstrate that next-token prediction is a strong self-supervised objective for representation learning from multi-modal physiological signals.
匹配关键词: self-supervised
---

[ACADEMIC - ARXIV]
标题: Integrating gene regulatory priors into Transformer attention with scTransformer for interpretable scRNA-seq analysis
作者: Mikele Milia, Louis Fabrice Tshimanga, Henning Mueller, Manfredo Atzori, Barbara Di Camillo
链接: https://arxiv.org/abs/2606.09558v1
完整摘要: Motivation: Transformer-based models are increasingly applied to large-scale single-cell transcriptomics, showing strong performance through self-supervised learning on millions of cells. However, most existing approaches treat genes as independent features, and largely ignore prior biological knowledge, which limits interpretability and robustness. In this paper, we explore whether explicitly incorporating gene regulatory information can improve both model performance and biological insight. Results: We present scTransformer, the first Transformer-based approach that builds a priori knowledge of biological mechanisms into the model's attention patterns. By constraining information flow according to known regulatory structures, the model learns representations that are more biologically meaningful. We evaluate scTransformer on a disease-relevant single-nucleus RNA-seq dataset using supervised cell-type classification. Compared to standard Transformers, our approach improves classification accuracy, enhances separation of cell types in embedding space, and produces attention patterns consistent with known regulatory programs. Overall, our results demonstrate that embedding biological structure into Transformer models can enhance interpretability without sacrificing performance, offering a principled step toward biologically grounded foundation models for single-cell omics.
匹配关键词: self-supervised
---

[ACADEMIC - ARXIV]
标题: Your U-Net Dereverberation Model is Secretly an RIR Encoder
作者: Sina Khanagha, Timo Gerkmann
链接: https://arxiv.org/abs/2606.09557v1
完整摘要: In this work, we analyze the ability of NCSN++ U-Net based audio dereverberation models to capture global room characteristics in their intermediate representations. Through an empirical study of both a state-of-the-art diffusion-based model and a discriminative counterpart, we show that deeper layers encode structured room impulse response (RIR)-dependent embeddings. Moreover, the discriminative ability of this implicit room representation correlates with dereverberation performance across objective metrics. Motivated by this observation, we propose a training strategy that explicitly conditions the network on pre-trained RIR embeddings, obtained via self-supervised contrastive learning. Incorporating RIR conditioning improves representation quality, accelerates convergence, and enhances dereverberation performance, while significantly reducing the number of reverse diffusion steps required by the diffusion-based model during inference.
匹配关键词: self-supervised
---

[ACADEMIC - ARXIV]
标题: Securing Self-supervised Data Curation for Foundation Models Robustness
作者: Sandeep Gupta, Roberto Passerone
链接: https://arxiv.org/abs/2606.09511v1
完整摘要: Self-supervised data curation provides a pathway to scaling and improving the generalization capabilities of machine learning models. By leveraging self-supervised learning (SSL) for data curation, the demand for massive training datasets required by foundation models can be effectively met. SSL greatly alleviates the costs associated with annotation and manual dataset curation while minimizing the need for human oversight. However, the integrity of SSL-curated datasets must be rigorously checked, as reliance on anonymous and unvetted external sources can substantially increase the risk of data poisoning. In this paper, we propose a Poisoned Data Detector (PDD), an active defense mechanism designed to ensure the integrity of SSL-curated datasets prior to foundation model training. PDDs are designed using a combination of the pretrained ImageBind model and traditional classifiers, including Random Forest (RF), k-Nearest Neighbors (KNN), Naive Bayes (NB), and Support Vector Machines (SVM). We rigorously evaluated PDDs using 176,200 images from three diverse datasets and three different adversarial attacks encompassing both in-distribution and out-of-distribution scenarios. Notably, SVM-PDD achieves superior performance for both in-distribution (Set3-Set5) and out-of-distribution (TrueFace and 140K RealFace) datasets. Our design demonstrates strong scalability and enables the rapid integration of new adversarial attack detectors through an ensemble approach.
匹配关键词: self-supervised
---

[ACADEMIC - ARXIV]
标题: MeCo: One-Step MeanFlow-based Corrector for Multi-Channel Speech Separation
作者: Dohwan Kim, Jung-Woo Choi
链接: https://arxiv.org/abs/2606.09677v1
完整摘要: While discriminative models for multi-channel speech separation excel in reference-based metrics, they often exhibit suboptimal human listening quality. To address this, we propose a novel MeanFlow-based one-step generative corrector (MeCo). MeCo learns a conditional average velocity field to map discriminative estimates directly onto the clean speech manifold in a single step. To maximize one-step generation performance, we introduce Data-Space Optimization (DSO). DSO integrates an $\mathbf{x}_r$-loss, which penalizes prediction errors on longer displacement intervals to serve as a generative objective for human listening quality, with an Endpoint SI-SDR loss that directly optimizes terminal signal fidelity. Experiments demonstrate that MeCo achieves state-of-the-art (SOTA) performance with minimal computational overhead, simultaneously achieving superior signal fidelity and human listening quality in both in-domain and out-of-domain scenarios.
匹配关键词: contrastive learning
---

[ACADEMIC - ARXIV]
标题: Correlation Is Not Enough: Embedding Human Metadata for Individual Causal Discovery
作者: Suraj Biswas, Saurabh Gupta, Pritam Mukherjee
链接: https://arxiv.org/abs/2606.09672v1
完整摘要: Ask a pretrained biomedical language model whether "cortisol 28 ug/dL" and "stock-market volatility" are related, and it returns a cosine similarity of 0.83 on a scale where 1.0 means identical. The two share no mechanism. This is not a corner case: every off-the-shelf biomedical encoder we tested (BioBERT, PubMedBERT, BioM-ELECTRA) scores unrelated cross-domain pairs between 0.76 and 0.92 when the answer should be near zero. Accuracy on cross-domain discrimination is 0%. Retrieval systems survive this, because a language model downstream filters the noise. A Large Behavioural Model (LBM), a foundation model whose subject is a person rather than a sentence, does not: it reasons over a graph of a user's life and treats embedding proximity as evidence that two events are causally linked. False proximity writes a false causal edge, and everything downstream inherits the error. Here, embedding geometry is not a tuning knob; it is correctness. We report the fix. A contrastive pass over 72,034 pairs raises PubMedBERT BIOSSES correlation from 0.633 to 0.828 and within-vs-across-domain separation from 1.05x to 1.63x. A second pass, BODHI, mines hard negatives from edges absent in a biomedical knowledge graph and lifts separation to 2.30x and the discrimination gap to +0.392, at a 4.5% BIOSSES cost. On an Intel Xeon 6737P with AMX, OpenVINO cuts single-query latency from 1367 ms to 10 ms (133x) and reaches 555 sentences/sec. One finding contradicts standard advice: FP16 beats INT8 on this silicon at every serving batch size, and we explain why. The same model on a no-AMX Ice Lake instance runs 13-27x slower. We release the benchmark suite, training corpora, the BODHI generator, and the OpenVINO scripts.
匹配关键词: contrastive learning
---

[ACADEMIC - ARXIV]
标题: Transition-Based Digital Twin Modelling for Alzheimer's Disease under Sparse Longitudinal Data
作者: Yinyu Huang, Yilin Zhang, Sofia Michopoulou, Christopher Kipps, Rahman Attar
链接: https://arxiv.org/abs/2606.09671v1
完整摘要: Alzheimer's disease (AD) progression is highly heterogeneous and is typically observed through sparse and irregular longitudinal data, posing challenges for prediction and personalised monitoring. Existing machine learning approaches have improved AD prediction using multimodal data, yet often focus on static classification or cohort-level risk estimation, providing limited support for subject-specific modelling and uncertainty-aware reasoning. To address these limitations, we present a personalised digital twin framework for AD prediction and scenario-based analysis using multimodal longitudinal data. The proposed approach integrates complementary modelling strategies to capture clinical transitions and temporal dependencies across visits. Using data from the Alzheimer's Disease Neuroimaging Initiative (ADNI), including cognitive assessments, clinical variables, and MRI-derived phenotypes, the framework predicts cognitive status and diagnostic categories while quantifying predictive uncertainty and enabling patient-specific what-if trajectory analysis. Evaluation on leak-free subject-level splits demonstrates strong performance in score forecasting and diagnosis classification. In this sparse and irregular ADNI setting, transition-based modelling of adjacent visits achieved higher predictive accuracy than the sequence-based branch, suggesting that local transition modelling may be more data-efficient. While sequence models remain valuable for uncertainty-aware trajectory forecasting, local transition modelling offers a more data-efficient and robust predictive strategy. These findings highlight the importance of aligning temporal modelling strategies with clinical data structure and suggest that transition-based digital twin formulations may provide a practical and interpretable approach for personalised disease forecasting in neurodegenerative disorders.
匹配关键词: contrastive learning
---

[ACADEMIC - ARXIV]
标题: Algorithm for Contextual Queueing Bandits with Rate-Optimal Queue Length Regret
作者: Seoungbin Bae, Dabeen Lee
链接: https://arxiv.org/abs/2606.09668v1
完整摘要: Contextual queueing bandits provide a framework for learning to schedule heterogeneous jobs under unknown context-dependent service rates. Under stochastic contexts, existing algorithms achieve $\widetilde{\mathcal{O}}(T^{-1/4})$ queue length regret, defined as the expected difference between the learner's and oracle's queue lengths at horizon $T$. In this paper, we improve this rate to $\widetilde{\mathcal{O}}(T^{-1/2})$. The key observation is that random exploration is needed only up to a carefully chosen cutoff round, rather than throughout the entire horizon. We propose CQB-$η$-2, a three-phase algorithm: (i) pure random exploration to construct an initial estimator, (ii) $η$-random exploration combined with a UCB rule to continue learning while maintaining negative drift, and (iii) pure UCB after the exploration cutoff. Our proof decomposes the queue length regret at the cutoff round. Before the cutoff, negative drift suppresses queue length differences caused by suboptimal choices. After the cutoff, the first two phases provide sufficient random exploration samples, ensuring that UCB decisions incur small departure-rate gaps. Combining these two bounds yields queue length regret of order $\widetilde{\mathcal{O}}(T^{-1/2})$. We further prove a minimax lower bound of order $Ω(T^{-1/2})$. The proof constructs two hard instances that are statistically indistinguishable up to the final service decision, and uses a queue-specific coupling argument to convert the resulting testing error into queue length regret. Together, our upper and lower bounds characterize the minimax dependence on the horizon $T$ up to logarithmic factors.
匹配关键词: contrastive learning
---

[ACADEMIC - ARXIV]
标题: In-Context Learning for Latent Space Bayesian Optimization
作者: Tuan A. Vu, Harri Lähdesmäki, Julien Martinelli
链接: https://arxiv.org/abs/2606.09664v1
完整摘要: Bayesian optimization (BO) is a central tool for sample-efficient design, and latent-space Bayesian optimization (LSBO) extends it to structured objects such as molecules and proteins. In parallel, tabular foundation models such as TabPFN and TabICL now achieve state-of-the-art regression performance and are increasingly used as BO surrogates. Because their Bayesian behavior is induced by large synthetic pretraining collections, the composition of this pretraining distribution is crucial. LSBO creates a distinctive mismatch: the induced map from latent code to objective value differs markedly from the regression tasks used to train current in-context models. We address this mismatch by complementing the pretraining stage of tabular foundation model surrogates with synthetic optimization tasks defined on the latent space of a molecular VAE. The continued-pretraining objective features a regularizer that anchors the model to the original checkpoint, preserving its broad regression prior while avoiding overspecialization to the adaptation tasks. On held-out molecular optimization benchmarks, the resulting model achieves strong performance, supporting the relevance of LSBO-specific adaptation for in-context surrogates.
匹配关键词: contrastive learning
---

[ACADEMIC - ARXIV]
标题: MeCo: One-Step MeanFlow-based Corrector for Multi-Channel Speech Separation
作者: Dohwan Kim, Jung-Woo Choi
链接: https://arxiv.org/abs/2606.09677v1
完整摘要: While discriminative models for multi-channel speech separation excel in reference-based metrics, they often exhibit suboptimal human listening quality. To address this, we propose a novel MeanFlow-based one-step generative corrector (MeCo). MeCo learns a conditional average velocity field to map discriminative estimates directly onto the clean speech manifold in a single step. To maximize one-step generation performance, we introduce Data-Space Optimization (DSO). DSO integrates an $\mathbf{x}_r$-loss, which penalizes prediction errors on longer displacement intervals to serve as a generative objective for human listening quality, with an Endpoint SI-SDR loss that directly optimizes terminal signal fidelity. Experiments demonstrate that MeCo achieves state-of-the-art (SOTA) performance with minimal computational overhead, simultaneously achieving superior signal fidelity and human listening quality in both in-domain and out-of-domain scenarios.
匹配关键词: representation learning
---

[ACADEMIC - ARXIV]
标题: Correlation Is Not Enough: Embedding Human Metadata for Individual Causal Discovery
作者: Suraj Biswas, Saurabh Gupta, Pritam Mukherjee
链接: https://arxiv.org/abs/2606.09672v1
完整摘要: Ask a pretrained biomedical language model whether "cortisol 28 ug/dL" and "stock-market volatility" are related, and it returns a cosine similarity of 0.83 on a scale where 1.0 means identical. The two share no mechanism. This is not a corner case: every off-the-shelf biomedical encoder we tested (BioBERT, PubMedBERT, BioM-ELECTRA) scores unrelated cross-domain pairs between 0.76 and 0.92 when the answer should be near zero. Accuracy on cross-domain discrimination is 0%. Retrieval systems survive this, because a language model downstream filters the noise. A Large Behavioural Model (LBM), a foundation model whose subject is a person rather than a sentence, does not: it reasons over a graph of a user's life and treats embedding proximity as evidence that two events are causally linked. False proximity writes a false causal edge, and everything downstream inherits the error. Here, embedding geometry is not a tuning knob; it is correctness. We report the fix. A contrastive pass over 72,034 pairs raises PubMedBERT BIOSSES correlation from 0.633 to 0.828 and within-vs-across-domain separation from 1.05x to 1.63x. A second pass, BODHI, mines hard negatives from edges absent in a biomedical knowledge graph and lifts separation to 2.30x and the discrimination gap to +0.392, at a 4.5% BIOSSES cost. On an Intel Xeon 6737P with AMX, OpenVINO cuts single-query latency from 1367 ms to 10 ms (133x) and reaches 555 sentences/sec. One finding contradicts standard advice: FP16 beats INT8 on this silicon at every serving batch size, and we explain why. The same model on a no-AMX Ice Lake instance runs 13-27x slower. We release the benchmark suite, training corpora, the BODHI generator, and the OpenVINO scripts.
匹配关键词: representation learning
---

[ACADEMIC - ARXIV]
标题: Transition-Based Digital Twin Modelling for Alzheimer's Disease under Sparse Longitudinal Data
作者: Yinyu Huang, Yilin Zhang, Sofia Michopoulou, Christopher Kipps, Rahman Attar
链接: https://arxiv.org/abs/2606.09671v1
完整摘要: Alzheimer's disease (AD) progression is highly heterogeneous and is typically observed through sparse and irregular longitudinal data, posing challenges for prediction and personalised monitoring. Existing machine learning approaches have improved AD prediction using multimodal data, yet often focus on static classification or cohort-level risk estimation, providing limited support for subject-specific modelling and uncertainty-aware reasoning. To address these limitations, we present a personalised digital twin framework for AD prediction and scenario-based analysis using multimodal longitudinal data. The proposed approach integrates complementary modelling strategies to capture clinical transitions and temporal dependencies across visits. Using data from the Alzheimer's Disease Neuroimaging Initiative (ADNI), including cognitive assessments, clinical variables, and MRI-derived phenotypes, the framework predicts cognitive status and diagnostic categories while quantifying predictive uncertainty and enabling patient-specific what-if trajectory analysis. Evaluation on leak-free subject-level splits demonstrates strong performance in score forecasting and diagnosis classification. In this sparse and irregular ADNI setting, transition-based modelling of adjacent visits achieved higher predictive accuracy than the sequence-based branch, suggesting that local transition modelling may be more data-efficient. While sequence models remain valuable for uncertainty-aware trajectory forecasting, local transition modelling offers a more data-efficient and robust predictive strategy. These findings highlight the importance of aligning temporal modelling strategies with clinical data structure and suggest that transition-based digital twin formulations may provide a practical and interpretable approach for personalised disease forecasting in neurodegenerative disorders.
匹配关键词: representation learning
---

[ACADEMIC - ARXIV]
标题: Algorithm for Contextual Queueing Bandits with Rate-Optimal Queue Length Regret
作者: Seoungbin Bae, Dabeen Lee
链接: https://arxiv.org/abs/2606.09668v1
完整摘要: Contextual queueing bandits provide a framework for learning to schedule heterogeneous jobs under unknown context-dependent service rates. Under stochastic contexts, existing algorithms achieve $\widetilde{\mathcal{O}}(T^{-1/4})$ queue length regret, defined as the expected difference between the learner's and oracle's queue lengths at horizon $T$. In this paper, we improve this rate to $\widetilde{\mathcal{O}}(T^{-1/2})$. The key observation is that random exploration is needed only up to a carefully chosen cutoff round, rather than throughout the entire horizon. We propose CQB-$η$-2, a three-phase algorithm: (i) pure random exploration to construct an initial estimator, (ii) $η$-random exploration combined with a UCB rule to continue learning while maintaining negative drift, and (iii) pure UCB after the exploration cutoff. Our proof decomposes the queue length regret at the cutoff round. Before the cutoff, negative drift suppresses queue length differences caused by suboptimal choices. After the cutoff, the first two phases provide sufficient random exploration samples, ensuring that UCB decisions incur small departure-rate gaps. Combining these two bounds yields queue length regret of order $\widetilde{\mathcal{O}}(T^{-1/2})$. We further prove a minimax lower bound of order $Ω(T^{-1/2})$. The proof constructs two hard instances that are statistically indistinguishable up to the final service decision, and uses a queue-specific coupling argument to convert the resulting testing error into queue length regret. Together, our upper and lower bounds characterize the minimax dependence on the horizon $T$ up to logarithmic factors.
匹配关键词: representation learning
---

[ACADEMIC - ARXIV]
标题: In-Context Learning for Latent Space Bayesian Optimization
作者: Tuan A. Vu, Harri Lähdesmäki, Julien Martinelli
链接: https://arxiv.org/abs/2606.09664v1
完整摘要: Bayesian optimization (BO) is a central tool for sample-efficient design, and latent-space Bayesian optimization (LSBO) extends it to structured objects such as molecules and proteins. In parallel, tabular foundation models such as TabPFN and TabICL now achieve state-of-the-art regression performance and are increasingly used as BO surrogates. Because their Bayesian behavior is induced by large synthetic pretraining collections, the composition of this pretraining distribution is crucial. LSBO creates a distinctive mismatch: the induced map from latent code to objective value differs markedly from the regression tasks used to train current in-context models. We address this mismatch by complementing the pretraining stage of tabular foundation model surrogates with synthetic optimization tasks defined on the latent space of a molecular VAE. The continued-pretraining objective features a regularizer that anchors the model to the original checkpoint, preserving its broad regression prior while avoiding overspecialization to the adaptation tasks. On held-out molecular optimization benchmarks, the resulting model achieves strong performance, supporting the relevance of LSBO-specific adaptation for in-context surrogates.
匹配关键词: representation learning
---

[ACADEMIC - ARXIV]
标题: SoccerNet 2026 Player-Centric Ball-Action Spotting:Retraining and Post-Processing Extensions to the FOOTPASS Baselines
作者: Parthsarthi Rawat
链接: https://arxiv.org/abs/2606.09679v1
完整摘要: We describe our system for the SoccerNet 2026 Player-Centric Ball-Action Spotting Challenge, which requires predicting who performs which action and when, across eight classes in broadcast soccer. Building on the three FOOTPASS baselines [1] (TAAD, TAAD+GNN, and TAAD+DST), we contribute four extensions: (1) gradient check pointing to enable full-backbone fine-tuning on a single GPU; (2) fusion of GNN logits into the DST encoder, combining graph-based tactical context with per-player visual features; (3) square-root frequency class weighting to address the 213:1 pass-to-tackle imbalance in the training data; and (4) a post processing pipeline comprising per-class logit gating, temporal frame refinement, jersey re-assignment, and a two-model ensemble. Our system achieves 0.548 Macro F1 on the test set and 0.446 on the challenge set (server evaluation).
匹配关键词: masked language model
---

[ACADEMIC - ARXIV]
标题: MeCo: One-Step MeanFlow-based Corrector for Multi-Channel Speech Separation
作者: Dohwan Kim, Jung-Woo Choi
链接: https://arxiv.org/abs/2606.09677v1
完整摘要: While discriminative models for multi-channel speech separation excel in reference-based metrics, they often exhibit suboptimal human listening quality. To address this, we propose a novel MeanFlow-based one-step generative corrector (MeCo). MeCo learns a conditional average velocity field to map discriminative estimates directly onto the clean speech manifold in a single step. To maximize one-step generation performance, we introduce Data-Space Optimization (DSO). DSO integrates an $\mathbf{x}_r$-loss, which penalizes prediction errors on longer displacement intervals to serve as a generative objective for human listening quality, with an Endpoint SI-SDR loss that directly optimizes terminal signal fidelity. Experiments demonstrate that MeCo achieves state-of-the-art (SOTA) performance with minimal computational overhead, simultaneously achieving superior signal fidelity and human listening quality in both in-domain and out-of-domain scenarios.
匹配关键词: masked language model
---

[ACADEMIC - ARXIV]
标题: (Auto)formalization is supposed to be easy: Trellis process semantics for spelling out rigorous proofs
作者: Wesley Pegden
链接: https://arxiv.org/abs/2606.09674v1
完整摘要: We present Trellis: an autoformalization system that leverages LLM agents in a deterministically constrained workflow to enforce incremental progress in Lean autoformalization tasks through iterative refinement of natural language proofs. Our approach is motivated by the common mathematician's notion of what it means to have a rigorous proof in the first place: namely, that it would be routine to elaborate any part of the proof in further detail. The result is a system which aims to achieve reliable autoformalization on a modest budget and with generalist agents, with specialization to autoformalization coming not from any task-specific agent training but instead from a meaning-of-rigor inspired workflow enforced by process semantics. We link to an end-to-end Lean formalization of a recent Ramsey theory breakthrough produced by the process.
匹配关键词: masked language model
---

[ACADEMIC - ARXIV]
标题: Correlation Is Not Enough: Embedding Human Metadata for Individual Causal Discovery
作者: Suraj Biswas, Saurabh Gupta, Pritam Mukherjee
链接: https://arxiv.org/abs/2606.09672v1
完整摘要: Ask a pretrained biomedical language model whether "cortisol 28 ug/dL" and "stock-market volatility" are related, and it returns a cosine similarity of 0.83 on a scale where 1.0 means identical. The two share no mechanism. This is not a corner case: every off-the-shelf biomedical encoder we tested (BioBERT, PubMedBERT, BioM-ELECTRA) scores unrelated cross-domain pairs between 0.76 and 0.92 when the answer should be near zero. Accuracy on cross-domain discrimination is 0%. Retrieval systems survive this, because a language model downstream filters the noise. A Large Behavioural Model (LBM), a foundation model whose subject is a person rather than a sentence, does not: it reasons over a graph of a user's life and treats embedding proximity as evidence that two events are causally linked. False proximity writes a false causal edge, and everything downstream inherits the error. Here, embedding geometry is not a tuning knob; it is correctness. We report the fix. A contrastive pass over 72,034 pairs raises PubMedBERT BIOSSES correlation from 0.633 to 0.828 and within-vs-across-domain separation from 1.05x to 1.63x. A second pass, BODHI, mines hard negatives from edges absent in a biomedical knowledge graph and lifts separation to 2.30x and the discrimination gap to +0.392, at a 4.5% BIOSSES cost. On an Intel Xeon 6737P with AMX, OpenVINO cuts single-query latency from 1367 ms to 10 ms (133x) and reaches 555 sentences/sec. One finding contradicts standard advice: FP16 beats INT8 on this silicon at every serving batch size, and we explain why. The same model on a no-AMX Ice Lake instance runs 13-27x slower. We release the benchmark suite, training corpora, the BODHI generator, and the OpenVINO scripts.
匹配关键词: masked language model
---

[ACADEMIC - ARXIV]
标题: Transition-Based Digital Twin Modelling for Alzheimer's Disease under Sparse Longitudinal Data
作者: Yinyu Huang, Yilin Zhang, Sofia Michopoulou, Christopher Kipps, Rahman Attar
链接: https://arxiv.org/abs/2606.09671v1
完整摘要: Alzheimer's disease (AD) progression is highly heterogeneous and is typically observed through sparse and irregular longitudinal data, posing challenges for prediction and personalised monitoring. Existing machine learning approaches have improved AD prediction using multimodal data, yet often focus on static classification or cohort-level risk estimation, providing limited support for subject-specific modelling and uncertainty-aware reasoning. To address these limitations, we present a personalised digital twin framework for AD prediction and scenario-based analysis using multimodal longitudinal data. The proposed approach integrates complementary modelling strategies to capture clinical transitions and temporal dependencies across visits. Using data from the Alzheimer's Disease Neuroimaging Initiative (ADNI), including cognitive assessments, clinical variables, and MRI-derived phenotypes, the framework predicts cognitive status and diagnostic categories while quantifying predictive uncertainty and enabling patient-specific what-if trajectory analysis. Evaluation on leak-free subject-level splits demonstrates strong performance in score forecasting and diagnosis classification. In this sparse and irregular ADNI setting, transition-based modelling of adjacent visits achieved higher predictive accuracy than the sequence-based branch, suggesting that local transition modelling may be more data-efficient. While sequence models remain valuable for uncertainty-aware trajectory forecasting, local transition modelling offers a more data-efficient and robust predictive strategy. These findings highlight the importance of aligning temporal modelling strategies with clinical data structure and suggest that transition-based digital twin formulations may provide a practical and interpretable approach for personalised disease forecasting in neurodegenerative disorders.
匹配关键词: masked language model
---

[ACADEMIC - ARXIV]
标题: Contrast encodes inductive bias: separating slow noise from dynamics in predictive representation learning
作者: Paarth Gulati, Ilya Nemenman
链接: https://arxiv.org/abs/2606.07770v1
完整摘要: Self-supervised methods that learn representations and predict dynamics fully in the latent space, such as JEPA, have been shown to confuse slowly varying noise with the dynamical signals they aim to capture. Specifically, when noise features remain approximately constant within each trajectory, contrastive predictive objectives preferentially encode these features instead of the true latent variables governing the system. The learned representation then becomes dominated by trajectory-specific noise, so downstream performance degrades with noise strength and does not improve even as the number and duration of training trajectories increase. We argue that this failure is a property of the objective itself, shared by a long line of contrastive predictive objectives that sample negatives across trajectories. To illustrate this generality, we study the failure mode and its remedy in two settings: a standard SimCLR-style JEPA on a synthetic moving-dot dataset, and DySIB, a recently introduced method designed for extracting physically interpretable representations of dynamics, on movies of a rigid-body pendulum. When negatives are instead sampled within a single trajectory, the slow noise can no longer distinguish frames within that trajectory, removing the predictive shortcut. Training one encoder simultaneously on many such trajectories then forces it to encode the variables relevant for the dynamics, with longer trajectories yielding better representations even for strong slow noise. Our results point toward principles for designing contrastive predictive objectives in dynamical representation learning, especially for physical systems with noisy experimental observations.
匹配关键词: SimCLR
---

[ACADEMIC - ARXIV]
标题: Implicit Data Synthesis for Contrastive Unsupervised Data Augmentation
作者: Patrick Kage, Trevor Hedges, N. Siddharth, Pavlos Andreadis
链接: https://arxiv.org/abs/2606.07498v1
完整摘要: Scientific observations generate large quantities of unlabeled data which is laborious to hand-label, making unsupervised learning techniques valuable for processing datasets. Among these approaches, contrastive learning provides a convenient mechanism for extracting structural representations from unannotated datasets. For natural imagery, the general approach is to use a variety of data-space augmentation methods in order to generate synthetic samples; however, for scientific observations data-space perturbations can fundamentally alter the underlying data. Our proposed method is to generate contrastive samples by perturbing the network weights rather than the underlying data, thus more closely preserving the structure of the data. We demonstrate this technique using a SimCLR-based pipeline applied over radar observations of meteors, and show performance gains under matched protocols.
匹配关键词: SimCLR
---

[ACADEMIC - ARXIV]
标题: Early High-Frequency Injection for Geometry-Sensitive OOD Detection
作者: Chuanjie Cheng, Ningkang Peng, Chenxi Liu, Yifan He, Peirong Ma, Yanhui Gu
链接: https://arxiv.org/abs/2605.20728v1
完整摘要: Post-hoc OOD detectors score logits or features after training, so their success depends on the geometry already encoded in the representation. We revisit this assumption through a band-wise MMD^2 analysis across CE, SimCLR, SupCon, and the OOD-oriented representation method PALM. In our diagnostic, low-frequency input bands induce weaker ID/OOD feature discrepancy, whereas higher-frequency bands tend to provide stronger separability. This observation motivates EIHF, an input-side intervention that exposes high-frequency evidence before the first convolution without changing the training objective. EIHF is strongest for geometry-sensitive OOD detection: under matched training and scoring settings, it reshapes class-conditional feature geometry and reduces ID/OOD Mahalanobis score overlap. Experiments on CIFAR-100 and ImageNet-100 show gains on CIFAR-100 and the best average FPR95 with second-best average AUROC on ImageNet-100, while also revealing a limitation on the scene-centric Places shift. Code is available at https://anonymous.4open.science/r/EIHF.
匹配关键词: SimCLR
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
标题: CineDance: Towards Next-Generation Multi-Shot Long-Form Cinematic Audio-Video Generation
作者: Yuheng Chen, Teng Hu, Yuji Wang, Qingdong He, Zhucun Xue, Qianyu Zhou, Xiangtai Li, Lizhuang Ma, Jiangning Zhang, Dacheng Tao
链接: https://arxiv.org/abs/2606.09639v1
完整摘要: The fidelity and structural diversity of training datasets fundamentally determine the capabilities of video generation models. While commercial systems showremarkableabilitytogeneratecinematicnarratives, the progress of open-source models remains limited by the scarcity of high-quality training data. To bridge this gap, we introduce CineDance-1M, a large-scale, open research Text-to-Audio-Video (T2AV) dataset designed specifically for multi-shot, long-form joint audio-video generation. Averaging 92.8 seconds and 24.2 continuous shots per video, it provides configurable, structured annotations for both audio and video modalities. This exceptional quality is achieved through a rigorous three-stage curation pipeline: i) diverse sourcing and comprehensive cleansing, ii) film-theory-inspired narrative parsing, and iii) hierarchical dual-modal captioning. For a comprehensive assessment, we propose CineBench, featuring a diverse prompt suite and a six-dimensional, human-aligned metric system tailored for complex narrative audio-video evaluation. Furthermore, we adapt LTX-2.3 into CineDance, which demonstrates exceptional single-modality quality alongside precise audio-video alignment and robust subject and environment consistency, effectively validating our curation strategy and the high quality of CineDance-1M. We anticipate that this work will serve as a solid foundation for accelerating future research in multi-shot, long-form joint audio-video generation. Our project page is available at https://aliothchen.github.io/projects/CineDance/.
匹配关键词: MAE
---

[ACADEMIC - ARXIV]
标题: UXBench: Benchmarking User Experience in AI Assistants
作者: Mengze Hong, Xia Zeng, Zeyang Lei, Sheng Wang, Chen Jason Zhang, Di Jiang, Taiming Fu, Jinfeng Huang, Mengqiao Liu, Qinghe Chang, Haosheng Zou, Qiongyi Zhou, Sijun He, Chen Xiaoshuai, Simon Deng, Haojing Huang, Zijian Li, Lucas Mu Li, Fubao Zhang, Mona Zhou, Wei Ma, Chenxuan Ma, Yuanmeng Zhang, Jian Song, Minlong Peng, Di Liang, Davey Chen
链接: https://arxiv.org/abs/2606.09570v1
完整摘要: As AI assistants serve millions of users daily, evaluating user experience (UX) beyond general model capability has become increasingly important. We present UXBench, the first user-centric benchmark grounded in real user feedback signals for evaluating preference alignment and dialogue generation. The benchmark consists of three interconnected tasks, UX Judge, UX Eval, and UX Recovery, with 7,400 test instances extracted from over 70K interaction logs of a mainstream Chinese AI assistant. The dataset closely reflects real user distributions, covering 8 scenarios, 83 domains, and diverse failure patterns that pose severe challenges. Extensive experiments on 26 frontier language models provide novel insights into how well models perceive user experience and how improvements in model capability contribute to better dialogue engagement. Through comprehensive analysis of model behavior and performance gaps, we show that user feedback prediction is a learnable capability, where a reward model trained from in-the-wild feedback signals can achieve well-calibrated accuracy. We further document the systematic biases of LLM-as-a-judge evaluation protocols and compare typical response strategies that directly affect user experience. UXBench establishes a new evaluation landscape and calls for greater attention to tailored UX optimization, contributing to a user-centric scaling law that shapes the success of AI assistants.
匹配关键词: MAE
---

[ACADEMIC - ARXIV]
标题: FuseFSS: Efficient Secure LLM Inference with Function Secret Sharing
作者: Yuhan Ma, Yong Li, Stefan Schmid
链接: https://arxiv.org/abs/2606.09551v1
完整摘要: Two-server secure inference allows a client to query a hosted large language model (LLM) without revealing prompts or embeddings. Recent GPU systems based on function secret sharing (FSS) make linear layers efficient, but fixed-point nonlinearities and helper operations remain a bottleneck because each operator is typically implemented as a bespoke protocol with its own comparisons, wrap-around corrections, and preprocessing material. We present FuseFSS, a compiler that replaces per-operator protocol design with a single compilation pipeline. For each scalar fixed-point operator, a compact specification lists its interval partition, low-degree arithmetic pieces, and required predicate bits. The compiler emits two batched FSS evaluations on the public masked value: one packed comparison that returns all predicate bits, and one vector interval lookup that returns the active coefficients and constants. Compared to the current state-of-the-art FSS-based GPU secure inference, FuseFSS preserves accuracy while achieving a $1.24\times$--$1.50\times$ end-to-end speedup and reducing online communication by $9\%$--$16\%$ on BERT and GPT-style models; preprocessing is also lighter, with $14\%$--$23\%$ lower key-generation time and $20\%$--$24\%$ smaller keys.
匹配关键词: MAE
---

[ACADEMIC - ARXIV]
标题: SecureClaw: Clawing Back Control of LLM Agents
作者: Yuhan Ma, Stefan Schmid
链接: https://arxiv.org/abs/2606.09549v1
完整摘要: Tool-using large language model (LLM) agents face two distinct security failures: unauthorized external actions and exposure of sensitive plaintext inside the runtime before any final output check can intervene. Existing defenses usually protect one boundary, either the planner/runtime or the action sink, and therefore do not by themselves secure both surfaces. We present SecureClaw, a dual-boundary architecture that places authorization at the effect sink and plaintext confinement at the read boundary. Sensitive reads pass through a trusted gateway that replaces raw values with opaque handles and, in the evaluated deployment, bounded summaries as an explicit declassification interface. Writes that change external state follow a PREVIEW$\rightarrow$COMMIT protocol in which only a trusted executor may commit the exact canonical request authorized by policy. The runtime can still plan over summaries and symbolic references, but cannot directly dereference secrets or perform side effects. Across AgentDojo, AgentLeak, and Agent Security Bench (ASB), SecureClaw is the only defense we evaluate in a common harness that simultaneously retains usable task utility and achieves 0\% attack success rate (ASR) on ASB, 0.64\% ASR on AgentDojo, and 3.23\% overall leak on AgentLeak's attacked parity lane, which measures final-output and internal-relay leakage.
匹配关键词: MAE
---

[ACADEMIC - ARXIV]
标题: Memory Beyond Recall: A Dual-Process Cognitive Memory System for Self-Evolving LLM Agents
作者: Tianxiang Fei, Mingyang Song, Mao Zheng, Xiang Yu
链接: https://arxiv.org/abs/2606.09483v1
完整摘要: Long-term memory for an LLM agent is more than retrieving the right passage at the right time. Current memory systems collapse belief revision, causal coupling, and cross-domain abstraction into a single retrieval surface tuned for surface recall, and consequently struggle on implicit personalisation that requires reasoning over how a user has evolved. We propose DCPM, which reorganises agent memory along a cognitive capability hierarchy ascending from raw inputs and atomic facts, through diachronic belief trajectories and identity, to domain schemas, latent intentions and cross-domain patterns. The hierarchy is driven by two processes inheriting the architectural split of dual-process theory: a synchronous daytime writer (System1) that records belief revisions as doubly linked supersedes chains, and an asynchronous nighttime engine (System2) that induces schemas and intentions and sweeps for cross-domain collisions abstracted into higher-level core schemas. On LongMemEval, PersonaMem and PersonaMem-v2, enabling System2 contributes most where the benchmark rewards implicit cross-session inference (up to +5.20 on PersonaMem-v2) and least on span recall, matching the architectural prediction.
匹配关键词: MAE
---

[ACADEMIC - ARXIV]
标题: SoccerNet 2026 Player-Centric Ball-Action Spotting:Retraining and Post-Processing Extensions to the FOOTPASS Baselines
作者: Parthsarthi Rawat
链接: https://arxiv.org/abs/2606.09679v1
完整摘要: We describe our system for the SoccerNet 2026 Player-Centric Ball-Action Spotting Challenge, which requires predicting who performs which action and when, across eight classes in broadcast soccer. Building on the three FOOTPASS baselines [1] (TAAD, TAAD+GNN, and TAAD+DST), we contribute four extensions: (1) gradient check pointing to enable full-backbone fine-tuning on a single GPU; (2) fusion of GNN logits into the DST encoder, combining graph-based tactical context with per-player visual features; (3) square-root frequency class weighting to address the 213:1 pass-to-tackle imbalance in the training data; and (4) a post processing pipeline comprising per-class logit gating, temporal frame refinement, jersey re-assignment, and a two-model ensemble. Our system achieves 0.548 Macro F1 on the test set and 0.446 on the challenge set (server evaluation).
匹配关键词: generative model
---

[ACADEMIC - ARXIV]
标题: MeCo: One-Step MeanFlow-based Corrector for Multi-Channel Speech Separation
作者: Dohwan Kim, Jung-Woo Choi
链接: https://arxiv.org/abs/2606.09677v1
完整摘要: While discriminative models for multi-channel speech separation excel in reference-based metrics, they often exhibit suboptimal human listening quality. To address this, we propose a novel MeanFlow-based one-step generative corrector (MeCo). MeCo learns a conditional average velocity field to map discriminative estimates directly onto the clean speech manifold in a single step. To maximize one-step generation performance, we introduce Data-Space Optimization (DSO). DSO integrates an $\mathbf{x}_r$-loss, which penalizes prediction errors on longer displacement intervals to serve as a generative objective for human listening quality, with an Endpoint SI-SDR loss that directly optimizes terminal signal fidelity. Experiments demonstrate that MeCo achieves state-of-the-art (SOTA) performance with minimal computational overhead, simultaneously achieving superior signal fidelity and human listening quality in both in-domain and out-of-domain scenarios.
匹配关键词: generative model
---

[ACADEMIC - ARXIV]
标题: Correlation Is Not Enough: Embedding Human Metadata for Individual Causal Discovery
作者: Suraj Biswas, Saurabh Gupta, Pritam Mukherjee
链接: https://arxiv.org/abs/2606.09672v1
完整摘要: Ask a pretrained biomedical language model whether "cortisol 28 ug/dL" and "stock-market volatility" are related, and it returns a cosine similarity of 0.83 on a scale where 1.0 means identical. The two share no mechanism. This is not a corner case: every off-the-shelf biomedical encoder we tested (BioBERT, PubMedBERT, BioM-ELECTRA) scores unrelated cross-domain pairs between 0.76 and 0.92 when the answer should be near zero. Accuracy on cross-domain discrimination is 0%. Retrieval systems survive this, because a language model downstream filters the noise. A Large Behavioural Model (LBM), a foundation model whose subject is a person rather than a sentence, does not: it reasons over a graph of a user's life and treats embedding proximity as evidence that two events are causally linked. False proximity writes a false causal edge, and everything downstream inherits the error. Here, embedding geometry is not a tuning knob; it is correctness. We report the fix. A contrastive pass over 72,034 pairs raises PubMedBERT BIOSSES correlation from 0.633 to 0.828 and within-vs-across-domain separation from 1.05x to 1.63x. A second pass, BODHI, mines hard negatives from edges absent in a biomedical knowledge graph and lifts separation to 2.30x and the discrimination gap to +0.392, at a 4.5% BIOSSES cost. On an Intel Xeon 6737P with AMX, OpenVINO cuts single-query latency from 1367 ms to 10 ms (133x) and reaches 555 sentences/sec. One finding contradicts standard advice: FP16 beats INT8 on this silicon at every serving batch size, and we explain why. The same model on a no-AMX Ice Lake instance runs 13-27x slower. We release the benchmark suite, training corpora, the BODHI generator, and the OpenVINO scripts.
匹配关键词: generative model
---

[ACADEMIC - ARXIV]
标题: Transition-Based Digital Twin Modelling for Alzheimer's Disease under Sparse Longitudinal Data
作者: Yinyu Huang, Yilin Zhang, Sofia Michopoulou, Christopher Kipps, Rahman Attar
链接: https://arxiv.org/abs/2606.09671v1
完整摘要: Alzheimer's disease (AD) progression is highly heterogeneous and is typically observed through sparse and irregular longitudinal data, posing challenges for prediction and personalised monitoring. Existing machine learning approaches have improved AD prediction using multimodal data, yet often focus on static classification or cohort-level risk estimation, providing limited support for subject-specific modelling and uncertainty-aware reasoning. To address these limitations, we present a personalised digital twin framework for AD prediction and scenario-based analysis using multimodal longitudinal data. The proposed approach integrates complementary modelling strategies to capture clinical transitions and temporal dependencies across visits. Using data from the Alzheimer's Disease Neuroimaging Initiative (ADNI), including cognitive assessments, clinical variables, and MRI-derived phenotypes, the framework predicts cognitive status and diagnostic categories while quantifying predictive uncertainty and enabling patient-specific what-if trajectory analysis. Evaluation on leak-free subject-level splits demonstrates strong performance in score forecasting and diagnosis classification. In this sparse and irregular ADNI setting, transition-based modelling of adjacent visits achieved higher predictive accuracy than the sequence-based branch, suggesting that local transition modelling may be more data-efficient. While sequence models remain valuable for uncertainty-aware trajectory forecasting, local transition modelling offers a more data-efficient and robust predictive strategy. These findings highlight the importance of aligning temporal modelling strategies with clinical data structure and suggest that transition-based digital twin formulations may provide a practical and interpretable approach for personalised disease forecasting in neurodegenerative disorders.
匹配关键词: generative model
---

[ACADEMIC - ARXIV]
标题: Visual Prompting Meets Feature Reconstruction-Based Anomaly Detection with Dual-Teacher Supervision
作者: Mateo Diaz-Bone, Daniel Caraballo, Florian Scheidegger, Thomas Frick, Mattia Rigotti, Andrea Bartezzaghi, Roy Assaf, Niccolo Avogaro, Yagmur G. Cinar, Brown Ebouky, Filip M. Janicki, Piotr S. Kluska, Cezary Skura, Cristiano Malossi
链接: https://arxiv.org/abs/2606.09670v1
完整摘要: Recent Anomaly Detection methods achieve perfect detection and segmentation scores on well-established datasets, such as MVTec. However, many of these methods face challenges when foundational assumptions - such as consistent object scale, viewpoint, background, illumination, and centered placement - are violated. Those variations that occur render anomaly detection methods unusable in many real-world scenarios. To address these limitations, we introduce three key contributions: (1) a visual prompting pipeline that isolates objects using foreground-background masking; (2) a mechanism for unfreezing the teacher in student-teacher models to improve domain adaptability; and (3) a data augmentation strategy leveraging diffusion-generated synthetic images to enhance anomaly detection performance. We achieve a 3.5 percentage point improvement over the previous state-of-the-art on the challenging AeBAD dataset by using the Masked Multiscale Reconstruction (MMR) model as our backbone.
匹配关键词: generative model
---

[ACADEMIC - ARXIV]
标题: SoccerNet 2026 Player-Centric Ball-Action Spotting:Retraining and Post-Processing Extensions to the FOOTPASS Baselines
作者: Parthsarthi Rawat
链接: https://arxiv.org/abs/2606.09679v1
完整摘要: We describe our system for the SoccerNet 2026 Player-Centric Ball-Action Spotting Challenge, which requires predicting who performs which action and when, across eight classes in broadcast soccer. Building on the three FOOTPASS baselines [1] (TAAD, TAAD+GNN, and TAAD+DST), we contribute four extensions: (1) gradient check pointing to enable full-backbone fine-tuning on a single GPU; (2) fusion of GNN logits into the DST encoder, combining graph-based tactical context with per-player visual features; (3) square-root frequency class weighting to address the 213:1 pass-to-tackle imbalance in the training data; and (4) a post processing pipeline comprising per-class logit gating, temporal frame refinement, jersey re-assignment, and a two-model ensemble. Our system achieves 0.548 Macro F1 on the test set and 0.446 on the challenge set (server evaluation).
匹配关键词: diffusion model
---

[ACADEMIC - ARXIV]
标题: MeCo: One-Step MeanFlow-based Corrector for Multi-Channel Speech Separation
作者: Dohwan Kim, Jung-Woo Choi
链接: https://arxiv.org/abs/2606.09677v1
完整摘要: While discriminative models for multi-channel speech separation excel in reference-based metrics, they often exhibit suboptimal human listening quality. To address this, we propose a novel MeanFlow-based one-step generative corrector (MeCo). MeCo learns a conditional average velocity field to map discriminative estimates directly onto the clean speech manifold in a single step. To maximize one-step generation performance, we introduce Data-Space Optimization (DSO). DSO integrates an $\mathbf{x}_r$-loss, which penalizes prediction errors on longer displacement intervals to serve as a generative objective for human listening quality, with an Endpoint SI-SDR loss that directly optimizes terminal signal fidelity. Experiments demonstrate that MeCo achieves state-of-the-art (SOTA) performance with minimal computational overhead, simultaneously achieving superior signal fidelity and human listening quality in both in-domain and out-of-domain scenarios.
匹配关键词: diffusion model
---

[ACADEMIC - ARXIV]
标题: Correlation Is Not Enough: Embedding Human Metadata for Individual Causal Discovery
作者: Suraj Biswas, Saurabh Gupta, Pritam Mukherjee
链接: https://arxiv.org/abs/2606.09672v1
完整摘要: Ask a pretrained biomedical language model whether "cortisol 28 ug/dL" and "stock-market volatility" are related, and it returns a cosine similarity of 0.83 on a scale where 1.0 means identical. The two share no mechanism. This is not a corner case: every off-the-shelf biomedical encoder we tested (BioBERT, PubMedBERT, BioM-ELECTRA) scores unrelated cross-domain pairs between 0.76 and 0.92 when the answer should be near zero. Accuracy on cross-domain discrimination is 0%. Retrieval systems survive this, because a language model downstream filters the noise. A Large Behavioural Model (LBM), a foundation model whose subject is a person rather than a sentence, does not: it reasons over a graph of a user's life and treats embedding proximity as evidence that two events are causally linked. False proximity writes a false causal edge, and everything downstream inherits the error. Here, embedding geometry is not a tuning knob; it is correctness. We report the fix. A contrastive pass over 72,034 pairs raises PubMedBERT BIOSSES correlation from 0.633 to 0.828 and within-vs-across-domain separation from 1.05x to 1.63x. A second pass, BODHI, mines hard negatives from edges absent in a biomedical knowledge graph and lifts separation to 2.30x and the discrimination gap to +0.392, at a 4.5% BIOSSES cost. On an Intel Xeon 6737P with AMX, OpenVINO cuts single-query latency from 1367 ms to 10 ms (133x) and reaches 555 sentences/sec. One finding contradicts standard advice: FP16 beats INT8 on this silicon at every serving batch size, and we explain why. The same model on a no-AMX Ice Lake instance runs 13-27x slower. We release the benchmark suite, training corpora, the BODHI generator, and the OpenVINO scripts.
匹配关键词: diffusion model
---

[ACADEMIC - ARXIV]
标题: Transition-Based Digital Twin Modelling for Alzheimer's Disease under Sparse Longitudinal Data
作者: Yinyu Huang, Yilin Zhang, Sofia Michopoulou, Christopher Kipps, Rahman Attar
链接: https://arxiv.org/abs/2606.09671v1
完整摘要: Alzheimer's disease (AD) progression is highly heterogeneous and is typically observed through sparse and irregular longitudinal data, posing challenges for prediction and personalised monitoring. Existing machine learning approaches have improved AD prediction using multimodal data, yet often focus on static classification or cohort-level risk estimation, providing limited support for subject-specific modelling and uncertainty-aware reasoning. To address these limitations, we present a personalised digital twin framework for AD prediction and scenario-based analysis using multimodal longitudinal data. The proposed approach integrates complementary modelling strategies to capture clinical transitions and temporal dependencies across visits. Using data from the Alzheimer's Disease Neuroimaging Initiative (ADNI), including cognitive assessments, clinical variables, and MRI-derived phenotypes, the framework predicts cognitive status and diagnostic categories while quantifying predictive uncertainty and enabling patient-specific what-if trajectory analysis. Evaluation on leak-free subject-level splits demonstrates strong performance in score forecasting and diagnosis classification. In this sparse and irregular ADNI setting, transition-based modelling of adjacent visits achieved higher predictive accuracy than the sequence-based branch, suggesting that local transition modelling may be more data-efficient. While sequence models remain valuable for uncertainty-aware trajectory forecasting, local transition modelling offers a more data-efficient and robust predictive strategy. These findings highlight the importance of aligning temporal modelling strategies with clinical data structure and suggest that transition-based digital twin formulations may provide a practical and interpretable approach for personalised disease forecasting in neurodegenerative disorders.
匹配关键词: diffusion model
---

[ACADEMIC - ARXIV]
标题: Visual Prompting Meets Feature Reconstruction-Based Anomaly Detection with Dual-Teacher Supervision
作者: Mateo Diaz-Bone, Daniel Caraballo, Florian Scheidegger, Thomas Frick, Mattia Rigotti, Andrea Bartezzaghi, Roy Assaf, Niccolo Avogaro, Yagmur G. Cinar, Brown Ebouky, Filip M. Janicki, Piotr S. Kluska, Cezary Skura, Cristiano Malossi
链接: https://arxiv.org/abs/2606.09670v1
完整摘要: Recent Anomaly Detection methods achieve perfect detection and segmentation scores on well-established datasets, such as MVTec. However, many of these methods face challenges when foundational assumptions - such as consistent object scale, viewpoint, background, illumination, and centered placement - are violated. Those variations that occur render anomaly detection methods unusable in many real-world scenarios. To address these limitations, we introduce three key contributions: (1) a visual prompting pipeline that isolates objects using foreground-background masking; (2) a mechanism for unfreezing the teacher in student-teacher models to improve domain adaptability; and (3) a data augmentation strategy leveraging diffusion-generated synthetic images to enhance anomaly detection performance. We achieve a 3.5 percentage point improvement over the previous state-of-the-art on the challenging AeBAD dataset by using the Masked Multiscale Reconstruction (MMR) model as our backbone.
匹配关键词: diffusion model
---

[ACADEMIC - ARXIV]
标题: TUDSR: Twice Upsampling-Diffusion for Higher Super-Resolution
作者: Zhiqiang Wu, Yitong Dong, Xian Wei
链接: https://arxiv.org/abs/2606.09608v1
完整摘要: Diffusion-based generative models have achieved remarkable success in real-world image super-resolution (SR). With tiled diffusion techniques, these models can produce high-resolution images that exceed their native-supported resolution. However, the quality of such high-resolution (e.g $2048^2$) outputs often remains extremely poor, primarily due to two factors we consider: the image upsampling ratio (e.g $\times8$) exceeding the model's native-supported upsampling ratio (e.g $\times4$), and the model's native-supported resolution. In practice, training a native high-resolution model requires larger architectures, which incur significant computational overhead and GPU memory costs, making it hard on limited-resource equipment. Thus, we present TUDSR, a Twice Upsampling-Diffusion framework for higher SR. The TUDSR framework mainly consists of two stages: the first involves training at $R$-resolution, and the second introduces a looped chunk-based training strategy at $NR$-resolution. Each stage adapts a one-step GAN architecture comprising a generator and a discriminator. Based on SD2.1-base, we develop TUDSR-S, which achieves state-of-the-art performance across multiple benchmarks. Extensive experiments further demonstrate that TUDSR-S generates high-quality images at the resolutions of $1024^2$ and even $2048^2$, significantly outperforming existing approaches. Code is available at https://github.com/wuer5/TUDSR.
匹配关键词: GAN
---

[ACADEMIC - ARXIV]
标题: Intention Driven Identification of In-Possession Match Phases in Association Football through Temporal Graph Learning
作者: Yuesen Li, Daniel Link
链接: https://arxiv.org/abs/2606.09289v1
完整摘要: Understanding tactical organisation of association football, hereafter referred to as football, requires identifying distinct match phases. Yet in-possession phases are rarely directly observable and are shaped by evolving tactical intentions, rather than spatial patterns alone. This study proposes a data-driven framework for identifying in-possession match phases from spatiotemporal tracking data. Seven German Bundesliga matches recorded at 25 Hz with TRACAB were analysed. A hierarchical phase model was defined with three tactical intentions (Invade Opponent Space, Keep Possession, Scoring) and six phases (Build Up, Progression, Counter Attack, Maintenance, Sustained Threat, Finishing). A Temporal Graph Attention Network (T-GAN) was developed to combine frame-level player-interaction graphs, contextual features, and Transformer-based temporal modelling. Performance was evaluated using frame-level F1 and a sequence-aware Intersection over Truth-Dominance (IoT-D) metric. T-GAN achieved macro-average frame-level F1 scores of 0.87 at the intention level, 0.76 for invasion-related phases, and 0.79 for scoring phases. At the sequence level, mean diagonal IoT-D F1 increased from 0.68 to 0.79 for intentions and from 0.61 to 0.71 for phases after post-processing, indicating improved temporal coherence. Model comparisons showed that sequence modelling was the main driver of segmentation quality, while graph-based relational modelling was particularly beneficial for Counter Attack recognition. Exploratory player attention analysis further suggested that wide and midfield positional groups contributed strongly to phase discrimination. Overall, the framework translates continuous tracking data into tactically interpretable in-possession phase representations, with potential applications in automated match annotation, tactical analysis, and playing-style profiling.
匹配关键词: GAN
---

[ACADEMIC - ARXIV]
标题: Self-Consistent Generative Paths via Admissible Random Variational Transport
作者: Lei Luo, Yingzhen Zhang, Jian Yang
链接: https://arxiv.org/abs/2606.08953v1
完整摘要: Modern generative models often define an entire probability path from a simple prior to the data law, rather than only an endpoint map. Diffusion models follow stochastic denoising paths, flow matching learns transport fields, consistency and distillation methods compress paths into one or a few steps, adversarial models match terminal distributions, and VAEs generate through latent kernels. Existing unifying views mainly describe how such paths are constructed. We study a complementary question: when is a generated probability path self-consistent? We define a self-consistent generative path as a random fixed point of admissible local variational transport corrections. In this framework, a local correction is specified by a random variational transport operator combining a divergence or geometry term, an energy term, and a structural constraint. The framework contains random regularized optimal-transport proximal steps as a structured instance, while also allowing non-OT divergences, latent kernels, adversarial constraints, causal discrete kernels, and terminal one-step maps. The theory yields a random fixed-point path residual (R-FPR), which measures the gap between the actual generated path and an admissible local correction. We prove well-posedness, random fixed-point existence and attraction, non-contractive existence, residual-to-generation error bounds, empirical residual concentration, proxy perturbation bounds, continuous-time limits, and operator-level generalization with model-specific corollaries. The resulting theory turns endpoint matching into path self-consistency testing and provides a residual-control principle for diagnosing failures, regularizing training, and guiding adaptive sampling across diffusion, flow, one-step, VAE, GAN/WGAN, and autoregressive generators.
匹配关键词: GAN
---

[ACADEMIC - ARXIV]
标题: In-Context Learning for Latent Space Bayesian Optimization
作者: Tuan A. Vu, Harri Lähdesmäki, Julien Martinelli
链接: https://arxiv.org/abs/2606.09664v1
完整摘要: Bayesian optimization (BO) is a central tool for sample-efficient design, and latent-space Bayesian optimization (LSBO) extends it to structured objects such as molecules and proteins. In parallel, tabular foundation models such as TabPFN and TabICL now achieve state-of-the-art regression performance and are increasingly used as BO surrogates. Because their Bayesian behavior is induced by large synthetic pretraining collections, the composition of this pretraining distribution is crucial. LSBO creates a distinctive mismatch: the induced map from latent code to objective value differs markedly from the regression tasks used to train current in-context models. We address this mismatch by complementing the pretraining stage of tabular foundation model surrogates with synthetic optimization tasks defined on the latent space of a molecular VAE. The continued-pretraining objective features a regularizer that anchors the model to the original checkpoint, preserving its broad regression prior while avoiding overspecialization to the adaptation tasks. On held-out molecular optimization benchmarks, the resulting model achieves strong performance, supporting the relevance of LSBO-specific adaptation for in-context surrogates.
匹配关键词: VAE
---

[ACADEMIC - ARXIV]
标题: Echo-DM: Ultrasound Marker Removal via Conditional Latent Diffusion and Region-Aware Fusion
作者: Zhiwei Wang, Tao Huang, Wentao Jiang, Muyi Li, Jianxin Liu, Jian Chen, Jie Zou, Yong Luo, Bo Du, Jing Zhang
链接: https://arxiv.org/abs/2606.09378v1
完整摘要: Clinical ultrasound images often contain artificial markers, such as measurement calipers and text, to assist diagnostic interpretation and comparison. However, these markers can introduce shortcut bias in downstream automated analysis, encouraging deep learning models to rely on marker-related cues rather than clinically meaningful anatomy. Existing marker removal methods are either mask-dependent and vulnerable to error propagation, or mask-free deterministic restorers that may over-smooth ultrasound texture and perturb unaffected background regions. To address these challenges, we present Echo-DM, a framework for ultrasound marker removal via conditional latent diffusion and region-aware fusion. Echo-DM follows a common encoder-diffusion-decoder pipeline, where a DiT-based conditional latent diffusion network performs global restoration and a region-aware fusion module enforces preservation-aware image-space refinement under end-to-end mask-free inference. Building on this fixed core design, we further instantiate Echo-DM-V and Echo-DM-R with VAE-based and RAE-based latent modules, respectively, which demonstrates that the Echo-DM architecture is compatible with diverse latent-module instantiations. Extensive experiments on Echo-PAIR, a large-scale paired clinical ultrasound dataset, demonstrate superior marker removal and strong anatomical fidelity compared with representative two-stage baselines, while providing favorable quality--efficiency trade-offs across deployment settings. Data, code and models will be released at https://github.com/MiliLab/Echo-DM.
匹配关键词: VAE
---

[ACADEMIC - ARXIV]
标题: Self-Consistent Generative Paths via Admissible Random Variational Transport
作者: Lei Luo, Yingzhen Zhang, Jian Yang
链接: https://arxiv.org/abs/2606.08953v1
完整摘要: Modern generative models often define an entire probability path from a simple prior to the data law, rather than only an endpoint map. Diffusion models follow stochastic denoising paths, flow matching learns transport fields, consistency and distillation methods compress paths into one or a few steps, adversarial models match terminal distributions, and VAEs generate through latent kernels. Existing unifying views mainly describe how such paths are constructed. We study a complementary question: when is a generated probability path self-consistent? We define a self-consistent generative path as a random fixed point of admissible local variational transport corrections. In this framework, a local correction is specified by a random variational transport operator combining a divergence or geometry term, an energy term, and a structural constraint. The framework contains random regularized optimal-transport proximal steps as a structured instance, while also allowing non-OT divergences, latent kernels, adversarial constraints, causal discrete kernels, and terminal one-step maps. The theory yields a random fixed-point path residual (R-FPR), which measures the gap between the actual generated path and an admissible local correction. We prove well-posedness, random fixed-point existence and attraction, non-contractive existence, residual-to-generation error bounds, empirical residual concentration, proxy perturbation bounds, continuous-time limits, and operator-level generalization with model-specific corollaries. The resulting theory turns endpoint matching into path self-consistency testing and provides a residual-control principle for diagnosing failures, regularizing training, and guiding adaptive sampling across diffusion, flow, one-step, VAE, GAN/WGAN, and autoregressive generators.
匹配关键词: VAE
---

[ACADEMIC - ARXIV]
标题: Graph Mamba Operator: A Latent Simulator for Interacting Particle Systems
作者: Karn Tiwari, Niladri Dutta, N M Anoop Krishnan, Prathosh A P
链接: https://arxiv.org/abs/2606.09432v1
完整摘要: Modeling interacting dynamical systems requires capturing spatial interactions alongside long-range temporal dependencies. Graph neural networks (GNNs) provide a natural representation but typically rely on autoregressive rollouts and treat spatial and temporal dynamics separately, leading to error accumulation over long horizons. Existing approaches also focus on local interactions and short temporal contexts, limiting their ability to capture multi-hop dependencies and global structure. We introduce the Graph Mamba Operator (GraMO), a latent-space simulator that integrates state-space models with graph-based interaction learning. In contrast to prior work that sequences nodes or applies spatial and temporal updates in separate stages, GraMO couples graph-based interactions and temporal state updates within a single recurrence. The update is linear in the latent state, with input-dependent coefficients that adapt across regimes. We evaluate GraMO on N-body systems, motion capture, and robotics datasets, achieving the lowest error across benchmarks and the largest gains in long-horizon prediction.
匹配关键词: autoregressive
---

[ACADEMIC - ARXIV]
标题: Real-time body pose non-verbal communication with a consistency-based reliability measure
作者: Alina Marcu, Dragos Costea, Cristina Lazar, Marius Leordeanu
链接: https://arxiv.org/abs/2606.09390v1
完整摘要: Body movement communicates intent at distances and in conditions where neither the face, nor speech can be captured. We study the recognition of communicative intent from 2D body pose alone. We argue that body motion is a reliable signal especially in scenarios that require real time low-cost on-device person-to-robot communication in long distance environments, such as rescue missions. However, existing resources do not isolate this signal. Affective corpora combine body, face, voice and text, while skeleton action-recognition benchmarks label the action performed rather than the message conveyed. We release a dataset of real frames of full-body pose covering ten communicative intents and we compare it against other real (IPC) and synthetic (MotionLCM, VEO3.1, Kimodo) ones that span a range of difficulty. We target systems that can run on a robot's limited onboard hardware. We benchmark multiple models, from skeleton graph classifiers to joint motion-forecasting networks, and report performance metrics together with frame rate on an embedded GPU (NVIDIA Orin~Nano), since speed matters as much as accuracy in our scenario. Finally, we show that a model's own autoregressive self-consistency works as an unsupervised reliability signal. We give a short proof that bounds the probability that a self-consistent prediction is correct, show that this probability grows with the number of consistent steps, and identify the conditions under which a confident prediction can still be false, benchmarked against industry-standard metrics.
匹配关键词: autoregressive
---

[ACADEMIC - ARXIV]
标题: Is Text All You Need? Text as a Universal Information Bottleneck for Speech LLMs
作者: Ming-Hao Hsu, Yuxuan Hu, Shujie Liu, Jinyu Li, Yan Lu, Zhizheng Wu
链接: https://arxiv.org/abs/2606.09366v1
完整摘要: Large language models (LLMs) provide a powerful reasoning backbone for speech understanding, but integrating continuous acoustic signals into a frozen LLM remains challenging. Existing speech-to-LLM interfaces typically operate at two extremes: either enforcing near-discrete token alignment, which benefits transcription but loses paralinguistic information, or learning unconstrained continuous representations, which can drift away from the LLM's input space and degrade autoregressive decoding. In this work, we propose Convex Gate (C-Gate), a speech-to-LLM bridge that constrains all speech representations to lie within the LLM's input embedding manifold with an architectural convex-hull constraint. Concretely, each frame is represented as a convex combination of token embeddings, ensuring compatibility with the pretrained LLM while preserving continuous expressivity. Across automatic speech recognition (ASR) and emotion recognition, C-Gate achieves strong joint performance, improving LibriSpeech WER by up to 48.7% relative while matching or exceeding single-task emotion accuracy. Beyond performance, our analysis reveals a key insight: information is not carried by discrete token identities, but by time-resolved trajectories in the embedding space. Causal interventions confirm that both the trajectory structure and alignment to the pretrained embedding manifold are critical for performance. These results suggest that geometry, rather than token discreteness, is the fundamental design factor in speech-to-LLM interfaces, and provide a controlled regime for studying multimodal integration in frozen LLMs. We release the checkpoint, per-sample outputs, mechanism dumps, and intervention suite for replication.
匹配关键词: autoregressive
---

[ACADEMIC - ARXIV]
标题: PBSD: Privileged Bayesian Self-Distillation for Long-Horizon Credit Assignment
作者: Yang Tian, Rui Wang, Xumeng Wen, Junjie Li, Shizhao Sun, Lei Song, Jiang Bian, Bo Zhao
链接: https://arxiv.org/abs/2606.09348v1
完整摘要: Long-horizon agentic tasks pose a fundamental credit assignment challenge for outcome-base reinforcement learning: trajectory-level rewards verify final correctness but provide limited guidance on which intermediate reasoning steps or tool interactions contribute to the outcome. The difficulty is especially pronounced in multi-turn search agents, where successful trajectories may contain misleading actions and failed trajectories may contain valuable evidence-gathering steps. We propose PBSD (Privileged Bayesian Self-Distillation), a Bayes-calibrated self-distillation method for fine-grained credit assignment under sparse final rewards. PBSD measures trajectory quality through the posterior-to-prior probability ratio of the verified answer and applies Bayes' rule to convert this hard-to-estimate answer-side ratio into a tractable likelihood ratio between a standard student model and a privileged answer-conditioned teacher model. Autoregressive decomposition of this Bayesian evidence score yields turn-level signals that identify whether each intermediate turn supports or undermines the verified outcome. Consequently, PBSD provides a principled and elegant reweighting scheme that transforms sparse outcome supervision into Bayes-calibrated turn-level credit signals, while remaining fully compatible with standard policy optimization. Experiments demonstrate that PBSD consistently enhances performance across both in-domain and out-of-domain settings, and effectively transfers knowledge from short-context training to long-context inference, suggesting that its fine-grained credit assignment mechanism facilitates more effective policy learning and yields improved generalization.
匹配关键词: autoregressive
---

[ACADEMIC - ARXIV]
标题: End-to-End Training for Discrete Token LLM based TTS System
作者: Changfeng Gao, Yong Ren, Jun Yuan, Ye Bai, Zhao You, ShiDong Shang
链接: https://arxiv.org/abs/2606.09234v1
完整摘要: Recent state-of-the-art (SOTA) text-to-speech (TTS) systems typically adopt a cascaded pipeline consisting of a speech tokenizer, an autoregressive large language model (LLM), and a diffusion based flow-matching (FM) model, with these components trained independently. In this paper, we propose a fully end-to-end (E2E) optimization framework that unifies the training of the speech tokenizer, LLM, FM model, and an additional reward model (RM). Specifically, we first jointly optimize the tokenizer using multi-task objectives derived from reconstruction for FM, next-token prediction for LLM, and multi recognition task for RM. This joint training encourages the discrete speech token space to capture acoustically and semantically salient information that is better tailored to TTS. We then further optimize the LLM using downstream reconstruction and recognition by FM and RM, which reduces inference-time mismatch and steers the LLM toward more preferred generations. Experimental results show that our E2E framework consistently outperforms cascaded baselines. On the Seed-TTS-Eval benchmark, our system achieves a word error rate (WER) of 0.78% and 1.56%, a new SOTA result with a 0.6B-parameter LLM and 0.5B-parameter FM model. These results validate that holistic E2E optimization is critical for improving discrete-token-based TTS systems with a much simpler training pipeline.
匹配关键词: autoregressive
---

[ACADEMIC - ARXIV]
标题: Visual Prompting Meets Feature Reconstruction-Based Anomaly Detection with Dual-Teacher Supervision
作者: Mateo Diaz-Bone, Daniel Caraballo, Florian Scheidegger, Thomas Frick, Mattia Rigotti, Andrea Bartezzaghi, Roy Assaf, Niccolo Avogaro, Yagmur G. Cinar, Brown Ebouky, Filip M. Janicki, Piotr S. Kluska, Cezary Skura, Cristiano Malossi
链接: https://arxiv.org/abs/2606.09670v1
完整摘要: Recent Anomaly Detection methods achieve perfect detection and segmentation scores on well-established datasets, such as MVTec. However, many of these methods face challenges when foundational assumptions - such as consistent object scale, viewpoint, background, illumination, and centered placement - are violated. Those variations that occur render anomaly detection methods unusable in many real-world scenarios. To address these limitations, we introduce three key contributions: (1) a visual prompting pipeline that isolates objects using foreground-background masking; (2) a mechanism for unfreezing the teacher in student-teacher models to improve domain adaptability; and (3) a data augmentation strategy leveraging diffusion-generated synthetic images to enhance anomaly detection performance. We achieve a 3.5 percentage point improvement over the previous state-of-the-art on the challenging AeBAD dataset by using the Masked Multiscale Reconstruction (MMR) model as our backbone.
匹配关键词: latent diffusion
---

[ACADEMIC - ARXIV]
标题: In-Context Learning for Latent Space Bayesian Optimization
作者: Tuan A. Vu, Harri Lähdesmäki, Julien Martinelli
链接: https://arxiv.org/abs/2606.09664v1
完整摘要: Bayesian optimization (BO) is a central tool for sample-efficient design, and latent-space Bayesian optimization (LSBO) extends it to structured objects such as molecules and proteins. In parallel, tabular foundation models such as TabPFN and TabICL now achieve state-of-the-art regression performance and are increasingly used as BO surrogates. Because their Bayesian behavior is induced by large synthetic pretraining collections, the composition of this pretraining distribution is crucial. LSBO creates a distinctive mismatch: the induced map from latent code to objective value differs markedly from the regression tasks used to train current in-context models. We address this mismatch by complementing the pretraining stage of tabular foundation model surrogates with synthetic optimization tasks defined on the latent space of a molecular VAE. The continued-pretraining objective features a regularizer that anchors the model to the original checkpoint, preserving its broad regression prior while avoiding overspecialization to the adaptation tasks. On held-out molecular optimization benchmarks, the resulting model achieves strong performance, supporting the relevance of LSBO-specific adaptation for in-context surrogates.
匹配关键词: latent diffusion
---

[ACADEMIC - ARXIV]
标题: End-to-End Context Compression at Scale
作者: Ang Li, Sean McLeish, Haozhe Chen, Nimit Kalra, Zaiqian Chen, Artem Gazizov, Venkata Anoop Suhas Kumar Morisetty, Bhavya Kailkhura, Harshitha Menon, Zhuang Liu, Brian R. Bartoldson, Tom Goldstein, Sanae Lotfi, Micah Goldblum, Pavel Izmailov
链接: https://arxiv.org/abs/2606.09659v1
完整摘要: Long-context language model inference is bottlenecked by memory, as the KV cache grows with context length. Recent techniques to compress the KV cache fall short: they either degrade model quality substantially or require considerable time and compute to compress a single long prompt. Furthermore, many methods require the input to fit within the target model's context window, and are generally incompatible with modern production inference engines. Encoder-decoder compressors, which map a long token sequence to a shorter sequence of latent embeddings consumed by a decoder, are an appealing alternative in principle. However, existing approaches are not competitive with KV cache compression on the accuracy-efficiency frontier. In this work, we revisit encoder-decoder compression and close this gap. We first perform an architecture search, pre-training many variants from scratch to determine how best to design and train encoder-decoder compressors. Guided by our findings, we continually pre-train a family of 0.6B-encoder, 4B-decoder models on over 350B tokens each, at compression ratios of 1:4, 1:8, and 1:16. We introduce Latent Context Language Models (LCLMs), a family of compressors that improve the Pareto frontier across general-task performance, compression speed, and peak memory usage. We demonstrate that LCLMs serve as efficient backbones for long-horizon agents, letting the agent skim through a compressed long context and adaptively expand relevant segments on demand.
匹配关键词: latent diffusion
---

[ACADEMIC - ARXIV]
标题: Do Video Foundation Models Understand Intuitive Physics? A Layerwise Probing Analysis
作者: Samuele Punzo, Niccolò Caselli, Ippokratis Pantelidis, Francesco Massafra, Salvatore Lo Sardo, Mohammadreza Salehi
链接: https://arxiv.org/abs/2606.09646v1
完整摘要: We study whether pretrained video foundation models encode intuitive-physics information in their frozen representations, and how this information varies across model families, layers, and probe types. Using frozen-feature probing on IntPhys2 and Minimal Video Pairs (MVP), we compare predictive joint-embedding models (V-JEPA), masked reconstruction models (VideoMAE), and a diffusion-based video generator (LTX-Video). V-JEPA achieves the strongest overall results across benchmarks, especially with probes that model temporal dynamics, while VideoMAE remains competitive and LTX-Video recovers weaker but non-trivial signal. Layerwise analyses show that physics-relevant information is weakest in early layers and becomes most accessible at intermediate-to-late depth, and temporal controls show that disrupting frame order substantially reduces performance, especially on MVP. Together, these results suggest that intuitive-physics knowledge emerges reliably in pretrained video representations, but its accessibility depends strongly on pretraining paradigm, representational depth, and readout mechanism.
匹配关键词: latent diffusion
---

[ACADEMIC - ARXIV]
标题: Physics-Aware Sparse Learning and Selective Online Adaptation for Euler-Lagrange Robot Dynamics
作者: Rishabh Dev Yadav, Samaksh Ujjawal, Sihao Sun, Spandan Roy, Wei Pan
链接: https://arxiv.org/abs/2606.09640v1
完整摘要: Accurate dynamics models are essential for model-based robotic control, yet nominal Euler--Lagrange models often become inaccurate in the presence of payload variation, unmodeled coupling, friction, aerodynamic effects, and changing operating conditions. Most learning-based correction methods improve prediction accuracy by introducing a single additive residual, but do not preserve the internal mechanical structure of Euler--Lagrange systems. This leads to models that do not preserve symmetry, positive-definiteness, or the coupling between inertia and velocity-dependent terms, which can result in physically inconsistent predictions and reduced reliability when embedded in model-based controllers. We propose a structure-preserving residual learning framework that decomposes model mismatch into an inertia correction, the corresponding induced Coriolis term, and a generalized-force residual. The mechanical component is learned under physical constraints, while the disturbance-sensitive component is represented through a sparse history-dependent latent interaction model and adapted online using Bayesian linear regression. This separation preserves key mechanical structure while restricting adaptation to the part of the dynamics most affected by changing conditions. Experiments across multiple robotic platforms, including mobile, aerial, and manipulator systems, show that the proposed method improves dynamics prediction and trajectory tracking under coupled and time-varying dynamics. These results highlight the value of combining structured residual modeling, compact latent interaction selection, and selective online adaptation for real-world model-based control.
匹配关键词: latent diffusion
---

[ACADEMIC - ARXIV]
标题: Transition-Based Digital Twin Modelling for Alzheimer's Disease under Sparse Longitudinal Data
作者: Yinyu Huang, Yilin Zhang, Sofia Michopoulou, Christopher Kipps, Rahman Attar
链接: https://arxiv.org/abs/2606.09671v1
完整摘要: Alzheimer's disease (AD) progression is highly heterogeneous and is typically observed through sparse and irregular longitudinal data, posing challenges for prediction and personalised monitoring. Existing machine learning approaches have improved AD prediction using multimodal data, yet often focus on static classification or cohort-level risk estimation, providing limited support for subject-specific modelling and uncertainty-aware reasoning. To address these limitations, we present a personalised digital twin framework for AD prediction and scenario-based analysis using multimodal longitudinal data. The proposed approach integrates complementary modelling strategies to capture clinical transitions and temporal dependencies across visits. Using data from the Alzheimer's Disease Neuroimaging Initiative (ADNI), including cognitive assessments, clinical variables, and MRI-derived phenotypes, the framework predicts cognitive status and diagnostic categories while quantifying predictive uncertainty and enabling patient-specific what-if trajectory analysis. Evaluation on leak-free subject-level splits demonstrates strong performance in score forecasting and diagnosis classification. In this sparse and irregular ADNI setting, transition-based modelling of adjacent visits achieved higher predictive accuracy than the sequence-based branch, suggesting that local transition modelling may be more data-efficient. While sequence models remain valuable for uncertainty-aware trajectory forecasting, local transition modelling offers a more data-efficient and robust predictive strategy. These findings highlight the importance of aligning temporal modelling strategies with clinical data structure and suggest that transition-based digital twin formulations may provide a practical and interpretable approach for personalised disease forecasting in neurodegenerative disorders.
匹配关键词: multimodal
---

[ACADEMIC - ARXIV]
标题: SpatialWorld: Benchmarking Interactive Spatial Reasoning of Multimodal Agents in Real-World Tasks
作者: Hongcheng Gao, Hailong Qu, Jingyi Tang, Jiahao Wang, Zihao Huang, Hengkang Qiao, Shihong Huang, Junming Yang, Yi Li, Hongyixuan Yuan, Wenjie Li, Bohan Zeng, Wenbo Li, Bo Wang, Jianhui Liu, Olive Huang, Haoyang Huang, Wentao Zhang, Guoqing Huang, Nan Duan, Yinpeng Dong
链接: https://arxiv.org/abs/2606.09669v1
完整摘要: Spatial reasoning is a foundational capability for multimodal large language models (MLLMs) to perceive and operate within the physical world. However, existing benchmarks predominantly rely on passive evaluation (e.g., static VQA) or simulator-specific pipelines, failing to assess general interactive spatial understanding. We introduce SpatialWorld, a unified benchmark designed specifically for evaluating the interactive spatial understanding of multimodal agents in complex real-world tasks. Integrating eight heterogeneous simulation backends under a shared, simulator-agnostic protocol, SpatialWorld features 760 human-annotated tasks across diverse domains (e.g., household routines, travel, social collaboration). Agents must solve tasks under vision-only partial observability, actively gathering egocentric visual evidence and expressing decisions via a unified, text-based action interface native to MLLMs. For reliable evaluation, each task includes a human-validated initial state, a reference trajectory, and a terminal-state verifier. Evaluating 15 advanced agents reveals that robust spatial task solving remains challenging: the strongest model, GPT-5, achieves an average task success rate (TSR) of only 17.4%, while the leading open-source model, Qwen-3.5, reaches 14.1%. Further analysis exposes a clear mismatch between task success and execution efficiency, alongside substantial domain-specific performance variations. These bottlenecks in active exploration and long-horizon planning position SpatialWorld as a rigorous testbed for future spatial agents.
匹配关键词: multimodal
---

[ACADEMIC - ARXIV]
标题: Cross-Modal Masking for Robust Silent Speech Synthesis Using sEMG and Lipreading
作者: Eder del Blanco, David Gimeno-Gómez, Eva Navas, Carlos-D. Martínez-Hinarejos, Inma Hernáez
链接: https://arxiv.org/abs/2606.09667v1
完整摘要: Speech restoration through silent speech interfaces (SSIs) has emerged as a promising assistive technology for individuals with impaired or absent laryngeal voice production. Among non-invasive SSI modalities, surface electromyography (sEMG) and video-based lipreading provide complementary articulatory information, yet their integration for continuous speech synthesis remains underexplored. Moreover, existing multimodal approaches rarely address robustness to modality degradation or temporary sensor failure, limiting their applicability in realistic scenarios. In this work, we propose a masked multimodal speech synthesis framework that jointly leverages sEMG and lipreading signals through modality masking during training. Under multispeaker settings, the proposed approach reduces word error rate by up to 14 absolute percentage points compared to the strongest unimodal baseline. Experimental results not only show that masking strategies are critical for these performance gains and robustness under low-bitrate conditions, but also that they generalize better than degradation-specific data augmentations in the presence of modality absence conditions. Phone-level analyses further reveal complementary contributions across modalities, with particularly strong benefits for vowels and for specific consonant groups. Overall, these findings demonstrate the effectiveness and robustness of masked multimodal integration for silent speech synthesis, although adaptation to laryngectomized speakers remains an open research challenge.
匹配关键词: multimodal
---

[ACADEMIC - ARXIV]
标题: Where Does the Answer Come From? Benchmarking View-Level Visual Evidence Identification in Multi-View MLLMs for Autonomous Driving
作者: Yimu Wang, Yee Man Choi, Barry Zhang, Mozhgan Nasr Azadani, Sean Sedwards, Krzysztof Czarnecki
链接: https://arxiv.org/abs/2606.09644v1
完整摘要: Multimodal large language models (MLLMs) achieve strong results on visual reasoning benchmarks, but answer accuracy alone does not indicate whether a model relied on the correct visual evidence. This gap is particularly important in multi-view driving scenes used for autonomous driving, where a model can produce a plausible answer while grounding it in the wrong camera view. We introduce a multi-view visual question answering benchmark for evaluating evidence-source identification: given six synchronized NuScenes views and a question, the model must identify the supporting camera view and answer the question. The benchmark contains 122 conflict-centric question-answer pairs from 73 scenes, spanning causality, counterfactual reasoning, and intent prediction. View labels are proposed by an automatic conflict-mining pipeline and manually verified by annotators. We evaluate three settings: camera-view selection, oracle QA given the golden view, and joint prediction in which the model selects a view and answers in one pass. Answers are evaluated in both multiple-choice and free-form formats, using exact match for structured predictions and an LLM judge for free-form responses. By explicitly separating visual-source identification from answer correctness, the benchmark exposes grounding failures that answer-only evaluation misses.
匹配关键词: multimodal
---

[ACADEMIC - ARXIV]
标题: FMplex: Model Virtualization for Serving Extensible Foundation Models
作者: Hetvi Shastri, Pragya Sharma, Walid A. Hanafy, David Irwin, Mani Srivastava, Prashant Shenoy
链接: https://arxiv.org/abs/2606.09643v1
完整摘要: Foundation models (FMs) are increasingly used as backbones for downstream tasks across language, vision, time-series, and multimodal applications. Yet existing model-serving systems deploy each customized task as an independent model instance, thereby replicating heavyweight backbones, wasting accelerator memory, and losing opportunities to amortize batching and loading costs. This paper presents FMplex, a serving system that treats FM backbones as a virtualization substrate for deployment sharing. FMplex presents each task with a virtual foundation model (vFM), a logically private FM instance backed by a shared physical FM. This abstraction lets independently customized tasks share a backbone while preserving task-specific extensions, independent lifecycles, and task-level isolation. In addition, we propose a batch-aware fair-queueing scheduler that combines weighted task-level sharing with inter- and intra-task batching across colocated tasks. We implement a FMplex-based serving stack spanning task construction, sharing-aware deployment, and runtime execution. Across 7 FM backbones (16 variants) and 92 downstream tasks, FMplex reduces latency by up to 80% over spatial partitioning and 33.3% over best-effort co-location, while hosting up to 6x more tasks at cluster scale.
匹配关键词: multimodal
---

[ACADEMIC - ARXIV]
标题: SoccerNet 2026 Player-Centric Ball-Action Spotting:Retraining and Post-Processing Extensions to the FOOTPASS Baselines
作者: Parthsarthi Rawat
链接: https://arxiv.org/abs/2606.09679v1
完整摘要: We describe our system for the SoccerNet 2026 Player-Centric Ball-Action Spotting Challenge, which requires predicting who performs which action and when, across eight classes in broadcast soccer. Building on the three FOOTPASS baselines [1] (TAAD, TAAD+GNN, and TAAD+DST), we contribute four extensions: (1) gradient check pointing to enable full-backbone fine-tuning on a single GPU; (2) fusion of GNN logits into the DST encoder, combining graph-based tactical context with per-player visual features; (3) square-root frequency class weighting to address the 213:1 pass-to-tackle imbalance in the training data; and (4) a post processing pipeline comprising per-class logit gating, temporal frame refinement, jersey re-assignment, and a two-model ensemble. Our system achieves 0.548 Macro F1 on the test set and 0.446 on the challenge set (server evaluation).
匹配关键词: vision language model
---

[ACADEMIC - ARXIV]
标题: MeCo: One-Step MeanFlow-based Corrector for Multi-Channel Speech Separation
作者: Dohwan Kim, Jung-Woo Choi
链接: https://arxiv.org/abs/2606.09677v1
完整摘要: While discriminative models for multi-channel speech separation excel in reference-based metrics, they often exhibit suboptimal human listening quality. To address this, we propose a novel MeanFlow-based one-step generative corrector (MeCo). MeCo learns a conditional average velocity field to map discriminative estimates directly onto the clean speech manifold in a single step. To maximize one-step generation performance, we introduce Data-Space Optimization (DSO). DSO integrates an $\mathbf{x}_r$-loss, which penalizes prediction errors on longer displacement intervals to serve as a generative objective for human listening quality, with an Endpoint SI-SDR loss that directly optimizes terminal signal fidelity. Experiments demonstrate that MeCo achieves state-of-the-art (SOTA) performance with minimal computational overhead, simultaneously achieving superior signal fidelity and human listening quality in both in-domain and out-of-domain scenarios.
匹配关键词: vision language model
---

[ACADEMIC - ARXIV]
标题: (Auto)formalization is supposed to be easy: Trellis process semantics for spelling out rigorous proofs
作者: Wesley Pegden
链接: https://arxiv.org/abs/2606.09674v1
完整摘要: We present Trellis: an autoformalization system that leverages LLM agents in a deterministically constrained workflow to enforce incremental progress in Lean autoformalization tasks through iterative refinement of natural language proofs. Our approach is motivated by the common mathematician's notion of what it means to have a rigorous proof in the first place: namely, that it would be routine to elaborate any part of the proof in further detail. The result is a system which aims to achieve reliable autoformalization on a modest budget and with generalist agents, with specialization to autoformalization coming not from any task-specific agent training but instead from a meaning-of-rigor inspired workflow enforced by process semantics. We link to an end-to-end Lean formalization of a recent Ramsey theory breakthrough produced by the process.
匹配关键词: vision language model
---

[ACADEMIC - ARXIV]
标题: Correlation Is Not Enough: Embedding Human Metadata for Individual Causal Discovery
作者: Suraj Biswas, Saurabh Gupta, Pritam Mukherjee
链接: https://arxiv.org/abs/2606.09672v1
完整摘要: Ask a pretrained biomedical language model whether "cortisol 28 ug/dL" and "stock-market volatility" are related, and it returns a cosine similarity of 0.83 on a scale where 1.0 means identical. The two share no mechanism. This is not a corner case: every off-the-shelf biomedical encoder we tested (BioBERT, PubMedBERT, BioM-ELECTRA) scores unrelated cross-domain pairs between 0.76 and 0.92 when the answer should be near zero. Accuracy on cross-domain discrimination is 0%. Retrieval systems survive this, because a language model downstream filters the noise. A Large Behavioural Model (LBM), a foundation model whose subject is a person rather than a sentence, does not: it reasons over a graph of a user's life and treats embedding proximity as evidence that two events are causally linked. False proximity writes a false causal edge, and everything downstream inherits the error. Here, embedding geometry is not a tuning knob; it is correctness. We report the fix. A contrastive pass over 72,034 pairs raises PubMedBERT BIOSSES correlation from 0.633 to 0.828 and within-vs-across-domain separation from 1.05x to 1.63x. A second pass, BODHI, mines hard negatives from edges absent in a biomedical knowledge graph and lifts separation to 2.30x and the discrimination gap to +0.392, at a 4.5% BIOSSES cost. On an Intel Xeon 6737P with AMX, OpenVINO cuts single-query latency from 1367 ms to 10 ms (133x) and reaches 555 sentences/sec. One finding contradicts standard advice: FP16 beats INT8 on this silicon at every serving batch size, and we explain why. The same model on a no-AMX Ice Lake instance runs 13-27x slower. We release the benchmark suite, training corpora, the BODHI generator, and the OpenVINO scripts.
匹配关键词: vision language model
---

[ACADEMIC - ARXIV]
标题: Transition-Based Digital Twin Modelling for Alzheimer's Disease under Sparse Longitudinal Data
作者: Yinyu Huang, Yilin Zhang, Sofia Michopoulou, Christopher Kipps, Rahman Attar
链接: https://arxiv.org/abs/2606.09671v1
完整摘要: Alzheimer's disease (AD) progression is highly heterogeneous and is typically observed through sparse and irregular longitudinal data, posing challenges for prediction and personalised monitoring. Existing machine learning approaches have improved AD prediction using multimodal data, yet often focus on static classification or cohort-level risk estimation, providing limited support for subject-specific modelling and uncertainty-aware reasoning. To address these limitations, we present a personalised digital twin framework for AD prediction and scenario-based analysis using multimodal longitudinal data. The proposed approach integrates complementary modelling strategies to capture clinical transitions and temporal dependencies across visits. Using data from the Alzheimer's Disease Neuroimaging Initiative (ADNI), including cognitive assessments, clinical variables, and MRI-derived phenotypes, the framework predicts cognitive status and diagnostic categories while quantifying predictive uncertainty and enabling patient-specific what-if trajectory analysis. Evaluation on leak-free subject-level splits demonstrates strong performance in score forecasting and diagnosis classification. In this sparse and irregular ADNI setting, transition-based modelling of adjacent visits achieved higher predictive accuracy than the sequence-based branch, suggesting that local transition modelling may be more data-efficient. While sequence models remain valuable for uncertainty-aware trajectory forecasting, local transition modelling offers a more data-efficient and robust predictive strategy. These findings highlight the importance of aligning temporal modelling strategies with clinical data structure and suggest that transition-based digital twin formulations may provide a practical and interpretable approach for personalised disease forecasting in neurodegenerative disorders.
匹配关键词: vision language model
---

[ACADEMIC - ARXIV]
标题: ReCoVLA: VLM-Guided Reward Compilation for Failure Recovery in Vision-Language-Action Policies
作者: Haodi Hu, Chung-Ta Huang, Jing Liu, Ye Wang, Kei Suzuki, Matthew Brand, Toshiaki Koike-Akino
链接: https://arxiv.org/abs/2606.09630v1
完整摘要: Vision-language-action (VLA) policies provide strong priors for language-conditioned manipulation, but remain brittle in off-nominal states requiring targeted recovery. We propose ReCoVLA -- a failure-conditioned residual recovery framework that keeps a pretrained VLA policy frozen, uses an external vision-language model (VLM) to infer the failure mode and recovery stage, and compiles a structured reward from task-relevant components. Rather than using the VLM to generate actions or rewards directly, ReCoVLA uses it as a semantic reward selector: it predicts a recovery descriptor and reward mask for in-simulation residual-policy training, followed by zero-shot sim-to-real deployment of the trained recovery policies. This decouples high-level failure understanding from low-level corrective control to support different VLAs. Experiments across short-horizon, long-horizon, and contact-rich manipulation tasks show that ReCoVLA outperforms the tested baselines on average. In simulation, our reward compiler improves average success from 36.7% for the fine-tuned $π_{0.5}$ baseline to 66.7%. In physical zero-shot sim-to-real experiments, ReCoVLA achieves the best average performance, with 61.7% success.
匹配关键词: VLM
---

[ACADEMIC - ARXIV]
标题: TABVERSE: Benchmarking Cross-Format Table Understanding in LLMs and VLMs
作者: Momina Ahsan, Sarfraz Ahmad, Ming Shan Hee, Roy Ka-Wei Lee, Preslav Nakov
链接: https://arxiv.org/abs/2606.09578v1
完整摘要: Large Language Models (LLMs) and Vision-Language Models (VLMs) are increasingly evaluated on table reasoning tasks, but the role of table representation remains under-explored. In practice, the same table content may appear in different structural formats, such as HTML, Markdown, and LaTeX, or as rendered images. However, existing evaluations often let content, format, layout, and modality vary together, making it difficult to isolate representation effects. We introduce TABVERSE, a controlled multimodal table benchmark that aligns the same table content across multiple structural formats and rendered images, with question category and difficulty tags. This design enables systematic evaluation of representation effects while holding table content fixed. We evaluate LLMs and VLMs across three tasks: Question Answering (QA), Structural Understanding Capability (SUC), and Structure Reconstruction (SR). Our results show that representation choice substantially affects table understanding. Models generally perform better with structured text than with rendered images, but the size of this gap depends on the task, model, and format. HTML is often the most robust text format, while row-sensitive structural tasks and syntactically usable LaTeX reconstruction remain challenging. These findings show that table representation is a key factor in reliable table evaluation.
匹配关键词: VLM
---

[ACADEMIC - ARXIV]
标题: MUDIDI: A Two-Stage Framework for Multilingual Dictionary Digitization with Language Models
作者: David Setiawan, Temuulen Khishigsuren, Milind Agarwal, Pagnarith Pit, Aso Mahmudi, Ekaterina Vylomova
链接: https://arxiv.org/abs/2606.09435v1
完整摘要: Multilingual dictionaries are among the most valuable documentary resources for low-resource and endangered languages, yet many remain available only as scans. For many decades, their digitization and conversion into a machine-readable format was nearly impossible due to language-specific scripts, complex multi-column layouts full of entries with abbreviations and cross-references. Recent vision-language models offer a promising solution, but it is unclear how well they preserve characters, markup, and process lexicographic structure. We introduce MUDIDI, a two-stage framework for multi-lingual dictionary digitization. Stage One evaluates the quality of character recognition and markup preservation; Stage Two focuses on dictionary entry segmentation with subsequent mapping into a machine-readable lexicographic schema, SIL's Multi-Dictionary Formatter. We also release a dataset that consists of human-annotated lexicographic entries collected from 30 public-domain dictionaries featuring diverse writing systems, language families, and formats. We benchmark OCR systems, general-purpose Large Language Models (LLMs), and Vision Language Models (VLMs) on the dataset, demonstrating superior performance of LLMs across most writing systems and languages in both stages, and provide practical guidelines on improving the results for more challenging scenarios. Finally, we show that supplementing additional information, such as dictionary introduction, to the LLMs can improve the quality of the digitized dictionary. Github: https://github.com/DavidSamuell/MUDIDI-Pipeline-for-Digitization-of-Multilingual-Dictionary/
匹配关键词: VLM
---

[ACADEMIC - ARXIV]
标题: Guide Me Out: A Framework to Benchmark VLM Operators Communication in Crisis Scenarios
作者: Giacomo Gonella, Stefano Menini, Marco Guerini
链接: https://arxiv.org/abs/2606.09428v1
完整摘要: Effective crisis response requires spatially grounded communication that bridges linguistic guidance of civilians with the physical environment, accounting for structural bottlenecks, evolving threats, and agent-specific contexts. Yet, current NLP research in crisis communication remains mainly limited to static, text-only classification settings, overlooking the critical communicative role of AI operators in dynamic, embodied scenarios. We address this gap with a novel benchmarking framework for evaluating Vision-Language Models (VLMs) tasked with guiding civilian agents through simulated evacuations. We test two communication strategies (narrowcast vs. broadcast), two environment representations (visual vs. graph-based), and two threat behaviors (static vs. moving) across nine maps of varying structural complexity. Our results show that Narrowcast consistently reduces civilian Fail rates compared to Broadcast across all difficulty levels. Guidance quality depends heavily on how the VLM operator represents the world: the visual modality drives performance, while adding an adjacency graph is model-dependent and often harmful. Moving threats raise Fail rates across all conditions as communication must continuously adapt over time. Together, these findings show that deploying VLMs as AI operators in evacuation scenarios remains a non-trivial challenge, where the choice of communication strategy and input representation can directly determine the success or failure of the intervention.
匹配关键词: VLM
---

[ACADEMIC - ARXIV]
标题: Zero-Shot Semantic Re-Identification for Autonomous Driving: A VLM Baseline Study
作者: Eduardo Borges, Manuel Abreu, Luís Garrote, Urbano J. Nunes
链接: https://arxiv.org/abs/2606.09362v1
完整摘要: Re-Identification (ReID) in autonomous driving is typically formulated as a visual matching problem, where observations of vehicles, pedestrians, and cyclists are associated across time, frames, or camera views using learned appearance embeddings, often complemented by motion, geometric, or multimodal cues. However, purely visual representations may be sensitive to viewpoint, occlusion, illumination, and sensor-domain variations, limiting their interpretability and robustness in complex driving scenes. We propose a baseline study of a zero-shot pipeline using Vision-Language Models (VLMs) to generate textual descriptions of detected traffic participants and evaluate whether these descriptions can support identity matching across observations. Instead of relying only on low-level visual similarity, the proposed formulation represents each object through structured semantic attributes, including category, color, shape, pose, visible parts, spatial context, and distinctive visual cues. This study provides an initial benchmark for language-based re-identification in autonomous-driving scenarios, discussing and evaluating the strengths and limitations of current VLMs for this task. Results demonstrate that zero-shot semantic descriptions can support effective object re-identification, achieving retrieval performance comparable to a supervised CNN baseline while offering greater interpretability through explicit identity cues. However, the experiments also reveal important challenges, including attribute inconsistency across viewpoints and limited fine-grained discrimination between visually similar instances.
匹配关键词: VLM
---

[ACADEMIC - ARXIV]
标题: MeCo: One-Step MeanFlow-based Corrector for Multi-Channel Speech Separation
作者: Dohwan Kim, Jung-Woo Choi
链接: https://arxiv.org/abs/2606.09677v1
完整摘要: While discriminative models for multi-channel speech separation excel in reference-based metrics, they often exhibit suboptimal human listening quality. To address this, we propose a novel MeanFlow-based one-step generative corrector (MeCo). MeCo learns a conditional average velocity field to map discriminative estimates directly onto the clean speech manifold in a single step. To maximize one-step generation performance, we introduce Data-Space Optimization (DSO). DSO integrates an $\mathbf{x}_r$-loss, which penalizes prediction errors on longer displacement intervals to serve as a generative objective for human listening quality, with an Endpoint SI-SDR loss that directly optimizes terminal signal fidelity. Experiments demonstrate that MeCo achieves state-of-the-art (SOTA) performance with minimal computational overhead, simultaneously achieving superior signal fidelity and human listening quality in both in-domain and out-of-domain scenarios.
匹配关键词: image generation
---

[ACADEMIC - ARXIV]
标题: Correlation Is Not Enough: Embedding Human Metadata for Individual Causal Discovery
作者: Suraj Biswas, Saurabh Gupta, Pritam Mukherjee
链接: https://arxiv.org/abs/2606.09672v1
完整摘要: Ask a pretrained biomedical language model whether "cortisol 28 ug/dL" and "stock-market volatility" are related, and it returns a cosine similarity of 0.83 on a scale where 1.0 means identical. The two share no mechanism. This is not a corner case: every off-the-shelf biomedical encoder we tested (BioBERT, PubMedBERT, BioM-ELECTRA) scores unrelated cross-domain pairs between 0.76 and 0.92 when the answer should be near zero. Accuracy on cross-domain discrimination is 0%. Retrieval systems survive this, because a language model downstream filters the noise. A Large Behavioural Model (LBM), a foundation model whose subject is a person rather than a sentence, does not: it reasons over a graph of a user's life and treats embedding proximity as evidence that two events are causally linked. False proximity writes a false causal edge, and everything downstream inherits the error. Here, embedding geometry is not a tuning knob; it is correctness. We report the fix. A contrastive pass over 72,034 pairs raises PubMedBERT BIOSSES correlation from 0.633 to 0.828 and within-vs-across-domain separation from 1.05x to 1.63x. A second pass, BODHI, mines hard negatives from edges absent in a biomedical knowledge graph and lifts separation to 2.30x and the discrimination gap to +0.392, at a 4.5% BIOSSES cost. On an Intel Xeon 6737P with AMX, OpenVINO cuts single-query latency from 1367 ms to 10 ms (133x) and reaches 555 sentences/sec. One finding contradicts standard advice: FP16 beats INT8 on this silicon at every serving batch size, and we explain why. The same model on a no-AMX Ice Lake instance runs 13-27x slower. We release the benchmark suite, training corpora, the BODHI generator, and the OpenVINO scripts.
匹配关键词: image generation
---

[ACADEMIC - ARXIV]
标题: Visual Prompting Meets Feature Reconstruction-Based Anomaly Detection with Dual-Teacher Supervision
作者: Mateo Diaz-Bone, Daniel Caraballo, Florian Scheidegger, Thomas Frick, Mattia Rigotti, Andrea Bartezzaghi, Roy Assaf, Niccolo Avogaro, Yagmur G. Cinar, Brown Ebouky, Filip M. Janicki, Piotr S. Kluska, Cezary Skura, Cristiano Malossi
链接: https://arxiv.org/abs/2606.09670v1
完整摘要: Recent Anomaly Detection methods achieve perfect detection and segmentation scores on well-established datasets, such as MVTec. However, many of these methods face challenges when foundational assumptions - such as consistent object scale, viewpoint, background, illumination, and centered placement - are violated. Those variations that occur render anomaly detection methods unusable in many real-world scenarios. To address these limitations, we introduce three key contributions: (1) a visual prompting pipeline that isolates objects using foreground-background masking; (2) a mechanism for unfreezing the teacher in student-teacher models to improve domain adaptability; and (3) a data augmentation strategy leveraging diffusion-generated synthetic images to enhance anomaly detection performance. We achieve a 3.5 percentage point improvement over the previous state-of-the-art on the challenging AeBAD dataset by using the Masked Multiscale Reconstruction (MMR) model as our backbone.
匹配关键词: image generation
---

[ACADEMIC - ARXIV]
标题: SpatialWorld: Benchmarking Interactive Spatial Reasoning of Multimodal Agents in Real-World Tasks
作者: Hongcheng Gao, Hailong Qu, Jingyi Tang, Jiahao Wang, Zihao Huang, Hengkang Qiao, Shihong Huang, Junming Yang, Yi Li, Hongyixuan Yuan, Wenjie Li, Bohan Zeng, Wenbo Li, Bo Wang, Jianhui Liu, Olive Huang, Haoyang Huang, Wentao Zhang, Guoqing Huang, Nan Duan, Yinpeng Dong
链接: https://arxiv.org/abs/2606.09669v1
完整摘要: Spatial reasoning is a foundational capability for multimodal large language models (MLLMs) to perceive and operate within the physical world. However, existing benchmarks predominantly rely on passive evaluation (e.g., static VQA) or simulator-specific pipelines, failing to assess general interactive spatial understanding. We introduce SpatialWorld, a unified benchmark designed specifically for evaluating the interactive spatial understanding of multimodal agents in complex real-world tasks. Integrating eight heterogeneous simulation backends under a shared, simulator-agnostic protocol, SpatialWorld features 760 human-annotated tasks across diverse domains (e.g., household routines, travel, social collaboration). Agents must solve tasks under vision-only partial observability, actively gathering egocentric visual evidence and expressing decisions via a unified, text-based action interface native to MLLMs. For reliable evaluation, each task includes a human-validated initial state, a reference trajectory, and a terminal-state verifier. Evaluating 15 advanced agents reveals that robust spatial task solving remains challenging: the strongest model, GPT-5, achieves an average task success rate (TSR) of only 17.4%, while the leading open-source model, Qwen-3.5, reaches 14.1%. Further analysis exposes a clear mismatch between task success and execution efficiency, alongside substantial domain-specific performance variations. These bottlenecks in active exploration and long-horizon planning position SpatialWorld as a rigorous testbed for future spatial agents.
匹配关键词: image generation
---

[ACADEMIC - ARXIV]
标题: Cross-Modal Masking for Robust Silent Speech Synthesis Using sEMG and Lipreading
作者: Eder del Blanco, David Gimeno-Gómez, Eva Navas, Carlos-D. Martínez-Hinarejos, Inma Hernáez
链接: https://arxiv.org/abs/2606.09667v1
完整摘要: Speech restoration through silent speech interfaces (SSIs) has emerged as a promising assistive technology for individuals with impaired or absent laryngeal voice production. Among non-invasive SSI modalities, surface electromyography (sEMG) and video-based lipreading provide complementary articulatory information, yet their integration for continuous speech synthesis remains underexplored. Moreover, existing multimodal approaches rarely address robustness to modality degradation or temporary sensor failure, limiting their applicability in realistic scenarios. In this work, we propose a masked multimodal speech synthesis framework that jointly leverages sEMG and lipreading signals through modality masking during training. Under multispeaker settings, the proposed approach reduces word error rate by up to 14 absolute percentage points compared to the strongest unimodal baseline. Experimental results not only show that masking strategies are critical for these performance gains and robustness under low-bitrate conditions, but also that they generalize better than degradation-specific data augmentations in the presence of modality absence conditions. Phone-level analyses further reveal complementary contributions across modalities, with particularly strong benefits for vowels and for specific consonant groups. Overall, these findings demonstrate the effectiveness and robustness of masked multimodal integration for silent speech synthesis, although adaptation to laryngectomized speakers remains an open research challenge.
匹配关键词: image generation
---

[ACADEMIC - ARXIV]
标题: SoccerNet 2026 Player-Centric Ball-Action Spotting:Retraining and Post-Processing Extensions to the FOOTPASS Baselines
作者: Parthsarthi Rawat
链接: https://arxiv.org/abs/2606.09679v1
完整摘要: We describe our system for the SoccerNet 2026 Player-Centric Ball-Action Spotting Challenge, which requires predicting who performs which action and when, across eight classes in broadcast soccer. Building on the three FOOTPASS baselines [1] (TAAD, TAAD+GNN, and TAAD+DST), we contribute four extensions: (1) gradient check pointing to enable full-backbone fine-tuning on a single GPU; (2) fusion of GNN logits into the DST encoder, combining graph-based tactical context with per-player visual features; (3) square-root frequency class weighting to address the 213:1 pass-to-tackle imbalance in the training data; and (4) a post processing pipeline comprising per-class logit gating, temporal frame refinement, jersey re-assignment, and a two-model ensemble. Our system achieves 0.548 Macro F1 on the test set and 0.446 on the challenge set (server evaluation).
匹配关键词: visual reasoning
---

[ACADEMIC - ARXIV]
标题: Correlation Is Not Enough: Embedding Human Metadata for Individual Causal Discovery
作者: Suraj Biswas, Saurabh Gupta, Pritam Mukherjee
链接: https://arxiv.org/abs/2606.09672v1
完整摘要: Ask a pretrained biomedical language model whether "cortisol 28 ug/dL" and "stock-market volatility" are related, and it returns a cosine similarity of 0.83 on a scale where 1.0 means identical. The two share no mechanism. This is not a corner case: every off-the-shelf biomedical encoder we tested (BioBERT, PubMedBERT, BioM-ELECTRA) scores unrelated cross-domain pairs between 0.76 and 0.92 when the answer should be near zero. Accuracy on cross-domain discrimination is 0%. Retrieval systems survive this, because a language model downstream filters the noise. A Large Behavioural Model (LBM), a foundation model whose subject is a person rather than a sentence, does not: it reasons over a graph of a user's life and treats embedding proximity as evidence that two events are causally linked. False proximity writes a false causal edge, and everything downstream inherits the error. Here, embedding geometry is not a tuning knob; it is correctness. We report the fix. A contrastive pass over 72,034 pairs raises PubMedBERT BIOSSES correlation from 0.633 to 0.828 and within-vs-across-domain separation from 1.05x to 1.63x. A second pass, BODHI, mines hard negatives from edges absent in a biomedical knowledge graph and lifts separation to 2.30x and the discrimination gap to +0.392, at a 4.5% BIOSSES cost. On an Intel Xeon 6737P with AMX, OpenVINO cuts single-query latency from 1367 ms to 10 ms (133x) and reaches 555 sentences/sec. One finding contradicts standard advice: FP16 beats INT8 on this silicon at every serving batch size, and we explain why. The same model on a no-AMX Ice Lake instance runs 13-27x slower. We release the benchmark suite, training corpora, the BODHI generator, and the OpenVINO scripts.
匹配关键词: visual reasoning
---

[ACADEMIC - ARXIV]
标题: Transition-Based Digital Twin Modelling for Alzheimer's Disease under Sparse Longitudinal Data
作者: Yinyu Huang, Yilin Zhang, Sofia Michopoulou, Christopher Kipps, Rahman Attar
链接: https://arxiv.org/abs/2606.09671v1
完整摘要: Alzheimer's disease (AD) progression is highly heterogeneous and is typically observed through sparse and irregular longitudinal data, posing challenges for prediction and personalised monitoring. Existing machine learning approaches have improved AD prediction using multimodal data, yet often focus on static classification or cohort-level risk estimation, providing limited support for subject-specific modelling and uncertainty-aware reasoning. To address these limitations, we present a personalised digital twin framework for AD prediction and scenario-based analysis using multimodal longitudinal data. The proposed approach integrates complementary modelling strategies to capture clinical transitions and temporal dependencies across visits. Using data from the Alzheimer's Disease Neuroimaging Initiative (ADNI), including cognitive assessments, clinical variables, and MRI-derived phenotypes, the framework predicts cognitive status and diagnostic categories while quantifying predictive uncertainty and enabling patient-specific what-if trajectory analysis. Evaluation on leak-free subject-level splits demonstrates strong performance in score forecasting and diagnosis classification. In this sparse and irregular ADNI setting, transition-based modelling of adjacent visits achieved higher predictive accuracy than the sequence-based branch, suggesting that local transition modelling may be more data-efficient. While sequence models remain valuable for uncertainty-aware trajectory forecasting, local transition modelling offers a more data-efficient and robust predictive strategy. These findings highlight the importance of aligning temporal modelling strategies with clinical data structure and suggest that transition-based digital twin formulations may provide a practical and interpretable approach for personalised disease forecasting in neurodegenerative disorders.
匹配关键词: visual reasoning
---

[ACADEMIC - ARXIV]
标题: Visual Prompting Meets Feature Reconstruction-Based Anomaly Detection with Dual-Teacher Supervision
作者: Mateo Diaz-Bone, Daniel Caraballo, Florian Scheidegger, Thomas Frick, Mattia Rigotti, Andrea Bartezzaghi, Roy Assaf, Niccolo Avogaro, Yagmur G. Cinar, Brown Ebouky, Filip M. Janicki, Piotr S. Kluska, Cezary Skura, Cristiano Malossi
链接: https://arxiv.org/abs/2606.09670v1
完整摘要: Recent Anomaly Detection methods achieve perfect detection and segmentation scores on well-established datasets, such as MVTec. However, many of these methods face challenges when foundational assumptions - such as consistent object scale, viewpoint, background, illumination, and centered placement - are violated. Those variations that occur render anomaly detection methods unusable in many real-world scenarios. To address these limitations, we introduce three key contributions: (1) a visual prompting pipeline that isolates objects using foreground-background masking; (2) a mechanism for unfreezing the teacher in student-teacher models to improve domain adaptability; and (3) a data augmentation strategy leveraging diffusion-generated synthetic images to enhance anomaly detection performance. We achieve a 3.5 percentage point improvement over the previous state-of-the-art on the challenging AeBAD dataset by using the Masked Multiscale Reconstruction (MMR) model as our backbone.
匹配关键词: visual reasoning
---

[ACADEMIC - ARXIV]
标题: SpatialWorld: Benchmarking Interactive Spatial Reasoning of Multimodal Agents in Real-World Tasks
作者: Hongcheng Gao, Hailong Qu, Jingyi Tang, Jiahao Wang, Zihao Huang, Hengkang Qiao, Shihong Huang, Junming Yang, Yi Li, Hongyixuan Yuan, Wenjie Li, Bohan Zeng, Wenbo Li, Bo Wang, Jianhui Liu, Olive Huang, Haoyang Huang, Wentao Zhang, Guoqing Huang, Nan Duan, Yinpeng Dong
链接: https://arxiv.org/abs/2606.09669v1
完整摘要: Spatial reasoning is a foundational capability for multimodal large language models (MLLMs) to perceive and operate within the physical world. However, existing benchmarks predominantly rely on passive evaluation (e.g., static VQA) or simulator-specific pipelines, failing to assess general interactive spatial understanding. We introduce SpatialWorld, a unified benchmark designed specifically for evaluating the interactive spatial understanding of multimodal agents in complex real-world tasks. Integrating eight heterogeneous simulation backends under a shared, simulator-agnostic protocol, SpatialWorld features 760 human-annotated tasks across diverse domains (e.g., household routines, travel, social collaboration). Agents must solve tasks under vision-only partial observability, actively gathering egocentric visual evidence and expressing decisions via a unified, text-based action interface native to MLLMs. For reliable evaluation, each task includes a human-validated initial state, a reference trajectory, and a terminal-state verifier. Evaluating 15 advanced agents reveals that robust spatial task solving remains challenging: the strongest model, GPT-5, achieves an average task success rate (TSR) of only 17.4%, while the leading open-source model, Qwen-3.5, reaches 14.1%. Further analysis exposes a clear mismatch between task success and execution efficiency, alongside substantial domain-specific performance variations. These bottlenecks in active exploration and long-horizon planning position SpatialWorld as a rigorous testbed for future spatial agents.
匹配关键词: visual reasoning
---

[ACADEMIC - ARXIV]
标题: Transition-Based Digital Twin Modelling for Alzheimer's Disease under Sparse Longitudinal Data
作者: Yinyu Huang, Yilin Zhang, Sofia Michopoulou, Christopher Kipps, Rahman Attar
链接: https://arxiv.org/abs/2606.09671v1
完整摘要: Alzheimer's disease (AD) progression is highly heterogeneous and is typically observed through sparse and irregular longitudinal data, posing challenges for prediction and personalised monitoring. Existing machine learning approaches have improved AD prediction using multimodal data, yet often focus on static classification or cohort-level risk estimation, providing limited support for subject-specific modelling and uncertainty-aware reasoning. To address these limitations, we present a personalised digital twin framework for AD prediction and scenario-based analysis using multimodal longitudinal data. The proposed approach integrates complementary modelling strategies to capture clinical transitions and temporal dependencies across visits. Using data from the Alzheimer's Disease Neuroimaging Initiative (ADNI), including cognitive assessments, clinical variables, and MRI-derived phenotypes, the framework predicts cognitive status and diagnostic categories while quantifying predictive uncertainty and enabling patient-specific what-if trajectory analysis. Evaluation on leak-free subject-level splits demonstrates strong performance in score forecasting and diagnosis classification. In this sparse and irregular ADNI setting, transition-based modelling of adjacent visits achieved higher predictive accuracy than the sequence-based branch, suggesting that local transition modelling may be more data-efficient. While sequence models remain valuable for uncertainty-aware trajectory forecasting, local transition modelling offers a more data-efficient and robust predictive strategy. These findings highlight the importance of aligning temporal modelling strategies with clinical data structure and suggest that transition-based digital twin formulations may provide a practical and interpretable approach for personalised disease forecasting in neurodegenerative disorders.
匹配关键词: embodied AI
---

[ACADEMIC - ARXIV]
标题: From 0-to-1 to 1-to-N: Reproducible Engineering Evidence for MetaAI Recursive Self-Design
作者: Dun Li, Jiatao Li, Hongzhi Li
链接: https://arxiv.org/abs/2606.09663v1
完整摘要: Recursive self-design refers to AI-assisted modification of the mechanisms by which an AI system is built, evaluated, and improved. This paper treats MetaAI not as a mature paradigm, but as a working term for a human-seeded, AI-expanded development pattern in which the design space itself becomes a target of modification. We propose an operational evidence framework with four criteria: inspectable target system, meta-level modifier, feedback-directed selection, and recursive continuation. We then map public systems, including Darwin Goedel Machine (DGM), STOP, Goedel Agent, and ShinkaEvolve, against these criteria. DGM provides the most direct currently reported evidence: its published results show improvement from 20% to 50% on SWE-bench Verified and from 14.2% to 30.7% on full Polyglot after 80 iterations, with ablations suggesting that both open-ended exploration and self-improvement contribute. Finally, we provide MetaAI-Mini, a reproducible HumanEval-based protocol and codebase. Because no completed model run is included in this build, MetaAI-Mini is reported as a protocol rather than as an experimental result.
匹配关键词: embodied AI
---

[ACADEMIC - ARXIV]
标题: Beyond Accuracy: Community Perspectives on Machine Translation
作者: Yujun Wang, Ehud Reiter, Shimei Pan, Steffen Eger, Wei Zhao
链接: https://arxiv.org/abs/2606.09655v1
完整摘要: Despite remarkable progress in machine translation (MT), non-AI communities have raised growing concerns about MT systems, suggesting a noticeable gap between technical advancement and the needs of real-world users. For instance, while NLP researchers focus on benchmark performance, end users care about ethical concerns, trust, reliability, costs, and more. We argue that listening to various user communities is essential so that research efforts would be directed towards the problems that the communities care about. To this end, we present a large-scale analysis, for the first time, that investigates what four stakeholder communities (AI developers, professional translators, language learners, and language service providers) post about MT technology on social media. To do so, we construct a dataset of 79,286 posts and comments from Reddit, Facebook, Bluesky, and Mastodon from 2019 to 2025, and analyse where these communities disagree, and how and why. Overall, we find that communities often disagree, and even show strong conflicts due to polarised sentiments on topics such as translation quality, efficiency, and reliability. This is because these communities approach these topics differently: the AI community frames them as technical and computational problems, while non-AI (user) communities care more about quality nuances, time savings, user trust, and broader social issues.
匹配关键词: embodied AI
---

[ACADEMIC - ARXIV]
标题: Data-driven discovery of governing differential equations across physical systems
作者: Siyu Lou, Hao Xu, Wenguan Wang, Lu Lu, Hao Sun, Yang Liu, Linfeng Zhang, Dongxiao Zhang, Yuntian Chen
链接: https://arxiv.org/abs/2606.09638v1
完整摘要: Differential equations play a critical role in scientific discovery because they provide a mathematical framework to describe the behaviour of physical phenomena. As a promising alternative to traditional first principles, data-driven differential equation discovery has attracted increasing attention for its ability to infer governing laws directly from experimental or simulated data, especially when the underlying physics is unclear. However, the field has expanded rapidly along diverse methodological directions, particularly with the emergence of AI-based approaches, and still lacks a clear organizing perspective. In this Review, we propose a problem-oriented perspective on data-driven differential equation discovery. We first introduce a two-dimensional phase diagram of equation discoverability, where discovery problems are organized according to structural complexity and coefficient complexity. This phase diagram shows how the field has moved from the discovery of sparse equations with simple coefficients toward more complex governing laws with richer structures and more flexible parameterizations. It also clarifies why different methodological families succeed or fail in different problem settings. We then present the representation-evaluation-optimization (REO) framework as a fundamental abstraction of the discovery process. By identifying the core problems of equation discovery that persist across algorithmic variations, REO shifts the discussion from individual algorithms to the fundamental principles that determine discoverability. We connect these perspectives to applications across physics and adjacent sciences, and argue that the next challenge is not merely recovering equations, but using them to revise existing theories, distil mechanisms and form new scientific concepts.
匹配关键词: embodied AI
---

[ACADEMIC - ARXIV]
标题: Civil Court Simulation with Large Language Models
作者: Yifan Chen, Haitao Li, Kaiyuan Zhang, Yueyue Wu, Qingyao Ai, Yiqun Liu
链接: https://arxiv.org/abs/2606.09632v1
完整摘要: Court simulation bridges legal education and judicial practice, yet human-based simulations are costly and difficult to scale. Large language models (LLMs) offer a scalable alternative, but existing court-simulation research mainly focuses on criminal cases. Civil litigation is more common in practice and harder to simulate because its claims, liability, and remedies are more flexible. We present a multi-agent court simulation framework for Chinese civil cases. The framework organizes role-based interaction through a five-stage civil trial procedure and integrates memory module and statute retrieval to support long-process adjudication. Experiments show that the framework produces reliable civil judgments, with clear strengths in liability allocation and multi-item adjudication. Further experiments show that memory quality substantially affects downstream simulation quality. Through a five-layer factor framework, we analyze how legal grounding, information conditions, judicial capability and role orientation, organizational pressure, and social context affect the framework's reliability and behavior. These results support the effectiveness of the proposed framework for civil court simulation. The dataset and code are available at: https://github.com/foggpoy/Civil-Court.
匹配关键词: embodied AI
---

[ACADEMIC - ARXIV]
标题: Modeling Components and Connections in Cyber-Physical Systems
作者: Kate Sanborn, Tanuj Kenchannavar, Vakul Nath, Jonathan Sprinkle
链接: https://arxiv.org/abs/2606.09645v1
完整摘要: Text based configuration files for cyber-physical systems show the hierarchy of component modules well but often hide the details of connections and interfaces between modules. A model-based visual approach to these configuration files can better capture this information. The XML structure of Robot Operating System (ROS) launch files can be improved using a modeling approach. This paper presents ROSLaunchVisual, a model-integrated environment built on WebGME for designing, visualizing, and managing ROS launch files. The tool raises the level of abstraction by allowing developers to create and modify launch files using a graphical interface that represents nodes, publishers, subscribers, and arguments as interconnected components. The tool provides a dynamic system analysis that can then be used in the static development and analysis of new and existing launch files. ROSLaunchVisual incorporates features such as metamodel-driven validation, automatic import/export of launch files, and visual communication mapping. Plugins further enhance functionality by updating libraries, checking for semantic errors, and managing remaps. By making launch file creation more intuitive and less error-prone, ROSLaunchVisual improves development efficiency and system understanding, especially in collaborative or large-scale robotics projects.
匹配关键词: robotics
---

[ACADEMIC - ARXIV]
标题: Physics-Aware Sparse Learning and Selective Online Adaptation for Euler-Lagrange Robot Dynamics
作者: Rishabh Dev Yadav, Samaksh Ujjawal, Sihao Sun, Spandan Roy, Wei Pan
链接: https://arxiv.org/abs/2606.09640v1
完整摘要: Accurate dynamics models are essential for model-based robotic control, yet nominal Euler--Lagrange models often become inaccurate in the presence of payload variation, unmodeled coupling, friction, aerodynamic effects, and changing operating conditions. Most learning-based correction methods improve prediction accuracy by introducing a single additive residual, but do not preserve the internal mechanical structure of Euler--Lagrange systems. This leads to models that do not preserve symmetry, positive-definiteness, or the coupling between inertia and velocity-dependent terms, which can result in physically inconsistent predictions and reduced reliability when embedded in model-based controllers. We propose a structure-preserving residual learning framework that decomposes model mismatch into an inertia correction, the corresponding induced Coriolis term, and a generalized-force residual. The mechanical component is learned under physical constraints, while the disturbance-sensitive component is represented through a sparse history-dependent latent interaction model and adapted online using Bayesian linear regression. This separation preserves key mechanical structure while restricting adaptation to the part of the dynamics most affected by changing conditions. Experiments across multiple robotic platforms, including mobile, aerial, and manipulator systems, show that the proposed method improves dynamics prediction and trajectory tracking under coupled and time-varying dynamics. These results highlight the value of combining structured residual modeling, compact latent interaction selection, and selective online adaptation for real-world model-based control.
匹配关键词: robotics
---

[ACADEMIC - ARXIV]
标题: ReCoVLA: VLM-Guided Reward Compilation for Failure Recovery in Vision-Language-Action Policies
作者: Haodi Hu, Chung-Ta Huang, Jing Liu, Ye Wang, Kei Suzuki, Matthew Brand, Toshiaki Koike-Akino
链接: https://arxiv.org/abs/2606.09630v1
完整摘要: Vision-language-action (VLA) policies provide strong priors for language-conditioned manipulation, but remain brittle in off-nominal states requiring targeted recovery. We propose ReCoVLA -- a failure-conditioned residual recovery framework that keeps a pretrained VLA policy frozen, uses an external vision-language model (VLM) to infer the failure mode and recovery stage, and compiles a structured reward from task-relevant components. Rather than using the VLM to generate actions or rewards directly, ReCoVLA uses it as a semantic reward selector: it predicts a recovery descriptor and reward mask for in-simulation residual-policy training, followed by zero-shot sim-to-real deployment of the trained recovery policies. This decouples high-level failure understanding from low-level corrective control to support different VLAs. Experiments across short-horizon, long-horizon, and contact-rich manipulation tasks show that ReCoVLA outperforms the tested baselines on average. In simulation, our reward compiler improves average success from 36.7% for the fine-tuned $π_{0.5}$ baseline to 66.7%. In physical zero-shot sim-to-real experiments, ReCoVLA achieves the best average performance, with 61.7% success.
匹配关键词: robotics
---

[ACADEMIC - ARXIV]
标题: Motion planning for hundreds of floating robots
作者: Jan Kamm, Antonio Terpin, Raffaello D'Andrea, Aswin Ramachandran
链接: https://arxiv.org/abs/2606.09620v1
完整摘要: Planning collision-free motion for large robot fleets is difficult because collision avoidance induces strong inter-agent coupling that grows rapidly with team size. We consider omnidirectional floating robots on water, where choreographies are specified by sparse keyframes and an interactive tool must generate trajectories within seconds, even when transitions span minutes and thousands of time steps. We propose a scalable pipeline that builds a collision graph from an initialization, decomposes the coupled problem into interaction clusters, and solves clusters independently (and in parallel) with robustness mechanisms for common decomposition pathologies. We validate the approach in simulations up to 500 robots. The synthesized trajectories have also been deployed in two real-world demonstrations, on Lake Zürich with a fleet of 24 Way of Water crafts and at the Time Space Existence 2025 Venice Biennale.
匹配关键词: robotics
---

[ACADEMIC - ARXIV]
标题: DexPIE: Stable Dexterous Policy Improvement from Real-World Experience
作者: Ruizhe Liao, Wenrui Chen, Liangji Zeng, Haoran Lin, Fan Yang, Kailun Yang, Yaonan Wang
链接: https://arxiv.org/abs/2606.09615v1
完整摘要: Dexterous manipulation presents substantial challenges for imitation learning due to its high-dimensional action space and complex contact-rich dynamics. Policies trained purely from demonstrations often suffer from compounding errors during deployment and require large amounts of expert data to achieve reliable performance. To move beyond the limitations of demonstration data, in this work, we propose DexPIE, a post-training framework for dexterous policy improvement from experience collected through real-world deployment. First, DexPIE enables effective exploration coverage through a dexterous-hand-adapted intervention system and multi-stage DAgger-style data collection across initial and intermediate task stages, providing reliable supervision for accurate policy evaluation. To reduce temporal noise between post-training rollouts and demonstration data, we introduce asynchronous inference in the relative action space, which better aligns rollout data with demonstrated behavior and allows the critic to learn a value function induced by a more consistent underlying policy. Finally, DexPIE improves the policy through conditioning on a continuous optimality indicator, allowing the policy to leverage the quality of data in a more fine-grained manner. Across three challenging real-world dexterous manipulation tasks, DexPIE achieves a 37% improvement in success rate over the demonstration-based reference policy, outperforming all baseline methods and demonstrating stronger robustness. The source code and dataset will be made publicly available.
匹配关键词: robotics
---

[ACADEMIC - ARXIV]
标题: Modeling Components and Connections in Cyber-Physical Systems
作者: Kate Sanborn, Tanuj Kenchannavar, Vakul Nath, Jonathan Sprinkle
链接: https://arxiv.org/abs/2606.09645v1
完整摘要: Text based configuration files for cyber-physical systems show the hierarchy of component modules well but often hide the details of connections and interfaces between modules. A model-based visual approach to these configuration files can better capture this information. The XML structure of Robot Operating System (ROS) launch files can be improved using a modeling approach. This paper presents ROSLaunchVisual, a model-integrated environment built on WebGME for designing, visualizing, and managing ROS launch files. The tool raises the level of abstraction by allowing developers to create and modify launch files using a graphical interface that represents nodes, publishers, subscribers, and arguments as interconnected components. The tool provides a dynamic system analysis that can then be used in the static development and analysis of new and existing launch files. ROSLaunchVisual incorporates features such as metamodel-driven validation, automatic import/export of launch files, and visual communication mapping. Plugins further enhance functionality by updating libraries, checking for semantic errors, and managing remaps. By making launch file creation more intuitive and less error-prone, ROSLaunchVisual improves development efficiency and system understanding, especially in collaborative or large-scale robotics projects.
匹配关键词: humanoid robot
---

[ACADEMIC - ARXIV]
标题: Physics-Aware Sparse Learning and Selective Online Adaptation for Euler-Lagrange Robot Dynamics
作者: Rishabh Dev Yadav, Samaksh Ujjawal, Sihao Sun, Spandan Roy, Wei Pan
链接: https://arxiv.org/abs/2606.09640v1
完整摘要: Accurate dynamics models are essential for model-based robotic control, yet nominal Euler--Lagrange models often become inaccurate in the presence of payload variation, unmodeled coupling, friction, aerodynamic effects, and changing operating conditions. Most learning-based correction methods improve prediction accuracy by introducing a single additive residual, but do not preserve the internal mechanical structure of Euler--Lagrange systems. This leads to models that do not preserve symmetry, positive-definiteness, or the coupling between inertia and velocity-dependent terms, which can result in physically inconsistent predictions and reduced reliability when embedded in model-based controllers. We propose a structure-preserving residual learning framework that decomposes model mismatch into an inertia correction, the corresponding induced Coriolis term, and a generalized-force residual. The mechanical component is learned under physical constraints, while the disturbance-sensitive component is represented through a sparse history-dependent latent interaction model and adapted online using Bayesian linear regression. This separation preserves key mechanical structure while restricting adaptation to the part of the dynamics most affected by changing conditions. Experiments across multiple robotic platforms, including mobile, aerial, and manipulator systems, show that the proposed method improves dynamics prediction and trajectory tracking under coupled and time-varying dynamics. These results highlight the value of combining structured residual modeling, compact latent interaction selection, and selective online adaptation for real-world model-based control.
匹配关键词: humanoid robot
---

[ACADEMIC - ARXIV]
标题: Motion planning for hundreds of floating robots
作者: Jan Kamm, Antonio Terpin, Raffaello D'Andrea, Aswin Ramachandran
链接: https://arxiv.org/abs/2606.09620v1
完整摘要: Planning collision-free motion for large robot fleets is difficult because collision avoidance induces strong inter-agent coupling that grows rapidly with team size. We consider omnidirectional floating robots on water, where choreographies are specified by sparse keyframes and an interactive tool must generate trajectories within seconds, even when transitions span minutes and thousands of time steps. We propose a scalable pipeline that builds a collision graph from an initialization, decomposes the coupled problem into interaction clusters, and solves clusters independently (and in parallel) with robustness mechanisms for common decomposition pathologies. We validate the approach in simulations up to 500 robots. The synthesized trajectories have also been deployed in two real-world demonstrations, on Lake Zürich with a fleet of 24 Way of Water crafts and at the Time Space Existence 2025 Venice Biennale.
匹配关键词: humanoid robot
---

[ACADEMIC - ARXIV]
标题: Shape Formation for the Cooperative Transportation of Arbitrary Objects Using Multi-Agent Reinforcement Learning
作者: Mohamed Sayed, Wolfram Burgard, Tanja Katharina Kaiser
链接: https://arxiv.org/abs/2606.09610v1
完整摘要: Cooperative object transportation is essential in numerous domains, including industrial to domestic services. A popular transportation strategy is to carry objects on top of multi-robot systems. The corresponding task is typically solved by decomposing it into three interconnected subproblems: formation control, cooperative navigation, and collision avoidance. A particular challenge posed by real-world objects is their potentially arbitrary shape and non-uniform mass distribution, necessitating robot formations that securely support the object. In this work, we address the challenge of pattern formation control for transporting such real-world objects by proposing a novel multi-agent reinforcement learning approach. Our approach enables a multi-robot system to autonomously position itself underneath an object to support its weight while avoiding obstacles during the formation process. Our evaluations with diverse environments and varying numbers of robots show that our approach leads to policies that reliably produce balanced formations and generalize to cluttered scenes and objects with complex geometry and non-uniform mass distribution.
匹配关键词: humanoid robot
---

[ACADEMIC - ARXIV]
标题: CT-VAM: A Cerebello-Thalamic-Inspired Vision-Action Model for Efficient Visuomotor Control
作者: Jiacheng Li, Yize Guo, Jiabin Guo, Qingchen Liu, Jiahu Qin
链接: https://arxiv.org/abs/2606.09572v1
完整摘要: Vision-language-action models have shown strong promise for robot manipulation, yet raw language is primarily needed to specify task intent rather than to be repeatedly processed during high-frequency low-level execution. Motivated by this separation, we propose a cerebello-thalamic-inspired vision-action model (CT-VAM) for efficient task-conditioned visuomotor control. CT-VAM acts as a compact local execution policy that predicts action chunks from dualview visual observations, proprioception, and a lightweight task condition, potentially enabling a practical cloud-edge paradigm in which high-level semantic reasoning can be handled by large models while fast closed-loop control runs on local hardware. To fuse heterogeneous inputs effectively, CT-VAM introduces TARS (Thalamic Action Routing Stream), a stream-separated conditional attention decoder that independently routes action, visual and task streams, preventing dense sensory tokens from overwhelming compact task-relevant conditions. With only 68M parameters, CT-VAM achieves LIBERO success rates competitive with substantially larger VLA models, while reducing inference latency. Together with flow-consistent inpainting for asynchronous chunk execution, CT-VAM supports high-frequency control and demonstrates robust realworld deployment on resource-constrained robotic platforms.
匹配关键词: humanoid robot
---

[ACADEMIC - ARXIV]
标题: Physics-Aware Sparse Learning and Selective Online Adaptation for Euler-Lagrange Robot Dynamics
作者: Rishabh Dev Yadav, Samaksh Ujjawal, Sihao Sun, Spandan Roy, Wei Pan
链接: https://arxiv.org/abs/2606.09640v1
完整摘要: Accurate dynamics models are essential for model-based robotic control, yet nominal Euler--Lagrange models often become inaccurate in the presence of payload variation, unmodeled coupling, friction, aerodynamic effects, and changing operating conditions. Most learning-based correction methods improve prediction accuracy by introducing a single additive residual, but do not preserve the internal mechanical structure of Euler--Lagrange systems. This leads to models that do not preserve symmetry, positive-definiteness, or the coupling between inertia and velocity-dependent terms, which can result in physically inconsistent predictions and reduced reliability when embedded in model-based controllers. We propose a structure-preserving residual learning framework that decomposes model mismatch into an inertia correction, the corresponding induced Coriolis term, and a generalized-force residual. The mechanical component is learned under physical constraints, while the disturbance-sensitive component is represented through a sparse history-dependent latent interaction model and adapted online using Bayesian linear regression. This separation preserves key mechanical structure while restricting adaptation to the part of the dynamics most affected by changing conditions. Experiments across multiple robotic platforms, including mobile, aerial, and manipulator systems, show that the proposed method improves dynamics prediction and trajectory tracking under coupled and time-varying dynamics. These results highlight the value of combining structured residual modeling, compact latent interaction selection, and selective online adaptation for real-world model-based control.
匹配关键词: manipulation
---

[ACADEMIC - ARXIV]
标题: ReCoVLA: VLM-Guided Reward Compilation for Failure Recovery in Vision-Language-Action Policies
作者: Haodi Hu, Chung-Ta Huang, Jing Liu, Ye Wang, Kei Suzuki, Matthew Brand, Toshiaki Koike-Akino
链接: https://arxiv.org/abs/2606.09630v1
完整摘要: Vision-language-action (VLA) policies provide strong priors for language-conditioned manipulation, but remain brittle in off-nominal states requiring targeted recovery. We propose ReCoVLA -- a failure-conditioned residual recovery framework that keeps a pretrained VLA policy frozen, uses an external vision-language model (VLM) to infer the failure mode and recovery stage, and compiles a structured reward from task-relevant components. Rather than using the VLM to generate actions or rewards directly, ReCoVLA uses it as a semantic reward selector: it predicts a recovery descriptor and reward mask for in-simulation residual-policy training, followed by zero-shot sim-to-real deployment of the trained recovery policies. This decouples high-level failure understanding from low-level corrective control to support different VLAs. Experiments across short-horizon, long-horizon, and contact-rich manipulation tasks show that ReCoVLA outperforms the tested baselines on average. In simulation, our reward compiler improves average success from 36.7% for the fine-tuned $π_{0.5}$ baseline to 66.7%. In physical zero-shot sim-to-real experiments, ReCoVLA achieves the best average performance, with 61.7% success.
匹配关键词: manipulation
---

[ACADEMIC - ARXIV]
标题: DexPIE: Stable Dexterous Policy Improvement from Real-World Experience
作者: Ruizhe Liao, Wenrui Chen, Liangji Zeng, Haoran Lin, Fan Yang, Kailun Yang, Yaonan Wang
链接: https://arxiv.org/abs/2606.09615v1
完整摘要: Dexterous manipulation presents substantial challenges for imitation learning due to its high-dimensional action space and complex contact-rich dynamics. Policies trained purely from demonstrations often suffer from compounding errors during deployment and require large amounts of expert data to achieve reliable performance. To move beyond the limitations of demonstration data, in this work, we propose DexPIE, a post-training framework for dexterous policy improvement from experience collected through real-world deployment. First, DexPIE enables effective exploration coverage through a dexterous-hand-adapted intervention system and multi-stage DAgger-style data collection across initial and intermediate task stages, providing reliable supervision for accurate policy evaluation. To reduce temporal noise between post-training rollouts and demonstration data, we introduce asynchronous inference in the relative action space, which better aligns rollout data with demonstrated behavior and allows the critic to learn a value function induced by a more consistent underlying policy. Finally, DexPIE improves the policy through conditioning on a continuous optimality indicator, allowing the policy to leverage the quality of data in a more fine-grained manner. Across three challenging real-world dexterous manipulation tasks, DexPIE achieves a 37% improvement in success rate over the demonstration-based reference policy, outperforming all baseline methods and demonstrating stronger robustness. The source code and dataset will be made publicly available.
匹配关键词: manipulation
---

[ACADEMIC - ARXIV]
标题: CT-VAM: A Cerebello-Thalamic-Inspired Vision-Action Model for Efficient Visuomotor Control
作者: Jiacheng Li, Yize Guo, Jiabin Guo, Qingchen Liu, Jiahu Qin
链接: https://arxiv.org/abs/2606.09572v1
完整摘要: Vision-language-action models have shown strong promise for robot manipulation, yet raw language is primarily needed to specify task intent rather than to be repeatedly processed during high-frequency low-level execution. Motivated by this separation, we propose a cerebello-thalamic-inspired vision-action model (CT-VAM) for efficient task-conditioned visuomotor control. CT-VAM acts as a compact local execution policy that predicts action chunks from dualview visual observations, proprioception, and a lightweight task condition, potentially enabling a practical cloud-edge paradigm in which high-level semantic reasoning can be handled by large models while fast closed-loop control runs on local hardware. To fuse heterogeneous inputs effectively, CT-VAM introduces TARS (Thalamic Action Routing Stream), a stream-separated conditional attention decoder that independently routes action, visual and task streams, preventing dense sensory tokens from overwhelming compact task-relevant conditions. With only 68M parameters, CT-VAM achieves LIBERO success rates competitive with substantially larger VLA models, while reducing inference latency. Together with flow-consistent inpainting for asynchronous chunk execution, CT-VAM supports high-frequency control and demonstrates robust realworld deployment on resource-constrained robotic platforms.
匹配关键词: manipulation
---

[ACADEMIC - ARXIV]
标题: ContextShift: A Controlled Benchmark for Context Dependence in Object Detection
作者: Dan Zlotnikov, Alex Lazarovich, Ohad Ben-Shahar
链接: https://arxiv.org/abs/2606.09495v1
完整摘要: Modern object detectors achieve strong performance on standard benchmarks, yet their robustness to contextual variation remains insufficiently understood. Prior evaluations largely rely on aggregate metrics such as AP on uncontrolled distribution shifts, which can obscure how performance degrades under context change. We introduce ContextShift, a controlled benchmark that systematically manipulates object--context relationships while preserving object appearance. Built on COCO 2017, it isolates context as an independent variable through geometric transformations and synthetic and natural background substitutions, including a continuous compatibility axis based on normalized pointwise mutual information (NPMI). Across diverse detector architectures, we observe a consistent degradation pattern: false negatives increase by up to 227% and prediction volume decreases by up to 44%, while false positives remain stable or decline. This suppression behavior is not captured by aggregate metrics such as AP, which can mask substantial recall loss and changes in prediction dynamics. Further analysis suggests that degradation is driven less by reduced confidence than by a reduced formation of valid detection candidates. Moreover, performance along the statistical compatibility axis is non-monotonic, peaking at intermediate NPMI and degrading toward both extremes, indicating that statistical co-occurrence does not correlate linearly with effective visual context. Finally, we show that context-aware augmentation improves robustness: every augmented variant outperforms the dataset-only baseline on both original and manipulated test images, partially recovering performance lost to prediction-suppression failures by exposing models to object--context decoupling during training.
匹配关键词: manipulation
---

[ACADEMIC - ARXIV]
标题: ReCoVLA: VLM-Guided Reward Compilation for Failure Recovery in Vision-Language-Action Policies
作者: Haodi Hu, Chung-Ta Huang, Jing Liu, Ye Wang, Kei Suzuki, Matthew Brand, Toshiaki Koike-Akino
链接: https://arxiv.org/abs/2606.09630v1
完整摘要: Vision-language-action (VLA) policies provide strong priors for language-conditioned manipulation, but remain brittle in off-nominal states requiring targeted recovery. We propose ReCoVLA -- a failure-conditioned residual recovery framework that keeps a pretrained VLA policy frozen, uses an external vision-language model (VLM) to infer the failure mode and recovery stage, and compiles a structured reward from task-relevant components. Rather than using the VLM to generate actions or rewards directly, ReCoVLA uses it as a semantic reward selector: it predicts a recovery descriptor and reward mask for in-simulation residual-policy training, followed by zero-shot sim-to-real deployment of the trained recovery policies. This decouples high-level failure understanding from low-level corrective control to support different VLAs. Experiments across short-horizon, long-horizon, and contact-rich manipulation tasks show that ReCoVLA outperforms the tested baselines on average. In simulation, our reward compiler improves average success from 36.7% for the fine-tuned $π_{0.5}$ baseline to 66.7%. In physical zero-shot sim-to-real experiments, ReCoVLA achieves the best average performance, with 61.7% success.
匹配关键词: sim-to-real
---

[ACADEMIC - ARXIV]
标题: Autonomous Obstacle Removal for Excavators through Policy Learning with Particle Simulation
作者: Yuki Kadokawa, Sandro M. Alcantara Tacora, Taro Abe, Daisuke Endo, Genki Yamauchi, Takeshi Hashimoto, Takamitsu Matsubara
链接: https://arxiv.org/abs/2606.09183v1
完整摘要: Autonomous obstacle removal from the ground is an important earthwork task, but this is difficult to automate because an excavator must adapt its excavation trajectories over repeated cycles as soil-obstacle conditions change. Learning such state-dependent behavior requires a training environment that reproduces accumulated soil-obstacle interactions, including contact states, terrain deformation, and obstacle visibility. Accordingly, particle-based simulation is suitable for the relevant policy learning. However, particle simulation is computationally expensive, and repeated excavation cycles further increase the learning cost. We observe that the burial condition of an obstacle governs both task difficulty and simulation cost: deeper burial makes obstacle removal harder while also requiring more particles for accurate simulation. This observation motivates a burial-conditioned curriculum learning strategy. We propose a time-efficient sim-to-real policy learning framework in which the policy observes terrain and obstacle information from RGB-D measurements and then outputs a parameterized excavation trajectory; in this process, the simulator reproduces in a real-world excavator the same observation-action interface it uses under controllable burial conditions. The curriculum begins with shallow burial conditions and progressively increases burial depth while adjusting particle count, thus simultaneously controlling task difficulty and simulation cost. Experiments show that the proposed framework successfully learns an effective obstacle-removal policy, whereas baseline methods fail even after a full week of training. The proposed curriculum achieves effective performance within three days and achieves successful transfer to a real 12-ton excavator operating on open ground with various steel obstacles, thus demonstrating robust obstacle removal.
匹配关键词: sim-to-real
---

[ACADEMIC - ARXIV]
标题: Bridged SBI: Correcting Biased Low-Fidelity Posteriors for Cost-Efficient High-Fidelity Inference
作者: Gahee Kim, Yuki Kadokawa, Sandro M. Alcantara Tacora, Taro Abe, Daisuke Endo, Genki Yamauchi, Takeshi Hashimoto, Takamitsu Matsubara
链接: https://arxiv.org/abs/2606.09155v1
完整摘要: Accurate calibration of particle-based simulators is crucial for robotic earthwork simulation, but analytical calibration is challenging due to this task's highly nonlinear particle dynamics and the black-box nature of conventional simulators. Although simulation-based inference (SBI) can estimate posterior distributions over simulation parameters solely from forward simulations, applying SBI directly to high-fidelity (HF) particle simulators is often computationally prohibitive. Low-fidelity (LF) simulators with coarser particles can reduce this cost, but changes in particle size and particle count shift the parameter values needed to reproduce the same observation, producing biased LF posteriors. We propose Bridged SBI, which leverages a biased but informative LF posterior to guide HF inference. This method first uses inexpensive LF simulations to identify a coarse high-density parameter region, and then it learns a local residual bridge to transport LF posterior samples toward HF-consistent regions by correcting the LF--HF discrepancy. We analyze how sequential multi-fidelity SBI (Naive-MF) can suffer from LF-induced posterior miscoverage when it directly relies on the LF posterior without discrepancy correction. We then show that Bridged SBI is designed to alleviate this issue by explicitly modeling the LF--HF discrepancy through residual correction. Experiments on both sim-to-sim particle-parameter calibration and real-to-sim calibration with real soil observation show that Bridged SBI produces more accurate and reliable HF posteriors than HF-only SBI or the Naive-MF baseline, especially under limited HF simulation costs.
匹配关键词: sim-to-real
---

[ACADEMIC - ARXIV]
标题: SoccerNet 2026 Player-Centric Ball-Action Spotting:Retraining and Post-Processing Extensions to the FOOTPASS Baselines
作者: Parthsarthi Rawat
链接: https://arxiv.org/abs/2606.09679v1
完整摘要: We describe our system for the SoccerNet 2026 Player-Centric Ball-Action Spotting Challenge, which requires predicting who performs which action and when, across eight classes in broadcast soccer. Building on the three FOOTPASS baselines [1] (TAAD, TAAD+GNN, and TAAD+DST), we contribute four extensions: (1) gradient check pointing to enable full-backbone fine-tuning on a single GPU; (2) fusion of GNN logits into the DST encoder, combining graph-based tactical context with per-player visual features; (3) square-root frequency class weighting to address the 213:1 pass-to-tackle imbalance in the training data; and (4) a post processing pipeline comprising per-class logit gating, temporal frame refinement, jersey re-assignment, and a two-model ensemble. Our system achieves 0.548 Macro F1 on the test set and 0.446 on the challenge set (server evaluation).
匹配关键词: world model
---

[ACADEMIC - ARXIV]
标题: MeCo: One-Step MeanFlow-based Corrector for Multi-Channel Speech Separation
作者: Dohwan Kim, Jung-Woo Choi
链接: https://arxiv.org/abs/2606.09677v1
完整摘要: While discriminative models for multi-channel speech separation excel in reference-based metrics, they often exhibit suboptimal human listening quality. To address this, we propose a novel MeanFlow-based one-step generative corrector (MeCo). MeCo learns a conditional average velocity field to map discriminative estimates directly onto the clean speech manifold in a single step. To maximize one-step generation performance, we introduce Data-Space Optimization (DSO). DSO integrates an $\mathbf{x}_r$-loss, which penalizes prediction errors on longer displacement intervals to serve as a generative objective for human listening quality, with an Endpoint SI-SDR loss that directly optimizes terminal signal fidelity. Experiments demonstrate that MeCo achieves state-of-the-art (SOTA) performance with minimal computational overhead, simultaneously achieving superior signal fidelity and human listening quality in both in-domain and out-of-domain scenarios.
匹配关键词: world model
---

[ACADEMIC - ARXIV]
标题: Correlation Is Not Enough: Embedding Human Metadata for Individual Causal Discovery
作者: Suraj Biswas, Saurabh Gupta, Pritam Mukherjee
链接: https://arxiv.org/abs/2606.09672v1
完整摘要: Ask a pretrained biomedical language model whether "cortisol 28 ug/dL" and "stock-market volatility" are related, and it returns a cosine similarity of 0.83 on a scale where 1.0 means identical. The two share no mechanism. This is not a corner case: every off-the-shelf biomedical encoder we tested (BioBERT, PubMedBERT, BioM-ELECTRA) scores unrelated cross-domain pairs between 0.76 and 0.92 when the answer should be near zero. Accuracy on cross-domain discrimination is 0%. Retrieval systems survive this, because a language model downstream filters the noise. A Large Behavioural Model (LBM), a foundation model whose subject is a person rather than a sentence, does not: it reasons over a graph of a user's life and treats embedding proximity as evidence that two events are causally linked. False proximity writes a false causal edge, and everything downstream inherits the error. Here, embedding geometry is not a tuning knob; it is correctness. We report the fix. A contrastive pass over 72,034 pairs raises PubMedBERT BIOSSES correlation from 0.633 to 0.828 and within-vs-across-domain separation from 1.05x to 1.63x. A second pass, BODHI, mines hard negatives from edges absent in a biomedical knowledge graph and lifts separation to 2.30x and the discrimination gap to +0.392, at a 4.5% BIOSSES cost. On an Intel Xeon 6737P with AMX, OpenVINO cuts single-query latency from 1367 ms to 10 ms (133x) and reaches 555 sentences/sec. One finding contradicts standard advice: FP16 beats INT8 on this silicon at every serving batch size, and we explain why. The same model on a no-AMX Ice Lake instance runs 13-27x slower. We release the benchmark suite, training corpora, the BODHI generator, and the OpenVINO scripts.
匹配关键词: world model
---

[ACADEMIC - ARXIV]
标题: Transition-Based Digital Twin Modelling for Alzheimer's Disease under Sparse Longitudinal Data
作者: Yinyu Huang, Yilin Zhang, Sofia Michopoulou, Christopher Kipps, Rahman Attar
链接: https://arxiv.org/abs/2606.09671v1
完整摘要: Alzheimer's disease (AD) progression is highly heterogeneous and is typically observed through sparse and irregular longitudinal data, posing challenges for prediction and personalised monitoring. Existing machine learning approaches have improved AD prediction using multimodal data, yet often focus on static classification or cohort-level risk estimation, providing limited support for subject-specific modelling and uncertainty-aware reasoning. To address these limitations, we present a personalised digital twin framework for AD prediction and scenario-based analysis using multimodal longitudinal data. The proposed approach integrates complementary modelling strategies to capture clinical transitions and temporal dependencies across visits. Using data from the Alzheimer's Disease Neuroimaging Initiative (ADNI), including cognitive assessments, clinical variables, and MRI-derived phenotypes, the framework predicts cognitive status and diagnostic categories while quantifying predictive uncertainty and enabling patient-specific what-if trajectory analysis. Evaluation on leak-free subject-level splits demonstrates strong performance in score forecasting and diagnosis classification. In this sparse and irregular ADNI setting, transition-based modelling of adjacent visits achieved higher predictive accuracy than the sequence-based branch, suggesting that local transition modelling may be more data-efficient. While sequence models remain valuable for uncertainty-aware trajectory forecasting, local transition modelling offers a more data-efficient and robust predictive strategy. These findings highlight the importance of aligning temporal modelling strategies with clinical data structure and suggest that transition-based digital twin formulations may provide a practical and interpretable approach for personalised disease forecasting in neurodegenerative disorders.
匹配关键词: world model
---

[ACADEMIC - ARXIV]
标题: Visual Prompting Meets Feature Reconstruction-Based Anomaly Detection with Dual-Teacher Supervision
作者: Mateo Diaz-Bone, Daniel Caraballo, Florian Scheidegger, Thomas Frick, Mattia Rigotti, Andrea Bartezzaghi, Roy Assaf, Niccolo Avogaro, Yagmur G. Cinar, Brown Ebouky, Filip M. Janicki, Piotr S. Kluska, Cezary Skura, Cristiano Malossi
链接: https://arxiv.org/abs/2606.09670v1
完整摘要: Recent Anomaly Detection methods achieve perfect detection and segmentation scores on well-established datasets, such as MVTec. However, many of these methods face challenges when foundational assumptions - such as consistent object scale, viewpoint, background, illumination, and centered placement - are violated. Those variations that occur render anomaly detection methods unusable in many real-world scenarios. To address these limitations, we introduce three key contributions: (1) a visual prompting pipeline that isolates objects using foreground-background masking; (2) a mechanism for unfreezing the teacher in student-teacher models to improve domain adaptability; and (3) a data augmentation strategy leveraging diffusion-generated synthetic images to enhance anomaly detection performance. We achieve a 3.5 percentage point improvement over the previous state-of-the-art on the challenging AeBAD dataset by using the Masked Multiscale Reconstruction (MMR) model as our backbone.
匹配关键词: world model
---

[ACADEMIC - ARXIV]
标题: MeCo: One-Step MeanFlow-based Corrector for Multi-Channel Speech Separation
作者: Dohwan Kim, Jung-Woo Choi
链接: https://arxiv.org/abs/2606.09677v1
完整摘要: While discriminative models for multi-channel speech separation excel in reference-based metrics, they often exhibit suboptimal human listening quality. To address this, we propose a novel MeanFlow-based one-step generative corrector (MeCo). MeCo learns a conditional average velocity field to map discriminative estimates directly onto the clean speech manifold in a single step. To maximize one-step generation performance, we introduce Data-Space Optimization (DSO). DSO integrates an $\mathbf{x}_r$-loss, which penalizes prediction errors on longer displacement intervals to serve as a generative objective for human listening quality, with an Endpoint SI-SDR loss that directly optimizes terminal signal fidelity. Experiments demonstrate that MeCo achieves state-of-the-art (SOTA) performance with minimal computational overhead, simultaneously achieving superior signal fidelity and human listening quality in both in-domain and out-of-domain scenarios.
匹配关键词: speech synthesis
---

[ACADEMIC - ARXIV]
标题: Cross-Modal Masking for Robust Silent Speech Synthesis Using sEMG and Lipreading
作者: Eder del Blanco, David Gimeno-Gómez, Eva Navas, Carlos-D. Martínez-Hinarejos, Inma Hernáez
链接: https://arxiv.org/abs/2606.09667v1
完整摘要: Speech restoration through silent speech interfaces (SSIs) has emerged as a promising assistive technology for individuals with impaired or absent laryngeal voice production. Among non-invasive SSI modalities, surface electromyography (sEMG) and video-based lipreading provide complementary articulatory information, yet their integration for continuous speech synthesis remains underexplored. Moreover, existing multimodal approaches rarely address robustness to modality degradation or temporary sensor failure, limiting their applicability in realistic scenarios. In this work, we propose a masked multimodal speech synthesis framework that jointly leverages sEMG and lipreading signals through modality masking during training. Under multispeaker settings, the proposed approach reduces word error rate by up to 14 absolute percentage points compared to the strongest unimodal baseline. Experimental results not only show that masking strategies are critical for these performance gains and robustness under low-bitrate conditions, but also that they generalize better than degradation-specific data augmentations in the presence of modality absence conditions. Phone-level analyses further reveal complementary contributions across modalities, with particularly strong benefits for vowels and for specific consonant groups. Overall, these findings demonstrate the effectiveness and robustness of masked multimodal integration for silent speech synthesis, although adaptation to laryngectomized speakers remains an open research challenge.
匹配关键词: speech synthesis
---

[ACADEMIC - ARXIV]
标题: Your U-Net Dereverberation Model is Secretly an RIR Encoder
作者: Sina Khanagha, Timo Gerkmann
链接: https://arxiv.org/abs/2606.09557v1
完整摘要: In this work, we analyze the ability of NCSN++ U-Net based audio dereverberation models to capture global room characteristics in their intermediate representations. Through an empirical study of both a state-of-the-art diffusion-based model and a discriminative counterpart, we show that deeper layers encode structured room impulse response (RIR)-dependent embeddings. Moreover, the discriminative ability of this implicit room representation correlates with dereverberation performance across objective metrics. Motivated by this observation, we propose a training strategy that explicitly conditions the network on pre-trained RIR embeddings, obtained via self-supervised contrastive learning. Incorporating RIR conditioning improves representation quality, accelerates convergence, and enhances dereverberation performance, while significantly reducing the number of reverse diffusion steps required by the diffusion-based model during inference.
匹配关键词: speech synthesis
---

[ACADEMIC - ARXIV]
标题: OpenBibleTTS: Large-Scale Speech Resources and TTS Models for Low-Resource Languages
作者: David Guzmán, Luel Hagos Beyene, Jesujoba Oluwadara Alabi, Yejin Jeon, Dietrich Klakow, David Ifeoluwa Adelani
链接: https://arxiv.org/abs/2606.09553v1
完整摘要: Recent advances in neural text-to-speech (TTS) and multilingual speech generation have substantially improved synthetic speech quality, yet these gains remain unevenly distributed across the world's languages. Existing models are still dominated by a small set of high-resource languages, while many studies of low-resource TTS are simulated on artificially downsampled high-resource corpora that do not reflect the orthographic variation and limited phonetic coverage encountered in genuinely underrepresented settings. As such, we introduce OpenBibleTTS, which is a large-scale benchmark for low-resource speech synthesis spanning 37 underrepresented languages. Moreover, a systematic comparison of various TTS architectures and large-scale speech generation models is conducted across in-domain Biblical text and out-of-domain material. Results show that no single system dominates across languages and metrics: Gemini-TTS achieves the highest listener ratings on most evaluated languages, but monolingual EveryVoice models trained on OpenBibleTTS remain strongest for intelligibility and are preferred in several African languages, while open from-scratch systems degrade sharply on out-of-domain text, revealing a persistent gap between broad multilingual coverage and reliable synthesis quality in underserved linguistic communities. We complement automatic evaluation with subjective human judgments, and open-source all processed datasets, alignments, and trained models to support future low-resource TTS research.
匹配关键词: speech synthesis
---

[ACADEMIC - ARXIV]
标题: Optical Music Recognition for Real-World Manuscripts with Synthetic Data
作者: Jiří Mayer, Martina Dvořáková, Vojtěch Dvořák, Markéta Herzánová Vlková, Filip Bím, Pavel Pecina, Samuel Šomorjai, Petr Žabička, Jan Hajič
链接: https://arxiv.org/abs/2606.09479v1
完整摘要: Optical Music Recognition (OMR) has seen major progress in model design, with end-to-end methods now capable of recognising notation at all levels of complexity. However, the impact of this progress has been limited by the visual domains of available training datasets, which are largely born-digital. Existing large collections of sheet music in libraries and other heritage institutions contain predominantly manuscripts, whose visual domains are highly diverse and different, so existing OMR systems fail when applied in the real world. These institutions are often resource-constrained, so large in-domain datasets cannot be expected. We provide a first baseline on real-world manuscripts with complex piano notation in the resource-constrained scenario. Using fine-grained music notation graph (MuNG) annotations and the Smashcima synthesis tool, we then show that while some direct transcriptions of in-domain data remain essential, domain adaptation using synthetic musical manuscript images brings significant improvement. Furthermore, the symbols used do not need to be in-domain, so the expensive fine-grained annotation can be avoided. We thus bring OMR closer to one of its stated goals: preserving and promoting musical cultural heritage.
匹配关键词: speech synthesis
---

[ACADEMIC - ARXIV]
标题: OpenBibleTTS: Large-Scale Speech Resources and TTS Models for Low-Resource Languages
作者: David Guzmán, Luel Hagos Beyene, Jesujoba Oluwadara Alabi, Yejin Jeon, Dietrich Klakow, David Ifeoluwa Adelani
链接: https://arxiv.org/abs/2606.09553v1
完整摘要: Recent advances in neural text-to-speech (TTS) and multilingual speech generation have substantially improved synthetic speech quality, yet these gains remain unevenly distributed across the world's languages. Existing models are still dominated by a small set of high-resource languages, while many studies of low-resource TTS are simulated on artificially downsampled high-resource corpora that do not reflect the orthographic variation and limited phonetic coverage encountered in genuinely underrepresented settings. As such, we introduce OpenBibleTTS, which is a large-scale benchmark for low-resource speech synthesis spanning 37 underrepresented languages. Moreover, a systematic comparison of various TTS architectures and large-scale speech generation models is conducted across in-domain Biblical text and out-of-domain material. Results show that no single system dominates across languages and metrics: Gemini-TTS achieves the highest listener ratings on most evaluated languages, but monolingual EveryVoice models trained on OpenBibleTTS remain strongest for intelligibility and are preferred in several African languages, while open from-scratch systems degrade sharply on out-of-domain text, revealing a persistent gap between broad multilingual coverage and reliable synthesis quality in underserved linguistic communities. We complement automatic evaluation with subjective human judgments, and open-source all processed datasets, alignments, and trained models to support future low-resource TTS research.
匹配关键词: TTS
---

[ACADEMIC - ARXIV]
标题: NüshuVoice: Reviving the Voice of Endangered Nüshu with Pitch-Aware Text-to-Speech
作者: Hongkun Yang, Xinhui Yi, Xiyan Zhao, Yibo Meng, Lionel Z. Wang, Lixu Wang, Yaqi Zhang, Ruiqi Chen, Xuanyue Zhao, Lanxin Zhang, Yu Zeng, Weijia Chu, Yiming Ma, Chenyu Liu, Jianghao Lin, Xin Xu
链接: https://arxiv.org/abs/2606.09295v1
完整摘要: Nüshu is an endangered phonetic script historically used by women in Jiangyong County, southern Hunan, China. While existing computational studies of Nüshu mainly focus on textual digitization and visual recognition, the acoustic reconstruction of its authentic pronunciation remains largely unexplored. Building a Nüshu text-to-speech (TTS) system is particularly challenging because available recordings are extremely limited and mostly consist of isolated syllable-level pronunciations rather than natural sentence-level utterances. In this work, we introduce NüshuVoice, the first TTS benchmark for Nüshu. We construct a sentence-level Nüshu text-to-audio dataset that aligns standardized Unicode Nüshu text, phonetic transcriptions, standard Chinese translations, and archival recordings. To synthesize speech under this extreme low-resource setting, we propose Nüshu-PitchVITS, an F0-conditioned VITS framework that leverages Nüshu's five-level pitch notation as an explicit prosodic inductive bias. Experimental results show that Nüshu-PitchVITS outperforms strong TTS baselines in spectral fidelity, pitch reconstruction, and human-rated intelligibility. We publicly release the dataset and code at: https://anonymous.4open.science/r/Nvshu-TTS-2EB6.
匹配关键词: TTS
---

[ACADEMIC - ARXIV]
标题: End-to-End Training for Discrete Token LLM based TTS System
作者: Changfeng Gao, Yong Ren, Jun Yuan, Ye Bai, Zhao You, ShiDong Shang
链接: https://arxiv.org/abs/2606.09234v1
完整摘要: Recent state-of-the-art (SOTA) text-to-speech (TTS) systems typically adopt a cascaded pipeline consisting of a speech tokenizer, an autoregressive large language model (LLM), and a diffusion based flow-matching (FM) model, with these components trained independently. In this paper, we propose a fully end-to-end (E2E) optimization framework that unifies the training of the speech tokenizer, LLM, FM model, and an additional reward model (RM). Specifically, we first jointly optimize the tokenizer using multi-task objectives derived from reconstruction for FM, next-token prediction for LLM, and multi recognition task for RM. This joint training encourages the discrete speech token space to capture acoustically and semantically salient information that is better tailored to TTS. We then further optimize the LLM using downstream reconstruction and recognition by FM and RM, which reduces inference-time mismatch and steers the LLM toward more preferred generations. Experimental results show that our E2E framework consistently outperforms cascaded baselines. On the Seed-TTS-Eval benchmark, our system achieves a word error rate (WER) of 0.78% and 1.56%, a new SOTA result with a 0.6B-parameter LLM and 0.5B-parameter FM model. These results validate that holistic E2E optimization is critical for improving discrete-token-based TTS systems with a much simpler training pipeline.
匹配关键词: TTS
---

[ACADEMIC - ARXIV]
标题: FlashTTS: Fast Streaming TTS with MTP Acceleration and X-pred Mean Flow Distillation
作者: Hanke Xie, Xiaming Ren, Dake Guo, Ruonan You, Wenhao Li, Jingbin Hu, Guobin Ma, Huakang Chen, Kejie Xu, Rui Huang, Weiguo Tan, Xianrong Wang, Lei Xi
链接: https://arxiv.org/abs/2606.09141v1
完整摘要: Recent progress in speech dialogue systems requires Text-to-Speech (TTS) models to be faster and more responsive. Modern speech dialogue systems impose two primary requirements on TTS models: low latency and support for streaming inputs and outputs. However, most existing single-codebook LLM-based TTS methods rely on multi-stage pipelines that lack native streaming capabilities. These systems typically suffer from high end-to-end latency due to slow autoregressive prediction and multi-step flow matching. To address these limitations, we propose FlashTTS, an open-source and low-latency streaming TTS framework. FlashTTS introduces a lagged multi-track architecture that natively processes streaming text and speech inputs, thereby eliminating the need for sentence-level buffering. To accelerate acoustic generation, we integrate parallel Multi-Token Prediction (MTP) with an X-pred mean flow matching decoder. This configuration achieves high-fidelity token-to-mel generation in exactly two function evaluations (2-NFE). By jointly optimizing input processing and decoding efficiency, FlashTTS offers a practical foundation for real-time speech dialogue systems. Experiments show that FlashTTS substantially reduces First-Packet Latency to 325ms compared to robust streaming baselines, all while preserving strong zero-shot voice cloning and cross-lingual intelligibility. Speech samples are available. The model code and checkpoints will be released as open source.
匹配关键词: TTS
---

[ACADEMIC - ARXIV]
标题: HoliDubber: Holistic Video Dubbing for Complex Acoustic Scenes via Text-Guided Audio Synthesis
作者: Wenhao Guan, Yifan Duan, Junxi Liu, Yu Gu, Feng Dang, Kaidi Wang, Qingyang Hong, Lin Li, Xie Chen
链接: https://arxiv.org/abs/2606.09098v1
完整摘要: Video dubbing is a cornerstone of multimedia content creation, aiming to synthesize synchronized acoustic sequences for visual streams. While Text-to-Speech (TTS) and Text-to-Audio (TTA) generation have each achieved remarkable progress, existing dubbing systems remain confined to isolated speech synthesis without incorporating sound effects and ambient audio, forcing practitioners to rely on fragmented workflows and laborious manual post-mixing. To address this limitation, we present HoliDubber, a holistic video dubbing framework that moves beyond speech-only generation by enabling the joint synthesis of speech and sound effects from a single text prompt. Specifically, HoliDubber adopts a patch-based autoregressive diffusion transformer architecture, where a causal language model autoregressively models aggregated patch embeddings to capture global temporal structure, and a Diffusion Transformer decoder generates high-fidelity continuous tokens within each patch, following a divide-and-conquer strategy. To achieve cross-modal alignment, visual features are encoded into patch-level representations and fused with audio patches via cross-attention, enabling the model to ground speech generation in the speaker's visual articulation dynamics. In addition, we introduce HoliDub-Bench, a benchmark curated from established datasets with synchronized video-text-audio triplets designed for holistic dubbing evaluation. Extensive experiments demonstrate that HoliDubber significantly outperforms existing methods across multiple benchmarks in speech quality, synchronization, and speaker similarity. Furthermore, results on HoliDub-Bench validate the effectiveness of joint speech-and-sound generation, establishing a new paradigm for holistic video dubbing in complex acoustic scenes. \footnote{The demo page of the project is https://holidubber.github.io}
匹配关键词: TTS
---

[ACADEMIC - ARXIV]
标题: SecureClaw: Clawing Back Control of LLM Agents
作者: Yuhan Ma, Stefan Schmid
链接: https://arxiv.org/abs/2606.09549v1
完整摘要: Tool-using large language model (LLM) agents face two distinct security failures: unauthorized external actions and exposure of sensitive plaintext inside the runtime before any final output check can intervene. Existing defenses usually protect one boundary, either the planner/runtime or the action sink, and therefore do not by themselves secure both surfaces. We present SecureClaw, a dual-boundary architecture that places authorization at the effect sink and plaintext confinement at the read boundary. Sensitive reads pass through a trusted gateway that replaces raw values with opaque handles and, in the evaluated deployment, bounded summaries as an explicit declassification interface. Writes that change external state follow a PREVIEW$\rightarrow$COMMIT protocol in which only a trusted executor may commit the exact canonical request authorized by policy. The runtime can still plan over summaries and symbolic references, but cannot directly dereference secrets or perform side effects. Across AgentDojo, AgentLeak, and Agent Security Bench (ASB), SecureClaw is the only defense we evaluate in a common harness that simultaneously retains usable task utility and achieves 0\% attack success rate (ASR) on ASB, 0.64\% ASR on AgentDojo, and 3.23\% overall leak on AgentLeak's attacked parity lane, which measures final-output and internal-relay leakage.
匹配关键词: ASR
---

[ACADEMIC - ARXIV]
标题: Overcoming Decoder Inconsistencies in Whisper for Dravidian and Low-Resource Languages
作者: Chowdam Venkata Kumar, Kumud Tripathi, Pankaj Wasnik
链接: https://arxiv.org/abs/2606.09535v1
完整摘要: Multilingual ASR models such as Whisper perform well on high-resource languages but exhibit substantially higher Word Error Rates (WER) for Dravidian languages compared to Indo-Aryan ones. Through linguistic and dataset analysis, we show that Dravidian languages have longer words, higher vocabulary diversity, and lower repetition, resulting in sparse token distributions and frequent character-level substitution errors. Baseline fine-tuning further reveals decoder imbalance between self-attention (linguistic context) and cross-attention (acoustic cues). Although synthetic token-repetition experiments indicate potential gains, they are impractical. Motivated by these observations, we introduce two decoder-level enhancements: Weighted-Attention, which adaptively balances attention sources, and Self-Conditioning, which reinjects intermediate predictions to improve token consistency. Experiments demonstrate consistent WER reductions for low-resource and agglutinative languages.
匹配关键词: ASR
---

[ACADEMIC - ARXIV]
标题: Is Text All You Need? Text as a Universal Information Bottleneck for Speech LLMs
作者: Ming-Hao Hsu, Yuxuan Hu, Shujie Liu, Jinyu Li, Yan Lu, Zhizheng Wu
链接: https://arxiv.org/abs/2606.09366v1
完整摘要: Large language models (LLMs) provide a powerful reasoning backbone for speech understanding, but integrating continuous acoustic signals into a frozen LLM remains challenging. Existing speech-to-LLM interfaces typically operate at two extremes: either enforcing near-discrete token alignment, which benefits transcription but loses paralinguistic information, or learning unconstrained continuous representations, which can drift away from the LLM's input space and degrade autoregressive decoding. In this work, we propose Convex Gate (C-Gate), a speech-to-LLM bridge that constrains all speech representations to lie within the LLM's input embedding manifold with an architectural convex-hull constraint. Concretely, each frame is represented as a convex combination of token embeddings, ensuring compatibility with the pretrained LLM while preserving continuous expressivity. Across automatic speech recognition (ASR) and emotion recognition, C-Gate achieves strong joint performance, improving LibriSpeech WER by up to 48.7% relative while matching or exceeding single-task emotion accuracy. Beyond performance, our analysis reveals a key insight: information is not carried by discrete token identities, but by time-resolved trajectories in the embedding space. Causal interventions confirm that both the trajectory structure and alignment to the pretrained embedding manifold are critical for performance. These results suggest that geometry, rather than token discreteness, is the fundamental design factor in speech-to-LLM interfaces, and provide a controlled regime for studying multimodal integration in frozen LLMs. We release the checkpoint, per-sample outputs, mechanism dumps, and intervention suite for replication.
匹配关键词: ASR
---

[ACADEMIC - ARXIV]
标题: Rethinking Depth: A study of the Recursive-Transformer for Speech Recognition
作者: Thomas Rolland, Carlos Carvalho, Alberto Abad
链接: https://arxiv.org/abs/2606.09357v1
完整摘要: Transformer-based architectures have led to significant improvements in Automatic Speech Recognition (ASR), often at the cost of substantially increased model sizes. A promising approach to address this issue is layer sharing through depth recursion, commonly referred to as the Recursive-Transformer, which involves repeatedly applying the same layers within the model. Despite its potential shown in other fields, this technique remains relatively unexplored in ASR. In this paper, we present an experimental study of the Recursive-Transformer applied to ASR encoder architectures. We systematically investigate the impact of recursion depth and layer allocation within the Recursive-based Transformer. Our results demonstrate that the Recursive-Transformer is a viable alternative, especially when recurrence is applied in the latent space with a restricted number of loops, obtaining comparable performance while reducing the parameter count by 66%.
匹配关键词: ASR
---

[ACADEMIC - ARXIV]
标题: A study on the impact of region specific data on the performance of Indic ASR
作者: Agneedh Basu, Pavan Kumar J, Pranav Bhat, Sujith Pulikodan, Visruth Sanka, Nihar Desai, Prasata Kumar Ghosh
链接: https://arxiv.org/abs/2606.09345v1
完整摘要: Automatic Speech Recognition (ASR) systems are widely deployed across linguistically diverse regions, yet their ability to generalize across fine-grained geographic variation remains underexplored. We present a systematic study of cross-district ASR generalization for Indian languages, analyzing the impact of regional variation on performance. Using finetuning as a controlled probe, we train models on speech from a single district and evaluate them on other districts within the same language. We examine trends across multiple train test district pairs and quantify performance differences. To assess geographic effects, we analyze the correlation between WER and inter district distance using two distance measures. Our results show consistent correlations between geographic distance and WER, highlighting the challenges of regional generalization and the need for geographically diverse speech data in ASR development and evaluation in India.
匹配关键词: ASR
---

[ACADEMIC - ARXIV]
标题: SoccerNet 2026 Player-Centric Ball-Action Spotting:Retraining and Post-Processing Extensions to the FOOTPASS Baselines
作者: Parthsarthi Rawat
链接: https://arxiv.org/abs/2606.09679v1
完整摘要: We describe our system for the SoccerNet 2026 Player-Centric Ball-Action Spotting Challenge, which requires predicting who performs which action and when, across eight classes in broadcast soccer. Building on the three FOOTPASS baselines [1] (TAAD, TAAD+GNN, and TAAD+DST), we contribute four extensions: (1) gradient check pointing to enable full-backbone fine-tuning on a single GPU; (2) fusion of GNN logits into the DST encoder, combining graph-based tactical context with per-player visual features; (3) square-root frequency class weighting to address the 213:1 pass-to-tackle imbalance in the training data; and (4) a post processing pipeline comprising per-class logit gating, temporal frame refinement, jersey re-assignment, and a two-model ensemble. Our system achieves 0.548 Macro F1 on the test set and 0.446 on the challenge set (server evaluation).
匹配关键词: audio language model
---

[ACADEMIC - ARXIV]
标题: MeCo: One-Step MeanFlow-based Corrector for Multi-Channel Speech Separation
作者: Dohwan Kim, Jung-Woo Choi
链接: https://arxiv.org/abs/2606.09677v1
完整摘要: While discriminative models for multi-channel speech separation excel in reference-based metrics, they often exhibit suboptimal human listening quality. To address this, we propose a novel MeanFlow-based one-step generative corrector (MeCo). MeCo learns a conditional average velocity field to map discriminative estimates directly onto the clean speech manifold in a single step. To maximize one-step generation performance, we introduce Data-Space Optimization (DSO). DSO integrates an $\mathbf{x}_r$-loss, which penalizes prediction errors on longer displacement intervals to serve as a generative objective for human listening quality, with an Endpoint SI-SDR loss that directly optimizes terminal signal fidelity. Experiments demonstrate that MeCo achieves state-of-the-art (SOTA) performance with minimal computational overhead, simultaneously achieving superior signal fidelity and human listening quality in both in-domain and out-of-domain scenarios.
匹配关键词: audio language model
---

[ACADEMIC - ARXIV]
标题: (Auto)formalization is supposed to be easy: Trellis process semantics for spelling out rigorous proofs
作者: Wesley Pegden
链接: https://arxiv.org/abs/2606.09674v1
完整摘要: We present Trellis: an autoformalization system that leverages LLM agents in a deterministically constrained workflow to enforce incremental progress in Lean autoformalization tasks through iterative refinement of natural language proofs. Our approach is motivated by the common mathematician's notion of what it means to have a rigorous proof in the first place: namely, that it would be routine to elaborate any part of the proof in further detail. The result is a system which aims to achieve reliable autoformalization on a modest budget and with generalist agents, with specialization to autoformalization coming not from any task-specific agent training but instead from a meaning-of-rigor inspired workflow enforced by process semantics. We link to an end-to-end Lean formalization of a recent Ramsey theory breakthrough produced by the process.
匹配关键词: audio language model
---

[ACADEMIC - ARXIV]
标题: Correlation Is Not Enough: Embedding Human Metadata for Individual Causal Discovery
作者: Suraj Biswas, Saurabh Gupta, Pritam Mukherjee
链接: https://arxiv.org/abs/2606.09672v1
完整摘要: Ask a pretrained biomedical language model whether "cortisol 28 ug/dL" and "stock-market volatility" are related, and it returns a cosine similarity of 0.83 on a scale where 1.0 means identical. The two share no mechanism. This is not a corner case: every off-the-shelf biomedical encoder we tested (BioBERT, PubMedBERT, BioM-ELECTRA) scores unrelated cross-domain pairs between 0.76 and 0.92 when the answer should be near zero. Accuracy on cross-domain discrimination is 0%. Retrieval systems survive this, because a language model downstream filters the noise. A Large Behavioural Model (LBM), a foundation model whose subject is a person rather than a sentence, does not: it reasons over a graph of a user's life and treats embedding proximity as evidence that two events are causally linked. False proximity writes a false causal edge, and everything downstream inherits the error. Here, embedding geometry is not a tuning knob; it is correctness. We report the fix. A contrastive pass over 72,034 pairs raises PubMedBERT BIOSSES correlation from 0.633 to 0.828 and within-vs-across-domain separation from 1.05x to 1.63x. A second pass, BODHI, mines hard negatives from edges absent in a biomedical knowledge graph and lifts separation to 2.30x and the discrimination gap to +0.392, at a 4.5% BIOSSES cost. On an Intel Xeon 6737P with AMX, OpenVINO cuts single-query latency from 1367 ms to 10 ms (133x) and reaches 555 sentences/sec. One finding contradicts standard advice: FP16 beats INT8 on this silicon at every serving batch size, and we explain why. The same model on a no-AMX Ice Lake instance runs 13-27x slower. We release the benchmark suite, training corpora, the BODHI generator, and the OpenVINO scripts.
匹配关键词: audio language model
---

[ACADEMIC - ARXIV]
标题: Transition-Based Digital Twin Modelling for Alzheimer's Disease under Sparse Longitudinal Data
作者: Yinyu Huang, Yilin Zhang, Sofia Michopoulou, Christopher Kipps, Rahman Attar
链接: https://arxiv.org/abs/2606.09671v1
完整摘要: Alzheimer's disease (AD) progression is highly heterogeneous and is typically observed through sparse and irregular longitudinal data, posing challenges for prediction and personalised monitoring. Existing machine learning approaches have improved AD prediction using multimodal data, yet often focus on static classification or cohort-level risk estimation, providing limited support for subject-specific modelling and uncertainty-aware reasoning. To address these limitations, we present a personalised digital twin framework for AD prediction and scenario-based analysis using multimodal longitudinal data. The proposed approach integrates complementary modelling strategies to capture clinical transitions and temporal dependencies across visits. Using data from the Alzheimer's Disease Neuroimaging Initiative (ADNI), including cognitive assessments, clinical variables, and MRI-derived phenotypes, the framework predicts cognitive status and diagnostic categories while quantifying predictive uncertainty and enabling patient-specific what-if trajectory analysis. Evaluation on leak-free subject-level splits demonstrates strong performance in score forecasting and diagnosis classification. In this sparse and irregular ADNI setting, transition-based modelling of adjacent visits achieved higher predictive accuracy than the sequence-based branch, suggesting that local transition modelling may be more data-efficient. While sequence models remain valuable for uncertainty-aware trajectory forecasting, local transition modelling offers a more data-efficient and robust predictive strategy. These findings highlight the importance of aligning temporal modelling strategies with clinical data structure and suggest that transition-based digital twin formulations may provide a practical and interpretable approach for personalised disease forecasting in neurodegenerative disorders.
匹配关键词: audio language model
---

[ACADEMIC - ARXIV]
标题: End-to-End Context Compression at Scale
作者: Ang Li, Sean McLeish, Haozhe Chen, Nimit Kalra, Zaiqian Chen, Artem Gazizov, Venkata Anoop Suhas Kumar Morisetty, Bhavya Kailkhura, Harshitha Menon, Zhuang Liu, Brian R. Bartoldson, Tom Goldstein, Sanae Lotfi, Micah Goldblum, Pavel Izmailov
链接: https://arxiv.org/abs/2606.09659v1
完整摘要: Long-context language model inference is bottlenecked by memory, as the KV cache grows with context length. Recent techniques to compress the KV cache fall short: they either degrade model quality substantially or require considerable time and compute to compress a single long prompt. Furthermore, many methods require the input to fit within the target model's context window, and are generally incompatible with modern production inference engines. Encoder-decoder compressors, which map a long token sequence to a shorter sequence of latent embeddings consumed by a decoder, are an appealing alternative in principle. However, existing approaches are not competitive with KV cache compression on the accuracy-efficiency frontier. In this work, we revisit encoder-decoder compression and close this gap. We first perform an architecture search, pre-training many variants from scratch to determine how best to design and train encoder-decoder compressors. Guided by our findings, we continually pre-train a family of 0.6B-encoder, 4B-decoder models on over 350B tokens each, at compression ratios of 1:4, 1:8, and 1:16. We introduce Latent Context Language Models (LCLMs), a family of compressors that improve the Pareto frontier across general-task performance, compression speed, and peak memory usage. We demonstrate that LCLMs serve as efficient backbones for long-horizon agents, letting the agent skim through a compressed long context and adaptively expand relevant segments on demand.
匹配关键词: KV cache
---

[ACADEMIC - ARXIV]
标题: AGENTSERVESIM: A Hardware-aware Simulator for Multi-Turn LLM Agent Serving
作者: Rakibul Hasan Rajib, Mengxin Zheng, Qian Lou
链接: https://arxiv.org/abs/2606.09613v1
完整摘要: Multi-turn LLM agents interleave model calls with external tool invocations, shifting serving from stateless request processing to stateful program execution. Serving these workloads requires scheduling, KV-cache management, and routing policies that use program-level context, including turn dependencies, tool-induced gaps, and reusable KV state. Evaluating such policies directly on real systems is costly, since each design point may require dedicated accelerator time across arrival rates, model scales, serving-instance counts, and memory hierarchies. Simulation offers a scalable alternative, but existing LLM serving simulators target stateless request-level workloads and therefore omit the core dynamics of agent serving: multi-turn program execution, cross-turn cache locality, and KV-cache residency during tool gaps. We present AGENTSERVESIM, a hardware-aware simulator for multi-turn LLM agent serving. AGENTSERVESIM evaluates serving policies at program granularity through composable modules: a Program Orchestrator preserves program identity and turn order, a Tool Simulator materializes tool-induced gaps, a Session-Aware Router maintains program-to-instance affinity for cache-aware dispatch, and a KV Residency Model tracks policy-defined KV placement across HBM, host DRAM/CXL, and eviction. Across real serving deployments and hardware configurations, AGENTSERVESIM reproduces real-system behavior within 6% error across key performance metrics while running entirely on commodity CPUs. These results show that AGENTSERVESIM enables controlled, repeatable exploration of agent-serving policies without requiring exhaustive deployment on costly accelerators.
匹配关键词: KV cache
---

[ACADEMIC - ARXIV]
标题: BUDDY: BUdget-Driven DYnamic Depth Routing for Adaptive Large Language Model Inference
作者: Yuhua Zhou, Shaoqi Yu, Shichao Weng, Changhai Zhou, Mingze Yin, Fei Yang, Aimin Pan
链接: https://arxiv.org/abs/2606.09514v1
完整摘要: Large language models (LLMs) incur high inference cost due to their depth and parameter scale. Depth pruning can reduce latency by skipping redundant Transformer blocks, but existing methods (i) provide limited control under user-specific compute budgets and (ii) typically fix the routing path, failing to adapt as the context grows during decoding. We propose Buddy, a budget-driven dynamic depth routing framework. Buddy uses a lightweight Decision Module to score intermediate layers conditioned on the input and deterministically executes the top-k layers to satisfy a given budget. To support decode-time adaptation, Buddy reuses the first-layer KV cache as a low-overhead global context source and pools it together with the newest token representation before each routing decision. When no explicit budget is provided, an optional Budget Predictor estimates an input-dependent compute level to balance quality and efficiency. Experiments on Llama-family and Qwen models show that Buddy is competitive with strong static pruning baselines and often improves the accuracy-compute trade-off, while uniquely supporting strict budget control, decode-time rerouting, and multiple budgets within a single trained model.
匹配关键词: KV cache
---

[ACADEMIC - ARXIV]
标题: From Rigid to Dynamic: Entropy-Guided Adaptive Inference for Long-Context LLMs
作者: Zhanchao Xu, Haoyang Li, Qingfa Xiao, Fei Teng, Chen Jason Zhang, Lei Chen, Qing Li
链接: https://arxiv.org/abs/2606.09508v1
完整摘要: Existing sparse attention and KV cache compression methods for long-context LLM inference typically apply fixed sparsity patterns or uniform budgets across all attention heads, overlooking the substantial variation in attention behavior among heads and contexts. We observe two distinct entropy patterns among attention heads: Rigid Heads, whose entropy stays near zero across input segments, and Dynamic Heads, whose entropy fluctuates significantly. Crucially, the distribution of these types is context-dependent and cannot be predetermined offline. We therefore propose EntropyInfer, a training-free framework that uses attention entropy to adaptively allocate compute at the granularity of individual heads and segments during prefilling. For decoding, we introduce a latent KV cache compression scheme that leverages generated output tokens, rather than prefill tokens alone, to identify and retain the most critical cache entries. Extensive experiments on Llama, Qwen and openPangu model series show that EntropyInfer consistently outperforms baselines including SnapKV, AdaKV, and CritiPrefill, achieving up to 2.39$\times$ end-to-end speedup beyond 100k tokens with minimal quality degradation compared to full attention. The code is released in https://github.com/SHA-4096/EntropyInfer.
匹配关键词: KV cache
---

[ACADEMIC - ARXIV]
标题: SIFT: Selective-Index For Fast Compute of RAG Prefill by Exploiting Attention Invariance
作者: Rya Sanovar, Srikant Bharadwaj, Hritvik Taneja, Moinuddin Qureshi
链接: https://arxiv.org/abs/2606.09441v1
完整摘要: Retrieval-Augmented Generation (RAG) injects LLM queries with relevant documents to improve response quality. This injection increases prompt length and slows time to first token (TTFT). Unlike standard queries, RAG queries have a unique property of context reuse where the same documents recur across user queries. Thus, fully recomputing documents for every RAG query does redundant compute and increases TTFT. Prior works precompute KV tensors of RAG documents offline and coarsely recompute some tokens during online prefill. However, such KV reuse is often slower than full recomputation on modern GPUs due to high-latency disk transfers. Further, such a coarse-grained recomputation degrades accuracy. To address these limitations, this paper proposes SIFT: Selective-Index For Fast Compute of RAG Prefill by Exploiting Attention Invariance. SIFT processes documents offline and extracts fine-grained locations of high attention scores for each document. Next, we identify the following attention invariance insights that enable us to exploit the extracted locations during runtime: (1) Local-Attention Invariance: The location of high attention scores within a document remain invariant to surrounding documents. This helps us predict the location of high scores where the document attends to itself. (2) Cross-Attention Consistency: Keys with high intra-document attention also attract cross-attention from subsequent documents. This helps us predict the location of high scores where the document attends to future documents. Critically, SIFT stores no KV data and only stores locations of high scores in the form of two compact bit vectors. SIFT's storage is up to 24,000x smaller than KV tensors, obviating costly disk transfers. During prefill, SIFT computes the attention only for the marked locations and improves TTFT by 1.71x while holding accuracy within 1% of full recompute.
匹配关键词: KV cache
---

[ACADEMIC - ARXIV]
标题: Next-Token Prediction Learns Generalisable Representations of Sleep Physiology
作者: Jonathan F. Carter, Lionel Tarassenko
链接: https://arxiv.org/abs/2606.09605v1
完整摘要: Foundation models offer a promising route to compress multi-modal physiological signals into compact representations of human health, with broad applications across sleep medicine, cardiology, neurology and other healthcare domains. Existing models have typically been trained with masked-reconstruction or contrastive objectives. However, masked reconstruction may be poorly suited to the stochastic nature of these signals, while contrastive approaches rely on positive-pair definitions despite the semantic invariances of physiological signals being poorly understood. In this work, we show that next-token prediction is a simple and scalable alternative. We develop Hypnos, a multi-modal sleep foundation model trained using eight different sensing modalities (e.g. EEG, ECG, respiratory signals) drawn from over 20,000 overnight polysomnography recordings. We tokenize each modality into streams of discrete tokens using residual vector quantization, then train a large auto-regressive RQ-Transformer to jointly predict the next token across all modalities in parallel. After training, Hypnos can be applied to continuous streams of sensor data from any subset of supported modalities, generating embeddings for downstream tasks. Across a range of benchmarks, Hypnos significantly outperforms existing foundation models. In sleep stage classification, we match the performance of strong supervised baselines on held-out test sets whilst using \(100\times\) less labelled data. Hypnos even generalises to daytime physiology, surpassing a dedicated ECG foundation model at detecting atrial fibrillation. Our results demonstrate that next-token prediction is a strong self-supervised objective for representation learning from multi-modal physiological signals.
匹配关键词: quantization
---

[ACADEMIC - ARXIV]
标题: EditSSC: Toward Editable Semantic Occupancy Scenes with Unconditional Diffusion Models
作者: Fatima Balde, Raoul de Charette, Alexandre Boulch
链接: https://arxiv.org/abs/2606.09273v1
完整摘要: 3D semantic scene generation is crucial for autonomous driving applications, yet most methods rely on complex 3D-specific architectures such as triplane encoders and adapted diffusion networks, limiting both their simplicity and their editing capabilities. We propose EditSSC, an editing-ready method for 3D semantic scene generation using 2D Bird's Eye View (BEV) representations and off-the-shelf latent diffusion network. Our approach reshapes 3D semantic occupancy grids into multi-channel BEV images and leverages the quantized autoencoder and UNet from Stable Diffusion with minimal modifications. We perform diffusion on the latents after quantization, which enables training-free editing capabilities. By exploiting class-to-code correspondences in the codebook, our method supports sketch-guided generation, inpainting, and outpainting without any retraining. On SemanticKITTI, EditSSC outperforms existing 3D-specific baselines on unconditional generation, demonstrating that well-established 2D architectures can be effectively repurposed for 3D scene generation and editing.
匹配关键词: quantization
---

[ACADEMIC - ARXIV]
标题: SNN-MLIR: An MLIR Dialect for Compiling Neuromorphic SNNs from NIR to Bare-Metal C
作者: Alejandro García Gener, Alvaro Rollón de Pinedo
链接: https://arxiv.org/abs/2606.09213v1
完整摘要: Spiking neural networks (SNNs) are increasingly trained in a wide range of frameworks (SnnTorch, Lava, Norse, and others) each with its own model format. The Neuromorphic Intermediate Representation (NIR) addresses this fragmentation by providing a common, framework-independent format for exchanging trained SNN models. NIR solves the exchange problem, but it stops there. It provides a description of a network, not a path to running one. Each backend is still left to implement deployment on its own, with no shared, transformable compiler representation in between. This paper presents snn-mlir, an outof-tree MLIR dialect for SNNs together with a NIR-MLIR-C compilation bridge. The dialect provides a small set of typepolymorphic operations that work identically on floating-point (f32/f64) and quantized data, so a single intermediate representation serves both simulation and hardware-oriented deployment. A Python front end reads any NIR file and emits dialect IR, automatically inserting rescaling operations to keep quantization scales consistent across layers. A reference lowering pass converts the dialect to standard linalg and arith operations, from which the toolchain produces self-contained, dependency free C11 code that compiles and runs on any C-capable CPU or embedded target. We evaluate numerical fidelity against reference outputs, portability across CPU targets, and the cost of quantization. The current scope is feedforward, fully-connected networks with a CPU backend. snn-mlir is released as open source under the Apache-2.0 license with LLVM-exception and it is already available on Github.
匹配关键词: quantization
---

[ACADEMIC - ARXIV]
标题: Understanding Quantization-Aware Training: Gradients at Quantized Weights Bias to the Low-Loss Basin
作者: Hanyang Li, Jianhao Ma, Ying Cui
链接: https://arxiv.org/abs/2606.09012v1
完整摘要: Post-training quantization (PTQ) converts a trained full-precision model into low-bit weights without task-level retraining, while quantization-aware training (QAT) incorporates quantization into the training loop. Although PTQ is efficient and often accurate at moderate bitwidths, it can fail sharply at aggressive bitwidths; QAT is more expensive but can often recover the lost accuracy. We propose a unified geometric framework that explains both PTQ failure and QAT recovery. We model full-precision training as following a low-loss \emph{river} inside a wider \emph{valley}: a normal neighborhood of the river forms a nearly flat \emph{basin}, while leaving this basin incurs a sharp loss increase. When the quantization grid is comparable to the basin width, local PTQ objectives, including rounding and Hessian-based second-order reconstruction, can select a high-loss deployed quantized point outside the basin even when nearby low-loss quantized points exist. In this regime, straight-through-estimator-based QAT has a useful bias: it evaluates gradients at the deployed quantized weights while updating latent full-precision weights, causing the gradient to sense the valley wall and acquire an inward component that steers subsequent quantized iterates back into the basin. We formalize this mechanism through a local landscape model, construct a geometric PTQ failure mode, and prove finite-time QAT recovery under local quantizer-compatibility assumptions. Experiments across vision and language models under multiple neural-network quantization schemes corroborate the predicted basin-crossing failure of PTQ and the corresponding recovery mechanism of QAT.
匹配关键词: quantization
---

[ACADEMIC - ARXIV]
标题: End-to-End Context Compression at Scale
作者: Ang Li, Sean McLeish, Haozhe Chen, Nimit Kalra, Zaiqian Chen, Artem Gazizov, Venkata Anoop Suhas Kumar Morisetty, Bhavya Kailkhura, Harshitha Menon, Zhuang Liu, Brian R. Bartoldson, Tom Goldstein, Sanae Lotfi, Micah Goldblum, Pavel Izmailov
链接: https://arxiv.org/abs/2606.09659v1
完整摘要: Long-context language model inference is bottlenecked by memory, as the KV cache grows with context length. Recent techniques to compress the KV cache fall short: they either degrade model quality substantially or require considerable time and compute to compress a single long prompt. Furthermore, many methods require the input to fit within the target model's context window, and are generally incompatible with modern production inference engines. Encoder-decoder compressors, which map a long token sequence to a shorter sequence of latent embeddings consumed by a decoder, are an appealing alternative in principle. However, existing approaches are not competitive with KV cache compression on the accuracy-efficiency frontier. In this work, we revisit encoder-decoder compression and close this gap. We first perform an architecture search, pre-training many variants from scratch to determine how best to design and train encoder-decoder compressors. Guided by our findings, we continually pre-train a family of 0.6B-encoder, 4B-decoder models on over 350B tokens each, at compression ratios of 1:4, 1:8, and 1:16. We introduce Latent Context Language Models (LCLMs), a family of compressors that improve the Pareto frontier across general-task performance, compression speed, and peak memory usage. We demonstrate that LCLMs serve as efficient backbones for long-horizon agents, letting the agent skim through a compressed long context and adaptively expand relevant segments on demand.
匹配关键词: speculative decoding
---

[ACADEMIC - ARXIV]
标题: Gradient-Guided Reward Optimization for Inference-time Alignment
作者: Hankun Lin, Ruqi Zhang
链接: https://arxiv.org/abs/2606.09635v1
完整摘要: Ensuring the reliability of Large Language Models (LLMs) under distribution drift requires inference-time adaptation. While inference-time alignment methods such as Best-of-$N$ and rejection sampling are widely used, they frame the task as a sampling-intensive, reward-guided search, leading to two key limitations: their performance is bounded by the base model's generation quality, and their reliance on imperfect reward models makes them vulnerable to reward hacking. To address these challenges, we introduce Gradient-Guided Reward Optimization (GGRO), a lightweight inference-time method that performs targeted, minimal intervention during decoding via gradient guidance. Specifically, GGRO monitors token-level entropy to identify high-uncertainty regions indicative of drift or misalignment. Upon detection, it responds by injecting nudging tokens, generated using gradient signals from an off-the-shelf reward model, to steer the generation trajectory rather than merely re-ranking samples. Experiments show that GGRO consistently improves inference-time alignment across safety, helpfulness, and reasoning benchmarks. It also increases coverage of high-quality responses and robustness to reward hacking, with minimal computational overhead. Code is available at https://github.com/lhk2004/GGRO.
匹配关键词: speculative decoding
---

[ACADEMIC - ARXIV]
标题: Automated IEP Generation from Traditional Chinese Parent-Teacher Interviews via Corpus-Grounded Feature Diffusion
作者: Kuanlin Chen, Cheng-En Ou
链接: https://arxiv.org/abs/2606.09603v1
完整摘要: Writing Individualized Education Programs (IEPs) is a high-labor, knowledge-intensive document burden; English-language research has demonstrated that generative AI can significantly reduce drafting time, yet automated IEP generation in Traditional Chinese remains virtually unexplored due to domain data scarcity, strict privacy regulations, and the absence of local evaluation benchmarks. We propose a low-resource fine-tuning pipeline centered on Corpus-Grounded Feature Diffusion (CGFD): (1) 25 dual-expert high-score seed transcripts are selected via a tau threshold with flag-aware score caps; (2) a FeatureProfile (sentence length, structure, quantification templates) is extracted from seeds and injected into LLM prompts alongside Verbalized-Sampling-style diversity control to drive diffusion; (3) 15 expert gold seeds are used as diffusion anchors, targeting 585 samples; 567 valid diffusion samples are obtained, yielding a 582-sample training set used to fine-tune Breeze-7B with QLoRA; (4) schema-constrained inference via Grammar-Constrained Decoding (GCD) enforces a hierarchical SMART Goal Ladder schema at inference time. Ablation results on a 55-sample schema stress set reveal an unexpected finding: GCD is counterproductive under Traditional Chinese token budgets -- the no-GCD path achieves 100% schema pass rate at 34% lower median latency, outperforming GCD on both reliability and speed. On the n=10 formal hold-out, the no-GCD inference path achieves BERTScore F1 = 0.779, exceeding GPT-5.4 (0.726), DeepSeek-V3.2 (0.703), Gemini-3-Flash-Preview (0.703), and Llama-4-Maverick (0.700) zero-shot baselines while maintaining fully local, air-gapped inference. This system addresses a gap in Traditional Chinese special-education NLP and offers a scalable, privacy-preserving local inference solution under an industrial engineering paradigm.
匹配关键词: speculative decoding
---

[ACADEMIC - ARXIV]
标题: Assessing Sample Quality in Conditional Generation under Compositional Shift
作者: Berker Demirel, Valentino Maiorca, Marco Fumero, Theofanis Karaletsos, Francesco Locatello
链接: https://arxiv.org/abs/2606.09601v1
完整摘要: Conditional generators provide a natural tool for controllable generation, including settings where the desired condition is a new composition of observed attributes or experimental factors. In many applications, especially in scientific domains, such models are attractive to explore conditions for which real samples are rare, expensive, or not yet observed. However, this creates a circularity for evaluation: standard conditional quality metrics require a reference target distribution, but in the extrapolative regime that distribution is unavailable by definition. We address this problem with a post-hoc, per-sample trust score for assessing conditional samples using only the training distribution. The score combines two estimable quantities: global realism, measuring compatibility with the real data manifold, and attribute-wise faithfulness, measuring whether a sample is closer to the requested attributes than to plausible alternatives. We show that the score can recover meaningful comparisons across extrapolated generations, under a mild coverage condition on the observed attributes. These comparisons enable effective filtering, ranking, and abstention of generations and can be used directly on off-the-shelf pretrained models. In biological imaging, selected samples preserve real morphological structure better and improve downstream predictive performance, while similar gains are observed on controlled vision benchmarks. Finally, we show how the score can be applied during generation, enabling abstention before full decoding. Code is available at https://github.com/berkerdemirel/faithful-cond-gen.
匹配关键词: speculative decoding
---

[ACADEMIC - ARXIV]
标题: CT-VAM: A Cerebello-Thalamic-Inspired Vision-Action Model for Efficient Visuomotor Control
作者: Jiacheng Li, Yize Guo, Jiabin Guo, Qingchen Liu, Jiahu Qin
链接: https://arxiv.org/abs/2606.09572v1
完整摘要: Vision-language-action models have shown strong promise for robot manipulation, yet raw language is primarily needed to specify task intent rather than to be repeatedly processed during high-frequency low-level execution. Motivated by this separation, we propose a cerebello-thalamic-inspired vision-action model (CT-VAM) for efficient task-conditioned visuomotor control. CT-VAM acts as a compact local execution policy that predicts action chunks from dualview visual observations, proprioception, and a lightweight task condition, potentially enabling a practical cloud-edge paradigm in which high-level semantic reasoning can be handled by large models while fast closed-loop control runs on local hardware. To fuse heterogeneous inputs effectively, CT-VAM introduces TARS (Thalamic Action Routing Stream), a stream-separated conditional attention decoder that independently routes action, visual and task streams, preventing dense sensory tokens from overwhelming compact task-relevant conditions. With only 68M parameters, CT-VAM achieves LIBERO success rates competitive with substantially larger VLA models, while reducing inference latency. Together with flow-consistent inpainting for asynchronous chunk execution, CT-VAM supports high-frequency control and demonstrates robust realworld deployment on resource-constrained robotic platforms.
匹配关键词: speculative decoding
---

[ACADEMIC - ARXIV]
标题: MeCo: One-Step MeanFlow-based Corrector for Multi-Channel Speech Separation
作者: Dohwan Kim, Jung-Woo Choi
链接: https://arxiv.org/abs/2606.09677v1
完整摘要: While discriminative models for multi-channel speech separation excel in reference-based metrics, they often exhibit suboptimal human listening quality. To address this, we propose a novel MeanFlow-based one-step generative corrector (MeCo). MeCo learns a conditional average velocity field to map discriminative estimates directly onto the clean speech manifold in a single step. To maximize one-step generation performance, we introduce Data-Space Optimization (DSO). DSO integrates an $\mathbf{x}_r$-loss, which penalizes prediction errors on longer displacement intervals to serve as a generative objective for human listening quality, with an Endpoint SI-SDR loss that directly optimizes terminal signal fidelity. Experiments demonstrate that MeCo achieves state-of-the-art (SOTA) performance with minimal computational overhead, simultaneously achieving superior signal fidelity and human listening quality in both in-domain and out-of-domain scenarios.
匹配关键词: kernel optimization
---

[ACADEMIC - ARXIV]
标题: Algorithm for Contextual Queueing Bandits with Rate-Optimal Queue Length Regret
作者: Seoungbin Bae, Dabeen Lee
链接: https://arxiv.org/abs/2606.09668v1
完整摘要: Contextual queueing bandits provide a framework for learning to schedule heterogeneous jobs under unknown context-dependent service rates. Under stochastic contexts, existing algorithms achieve $\widetilde{\mathcal{O}}(T^{-1/4})$ queue length regret, defined as the expected difference between the learner's and oracle's queue lengths at horizon $T$. In this paper, we improve this rate to $\widetilde{\mathcal{O}}(T^{-1/2})$. The key observation is that random exploration is needed only up to a carefully chosen cutoff round, rather than throughout the entire horizon. We propose CQB-$η$-2, a three-phase algorithm: (i) pure random exploration to construct an initial estimator, (ii) $η$-random exploration combined with a UCB rule to continue learning while maintaining negative drift, and (iii) pure UCB after the exploration cutoff. Our proof decomposes the queue length regret at the cutoff round. Before the cutoff, negative drift suppresses queue length differences caused by suboptimal choices. After the cutoff, the first two phases provide sufficient random exploration samples, ensuring that UCB decisions incur small departure-rate gaps. Combining these two bounds yields queue length regret of order $\widetilde{\mathcal{O}}(T^{-1/2})$. We further prove a minimax lower bound of order $Ω(T^{-1/2})$. The proof constructs two hard instances that are statistically indistinguishable up to the final service decision, and uses a queue-specific coupling argument to convert the resulting testing error into queue length regret. Together, our upper and lower bounds characterize the minimax dependence on the horizon $T$ up to logarithmic factors.
匹配关键词: kernel optimization
---

[ACADEMIC - ARXIV]
标题: In-Context Learning for Latent Space Bayesian Optimization
作者: Tuan A. Vu, Harri Lähdesmäki, Julien Martinelli
链接: https://arxiv.org/abs/2606.09664v1
完整摘要: Bayesian optimization (BO) is a central tool for sample-efficient design, and latent-space Bayesian optimization (LSBO) extends it to structured objects such as molecules and proteins. In parallel, tabular foundation models such as TabPFN and TabICL now achieve state-of-the-art regression performance and are increasingly used as BO surrogates. Because their Bayesian behavior is induced by large synthetic pretraining collections, the composition of this pretraining distribution is crucial. LSBO creates a distinctive mismatch: the induced map from latent code to objective value differs markedly from the regression tasks used to train current in-context models. We address this mismatch by complementing the pretraining stage of tabular foundation model surrogates with synthetic optimization tasks defined on the latent space of a molecular VAE. The continued-pretraining objective features a regularizer that anchors the model to the original checkpoint, preserving its broad regression prior while avoiding overspecialization to the adaptation tasks. On held-out molecular optimization benchmarks, the resulting model achieves strong performance, supporting the relevance of LSBO-specific adaptation for in-context surrogates.
匹配关键词: kernel optimization
---

[ACADEMIC - ARXIV]
标题: Muon Learns More Robust and Transferable Features than Adam
作者: Tianyu Ruan, Fengzhuo Zhang, Shuche Wang, Shihua Zhang
链接: https://arxiv.org/abs/2606.09658v1
完整摘要: Muon has recently emerged as a state-of-the-art optimizer for pretraining Large Language Models (LLMs) and vision classifiers. Despite its efficiency advantage over Adam and SGD, the feature-learning advantage of Muon remains unclear. This paper investigates Muon's feature-learning advantage through the lens of robustness and transferability. First, by evaluating pretrained models on corrupted images and texts, we show that features learned by Muon are consistently more robust than those learned by Adam and SGD across different architectures, including transformers and Convolutional Neural Networks (CNNs). Using trained layer-wise probes, we further show that this robustness advantage is reflected in larger logit margins across layers. Second, by training linear classifiers or fine-tuning full models from pretrained parameters on downstream tasks, we demonstrate that Muon-learned features transfer more effectively than those learned by Adam and SGD. This transferability advantage is further supported by the diversity of hidden states across layers, as measured by effective rank. Finally, in a representative classification problem with multi-component features, we prove that Muon attains larger margins and higher effective rank than Adam and SGD, providing theoretical support for our empirical findings.
匹配关键词: kernel optimization
---

[ACADEMIC - ARXIV]
标题: A Unifying Framework for Concept-Based Representational Similarity
作者: Grégoire Dhimoïla, Victor Boutin, Agustin Martin Picard, Thomas Fel, Thomas Serre
链接: https://arxiv.org/abs/2606.09653v1
完整摘要: Learned representations across models and modalities often exhibit striking structural similarities, suggesting shared underlying concept decompositions. However, concept alignment remains poorly defined: existing approaches optimize different objectives under the same terminology, obscuring what is actually aligned. We propose a unifying framework that decomposes alignment along two axes: what is aligned (representations vs. concepts) and at what level (instance-wise vs. distributional). This induces four corresponding properties -- instance-wise and distributional variants of translation and concept consistency -- and reveals precisely which of these guarantees existing methods provide. We further introduce \InterVenchA, an intervention-based benchmark that separately measures extraction quality, translation quality, and concept consistency. Through theory and experiments, we show that commonly assumed equivalences between alignment objectives fail in practice: optimizing one property does not reliably recover the others, and purely unsupervised objectives fail to recover meaningful instance-level alignment. We then propose the Coupled Sparse Autoencoder (CoSAE), which jointly enforces complementary alignment objectives. Strong alignment emerges only in this regime. Surprisingly, as little as 0.1\% paired data is sufficient to recover instance-level alignment when anchoring distributional objectives. Overall, our results show that concept alignment is fundamentally multi-objective: it must be defined, measured, and optimized as such.
匹配关键词: kernel optimization
---

[ACADEMIC - ARXIV]
标题: Transition-Based Digital Twin Modelling for Alzheimer's Disease under Sparse Longitudinal Data
作者: Yinyu Huang, Yilin Zhang, Sofia Michopoulou, Christopher Kipps, Rahman Attar
链接: https://arxiv.org/abs/2606.09671v1
完整摘要: Alzheimer's disease (AD) progression is highly heterogeneous and is typically observed through sparse and irregular longitudinal data, posing challenges for prediction and personalised monitoring. Existing machine learning approaches have improved AD prediction using multimodal data, yet often focus on static classification or cohort-level risk estimation, providing limited support for subject-specific modelling and uncertainty-aware reasoning. To address these limitations, we present a personalised digital twin framework for AD prediction and scenario-based analysis using multimodal longitudinal data. The proposed approach integrates complementary modelling strategies to capture clinical transitions and temporal dependencies across visits. Using data from the Alzheimer's Disease Neuroimaging Initiative (ADNI), including cognitive assessments, clinical variables, and MRI-derived phenotypes, the framework predicts cognitive status and diagnostic categories while quantifying predictive uncertainty and enabling patient-specific what-if trajectory analysis. Evaluation on leak-free subject-level splits demonstrates strong performance in score forecasting and diagnosis classification. In this sparse and irregular ADNI setting, transition-based modelling of adjacent visits achieved higher predictive accuracy than the sequence-based branch, suggesting that local transition modelling may be more data-efficient. While sequence models remain valuable for uncertainty-aware trajectory forecasting, local transition modelling offers a more data-efficient and robust predictive strategy. These findings highlight the importance of aligning temporal modelling strategies with clinical data structure and suggest that transition-based digital twin formulations may provide a practical and interpretable approach for personalised disease forecasting in neurodegenerative disorders.
匹配关键词: memory efficiency
---

[ACADEMIC - ARXIV]
标题: SpatialWorld: Benchmarking Interactive Spatial Reasoning of Multimodal Agents in Real-World Tasks
作者: Hongcheng Gao, Hailong Qu, Jingyi Tang, Jiahao Wang, Zihao Huang, Hengkang Qiao, Shihong Huang, Junming Yang, Yi Li, Hongyixuan Yuan, Wenjie Li, Bohan Zeng, Wenbo Li, Bo Wang, Jianhui Liu, Olive Huang, Haoyang Huang, Wentao Zhang, Guoqing Huang, Nan Duan, Yinpeng Dong
链接: https://arxiv.org/abs/2606.09669v1
完整摘要: Spatial reasoning is a foundational capability for multimodal large language models (MLLMs) to perceive and operate within the physical world. However, existing benchmarks predominantly rely on passive evaluation (e.g., static VQA) or simulator-specific pipelines, failing to assess general interactive spatial understanding. We introduce SpatialWorld, a unified benchmark designed specifically for evaluating the interactive spatial understanding of multimodal agents in complex real-world tasks. Integrating eight heterogeneous simulation backends under a shared, simulator-agnostic protocol, SpatialWorld features 760 human-annotated tasks across diverse domains (e.g., household routines, travel, social collaboration). Agents must solve tasks under vision-only partial observability, actively gathering egocentric visual evidence and expressing decisions via a unified, text-based action interface native to MLLMs. For reliable evaluation, each task includes a human-validated initial state, a reference trajectory, and a terminal-state verifier. Evaluating 15 advanced agents reveals that robust spatial task solving remains challenging: the strongest model, GPT-5, achieves an average task success rate (TSR) of only 17.4%, while the leading open-source model, Qwen-3.5, reaches 14.1%. Further analysis exposes a clear mismatch between task success and execution efficiency, alongside substantial domain-specific performance variations. These bottlenecks in active exploration and long-horizon planning position SpatialWorld as a rigorous testbed for future spatial agents.
匹配关键词: memory efficiency
---

[ACADEMIC - ARXIV]
标题: In-Context Learning for Latent Space Bayesian Optimization
作者: Tuan A. Vu, Harri Lähdesmäki, Julien Martinelli
链接: https://arxiv.org/abs/2606.09664v1
完整摘要: Bayesian optimization (BO) is a central tool for sample-efficient design, and latent-space Bayesian optimization (LSBO) extends it to structured objects such as molecules and proteins. In parallel, tabular foundation models such as TabPFN and TabICL now achieve state-of-the-art regression performance and are increasingly used as BO surrogates. Because their Bayesian behavior is induced by large synthetic pretraining collections, the composition of this pretraining distribution is crucial. LSBO creates a distinctive mismatch: the induced map from latent code to objective value differs markedly from the regression tasks used to train current in-context models. We address this mismatch by complementing the pretraining stage of tabular foundation model surrogates with synthetic optimization tasks defined on the latent space of a molecular VAE. The continued-pretraining objective features a regularizer that anchors the model to the original checkpoint, preserving its broad regression prior while avoiding overspecialization to the adaptation tasks. On held-out molecular optimization benchmarks, the resulting model achieves strong performance, supporting the relevance of LSBO-specific adaptation for in-context surrogates.
匹配关键词: memory efficiency
---

[ACADEMIC - ARXIV]
标题: End-to-End Context Compression at Scale
作者: Ang Li, Sean McLeish, Haozhe Chen, Nimit Kalra, Zaiqian Chen, Artem Gazizov, Venkata Anoop Suhas Kumar Morisetty, Bhavya Kailkhura, Harshitha Menon, Zhuang Liu, Brian R. Bartoldson, Tom Goldstein, Sanae Lotfi, Micah Goldblum, Pavel Izmailov
链接: https://arxiv.org/abs/2606.09659v1
完整摘要: Long-context language model inference is bottlenecked by memory, as the KV cache grows with context length. Recent techniques to compress the KV cache fall short: they either degrade model quality substantially or require considerable time and compute to compress a single long prompt. Furthermore, many methods require the input to fit within the target model's context window, and are generally incompatible with modern production inference engines. Encoder-decoder compressors, which map a long token sequence to a shorter sequence of latent embeddings consumed by a decoder, are an appealing alternative in principle. However, existing approaches are not competitive with KV cache compression on the accuracy-efficiency frontier. In this work, we revisit encoder-decoder compression and close this gap. We first perform an architecture search, pre-training many variants from scratch to determine how best to design and train encoder-decoder compressors. Guided by our findings, we continually pre-train a family of 0.6B-encoder, 4B-decoder models on over 350B tokens each, at compression ratios of 1:4, 1:8, and 1:16. We introduce Latent Context Language Models (LCLMs), a family of compressors that improve the Pareto frontier across general-task performance, compression speed, and peak memory usage. We demonstrate that LCLMs serve as efficient backbones for long-horizon agents, letting the agent skim through a compressed long context and adaptively expand relevant segments on demand.
匹配关键词: memory efficiency
---

[ACADEMIC - ARXIV]
标题: Muon Learns More Robust and Transferable Features than Adam
作者: Tianyu Ruan, Fengzhuo Zhang, Shuche Wang, Shihua Zhang
链接: https://arxiv.org/abs/2606.09658v1
完整摘要: Muon has recently emerged as a state-of-the-art optimizer for pretraining Large Language Models (LLMs) and vision classifiers. Despite its efficiency advantage over Adam and SGD, the feature-learning advantage of Muon remains unclear. This paper investigates Muon's feature-learning advantage through the lens of robustness and transferability. First, by evaluating pretrained models on corrupted images and texts, we show that features learned by Muon are consistently more robust than those learned by Adam and SGD across different architectures, including transformers and Convolutional Neural Networks (CNNs). Using trained layer-wise probes, we further show that this robustness advantage is reflected in larger logit margins across layers. Second, by training linear classifiers or fine-tuning full models from pretrained parameters on downstream tasks, we demonstrate that Muon-learned features transfer more effectively than those learned by Adam and SGD. This transferability advantage is further supported by the diversity of hidden states across layers, as measured by effective rank. Finally, in a representative classification problem with multi-component features, we prove that Muon attains larger margins and higher effective rank than Adam and SGD, providing theoretical support for our empirical findings.
匹配关键词: memory efficiency
---

[ACADEMIC - ARXIV]
标题: (Auto)formalization is supposed to be easy: Trellis process semantics for spelling out rigorous proofs
作者: Wesley Pegden
链接: https://arxiv.org/abs/2606.09674v1
完整摘要: We present Trellis: an autoformalization system that leverages LLM agents in a deterministically constrained workflow to enforce incremental progress in Lean autoformalization tasks through iterative refinement of natural language proofs. Our approach is motivated by the common mathematician's notion of what it means to have a rigorous proof in the first place: namely, that it would be routine to elaborate any part of the proof in further detail. The result is a system which aims to achieve reliable autoformalization on a modest budget and with generalist agents, with specialization to autoformalization coming not from any task-specific agent training but instead from a meaning-of-rigor inspired workflow enforced by process semantics. We link to an end-to-end Lean formalization of a recent Ramsey theory breakthrough produced by the process.
匹配关键词: agent
---

[ACADEMIC - ARXIV]
标题: SpatialWorld: Benchmarking Interactive Spatial Reasoning of Multimodal Agents in Real-World Tasks
作者: Hongcheng Gao, Hailong Qu, Jingyi Tang, Jiahao Wang, Zihao Huang, Hengkang Qiao, Shihong Huang, Junming Yang, Yi Li, Hongyixuan Yuan, Wenjie Li, Bohan Zeng, Wenbo Li, Bo Wang, Jianhui Liu, Olive Huang, Haoyang Huang, Wentao Zhang, Guoqing Huang, Nan Duan, Yinpeng Dong
链接: https://arxiv.org/abs/2606.09669v1
完整摘要: Spatial reasoning is a foundational capability for multimodal large language models (MLLMs) to perceive and operate within the physical world. However, existing benchmarks predominantly rely on passive evaluation (e.g., static VQA) or simulator-specific pipelines, failing to assess general interactive spatial understanding. We introduce SpatialWorld, a unified benchmark designed specifically for evaluating the interactive spatial understanding of multimodal agents in complex real-world tasks. Integrating eight heterogeneous simulation backends under a shared, simulator-agnostic protocol, SpatialWorld features 760 human-annotated tasks across diverse domains (e.g., household routines, travel, social collaboration). Agents must solve tasks under vision-only partial observability, actively gathering egocentric visual evidence and expressing decisions via a unified, text-based action interface native to MLLMs. For reliable evaluation, each task includes a human-validated initial state, a reference trajectory, and a terminal-state verifier. Evaluating 15 advanced agents reveals that robust spatial task solving remains challenging: the strongest model, GPT-5, achieves an average task success rate (TSR) of only 17.4%, while the leading open-source model, Qwen-3.5, reaches 14.1%. Further analysis exposes a clear mismatch between task success and execution efficiency, alongside substantial domain-specific performance variations. These bottlenecks in active exploration and long-horizon planning position SpatialWorld as a rigorous testbed for future spatial agents.
匹配关键词: agent
---

[ACADEMIC - ARXIV]
标题: From 0-to-1 to 1-to-N: Reproducible Engineering Evidence for MetaAI Recursive Self-Design
作者: Dun Li, Jiatao Li, Hongzhi Li
链接: https://arxiv.org/abs/2606.09663v1
完整摘要: Recursive self-design refers to AI-assisted modification of the mechanisms by which an AI system is built, evaluated, and improved. This paper treats MetaAI not as a mature paradigm, but as a working term for a human-seeded, AI-expanded development pattern in which the design space itself becomes a target of modification. We propose an operational evidence framework with four criteria: inspectable target system, meta-level modifier, feedback-directed selection, and recursive continuation. We then map public systems, including Darwin Goedel Machine (DGM), STOP, Goedel Agent, and ShinkaEvolve, against these criteria. DGM provides the most direct currently reported evidence: its published results show improvement from 20% to 50% on SWE-bench Verified and from 14.2% to 30.7% on full Polyglot after 80 iterations, with ablations suggesting that both open-ended exploration and self-improvement contribute. Finally, we provide MetaAI-Mini, a reproducible HumanEval-based protocol and codebase. Because no completed model run is included in this build, MetaAI-Mini is reported as a protocol rather than as an experimental result.
匹配关键词: agent
---

[ACADEMIC - ARXIV]
标题: End-to-End Context Compression at Scale
作者: Ang Li, Sean McLeish, Haozhe Chen, Nimit Kalra, Zaiqian Chen, Artem Gazizov, Venkata Anoop Suhas Kumar Morisetty, Bhavya Kailkhura, Harshitha Menon, Zhuang Liu, Brian R. Bartoldson, Tom Goldstein, Sanae Lotfi, Micah Goldblum, Pavel Izmailov
链接: https://arxiv.org/abs/2606.09659v1
完整摘要: Long-context language model inference is bottlenecked by memory, as the KV cache grows with context length. Recent techniques to compress the KV cache fall short: they either degrade model quality substantially or require considerable time and compute to compress a single long prompt. Furthermore, many methods require the input to fit within the target model's context window, and are generally incompatible with modern production inference engines. Encoder-decoder compressors, which map a long token sequence to a shorter sequence of latent embeddings consumed by a decoder, are an appealing alternative in principle. However, existing approaches are not competitive with KV cache compression on the accuracy-efficiency frontier. In this work, we revisit encoder-decoder compression and close this gap. We first perform an architecture search, pre-training many variants from scratch to determine how best to design and train encoder-decoder compressors. Guided by our findings, we continually pre-train a family of 0.6B-encoder, 4B-decoder models on over 350B tokens each, at compression ratios of 1:4, 1:8, and 1:16. We introduce Latent Context Language Models (LCLMs), a family of compressors that improve the Pareto frontier across general-task performance, compression speed, and peak memory usage. We demonstrate that LCLMs serve as efficient backbones for long-horizon agents, letting the agent skim through a compressed long context and adaptively expand relevant segments on demand.
匹配关键词: agent
---

[ACADEMIC - ARXIV]
标题: MAVIS: Multi-Agent Video Retrieval via Structured Video Understanding
作者: Jie Zhang, Qilang Ye, Hao Zhou, Haochen Liang, Fei Luo
链接: https://arxiv.org/abs/2606.09641v1
完整摘要: The dominant paradigm in video retrieval relies on embedding-based full-corpus scanning, which suffers from inherent computational inefficiency and the semantic asymmetry between information-dense videos and sparse textual queries. To bridge this gap, we introduce \textbf{MAVIS}, a novel multi-agent framework that rethinks retrieval as cooperative reasoning rather than brute-force search. MAVIS first bridges the granularity mismatch by parsing raw videos into a \textbf{Structured Semantic Library}, enabling explicit attribute-level indexing. During retrieval, a planner decomposes complex user intents into atomic sub-tasks, dispatching specialized agents to independently nominate candidates. Crucially, MAVIS employs a \textbf{Logic-aware Debate} mechanism with a strict veto protocol, where agents collaboratively prune logical mismatches to identify a compact set of ``controversial'' candidates for fine-grained verification. This agentic workflow effectively bypasses the inefficiency of full-library traversal. Extensive experiments on MSR-VTT, MSVD, and ActivityNet demonstrate that MAVIS achieves competitive performance without task-specific fine-tuning, offering a scalable and interpretable alternative to traditional dual-encoder approaches.
匹配关键词: agent
---

[ACADEMIC - ARXIV]
标题: Transition-Based Digital Twin Modelling for Alzheimer's Disease under Sparse Longitudinal Data
作者: Yinyu Huang, Yilin Zhang, Sofia Michopoulou, Christopher Kipps, Rahman Attar
链接: https://arxiv.org/abs/2606.09671v1
完整摘要: Alzheimer's disease (AD) progression is highly heterogeneous and is typically observed through sparse and irregular longitudinal data, posing challenges for prediction and personalised monitoring. Existing machine learning approaches have improved AD prediction using multimodal data, yet often focus on static classification or cohort-level risk estimation, providing limited support for subject-specific modelling and uncertainty-aware reasoning. To address these limitations, we present a personalised digital twin framework for AD prediction and scenario-based analysis using multimodal longitudinal data. The proposed approach integrates complementary modelling strategies to capture clinical transitions and temporal dependencies across visits. Using data from the Alzheimer's Disease Neuroimaging Initiative (ADNI), including cognitive assessments, clinical variables, and MRI-derived phenotypes, the framework predicts cognitive status and diagnostic categories while quantifying predictive uncertainty and enabling patient-specific what-if trajectory analysis. Evaluation on leak-free subject-level splits demonstrates strong performance in score forecasting and diagnosis classification. In this sparse and irregular ADNI setting, transition-based modelling of adjacent visits achieved higher predictive accuracy than the sequence-based branch, suggesting that local transition modelling may be more data-efficient. While sequence models remain valuable for uncertainty-aware trajectory forecasting, local transition modelling offers a more data-efficient and robust predictive strategy. These findings highlight the importance of aligning temporal modelling strategies with clinical data structure and suggest that transition-based digital twin formulations may provide a practical and interpretable approach for personalised disease forecasting in neurodegenerative disorders.
匹配关键词: tool use
---

[ACADEMIC - ARXIV]
标题: Visual Prompting Meets Feature Reconstruction-Based Anomaly Detection with Dual-Teacher Supervision
作者: Mateo Diaz-Bone, Daniel Caraballo, Florian Scheidegger, Thomas Frick, Mattia Rigotti, Andrea Bartezzaghi, Roy Assaf, Niccolo Avogaro, Yagmur G. Cinar, Brown Ebouky, Filip M. Janicki, Piotr S. Kluska, Cezary Skura, Cristiano Malossi
链接: https://arxiv.org/abs/2606.09670v1
完整摘要: Recent Anomaly Detection methods achieve perfect detection and segmentation scores on well-established datasets, such as MVTec. However, many of these methods face challenges when foundational assumptions - such as consistent object scale, viewpoint, background, illumination, and centered placement - are violated. Those variations that occur render anomaly detection methods unusable in many real-world scenarios. To address these limitations, we introduce three key contributions: (1) a visual prompting pipeline that isolates objects using foreground-background masking; (2) a mechanism for unfreezing the teacher in student-teacher models to improve domain adaptability; and (3) a data augmentation strategy leveraging diffusion-generated synthetic images to enhance anomaly detection performance. We achieve a 3.5 percentage point improvement over the previous state-of-the-art on the challenging AeBAD dataset by using the Masked Multiscale Reconstruction (MMR) model as our backbone.
匹配关键词: tool use
---

[ACADEMIC - ARXIV]
标题: Algorithm for Contextual Queueing Bandits with Rate-Optimal Queue Length Regret
作者: Seoungbin Bae, Dabeen Lee
链接: https://arxiv.org/abs/2606.09668v1
完整摘要: Contextual queueing bandits provide a framework for learning to schedule heterogeneous jobs under unknown context-dependent service rates. Under stochastic contexts, existing algorithms achieve $\widetilde{\mathcal{O}}(T^{-1/4})$ queue length regret, defined as the expected difference between the learner's and oracle's queue lengths at horizon $T$. In this paper, we improve this rate to $\widetilde{\mathcal{O}}(T^{-1/2})$. The key observation is that random exploration is needed only up to a carefully chosen cutoff round, rather than throughout the entire horizon. We propose CQB-$η$-2, a three-phase algorithm: (i) pure random exploration to construct an initial estimator, (ii) $η$-random exploration combined with a UCB rule to continue learning while maintaining negative drift, and (iii) pure UCB after the exploration cutoff. Our proof decomposes the queue length regret at the cutoff round. Before the cutoff, negative drift suppresses queue length differences caused by suboptimal choices. After the cutoff, the first two phases provide sufficient random exploration samples, ensuring that UCB decisions incur small departure-rate gaps. Combining these two bounds yields queue length regret of order $\widetilde{\mathcal{O}}(T^{-1/2})$. We further prove a minimax lower bound of order $Ω(T^{-1/2})$. The proof constructs two hard instances that are statistically indistinguishable up to the final service decision, and uses a queue-specific coupling argument to convert the resulting testing error into queue length regret. Together, our upper and lower bounds characterize the minimax dependence on the horizon $T$ up to logarithmic factors.
匹配关键词: tool use
---

[ACADEMIC - ARXIV]
标题: Cross-Modal Masking for Robust Silent Speech Synthesis Using sEMG and Lipreading
作者: Eder del Blanco, David Gimeno-Gómez, Eva Navas, Carlos-D. Martínez-Hinarejos, Inma Hernáez
链接: https://arxiv.org/abs/2606.09667v1
完整摘要: Speech restoration through silent speech interfaces (SSIs) has emerged as a promising assistive technology for individuals with impaired or absent laryngeal voice production. Among non-invasive SSI modalities, surface electromyography (sEMG) and video-based lipreading provide complementary articulatory information, yet their integration for continuous speech synthesis remains underexplored. Moreover, existing multimodal approaches rarely address robustness to modality degradation or temporary sensor failure, limiting their applicability in realistic scenarios. In this work, we propose a masked multimodal speech synthesis framework that jointly leverages sEMG and lipreading signals through modality masking during training. Under multispeaker settings, the proposed approach reduces word error rate by up to 14 absolute percentage points compared to the strongest unimodal baseline. Experimental results not only show that masking strategies are critical for these performance gains and robustness under low-bitrate conditions, but also that they generalize better than degradation-specific data augmentations in the presence of modality absence conditions. Phone-level analyses further reveal complementary contributions across modalities, with particularly strong benefits for vowels and for specific consonant groups. Overall, these findings demonstrate the effectiveness and robustness of masked multimodal integration for silent speech synthesis, although adaptation to laryngectomized speakers remains an open research challenge.
匹配关键词: tool use
---

[ACADEMIC - ARXIV]
标题: In-Context Learning for Latent Space Bayesian Optimization
作者: Tuan A. Vu, Harri Lähdesmäki, Julien Martinelli
链接: https://arxiv.org/abs/2606.09664v1
完整摘要: Bayesian optimization (BO) is a central tool for sample-efficient design, and latent-space Bayesian optimization (LSBO) extends it to structured objects such as molecules and proteins. In parallel, tabular foundation models such as TabPFN and TabICL now achieve state-of-the-art regression performance and are increasingly used as BO surrogates. Because their Bayesian behavior is induced by large synthetic pretraining collections, the composition of this pretraining distribution is crucial. LSBO creates a distinctive mismatch: the induced map from latent code to objective value differs markedly from the regression tasks used to train current in-context models. We address this mismatch by complementing the pretraining stage of tabular foundation model surrogates with synthetic optimization tasks defined on the latent space of a molecular VAE. The continued-pretraining objective features a regularizer that anchors the model to the original checkpoint, preserving its broad regression prior while avoiding overspecialization to the adaptation tasks. On held-out molecular optimization benchmarks, the resulting model achieves strong performance, supporting the relevance of LSBO-specific adaptation for in-context surrogates.
匹配关键词: tool use
---

[ACADEMIC - ARXIV]
标题: SpatialWorld: Benchmarking Interactive Spatial Reasoning of Multimodal Agents in Real-World Tasks
作者: Hongcheng Gao, Hailong Qu, Jingyi Tang, Jiahao Wang, Zihao Huang, Hengkang Qiao, Shihong Huang, Junming Yang, Yi Li, Hongyixuan Yuan, Wenjie Li, Bohan Zeng, Wenbo Li, Bo Wang, Jianhui Liu, Olive Huang, Haoyang Huang, Wentao Zhang, Guoqing Huang, Nan Duan, Yinpeng Dong
链接: https://arxiv.org/abs/2606.09669v1
完整摘要: Spatial reasoning is a foundational capability for multimodal large language models (MLLMs) to perceive and operate within the physical world. However, existing benchmarks predominantly rely on passive evaluation (e.g., static VQA) or simulator-specific pipelines, failing to assess general interactive spatial understanding. We introduce SpatialWorld, a unified benchmark designed specifically for evaluating the interactive spatial understanding of multimodal agents in complex real-world tasks. Integrating eight heterogeneous simulation backends under a shared, simulator-agnostic protocol, SpatialWorld features 760 human-annotated tasks across diverse domains (e.g., household routines, travel, social collaboration). Agents must solve tasks under vision-only partial observability, actively gathering egocentric visual evidence and expressing decisions via a unified, text-based action interface native to MLLMs. For reliable evaluation, each task includes a human-validated initial state, a reference trajectory, and a terminal-state verifier. Evaluating 15 advanced agents reveals that robust spatial task solving remains challenging: the strongest model, GPT-5, achieves an average task success rate (TSR) of only 17.4%, while the leading open-source model, Qwen-3.5, reaches 14.1%. Further analysis exposes a clear mismatch between task success and execution efficiency, alongside substantial domain-specific performance variations. These bottlenecks in active exploration and long-horizon planning position SpatialWorld as a rigorous testbed for future spatial agents.
匹配关键词: planning
---

[ACADEMIC - ARXIV]
标题: When Built-in Thinking Helps and Hurts: Constraint-Level Error Shifts in Instruction Following
作者: Sai Adith Senthil Kumar
链接: https://arxiv.org/abs/2606.09662v1
完整摘要: Large reasoning models (LRMs) often improve math and coding performance, but their effect on instruction following is unclear. We study IFEval with Qwen3 models (1.7B-32B), using same-weights Thinking ON/OFF controls; four Hunyuan models provide directional cross-family support. Aggregate pass-rate changes are small (-0.55 to -3.52 pp), yet 10-20% of prompts switch between pass and fail across modes, suggesting that thinking changes the pattern of errors--some prompts improve while others worsen--rather than uniformly degrading performance. Under a post-hoc Qwen3-derived grouping, constraint types separate into Planning (global counting, structure, coordination), which improves at the class level under thinking, and Precision (exact local form), which consistently worsens; the class-level Planning/Precision sign pattern holds directionally for all four Hunyuan models despite Hunyuan's opposite aggregate direction. Thinking also changes final-answer length; matched-length analyses substantially reduce the Precision drop, but a residual penalty remains. Analyzing thinking traces with a cross-encoder relevance metric reveals three patterns: Neutral shows a positive relevance-compliance link (r approximately 0.15); Planning shows near-zero predictive correlation (r approximately 0.02) despite measurable trace engagement, consistent with an execution gap between CE-measured trace relevance and final-answer compliance; Precision shows a small negative correlation (r approximately -0.05), with failing instances having higher mean relevance than passing ones. Activation patching across four model sizes (1.7B-14B) shows that Precision flip instances are more often restored than Planning flip instances (32-58% vs. 14-40% mean layer-restoration), with the largest gap at 14B (about 30 pp).
匹配关键词: planning
---

[ACADEMIC - ARXIV]
标题: Motion planning for hundreds of floating robots
作者: Jan Kamm, Antonio Terpin, Raffaello D'Andrea, Aswin Ramachandran
链接: https://arxiv.org/abs/2606.09620v1
完整摘要: Planning collision-free motion for large robot fleets is difficult because collision avoidance induces strong inter-agent coupling that grows rapidly with team size. We consider omnidirectional floating robots on water, where choreographies are specified by sparse keyframes and an interactive tool must generate trajectories within seconds, even when transitions span minutes and thousands of time steps. We propose a scalable pipeline that builds a collision graph from an initialization, decomposes the coupled problem into interaction clusters, and solves clusters independently (and in parallel) with robustness mechanisms for common decomposition pathologies. We validate the approach in simulations up to 500 robots. The synthesized trajectories have also been deployed in two real-world demonstrations, on Lake Zürich with a fleet of 24 Way of Water crafts and at the Time Space Existence 2025 Venice Biennale.
匹配关键词: planning
---

[ACADEMIC - ARXIV]
标题: Powering the Future of AI: Navigating the Trade-offs for Europe's Energy Transition and Net-Zero Goals
作者: Mohammad Hemmati, Gbemi Oluleye, Vassilis M. Charitopoulos
链接: https://arxiv.org/abs/2606.09617v1
完整摘要: The rapid expansion of AI globally has led to the proliferation of energy-intensive hyperscale data centres (DCs), making them as a structurally challenging component in power system planning and operation. Using a spatially explicit optimisation model of Europe across 21 AI growth scenarios, we systematically quantify additional demand, capacity requirements, emissions, and operational impacts of DCs. Results indicate that AI could drive 73-723 TWh of extra demand by 2050, risking cumulative emissions overshoots of 67-181 MtCO2 between 2030 and 2050. Our analysis indicates that after 2030, the geography of AI infrastructure will be shaped more by firm power and system flexibility than by the mere abundance of clean energy. In moderate scenarios, AI requires an additional of 200 hours of firm generation, which increases LCOE by 35 EUR/MWh in key hubs. We show that even under the pessimistic scenarios, existing infrastructure would require 70 GW additional capacity, while under managed growth pathways, this expansion could reach 226 GW. We further find DCs workload dynamics strongly shape energy dispatch, system flexibility, and emissions, while improved efficiency significantly reduces capacity needs, and system peaks. While our findings suggest that net-zero targets for 2050 may be achieved, critical emission risks may appear in the intermediate years, and the EU may compromise its carbon-neutral goals unless policies adapt to this accelerating digital transformation.
匹配关键词: planning
---

[ACADEMIC - ARXIV]
标题: SecureClaw: Clawing Back Control of LLM Agents
作者: Yuhan Ma, Stefan Schmid
链接: https://arxiv.org/abs/2606.09549v1
完整摘要: Tool-using large language model (LLM) agents face two distinct security failures: unauthorized external actions and exposure of sensitive plaintext inside the runtime before any final output check can intervene. Existing defenses usually protect one boundary, either the planner/runtime or the action sink, and therefore do not by themselves secure both surfaces. We present SecureClaw, a dual-boundary architecture that places authorization at the effect sink and plaintext confinement at the read boundary. Sensitive reads pass through a trusted gateway that replaces raw values with opaque handles and, in the evaluated deployment, bounded summaries as an explicit declassification interface. Writes that change external state follow a PREVIEW$\rightarrow$COMMIT protocol in which only a trusted executor may commit the exact canonical request authorized by policy. The runtime can still plan over summaries and symbolic references, but cannot directly dereference secrets or perform side effects. Across AgentDojo, AgentLeak, and Agent Security Bench (ASB), SecureClaw is the only defense we evaluate in a common harness that simultaneously retains usable task utility and achieves 0\% attack success rate (ASR) on ASB, 0.64\% ASR on AgentDojo, and 3.23\% overall leak on AgentLeak's attacked parity lane, which measures final-output and internal-relay leakage.
匹配关键词: planning
---

[ACADEMIC - ARXIV]
标题: A Regret Minimization Framework on Preference Learning in Large Language Models
作者: Suhwan Kim, Taehyun Cho, Geon-Hyeong Kim, Yu Jin Kim, Youngsoo Jang, Moontae Lee, Jungwoo Lee
链接: https://arxiv.org/abs/2606.09124v1
完整摘要: Reinforcement learning with verifiable rewards (RLVR) has enabled progress on reasoning-intensive tasks by relying on task-specific verifiers that provide automated correctness signals. However, many realistic language tasks are difficult to equip with reliable verifiers, motivating a growing reliance on reinforcement learning from human feedback (RLHF). In this setting, we argue that a closer examination of how human feedback should be interpreted is essential. We introduce Regret-based Preference Optimization $(\textbf{RePO})$, which reframes RLHF through $\textit{regret minimization}$ rather than reward maximization. Human preferences are often shaped by $\textit{prospective}$ anticipation of outcomes and $\textit{counterfactual}$ comparisons to alternative behaviors, rather than by immediate, outcome-independent utility. $\textbf{RePO}$ captures this structure by modeling preferences as behavior-conditioned assessments of relative suboptimality. Experiments on mathematical reasoning benchmarks and human preference datasets demonstrate consistent performance gains, indicating that $\textbf{RePO}$ is an effective and human-aligned approach for training large language models.
匹配关键词: RLHF
---

[ACADEMIC - ARXIV]
标题: A Unifying Lens on Reward Uncertainty in RLHF
作者: Ely Hahami, Yoel Zimmermann, Ray Zhou, Jack Benarroch Jedlicki
链接: https://arxiv.org/abs/2606.09073v1
完整摘要: Reinforcement learning from human feedback (RLHF) is bottlenecked by \emph{reward hacking}, where the policy exploits errors in a proxy reward model (RM) and produces high RM scores without genuine quality gains. A natural mitigation is \emph{pessimism}: penalizing rewards in regions where the RM is uncertain. However, standard scalar RMs provide no principled notion of uncertainty. We argue that the right object is a \emph{distributional} reward model $p(r\mid x,y)$. Under either a Bayesian inference or a KL-distributionally robust optimization (KL-DRO) lens, the KL-regularized RLHF objective admits a closed-form effective reward $\tilde r(x,y) = \pmβ\log\mathbb{E}_p[e^{\pm r/β}]$. The pessimistic branch unifies the prior heuristics for RM ensemble aggregation: mean aggregation, worst-case optimization (WCO), and uncertainty-weighted optimization (UWO) all emerge as limits or truncations of this single expression. This also clarifies the implicit assumptions of each existing rule.
匹配关键词: RLHF
---

[ACADEMIC - ARXIV]
标题: Multilingual Sentiment Aware Text Summarization A Reinforcement Learning Approach for Consistency Maintenance
作者: Mikhail Krasitskii, Alexander Gelbukh, Olga Kolesnikova, Grigori Sidorov
链接: https://arxiv.org/abs/2606.08940v1
完整摘要: Reinforcement Learning from Human Feedback (RLHF) has significantly improved the quality and fluency of large language models in text summarization. However, its impact on affective properties remains insufficiently understood. In this work, we study sentiment drift, a systematic shift toward neutral sentiment in RLHF-based summarization outputs compared to source texts. We conduct extensive experiments across multiple datasets, model architectures, and eight languages to analyze how alignment objectives influence sentiment preservation. Our results show that sentiment drift is a consistent phenomenon that becomes stronger with increased KL regularization strength, indicating a trade-off between alignment stability and affective fidelity. To explain this behavior, we introduce a Policy Attribution framework that decomposes the RLHF objective and quantifies the contribution of its components. Our analysis reveals that KL regularization is the primary driver of sentiment suppression across all settings. Based on these findings, we propose a sentiment-aware modification of the KL regularization term, which selectively reduces constraints on sentiment-bearing tokens. Empirical results demonstrate that this approach mitigates sentiment drift while maintaining summarization quality. Overall, our findings highlight a fundamental limitation of current alignment methods: while they improve factual consistency and safety, they may unintentionally suppress emotional expressiveness. This motivates the development of alignment strategies that explicitly account for affective preservation.
匹配关键词: RLHF
---

[ACADEMIC - ARXIV]
标题: Emergence of Context Characteristics Sensitivity in Large Language Models
作者: Nadya Yuki Wangsajaya, Haeun Yu, Isabelle Augenstein
链接: https://arxiv.org/abs/2606.09525v1
完整摘要: During instruction fine-tuning (IFT), large language models (LLMs) learn to follow instructions by using the provided context to answer a query. While prior work has studied how context characteristics correlate with context usage by the LLM, this analysis has been limited to inference time, leaving open how these relationships are acquired in the first place. Here, we measure how models' sensitivity to such characteristics shifts across successive IFT stages: supervised fine-tuning (SFT), direct preference optimization (DPO), and reinforcement learning with verifiable rewards (RLVR). Experiments across four models and three datasets show that SFT makes models more likely to use contexts that are easy to understand, such as containing high length, context-query similarity, and fluency. Post-SFT dynamics may either reinforce or resolve these preferences depending on the training dataset. Our findings reveal that context usage is actively reshaped at each IFT stage, and designing a balanced IFT dataset is important in ensuring robust context utilization of instruction-tuned models.
匹配关键词: DPO
---

[ACADEMIC - ARXIV]
标题: Transition-Based Digital Twin Modelling for Alzheimer's Disease under Sparse Longitudinal Data
作者: Yinyu Huang, Yilin Zhang, Sofia Michopoulou, Christopher Kipps, Rahman Attar
链接: https://arxiv.org/abs/2606.09671v1
完整摘要: Alzheimer's disease (AD) progression is highly heterogeneous and is typically observed through sparse and irregular longitudinal data, posing challenges for prediction and personalised monitoring. Existing machine learning approaches have improved AD prediction using multimodal data, yet often focus on static classification or cohort-level risk estimation, providing limited support for subject-specific modelling and uncertainty-aware reasoning. To address these limitations, we present a personalised digital twin framework for AD prediction and scenario-based analysis using multimodal longitudinal data. The proposed approach integrates complementary modelling strategies to capture clinical transitions and temporal dependencies across visits. Using data from the Alzheimer's Disease Neuroimaging Initiative (ADNI), including cognitive assessments, clinical variables, and MRI-derived phenotypes, the framework predicts cognitive status and diagnostic categories while quantifying predictive uncertainty and enabling patient-specific what-if trajectory analysis. Evaluation on leak-free subject-level splits demonstrates strong performance in score forecasting and diagnosis classification. In this sparse and irregular ADNI setting, transition-based modelling of adjacent visits achieved higher predictive accuracy than the sequence-based branch, suggesting that local transition modelling may be more data-efficient. While sequence models remain valuable for uncertainty-aware trajectory forecasting, local transition modelling offers a more data-efficient and robust predictive strategy. These findings highlight the importance of aligning temporal modelling strategies with clinical data structure and suggest that transition-based digital twin formulations may provide a practical and interpretable approach for personalised disease forecasting in neurodegenerative disorders.
匹配关键词: alignment
---

[ACADEMIC - ARXIV]
标题: A Unifying Framework for Concept-Based Representational Similarity
作者: Grégoire Dhimoïla, Victor Boutin, Agustin Martin Picard, Thomas Fel, Thomas Serre
链接: https://arxiv.org/abs/2606.09653v1
完整摘要: Learned representations across models and modalities often exhibit striking structural similarities, suggesting shared underlying concept decompositions. However, concept alignment remains poorly defined: existing approaches optimize different objectives under the same terminology, obscuring what is actually aligned. We propose a unifying framework that decomposes alignment along two axes: what is aligned (representations vs. concepts) and at what level (instance-wise vs. distributional). This induces four corresponding properties -- instance-wise and distributional variants of translation and concept consistency -- and reveals precisely which of these guarantees existing methods provide. We further introduce \InterVenchA, an intervention-based benchmark that separately measures extraction quality, translation quality, and concept consistency. Through theory and experiments, we show that commonly assumed equivalences between alignment objectives fail in practice: optimizing one property does not reliably recover the others, and purely unsupervised objectives fail to recover meaningful instance-level alignment. We then propose the Coupled Sparse Autoencoder (CoSAE), which jointly enforces complementary alignment objectives. Strong alignment emerges only in this regime. Surprisingly, as little as 0.1\% paired data is sufficient to recover instance-level alignment when anchoring distributional objectives. Overall, our results show that concept alignment is fundamentally multi-objective: it must be defined, measured, and optimized as such.
匹配关键词: alignment
---

[ACADEMIC - ARXIV]
标题: CineDance: Towards Next-Generation Multi-Shot Long-Form Cinematic Audio-Video Generation
作者: Yuheng Chen, Teng Hu, Yuji Wang, Qingdong He, Zhucun Xue, Qianyu Zhou, Xiangtai Li, Lizhuang Ma, Jiangning Zhang, Dacheng Tao
链接: https://arxiv.org/abs/2606.09639v1
完整摘要: The fidelity and structural diversity of training datasets fundamentally determine the capabilities of video generation models. While commercial systems showremarkableabilitytogeneratecinematicnarratives, the progress of open-source models remains limited by the scarcity of high-quality training data. To bridge this gap, we introduce CineDance-1M, a large-scale, open research Text-to-Audio-Video (T2AV) dataset designed specifically for multi-shot, long-form joint audio-video generation. Averaging 92.8 seconds and 24.2 continuous shots per video, it provides configurable, structured annotations for both audio and video modalities. This exceptional quality is achieved through a rigorous three-stage curation pipeline: i) diverse sourcing and comprehensive cleansing, ii) film-theory-inspired narrative parsing, and iii) hierarchical dual-modal captioning. For a comprehensive assessment, we propose CineBench, featuring a diverse prompt suite and a six-dimensional, human-aligned metric system tailored for complex narrative audio-video evaluation. Furthermore, we adapt LTX-2.3 into CineDance, which demonstrates exceptional single-modality quality alongside precise audio-video alignment and robust subject and environment consistency, effectively validating our curation strategy and the high quality of CineDance-1M. We anticipate that this work will serve as a solid foundation for accelerating future research in multi-shot, long-form joint audio-video generation. Our project page is available at https://aliothchen.github.io/projects/CineDance/.
匹配关键词: alignment
---

[ACADEMIC - ARXIV]
标题: Gradient-Guided Reward Optimization for Inference-time Alignment
作者: Hankun Lin, Ruqi Zhang
链接: https://arxiv.org/abs/2606.09635v1
完整摘要: Ensuring the reliability of Large Language Models (LLMs) under distribution drift requires inference-time adaptation. While inference-time alignment methods such as Best-of-$N$ and rejection sampling are widely used, they frame the task as a sampling-intensive, reward-guided search, leading to two key limitations: their performance is bounded by the base model's generation quality, and their reliance on imperfect reward models makes them vulnerable to reward hacking. To address these challenges, we introduce Gradient-Guided Reward Optimization (GGRO), a lightweight inference-time method that performs targeted, minimal intervention during decoding via gradient guidance. Specifically, GGRO monitors token-level entropy to identify high-uncertainty regions indicative of drift or misalignment. Upon detection, it responds by injecting nudging tokens, generated using gradient signals from an off-the-shelf reward model, to steer the generation trajectory rather than merely re-ranking samples. Experiments show that GGRO consistently improves inference-time alignment across safety, helpfulness, and reasoning benchmarks. It also increases coverage of high-quality responses and robustness to reward hacking, with minimal computational overhead. Code is available at https://github.com/lhk2004/GGRO.
匹配关键词: alignment
---

[ACADEMIC - ARXIV]
标题: ATN3D: Density-Aware LiDAR-Radar Early 3D Object Detection Under Extreme Sparsity
作者: Debojyoti Biswas, Xianbiao Hu
链接: https://arxiv.org/abs/2606.09634v1
完整摘要: 3D object detection is the backbone of perception for automated vehicles (AV) and broader intelligent transportation systems applications. Long-range detection is challenging because sensing evidence is sparse; yet this ``long-range'' scenario is routine in traffic. Although >30m is often labeled long-range in computer vision, on roadways it affords only approx. 1-2s for perception and decision-making. Under such extreme sparsity, two core challenges arise. First, early multimodal fusion tends to discard sparsity information and inject noise from empty or falsely occupied cells, degrading long-range recall. Second, context-agnostic uniform channel supervision favors dense and near-range samples, leaving far and small objects under-optimized, delaying the earliest detection of distant objects. We propose ``Ask The Neighbor'' (ATN3D), a LiDAR-Radar framework tailored for sparse-range conditions. ATN3D introduces (i) Density-aware early fusion with cross-modal gating that conditions fusion on per-voxel density/sparsity and Radar evidence, (ii) Occupancy-gated neighborhood aggregation with circular kernels to aggregate only from credible cells, (iii) Evidence-conditioned channel self-attention to adapt channel weights with weather/range, and (iv) a Range-aware loss that re-balances classification and localization by distance, aligning training with distance-stratified evaluation. On the VoD benchmark across clear and foggy conditions, ATN3D surpasses strong baselines: +3.55% mAP in clear weather and +8.41% mAP under simulated heavy fog; for >30m objects, gains are +3.33% (clear) and +2.09% (heavy fog). These results indicate earlier and more reliable long-range detections under sparse sensing in on-road traffic.
匹配关键词: alignment
---

[ACADEMIC - ARXIV]
标题: MeCo: One-Step MeanFlow-based Corrector for Multi-Channel Speech Separation
作者: Dohwan Kim, Jung-Woo Choi
链接: https://arxiv.org/abs/2606.09677v1
完整摘要: While discriminative models for multi-channel speech separation excel in reference-based metrics, they often exhibit suboptimal human listening quality. To address this, we propose a novel MeanFlow-based one-step generative corrector (MeCo). MeCo learns a conditional average velocity field to map discriminative estimates directly onto the clean speech manifold in a single step. To maximize one-step generation performance, we introduce Data-Space Optimization (DSO). DSO integrates an $\mathbf{x}_r$-loss, which penalizes prediction errors on longer displacement intervals to serve as a generative objective for human listening quality, with an Endpoint SI-SDR loss that directly optimizes terminal signal fidelity. Experiments demonstrate that MeCo achieves state-of-the-art (SOTA) performance with minimal computational overhead, simultaneously achieving superior signal fidelity and human listening quality in both in-domain and out-of-domain scenarios.
匹配关键词: preference learning
---

[ACADEMIC - ARXIV]
标题: Correlation Is Not Enough: Embedding Human Metadata for Individual Causal Discovery
作者: Suraj Biswas, Saurabh Gupta, Pritam Mukherjee
链接: https://arxiv.org/abs/2606.09672v1
完整摘要: Ask a pretrained biomedical language model whether "cortisol 28 ug/dL" and "stock-market volatility" are related, and it returns a cosine similarity of 0.83 on a scale where 1.0 means identical. The two share no mechanism. This is not a corner case: every off-the-shelf biomedical encoder we tested (BioBERT, PubMedBERT, BioM-ELECTRA) scores unrelated cross-domain pairs between 0.76 and 0.92 when the answer should be near zero. Accuracy on cross-domain discrimination is 0%. Retrieval systems survive this, because a language model downstream filters the noise. A Large Behavioural Model (LBM), a foundation model whose subject is a person rather than a sentence, does not: it reasons over a graph of a user's life and treats embedding proximity as evidence that two events are causally linked. False proximity writes a false causal edge, and everything downstream inherits the error. Here, embedding geometry is not a tuning knob; it is correctness. We report the fix. A contrastive pass over 72,034 pairs raises PubMedBERT BIOSSES correlation from 0.633 to 0.828 and within-vs-across-domain separation from 1.05x to 1.63x. A second pass, BODHI, mines hard negatives from edges absent in a biomedical knowledge graph and lifts separation to 2.30x and the discrimination gap to +0.392, at a 4.5% BIOSSES cost. On an Intel Xeon 6737P with AMX, OpenVINO cuts single-query latency from 1367 ms to 10 ms (133x) and reaches 555 sentences/sec. One finding contradicts standard advice: FP16 beats INT8 on this silicon at every serving batch size, and we explain why. The same model on a no-AMX Ice Lake instance runs 13-27x slower. We release the benchmark suite, training corpora, the BODHI generator, and the OpenVINO scripts.
匹配关键词: preference learning
---

[ACADEMIC - ARXIV]
标题: Transition-Based Digital Twin Modelling for Alzheimer's Disease under Sparse Longitudinal Data
作者: Yinyu Huang, Yilin Zhang, Sofia Michopoulou, Christopher Kipps, Rahman Attar
链接: https://arxiv.org/abs/2606.09671v1
完整摘要: Alzheimer's disease (AD) progression is highly heterogeneous and is typically observed through sparse and irregular longitudinal data, posing challenges for prediction and personalised monitoring. Existing machine learning approaches have improved AD prediction using multimodal data, yet often focus on static classification or cohort-level risk estimation, providing limited support for subject-specific modelling and uncertainty-aware reasoning. To address these limitations, we present a personalised digital twin framework for AD prediction and scenario-based analysis using multimodal longitudinal data. The proposed approach integrates complementary modelling strategies to capture clinical transitions and temporal dependencies across visits. Using data from the Alzheimer's Disease Neuroimaging Initiative (ADNI), including cognitive assessments, clinical variables, and MRI-derived phenotypes, the framework predicts cognitive status and diagnostic categories while quantifying predictive uncertainty and enabling patient-specific what-if trajectory analysis. Evaluation on leak-free subject-level splits demonstrates strong performance in score forecasting and diagnosis classification. In this sparse and irregular ADNI setting, transition-based modelling of adjacent visits achieved higher predictive accuracy than the sequence-based branch, suggesting that local transition modelling may be more data-efficient. While sequence models remain valuable for uncertainty-aware trajectory forecasting, local transition modelling offers a more data-efficient and robust predictive strategy. These findings highlight the importance of aligning temporal modelling strategies with clinical data structure and suggest that transition-based digital twin formulations may provide a practical and interpretable approach for personalised disease forecasting in neurodegenerative disorders.
匹配关键词: preference learning
---

[ACADEMIC - ARXIV]
标题: Algorithm for Contextual Queueing Bandits with Rate-Optimal Queue Length Regret
作者: Seoungbin Bae, Dabeen Lee
链接: https://arxiv.org/abs/2606.09668v1
完整摘要: Contextual queueing bandits provide a framework for learning to schedule heterogeneous jobs under unknown context-dependent service rates. Under stochastic contexts, existing algorithms achieve $\widetilde{\mathcal{O}}(T^{-1/4})$ queue length regret, defined as the expected difference between the learner's and oracle's queue lengths at horizon $T$. In this paper, we improve this rate to $\widetilde{\mathcal{O}}(T^{-1/2})$. The key observation is that random exploration is needed only up to a carefully chosen cutoff round, rather than throughout the entire horizon. We propose CQB-$η$-2, a three-phase algorithm: (i) pure random exploration to construct an initial estimator, (ii) $η$-random exploration combined with a UCB rule to continue learning while maintaining negative drift, and (iii) pure UCB after the exploration cutoff. Our proof decomposes the queue length regret at the cutoff round. Before the cutoff, negative drift suppresses queue length differences caused by suboptimal choices. After the cutoff, the first two phases provide sufficient random exploration samples, ensuring that UCB decisions incur small departure-rate gaps. Combining these two bounds yields queue length regret of order $\widetilde{\mathcal{O}}(T^{-1/2})$. We further prove a minimax lower bound of order $Ω(T^{-1/2})$. The proof constructs two hard instances that are statistically indistinguishable up to the final service decision, and uses a queue-specific coupling argument to convert the resulting testing error into queue length regret. Together, our upper and lower bounds characterize the minimax dependence on the horizon $T$ up to logarithmic factors.
匹配关键词: preference learning
---

[ACADEMIC - ARXIV]
标题: In-Context Learning for Latent Space Bayesian Optimization
作者: Tuan A. Vu, Harri Lähdesmäki, Julien Martinelli
链接: https://arxiv.org/abs/2606.09664v1
完整摘要: Bayesian optimization (BO) is a central tool for sample-efficient design, and latent-space Bayesian optimization (LSBO) extends it to structured objects such as molecules and proteins. In parallel, tabular foundation models such as TabPFN and TabICL now achieve state-of-the-art regression performance and are increasingly used as BO surrogates. Because their Bayesian behavior is induced by large synthetic pretraining collections, the composition of this pretraining distribution is crucial. LSBO creates a distinctive mismatch: the induced map from latent code to objective value differs markedly from the regression tasks used to train current in-context models. We address this mismatch by complementing the pretraining stage of tabular foundation model surrogates with synthetic optimization tasks defined on the latent space of a molecular VAE. The continued-pretraining objective features a regularizer that anchors the model to the original checkpoint, preserving its broad regression prior while avoiding overspecialization to the adaptation tasks. On held-out molecular optimization benchmarks, the resulting model achieves strong performance, supporting the relevance of LSBO-specific adaptation for in-context surrogates.
匹配关键词: preference learning
---

[ACADEMIC - ARXIV]
标题: SoccerNet 2026 Player-Centric Ball-Action Spotting:Retraining and Post-Processing Extensions to the FOOTPASS Baselines
作者: Parthsarthi Rawat
链接: https://arxiv.org/abs/2606.09679v1
完整摘要: We describe our system for the SoccerNet 2026 Player-Centric Ball-Action Spotting Challenge, which requires predicting who performs which action and when, across eight classes in broadcast soccer. Building on the three FOOTPASS baselines [1] (TAAD, TAAD+GNN, and TAAD+DST), we contribute four extensions: (1) gradient check pointing to enable full-backbone fine-tuning on a single GPU; (2) fusion of GNN logits into the DST encoder, combining graph-based tactical context with per-player visual features; (3) square-root frequency class weighting to address the 213:1 pass-to-tackle imbalance in the training data; and (4) a post processing pipeline comprising per-class logit gating, temporal frame refinement, jersey re-assignment, and a two-model ensemble. Our system achieves 0.548 Macro F1 on the test set and 0.446 on the challenge set (server evaluation).
匹配关键词: reward model
---

[ACADEMIC - ARXIV]
标题: MeCo: One-Step MeanFlow-based Corrector for Multi-Channel Speech Separation
作者: Dohwan Kim, Jung-Woo Choi
链接: https://arxiv.org/abs/2606.09677v1
完整摘要: While discriminative models for multi-channel speech separation excel in reference-based metrics, they often exhibit suboptimal human listening quality. To address this, we propose a novel MeanFlow-based one-step generative corrector (MeCo). MeCo learns a conditional average velocity field to map discriminative estimates directly onto the clean speech manifold in a single step. To maximize one-step generation performance, we introduce Data-Space Optimization (DSO). DSO integrates an $\mathbf{x}_r$-loss, which penalizes prediction errors on longer displacement intervals to serve as a generative objective for human listening quality, with an Endpoint SI-SDR loss that directly optimizes terminal signal fidelity. Experiments demonstrate that MeCo achieves state-of-the-art (SOTA) performance with minimal computational overhead, simultaneously achieving superior signal fidelity and human listening quality in both in-domain and out-of-domain scenarios.
匹配关键词: reward model
---

[ACADEMIC - ARXIV]
标题: Correlation Is Not Enough: Embedding Human Metadata for Individual Causal Discovery
作者: Suraj Biswas, Saurabh Gupta, Pritam Mukherjee
链接: https://arxiv.org/abs/2606.09672v1
完整摘要: Ask a pretrained biomedical language model whether "cortisol 28 ug/dL" and "stock-market volatility" are related, and it returns a cosine similarity of 0.83 on a scale where 1.0 means identical. The two share no mechanism. This is not a corner case: every off-the-shelf biomedical encoder we tested (BioBERT, PubMedBERT, BioM-ELECTRA) scores unrelated cross-domain pairs between 0.76 and 0.92 when the answer should be near zero. Accuracy on cross-domain discrimination is 0%. Retrieval systems survive this, because a language model downstream filters the noise. A Large Behavioural Model (LBM), a foundation model whose subject is a person rather than a sentence, does not: it reasons over a graph of a user's life and treats embedding proximity as evidence that two events are causally linked. False proximity writes a false causal edge, and everything downstream inherits the error. Here, embedding geometry is not a tuning knob; it is correctness. We report the fix. A contrastive pass over 72,034 pairs raises PubMedBERT BIOSSES correlation from 0.633 to 0.828 and within-vs-across-domain separation from 1.05x to 1.63x. A second pass, BODHI, mines hard negatives from edges absent in a biomedical knowledge graph and lifts separation to 2.30x and the discrimination gap to +0.392, at a 4.5% BIOSSES cost. On an Intel Xeon 6737P with AMX, OpenVINO cuts single-query latency from 1367 ms to 10 ms (133x) and reaches 555 sentences/sec. One finding contradicts standard advice: FP16 beats INT8 on this silicon at every serving batch size, and we explain why. The same model on a no-AMX Ice Lake instance runs 13-27x slower. We release the benchmark suite, training corpora, the BODHI generator, and the OpenVINO scripts.
匹配关键词: reward model
---

[ACADEMIC - ARXIV]
标题: Transition-Based Digital Twin Modelling for Alzheimer's Disease under Sparse Longitudinal Data
作者: Yinyu Huang, Yilin Zhang, Sofia Michopoulou, Christopher Kipps, Rahman Attar
链接: https://arxiv.org/abs/2606.09671v1
完整摘要: Alzheimer's disease (AD) progression is highly heterogeneous and is typically observed through sparse and irregular longitudinal data, posing challenges for prediction and personalised monitoring. Existing machine learning approaches have improved AD prediction using multimodal data, yet often focus on static classification or cohort-level risk estimation, providing limited support for subject-specific modelling and uncertainty-aware reasoning. To address these limitations, we present a personalised digital twin framework for AD prediction and scenario-based analysis using multimodal longitudinal data. The proposed approach integrates complementary modelling strategies to capture clinical transitions and temporal dependencies across visits. Using data from the Alzheimer's Disease Neuroimaging Initiative (ADNI), including cognitive assessments, clinical variables, and MRI-derived phenotypes, the framework predicts cognitive status and diagnostic categories while quantifying predictive uncertainty and enabling patient-specific what-if trajectory analysis. Evaluation on leak-free subject-level splits demonstrates strong performance in score forecasting and diagnosis classification. In this sparse and irregular ADNI setting, transition-based modelling of adjacent visits achieved higher predictive accuracy than the sequence-based branch, suggesting that local transition modelling may be more data-efficient. While sequence models remain valuable for uncertainty-aware trajectory forecasting, local transition modelling offers a more data-efficient and robust predictive strategy. These findings highlight the importance of aligning temporal modelling strategies with clinical data structure and suggest that transition-based digital twin formulations may provide a practical and interpretable approach for personalised disease forecasting in neurodegenerative disorders.
匹配关键词: reward model
---

[ACADEMIC - ARXIV]
标题: Visual Prompting Meets Feature Reconstruction-Based Anomaly Detection with Dual-Teacher Supervision
作者: Mateo Diaz-Bone, Daniel Caraballo, Florian Scheidegger, Thomas Frick, Mattia Rigotti, Andrea Bartezzaghi, Roy Assaf, Niccolo Avogaro, Yagmur G. Cinar, Brown Ebouky, Filip M. Janicki, Piotr S. Kluska, Cezary Skura, Cristiano Malossi
链接: https://arxiv.org/abs/2606.09670v1
完整摘要: Recent Anomaly Detection methods achieve perfect detection and segmentation scores on well-established datasets, such as MVTec. However, many of these methods face challenges when foundational assumptions - such as consistent object scale, viewpoint, background, illumination, and centered placement - are violated. Those variations that occur render anomaly detection methods unusable in many real-world scenarios. To address these limitations, we introduce three key contributions: (1) a visual prompting pipeline that isolates objects using foreground-background masking; (2) a mechanism for unfreezing the teacher in student-teacher models to improve domain adaptability; and (3) a data augmentation strategy leveraging diffusion-generated synthetic images to enhance anomaly detection performance. We achieve a 3.5 percentage point improvement over the previous state-of-the-art on the challenging AeBAD dataset by using the Masked Multiscale Reconstruction (MMR) model as our backbone.
匹配关键词: reward model
---

[ACADEMIC - ARXIV]
标题: Transition-Based Digital Twin Modelling for Alzheimer's Disease under Sparse Longitudinal Data
作者: Yinyu Huang, Yilin Zhang, Sofia Michopoulou, Christopher Kipps, Rahman Attar
链接: https://arxiv.org/abs/2606.09671v1
完整摘要: Alzheimer's disease (AD) progression is highly heterogeneous and is typically observed through sparse and irregular longitudinal data, posing challenges for prediction and personalised monitoring. Existing machine learning approaches have improved AD prediction using multimodal data, yet often focus on static classification or cohort-level risk estimation, providing limited support for subject-specific modelling and uncertainty-aware reasoning. To address these limitations, we present a personalised digital twin framework for AD prediction and scenario-based analysis using multimodal longitudinal data. The proposed approach integrates complementary modelling strategies to capture clinical transitions and temporal dependencies across visits. Using data from the Alzheimer's Disease Neuroimaging Initiative (ADNI), including cognitive assessments, clinical variables, and MRI-derived phenotypes, the framework predicts cognitive status and diagnostic categories while quantifying predictive uncertainty and enabling patient-specific what-if trajectory analysis. Evaluation on leak-free subject-level splits demonstrates strong performance in score forecasting and diagnosis classification. In this sparse and irregular ADNI setting, transition-based modelling of adjacent visits achieved higher predictive accuracy than the sequence-based branch, suggesting that local transition modelling may be more data-efficient. While sequence models remain valuable for uncertainty-aware trajectory forecasting, local transition modelling offers a more data-efficient and robust predictive strategy. These findings highlight the importance of aligning temporal modelling strategies with clinical data structure and suggest that transition-based digital twin formulations may provide a practical and interpretable approach for personalised disease forecasting in neurodegenerative disorders.
匹配关键词: constitutional AI
---

[ACADEMIC - ARXIV]
标题: From 0-to-1 to 1-to-N: Reproducible Engineering Evidence for MetaAI Recursive Self-Design
作者: Dun Li, Jiatao Li, Hongzhi Li
链接: https://arxiv.org/abs/2606.09663v1
完整摘要: Recursive self-design refers to AI-assisted modification of the mechanisms by which an AI system is built, evaluated, and improved. This paper treats MetaAI not as a mature paradigm, but as a working term for a human-seeded, AI-expanded development pattern in which the design space itself becomes a target of modification. We propose an operational evidence framework with four criteria: inspectable target system, meta-level modifier, feedback-directed selection, and recursive continuation. We then map public systems, including Darwin Goedel Machine (DGM), STOP, Goedel Agent, and ShinkaEvolve, against these criteria. DGM provides the most direct currently reported evidence: its published results show improvement from 20% to 50% on SWE-bench Verified and from 14.2% to 30.7% on full Polyglot after 80 iterations, with ablations suggesting that both open-ended exploration and self-improvement contribute. Finally, we provide MetaAI-Mini, a reproducible HumanEval-based protocol and codebase. Because no completed model run is included in this build, MetaAI-Mini is reported as a protocol rather than as an experimental result.
匹配关键词: constitutional AI
---

[ACADEMIC - ARXIV]
标题: Beyond Accuracy: Community Perspectives on Machine Translation
作者: Yujun Wang, Ehud Reiter, Shimei Pan, Steffen Eger, Wei Zhao
链接: https://arxiv.org/abs/2606.09655v1
完整摘要: Despite remarkable progress in machine translation (MT), non-AI communities have raised growing concerns about MT systems, suggesting a noticeable gap between technical advancement and the needs of real-world users. For instance, while NLP researchers focus on benchmark performance, end users care about ethical concerns, trust, reliability, costs, and more. We argue that listening to various user communities is essential so that research efforts would be directed towards the problems that the communities care about. To this end, we present a large-scale analysis, for the first time, that investigates what four stakeholder communities (AI developers, professional translators, language learners, and language service providers) post about MT technology on social media. To do so, we construct a dataset of 79,286 posts and comments from Reddit, Facebook, Bluesky, and Mastodon from 2019 to 2025, and analyse where these communities disagree, and how and why. Overall, we find that communities often disagree, and even show strong conflicts due to polarised sentiments on topics such as translation quality, efficiency, and reliability. This is because these communities approach these topics differently: the AI community frames them as technical and computational problems, while non-AI (user) communities care more about quality nuances, time savings, user trust, and broader social issues.
匹配关键词: constitutional AI
---

[ACADEMIC - ARXIV]
标题: Data-driven discovery of governing differential equations across physical systems
作者: Siyu Lou, Hao Xu, Wenguan Wang, Lu Lu, Hao Sun, Yang Liu, Linfeng Zhang, Dongxiao Zhang, Yuntian Chen
链接: https://arxiv.org/abs/2606.09638v1
完整摘要: Differential equations play a critical role in scientific discovery because they provide a mathematical framework to describe the behaviour of physical phenomena. As a promising alternative to traditional first principles, data-driven differential equation discovery has attracted increasing attention for its ability to infer governing laws directly from experimental or simulated data, especially when the underlying physics is unclear. However, the field has expanded rapidly along diverse methodological directions, particularly with the emergence of AI-based approaches, and still lacks a clear organizing perspective. In this Review, we propose a problem-oriented perspective on data-driven differential equation discovery. We first introduce a two-dimensional phase diagram of equation discoverability, where discovery problems are organized according to structural complexity and coefficient complexity. This phase diagram shows how the field has moved from the discovery of sparse equations with simple coefficients toward more complex governing laws with richer structures and more flexible parameterizations. It also clarifies why different methodological families succeed or fail in different problem settings. We then present the representation-evaluation-optimization (REO) framework as a fundamental abstraction of the discovery process. By identifying the core problems of equation discovery that persist across algorithmic variations, REO shifts the discussion from individual algorithms to the fundamental principles that determine discoverability. We connect these perspectives to applications across physics and adjacent sciences, and argue that the next challenge is not merely recovering equations, but using them to revise existing theories, distil mechanisms and form new scientific concepts.
匹配关键词: constitutional AI
---

[ACADEMIC - ARXIV]
标题: Civil Court Simulation with Large Language Models
作者: Yifan Chen, Haitao Li, Kaiyuan Zhang, Yueyue Wu, Qingyao Ai, Yiqun Liu
链接: https://arxiv.org/abs/2606.09632v1
完整摘要: Court simulation bridges legal education and judicial practice, yet human-based simulations are costly and difficult to scale. Large language models (LLMs) offer a scalable alternative, but existing court-simulation research mainly focuses on criminal cases. Civil litigation is more common in practice and harder to simulate because its claims, liability, and remedies are more flexible. We present a multi-agent court simulation framework for Chinese civil cases. The framework organizes role-based interaction through a five-stage civil trial procedure and integrates memory module and statute retrieval to support long-process adjudication. Experiments show that the framework produces reliable civil judgments, with clear strengths in liability allocation and multi-item adjudication. Further experiments show that memory quality substantially affects downstream simulation quality. Through a five-layer factor framework, we analyze how legal grounding, information conditions, judicial capability and role orientation, organizational pressure, and social context affect the framework's reliability and behavior. These results support the effectiveness of the proposed framework for civil court simulation. The dataset and code are available at: https://github.com/foggpoy/Civil-Court.
匹配关键词: constitutional AI
---

[ACADEMIC - ARXIV]
标题: SIFT: Selective-Index For Fast Compute of RAG Prefill by Exploiting Attention Invariance
作者: Rya Sanovar, Srikant Bharadwaj, Hritvik Taneja, Moinuddin Qureshi
链接: https://arxiv.org/abs/2606.09441v1
完整摘要: Retrieval-Augmented Generation (RAG) injects LLM queries with relevant documents to improve response quality. This injection increases prompt length and slows time to first token (TTFT). Unlike standard queries, RAG queries have a unique property of context reuse where the same documents recur across user queries. Thus, fully recomputing documents for every RAG query does redundant compute and increases TTFT. Prior works precompute KV tensors of RAG documents offline and coarsely recompute some tokens during online prefill. However, such KV reuse is often slower than full recomputation on modern GPUs due to high-latency disk transfers. Further, such a coarse-grained recomputation degrades accuracy. To address these limitations, this paper proposes SIFT: Selective-Index For Fast Compute of RAG Prefill by Exploiting Attention Invariance. SIFT processes documents offline and extracts fine-grained locations of high attention scores for each document. Next, we identify the following attention invariance insights that enable us to exploit the extracted locations during runtime: (1) Local-Attention Invariance: The location of high attention scores within a document remain invariant to surrounding documents. This helps us predict the location of high scores where the document attends to itself. (2) Cross-Attention Consistency: Keys with high intra-document attention also attract cross-attention from subsequent documents. This helps us predict the location of high scores where the document attends to future documents. Critically, SIFT stores no KV data and only stores locations of high scores in the form of two compact bit vectors. SIFT's storage is up to 24,000x smaller than KV tensors, obviating costly disk transfers. During prefill, SIFT computes the attention only for the marked locations and improves TTFT by 1.71x while holding accuracy within 1% of full recompute.
匹配关键词: RAG
---

[ACADEMIC - ARXIV]
标题: Anything2Skill: Compiling External Knowledge into Reusable Skills for Agents
作者: Qianjun Pan, Yutao Yang, Junsong Li, Jie Zhou, Kai Chen, Xin Li, Qin Chen, Liang He
链接: https://arxiv.org/abs/2606.09316v1
完整摘要: Retrieval-augmented generation (RAG) enables agents to access external knowledge at inference time, but it primarily retrieves fragmented declarative evidence, leaving agents to repeatedly infer task procedures from passages, manuals, examples, logs, or trajectories. This raises a fundamental question: can skills extracted from external knowledge bases be installed into an agent, enabling it to rapidly approximate domain expertise? In this paper, we propose Anything2Skill, a taxonomy-guided framework that compiles heterogeneous external knowledge into reusable, retrievable, and executable skills for agents. Given a corpus of knowledge records, \textsc{Anything2Skill} first decomposes each record into evidence windows and performs plan-and-expand skill extraction under a skill-tree prior. The extracted candidates are then converted into structured skill contracts that specify invocation conditions, contraindications, action moves, workflow steps, constraints, output specifications, supporting evidence, and confidence scores. To construct a deployable procedural memory, Anything2Skill manages the extracted skills in a persistent SkillBank through taxonomy-aware compilation, registry-level reconciliation, lifecycle tracking, versioned updates, and visible skill-tree projection. At inference time, agents retrieve both task-specific passages from the original knowledge base and relevant procedural skills from the SkillBank, allowing RAG to provide declarative evidence while compiled skills provide reusable procedural guidance. Experiments on qsv and GitHub-CLI show that Anything2Skill combined with RAG achieves 98.85\% and 94.10\% success rates, respectively, substantially outperforming RAG-only agents. These results suggest that compiling latent procedural knowledge into explicit skills is an effective way to extend retrieval-augmented agents from knowledge access toward capability reuse.
匹配关键词: RAG
---

[ACADEMIC - ARXIV]
标题: The Injection Paradox: Brand-Level Suppression in Safety-Trained LLM Recommendations via RAG Context Injection
作者: Hyunseok Paeng
链接: https://arxiv.org/abs/2606.09204v1
完整摘要: We present a reproducible failure mode of safety training in RAG-based LLM recommendation -- the Injection Paradox -- in which prompt injections embedded in retrieved documents backfire against the attacker, suppressing the target brand below the injection-free baseline. In safety-trained Claude models, documents containing prompt injections suffer a sharp drop in recommendation rate, and this suppression propagates beyond the injected document to unmodified documents of the same brand. In Claude Opus 4.6, the target brand drops from a 54% baseline to zero top-2 recommendations across all 50 trials, even though only 1 of 4 brand documents in the corpus contains an injection. The directional pattern is reproduced in counterfactual experiments and across three brands. A contrasting result across the GPT models tested, where the same injection instead increases recommendations, suggests model-family differences in how injection-like context affects recommendation behavior. These findings raise the technical possibility of a reverse-attack scenario in which an adversary embeds injections in a competitor's documents to suppress the competitor's brand via safety-sensitive model behavior.
匹配关键词: RAG
---

[ACADEMIC - ARXIV]
标题: Crop Recommendation and Agricultural Query Answering System Using Spatio-Temporal Graph Neural Networks and Hybrid Retrieval Augmentation
作者: Prajwal Thapa, Yagya Raj Pandeya
链接: https://arxiv.org/abs/2606.09160v1
完整摘要: This paper presents a unified system designed to support precision agriculture by integrating advanced weather prediction, crop recommendation, and a question-answering tool for farmers. We propose two deep learning models -- a Transformer-based Graph Neural Network and a Spatio-Temporal Graph Convolutional Network (STGCN) -- to forecast weather conditions for the next 30 days using data from 1,359 locations in Nepal. The STGCN outperforms the Transformer-based model in accuracy (MSE ~0.011 vs. 0.013), effectively modeling both spatial and temporal dependencies in climate data. These predictions are combined with static soil properties such as pH, moisture, and organic content to generate localized crop recommendations through a scoring algorithm that matches each crop's optimal growing conditions. Additionally, we develop a Retrieval-Augmented Generation (RAG) chatbot that leverages domain-specific agricultural documents to answer farmers' questions in natural language. The entire system is deployed via a mobile application, offering real-time suggestions and conversational support. User feedback confirms the system's usability and relevance, especially in rural settings where personalized farming guidance is limited. Overall, our approach demonstrates how combining machine learning models with local agricultural data can empower farmers with actionable insights, promoting more informed decisions, better crop yields, and increased resilience to climate variability.
匹配关键词: RAG
---

[ACADEMIC - ARXIV]
标题: A Multi-Agent System for IPMSM Design Optimization via an FEA-AI Hybrid Approach
作者: Jinseong Han, Sunwoong Yang, Namwoo Kang
链接: https://arxiv.org/abs/2606.09037v1
完整摘要: Interior permanent magnet synchronous motor (IPMSM) design requires balancing conflicting objectives and multi-physics constraints, while modern optimization workflows face three bottlenecks: manual problem setup, high finite element analysis (FEA) cost, and unreliable surrogate-based search in sparse or out-of-distribution regions. To address these limitations, we propose an end-to-end automated IPMSM design optimization framework that integrates retrieval-augmented generation (RAG) for structured problem definition with an uncertainty-aware FEA-AI hybrid optimization pipeline. A Design agent, connected to a motor textbook through RAG, provides domain-knowledge-based options and engineering tips, and compiles an optimization card and a design-of-experiments plan for AI-model training. A Training agent automates electromagnetic FEA, records geometry-validation and solver-failure logs, analyzes failed geometries using ANOVA-based data analysis and LLM reasoning, and invokes a Design Sampling agent to redefine the design space and generate additional samples. An Optimization agent performs GA-based search with uncertainty-driven switching: low-uncertainty candidates are evaluated by AI-surrogate inference, whereas high-uncertainty and reliability-critical Pareto-front or top-K candidates are corrected by high-fidelity FEA and reused for iterative retraining. The framework converts manual, experience-dependent configuration into a reproducible workflow that balances computational cost and prediction reliability. Experimental results under a matched high-fidelity FEA budget show that the proposed hybrid approach achieves better objective performance while maintaining low and further reducible predictive uncertainty, outperforming FEA-only search, which is limited by early budget exhaustion, and AI-only search, which converges to a low-confidence optimum.
匹配关键词: RAG
---

[ACADEMIC - ARXIV]
标题: MeCo: One-Step MeanFlow-based Corrector for Multi-Channel Speech Separation
作者: Dohwan Kim, Jung-Woo Choi
链接: https://arxiv.org/abs/2606.09677v1
完整摘要: While discriminative models for multi-channel speech separation excel in reference-based metrics, they often exhibit suboptimal human listening quality. To address this, we propose a novel MeanFlow-based one-step generative corrector (MeCo). MeCo learns a conditional average velocity field to map discriminative estimates directly onto the clean speech manifold in a single step. To maximize one-step generation performance, we introduce Data-Space Optimization (DSO). DSO integrates an $\mathbf{x}_r$-loss, which penalizes prediction errors on longer displacement intervals to serve as a generative objective for human listening quality, with an Endpoint SI-SDR loss that directly optimizes terminal signal fidelity. Experiments demonstrate that MeCo achieves state-of-the-art (SOTA) performance with minimal computational overhead, simultaneously achieving superior signal fidelity and human listening quality in both in-domain and out-of-domain scenarios.
匹配关键词: code generation
---

[ACADEMIC - ARXIV]
标题: Correlation Is Not Enough: Embedding Human Metadata for Individual Causal Discovery
作者: Suraj Biswas, Saurabh Gupta, Pritam Mukherjee
链接: https://arxiv.org/abs/2606.09672v1
完整摘要: Ask a pretrained biomedical language model whether "cortisol 28 ug/dL" and "stock-market volatility" are related, and it returns a cosine similarity of 0.83 on a scale where 1.0 means identical. The two share no mechanism. This is not a corner case: every off-the-shelf biomedical encoder we tested (BioBERT, PubMedBERT, BioM-ELECTRA) scores unrelated cross-domain pairs between 0.76 and 0.92 when the answer should be near zero. Accuracy on cross-domain discrimination is 0%. Retrieval systems survive this, because a language model downstream filters the noise. A Large Behavioural Model (LBM), a foundation model whose subject is a person rather than a sentence, does not: it reasons over a graph of a user's life and treats embedding proximity as evidence that two events are causally linked. False proximity writes a false causal edge, and everything downstream inherits the error. Here, embedding geometry is not a tuning knob; it is correctness. We report the fix. A contrastive pass over 72,034 pairs raises PubMedBERT BIOSSES correlation from 0.633 to 0.828 and within-vs-across-domain separation from 1.05x to 1.63x. A second pass, BODHI, mines hard negatives from edges absent in a biomedical knowledge graph and lifts separation to 2.30x and the discrimination gap to +0.392, at a 4.5% BIOSSES cost. On an Intel Xeon 6737P with AMX, OpenVINO cuts single-query latency from 1367 ms to 10 ms (133x) and reaches 555 sentences/sec. One finding contradicts standard advice: FP16 beats INT8 on this silicon at every serving batch size, and we explain why. The same model on a no-AMX Ice Lake instance runs 13-27x slower. We release the benchmark suite, training corpora, the BODHI generator, and the OpenVINO scripts.
匹配关键词: code generation
---

[ACADEMIC - ARXIV]
标题: Visual Prompting Meets Feature Reconstruction-Based Anomaly Detection with Dual-Teacher Supervision
作者: Mateo Diaz-Bone, Daniel Caraballo, Florian Scheidegger, Thomas Frick, Mattia Rigotti, Andrea Bartezzaghi, Roy Assaf, Niccolo Avogaro, Yagmur G. Cinar, Brown Ebouky, Filip M. Janicki, Piotr S. Kluska, Cezary Skura, Cristiano Malossi
链接: https://arxiv.org/abs/2606.09670v1
完整摘要: Recent Anomaly Detection methods achieve perfect detection and segmentation scores on well-established datasets, such as MVTec. However, many of these methods face challenges when foundational assumptions - such as consistent object scale, viewpoint, background, illumination, and centered placement - are violated. Those variations that occur render anomaly detection methods unusable in many real-world scenarios. To address these limitations, we introduce three key contributions: (1) a visual prompting pipeline that isolates objects using foreground-background masking; (2) a mechanism for unfreezing the teacher in student-teacher models to improve domain adaptability; and (3) a data augmentation strategy leveraging diffusion-generated synthetic images to enhance anomaly detection performance. We achieve a 3.5 percentage point improvement over the previous state-of-the-art on the challenging AeBAD dataset by using the Masked Multiscale Reconstruction (MMR) model as our backbone.
匹配关键词: code generation
---

[ACADEMIC - ARXIV]
标题: SpatialWorld: Benchmarking Interactive Spatial Reasoning of Multimodal Agents in Real-World Tasks
作者: Hongcheng Gao, Hailong Qu, Jingyi Tang, Jiahao Wang, Zihao Huang, Hengkang Qiao, Shihong Huang, Junming Yang, Yi Li, Hongyixuan Yuan, Wenjie Li, Bohan Zeng, Wenbo Li, Bo Wang, Jianhui Liu, Olive Huang, Haoyang Huang, Wentao Zhang, Guoqing Huang, Nan Duan, Yinpeng Dong
链接: https://arxiv.org/abs/2606.09669v1
完整摘要: Spatial reasoning is a foundational capability for multimodal large language models (MLLMs) to perceive and operate within the physical world. However, existing benchmarks predominantly rely on passive evaluation (e.g., static VQA) or simulator-specific pipelines, failing to assess general interactive spatial understanding. We introduce SpatialWorld, a unified benchmark designed specifically for evaluating the interactive spatial understanding of multimodal agents in complex real-world tasks. Integrating eight heterogeneous simulation backends under a shared, simulator-agnostic protocol, SpatialWorld features 760 human-annotated tasks across diverse domains (e.g., household routines, travel, social collaboration). Agents must solve tasks under vision-only partial observability, actively gathering egocentric visual evidence and expressing decisions via a unified, text-based action interface native to MLLMs. For reliable evaluation, each task includes a human-validated initial state, a reference trajectory, and a terminal-state verifier. Evaluating 15 advanced agents reveals that robust spatial task solving remains challenging: the strongest model, GPT-5, achieves an average task success rate (TSR) of only 17.4%, while the leading open-source model, Qwen-3.5, reaches 14.1%. Further analysis exposes a clear mismatch between task success and execution efficiency, alongside substantial domain-specific performance variations. These bottlenecks in active exploration and long-horizon planning position SpatialWorld as a rigorous testbed for future spatial agents.
匹配关键词: code generation
---

[ACADEMIC - ARXIV]
标题: Cross-Modal Masking for Robust Silent Speech Synthesis Using sEMG and Lipreading
作者: Eder del Blanco, David Gimeno-Gómez, Eva Navas, Carlos-D. Martínez-Hinarejos, Inma Hernáez
链接: https://arxiv.org/abs/2606.09667v1
完整摘要: Speech restoration through silent speech interfaces (SSIs) has emerged as a promising assistive technology for individuals with impaired or absent laryngeal voice production. Among non-invasive SSI modalities, surface electromyography (sEMG) and video-based lipreading provide complementary articulatory information, yet their integration for continuous speech synthesis remains underexplored. Moreover, existing multimodal approaches rarely address robustness to modality degradation or temporary sensor failure, limiting their applicability in realistic scenarios. In this work, we propose a masked multimodal speech synthesis framework that jointly leverages sEMG and lipreading signals through modality masking during training. Under multispeaker settings, the proposed approach reduces word error rate by up to 14 absolute percentage points compared to the strongest unimodal baseline. Experimental results not only show that masking strategies are critical for these performance gains and robustness under low-bitrate conditions, but also that they generalize better than degradation-specific data augmentations in the presence of modality absence conditions. Phone-level analyses further reveal complementary contributions across modalities, with particularly strong benefits for vowels and for specific consonant groups. Overall, these findings demonstrate the effectiveness and robustness of masked multimodal integration for silent speech synthesis, although adaptation to laryngectomized speakers remains an open research challenge.
匹配关键词: code generation
---

[ACADEMIC - ARXIV]
标题: Correlation Is Not Enough: Embedding Human Metadata for Individual Causal Discovery
作者: Suraj Biswas, Saurabh Gupta, Pritam Mukherjee
链接: https://arxiv.org/abs/2606.09672v1
完整摘要: Ask a pretrained biomedical language model whether "cortisol 28 ug/dL" and "stock-market volatility" are related, and it returns a cosine similarity of 0.83 on a scale where 1.0 means identical. The two share no mechanism. This is not a corner case: every off-the-shelf biomedical encoder we tested (BioBERT, PubMedBERT, BioM-ELECTRA) scores unrelated cross-domain pairs between 0.76 and 0.92 when the answer should be near zero. Accuracy on cross-domain discrimination is 0%. Retrieval systems survive this, because a language model downstream filters the noise. A Large Behavioural Model (LBM), a foundation model whose subject is a person rather than a sentence, does not: it reasons over a graph of a user's life and treats embedding proximity as evidence that two events are causally linked. False proximity writes a false causal edge, and everything downstream inherits the error. Here, embedding geometry is not a tuning knob; it is correctness. We report the fix. A contrastive pass over 72,034 pairs raises PubMedBERT BIOSSES correlation from 0.633 to 0.828 and within-vs-across-domain separation from 1.05x to 1.63x. A second pass, BODHI, mines hard negatives from edges absent in a biomedical knowledge graph and lifts separation to 2.30x and the discrimination gap to +0.392, at a 4.5% BIOSSES cost. On an Intel Xeon 6737P with AMX, OpenVINO cuts single-query latency from 1367 ms to 10 ms (133x) and reaches 555 sentences/sec. One finding contradicts standard advice: FP16 beats INT8 on this silicon at every serving batch size, and we explain why. The same model on a no-AMX Ice Lake instance runs 13-27x slower. We release the benchmark suite, training corpora, the BODHI generator, and the OpenVINO scripts.
匹配关键词: benchmark
---

[ACADEMIC - ARXIV]
标题: SpatialWorld: Benchmarking Interactive Spatial Reasoning of Multimodal Agents in Real-World Tasks
作者: Hongcheng Gao, Hailong Qu, Jingyi Tang, Jiahao Wang, Zihao Huang, Hengkang Qiao, Shihong Huang, Junming Yang, Yi Li, Hongyixuan Yuan, Wenjie Li, Bohan Zeng, Wenbo Li, Bo Wang, Jianhui Liu, Olive Huang, Haoyang Huang, Wentao Zhang, Guoqing Huang, Nan Duan, Yinpeng Dong
链接: https://arxiv.org/abs/2606.09669v1
完整摘要: Spatial reasoning is a foundational capability for multimodal large language models (MLLMs) to perceive and operate within the physical world. However, existing benchmarks predominantly rely on passive evaluation (e.g., static VQA) or simulator-specific pipelines, failing to assess general interactive spatial understanding. We introduce SpatialWorld, a unified benchmark designed specifically for evaluating the interactive spatial understanding of multimodal agents in complex real-world tasks. Integrating eight heterogeneous simulation backends under a shared, simulator-agnostic protocol, SpatialWorld features 760 human-annotated tasks across diverse domains (e.g., household routines, travel, social collaboration). Agents must solve tasks under vision-only partial observability, actively gathering egocentric visual evidence and expressing decisions via a unified, text-based action interface native to MLLMs. For reliable evaluation, each task includes a human-validated initial state, a reference trajectory, and a terminal-state verifier. Evaluating 15 advanced agents reveals that robust spatial task solving remains challenging: the strongest model, GPT-5, achieves an average task success rate (TSR) of only 17.4%, while the leading open-source model, Qwen-3.5, reaches 14.1%. Further analysis exposes a clear mismatch between task success and execution efficiency, alongside substantial domain-specific performance variations. These bottlenecks in active exploration and long-horizon planning position SpatialWorld as a rigorous testbed for future spatial agents.
匹配关键词: benchmark
---

[ACADEMIC - ARXIV]
标题: In-Context Learning for Latent Space Bayesian Optimization
作者: Tuan A. Vu, Harri Lähdesmäki, Julien Martinelli
链接: https://arxiv.org/abs/2606.09664v1
完整摘要: Bayesian optimization (BO) is a central tool for sample-efficient design, and latent-space Bayesian optimization (LSBO) extends it to structured objects such as molecules and proteins. In parallel, tabular foundation models such as TabPFN and TabICL now achieve state-of-the-art regression performance and are increasingly used as BO surrogates. Because their Bayesian behavior is induced by large synthetic pretraining collections, the composition of this pretraining distribution is crucial. LSBO creates a distinctive mismatch: the induced map from latent code to objective value differs markedly from the regression tasks used to train current in-context models. We address this mismatch by complementing the pretraining stage of tabular foundation model surrogates with synthetic optimization tasks defined on the latent space of a molecular VAE. The continued-pretraining objective features a regularizer that anchors the model to the original checkpoint, preserving its broad regression prior while avoiding overspecialization to the adaptation tasks. On held-out molecular optimization benchmarks, the resulting model achieves strong performance, supporting the relevance of LSBO-specific adaptation for in-context surrogates.
匹配关键词: benchmark
---

[ACADEMIC - ARXIV]
标题: Beyond Accuracy: Community Perspectives on Machine Translation
作者: Yujun Wang, Ehud Reiter, Shimei Pan, Steffen Eger, Wei Zhao
链接: https://arxiv.org/abs/2606.09655v1
完整摘要: Despite remarkable progress in machine translation (MT), non-AI communities have raised growing concerns about MT systems, suggesting a noticeable gap between technical advancement and the needs of real-world users. For instance, while NLP researchers focus on benchmark performance, end users care about ethical concerns, trust, reliability, costs, and more. We argue that listening to various user communities is essential so that research efforts would be directed towards the problems that the communities care about. To this end, we present a large-scale analysis, for the first time, that investigates what four stakeholder communities (AI developers, professional translators, language learners, and language service providers) post about MT technology on social media. To do so, we construct a dataset of 79,286 posts and comments from Reddit, Facebook, Bluesky, and Mastodon from 2019 to 2025, and analyse where these communities disagree, and how and why. Overall, we find that communities often disagree, and even show strong conflicts due to polarised sentiments on topics such as translation quality, efficiency, and reliability. This is because these communities approach these topics differently: the AI community frames them as technical and computational problems, while non-AI (user) communities care more about quality nuances, time savings, user trust, and broader social issues.
匹配关键词: benchmark
---

[ACADEMIC - ARXIV]
标题: A Unifying Framework for Concept-Based Representational Similarity
作者: Grégoire Dhimoïla, Victor Boutin, Agustin Martin Picard, Thomas Fel, Thomas Serre
链接: https://arxiv.org/abs/2606.09653v1
完整摘要: Learned representations across models and modalities often exhibit striking structural similarities, suggesting shared underlying concept decompositions. However, concept alignment remains poorly defined: existing approaches optimize different objectives under the same terminology, obscuring what is actually aligned. We propose a unifying framework that decomposes alignment along two axes: what is aligned (representations vs. concepts) and at what level (instance-wise vs. distributional). This induces four corresponding properties -- instance-wise and distributional variants of translation and concept consistency -- and reveals precisely which of these guarantees existing methods provide. We further introduce \InterVenchA, an intervention-based benchmark that separately measures extraction quality, translation quality, and concept consistency. Through theory and experiments, we show that commonly assumed equivalences between alignment objectives fail in practice: optimizing one property does not reliably recover the others, and purely unsupervised objectives fail to recover meaningful instance-level alignment. We then propose the Coupled Sparse Autoencoder (CoSAE), which jointly enforces complementary alignment objectives. Strong alignment emerges only in this regime. Surprisingly, as little as 0.1\% paired data is sufficient to recover instance-level alignment when anchoring distributional objectives. Overall, our results show that concept alignment is fundamentally multi-objective: it must be defined, measured, and optimized as such.
匹配关键词: benchmark
---

[ACADEMIC - ARXIV]
标题: Gradient-Guided Reward Optimization for Inference-time Alignment
作者: Hankun Lin, Ruqi Zhang
链接: https://arxiv.org/abs/2606.09635v1
完整摘要: Ensuring the reliability of Large Language Models (LLMs) under distribution drift requires inference-time adaptation. While inference-time alignment methods such as Best-of-$N$ and rejection sampling are widely used, they frame the task as a sampling-intensive, reward-guided search, leading to two key limitations: their performance is bounded by the base model's generation quality, and their reliance on imperfect reward models makes them vulnerable to reward hacking. To address these challenges, we introduce Gradient-Guided Reward Optimization (GGRO), a lightweight inference-time method that performs targeted, minimal intervention during decoding via gradient guidance. Specifically, GGRO monitors token-level entropy to identify high-uncertainty regions indicative of drift or misalignment. Upon detection, it responds by injecting nudging tokens, generated using gradient signals from an off-the-shelf reward model, to steer the generation trajectory rather than merely re-ranking samples. Experiments show that GGRO consistently improves inference-time alignment across safety, helpfulness, and reasoning benchmarks. It also increases coverage of high-quality responses and robustness to reward hacking, with minimal computational overhead. Code is available at https://github.com/lhk2004/GGRO.
匹配关键词: safety
---

[ACADEMIC - ARXIV]
标题: Code Is More Than Text: Uncertainty Estimation for Code Generation
作者: Yuling Shi, Caiqi Zhang, Yuexian Li, Haopeng Wang, Yeheng Chen, Nigel Collier, Xiaodong Gu
链接: https://arxiv.org/abs/2606.09577v1
完整摘要: Large language models (LLMs) are increasingly deployed as code generators, where silently wrong programs pose real safety and reliability risks. Reliable uncertainty estimation (UE) is essential for selective prediction, human-in-the-loop review, and downstream agentic decisions. Yet most existing code UE methods are inherited from natural language (NL) generation and ignore properties that make code distinct. We argue that code differs from NL in three ways: a single wrong token can break an entire program (token fragility); algorithmic intent and concrete implementation can disagree independently (intent-code gap); and programs can be executed (executability). We instantiate these properties as three orthogonal uncertainty axes: lexical (Top-K token entropy), algorithmic (pseudo-code consistency), and functional (behavioral consistency). Across five code LLMs, our three-axis ensemble improves average AUROC from 0.696 for the strongest NL-derived baseline to 0.776 (+8.1 points). Notably, on Qwen3-14B, our single-pass Top-K token entropy matches the strongest multi-pass baseline while being over 3x cheaper; across models, it remains a competitive low-cost signal. These results suggest that code UE deserves code-specific design rather than direct NL ports.
匹配关键词: safety
---

[ACADEMIC - ARXIV]
标题: Safe-RULE: Safe Reinforcement UnLEarning
作者: Shixiong Jiang, Taozheng Zhu, Fanxin Kong
链接: https://arxiv.org/abs/2606.09559v1
完整摘要: Offline safe reinforcement learning (Safe RL) enables policy learning without online interactions, making it suitable for safety-critical systems such as robotics systems. However, its reliance on static datasets exposes offline Safe RL to data poisoning attacks, where adversaries inject malicious samples that compromise safety and induce unsafe policy behavior. In this work, we propose a new learning paradigm, named safe reinforcement unlearning (Safe-RULE), used as a defense framework to remove the influence of poisoned data without retraining from scratch or requiring access to the original training environment. We further extend reinforcement unlearning to offline Safe RL by explicitly accounting for both task performance and safety constraints during the unlearning process. Experiments across benchmark Safe RL tasks demonstrate that our approach effectively enhances safety performance against data poisoning attacks.
匹配关键词: safety
---

[ACADEMIC - ARXIV]
标题: A VideoMAE-v2 Approach to Zero-Shot Traffic Accident Anticipation
作者: Siyuan Li, Xiaoyang Bi, Mengshi Qi
链接: https://arxiv.org/abs/2606.09542v1
完整摘要: Traffic accident anticipation -- predicting the likelihood of an imminent collision at every frame of a dashcam video -- is safety-critical yet difficult to scale, because collecting in-domain annotated accident footage for every deployment scenario is prohibitively expensive. We study this task under a zero-shot setting where no target-domain training data is available: the model must learn exclusively from a publicly available binary-labelled driving-accident dataset and generalise to unseen dashcam footage. We propose a framework that bridges the gap between the frame-level temporal risk estimation task and coarsely labelled binary accident datasets by coupling a VideoMAE-v2 backbone with a per-frame prediction head under a sliding-window protocol. Our method achieves 2nd place in the 2026 CVPR@AUTOPILOT Zero-Shot Accident Anticipation competition. Code is available at https://github.com/TimeSouth/zero-shot-taa-solution.
匹配关键词: safety
---

[ACADEMIC - ARXIV]
标题: Emergent alignment and the projectability of ethical personas
作者: Guillermo Del Pinal, Youngchan Lee, Cameron McNamara, Alejandro Perez Carballo
链接: https://arxiv.org/abs/2606.09475v1
完整摘要: Work on `emergent misalignment' shows that finetuning LLMs on narrow tasks can induce broadly misaligned behavior. This supports the `persona selection' (PSM) hypothesis: during pre-training, LLMs learn to simulate different characters and perspectives, which can be elicited and refined during post-training. This paper investigates the converse phenomenon, `emergent alignment', and uses it to support and refine the PSM and motivate a novel desideratum for alignment. We finetune a helpful-only model on broad and narrow safety tasks. To create SFT samples, we follow the `Constitutional AI' (CAI) approach and use four constitutions which encode reasonable alignment strategies: deontology, consequentialism, virtue ethics, and aligning AIs as subordinate to human authority. For each of those models, we show that finetuning on two narrow safety sub-categories reliably induces emergent alignment over a representative set of general safety categories, and on safety subcategories that we directly filtered-out of the data sets used for narrow alignment. To test the `PSM' using a more fine-grained evaluation, we used a multidimensional `ethical persona' diagnostic. For each constitutionally finetuned (broad/narrow) model, we evaluate how well their behavior matches their expected signature profile. Our results show that our CAI models acquire their expected ``ethical persona'' -- e.g., the model narrowly fine-tuned on SFT samples created using the consequentialist constitution agrees significantly more with utilitarian than deontological beliefs. Yet our coarse and fine-grained evaluations show that there are significant differences across our (broad/narrow) finetuned CAI models in how well they project. We conclude that alignment strategies should be evaluated, not just on their (in-distribution) general safety performance, but also specifically on their degree of projectability.
匹配关键词: safety
---

