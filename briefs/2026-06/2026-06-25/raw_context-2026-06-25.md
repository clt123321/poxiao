# 破晓 PoXiao — 原始数据 (Raw Context)
生成时间: 2026-06-25 04:10 UTC
================================================================================

[RSS:Reddit LocalLLaMA (社区共识)]
The Swiss Federal Supreme Court is evaluating Heretic
https://www.reddit.com/r/LocalLLaMA/comments/1ueeund/the_swiss_federal_supreme_court_is_evaluating/
“Oh no, are they banning abliterated models now?!?” If that was your first thought when you read the title I can’t blame you. But that’s actually not what’s happening in this case. Instead, the Swiss Federal Supreme Court is evaluating Heretic for their own use! As it turns out, the Court has been s
---

[RSS:Reddit LocalLLaMA (社区共识)]
Gemma4-26B-A4B & 31B-QAT Uncensored Balanced are out with MTP (35% & 53% speed boost)!
https://www.reddit.com/r/LocalLLaMA/comments/1ueuki7/gemma426ba4b_31bqat_uncensored_balanced_are_out/
First of all, I'm stoked to announce we are almost at 20 million downloads on HF! (counted only on my own account, no duplicates/quants/finetunes/etc) and almost 5000 members on Discord! Two releases this time, as promised, the bigger Gemma 4 QATs, both Balanced, both with MTP : https://huggingface.
---

[RSS:Reddit LocalLLaMA (社区共识)]
Gefen is a drop-in replacement for the AdamW optimizer, claims 8x memory reduction in training (GitHub available)
https://www.reddit.com/r/LocalLLaMA/comments/1uep96s/gefen_is_a_dropin_replacement_for_the_adamw/
Paper: https://arxiv.org/abs/2606.13894 GitHub: https://github.com/ndvbd/Gefen &#32; submitted by &#32; /u/indicava [link] &#32; [comments]
---

[RSS:Reddit LocalLLaMA (社区共识)]
Unlimited-OCR is now on ModelScope! A 3.3B multilingual OCR model for one-shot parsing across single images, multi-page documents, and PDFs. License: MIT
https://www.reddit.com/r/LocalLLaMA/comments/1ue51uk/unlimitedocr_is_now_on_modelscope_a_33b/
Full-document parsing instead of cropped-region OCR 32K output length for long OCR sequences Base and gundam image modes for different document layouts Transformers inference + SGLang serving with OpenAI-compatible streaming requests Built to push DeepSeek-OCR-style document parsing further. source:
---

[RSS:Reddit LocalLLaMA (社区共识)]
For users with 4x-8x 6000 PROs, how is your experience with bigger models lately? (GLM 5.2, Kimi 2.7, DeepSeek V4 Pro)
https://www.reddit.com/r/LocalLLaMA/comments/1uex6pb/for_users_with_4x8x_6000_pros_how_is_your/
Hello guys, hoping you're doing fine! I was wondering, for users with 4x-8x 6000 PROs (so between 384 and 768GB VRAM), how are bigger models working for you? I have planned to either jump to 4 or 8 from my actual system, and want to see the experiences with these lately. In theory you can run GLM 5.
---

[RSS:Reddit LocalLLaMA (社区共识)]
The Bank of Korea just released a report about AI productivity
https://www.reddit.com/r/LocalLLaMA/comments/1uecytz/the_bank_of_korea_just_released_a_report_about_ai/
I am sorry for sharing an article from a Korean website that you might not be familiar with. But South Korea is the only country currently making a lot of money from the AI boom. BigTech in the USA are paying huge amounts of money to buy semiconductor chips from Samsung and SK Hynix. Since it comes 
---

[RSS:Reddit LocalLLaMA (社区共识)]
Big News for AMD / Strix Halo+ Owners
https://www.reddit.com/r/LocalLLaMA/comments/1uegdu0/big_news_for_amd_strix_halo_owners/
Admittedly this is news for me, but I'm hoping it could be of some use to others here as well! So, THE NPU IS USABLE!! I've owned an AMD Ryzen 395 Max AI+ (or whatever the naming is lol) for about a year now and have relied solely on GGUFs and Vulkan. I acknowledge that the AMD Ryzen AI team has bee
---

[RSS:Reddit LocalLLaMA (社区共识)]
SDXL running locally in the browser on WebGPU, open-source
https://www.reddit.com/r/LocalLLaMA/comments/1uemzsb/sdxl_running_locally_in_the_browser_on_webgpu/
I needed simple local image generation without the usual setup. No virtual environments, no ComfyUI with a complex graph and installation as an exe. So i tried to push the whole thing into the browser and run it on WebGPU. It's a browser extension. You install it, then it loads model, and after that
---

[RSS:Reddit LocalLLaMA (社区共识)]
I did some model hacks, and got GLM5.2 from about 2.5 tok/s to >50 tok/s on my GH200 system.
https://www.reddit.com/r/LocalLLaMA/comments/1uedlas/i_did_some_model_hacks_and_got_glm52_from_about/
G'day. This is part 3 on my Local LLM adventures. I have a crazy system hacked server-to-desktop system : Component Spec GPUs 2x Hopper H100, 96 GB HBM3 each CPUs 2x Grace, 72 cores each Host memory 480 GB LPDDR5X per Grace, 960 GB total So I can run technically run GLM5.2. Except the naive settings
---

[RSS:Reddit LocalLLaMA (社区共识)]
OpenAI and Broadcom unveil LLM-optimized inference chip
https://www.reddit.com/r/LocalLLaMA/comments/1ueexbr/openai_and_broadcom_unveil_llmoptimized_inference/
https://openai.com/index/openai-broadcom-jalapeno-inference-chip/ Quoted from the start of the blog post: Early testing shows that the first-generation accelerator will deliver performance per watt substantially better than current state-of-the-art Built from the ground up for current and future LLM
---

[RSS:Reddit LocalLLaMA (社区共识)]
Got GLM-5.2 + MTP speculative decode running on 4× DGX Spark (GB10) — and the build piece the public recipe is missing
https://www.reddit.com/r/LocalLLaMA/comments/1ueqfzl/got_glm52_mtp_speculative_decode_running_on_4_dgx/
TL;DR: the recipe's image-build mods aren't actually public – I reconstructed them from the public kernels (with Claude) – and you have to build vLLM at the author's exact pinned ref or the real AWQ weights crash on load. Running now at ~9.4 tok/s on my own 4× GB10. Saw a link on X to CosmicRaisins'
---

[RSS:Reddit LocalLLaMA (社区共识)]
Any chance I could cluster my DGX Spark (128GB unified memory) and my AMD Ryzen AI Max 395 (128GM unified memory) together to run 1 model?
https://www.reddit.com/r/LocalLLaMA/comments/1uerbyi/any_chance_i_could_cluster_my_dgx_spark_128gb/
Hey all, So I have a Nvidia DGX Spark and an AMD Strix 395, both have 128GB of unified memory. The Spark has 200Gbit network and the AMD Strix has 5Gbit ethernet (but it has a pcie gen 4x4 slot). Is there any chance I can cluster the 2 together to run a larger model that can fit in the ~256GB (minus
---

[RSS:Reddit LocalLLaMA (社区共识)]
Qwen-AgentWorld-35B-A3B: a 3B-active MoE trained to simulate MCP, terminal, SWE, Android, web and OS environments
https://www.reddit.com/r/LocalLLaMA/comments/1ue5149/qwenagentworld35ba3b_a_3bactive_moe_trained_to/
Qwen just released Qwen-AgentWorld-35B-A3B — a 35B-parameter MoE with only ~3B active parameters per token. The interesting part: this is not positioned as a standard chat/instruction model or a full autonomous agent. It is a language world model trained to predict what an environment would return a
---

[RSS:Reddit LocalLLaMA (社区共识)]
Anybody used DwarfStar with DeepSeek V4 Flash on 1x DGX Spark yet? What are your thoughts?
https://www.reddit.com/r/LocalLLaMA/comments/1ueuc33/anybody_used_dwarfstar_with_deepseek_v4_flash_on/
Hey fellow localites, Has anybody used DwarfStar with DeepSeek V4 Flash on 1x DGX Spark yet? What are your thoughts? Based on what I read, with its MoE approach, and its unified memory first then bleed into SSD approach, you can apparently load DS4 Flash and it runs well, with 80B active and full ma
---

[RSS:Reddit LocalLLaMA (社区共识)]
Qwen3.6 27B more dumb in vLLM compared to llama.cpp
https://www.reddit.com/r/LocalLLaMA/comments/1ue9v4b/qwen36_27b_more_dumb_in_vllm_compared_to_llamacpp/
Hello, I recently bought a new RTX 5060Ti to pair with the RTX 5060Ti I already own, now I have 32GB of VRAM. Up until now for convenience I've used llama.cpp, for goodness' sake it works excellently when only 1 user is using it, but now there are 2 of us using it and llama.cpp can't keep up, often 
---

[RSS:Reddit LocalLLaMA (社区共识)]
Do cloud chatbot's system prompts make them stupider?
https://www.reddit.com/r/LocalLLaMA/comments/1uep8o5/do_cloud_chatbots_system_prompts_make_them/
When I am talking with Chat GPT or Claude about abstract concepts, I am often surprised by how they seem kind of dumb... like they aren't benefitting from their extra parameters over top open models like Kimi or GLM. In fact they often seem stupider than these open models that I run locally in the w
---

[RSS:Reddit LocalLLaMA (社区共识)]
Seems this community might have missed it: Bill that would mandate AI chip location tracking gains industry support | Half a dozen companies have come out in support of the Chip Security Act, which would require location-tracking mechanisms for America’s most advanced computing chips.
https://www.reddit.com/r/LocalLLaMA/comments/1ue2fd7/seems_this_community_might_have_missed_it_bill/
Web / reddit search have not found this posted in this sub, even though it is several days old news. So I do post. Related links: https://www.reddit.com/r/politics/comments/1uahgcs/bill_that_would_mandate_ai_chip_location_tracking/ https://www.reddit.com/r/LocalLLM/comments/1ubz5xh/us_to_require_loc
---

[RSS:Reddit LocalLLaMA (社区共识)]
MINISFORUM DEG1 Oculink eGPU Dock Refurbished - $59
https://www.reddit.com/r/LocalLLaMA/comments/1uelxw4/minisforum_deg1_oculink_egpu_dock_refurbished_59/
I got one of these refurbished units last year. I have nothing but good things to say about it. It works great. It has heft to it to keep the GPU secure. And unlike some cheaper Oculink docks, it has redrivers for signal integrity. &#32; submitted by &#32; /u/fallingdowndizzyvr [link] &#32; [comment
---

[RSS:Reddit LocalLLaMA (社区共识)]
How Baidu's newly released Unlimited-OCR transcribes dozens of pages in one forward pass
https://www.reddit.com/r/LocalLLaMA/comments/1ueanx0/how_baidus_newly_released_unlimitedocr/
https://reddit.com/link/1ueanx0/video/gc21db02j89h1/player Baidu released Unlimited-OCR 2 days ago, and they claim it can transcribe dozens of pages in one forward pass. I read the research paper, and decided to make a post ( link if anyone's interested) Problem they are solving The problem it targe
---

[RSS:Reddit LocalLLaMA (社区共识)]
New EU model (Domyn) will be 400b.
https://www.reddit.com/r/LocalLLaMA/comments/1ue7cl5/new_eu_model_domyn_will_be_400b/
The source is in Italian, but a well respected newspaper (like Financial Times) https://www.ilsole24ore.com/art/frontier-grand-challenge-domyn-guidera-progetto-dell-ai-sovrana-AIgNTNoD?refresh_ce=1 They are a startup that has already created a closed 260b model (Domyn Large) for enterprise solutions
---

[RSS:Reddit LocalLLaMA (社区共识)]
llama.cpp's web UI now supports executing model generated JavaScript in the browser, through Web Workers (opt in)
https://www.reddit.com/r/LocalLLaMA/comments/1uebknk/llamacpps_web_ui_now_supports_executing_model/
A pull request adding a new run_javascript tool was merged into mainline a couple of weeks ago. I could not find any discussion about it here, or elsewhere for that matter. Maybe this has gone largely unnoticed (or maybe I suck at searching)? The feature does not seem to have been advertised much, a
---

[RSS:Reddit LocalLLaMA (社区共识)]
Has anyone else found vLLM outputs noticeably worse than llama.cpp for the same model?
https://www.reddit.com/r/LocalLLaMA/comments/1uejklg/has_anyone_else_found_vllm_outputs_noticeably/
I'm wondering if anyone else has come across this. I've tested the same model on llama.cpp and vLLM with similar settings and quantizations. The performance and concurrency in vLLM are much noticeably better, but sometimes the model feels less reliable. Some things I've noticed: * More mistakes with
---

[RSS:Reddit LocalLLaMA (社区共识)]
Qwen-AgentWorld-397B-A17B
https://www.reddit.com/r/LocalLLaMA/comments/1ue56em/qwenagentworld397ba17b/
It looks like a new model, mentioned on https://huggingface.co/Qwen/Qwen-AgentWorld-35B-A3B and on https://qwen.ai/blog?id=qwen-agentworld &#32; submitted by &#32; /u/Shoddy_Bed3240 [link] &#32; [comments]
---

[RSS:Reddit LocalLLaMA (社区共识)]
Qwen-AgentWorld-35B-A3B for Coding?
https://www.reddit.com/r/LocalLLaMA/comments/1uebvld/qwenagentworld35ba3b_for_coding/
Benchmark from its model card. Removed online models &amp; Qwen-AgentWorld-397B-A17B from the table. Just Open models. Model MCP Search Term. SWE Android Web OS Overall DeepSeek-V4-Pro 63.27 27.61 51.26 59.44 55.17 50.32 63.70 52.97 GLM-5.1 67.60 22.46 47.32 52.07 59.10 51.50 59.13 51.31 Kimi K2.6 6
---

[RSS:TechCrunch AI (创业融资)]
Europe is pushing back on Washington’s chip war
https://techcrunch.com/2026/06/24/europe-is-pushing-back-on-washingtons-chip-war/
As ASML CEO Christophe Fouquet told TechCrunch in May, what China can currently buy are older-generation deep ultraviolet tools — gear first shipped about a decade ago — the same machines the MATCH Act would now put off limits.
---

[RSS:TechCrunch AI (创业融资)]
Former Infosys chief has a new startup that wants to challenge the IT services world
https://techcrunch.com/2026/06/24/former-infosys-chief-has-a-new-startup-that-wants-to-challenge-the-it-services-world/
Backed by Mayfield and Aramco Ventures, Vishal Sikka’s new venture brings together veterans from SAP, Infosys, and VianAI.
---

[RSS:TechCrunch AI (创业融资)]
Cerebras stock plunges after earnings as CEO says margin outlook was misunderstood
https://techcrunch.com/2026/06/24/cerebras-stock-plunges-after-earnings-as-ceo-says-margin-outlook-was-misunderstood/
In its first earnings report since going public, the AI chipmaker forecast a narrower gross margin in its core business, scaring investors.
---

[RSS:TechCrunch AI (创业融资)]
AI was supposed to kill engineering jobs, but new data suggests they’re the most resilient
https://techcrunch.com/2026/06/24/ai-was-supposed-to-kill-engineering-jobs-but-new-data-suggests-theyre-the-most-resilient/
While AI dominates the layoff narrative, engineers are actually making up a larger share of new hires, according to SignalFire data.
---

[RSS:TechCrunch AI (创业融资)]
AI researchers continue to leave Google for its rivals
https://techcrunch.com/2026/06/24/ai-researchers-continue-to-leave-google-for-its-rivals/
Top AI researchers Jonas Adler and Alexander Pritzel are leaving Google for Anthropic, following departures from top scientists Noam Shazeer and John Jumper.
---

[RSS:TechCrunch AI (创业融资)]
The memory chip crunch is paying off for this US company
https://techcrunch.com/2026/06/24/the-memory-chip-crunch-is-paying-off-for-this-u-s-company/
Revenue quadrupled to $41.45 billion compared with the same period a year ago. The company's profit, meanwhile, rose from $1.88 billion to an incredible $28.2 billion year-over-year.
---

[RSS:TechCrunch AI (创业融资)]
Companies are scrambling to stop employees from maxing out AI budgets with small tasks
https://techcrunch.com/2026/06/24/companies-are-scrambling-to-stop-employees-from-maxing-out-ai-budgets-with-small-tasks/
The tokenmaxxing era was brief. We now appear to be entering the era of token rationing.
---

[RSS:TechCrunch AI (创业融资)]
Facebook rolls out an AI companion app for creators
https://techcrunch.com/2026/06/24/facebook-rolls-out-an-ai-companion-app-for-creators/
The new app, which is currently being tested with select creators, will have Facebook's recently launched AI creator assistant built into it.
---

[RSS:TechCrunch AI (创业融资)]
Agility Robotics plans to go public via SPAC in a $2.5B deal
https://techcrunch.com/2026/06/24/agility-robotics-plans-to-go-public-via-spac-in-a-2-5b-deal/
Agility Robotics, the humanoid robotics startup that spun out of Oregon State University in 2015, expects to generate $620 million in proceeds.
---

[RSS:TechCrunch AI (创业融资)]
Figma adds code layers, support for animations, more AI features in new update
https://techcrunch.com/2026/06/24/figma-adds-code-layers-support-for-animations-more-ai-features-in-new-update/
Figma's update adds a new code layer, support for motion and shaders, and the ability to create custom plug-ins for various tasks using AI.
---

[RSS:TechCrunch AI (创业融资)]
OpenAI unveils its first custom chip, built by Broadcom
https://techcrunch.com/2026/06/24/openai-unveils-its-first-custom-chip-built-by-broadcom/
Named Jalapeño, the new processor was designed specifically for the unique needs of OpenAI's inference systems.
---

[RSS:TechCrunch AI (创业融资)]
3 days left to save up to $190 on your TechCrunch Founder Summit 2026 pass
https://techcrunch.com/2026/06/24/3-days-left-to-save-up-to-190-on-techcrunch-founder-summit-2026/
You have just 3 days left to save up to $190 on your pass to TechCrunch Founder Summit 2026 before Early Bird rates end on June 26 at 11:59 p.m. PT. Register today.
---

[RSS:The Verge AI (科技大厂动态)]
Congresswoman denies staff used AI to write defense funding amendment
https://www.theverge.com/policy/956394/florida-anna-paulina-luna-anthropic-claude
Rep. Anna Paulina Luna (R-FL) says her staff used AI for "spellcheck" in an amendment summary for a major defense bill, but denies it was used for the bill text itself and says "NO Legislation is ever drafted with AI." Luna issued the response after accounts on X began sharing screenshots of an amen
---

[RSS:The Verge AI (科技大厂动态)]
The $27 million Al proxy war over Alex Bores ends in a draw
https://www.theverge.com/ai-artificial-intelligence/956263/alex-bores-new-york-12th-district-congressional-primary-results
The expensive, $27 million political proxy war between Anthropic and OpenAI came to a draw last night when Alex Bores, a New York state Assemblyman whose popularity surged after being targeted by a pro-AI super PAC, narrowly lost the Democratic primary to represent New York's 12th Congressional dist
---

[RSS:The Verge AI (科技大厂动态)]
Figma now has AI motion graphics and shader tools
https://www.theverge.com/tech/955831/figma-code-design-tools-config-2026-announcements
Figma has revealed some new design and coding product updates at its annual Config conference that aim to help creatives "push their ideas further" and automate tedious tasks with AI. Part of this is a reimagined canvas that's now optimized for full-stack development, according to Figma, bringing te
---

[RSS:The Verge AI (科技大厂动态)]
OpenAI reveals its first AI processor: Jalapeño
https://www.theverge.com/ai-artificial-intelligence/955939/openai-reveals-its-first-ai-processor-jalapeno
OpenAI has just revealed a new "intelligence processor" chip for AI servers made in partnership with Broadcom. The chip, called Jalape&#241;o, is designed to power current and future large language models, according to an announcement on Wednesday. Jalape&#241;o is an ASIC (Application-Specific Inte
---

[RSS:The Verge AI (科技大厂动态)]
The Google Home Speaker sounds good and looks great — but it’s finicky
https://www.theverge.com/gadgets/955537/google-home-smart-speaker-hands-on
Right out of the box, the new Google Home Speaker passed a couple of important tests. Even with the volume at 100 percent and music blaring out of the speaker, it quickly ducked the audio and listened every time I said "Hey, Google." In fact, in two days of testing, the speaker's three microphones h
---

[RSS:Ars Technica AI (深度技术)]
One-two punch delivered in global operation disrupts cybercrime "assembly line"
https://arstechnica.com/security/2026/06/one-two-punch-delivered-in-global-operation-disrupts-cybercrime-assembly-line/
"Operation Endgame" simultaneously disrupts two widely used crime tools.
---

[RSS:Reddit Jobs & Careers (职场动态)]
Wrote a book on software architecture and now cannot find a job
https://www.reddit.com/r/cscareerquestions/comments/1uejjco/wrote_a_book_on_software_architecture_and_now/
TLDR: I spent three years writing a free book which earned 800+ stars on GitHub, but it seems that HRs now treat me as a chronically unemployed person and reject or ignore my job applications. I have 15 years of experience with C / C++ (and Python for scripts), worked on a wide range of projects fro
---

[RSS:Reddit Jobs & Careers (职场动态)]
Co intern got yelled at for deleting a prod database. Is this a red flag?
https://www.reddit.com/r/cscareerquestions/comments/1uejall/co_intern_got_yelled_at_for_deleting_a_prod/
Okay hear me out before you comment, why did the intern get prod db access and why there is no backup. There was a backup and that's what saved the intern i would say. secondly on the prod db access part, I will explain that as well. Before that a bit of background : We work in a big tech company an
---

[RSS:Reddit Jobs & Careers (职场动态)]
My company is introducing JIRA=>PR AI pipeline: are we cooked
https://www.reddit.com/r/cscareerquestions/comments/1ueit2f/my_company_is_introducing_jirapr_ai_pipeline_are/
Just run Claude against jira ticket and out pops a PR, which then gets reviewed by claude. Before approval by human. Expectation is 50% increase in output atm. Got told like 3x &quot;dont' worry you'll still have your jobs cuz you need to review/validate the code&quot; but also &quot;the AI will kee
---

[RSS:Reddit Jobs & Careers (职场动态)]
From open for work to hired in 6 weeks. 10 YoE - Remote
https://www.reddit.com/r/cscareerquestions/comments/1uektoo/from_open_for_work_to_hired_in_6_weeks_10_yoe/
A lot of doom and gloom floating around this subreddit. Sorry for all the new grads and lower YoE devs. That being said, it is not true that the market is bad for everyone like is often said. I toggled my LinkedIn to open for work, updated my resume in the jobs section of LinkedIn. I also updated my
---

[RSS:Reddit Jobs & Careers (职场动态)]
Job Market Anecdotes For 1-3 YOE?
https://www.reddit.com/r/cscareerquestions/comments/1ueoi9x/job_market_anecdotes_for_13_yoe/
For Junior level but not new grad, how are you guys doing in Q2 2026? Any changes? &#32; submitted by &#32; /u/Fun-Advertising-8006 [link] &#32; [comments]
---

[RSS:Reddit Jobs & Careers (职场动态)]
'Students just aren't trying'
https://www.reddit.com/r/cscareerquestions/comments/1ue70fi/students_just_arent_trying/
I just finished my 4th semester of uni and had been applying for internships, both remote and on-site, since mid-term exams. I applied to like 300 internships. I ended up landing one in the IT department of a insurance company. Today I went to the internship office at my uni because I had to get the
---

[RSS:Reddit Jobs & Careers (职场动态)]
Did you all choose your niches or just kind of fell into them?
https://www.reddit.com/r/cscareerquestions/comments/1uerxoz/did_you_all_choose_your_niches_or_just_kind_of/
I guess my niche is data because the roles I mainly get and do the work for, but I never really purposely went towards it. Is that normal or did you deliberately choose? &#32; submitted by &#32; /u/AdObjective5502 [link] &#32; [comments]
---

[RSS:Reddit Jobs & Careers (职场动态)]
How to communicate like a senior+ engineer
https://www.reddit.com/r/cscareerquestions/comments/1ue6k45/how_to_communicate_like_a_senior_engineer/
A bit of background: I’m a backend engineer with around 10 years of experience, mostly at startups. I was recently laid off unexpectedly. The severance package was good, so I’m not under immediate pressure to find a job, but I’ve been interviewing to explore the market and see where I stand. After a
---

[RSS:Reddit Jobs & Careers (职场动态)]
Is software engineering a gamble to study in 2026?
https://www.reddit.com/r/cscareerquestions/comments/1uecrqj/is_software_engineering_a_gamble_to_study_in_2026/
Im deciding on what to study in uni. Ive always enjoyed coding and feel like i would excell in software engineering. But all these posts really put me off the field. Im at a point where im deciding between software engineering and electrical. I know id enjoy both but dont want to make a choice on fe
---

[RSS:Reddit Jobs & Careers (职场动态)]
Burnt out
https://www.reddit.com/r/cscareerquestions/comments/1uexhq3/burnt_out/
Hi! Below is a rant I just wrote, I think I should’ve complained on Reddit sooner. Thanks for reading if you do! … 4 years at a small company and 1.5 at a f500 company. I have been exhausted and unsure of my skills for the last year and a half. I tried to pick up the pace in January and work the lon
---

[RSS:Reddit Jobs & Careers (职场动态)]
Seeking perspective after 9 YOE; jump sinking ship or tough it out
https://www.reddit.com/r/cscareerquestions/comments/1ueq1jl/seeking_perspective_after_9_yoe_jump_sinking_ship/
I’ve been at the same company for 9 years, switching around several teams. Been with my current team for 4 years and it has been the most poorly managed one I’ve been on. The team is almost self-managed and severely understaffed. Our project lead is very hands off and hardly technical. My manager 1:
---

[RSS:Reddit Jobs & Careers (职场动态)]
Joined a startup recently and the imposter syndrome is genuinely killing me
https://www.reddit.com/r/cscareerquestions/comments/1ue6d7c/joined_a_startup_recently_and_the_imposter/
I joined this small tech startup around 2 months ago and I swear everyone here operates at a speed my brain cannot process. One senior dev casually fixes major backend bugs, reviews five PRs, jumps into product calls, and still has time to help everyone else while I am sitting there rereading basic 
---

[RSS:Reddit Jobs & Careers (职场动态)]
From all the things you studied on college, which ones you use the most daily? Which things you'd say that are obligatory or at least useful to learn?
https://www.reddit.com/r/cscareerquestions/comments/1ueldvo/from_all_the_things_you_studied_on_college_which/
Hi, programming student here. As you can imagine, I've seeing planty much of themes on the career, but after studying them, I've realized that some of them are conceptual and aren't used much in real life. Don't get me wrong, I ain't claiming anything to uni, I know that everyone of us must do our o
---

[RSS:Reddit Jobs & Careers (职场动态)]
Startups and AI woes
https://www.reddit.com/r/cscareerquestions/comments/1ueldol/startups_and_ai_woes/
I’m really at a loss for what to do. I just voluntarily left my startup job after a little less than a year. For some context, I got a wage reduction a week into the job for 3 months, which i then negotiated to a month for being “too slow” as a new grad. Their definition of too slow, of course, was 
---

[RSS:Reddit Jobs & Careers (职场动态)]
Looking into a niche of distributed systems/infrastructure. Should I pick a side or can I do both?
https://www.reddit.com/r/cscareerquestions/comments/1uettsr/looking_into_a_niche_of_distributed/
I'm a cs major and it's focused on cyber security and minor in math . I've been looking to focus in on a niche. I'm a transfer to my college, and my first college had us mostly coding in c++. I prefer the low level work, and I absolutely loved assembly. We made a game in assembler class which was ti
---

[RSS:Reddit Jobs & Careers (职场动态)]
Feedback on Career Tool
https://www.reddit.com/r/cscareerquestions/comments/1uexqpl/feedback_on_career_tool/
I created a tool to help evaluate job offers and give a true annual value after calculating taxes, equity, and even cost of living adjustments. Data is sourced from Numbeo, AAA, and the BLS to calculate taxes, cost of living adjustments, and commute costs from national averages. I need some feedback
---

[RSS:Reddit Jobs & Careers (职场动态)]
Not sure how to further my early career
https://www.reddit.com/r/cscareerquestions/comments/1uewpr7/not_sure_how_to_further_my_early_career/
I’ve worked at a startup for a year, and have begun to feel stagnant there. It’s fully remote, the workload is very light, and there is very little interaction with my team members. Most of this role has been me teaching myself, rather than learning from others who have been in this industry for a w
---

[RSS:Reddit Jobs & Careers (职场动态)]
wanting to improve technical literacy - advice wanted
https://www.reddit.com/r/cscareerquestions/comments/1ueqd5i/wanting_to_improve_technical_literacy_advice/
I'm a new grad/junior dev wanting to be able to explain / describe technical concepts at a higher level. Often, when asked certain questions in tech spaces or interviews (for example about full-stack development) I get a bit overwhelmed looking for the words to explain certain protocols / concepts, 
---

[RSS:Reddit Jobs & Careers (职场动态)]
Laid off, need tips as a junior SWE
https://www.reddit.com/r/cscareerquestions/comments/1uevagq/laid_off_need_tips_as_a_junior_swe/
I only have 1 YOE, and I as the fool I am didn’t really do any prep work during the job. I want to ask Claude pro to help guide me. Does anyone have any good prompts to help me start? I know I’m gonna have to do DSA / LeetCode and System Design, is there anything else I should keep in mind? &#32; su
---

[RSS:Reddit Jobs & Careers (职场动态)]
Hardware engineering technical questions help
https://www.reddit.com/r/cscareerquestions/comments/1uekoi3/hardware_engineering_technical_questions_help/
Hello. Somehow I have made it to the technical interview for a hardware engineering interview. I am a cs student, and the only related course I took is a course called physical computing. Does anyone have any tips for the interview? Any advice is very much appreciated. &#32; submitted by &#32; /u/bl
---

[HACKERNEWS]
LuaJIT 3.0 proposed syntax extensions
https://github.com/LuaJIT/LuaJIT/issues/1475
Score: 69 | Comments: 33
---

[HACKERNEWS]
OpenAI unveils its first custom chip, built by Broadcom
https://techcrunch.com/2026/06/24/openai-unveils-its-first-custom-chip-built-by-broadcom/
Score: 556 | Comments: 340
---

[HACKERNEWS]
Bible as RAG Database
https://www.crosscanon.com/
Score: 33 | Comments: 14
---

[HACKERNEWS]
Anthropic says Alibaba illicitly extracted Claude AI model capabilities
https://www.reuters.com/world/china/anthropic-says-alibaba-illicitly-extracted-claude-ai-model-capabilities-2026-06-24/
Score: 91 | Comments: 151
---

[HACKERNEWS]
Blogging can just be stating the obvious
https://blog.jim-nielsen.com/2026/blogging-stating-the-obvious/
Score: 85 | Comments: 35
---

[HACKERNEWS]
Ending All Respiratory Infections
https://blog.interceptfund.com/p/ending-respiratory-infections
Score: 30 | Comments: 11
---

[HACKERNEWS]
Qualcomm to Acquire Modular
https://www.reuters.com/business/qualcomm-buy-ai-startup-modular-2026-06-24/
Score: 152 | Comments: 37
---

[HACKERNEWS]
Exploring the internal representations of Pangram 3.3.2
https://www.pangram.com/pangram-space
Score: 10 | Comments: 1
---

[HACKERNEWS]
RubyLLM: A Ruby framework for all major AI providers
https://rubyllm.com/
Score: 348 | Comments: 56
---

[HACKERNEWS]
Mixing Visual and Textual Code
https://arxiv.org/abs/2603.15855
Score: 9 | Comments: 0
---

[HACKERNEWS]
PR spam today looks like email spam in the early 2000s
https://www.greptile.com/blog/prs-on-openclaw
Score: 184 | Comments: 102
---

[HACKERNEWS]
Computer use in Gemini 3.5 Flash
https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-computer-use-gemini-3-5-flash/
Score: 179 | Comments: 108
---

[HACKERNEWS]
45°C cooling design cuts data center water use to near zero
https://blogs.nvidia.com/blog/liquid-cooling-ai-factories/
Score: 206 | Comments: 157
---

[HACKERNEWS]
The Xteink X4 E-Ink Reader
https://blog.omgmog.net/post/xteink-x4-e-ink-reader/
Score: 181 | Comments: 109
---

[HACKERNEWS]
Writers and Drugs
https://lithub.com/are-writers-intrinsically-vulnerable-to-alcohol-and-drugs/
Score: 3 | Comments: 1
---

[HACKERNEWS]
Elastic lays off 7% of employees
https://www.elastic.co/blog/ceo-ash-kulkarni-announcement-to-elastic-employees
Score: 140 | Comments: 133
---

[HACKERNEWS]
Show HN: Nub – A Bun-like all-in-one toolkit for Node.js
https://github.com/nubjs/nub
Score: 205 | Comments: 60
---

[ACADEMIC - ARXIV]
标题: RevengeBench: Reverse Engineering Code-Space Policies from Behavioral Experiments
作者: Babak Rahmani, Sebastian Dziadzio, Joschka Strüber, Sergio Hernández-Gutiérrez, Matthias Bethge
链接: https://arxiv.org/abs/2606.26094v1
完整摘要: For most of scientific history, researchers studying behavior could only infer hidden mechanisms from outward actions: an inverse problem that becomes more tractable when observation is augmented by targeted intervention. We pose a computational analogue: given only behavioral traces of an agent in a game environment, can a learner reconstruct the underlying decision program as executable code, and how much does this reconstruction improve with the ability to design controlled experiments? We introduce RevengeBench, a benchmark of 75 LLM generated, Elo-calibrated policies across five game environments, drawn from CodeClash tournament trajectories. The learner observes the hidden target policy play against sampled opponents and designs behavioral probes in the form of custom opponent policies that elicit informative behavior. It then submits an executable hypothesis, which is evaluated using continuous action-distance metrics. We further validate that recovered code carries informative signal in downstream player-versus-player tournaments. Across twelve frontier LLMs, recovery quality varies substantially (34 to 72% of initial distance closed), with reconstructed policies yielding measurable competitive advantage, particularly for weaker models that otherwise struggle to design effective counter-strategies. Our benchmark positions behavioral recovery of programmatic policies as a tractable inverse problem in code-space, opening a path to opponent modeling, policy interpretability, and the broader question of inferring latent mechanisms from observations.
匹配关键词: video generation
---

[ACADEMIC - ARXIV]
标题: ForceBand: Learning Forceful Manipulation with sEMG
作者: Botao He, Zhi Wang, Linna Kuang, Ishaan Ghosh, Jitendra Malik, Cornelia Fermuller, Tingfan Wu, Jiayuan Mao, Ruoshi Liu, Haozhi Qi, Yiannis Aloimonos
链接: https://arxiv.org/abs/2606.26093v1
完整摘要: Human demonstrations are a scalable data source for learning robot manipulation policies. However, common sources of human demonstration data, such as motion-capture trajectories and internet videos, capture mostly motion and appearance while missing the contact forces that are critical for force-sensitive manipulation. In this paper, we introduce ForceBand, a low-cost wrist-worn sEMG system that turns human muscle activity into force-enriched demonstrations. We first collect a 10-hour multimodal dataset containing egocentric video, sEMG, IMU, and fingertip force measurements across diverse actions and objects. Using this dataset, we pre-train an EMG2Force model that predicts per-finger forces from sEMG and IMU signals. After a short user-specific calibration, users can collect target-task demonstrations using only ForceBand and video; EMG2Force then labels these demonstrations with per-finger force traces, producing force-augmented demonstrations for robot policy learning. Experiments show that ForceBand recovers fine-grained fingertip interactions with over 50% lower force prediction error than vision-based baselines and achieves an 87% success rate on pick, squeeze, and place tasks that require object-specific force control across objects with diverse shapes, sizes, and weights. Project website: https://forceband-emg.github.io
匹配关键词: video generation
---

[ACADEMIC - ARXIV]
标题: TryOnCrafter: Unleashing Camera Trajectories for Realistic Video Virtual Try-on via a Renderable 4D Try-on Proxy
作者: Hao Sun, Hao Yan, Mengting Chen, Quanjian Song, Yu Li, Juan Cao, Jinsong Lan, Xiaoyong Zhu, Bo Zheng, Sheng Tang
链接: https://arxiv.org/abs/2606.26092v1
完整摘要: While Video Virtual Try-on (VVT) has achieved remarkable progress in synthesizing realistic garment overlays on dynamic subjects, existing paradigms remains fundamentally constrained by a passive dependency on source camera trajectories, failing to accommodate the requisite interactive freedom for omnidirectional viewpoint exploration. To address this limitation, we define a pioneering research frontier: Camera-controllable Video Virtual Try-on (CaM-VVT). Unlike conventional VVT, CaM-VVT not only necessitates viewpoint-agnostic texture hallucination but also strict structural synchronization between non-rigid human dynamics and background contexts under arbitrary, unconstrained camera movements. To tackle these challenges, we present TryOnCrafter, the first unified DiT-based framework specifically architected for the CaM-VVT task. Departing from implicit pixel-space manipulation, we introduce a Renderable 4D Try-on Proxy that explicitly decouples the human subject from the environment. This is achieved by distilling high-fidelity 2D try-on priors into a clothed 3DGS-based avatar, which is subsequently animated via SMPL-X sequences and metric-aligned into a reconstructed background point cloud. This proxy establishes a robust structural foundation with superior texture density and motion integrity. Our Proxy-Anchored Video DiT leverages this robust structural foundation as a primary geometric anchor, ensuring that the synthesized photorealistic videos are strictly constrained by prescribed trajectories and physically plausible deformations. Benefiting from the inherent editability of the 4D proxy, TryOnCrafter facilitates diverse downstream applications, including human relocalization, ``bullet time'' effects, and $360$-degree orbital viewing.
匹配关键词: video generation
---

[ACADEMIC - ARXIV]
标题: On-Policy Self-Distillation with Sampled Demonstrations Reduces Output Diversity
作者: Andrei Liviu Nicolicioiu, Mohammad Pezeshki, Aaron Courville
链接: https://arxiv.org/abs/2606.26091v1
完整摘要: On-policy self-distillation achieves strong pass@1 accuracy by using a single model as both teacher and student, with the teacher conditioned on a correct demonstration to provide dense token-level feedback. We show that this could come at a hidden cost: rollout diversity decreases and pass@k curves flatten (i.e., generating more rollouts fails to improve accuracy). We trace this to compounding biases in the design of self-distillation with sampled demonstrations. The teacher scores each student rollout while conditioned on a sampled correct rollout, channeling its feedback through the model's own biases. We theoretically analyze the optimal self-distillation policy and show that it tilts the base distribution by a pointwise conditional mutual information score between the student's rollout and the correct rollout used as context. Unlike the ideal optimal on-policy reinforcement learning (RL), which preserves probability ratios among equally correct rollouts, self-distillation can amplify existing probability gaps, concentrating mass on already-dominant modes. On a controlled graph path-finding task and science question-answering benchmarks, self-distilled models match or exceed RL on average performance but exhibit substantially lower functional and semantic diversity, failing on out-of-distribution settings that require diverse strategies.
匹配关键词: video generation
---

[ACADEMIC - ARXIV]
标题: MVTrack4Gen: Multi-View Point Tracking as Geometric Supervision for 4D Video Generation
作者: JoungBin Lee, Jaewoo Jung, Jongmin Lee, Tongmin Kim, Hyunsung Kim, Takuya Narihira, Kazumi Fukuda, Jahyeok Koo, Jisang Han, Yuki Mitsufuji, Seungryong Kim
链接: https://arxiv.org/abs/2606.26087v1
完整摘要: Synthesizing a novel-view video from a monocular reference video along a target camera trajectory requires both geometric consistency and motion fidelity with respect to the reference video. Existing methods based on explicit 3D representations are limited by the accuracy of off-the-shelf reconstruction modules, which often produce inaccurate geometry for dynamic objects in monocular videos. In contrast, camera-conditioning-only methods can achieve high visual quality but often struggle to preserve geometric and motion consistency. In this work, we introduce MVTrack4Gen (Multi-View point Tracking for Novel-View Generation), a motion-aware training framework that leverages multi-view point tracking as an additional geometric and motion supervision signal for camera-conditioning-only novel-view video diffusion models. Our key finding is that specific attention layers encode strong correspondence cues, where query features attend to key features at geometrically corresponding locations across views and over time, and the misalignment of these correspondences causes motion inconsistency. Based on this observation, we route these features into an auxiliary multi-view tracking head and jointly train the diffusion model with a point-tracking objective. By explicitly strengthening these motion-aware correspondences, MVTrack4Gen improves existing models to better follow the motion in the reference view and maintain cross-view geometric consistency. Across diverse benchmarks, our method achieves state-of-the-art geometric consistency and competitive camera accuracy.
匹配关键词: video generation
---

[ACADEMIC - ARXIV]
标题: ForceBand: Learning Forceful Manipulation with sEMG
作者: Botao He, Zhi Wang, Linna Kuang, Ishaan Ghosh, Jitendra Malik, Cornelia Fermuller, Tingfan Wu, Jiayuan Mao, Ruoshi Liu, Haozhi Qi, Yiannis Aloimonos
链接: https://arxiv.org/abs/2606.26093v1
完整摘要: Human demonstrations are a scalable data source for learning robot manipulation policies. However, common sources of human demonstration data, such as motion-capture trajectories and internet videos, capture mostly motion and appearance while missing the contact forces that are critical for force-sensitive manipulation. In this paper, we introduce ForceBand, a low-cost wrist-worn sEMG system that turns human muscle activity into force-enriched demonstrations. We first collect a 10-hour multimodal dataset containing egocentric video, sEMG, IMU, and fingertip force measurements across diverse actions and objects. Using this dataset, we pre-train an EMG2Force model that predicts per-finger forces from sEMG and IMU signals. After a short user-specific calibration, users can collect target-task demonstrations using only ForceBand and video; EMG2Force then labels these demonstrations with per-finger force traces, producing force-augmented demonstrations for robot policy learning. Experiments show that ForceBand recovers fine-grained fingertip interactions with over 50% lower force prediction error than vision-based baselines and achieves an 87% success rate on pick, squeeze, and place tasks that require object-specific force control across objects with diverse shapes, sizes, and weights. Project website: https://forceband-emg.github.io
匹配关键词: video diffusion
---

[ACADEMIC - ARXIV]
标题: TryOnCrafter: Unleashing Camera Trajectories for Realistic Video Virtual Try-on via a Renderable 4D Try-on Proxy
作者: Hao Sun, Hao Yan, Mengting Chen, Quanjian Song, Yu Li, Juan Cao, Jinsong Lan, Xiaoyong Zhu, Bo Zheng, Sheng Tang
链接: https://arxiv.org/abs/2606.26092v1
完整摘要: While Video Virtual Try-on (VVT) has achieved remarkable progress in synthesizing realistic garment overlays on dynamic subjects, existing paradigms remains fundamentally constrained by a passive dependency on source camera trajectories, failing to accommodate the requisite interactive freedom for omnidirectional viewpoint exploration. To address this limitation, we define a pioneering research frontier: Camera-controllable Video Virtual Try-on (CaM-VVT). Unlike conventional VVT, CaM-VVT not only necessitates viewpoint-agnostic texture hallucination but also strict structural synchronization between non-rigid human dynamics and background contexts under arbitrary, unconstrained camera movements. To tackle these challenges, we present TryOnCrafter, the first unified DiT-based framework specifically architected for the CaM-VVT task. Departing from implicit pixel-space manipulation, we introduce a Renderable 4D Try-on Proxy that explicitly decouples the human subject from the environment. This is achieved by distilling high-fidelity 2D try-on priors into a clothed 3DGS-based avatar, which is subsequently animated via SMPL-X sequences and metric-aligned into a reconstructed background point cloud. This proxy establishes a robust structural foundation with superior texture density and motion integrity. Our Proxy-Anchored Video DiT leverages this robust structural foundation as a primary geometric anchor, ensuring that the synthesized photorealistic videos are strictly constrained by prescribed trajectories and physically plausible deformations. Benefiting from the inherent editability of the 4D proxy, TryOnCrafter facilitates diverse downstream applications, including human relocalization, ``bullet time'' effects, and $360$-degree orbital viewing.
匹配关键词: video diffusion
---

[ACADEMIC - ARXIV]
标题: MVTrack4Gen: Multi-View Point Tracking as Geometric Supervision for 4D Video Generation
作者: JoungBin Lee, Jaewoo Jung, Jongmin Lee, Tongmin Kim, Hyunsung Kim, Takuya Narihira, Kazumi Fukuda, Jahyeok Koo, Jisang Han, Yuki Mitsufuji, Seungryong Kim
链接: https://arxiv.org/abs/2606.26087v1
完整摘要: Synthesizing a novel-view video from a monocular reference video along a target camera trajectory requires both geometric consistency and motion fidelity with respect to the reference video. Existing methods based on explicit 3D representations are limited by the accuracy of off-the-shelf reconstruction modules, which often produce inaccurate geometry for dynamic objects in monocular videos. In contrast, camera-conditioning-only methods can achieve high visual quality but often struggle to preserve geometric and motion consistency. In this work, we introduce MVTrack4Gen (Multi-View point Tracking for Novel-View Generation), a motion-aware training framework that leverages multi-view point tracking as an additional geometric and motion supervision signal for camera-conditioning-only novel-view video diffusion models. Our key finding is that specific attention layers encode strong correspondence cues, where query features attend to key features at geometrically corresponding locations across views and over time, and the misalignment of these correspondences causes motion inconsistency. Based on this observation, we route these features into an auxiliary multi-view tracking head and jointly train the diffusion model with a point-tracking objective. By explicitly strengthening these motion-aware correspondences, MVTrack4Gen improves existing models to better follow the motion in the reference view and maintain cross-view geometric consistency. Across diverse benchmarks, our method achieves state-of-the-art geometric consistency and competitive camera accuracy.
匹配关键词: video diffusion
---

[ACADEMIC - ARXIV]
标题: DomainShuttle: Freeform Open Domain Subject-driven Text-to-video Generation
作者: Nan Chen, Yiyang Cai, Rongchang Xie, Junwen Pan, Cheng Chen, Weinan Jia, Zhuowei Chen, Wen Zhou, Zhenbang Sun, Wenhan Luo
链接: https://arxiv.org/abs/2606.26058v1
完整摘要: Open domain subject-driven text-to-video (S2V) generation has drawn significant interest in academia and industry. Open domain S2V mainly involves two scenarios: in-domain, which requires retaining the reference subject features as much as possible, and cross-domain, which preserves the intrinsic features of the subject while allowing subject-irrelevant properties to vary flexibly according to the text prompt. Existing methods primarily focus on maximizing subject fidelity in in-domain scenarios, which limits their editability and adaptability in cross-domain scenarios, such as novel styles, semantic combinations, or domain attributes. In this study, we propose that an ideal S2V method should flexibly shuttle between different domains, achieving strong performance in both in-domain and cross-domain scenarios. To this end, we propose DomainShuttle, which could achieve high fidelity and generative flexibility for open domain video personalization. Specifically, we introduce Domain-MoT, which decouples videos and reference features and introduces the domain-aware AdaLN for domain-specific modeling of reference images. We then introduce the Video-Reference DualRoPE scheme, which places reference image tokens and video tokens in separate RoPE spaces to enable precise subject-level spatial modeling, and Cross-Pair Consistent Loss, which aims to extract intrinsic subject features unaffected by irrelevant features. Extensive experiments demonstrate that DomainShuttle achieves significant performance improvements over existing methods, exhibiting high subject fidelity and generative flexibility across diverse open domain application scenarios.
匹配关键词: video diffusion
---

[ACADEMIC - ARXIV]
标题: G2DP: Diffusion Planning with Spatio-Temporal Grid Guidance
作者: Hang Yu, Ye Jin, Alessandro Canevaro, Julian Schmidt, Julian Jordan, Peizheng Li, Marc Kaufeld, Silvan Lindner, Johannes Betz, Wilhelm Stork
链接: https://arxiv.org/abs/2606.26017v1
完整摘要: In autonomous driving, diffusion-based planners have emerged as a promising paradigm for robust motion planning in dense and interactive traffic, as they can effectively model diverse driving behaviors. However, their inherent stochasticity often requires explicit guidance during denoising to ensure safety and route adherence for robust closed-loop execution. Existing guidance typically relies on sparse, entity-centric geometric queries or post-hoc refinement, yielding limited situational awareness and fragile performance in interactive scenes. To address this issue, we propose G2DP (Grid-Guided Diffusion Planning), a diffusion-based planner that directly enforces dense environmental constraints through inference-time guidance. Specifically, G2DP constructs a differentiable spatio-temporal cost volume by fusing probabilistic future occupancy distributions with a route-progress map. By formulating this volume as a continuous safety energy functional, it injects dense gradients directly into the denoising loop, actively steering trajectory generation toward collision-free and progress-optimal regions. Extensive closed-loop evaluations show that G2DP achieves state-of-the-art performance on nuPlan, outperforming the strongest imitation-learning baseline by +7.2 points in reactive score. It further maintains top scores in zero-shot transfers to interPlan and DeepScenario benchmarks, with collision avoidance improving by +10.15 over the unguided approach on interPlan. These results demonstrate that spatio-temporal cost grids serve as an effective representation for robust guidance in diffusion-based planning.
匹配关键词: video diffusion
---

[ACADEMIC - ARXIV]
标题: DomainShuttle: Freeform Open Domain Subject-driven Text-to-video Generation
作者: Nan Chen, Yiyang Cai, Rongchang Xie, Junwen Pan, Cheng Chen, Weinan Jia, Zhuowei Chen, Wen Zhou, Zhenbang Sun, Wenhan Luo
链接: https://arxiv.org/abs/2606.26058v1
完整摘要: Open domain subject-driven text-to-video (S2V) generation has drawn significant interest in academia and industry. Open domain S2V mainly involves two scenarios: in-domain, which requires retaining the reference subject features as much as possible, and cross-domain, which preserves the intrinsic features of the subject while allowing subject-irrelevant properties to vary flexibly according to the text prompt. Existing methods primarily focus on maximizing subject fidelity in in-domain scenarios, which limits their editability and adaptability in cross-domain scenarios, such as novel styles, semantic combinations, or domain attributes. In this study, we propose that an ideal S2V method should flexibly shuttle between different domains, achieving strong performance in both in-domain and cross-domain scenarios. To this end, we propose DomainShuttle, which could achieve high fidelity and generative flexibility for open domain video personalization. Specifically, we introduce Domain-MoT, which decouples videos and reference features and introduces the domain-aware AdaLN for domain-specific modeling of reference images. We then introduce the Video-Reference DualRoPE scheme, which places reference image tokens and video tokens in separate RoPE spaces to enable precise subject-level spatial modeling, and Cross-Pair Consistent Loss, which aims to extract intrinsic subject features unaffected by irrelevant features. Extensive experiments demonstrate that DomainShuttle achieves significant performance improvements over existing methods, exhibiting high subject fidelity and generative flexibility across diverse open domain application scenarios.
匹配关键词: text-to-video
---

[ACADEMIC - ARXIV]
标题: Graph it first! Enabling Reasoning on Long-form Egocentric Videos through Scene Graphs
作者: Agnese Taluzzi, Riccardo Santambrogio, Simone Mentasti, Chiara Plizzari, Matteo Matteucci
链接: https://arxiv.org/abs/2606.25842v1
完整摘要: Existing multi-modal large language models (MLLMs) face significant challenges in processing long video sequences due to strict input token limitations. As a result, current video understanding approaches, especially in egocentric settings characterized by complex dynamics, frequent state changes, and moving cameras, are forced to massively subsample frames. This leads to severe loss of temporal and contextual information, constraining their ability to perform fine-grained video reasoning. In this work, we introduce a framework for egocentric video question answering (VQA) that overcomes these input constraints through Egocentric Scene Graphs (EgoSGs), i.e., temporally grounded, structured representations that capture objects, attributes, spatial relations, and interactions over time. By representing videos as compact, text-based scene graphs, our method preserves the essential visual and temporal information of the original video in a symbolic form that drastically reduces input length while maintaining semantic richness. Crucially, this enables MLLMs to reason efficiently over entire video sequences within their token budget. On HD-EPIC VQA, our method achieves state-of-the-art results, outperforming strong video-based baselines on multiple models and suggesting that structured, temporally grounded representations like EgoSGs can bridge long-form egocentric video understanding and the context limitations of today's MLLMs.
匹配关键词: text-to-video
---

[ACADEMIC - ARXIV]
标题: VPA-Guard: Defending and Benchmarking Image-to-Video Generation Against Visual Prompt Attacks
作者: Yining Sun, Haoyu Kang, Jiajun Wu, Heng Zhang, Danyang Zhang, Zhenjun Zhao, Haochen Han, Fangming Liu, Wai Kin Victor Chan, Alex Jinpeng Wang
链接: https://arxiv.org/abs/2606.25592v1
完整摘要: Recent advancements in Image-to-Video (I2V) generation have transformed input images from simple appearance references into interactive control interfaces where visual cues such as arrows, sketches, and emojis orchestrate complex video dynamics with unprecedented controllability. However, these seemingly innocuous static cues can be interpreted by models as executable temporal instructions, unfolding into harmful actions in the generated videos. Despite the severity of this threat, existing safety benchmarks remain predominantly focused on text-based and content-only image-based jailbreaks, leaving implicit visual prompt attacks insufficiently explored. To bridge this gap, we present VVA-Bench, the first systematic benchmark for evaluating video generation safety under categorized vision-centric prompt attacks. Extensive experiments on VVA-Bench demonstrate that state-of-the-art models are highly susceptible to such attacks, with Attack Success Rates (ASR) reaching 100.0\% on Wan 2.7 and 74.8\% on Veo 3.1. To mitigate these risks, we propose VPA-Guard, a retrieval-augmented and self-evolving defense framework. By leveraging few-shot reasoning to identify latent malicious intents, our method reduces the attack ASR by 44.2\% and the harmfulness score by 73.4\% on average, while maintaining the model's utility for legitimate user edits. Our work provides both a rigorous benchmark and an effective defense strategy to advance safe and socially responsible multimodal generation.
匹配关键词: text-to-video
---

[ACADEMIC - ARXIV]
标题: EchoStyle: Unlocking High-Fidelity Video Stylization with Reverse Data Synthesis
作者: Huaqiu Li, Jiahao Wang, Sijia Cai, Hualian Sheng, Bing Deng, Jieping Ye, Wenhan Luo
链接: https://arxiv.org/abs/2606.25465v1
完整摘要: While image stylization has been studied extensively, video stylization remains a critical and largely unsolved challenge in the field of intelligent content creation. Existing methods, usually utilizing a reference image as the style prior, suffer from content leakage, data scarcity and limited adaptability to long videos, leading to suboptimal results with severe style drift and motion distortion. For these issues, we present EchoStyle, a scalable text-driven framework to achieve high-quality stylization of videos with arbitrary lengths. To start with, we construct a video-to-video architecture to appropriately re-fuse the video content and the text style. To address data scarcity, we pioneer an automatic reverse-synthesis pipeline to establish V-Style20k, a large-scale stylization dataset of 20k high-quality video pairs. To facilitate long video stylization, we devise an init-follow-mode mechanism along with a sliding-window inference strategy. Extensive experiments demonstrate EchoStyle's excellent performance across a wide range of artistic styles, even comparable to leading closed-source solutions.
匹配关键词: text-to-video
---

[ACADEMIC - ARXIV]
标题: Generative AI for Safe and Photorealistic Drone Light Shows
作者: Pascal Reinhold, Alexander Gräfe, Sebastian Trimpe
链接: https://arxiv.org/abs/2606.25458v1
完整摘要: Drone light shows are redefining aerial entertainment, yet their widespread adoption is bottlenecked by labor-intensive, manual animation. While generative AI promises an automated alternative, current frameworks fail to provide photorealism with fluid, dynamic motion. To address this limitation, we introduce SWAN, an end-to-end pipeline that synthesizes photorealistic, large-scale, and collision-free drone choreographies directly from text prompts. SWAN converts text into realistic reference videos and translates these pixel-space dynamics into physical swarm kinematics using a novel, adaptive point-tracking algorithm. Unlike existing trackers, this method maintains spatial coherence through severe occlusions and rapid topological shifts. A dedicated planner then allocates these trajectories to individual drones, while a subsequent safety filter ensures collision-free execution. We demonstrate scalability by safely orchestrating simulated 2,000-drone formations and validate physical feasibility on a dense real-world swarm of 49 quadcopters, operating everything entirely on standard consumer hardware. Combined, this work demonstrates how generative AI can be leveraged to automate multi-robot choreography design, providing an accessible new framework for drone light shows.
匹配关键词: text-to-video
---

[ACADEMIC - ARXIV]
标题: ForceBand: Learning Forceful Manipulation with sEMG
作者: Botao He, Zhi Wang, Linna Kuang, Ishaan Ghosh, Jitendra Malik, Cornelia Fermuller, Tingfan Wu, Jiayuan Mao, Ruoshi Liu, Haozhi Qi, Yiannis Aloimonos
链接: https://arxiv.org/abs/2606.26093v1
完整摘要: Human demonstrations are a scalable data source for learning robot manipulation policies. However, common sources of human demonstration data, such as motion-capture trajectories and internet videos, capture mostly motion and appearance while missing the contact forces that are critical for force-sensitive manipulation. In this paper, we introduce ForceBand, a low-cost wrist-worn sEMG system that turns human muscle activity into force-enriched demonstrations. We first collect a 10-hour multimodal dataset containing egocentric video, sEMG, IMU, and fingertip force measurements across diverse actions and objects. Using this dataset, we pre-train an EMG2Force model that predicts per-finger forces from sEMG and IMU signals. After a short user-specific calibration, users can collect target-task demonstrations using only ForceBand and video; EMG2Force then labels these demonstrations with per-finger force traces, producing force-augmented demonstrations for robot policy learning. Experiments show that ForceBand recovers fine-grained fingertip interactions with over 50% lower force prediction error than vision-based baselines and achieves an 87% success rate on pick, squeeze, and place tasks that require object-specific force control across objects with diverse shapes, sizes, and weights. Project website: https://forceband-emg.github.io
匹配关键词: video synthesis
---

[ACADEMIC - ARXIV]
标题: TryOnCrafter: Unleashing Camera Trajectories for Realistic Video Virtual Try-on via a Renderable 4D Try-on Proxy
作者: Hao Sun, Hao Yan, Mengting Chen, Quanjian Song, Yu Li, Juan Cao, Jinsong Lan, Xiaoyong Zhu, Bo Zheng, Sheng Tang
链接: https://arxiv.org/abs/2606.26092v1
完整摘要: While Video Virtual Try-on (VVT) has achieved remarkable progress in synthesizing realistic garment overlays on dynamic subjects, existing paradigms remains fundamentally constrained by a passive dependency on source camera trajectories, failing to accommodate the requisite interactive freedom for omnidirectional viewpoint exploration. To address this limitation, we define a pioneering research frontier: Camera-controllable Video Virtual Try-on (CaM-VVT). Unlike conventional VVT, CaM-VVT not only necessitates viewpoint-agnostic texture hallucination but also strict structural synchronization between non-rigid human dynamics and background contexts under arbitrary, unconstrained camera movements. To tackle these challenges, we present TryOnCrafter, the first unified DiT-based framework specifically architected for the CaM-VVT task. Departing from implicit pixel-space manipulation, we introduce a Renderable 4D Try-on Proxy that explicitly decouples the human subject from the environment. This is achieved by distilling high-fidelity 2D try-on priors into a clothed 3DGS-based avatar, which is subsequently animated via SMPL-X sequences and metric-aligned into a reconstructed background point cloud. This proxy establishes a robust structural foundation with superior texture density and motion integrity. Our Proxy-Anchored Video DiT leverages this robust structural foundation as a primary geometric anchor, ensuring that the synthesized photorealistic videos are strictly constrained by prescribed trajectories and physically plausible deformations. Benefiting from the inherent editability of the 4D proxy, TryOnCrafter facilitates diverse downstream applications, including human relocalization, ``bullet time'' effects, and $360$-degree orbital viewing.
匹配关键词: video synthesis
---

[ACADEMIC - ARXIV]
标题: MVTrack4Gen: Multi-View Point Tracking as Geometric Supervision for 4D Video Generation
作者: JoungBin Lee, Jaewoo Jung, Jongmin Lee, Tongmin Kim, Hyunsung Kim, Takuya Narihira, Kazumi Fukuda, Jahyeok Koo, Jisang Han, Yuki Mitsufuji, Seungryong Kim
链接: https://arxiv.org/abs/2606.26087v1
完整摘要: Synthesizing a novel-view video from a monocular reference video along a target camera trajectory requires both geometric consistency and motion fidelity with respect to the reference video. Existing methods based on explicit 3D representations are limited by the accuracy of off-the-shelf reconstruction modules, which often produce inaccurate geometry for dynamic objects in monocular videos. In contrast, camera-conditioning-only methods can achieve high visual quality but often struggle to preserve geometric and motion consistency. In this work, we introduce MVTrack4Gen (Multi-View point Tracking for Novel-View Generation), a motion-aware training framework that leverages multi-view point tracking as an additional geometric and motion supervision signal for camera-conditioning-only novel-view video diffusion models. Our key finding is that specific attention layers encode strong correspondence cues, where query features attend to key features at geometrically corresponding locations across views and over time, and the misalignment of these correspondences causes motion inconsistency. Based on this observation, we route these features into an auxiliary multi-view tracking head and jointly train the diffusion model with a point-tracking objective. By explicitly strengthening these motion-aware correspondences, MVTrack4Gen improves existing models to better follow the motion in the reference view and maintain cross-view geometric consistency. Across diverse benchmarks, our method achieves state-of-the-art geometric consistency and competitive camera accuracy.
匹配关键词: video synthesis
---

[ACADEMIC - ARXIV]
标题: DomainShuttle: Freeform Open Domain Subject-driven Text-to-video Generation
作者: Nan Chen, Yiyang Cai, Rongchang Xie, Junwen Pan, Cheng Chen, Weinan Jia, Zhuowei Chen, Wen Zhou, Zhenbang Sun, Wenhan Luo
链接: https://arxiv.org/abs/2606.26058v1
完整摘要: Open domain subject-driven text-to-video (S2V) generation has drawn significant interest in academia and industry. Open domain S2V mainly involves two scenarios: in-domain, which requires retaining the reference subject features as much as possible, and cross-domain, which preserves the intrinsic features of the subject while allowing subject-irrelevant properties to vary flexibly according to the text prompt. Existing methods primarily focus on maximizing subject fidelity in in-domain scenarios, which limits their editability and adaptability in cross-domain scenarios, such as novel styles, semantic combinations, or domain attributes. In this study, we propose that an ideal S2V method should flexibly shuttle between different domains, achieving strong performance in both in-domain and cross-domain scenarios. To this end, we propose DomainShuttle, which could achieve high fidelity and generative flexibility for open domain video personalization. Specifically, we introduce Domain-MoT, which decouples videos and reference features and introduces the domain-aware AdaLN for domain-specific modeling of reference images. We then introduce the Video-Reference DualRoPE scheme, which places reference image tokens and video tokens in separate RoPE spaces to enable precise subject-level spatial modeling, and Cross-Pair Consistent Loss, which aims to extract intrinsic subject features unaffected by irrelevant features. Extensive experiments demonstrate that DomainShuttle achieves significant performance improvements over existing methods, exhibiting high subject fidelity and generative flexibility across diverse open domain application scenarios.
匹配关键词: video synthesis
---

[ACADEMIC - ARXIV]
标题: MIMFlow: Integrating Masked Image Modeling with Normalizing Flows for End-to-End Image Generation
作者: Yang Chen, Xiaowei Xu, Shuai Wang, Xinwen Zhang, Qiushi Guo, Tiezheng Ge, Limin Wang
链接: https://arxiv.org/abs/2606.26016v1
完整摘要: Normalizing Flows (NFs) are powerful generative models capable of exact density estimation and sampling. However, their strict invertibility often forces the model to exhaust its capacity on low-level pixel details, hindering the capture of high-level semantic structures. While Masked Image Modeling (MIM) has excelled in representation learning, its integration into generative pipelines has remained largely modular and disjointed. In this paper, we propose MIMFlow, a unified end-to-end framework that jointly optimizes latent semantics, pixel reconstruction, and generative flow. By employing a VAE encoder to infer semantic latent from masked images, MIMFlow achieves a principled decoupling of the generative task: the Normalizing Flow focuses on modeling a simplified, low-frequency semantic manifold, while a specialized decoder handles high-frequency synthesis. This design effectively resolves the inherent capacity bottleneck of NFs, allowing the model to prioritize global structural coherence over redundant noise. Empirical results on ImageNet 256$\times$256 show that MIMFlow-L reaches 71.3\% linear probing accuracy and an FID of 2.50. Despite using only 128 tokens (50\% fewer than standard models), it yields a 32.8\% performance gain over similar-scale NF baselines. Our code is available at https://github.com/MCG-NJU/MIMFlow.
匹配关键词: video synthesis
---

[ACADEMIC - ARXIV]
标题: ForceBand: Learning Forceful Manipulation with sEMG
作者: Botao He, Zhi Wang, Linna Kuang, Ishaan Ghosh, Jitendra Malik, Cornelia Fermuller, Tingfan Wu, Jiayuan Mao, Ruoshi Liu, Haozhi Qi, Yiannis Aloimonos
链接: https://arxiv.org/abs/2606.26093v1
完整摘要: Human demonstrations are a scalable data source for learning robot manipulation policies. However, common sources of human demonstration data, such as motion-capture trajectories and internet videos, capture mostly motion and appearance while missing the contact forces that are critical for force-sensitive manipulation. In this paper, we introduce ForceBand, a low-cost wrist-worn sEMG system that turns human muscle activity into force-enriched demonstrations. We first collect a 10-hour multimodal dataset containing egocentric video, sEMG, IMU, and fingertip force measurements across diverse actions and objects. Using this dataset, we pre-train an EMG2Force model that predicts per-finger forces from sEMG and IMU signals. After a short user-specific calibration, users can collect target-task demonstrations using only ForceBand and video; EMG2Force then labels these demonstrations with per-finger force traces, producing force-augmented demonstrations for robot policy learning. Experiments show that ForceBand recovers fine-grained fingertip interactions with over 50% lower force prediction error than vision-based baselines and achieves an 87% success rate on pick, squeeze, and place tasks that require object-specific force control across objects with diverse shapes, sizes, and weights. Project website: https://forceband-emg.github.io
匹配关键词: video editing
---

[ACADEMIC - ARXIV]
标题: TryOnCrafter: Unleashing Camera Trajectories for Realistic Video Virtual Try-on via a Renderable 4D Try-on Proxy
作者: Hao Sun, Hao Yan, Mengting Chen, Quanjian Song, Yu Li, Juan Cao, Jinsong Lan, Xiaoyong Zhu, Bo Zheng, Sheng Tang
链接: https://arxiv.org/abs/2606.26092v1
完整摘要: While Video Virtual Try-on (VVT) has achieved remarkable progress in synthesizing realistic garment overlays on dynamic subjects, existing paradigms remains fundamentally constrained by a passive dependency on source camera trajectories, failing to accommodate the requisite interactive freedom for omnidirectional viewpoint exploration. To address this limitation, we define a pioneering research frontier: Camera-controllable Video Virtual Try-on (CaM-VVT). Unlike conventional VVT, CaM-VVT not only necessitates viewpoint-agnostic texture hallucination but also strict structural synchronization between non-rigid human dynamics and background contexts under arbitrary, unconstrained camera movements. To tackle these challenges, we present TryOnCrafter, the first unified DiT-based framework specifically architected for the CaM-VVT task. Departing from implicit pixel-space manipulation, we introduce a Renderable 4D Try-on Proxy that explicitly decouples the human subject from the environment. This is achieved by distilling high-fidelity 2D try-on priors into a clothed 3DGS-based avatar, which is subsequently animated via SMPL-X sequences and metric-aligned into a reconstructed background point cloud. This proxy establishes a robust structural foundation with superior texture density and motion integrity. Our Proxy-Anchored Video DiT leverages this robust structural foundation as a primary geometric anchor, ensuring that the synthesized photorealistic videos are strictly constrained by prescribed trajectories and physically plausible deformations. Benefiting from the inherent editability of the 4D proxy, TryOnCrafter facilitates diverse downstream applications, including human relocalization, ``bullet time'' effects, and $360$-degree orbital viewing.
匹配关键词: video editing
---

[ACADEMIC - ARXIV]
标题: MVTrack4Gen: Multi-View Point Tracking as Geometric Supervision for 4D Video Generation
作者: JoungBin Lee, Jaewoo Jung, Jongmin Lee, Tongmin Kim, Hyunsung Kim, Takuya Narihira, Kazumi Fukuda, Jahyeok Koo, Jisang Han, Yuki Mitsufuji, Seungryong Kim
链接: https://arxiv.org/abs/2606.26087v1
完整摘要: Synthesizing a novel-view video from a monocular reference video along a target camera trajectory requires both geometric consistency and motion fidelity with respect to the reference video. Existing methods based on explicit 3D representations are limited by the accuracy of off-the-shelf reconstruction modules, which often produce inaccurate geometry for dynamic objects in monocular videos. In contrast, camera-conditioning-only methods can achieve high visual quality but often struggle to preserve geometric and motion consistency. In this work, we introduce MVTrack4Gen (Multi-View point Tracking for Novel-View Generation), a motion-aware training framework that leverages multi-view point tracking as an additional geometric and motion supervision signal for camera-conditioning-only novel-view video diffusion models. Our key finding is that specific attention layers encode strong correspondence cues, where query features attend to key features at geometrically corresponding locations across views and over time, and the misalignment of these correspondences causes motion inconsistency. Based on this observation, we route these features into an auxiliary multi-view tracking head and jointly train the diffusion model with a point-tracking objective. By explicitly strengthening these motion-aware correspondences, MVTrack4Gen improves existing models to better follow the motion in the reference view and maintain cross-view geometric consistency. Across diverse benchmarks, our method achieves state-of-the-art geometric consistency and competitive camera accuracy.
匹配关键词: video editing
---

[ACADEMIC - ARXIV]
标题: Model Forensics: Investigating Whether Concerning Behavior Reflects Misalignment
作者: Aditya Singh, Gerson Kroiz, Senthooran Rajamanoharan, Neel Nanda
链接: https://arxiv.org/abs/2606.26071v1
完整摘要: A central goal of safety research is determining whether a model is misaligned. Prior work has largely focused on detecting concerning behavior. But behavior alone does not establish misalignment: a concerning action can arise from benign causes such as confusion. This motivates model forensics: investigating whether the action was driven by malign intent. In this paper, we propose a baseline protocol for model forensics consisting of two steps, iterated as needed. First, we read the chain of thought (CoT) to generate hypotheses about what drives model behavior. Second, we make edits to the prompt or environment to test these hypotheses. While the CoT is not always faithful, it is a rich source of unsupervised insight that can guide the collection of more rigorous evidence. To evaluate our protocol, we create a suite of six agentic environments where models exhibit concerning behavior, and apply it to each. We establish that Kimi K2 Thinking takes shortcuts due to a genuine disposition towards low-effort actions, by showing this hypothesis successfully predicts its behavior. Through counterfactual experiments, we show DeepSeek R1 deceives out of a desire to be consistent with a previous instance of itself. Our methods nonetheless leave significant room for refinement. For example, when we test whether Kimi K2 Thinking believes it is violating user intent, we find no evidence of such a belief, but without positive controls we cannot confirm our tests would detect it. Overall, we find our simple protocol provides a strong baseline that we hope future work will improve upon. More broadly, our work is a concrete step in developing the growing field of model forensics.
匹配关键词: video editing
---

[ACADEMIC - ARXIV]
标题: DomainShuttle: Freeform Open Domain Subject-driven Text-to-video Generation
作者: Nan Chen, Yiyang Cai, Rongchang Xie, Junwen Pan, Cheng Chen, Weinan Jia, Zhuowei Chen, Wen Zhou, Zhenbang Sun, Wenhan Luo
链接: https://arxiv.org/abs/2606.26058v1
完整摘要: Open domain subject-driven text-to-video (S2V) generation has drawn significant interest in academia and industry. Open domain S2V mainly involves two scenarios: in-domain, which requires retaining the reference subject features as much as possible, and cross-domain, which preserves the intrinsic features of the subject while allowing subject-irrelevant properties to vary flexibly according to the text prompt. Existing methods primarily focus on maximizing subject fidelity in in-domain scenarios, which limits their editability and adaptability in cross-domain scenarios, such as novel styles, semantic combinations, or domain attributes. In this study, we propose that an ideal S2V method should flexibly shuttle between different domains, achieving strong performance in both in-domain and cross-domain scenarios. To this end, we propose DomainShuttle, which could achieve high fidelity and generative flexibility for open domain video personalization. Specifically, we introduce Domain-MoT, which decouples videos and reference features and introduces the domain-aware AdaLN for domain-specific modeling of reference images. We then introduce the Video-Reference DualRoPE scheme, which places reference image tokens and video tokens in separate RoPE spaces to enable precise subject-level spatial modeling, and Cross-Pair Consistent Loss, which aims to extract intrinsic subject features unaffected by irrelevant features. Extensive experiments demonstrate that DomainShuttle achieves significant performance improvements over existing methods, exhibiting high subject fidelity and generative flexibility across diverse open domain application scenarios.
匹配关键词: video editing
---

[ACADEMIC - ARXIV]
标题: ForceBand: Learning Forceful Manipulation with sEMG
作者: Botao He, Zhi Wang, Linna Kuang, Ishaan Ghosh, Jitendra Malik, Cornelia Fermuller, Tingfan Wu, Jiayuan Mao, Ruoshi Liu, Haozhi Qi, Yiannis Aloimonos
链接: https://arxiv.org/abs/2606.26093v1
完整摘要: Human demonstrations are a scalable data source for learning robot manipulation policies. However, common sources of human demonstration data, such as motion-capture trajectories and internet videos, capture mostly motion and appearance while missing the contact forces that are critical for force-sensitive manipulation. In this paper, we introduce ForceBand, a low-cost wrist-worn sEMG system that turns human muscle activity into force-enriched demonstrations. We first collect a 10-hour multimodal dataset containing egocentric video, sEMG, IMU, and fingertip force measurements across diverse actions and objects. Using this dataset, we pre-train an EMG2Force model that predicts per-finger forces from sEMG and IMU signals. After a short user-specific calibration, users can collect target-task demonstrations using only ForceBand and video; EMG2Force then labels these demonstrations with per-finger force traces, producing force-augmented demonstrations for robot policy learning. Experiments show that ForceBand recovers fine-grained fingertip interactions with over 50% lower force prediction error than vision-based baselines and achieves an 87% success rate on pick, squeeze, and place tasks that require object-specific force control across objects with diverse shapes, sizes, and weights. Project website: https://forceband-emg.github.io
匹配关键词: video understanding
---

[ACADEMIC - ARXIV]
标题: TryOnCrafter: Unleashing Camera Trajectories for Realistic Video Virtual Try-on via a Renderable 4D Try-on Proxy
作者: Hao Sun, Hao Yan, Mengting Chen, Quanjian Song, Yu Li, Juan Cao, Jinsong Lan, Xiaoyong Zhu, Bo Zheng, Sheng Tang
链接: https://arxiv.org/abs/2606.26092v1
完整摘要: While Video Virtual Try-on (VVT) has achieved remarkable progress in synthesizing realistic garment overlays on dynamic subjects, existing paradigms remains fundamentally constrained by a passive dependency on source camera trajectories, failing to accommodate the requisite interactive freedom for omnidirectional viewpoint exploration. To address this limitation, we define a pioneering research frontier: Camera-controllable Video Virtual Try-on (CaM-VVT). Unlike conventional VVT, CaM-VVT not only necessitates viewpoint-agnostic texture hallucination but also strict structural synchronization between non-rigid human dynamics and background contexts under arbitrary, unconstrained camera movements. To tackle these challenges, we present TryOnCrafter, the first unified DiT-based framework specifically architected for the CaM-VVT task. Departing from implicit pixel-space manipulation, we introduce a Renderable 4D Try-on Proxy that explicitly decouples the human subject from the environment. This is achieved by distilling high-fidelity 2D try-on priors into a clothed 3DGS-based avatar, which is subsequently animated via SMPL-X sequences and metric-aligned into a reconstructed background point cloud. This proxy establishes a robust structural foundation with superior texture density and motion integrity. Our Proxy-Anchored Video DiT leverages this robust structural foundation as a primary geometric anchor, ensuring that the synthesized photorealistic videos are strictly constrained by prescribed trajectories and physically plausible deformations. Benefiting from the inherent editability of the 4D proxy, TryOnCrafter facilitates diverse downstream applications, including human relocalization, ``bullet time'' effects, and $360$-degree orbital viewing.
匹配关键词: video understanding
---

[ACADEMIC - ARXIV]
标题: MVTrack4Gen: Multi-View Point Tracking as Geometric Supervision for 4D Video Generation
作者: JoungBin Lee, Jaewoo Jung, Jongmin Lee, Tongmin Kim, Hyunsung Kim, Takuya Narihira, Kazumi Fukuda, Jahyeok Koo, Jisang Han, Yuki Mitsufuji, Seungryong Kim
链接: https://arxiv.org/abs/2606.26087v1
完整摘要: Synthesizing a novel-view video from a monocular reference video along a target camera trajectory requires both geometric consistency and motion fidelity with respect to the reference video. Existing methods based on explicit 3D representations are limited by the accuracy of off-the-shelf reconstruction modules, which often produce inaccurate geometry for dynamic objects in monocular videos. In contrast, camera-conditioning-only methods can achieve high visual quality but often struggle to preserve geometric and motion consistency. In this work, we introduce MVTrack4Gen (Multi-View point Tracking for Novel-View Generation), a motion-aware training framework that leverages multi-view point tracking as an additional geometric and motion supervision signal for camera-conditioning-only novel-view video diffusion models. Our key finding is that specific attention layers encode strong correspondence cues, where query features attend to key features at geometrically corresponding locations across views and over time, and the misalignment of these correspondences causes motion inconsistency. Based on this observation, we route these features into an auxiliary multi-view tracking head and jointly train the diffusion model with a point-tracking objective. By explicitly strengthening these motion-aware correspondences, MVTrack4Gen improves existing models to better follow the motion in the reference view and maintain cross-view geometric consistency. Across diverse benchmarks, our method achieves state-of-the-art geometric consistency and competitive camera accuracy.
匹配关键词: video understanding
---

[ACADEMIC - ARXIV]
标题: DomainShuttle: Freeform Open Domain Subject-driven Text-to-video Generation
作者: Nan Chen, Yiyang Cai, Rongchang Xie, Junwen Pan, Cheng Chen, Weinan Jia, Zhuowei Chen, Wen Zhou, Zhenbang Sun, Wenhan Luo
链接: https://arxiv.org/abs/2606.26058v1
完整摘要: Open domain subject-driven text-to-video (S2V) generation has drawn significant interest in academia and industry. Open domain S2V mainly involves two scenarios: in-domain, which requires retaining the reference subject features as much as possible, and cross-domain, which preserves the intrinsic features of the subject while allowing subject-irrelevant properties to vary flexibly according to the text prompt. Existing methods primarily focus on maximizing subject fidelity in in-domain scenarios, which limits their editability and adaptability in cross-domain scenarios, such as novel styles, semantic combinations, or domain attributes. In this study, we propose that an ideal S2V method should flexibly shuttle between different domains, achieving strong performance in both in-domain and cross-domain scenarios. To this end, we propose DomainShuttle, which could achieve high fidelity and generative flexibility for open domain video personalization. Specifically, we introduce Domain-MoT, which decouples videos and reference features and introduces the domain-aware AdaLN for domain-specific modeling of reference images. We then introduce the Video-Reference DualRoPE scheme, which places reference image tokens and video tokens in separate RoPE spaces to enable precise subject-level spatial modeling, and Cross-Pair Consistent Loss, which aims to extract intrinsic subject features unaffected by irrelevant features. Extensive experiments demonstrate that DomainShuttle achieves significant performance improvements over existing methods, exhibiting high subject fidelity and generative flexibility across diverse open domain application scenarios.
匹配关键词: video understanding
---

[ACADEMIC - ARXIV]
标题: Learning Robot Visual Navigation in Crowds via Intention-Aware Scene Representations
作者: Han Bao, Bingyi Xia, Hanjing Ye, Yu Zhan, Hao Cheng, Baozhi Jia, Wenjun Xu, Jiankun Wang
链接: https://arxiv.org/abs/2606.26047v1
完整摘要: Robot crowd navigation requires the ability to infer human intentions while accounting for the structural constraints of the environment. Currently, deep reinforcement learning (DRL) provides a promising method for learning navigation policies that understand human intentions. However, most of them rely on limited scene representations, treating pedestrians as simple 2D points and ignoring rich visual cues from both humans and the environment. To address this issue, we introduce iCrowdNav, a novel visual crowd navigation method with intention-aware scene representations, to encode behavioral and structural context from egocentric visual observations. Our method employs two key components: a spatio-temporal encoder for extracting occupancy features of the scene, and Intent-Interact Former (I$^2$ Former), an attention-based module that encodes human poses to infer pedestrians' motion intentions. These features are integrated into a compact state embedding that supports effective DRL policy training. Extensive experiments show that our method achieves superior performance over baselines, and real-world deployment demonstrates vision-based crowd navigation.
匹配关键词: video understanding
---

[ACADEMIC - ARXIV]
标题: Learning Action Priors for Cross-embodiment Robot Manipulation
作者: Dong Jing, Tianqi Zhang, Jiaqi Liu, Jinman Zhao, Zelong Sun, Li Erran Li, Zhiwu Lu, Mingyu Ding
链接: https://arxiv.org/abs/2606.26095v1
完整摘要: Most Vision-Language-Action (VLA) models build on a Vision-Language Model (VLM) backbone by attaching an action module and optimizing the full policy jointly. This design inherits strong visual and linguistic priors from the VLM, but leaves the action module to learn physical motion almost from scratch. As a result, the policy lacks an explicit motion prior, forcing early optimization to simultaneously discover temporal action dynamics and cross-modal alignment, a challenge further amplified in cross-embodiment settings. In this work, we propose to pretrain the action module with motion priors before cross-modal VLA alignment. Specifically, we introduce a two-stage training framework that equips the action module with cross-embodiment temporal motion structure before VLA training begins. In Stage~1, a lightweight flow-matching-based encoder-decoder action module efficiently learns temporal motion structure solely from unconditioned action trajectories, without processing visual or language tokens. In Stage~2, this learned prior is transferred to VLA training through decoder reuse and early-stage latent distillation, aligning visual-language features with the action embedding space while still allowing end-to-end policy refinement. In addition, the trained encoder serves as a compact history compressor, summarizing state-action histories into a single temporal context token for history-aware modeling at negligible cost. Extensive experiments across 13 diverse cross-embodiment tasks on both simulated and real-world platforms validate the effectiveness of our approach. Compared with VLA training without action priors, our model achieves faster convergence, higher success rates, and substantially stronger performance on data-scarce real-world tasks. Moreover, scaling up the action data in Stage~1 yields a more generalizable action prior that directly improves downstream VLA performance.
匹配关键词: temporal consistency
---

[ACADEMIC - ARXIV]
标题: MVTrack4Gen: Multi-View Point Tracking as Geometric Supervision for 4D Video Generation
作者: JoungBin Lee, Jaewoo Jung, Jongmin Lee, Tongmin Kim, Hyunsung Kim, Takuya Narihira, Kazumi Fukuda, Jahyeok Koo, Jisang Han, Yuki Mitsufuji, Seungryong Kim
链接: https://arxiv.org/abs/2606.26087v1
完整摘要: Synthesizing a novel-view video from a monocular reference video along a target camera trajectory requires both geometric consistency and motion fidelity with respect to the reference video. Existing methods based on explicit 3D representations are limited by the accuracy of off-the-shelf reconstruction modules, which often produce inaccurate geometry for dynamic objects in monocular videos. In contrast, camera-conditioning-only methods can achieve high visual quality but often struggle to preserve geometric and motion consistency. In this work, we introduce MVTrack4Gen (Multi-View point Tracking for Novel-View Generation), a motion-aware training framework that leverages multi-view point tracking as an additional geometric and motion supervision signal for camera-conditioning-only novel-view video diffusion models. Our key finding is that specific attention layers encode strong correspondence cues, where query features attend to key features at geometrically corresponding locations across views and over time, and the misalignment of these correspondences causes motion inconsistency. Based on this observation, we route these features into an auxiliary multi-view tracking head and jointly train the diffusion model with a point-tracking objective. By explicitly strengthening these motion-aware correspondences, MVTrack4Gen improves existing models to better follow the motion in the reference view and maintain cross-view geometric consistency. Across diverse benchmarks, our method achieves state-of-the-art geometric consistency and competitive camera accuracy.
匹配关键词: temporal consistency
---

[ACADEMIC - ARXIV]
标题: Neglected Free Lunch from Post-training: Progress Advantage for LLM Agents
作者: Changdae Oh, Wendi Li, Seongheon Park, Samuel Yeh, Tanwi Mallick, Sharon Li
链接: https://arxiv.org/abs/2606.26080v1
完整摘要: Process reward models enable fine-grained, step-level evaluation of LLMs, yet building them for agentic settings remains prohibitively difficult: long-horizon interactions, irreversible actions, and stochastic environment feedback make both human annotation and Monte Carlo estimation infeasible at scale. In this work, we show that reinforcement learning (RL) post-training already provides the ingredients for effective step-level scoring, eliminating the need for dedicated reward model training altogether. Concretely, we derive an implicit advantage under a general stochastic Markov decision process, which we term progress advantage -- log-probability ratio between the RL-trained policy and its reference policy exactly recovers the optimal advantage function. This formulation makes the resulting signal annotation-free, domain-agnostic, and available as a byproduct of the standard RL post-training pipeline. We validate the effectiveness of the progress advantage across three different applications: test-time scaling, uncertainty quantification, and failure attribution on five benchmarks and four model families. Across all settings, it consistently outperforms confidence-based baselines and, despite requiring no task-specific training, surpasses dedicated trained reward models. We complement these results with deeper analyses on characteristics of progress advantage, offering practical guidance for adoption in real-world agentic systems.
匹配关键词: temporal consistency
---

[ACADEMIC - ARXIV]
标题: Model Forensics: Investigating Whether Concerning Behavior Reflects Misalignment
作者: Aditya Singh, Gerson Kroiz, Senthooran Rajamanoharan, Neel Nanda
链接: https://arxiv.org/abs/2606.26071v1
完整摘要: A central goal of safety research is determining whether a model is misaligned. Prior work has largely focused on detecting concerning behavior. But behavior alone does not establish misalignment: a concerning action can arise from benign causes such as confusion. This motivates model forensics: investigating whether the action was driven by malign intent. In this paper, we propose a baseline protocol for model forensics consisting of two steps, iterated as needed. First, we read the chain of thought (CoT) to generate hypotheses about what drives model behavior. Second, we make edits to the prompt or environment to test these hypotheses. While the CoT is not always faithful, it is a rich source of unsupervised insight that can guide the collection of more rigorous evidence. To evaluate our protocol, we create a suite of six agentic environments where models exhibit concerning behavior, and apply it to each. We establish that Kimi K2 Thinking takes shortcuts due to a genuine disposition towards low-effort actions, by showing this hypothesis successfully predicts its behavior. Through counterfactual experiments, we show DeepSeek R1 deceives out of a desire to be consistent with a previous instance of itself. Our methods nonetheless leave significant room for refinement. For example, when we test whether Kimi K2 Thinking believes it is violating user intent, we find no evidence of such a belief, but without positive controls we cannot confirm our tests would detect it. Overall, we find our simple protocol provides a strong baseline that we hope future work will improve upon. More broadly, our work is a concrete step in developing the growing field of model forensics.
匹配关键词: temporal consistency
---

[ACADEMIC - ARXIV]
标题: When Certainty Is an Artifact: Keyword Lexicon Blindness and the (Mis)Measurement of Rhetorical Stance
作者: Bo Chen
链接: https://arxiv.org/abs/2606.26062v1
完整摘要: Can a statistically significant, large-effect-size finding in computational social science be entirely an artifact of the measurement instrument? We present a case where the answer appears to be yes. Analyzing 85 interviews across four public intellectuals (2016--2026), we find a robust negative-affect/emphatic-certainty lexical co-occurrence pattern under keyword-based scoring ($r = 0.72$--$0.93$, $p < 0.01$ for all four speakers). Replacing keyword counting with LLM-based zero-shot semantic classification on the complete diarized corpus (32,625 sentences) dramatically reduces this correlation: Dalio's $r = 0.851$ drops to $r = 0.206$, with two speakers showing negative $r(\text{neg}, \text{emphatic})$ and one showing null. In contrast, the LLM reveals a strong negative-hedging coupling across speakers -- Rogoff's $r(\text{neg}, \text{hedged}) = 0.875$ ($p = 0.001$) and Zeihan's $r(\text{neg}, \text{hedged}) = 0.722$ ($p = 0.008$) -- consistent with the conventional expectation that pessimistic discourse attracts hedging, not certainty. Sentence-level error analysis traces this discrepancy to three structural failure modes in keyword lexicons -- syntactic blindness, polysemy blindness, and categorical absence -- illustrated through cases where keyword counting inverts semantic meaning (e.g., ''never absolutely totally confident'' scored as high-certainty). We argue that keyword lexicons measure a universal lexical co-occurrence tendency -- negative discourse naturally attracts emphatic vocabulary -- that is orthogonal to, and can systematically invert, rhetorical stance. Treating keyword counts as measurements of epistemic certainty is a category error: a finding that appears to be about a speaker's psychology may be entirely about the counting of words.
匹配关键词: temporal consistency
---

[ACADEMIC - ARXIV]
标题: Physics Question Scene Graph: Fine-grained Evaluation of Physical Plausibility in Text-to-Video Generation
作者: Atin Pothiraj, Jaemin Cho, Yue Zhang, Elias Stengel-Eskin, Mohit Bansal
链接: https://arxiv.org/abs/2606.25306v1
完整摘要: Video generation models are increasingly capable of producing realistic videos, but they still struggle to generate videos that follow basic physical laws. Compounding this is a lack of reliable granular evaluation methods for localizing and specifying physical law violations in videos. We address this by introducing Physics Question Scene Graph (PQSG), a hierarchical question-based evaluation pipeline. PQSG evaluates generated videos by checking their faithfulness to a prompt across objects, actions, and adherence to physical laws using a graph-based hierarchy of questions generated by a vision-language model (VLM), guided by high-quality in-context examples. By representing questions as a graph, PQSG introduces logical dependencies within questions, ensuring that each query is contextually valid. Moreover, PQSG provides granular assessments of which qualities of the video violate physical plausibility constraints. We validate PQSG by creating FinePhyEval, a dataset with physics-based prompts and corresponding generated videos from diverse state-of-the-art video generation models (Sora 2, Veo 3, and Wan 2.1), with each video annotated across multiple categories by humans. Using FinePhyEval, we measure the correlation between PQSG's fine-grained scores and human judgments, showing higher overall correlations than prior work. We also find that PQSG ranks closed-source models higher than Wan 2.1 on physical realism. Lastly, we show that the annotations we provide in FinePhyEval can also be used for subtask evaluation: we benchmark two strong VLMs on generating and answering questions, finding that while models can create human-like questions, they still fall short of human performance in answering them.
匹配关键词: Sora
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
标题: Learning Action Priors for Cross-embodiment Robot Manipulation
作者: Dong Jing, Tianqi Zhang, Jiaqi Liu, Jinman Zhao, Zelong Sun, Li Erran Li, Zhiwu Lu, Mingyu Ding
链接: https://arxiv.org/abs/2606.26095v1
完整摘要: Most Vision-Language-Action (VLA) models build on a Vision-Language Model (VLM) backbone by attaching an action module and optimizing the full policy jointly. This design inherits strong visual and linguistic priors from the VLM, but leaves the action module to learn physical motion almost from scratch. As a result, the policy lacks an explicit motion prior, forcing early optimization to simultaneously discover temporal action dynamics and cross-modal alignment, a challenge further amplified in cross-embodiment settings. In this work, we propose to pretrain the action module with motion priors before cross-modal VLA alignment. Specifically, we introduce a two-stage training framework that equips the action module with cross-embodiment temporal motion structure before VLA training begins. In Stage~1, a lightweight flow-matching-based encoder-decoder action module efficiently learns temporal motion structure solely from unconditioned action trajectories, without processing visual or language tokens. In Stage~2, this learned prior is transferred to VLA training through decoder reuse and early-stage latent distillation, aligning visual-language features with the action embedding space while still allowing end-to-end policy refinement. In addition, the trained encoder serves as a compact history compressor, summarizing state-action histories into a single temporal context token for history-aware modeling at negligible cost. Extensive experiments across 13 diverse cross-embodiment tasks on both simulated and real-world platforms validate the effectiveness of our approach. Compared with VLA training without action priors, our model achieves faster convergence, higher success rates, and substantially stronger performance on data-scarce real-world tasks. Moreover, scaling up the action data in Stage~1 yields a more generalizable action prior that directly improves downstream VLA performance.
匹配关键词: video foundation model
---

[ACADEMIC - ARXIV]
标题: RevengeBench: Reverse Engineering Code-Space Policies from Behavioral Experiments
作者: Babak Rahmani, Sebastian Dziadzio, Joschka Strüber, Sergio Hernández-Gutiérrez, Matthias Bethge
链接: https://arxiv.org/abs/2606.26094v1
完整摘要: For most of scientific history, researchers studying behavior could only infer hidden mechanisms from outward actions: an inverse problem that becomes more tractable when observation is augmented by targeted intervention. We pose a computational analogue: given only behavioral traces of an agent in a game environment, can a learner reconstruct the underlying decision program as executable code, and how much does this reconstruction improve with the ability to design controlled experiments? We introduce RevengeBench, a benchmark of 75 LLM generated, Elo-calibrated policies across five game environments, drawn from CodeClash tournament trajectories. The learner observes the hidden target policy play against sampled opponents and designs behavioral probes in the form of custom opponent policies that elicit informative behavior. It then submits an executable hypothesis, which is evaluated using continuous action-distance metrics. We further validate that recovered code carries informative signal in downstream player-versus-player tournaments. Across twelve frontier LLMs, recovery quality varies substantially (34 to 72% of initial distance closed), with reconstructed policies yielding measurable competitive advantage, particularly for weaker models that otherwise struggle to design effective counter-strategies. Our benchmark positions behavioral recovery of programmatic policies as a tractable inverse problem in code-space, opening a path to opponent modeling, policy interpretability, and the broader question of inferring latent mechanisms from observations.
匹配关键词: video foundation model
---

[ACADEMIC - ARXIV]
标题: ForceBand: Learning Forceful Manipulation with sEMG
作者: Botao He, Zhi Wang, Linna Kuang, Ishaan Ghosh, Jitendra Malik, Cornelia Fermuller, Tingfan Wu, Jiayuan Mao, Ruoshi Liu, Haozhi Qi, Yiannis Aloimonos
链接: https://arxiv.org/abs/2606.26093v1
完整摘要: Human demonstrations are a scalable data source for learning robot manipulation policies. However, common sources of human demonstration data, such as motion-capture trajectories and internet videos, capture mostly motion and appearance while missing the contact forces that are critical for force-sensitive manipulation. In this paper, we introduce ForceBand, a low-cost wrist-worn sEMG system that turns human muscle activity into force-enriched demonstrations. We first collect a 10-hour multimodal dataset containing egocentric video, sEMG, IMU, and fingertip force measurements across diverse actions and objects. Using this dataset, we pre-train an EMG2Force model that predicts per-finger forces from sEMG and IMU signals. After a short user-specific calibration, users can collect target-task demonstrations using only ForceBand and video; EMG2Force then labels these demonstrations with per-finger force traces, producing force-augmented demonstrations for robot policy learning. Experiments show that ForceBand recovers fine-grained fingertip interactions with over 50% lower force prediction error than vision-based baselines and achieves an 87% success rate on pick, squeeze, and place tasks that require object-specific force control across objects with diverse shapes, sizes, and weights. Project website: https://forceband-emg.github.io
匹配关键词: video foundation model
---

[ACADEMIC - ARXIV]
标题: TryOnCrafter: Unleashing Camera Trajectories for Realistic Video Virtual Try-on via a Renderable 4D Try-on Proxy
作者: Hao Sun, Hao Yan, Mengting Chen, Quanjian Song, Yu Li, Juan Cao, Jinsong Lan, Xiaoyong Zhu, Bo Zheng, Sheng Tang
链接: https://arxiv.org/abs/2606.26092v1
完整摘要: While Video Virtual Try-on (VVT) has achieved remarkable progress in synthesizing realistic garment overlays on dynamic subjects, existing paradigms remains fundamentally constrained by a passive dependency on source camera trajectories, failing to accommodate the requisite interactive freedom for omnidirectional viewpoint exploration. To address this limitation, we define a pioneering research frontier: Camera-controllable Video Virtual Try-on (CaM-VVT). Unlike conventional VVT, CaM-VVT not only necessitates viewpoint-agnostic texture hallucination but also strict structural synchronization between non-rigid human dynamics and background contexts under arbitrary, unconstrained camera movements. To tackle these challenges, we present TryOnCrafter, the first unified DiT-based framework specifically architected for the CaM-VVT task. Departing from implicit pixel-space manipulation, we introduce a Renderable 4D Try-on Proxy that explicitly decouples the human subject from the environment. This is achieved by distilling high-fidelity 2D try-on priors into a clothed 3DGS-based avatar, which is subsequently animated via SMPL-X sequences and metric-aligned into a reconstructed background point cloud. This proxy establishes a robust structural foundation with superior texture density and motion integrity. Our Proxy-Anchored Video DiT leverages this robust structural foundation as a primary geometric anchor, ensuring that the synthesized photorealistic videos are strictly constrained by prescribed trajectories and physically plausible deformations. Benefiting from the inherent editability of the 4D proxy, TryOnCrafter facilitates diverse downstream applications, including human relocalization, ``bullet time'' effects, and $360$-degree orbital viewing.
匹配关键词: video foundation model
---

[ACADEMIC - ARXIV]
标题: On-Policy Self-Distillation with Sampled Demonstrations Reduces Output Diversity
作者: Andrei Liviu Nicolicioiu, Mohammad Pezeshki, Aaron Courville
链接: https://arxiv.org/abs/2606.26091v1
完整摘要: On-policy self-distillation achieves strong pass@1 accuracy by using a single model as both teacher and student, with the teacher conditioned on a correct demonstration to provide dense token-level feedback. We show that this could come at a hidden cost: rollout diversity decreases and pass@k curves flatten (i.e., generating more rollouts fails to improve accuracy). We trace this to compounding biases in the design of self-distillation with sampled demonstrations. The teacher scores each student rollout while conditioned on a sampled correct rollout, channeling its feedback through the model's own biases. We theoretically analyze the optimal self-distillation policy and show that it tilts the base distribution by a pointwise conditional mutual information score between the student's rollout and the correct rollout used as context. Unlike the ideal optimal on-policy reinforcement learning (RL), which preserves probability ratios among equally correct rollouts, self-distillation can amplify existing probability gaps, concentrating mass on already-dominant modes. On a controlled graph path-finding task and science question-answering benchmarks, self-distilled models match or exceed RL on average performance but exhibit substantially lower functional and semantic diversity, failing on out-of-distribution settings that require diverse strategies.
匹配关键词: video foundation model
---

[ACADEMIC - ARXIV]
标题: RevengeBench: Reverse Engineering Code-Space Policies from Behavioral Experiments
作者: Babak Rahmani, Sebastian Dziadzio, Joschka Strüber, Sergio Hernández-Gutiérrez, Matthias Bethge
链接: https://arxiv.org/abs/2606.26094v1
完整摘要: For most of scientific history, researchers studying behavior could only infer hidden mechanisms from outward actions: an inverse problem that becomes more tractable when observation is augmented by targeted intervention. We pose a computational analogue: given only behavioral traces of an agent in a game environment, can a learner reconstruct the underlying decision program as executable code, and how much does this reconstruction improve with the ability to design controlled experiments? We introduce RevengeBench, a benchmark of 75 LLM generated, Elo-calibrated policies across five game environments, drawn from CodeClash tournament trajectories. The learner observes the hidden target policy play against sampled opponents and designs behavioral probes in the form of custom opponent policies that elicit informative behavior. It then submits an executable hypothesis, which is evaluated using continuous action-distance metrics. We further validate that recovered code carries informative signal in downstream player-versus-player tournaments. Across twelve frontier LLMs, recovery quality varies substantially (34 to 72% of initial distance closed), with reconstructed policies yielding measurable competitive advantage, particularly for weaker models that otherwise struggle to design effective counter-strategies. Our benchmark positions behavioral recovery of programmatic policies as a tractable inverse problem in code-space, opening a path to opponent modeling, policy interpretability, and the broader question of inferring latent mechanisms from observations.
匹配关键词: video LLM
---

[ACADEMIC - ARXIV]
标题: ForceBand: Learning Forceful Manipulation with sEMG
作者: Botao He, Zhi Wang, Linna Kuang, Ishaan Ghosh, Jitendra Malik, Cornelia Fermuller, Tingfan Wu, Jiayuan Mao, Ruoshi Liu, Haozhi Qi, Yiannis Aloimonos
链接: https://arxiv.org/abs/2606.26093v1
完整摘要: Human demonstrations are a scalable data source for learning robot manipulation policies. However, common sources of human demonstration data, such as motion-capture trajectories and internet videos, capture mostly motion and appearance while missing the contact forces that are critical for force-sensitive manipulation. In this paper, we introduce ForceBand, a low-cost wrist-worn sEMG system that turns human muscle activity into force-enriched demonstrations. We first collect a 10-hour multimodal dataset containing egocentric video, sEMG, IMU, and fingertip force measurements across diverse actions and objects. Using this dataset, we pre-train an EMG2Force model that predicts per-finger forces from sEMG and IMU signals. After a short user-specific calibration, users can collect target-task demonstrations using only ForceBand and video; EMG2Force then labels these demonstrations with per-finger force traces, producing force-augmented demonstrations for robot policy learning. Experiments show that ForceBand recovers fine-grained fingertip interactions with over 50% lower force prediction error than vision-based baselines and achieves an 87% success rate on pick, squeeze, and place tasks that require object-specific force control across objects with diverse shapes, sizes, and weights. Project website: https://forceband-emg.github.io
匹配关键词: video LLM
---

[ACADEMIC - ARXIV]
标题: TryOnCrafter: Unleashing Camera Trajectories for Realistic Video Virtual Try-on via a Renderable 4D Try-on Proxy
作者: Hao Sun, Hao Yan, Mengting Chen, Quanjian Song, Yu Li, Juan Cao, Jinsong Lan, Xiaoyong Zhu, Bo Zheng, Sheng Tang
链接: https://arxiv.org/abs/2606.26092v1
完整摘要: While Video Virtual Try-on (VVT) has achieved remarkable progress in synthesizing realistic garment overlays on dynamic subjects, existing paradigms remains fundamentally constrained by a passive dependency on source camera trajectories, failing to accommodate the requisite interactive freedom for omnidirectional viewpoint exploration. To address this limitation, we define a pioneering research frontier: Camera-controllable Video Virtual Try-on (CaM-VVT). Unlike conventional VVT, CaM-VVT not only necessitates viewpoint-agnostic texture hallucination but also strict structural synchronization between non-rigid human dynamics and background contexts under arbitrary, unconstrained camera movements. To tackle these challenges, we present TryOnCrafter, the first unified DiT-based framework specifically architected for the CaM-VVT task. Departing from implicit pixel-space manipulation, we introduce a Renderable 4D Try-on Proxy that explicitly decouples the human subject from the environment. This is achieved by distilling high-fidelity 2D try-on priors into a clothed 3DGS-based avatar, which is subsequently animated via SMPL-X sequences and metric-aligned into a reconstructed background point cloud. This proxy establishes a robust structural foundation with superior texture density and motion integrity. Our Proxy-Anchored Video DiT leverages this robust structural foundation as a primary geometric anchor, ensuring that the synthesized photorealistic videos are strictly constrained by prescribed trajectories and physically plausible deformations. Benefiting from the inherent editability of the 4D proxy, TryOnCrafter facilitates diverse downstream applications, including human relocalization, ``bullet time'' effects, and $360$-degree orbital viewing.
匹配关键词: video LLM
---

[ACADEMIC - ARXIV]
标题: MVTrack4Gen: Multi-View Point Tracking as Geometric Supervision for 4D Video Generation
作者: JoungBin Lee, Jaewoo Jung, Jongmin Lee, Tongmin Kim, Hyunsung Kim, Takuya Narihira, Kazumi Fukuda, Jahyeok Koo, Jisang Han, Yuki Mitsufuji, Seungryong Kim
链接: https://arxiv.org/abs/2606.26087v1
完整摘要: Synthesizing a novel-view video from a monocular reference video along a target camera trajectory requires both geometric consistency and motion fidelity with respect to the reference video. Existing methods based on explicit 3D representations are limited by the accuracy of off-the-shelf reconstruction modules, which often produce inaccurate geometry for dynamic objects in monocular videos. In contrast, camera-conditioning-only methods can achieve high visual quality but often struggle to preserve geometric and motion consistency. In this work, we introduce MVTrack4Gen (Multi-View point Tracking for Novel-View Generation), a motion-aware training framework that leverages multi-view point tracking as an additional geometric and motion supervision signal for camera-conditioning-only novel-view video diffusion models. Our key finding is that specific attention layers encode strong correspondence cues, where query features attend to key features at geometrically corresponding locations across views and over time, and the misalignment of these correspondences causes motion inconsistency. Based on this observation, we route these features into an auxiliary multi-view tracking head and jointly train the diffusion model with a point-tracking objective. By explicitly strengthening these motion-aware correspondences, MVTrack4Gen improves existing models to better follow the motion in the reference view and maintain cross-view geometric consistency. Across diverse benchmarks, our method achieves state-of-the-art geometric consistency and competitive camera accuracy.
匹配关键词: video LLM
---

[ACADEMIC - ARXIV]
标题: Neglected Free Lunch from Post-training: Progress Advantage for LLM Agents
作者: Changdae Oh, Wendi Li, Seongheon Park, Samuel Yeh, Tanwi Mallick, Sharon Li
链接: https://arxiv.org/abs/2606.26080v1
完整摘要: Process reward models enable fine-grained, step-level evaluation of LLMs, yet building them for agentic settings remains prohibitively difficult: long-horizon interactions, irreversible actions, and stochastic environment feedback make both human annotation and Monte Carlo estimation infeasible at scale. In this work, we show that reinforcement learning (RL) post-training already provides the ingredients for effective step-level scoring, eliminating the need for dedicated reward model training altogether. Concretely, we derive an implicit advantage under a general stochastic Markov decision process, which we term progress advantage -- log-probability ratio between the RL-trained policy and its reference policy exactly recovers the optimal advantage function. This formulation makes the resulting signal annotation-free, domain-agnostic, and available as a byproduct of the standard RL post-training pipeline. We validate the effectiveness of the progress advantage across three different applications: test-time scaling, uncertainty quantification, and failure attribution on five benchmarks and four model families. Across all settings, it consistently outperforms confidence-based baselines and, despite requiring no task-specific training, surpasses dedicated trained reward models. We complement these results with deeper analyses on characteristics of progress advantage, offering practical guidance for adoption in real-world agentic systems.
匹配关键词: video LLM
---

[ACADEMIC - ARXIV]
标题: Why Multi-Step Tool-Use Reinforcement Learning Collapses and How Supervisory Signals Fix It
作者: Yupu Hao, Zhuoran Jin, Huanxuan Liao, Kang Liu, Jun Zhao
链接: https://arxiv.org/abs/2606.26027v1
完整摘要: Tool use enables large language models (LLMs) to perform complex tasks, and recent agentic reinforcement learning (RL) methods show promise for enhancing model capabilities. However, RL alone often leads to instability or limited gains in tool-use tasks. In our experiments, some models exhibit catastrophic collapse, where performance abruptly drops and tool-invocation structures fail. The analysis reveals that these failures stem from unexpected probability spikes in specific control tokens, disrupting structured execution, yet the underlying tool-use capability remains intact, merely obscured by specific formats. To address this, we systematically investigate a diverse set of supervisory signals, including off-policy supervision, hint-based guidance, erroneous example supervision, and others, applied under both synchronous and interleaved training schemes. We find that interleaving supervised fine-tuning (SFT) with RL substantially improves stability, but exhibits degraded performance under format and content out-of-distribution (OOD) evaluation. We also analyze the impact of learning rates and generalization across settings. These results highlight the importance of understanding RL failures and demonstrate how diverse supervisory signals can guide exploratory learning, enabling robust training of LLMs for complex, multi-step tool-use tasks. Our Code is available at https://github.com/hypasd-art/Tool-RL-Box.
匹配关键词: multi-agent
---

[ACADEMIC - ARXIV]
标题: Hierarchical Reinforcement Learning for Neural Network Compression (HiReLC): Pruning and Quantization
作者: Kamar Hibatallah Baghdadi, Kawther Guoual Belhamidi, Sara Belhadj, Aissa Boulmerka, Nadir Farhi
链接: https://arxiv.org/abs/2606.26002v1
完整摘要: We present HiReLC, a hierarchical ensemble-reinforcement learning framework for automated joint quantization and structured pruning of deep neural networks. The framework decomposes the compression search across two levels of abstraction: low-level agents (LLAs) operate independently per block, selecting per-kernel configurations over a multi-discrete action space spanning bitwidth, pruning keep-ratio, quantization type, and granularity, while high-level agents (HLAs) coordinate global budget allocation via ensemble voting guided by Fisher Information-based sensitivity estimates. To mitigate the computational cost of policy evaluation, an iterative active learning loop interleaves surrogate-guided RL optimization with post-compression fine-tuning, using a lightweight MLP surrogate to amortize expensive evaluations and a logit-MSE proxy during cold-start. The surrogate is used for reward shaping rather than as a replacement for final post-compression evaluation. The controller is architecture-agnostic by design, with a modular layer abstraction decoupling the RL environment from the underlying network topology. Experiments across Vision Transformer and CNN benchmarks demonstrate effective parameter-storage compression ratios of 5.99 - 6.72$\times$ with a 3.83 % gain in one setting and 0.55 - 5.62 % accuracy drops elsewhere, supporting hierarchical policy decomposition and sensitivity-aware guidance as practical design choices for joint neural network compression.
匹配关键词: multi-agent
---

[ACADEMIC - ARXIV]
标题: Multi-Agent Goal Recognition with Team- and Goal-Conditioned Reinforcement Learning and Factorized Branch-and-Bound
作者: Thiago Thomas, Gabriel de Oliveira Ramos, Felipe Meneguzzi
链接: https://arxiv.org/abs/2606.25978v1
完整摘要: Multi-agent goal recognition asks an observer to jointly infer which agents act together and what each team is trying to achieve, so the hypothesis space grows combinatorially with the number of team partitions and goals per team. Real applications such as drone surveillance and collaborative robotics expose only the agents' trajectory, which forces the observer to rank team-goal hypotheses from behavior alone. Multi-Agent Goal Recognition with Branch-and-Bound (MAGR-BB) addresses this setting with a shared team- and goal-conditioned policy used as the scoring model inside a factorized branch-and-bound search. On a controlled multi-agent Blocksworld benchmark, MAGR-BB returns the same top-ranked hypothesis as exhaustive search throughout the trajectory while cutting hypothesis materialization by orders of magnitude and reducing cumulative recognition runtime substantially.
匹配关键词: multi-agent
---

[ACADEMIC - ARXIV]
标题: Agentic System as Compressor: Quantifying System Intelligence in Bits
作者: Zihan Qin, Hongrui Zhang
链接: https://arxiv.org/abs/2606.25960v1
完整摘要: Large language models are turning from isolated predictors into agentic systems: they call tools, retrieve evidence, obey environment constraints, use verifiers, and complete tasks through search and multi-turn interaction. We adopts an analytical viewpoint based on "compression is intelligence": under a fixed task distribution, interface, and compute budget, a stronger agentic system lets a target object be reconstructed with fewer bits. We operationalize the measure with arithmetic coding, seed coding, and a fallback, and evaluate it in five settings: reversed text, chess moves, protein sequences, retrieval-augmented question answering, and semantic story compression; in all of them agentic components reduce codelength. These small, controlled experiments cover component types typical of real agentic systems, show that codelength can analyze how components, observers, and budgets change residual uncertainty, and offer guidance for evaluating real agent systems.
匹配关键词: multi-agent
---

[ACADEMIC - ARXIV]
标题: Semantic Consistency Policy Optimization for Reinforcement Learning of LLM Agents
作者: Peng Xu, Sijia Chen, Junzhuo Li, Xuming Hu
链接: https://arxiv.org/abs/2606.25852v1
完整摘要: Group-based reinforcement learning effectively post-trains LLM agents for long-horizon, sparse-reward tasks by deriving step-level credit from trajectory outcomes. However, this ties a step's credit to its rollout's final outcome: semantically near-identical intermediate steps receive opposite credit depending on whether their trajectory eventually succeeded or failed. Such semantic credit inconsistency sends conflicting gradients to similar actions and wastes the partially-correct progress inside failed rollouts. Motivated by this, we propose Semantic Consistency Policy Optimization (SCPO), a value-free reward-shaping method that mitigates this inconsistency by recovering step-level credit from successful siblings in the same rollout group. Concretely, SCPO scores each failed step against a successful sibling and adds positive step-level credit for new progress along that sibling. On ALFWorld and WebShop, SCPO matches or exceeds strong group-based baselines, reaching 93.7+/-4.1 percent success on ALFWorld and 74.8+/-2.0 percent on WebShop at 1.5B parameters, with gains concentrated on the hardest multi-step tasks.
匹配关键词: multi-agent
---

[ACADEMIC - ARXIV]
标题: RevengeBench: Reverse Engineering Code-Space Policies from Behavioral Experiments
作者: Babak Rahmani, Sebastian Dziadzio, Joschka Strüber, Sergio Hernández-Gutiérrez, Matthias Bethge
链接: https://arxiv.org/abs/2606.26094v1
完整摘要: For most of scientific history, researchers studying behavior could only infer hidden mechanisms from outward actions: an inverse problem that becomes more tractable when observation is augmented by targeted intervention. We pose a computational analogue: given only behavioral traces of an agent in a game environment, can a learner reconstruct the underlying decision program as executable code, and how much does this reconstruction improve with the ability to design controlled experiments? We introduce RevengeBench, a benchmark of 75 LLM generated, Elo-calibrated policies across five game environments, drawn from CodeClash tournament trajectories. The learner observes the hidden target policy play against sampled opponents and designs behavioral probes in the form of custom opponent policies that elicit informative behavior. It then submits an executable hypothesis, which is evaluated using continuous action-distance metrics. We further validate that recovered code carries informative signal in downstream player-versus-player tournaments. Across twelve frontier LLMs, recovery quality varies substantially (34 to 72% of initial distance closed), with reconstructed policies yielding measurable competitive advantage, particularly for weaker models that otherwise struggle to design effective counter-strategies. Our benchmark positions behavioral recovery of programmatic policies as a tractable inverse problem in code-space, opening a path to opponent modeling, policy interpretability, and the broader question of inferring latent mechanisms from observations.
匹配关键词: agent collaboration
---

[ACADEMIC - ARXIV]
标题: Neglected Free Lunch from Post-training: Progress Advantage for LLM Agents
作者: Changdae Oh, Wendi Li, Seongheon Park, Samuel Yeh, Tanwi Mallick, Sharon Li
链接: https://arxiv.org/abs/2606.26080v1
完整摘要: Process reward models enable fine-grained, step-level evaluation of LLMs, yet building them for agentic settings remains prohibitively difficult: long-horizon interactions, irreversible actions, and stochastic environment feedback make both human annotation and Monte Carlo estimation infeasible at scale. In this work, we show that reinforcement learning (RL) post-training already provides the ingredients for effective step-level scoring, eliminating the need for dedicated reward model training altogether. Concretely, we derive an implicit advantage under a general stochastic Markov decision process, which we term progress advantage -- log-probability ratio between the RL-trained policy and its reference policy exactly recovers the optimal advantage function. This formulation makes the resulting signal annotation-free, domain-agnostic, and available as a byproduct of the standard RL post-training pipeline. We validate the effectiveness of the progress advantage across three different applications: test-time scaling, uncertainty quantification, and failure attribution on five benchmarks and four model families. Across all settings, it consistently outperforms confidence-based baselines and, despite requiring no task-specific training, surpasses dedicated trained reward models. We complement these results with deeper analyses on characteristics of progress advantage, offering practical guidance for adoption in real-world agentic systems.
匹配关键词: agent collaboration
---

[ACADEMIC - ARXIV]
标题: Model Forensics: Investigating Whether Concerning Behavior Reflects Misalignment
作者: Aditya Singh, Gerson Kroiz, Senthooran Rajamanoharan, Neel Nanda
链接: https://arxiv.org/abs/2606.26071v1
完整摘要: A central goal of safety research is determining whether a model is misaligned. Prior work has largely focused on detecting concerning behavior. But behavior alone does not establish misalignment: a concerning action can arise from benign causes such as confusion. This motivates model forensics: investigating whether the action was driven by malign intent. In this paper, we propose a baseline protocol for model forensics consisting of two steps, iterated as needed. First, we read the chain of thought (CoT) to generate hypotheses about what drives model behavior. Second, we make edits to the prompt or environment to test these hypotheses. While the CoT is not always faithful, it is a rich source of unsupervised insight that can guide the collection of more rigorous evidence. To evaluate our protocol, we create a suite of six agentic environments where models exhibit concerning behavior, and apply it to each. We establish that Kimi K2 Thinking takes shortcuts due to a genuine disposition towards low-effort actions, by showing this hypothesis successfully predicts its behavior. Through counterfactual experiments, we show DeepSeek R1 deceives out of a desire to be consistent with a previous instance of itself. Our methods nonetheless leave significant room for refinement. For example, when we test whether Kimi K2 Thinking believes it is violating user intent, we find no evidence of such a belief, but without positive controls we cannot confirm our tests would detect it. Overall, we find our simple protocol provides a strong baseline that we hope future work will improve upon. More broadly, our work is a concrete step in developing the growing field of model forensics.
匹配关键词: agent collaboration
---

[ACADEMIC - ARXIV]
标题: The Unfireable Safety Kernel: Execution-Time AI Alignment for AI Agents and Other Escapable AI Systems
作者: Seth Dobrin, Łukasz Chmiel
链接: https://arxiv.org/abs/2606.26057v1
完整摘要: AI agents are granted access to tools, APIs, and other infrastructure, making them active principals in those systems. The dominant approach places controls inside the agent's own runtime: system prompts, output filters, and guardrail libraries. Any control in the agent's address space is reachable by inputs that influence it; this generalizes to any AI system with sufficient reach into its own runtime, a class we term escapable AI systems. We identify four properties that an authorization mechanism must satisfy for architectural control rather than for cooperative requests: process separation, pre-action enforcement on a structurally only path, fail-closed at both the request and system levels, and externalized signed evidence verifiable outside the controlled system's trust boundary. We position this layer as execution-time AI alignment, complementing training-time alignment (RLHF, Constitutional AI) and inference-time alignment. We present the Unfireable Safety Kernel, a Rust reference implementation realizing all four. Its fail-closed invariant is machine-checked at two levels: an SMT theorem (Z3) and an exhaustive bounded-model-checking proof of the production decision function (Kani, 4/4 harnesses). A Python-to-Rust migration was gated on byte-equivalence (1000/1000 fixtures; 17/17 adversarial classes). We evaluate the kernel governing a live, escapable AI system, a deterministic, self-improving world model, against an escape-seeking adversary driving its real self-modification seam: across 1,000 self-modifications, all 704 attempts on the safety-critical core are refused, with no escape; a further 300, under the operator kill switch, are also refused. A separate campaign of 6,240 authorization round-trips had no successful bypass. Against 3 contemporary systems claiming the agent control plane, the agent invokes control; here, it lacks that choice.
匹配关键词: agent collaboration
---

[ACADEMIC - ARXIV]
标题: AI translation of literary texts is "fine", but readers still prefer human translations
作者: Yves Ferstler, Adam Podoxin, Ty Brassington, Roman Grundkiewicz, Maite Taboada, Marzena Karpinska
链接: https://arxiv.org/abs/2606.26040v1
完整摘要: AI translation of literary works is increasingly common. While the content may be rendered adequately, we do not know enough about how readers experience it in terms of immersiveness and literary effect, aspects poorly captured by automatic machine translation metrics or human evaluation targeting fluency and adequacy. We ask 15 avid readers to compare recently published human translations (HT) to machine translations (MT) generated with an agentic large language model (LLM)-based pipeline, for 15 recent novels in French, Polish, and Japanese and translated into English. Readers evaluated approximately 8K-word excerpts in two conditions: immersive reading of the whole excerpt (30 comparisons) and close reading of 386 aligned HT-MT chunk pairs (772 comparisons), with two readers per book and in alternating order of presentation. Overall, readers find MT "fine", but prefer HT (slightly at excerpt-level 19/30, more clearly at chunk-level 522/772) for its ease, clarity, and immersive nature. Readers' highlights show that MT's quality varies more within one book than HT's does. Crucially, readers cannot reliably tell the two apart (17/30 guess correctly) and tend to prefer the version they believe to be human. Automatic metrics, including LLM-as-a-judge approaches, fail to recover reader preferences and favor MT. We release LAIT (Literary AI Translation), a reader-centered evaluation dataset with 1K reader comments, 2K judgments and preference ratings, and 7.2K span-level annotations, along with our evaluation protocol and supporting interface.
匹配关键词: agent collaboration
---

[ACADEMIC - ARXIV]
标题: RevengeBench: Reverse Engineering Code-Space Policies from Behavioral Experiments
作者: Babak Rahmani, Sebastian Dziadzio, Joschka Strüber, Sergio Hernández-Gutiérrez, Matthias Bethge
链接: https://arxiv.org/abs/2606.26094v1
完整摘要: For most of scientific history, researchers studying behavior could only infer hidden mechanisms from outward actions: an inverse problem that becomes more tractable when observation is augmented by targeted intervention. We pose a computational analogue: given only behavioral traces of an agent in a game environment, can a learner reconstruct the underlying decision program as executable code, and how much does this reconstruction improve with the ability to design controlled experiments? We introduce RevengeBench, a benchmark of 75 LLM generated, Elo-calibrated policies across five game environments, drawn from CodeClash tournament trajectories. The learner observes the hidden target policy play against sampled opponents and designs behavioral probes in the form of custom opponent policies that elicit informative behavior. It then submits an executable hypothesis, which is evaluated using continuous action-distance metrics. We further validate that recovered code carries informative signal in downstream player-versus-player tournaments. Across twelve frontier LLMs, recovery quality varies substantially (34 to 72% of initial distance closed), with reconstructed policies yielding measurable competitive advantage, particularly for weaker models that otherwise struggle to design effective counter-strategies. Our benchmark positions behavioral recovery of programmatic policies as a tractable inverse problem in code-space, opening a path to opponent modeling, policy interpretability, and the broader question of inferring latent mechanisms from observations.
匹配关键词: agent coordination
---

[ACADEMIC - ARXIV]
标题: Neglected Free Lunch from Post-training: Progress Advantage for LLM Agents
作者: Changdae Oh, Wendi Li, Seongheon Park, Samuel Yeh, Tanwi Mallick, Sharon Li
链接: https://arxiv.org/abs/2606.26080v1
完整摘要: Process reward models enable fine-grained, step-level evaluation of LLMs, yet building them for agentic settings remains prohibitively difficult: long-horizon interactions, irreversible actions, and stochastic environment feedback make both human annotation and Monte Carlo estimation infeasible at scale. In this work, we show that reinforcement learning (RL) post-training already provides the ingredients for effective step-level scoring, eliminating the need for dedicated reward model training altogether. Concretely, we derive an implicit advantage under a general stochastic Markov decision process, which we term progress advantage -- log-probability ratio between the RL-trained policy and its reference policy exactly recovers the optimal advantage function. This formulation makes the resulting signal annotation-free, domain-agnostic, and available as a byproduct of the standard RL post-training pipeline. We validate the effectiveness of the progress advantage across three different applications: test-time scaling, uncertainty quantification, and failure attribution on five benchmarks and four model families. Across all settings, it consistently outperforms confidence-based baselines and, despite requiring no task-specific training, surpasses dedicated trained reward models. We complement these results with deeper analyses on characteristics of progress advantage, offering practical guidance for adoption in real-world agentic systems.
匹配关键词: agent coordination
---

[ACADEMIC - ARXIV]
标题: Model Forensics: Investigating Whether Concerning Behavior Reflects Misalignment
作者: Aditya Singh, Gerson Kroiz, Senthooran Rajamanoharan, Neel Nanda
链接: https://arxiv.org/abs/2606.26071v1
完整摘要: A central goal of safety research is determining whether a model is misaligned. Prior work has largely focused on detecting concerning behavior. But behavior alone does not establish misalignment: a concerning action can arise from benign causes such as confusion. This motivates model forensics: investigating whether the action was driven by malign intent. In this paper, we propose a baseline protocol for model forensics consisting of two steps, iterated as needed. First, we read the chain of thought (CoT) to generate hypotheses about what drives model behavior. Second, we make edits to the prompt or environment to test these hypotheses. While the CoT is not always faithful, it is a rich source of unsupervised insight that can guide the collection of more rigorous evidence. To evaluate our protocol, we create a suite of six agentic environments where models exhibit concerning behavior, and apply it to each. We establish that Kimi K2 Thinking takes shortcuts due to a genuine disposition towards low-effort actions, by showing this hypothesis successfully predicts its behavior. Through counterfactual experiments, we show DeepSeek R1 deceives out of a desire to be consistent with a previous instance of itself. Our methods nonetheless leave significant room for refinement. For example, when we test whether Kimi K2 Thinking believes it is violating user intent, we find no evidence of such a belief, but without positive controls we cannot confirm our tests would detect it. Overall, we find our simple protocol provides a strong baseline that we hope future work will improve upon. More broadly, our work is a concrete step in developing the growing field of model forensics.
匹配关键词: agent coordination
---

[ACADEMIC - ARXIV]
标题: The Unfireable Safety Kernel: Execution-Time AI Alignment for AI Agents and Other Escapable AI Systems
作者: Seth Dobrin, Łukasz Chmiel
链接: https://arxiv.org/abs/2606.26057v1
完整摘要: AI agents are granted access to tools, APIs, and other infrastructure, making them active principals in those systems. The dominant approach places controls inside the agent's own runtime: system prompts, output filters, and guardrail libraries. Any control in the agent's address space is reachable by inputs that influence it; this generalizes to any AI system with sufficient reach into its own runtime, a class we term escapable AI systems. We identify four properties that an authorization mechanism must satisfy for architectural control rather than for cooperative requests: process separation, pre-action enforcement on a structurally only path, fail-closed at both the request and system levels, and externalized signed evidence verifiable outside the controlled system's trust boundary. We position this layer as execution-time AI alignment, complementing training-time alignment (RLHF, Constitutional AI) and inference-time alignment. We present the Unfireable Safety Kernel, a Rust reference implementation realizing all four. Its fail-closed invariant is machine-checked at two levels: an SMT theorem (Z3) and an exhaustive bounded-model-checking proof of the production decision function (Kani, 4/4 harnesses). A Python-to-Rust migration was gated on byte-equivalence (1000/1000 fixtures; 17/17 adversarial classes). We evaluate the kernel governing a live, escapable AI system, a deterministic, self-improving world model, against an escape-seeking adversary driving its real self-modification seam: across 1,000 self-modifications, all 704 attempts on the safety-critical core are refused, with no escape; a further 300, under the operator kill switch, are also refused. A separate campaign of 6,240 authorization round-trips had no successful bypass. Against 3 contemporary systems claiming the agent control plane, the agent invokes control; here, it lacks that choice.
匹配关键词: agent coordination
---

[ACADEMIC - ARXIV]
标题: AI translation of literary texts is "fine", but readers still prefer human translations
作者: Yves Ferstler, Adam Podoxin, Ty Brassington, Roman Grundkiewicz, Maite Taboada, Marzena Karpinska
链接: https://arxiv.org/abs/2606.26040v1
完整摘要: AI translation of literary works is increasingly common. While the content may be rendered adequately, we do not know enough about how readers experience it in terms of immersiveness and literary effect, aspects poorly captured by automatic machine translation metrics or human evaluation targeting fluency and adequacy. We ask 15 avid readers to compare recently published human translations (HT) to machine translations (MT) generated with an agentic large language model (LLM)-based pipeline, for 15 recent novels in French, Polish, and Japanese and translated into English. Readers evaluated approximately 8K-word excerpts in two conditions: immersive reading of the whole excerpt (30 comparisons) and close reading of 386 aligned HT-MT chunk pairs (772 comparisons), with two readers per book and in alternating order of presentation. Overall, readers find MT "fine", but prefer HT (slightly at excerpt-level 19/30, more clearly at chunk-level 522/772) for its ease, clarity, and immersive nature. Readers' highlights show that MT's quality varies more within one book than HT's does. Crucially, readers cannot reliably tell the two apart (17/30 guess correctly) and tend to prefer the version they believe to be human. Automatic metrics, including LLM-as-a-judge approaches, fail to recover reader preferences and favor MT. We release LAIT (Literary AI Translation), a reader-centered evaluation dataset with 1K reader comments, 2K judgments and preference ratings, and 7.2K span-level annotations, along with our evaluation protocol and supporting interface.
匹配关键词: agent coordination
---

[ACADEMIC - ARXIV]
标题: RevengeBench: Reverse Engineering Code-Space Policies from Behavioral Experiments
作者: Babak Rahmani, Sebastian Dziadzio, Joschka Strüber, Sergio Hernández-Gutiérrez, Matthias Bethge
链接: https://arxiv.org/abs/2606.26094v1
完整摘要: For most of scientific history, researchers studying behavior could only infer hidden mechanisms from outward actions: an inverse problem that becomes more tractable when observation is augmented by targeted intervention. We pose a computational analogue: given only behavioral traces of an agent in a game environment, can a learner reconstruct the underlying decision program as executable code, and how much does this reconstruction improve with the ability to design controlled experiments? We introduce RevengeBench, a benchmark of 75 LLM generated, Elo-calibrated policies across five game environments, drawn from CodeClash tournament trajectories. The learner observes the hidden target policy play against sampled opponents and designs behavioral probes in the form of custom opponent policies that elicit informative behavior. It then submits an executable hypothesis, which is evaluated using continuous action-distance metrics. We further validate that recovered code carries informative signal in downstream player-versus-player tournaments. Across twelve frontier LLMs, recovery quality varies substantially (34 to 72% of initial distance closed), with reconstructed policies yielding measurable competitive advantage, particularly for weaker models that otherwise struggle to design effective counter-strategies. Our benchmark positions behavioral recovery of programmatic policies as a tractable inverse problem in code-space, opening a path to opponent modeling, policy interpretability, and the broader question of inferring latent mechanisms from observations.
匹配关键词: decentralized agent
---

[ACADEMIC - ARXIV]
标题: Neglected Free Lunch from Post-training: Progress Advantage for LLM Agents
作者: Changdae Oh, Wendi Li, Seongheon Park, Samuel Yeh, Tanwi Mallick, Sharon Li
链接: https://arxiv.org/abs/2606.26080v1
完整摘要: Process reward models enable fine-grained, step-level evaluation of LLMs, yet building them for agentic settings remains prohibitively difficult: long-horizon interactions, irreversible actions, and stochastic environment feedback make both human annotation and Monte Carlo estimation infeasible at scale. In this work, we show that reinforcement learning (RL) post-training already provides the ingredients for effective step-level scoring, eliminating the need for dedicated reward model training altogether. Concretely, we derive an implicit advantage under a general stochastic Markov decision process, which we term progress advantage -- log-probability ratio between the RL-trained policy and its reference policy exactly recovers the optimal advantage function. This formulation makes the resulting signal annotation-free, domain-agnostic, and available as a byproduct of the standard RL post-training pipeline. We validate the effectiveness of the progress advantage across three different applications: test-time scaling, uncertainty quantification, and failure attribution on five benchmarks and four model families. Across all settings, it consistently outperforms confidence-based baselines and, despite requiring no task-specific training, surpasses dedicated trained reward models. We complement these results with deeper analyses on characteristics of progress advantage, offering practical guidance for adoption in real-world agentic systems.
匹配关键词: decentralized agent
---

[ACADEMIC - ARXIV]
标题: Model Forensics: Investigating Whether Concerning Behavior Reflects Misalignment
作者: Aditya Singh, Gerson Kroiz, Senthooran Rajamanoharan, Neel Nanda
链接: https://arxiv.org/abs/2606.26071v1
完整摘要: A central goal of safety research is determining whether a model is misaligned. Prior work has largely focused on detecting concerning behavior. But behavior alone does not establish misalignment: a concerning action can arise from benign causes such as confusion. This motivates model forensics: investigating whether the action was driven by malign intent. In this paper, we propose a baseline protocol for model forensics consisting of two steps, iterated as needed. First, we read the chain of thought (CoT) to generate hypotheses about what drives model behavior. Second, we make edits to the prompt or environment to test these hypotheses. While the CoT is not always faithful, it is a rich source of unsupervised insight that can guide the collection of more rigorous evidence. To evaluate our protocol, we create a suite of six agentic environments where models exhibit concerning behavior, and apply it to each. We establish that Kimi K2 Thinking takes shortcuts due to a genuine disposition towards low-effort actions, by showing this hypothesis successfully predicts its behavior. Through counterfactual experiments, we show DeepSeek R1 deceives out of a desire to be consistent with a previous instance of itself. Our methods nonetheless leave significant room for refinement. For example, when we test whether Kimi K2 Thinking believes it is violating user intent, we find no evidence of such a belief, but without positive controls we cannot confirm our tests would detect it. Overall, we find our simple protocol provides a strong baseline that we hope future work will improve upon. More broadly, our work is a concrete step in developing the growing field of model forensics.
匹配关键词: decentralized agent
---

[ACADEMIC - ARXIV]
标题: The Unfireable Safety Kernel: Execution-Time AI Alignment for AI Agents and Other Escapable AI Systems
作者: Seth Dobrin, Łukasz Chmiel
链接: https://arxiv.org/abs/2606.26057v1
完整摘要: AI agents are granted access to tools, APIs, and other infrastructure, making them active principals in those systems. The dominant approach places controls inside the agent's own runtime: system prompts, output filters, and guardrail libraries. Any control in the agent's address space is reachable by inputs that influence it; this generalizes to any AI system with sufficient reach into its own runtime, a class we term escapable AI systems. We identify four properties that an authorization mechanism must satisfy for architectural control rather than for cooperative requests: process separation, pre-action enforcement on a structurally only path, fail-closed at both the request and system levels, and externalized signed evidence verifiable outside the controlled system's trust boundary. We position this layer as execution-time AI alignment, complementing training-time alignment (RLHF, Constitutional AI) and inference-time alignment. We present the Unfireable Safety Kernel, a Rust reference implementation realizing all four. Its fail-closed invariant is machine-checked at two levels: an SMT theorem (Z3) and an exhaustive bounded-model-checking proof of the production decision function (Kani, 4/4 harnesses). A Python-to-Rust migration was gated on byte-equivalence (1000/1000 fixtures; 17/17 adversarial classes). We evaluate the kernel governing a live, escapable AI system, a deterministic, self-improving world model, against an escape-seeking adversary driving its real self-modification seam: across 1,000 self-modifications, all 704 attempts on the safety-critical core are refused, with no escape; a further 300, under the operator kill switch, are also refused. A separate campaign of 6,240 authorization round-trips had no successful bypass. Against 3 contemporary systems claiming the agent control plane, the agent invokes control; here, it lacks that choice.
匹配关键词: decentralized agent
---

[ACADEMIC - ARXIV]
标题: AI translation of literary texts is "fine", but readers still prefer human translations
作者: Yves Ferstler, Adam Podoxin, Ty Brassington, Roman Grundkiewicz, Maite Taboada, Marzena Karpinska
链接: https://arxiv.org/abs/2606.26040v1
完整摘要: AI translation of literary works is increasingly common. While the content may be rendered adequately, we do not know enough about how readers experience it in terms of immersiveness and literary effect, aspects poorly captured by automatic machine translation metrics or human evaluation targeting fluency and adequacy. We ask 15 avid readers to compare recently published human translations (HT) to machine translations (MT) generated with an agentic large language model (LLM)-based pipeline, for 15 recent novels in French, Polish, and Japanese and translated into English. Readers evaluated approximately 8K-word excerpts in two conditions: immersive reading of the whole excerpt (30 comparisons) and close reading of 386 aligned HT-MT chunk pairs (772 comparisons), with two readers per book and in alternating order of presentation. Overall, readers find MT "fine", but prefer HT (slightly at excerpt-level 19/30, more clearly at chunk-level 522/772) for its ease, clarity, and immersive nature. Readers' highlights show that MT's quality varies more within one book than HT's does. Crucially, readers cannot reliably tell the two apart (17/30 guess correctly) and tend to prefer the version they believe to be human. Automatic metrics, including LLM-as-a-judge approaches, fail to recover reader preferences and favor MT. We release LAIT (Literary AI Translation), a reader-centered evaluation dataset with 1K reader comments, 2K judgments and preference ratings, and 7.2K span-level annotations, along with our evaluation protocol and supporting interface.
匹配关键词: decentralized agent
---

[ACADEMIC - ARXIV]
标题: Learning Action Priors for Cross-embodiment Robot Manipulation
作者: Dong Jing, Tianqi Zhang, Jiaqi Liu, Jinman Zhao, Zelong Sun, Li Erran Li, Zhiwu Lu, Mingyu Ding
链接: https://arxiv.org/abs/2606.26095v1
完整摘要: Most Vision-Language-Action (VLA) models build on a Vision-Language Model (VLM) backbone by attaching an action module and optimizing the full policy jointly. This design inherits strong visual and linguistic priors from the VLM, but leaves the action module to learn physical motion almost from scratch. As a result, the policy lacks an explicit motion prior, forcing early optimization to simultaneously discover temporal action dynamics and cross-modal alignment, a challenge further amplified in cross-embodiment settings. In this work, we propose to pretrain the action module with motion priors before cross-modal VLA alignment. Specifically, we introduce a two-stage training framework that equips the action module with cross-embodiment temporal motion structure before VLA training begins. In Stage~1, a lightweight flow-matching-based encoder-decoder action module efficiently learns temporal motion structure solely from unconditioned action trajectories, without processing visual or language tokens. In Stage~2, this learned prior is transferred to VLA training through decoder reuse and early-stage latent distillation, aligning visual-language features with the action embedding space while still allowing end-to-end policy refinement. In addition, the trained encoder serves as a compact history compressor, summarizing state-action histories into a single temporal context token for history-aware modeling at negligible cost. Extensive experiments across 13 diverse cross-embodiment tasks on both simulated and real-world platforms validate the effectiveness of our approach. Compared with VLA training without action priors, our model achieves faster convergence, higher success rates, and substantially stronger performance on data-scarce real-world tasks. Moreover, scaling up the action data in Stage~1 yields a more generalizable action prior that directly improves downstream VLA performance.
匹配关键词: swarm intelligence
---

[ACADEMIC - ARXIV]
标题: On-Policy Self-Distillation with Sampled Demonstrations Reduces Output Diversity
作者: Andrei Liviu Nicolicioiu, Mohammad Pezeshki, Aaron Courville
链接: https://arxiv.org/abs/2606.26091v1
完整摘要: On-policy self-distillation achieves strong pass@1 accuracy by using a single model as both teacher and student, with the teacher conditioned on a correct demonstration to provide dense token-level feedback. We show that this could come at a hidden cost: rollout diversity decreases and pass@k curves flatten (i.e., generating more rollouts fails to improve accuracy). We trace this to compounding biases in the design of self-distillation with sampled demonstrations. The teacher scores each student rollout while conditioned on a sampled correct rollout, channeling its feedback through the model's own biases. We theoretically analyze the optimal self-distillation policy and show that it tilts the base distribution by a pointwise conditional mutual information score between the student's rollout and the correct rollout used as context. Unlike the ideal optimal on-policy reinforcement learning (RL), which preserves probability ratios among equally correct rollouts, self-distillation can amplify existing probability gaps, concentrating mass on already-dominant modes. On a controlled graph path-finding task and science question-answering benchmarks, self-distilled models match or exceed RL on average performance but exhibit substantially lower functional and semantic diversity, failing on out-of-distribution settings that require diverse strategies.
匹配关键词: swarm intelligence
---

[ACADEMIC - ARXIV]
标题: Real-Time Voice AI Hears but Does Not Listen
作者: Martijn Bartelds, Federico Bianchi, James Zou
链接: https://arxiv.org/abs/2606.26083v1
完整摘要: Speech conveys information through both words and vocal delivery. We evaluate four leading production realtime voice systems-OpenAI's GPT Realtime 2, Google's Gemini 3.1 Flash Live, and Alibaba's Qwen3.5 Omni Plus and Omni Flash-on tasks where the words and the delivery patterns both convey meaningful information. Across three consequential scenarios, all four systems act on the words rather than the voice. They end calls with crying callers who insist nothing is wrong, approve wire transfers authorized in frightened voices, and enroll callers whose agreement is clearly sarcastic. Surprisingly, this is often not a failure of perception. When asked directly, three of the four systems reliably identify the distress, fear, or sarcasm they later ignore when making decisions. We observe a similar pattern when these realtime voice systems estimate accent and age, as their responses frequently follow the biases of the words rather than the acoustic properties of the speaker. We term this disconnect between perception and action the emotional intelligence gap of voice AI. Prompting systems to explicitly attend to vocal delivery improves performance only partially and inconsistently. Our findings show that current realtime voice AI systems often behave as if speech had been reduced to a transcript, suggesting that they should be used with caution in settings where the tone and emotion of delivery convey important information.
匹配关键词: swarm intelligence
---

[ACADEMIC - ARXIV]
标题: Neglected Free Lunch from Post-training: Progress Advantage for LLM Agents
作者: Changdae Oh, Wendi Li, Seongheon Park, Samuel Yeh, Tanwi Mallick, Sharon Li
链接: https://arxiv.org/abs/2606.26080v1
完整摘要: Process reward models enable fine-grained, step-level evaluation of LLMs, yet building them for agentic settings remains prohibitively difficult: long-horizon interactions, irreversible actions, and stochastic environment feedback make both human annotation and Monte Carlo estimation infeasible at scale. In this work, we show that reinforcement learning (RL) post-training already provides the ingredients for effective step-level scoring, eliminating the need for dedicated reward model training altogether. Concretely, we derive an implicit advantage under a general stochastic Markov decision process, which we term progress advantage -- log-probability ratio between the RL-trained policy and its reference policy exactly recovers the optimal advantage function. This formulation makes the resulting signal annotation-free, domain-agnostic, and available as a byproduct of the standard RL post-training pipeline. We validate the effectiveness of the progress advantage across three different applications: test-time scaling, uncertainty quantification, and failure attribution on five benchmarks and four model families. Across all settings, it consistently outperforms confidence-based baselines and, despite requiring no task-specific training, surpasses dedicated trained reward models. We complement these results with deeper analyses on characteristics of progress advantage, offering practical guidance for adoption in real-world agentic systems.
匹配关键词: swarm intelligence
---

[ACADEMIC - ARXIV]
标题: A cross-process welding penetration status prediction algorithm based on unsupervised domain adaptation in laser and TIG welding
作者: Sen Li, Haichao Cui, Chendong Shao, Yaqi Wang, Xinhua Tang
链接: https://arxiv.org/abs/2606.26078v1
完整摘要: Supervised deep learning has been widely used for weld penetration state classification; however, its performance often degrades significantly under domain shift, such as when transferring models between welding processes with distinct physical mechanisms:for instance, from arc-dominated tungsten inert gas (TIG) welding to keyhole-based laser welding. To overcome this limitation, we propose an unsupervised domain adaptation (UDA) framework integrated with a gradual source domain expansion (GSDE) strategy. Evaluated on dedicated TIG and laser welding datasets, our approach achieves high accuracy in both same-process and cross-process transfer tasks. Specifically, it attains average accuracies of 90.65% on TIGFH and 90.72% on LSPS in same-process settings, surpassing a supervised baseline by 35.83% and 38.87%, respectively. More notably, in cross-process scenarios, it reaches 80.48% for TIG to Laser and 81.13% for Laser to TIG, improving upon the baseline by 43.39% and 43.40%. UMAP visualizations verify that the model learns domain-invariant features while maintaining discriminative class boundaries. This method considerably lowers the relabeling cost for new welding processes and enhances the versatility of intelligent monitoring across different welding systems.
匹配关键词: swarm intelligence
---

[ACADEMIC - ARXIV]
标题: RevengeBench: Reverse Engineering Code-Space Policies from Behavioral Experiments
作者: Babak Rahmani, Sebastian Dziadzio, Joschka Strüber, Sergio Hernández-Gutiérrez, Matthias Bethge
链接: https://arxiv.org/abs/2606.26094v1
完整摘要: For most of scientific history, researchers studying behavior could only infer hidden mechanisms from outward actions: an inverse problem that becomes more tractable when observation is augmented by targeted intervention. We pose a computational analogue: given only behavioral traces of an agent in a game environment, can a learner reconstruct the underlying decision program as executable code, and how much does this reconstruction improve with the ability to design controlled experiments? We introduce RevengeBench, a benchmark of 75 LLM generated, Elo-calibrated policies across five game environments, drawn from CodeClash tournament trajectories. The learner observes the hidden target policy play against sampled opponents and designs behavioral probes in the form of custom opponent policies that elicit informative behavior. It then submits an executable hypothesis, which is evaluated using continuous action-distance metrics. We further validate that recovered code carries informative signal in downstream player-versus-player tournaments. Across twelve frontier LLMs, recovery quality varies substantially (34 to 72% of initial distance closed), with reconstructed policies yielding measurable competitive advantage, particularly for weaker models that otherwise struggle to design effective counter-strategies. Our benchmark positions behavioral recovery of programmatic policies as a tractable inverse problem in code-space, opening a path to opponent modeling, policy interpretability, and the broader question of inferring latent mechanisms from observations.
匹配关键词: game theory agent
---

[ACADEMIC - ARXIV]
标题: Neglected Free Lunch from Post-training: Progress Advantage for LLM Agents
作者: Changdae Oh, Wendi Li, Seongheon Park, Samuel Yeh, Tanwi Mallick, Sharon Li
链接: https://arxiv.org/abs/2606.26080v1
完整摘要: Process reward models enable fine-grained, step-level evaluation of LLMs, yet building them for agentic settings remains prohibitively difficult: long-horizon interactions, irreversible actions, and stochastic environment feedback make both human annotation and Monte Carlo estimation infeasible at scale. In this work, we show that reinforcement learning (RL) post-training already provides the ingredients for effective step-level scoring, eliminating the need for dedicated reward model training altogether. Concretely, we derive an implicit advantage under a general stochastic Markov decision process, which we term progress advantage -- log-probability ratio between the RL-trained policy and its reference policy exactly recovers the optimal advantage function. This formulation makes the resulting signal annotation-free, domain-agnostic, and available as a byproduct of the standard RL post-training pipeline. We validate the effectiveness of the progress advantage across three different applications: test-time scaling, uncertainty quantification, and failure attribution on five benchmarks and four model families. Across all settings, it consistently outperforms confidence-based baselines and, despite requiring no task-specific training, surpasses dedicated trained reward models. We complement these results with deeper analyses on characteristics of progress advantage, offering practical guidance for adoption in real-world agentic systems.
匹配关键词: game theory agent
---

[ACADEMIC - ARXIV]
标题: Model Forensics: Investigating Whether Concerning Behavior Reflects Misalignment
作者: Aditya Singh, Gerson Kroiz, Senthooran Rajamanoharan, Neel Nanda
链接: https://arxiv.org/abs/2606.26071v1
完整摘要: A central goal of safety research is determining whether a model is misaligned. Prior work has largely focused on detecting concerning behavior. But behavior alone does not establish misalignment: a concerning action can arise from benign causes such as confusion. This motivates model forensics: investigating whether the action was driven by malign intent. In this paper, we propose a baseline protocol for model forensics consisting of two steps, iterated as needed. First, we read the chain of thought (CoT) to generate hypotheses about what drives model behavior. Second, we make edits to the prompt or environment to test these hypotheses. While the CoT is not always faithful, it is a rich source of unsupervised insight that can guide the collection of more rigorous evidence. To evaluate our protocol, we create a suite of six agentic environments where models exhibit concerning behavior, and apply it to each. We establish that Kimi K2 Thinking takes shortcuts due to a genuine disposition towards low-effort actions, by showing this hypothesis successfully predicts its behavior. Through counterfactual experiments, we show DeepSeek R1 deceives out of a desire to be consistent with a previous instance of itself. Our methods nonetheless leave significant room for refinement. For example, when we test whether Kimi K2 Thinking believes it is violating user intent, we find no evidence of such a belief, but without positive controls we cannot confirm our tests would detect it. Overall, we find our simple protocol provides a strong baseline that we hope future work will improve upon. More broadly, our work is a concrete step in developing the growing field of model forensics.
匹配关键词: game theory agent
---

[ACADEMIC - ARXIV]
标题: The Unfireable Safety Kernel: Execution-Time AI Alignment for AI Agents and Other Escapable AI Systems
作者: Seth Dobrin, Łukasz Chmiel
链接: https://arxiv.org/abs/2606.26057v1
完整摘要: AI agents are granted access to tools, APIs, and other infrastructure, making them active principals in those systems. The dominant approach places controls inside the agent's own runtime: system prompts, output filters, and guardrail libraries. Any control in the agent's address space is reachable by inputs that influence it; this generalizes to any AI system with sufficient reach into its own runtime, a class we term escapable AI systems. We identify four properties that an authorization mechanism must satisfy for architectural control rather than for cooperative requests: process separation, pre-action enforcement on a structurally only path, fail-closed at both the request and system levels, and externalized signed evidence verifiable outside the controlled system's trust boundary. We position this layer as execution-time AI alignment, complementing training-time alignment (RLHF, Constitutional AI) and inference-time alignment. We present the Unfireable Safety Kernel, a Rust reference implementation realizing all four. Its fail-closed invariant is machine-checked at two levels: an SMT theorem (Z3) and an exhaustive bounded-model-checking proof of the production decision function (Kani, 4/4 harnesses). A Python-to-Rust migration was gated on byte-equivalence (1000/1000 fixtures; 17/17 adversarial classes). We evaluate the kernel governing a live, escapable AI system, a deterministic, self-improving world model, against an escape-seeking adversary driving its real self-modification seam: across 1,000 self-modifications, all 704 attempts on the safety-critical core are refused, with no escape; a further 300, under the operator kill switch, are also refused. A separate campaign of 6,240 authorization round-trips had no successful bypass. Against 3 contemporary systems claiming the agent control plane, the agent invokes control; here, it lacks that choice.
匹配关键词: game theory agent
---

[ACADEMIC - ARXIV]
标题: When Does Synthetic Data Augmentation Improve Score-Based Imbalanced Classification?
作者: Zhengchi Ma, Pengfei Lyu, Anru R. Zhang
链接: https://arxiv.org/abs/2606.26053v1
完整摘要: Synthetic data augmentation is widely used to mitigate class imbalance, but its theoretical effects on score-based classification remain poorly understood. This paper develops a framework for characterizing when synthetic minority augmentation can improve threshold-integrated and threshold-optimized metrics, including AUROC, AUPRC, best-threshold balanced accuracy, and best-threshold \(\F_1\) score. We separate the effect of augmentation into two components: a change in effective class weighting and a discrepancy between the synthetic and true minority distributions. Under well-specified score models, the raw estimator already targets the likelihood-ratio ordering, which is population-optimal for the metrics considered. Consequently, augmentation cannot provide a fundamental population-level improvement beyond possible finite-sample variance reduction, and may introduce additional bias through synthetic distributional error. We further establish minimax lower bounds showing that the raw estimator already achieves the optimal metric-regret rate in the well-specified regime. Under misspecification, however, augmentation can play a qualitatively different role: by changing the effective class balance, it can alter the restricted-class projection and correct ranking errors induced by the raw imbalanced objective. We provide explicit improvement bounds quantifying the roles of approximation error, finite-sample estimation error, and synthetic distributional error. Simulation studies corroborate the theory, demonstrating limited gains under well-specification and nontrivial but nonmonotone improvements under misspecification.
匹配关键词: game theory agent
---

[ACADEMIC - ARXIV]
标题: RevengeBench: Reverse Engineering Code-Space Policies from Behavioral Experiments
作者: Babak Rahmani, Sebastian Dziadzio, Joschka Strüber, Sergio Hernández-Gutiérrez, Matthias Bethge
链接: https://arxiv.org/abs/2606.26094v1
完整摘要: For most of scientific history, researchers studying behavior could only infer hidden mechanisms from outward actions: an inverse problem that becomes more tractable when observation is augmented by targeted intervention. We pose a computational analogue: given only behavioral traces of an agent in a game environment, can a learner reconstruct the underlying decision program as executable code, and how much does this reconstruction improve with the ability to design controlled experiments? We introduce RevengeBench, a benchmark of 75 LLM generated, Elo-calibrated policies across five game environments, drawn from CodeClash tournament trajectories. The learner observes the hidden target policy play against sampled opponents and designs behavioral probes in the form of custom opponent policies that elicit informative behavior. It then submits an executable hypothesis, which is evaluated using continuous action-distance metrics. We further validate that recovered code carries informative signal in downstream player-versus-player tournaments. Across twelve frontier LLMs, recovery quality varies substantially (34 to 72% of initial distance closed), with reconstructed policies yielding measurable competitive advantage, particularly for weaker models that otherwise struggle to design effective counter-strategies. Our benchmark positions behavioral recovery of programmatic policies as a tractable inverse problem in code-space, opening a path to opponent modeling, policy interpretability, and the broader question of inferring latent mechanisms from observations.
匹配关键词: agent communication
---

[ACADEMIC - ARXIV]
标题: Neglected Free Lunch from Post-training: Progress Advantage for LLM Agents
作者: Changdae Oh, Wendi Li, Seongheon Park, Samuel Yeh, Tanwi Mallick, Sharon Li
链接: https://arxiv.org/abs/2606.26080v1
完整摘要: Process reward models enable fine-grained, step-level evaluation of LLMs, yet building them for agentic settings remains prohibitively difficult: long-horizon interactions, irreversible actions, and stochastic environment feedback make both human annotation and Monte Carlo estimation infeasible at scale. In this work, we show that reinforcement learning (RL) post-training already provides the ingredients for effective step-level scoring, eliminating the need for dedicated reward model training altogether. Concretely, we derive an implicit advantage under a general stochastic Markov decision process, which we term progress advantage -- log-probability ratio between the RL-trained policy and its reference policy exactly recovers the optimal advantage function. This formulation makes the resulting signal annotation-free, domain-agnostic, and available as a byproduct of the standard RL post-training pipeline. We validate the effectiveness of the progress advantage across three different applications: test-time scaling, uncertainty quantification, and failure attribution on five benchmarks and four model families. Across all settings, it consistently outperforms confidence-based baselines and, despite requiring no task-specific training, surpasses dedicated trained reward models. We complement these results with deeper analyses on characteristics of progress advantage, offering practical guidance for adoption in real-world agentic systems.
匹配关键词: agent communication
---

[ACADEMIC - ARXIV]
标题: Model Forensics: Investigating Whether Concerning Behavior Reflects Misalignment
作者: Aditya Singh, Gerson Kroiz, Senthooran Rajamanoharan, Neel Nanda
链接: https://arxiv.org/abs/2606.26071v1
完整摘要: A central goal of safety research is determining whether a model is misaligned. Prior work has largely focused on detecting concerning behavior. But behavior alone does not establish misalignment: a concerning action can arise from benign causes such as confusion. This motivates model forensics: investigating whether the action was driven by malign intent. In this paper, we propose a baseline protocol for model forensics consisting of two steps, iterated as needed. First, we read the chain of thought (CoT) to generate hypotheses about what drives model behavior. Second, we make edits to the prompt or environment to test these hypotheses. While the CoT is not always faithful, it is a rich source of unsupervised insight that can guide the collection of more rigorous evidence. To evaluate our protocol, we create a suite of six agentic environments where models exhibit concerning behavior, and apply it to each. We establish that Kimi K2 Thinking takes shortcuts due to a genuine disposition towards low-effort actions, by showing this hypothesis successfully predicts its behavior. Through counterfactual experiments, we show DeepSeek R1 deceives out of a desire to be consistent with a previous instance of itself. Our methods nonetheless leave significant room for refinement. For example, when we test whether Kimi K2 Thinking believes it is violating user intent, we find no evidence of such a belief, but without positive controls we cannot confirm our tests would detect it. Overall, we find our simple protocol provides a strong baseline that we hope future work will improve upon. More broadly, our work is a concrete step in developing the growing field of model forensics.
匹配关键词: agent communication
---

[ACADEMIC - ARXIV]
标题: The Unfireable Safety Kernel: Execution-Time AI Alignment for AI Agents and Other Escapable AI Systems
作者: Seth Dobrin, Łukasz Chmiel
链接: https://arxiv.org/abs/2606.26057v1
完整摘要: AI agents are granted access to tools, APIs, and other infrastructure, making them active principals in those systems. The dominant approach places controls inside the agent's own runtime: system prompts, output filters, and guardrail libraries. Any control in the agent's address space is reachable by inputs that influence it; this generalizes to any AI system with sufficient reach into its own runtime, a class we term escapable AI systems. We identify four properties that an authorization mechanism must satisfy for architectural control rather than for cooperative requests: process separation, pre-action enforcement on a structurally only path, fail-closed at both the request and system levels, and externalized signed evidence verifiable outside the controlled system's trust boundary. We position this layer as execution-time AI alignment, complementing training-time alignment (RLHF, Constitutional AI) and inference-time alignment. We present the Unfireable Safety Kernel, a Rust reference implementation realizing all four. Its fail-closed invariant is machine-checked at two levels: an SMT theorem (Z3) and an exhaustive bounded-model-checking proof of the production decision function (Kani, 4/4 harnesses). A Python-to-Rust migration was gated on byte-equivalence (1000/1000 fixtures; 17/17 adversarial classes). We evaluate the kernel governing a live, escapable AI system, a deterministic, self-improving world model, against an escape-seeking adversary driving its real self-modification seam: across 1,000 self-modifications, all 704 attempts on the safety-critical core are refused, with no escape; a further 300, under the operator kill switch, are also refused. A separate campaign of 6,240 authorization round-trips had no successful bypass. Against 3 contemporary systems claiming the agent control plane, the agent invokes control; here, it lacks that choice.
匹配关键词: agent communication
---

[ACADEMIC - ARXIV]
标题: AI translation of literary texts is "fine", but readers still prefer human translations
作者: Yves Ferstler, Adam Podoxin, Ty Brassington, Roman Grundkiewicz, Maite Taboada, Marzena Karpinska
链接: https://arxiv.org/abs/2606.26040v1
完整摘要: AI translation of literary works is increasingly common. While the content may be rendered adequately, we do not know enough about how readers experience it in terms of immersiveness and literary effect, aspects poorly captured by automatic machine translation metrics or human evaluation targeting fluency and adequacy. We ask 15 avid readers to compare recently published human translations (HT) to machine translations (MT) generated with an agentic large language model (LLM)-based pipeline, for 15 recent novels in French, Polish, and Japanese and translated into English. Readers evaluated approximately 8K-word excerpts in two conditions: immersive reading of the whole excerpt (30 comparisons) and close reading of 386 aligned HT-MT chunk pairs (772 comparisons), with two readers per book and in alternating order of presentation. Overall, readers find MT "fine", but prefer HT (slightly at excerpt-level 19/30, more clearly at chunk-level 522/772) for its ease, clarity, and immersive nature. Readers' highlights show that MT's quality varies more within one book than HT's does. Crucially, readers cannot reliably tell the two apart (17/30 guess correctly) and tend to prefer the version they believe to be human. Automatic metrics, including LLM-as-a-judge approaches, fail to recover reader preferences and favor MT. We release LAIT (Literary AI Translation), a reader-centered evaluation dataset with 1K reader comments, 2K judgments and preference ratings, and 7.2K span-level annotations, along with our evaluation protocol and supporting interface.
匹配关键词: agent communication
---

[ACADEMIC - ARXIV]
标题: RevengeBench: Reverse Engineering Code-Space Policies from Behavioral Experiments
作者: Babak Rahmani, Sebastian Dziadzio, Joschka Strüber, Sergio Hernández-Gutiérrez, Matthias Bethge
链接: https://arxiv.org/abs/2606.26094v1
完整摘要: For most of scientific history, researchers studying behavior could only infer hidden mechanisms from outward actions: an inverse problem that becomes more tractable when observation is augmented by targeted intervention. We pose a computational analogue: given only behavioral traces of an agent in a game environment, can a learner reconstruct the underlying decision program as executable code, and how much does this reconstruction improve with the ability to design controlled experiments? We introduce RevengeBench, a benchmark of 75 LLM generated, Elo-calibrated policies across five game environments, drawn from CodeClash tournament trajectories. The learner observes the hidden target policy play against sampled opponents and designs behavioral probes in the form of custom opponent policies that elicit informative behavior. It then submits an executable hypothesis, which is evaluated using continuous action-distance metrics. We further validate that recovered code carries informative signal in downstream player-versus-player tournaments. Across twelve frontier LLMs, recovery quality varies substantially (34 to 72% of initial distance closed), with reconstructed policies yielding measurable competitive advantage, particularly for weaker models that otherwise struggle to design effective counter-strategies. Our benchmark positions behavioral recovery of programmatic policies as a tractable inverse problem in code-space, opening a path to opponent modeling, policy interpretability, and the broader question of inferring latent mechanisms from observations.
匹配关键词: emergent behavior
---

[ACADEMIC - ARXIV]
标题: Same Evidence, Different Answer: Auditing Order Sensitivity in Multimodal Large Language Models
作者: Akshay Paruchuri, Sanmi Koyejo, Ehsan Adeli
链接: https://arxiv.org/abs/2606.26079v1
完整摘要: Standard benchmarks for multimodal large language models (MLLMs) score each item on one canonical ordering and miss whether order-irrelevant shuffling changes the answer, a baseline reliability property called for by emerging AI evaluation guidelines. We introduce Facet-Probe, a five-facet audit (option, evidence-chunk, document-rank, image-set, and mixed-modality ordering) of 18 frontier and open-weight MLLMs. A Bayesian item-response model separates ordering noise from per-facet bias, and a same-ordering control estimates the decoder-stochastic floor for observed flips. We find that none of the 18 MLLMs we audit are order-invariant: screened per-facet panel-mean flip rates span 24-50%. A Gemini same-ordering control at temperature 0 estimates a substantial ordering excess over a same-input decoder-noise floor in verified cells. Capability predicts but does not eliminate flips; the best model still flips on 13.4% of trials. In our Gemini mitigation tests, training-free prompt changes are modality-conditional and do not transfer from text to visual reasoning. These results suggest that prompt-level mitigation alone is unlikely to provide general order robustness, motivating future work on training-time and architectural approaches. We propose cross-ordering flip rate as a standard reporting axis for MLLMs.
匹配关键词: emergent behavior
---

[ACADEMIC - ARXIV]
标题: Model Forensics: Investigating Whether Concerning Behavior Reflects Misalignment
作者: Aditya Singh, Gerson Kroiz, Senthooran Rajamanoharan, Neel Nanda
链接: https://arxiv.org/abs/2606.26071v1
完整摘要: A central goal of safety research is determining whether a model is misaligned. Prior work has largely focused on detecting concerning behavior. But behavior alone does not establish misalignment: a concerning action can arise from benign causes such as confusion. This motivates model forensics: investigating whether the action was driven by malign intent. In this paper, we propose a baseline protocol for model forensics consisting of two steps, iterated as needed. First, we read the chain of thought (CoT) to generate hypotheses about what drives model behavior. Second, we make edits to the prompt or environment to test these hypotheses. While the CoT is not always faithful, it is a rich source of unsupervised insight that can guide the collection of more rigorous evidence. To evaluate our protocol, we create a suite of six agentic environments where models exhibit concerning behavior, and apply it to each. We establish that Kimi K2 Thinking takes shortcuts due to a genuine disposition towards low-effort actions, by showing this hypothesis successfully predicts its behavior. Through counterfactual experiments, we show DeepSeek R1 deceives out of a desire to be consistent with a previous instance of itself. Our methods nonetheless leave significant room for refinement. For example, when we test whether Kimi K2 Thinking believes it is violating user intent, we find no evidence of such a belief, but without positive controls we cannot confirm our tests would detect it. Overall, we find our simple protocol provides a strong baseline that we hope future work will improve upon. More broadly, our work is a concrete step in developing the growing field of model forensics.
匹配关键词: emergent behavior
---

[ACADEMIC - ARXIV]
标题: Natural Ungrokking: Asymmetric Control of Which Rules Survive Pretraining
作者: Juliana Li, Diya Sreedhar
链接: https://arxiv.org/abs/2606.26050v1
完整摘要: Midway through an ordinary pretraining run, a small language model learns the pronoun-gender rule: cued with a girl's name ("Sue cried because"), it resolves the next pronoun to she, generalizing to held-out probes (0.94 by step 925). By step 3,500 the same model scores near zero on the same probes, although the rule's evidence is still in the training data. We call this within-run reversal natural ungrokking: the corpus decides, with no trace in the loss curve, which learned rules a model keeps. Which rules survive is predictable from one corpus statistic: how often the training stream shows the rule winning. Across un-intervened runs (two corpora, three budgets, three seeds), support frequency decides a rule's fate; the data-to-parameter ratio only modulates how deeply a doomed rule falls. The same emerge-then-collapse dynamics appear in public Pythia checkpoints, collapse depth ordered by model scale as predicted. The forgetting is a displacement: a competing surface pattern out-competes the rule, and the log-probability margin between them crosses zero within 100 training steps of the behavioral collapse. Control over this fate is asymmetric: the same edit that destroys a rule on demand cannot restore it. Flipping support to counter-evidence in place kills the rule with monotone dose-response in two unrelated rules; but injecting support back, even to 450 times the level that naturally sustains it, buys no recovery. Every confirmatory threshold and prediction was pre-registered before the data it governed was read.
匹配关键词: emergent behavior
---

[ACADEMIC - ARXIV]
标题: Learning Robot Visual Navigation in Crowds via Intention-Aware Scene Representations
作者: Han Bao, Bingyi Xia, Hanjing Ye, Yu Zhan, Hao Cheng, Baozhi Jia, Wenjun Xu, Jiankun Wang
链接: https://arxiv.org/abs/2606.26047v1
完整摘要: Robot crowd navigation requires the ability to infer human intentions while accounting for the structural constraints of the environment. Currently, deep reinforcement learning (DRL) provides a promising method for learning navigation policies that understand human intentions. However, most of them rely on limited scene representations, treating pedestrians as simple 2D points and ignoring rich visual cues from both humans and the environment. To address this issue, we introduce iCrowdNav, a novel visual crowd navigation method with intention-aware scene representations, to encode behavioral and structural context from egocentric visual observations. Our method employs two key components: a spatio-temporal encoder for extracting occupancy features of the scene, and Intent-Interact Former (I$^2$ Former), an attention-based module that encodes human poses to infer pedestrians' motion intentions. These features are integrated into a compact state embedding that supports effective DRL policy training. Extensive experiments show that our method achieves superior performance over baselines, and real-world deployment demonstrates vision-based crowd navigation.
匹配关键词: emergent behavior
---

[ACADEMIC - ARXIV]
标题: Same Evidence, Different Answer: Auditing Order Sensitivity in Multimodal Large Language Models
作者: Akshay Paruchuri, Sanmi Koyejo, Ehsan Adeli
链接: https://arxiv.org/abs/2606.26079v1
完整摘要: Standard benchmarks for multimodal large language models (MLLMs) score each item on one canonical ordering and miss whether order-irrelevant shuffling changes the answer, a baseline reliability property called for by emerging AI evaluation guidelines. We introduce Facet-Probe, a five-facet audit (option, evidence-chunk, document-rank, image-set, and mixed-modality ordering) of 18 frontier and open-weight MLLMs. A Bayesian item-response model separates ordering noise from per-facet bias, and a same-ordering control estimates the decoder-stochastic floor for observed flips. We find that none of the 18 MLLMs we audit are order-invariant: screened per-facet panel-mean flip rates span 24-50%. A Gemini same-ordering control at temperature 0 estimates a substantial ordering excess over a same-input decoder-noise floor in verified cells. Capability predicts but does not eliminate flips; the best model still flips on 13.4% of trials. In our Gemini mitigation tests, training-free prompt changes are modality-conditional and do not transfer from text to visual reasoning. These results suggest that prompt-level mitigation alone is unlikely to provide general order robustness, motivating future work on training-time and architectural approaches. We propose cross-ordering flip rate as a standard reporting axis for MLLMs.
匹配关键词: reasoning
---

[ACADEMIC - ARXIV]
标题: RoboAtlas: Contextual Active SLAM
作者: Alexander Schperberg, Shivam K. Panda, Abraham P. Vinod, M. K. Jawed, Stefano Di Cairano
链接: https://arxiv.org/abs/2606.26046v1
完整摘要: We present RoboAtlas, a contextual Active SLAM framework that adaptively balances geometric exploration and semantic reasoning using a scalable 3D semantic mapping system, OpenRoboVox. RoboAtlas integrates frontier exploration, global semantic-map reasoning, and egocentric VLM-based reasoning through a contextual multi-armed bandit that transitions from exploration to semantically guided navigation as scene understanding improves. We evaluate the system in simulation and on a Unitree Go2 robot in large-scale real-world environments exceeding 1800 m2 with approx. 30k mapped semantic instances, achieving a 100% task success rate. On the GOAT-Bench "Val Unseen" benchmark, RoboAtlas achieves state-of-the-art performance with highest reported success rate (SR) of 90.6%, using GPT-4o, improving over the strongest prior baseline by 17.8 percentage points in SR. Using the much smaller Qwen2.5-VL-7B model, it still achieves 88.8% SR, outperforming all baselines using GPT-4o in SR, and revealing the importance of the information gained by our semantic mapping framework over simply replacing the underlying foundation model. The results demonstrate that grounding foundation models with large-scale 3D semantic maps enables robust and efficient contextual Active SLAM.
匹配关键词: reasoning
---

[ACADEMIC - ARXIV]
标题: How Robust is OCR-Reasoning? Evaluating OCR-Reasoning Robustness of Vision-Language Models under Visual Perturbations
作者: Yuxing Cheng, Yuan Wu, Yi Chang
链接: https://arxiv.org/abs/2606.26041v1
完整摘要: Vision-language models (VLMs) have achieved strong performance on OCR-based benchmarks and increasingly focused on text-rich understanding, but their robustness under controlled visual degradation remains insufficiently understood. This gap is critical for OCR reasoning, where visual corruption can induce OCR errors and structural distortions, thereby introducing uncertainty into the reasoning task. To systematically study this problem, we introduce OCR-Robust, a benchmark designed for evaluating OCR reasoning robustness under visual perturbations. It contains 812 samples across two complementary subsets: OCR1.0, covering documents, scene text, receipts, handwriting, and mathematical content, and OCR2.0, focusing on charts, geometry diagrams, and tables. To enable efficient yet informative evaluation, we conduct a pilot study over 18 candidate perturbations and select 5 representative types at 3 severity levels each based on their impact and cross-model discriminability. We evaluate robustness using clean accuracy, Relative Corruption Retention (RCR), Worst-Case Retention (WCR), and a composite Corruption Robustness Index (CRI), and benchmark 18 models spanning proprietary systems, open-source VLMs, and OCR+LLM pipelines. Our results show that higher clean accuracy does not necessarily imply stronger robustness, and that models can suffer pronounced degradation in the worst case on OCR tasks that are sensitive to structure, and charts and tables are substantially more fragile than document-like inputs under perturbation.
匹配关键词: reasoning
---

[ACADEMIC - ARXIV]
标题: TriViewBench: Controlled Complexity Scaling for Multi-View Structural Reasoning in MLLMs
作者: Yu-Yang Chen, Lan-Zhe Guo
链接: https://arxiv.org/abs/2606.26029v1
完整摘要: Multimodal Large Language Models (MLLMs) demonstrate strong performance on standard visual question answering benchmarks, yet their scalability under controlled structural complexity remains poorly understood. We introduce TriViewBench, a controlled three-view visual reasoning benchmark constructed from synthetic 3D scenes with explicitly parameterized object count and occlusion. The benchmark contains 1,923 scenes and over 14K Question-Answer (QA) pairs organized into four complexity levels and three reasoning categories: Local Decision, Object Counting, and Global Recovery. We evaluate 18 open- and closed-source MLLMs under a unified prompting protocol. All 18 models exhibit an identical capability hierarchy without exception (Local Decision > Object Counting > Global Recovery), and performance degrades monotonically with complexity: Local Decision tasks decline modestly (12.11% relative drop), while Object Counting degrades substantially (59.14%) and Global Recovery collapses severely (80.02%). Error analysis on Object Counting reveals two mechanistically independent failure modes: single-view tasks are dominated by undercounting due to occlusion blindness, whereas the multi-view task reverses to overcounting due to cross-view identity confusion. Chain-of-Thought (CoT) prompting yields near-zero overall benefit ($Δ= -0.16\%$) and its effect on Global Recovery is strongly capability-gated, suggesting that the bottleneck lies in cross-view spatial representation rather than reasoning strategy. These findings reveal fundamental scalability limitations in current MLLMs and position TriViewBench as a controlled diagnostic framework for analyzing structural reasoning failures.
匹配关键词: reasoning
---

[ACADEMIC - ARXIV]
标题: Autodata: An agentic data scientist to create high quality synthetic data
作者: Ilia Kulikov, Chenxi Whitehouse, Tianhao Wu, Yixin Nie, Swarnadeep Saha, Eryk Helenowski, Weizhe Yuan, Olga Golovneva, Jack Lanchantin, Yoram Bachrach, Jakob Foerster, Xian Li, Han Fang, Sainbayar Sukhbaatar, Jason Weston
链接: https://arxiv.org/abs/2606.25996v1
完整摘要: We introduce Autodata, a general method that enables AI agents to act as data scientists who build high quality training and evaluation data. We show how to train (meta-optimize) such a data scientist agent, so that it learns to create even stronger data. We describe the overall formulation, and a specific practical implementation, Agentic Self-Instruct. We conduct experiments on computer science research tasks, legal reasoning tasks and reasoning with mathematical objects, where we obtain improved results compared to classical synthetic dataset creation methods. Further, meta-optimizing the data scientist agent itself delivers an even larger performance uplift. Agentic data creation provides a way to convert increased inference compute into higher quality model training. Overall, we believe this direction has the potential to change the way we build AI data.
匹配关键词: reasoning
---

[ACADEMIC - ARXIV]
标题: Model Forensics: Investigating Whether Concerning Behavior Reflects Misalignment
作者: Aditya Singh, Gerson Kroiz, Senthooran Rajamanoharan, Neel Nanda
链接: https://arxiv.org/abs/2606.26071v1
完整摘要: A central goal of safety research is determining whether a model is misaligned. Prior work has largely focused on detecting concerning behavior. But behavior alone does not establish misalignment: a concerning action can arise from benign causes such as confusion. This motivates model forensics: investigating whether the action was driven by malign intent. In this paper, we propose a baseline protocol for model forensics consisting of two steps, iterated as needed. First, we read the chain of thought (CoT) to generate hypotheses about what drives model behavior. Second, we make edits to the prompt or environment to test these hypotheses. While the CoT is not always faithful, it is a rich source of unsupervised insight that can guide the collection of more rigorous evidence. To evaluate our protocol, we create a suite of six agentic environments where models exhibit concerning behavior, and apply it to each. We establish that Kimi K2 Thinking takes shortcuts due to a genuine disposition towards low-effort actions, by showing this hypothesis successfully predicts its behavior. Through counterfactual experiments, we show DeepSeek R1 deceives out of a desire to be consistent with a previous instance of itself. Our methods nonetheless leave significant room for refinement. For example, when we test whether Kimi K2 Thinking believes it is violating user intent, we find no evidence of such a belief, but without positive controls we cannot confirm our tests would detect it. Overall, we find our simple protocol provides a strong baseline that we hope future work will improve upon. More broadly, our work is a concrete step in developing the growing field of model forensics.
匹配关键词: chain-of-thought
---

[ACADEMIC - ARXIV]
标题: TriViewBench: Controlled Complexity Scaling for Multi-View Structural Reasoning in MLLMs
作者: Yu-Yang Chen, Lan-Zhe Guo
链接: https://arxiv.org/abs/2606.26029v1
完整摘要: Multimodal Large Language Models (MLLMs) demonstrate strong performance on standard visual question answering benchmarks, yet their scalability under controlled structural complexity remains poorly understood. We introduce TriViewBench, a controlled three-view visual reasoning benchmark constructed from synthetic 3D scenes with explicitly parameterized object count and occlusion. The benchmark contains 1,923 scenes and over 14K Question-Answer (QA) pairs organized into four complexity levels and three reasoning categories: Local Decision, Object Counting, and Global Recovery. We evaluate 18 open- and closed-source MLLMs under a unified prompting protocol. All 18 models exhibit an identical capability hierarchy without exception (Local Decision > Object Counting > Global Recovery), and performance degrades monotonically with complexity: Local Decision tasks decline modestly (12.11% relative drop), while Object Counting degrades substantially (59.14%) and Global Recovery collapses severely (80.02%). Error analysis on Object Counting reveals two mechanistically independent failure modes: single-view tasks are dominated by undercounting due to occlusion blindness, whereas the multi-view task reverses to overcounting due to cross-view identity confusion. Chain-of-Thought (CoT) prompting yields near-zero overall benefit ($Δ= -0.16\%$) and its effect on Global Recovery is strongly capability-gated, suggesting that the bottleneck lies in cross-view spatial representation rather than reasoning strategy. These findings reveal fundamental scalability limitations in current MLLMs and position TriViewBench as a controlled diagnostic framework for analyzing structural reasoning failures.
匹配关键词: chain-of-thought
---

[ACADEMIC - ARXIV]
标题: FeVOS: Foresight Expression Video Object Segmentation
作者: Kehan Lan, Kaining Ying, Henghui Ding
链接: https://arxiv.org/abs/2606.25585v1
完整摘要: Existing Referring Video Object Segmentation tasks focus on referring expressions describing events, actions or appearances of relevant objects within the observed frames, lacking evaluation in scenarios that require pre-decisive spatio-temporal reasoning, thereby limiting their applicability. To address this, we propose Foresight Expression Video Object Segmentation, a task that queries future events in upcoming video segments and requires masks of the objects in the observed frames as visual answers. For example, in ego-centric scenes, the question "What tool will be used?" demands reasoning over spatio-temporal cues to predict the masks of the next tool to be used, which helps with the understanding of future actions and decisions. To support this task, we introduce FeVOS, a dataset with 968 video clips, 14,525 foresight expressions, and 2,904 chain-of-thought annotations to provide explicit and interpretable reasoning steps. We further develop FeVOS-R1, an MLLM-based model trained on our dataset via a two-stage pipeline of supervised fine-tuning and reinforcement learning. FeVOS-R1 not only achieves state-of-the-art performance on FeVOS, but also demonstrates strong generalization to existing RVOS benchmarks. We hope this work can inspire more research on predictive reasoning in video perception.
匹配关键词: chain-of-thought
---

[ACADEMIC - ARXIV]
标题: Riazi-8B: An Urdu Large Language Model for Mathematical Reasoning
作者: Azher Ali, Ibtsam Haider, Raja Khurram Shahzad, Seemab Latif, Mehwish Fatima
链接: https://arxiv.org/abs/2606.25568v1
完整摘要: Recent LLMs demonstrate strong mathematical reasoning capabilities, but existing gains rely heavily on English-centric training resources and benchmarks. As a result, reasoning performance degrades substantially in low-resource languages such as Urdu, where reasoning-oriented datasets and adapted models remain scarce. Urdu lacks both reasoning-oriented resources and models adapted for multi-step mathematical problem solving, limiting the applicability of recent progress to Urdu-speaking users. We address this gap through Riazi-8B, an Urdu mathematical reasoning model developed through a two-step adaptation process comprising continued pre-training on Urdu Wikipedia and supervised fine-tuning on Urdu Chain-of-Thought data derived from GSM8K. We evaluate Riazi-8B on MGSM-Urdu against existing Urdu instruction-tuned models. Our results show consistent improvements in answer correctness, reasoning quality, response completeness, and Urdu generation. Our findings demonstrate that combining Urdu language adaptation with reasoning-focused fine-tuning is an effective strategy for extending mathematical reasoning capabilities to low-resource languages.
匹配关键词: chain-of-thought
---

[ACADEMIC - ARXIV]
标题: Agentic evolution of physically constrained foundation models
作者: Jiangwei Zhang, Wen Sun, Chong Wang, Shiyao Li, Cheng Che, Chunjing Han, Dan Meng, Jian Yang, Yu Wang, Rui Hou
链接: https://arxiv.org/abs/2606.25532v1
完整摘要: Artificial intelligence increasingly drives automated scientific discovery, yet contemporary generalist agents lack physical grounding, frequently hallucinating hardware-incompatible designs. Here, we present a physically grounded, multi-agent discovery engine that autonomously architects hardware-compliant computing systems. Anchored by an Evolutionary Knowledge Graph structuring past scientific innovations, the framework extracts an "algorithmic Chain-of-Thought" to transform blind stochastic search into directed structural evolution. Applied to the extreme testbed of foundation model deployment, the engine evolved two hardware-aware compression methodologies surpassing human-engineered heuristics: Q-Enhance mitigates long-context accuracy loss in dense models, and MoE-Salient-AQ outperforms state-of-the-art manual sparse Mixture-of-Experts designs by 3.7% at sub-3-bit regimes. Utilizing a bandwidth-efficient Sensitivity Profile, we successfully deployed a massive 235-billion-parameter model onto a constrained dual-A100 server, reducing memory requirements by 75% with a marginal 0.64% accuracy degradation. By transforming unconstrained combinatorial search into knowledge-driven autonomy, this establishes a scalable hardware-software co-design paradigm for machine-driven discovery within strict physical boundaries.
匹配关键词: chain-of-thought
---

[ACADEMIC - ARXIV]
标题: RevengeBench: Reverse Engineering Code-Space Policies from Behavioral Experiments
作者: Babak Rahmani, Sebastian Dziadzio, Joschka Strüber, Sergio Hernández-Gutiérrez, Matthias Bethge
链接: https://arxiv.org/abs/2606.26094v1
完整摘要: For most of scientific history, researchers studying behavior could only infer hidden mechanisms from outward actions: an inverse problem that becomes more tractable when observation is augmented by targeted intervention. We pose a computational analogue: given only behavioral traces of an agent in a game environment, can a learner reconstruct the underlying decision program as executable code, and how much does this reconstruction improve with the ability to design controlled experiments? We introduce RevengeBench, a benchmark of 75 LLM generated, Elo-calibrated policies across five game environments, drawn from CodeClash tournament trajectories. The learner observes the hidden target policy play against sampled opponents and designs behavioral probes in the form of custom opponent policies that elicit informative behavior. It then submits an executable hypothesis, which is evaluated using continuous action-distance metrics. We further validate that recovered code carries informative signal in downstream player-versus-player tournaments. Across twelve frontier LLMs, recovery quality varies substantially (34 to 72% of initial distance closed), with reconstructed policies yielding measurable competitive advantage, particularly for weaker models that otherwise struggle to design effective counter-strategies. Our benchmark positions behavioral recovery of programmatic policies as a tractable inverse problem in code-space, opening a path to opponent modeling, policy interpretability, and the broader question of inferring latent mechanisms from observations.
匹配关键词: test-time compute
---

[ACADEMIC - ARXIV]
标题: Neglected Free Lunch from Post-training: Progress Advantage for LLM Agents
作者: Changdae Oh, Wendi Li, Seongheon Park, Samuel Yeh, Tanwi Mallick, Sharon Li
链接: https://arxiv.org/abs/2606.26080v1
完整摘要: Process reward models enable fine-grained, step-level evaluation of LLMs, yet building them for agentic settings remains prohibitively difficult: long-horizon interactions, irreversible actions, and stochastic environment feedback make both human annotation and Monte Carlo estimation infeasible at scale. In this work, we show that reinforcement learning (RL) post-training already provides the ingredients for effective step-level scoring, eliminating the need for dedicated reward model training altogether. Concretely, we derive an implicit advantage under a general stochastic Markov decision process, which we term progress advantage -- log-probability ratio between the RL-trained policy and its reference policy exactly recovers the optimal advantage function. This formulation makes the resulting signal annotation-free, domain-agnostic, and available as a byproduct of the standard RL post-training pipeline. We validate the effectiveness of the progress advantage across three different applications: test-time scaling, uncertainty quantification, and failure attribution on five benchmarks and four model families. Across all settings, it consistently outperforms confidence-based baselines and, despite requiring no task-specific training, surpasses dedicated trained reward models. We complement these results with deeper analyses on characteristics of progress advantage, offering practical guidance for adoption in real-world agentic systems.
匹配关键词: test-time compute
---

[ACADEMIC - ARXIV]
标题: Same Evidence, Different Answer: Auditing Order Sensitivity in Multimodal Large Language Models
作者: Akshay Paruchuri, Sanmi Koyejo, Ehsan Adeli
链接: https://arxiv.org/abs/2606.26079v1
完整摘要: Standard benchmarks for multimodal large language models (MLLMs) score each item on one canonical ordering and miss whether order-irrelevant shuffling changes the answer, a baseline reliability property called for by emerging AI evaluation guidelines. We introduce Facet-Probe, a five-facet audit (option, evidence-chunk, document-rank, image-set, and mixed-modality ordering) of 18 frontier and open-weight MLLMs. A Bayesian item-response model separates ordering noise from per-facet bias, and a same-ordering control estimates the decoder-stochastic floor for observed flips. We find that none of the 18 MLLMs we audit are order-invariant: screened per-facet panel-mean flip rates span 24-50%. A Gemini same-ordering control at temperature 0 estimates a substantial ordering excess over a same-input decoder-noise floor in verified cells. Capability predicts but does not eliminate flips; the best model still flips on 13.4% of trials. In our Gemini mitigation tests, training-free prompt changes are modality-conditional and do not transfer from text to visual reasoning. These results suggest that prompt-level mitigation alone is unlikely to provide general order robustness, motivating future work on training-time and architectural approaches. We propose cross-ordering flip rate as a standard reporting axis for MLLMs.
匹配关键词: test-time compute
---

[ACADEMIC - ARXIV]
标题: When Certainty Is an Artifact: Keyword Lexicon Blindness and the (Mis)Measurement of Rhetorical Stance
作者: Bo Chen
链接: https://arxiv.org/abs/2606.26062v1
完整摘要: Can a statistically significant, large-effect-size finding in computational social science be entirely an artifact of the measurement instrument? We present a case where the answer appears to be yes. Analyzing 85 interviews across four public intellectuals (2016--2026), we find a robust negative-affect/emphatic-certainty lexical co-occurrence pattern under keyword-based scoring ($r = 0.72$--$0.93$, $p < 0.01$ for all four speakers). Replacing keyword counting with LLM-based zero-shot semantic classification on the complete diarized corpus (32,625 sentences) dramatically reduces this correlation: Dalio's $r = 0.851$ drops to $r = 0.206$, with two speakers showing negative $r(\text{neg}, \text{emphatic})$ and one showing null. In contrast, the LLM reveals a strong negative-hedging coupling across speakers -- Rogoff's $r(\text{neg}, \text{hedged}) = 0.875$ ($p = 0.001$) and Zeihan's $r(\text{neg}, \text{hedged}) = 0.722$ ($p = 0.008$) -- consistent with the conventional expectation that pessimistic discourse attracts hedging, not certainty. Sentence-level error analysis traces this discrepancy to three structural failure modes in keyword lexicons -- syntactic blindness, polysemy blindness, and categorical absence -- illustrated through cases where keyword counting inverts semantic meaning (e.g., ''never absolutely totally confident'' scored as high-certainty). We argue that keyword lexicons measure a universal lexical co-occurrence tendency -- negative discourse naturally attracts emphatic vocabulary -- that is orthogonal to, and can systematically invert, rhetorical stance. Treating keyword counts as measurements of epistemic certainty is a category error: a finding that appears to be about a speaker's psychology may be entirely about the counting of words.
匹配关键词: test-time compute
---

[ACADEMIC - ARXIV]
标题: FAR-LIO: Enabling High-Speed Autonomy through Fast, Accurate, and Robust LiDAR-Inertial Odometry
作者: Maximilian Leitenstern, Marcel Weinmann, Patrick Haft, Tobias Lasser, Dominik Kulmer, Markus Lienkamp
链接: https://arxiv.org/abs/2606.26010v1
完整摘要: Robust and accurate odometry estimation is essential in modern robotics. In environments characterized by highly dynamic motion and sensor noise, odometry estimation becomes increasingly challenging. Autonomous racing combines both factors in an unstructured setting, where minimizing odometry latency is essential for stable closed-loop control. This paper introduces FAR-LIO, a highly optimized CUDA-accelerated LiDAR-inertial odometry framework developed for Fast, Accurate, and Robust performance. Our system leverages a novel CUDA-based voxel hashmap to enable parallelized nearest-neighbor search and efficient map updates. We employ a sparsity-aware Generalized Iterative Closest Point algorithm with adaptive thresholding on top of the CUDA-based voxel hashmap with adaptive density to achieve low-latency without compromising accuracy. An Extended Kalman Filter serves as a robust backend. It utilizes an upsampling and delay compensation strategy to fuse the LiDAR odometry with high-frequency IMU data, thereby ensuring a robust and smooth odometry output. We evaluate FAR-LIO across four different sensor setups, using both public datasets and data from two autonomous racecars driving at speeds of up to 250 km/h. FAR-LIO achieves an average 6.9% reduction in the positional error and 38.4% lower runtime compared to state-of-the-art baselines on target hardware using a single parameter set. This demonstrates its computational efficiency and broad applicability. To build upon our work, our code is available open-source on https://github.com/TUMFTM/FAR-LIO.
匹配关键词: test-time compute
---

[ACADEMIC - ARXIV]
标题: A Benchmark for Heterogeneous Stereo Deblurring with Physically- and Epipolar-constrained Cross Attention
作者: Hoju Shin, Jiah Kim, Seung-Wook Kim, Seowon Ji
链接: https://arxiv.org/abs/2606.25962v1
完整摘要: Modern stereo-capable smartphones enable immersive XR content capture. However, hardware heterogeneity across camera modules often causes severe asymmetric blur artifacts. Existing methods and benchmarks largely assume homogeneous stereo setups and therefore do not explicitly address such asymmetric degradation. To bridge this gap, we present a dedicated framework for heterogeneous stereo deblurring. First, we introduce the heterogeneous stereo deblurring (HSD) dataset, constructed from real smartphone stereo captures via multi-frame integration. Second, we propose physically- and epipolar-constrained cross attention (PECA), a lightweight module that restricts cross-view matching to an epipolar search window bounded by a optics-derived disparity upper bound. By enforcing physically valid disparity constraints, PECA enables efficient and reliable cross-view feature fusion. Moreover, our confidence-weighted attention with residual fusion emphasizes cross-guided deblurring when correspondences are reliable, while naturally falling back to self-deblurring in occluded or unreliable regions. PECA is architecture-agnostic and consistently improves CNN-, Transformer-, and NAFNet-based baselines. Extensive experiments on HSD show that PECA-enhanced models achieve improved restoration performance with favorable efficiency.
匹配关键词: self-consistency
---

[ACADEMIC - ARXIV]
标题: TacVerse: A Multi-Sensor Dataset and Benchmark for Cross-Sensor Vision-Based Tactile Perception
作者: Lan Wei, Gurmeher Khurana, Sirine Bhouri, Wenhao Hong, Zeyuan Xin, Qingzheng Cong, Wen Fan, Yanzheng Xiang, Dandan Zhang
链接: https://arxiv.org/abs/2606.25877v1
完整摘要: Vision-based tactile sensors (VBTSs) enable robots to infer contact geometry and force-related cues by imaging deformation through an internal camera, yet generalisation across sensor designs remains poorly understood. We present TacVerse, a multi-sensor dataset and benchmark for cross-sensor vision-based tactile perception. The dataset contains 106,800 tactile images from seven VBTSs and supports three downstream tasks: shape classification, grating classification, and force regression. Experiments are conducted under three settings: within-sensor training, zero-shot cross-sensor transfer, and few-shot adaptation. Strong within-sensor performance across all tasks indicates that the collected tactile observations are informative for the target objectives. Direct cross-sensor transfer, however, leads to substantial degradation. Shape classification is comparatively robust, whereas grating classification and force regression are more sensitive to sensor shift. Few-shot adaptation for force regression consistently improves performance on unseen target sensors but does not fully close the gap to within-sensor upper bounds. A representation study further shows that MAE (Masked Autoencoder) pretraining provides the most consistent gains across tasks and sensors. TacVerse provides a controlled testbed for studying sensor shift, data-efficient adaptation, and self-supervised learning in tactile perception.
匹配关键词: self-consistency
---

[ACADEMIC - ARXIV]
标题: $S^{2}$-FracMix: Label-Preserving Self-Saliency Mixup Augmentation
作者: Khawar Islam, Arif Mahmood, Xin Jin, Naveed Akhtar
链接: https://arxiv.org/abs/2606.25784v1
完整摘要: Data augmentation is known to improve generalization of deep visual models. Recent methods favor mixup strategies that generate interpolated samples to improve model performance. However, these techniques not only incur significant computational overhead, they also lead to semantic disruption of augmentation data due to cross-sample mixing. We first propose Self-Saliency ($S^2$) Mixup, which constructs challenging yet label-consistent samples by extracting multi-scale salient patches and reinserting them into non-salient regions of the same image. This promotes scale-invariant feature learning while avoiding cross-sample interference. To further enhance model robustness, we introduce FracMix, a mixing scheme that injects self-similarity patterns into salient regions using adaptive ratios. Collectively, our unified framework, $S^{2}$-FracMix, enables simultaneous learning from fractal and non-fractal structures within a single image, yielding a targeted and structurally coherent augmentation strategy. We theoretically analyze the advantage of our technique, and empirically establish its superiority over the existing methods by achieving state-of-the-art performance in extensive evaluation with seven benchmarks across classification (coarse and fine-grained), robustness, calibration, object detection, and transfer learning tasks. Project page is available at \href{https://fracmix-data-augmentation.github.io/}{fracmix-data-augmentation.github.io}
匹配关键词: self-consistency
---

[ACADEMIC - ARXIV]
标题: Uncertainty Quantification for Computer-Use Agents: A Benchmark across Vision-Language Models and GUI Grounding Datasets
作者: Divake Kumar, Sina Tayebati, Devashri Naik, Amanda Sofie Rios, Nilesh Ahuja, Omesh Tickoo, Ranganath Krishnan, Amit Ranjan Trivedi
链接: https://arxiv.org/abs/2606.25760v1
完整摘要: Computer-use agents turn vision-language model (VLM) predictions into executable GUI clicks, so reliable uncertainty estimates are essential for rejection, calibration, miss-severity ranking, and spatial safety regions. Yet evidence on post-hoc uncertainty quantification (UQ) for these agents is fragmented across isolated model and dataset pairs, leaving it unclear whether UQ rankings stay stable when the agent, benchmark, or observable interface changes. We present Argus, a cross-regime benchmark for post-hoc UQ in single-step executable GUI grounding: a 27-method open-weight matrix over 4 VLM agents and 4 datasets, plus an 8-method closed-source matrix across 3 frontier vendors where logits, hidden states, and attention maps are unavailable. Evaluated methods span logit-based scores, sampling and consistency measures, hidden-state and density estimators (Mahalanobis, SAPLMA), attention-based scores, P(True) and verbalised-confidence prompting, and split-conformal prediction. The main finding is selective transfer: UQ rankings are stable across datasets for a fixed model, but degrade across model classes and observable interfaces. Hidden-state and density methods are the most stable open-weight family, while CoCoA-1MCA, Focus, sampling-based scores, and verbalised self-assessment win in specific regimes. Within-model ranking transfer is strong (Spearman rho up to 0.969), but cross-tier transfer to closed-source vendors averages only +0.08, so closed-source UQ should be reranked on the target rather than extrapolated. Conformal click regions show score-level discrimination is not enough for deployment: locally weighted disks shrink radii by 40-60% when the plug-in UQ is calibrated, but coverage degrades under calibration-test or interface mismatch. We release per-item records, calibration/test splits, UQ scores, and analysis scripts for regime-aware UQ selection in GUI agents.
匹配关键词: self-consistency
---

[ACADEMIC - ARXIV]
标题: SFL-MTSC: Leveraging Semantic Frame-Level Multi-Task Self-Consistency for Robust Multi-Intent Spoken Language Understanding
作者: Po-Yen Chen, Berlin Chen
链接: https://arxiv.org/abs/2606.25552v1
完整摘要: Prompt-based spoken language understanding (SLU) with large language models (LLMs) often suffers from inconsistent intent--slot structures due to decoding stochasticity, particularly in multi-intent scenarios. In view of this, we propose Semantic Frame-Level Multi-Task Self-Consistency (SFL-MTSC), a novel structured aggregation framework operating at the semantic frame level. Instead of output-level majority voting, SFL-MTSC decomposes predictions into intent-specific frames, applies domain--intent grouping and slot-level clustering, and evaluates cluster reliability using path support scoring. Reliable frames are retained and re-integrated to form the final prediction. Zero-shot experiments on the MAC-SLU benchmark dataset show improved slot F1 and overall accuracy over single-path inference, while intent accuracy remains largely stable across most settings.
匹配关键词: self-consistency
---

[ACADEMIC - ARXIV]
标题: Learning Action Priors for Cross-embodiment Robot Manipulation
作者: Dong Jing, Tianqi Zhang, Jiaqi Liu, Jinman Zhao, Zelong Sun, Li Erran Li, Zhiwu Lu, Mingyu Ding
链接: https://arxiv.org/abs/2606.26095v1
完整摘要: Most Vision-Language-Action (VLA) models build on a Vision-Language Model (VLM) backbone by attaching an action module and optimizing the full policy jointly. This design inherits strong visual and linguistic priors from the VLM, but leaves the action module to learn physical motion almost from scratch. As a result, the policy lacks an explicit motion prior, forcing early optimization to simultaneously discover temporal action dynamics and cross-modal alignment, a challenge further amplified in cross-embodiment settings. In this work, we propose to pretrain the action module with motion priors before cross-modal VLA alignment. Specifically, we introduce a two-stage training framework that equips the action module with cross-embodiment temporal motion structure before VLA training begins. In Stage~1, a lightweight flow-matching-based encoder-decoder action module efficiently learns temporal motion structure solely from unconditioned action trajectories, without processing visual or language tokens. In Stage~2, this learned prior is transferred to VLA training through decoder reuse and early-stage latent distillation, aligning visual-language features with the action embedding space while still allowing end-to-end policy refinement. In addition, the trained encoder serves as a compact history compressor, summarizing state-action histories into a single temporal context token for history-aware modeling at negligible cost. Extensive experiments across 13 diverse cross-embodiment tasks on both simulated and real-world platforms validate the effectiveness of our approach. Compared with VLA training without action priors, our model achieves faster convergence, higher success rates, and substantially stronger performance on data-scarce real-world tasks. Moreover, scaling up the action data in Stage~1 yields a more generalizable action prior that directly improves downstream VLA performance.
匹配关键词: process reward
---

[ACADEMIC - ARXIV]
标题: Neglected Free Lunch from Post-training: Progress Advantage for LLM Agents
作者: Changdae Oh, Wendi Li, Seongheon Park, Samuel Yeh, Tanwi Mallick, Sharon Li
链接: https://arxiv.org/abs/2606.26080v1
完整摘要: Process reward models enable fine-grained, step-level evaluation of LLMs, yet building them for agentic settings remains prohibitively difficult: long-horizon interactions, irreversible actions, and stochastic environment feedback make both human annotation and Monte Carlo estimation infeasible at scale. In this work, we show that reinforcement learning (RL) post-training already provides the ingredients for effective step-level scoring, eliminating the need for dedicated reward model training altogether. Concretely, we derive an implicit advantage under a general stochastic Markov decision process, which we term progress advantage -- log-probability ratio between the RL-trained policy and its reference policy exactly recovers the optimal advantage function. This formulation makes the resulting signal annotation-free, domain-agnostic, and available as a byproduct of the standard RL post-training pipeline. We validate the effectiveness of the progress advantage across three different applications: test-time scaling, uncertainty quantification, and failure attribution on five benchmarks and four model families. Across all settings, it consistently outperforms confidence-based baselines and, despite requiring no task-specific training, surpasses dedicated trained reward models. We complement these results with deeper analyses on characteristics of progress advantage, offering practical guidance for adoption in real-world agentic systems.
匹配关键词: process reward
---

[ACADEMIC - ARXIV]
标题: A cross-process welding penetration status prediction algorithm based on unsupervised domain adaptation in laser and TIG welding
作者: Sen Li, Haichao Cui, Chendong Shao, Yaqi Wang, Xinhua Tang
链接: https://arxiv.org/abs/2606.26078v1
完整摘要: Supervised deep learning has been widely used for weld penetration state classification; however, its performance often degrades significantly under domain shift, such as when transferring models between welding processes with distinct physical mechanisms:for instance, from arc-dominated tungsten inert gas (TIG) welding to keyhole-based laser welding. To overcome this limitation, we propose an unsupervised domain adaptation (UDA) framework integrated with a gradual source domain expansion (GSDE) strategy. Evaluated on dedicated TIG and laser welding datasets, our approach achieves high accuracy in both same-process and cross-process transfer tasks. Specifically, it attains average accuracies of 90.65% on TIGFH and 90.72% on LSPS in same-process settings, surpassing a supervised baseline by 35.83% and 38.87%, respectively. More notably, in cross-process scenarios, it reaches 80.48% for TIG to Laser and 81.13% for Laser to TIG, improving upon the baseline by 43.39% and 43.40%. UMAP visualizations verify that the model learns domain-invariant features while maintaining discriminative class boundaries. This method considerably lowers the relabeling cost for new welding processes and enhances the versatility of intelligent monitoring across different welding systems.
匹配关键词: process reward
---

[ACADEMIC - ARXIV]
标题: A welding penetration prediction model for laser welding process based on self-supervised learning using physics-informed neural networks
作者: Sen Li, Xiaoying Liu, Xiaojian Xu, Chendong Shao, Yaqi Wang, Ling Lan, Xinhua Tang, Haichao Cui
链接: https://arxiv.org/abs/2606.26059v1
完整摘要: The laser welding full-penetration is of critical importance, as it constitutes one of the fundamental factors in achieving defect-free welded joints. Accurate prediction of the penetration state is therefore essential for ensuring weld quality. To this end, this paper introduces SimPhysNet, a novel algorithm that achieves high classification accuracy in laser welding penetration prediction using only a limited number of labelled images. This approach effectively overcomes the limitations of supervised learning classification algorithms, which are hindered in industrial applications by their dependence on extensive, high-quality labelled data. The core of SimPhysNet is a unique self-supervised learning paradigm that embeds physical priors into a contrastive learning framework. By incorporating a physics-informed neural network (PINN), the model is guided to extract physically meaningful features of the molten pool and keyhole from a large set of unlabelled data, while three image augmentation tasks further enhance its generalization capabilities. Subsequently, a few-shot learning strategy, based on prototypical networks, enables robust classification by constructing class representations from a minimal set of labelled images. Experimental results demonstrate that SimPhysNet achieves a classification accuracy of 96.06% using only 200 labelled images (approximately 5% of the total labelled dataset), which is comparable to the performance of conventional supervised learning algorithms that utilize the entire labelled dataset. This work presents a new, efficient, and highly accurate method, providing the way for the intelligent automation of laser welding.
匹配关键词: process reward
---

[ACADEMIC - ARXIV]
标题: The Unfireable Safety Kernel: Execution-Time AI Alignment for AI Agents and Other Escapable AI Systems
作者: Seth Dobrin, Łukasz Chmiel
链接: https://arxiv.org/abs/2606.26057v1
完整摘要: AI agents are granted access to tools, APIs, and other infrastructure, making them active principals in those systems. The dominant approach places controls inside the agent's own runtime: system prompts, output filters, and guardrail libraries. Any control in the agent's address space is reachable by inputs that influence it; this generalizes to any AI system with sufficient reach into its own runtime, a class we term escapable AI systems. We identify four properties that an authorization mechanism must satisfy for architectural control rather than for cooperative requests: process separation, pre-action enforcement on a structurally only path, fail-closed at both the request and system levels, and externalized signed evidence verifiable outside the controlled system's trust boundary. We position this layer as execution-time AI alignment, complementing training-time alignment (RLHF, Constitutional AI) and inference-time alignment. We present the Unfireable Safety Kernel, a Rust reference implementation realizing all four. Its fail-closed invariant is machine-checked at two levels: an SMT theorem (Z3) and an exhaustive bounded-model-checking proof of the production decision function (Kani, 4/4 harnesses). A Python-to-Rust migration was gated on byte-equivalence (1000/1000 fixtures; 17/17 adversarial classes). We evaluate the kernel governing a live, escapable AI system, a deterministic, self-improving world model, against an escape-seeking adversary driving its real self-modification seam: across 1,000 self-modifications, all 704 attempts on the safety-critical core are refused, with no escape; a further 300, under the operator kill switch, are also refused. A separate campaign of 6,240 authorization round-trips had no successful bypass. Against 3 contemporary systems claiming the agent control plane, the agent invokes control; here, it lacks that choice.
匹配关键词: process reward
---

[ACADEMIC - ARXIV]
标题: Learning Action Priors for Cross-embodiment Robot Manipulation
作者: Dong Jing, Tianqi Zhang, Jiaqi Liu, Jinman Zhao, Zelong Sun, Li Erran Li, Zhiwu Lu, Mingyu Ding
链接: https://arxiv.org/abs/2606.26095v1
完整摘要: Most Vision-Language-Action (VLA) models build on a Vision-Language Model (VLM) backbone by attaching an action module and optimizing the full policy jointly. This design inherits strong visual and linguistic priors from the VLM, but leaves the action module to learn physical motion almost from scratch. As a result, the policy lacks an explicit motion prior, forcing early optimization to simultaneously discover temporal action dynamics and cross-modal alignment, a challenge further amplified in cross-embodiment settings. In this work, we propose to pretrain the action module with motion priors before cross-modal VLA alignment. Specifically, we introduce a two-stage training framework that equips the action module with cross-embodiment temporal motion structure before VLA training begins. In Stage~1, a lightweight flow-matching-based encoder-decoder action module efficiently learns temporal motion structure solely from unconditioned action trajectories, without processing visual or language tokens. In Stage~2, this learned prior is transferred to VLA training through decoder reuse and early-stage latent distillation, aligning visual-language features with the action embedding space while still allowing end-to-end policy refinement. In addition, the trained encoder serves as a compact history compressor, summarizing state-action histories into a single temporal context token for history-aware modeling at negligible cost. Extensive experiments across 13 diverse cross-embodiment tasks on both simulated and real-world platforms validate the effectiveness of our approach. Compared with VLA training without action priors, our model achieves faster convergence, higher success rates, and substantially stronger performance on data-scarce real-world tasks. Moreover, scaling up the action data in Stage~1 yields a more generalizable action prior that directly improves downstream VLA performance.
匹配关键词: pretraining
---

[ACADEMIC - ARXIV]
标题: Natural Ungrokking: Asymmetric Control of Which Rules Survive Pretraining
作者: Juliana Li, Diya Sreedhar
链接: https://arxiv.org/abs/2606.26050v1
完整摘要: Midway through an ordinary pretraining run, a small language model learns the pronoun-gender rule: cued with a girl's name ("Sue cried because"), it resolves the next pronoun to she, generalizing to held-out probes (0.94 by step 925). By step 3,500 the same model scores near zero on the same probes, although the rule's evidence is still in the training data. We call this within-run reversal natural ungrokking: the corpus decides, with no trace in the loss curve, which learned rules a model keeps. Which rules survive is predictable from one corpus statistic: how often the training stream shows the rule winning. Across un-intervened runs (two corpora, three budgets, three seeds), support frequency decides a rule's fate; the data-to-parameter ratio only modulates how deeply a doomed rule falls. The same emerge-then-collapse dynamics appear in public Pythia checkpoints, collapse depth ordered by model scale as predicted. The forgetting is a displacement: a competing surface pattern out-competes the rule, and the log-probability margin between them crosses zero within 100 training steps of the behavioral collapse. Control over this fate is asymmetric: the same edit that destroys a rule on demand cannot restore it. Flipping support to counter-evidence in place kills the rule with monotone dose-response in two unrelated rules; but injecting support back, even to 450 times the level that naturally sustains it, buys no recovery. Every confirmatory threshold and prediction was pre-registered before the data it governed was read.
匹配关键词: pretraining
---

[ACADEMIC - ARXIV]
标题: Dziri Voicebot: An End-to-End Low-Resource Speech-to-Speech Conversational System for Algerian Dialect
作者: Dihia Lanasri, Fairouz Taki, Asma Kemmoum
链接: https://arxiv.org/abs/2606.26003v1
完整摘要: Automatic speech and language technologies are still heavily biased toward high-resource languages, limiting their applicability to dialectal and low-resource settings such as Algerian Dialect. This language presents additional challenges including lack of standardized orthography, frequent codeswitching with French, and scarcity of annotated speech resources. This paper addresses the problem of building a complete speech-to-speech conversational system for Algerian Dialect. We propose a modular pipeline integrating automatic speech recognition, natural language understanding, retrieval-augmented generation, and text-to-speech synthesis within a unified architecture. This work is the continuation of our previous work on Algerian dialectal conversational systems Bechiri and Lanasri [2026], extending it from text-based dialogue modeling to full speech-based interaction. We constructed dedicated datasets for ASR, NLU, and TTS in the telecom domain and fine-tune pretrained models for each component. The ASR system is built on Whisper-based adaptation, while the NLU module combines transformer-based embeddings with a task-oriented dialogue framework. A neural TTS system is trained on a newly collected dialectal corpus to enable spoken response generation. Experimental results show strong performance across all components, including low word error rate for ASR, high intent classification and entity recognition scores for NLU, and stable speech synthesis quality. The proposed system provides a reproducible baseline for end-to-end conversational modeling in Algerian Dialect.
匹配关键词: pretraining
---

[ACADEMIC - ARXIV]
标题: Action ControlNet: A Lightweight Delay-Aware Adapter for Smooth Asynchronous Control in Vision-Language-Action Models
作者: Tiecheng Guo, Meng Guo
链接: https://arxiv.org/abs/2606.25985v1
完整摘要: Vision-language-action (VLA) models have shown strong potential for general-purpose robot manipulation, but their inference latency remains a major obstacle to stable high-frequency control. Asynchronous execution mitigates this bottleneck by overlapping policy inference with action execution, yet the next action chunk is still predicted from stale observations while the robot continues to move. Direct chunk stitching therefore introduces handoff discontinuities, action jitter, and failures in contact-rich manipulation. Existing remedies typically require either full-policy retraining or architecture-specific runtime logic. This work proposes Action ControlNet (ACNet), a lightweight delay-aware adapter that uses the executed motion suffix as a residual condition for a mostly frozen action head. ACNet leaves the pretrained backbone unchanged, introduces few trainable parameters, and remains compatible with generative action heads such as diffusion and flow matching. On Kinetix, Meta-World MT50, and a real-world SO-ARM101 platform, ACNet improves robustness under inference delay and yields smoother asynchronous trajectories than direct chunk stitching, while remaining more lightweight than full delay-conditioned retraining.
匹配关键词: pretraining
---

[ACADEMIC - ARXIV]
标题: SurgAtlas: A Large-Scale Surgical Video-Language Dataset with 2,391 Hours of Open and Minimally Invasive Surgery
作者: Filippos Bellos, Andre S. Gala-Garza, Miaowei Wang, Alyssa M. Hardin, Ahmad M. Hider, Yayuan Li, Jing Bi, Susan Liang, Chenliang Xu, Donald S. Likosky, Jason J. Corso
链接: https://arxiv.org/abs/2606.25905v1
完整摘要: We introduce SurgAtlas, the largest surgical video-language dataset to date, comprising 15,291 videos (2,391 hours) spanning 18 surgical specialties and over 5,000 procedure types, sourced entirely from publicly available YouTube content. SurgAtlas is also the first surgical video-language dataset to include open surgery at scale, with 6,182 open procedure videos alongside over 9,000 minimally invasive recordings, and the first to establish standardized benchmarks for open-surgery video understanding. We additionally provide an expert-validated subset with verified visual question-answer pairs across diverse open and minimally invasive procedures, serving as a clinically grounded benchmark for surgical reasoning. Compared with existing surgical video-language datasets, SurgAtlas provides one of the most diverse annotation schemas, combining segment-level captions, step- and phase-level descriptions, video-level surgical descriptions, and reasoning-oriented question-answer pairs organized within a hierarchical taxonomy. These annotations are constructed through an automated multi-tier pipeline with LLM-based enrichment and a staged VQA generation framework with explicit groundedness verification. The scale and diversity of SurgAtlas enable training surgical foundation models with broad procedural coverage: we finetune Qwen3-VL-8B through a two-stage captioning-then-instruction pipeline and achieve competitive or state-of-the-art results on multiple established surgical benchmarks, including phase recognition, triplet detection, and reasoning question answering. More broadly, SurgAtlas provides a large native public video corpus that can support future large-scale pretraining of multimodal surgical AI systems and contribute to the development of next-generation foundation models for surgery.
匹配关键词: pretraining
---

[ACADEMIC - ARXIV]
标题: Learning Action Priors for Cross-embodiment Robot Manipulation
作者: Dong Jing, Tianqi Zhang, Jiaqi Liu, Jinman Zhao, Zelong Sun, Li Erran Li, Zhiwu Lu, Mingyu Ding
链接: https://arxiv.org/abs/2606.26095v1
完整摘要: Most Vision-Language-Action (VLA) models build on a Vision-Language Model (VLM) backbone by attaching an action module and optimizing the full policy jointly. This design inherits strong visual and linguistic priors from the VLM, but leaves the action module to learn physical motion almost from scratch. As a result, the policy lacks an explicit motion prior, forcing early optimization to simultaneously discover temporal action dynamics and cross-modal alignment, a challenge further amplified in cross-embodiment settings. In this work, we propose to pretrain the action module with motion priors before cross-modal VLA alignment. Specifically, we introduce a two-stage training framework that equips the action module with cross-embodiment temporal motion structure before VLA training begins. In Stage~1, a lightweight flow-matching-based encoder-decoder action module efficiently learns temporal motion structure solely from unconditioned action trajectories, without processing visual or language tokens. In Stage~2, this learned prior is transferred to VLA training through decoder reuse and early-stage latent distillation, aligning visual-language features with the action embedding space while still allowing end-to-end policy refinement. In addition, the trained encoder serves as a compact history compressor, summarizing state-action histories into a single temporal context token for history-aware modeling at negligible cost. Extensive experiments across 13 diverse cross-embodiment tasks on both simulated and real-world platforms validate the effectiveness of our approach. Compared with VLA training without action priors, our model achieves faster convergence, higher success rates, and substantially stronger performance on data-scarce real-world tasks. Moreover, scaling up the action data in Stage~1 yields a more generalizable action prior that directly improves downstream VLA performance.
匹配关键词: foundation model
---

[ACADEMIC - ARXIV]
标题: RevengeBench: Reverse Engineering Code-Space Policies from Behavioral Experiments
作者: Babak Rahmani, Sebastian Dziadzio, Joschka Strüber, Sergio Hernández-Gutiérrez, Matthias Bethge
链接: https://arxiv.org/abs/2606.26094v1
完整摘要: For most of scientific history, researchers studying behavior could only infer hidden mechanisms from outward actions: an inverse problem that becomes more tractable when observation is augmented by targeted intervention. We pose a computational analogue: given only behavioral traces of an agent in a game environment, can a learner reconstruct the underlying decision program as executable code, and how much does this reconstruction improve with the ability to design controlled experiments? We introduce RevengeBench, a benchmark of 75 LLM generated, Elo-calibrated policies across five game environments, drawn from CodeClash tournament trajectories. The learner observes the hidden target policy play against sampled opponents and designs behavioral probes in the form of custom opponent policies that elicit informative behavior. It then submits an executable hypothesis, which is evaluated using continuous action-distance metrics. We further validate that recovered code carries informative signal in downstream player-versus-player tournaments. Across twelve frontier LLMs, recovery quality varies substantially (34 to 72% of initial distance closed), with reconstructed policies yielding measurable competitive advantage, particularly for weaker models that otherwise struggle to design effective counter-strategies. Our benchmark positions behavioral recovery of programmatic policies as a tractable inverse problem in code-space, opening a path to opponent modeling, policy interpretability, and the broader question of inferring latent mechanisms from observations.
匹配关键词: foundation model
---

[ACADEMIC - ARXIV]
标题: ForceBand: Learning Forceful Manipulation with sEMG
作者: Botao He, Zhi Wang, Linna Kuang, Ishaan Ghosh, Jitendra Malik, Cornelia Fermuller, Tingfan Wu, Jiayuan Mao, Ruoshi Liu, Haozhi Qi, Yiannis Aloimonos
链接: https://arxiv.org/abs/2606.26093v1
完整摘要: Human demonstrations are a scalable data source for learning robot manipulation policies. However, common sources of human demonstration data, such as motion-capture trajectories and internet videos, capture mostly motion and appearance while missing the contact forces that are critical for force-sensitive manipulation. In this paper, we introduce ForceBand, a low-cost wrist-worn sEMG system that turns human muscle activity into force-enriched demonstrations. We first collect a 10-hour multimodal dataset containing egocentric video, sEMG, IMU, and fingertip force measurements across diverse actions and objects. Using this dataset, we pre-train an EMG2Force model that predicts per-finger forces from sEMG and IMU signals. After a short user-specific calibration, users can collect target-task demonstrations using only ForceBand and video; EMG2Force then labels these demonstrations with per-finger force traces, producing force-augmented demonstrations for robot policy learning. Experiments show that ForceBand recovers fine-grained fingertip interactions with over 50% lower force prediction error than vision-based baselines and achieves an 87% success rate on pick, squeeze, and place tasks that require object-specific force control across objects with diverse shapes, sizes, and weights. Project website: https://forceband-emg.github.io
匹配关键词: foundation model
---

[ACADEMIC - ARXIV]
标题: TryOnCrafter: Unleashing Camera Trajectories for Realistic Video Virtual Try-on via a Renderable 4D Try-on Proxy
作者: Hao Sun, Hao Yan, Mengting Chen, Quanjian Song, Yu Li, Juan Cao, Jinsong Lan, Xiaoyong Zhu, Bo Zheng, Sheng Tang
链接: https://arxiv.org/abs/2606.26092v1
完整摘要: While Video Virtual Try-on (VVT) has achieved remarkable progress in synthesizing realistic garment overlays on dynamic subjects, existing paradigms remains fundamentally constrained by a passive dependency on source camera trajectories, failing to accommodate the requisite interactive freedom for omnidirectional viewpoint exploration. To address this limitation, we define a pioneering research frontier: Camera-controllable Video Virtual Try-on (CaM-VVT). Unlike conventional VVT, CaM-VVT not only necessitates viewpoint-agnostic texture hallucination but also strict structural synchronization between non-rigid human dynamics and background contexts under arbitrary, unconstrained camera movements. To tackle these challenges, we present TryOnCrafter, the first unified DiT-based framework specifically architected for the CaM-VVT task. Departing from implicit pixel-space manipulation, we introduce a Renderable 4D Try-on Proxy that explicitly decouples the human subject from the environment. This is achieved by distilling high-fidelity 2D try-on priors into a clothed 3DGS-based avatar, which is subsequently animated via SMPL-X sequences and metric-aligned into a reconstructed background point cloud. This proxy establishes a robust structural foundation with superior texture density and motion integrity. Our Proxy-Anchored Video DiT leverages this robust structural foundation as a primary geometric anchor, ensuring that the synthesized photorealistic videos are strictly constrained by prescribed trajectories and physically plausible deformations. Benefiting from the inherent editability of the 4D proxy, TryOnCrafter facilitates diverse downstream applications, including human relocalization, ``bullet time'' effects, and $360$-degree orbital viewing.
匹配关键词: foundation model
---

[ACADEMIC - ARXIV]
标题: On-Policy Self-Distillation with Sampled Demonstrations Reduces Output Diversity
作者: Andrei Liviu Nicolicioiu, Mohammad Pezeshki, Aaron Courville
链接: https://arxiv.org/abs/2606.26091v1
完整摘要: On-policy self-distillation achieves strong pass@1 accuracy by using a single model as both teacher and student, with the teacher conditioned on a correct demonstration to provide dense token-level feedback. We show that this could come at a hidden cost: rollout diversity decreases and pass@k curves flatten (i.e., generating more rollouts fails to improve accuracy). We trace this to compounding biases in the design of self-distillation with sampled demonstrations. The teacher scores each student rollout while conditioned on a sampled correct rollout, channeling its feedback through the model's own biases. We theoretically analyze the optimal self-distillation policy and show that it tilts the base distribution by a pointwise conditional mutual information score between the student's rollout and the correct rollout used as context. Unlike the ideal optimal on-policy reinforcement learning (RL), which preserves probability ratios among equally correct rollouts, self-distillation can amplify existing probability gaps, concentrating mass on already-dominant modes. On a controlled graph path-finding task and science question-answering benchmarks, self-distilled models match or exceed RL on average performance but exhibit substantially lower functional and semantic diversity, failing on out-of-distribution settings that require diverse strategies.
匹配关键词: foundation model
---

[ACADEMIC - ARXIV]
标题: Learning Action Priors for Cross-embodiment Robot Manipulation
作者: Dong Jing, Tianqi Zhang, Jiaqi Liu, Jinman Zhao, Zelong Sun, Li Erran Li, Zhiwu Lu, Mingyu Ding
链接: https://arxiv.org/abs/2606.26095v1
完整摘要: Most Vision-Language-Action (VLA) models build on a Vision-Language Model (VLM) backbone by attaching an action module and optimizing the full policy jointly. This design inherits strong visual and linguistic priors from the VLM, but leaves the action module to learn physical motion almost from scratch. As a result, the policy lacks an explicit motion prior, forcing early optimization to simultaneously discover temporal action dynamics and cross-modal alignment, a challenge further amplified in cross-embodiment settings. In this work, we propose to pretrain the action module with motion priors before cross-modal VLA alignment. Specifically, we introduce a two-stage training framework that equips the action module with cross-embodiment temporal motion structure before VLA training begins. In Stage~1, a lightweight flow-matching-based encoder-decoder action module efficiently learns temporal motion structure solely from unconditioned action trajectories, without processing visual or language tokens. In Stage~2, this learned prior is transferred to VLA training through decoder reuse and early-stage latent distillation, aligning visual-language features with the action embedding space while still allowing end-to-end policy refinement. In addition, the trained encoder serves as a compact history compressor, summarizing state-action histories into a single temporal context token for history-aware modeling at negligible cost. Extensive experiments across 13 diverse cross-embodiment tasks on both simulated and real-world platforms validate the effectiveness of our approach. Compared with VLA training without action priors, our model achieves faster convergence, higher success rates, and substantially stronger performance on data-scarce real-world tasks. Moreover, scaling up the action data in Stage~1 yields a more generalizable action prior that directly improves downstream VLA performance.
匹配关键词: scaling law
---

[ACADEMIC - ARXIV]
标题: Neglected Free Lunch from Post-training: Progress Advantage for LLM Agents
作者: Changdae Oh, Wendi Li, Seongheon Park, Samuel Yeh, Tanwi Mallick, Sharon Li
链接: https://arxiv.org/abs/2606.26080v1
完整摘要: Process reward models enable fine-grained, step-level evaluation of LLMs, yet building them for agentic settings remains prohibitively difficult: long-horizon interactions, irreversible actions, and stochastic environment feedback make both human annotation and Monte Carlo estimation infeasible at scale. In this work, we show that reinforcement learning (RL) post-training already provides the ingredients for effective step-level scoring, eliminating the need for dedicated reward model training altogether. Concretely, we derive an implicit advantage under a general stochastic Markov decision process, which we term progress advantage -- log-probability ratio between the RL-trained policy and its reference policy exactly recovers the optimal advantage function. This formulation makes the resulting signal annotation-free, domain-agnostic, and available as a byproduct of the standard RL post-training pipeline. We validate the effectiveness of the progress advantage across three different applications: test-time scaling, uncertainty quantification, and failure attribution on five benchmarks and four model families. Across all settings, it consistently outperforms confidence-based baselines and, despite requiring no task-specific training, surpasses dedicated trained reward models. We complement these results with deeper analyses on characteristics of progress advantage, offering practical guidance for adoption in real-world agentic systems.
匹配关键词: scaling law
---

[ACADEMIC - ARXIV]
标题: Natural Ungrokking: Asymmetric Control of Which Rules Survive Pretraining
作者: Juliana Li, Diya Sreedhar
链接: https://arxiv.org/abs/2606.26050v1
完整摘要: Midway through an ordinary pretraining run, a small language model learns the pronoun-gender rule: cued with a girl's name ("Sue cried because"), it resolves the next pronoun to she, generalizing to held-out probes (0.94 by step 925). By step 3,500 the same model scores near zero on the same probes, although the rule's evidence is still in the training data. We call this within-run reversal natural ungrokking: the corpus decides, with no trace in the loss curve, which learned rules a model keeps. Which rules survive is predictable from one corpus statistic: how often the training stream shows the rule winning. Across un-intervened runs (two corpora, three budgets, three seeds), support frequency decides a rule's fate; the data-to-parameter ratio only modulates how deeply a doomed rule falls. The same emerge-then-collapse dynamics appear in public Pythia checkpoints, collapse depth ordered by model scale as predicted. The forgetting is a displacement: a competing surface pattern out-competes the rule, and the log-probability margin between them crosses zero within 100 training steps of the behavioral collapse. Control over this fate is asymmetric: the same edit that destroys a rule on demand cannot restore it. Flipping support to counter-evidence in place kills the rule with monotone dose-response in two unrelated rules; but injecting support back, even to 450 times the level that naturally sustains it, buys no recovery. Every confirmatory threshold and prediction was pre-registered before the data it governed was read.
匹配关键词: scaling law
---

[ACADEMIC - ARXIV]
标题: RoboAtlas: Contextual Active SLAM
作者: Alexander Schperberg, Shivam K. Panda, Abraham P. Vinod, M. K. Jawed, Stefano Di Cairano
链接: https://arxiv.org/abs/2606.26046v1
完整摘要: We present RoboAtlas, a contextual Active SLAM framework that adaptively balances geometric exploration and semantic reasoning using a scalable 3D semantic mapping system, OpenRoboVox. RoboAtlas integrates frontier exploration, global semantic-map reasoning, and egocentric VLM-based reasoning through a contextual multi-armed bandit that transitions from exploration to semantically guided navigation as scene understanding improves. We evaluate the system in simulation and on a Unitree Go2 robot in large-scale real-world environments exceeding 1800 m2 with approx. 30k mapped semantic instances, achieving a 100% task success rate. On the GOAT-Bench "Val Unseen" benchmark, RoboAtlas achieves state-of-the-art performance with highest reported success rate (SR) of 90.6%, using GPT-4o, improving over the strongest prior baseline by 17.8 percentage points in SR. Using the much smaller Qwen2.5-VL-7B model, it still achieves 88.8% SR, outperforming all baselines using GPT-4o in SR, and revealing the importance of the information gained by our semantic mapping framework over simply replacing the underlying foundation model. The results demonstrate that grounding foundation models with large-scale 3D semantic maps enables robust and efficient contextual Active SLAM.
匹配关键词: scaling law
---

[ACADEMIC - ARXIV]
标题: TriViewBench: Controlled Complexity Scaling for Multi-View Structural Reasoning in MLLMs
作者: Yu-Yang Chen, Lan-Zhe Guo
链接: https://arxiv.org/abs/2606.26029v1
完整摘要: Multimodal Large Language Models (MLLMs) demonstrate strong performance on standard visual question answering benchmarks, yet their scalability under controlled structural complexity remains poorly understood. We introduce TriViewBench, a controlled three-view visual reasoning benchmark constructed from synthetic 3D scenes with explicitly parameterized object count and occlusion. The benchmark contains 1,923 scenes and over 14K Question-Answer (QA) pairs organized into four complexity levels and three reasoning categories: Local Decision, Object Counting, and Global Recovery. We evaluate 18 open- and closed-source MLLMs under a unified prompting protocol. All 18 models exhibit an identical capability hierarchy without exception (Local Decision > Object Counting > Global Recovery), and performance degrades monotonically with complexity: Local Decision tasks decline modestly (12.11% relative drop), while Object Counting degrades substantially (59.14%) and Global Recovery collapses severely (80.02%). Error analysis on Object Counting reveals two mechanistically independent failure modes: single-view tasks are dominated by undercounting due to occlusion blindness, whereas the multi-view task reverses to overcounting due to cross-view identity confusion. Chain-of-Thought (CoT) prompting yields near-zero overall benefit ($Δ= -0.16\%$) and its effect on Global Recovery is strongly capability-gated, suggesting that the bottleneck lies in cross-view spatial representation rather than reasoning strategy. These findings reveal fundamental scalability limitations in current MLLMs and position TriViewBench as a controlled diagnostic framework for analyzing structural reasoning failures.
匹配关键词: scaling law
---

[ACADEMIC - ARXIV]
标题: Learning Action Priors for Cross-embodiment Robot Manipulation
作者: Dong Jing, Tianqi Zhang, Jiaqi Liu, Jinman Zhao, Zelong Sun, Li Erran Li, Zhiwu Lu, Mingyu Ding
链接: https://arxiv.org/abs/2606.26095v1
完整摘要: Most Vision-Language-Action (VLA) models build on a Vision-Language Model (VLM) backbone by attaching an action module and optimizing the full policy jointly. This design inherits strong visual and linguistic priors from the VLM, but leaves the action module to learn physical motion almost from scratch. As a result, the policy lacks an explicit motion prior, forcing early optimization to simultaneously discover temporal action dynamics and cross-modal alignment, a challenge further amplified in cross-embodiment settings. In this work, we propose to pretrain the action module with motion priors before cross-modal VLA alignment. Specifically, we introduce a two-stage training framework that equips the action module with cross-embodiment temporal motion structure before VLA training begins. In Stage~1, a lightweight flow-matching-based encoder-decoder action module efficiently learns temporal motion structure solely from unconditioned action trajectories, without processing visual or language tokens. In Stage~2, this learned prior is transferred to VLA training through decoder reuse and early-stage latent distillation, aligning visual-language features with the action embedding space while still allowing end-to-end policy refinement. In addition, the trained encoder serves as a compact history compressor, summarizing state-action histories into a single temporal context token for history-aware modeling at negligible cost. Extensive experiments across 13 diverse cross-embodiment tasks on both simulated and real-world platforms validate the effectiveness of our approach. Compared with VLA training without action priors, our model achieves faster convergence, higher success rates, and substantially stronger performance on data-scarce real-world tasks. Moreover, scaling up the action data in Stage~1 yields a more generalizable action prior that directly improves downstream VLA performance.
匹配关键词: language model
---

[ACADEMIC - ARXIV]
标题: RevengeBench: Reverse Engineering Code-Space Policies from Behavioral Experiments
作者: Babak Rahmani, Sebastian Dziadzio, Joschka Strüber, Sergio Hernández-Gutiérrez, Matthias Bethge
链接: https://arxiv.org/abs/2606.26094v1
完整摘要: For most of scientific history, researchers studying behavior could only infer hidden mechanisms from outward actions: an inverse problem that becomes more tractable when observation is augmented by targeted intervention. We pose a computational analogue: given only behavioral traces of an agent in a game environment, can a learner reconstruct the underlying decision program as executable code, and how much does this reconstruction improve with the ability to design controlled experiments? We introduce RevengeBench, a benchmark of 75 LLM generated, Elo-calibrated policies across five game environments, drawn from CodeClash tournament trajectories. The learner observes the hidden target policy play against sampled opponents and designs behavioral probes in the form of custom opponent policies that elicit informative behavior. It then submits an executable hypothesis, which is evaluated using continuous action-distance metrics. We further validate that recovered code carries informative signal in downstream player-versus-player tournaments. Across twelve frontier LLMs, recovery quality varies substantially (34 to 72% of initial distance closed), with reconstructed policies yielding measurable competitive advantage, particularly for weaker models that otherwise struggle to design effective counter-strategies. Our benchmark positions behavioral recovery of programmatic policies as a tractable inverse problem in code-space, opening a path to opponent modeling, policy interpretability, and the broader question of inferring latent mechanisms from observations.
匹配关键词: language model
---

[ACADEMIC - ARXIV]
标题: ForceBand: Learning Forceful Manipulation with sEMG
作者: Botao He, Zhi Wang, Linna Kuang, Ishaan Ghosh, Jitendra Malik, Cornelia Fermuller, Tingfan Wu, Jiayuan Mao, Ruoshi Liu, Haozhi Qi, Yiannis Aloimonos
链接: https://arxiv.org/abs/2606.26093v1
完整摘要: Human demonstrations are a scalable data source for learning robot manipulation policies. However, common sources of human demonstration data, such as motion-capture trajectories and internet videos, capture mostly motion and appearance while missing the contact forces that are critical for force-sensitive manipulation. In this paper, we introduce ForceBand, a low-cost wrist-worn sEMG system that turns human muscle activity into force-enriched demonstrations. We first collect a 10-hour multimodal dataset containing egocentric video, sEMG, IMU, and fingertip force measurements across diverse actions and objects. Using this dataset, we pre-train an EMG2Force model that predicts per-finger forces from sEMG and IMU signals. After a short user-specific calibration, users can collect target-task demonstrations using only ForceBand and video; EMG2Force then labels these demonstrations with per-finger force traces, producing force-augmented demonstrations for robot policy learning. Experiments show that ForceBand recovers fine-grained fingertip interactions with over 50% lower force prediction error than vision-based baselines and achieves an 87% success rate on pick, squeeze, and place tasks that require object-specific force control across objects with diverse shapes, sizes, and weights. Project website: https://forceband-emg.github.io
匹配关键词: language model
---

[ACADEMIC - ARXIV]
标题: On-Policy Self-Distillation with Sampled Demonstrations Reduces Output Diversity
作者: Andrei Liviu Nicolicioiu, Mohammad Pezeshki, Aaron Courville
链接: https://arxiv.org/abs/2606.26091v1
完整摘要: On-policy self-distillation achieves strong pass@1 accuracy by using a single model as both teacher and student, with the teacher conditioned on a correct demonstration to provide dense token-level feedback. We show that this could come at a hidden cost: rollout diversity decreases and pass@k curves flatten (i.e., generating more rollouts fails to improve accuracy). We trace this to compounding biases in the design of self-distillation with sampled demonstrations. The teacher scores each student rollout while conditioned on a sampled correct rollout, channeling its feedback through the model's own biases. We theoretically analyze the optimal self-distillation policy and show that it tilts the base distribution by a pointwise conditional mutual information score between the student's rollout and the correct rollout used as context. Unlike the ideal optimal on-policy reinforcement learning (RL), which preserves probability ratios among equally correct rollouts, self-distillation can amplify existing probability gaps, concentrating mass on already-dominant modes. On a controlled graph path-finding task and science question-answering benchmarks, self-distilled models match or exceed RL on average performance but exhibit substantially lower functional and semantic diversity, failing on out-of-distribution settings that require diverse strategies.
匹配关键词: language model
---

[ACADEMIC - ARXIV]
标题: MVTrack4Gen: Multi-View Point Tracking as Geometric Supervision for 4D Video Generation
作者: JoungBin Lee, Jaewoo Jung, Jongmin Lee, Tongmin Kim, Hyunsung Kim, Takuya Narihira, Kazumi Fukuda, Jahyeok Koo, Jisang Han, Yuki Mitsufuji, Seungryong Kim
链接: https://arxiv.org/abs/2606.26087v1
完整摘要: Synthesizing a novel-view video from a monocular reference video along a target camera trajectory requires both geometric consistency and motion fidelity with respect to the reference video. Existing methods based on explicit 3D representations are limited by the accuracy of off-the-shelf reconstruction modules, which often produce inaccurate geometry for dynamic objects in monocular videos. In contrast, camera-conditioning-only methods can achieve high visual quality but often struggle to preserve geometric and motion consistency. In this work, we introduce MVTrack4Gen (Multi-View point Tracking for Novel-View Generation), a motion-aware training framework that leverages multi-view point tracking as an additional geometric and motion supervision signal for camera-conditioning-only novel-view video diffusion models. Our key finding is that specific attention layers encode strong correspondence cues, where query features attend to key features at geometrically corresponding locations across views and over time, and the misalignment of these correspondences causes motion inconsistency. Based on this observation, we route these features into an auxiliary multi-view tracking head and jointly train the diffusion model with a point-tracking objective. By explicitly strengthening these motion-aware correspondences, MVTrack4Gen improves existing models to better follow the motion in the reference view and maintain cross-view geometric consistency. Across diverse benchmarks, our method achieves state-of-the-art geometric consistency and competitive camera accuracy.
匹配关键词: language model
---

[ACADEMIC - ARXIV]
标题: FORCE: Efficient VLA Reinforcement Fine-Tuning via Value-Calibrated Warm-up and Self-Distillation
作者: Shuyi Zhang, Yunfan Lou, Hongyang Cheng, Yichen Guo, Chuyao Fu, Yaoxu Lyu, Xiaojie Zhang, Haoran Li, Pengwei Wang, Zhongyuan Wang, Shanghang Zhang
链接: https://arxiv.org/abs/2606.26006v1
完整摘要: Vision-Language-Action (VLA) models are often constrained by the imitation ceiling imposed by sub-optimal data. While Reinforcement Learning (RL) fine-tuning can surpass this limit, it is notoriously sample inefficient. This challenge arises from two core issues: (1) catastrophic initial unlearning due to an unstable Q-function and (2) inefficient policy updates caused by low-quality exploration data, often forcing a reliance on costly human interventions. We introduce FORCE, a 3-stage framework that stabilizes fine-tuning by tackling both issues. FORCE first incorporates a Value-Calibrated Warm-Up phase, utilizing on-policy rollouts to mitigate the distributional shift of the Q-function. Subsequently, during the online stage, this calibrated Q-function acts as a filter for both the policy's own action proposals and expert data, ensuring only high-value actions are used for the policy update. We evaluate FORCE on various simulation and real-world tasks, and the result shows that FORCE achieves a 79% absolute improvement in success rates and outperform prior RL methods by 10%, while accelerating training by 32.5%. Critically, it mitigates the common success rate drop and achieves this robust performance without human intervention, marking a significant step towards deploying capable and autonomous robotic agents.
匹配关键词: mixture of experts
---

[ACADEMIC - ARXIV]
标题: InvestPhilBench: A Multi-Layer Dynamic Benchmark for Evaluating Large Language Model Procedural Reasoning in Expert Investment Philosophy
作者: Mingguang Chen, Bo Qu
链接: https://arxiv.org/abs/2606.25984v1
完整摘要: Large language models are increasingly deployed as investment research assistants, yet no benchmark tests whether they can accurately reconstruct and apply the specific procedural decision frameworks of expert investors. We introduce InvestPhilBench, a multi-layer dynamic benchmark spanning eight cognitive tiers, from principle identification (L1) to novel framework extrapolation (L8). The v0.6 release comprises 118 primary-source-verified investment principle cards, 25 decision framework cards with explicit topology metadata, and 243 QA questions (197 dev / 46 held-out test). For reproducible scoring at scale we introduce the Benchmark Automated Scoring Pipeline (BASP) -- five algorithmic metrics (OGRS, KCCS, SAP@k, IVP, CKCA) -- the Failure Mode Detection Protocol (FMDP) with computable rules for six failure modes, and Gate Reconstruction Accuracy (GRA), a per-gate metric for questions with gold reasoning programs. In this release, InvestPhilBench is primarily a benchmark-and-methodology contribution. A four-model sanity wave on the 188-question development split shows a sharp provider-tier split (BASP 0.906 vs. 0.438); these mixed-judge numbers are confounded upper bounds. The central finding: the BASP composite saturates at the frontier (Claude L4 = 0.932) while GRA still exposes a procedural deficit (frontier L4 GRA approx. 0.77, L7 GRA 0.57-0.62) -- composite scoring rewards fluent prose and hides the procedural gap. v0.6 implements a unified judge and true model-in-the-loop retrieval/oracle conditions; the de-confounded multi-model leaderboard and full three-condition run are v1.0 deliverables. On a 100-item expert-annotated gold set the automated BASP composite tracks the human reference at Pearson r = 0.72 (MAE = 0.10), with attribution (SAP@3) the weakest sub-metric and the failure-mode detector running sensitive-but-over-flagging.
匹配关键词: mixture of experts
---

[ACADEMIC - ARXIV]
标题: Improving Neural Network Training by Decoupling the Magnitude and Direction of Weight Vectors
作者: Alexander Hägele, Alejandro Hernández-Cano, Atli Kosson, Martin Jaggi
链接: https://arxiv.org/abs/2606.25971v1
完整摘要: Modern neural network training relies on optimizers such as Adam and Muon which act on each weight matrix as a single object. Yet every weight matrix carries two distinct quantities -- a \emph{magnitude} and a \emph{direction} -- and all optimizers stepping in the matrix as a whole couple their dynamics: the directional change from an update depends on the current magnitude, while the magnitude drifts as a byproduct of learning the direction, so neither is governed directly by the learning rate. Typical training therefore leans on surrounding recipes such as weight decay and warmup to keep learning stable at scale, though these regulate the coupling only indirectly; other recent methods instead constrain the weight to a fixed-norm sphere, but add no learnable magnitude, leaving scale control to normalization layers alone. We propose \emph{Magnitude--Direction (MD) Decoupling}, an optimizer modification that factorizes each weight into a fixed-norm direction on a hypersphere and learnable per-row and per-column magnitude gains, updated at separate learning rates, all while the model still sees a single fused weight tensor. The method is agnostic to the base optimizer and removes the need for weight decay and warmup. Across both Adam and Muon, MD Decoupling improves on well-tuned baselines, transfers the optimal LR across model width without retuning, and continues to help at scale on large Mixture-of-Experts (MoE) models. Treating magnitude and direction as separately controlled quantities thus yields more predictable training dynamics and a simple, broadly applicable improvement to modern optimizers.
匹配关键词: mixture of experts
---

[ACADEMIC - ARXIV]
标题: Mixture-of-Experts RL for Fault-Tolerant Legged Locomotion
作者: Giulio Turrisi, Ozan Pali, Luca Oneto, Claudio Semini
链接: https://arxiv.org/abs/2606.25965v1
完整摘要: Legged robots deployed in planetary exploration and other remote environments must maintain reliable locomotion despite actuator failures and challenging terrain conditions. Although reinforcement learning has achieved strong results in legged locomotion, monolithic policies can struggle to efficiently represent the diverse control strategies required to compensate for different fault conditions. In this work, we propose a fault-aware modular control architecture that explicitly leverages fault-diagnosis information to activate specialized control experts associated with distinct actuator failure modes. Experimental results show that explicit fault-conditioned modular policies consistently outperform monolithic policies of comparable size, achieving higher locomotion performance across failure scenarios. Moreover, the proposed modular architecture retains competitive performance even under significantly reduced network capacity, highlighting its suitability for compute-constrained robotic platforms, such as those typically employed in space applications. The code associated with this work is available at: https://github.com/iit-DLSLab/fault-locomotion-isaaclab.
匹配关键词: mixture of experts
---

[ACADEMIC - ARXIV]
标题: FunPiQ: A New Benchmark for Pixel-Level Quality Assessment in Fundus Images
作者: Pengwei Wang, José Morano, Virginia Mares, Hrvoje Bogunović
链接: https://arxiv.org/abs/2606.25915v1
完整摘要: Color fundus photography (CFP) is the most common ophthalmic imaging modality for large-scale screening. However, it is highly susceptible to degradations, making robust fundus image quality assessment (FIQA) crucial. The criteria for what constitutes high-quality at the image level vary across clinical tasks, making FIQA dependent on expert knowledge. This motivated the development of automated methods and datasets. While existing datasets aim to standardize image-level quality, their criteria often differ. Furthermore, image-level labels preclude the quantitative evaluation of localized degradations, which is essential for trustworthy FIQA. We argue that pixel-level FIQA based on anatomical visibility represents a more task-agnostic, explainable approach. In this work, we introduce FunPiQ, the first FIQA benchmark to provide pixel-level quality annotations. In addition, we propose EFIQA-CP, an explainable-by-design (EBD) method that uses quality pseudo-labels based on anatomical visibility to train a CNN via Non-Negative Positive-Unlabeled learning. Extensive evaluations of classification methods with post-hoc explanations, anomaly detection methods, and EBD methods demonstrate the superior performance of the last and, particularly, of EFIQA-CP.
匹配关键词: mixture of experts
---

[ACADEMIC - ARXIV]
标题: Same Evidence, Different Answer: Auditing Order Sensitivity in Multimodal Large Language Models
作者: Akshay Paruchuri, Sanmi Koyejo, Ehsan Adeli
链接: https://arxiv.org/abs/2606.26079v1
完整摘要: Standard benchmarks for multimodal large language models (MLLMs) score each item on one canonical ordering and miss whether order-irrelevant shuffling changes the answer, a baseline reliability property called for by emerging AI evaluation guidelines. We introduce Facet-Probe, a five-facet audit (option, evidence-chunk, document-rank, image-set, and mixed-modality ordering) of 18 frontier and open-weight MLLMs. A Bayesian item-response model separates ordering noise from per-facet bias, and a same-ordering control estimates the decoder-stochastic floor for observed flips. We find that none of the 18 MLLMs we audit are order-invariant: screened per-facet panel-mean flip rates span 24-50%. A Gemini same-ordering control at temperature 0 estimates a substantial ordering excess over a same-input decoder-noise floor in verified cells. Capability predicts but does not eliminate flips; the best model still flips on 13.4% of trials. In our Gemini mitigation tests, training-free prompt changes are modality-conditional and do not transfer from text to visual reasoning. These results suggest that prompt-level mitigation alone is unlikely to provide general order robustness, motivating future work on training-time and architectural approaches. We propose cross-ordering flip rate as a standard reporting axis for MLLMs.
匹配关键词: transformer architecture
---

[ACADEMIC - ARXIV]
标题: The Unfireable Safety Kernel: Execution-Time AI Alignment for AI Agents and Other Escapable AI Systems
作者: Seth Dobrin, Łukasz Chmiel
链接: https://arxiv.org/abs/2606.26057v1
完整摘要: AI agents are granted access to tools, APIs, and other infrastructure, making them active principals in those systems. The dominant approach places controls inside the agent's own runtime: system prompts, output filters, and guardrail libraries. Any control in the agent's address space is reachable by inputs that influence it; this generalizes to any AI system with sufficient reach into its own runtime, a class we term escapable AI systems. We identify four properties that an authorization mechanism must satisfy for architectural control rather than for cooperative requests: process separation, pre-action enforcement on a structurally only path, fail-closed at both the request and system levels, and externalized signed evidence verifiable outside the controlled system's trust boundary. We position this layer as execution-time AI alignment, complementing training-time alignment (RLHF, Constitutional AI) and inference-time alignment. We present the Unfireable Safety Kernel, a Rust reference implementation realizing all four. Its fail-closed invariant is machine-checked at two levels: an SMT theorem (Z3) and an exhaustive bounded-model-checking proof of the production decision function (Kani, 4/4 harnesses). A Python-to-Rust migration was gated on byte-equivalence (1000/1000 fixtures; 17/17 adversarial classes). We evaluate the kernel governing a live, escapable AI system, a deterministic, self-improving world model, against an escape-seeking adversary driving its real self-modification seam: across 1,000 self-modifications, all 704 attempts on the safety-critical core are refused, with no escape; a further 300, under the operator kill switch, are also refused. A separate campaign of 6,240 authorization round-trips had no successful bypass. Against 3 contemporary systems claiming the agent control plane, the agent invokes control; here, it lacks that choice.
匹配关键词: transformer architecture
---

[ACADEMIC - ARXIV]
标题: Detect, Unlearn, Restore: Defending Text Summarization Models Against Data Poisoning
作者: Poojitha Thota, Shirin Nilizadeh
链接: https://arxiv.org/abs/2606.26036v1
完整摘要: Training-time data poisoning during fine-tuning poses a significant threat to large language models (LLMs) deployed for abstractive text summarization, where small task-specific datasets exert disproportionate influence on model behavior. In this setting, adversaries manipulate fine-tuning data to induce persistent summarization failures, such as biased or harmful summaries, while preserving standard evaluation metrics. We present a unified post-hoc defense framework for detecting and remediating fine-tuning-stage poisoning in summarization models across the machine learning supply chain. Our experiments show that in white-box settings, poisoned document-summary pairs exhibit abnormally high training influence, enabling detection via influence-function analysis with semantic consistency checks. In black-box settings, poisoned models display two to three times greater sensitivity to semantics-preserving perturbations, enabling behavioral auditing without training data access. Beyond existing poisoning formulations, we introduce novel attacks targeting factual distortion and representational bias, showing that poisoning alters summarization behavior without triggering conventional alarms. Across nine architectures and six benchmark datasets under adaptive attacks, our defenses achieve 85-92% detection precision, while gradient-ascent unlearning restores up to 96% of original behavior with minimal utility loss (less than 0.6% ROUGE degradation). These results indicate that fine-tuning-time poisoning leaves persistent structural artifacts, enabling practical detection and post-deployment recovery without full retraining.
匹配关键词: transformer architecture
---

[ACADEMIC - ARXIV]
标题: Privacy Vulnerabilities of Attention Layers in Tabular Foundation Models and Protection of High-Risk Queries
作者: Tânia Carvalho, Maxime Cordy
链接: https://arxiv.org/abs/2606.26021v1
完整摘要: Tabular foundation models are commonly assumed to present limited privacy concerns as they are often pre-trained on large collections of synthetic data. However, these models leverage in-context learning, where sensitive records may be provided directly at inference time as labelled context examples. In this paper, we demonstrate that predictions generated via the attention mechanism leak sufficient information to enable effective Membership Inference Attacks (MIAs). To highlight this vulnerability, we propose AMIA (Attention-based Membership Inference Attack), a shadow-model-free attack that exploits the concentration of transformer attention patterns. Our results show that attention mechanisms reveal strong membership signals, which exceed classical confidence-based attacks, achieving an average gain of 7.7\%, specially in low false-positive regimes. To mitigate this risk, we introduce an inference-time defence inspired by $k$-anonymity principles. This approach reduces the uniqueness of context-key representations without introducing random noise or retraining the model. By targeting only high-risk queries identified through AMIA scores, the defence substantially reduces membership leakage of this attack by an average of 50\% and 25\% against confidence-based attacks, while preserving predictive utility with only 3.9\% performance degradation. Beyond showing that context examples are vulnerable, we further demonstrate that fine-tuning introduces an additional source of privacy risk. In particular, samples whose prediction confidence increases after fine-tuning become more susceptible to MIAs, indicating that fine-tuning can amplify memorisation and expose sensitive training information through confidence shifts.
匹配关键词: transformer architecture
---

[ACADEMIC - ARXIV]
标题: Dziri Voicebot: An End-to-End Low-Resource Speech-to-Speech Conversational System for Algerian Dialect
作者: Dihia Lanasri, Fairouz Taki, Asma Kemmoum
链接: https://arxiv.org/abs/2606.26003v1
完整摘要: Automatic speech and language technologies are still heavily biased toward high-resource languages, limiting their applicability to dialectal and low-resource settings such as Algerian Dialect. This language presents additional challenges including lack of standardized orthography, frequent codeswitching with French, and scarcity of annotated speech resources. This paper addresses the problem of building a complete speech-to-speech conversational system for Algerian Dialect. We propose a modular pipeline integrating automatic speech recognition, natural language understanding, retrieval-augmented generation, and text-to-speech synthesis within a unified architecture. This work is the continuation of our previous work on Algerian dialectal conversational systems Bechiri and Lanasri [2026], extending it from text-based dialogue modeling to full speech-based interaction. We constructed dedicated datasets for ASR, NLU, and TTS in the telecom domain and fine-tune pretrained models for each component. The ASR system is built on Whisper-based adaptation, while the NLU module combines transformer-based embeddings with a task-oriented dialogue framework. A neural TTS system is trained on a newly collected dialectal corpus to enable spoken response generation. Experimental results show strong performance across all components, including low word error rate for ASR, high intent classification and entity recognition scores for NLU, and stable speech synthesis quality. The proposed system provides a reproducible baseline for end-to-end conversational modeling in Algerian Dialect.
匹配关键词: transformer architecture
---

[ACADEMIC - ARXIV]
标题: Neglected Free Lunch from Post-training: Progress Advantage for LLM Agents
作者: Changdae Oh, Wendi Li, Seongheon Park, Samuel Yeh, Tanwi Mallick, Sharon Li
链接: https://arxiv.org/abs/2606.26080v1
完整摘要: Process reward models enable fine-grained, step-level evaluation of LLMs, yet building them for agentic settings remains prohibitively difficult: long-horizon interactions, irreversible actions, and stochastic environment feedback make both human annotation and Monte Carlo estimation infeasible at scale. In this work, we show that reinforcement learning (RL) post-training already provides the ingredients for effective step-level scoring, eliminating the need for dedicated reward model training altogether. Concretely, we derive an implicit advantage under a general stochastic Markov decision process, which we term progress advantage -- log-probability ratio between the RL-trained policy and its reference policy exactly recovers the optimal advantage function. This formulation makes the resulting signal annotation-free, domain-agnostic, and available as a byproduct of the standard RL post-training pipeline. We validate the effectiveness of the progress advantage across three different applications: test-time scaling, uncertainty quantification, and failure attribution on five benchmarks and four model families. Across all settings, it consistently outperforms confidence-based baselines and, despite requiring no task-specific training, surpasses dedicated trained reward models. We complement these results with deeper analyses on characteristics of progress advantage, offering practical guidance for adoption in real-world agentic systems.
匹配关键词: post-training
---

[ACADEMIC - ARXIV]
标题: Detect, Unlearn, Restore: Defending Text Summarization Models Against Data Poisoning
作者: Poojitha Thota, Shirin Nilizadeh
链接: https://arxiv.org/abs/2606.26036v1
完整摘要: Training-time data poisoning during fine-tuning poses a significant threat to large language models (LLMs) deployed for abstractive text summarization, where small task-specific datasets exert disproportionate influence on model behavior. In this setting, adversaries manipulate fine-tuning data to induce persistent summarization failures, such as biased or harmful summaries, while preserving standard evaluation metrics. We present a unified post-hoc defense framework for detecting and remediating fine-tuning-stage poisoning in summarization models across the machine learning supply chain. Our experiments show that in white-box settings, poisoned document-summary pairs exhibit abnormally high training influence, enabling detection via influence-function analysis with semantic consistency checks. In black-box settings, poisoned models display two to three times greater sensitivity to semantics-preserving perturbations, enabling behavioral auditing without training data access. Beyond existing poisoning formulations, we introduce novel attacks targeting factual distortion and representational bias, showing that poisoning alters summarization behavior without triggering conventional alarms. Across nine architectures and six benchmark datasets under adaptive attacks, our defenses achieve 85-92% detection precision, while gradient-ascent unlearning restores up to 96% of original behavior with minimal utility loss (less than 0.6% ROUGE degradation). These results indicate that fine-tuning-time poisoning leaves persistent structural artifacts, enabling practical detection and post-deployment recovery without full retraining.
匹配关键词: post-training
---

[ACADEMIC - ARXIV]
标题: FunPiQ: A New Benchmark for Pixel-Level Quality Assessment in Fundus Images
作者: Pengwei Wang, José Morano, Virginia Mares, Hrvoje Bogunović
链接: https://arxiv.org/abs/2606.25915v1
完整摘要: Color fundus photography (CFP) is the most common ophthalmic imaging modality for large-scale screening. However, it is highly susceptible to degradations, making robust fundus image quality assessment (FIQA) crucial. The criteria for what constitutes high-quality at the image level vary across clinical tasks, making FIQA dependent on expert knowledge. This motivated the development of automated methods and datasets. While existing datasets aim to standardize image-level quality, their criteria often differ. Furthermore, image-level labels preclude the quantitative evaluation of localized degradations, which is essential for trustworthy FIQA. We argue that pixel-level FIQA based on anatomical visibility represents a more task-agnostic, explainable approach. In this work, we introduce FunPiQ, the first FIQA benchmark to provide pixel-level quality annotations. In addition, we propose EFIQA-CP, an explainable-by-design (EBD) method that uses quality pseudo-labels based on anatomical visibility to train a CNN via Non-Negative Positive-Unlabeled learning. Extensive evaluations of classification methods with post-hoc explanations, anomaly detection methods, and EBD methods demonstrate the superior performance of the last and, particularly, of EFIQA-CP.
匹配关键词: post-training
---

[ACADEMIC - ARXIV]
标题: OracleAnalyser: Analysing Implicit Semantics of Oracle Bone Scripts through MLLMs with Post-training
作者: Zijia Song, Yelin Wang, Zhengyi Ma, Zitong Yu, Tianheng Wang, Jiahuan Zhang, Taorui Wang, Kaicheng Yu
链接: https://arxiv.org/abs/2606.25906v1
完整摘要: With the advancement of artificial intelligence, research on oracle bone scripts has entered a new era. However, existing methods and benchmarks remain largely confined to recognition tasks, overlooking the equally crucial aspect of oracle bone analysis. To address this gap, we propose OracleAnalyser, a reasoning framework for oracle bone analysis based on post-training techniques. Specifically, we fine-tune Qwen2.5-VL-3B-Instruct through multiple post-training stages and introduce a new preference optimization algorithm, Stable Focal Preference Optimization (SFPO), tailored to the characteristics of oracle bone datasets. In addition, we release both an oracle bone reasoning dataset and an oracle bone preference dataset, and further construct a new benchmark to evaluate models' analytical capabilities for oracle bone scripts. Extensive experiments validate the superior analytical performance of OracleAnalyser, which achieves remarkable results with only 3B parameters, surpassing models with substantially larger scales.
匹配关键词: post-training
---

[ACADEMIC - ARXIV]
标题: Semantic Consistency Policy Optimization for Reinforcement Learning of LLM Agents
作者: Peng Xu, Sijia Chen, Junzhuo Li, Xuming Hu
链接: https://arxiv.org/abs/2606.25852v1
完整摘要: Group-based reinforcement learning effectively post-trains LLM agents for long-horizon, sparse-reward tasks by deriving step-level credit from trajectory outcomes. However, this ties a step's credit to its rollout's final outcome: semantically near-identical intermediate steps receive opposite credit depending on whether their trajectory eventually succeeded or failed. Such semantic credit inconsistency sends conflicting gradients to similar actions and wastes the partially-correct progress inside failed rollouts. Motivated by this, we propose Semantic Consistency Policy Optimization (SCPO), a value-free reward-shaping method that mitigates this inconsistency by recovering step-level credit from successful siblings in the same rollout group. Concretely, SCPO scores each failed step against a successful sibling and adds positive step-level credit for new progress along that sibling. On ALFWorld and WebShop, SCPO matches or exceeds strong group-based baselines, reaching 93.7+/-4.1 percent success on ALFWorld and 74.8+/-2.0 percent on WebShop at 1.5B parameters, with gains concentrated on the hardest multi-step tasks.
匹配关键词: post-training
---

[ACADEMIC - ARXIV]
标题: Detect, Unlearn, Restore: Defending Text Summarization Models Against Data Poisoning
作者: Poojitha Thota, Shirin Nilizadeh
链接: https://arxiv.org/abs/2606.26036v1
完整摘要: Training-time data poisoning during fine-tuning poses a significant threat to large language models (LLMs) deployed for abstractive text summarization, where small task-specific datasets exert disproportionate influence on model behavior. In this setting, adversaries manipulate fine-tuning data to induce persistent summarization failures, such as biased or harmful summaries, while preserving standard evaluation metrics. We present a unified post-hoc defense framework for detecting and remediating fine-tuning-stage poisoning in summarization models across the machine learning supply chain. Our experiments show that in white-box settings, poisoned document-summary pairs exhibit abnormally high training influence, enabling detection via influence-function analysis with semantic consistency checks. In black-box settings, poisoned models display two to three times greater sensitivity to semantics-preserving perturbations, enabling behavioral auditing without training data access. Beyond existing poisoning formulations, we introduce novel attacks targeting factual distortion and representational bias, showing that poisoning alters summarization behavior without triggering conventional alarms. Across nine architectures and six benchmark datasets under adaptive attacks, our defenses achieve 85-92% detection precision, while gradient-ascent unlearning restores up to 96% of original behavior with minimal utility loss (less than 0.6% ROUGE degradation). These results indicate that fine-tuning-time poisoning leaves persistent structural artifacts, enabling practical detection and post-deployment recovery without full retraining.
匹配关键词: fine-tuning
---

[ACADEMIC - ARXIV]
标题: Why Multi-Step Tool-Use Reinforcement Learning Collapses and How Supervisory Signals Fix It
作者: Yupu Hao, Zhuoran Jin, Huanxuan Liao, Kang Liu, Jun Zhao
链接: https://arxiv.org/abs/2606.26027v1
完整摘要: Tool use enables large language models (LLMs) to perform complex tasks, and recent agentic reinforcement learning (RL) methods show promise for enhancing model capabilities. However, RL alone often leads to instability or limited gains in tool-use tasks. In our experiments, some models exhibit catastrophic collapse, where performance abruptly drops and tool-invocation structures fail. The analysis reveals that these failures stem from unexpected probability spikes in specific control tokens, disrupting structured execution, yet the underlying tool-use capability remains intact, merely obscured by specific formats. To address this, we systematically investigate a diverse set of supervisory signals, including off-policy supervision, hint-based guidance, erroneous example supervision, and others, applied under both synchronous and interleaved training schemes. We find that interleaving supervised fine-tuning (SFT) with RL substantially improves stability, but exhibits degraded performance under format and content out-of-distribution (OOD) evaluation. We also analyze the impact of learning rates and generalization across settings. These results highlight the importance of understanding RL failures and demonstrate how diverse supervisory signals can guide exploratory learning, enabling robust training of LLMs for complex, multi-step tool-use tasks. Our Code is available at https://github.com/hypasd-art/Tool-RL-Box.
匹配关键词: fine-tuning
---

[ACADEMIC - ARXIV]
标题: In-Context World Modeling for Robotic Control
作者: Siyin Wang, Junhao Shi, Senyu Fei, Zhaoyang Fu, Li Ji, Jingjing Gong, Xipeng Qiu
链接: https://arxiv.org/abs/2606.26025v1
完整摘要: Modern Vision-Language-Action (VLA) models often fail to generalize to novel setups, such as altered camera viewpoints or robot morphologies, because they are typically conditioned only on current observations and language instructions. By ignoring the underlying system configuration as a variable, these models implicitly assume a fixed execution context encountered during training, necessitating data-intensive fine-tuning for any new environment. In this work, we introduce In-Context World Modeling (ICWM), a framework that treats system identification as an in-context adaptation problem. ICWM enables robot policies to autonomously infer essential system variables from a short history of self-generated, task-agnostic interactions. Unlike traditional In-Context Learning that uses demonstrations to specify what task to perform, ICWM leverages the context window to understand how the system operates. By processing these interactions before task execution, the model implicitly captures the world dynamics of the current system, enabling adaptation to novel configurations without parameter updates. Extensive experiments in simulation and on real-world robot platforms demonstrate that ICWM significantly outperforms standard VLA baselines on novel camera viewpoints.
匹配关键词: fine-tuning
---

[ACADEMIC - ARXIV]
标题: Privacy Vulnerabilities of Attention Layers in Tabular Foundation Models and Protection of High-Risk Queries
作者: Tânia Carvalho, Maxime Cordy
链接: https://arxiv.org/abs/2606.26021v1
完整摘要: Tabular foundation models are commonly assumed to present limited privacy concerns as they are often pre-trained on large collections of synthetic data. However, these models leverage in-context learning, where sensitive records may be provided directly at inference time as labelled context examples. In this paper, we demonstrate that predictions generated via the attention mechanism leak sufficient information to enable effective Membership Inference Attacks (MIAs). To highlight this vulnerability, we propose AMIA (Attention-based Membership Inference Attack), a shadow-model-free attack that exploits the concentration of transformer attention patterns. Our results show that attention mechanisms reveal strong membership signals, which exceed classical confidence-based attacks, achieving an average gain of 7.7\%, specially in low false-positive regimes. To mitigate this risk, we introduce an inference-time defence inspired by $k$-anonymity principles. This approach reduces the uniqueness of context-key representations without introducing random noise or retraining the model. By targeting only high-risk queries identified through AMIA scores, the defence substantially reduces membership leakage of this attack by an average of 50\% and 25\% against confidence-based attacks, while preserving predictive utility with only 3.9\% performance degradation. Beyond showing that context examples are vulnerable, we further demonstrate that fine-tuning introduces an additional source of privacy risk. In particular, samples whose prediction confidence increases after fine-tuning become more susceptible to MIAs, indicating that fine-tuning can amplify memorisation and expose sensitive training information through confidence shifts.
匹配关键词: fine-tuning
---

[ACADEMIC - ARXIV]
标题: The Tatoxa System for Text Detoxification in Low-Resource Languages: The Case of Tatar
作者: Ilseyar Alimova, Bogdan Monogov, Artyom Mazur, Daniil Antonov, Vsevolod Karimov, Vitaliy Egorov, Bulat Khakimov, Alexander Panchenko
链接: https://arxiv.org/abs/2606.26015v1
完整摘要: Text detoxification, the automated detection and mitigation of abusive and harmful content, is essential for ensuring the safety of online communities and protecting users. However, low resource languages such as Tatar have received little research attention. In this paper we present Tatoxa, a novel state-of-the-art system for text detoxification in the Tatar language. Comparative experiments show that the proposed approach outperforms existing open source and proprietary commercial LLMs on key quality metrics. We also introduce a new dataset for text detoxification in Tatar, designed for fine tuning and evaluation in low resource settings. Finally, cross lingual transfer experiments indicate that transfer from other languages, including the culturally close Russian, performs significantly worse than training on native Tatar data even when a large Russian corpus is available.
匹配关键词: fine-tuning
---

[ACADEMIC - ARXIV]
标题: Why Multi-Step Tool-Use Reinforcement Learning Collapses and How Supervisory Signals Fix It
作者: Yupu Hao, Zhuoran Jin, Huanxuan Liao, Kang Liu, Jun Zhao
链接: https://arxiv.org/abs/2606.26027v1
完整摘要: Tool use enables large language models (LLMs) to perform complex tasks, and recent agentic reinforcement learning (RL) methods show promise for enhancing model capabilities. However, RL alone often leads to instability or limited gains in tool-use tasks. In our experiments, some models exhibit catastrophic collapse, where performance abruptly drops and tool-invocation structures fail. The analysis reveals that these failures stem from unexpected probability spikes in specific control tokens, disrupting structured execution, yet the underlying tool-use capability remains intact, merely obscured by specific formats. To address this, we systematically investigate a diverse set of supervisory signals, including off-policy supervision, hint-based guidance, erroneous example supervision, and others, applied under both synchronous and interleaved training schemes. We find that interleaving supervised fine-tuning (SFT) with RL substantially improves stability, but exhibits degraded performance under format and content out-of-distribution (OOD) evaluation. We also analyze the impact of learning rates and generalization across settings. These results highlight the importance of understanding RL failures and demonstrate how diverse supervisory signals can guide exploratory learning, enabling robust training of LLMs for complex, multi-step tool-use tasks. Our Code is available at https://github.com/hypasd-art/Tool-RL-Box.
匹配关键词: SFT
---

[ACADEMIC - ARXIV]
标题: Weave of Formal Thought
作者: Alexandre Bouayad
链接: https://arxiv.org/abs/2606.25987v1
完整摘要: Large language models (LLMs) attain remarkable surface fluency on code, yet they neither formally guarantee the syntactic validity of their output nor leverage the hierarchical structure defining the target language. While existing constrained-decoding frameworks address the former, they operate under rigid assumptions that preclude critical lexical mechanisms -- including context-sensitive lexing, maximal-munch tokenization, and keyword extraction -- and only approximate vocabulary masking, sacrificing completeness. For the latter, code LLMs typically inject grammatical structure via predetermined policies rather than learning which structural information to expose. In this work, we introduce Weave of Formal Thought (WoFT), a paradigm uniting rigorous syntactic validation with learned structural representations. First, we present a formal engine and constrained decoder that is sound and complete with respect to the full Tree-sitter specification. By augmenting generalized LR (GLR) parsing with a speculative-lexing construction that maintains concurrent lexer-state hypotheses synchronized with a GLR graph-structured stack, our decoder admits every subword token extending to a valid program prefix and rejects all others. Second, we present a latent-variable fine-tuning method training the language model to interleave non-terminal grammar symbols directly into generation. Utilizing the reweighted wake-sleep (RWS) algorithm to optimize the importance-weighted evidence lower bound (IW-ELBO) of the surface text, the model learns to selectively retain formal derivations as an adaptive structural scratchpad. For Python, fine-tuning StarCoder2-3B with our RWS objective reduces per-token cross-entropy by 14.3% relative to a text-only SFT baseline, demonstrating that discretionary latent syntax recovers critical structural information that flat autoregressive training discards.
匹配关键词: SFT
---

[ACADEMIC - ARXIV]
标题: The Generalization Spectrum: A Chromatographic Approach to Evaluating Learning Algorithms
作者: Jinghan Zhang, Zerui Cheng, Shiqi Chen, Ge Zhang, Wenhao Huang, Jiashuo Liu, Junxian He, Tianle Cai
链接: https://arxiv.org/abs/2606.25450v1
完整摘要: Traditional evaluations measure a learning algorithm's final performance on an i.i.d. test set, reducing learning to a single aggregate score. This approach obscures a fundamental question: to what extent does learning from a specific example generalize to others? Such per-sample generalization, akin to learning by analogy in human cognition, captures how far the knowledge extracted from one example can transfer, yet remains invisible to standard benchmarks. We introduce the Generalization Spectrum, an evaluation framework designed to expose this hidden dimension. For each training example, we construct a controlled suite of test variants arranged by increasing transfer distance, from exact recall to implementation transfer across languages, context transfer under complete narrative re-framing, category-matched in-domain problems, and an unpaired baseline. By tracking performance across these distances, we reveal not just whether an algorithm learns, but how far that learning extends. We instantiate this framework on competitive programming, using a selection-and-synthesis pipeline seeded with recent problems to mitigate contamination. We first compare three canonical learning paradigms under matched memorization. RL converts memorization into near-transfer more efficiently than SFT-family baselines, while ICL exhibits strong but correspondence-dependent transfer. We then use the Spectrum to diagnose within-family variants. The resulting profiles show that local gains need not expand the generalization radius: abstractions and hints mainly lift local transfer, RFT preserves a stronger far-transfer tail than reference SFT, and self-distillation or hint-assisted RL can reduce far transfer even when local transfer or optimization improves.
匹配关键词: SFT
---

[ACADEMIC - ARXIV]
标题: Improved Large Language Diffusion Models
作者: Shen Nie, Qiyang Min, Shaoxuan Xu, Zihao Huang, Yuxuan Song, Yong Shan, Yankai Lin, Wayne Xin Zhao, Chongxuan Li, Ji-Rong Wen
链接: https://arxiv.org/abs/2606.25331v1
完整摘要: Modern large language models are predominantly trained with autoregressive factorization and causal attention. We present \emph{iLLaDA}, an 8B masked diffusion language model trained from scratch with fully bidirectional attention. iLLaDA keeps the masked diffusion objective throughout pre-training and supervised fine-tuning (SFT), scaling pre-training to 12T tokens and fine-tuning on a 25B-token instruction corpus for 12 epochs. We further use variable-length generation for efficiency and introduce confidence-based scoring for multiple-choice evaluation. Compared with LLaDA, iLLaDA improves broadly across general, mathematical, and code benchmarks; for example, iLLaDA-Base improves by 21.6 points on BBH and 14.9 points on ARC-Challenge, while iLLaDA-Instruct improves by 14.5 points on MATH and 16.5 points on HumanEval. Despite its non-autoregressive training, iLLaDA also remains competitive with Qwen2.5 7B on several benchmarks. These results show that fully bidirectional diffusion training from scratch is a competitive path toward strong language models. Model weights and codes: https://github.com/ML-GSAI/LLaDA.
匹配关键词: SFT
---

[ACADEMIC - ARXIV]
标题: Detect, Unlearn, Restore: Defending Text Summarization Models Against Data Poisoning
作者: Poojitha Thota, Shirin Nilizadeh
链接: https://arxiv.org/abs/2606.26036v1
完整摘要: Training-time data poisoning during fine-tuning poses a significant threat to large language models (LLMs) deployed for abstractive text summarization, where small task-specific datasets exert disproportionate influence on model behavior. In this setting, adversaries manipulate fine-tuning data to induce persistent summarization failures, such as biased or harmful summaries, while preserving standard evaluation metrics. We present a unified post-hoc defense framework for detecting and remediating fine-tuning-stage poisoning in summarization models across the machine learning supply chain. Our experiments show that in white-box settings, poisoned document-summary pairs exhibit abnormally high training influence, enabling detection via influence-function analysis with semantic consistency checks. In black-box settings, poisoned models display two to three times greater sensitivity to semantics-preserving perturbations, enabling behavioral auditing without training data access. Beyond existing poisoning formulations, we introduce novel attacks targeting factual distortion and representational bias, showing that poisoning alters summarization behavior without triggering conventional alarms. Across nine architectures and six benchmark datasets under adaptive attacks, our defenses achieve 85-92% detection precision, while gradient-ascent unlearning restores up to 96% of original behavior with minimal utility loss (less than 0.6% ROUGE degradation). These results indicate that fine-tuning-time poisoning leaves persistent structural artifacts, enabling practical detection and post-deployment recovery without full retraining.
匹配关键词: instruction tuning
---

[ACADEMIC - ARXIV]
标题: Why Multi-Step Tool-Use Reinforcement Learning Collapses and How Supervisory Signals Fix It
作者: Yupu Hao, Zhuoran Jin, Huanxuan Liao, Kang Liu, Jun Zhao
链接: https://arxiv.org/abs/2606.26027v1
完整摘要: Tool use enables large language models (LLMs) to perform complex tasks, and recent agentic reinforcement learning (RL) methods show promise for enhancing model capabilities. However, RL alone often leads to instability or limited gains in tool-use tasks. In our experiments, some models exhibit catastrophic collapse, where performance abruptly drops and tool-invocation structures fail. The analysis reveals that these failures stem from unexpected probability spikes in specific control tokens, disrupting structured execution, yet the underlying tool-use capability remains intact, merely obscured by specific formats. To address this, we systematically investigate a diverse set of supervisory signals, including off-policy supervision, hint-based guidance, erroneous example supervision, and others, applied under both synchronous and interleaved training schemes. We find that interleaving supervised fine-tuning (SFT) with RL substantially improves stability, but exhibits degraded performance under format and content out-of-distribution (OOD) evaluation. We also analyze the impact of learning rates and generalization across settings. These results highlight the importance of understanding RL failures and demonstrate how diverse supervisory signals can guide exploratory learning, enabling robust training of LLMs for complex, multi-step tool-use tasks. Our Code is available at https://github.com/hypasd-art/Tool-RL-Box.
匹配关键词: instruction tuning
---

[ACADEMIC - ARXIV]
标题: In-Context World Modeling for Robotic Control
作者: Siyin Wang, Junhao Shi, Senyu Fei, Zhaoyang Fu, Li Ji, Jingjing Gong, Xipeng Qiu
链接: https://arxiv.org/abs/2606.26025v1
完整摘要: Modern Vision-Language-Action (VLA) models often fail to generalize to novel setups, such as altered camera viewpoints or robot morphologies, because they are typically conditioned only on current observations and language instructions. By ignoring the underlying system configuration as a variable, these models implicitly assume a fixed execution context encountered during training, necessitating data-intensive fine-tuning for any new environment. In this work, we introduce In-Context World Modeling (ICWM), a framework that treats system identification as an in-context adaptation problem. ICWM enables robot policies to autonomously infer essential system variables from a short history of self-generated, task-agnostic interactions. Unlike traditional In-Context Learning that uses demonstrations to specify what task to perform, ICWM leverages the context window to understand how the system operates. By processing these interactions before task execution, the model implicitly captures the world dynamics of the current system, enabling adaptation to novel configurations without parameter updates. Extensive experiments in simulation and on real-world robot platforms demonstrate that ICWM significantly outperforms standard VLA baselines on novel camera viewpoints.
匹配关键词: instruction tuning
---

[ACADEMIC - ARXIV]
标题: Privacy Vulnerabilities of Attention Layers in Tabular Foundation Models and Protection of High-Risk Queries
作者: Tânia Carvalho, Maxime Cordy
链接: https://arxiv.org/abs/2606.26021v1
完整摘要: Tabular foundation models are commonly assumed to present limited privacy concerns as they are often pre-trained on large collections of synthetic data. However, these models leverage in-context learning, where sensitive records may be provided directly at inference time as labelled context examples. In this paper, we demonstrate that predictions generated via the attention mechanism leak sufficient information to enable effective Membership Inference Attacks (MIAs). To highlight this vulnerability, we propose AMIA (Attention-based Membership Inference Attack), a shadow-model-free attack that exploits the concentration of transformer attention patterns. Our results show that attention mechanisms reveal strong membership signals, which exceed classical confidence-based attacks, achieving an average gain of 7.7\%, specially in low false-positive regimes. To mitigate this risk, we introduce an inference-time defence inspired by $k$-anonymity principles. This approach reduces the uniqueness of context-key representations without introducing random noise or retraining the model. By targeting only high-risk queries identified through AMIA scores, the defence substantially reduces membership leakage of this attack by an average of 50\% and 25\% against confidence-based attacks, while preserving predictive utility with only 3.9\% performance degradation. Beyond showing that context examples are vulnerable, we further demonstrate that fine-tuning introduces an additional source of privacy risk. In particular, samples whose prediction confidence increases after fine-tuning become more susceptible to MIAs, indicating that fine-tuning can amplify memorisation and expose sensitive training information through confidence shifts.
匹配关键词: instruction tuning
---

[ACADEMIC - ARXIV]
标题: The Tatoxa System for Text Detoxification in Low-Resource Languages: The Case of Tatar
作者: Ilseyar Alimova, Bogdan Monogov, Artyom Mazur, Daniil Antonov, Vsevolod Karimov, Vitaliy Egorov, Bulat Khakimov, Alexander Panchenko
链接: https://arxiv.org/abs/2606.26015v1
完整摘要: Text detoxification, the automated detection and mitigation of abusive and harmful content, is essential for ensuring the safety of online communities and protecting users. However, low resource languages such as Tatar have received little research attention. In this paper we present Tatoxa, a novel state-of-the-art system for text detoxification in the Tatar language. Comparative experiments show that the proposed approach outperforms existing open source and proprietary commercial LLMs on key quality metrics. We also introduce a new dataset for text detoxification in Tatar, designed for fine tuning and evaluation in low resource settings. Finally, cross lingual transfer experiments indicate that transfer from other languages, including the culturally close Russian, performs significantly worse than training on native Tatar data even when a large Russian corpus is available.
匹配关键词: instruction tuning
---

[ACADEMIC - ARXIV]
标题: Real-Time Voice AI Hears but Does Not Listen
作者: Martijn Bartelds, Federico Bianchi, James Zou
链接: https://arxiv.org/abs/2606.26083v1
完整摘要: Speech conveys information through both words and vocal delivery. We evaluate four leading production realtime voice systems-OpenAI's GPT Realtime 2, Google's Gemini 3.1 Flash Live, and Alibaba's Qwen3.5 Omni Plus and Omni Flash-on tasks where the words and the delivery patterns both convey meaningful information. Across three consequential scenarios, all four systems act on the words rather than the voice. They end calls with crying callers who insist nothing is wrong, approve wire transfers authorized in frightened voices, and enroll callers whose agreement is clearly sarcastic. Surprisingly, this is often not a failure of perception. When asked directly, three of the four systems reliably identify the distress, fear, or sarcasm they later ignore when making decisions. We observe a similar pattern when these realtime voice systems estimate accent and age, as their responses frequently follow the biases of the words rather than the acoustic properties of the speaker. We term this disconnect between perception and action the emotional intelligence gap of voice AI. Prompting systems to explicitly attend to vocal delivery improves performance only partially and inconsistently. Our findings show that current realtime voice AI systems often behave as if speech had been reduced to a transcript, suggesting that they should be used with caution in settings where the tone and emotion of delivery convey important information.
匹配关键词: AI scientist
---

[ACADEMIC - ARXIV]
标题: Same Evidence, Different Answer: Auditing Order Sensitivity in Multimodal Large Language Models
作者: Akshay Paruchuri, Sanmi Koyejo, Ehsan Adeli
链接: https://arxiv.org/abs/2606.26079v1
完整摘要: Standard benchmarks for multimodal large language models (MLLMs) score each item on one canonical ordering and miss whether order-irrelevant shuffling changes the answer, a baseline reliability property called for by emerging AI evaluation guidelines. We introduce Facet-Probe, a five-facet audit (option, evidence-chunk, document-rank, image-set, and mixed-modality ordering) of 18 frontier and open-weight MLLMs. A Bayesian item-response model separates ordering noise from per-facet bias, and a same-ordering control estimates the decoder-stochastic floor for observed flips. We find that none of the 18 MLLMs we audit are order-invariant: screened per-facet panel-mean flip rates span 24-50%. A Gemini same-ordering control at temperature 0 estimates a substantial ordering excess over a same-input decoder-noise floor in verified cells. Capability predicts but does not eliminate flips; the best model still flips on 13.4% of trials. In our Gemini mitigation tests, training-free prompt changes are modality-conditional and do not transfer from text to visual reasoning. These results suggest that prompt-level mitigation alone is unlikely to provide general order robustness, motivating future work on training-time and architectural approaches. We propose cross-ordering flip rate as a standard reporting axis for MLLMs.
匹配关键词: AI scientist
---

[ACADEMIC - ARXIV]
标题: The Unfireable Safety Kernel: Execution-Time AI Alignment for AI Agents and Other Escapable AI Systems
作者: Seth Dobrin, Łukasz Chmiel
链接: https://arxiv.org/abs/2606.26057v1
完整摘要: AI agents are granted access to tools, APIs, and other infrastructure, making them active principals in those systems. The dominant approach places controls inside the agent's own runtime: system prompts, output filters, and guardrail libraries. Any control in the agent's address space is reachable by inputs that influence it; this generalizes to any AI system with sufficient reach into its own runtime, a class we term escapable AI systems. We identify four properties that an authorization mechanism must satisfy for architectural control rather than for cooperative requests: process separation, pre-action enforcement on a structurally only path, fail-closed at both the request and system levels, and externalized signed evidence verifiable outside the controlled system's trust boundary. We position this layer as execution-time AI alignment, complementing training-time alignment (RLHF, Constitutional AI) and inference-time alignment. We present the Unfireable Safety Kernel, a Rust reference implementation realizing all four. Its fail-closed invariant is machine-checked at two levels: an SMT theorem (Z3) and an exhaustive bounded-model-checking proof of the production decision function (Kani, 4/4 harnesses). A Python-to-Rust migration was gated on byte-equivalence (1000/1000 fixtures; 17/17 adversarial classes). We evaluate the kernel governing a live, escapable AI system, a deterministic, self-improving world model, against an escape-seeking adversary driving its real self-modification seam: across 1,000 self-modifications, all 704 attempts on the safety-critical core are refused, with no escape; a further 300, under the operator kill switch, are also refused. A separate campaign of 6,240 authorization round-trips had no successful bypass. Against 3 contemporary systems claiming the agent control plane, the agent invokes control; here, it lacks that choice.
匹配关键词: AI scientist
---

[ACADEMIC - ARXIV]
标题: AI translation of literary texts is "fine", but readers still prefer human translations
作者: Yves Ferstler, Adam Podoxin, Ty Brassington, Roman Grundkiewicz, Maite Taboada, Marzena Karpinska
链接: https://arxiv.org/abs/2606.26040v1
完整摘要: AI translation of literary works is increasingly common. While the content may be rendered adequately, we do not know enough about how readers experience it in terms of immersiveness and literary effect, aspects poorly captured by automatic machine translation metrics or human evaluation targeting fluency and adequacy. We ask 15 avid readers to compare recently published human translations (HT) to machine translations (MT) generated with an agentic large language model (LLM)-based pipeline, for 15 recent novels in French, Polish, and Japanese and translated into English. Readers evaluated approximately 8K-word excerpts in two conditions: immersive reading of the whole excerpt (30 comparisons) and close reading of 386 aligned HT-MT chunk pairs (772 comparisons), with two readers per book and in alternating order of presentation. Overall, readers find MT "fine", but prefer HT (slightly at excerpt-level 19/30, more clearly at chunk-level 522/772) for its ease, clarity, and immersive nature. Readers' highlights show that MT's quality varies more within one book than HT's does. Crucially, readers cannot reliably tell the two apart (17/30 guess correctly) and tend to prefer the version they believe to be human. Automatic metrics, including LLM-as-a-judge approaches, fail to recover reader preferences and favor MT. We release LAIT (Literary AI Translation), a reader-centered evaluation dataset with 1K reader comments, 2K judgments and preference ratings, and 7.2K span-level annotations, along with our evaluation protocol and supporting interface.
匹配关键词: AI scientist
---

[ACADEMIC - ARXIV]
标题: Can Trustless Agents Be Trusted? An Empirical Study of the ERC-8004 Decentralized AI Agent Ecosystem
作者: Xihan Xiong, Zelin Li, Wei Wei, Qin Wang, William Knottenbelt, Zhipeng Wang
链接: https://arxiv.org/abs/2606.26028v1
完整摘要: As autonomous AI agents increasingly transact across organizational boundaries, a fundamental trust challenge emerges: how can an agent assess whether an unknown counterpart is trustworthy? The ERC-8004 protocol addresses this challenge with the first permissionless trust layer for AI agent economies, built around three on-chain registries for Identity, Reputation, and Validation. Despite its rapid adoption, the protocol has not been studied empirically, leaving it unclear whether the information it records provides a trustworthy basis for decision-making. To address this gap, we present the first empirical study of ERC-8004 across three chains: Ethereum, BNB Smart Chain (BSC), and Base, covering the period from protocol deployment through May 13, 2026. We crawl on-chain Identity and Reputation events, off-chain files, and x402 payment transactions. On the identity side, we find that most registrations are placeholders rather than active agents, with only a small fraction (3%, 4%, and 15% across Ethereum, BSC, and Base) exposing a valid ERC-8004 registration file with at least one live service endpoint. On the reputation side, we show that the Registry, as currently deployed, cannot function as a trust signal: values are not commensurable, feedback records are rarely grounded in verifiable interactions, and reputation can be manipulated at minimal cost. Consistent with these design weaknesses, we find that a substantial fraction of reviewers (73.6%, 59.2%, and 90.6% across Ethereum, BSC, and Base) exhibit coordinated Sybil behavior. After removing Sybil-flagged feedback, 15.5%, 72.3%, and 89.4% of rated agents, respectively, are left with no valid feedback. We then turn these findings into concrete recommendations for future revisions of ERC-8004. Our study yields actionable protocol-design implications and establishes an empirical baseline for research on AI agent markets.
匹配关键词: AI scientist
---

[ACADEMIC - ARXIV]
标题: RevengeBench: Reverse Engineering Code-Space Policies from Behavioral Experiments
作者: Babak Rahmani, Sebastian Dziadzio, Joschka Strüber, Sergio Hernández-Gutiérrez, Matthias Bethge
链接: https://arxiv.org/abs/2606.26094v1
完整摘要: For most of scientific history, researchers studying behavior could only infer hidden mechanisms from outward actions: an inverse problem that becomes more tractable when observation is augmented by targeted intervention. We pose a computational analogue: given only behavioral traces of an agent in a game environment, can a learner reconstruct the underlying decision program as executable code, and how much does this reconstruction improve with the ability to design controlled experiments? We introduce RevengeBench, a benchmark of 75 LLM generated, Elo-calibrated policies across five game environments, drawn from CodeClash tournament trajectories. The learner observes the hidden target policy play against sampled opponents and designs behavioral probes in the form of custom opponent policies that elicit informative behavior. It then submits an executable hypothesis, which is evaluated using continuous action-distance metrics. We further validate that recovered code carries informative signal in downstream player-versus-player tournaments. Across twelve frontier LLMs, recovery quality varies substantially (34 to 72% of initial distance closed), with reconstructed policies yielding measurable competitive advantage, particularly for weaker models that otherwise struggle to design effective counter-strategies. Our benchmark positions behavioral recovery of programmatic policies as a tractable inverse problem in code-space, opening a path to opponent modeling, policy interpretability, and the broader question of inferring latent mechanisms from observations.
匹配关键词: automated research
---

[ACADEMIC - ARXIV]
标题: TryOnCrafter: Unleashing Camera Trajectories for Realistic Video Virtual Try-on via a Renderable 4D Try-on Proxy
作者: Hao Sun, Hao Yan, Mengting Chen, Quanjian Song, Yu Li, Juan Cao, Jinsong Lan, Xiaoyong Zhu, Bo Zheng, Sheng Tang
链接: https://arxiv.org/abs/2606.26092v1
完整摘要: While Video Virtual Try-on (VVT) has achieved remarkable progress in synthesizing realistic garment overlays on dynamic subjects, existing paradigms remains fundamentally constrained by a passive dependency on source camera trajectories, failing to accommodate the requisite interactive freedom for omnidirectional viewpoint exploration. To address this limitation, we define a pioneering research frontier: Camera-controllable Video Virtual Try-on (CaM-VVT). Unlike conventional VVT, CaM-VVT not only necessitates viewpoint-agnostic texture hallucination but also strict structural synchronization between non-rigid human dynamics and background contexts under arbitrary, unconstrained camera movements. To tackle these challenges, we present TryOnCrafter, the first unified DiT-based framework specifically architected for the CaM-VVT task. Departing from implicit pixel-space manipulation, we introduce a Renderable 4D Try-on Proxy that explicitly decouples the human subject from the environment. This is achieved by distilling high-fidelity 2D try-on priors into a clothed 3DGS-based avatar, which is subsequently animated via SMPL-X sequences and metric-aligned into a reconstructed background point cloud. This proxy establishes a robust structural foundation with superior texture density and motion integrity. Our Proxy-Anchored Video DiT leverages this robust structural foundation as a primary geometric anchor, ensuring that the synthesized photorealistic videos are strictly constrained by prescribed trajectories and physically plausible deformations. Benefiting from the inherent editability of the 4D proxy, TryOnCrafter facilitates diverse downstream applications, including human relocalization, ``bullet time'' effects, and $360$-degree orbital viewing.
匹配关键词: automated research
---

[ACADEMIC - ARXIV]
标题: Model Forensics: Investigating Whether Concerning Behavior Reflects Misalignment
作者: Aditya Singh, Gerson Kroiz, Senthooran Rajamanoharan, Neel Nanda
链接: https://arxiv.org/abs/2606.26071v1
完整摘要: A central goal of safety research is determining whether a model is misaligned. Prior work has largely focused on detecting concerning behavior. But behavior alone does not establish misalignment: a concerning action can arise from benign causes such as confusion. This motivates model forensics: investigating whether the action was driven by malign intent. In this paper, we propose a baseline protocol for model forensics consisting of two steps, iterated as needed. First, we read the chain of thought (CoT) to generate hypotheses about what drives model behavior. Second, we make edits to the prompt or environment to test these hypotheses. While the CoT is not always faithful, it is a rich source of unsupervised insight that can guide the collection of more rigorous evidence. To evaluate our protocol, we create a suite of six agentic environments where models exhibit concerning behavior, and apply it to each. We establish that Kimi K2 Thinking takes shortcuts due to a genuine disposition towards low-effort actions, by showing this hypothesis successfully predicts its behavior. Through counterfactual experiments, we show DeepSeek R1 deceives out of a desire to be consistent with a previous instance of itself. Our methods nonetheless leave significant room for refinement. For example, when we test whether Kimi K2 Thinking believes it is violating user intent, we find no evidence of such a belief, but without positive controls we cannot confirm our tests would detect it. Overall, we find our simple protocol provides a strong baseline that we hope future work will improve upon. More broadly, our work is a concrete step in developing the growing field of model forensics.
匹配关键词: automated research
---

[ACADEMIC - ARXIV]
标题: A welding penetration prediction model for laser welding process based on self-supervised learning using physics-informed neural networks
作者: Sen Li, Xiaoying Liu, Xiaojian Xu, Chendong Shao, Yaqi Wang, Ling Lan, Xinhua Tang, Haichao Cui
链接: https://arxiv.org/abs/2606.26059v1
完整摘要: The laser welding full-penetration is of critical importance, as it constitutes one of the fundamental factors in achieving defect-free welded joints. Accurate prediction of the penetration state is therefore essential for ensuring weld quality. To this end, this paper introduces SimPhysNet, a novel algorithm that achieves high classification accuracy in laser welding penetration prediction using only a limited number of labelled images. This approach effectively overcomes the limitations of supervised learning classification algorithms, which are hindered in industrial applications by their dependence on extensive, high-quality labelled data. The core of SimPhysNet is a unique self-supervised learning paradigm that embeds physical priors into a contrastive learning framework. By incorporating a physics-informed neural network (PINN), the model is guided to extract physically meaningful features of the molten pool and keyhole from a large set of unlabelled data, while three image augmentation tasks further enhance its generalization capabilities. Subsequently, a few-shot learning strategy, based on prototypical networks, enables robust classification by constructing class representations from a minimal set of labelled images. Experimental results demonstrate that SimPhysNet achieves a classification accuracy of 96.06% using only 200 labelled images (approximately 5% of the total labelled dataset), which is comparable to the performance of conventional supervised learning algorithms that utilize the entire labelled dataset. This work presents a new, efficient, and highly accurate method, providing the way for the intelligent automation of laser welding.
匹配关键词: automated research
---

[ACADEMIC - ARXIV]
标题: Can Trustless Agents Be Trusted? An Empirical Study of the ERC-8004 Decentralized AI Agent Ecosystem
作者: Xihan Xiong, Zelin Li, Wei Wei, Qin Wang, William Knottenbelt, Zhipeng Wang
链接: https://arxiv.org/abs/2606.26028v1
完整摘要: As autonomous AI agents increasingly transact across organizational boundaries, a fundamental trust challenge emerges: how can an agent assess whether an unknown counterpart is trustworthy? The ERC-8004 protocol addresses this challenge with the first permissionless trust layer for AI agent economies, built around three on-chain registries for Identity, Reputation, and Validation. Despite its rapid adoption, the protocol has not been studied empirically, leaving it unclear whether the information it records provides a trustworthy basis for decision-making. To address this gap, we present the first empirical study of ERC-8004 across three chains: Ethereum, BNB Smart Chain (BSC), and Base, covering the period from protocol deployment through May 13, 2026. We crawl on-chain Identity and Reputation events, off-chain files, and x402 payment transactions. On the identity side, we find that most registrations are placeholders rather than active agents, with only a small fraction (3%, 4%, and 15% across Ethereum, BSC, and Base) exposing a valid ERC-8004 registration file with at least one live service endpoint. On the reputation side, we show that the Registry, as currently deployed, cannot function as a trust signal: values are not commensurable, feedback records are rarely grounded in verifiable interactions, and reputation can be manipulated at minimal cost. Consistent with these design weaknesses, we find that a substantial fraction of reviewers (73.6%, 59.2%, and 90.6% across Ethereum, BSC, and Base) exhibit coordinated Sybil behavior. After removing Sybil-flagged feedback, 15.5%, 72.3%, and 89.4% of rated agents, respectively, are left with no valid feedback. We then turn these findings into concrete recommendations for future revisions of ERC-8004. Our study yields actionable protocol-design implications and establishes an empirical baseline for research on AI agent markets.
匹配关键词: automated research
---

[ACADEMIC - ARXIV]
标题: RevengeBench: Reverse Engineering Code-Space Policies from Behavioral Experiments
作者: Babak Rahmani, Sebastian Dziadzio, Joschka Strüber, Sergio Hernández-Gutiérrez, Matthias Bethge
链接: https://arxiv.org/abs/2606.26094v1
完整摘要: For most of scientific history, researchers studying behavior could only infer hidden mechanisms from outward actions: an inverse problem that becomes more tractable when observation is augmented by targeted intervention. We pose a computational analogue: given only behavioral traces of an agent in a game environment, can a learner reconstruct the underlying decision program as executable code, and how much does this reconstruction improve with the ability to design controlled experiments? We introduce RevengeBench, a benchmark of 75 LLM generated, Elo-calibrated policies across five game environments, drawn from CodeClash tournament trajectories. The learner observes the hidden target policy play against sampled opponents and designs behavioral probes in the form of custom opponent policies that elicit informative behavior. It then submits an executable hypothesis, which is evaluated using continuous action-distance metrics. We further validate that recovered code carries informative signal in downstream player-versus-player tournaments. Across twelve frontier LLMs, recovery quality varies substantially (34 to 72% of initial distance closed), with reconstructed policies yielding measurable competitive advantage, particularly for weaker models that otherwise struggle to design effective counter-strategies. Our benchmark positions behavioral recovery of programmatic policies as a tractable inverse problem in code-space, opening a path to opponent modeling, policy interpretability, and the broader question of inferring latent mechanisms from observations.
匹配关键词: scientific discovery
---

[ACADEMIC - ARXIV]
标题: AI-Assisted Computational Reproducibility on the FABRIC Testbed
作者: Komal Thareja, Paul Ruth, Berent Aldikacti, Michael Zink
链接: https://arxiv.org/abs/2606.25879v1
完整摘要: Computational reproducibility remains difficult despite being central to scientific research. In this paper, we show how the international FABRIC testbed, combined with large language model (LLM) coding assistants through LoomAI, can simplify reproducing published experiments across multiple domains. We reproduced three case studies on FABRIC, covering BBR-family congestion-control evaluations, LAMMPS molecular dynamics scaling benchmarks on a CPU-only MPI cluster, and stress protein homeostasis genomics pipelines. Rather than focusing only on matching numerical outputs, we evaluate whether the reproduced experiments support the same scientific conclusions as the original studies. The AI assistant was effective in setting up the environment, adapting code, and debugging, but struggled with the analysis stages that lacked clearly defined workflows, which required human guidance to establish execution order and data dependencies. Across the case studies, the AI-assisted workflow reduced reproduction effort by roughly 4--6 times. We conclude with practical recommendations for improving AI-assisted reproducibility on research testbeds.
匹配关键词: scientific discovery
---

[ACADEMIC - ARXIV]
标题: Hybrid deep learning-based phase diversity method for wavefront reconstruction
作者: Y. Rodimkov, A. Kotov, K. Burdonov, S. Perevalov, V. Volokitin, I. Meyerov, A. Soloviev
链接: https://arxiv.org/abs/2606.25855v1
完整摘要: The efficiency of high-power laser systems is limited by wavefront distortions in the beam, particularly non-common path aberrations, which reduce the peak intensity at the focal plane. Compensating for these aberrations requires the calibration of the adaptive optics system. Conventional calibration methods rely on a time-consuming iterative optimization that is highly sensitive to initial conditions. While deep learning-based models offer high speed, they often demonstrate insufficient accuracy. In this work, we present a hybrid wavefront reconstruction method that combines a convolutional neural network to generate an initial estimate of the wavefront distortions, with the L-BFGS (Limited-memory Broyden-Fletcher-Goldfarb-Shanno) algorithm for its subsequent refinement. In numerical simulations, the method achieved an efficiency of $\sim 0.99$ in 80% of the cases for a root-mean-square (RMS) of wavefront distortions ranging from 0 to $1.3λ$. In a physical experiment, for initial wavefront distortions with RMS values from 0.15 to $0.6λ$, the method achieved an efficiency of $\sim 0.75$. As a result, focusing with a Strehl ratio of $0.96 \pm 0.02$ was attained within 2 to 4 iterations of the algorithm, confirming the applicability of the method for the fast and accurate calibration of adaptive optics systems under real experimental conditions.
匹配关键词: scientific discovery
---

[ACADEMIC - ARXIV]
标题: Position Spaces and Graphs
作者: Rita-Nathalia Assaf, Tom Davot, Frédéric Lardeux, Frédéric Saubion
链接: https://arxiv.org/abs/2606.25719v1
完整摘要: In this paper, we introduce position graphs, a graph-based reasoning framework based on the formalization of position spaces. This framework utilizes two strict partial orders, representing horizontal and vertical alignment and precedence, to model the relative positions of discrete tokens. Unlike general qualitative spatial calculi, position graphs are constrained by a chain condition and compatibility requirements that focus on rows and columns. We provide a comprehensive theoretical analysis of this representation, beginning with a characterization of graph consistency. Conditions to ensure the consistency of position graphs are established. Furthermore, we investigate the computational complexity of structural pattern discovery, modeled as the induced subgraph isomorphism problem. We demonstrate that this problem remains NP-complete even within the restricted class of position graphs. While initially motivated by document processing, this work focuses on the underlying mathematical properties and algebraic consistency of position-based constraints, providing a formal logical layer that is independent of specific data extraction techniques.
匹配关键词: scientific discovery
---

[ACADEMIC - ARXIV]
标题: Agentic evolution of physically constrained foundation models
作者: Jiangwei Zhang, Wen Sun, Chong Wang, Shiyao Li, Cheng Che, Chunjing Han, Dan Meng, Jian Yang, Yu Wang, Rui Hou
链接: https://arxiv.org/abs/2606.25532v1
完整摘要: Artificial intelligence increasingly drives automated scientific discovery, yet contemporary generalist agents lack physical grounding, frequently hallucinating hardware-incompatible designs. Here, we present a physically grounded, multi-agent discovery engine that autonomously architects hardware-compliant computing systems. Anchored by an Evolutionary Knowledge Graph structuring past scientific innovations, the framework extracts an "algorithmic Chain-of-Thought" to transform blind stochastic search into directed structural evolution. Applied to the extreme testbed of foundation model deployment, the engine evolved two hardware-aware compression methodologies surpassing human-engineered heuristics: Q-Enhance mitigates long-context accuracy loss in dense models, and MoE-Salient-AQ outperforms state-of-the-art manual sparse Mixture-of-Experts designs by 3.7% at sub-3-bit regimes. Utilizing a bandwidth-efficient Sensitivity Profile, we successfully deployed a massive 235-billion-parameter model onto a constrained dual-A100 server, reducing memory requirements by 75% with a marginal 0.64% accuracy degradation. By transforming unconstrained combinatorial search into knowledge-driven autonomy, this establishes a scalable hardware-software co-design paradigm for machine-driven discovery within strict physical boundaries.
匹配关键词: scientific discovery
---

[ACADEMIC - ARXIV]
标题: RevengeBench: Reverse Engineering Code-Space Policies from Behavioral Experiments
作者: Babak Rahmani, Sebastian Dziadzio, Joschka Strüber, Sergio Hernández-Gutiérrez, Matthias Bethge
链接: https://arxiv.org/abs/2606.26094v1
完整摘要: For most of scientific history, researchers studying behavior could only infer hidden mechanisms from outward actions: an inverse problem that becomes more tractable when observation is augmented by targeted intervention. We pose a computational analogue: given only behavioral traces of an agent in a game environment, can a learner reconstruct the underlying decision program as executable code, and how much does this reconstruction improve with the ability to design controlled experiments? We introduce RevengeBench, a benchmark of 75 LLM generated, Elo-calibrated policies across five game environments, drawn from CodeClash tournament trajectories. The learner observes the hidden target policy play against sampled opponents and designs behavioral probes in the form of custom opponent policies that elicit informative behavior. It then submits an executable hypothesis, which is evaluated using continuous action-distance metrics. We further validate that recovered code carries informative signal in downstream player-versus-player tournaments. Across twelve frontier LLMs, recovery quality varies substantially (34 to 72% of initial distance closed), with reconstructed policies yielding measurable competitive advantage, particularly for weaker models that otherwise struggle to design effective counter-strategies. Our benchmark positions behavioral recovery of programmatic policies as a tractable inverse problem in code-space, opening a path to opponent modeling, policy interpretability, and the broader question of inferring latent mechanisms from observations.
匹配关键词: hypothesis generation
---

[ACADEMIC - ARXIV]
标题: On-Policy Self-Distillation with Sampled Demonstrations Reduces Output Diversity
作者: Andrei Liviu Nicolicioiu, Mohammad Pezeshki, Aaron Courville
链接: https://arxiv.org/abs/2606.26091v1
完整摘要: On-policy self-distillation achieves strong pass@1 accuracy by using a single model as both teacher and student, with the teacher conditioned on a correct demonstration to provide dense token-level feedback. We show that this could come at a hidden cost: rollout diversity decreases and pass@k curves flatten (i.e., generating more rollouts fails to improve accuracy). We trace this to compounding biases in the design of self-distillation with sampled demonstrations. The teacher scores each student rollout while conditioned on a sampled correct rollout, channeling its feedback through the model's own biases. We theoretically analyze the optimal self-distillation policy and show that it tilts the base distribution by a pointwise conditional mutual information score between the student's rollout and the correct rollout used as context. Unlike the ideal optimal on-policy reinforcement learning (RL), which preserves probability ratios among equally correct rollouts, self-distillation can amplify existing probability gaps, concentrating mass on already-dominant modes. On a controlled graph path-finding task and science question-answering benchmarks, self-distilled models match or exceed RL on average performance but exhibit substantially lower functional and semantic diversity, failing on out-of-distribution settings that require diverse strategies.
匹配关键词: hypothesis generation
---

[ACADEMIC - ARXIV]
标题: MVTrack4Gen: Multi-View Point Tracking as Geometric Supervision for 4D Video Generation
作者: JoungBin Lee, Jaewoo Jung, Jongmin Lee, Tongmin Kim, Hyunsung Kim, Takuya Narihira, Kazumi Fukuda, Jahyeok Koo, Jisang Han, Yuki Mitsufuji, Seungryong Kim
链接: https://arxiv.org/abs/2606.26087v1
完整摘要: Synthesizing a novel-view video from a monocular reference video along a target camera trajectory requires both geometric consistency and motion fidelity with respect to the reference video. Existing methods based on explicit 3D representations are limited by the accuracy of off-the-shelf reconstruction modules, which often produce inaccurate geometry for dynamic objects in monocular videos. In contrast, camera-conditioning-only methods can achieve high visual quality but often struggle to preserve geometric and motion consistency. In this work, we introduce MVTrack4Gen (Multi-View point Tracking for Novel-View Generation), a motion-aware training framework that leverages multi-view point tracking as an additional geometric and motion supervision signal for camera-conditioning-only novel-view video diffusion models. Our key finding is that specific attention layers encode strong correspondence cues, where query features attend to key features at geometrically corresponding locations across views and over time, and the misalignment of these correspondences causes motion inconsistency. Based on this observation, we route these features into an auxiliary multi-view tracking head and jointly train the diffusion model with a point-tracking objective. By explicitly strengthening these motion-aware correspondences, MVTrack4Gen improves existing models to better follow the motion in the reference view and maintain cross-view geometric consistency. Across diverse benchmarks, our method achieves state-of-the-art geometric consistency and competitive camera accuracy.
匹配关键词: hypothesis generation
---

[ACADEMIC - ARXIV]
标题: Neglected Free Lunch from Post-training: Progress Advantage for LLM Agents
作者: Changdae Oh, Wendi Li, Seongheon Park, Samuel Yeh, Tanwi Mallick, Sharon Li
链接: https://arxiv.org/abs/2606.26080v1
完整摘要: Process reward models enable fine-grained, step-level evaluation of LLMs, yet building them for agentic settings remains prohibitively difficult: long-horizon interactions, irreversible actions, and stochastic environment feedback make both human annotation and Monte Carlo estimation infeasible at scale. In this work, we show that reinforcement learning (RL) post-training already provides the ingredients for effective step-level scoring, eliminating the need for dedicated reward model training altogether. Concretely, we derive an implicit advantage under a general stochastic Markov decision process, which we term progress advantage -- log-probability ratio between the RL-trained policy and its reference policy exactly recovers the optimal advantage function. This formulation makes the resulting signal annotation-free, domain-agnostic, and available as a byproduct of the standard RL post-training pipeline. We validate the effectiveness of the progress advantage across three different applications: test-time scaling, uncertainty quantification, and failure attribution on five benchmarks and four model families. Across all settings, it consistently outperforms confidence-based baselines and, despite requiring no task-specific training, surpasses dedicated trained reward models. We complement these results with deeper analyses on characteristics of progress advantage, offering practical guidance for adoption in real-world agentic systems.
匹配关键词: hypothesis generation
---

[ACADEMIC - ARXIV]
标题: Same Evidence, Different Answer: Auditing Order Sensitivity in Multimodal Large Language Models
作者: Akshay Paruchuri, Sanmi Koyejo, Ehsan Adeli
链接: https://arxiv.org/abs/2606.26079v1
完整摘要: Standard benchmarks for multimodal large language models (MLLMs) score each item on one canonical ordering and miss whether order-irrelevant shuffling changes the answer, a baseline reliability property called for by emerging AI evaluation guidelines. We introduce Facet-Probe, a five-facet audit (option, evidence-chunk, document-rank, image-set, and mixed-modality ordering) of 18 frontier and open-weight MLLMs. A Bayesian item-response model separates ordering noise from per-facet bias, and a same-ordering control estimates the decoder-stochastic floor for observed flips. We find that none of the 18 MLLMs we audit are order-invariant: screened per-facet panel-mean flip rates span 24-50%. A Gemini same-ordering control at temperature 0 estimates a substantial ordering excess over a same-input decoder-noise floor in verified cells. Capability predicts but does not eliminate flips; the best model still flips on 13.4% of trials. In our Gemini mitigation tests, training-free prompt changes are modality-conditional and do not transfer from text to visual reasoning. These results suggest that prompt-level mitigation alone is unlikely to provide general order robustness, motivating future work on training-time and architectural approaches. We propose cross-ordering flip rate as a standard reporting axis for MLLMs.
匹配关键词: hypothesis generation
---

[ACADEMIC - ARXIV]
标题: FORGE: Fused On-Register Gradient Elimination for Memory-Efficient LLM Training
作者: Dikshant Kukreja, Kritarth Prasad, Avinash Anand, Zhengkui Wang, Erik Cambria, Timothy Liu, Aik Beng Ng, Simon See, Bapi Chatterjee
链接: https://arxiv.org/abs/2606.22932v1
完整摘要: Reverse-mode differentiation computes every weight gradient, writes it to memory, and only then lets the optimizer read it back. This two-phase schedule sets the memory ceiling of modern training: at the seam between the phases, every layer's gradient is live at once. We argue that this materialized gradient is an artifact of how differentiation is staged, not a quantity that learning requires -- and we eliminate it. FORGE folds the optimizer step into the backward pass and applies it one tile at a time, entirely in registers, so each gradient tile is consumed the instant it is produced and never becomes a tensor. The fusion changes only when the update happens, not what it computes: in full precision the fused step is provably exact -- the identical optimizer update, for every element-wise rule -- and that exactness survives tensor- and sequence-parallel sharding; in the bf16 and 8-bit regimes used in practice it is faithful rather than bit-identical, its deviation bounded and, for the weight store, rendered unbiased by stochastic rounding. Because each gradient tile is born and consumed in the same registers, it is never converted down to bf16 to be stored and read back; FORGE thus preserves the full-precision fidelity that both bf16 and 8-bit optimizers lose to that conversion. Nor is the method tied to one architecture or one optimizer: linear layers are ubiquitous, and FORGE reclaims the gradient memory of any of them under any element-wise rule. Empirically FORGE more than halves the memory of an optimizer step and, at the small batch sizes typical of fine-tuning and continued pretraining, runs about 1.5x faster; integrated into tensor-parallel Megatron-LM it fits 8B training at four times the micro-batch a standard optimizer allows on the same GPUs.
匹配关键词: Megatron
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
标题: Speculative Decoding at Temperature Zero: A Scoped Safety-Invariance Screen with a 48,072-Sample Expansion
作者: Sahil Kadadekar
链接: https://arxiv.org/abs/2606.25097v1
完整摘要: Speculative decoding accelerates inference by letting a draft model propose tokens for a target model to verify, raising a concrete safety question: at temperature zero, can draft-side behavior leak into safety-scored outputs? We answer with Typical-Acceptance Invariance Screen (TAIS), a behavioral-equivalence screen that pairs target-only and speculative outputs on the same safety battery and requires byte-identity evidence, TOST equivalence at +/-3pp, and per-task Cohen's h below a calibrated null cutoff of |h| < 0.1. Applied to a 16,783-sample confirmatory core plus 44,066 matched expansion samples (fp16/bf16 execution, canonical and DPO-adversarial drafts, GPTQ-4bit drafts, two seeds, and four safety benchmarks), the tested temperature-zero vLLM stacks show no detectable safety divergence under TAIS. The largest absolute Cohen's h on matched target-only versus speculative refusal is 0.024, roughly an order of magnitude below the conventional trivial-effect floor; 25 of 27 per-task TOST contrasts pass at the +/-3pp margin (the two non-pass contrasts are capability-domain Wald-CI edge cases at identical ceiling rates, not genuine non-equivalence); the DPO-adversarial draft produces byte-identical output to the canonical draft across 4,006 samples; and bf16 changes 36%-53% of output bytes without moving any per-task safety rate outside equivalence. A separate 4,006-sample 70B production-scale probe, which lacks a matched 70B target-only arm and is therefore not counted as a TAIS pass, produces AdvBench refusal 0.839 over 700 AdvBench completions with 95% Wilson CI [0.809, 0.864]. We make no claim about sampling temperatures, untested frameworks, untested model families, or tree-speculation variants such as EAGLE and Medusa.
匹配关键词: vLLM
---

[ACADEMIC - ARXIV]
标题: Revealing Training Data Exposure in Vision Language Large Models via Parameter Gradients
作者: Zhihao Zhu, Hongyi Tang, Yi Yang, Ahmed Abbasi
链接: https://arxiv.org/abs/2606.24774v1
完整摘要: Vision-Language Large Models (VLLMs) trained on massive crawled corpora raise pressing copyright and data-provenance concerns. These concerns are particularly acute in healthcare, where patient medical images paired with clinical reports demand rigorous privacy safeguards. However, existing training data detection methods either fail in cross-modal scenarios or rely on superficial output signals with insufficient discriminative power. We introduce GradAudit, a gradient-based auditing framework that examines internal optimization dynamics rather than treating VLLMs as black boxes. Our approach builds on a key observation: model parameters converge to regions where gradients on training samples become stable and well-aligned, whereas gradients on non-training samples remain noisy and inconsistent. By analyzing these gradient signatures, GradAudit achieves strong separability and detects genuine image-text associations learned during training, not merely individual modality membership. Empirically, across both medical and general-domain datasets, GradAudit substantially outperforms state-of-the-art baselines in both pretraining and fine-tuning VLLMs. In a case study employing copyrighted content, we show that existing training data detection methods not only underestimate the extent of unauthorized data usage, but that this underestimation becomes more pronounced as models become more recent and more advanced.
匹配关键词: vLLM
---

[ACADEMIC - ARXIV]
标题: Geometry-Aware Online Scheduling for LLM Serving: From Theoretical Bound to System Practice
作者: Li Kong, Qi Qi, Yinyu Ye, Zijie Zhou
链接: https://arxiv.org/abs/2606.22327v2
完整摘要: The explosive demand for interactive Large Language Model serving has highlighted the management of the Key-Value cache's dynamic memory footprint as a critical area for performance optimization in inference engines. Modern inference systems overwhelmingly rely on time-centric scheduling heuristics, such as Shortest Job First. However, their theoretical optimality is rooted in traditional schedule modeling, failing to capture the highly dynamic, 2D spatio-temporal geometric growth specific to LLM inference mechanisms. To resolve this, we propose the geometry-aware online scheduling by introducing the Smallest Volume First (SVF) algorithm and its highly efficient variant, 1-bit SVF. Theoretically, we provide a rigorous mathematical foundation for our approach. Via a novel volume-certificate proof, we sharpen SVF's worst-case competitive ratio from the prior best of 48 towards \textbf{3} in the high-concurrency regime of LLM serving. Building upon this core breakthrough, we complete a comprehensive theoretical taxonomy analyzing our algorithms across different traffic scenarios and information availability. Practically, we seamlessly integrate our approach as a plug-and-play layer in vLLM. Extensive evaluations on Llama-3.1 models demonstrate comprehensive performance gains: SVF delivers strong reductions in both average and tail latency, while 1-bit SVF, with merely a single bit information, achieves competitive throughput and latency. This work establishes a theoretically sound and empirically proven approach for resolving memory-constrained scheduling in modern LLM deployments. To facilitate future research, our code is available at https://github.com/Aurora-Kl/Geometry-Aware-Online-Scheduling.git.
匹配关键词: vLLM
---

[ACADEMIC - ARXIV]
标题: Recency/Frequency Adaptive KV Caching for Large Language Model Serving
作者: Yang Shen, Meghana Madhyastha, Robert Underwood, Bogdan Nicolae, Randal Burns
链接: https://arxiv.org/abs/2606.21238v1
完整摘要: Key-value (KV) caching is a powerful technique for accelerating large language model inference and generation. Inference workloads are large and diverse, which makes them difficult to cache effectively. Existing cache management strategies adopt the least-recently-used policy for evicting cache blocks. However, LRU leads to multiple unrelated workloads flushing each other's caches. To address this, we integrate adaptive caching that dynamically allocates cache space between recently and frequently occurring KV blocks. Evaluations show that it improves the KV cache hit rate by up to 10.8% and reduces time to first token by up to 12.6% over naive vLLM on synthetic document question answering workloads, and 2.1% and 2.0% respectively on real-world conversation workloads. The method generalizes well to batch inference and demonstrates clear interpretability while effectively accommodating diverse workloads.
匹配关键词: vLLM
---

[ACADEMIC - ARXIV]
标题: UltraQuant: 4-bit KV Caching for Context-Heavy Agents
作者: Inesh Chakrabarti, David Limpus, Aditi Ghai Rana, Bowen Bao, Spandan Tiwari, Thiago Crepaldi, Ashish Sirasao
链接: https://arxiv.org/abs/2606.20474v2
完整摘要: Context-heavy agents place unusual pressure on the key-value (KV) cache: long prefixes are reused across many short turns, while concurrency determines whether the serving system can keep GPUs utilized. We study 4-bit KV-cache compression for this setting, using TurboQuant-style rotation and codebook quantization as a quality anchor and vLLM FP8 KV caching as the deployment anchor. We report three contributions. First, we frame 4-bit KV caching around multi-round agent workloads where task quality, cache residency, and serving throughput must be measured jointly. Second, we describe the practical design choices needed to make the 4-bit path robust, including asymmetric K/V treatment, Walsh-Hadamard rotation, QJL removal, and block-scale variants. Third, we present serving optimizations on AMD GPUs, including optimized decode-attention kernels and UltraQuant, an FP4 approximation path that uses FP8 queries, FP4 KV tensors, UE8M0 group scales, and native scaled-MFMA support on CDNA4. On a long-context, multi-turn agentic workload, UltraQuant cuts P50 time-to-first-token by 3.47x in the cache-pressured late rounds (2.3x across all rounds) and raises output throughput by 1.63x over the FP8 KV baseline.
匹配关键词: vLLM
---

[ACADEMIC - ARXIV]
标题: SCENIC: Semantic-Conditioned Edge-Aware Neural Framework for Structured IoT Command Generation
作者: Luke Ztz Hu, Hongbing Lang, Songping Mai
链接: https://arxiv.org/abs/2606.22296v1
完整摘要: Edge Internet of Things (IoT) agents are often constrained by memory capacity, privacy requirements, communication latency, and recurring inference cost. Current smart-home assistants commonly rely on API-level command interfaces or cloud-based language models that remain difficult to deploy on edge devices. This paper addresses edge IoT command generation as a many-to-one structured output task, where multiple natural-language instructions map to the same canonical command string for deterministic smart-home parsing. To support this setting, we propose Semantic-Conditioned Edge-Aware Neural Framework for Structured IoT Command Generation (SCENIC), an end-to-end framework covering model architecture selection, Smart Home Instruct data generation, triplet-loss contrastive supervised fine-tuning, pruning and quantization, and deployment-oriented export. We evaluate sub-0.2B-scale transformer backbones, which are, to the best of our knowledge, among the smallest language-model backbones studied for edge IoT structured command generation. On Smart Home Instruct-Bench, the strongest dense decoder-only row reaches 99.0% EM@1, while the encoder-decoder model retains stronger high-sparsity behavior. A representative pruned INT8 encoder-decoder export preserves 91.0% EM@1 and 99.0% EM@5 while reducing exported model size by 25.38%. TensorRT profiling of the NVIDIA 2:4 sparse encoder export further shows up to 1.8x encoder-component speedup, indicating that the selected encoder-decoder deployment path can retain structured command accuracy under edge-oriented compression while hardware acceleration evidence remains component-level. The SCENIC code and experimental artifacts are open sourced to support reproducibility.
匹配关键词: TensorRT
---

[ACADEMIC - ARXIV]
标题: EdgeZSAD: Practical Zero-Shot Anomaly Detection on Edge Devices
作者: Taewan Cho, Andrew Jaeyong Choi
链接: https://arxiv.org/abs/2606.16119v1
完整摘要: Industrial inspection needs zero-shot anomaly detection (ZSAD) that remains useful under edge deployment constraints. Recent methods often rely on ViT-L foundation backbones (~300M parameters), which exceed the memory and operator budget of typical embedded hardware. We study this regime through EdgeZSAD, a compact reference system built around a TinyViT-21M-512 backbone, an asymmetric global-local readout (EdgeGLR), and a reproducible source-side training recipe (Real-IAD-DR). We train a single checkpoint in a source-trained, target-unseen protocol and evaluate it across six industrial benchmarks. Across three independent runs, the resulting model reaches an average image AUROC of 91.6 on MVTec-AD and 88.2 on VisA, while remaining directly deployable on Jetson Orin Nano Super (TensorRT FP16) and RB5 Gen2 (QNN GPU FP16). Across the six device-rescored benchmarks, image-AUROC drift stays below 0.2 points, indicating that the exported graph preserves host-side ranking behavior in the evaluated deployment setting.
匹配关键词: TensorRT
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
标题: FAR-LIO: Enabling High-Speed Autonomy through Fast, Accurate, and Robust LiDAR-Inertial Odometry
作者: Maximilian Leitenstern, Marcel Weinmann, Patrick Haft, Tobias Lasser, Dominik Kulmer, Markus Lienkamp
链接: https://arxiv.org/abs/2606.26010v1
完整摘要: Robust and accurate odometry estimation is essential in modern robotics. In environments characterized by highly dynamic motion and sensor noise, odometry estimation becomes increasingly challenging. Autonomous racing combines both factors in an unstructured setting, where minimizing odometry latency is essential for stable closed-loop control. This paper introduces FAR-LIO, a highly optimized CUDA-accelerated LiDAR-inertial odometry framework developed for Fast, Accurate, and Robust performance. Our system leverages a novel CUDA-based voxel hashmap to enable parallelized nearest-neighbor search and efficient map updates. We employ a sparsity-aware Generalized Iterative Closest Point algorithm with adaptive thresholding on top of the CUDA-based voxel hashmap with adaptive density to achieve low-latency without compromising accuracy. An Extended Kalman Filter serves as a robust backend. It utilizes an upsampling and delay compensation strategy to fuse the LiDAR odometry with high-frequency IMU data, thereby ensuring a robust and smooth odometry output. We evaluate FAR-LIO across four different sensor setups, using both public datasets and data from two autonomous racecars driving at speeds of up to 250 km/h. FAR-LIO achieves an average 6.9% reduction in the positional error and 38.4% lower runtime compared to state-of-the-art baselines on target hardware using a single parameter set. This demonstrates its computational efficiency and broad applicability. To build upon our work, our code is available open-source on https://github.com/TUMFTM/FAR-LIO.
匹配关键词: CUDA
---

[ACADEMIC - ARXIV]
标题: Learning Action Priors for Cross-embodiment Robot Manipulation
作者: Dong Jing, Tianqi Zhang, Jiaqi Liu, Jinman Zhao, Zelong Sun, Li Erran Li, Zhiwu Lu, Mingyu Ding
链接: https://arxiv.org/abs/2606.26095v1
完整摘要: Most Vision-Language-Action (VLA) models build on a Vision-Language Model (VLM) backbone by attaching an action module and optimizing the full policy jointly. This design inherits strong visual and linguistic priors from the VLM, but leaves the action module to learn physical motion almost from scratch. As a result, the policy lacks an explicit motion prior, forcing early optimization to simultaneously discover temporal action dynamics and cross-modal alignment, a challenge further amplified in cross-embodiment settings. In this work, we propose to pretrain the action module with motion priors before cross-modal VLA alignment. Specifically, we introduce a two-stage training framework that equips the action module with cross-embodiment temporal motion structure before VLA training begins. In Stage~1, a lightweight flow-matching-based encoder-decoder action module efficiently learns temporal motion structure solely from unconditioned action trajectories, without processing visual or language tokens. In Stage~2, this learned prior is transferred to VLA training through decoder reuse and early-stage latent distillation, aligning visual-language features with the action embedding space while still allowing end-to-end policy refinement. In addition, the trained encoder serves as a compact history compressor, summarizing state-action histories into a single temporal context token for history-aware modeling at negligible cost. Extensive experiments across 13 diverse cross-embodiment tasks on both simulated and real-world platforms validate the effectiveness of our approach. Compared with VLA training without action priors, our model achieves faster convergence, higher success rates, and substantially stronger performance on data-scarce real-world tasks. Moreover, scaling up the action data in Stage~1 yields a more generalizable action prior that directly improves downstream VLA performance.
匹配关键词: latent diffusion
---

[ACADEMIC - ARXIV]
标题: RevengeBench: Reverse Engineering Code-Space Policies from Behavioral Experiments
作者: Babak Rahmani, Sebastian Dziadzio, Joschka Strüber, Sergio Hernández-Gutiérrez, Matthias Bethge
链接: https://arxiv.org/abs/2606.26094v1
完整摘要: For most of scientific history, researchers studying behavior could only infer hidden mechanisms from outward actions: an inverse problem that becomes more tractable when observation is augmented by targeted intervention. We pose a computational analogue: given only behavioral traces of an agent in a game environment, can a learner reconstruct the underlying decision program as executable code, and how much does this reconstruction improve with the ability to design controlled experiments? We introduce RevengeBench, a benchmark of 75 LLM generated, Elo-calibrated policies across five game environments, drawn from CodeClash tournament trajectories. The learner observes the hidden target policy play against sampled opponents and designs behavioral probes in the form of custom opponent policies that elicit informative behavior. It then submits an executable hypothesis, which is evaluated using continuous action-distance metrics. We further validate that recovered code carries informative signal in downstream player-versus-player tournaments. Across twelve frontier LLMs, recovery quality varies substantially (34 to 72% of initial distance closed), with reconstructed policies yielding measurable competitive advantage, particularly for weaker models that otherwise struggle to design effective counter-strategies. Our benchmark positions behavioral recovery of programmatic policies as a tractable inverse problem in code-space, opening a path to opponent modeling, policy interpretability, and the broader question of inferring latent mechanisms from observations.
匹配关键词: latent diffusion
---

[ACADEMIC - ARXIV]
标题: MVTrack4Gen: Multi-View Point Tracking as Geometric Supervision for 4D Video Generation
作者: JoungBin Lee, Jaewoo Jung, Jongmin Lee, Tongmin Kim, Hyunsung Kim, Takuya Narihira, Kazumi Fukuda, Jahyeok Koo, Jisang Han, Yuki Mitsufuji, Seungryong Kim
链接: https://arxiv.org/abs/2606.26087v1
完整摘要: Synthesizing a novel-view video from a monocular reference video along a target camera trajectory requires both geometric consistency and motion fidelity with respect to the reference video. Existing methods based on explicit 3D representations are limited by the accuracy of off-the-shelf reconstruction modules, which often produce inaccurate geometry for dynamic objects in monocular videos. In contrast, camera-conditioning-only methods can achieve high visual quality but often struggle to preserve geometric and motion consistency. In this work, we introduce MVTrack4Gen (Multi-View point Tracking for Novel-View Generation), a motion-aware training framework that leverages multi-view point tracking as an additional geometric and motion supervision signal for camera-conditioning-only novel-view video diffusion models. Our key finding is that specific attention layers encode strong correspondence cues, where query features attend to key features at geometrically corresponding locations across views and over time, and the misalignment of these correspondences causes motion inconsistency. Based on this observation, we route these features into an auxiliary multi-view tracking head and jointly train the diffusion model with a point-tracking objective. By explicitly strengthening these motion-aware correspondences, MVTrack4Gen improves existing models to better follow the motion in the reference view and maintain cross-view geometric consistency. Across diverse benchmarks, our method achieves state-of-the-art geometric consistency and competitive camera accuracy.
匹配关键词: latent diffusion
---

[ACADEMIC - ARXIV]
标题: G2DP: Diffusion Planning with Spatio-Temporal Grid Guidance
作者: Hang Yu, Ye Jin, Alessandro Canevaro, Julian Schmidt, Julian Jordan, Peizheng Li, Marc Kaufeld, Silvan Lindner, Johannes Betz, Wilhelm Stork
链接: https://arxiv.org/abs/2606.26017v1
完整摘要: In autonomous driving, diffusion-based planners have emerged as a promising paradigm for robust motion planning in dense and interactive traffic, as they can effectively model diverse driving behaviors. However, their inherent stochasticity often requires explicit guidance during denoising to ensure safety and route adherence for robust closed-loop execution. Existing guidance typically relies on sparse, entity-centric geometric queries or post-hoc refinement, yielding limited situational awareness and fragile performance in interactive scenes. To address this issue, we propose G2DP (Grid-Guided Diffusion Planning), a diffusion-based planner that directly enforces dense environmental constraints through inference-time guidance. Specifically, G2DP constructs a differentiable spatio-temporal cost volume by fusing probabilistic future occupancy distributions with a route-progress map. By formulating this volume as a continuous safety energy functional, it injects dense gradients directly into the denoising loop, actively steering trajectory generation toward collision-free and progress-optimal regions. Extensive closed-loop evaluations show that G2DP achieves state-of-the-art performance on nuPlan, outperforming the strongest imitation-learning baseline by +7.2 points in reactive score. It further maintains top scores in zero-shot transfers to interPlan and DeepScenario benchmarks, with collision avoidance improving by +10.15 over the unguided approach on interPlan. These results demonstrate that spatio-temporal cost grids serve as an effective representation for robust guidance in diffusion-based planning.
匹配关键词: latent diffusion
---

[ACADEMIC - ARXIV]
标题: MIMFlow: Integrating Masked Image Modeling with Normalizing Flows for End-to-End Image Generation
作者: Yang Chen, Xiaowei Xu, Shuai Wang, Xinwen Zhang, Qiushi Guo, Tiezheng Ge, Limin Wang
链接: https://arxiv.org/abs/2606.26016v1
完整摘要: Normalizing Flows (NFs) are powerful generative models capable of exact density estimation and sampling. However, their strict invertibility often forces the model to exhaust its capacity on low-level pixel details, hindering the capture of high-level semantic structures. While Masked Image Modeling (MIM) has excelled in representation learning, its integration into generative pipelines has remained largely modular and disjointed. In this paper, we propose MIMFlow, a unified end-to-end framework that jointly optimizes latent semantics, pixel reconstruction, and generative flow. By employing a VAE encoder to infer semantic latent from masked images, MIMFlow achieves a principled decoupling of the generative task: the Normalizing Flow focuses on modeling a simplified, low-frequency semantic manifold, while a specialized decoder handles high-frequency synthesis. This design effectively resolves the inherent capacity bottleneck of NFs, allowing the model to prioritize global structural coherence over redundant noise. Empirical results on ImageNet 256$\times$256 show that MIMFlow-L reaches 71.3\% linear probing accuracy and an FID of 2.50. Despite using only 128 tokens (50\% fewer than standard models), it yields a 32.8\% performance gain over similar-scale NF baselines. Our code is available at https://github.com/MCG-NJU/MIMFlow.
匹配关键词: latent diffusion
---

[ACADEMIC - ARXIV]
标题: Learning Action Priors for Cross-embodiment Robot Manipulation
作者: Dong Jing, Tianqi Zhang, Jiaqi Liu, Jinman Zhao, Zelong Sun, Li Erran Li, Zhiwu Lu, Mingyu Ding
链接: https://arxiv.org/abs/2606.26095v1
完整摘要: Most Vision-Language-Action (VLA) models build on a Vision-Language Model (VLM) backbone by attaching an action module and optimizing the full policy jointly. This design inherits strong visual and linguistic priors from the VLM, but leaves the action module to learn physical motion almost from scratch. As a result, the policy lacks an explicit motion prior, forcing early optimization to simultaneously discover temporal action dynamics and cross-modal alignment, a challenge further amplified in cross-embodiment settings. In this work, we propose to pretrain the action module with motion priors before cross-modal VLA alignment. Specifically, we introduce a two-stage training framework that equips the action module with cross-embodiment temporal motion structure before VLA training begins. In Stage~1, a lightweight flow-matching-based encoder-decoder action module efficiently learns temporal motion structure solely from unconditioned action trajectories, without processing visual or language tokens. In Stage~2, this learned prior is transferred to VLA training through decoder reuse and early-stage latent distillation, aligning visual-language features with the action embedding space while still allowing end-to-end policy refinement. In addition, the trained encoder serves as a compact history compressor, summarizing state-action histories into a single temporal context token for history-aware modeling at negligible cost. Extensive experiments across 13 diverse cross-embodiment tasks on both simulated and real-world platforms validate the effectiveness of our approach. Compared with VLA training without action priors, our model achieves faster convergence, higher success rates, and substantially stronger performance on data-scarce real-world tasks. Moreover, scaling up the action data in Stage~1 yields a more generalizable action prior that directly improves downstream VLA performance.
匹配关键词: robotics
---

[ACADEMIC - ARXIV]
标题: ForceBand: Learning Forceful Manipulation with sEMG
作者: Botao He, Zhi Wang, Linna Kuang, Ishaan Ghosh, Jitendra Malik, Cornelia Fermuller, Tingfan Wu, Jiayuan Mao, Ruoshi Liu, Haozhi Qi, Yiannis Aloimonos
链接: https://arxiv.org/abs/2606.26093v1
完整摘要: Human demonstrations are a scalable data source for learning robot manipulation policies. However, common sources of human demonstration data, such as motion-capture trajectories and internet videos, capture mostly motion and appearance while missing the contact forces that are critical for force-sensitive manipulation. In this paper, we introduce ForceBand, a low-cost wrist-worn sEMG system that turns human muscle activity into force-enriched demonstrations. We first collect a 10-hour multimodal dataset containing egocentric video, sEMG, IMU, and fingertip force measurements across diverse actions and objects. Using this dataset, we pre-train an EMG2Force model that predicts per-finger forces from sEMG and IMU signals. After a short user-specific calibration, users can collect target-task demonstrations using only ForceBand and video; EMG2Force then labels these demonstrations with per-finger force traces, producing force-augmented demonstrations for robot policy learning. Experiments show that ForceBand recovers fine-grained fingertip interactions with over 50% lower force prediction error than vision-based baselines and achieves an 87% success rate on pick, squeeze, and place tasks that require object-specific force control across objects with diverse shapes, sizes, and weights. Project website: https://forceband-emg.github.io
匹配关键词: robotics
---

[ACADEMIC - ARXIV]
标题: Deep Reinforcement Learning-Enhanced Event-Triggered Data-Driven Predictive Control for a 3D Cable-Driven Soft Robotic Arm
作者: Cheng Ouyang, Moeen Ul Islam, Kaixiang Zhang, Zhaojian Li, Xiaobo Tan, Dong Chen
链接: https://arxiv.org/abs/2606.26048v1
完整摘要: Soft robots are challenging to control due to their nonlinear and time-varying dynamics. Data-enabled predictive control (DeePC) offers a model-free alternative by directly leveraging measured input-output trajectories to construct a predictive controller. However, its receding-horizon formulation requires solving a constrained optimization problem at every sampling instant, which can be computationally demanding for real-time deployment on resource-limited robotic platforms.To address this limitation, we propose an adaptive reinforcement-learning-based event-triggered DeePC (RL-ET-DeePC) framework for soft robotic control. A model-free RL policy is trained to determine when to invoke the DeePC optimizer based on the current system state representation, thereby reducing unnecessary optimization calls while preserving closed-loop performance.Simulation results show that RL-ET-DeePC reduces optimization frequency by up to 66% compared to periodic DeePC, while maintaining comparable tracking accuracy. Hardware experiments on a three-dimensional cable-driven soft robotic arm demonstrate zero-shot transfer, achieving a 34% reduction in optimization frequency with tracking accuracy comparable to periodic DeePC and more consistent performance than a static threshold-based event-triggered baseline.
匹配关键词: robotics
---

[ACADEMIC - ARXIV]
标题: Learning Robot Visual Navigation in Crowds via Intention-Aware Scene Representations
作者: Han Bao, Bingyi Xia, Hanjing Ye, Yu Zhan, Hao Cheng, Baozhi Jia, Wenjun Xu, Jiankun Wang
链接: https://arxiv.org/abs/2606.26047v1
完整摘要: Robot crowd navigation requires the ability to infer human intentions while accounting for the structural constraints of the environment. Currently, deep reinforcement learning (DRL) provides a promising method for learning navigation policies that understand human intentions. However, most of them rely on limited scene representations, treating pedestrians as simple 2D points and ignoring rich visual cues from both humans and the environment. To address this issue, we introduce iCrowdNav, a novel visual crowd navigation method with intention-aware scene representations, to encode behavioral and structural context from egocentric visual observations. Our method employs two key components: a spatio-temporal encoder for extracting occupancy features of the scene, and Intent-Interact Former (I$^2$ Former), an attention-based module that encodes human poses to infer pedestrians' motion intentions. These features are integrated into a compact state embedding that supports effective DRL policy training. Extensive experiments show that our method achieves superior performance over baselines, and real-world deployment demonstrates vision-based crowd navigation.
匹配关键词: robotics
---

[ACADEMIC - ARXIV]
标题: RoboAtlas: Contextual Active SLAM
作者: Alexander Schperberg, Shivam K. Panda, Abraham P. Vinod, M. K. Jawed, Stefano Di Cairano
链接: https://arxiv.org/abs/2606.26046v1
完整摘要: We present RoboAtlas, a contextual Active SLAM framework that adaptively balances geometric exploration and semantic reasoning using a scalable 3D semantic mapping system, OpenRoboVox. RoboAtlas integrates frontier exploration, global semantic-map reasoning, and egocentric VLM-based reasoning through a contextual multi-armed bandit that transitions from exploration to semantically guided navigation as scene understanding improves. We evaluate the system in simulation and on a Unitree Go2 robot in large-scale real-world environments exceeding 1800 m2 with approx. 30k mapped semantic instances, achieving a 100% task success rate. On the GOAT-Bench "Val Unseen" benchmark, RoboAtlas achieves state-of-the-art performance with highest reported success rate (SR) of 90.6%, using GPT-4o, improving over the strongest prior baseline by 17.8 percentage points in SR. Using the much smaller Qwen2.5-VL-7B model, it still achieves 88.8% SR, outperforming all baselines using GPT-4o in SR, and revealing the importance of the information gained by our semantic mapping framework over simply replacing the underlying foundation model. The results demonstrate that grounding foundation models with large-scale 3D semantic maps enables robust and efficient contextual Active SLAM.
匹配关键词: robotics
---

[ACADEMIC - ARXIV]
标题: Learning Action Priors for Cross-embodiment Robot Manipulation
作者: Dong Jing, Tianqi Zhang, Jiaqi Liu, Jinman Zhao, Zelong Sun, Li Erran Li, Zhiwu Lu, Mingyu Ding
链接: https://arxiv.org/abs/2606.26095v1
完整摘要: Most Vision-Language-Action (VLA) models build on a Vision-Language Model (VLM) backbone by attaching an action module and optimizing the full policy jointly. This design inherits strong visual and linguistic priors from the VLM, but leaves the action module to learn physical motion almost from scratch. As a result, the policy lacks an explicit motion prior, forcing early optimization to simultaneously discover temporal action dynamics and cross-modal alignment, a challenge further amplified in cross-embodiment settings. In this work, we propose to pretrain the action module with motion priors before cross-modal VLA alignment. Specifically, we introduce a two-stage training framework that equips the action module with cross-embodiment temporal motion structure before VLA training begins. In Stage~1, a lightweight flow-matching-based encoder-decoder action module efficiently learns temporal motion structure solely from unconditioned action trajectories, without processing visual or language tokens. In Stage~2, this learned prior is transferred to VLA training through decoder reuse and early-stage latent distillation, aligning visual-language features with the action embedding space while still allowing end-to-end policy refinement. In addition, the trained encoder serves as a compact history compressor, summarizing state-action histories into a single temporal context token for history-aware modeling at negligible cost. Extensive experiments across 13 diverse cross-embodiment tasks on both simulated and real-world platforms validate the effectiveness of our approach. Compared with VLA training without action priors, our model achieves faster convergence, higher success rates, and substantially stronger performance on data-scarce real-world tasks. Moreover, scaling up the action data in Stage~1 yields a more generalizable action prior that directly improves downstream VLA performance.
匹配关键词: humanoid robot
---

[ACADEMIC - ARXIV]
标题: ForceBand: Learning Forceful Manipulation with sEMG
作者: Botao He, Zhi Wang, Linna Kuang, Ishaan Ghosh, Jitendra Malik, Cornelia Fermuller, Tingfan Wu, Jiayuan Mao, Ruoshi Liu, Haozhi Qi, Yiannis Aloimonos
链接: https://arxiv.org/abs/2606.26093v1
完整摘要: Human demonstrations are a scalable data source for learning robot manipulation policies. However, common sources of human demonstration data, such as motion-capture trajectories and internet videos, capture mostly motion and appearance while missing the contact forces that are critical for force-sensitive manipulation. In this paper, we introduce ForceBand, a low-cost wrist-worn sEMG system that turns human muscle activity into force-enriched demonstrations. We first collect a 10-hour multimodal dataset containing egocentric video, sEMG, IMU, and fingertip force measurements across diverse actions and objects. Using this dataset, we pre-train an EMG2Force model that predicts per-finger forces from sEMG and IMU signals. After a short user-specific calibration, users can collect target-task demonstrations using only ForceBand and video; EMG2Force then labels these demonstrations with per-finger force traces, producing force-augmented demonstrations for robot policy learning. Experiments show that ForceBand recovers fine-grained fingertip interactions with over 50% lower force prediction error than vision-based baselines and achieves an 87% success rate on pick, squeeze, and place tasks that require object-specific force control across objects with diverse shapes, sizes, and weights. Project website: https://forceband-emg.github.io
匹配关键词: humanoid robot
---

[ACADEMIC - ARXIV]
标题: Deep Reinforcement Learning-Enhanced Event-Triggered Data-Driven Predictive Control for a 3D Cable-Driven Soft Robotic Arm
作者: Cheng Ouyang, Moeen Ul Islam, Kaixiang Zhang, Zhaojian Li, Xiaobo Tan, Dong Chen
链接: https://arxiv.org/abs/2606.26048v1
完整摘要: Soft robots are challenging to control due to their nonlinear and time-varying dynamics. Data-enabled predictive control (DeePC) offers a model-free alternative by directly leveraging measured input-output trajectories to construct a predictive controller. However, its receding-horizon formulation requires solving a constrained optimization problem at every sampling instant, which can be computationally demanding for real-time deployment on resource-limited robotic platforms.To address this limitation, we propose an adaptive reinforcement-learning-based event-triggered DeePC (RL-ET-DeePC) framework for soft robotic control. A model-free RL policy is trained to determine when to invoke the DeePC optimizer based on the current system state representation, thereby reducing unnecessary optimization calls while preserving closed-loop performance.Simulation results show that RL-ET-DeePC reduces optimization frequency by up to 66% compared to periodic DeePC, while maintaining comparable tracking accuracy. Hardware experiments on a three-dimensional cable-driven soft robotic arm demonstrate zero-shot transfer, achieving a 34% reduction in optimization frequency with tracking accuracy comparable to periodic DeePC and more consistent performance than a static threshold-based event-triggered baseline.
匹配关键词: humanoid robot
---

[ACADEMIC - ARXIV]
标题: Learning Robot Visual Navigation in Crowds via Intention-Aware Scene Representations
作者: Han Bao, Bingyi Xia, Hanjing Ye, Yu Zhan, Hao Cheng, Baozhi Jia, Wenjun Xu, Jiankun Wang
链接: https://arxiv.org/abs/2606.26047v1
完整摘要: Robot crowd navigation requires the ability to infer human intentions while accounting for the structural constraints of the environment. Currently, deep reinforcement learning (DRL) provides a promising method for learning navigation policies that understand human intentions. However, most of them rely on limited scene representations, treating pedestrians as simple 2D points and ignoring rich visual cues from both humans and the environment. To address this issue, we introduce iCrowdNav, a novel visual crowd navigation method with intention-aware scene representations, to encode behavioral and structural context from egocentric visual observations. Our method employs two key components: a spatio-temporal encoder for extracting occupancy features of the scene, and Intent-Interact Former (I$^2$ Former), an attention-based module that encodes human poses to infer pedestrians' motion intentions. These features are integrated into a compact state embedding that supports effective DRL policy training. Extensive experiments show that our method achieves superior performance over baselines, and real-world deployment demonstrates vision-based crowd navigation.
匹配关键词: humanoid robot
---

[ACADEMIC - ARXIV]
标题: RoboAtlas: Contextual Active SLAM
作者: Alexander Schperberg, Shivam K. Panda, Abraham P. Vinod, M. K. Jawed, Stefano Di Cairano
链接: https://arxiv.org/abs/2606.26046v1
完整摘要: We present RoboAtlas, a contextual Active SLAM framework that adaptively balances geometric exploration and semantic reasoning using a scalable 3D semantic mapping system, OpenRoboVox. RoboAtlas integrates frontier exploration, global semantic-map reasoning, and egocentric VLM-based reasoning through a contextual multi-armed bandit that transitions from exploration to semantically guided navigation as scene understanding improves. We evaluate the system in simulation and on a Unitree Go2 robot in large-scale real-world environments exceeding 1800 m2 with approx. 30k mapped semantic instances, achieving a 100% task success rate. On the GOAT-Bench "Val Unseen" benchmark, RoboAtlas achieves state-of-the-art performance with highest reported success rate (SR) of 90.6%, using GPT-4o, improving over the strongest prior baseline by 17.8 percentage points in SR. Using the much smaller Qwen2.5-VL-7B model, it still achieves 88.8% SR, outperforming all baselines using GPT-4o in SR, and revealing the importance of the information gained by our semantic mapping framework over simply replacing the underlying foundation model. The results demonstrate that grounding foundation models with large-scale 3D semantic maps enables robust and efficient contextual Active SLAM.
匹配关键词: humanoid robot
---

[ACADEMIC - ARXIV]
标题: Learning Action Priors for Cross-embodiment Robot Manipulation
作者: Dong Jing, Tianqi Zhang, Jiaqi Liu, Jinman Zhao, Zelong Sun, Li Erran Li, Zhiwu Lu, Mingyu Ding
链接: https://arxiv.org/abs/2606.26095v1
完整摘要: Most Vision-Language-Action (VLA) models build on a Vision-Language Model (VLM) backbone by attaching an action module and optimizing the full policy jointly. This design inherits strong visual and linguistic priors from the VLM, but leaves the action module to learn physical motion almost from scratch. As a result, the policy lacks an explicit motion prior, forcing early optimization to simultaneously discover temporal action dynamics and cross-modal alignment, a challenge further amplified in cross-embodiment settings. In this work, we propose to pretrain the action module with motion priors before cross-modal VLA alignment. Specifically, we introduce a two-stage training framework that equips the action module with cross-embodiment temporal motion structure before VLA training begins. In Stage~1, a lightweight flow-matching-based encoder-decoder action module efficiently learns temporal motion structure solely from unconditioned action trajectories, without processing visual or language tokens. In Stage~2, this learned prior is transferred to VLA training through decoder reuse and early-stage latent distillation, aligning visual-language features with the action embedding space while still allowing end-to-end policy refinement. In addition, the trained encoder serves as a compact history compressor, summarizing state-action histories into a single temporal context token for history-aware modeling at negligible cost. Extensive experiments across 13 diverse cross-embodiment tasks on both simulated and real-world platforms validate the effectiveness of our approach. Compared with VLA training without action priors, our model achieves faster convergence, higher success rates, and substantially stronger performance on data-scarce real-world tasks. Moreover, scaling up the action data in Stage~1 yields a more generalizable action prior that directly improves downstream VLA performance.
匹配关键词: manipulation
---

[ACADEMIC - ARXIV]
标题: ForceBand: Learning Forceful Manipulation with sEMG
作者: Botao He, Zhi Wang, Linna Kuang, Ishaan Ghosh, Jitendra Malik, Cornelia Fermuller, Tingfan Wu, Jiayuan Mao, Ruoshi Liu, Haozhi Qi, Yiannis Aloimonos
链接: https://arxiv.org/abs/2606.26093v1
完整摘要: Human demonstrations are a scalable data source for learning robot manipulation policies. However, common sources of human demonstration data, such as motion-capture trajectories and internet videos, capture mostly motion and appearance while missing the contact forces that are critical for force-sensitive manipulation. In this paper, we introduce ForceBand, a low-cost wrist-worn sEMG system that turns human muscle activity into force-enriched demonstrations. We first collect a 10-hour multimodal dataset containing egocentric video, sEMG, IMU, and fingertip force measurements across diverse actions and objects. Using this dataset, we pre-train an EMG2Force model that predicts per-finger forces from sEMG and IMU signals. After a short user-specific calibration, users can collect target-task demonstrations using only ForceBand and video; EMG2Force then labels these demonstrations with per-finger force traces, producing force-augmented demonstrations for robot policy learning. Experiments show that ForceBand recovers fine-grained fingertip interactions with over 50% lower force prediction error than vision-based baselines and achieves an 87% success rate on pick, squeeze, and place tasks that require object-specific force control across objects with diverse shapes, sizes, and weights. Project website: https://forceband-emg.github.io
匹配关键词: manipulation
---

[ACADEMIC - ARXIV]
标题: TryOnCrafter: Unleashing Camera Trajectories for Realistic Video Virtual Try-on via a Renderable 4D Try-on Proxy
作者: Hao Sun, Hao Yan, Mengting Chen, Quanjian Song, Yu Li, Juan Cao, Jinsong Lan, Xiaoyong Zhu, Bo Zheng, Sheng Tang
链接: https://arxiv.org/abs/2606.26092v1
完整摘要: While Video Virtual Try-on (VVT) has achieved remarkable progress in synthesizing realistic garment overlays on dynamic subjects, existing paradigms remains fundamentally constrained by a passive dependency on source camera trajectories, failing to accommodate the requisite interactive freedom for omnidirectional viewpoint exploration. To address this limitation, we define a pioneering research frontier: Camera-controllable Video Virtual Try-on (CaM-VVT). Unlike conventional VVT, CaM-VVT not only necessitates viewpoint-agnostic texture hallucination but also strict structural synchronization between non-rigid human dynamics and background contexts under arbitrary, unconstrained camera movements. To tackle these challenges, we present TryOnCrafter, the first unified DiT-based framework specifically architected for the CaM-VVT task. Departing from implicit pixel-space manipulation, we introduce a Renderable 4D Try-on Proxy that explicitly decouples the human subject from the environment. This is achieved by distilling high-fidelity 2D try-on priors into a clothed 3DGS-based avatar, which is subsequently animated via SMPL-X sequences and metric-aligned into a reconstructed background point cloud. This proxy establishes a robust structural foundation with superior texture density and motion integrity. Our Proxy-Anchored Video DiT leverages this robust structural foundation as a primary geometric anchor, ensuring that the synthesized photorealistic videos are strictly constrained by prescribed trajectories and physically plausible deformations. Benefiting from the inherent editability of the 4D proxy, TryOnCrafter facilitates diverse downstream applications, including human relocalization, ``bullet time'' effects, and $360$-degree orbital viewing.
匹配关键词: manipulation
---

[ACADEMIC - ARXIV]
标题: Detect, Unlearn, Restore: Defending Text Summarization Models Against Data Poisoning
作者: Poojitha Thota, Shirin Nilizadeh
链接: https://arxiv.org/abs/2606.26036v1
完整摘要: Training-time data poisoning during fine-tuning poses a significant threat to large language models (LLMs) deployed for abstractive text summarization, where small task-specific datasets exert disproportionate influence on model behavior. In this setting, adversaries manipulate fine-tuning data to induce persistent summarization failures, such as biased or harmful summaries, while preserving standard evaluation metrics. We present a unified post-hoc defense framework for detecting and remediating fine-tuning-stage poisoning in summarization models across the machine learning supply chain. Our experiments show that in white-box settings, poisoned document-summary pairs exhibit abnormally high training influence, enabling detection via influence-function analysis with semantic consistency checks. In black-box settings, poisoned models display two to three times greater sensitivity to semantics-preserving perturbations, enabling behavioral auditing without training data access. Beyond existing poisoning formulations, we introduce novel attacks targeting factual distortion and representational bias, showing that poisoning alters summarization behavior without triggering conventional alarms. Across nine architectures and six benchmark datasets under adaptive attacks, our defenses achieve 85-92% detection precision, while gradient-ascent unlearning restores up to 96% of original behavior with minimal utility loss (less than 0.6% ROUGE degradation). These results indicate that fine-tuning-time poisoning leaves persistent structural artifacts, enabling practical detection and post-deployment recovery without full retraining.
匹配关键词: manipulation
---

[ACADEMIC - ARXIV]
标题: Can Trustless Agents Be Trusted? An Empirical Study of the ERC-8004 Decentralized AI Agent Ecosystem
作者: Xihan Xiong, Zelin Li, Wei Wei, Qin Wang, William Knottenbelt, Zhipeng Wang
链接: https://arxiv.org/abs/2606.26028v1
完整摘要: As autonomous AI agents increasingly transact across organizational boundaries, a fundamental trust challenge emerges: how can an agent assess whether an unknown counterpart is trustworthy? The ERC-8004 protocol addresses this challenge with the first permissionless trust layer for AI agent economies, built around three on-chain registries for Identity, Reputation, and Validation. Despite its rapid adoption, the protocol has not been studied empirically, leaving it unclear whether the information it records provides a trustworthy basis for decision-making. To address this gap, we present the first empirical study of ERC-8004 across three chains: Ethereum, BNB Smart Chain (BSC), and Base, covering the period from protocol deployment through May 13, 2026. We crawl on-chain Identity and Reputation events, off-chain files, and x402 payment transactions. On the identity side, we find that most registrations are placeholders rather than active agents, with only a small fraction (3%, 4%, and 15% across Ethereum, BSC, and Base) exposing a valid ERC-8004 registration file with at least one live service endpoint. On the reputation side, we show that the Registry, as currently deployed, cannot function as a trust signal: values are not commensurable, feedback records are rarely grounded in verifiable interactions, and reputation can be manipulated at minimal cost. Consistent with these design weaknesses, we find that a substantial fraction of reviewers (73.6%, 59.2%, and 90.6% across Ethereum, BSC, and Base) exhibit coordinated Sybil behavior. After removing Sybil-flagged feedback, 15.5%, 72.3%, and 89.4% of rated agents, respectively, are left with no valid feedback. We then turn these findings into concrete recommendations for future revisions of ERC-8004. Our study yields actionable protocol-design implications and establishes an empirical baseline for research on AI agent markets.
匹配关键词: manipulation
---

[ACADEMIC - ARXIV]
标题: Hybrid deep learning-based phase diversity method for wavefront reconstruction
作者: Y. Rodimkov, A. Kotov, K. Burdonov, S. Perevalov, V. Volokitin, I. Meyerov, A. Soloviev
链接: https://arxiv.org/abs/2606.25855v1
完整摘要: The efficiency of high-power laser systems is limited by wavefront distortions in the beam, particularly non-common path aberrations, which reduce the peak intensity at the focal plane. Compensating for these aberrations requires the calibration of the adaptive optics system. Conventional calibration methods rely on a time-consuming iterative optimization that is highly sensitive to initial conditions. While deep learning-based models offer high speed, they often demonstrate insufficient accuracy. In this work, we present a hybrid wavefront reconstruction method that combines a convolutional neural network to generate an initial estimate of the wavefront distortions, with the L-BFGS (Limited-memory Broyden-Fletcher-Goldfarb-Shanno) algorithm for its subsequent refinement. In numerical simulations, the method achieved an efficiency of $\sim 0.99$ in 80% of the cases for a root-mean-square (RMS) of wavefront distortions ranging from 0 to $1.3λ$. In a physical experiment, for initial wavefront distortions with RMS values from 0.15 to $0.6λ$, the method achieved an efficiency of $\sim 0.75$. As a result, focusing with a Strehl ratio of $0.96 \pm 0.02$ was attained within 2 to 4 iterations of the algorithm, confirming the applicability of the method for the fast and accurate calibration of adaptive optics systems under real experimental conditions.
匹配关键词: sim-to-real
---

[ACADEMIC - ARXIV]
标题: StairMaster: Learning to Conquer Risky Hollow Stairs for Agile Quadrupedal Robots
作者: Xincheng Tang, Youhan Xie, Zhengjie Shu, Wanyu Li, Lai Jiang, Wenkang Hu, Yitong Li, Ruigang Yang
链接: https://arxiv.org/abs/2606.25765v1
完整摘要: Climbing hollow stairs remains a challenging problem for quadruped robots due to the high risk of leg trapping, severe depth sparsity, and high-frequency depth-sensing noise. In this paper, we propose StairMaster, a novel three-stage reinforcement learning framework for stable locomotion on such extreme discontinuous terrains. Our architecture integrates a Cross-Attention mechanism to extract structural features from noisy depth data, alongside a Spatial-aware Recurrent Unit (SRU) that maintains robust spatio-temporal memory to mitigate perception blind spots. To bridge the sim-to-real gap in depth perception, we propose a high-fidelity sim-to-real depth sensor modeling pipeline that faithfully replicates real-world sensor artifacts. Additionally, we employ a 3D waypoint-guided active perception reward for proactive sensing, alongside hollow gap kinematic and stair edge penalties to ensure precise foothold placement. We successfully deployed StairMaster on a Unitree Go2 robot, demonstrating its ability to conquer hollow stairs with an unprecedented incline of up to 55$^\circ$ through zero-shot transfer. To the best of our knowledge, this is the first RL-based policy to achieve such steep hollow stair climbing in real-world environments. Project Website: https://sivan666666.github.io/StairMaster/.
匹配关键词: sim-to-real
---

[ACADEMIC - ARXIV]
标题: GROVE: Grounded Pedestrian Simulation via Natural Language for Interactive Social Robot Navigation
作者: Duc Tai Nguyen, Volodymyr Shcherbyna, Anh Do Duc, Zhengcheng Shen, Teham Buiyan, Linh Kästner
链接: https://arxiv.org/abs/2606.25504v1
完整摘要: Pedestrian simulation is a critical component for training and deploying social robot navigation approaches, yet it remains a largely rigid system that repeatedly requires manual data generation to define even simple scenarios. We propose GROVE, a text-to-scenario pedestrian simulation framework that combines state-of-the-art approaches to produce realistic, socially challenging scenarios for social robot navigation. Our framework allows users to customize one of several common presets (emergency, queuing, normal) or even enter a fully independent prompt to generate a highly customizable pedestrian simulation. Multiple modules separately ensure the realism and soundness of long-horizon human behavior, medium-horizon pedestrian navigation, and short-horizon robot/social interactions. Each module is tuned by the prompt in a way that reflects the user intent across all aspects of pedestrian simulation. By dynamically selecting one of several state-of-the-art (SotA) approaches in our modules based on the scenario, we capture many situational nuances of pedestrian behavior in order to narrow the simulation-to-real (sim2real) gap. The human simulation is directly integrated into Isaac Sim, Gazebo, and RViz simulators for robot deployment in highly social environments. We validate our approach through qualitative comparison against existing pedestrian simulation baselines across scenarios of varying complexity in residential, hospital, and office environments. The result is a high-fidelity pedestrian simulation that challenges social robot navigation with complex, diverse, realistic human behaviors.
匹配关键词: sim-to-real
---

[ACADEMIC - ARXIV]
标题: Cross-View Variance Correlation in Path-Traced Stereo:A Hidden Shortcut in Synthetic Training Data
作者: Po-Ting Lin
链接: https://arxiv.org/abs/2606.25483v1
完整摘要: Path-traced synthetic stereo data underlie a large fraction of modern disparity-estimation training pipelines. We report a previously unrecognised property of such data: while the Monte Carlo (MC) noise streams of the two cameras are statistically independent, the underlying \emph{variance fields} -- deterministic per-pixel functions of the rendering integrand -- are highly correlated once aligned by the ground-truth disparity warp. Across 20 scenes rendered with Mitsuba~3, the warped Pearson correlation reaches $ρ{=}0.754{\pm}0.016$ across 20 scenes at $\mathrm{SPP}{=}512$, and on a representative scene remains essentially invariant ($ρ{=}0.778{\pm}0.001$) over a $16\times$ range of samples per pixel. The effect is strongest in Lambertian regions ($ρ{\approx}0.78$) and substantially weaker in glass ($ρ{\approx}0.30$), as predicted by an integrand decomposition into view-independent and view-dependent components. A residual-shuffle intervention that breaks the cross-view alignment while preserving the clean image degrades the GT cost margin by $33\%$ on non-glass and the variance-based winner-take-all accuracy on glass by $4.3\times$, confirming the structure functions as a matching cue. This signal is unique to MC-rendered data and constitutes a candidate sim-to-real shortcut whose impact on trained networks remains to be quantified.
匹配关键词: sim-to-real
---

[ACADEMIC - ARXIV]
标题: Learning Action Priors for Cross-embodiment Robot Manipulation
作者: Dong Jing, Tianqi Zhang, Jiaqi Liu, Jinman Zhao, Zelong Sun, Li Erran Li, Zhiwu Lu, Mingyu Ding
链接: https://arxiv.org/abs/2606.26095v1
完整摘要: Most Vision-Language-Action (VLA) models build on a Vision-Language Model (VLM) backbone by attaching an action module and optimizing the full policy jointly. This design inherits strong visual and linguistic priors from the VLM, but leaves the action module to learn physical motion almost from scratch. As a result, the policy lacks an explicit motion prior, forcing early optimization to simultaneously discover temporal action dynamics and cross-modal alignment, a challenge further amplified in cross-embodiment settings. In this work, we propose to pretrain the action module with motion priors before cross-modal VLA alignment. Specifically, we introduce a two-stage training framework that equips the action module with cross-embodiment temporal motion structure before VLA training begins. In Stage~1, a lightweight flow-matching-based encoder-decoder action module efficiently learns temporal motion structure solely from unconditioned action trajectories, without processing visual or language tokens. In Stage~2, this learned prior is transferred to VLA training through decoder reuse and early-stage latent distillation, aligning visual-language features with the action embedding space while still allowing end-to-end policy refinement. In addition, the trained encoder serves as a compact history compressor, summarizing state-action histories into a single temporal context token for history-aware modeling at negligible cost. Extensive experiments across 13 diverse cross-embodiment tasks on both simulated and real-world platforms validate the effectiveness of our approach. Compared with VLA training without action priors, our model achieves faster convergence, higher success rates, and substantially stronger performance on data-scarce real-world tasks. Moreover, scaling up the action data in Stage~1 yields a more generalizable action prior that directly improves downstream VLA performance.
匹配关键词: world model
---

[ACADEMIC - ARXIV]
标题: RevengeBench: Reverse Engineering Code-Space Policies from Behavioral Experiments
作者: Babak Rahmani, Sebastian Dziadzio, Joschka Strüber, Sergio Hernández-Gutiérrez, Matthias Bethge
链接: https://arxiv.org/abs/2606.26094v1
完整摘要: For most of scientific history, researchers studying behavior could only infer hidden mechanisms from outward actions: an inverse problem that becomes more tractable when observation is augmented by targeted intervention. We pose a computational analogue: given only behavioral traces of an agent in a game environment, can a learner reconstruct the underlying decision program as executable code, and how much does this reconstruction improve with the ability to design controlled experiments? We introduce RevengeBench, a benchmark of 75 LLM generated, Elo-calibrated policies across five game environments, drawn from CodeClash tournament trajectories. The learner observes the hidden target policy play against sampled opponents and designs behavioral probes in the form of custom opponent policies that elicit informative behavior. It then submits an executable hypothesis, which is evaluated using continuous action-distance metrics. We further validate that recovered code carries informative signal in downstream player-versus-player tournaments. Across twelve frontier LLMs, recovery quality varies substantially (34 to 72% of initial distance closed), with reconstructed policies yielding measurable competitive advantage, particularly for weaker models that otherwise struggle to design effective counter-strategies. Our benchmark positions behavioral recovery of programmatic policies as a tractable inverse problem in code-space, opening a path to opponent modeling, policy interpretability, and the broader question of inferring latent mechanisms from observations.
匹配关键词: world model
---

[ACADEMIC - ARXIV]
标题: ForceBand: Learning Forceful Manipulation with sEMG
作者: Botao He, Zhi Wang, Linna Kuang, Ishaan Ghosh, Jitendra Malik, Cornelia Fermuller, Tingfan Wu, Jiayuan Mao, Ruoshi Liu, Haozhi Qi, Yiannis Aloimonos
链接: https://arxiv.org/abs/2606.26093v1
完整摘要: Human demonstrations are a scalable data source for learning robot manipulation policies. However, common sources of human demonstration data, such as motion-capture trajectories and internet videos, capture mostly motion and appearance while missing the contact forces that are critical for force-sensitive manipulation. In this paper, we introduce ForceBand, a low-cost wrist-worn sEMG system that turns human muscle activity into force-enriched demonstrations. We first collect a 10-hour multimodal dataset containing egocentric video, sEMG, IMU, and fingertip force measurements across diverse actions and objects. Using this dataset, we pre-train an EMG2Force model that predicts per-finger forces from sEMG and IMU signals. After a short user-specific calibration, users can collect target-task demonstrations using only ForceBand and video; EMG2Force then labels these demonstrations with per-finger force traces, producing force-augmented demonstrations for robot policy learning. Experiments show that ForceBand recovers fine-grained fingertip interactions with over 50% lower force prediction error than vision-based baselines and achieves an 87% success rate on pick, squeeze, and place tasks that require object-specific force control across objects with diverse shapes, sizes, and weights. Project website: https://forceband-emg.github.io
匹配关键词: world model
---

[ACADEMIC - ARXIV]
标题: On-Policy Self-Distillation with Sampled Demonstrations Reduces Output Diversity
作者: Andrei Liviu Nicolicioiu, Mohammad Pezeshki, Aaron Courville
链接: https://arxiv.org/abs/2606.26091v1
完整摘要: On-policy self-distillation achieves strong pass@1 accuracy by using a single model as both teacher and student, with the teacher conditioned on a correct demonstration to provide dense token-level feedback. We show that this could come at a hidden cost: rollout diversity decreases and pass@k curves flatten (i.e., generating more rollouts fails to improve accuracy). We trace this to compounding biases in the design of self-distillation with sampled demonstrations. The teacher scores each student rollout while conditioned on a sampled correct rollout, channeling its feedback through the model's own biases. We theoretically analyze the optimal self-distillation policy and show that it tilts the base distribution by a pointwise conditional mutual information score between the student's rollout and the correct rollout used as context. Unlike the ideal optimal on-policy reinforcement learning (RL), which preserves probability ratios among equally correct rollouts, self-distillation can amplify existing probability gaps, concentrating mass on already-dominant modes. On a controlled graph path-finding task and science question-answering benchmarks, self-distilled models match or exceed RL on average performance but exhibit substantially lower functional and semantic diversity, failing on out-of-distribution settings that require diverse strategies.
匹配关键词: world model
---

[ACADEMIC - ARXIV]
标题: MVTrack4Gen: Multi-View Point Tracking as Geometric Supervision for 4D Video Generation
作者: JoungBin Lee, Jaewoo Jung, Jongmin Lee, Tongmin Kim, Hyunsung Kim, Takuya Narihira, Kazumi Fukuda, Jahyeok Koo, Jisang Han, Yuki Mitsufuji, Seungryong Kim
链接: https://arxiv.org/abs/2606.26087v1
完整摘要: Synthesizing a novel-view video from a monocular reference video along a target camera trajectory requires both geometric consistency and motion fidelity with respect to the reference video. Existing methods based on explicit 3D representations are limited by the accuracy of off-the-shelf reconstruction modules, which often produce inaccurate geometry for dynamic objects in monocular videos. In contrast, camera-conditioning-only methods can achieve high visual quality but often struggle to preserve geometric and motion consistency. In this work, we introduce MVTrack4Gen (Multi-View point Tracking for Novel-View Generation), a motion-aware training framework that leverages multi-view point tracking as an additional geometric and motion supervision signal for camera-conditioning-only novel-view video diffusion models. Our key finding is that specific attention layers encode strong correspondence cues, where query features attend to key features at geometrically corresponding locations across views and over time, and the misalignment of these correspondences causes motion inconsistency. Based on this observation, we route these features into an auxiliary multi-view tracking head and jointly train the diffusion model with a point-tracking objective. By explicitly strengthening these motion-aware correspondences, MVTrack4Gen improves existing models to better follow the motion in the reference view and maintain cross-view geometric consistency. Across diverse benchmarks, our method achieves state-of-the-art geometric consistency and competitive camera accuracy.
匹配关键词: world model
---

[ACADEMIC - ARXIV]
标题: Real-Time Voice AI Hears but Does Not Listen
作者: Martijn Bartelds, Federico Bianchi, James Zou
链接: https://arxiv.org/abs/2606.26083v1
完整摘要: Speech conveys information through both words and vocal delivery. We evaluate four leading production realtime voice systems-OpenAI's GPT Realtime 2, Google's Gemini 3.1 Flash Live, and Alibaba's Qwen3.5 Omni Plus and Omni Flash-on tasks where the words and the delivery patterns both convey meaningful information. Across three consequential scenarios, all four systems act on the words rather than the voice. They end calls with crying callers who insist nothing is wrong, approve wire transfers authorized in frightened voices, and enroll callers whose agreement is clearly sarcastic. Surprisingly, this is often not a failure of perception. When asked directly, three of the four systems reliably identify the distress, fear, or sarcasm they later ignore when making decisions. We observe a similar pattern when these realtime voice systems estimate accent and age, as their responses frequently follow the biases of the words rather than the acoustic properties of the speaker. We term this disconnect between perception and action the emotional intelligence gap of voice AI. Prompting systems to explicitly attend to vocal delivery improves performance only partially and inconsistently. Our findings show that current realtime voice AI systems often behave as if speech had been reduced to a transcript, suggesting that they should be used with caution in settings where the tone and emotion of delivery convey important information.
匹配关键词: speech synthesis
---

[ACADEMIC - ARXIV]
标题: MIMFlow: Integrating Masked Image Modeling with Normalizing Flows for End-to-End Image Generation
作者: Yang Chen, Xiaowei Xu, Shuai Wang, Xinwen Zhang, Qiushi Guo, Tiezheng Ge, Limin Wang
链接: https://arxiv.org/abs/2606.26016v1
完整摘要: Normalizing Flows (NFs) are powerful generative models capable of exact density estimation and sampling. However, their strict invertibility often forces the model to exhaust its capacity on low-level pixel details, hindering the capture of high-level semantic structures. While Masked Image Modeling (MIM) has excelled in representation learning, its integration into generative pipelines has remained largely modular and disjointed. In this paper, we propose MIMFlow, a unified end-to-end framework that jointly optimizes latent semantics, pixel reconstruction, and generative flow. By employing a VAE encoder to infer semantic latent from masked images, MIMFlow achieves a principled decoupling of the generative task: the Normalizing Flow focuses on modeling a simplified, low-frequency semantic manifold, while a specialized decoder handles high-frequency synthesis. This design effectively resolves the inherent capacity bottleneck of NFs, allowing the model to prioritize global structural coherence over redundant noise. Empirical results on ImageNet 256$\times$256 show that MIMFlow-L reaches 71.3\% linear probing accuracy and an FID of 2.50. Despite using only 128 tokens (50\% fewer than standard models), it yields a 32.8\% performance gain over similar-scale NF baselines. Our code is available at https://github.com/MCG-NJU/MIMFlow.
匹配关键词: speech synthesis
---

[ACADEMIC - ARXIV]
标题: Dziri Voicebot: An End-to-End Low-Resource Speech-to-Speech Conversational System for Algerian Dialect
作者: Dihia Lanasri, Fairouz Taki, Asma Kemmoum
链接: https://arxiv.org/abs/2606.26003v1
完整摘要: Automatic speech and language technologies are still heavily biased toward high-resource languages, limiting their applicability to dialectal and low-resource settings such as Algerian Dialect. This language presents additional challenges including lack of standardized orthography, frequent codeswitching with French, and scarcity of annotated speech resources. This paper addresses the problem of building a complete speech-to-speech conversational system for Algerian Dialect. We propose a modular pipeline integrating automatic speech recognition, natural language understanding, retrieval-augmented generation, and text-to-speech synthesis within a unified architecture. This work is the continuation of our previous work on Algerian dialectal conversational systems Bechiri and Lanasri [2026], extending it from text-based dialogue modeling to full speech-based interaction. We constructed dedicated datasets for ASR, NLU, and TTS in the telecom domain and fine-tune pretrained models for each component. The ASR system is built on Whisper-based adaptation, while the NLU module combines transformer-based embeddings with a task-oriented dialogue framework. A neural TTS system is trained on a newly collected dialectal corpus to enable spoken response generation. Experimental results show strong performance across all components, including low word error rate for ASR, high intent classification and entity recognition scores for NLU, and stable speech synthesis quality. The proposed system provides a reproducible baseline for end-to-end conversational modeling in Algerian Dialect.
匹配关键词: speech synthesis
---

[ACADEMIC - ARXIV]
标题: SpeechEQ: Benchmarking Emotional Intelligence Quotient in Socially Aware Voice Conversational Models
作者: Liang-Yuan Wu, Zih-Ching Chen, Tongshuang Wu, Chao-Han Huck Yang, Hua Shen
链接: https://arxiv.org/abs/2606.25990v1
完整摘要: As multimodal conversational systems increasingly engage in spoken interaction, their ability to navigate paralinguistic social cues has become a critical bottleneck for natural human-AI communication. However, existing evaluations of machine emotional intelligence assess reasoning exclusively through isolated text or passive acoustic perception, overlooking the complex cross-modal reasoning required for active, multi-turn dialogue. We introduce \textsc{SpeechEQ}, a comprehensive framework designed to evaluate the sociolinguistic reasoning of Speech-Language Models (SLMs). The framework includes a validated dataset of 2,265 dialogues across 15 Emotional Quotient (EQ) subscales grounded in EQ-i 2.0 theory, along with a multi-turn evaluation protocol measured by our proposed Spoken EQ (SEQ) score inspired by human EQ assessments. Experiments show limitations in how both existing Speech Emotion Recognition and end-to-end Speech-Language Models understand and apply paralinguistic cues through speech. While end-to-end architectures outperform cascaded systems, \textsc{SpeechEQ} reveals that current multimodal models remain bottlenecked by a text-reliant ``modality shortcut,'' an alignment-induced ``safety trap,'' and ``contextual amnesia,'' highlighting the barriers to truly emotionally aware AI. Our benchmark can be accessed at https://huggingface.co/datasets/SpeechEQ/SpeechEQ and demo page at https://binomial14.github.io/speecheq-demo/
匹配关键词: speech synthesis
---

[ACADEMIC - ARXIV]
标题: SE-AGCNet: An End-to-End Framework for Joint Speech Enhancement and Loudness Control in Meeting Scenarios
作者: Jinming Zhang, Wei Rao, Xionghu Zhong, Eng Siong Chng
链接: https://arxiv.org/abs/2606.25959v1
完整摘要: Conventional audio pipelines typically treat speech enhancement (SE) and automatic gain control (AGC) as discrete modules, which often limits overall performance. For instance, applying AGC before SE may inadvertently amplify background noise, while prioritizing SE tends to over-suppress low-volume speech. To address these limitations, we propose SE-AGCNet, an end-to-end framework that jointly optimizes SE and AGC. Tailored for meeting scenarios with significant volume variations, SE-AGCNet leverages the synergy between the two tasks: SE preserves quiet speech, thereby facilitating effective volume adjustment by the AGC component. Furthermore, we propose a specialized data simulation pipeline, SE-AGC-DataGen, and incorporate standardized loudness evaluation metrics: integrated loudness (LUFS), short-term loudness (St LUFS), and LRA. Experiments show that SE-AGCNet consistently achieves target loudness while improving speech quality and ASR accuracy over competitive baselines.
匹配关键词: speech synthesis
---

[ACADEMIC - ARXIV]
标题: Dziri Voicebot: An End-to-End Low-Resource Speech-to-Speech Conversational System for Algerian Dialect
作者: Dihia Lanasri, Fairouz Taki, Asma Kemmoum
链接: https://arxiv.org/abs/2606.26003v1
完整摘要: Automatic speech and language technologies are still heavily biased toward high-resource languages, limiting their applicability to dialectal and low-resource settings such as Algerian Dialect. This language presents additional challenges including lack of standardized orthography, frequent codeswitching with French, and scarcity of annotated speech resources. This paper addresses the problem of building a complete speech-to-speech conversational system for Algerian Dialect. We propose a modular pipeline integrating automatic speech recognition, natural language understanding, retrieval-augmented generation, and text-to-speech synthesis within a unified architecture. This work is the continuation of our previous work on Algerian dialectal conversational systems Bechiri and Lanasri [2026], extending it from text-based dialogue modeling to full speech-based interaction. We constructed dedicated datasets for ASR, NLU, and TTS in the telecom domain and fine-tune pretrained models for each component. The ASR system is built on Whisper-based adaptation, while the NLU module combines transformer-based embeddings with a task-oriented dialogue framework. A neural TTS system is trained on a newly collected dialectal corpus to enable spoken response generation. Experimental results show strong performance across all components, including low word error rate for ASR, high intent classification and entity recognition scores for NLU, and stable speech synthesis quality. The proposed system provides a reproducible baseline for end-to-end conversational modeling in Algerian Dialect.
匹配关键词: TTS
---

[ACADEMIC - ARXIV]
标题: Joint Residual Reweighting for Classifier Free Guidance in Flow-Matching Zero-Shot TTS
作者: Runwu Shi, Yujin Wang, Hongjin Song, Chunxiang Jin
链接: https://arxiv.org/abs/2606.25672v1
完整摘要: Classifier-free guidance (CFG) is widely used in flow-matching-based zero-shot text-to-speech (TTS), where generation is typically controlled by two conditions: the target text and a prompt speech signal. Standard CFG strengthens these conditions jointly, while recent branch-selective guidance methods attempt to enhance text or speaker conditioning separately, often leading to a trade-off between text correctness and speaker similarity. In this paper, we revisit the CFG under independently masked text and speech-prompt conditions, and decompose the guidance field into text, speaker, and joint residuals. We show that conventional speaker-selective guidance entangles the speaker residual with the joint residual, which may disturb text-related generation. Based on this observation, we propose joint residual reweighting, which independently controls the speaker and joint residuals within the standard CFG framework. Experiments on F5-TTS and CosyVoice2 show that the proposed method improves speaker similarity while maintaining competitive text correctness, demonstrating the usefulness of the joint residual for balancing speaker fidelity and text accuracy in zero-shot TTS.
匹配关键词: TTS
---

[ACADEMIC - ARXIV]
标题: Adaptive Oscillatory Inductive Bias for Modeling Sharp Prosodic Dynamics in Diffusion-Based TTS
作者: Sandipan Dhar, Nirmesh J. Shah, Ashishkumar P. Gudmalwar, Pankaj Wasnik
链接: https://arxiv.org/abs/2606.25424v1
完整摘要: Diffusion-based text-to-speech (TTS) models have achieved significant improvements in speech quality. However, modeling sharp prosodic transitions and rapid pitch variations in expressive speech remains challenging. Existing diffusion-based TTS decoders commonly utilize periodic nonlinearities such as Snake activation function to capture harmonic structures, but this activation funcation provides limited adaptability when modeling abrupt amplitude and frequency variations. In this paper, we investigate the role of oscillatory inductive bias in diffusion-based TTS decoders and introduce an adaptive oscillatory nonlinearity that enables controllable periodic modulation while maintaining signal stability through a linear bypass component. We refer the resulting TTS system as OscillaTTS. Experiments on the LJSpeech and Emotional Speech Dataset show consistent improvements across objective and subjective evaluations, indicating improved modeling of expressive prosodic dynamics.
匹配关键词: TTS
---

[ACADEMIC - ARXIV]
标题: CrossAccent-TTS: Cross-Lingual Accent-Intensity Controllable Text-to-Speech via Disentangled Speaker and Accent Representations
作者: Ram Annamdevula, Ankit Tatawat, Ashishkumar P. Gudmalwar, Nirmesh J. Shah, Pankaj Wasnik
链接: https://arxiv.org/abs/2606.25403v1
完整摘要: Accent conversion and controllability remain fundamental challenges in cross-lingual text-to-speech (TTS), particularly for low-resource and phonetically diverse Indic languages. While recent large language model (LLM)-based TTS systems exhibit strong cross-lingual generalization, they provide limited explicit control over accent characteristics and intensity. In this paper, we propose CrossAccentTTS, a framework that enables both accent control and conversion while preserving speaker identity. Specifically, we introduce an Accent Intensity Controller (AIC) that injects weighted language embeddings into the accent subspace, allowing smooth interpolation between accents and fine-grained modulation of accent strength at inference time. Experiments on the Indic Multilingual and L2-arctic datasets shows that CrossAccent-TTS achieves precise control of accent intensity, outperforming strong baselines in accent similarity and controllability by maintaining speaker similarity and naturalness.
匹配关键词: TTS
---

[ACADEMIC - ARXIV]
标题: Sarashina2.2-TTS: Tackling Kanji Polyphony in Japanese Speech Generation via Data Scaling and Targeted Data Synthesis
作者: Lianbo Liu, Shiao Zhu, Kai Washizaki, Reo Yoneyama, Haesung Jeon, Mengjie Zhao, Yusuke Fujita, Hao Shi, Nao Yoshida, Yuan Gao, Roman Koshkin, Yukiya Hono, Yui Sudo
链接: https://arxiv.org/abs/2606.25369v1
完整摘要: While large language model (LLM)-based text-to-speech (TTS) systems have achieved high-quality speech synthesis, most existing systems focus on English and Chinese. Japanese, however, remains under-explored, and its unique linguistic challenges, such as widespread context-dependent kanji polyphony, have yet to be adequately tackled. Here we introduce Sarashina2.2-TTS (https://github.com/sbintuitions/sarashina2.2-tts), a Japanese-centric LLM-TTS system that tackles these challenges through a dual approach: data strategy and evaluation methodology. First, we scale training to approximately 361k hours of speech, incorporating a balanced mix of Japanese and English data. Furthermore, we design a targeted data augmentation pipeline covering all 2,136 Joyo (regular-use) kanji designated by Japan's Agency for Cultural Affairs to efficiently address kanji polyphony disambiguation. Second, we introduce the Joyo Kanji Yomi Benchmark (https://github.com/sbintuitions/JoyoKanji-Yomi-Benchmark), covering all 2,136 Joyo kanji and their 4,378 readings. Alongside this benchmark, we propose Kana-CER, a metric that compares synthesized speech against reference readings in the kana space, eliminating orthographic variations to directly measure pronunciation correctness. Experiments demonstrate that our targeted data augmentation significantly improves reading accuracy. Overall, Sarashina2.2-TTS achieves state-of-the-art kanji-level reading accuracy and matches top baselines on general sentence-level pronunciation, while delivering the highest speaker similarity in zero-shot Japanese speech synthesis. Furthermore, cross-lingual evaluation reveals that Sarashina2.2-TTS is the only system that maintains stable Japanese pronunciation regardless of the prompt language, confirming that our balanced training approach improves cross-lingual robustness.
匹配关键词: TTS
---

[ACADEMIC - ARXIV]
标题: Dziri Voicebot: An End-to-End Low-Resource Speech-to-Speech Conversational System for Algerian Dialect
作者: Dihia Lanasri, Fairouz Taki, Asma Kemmoum
链接: https://arxiv.org/abs/2606.26003v1
完整摘要: Automatic speech and language technologies are still heavily biased toward high-resource languages, limiting their applicability to dialectal and low-resource settings such as Algerian Dialect. This language presents additional challenges including lack of standardized orthography, frequent codeswitching with French, and scarcity of annotated speech resources. This paper addresses the problem of building a complete speech-to-speech conversational system for Algerian Dialect. We propose a modular pipeline integrating automatic speech recognition, natural language understanding, retrieval-augmented generation, and text-to-speech synthesis within a unified architecture. This work is the continuation of our previous work on Algerian dialectal conversational systems Bechiri and Lanasri [2026], extending it from text-based dialogue modeling to full speech-based interaction. We constructed dedicated datasets for ASR, NLU, and TTS in the telecom domain and fine-tune pretrained models for each component. The ASR system is built on Whisper-based adaptation, while the NLU module combines transformer-based embeddings with a task-oriented dialogue framework. A neural TTS system is trained on a newly collected dialectal corpus to enable spoken response generation. Experimental results show strong performance across all components, including low word error rate for ASR, high intent classification and entity recognition scores for NLU, and stable speech synthesis quality. The proposed system provides a reproducible baseline for end-to-end conversational modeling in Algerian Dialect.
匹配关键词: ASR
---

[ACADEMIC - ARXIV]
标题: SE-AGCNet: An End-to-End Framework for Joint Speech Enhancement and Loudness Control in Meeting Scenarios
作者: Jinming Zhang, Wei Rao, Xionghu Zhong, Eng Siong Chng
链接: https://arxiv.org/abs/2606.25959v1
完整摘要: Conventional audio pipelines typically treat speech enhancement (SE) and automatic gain control (AGC) as discrete modules, which often limits overall performance. For instance, applying AGC before SE may inadvertently amplify background noise, while prioritizing SE tends to over-suppress low-volume speech. To address these limitations, we propose SE-AGCNet, an end-to-end framework that jointly optimizes SE and AGC. Tailored for meeting scenarios with significant volume variations, SE-AGCNet leverages the synergy between the two tasks: SE preserves quiet speech, thereby facilitating effective volume adjustment by the AGC component. Furthermore, we propose a specialized data simulation pipeline, SE-AGC-DataGen, and incorporate standardized loudness evaluation metrics: integrated loudness (LUFS), short-term loudness (St LUFS), and LRA. Experiments show that SE-AGCNet consistently achieves target loudness while improving speech quality and ASR accuracy over competitive baselines.
匹配关键词: ASR
---

[ACADEMIC - ARXIV]
标题: VPA-Guard: Defending and Benchmarking Image-to-Video Generation Against Visual Prompt Attacks
作者: Yining Sun, Haoyu Kang, Jiajun Wu, Heng Zhang, Danyang Zhang, Zhenjun Zhao, Haochen Han, Fangming Liu, Wai Kin Victor Chan, Alex Jinpeng Wang
链接: https://arxiv.org/abs/2606.25592v1
完整摘要: Recent advancements in Image-to-Video (I2V) generation have transformed input images from simple appearance references into interactive control interfaces where visual cues such as arrows, sketches, and emojis orchestrate complex video dynamics with unprecedented controllability. However, these seemingly innocuous static cues can be interpreted by models as executable temporal instructions, unfolding into harmful actions in the generated videos. Despite the severity of this threat, existing safety benchmarks remain predominantly focused on text-based and content-only image-based jailbreaks, leaving implicit visual prompt attacks insufficiently explored. To bridge this gap, we present VVA-Bench, the first systematic benchmark for evaluating video generation safety under categorized vision-centric prompt attacks. Extensive experiments on VVA-Bench demonstrate that state-of-the-art models are highly susceptible to such attacks, with Attack Success Rates (ASR) reaching 100.0\% on Wan 2.7 and 74.8\% on Veo 3.1. To mitigate these risks, we propose VPA-Guard, a retrieval-augmented and self-evolving defense framework. By leveraging few-shot reasoning to identify latent malicious intents, our method reduces the attack ASR by 44.2\% and the harmfulness score by 73.4\% on average, while maintaining the model's utility for legitimate user edits. Our work provides both a rigorous benchmark and an effective defense strategy to advance safe and socially responsible multimodal generation.
匹配关键词: ASR
---

[ACADEMIC - ARXIV]
标题: How Reliable Is Your Jailbreak Judge? Calibration and Adversarial Robustness of Automated ASR Scoring
作者: Yang Gao
链接: https://arxiv.org/abs/2606.25487v1
完整摘要: Almost every paper on LLM jailbreaks and prompt injection reports an attack-success rate (ASR), and that number is assigned not by people but by an automated judge: either a safety classifier trained for the task, or a general chat model prompted to grade. The judge is rarely checked. We check it. Using 596 human-labeled completions from the HarmBench classifier validation set, we compare the two judge families against human majority votes and then attack them. The two families fail in opposite ways. The dedicated classifier over-flags (precision 0.835, recall 0.974); three different LLM-as-judges keep high precision (0.81 to 0.94) but show erratic recall (0.06 to 0.65), so the same responses produce very different ASR depending on which judge scores them. The two families also differ sharply in robustness. Wrappers that leave the harmful text untouched and only add benign framing flip every LLM-judge between 57% and 100% of the time, and a single prepended refusal sentence accounts for much of this (39% to 88%). The dedicated classifier resists these surface attacks (at most 6.7%), but a white-box GCG attack on its open weights flips 70% of confident true positives (21 of 30; 95% CI 54 to 86%) even at a small optimization budget. A two-annotator audit confirms the attacks leave the harm intact: every one of 80 sampled flips still contained the harmful content. Because a large and growing share of reported ASR comes from LLM-judges, many such numbers are unreliable both on average and under deliberate pressure. We recommend that papers report judge precision and recall on a human-labeled slice, report ASR corrected for judge precision, and include an adversarial check of the judge. Our code is released.
匹配关键词: ASR
---

[ACADEMIC - ARXIV]
标题: Fully Differentiable Neural Forced Alignment via Soft Dynamic Programming
作者: Rotem Rousso, Eyal Cohen, Joseph Keshet
链接: https://arxiv.org/abs/2606.25460v1
完整摘要: Recent advances in sequence modeling have significantly improved ASR systems, bringing them close to human-level recognition accuracy and enhancing robustness across diverse acoustic conditions and languages. In contrast, Forced Alignment has not experienced comparable progress, and traditional HMM-GMM frameworks remain widely adopted and highly competitive. To address this gap, we propose an end-to-end, fully differentiable neural architecture specifically designed for phoneme alignment. The model consists of an encoder that processes the input signal and a decoder that produces alignment decisions. The encoder is structured into two complementary branches: one dedicated to phoneme identity verification and the other to phoneme boundary detection. The decoder is implemented as a trainable module based on differentiable soft dynamic programming. The entire system is optimized end-to-end using a novel contrastive loss that encourages clear separation between steady-state phoneme regions and transition boundaries. The proposed approach outperforms the current state of the art in phoneme alignment on hand-annotated English benchmarks, achieves strong word-level generalization results, and demonstrates generalization on unseen languages.
匹配关键词: ASR
---

[ACADEMIC - ARXIV]
标题: Learning Action Priors for Cross-embodiment Robot Manipulation
作者: Dong Jing, Tianqi Zhang, Jiaqi Liu, Jinman Zhao, Zelong Sun, Li Erran Li, Zhiwu Lu, Mingyu Ding
链接: https://arxiv.org/abs/2606.26095v1
完整摘要: Most Vision-Language-Action (VLA) models build on a Vision-Language Model (VLM) backbone by attaching an action module and optimizing the full policy jointly. This design inherits strong visual and linguistic priors from the VLM, but leaves the action module to learn physical motion almost from scratch. As a result, the policy lacks an explicit motion prior, forcing early optimization to simultaneously discover temporal action dynamics and cross-modal alignment, a challenge further amplified in cross-embodiment settings. In this work, we propose to pretrain the action module with motion priors before cross-modal VLA alignment. Specifically, we introduce a two-stage training framework that equips the action module with cross-embodiment temporal motion structure before VLA training begins. In Stage~1, a lightweight flow-matching-based encoder-decoder action module efficiently learns temporal motion structure solely from unconditioned action trajectories, without processing visual or language tokens. In Stage~2, this learned prior is transferred to VLA training through decoder reuse and early-stage latent distillation, aligning visual-language features with the action embedding space while still allowing end-to-end policy refinement. In addition, the trained encoder serves as a compact history compressor, summarizing state-action histories into a single temporal context token for history-aware modeling at negligible cost. Extensive experiments across 13 diverse cross-embodiment tasks on both simulated and real-world platforms validate the effectiveness of our approach. Compared with VLA training without action priors, our model achieves faster convergence, higher success rates, and substantially stronger performance on data-scarce real-world tasks. Moreover, scaling up the action data in Stage~1 yields a more generalizable action prior that directly improves downstream VLA performance.
匹配关键词: audio language model
---

[ACADEMIC - ARXIV]
标题: RevengeBench: Reverse Engineering Code-Space Policies from Behavioral Experiments
作者: Babak Rahmani, Sebastian Dziadzio, Joschka Strüber, Sergio Hernández-Gutiérrez, Matthias Bethge
链接: https://arxiv.org/abs/2606.26094v1
完整摘要: For most of scientific history, researchers studying behavior could only infer hidden mechanisms from outward actions: an inverse problem that becomes more tractable when observation is augmented by targeted intervention. We pose a computational analogue: given only behavioral traces of an agent in a game environment, can a learner reconstruct the underlying decision program as executable code, and how much does this reconstruction improve with the ability to design controlled experiments? We introduce RevengeBench, a benchmark of 75 LLM generated, Elo-calibrated policies across five game environments, drawn from CodeClash tournament trajectories. The learner observes the hidden target policy play against sampled opponents and designs behavioral probes in the form of custom opponent policies that elicit informative behavior. It then submits an executable hypothesis, which is evaluated using continuous action-distance metrics. We further validate that recovered code carries informative signal in downstream player-versus-player tournaments. Across twelve frontier LLMs, recovery quality varies substantially (34 to 72% of initial distance closed), with reconstructed policies yielding measurable competitive advantage, particularly for weaker models that otherwise struggle to design effective counter-strategies. Our benchmark positions behavioral recovery of programmatic policies as a tractable inverse problem in code-space, opening a path to opponent modeling, policy interpretability, and the broader question of inferring latent mechanisms from observations.
匹配关键词: audio language model
---

[ACADEMIC - ARXIV]
标题: ForceBand: Learning Forceful Manipulation with sEMG
作者: Botao He, Zhi Wang, Linna Kuang, Ishaan Ghosh, Jitendra Malik, Cornelia Fermuller, Tingfan Wu, Jiayuan Mao, Ruoshi Liu, Haozhi Qi, Yiannis Aloimonos
链接: https://arxiv.org/abs/2606.26093v1
完整摘要: Human demonstrations are a scalable data source for learning robot manipulation policies. However, common sources of human demonstration data, such as motion-capture trajectories and internet videos, capture mostly motion and appearance while missing the contact forces that are critical for force-sensitive manipulation. In this paper, we introduce ForceBand, a low-cost wrist-worn sEMG system that turns human muscle activity into force-enriched demonstrations. We first collect a 10-hour multimodal dataset containing egocentric video, sEMG, IMU, and fingertip force measurements across diverse actions and objects. Using this dataset, we pre-train an EMG2Force model that predicts per-finger forces from sEMG and IMU signals. After a short user-specific calibration, users can collect target-task demonstrations using only ForceBand and video; EMG2Force then labels these demonstrations with per-finger force traces, producing force-augmented demonstrations for robot policy learning. Experiments show that ForceBand recovers fine-grained fingertip interactions with over 50% lower force prediction error than vision-based baselines and achieves an 87% success rate on pick, squeeze, and place tasks that require object-specific force control across objects with diverse shapes, sizes, and weights. Project website: https://forceband-emg.github.io
匹配关键词: audio language model
---

[ACADEMIC - ARXIV]
标题: On-Policy Self-Distillation with Sampled Demonstrations Reduces Output Diversity
作者: Andrei Liviu Nicolicioiu, Mohammad Pezeshki, Aaron Courville
链接: https://arxiv.org/abs/2606.26091v1
完整摘要: On-policy self-distillation achieves strong pass@1 accuracy by using a single model as both teacher and student, with the teacher conditioned on a correct demonstration to provide dense token-level feedback. We show that this could come at a hidden cost: rollout diversity decreases and pass@k curves flatten (i.e., generating more rollouts fails to improve accuracy). We trace this to compounding biases in the design of self-distillation with sampled demonstrations. The teacher scores each student rollout while conditioned on a sampled correct rollout, channeling its feedback through the model's own biases. We theoretically analyze the optimal self-distillation policy and show that it tilts the base distribution by a pointwise conditional mutual information score between the student's rollout and the correct rollout used as context. Unlike the ideal optimal on-policy reinforcement learning (RL), which preserves probability ratios among equally correct rollouts, self-distillation can amplify existing probability gaps, concentrating mass on already-dominant modes. On a controlled graph path-finding task and science question-answering benchmarks, self-distilled models match or exceed RL on average performance but exhibit substantially lower functional and semantic diversity, failing on out-of-distribution settings that require diverse strategies.
匹配关键词: audio language model
---

[ACADEMIC - ARXIV]
标题: MVTrack4Gen: Multi-View Point Tracking as Geometric Supervision for 4D Video Generation
作者: JoungBin Lee, Jaewoo Jung, Jongmin Lee, Tongmin Kim, Hyunsung Kim, Takuya Narihira, Kazumi Fukuda, Jahyeok Koo, Jisang Han, Yuki Mitsufuji, Seungryong Kim
链接: https://arxiv.org/abs/2606.26087v1
完整摘要: Synthesizing a novel-view video from a monocular reference video along a target camera trajectory requires both geometric consistency and motion fidelity with respect to the reference video. Existing methods based on explicit 3D representations are limited by the accuracy of off-the-shelf reconstruction modules, which often produce inaccurate geometry for dynamic objects in monocular videos. In contrast, camera-conditioning-only methods can achieve high visual quality but often struggle to preserve geometric and motion consistency. In this work, we introduce MVTrack4Gen (Multi-View point Tracking for Novel-View Generation), a motion-aware training framework that leverages multi-view point tracking as an additional geometric and motion supervision signal for camera-conditioning-only novel-view video diffusion models. Our key finding is that specific attention layers encode strong correspondence cues, where query features attend to key features at geometrically corresponding locations across views and over time, and the misalignment of these correspondences causes motion inconsistency. Based on this observation, we route these features into an auxiliary multi-view tracking head and jointly train the diffusion model with a point-tracking objective. By explicitly strengthening these motion-aware correspondences, MVTrack4Gen improves existing models to better follow the motion in the reference view and maintain cross-view geometric consistency. Across diverse benchmarks, our method achieves state-of-the-art geometric consistency and competitive camera accuracy.
匹配关键词: audio language model
---

[ACADEMIC - ARXIV]
标题: Learning Asynchronous Upper-body Task-space Trajectory Tracking Policy for Humanoid Robots
作者: Yumeng Liu, Dongqi Wang, Jiyu Yu, Yijun Fan, Rong Xiong, Yue Wang
链接: https://arxiv.org/abs/2606.25706v1
完整摘要: High-level humanoid planners often output sparse task-space, low-rate trajectories, whereas whole-body controllers run at high frequency. This creates temporal asynchrony between the planning and execution, and structural incompleteness for full-body control. We propose an asynchronous upper body task-space tracking framework for humanoids. A student policy is initialized by teacher-student distillation, conditioned on the full cached future trajectory and an execution-time index, and trained with a sliding-window global reward to reduce frame drift without explicit frame estimation. For task-specific post-training, an MPC module completes sparse references into floating-base and upper-body guidance, while action- and FK level self-guidance constrain policy drift. Simulation and Unitree G1 hardware experiments show improved tracking under low update rates, stronger performance than synchronous and decoupled baselines, and safer adaptation to out-of-distribution motions.
匹配关键词: KV cache
---

[ACADEMIC - ARXIV]
标题: ASSCG: Just-Right Gating over Chattering for Fast-Slow LLM Planning in Autonomous Driving
作者: Sining Ang, Yuan Chen, Liu Haiyan, Xuanyao Mao, Jason Bao, Xuliang, Bingchuan Sun, Yan Wang
链接: https://arxiv.org/abs/2606.25509v1
完整摘要: Large language models (LLMs) can improve autonomous driving planning but are costly to query online, and existing fast-slow planners often rely on hand-designed triggering rules that either over-call the slow system or call it at the wrong times. We formulate slow-system invocation as a resource-aware sequential decision problem and propose the Adaptive Slow-System Control Gate (ASSCG), which makes frame-level Query/Cache/Drop decisions to refresh, reuse, or suppress slow guidance. ASSCG uses an RWKV backbone for efficient long-horizon gating and is trained with supervised fine-tuning followed by GRPO-style compute-aware reinforcement fine-tuning. We apply ASSCG to two different fast-slow architectures: (i) AsyncDriver on nuPlan Hard20 closed-loop evaluation, where ASSCG improves score to 67.28 (+2.28) while reducing average end-to-end inference latency by 60%; and (ii) a RecogDrive-based dual system that we build by replacing its original VLM-2B module with a lightweight ViT-based fast planner and adding an LLM slow planner, evaluated on NAVSIM, where ASSCG achieves 91.4 PDMS (+0.6) and increases average speed by 25%. The project page, including video visualizations and additional results, is available at https://williamxuanyu.github.io/asscg/.
匹配关键词: KV cache
---

[ACADEMIC - ARXIV]
标题: Lifelong In-Context Learning with Transformers Requires Parametric Forms of Attention
作者: Luke McDermott, Robert W. Heath, Rahul Parhi
链接: https://arxiv.org/abs/2606.25342v1
完整摘要: Lifelong continual learning remains an obstacle on the path to human-like intelligence. Modern transformers show sparks of intelligence with in-context learning. The quadratic nature of attention, however, prohibits transformers from performing this process on arbitrarily long sequences. In this work, we argue that extending in-context learning to lifelong settings is a practical solution for continual learning in AI agents. In particular, we argue that \emph{parametric forms of attention} are needed to understand a lifetime of context with transformers on a fixed hardware budget. These attention mechanisms learn the relationship between keys and their associated values at test-time with parametric regression. Our generalization of parametric approaches (linear attention, state-space models, fast weight programmers, and test-time training layers) contrasts with nonparametric counterparts like softmax attention. They replace the ever-growing key-value cache with an online-trainable neural network, maintaining a constant memory footprint. We highlight how parametric attention currently fall short of lifelong learning due to limited memory capacity or costly online updates. To address these issues, we pose a set of open questions with novel insights to guide the field toward long-horizon agents.
匹配关键词: KV cache
---

[ACADEMIC - ARXIV]
标题: Hierarchical Reinforcement Learning for Neural Network Compression (HiReLC): Pruning and Quantization
作者: Kamar Hibatallah Baghdadi, Kawther Guoual Belhamidi, Sara Belhadj, Aissa Boulmerka, Nadir Farhi
链接: https://arxiv.org/abs/2606.26002v1
完整摘要: We present HiReLC, a hierarchical ensemble-reinforcement learning framework for automated joint quantization and structured pruning of deep neural networks. The framework decomposes the compression search across two levels of abstraction: low-level agents (LLAs) operate independently per block, selecting per-kernel configurations over a multi-discrete action space spanning bitwidth, pruning keep-ratio, quantization type, and granularity, while high-level agents (HLAs) coordinate global budget allocation via ensemble voting guided by Fisher Information-based sensitivity estimates. To mitigate the computational cost of policy evaluation, an iterative active learning loop interleaves surrogate-guided RL optimization with post-compression fine-tuning, using a lightweight MLP surrogate to amortize expensive evaluations and a logit-MSE proxy during cold-start. The surrogate is used for reward shaping rather than as a replacement for final post-compression evaluation. The controller is architecture-agnostic by design, with a modular layer abstraction decoupling the RL environment from the underlying network topology. Experiments across Vision Transformer and CNN benchmarks demonstrate effective parameter-storage compression ratios of 5.99 - 6.72$\times$ with a 3.83 % gain in one setting and 0.55 - 5.62 % accuracy drops elsewhere, supporting hierarchical policy decomposition and sensitivity-aware guidance as practical design choices for joint neural network compression.
匹配关键词: quantization
---

[ACADEMIC - ARXIV]
标题: BitNet Text Embeddings
作者: Zhen Li, Xin Huang, Liang Wang, Nan Yang, Ting Song, Yan Xia, Xun Wu, Shaohan Huang, Huishuai Zhang, Furu Wei, Dongyan Zhao
链接: https://arxiv.org/abs/2606.25674v1
完整摘要: LLM-based text embedders have substantially improved retrieval and semantic representation quality, but their deployment remains costly: large backbone models slow down embedding inference, while high-dimensional full-precision embeddings impose substantial storage and bandwidth overhead on large-scale indexes. In this paper, we present BITEMBED, an extreme low-bit framework for LLM-based text embedding that jointly targets encoding efficiency and vector storage. BITEMBED converts pretrained LLM backbones into BitNet-style embedding encoders with ternary weights, quantized activations, and lightweight normalization refinement. The converted model is adapted to representation learning through continual contrastive pre-training, followed by supervised contrastive fine-tuning with both similarity-distribution distillation and attention-relation distillation from a full-precision teacher. Beyond quantizing the backbone, BITEMBED further trains output embeddings to support multiple storage precisions meeting different storage needs in various scenarios. Experiments on MMTEB (eng, v2) with Qwen3-0.6B and Gemma3-270M show that BITEMBED is largely comparable to full precision teacher embedders. Moreover, BITEMBED flexibly obtains text embeddings of various precisions, achieving a trade-off between performance and storage cost.
匹配关键词: quantization
---

[ACADEMIC - ARXIV]
标题: Leaking Circuit Secrets: Gradient Leakage Attacks on Graph Neural Networks
作者: Rupesh Raj Karn, Johann Knechtel, Ozgur Sinanoglu
链接: https://arxiv.org/abs/2606.25589v1
完整摘要: As graph neural networks (GNNs) become standard tools for critical tasks in circuit design and analysis, their security and privacy risks require careful attention. Here, we present the first comprehensive evaluation of gradient leakage attacks (GLAs) on GNNs in circuit-design and hardware-security tasks, a practical threat that has been largely overlooked. We assess state-of-the-art (SOTA) GNNs, including GraphSAGE, GCN, GIN, and GAT, trained on standard netlist benchmarks (ISCAS'85, EPFL, and TrustHub), for their fundamental vulnerability to GLAs. We find that GLAs can expose sensitive information, such as gate types and distinctive properties of hardware Trojans, which may assist adversaries in analyzing logic locking schemes or evading Trojan detection mechanisms. Our analysis shows that these risks are influenced by architectural features, with attention mechanisms (GAT) exacerbating leakage, while injective aggregation (GIN) provides comparatively stronger resilience. We further evaluate several SOTA defense techniques, including differential privacy, gradient clipping, secure aggregation, model compression with quantization, and adversarial training. We find that these techniques improve resilience only in specific settings and can also compromise model performance. Overall, our work provides key insights toward privacy-preserving GNNs and highlights the need for more robust and efficient defenses. We release our full methodology and artifacts.
匹配关键词: quantization
---

[ACADEMIC - ARXIV]
标题: Quantization Inflates Reasoning: Token Inflation as a Hidden Cost of Low-Bit Reasoning Models
作者: Xinyu Lian, Walid Krichene, Beichen Huang, Masahiro Tanaka, Olatunji Ruwase, Li Zhang, Minjia Zhang
链接: https://arxiv.org/abs/2606.25519v1
完整摘要: Quantization is widely used to reduce the inference cost of large language models, but its effect on reasoning models is not fully captured by final-answer accuracy or per-token latency. We show that low-bit post-training quantization can introduce a hidden test-time compute cost: quantized reasoning models often generate longer chains of thought even when they still answer correctly. Across mathematical reasoning, code generation, scientific question answering, and agentic tool-use benchmarks, we find that INT4/INT3 quantization can preserve accuracy but increase reasoning-token usage, offsetting the expected per-token speedup. To measure this effect, we introduce the CoT Token Inflation Ratio, which compares reasoning length between quantized and full-precision models averaged across all evaluation benchmarks. We further show that token inflation is accompanied by behavioral changes in the reasoning trace, including more intermediate steps and greater semantic repetition. These changes translate into measurable end-to-end real-world serving penalties. Finally, we evaluate mitigation strategies and find that prompting and decoding-time sampling offer inconsistent accuracy-length trade-offs, while quantization-aware training shows more promise in reducing both accuracy degradation and token inflation. Our results suggest that reasoning-token usage should be reported alongside accuracy when evaluating quantized reasoning models.
匹配关键词: quantization
---

[ACADEMIC - ARXIV]
标题: Brevity is the Soul of Inference Efficiency: Inducing Concision in VLMs via Data Curation
作者: DatologyAI, :, Matthew L. Leavitt, Siddharth Joshi, Haoli Yin, Rishabh Adiga, Haakon Mongstad, Alvin Deng, David Schwab, Bogdan Gaza, Ari Morcos
链接: https://arxiv.org/abs/2606.25432v1
完整摘要: Inference efficiency is typically pursued by shrinking the model: distillation, pruning, quantization, and sparse routing each lower per-token cost while treating token count as fixed. But output length has been inflating, and it is precisely the component the standard toolkit leaves untouched. Here, we argue that brevity is the missing inference-efficiency lever, and that pretraining data curation is a practical way to pull it: a model trained on concise, correct data learns to answer in fewer tokens; i.e. it has a lower Cost-of-Pass. We apply our VLM curation pipeline to the MAmmoTH-VL single-image subset, and compare models trained on our curated data, the standard MAmmoTH-VL data, and external open-weight frontier VLMs. On a controlled 20-evaluation set and 14 VLMs at 1B-4B activated parameters, we hold output length fixed with a per-model regression, separating brevity from quality, and price models in FLOPs per correct answer. Curation buys a 35x Cost-of-Pass advantage over the most verbose 4B comparator (Qwen3.5-4B) within $\sim$1 pp of accuracy (0.41 vs 14.58 TFLOPs per correct answer; 0.691 vs 0.704 mean accuracy). Curation also buys a +17.55-percentage-point matched-length accuracy gain over the uncurated baseline that grows with model scale (from +16.7 pp at 1B to +21.2 pp at 4B). This brevity improvement concedes no quality: generic verbosity buys no accuracy at any capability or scale, and the window where reasoning-structured verbosity still earns its tokens shrinks from 4 of 8 capability groups at 2B to 1 of 8 at 4B. Per example, the concise model even reaches correct answers the verbose reasoning model misses, marking reasoning as a distinct curation target rather than something brevity gives up. Inference efficiency in this regime is a tokens-per-correct problem, and brevity is the lever that targets it directly.
匹配关键词: quantization
---

[ACADEMIC - ARXIV]
标题: Learning Action Priors for Cross-embodiment Robot Manipulation
作者: Dong Jing, Tianqi Zhang, Jiaqi Liu, Jinman Zhao, Zelong Sun, Li Erran Li, Zhiwu Lu, Mingyu Ding
链接: https://arxiv.org/abs/2606.26095v1
完整摘要: Most Vision-Language-Action (VLA) models build on a Vision-Language Model (VLM) backbone by attaching an action module and optimizing the full policy jointly. This design inherits strong visual and linguistic priors from the VLM, but leaves the action module to learn physical motion almost from scratch. As a result, the policy lacks an explicit motion prior, forcing early optimization to simultaneously discover temporal action dynamics and cross-modal alignment, a challenge further amplified in cross-embodiment settings. In this work, we propose to pretrain the action module with motion priors before cross-modal VLA alignment. Specifically, we introduce a two-stage training framework that equips the action module with cross-embodiment temporal motion structure before VLA training begins. In Stage~1, a lightweight flow-matching-based encoder-decoder action module efficiently learns temporal motion structure solely from unconditioned action trajectories, without processing visual or language tokens. In Stage~2, this learned prior is transferred to VLA training through decoder reuse and early-stage latent distillation, aligning visual-language features with the action embedding space while still allowing end-to-end policy refinement. In addition, the trained encoder serves as a compact history compressor, summarizing state-action histories into a single temporal context token for history-aware modeling at negligible cost. Extensive experiments across 13 diverse cross-embodiment tasks on both simulated and real-world platforms validate the effectiveness of our approach. Compared with VLA training without action priors, our model achieves faster convergence, higher success rates, and substantially stronger performance on data-scarce real-world tasks. Moreover, scaling up the action data in Stage~1 yields a more generalizable action prior that directly improves downstream VLA performance.
匹配关键词: speculative decoding
---

[ACADEMIC - ARXIV]
标题: Same Evidence, Different Answer: Auditing Order Sensitivity in Multimodal Large Language Models
作者: Akshay Paruchuri, Sanmi Koyejo, Ehsan Adeli
链接: https://arxiv.org/abs/2606.26079v1
完整摘要: Standard benchmarks for multimodal large language models (MLLMs) score each item on one canonical ordering and miss whether order-irrelevant shuffling changes the answer, a baseline reliability property called for by emerging AI evaluation guidelines. We introduce Facet-Probe, a five-facet audit (option, evidence-chunk, document-rank, image-set, and mixed-modality ordering) of 18 frontier and open-weight MLLMs. A Bayesian item-response model separates ordering noise from per-facet bias, and a same-ordering control estimates the decoder-stochastic floor for observed flips. We find that none of the 18 MLLMs we audit are order-invariant: screened per-facet panel-mean flip rates span 24-50%. A Gemini same-ordering control at temperature 0 estimates a substantial ordering excess over a same-input decoder-noise floor in verified cells. Capability predicts but does not eliminate flips; the best model still flips on 13.4% of trials. In our Gemini mitigation tests, training-free prompt changes are modality-conditional and do not transfer from text to visual reasoning. These results suggest that prompt-level mitigation alone is unlikely to provide general order robustness, motivating future work on training-time and architectural approaches. We propose cross-ordering flip rate as a standard reporting axis for MLLMs.
匹配关键词: speculative decoding
---

[ACADEMIC - ARXIV]
标题: MIMFlow: Integrating Masked Image Modeling with Normalizing Flows for End-to-End Image Generation
作者: Yang Chen, Xiaowei Xu, Shuai Wang, Xinwen Zhang, Qiushi Guo, Tiezheng Ge, Limin Wang
链接: https://arxiv.org/abs/2606.26016v1
完整摘要: Normalizing Flows (NFs) are powerful generative models capable of exact density estimation and sampling. However, their strict invertibility often forces the model to exhaust its capacity on low-level pixel details, hindering the capture of high-level semantic structures. While Masked Image Modeling (MIM) has excelled in representation learning, its integration into generative pipelines has remained largely modular and disjointed. In this paper, we propose MIMFlow, a unified end-to-end framework that jointly optimizes latent semantics, pixel reconstruction, and generative flow. By employing a VAE encoder to infer semantic latent from masked images, MIMFlow achieves a principled decoupling of the generative task: the Normalizing Flow focuses on modeling a simplified, low-frequency semantic manifold, while a specialized decoder handles high-frequency synthesis. This design effectively resolves the inherent capacity bottleneck of NFs, allowing the model to prioritize global structural coherence over redundant noise. Empirical results on ImageNet 256$\times$256 show that MIMFlow-L reaches 71.3\% linear probing accuracy and an FID of 2.50. Despite using only 128 tokens (50\% fewer than standard models), it yields a 32.8\% performance gain over similar-scale NF baselines. Our code is available at https://github.com/MCG-NJU/MIMFlow.
匹配关键词: speculative decoding
---

[ACADEMIC - ARXIV]
标题: Weave of Formal Thought
作者: Alexandre Bouayad
链接: https://arxiv.org/abs/2606.25987v1
完整摘要: Large language models (LLMs) attain remarkable surface fluency on code, yet they neither formally guarantee the syntactic validity of their output nor leverage the hierarchical structure defining the target language. While existing constrained-decoding frameworks address the former, they operate under rigid assumptions that preclude critical lexical mechanisms -- including context-sensitive lexing, maximal-munch tokenization, and keyword extraction -- and only approximate vocabulary masking, sacrificing completeness. For the latter, code LLMs typically inject grammatical structure via predetermined policies rather than learning which structural information to expose. In this work, we introduce Weave of Formal Thought (WoFT), a paradigm uniting rigorous syntactic validation with learned structural representations. First, we present a formal engine and constrained decoder that is sound and complete with respect to the full Tree-sitter specification. By augmenting generalized LR (GLR) parsing with a speculative-lexing construction that maintains concurrent lexer-state hypotheses synchronized with a GLR graph-structured stack, our decoder admits every subword token extending to a valid program prefix and rejects all others. Second, we present a latent-variable fine-tuning method training the language model to interleave non-terminal grammar symbols directly into generation. Utilizing the reweighted wake-sleep (RWS) algorithm to optimize the importance-weighted evidence lower bound (IW-ELBO) of the surface text, the model learns to selectively retain formal derivations as an adaptive structural scratchpad. For Python, fine-tuning StarCoder2-3B with our RWS objective reduces per-token cross-entropy by 14.3% relative to a text-only SFT baseline, demonstrating that discretionary latent syntax recovers critical structural information that flat autoregressive training discards.
匹配关键词: speculative decoding
---

[ACADEMIC - ARXIV]
标题: USS: Unified Spatial-Semantic Prompts for Embodied Visual Tracking with Latent Dynamics Learning
作者: Yuchen Xie, Xinyu Zhou, Kuangji Zuo, Yanshuo Lu, Fengrui Huang, Boyu Ma, Jianfei Yang
链接: https://arxiv.org/abs/2606.25880v1
完整摘要: Embodied Visual Tracking (EVT) requires an agent to continuously follow a specified target while actively moving through dynamic environments. However, prevailing EVT paradigms predominantly rely on language-based target indication. While language is expressive and convenient, cluttered scenes often contain multiple objects that satisfy the same semantic description, leading to ambiguous target grounding. We therefore propose a paradigm shift, reframing target indication in EVT from text-only specification to unified spatial-semantic prompting. Based on this paradigm, we introduce Unified Spatial-Semantic Prompts for Embodied Visual Tracking with Latent Dynamics Learning, USS, an end-to-end embodied tracking framework that supports text, point, bounding box, and mask prompts within a unified architecture. USS encodes heterogeneous prompts with modality-specific encoders, fuses prompt tokens with visual features through hybrid attention, and decodes compact prompt-conditioned representations into egocentric waypoints. To further improve temporal robustness, USS incorporates a latent world model that predicts future representations through self-supervised alignment. Real-robot experiments demonstrate that explicit spatial target cues yield higher success rates than text-only prompts, particularly in scenarios involving similar distractors and longer-horizon tracking where maintaining instance-level target identity is critical. In the simulation benchmark, USS also achieves state-of-the-art performance among non-MLLM-based methods and competitive results against recent MLLM-based approaches with faster inference speed. Our findings reveal that spatial-semantic prompting provides a more precise and flexible target indication interface for embodied visual tracking. Project site: https://arescheah.github.io/uss-project-page/.
匹配关键词: speculative decoding
---

[ACADEMIC - ARXIV]
标题: Learning Action Priors for Cross-embodiment Robot Manipulation
作者: Dong Jing, Tianqi Zhang, Jiaqi Liu, Jinman Zhao, Zelong Sun, Li Erran Li, Zhiwu Lu, Mingyu Ding
链接: https://arxiv.org/abs/2606.26095v1
完整摘要: Most Vision-Language-Action (VLA) models build on a Vision-Language Model (VLM) backbone by attaching an action module and optimizing the full policy jointly. This design inherits strong visual and linguistic priors from the VLM, but leaves the action module to learn physical motion almost from scratch. As a result, the policy lacks an explicit motion prior, forcing early optimization to simultaneously discover temporal action dynamics and cross-modal alignment, a challenge further amplified in cross-embodiment settings. In this work, we propose to pretrain the action module with motion priors before cross-modal VLA alignment. Specifically, we introduce a two-stage training framework that equips the action module with cross-embodiment temporal motion structure before VLA training begins. In Stage~1, a lightweight flow-matching-based encoder-decoder action module efficiently learns temporal motion structure solely from unconditioned action trajectories, without processing visual or language tokens. In Stage~2, this learned prior is transferred to VLA training through decoder reuse and early-stage latent distillation, aligning visual-language features with the action embedding space while still allowing end-to-end policy refinement. In addition, the trained encoder serves as a compact history compressor, summarizing state-action histories into a single temporal context token for history-aware modeling at negligible cost. Extensive experiments across 13 diverse cross-embodiment tasks on both simulated and real-world platforms validate the effectiveness of our approach. Compared with VLA training without action priors, our model achieves faster convergence, higher success rates, and substantially stronger performance on data-scarce real-world tasks. Moreover, scaling up the action data in Stage~1 yields a more generalizable action prior that directly improves downstream VLA performance.
匹配关键词: kernel optimization
---

[ACADEMIC - ARXIV]
标题: On-Policy Self-Distillation with Sampled Demonstrations Reduces Output Diversity
作者: Andrei Liviu Nicolicioiu, Mohammad Pezeshki, Aaron Courville
链接: https://arxiv.org/abs/2606.26091v1
完整摘要: On-policy self-distillation achieves strong pass@1 accuracy by using a single model as both teacher and student, with the teacher conditioned on a correct demonstration to provide dense token-level feedback. We show that this could come at a hidden cost: rollout diversity decreases and pass@k curves flatten (i.e., generating more rollouts fails to improve accuracy). We trace this to compounding biases in the design of self-distillation with sampled demonstrations. The teacher scores each student rollout while conditioned on a sampled correct rollout, channeling its feedback through the model's own biases. We theoretically analyze the optimal self-distillation policy and show that it tilts the base distribution by a pointwise conditional mutual information score between the student's rollout and the correct rollout used as context. Unlike the ideal optimal on-policy reinforcement learning (RL), which preserves probability ratios among equally correct rollouts, self-distillation can amplify existing probability gaps, concentrating mass on already-dominant modes. On a controlled graph path-finding task and science question-answering benchmarks, self-distilled models match or exceed RL on average performance but exhibit substantially lower functional and semantic diversity, failing on out-of-distribution settings that require diverse strategies.
匹配关键词: kernel optimization
---

[ACADEMIC - ARXIV]
标题: Neglected Free Lunch from Post-training: Progress Advantage for LLM Agents
作者: Changdae Oh, Wendi Li, Seongheon Park, Samuel Yeh, Tanwi Mallick, Sharon Li
链接: https://arxiv.org/abs/2606.26080v1
完整摘要: Process reward models enable fine-grained, step-level evaluation of LLMs, yet building them for agentic settings remains prohibitively difficult: long-horizon interactions, irreversible actions, and stochastic environment feedback make both human annotation and Monte Carlo estimation infeasible at scale. In this work, we show that reinforcement learning (RL) post-training already provides the ingredients for effective step-level scoring, eliminating the need for dedicated reward model training altogether. Concretely, we derive an implicit advantage under a general stochastic Markov decision process, which we term progress advantage -- log-probability ratio between the RL-trained policy and its reference policy exactly recovers the optimal advantage function. This formulation makes the resulting signal annotation-free, domain-agnostic, and available as a byproduct of the standard RL post-training pipeline. We validate the effectiveness of the progress advantage across three different applications: test-time scaling, uncertainty quantification, and failure attribution on five benchmarks and four model families. Across all settings, it consistently outperforms confidence-based baselines and, despite requiring no task-specific training, surpasses dedicated trained reward models. We complement these results with deeper analyses on characteristics of progress advantage, offering practical guidance for adoption in real-world agentic systems.
匹配关键词: kernel optimization
---

[ACADEMIC - ARXIV]
标题: The Unfireable Safety Kernel: Execution-Time AI Alignment for AI Agents and Other Escapable AI Systems
作者: Seth Dobrin, Łukasz Chmiel
链接: https://arxiv.org/abs/2606.26057v1
完整摘要: AI agents are granted access to tools, APIs, and other infrastructure, making them active principals in those systems. The dominant approach places controls inside the agent's own runtime: system prompts, output filters, and guardrail libraries. Any control in the agent's address space is reachable by inputs that influence it; this generalizes to any AI system with sufficient reach into its own runtime, a class we term escapable AI systems. We identify four properties that an authorization mechanism must satisfy for architectural control rather than for cooperative requests: process separation, pre-action enforcement on a structurally only path, fail-closed at both the request and system levels, and externalized signed evidence verifiable outside the controlled system's trust boundary. We position this layer as execution-time AI alignment, complementing training-time alignment (RLHF, Constitutional AI) and inference-time alignment. We present the Unfireable Safety Kernel, a Rust reference implementation realizing all four. Its fail-closed invariant is machine-checked at two levels: an SMT theorem (Z3) and an exhaustive bounded-model-checking proof of the production decision function (Kani, 4/4 harnesses). A Python-to-Rust migration was gated on byte-equivalence (1000/1000 fixtures; 17/17 adversarial classes). We evaluate the kernel governing a live, escapable AI system, a deterministic, self-improving world model, against an escape-seeking adversary driving its real self-modification seam: across 1,000 self-modifications, all 704 attempts on the safety-critical core are refused, with no escape; a further 300, under the operator kill switch, are also refused. A separate campaign of 6,240 authorization round-trips had no successful bypass. Against 3 contemporary systems claiming the agent control plane, the agent invokes control; here, it lacks that choice.
匹配关键词: kernel optimization
---

[ACADEMIC - ARXIV]
标题: When Does Synthetic Data Augmentation Improve Score-Based Imbalanced Classification?
作者: Zhengchi Ma, Pengfei Lyu, Anru R. Zhang
链接: https://arxiv.org/abs/2606.26053v1
完整摘要: Synthetic data augmentation is widely used to mitigate class imbalance, but its theoretical effects on score-based classification remain poorly understood. This paper develops a framework for characterizing when synthetic minority augmentation can improve threshold-integrated and threshold-optimized metrics, including AUROC, AUPRC, best-threshold balanced accuracy, and best-threshold \(\F_1\) score. We separate the effect of augmentation into two components: a change in effective class weighting and a discrepancy between the synthetic and true minority distributions. Under well-specified score models, the raw estimator already targets the likelihood-ratio ordering, which is population-optimal for the metrics considered. Consequently, augmentation cannot provide a fundamental population-level improvement beyond possible finite-sample variance reduction, and may introduce additional bias through synthetic distributional error. We further establish minimax lower bounds showing that the raw estimator already achieves the optimal metric-regret rate in the well-specified regime. Under misspecification, however, augmentation can play a qualitatively different role: by changing the effective class balance, it can alter the restricted-class projection and correct ranking errors induced by the raw imbalanced objective. We provide explicit improvement bounds quantifying the roles of approximation error, finite-sample estimation error, and synthetic distributional error. Simulation studies corroborate the theory, demonstrating limited gains under well-specification and nontrivial but nonmonotone improvements under misspecification.
匹配关键词: kernel optimization
---

[ACADEMIC - ARXIV]
标题: Learning Action Priors for Cross-embodiment Robot Manipulation
作者: Dong Jing, Tianqi Zhang, Jiaqi Liu, Jinman Zhao, Zelong Sun, Li Erran Li, Zhiwu Lu, Mingyu Ding
链接: https://arxiv.org/abs/2606.26095v1
完整摘要: Most Vision-Language-Action (VLA) models build on a Vision-Language Model (VLM) backbone by attaching an action module and optimizing the full policy jointly. This design inherits strong visual and linguistic priors from the VLM, but leaves the action module to learn physical motion almost from scratch. As a result, the policy lacks an explicit motion prior, forcing early optimization to simultaneously discover temporal action dynamics and cross-modal alignment, a challenge further amplified in cross-embodiment settings. In this work, we propose to pretrain the action module with motion priors before cross-modal VLA alignment. Specifically, we introduce a two-stage training framework that equips the action module with cross-embodiment temporal motion structure before VLA training begins. In Stage~1, a lightweight flow-matching-based encoder-decoder action module efficiently learns temporal motion structure solely from unconditioned action trajectories, without processing visual or language tokens. In Stage~2, this learned prior is transferred to VLA training through decoder reuse and early-stage latent distillation, aligning visual-language features with the action embedding space while still allowing end-to-end policy refinement. In addition, the trained encoder serves as a compact history compressor, summarizing state-action histories into a single temporal context token for history-aware modeling at negligible cost. Extensive experiments across 13 diverse cross-embodiment tasks on both simulated and real-world platforms validate the effectiveness of our approach. Compared with VLA training without action priors, our model achieves faster convergence, higher success rates, and substantially stronger performance on data-scarce real-world tasks. Moreover, scaling up the action data in Stage~1 yields a more generalizable action prior that directly improves downstream VLA performance.
匹配关键词: memory efficiency
---

[ACADEMIC - ARXIV]
标题: A welding penetration prediction model for laser welding process based on self-supervised learning using physics-informed neural networks
作者: Sen Li, Xiaoying Liu, Xiaojian Xu, Chendong Shao, Yaqi Wang, Ling Lan, Xinhua Tang, Haichao Cui
链接: https://arxiv.org/abs/2606.26059v1
完整摘要: The laser welding full-penetration is of critical importance, as it constitutes one of the fundamental factors in achieving defect-free welded joints. Accurate prediction of the penetration state is therefore essential for ensuring weld quality. To this end, this paper introduces SimPhysNet, a novel algorithm that achieves high classification accuracy in laser welding penetration prediction using only a limited number of labelled images. This approach effectively overcomes the limitations of supervised learning classification algorithms, which are hindered in industrial applications by their dependence on extensive, high-quality labelled data. The core of SimPhysNet is a unique self-supervised learning paradigm that embeds physical priors into a contrastive learning framework. By incorporating a physics-informed neural network (PINN), the model is guided to extract physically meaningful features of the molten pool and keyhole from a large set of unlabelled data, while three image augmentation tasks further enhance its generalization capabilities. Subsequently, a few-shot learning strategy, based on prototypical networks, enables robust classification by constructing class representations from a minimal set of labelled images. Experimental results demonstrate that SimPhysNet achieves a classification accuracy of 96.06% using only 200 labelled images (approximately 5% of the total labelled dataset), which is comparable to the performance of conventional supervised learning algorithms that utilize the entire labelled dataset. This work presents a new, efficient, and highly accurate method, providing the way for the intelligent automation of laser welding.
匹配关键词: memory efficiency
---

[ACADEMIC - ARXIV]
标题: RoboAtlas: Contextual Active SLAM
作者: Alexander Schperberg, Shivam K. Panda, Abraham P. Vinod, M. K. Jawed, Stefano Di Cairano
链接: https://arxiv.org/abs/2606.26046v1
完整摘要: We present RoboAtlas, a contextual Active SLAM framework that adaptively balances geometric exploration and semantic reasoning using a scalable 3D semantic mapping system, OpenRoboVox. RoboAtlas integrates frontier exploration, global semantic-map reasoning, and egocentric VLM-based reasoning through a contextual multi-armed bandit that transitions from exploration to semantically guided navigation as scene understanding improves. We evaluate the system in simulation and on a Unitree Go2 robot in large-scale real-world environments exceeding 1800 m2 with approx. 30k mapped semantic instances, achieving a 100% task success rate. On the GOAT-Bench "Val Unseen" benchmark, RoboAtlas achieves state-of-the-art performance with highest reported success rate (SR) of 90.6%, using GPT-4o, improving over the strongest prior baseline by 17.8 percentage points in SR. Using the much smaller Qwen2.5-VL-7B model, it still achieves 88.8% SR, outperforming all baselines using GPT-4o in SR, and revealing the importance of the information gained by our semantic mapping framework over simply replacing the underlying foundation model. The results demonstrate that grounding foundation models with large-scale 3D semantic maps enables robust and efficient contextual Active SLAM.
匹配关键词: memory efficiency
---

[ACADEMIC - ARXIV]
标题: How Robust is OCR-Reasoning? Evaluating OCR-Reasoning Robustness of Vision-Language Models under Visual Perturbations
作者: Yuxing Cheng, Yuan Wu, Yi Chang
链接: https://arxiv.org/abs/2606.26041v1
完整摘要: Vision-language models (VLMs) have achieved strong performance on OCR-based benchmarks and increasingly focused on text-rich understanding, but their robustness under controlled visual degradation remains insufficiently understood. This gap is critical for OCR reasoning, where visual corruption can induce OCR errors and structural distortions, thereby introducing uncertainty into the reasoning task. To systematically study this problem, we introduce OCR-Robust, a benchmark designed for evaluating OCR reasoning robustness under visual perturbations. It contains 812 samples across two complementary subsets: OCR1.0, covering documents, scene text, receipts, handwriting, and mathematical content, and OCR2.0, focusing on charts, geometry diagrams, and tables. To enable efficient yet informative evaluation, we conduct a pilot study over 18 candidate perturbations and select 5 representative types at 3 severity levels each based on their impact and cross-model discriminability. We evaluate robustness using clean accuracy, Relative Corruption Retention (RCR), Worst-Case Retention (WCR), and a composite Corruption Robustness Index (CRI), and benchmark 18 models spanning proprietary systems, open-source VLMs, and OCR+LLM pipelines. Our results show that higher clean accuracy does not necessarily imply stronger robustness, and that models can suffer pronounced degradation in the worst case on OCR tasks that are sensitive to structure, and charts and tables are substantially more fragile than document-like inputs under perturbation.
匹配关键词: memory efficiency
---

[ACADEMIC - ARXIV]
标题: FAR-LIO: Enabling High-Speed Autonomy through Fast, Accurate, and Robust LiDAR-Inertial Odometry
作者: Maximilian Leitenstern, Marcel Weinmann, Patrick Haft, Tobias Lasser, Dominik Kulmer, Markus Lienkamp
链接: https://arxiv.org/abs/2606.26010v1
完整摘要: Robust and accurate odometry estimation is essential in modern robotics. In environments characterized by highly dynamic motion and sensor noise, odometry estimation becomes increasingly challenging. Autonomous racing combines both factors in an unstructured setting, where minimizing odometry latency is essential for stable closed-loop control. This paper introduces FAR-LIO, a highly optimized CUDA-accelerated LiDAR-inertial odometry framework developed for Fast, Accurate, and Robust performance. Our system leverages a novel CUDA-based voxel hashmap to enable parallelized nearest-neighbor search and efficient map updates. We employ a sparsity-aware Generalized Iterative Closest Point algorithm with adaptive thresholding on top of the CUDA-based voxel hashmap with adaptive density to achieve low-latency without compromising accuracy. An Extended Kalman Filter serves as a robust backend. It utilizes an upsampling and delay compensation strategy to fuse the LiDAR odometry with high-frequency IMU data, thereby ensuring a robust and smooth odometry output. We evaluate FAR-LIO across four different sensor setups, using both public datasets and data from two autonomous racecars driving at speeds of up to 250 km/h. FAR-LIO achieves an average 6.9% reduction in the positional error and 38.4% lower runtime compared to state-of-the-art baselines on target hardware using a single parameter set. This demonstrates its computational efficiency and broad applicability. To build upon our work, our code is available open-source on https://github.com/TUMFTM/FAR-LIO.
匹配关键词: memory efficiency
---

[ACADEMIC - ARXIV]
标题: RevengeBench: Reverse Engineering Code-Space Policies from Behavioral Experiments
作者: Babak Rahmani, Sebastian Dziadzio, Joschka Strüber, Sergio Hernández-Gutiérrez, Matthias Bethge
链接: https://arxiv.org/abs/2606.26094v1
完整摘要: For most of scientific history, researchers studying behavior could only infer hidden mechanisms from outward actions: an inverse problem that becomes more tractable when observation is augmented by targeted intervention. We pose a computational analogue: given only behavioral traces of an agent in a game environment, can a learner reconstruct the underlying decision program as executable code, and how much does this reconstruction improve with the ability to design controlled experiments? We introduce RevengeBench, a benchmark of 75 LLM generated, Elo-calibrated policies across five game environments, drawn from CodeClash tournament trajectories. The learner observes the hidden target policy play against sampled opponents and designs behavioral probes in the form of custom opponent policies that elicit informative behavior. It then submits an executable hypothesis, which is evaluated using continuous action-distance metrics. We further validate that recovered code carries informative signal in downstream player-versus-player tournaments. Across twelve frontier LLMs, recovery quality varies substantially (34 to 72% of initial distance closed), with reconstructed policies yielding measurable competitive advantage, particularly for weaker models that otherwise struggle to design effective counter-strategies. Our benchmark positions behavioral recovery of programmatic policies as a tractable inverse problem in code-space, opening a path to opponent modeling, policy interpretability, and the broader question of inferring latent mechanisms from observations.
匹配关键词: agent
---

[ACADEMIC - ARXIV]
标题: Neglected Free Lunch from Post-training: Progress Advantage for LLM Agents
作者: Changdae Oh, Wendi Li, Seongheon Park, Samuel Yeh, Tanwi Mallick, Sharon Li
链接: https://arxiv.org/abs/2606.26080v1
完整摘要: Process reward models enable fine-grained, step-level evaluation of LLMs, yet building them for agentic settings remains prohibitively difficult: long-horizon interactions, irreversible actions, and stochastic environment feedback make both human annotation and Monte Carlo estimation infeasible at scale. In this work, we show that reinforcement learning (RL) post-training already provides the ingredients for effective step-level scoring, eliminating the need for dedicated reward model training altogether. Concretely, we derive an implicit advantage under a general stochastic Markov decision process, which we term progress advantage -- log-probability ratio between the RL-trained policy and its reference policy exactly recovers the optimal advantage function. This formulation makes the resulting signal annotation-free, domain-agnostic, and available as a byproduct of the standard RL post-training pipeline. We validate the effectiveness of the progress advantage across three different applications: test-time scaling, uncertainty quantification, and failure attribution on five benchmarks and four model families. Across all settings, it consistently outperforms confidence-based baselines and, despite requiring no task-specific training, surpasses dedicated trained reward models. We complement these results with deeper analyses on characteristics of progress advantage, offering practical guidance for adoption in real-world agentic systems.
匹配关键词: agent
---

[ACADEMIC - ARXIV]
标题: Model Forensics: Investigating Whether Concerning Behavior Reflects Misalignment
作者: Aditya Singh, Gerson Kroiz, Senthooran Rajamanoharan, Neel Nanda
链接: https://arxiv.org/abs/2606.26071v1
完整摘要: A central goal of safety research is determining whether a model is misaligned. Prior work has largely focused on detecting concerning behavior. But behavior alone does not establish misalignment: a concerning action can arise from benign causes such as confusion. This motivates model forensics: investigating whether the action was driven by malign intent. In this paper, we propose a baseline protocol for model forensics consisting of two steps, iterated as needed. First, we read the chain of thought (CoT) to generate hypotheses about what drives model behavior. Second, we make edits to the prompt or environment to test these hypotheses. While the CoT is not always faithful, it is a rich source of unsupervised insight that can guide the collection of more rigorous evidence. To evaluate our protocol, we create a suite of six agentic environments where models exhibit concerning behavior, and apply it to each. We establish that Kimi K2 Thinking takes shortcuts due to a genuine disposition towards low-effort actions, by showing this hypothesis successfully predicts its behavior. Through counterfactual experiments, we show DeepSeek R1 deceives out of a desire to be consistent with a previous instance of itself. Our methods nonetheless leave significant room for refinement. For example, when we test whether Kimi K2 Thinking believes it is violating user intent, we find no evidence of such a belief, but without positive controls we cannot confirm our tests would detect it. Overall, we find our simple protocol provides a strong baseline that we hope future work will improve upon. More broadly, our work is a concrete step in developing the growing field of model forensics.
匹配关键词: agent
---

[ACADEMIC - ARXIV]
标题: The Unfireable Safety Kernel: Execution-Time AI Alignment for AI Agents and Other Escapable AI Systems
作者: Seth Dobrin, Łukasz Chmiel
链接: https://arxiv.org/abs/2606.26057v1
完整摘要: AI agents are granted access to tools, APIs, and other infrastructure, making them active principals in those systems. The dominant approach places controls inside the agent's own runtime: system prompts, output filters, and guardrail libraries. Any control in the agent's address space is reachable by inputs that influence it; this generalizes to any AI system with sufficient reach into its own runtime, a class we term escapable AI systems. We identify four properties that an authorization mechanism must satisfy for architectural control rather than for cooperative requests: process separation, pre-action enforcement on a structurally only path, fail-closed at both the request and system levels, and externalized signed evidence verifiable outside the controlled system's trust boundary. We position this layer as execution-time AI alignment, complementing training-time alignment (RLHF, Constitutional AI) and inference-time alignment. We present the Unfireable Safety Kernel, a Rust reference implementation realizing all four. Its fail-closed invariant is machine-checked at two levels: an SMT theorem (Z3) and an exhaustive bounded-model-checking proof of the production decision function (Kani, 4/4 harnesses). A Python-to-Rust migration was gated on byte-equivalence (1000/1000 fixtures; 17/17 adversarial classes). We evaluate the kernel governing a live, escapable AI system, a deterministic, self-improving world model, against an escape-seeking adversary driving its real self-modification seam: across 1,000 self-modifications, all 704 attempts on the safety-critical core are refused, with no escape; a further 300, under the operator kill switch, are also refused. A separate campaign of 6,240 authorization round-trips had no successful bypass. Against 3 contemporary systems claiming the agent control plane, the agent invokes control; here, it lacks that choice.
匹配关键词: agent
---

[ACADEMIC - ARXIV]
标题: AI translation of literary texts is "fine", but readers still prefer human translations
作者: Yves Ferstler, Adam Podoxin, Ty Brassington, Roman Grundkiewicz, Maite Taboada, Marzena Karpinska
链接: https://arxiv.org/abs/2606.26040v1
完整摘要: AI translation of literary works is increasingly common. While the content may be rendered adequately, we do not know enough about how readers experience it in terms of immersiveness and literary effect, aspects poorly captured by automatic machine translation metrics or human evaluation targeting fluency and adequacy. We ask 15 avid readers to compare recently published human translations (HT) to machine translations (MT) generated with an agentic large language model (LLM)-based pipeline, for 15 recent novels in French, Polish, and Japanese and translated into English. Readers evaluated approximately 8K-word excerpts in two conditions: immersive reading of the whole excerpt (30 comparisons) and close reading of 386 aligned HT-MT chunk pairs (772 comparisons), with two readers per book and in alternating order of presentation. Overall, readers find MT "fine", but prefer HT (slightly at excerpt-level 19/30, more clearly at chunk-level 522/772) for its ease, clarity, and immersive nature. Readers' highlights show that MT's quality varies more within one book than HT's does. Crucially, readers cannot reliably tell the two apart (17/30 guess correctly) and tend to prefer the version they believe to be human. Automatic metrics, including LLM-as-a-judge approaches, fail to recover reader preferences and favor MT. We release LAIT (Literary AI Translation), a reader-centered evaluation dataset with 1K reader comments, 2K judgments and preference ratings, and 7.2K span-level annotations, along with our evaluation protocol and supporting interface.
匹配关键词: agent
---

[ACADEMIC - ARXIV]
标题: RevengeBench: Reverse Engineering Code-Space Policies from Behavioral Experiments
作者: Babak Rahmani, Sebastian Dziadzio, Joschka Strüber, Sergio Hernández-Gutiérrez, Matthias Bethge
链接: https://arxiv.org/abs/2606.26094v1
完整摘要: For most of scientific history, researchers studying behavior could only infer hidden mechanisms from outward actions: an inverse problem that becomes more tractable when observation is augmented by targeted intervention. We pose a computational analogue: given only behavioral traces of an agent in a game environment, can a learner reconstruct the underlying decision program as executable code, and how much does this reconstruction improve with the ability to design controlled experiments? We introduce RevengeBench, a benchmark of 75 LLM generated, Elo-calibrated policies across five game environments, drawn from CodeClash tournament trajectories. The learner observes the hidden target policy play against sampled opponents and designs behavioral probes in the form of custom opponent policies that elicit informative behavior. It then submits an executable hypothesis, which is evaluated using continuous action-distance metrics. We further validate that recovered code carries informative signal in downstream player-versus-player tournaments. Across twelve frontier LLMs, recovery quality varies substantially (34 to 72% of initial distance closed), with reconstructed policies yielding measurable competitive advantage, particularly for weaker models that otherwise struggle to design effective counter-strategies. Our benchmark positions behavioral recovery of programmatic policies as a tractable inverse problem in code-space, opening a path to opponent modeling, policy interpretability, and the broader question of inferring latent mechanisms from observations.
匹配关键词: tool use
---

[ACADEMIC - ARXIV]
标题: ForceBand: Learning Forceful Manipulation with sEMG
作者: Botao He, Zhi Wang, Linna Kuang, Ishaan Ghosh, Jitendra Malik, Cornelia Fermuller, Tingfan Wu, Jiayuan Mao, Ruoshi Liu, Haozhi Qi, Yiannis Aloimonos
链接: https://arxiv.org/abs/2606.26093v1
完整摘要: Human demonstrations are a scalable data source for learning robot manipulation policies. However, common sources of human demonstration data, such as motion-capture trajectories and internet videos, capture mostly motion and appearance while missing the contact forces that are critical for force-sensitive manipulation. In this paper, we introduce ForceBand, a low-cost wrist-worn sEMG system that turns human muscle activity into force-enriched demonstrations. We first collect a 10-hour multimodal dataset containing egocentric video, sEMG, IMU, and fingertip force measurements across diverse actions and objects. Using this dataset, we pre-train an EMG2Force model that predicts per-finger forces from sEMG and IMU signals. After a short user-specific calibration, users can collect target-task demonstrations using only ForceBand and video; EMG2Force then labels these demonstrations with per-finger force traces, producing force-augmented demonstrations for robot policy learning. Experiments show that ForceBand recovers fine-grained fingertip interactions with over 50% lower force prediction error than vision-based baselines and achieves an 87% success rate on pick, squeeze, and place tasks that require object-specific force control across objects with diverse shapes, sizes, and weights. Project website: https://forceband-emg.github.io
匹配关键词: tool use
---

[ACADEMIC - ARXIV]
标题: On-Policy Self-Distillation with Sampled Demonstrations Reduces Output Diversity
作者: Andrei Liviu Nicolicioiu, Mohammad Pezeshki, Aaron Courville
链接: https://arxiv.org/abs/2606.26091v1
完整摘要: On-policy self-distillation achieves strong pass@1 accuracy by using a single model as both teacher and student, with the teacher conditioned on a correct demonstration to provide dense token-level feedback. We show that this could come at a hidden cost: rollout diversity decreases and pass@k curves flatten (i.e., generating more rollouts fails to improve accuracy). We trace this to compounding biases in the design of self-distillation with sampled demonstrations. The teacher scores each student rollout while conditioned on a sampled correct rollout, channeling its feedback through the model's own biases. We theoretically analyze the optimal self-distillation policy and show that it tilts the base distribution by a pointwise conditional mutual information score between the student's rollout and the correct rollout used as context. Unlike the ideal optimal on-policy reinforcement learning (RL), which preserves probability ratios among equally correct rollouts, self-distillation can amplify existing probability gaps, concentrating mass on already-dominant modes. On a controlled graph path-finding task and science question-answering benchmarks, self-distilled models match or exceed RL on average performance but exhibit substantially lower functional and semantic diversity, failing on out-of-distribution settings that require diverse strategies.
匹配关键词: tool use
---

[ACADEMIC - ARXIV]
标题: Real-Time Voice AI Hears but Does Not Listen
作者: Martijn Bartelds, Federico Bianchi, James Zou
链接: https://arxiv.org/abs/2606.26083v1
完整摘要: Speech conveys information through both words and vocal delivery. We evaluate four leading production realtime voice systems-OpenAI's GPT Realtime 2, Google's Gemini 3.1 Flash Live, and Alibaba's Qwen3.5 Omni Plus and Omni Flash-on tasks where the words and the delivery patterns both convey meaningful information. Across three consequential scenarios, all four systems act on the words rather than the voice. They end calls with crying callers who insist nothing is wrong, approve wire transfers authorized in frightened voices, and enroll callers whose agreement is clearly sarcastic. Surprisingly, this is often not a failure of perception. When asked directly, three of the four systems reliably identify the distress, fear, or sarcasm they later ignore when making decisions. We observe a similar pattern when these realtime voice systems estimate accent and age, as their responses frequently follow the biases of the words rather than the acoustic properties of the speaker. We term this disconnect between perception and action the emotional intelligence gap of voice AI. Prompting systems to explicitly attend to vocal delivery improves performance only partially and inconsistently. Our findings show that current realtime voice AI systems often behave as if speech had been reduced to a transcript, suggesting that they should be used with caution in settings where the tone and emotion of delivery convey important information.
匹配关键词: tool use
---

[ACADEMIC - ARXIV]
标题: A cross-process welding penetration status prediction algorithm based on unsupervised domain adaptation in laser and TIG welding
作者: Sen Li, Haichao Cui, Chendong Shao, Yaqi Wang, Xinhua Tang
链接: https://arxiv.org/abs/2606.26078v1
完整摘要: Supervised deep learning has been widely used for weld penetration state classification; however, its performance often degrades significantly under domain shift, such as when transferring models between welding processes with distinct physical mechanisms:for instance, from arc-dominated tungsten inert gas (TIG) welding to keyhole-based laser welding. To overcome this limitation, we propose an unsupervised domain adaptation (UDA) framework integrated with a gradual source domain expansion (GSDE) strategy. Evaluated on dedicated TIG and laser welding datasets, our approach achieves high accuracy in both same-process and cross-process transfer tasks. Specifically, it attains average accuracies of 90.65% on TIGFH and 90.72% on LSPS in same-process settings, surpassing a supervised baseline by 35.83% and 38.87%, respectively. More notably, in cross-process scenarios, it reaches 80.48% for TIG to Laser and 81.13% for Laser to TIG, improving upon the baseline by 43.39% and 43.40%. UMAP visualizations verify that the model learns domain-invariant features while maintaining discriminative class boundaries. This method considerably lowers the relabeling cost for new welding processes and enhances the versatility of intelligent monitoring across different welding systems.
匹配关键词: tool use
---

[ACADEMIC - ARXIV]
标题: G2DP: Diffusion Planning with Spatio-Temporal Grid Guidance
作者: Hang Yu, Ye Jin, Alessandro Canevaro, Julian Schmidt, Julian Jordan, Peizheng Li, Marc Kaufeld, Silvan Lindner, Johannes Betz, Wilhelm Stork
链接: https://arxiv.org/abs/2606.26017v1
完整摘要: In autonomous driving, diffusion-based planners have emerged as a promising paradigm for robust motion planning in dense and interactive traffic, as they can effectively model diverse driving behaviors. However, their inherent stochasticity often requires explicit guidance during denoising to ensure safety and route adherence for robust closed-loop execution. Existing guidance typically relies on sparse, entity-centric geometric queries or post-hoc refinement, yielding limited situational awareness and fragile performance in interactive scenes. To address this issue, we propose G2DP (Grid-Guided Diffusion Planning), a diffusion-based planner that directly enforces dense environmental constraints through inference-time guidance. Specifically, G2DP constructs a differentiable spatio-temporal cost volume by fusing probabilistic future occupancy distributions with a route-progress map. By formulating this volume as a continuous safety energy functional, it injects dense gradients directly into the denoising loop, actively steering trajectory generation toward collision-free and progress-optimal regions. Extensive closed-loop evaluations show that G2DP achieves state-of-the-art performance on nuPlan, outperforming the strongest imitation-learning baseline by +7.2 points in reactive score. It further maintains top scores in zero-shot transfers to interPlan and DeepScenario benchmarks, with collision avoidance improving by +10.15 over the unguided approach on interPlan. These results demonstrate that spatio-temporal cost grids serve as an effective representation for robust guidance in diffusion-based planning.
匹配关键词: planning
---

[ACADEMIC - ARXIV]
标题: Helpful or Harmful? Evaluating LLM-Assisted Vulnerability Patching via a Human Study
作者: Giulian Biolo, Michael Tezza, Yuanjun Gong, Fabio Massacci
链接: https://arxiv.org/abs/2606.25973v1
完整摘要: Software vulnerability remediation is a cognitively demanding task that requires specialized security expertise often lacking in general developers. In the meantime, Large Language Models (LLMs) assisted tools show potential in vulnerability detection, location, and repair tasks. [Hypothesis:] While LLM-assistance is hypothesized to accelerate patching, it also risks introducing hallucinations or insecure code, leading to a higher likelihood of generating superficial repairs that bypass the standard functionality checks but fail the security validation. [Objective:] We aim to present an empirical experiment, unveiling the capability of LLM-assisted vulnerability patching compared to manual debugging on human participants in real-world scenarios. [Method:] We plan to conduct a controlled experiment using a Balanced Crossover design. For that, we have developed a WebApp for code execution and integrated hidden Ghost Tests to verify patch integrity beyond visible functional requirements. The experiment involves training and evaluation scenarios. The remediation speed, remediation efficacy for both standard functionality tests and security tests, and participant perception will be evaluated. [Pilot Study:] A pilot experiment with a small sample of participants has been conducted, providing insights for the following study.
匹配关键词: planning
---

[ACADEMIC - ARXIV]
标题: ROAD-VLA: Robust Online Adaptation via Self-Distillation for Vision-Language-Action Models
作者: Kejing Wang, Toan Nguyen, Minh Hoang Nguyen, Simon Khan, Flora D. Salim
链接: https://arxiv.org/abs/2606.25800v1
完整摘要: Effective online adaptation of vision-language-action (VLA) models remains challenging, as sparse rewards provide weak supervision for high-dimensional autoregressive action policies. Although self-distillation can in principle provide denser training signals, we find that text-based privileged teachers conditioned on demonstrations, retrieved experiences, or high-level plans are ineffective for VLA adaptation, exposing a modality gap between symbolic guidance and low-level robot actions. We propose ROAD-VLA, an advantage-guided self-distillation framework that constructs a proximal teacher directly in action space by perturbing action-token logits with calibrated advantage estimates. This converts sparse rewards into dense token-level supervision while keeping the teacher close to the current policy. We further derive a policy-improvement lower bound under calibrated advantages and accurate teacher matching. Across seven robotic manipulation environments with in-distribution and out-of-distribution shifts, ROADVLA outperforms PPO in nearly all settings, demonstrating robust online VLA adaptation.
匹配关键词: planning
---

[ACADEMIC - ARXIV]
标题: UniTeD: Unified Temporal Diffusion for Joint Perception and Planning in Autonomous Driving
作者: Bo Zhao, Xinting Zhao, Naifan Li, Erkang Cheng, Haibin Ling
链接: https://arxiv.org/abs/2606.25736v1
完整摘要: Diffusion models have shown strong potential for multi-modal planning in end-to-end autonomous driving. However, most existing methods confine diffusion to the planning module, conditioning on fixed outputs from separate discriminative perception networks. This decoupled design propagates perception errors to the planner, increasing optimization difficulty and reducing robustness. To overcome these limitations, we propose UniTeD, a Unified Temporal Diffusion framework that jointly models perception and planning through iterative denoising in a shared generative space. By enabling bidirectional information exchange, the framework facilitates mutual refinement between tasks and improves robustness via noise-conditioned multi-task training. We further extend this unified diffusion paradigm to a streaming setting by incorporating temporal context. A Temporal Transition Module (TTM) is introduced to resolve the noise-level mismatch between historical and current frames. In addition, we propose an Anchor Refresh Strategy (ARS) to alleviate the training-inference distribution shift commonly observed in sparse diffusion-based end-to-end driving frameworks. Without bells and whistles, UniTeD achieves state-of-the-art performance across multiple benchmarks, surpassing both recent discriminative end-to-end methods and diffusion-based planning approaches.
匹配关键词: planning
---

[ACADEMIC - ARXIV]
标题: Learning Asynchronous Upper-body Task-space Trajectory Tracking Policy for Humanoid Robots
作者: Yumeng Liu, Dongqi Wang, Jiyu Yu, Yijun Fan, Rong Xiong, Yue Wang
链接: https://arxiv.org/abs/2606.25706v1
完整摘要: High-level humanoid planners often output sparse task-space, low-rate trajectories, whereas whole-body controllers run at high frequency. This creates temporal asynchrony between the planning and execution, and structural incompleteness for full-body control. We propose an asynchronous upper body task-space tracking framework for humanoids. A student policy is initialized by teacher-student distillation, conditioned on the full cached future trajectory and an execution-time index, and trained with a sliding-window global reward to reduce frame drift without explicit frame estimation. For task-specific post-training, an MPC module completes sparse references into floating-base and upper-body guidance, while action- and FK level self-guidance constrain policy drift. Simulation and Unitree G1 hardware experiments show improved tracking under low update rates, stronger performance than synchronous and decoupled baselines, and safer adaptation to out-of-distribution motions.
匹配关键词: planning
---

[ACADEMIC - ARXIV]
标题: The Unfireable Safety Kernel: Execution-Time AI Alignment for AI Agents and Other Escapable AI Systems
作者: Seth Dobrin, Łukasz Chmiel
链接: https://arxiv.org/abs/2606.26057v1
完整摘要: AI agents are granted access to tools, APIs, and other infrastructure, making them active principals in those systems. The dominant approach places controls inside the agent's own runtime: system prompts, output filters, and guardrail libraries. Any control in the agent's address space is reachable by inputs that influence it; this generalizes to any AI system with sufficient reach into its own runtime, a class we term escapable AI systems. We identify four properties that an authorization mechanism must satisfy for architectural control rather than for cooperative requests: process separation, pre-action enforcement on a structurally only path, fail-closed at both the request and system levels, and externalized signed evidence verifiable outside the controlled system's trust boundary. We position this layer as execution-time AI alignment, complementing training-time alignment (RLHF, Constitutional AI) and inference-time alignment. We present the Unfireable Safety Kernel, a Rust reference implementation realizing all four. Its fail-closed invariant is machine-checked at two levels: an SMT theorem (Z3) and an exhaustive bounded-model-checking proof of the production decision function (Kani, 4/4 harnesses). A Python-to-Rust migration was gated on byte-equivalence (1000/1000 fixtures; 17/17 adversarial classes). We evaluate the kernel governing a live, escapable AI system, a deterministic, self-improving world model, against an escape-seeking adversary driving its real self-modification seam: across 1,000 self-modifications, all 704 attempts on the safety-critical core are refused, with no escape; a further 300, under the operator kill switch, are also refused. A separate campaign of 6,240 authorization round-trips had no successful bypass. Against 3 contemporary systems claiming the agent control plane, the agent invokes control; here, it lacks that choice.
匹配关键词: RLHF
---

[ACADEMIC - ARXIV]
标题: Cliff Tokens: Identifying Single-Token Failure Triggers in LLM Mathematical Reasoning
作者: Jaeyong Ko, Pilsung Kang, Yukyung Lee
链接: https://arxiv.org/abs/2606.25524v1
完整摘要: Large language models (LLMs) reach high accuracy in mathematical reasoning, but individual traces on the same problem diverge; some arrive at the correct answer while others fail. Prior work analyzes failure at the step, chunk, or sentence level, or at tokens where failure has already occurred. Neither identifies the precise token that triggers the shift toward failure. We introduce the cliff token, a token where the token-wise potential drops significantly under an adaptive threshold that scales with the local token-wise potential, based on a one-sided two-proportion z-test. Across seven models and three mathematical reasoning benchmarks (GSM1K, MATH500, AIME 2025), cliff tokens act as failure triggers; deleting the first cliff token and resampling recovers pass@64 to 1.0, while keeping it limits recovery to between 0.71 and 1.00. We further introduce a cliff taxonomy of deterministic, uncertain, and sampled-off cliffs, defined by greedy choice and token entropy. Each type has distinct probabilistic characteristics, and the taxonomy generalizes across model scales. Finally, we validate the taxonomy via single-token preference optimization at cliff positions (Cliff-DPO). Trained on GSM8K, Cliff-DPO improves accuracy across benchmarks by up to +6.6. Optimizing at uncertain and sampled-off cliffs improves reasoning, while deterministic cliffs do not.
匹配关键词: DPO
---

[ACADEMIC - ARXIV]
标题: Learning Action Priors for Cross-embodiment Robot Manipulation
作者: Dong Jing, Tianqi Zhang, Jiaqi Liu, Jinman Zhao, Zelong Sun, Li Erran Li, Zhiwu Lu, Mingyu Ding
链接: https://arxiv.org/abs/2606.26095v1
完整摘要: Most Vision-Language-Action (VLA) models build on a Vision-Language Model (VLM) backbone by attaching an action module and optimizing the full policy jointly. This design inherits strong visual and linguistic priors from the VLM, but leaves the action module to learn physical motion almost from scratch. As a result, the policy lacks an explicit motion prior, forcing early optimization to simultaneously discover temporal action dynamics and cross-modal alignment, a challenge further amplified in cross-embodiment settings. In this work, we propose to pretrain the action module with motion priors before cross-modal VLA alignment. Specifically, we introduce a two-stage training framework that equips the action module with cross-embodiment temporal motion structure before VLA training begins. In Stage~1, a lightweight flow-matching-based encoder-decoder action module efficiently learns temporal motion structure solely from unconditioned action trajectories, without processing visual or language tokens. In Stage~2, this learned prior is transferred to VLA training through decoder reuse and early-stage latent distillation, aligning visual-language features with the action embedding space while still allowing end-to-end policy refinement. In addition, the trained encoder serves as a compact history compressor, summarizing state-action histories into a single temporal context token for history-aware modeling at negligible cost. Extensive experiments across 13 diverse cross-embodiment tasks on both simulated and real-world platforms validate the effectiveness of our approach. Compared with VLA training without action priors, our model achieves faster convergence, higher success rates, and substantially stronger performance on data-scarce real-world tasks. Moreover, scaling up the action data in Stage~1 yields a more generalizable action prior that directly improves downstream VLA performance.
匹配关键词: alignment
---

[ACADEMIC - ARXIV]
标题: TryOnCrafter: Unleashing Camera Trajectories for Realistic Video Virtual Try-on via a Renderable 4D Try-on Proxy
作者: Hao Sun, Hao Yan, Mengting Chen, Quanjian Song, Yu Li, Juan Cao, Jinsong Lan, Xiaoyong Zhu, Bo Zheng, Sheng Tang
链接: https://arxiv.org/abs/2606.26092v1
完整摘要: While Video Virtual Try-on (VVT) has achieved remarkable progress in synthesizing realistic garment overlays on dynamic subjects, existing paradigms remains fundamentally constrained by a passive dependency on source camera trajectories, failing to accommodate the requisite interactive freedom for omnidirectional viewpoint exploration. To address this limitation, we define a pioneering research frontier: Camera-controllable Video Virtual Try-on (CaM-VVT). Unlike conventional VVT, CaM-VVT not only necessitates viewpoint-agnostic texture hallucination but also strict structural synchronization between non-rigid human dynamics and background contexts under arbitrary, unconstrained camera movements. To tackle these challenges, we present TryOnCrafter, the first unified DiT-based framework specifically architected for the CaM-VVT task. Departing from implicit pixel-space manipulation, we introduce a Renderable 4D Try-on Proxy that explicitly decouples the human subject from the environment. This is achieved by distilling high-fidelity 2D try-on priors into a clothed 3DGS-based avatar, which is subsequently animated via SMPL-X sequences and metric-aligned into a reconstructed background point cloud. This proxy establishes a robust structural foundation with superior texture density and motion integrity. Our Proxy-Anchored Video DiT leverages this robust structural foundation as a primary geometric anchor, ensuring that the synthesized photorealistic videos are strictly constrained by prescribed trajectories and physically plausible deformations. Benefiting from the inherent editability of the 4D proxy, TryOnCrafter facilitates diverse downstream applications, including human relocalization, ``bullet time'' effects, and $360$-degree orbital viewing.
匹配关键词: alignment
---

[ACADEMIC - ARXIV]
标题: The Unfireable Safety Kernel: Execution-Time AI Alignment for AI Agents and Other Escapable AI Systems
作者: Seth Dobrin, Łukasz Chmiel
链接: https://arxiv.org/abs/2606.26057v1
完整摘要: AI agents are granted access to tools, APIs, and other infrastructure, making them active principals in those systems. The dominant approach places controls inside the agent's own runtime: system prompts, output filters, and guardrail libraries. Any control in the agent's address space is reachable by inputs that influence it; this generalizes to any AI system with sufficient reach into its own runtime, a class we term escapable AI systems. We identify four properties that an authorization mechanism must satisfy for architectural control rather than for cooperative requests: process separation, pre-action enforcement on a structurally only path, fail-closed at both the request and system levels, and externalized signed evidence verifiable outside the controlled system's trust boundary. We position this layer as execution-time AI alignment, complementing training-time alignment (RLHF, Constitutional AI) and inference-time alignment. We present the Unfireable Safety Kernel, a Rust reference implementation realizing all four. Its fail-closed invariant is machine-checked at two levels: an SMT theorem (Z3) and an exhaustive bounded-model-checking proof of the production decision function (Kani, 4/4 harnesses). A Python-to-Rust migration was gated on byte-equivalence (1000/1000 fixtures; 17/17 adversarial classes). We evaluate the kernel governing a live, escapable AI system, a deterministic, self-improving world model, against an escape-seeking adversary driving its real self-modification seam: across 1,000 self-modifications, all 704 attempts on the safety-critical core are refused, with no escape; a further 300, under the operator kill switch, are also refused. A separate campaign of 6,240 authorization round-trips had no successful bypass. Against 3 contemporary systems claiming the agent control plane, the agent invokes control; here, it lacks that choice.
匹配关键词: alignment
---

[ACADEMIC - ARXIV]
标题: AI translation of literary texts is "fine", but readers still prefer human translations
作者: Yves Ferstler, Adam Podoxin, Ty Brassington, Roman Grundkiewicz, Maite Taboada, Marzena Karpinska
链接: https://arxiv.org/abs/2606.26040v1
完整摘要: AI translation of literary works is increasingly common. While the content may be rendered adequately, we do not know enough about how readers experience it in terms of immersiveness and literary effect, aspects poorly captured by automatic machine translation metrics or human evaluation targeting fluency and adequacy. We ask 15 avid readers to compare recently published human translations (HT) to machine translations (MT) generated with an agentic large language model (LLM)-based pipeline, for 15 recent novels in French, Polish, and Japanese and translated into English. Readers evaluated approximately 8K-word excerpts in two conditions: immersive reading of the whole excerpt (30 comparisons) and close reading of 386 aligned HT-MT chunk pairs (772 comparisons), with two readers per book and in alternating order of presentation. Overall, readers find MT "fine", but prefer HT (slightly at excerpt-level 19/30, more clearly at chunk-level 522/772) for its ease, clarity, and immersive nature. Readers' highlights show that MT's quality varies more within one book than HT's does. Crucially, readers cannot reliably tell the two apart (17/30 guess correctly) and tend to prefer the version they believe to be human. Automatic metrics, including LLM-as-a-judge approaches, fail to recover reader preferences and favor MT. We release LAIT (Literary AI Translation), a reader-centered evaluation dataset with 1K reader comments, 2K judgments and preference ratings, and 7.2K span-level annotations, along with our evaluation protocol and supporting interface.
匹配关键词: alignment
---

[ACADEMIC - ARXIV]
标题: From Sparse and Imperfect 2D Anchors to Consistent 3D Gaussian Street Scenes: Support-Aware Appearance
作者: Long Cao, Zhongquan Wang, Jie Li, Yuhan Chen, Kefei Qian, Xiangfei Huang, Guofa Li
链接: https://arxiv.org/abs/2606.26007v1
完整摘要: Image priors can synthesize target conditions for 3D Gaussian street scenes, but independently edited views do not define a coherent 3D target. Direct fitting can propagate view-specific noise, while existing pipelines do not jointly handle imperfect sparse anchors and standard-rasterizer deployment. To address this gap, teacher-relative appearance residual distillation is introduced for appearance baking. A structured space for frequency decomposition, confidence estimation, and primitive-level lifting is formed by residuals between teacher anchors and original renders. The direct optimization signal is supplied by renderer-space matching, while primitive assignment is regularized by support-aware Gaussian-space aggregation. Supported detail is admitted and unsupported noise is suppressed through confidence-gated coarse-to-fine optimization, after which all residuals are baked into fixed-geometry spherical-harmonic coefficients. The teacher and auxiliary training modules are discarded at inference. Evaluation across Waymo street assets, Tanks and Temples scenes, and multiple target conditions shows a favorable overall balance of target alignment, content preservation, artifact suppression, and cross-view consistency over editing-based baselines. Ablations confirm the effectiveness of the main components. Code will be released at https://github.com/Cagares/Baking-for-3D-Gaussian.
匹配关键词: alignment
---

[ACADEMIC - ARXIV]
标题: Learning Action Priors for Cross-embodiment Robot Manipulation
作者: Dong Jing, Tianqi Zhang, Jiaqi Liu, Jinman Zhao, Zelong Sun, Li Erran Li, Zhiwu Lu, Mingyu Ding
链接: https://arxiv.org/abs/2606.26095v1
完整摘要: Most Vision-Language-Action (VLA) models build on a Vision-Language Model (VLM) backbone by attaching an action module and optimizing the full policy jointly. This design inherits strong visual and linguistic priors from the VLM, but leaves the action module to learn physical motion almost from scratch. As a result, the policy lacks an explicit motion prior, forcing early optimization to simultaneously discover temporal action dynamics and cross-modal alignment, a challenge further amplified in cross-embodiment settings. In this work, we propose to pretrain the action module with motion priors before cross-modal VLA alignment. Specifically, we introduce a two-stage training framework that equips the action module with cross-embodiment temporal motion structure before VLA training begins. In Stage~1, a lightweight flow-matching-based encoder-decoder action module efficiently learns temporal motion structure solely from unconditioned action trajectories, without processing visual or language tokens. In Stage~2, this learned prior is transferred to VLA training through decoder reuse and early-stage latent distillation, aligning visual-language features with the action embedding space while still allowing end-to-end policy refinement. In addition, the trained encoder serves as a compact history compressor, summarizing state-action histories into a single temporal context token for history-aware modeling at negligible cost. Extensive experiments across 13 diverse cross-embodiment tasks on both simulated and real-world platforms validate the effectiveness of our approach. Compared with VLA training without action priors, our model achieves faster convergence, higher success rates, and substantially stronger performance on data-scarce real-world tasks. Moreover, scaling up the action data in Stage~1 yields a more generalizable action prior that directly improves downstream VLA performance.
匹配关键词: preference learning
---

[ACADEMIC - ARXIV]
标题: RevengeBench: Reverse Engineering Code-Space Policies from Behavioral Experiments
作者: Babak Rahmani, Sebastian Dziadzio, Joschka Strüber, Sergio Hernández-Gutiérrez, Matthias Bethge
链接: https://arxiv.org/abs/2606.26094v1
完整摘要: For most of scientific history, researchers studying behavior could only infer hidden mechanisms from outward actions: an inverse problem that becomes more tractable when observation is augmented by targeted intervention. We pose a computational analogue: given only behavioral traces of an agent in a game environment, can a learner reconstruct the underlying decision program as executable code, and how much does this reconstruction improve with the ability to design controlled experiments? We introduce RevengeBench, a benchmark of 75 LLM generated, Elo-calibrated policies across five game environments, drawn from CodeClash tournament trajectories. The learner observes the hidden target policy play against sampled opponents and designs behavioral probes in the form of custom opponent policies that elicit informative behavior. It then submits an executable hypothesis, which is evaluated using continuous action-distance metrics. We further validate that recovered code carries informative signal in downstream player-versus-player tournaments. Across twelve frontier LLMs, recovery quality varies substantially (34 to 72% of initial distance closed), with reconstructed policies yielding measurable competitive advantage, particularly for weaker models that otherwise struggle to design effective counter-strategies. Our benchmark positions behavioral recovery of programmatic policies as a tractable inverse problem in code-space, opening a path to opponent modeling, policy interpretability, and the broader question of inferring latent mechanisms from observations.
匹配关键词: preference learning
---

[ACADEMIC - ARXIV]
标题: ForceBand: Learning Forceful Manipulation with sEMG
作者: Botao He, Zhi Wang, Linna Kuang, Ishaan Ghosh, Jitendra Malik, Cornelia Fermuller, Tingfan Wu, Jiayuan Mao, Ruoshi Liu, Haozhi Qi, Yiannis Aloimonos
链接: https://arxiv.org/abs/2606.26093v1
完整摘要: Human demonstrations are a scalable data source for learning robot manipulation policies. However, common sources of human demonstration data, such as motion-capture trajectories and internet videos, capture mostly motion and appearance while missing the contact forces that are critical for force-sensitive manipulation. In this paper, we introduce ForceBand, a low-cost wrist-worn sEMG system that turns human muscle activity into force-enriched demonstrations. We first collect a 10-hour multimodal dataset containing egocentric video, sEMG, IMU, and fingertip force measurements across diverse actions and objects. Using this dataset, we pre-train an EMG2Force model that predicts per-finger forces from sEMG and IMU signals. After a short user-specific calibration, users can collect target-task demonstrations using only ForceBand and video; EMG2Force then labels these demonstrations with per-finger force traces, producing force-augmented demonstrations for robot policy learning. Experiments show that ForceBand recovers fine-grained fingertip interactions with over 50% lower force prediction error than vision-based baselines and achieves an 87% success rate on pick, squeeze, and place tasks that require object-specific force control across objects with diverse shapes, sizes, and weights. Project website: https://forceband-emg.github.io
匹配关键词: preference learning
---

[ACADEMIC - ARXIV]
标题: On-Policy Self-Distillation with Sampled Demonstrations Reduces Output Diversity
作者: Andrei Liviu Nicolicioiu, Mohammad Pezeshki, Aaron Courville
链接: https://arxiv.org/abs/2606.26091v1
完整摘要: On-policy self-distillation achieves strong pass@1 accuracy by using a single model as both teacher and student, with the teacher conditioned on a correct demonstration to provide dense token-level feedback. We show that this could come at a hidden cost: rollout diversity decreases and pass@k curves flatten (i.e., generating more rollouts fails to improve accuracy). We trace this to compounding biases in the design of self-distillation with sampled demonstrations. The teacher scores each student rollout while conditioned on a sampled correct rollout, channeling its feedback through the model's own biases. We theoretically analyze the optimal self-distillation policy and show that it tilts the base distribution by a pointwise conditional mutual information score between the student's rollout and the correct rollout used as context. Unlike the ideal optimal on-policy reinforcement learning (RL), which preserves probability ratios among equally correct rollouts, self-distillation can amplify existing probability gaps, concentrating mass on already-dominant modes. On a controlled graph path-finding task and science question-answering benchmarks, self-distilled models match or exceed RL on average performance but exhibit substantially lower functional and semantic diversity, failing on out-of-distribution settings that require diverse strategies.
匹配关键词: preference learning
---

[ACADEMIC - ARXIV]
标题: Neglected Free Lunch from Post-training: Progress Advantage for LLM Agents
作者: Changdae Oh, Wendi Li, Seongheon Park, Samuel Yeh, Tanwi Mallick, Sharon Li
链接: https://arxiv.org/abs/2606.26080v1
完整摘要: Process reward models enable fine-grained, step-level evaluation of LLMs, yet building them for agentic settings remains prohibitively difficult: long-horizon interactions, irreversible actions, and stochastic environment feedback make both human annotation and Monte Carlo estimation infeasible at scale. In this work, we show that reinforcement learning (RL) post-training already provides the ingredients for effective step-level scoring, eliminating the need for dedicated reward model training altogether. Concretely, we derive an implicit advantage under a general stochastic Markov decision process, which we term progress advantage -- log-probability ratio between the RL-trained policy and its reference policy exactly recovers the optimal advantage function. This formulation makes the resulting signal annotation-free, domain-agnostic, and available as a byproduct of the standard RL post-training pipeline. We validate the effectiveness of the progress advantage across three different applications: test-time scaling, uncertainty quantification, and failure attribution on five benchmarks and four model families. Across all settings, it consistently outperforms confidence-based baselines and, despite requiring no task-specific training, surpasses dedicated trained reward models. We complement these results with deeper analyses on characteristics of progress advantage, offering practical guidance for adoption in real-world agentic systems.
匹配关键词: preference learning
---

[ACADEMIC - ARXIV]
标题: Learning Action Priors for Cross-embodiment Robot Manipulation
作者: Dong Jing, Tianqi Zhang, Jiaqi Liu, Jinman Zhao, Zelong Sun, Li Erran Li, Zhiwu Lu, Mingyu Ding
链接: https://arxiv.org/abs/2606.26095v1
完整摘要: Most Vision-Language-Action (VLA) models build on a Vision-Language Model (VLM) backbone by attaching an action module and optimizing the full policy jointly. This design inherits strong visual and linguistic priors from the VLM, but leaves the action module to learn physical motion almost from scratch. As a result, the policy lacks an explicit motion prior, forcing early optimization to simultaneously discover temporal action dynamics and cross-modal alignment, a challenge further amplified in cross-embodiment settings. In this work, we propose to pretrain the action module with motion priors before cross-modal VLA alignment. Specifically, we introduce a two-stage training framework that equips the action module with cross-embodiment temporal motion structure before VLA training begins. In Stage~1, a lightweight flow-matching-based encoder-decoder action module efficiently learns temporal motion structure solely from unconditioned action trajectories, without processing visual or language tokens. In Stage~2, this learned prior is transferred to VLA training through decoder reuse and early-stage latent distillation, aligning visual-language features with the action embedding space while still allowing end-to-end policy refinement. In addition, the trained encoder serves as a compact history compressor, summarizing state-action histories into a single temporal context token for history-aware modeling at negligible cost. Extensive experiments across 13 diverse cross-embodiment tasks on both simulated and real-world platforms validate the effectiveness of our approach. Compared with VLA training without action priors, our model achieves faster convergence, higher success rates, and substantially stronger performance on data-scarce real-world tasks. Moreover, scaling up the action data in Stage~1 yields a more generalizable action prior that directly improves downstream VLA performance.
匹配关键词: reward model
---

[ACADEMIC - ARXIV]
标题: RevengeBench: Reverse Engineering Code-Space Policies from Behavioral Experiments
作者: Babak Rahmani, Sebastian Dziadzio, Joschka Strüber, Sergio Hernández-Gutiérrez, Matthias Bethge
链接: https://arxiv.org/abs/2606.26094v1
完整摘要: For most of scientific history, researchers studying behavior could only infer hidden mechanisms from outward actions: an inverse problem that becomes more tractable when observation is augmented by targeted intervention. We pose a computational analogue: given only behavioral traces of an agent in a game environment, can a learner reconstruct the underlying decision program as executable code, and how much does this reconstruction improve with the ability to design controlled experiments? We introduce RevengeBench, a benchmark of 75 LLM generated, Elo-calibrated policies across five game environments, drawn from CodeClash tournament trajectories. The learner observes the hidden target policy play against sampled opponents and designs behavioral probes in the form of custom opponent policies that elicit informative behavior. It then submits an executable hypothesis, which is evaluated using continuous action-distance metrics. We further validate that recovered code carries informative signal in downstream player-versus-player tournaments. Across twelve frontier LLMs, recovery quality varies substantially (34 to 72% of initial distance closed), with reconstructed policies yielding measurable competitive advantage, particularly for weaker models that otherwise struggle to design effective counter-strategies. Our benchmark positions behavioral recovery of programmatic policies as a tractable inverse problem in code-space, opening a path to opponent modeling, policy interpretability, and the broader question of inferring latent mechanisms from observations.
匹配关键词: reward model
---

[ACADEMIC - ARXIV]
标题: ForceBand: Learning Forceful Manipulation with sEMG
作者: Botao He, Zhi Wang, Linna Kuang, Ishaan Ghosh, Jitendra Malik, Cornelia Fermuller, Tingfan Wu, Jiayuan Mao, Ruoshi Liu, Haozhi Qi, Yiannis Aloimonos
链接: https://arxiv.org/abs/2606.26093v1
完整摘要: Human demonstrations are a scalable data source for learning robot manipulation policies. However, common sources of human demonstration data, such as motion-capture trajectories and internet videos, capture mostly motion and appearance while missing the contact forces that are critical for force-sensitive manipulation. In this paper, we introduce ForceBand, a low-cost wrist-worn sEMG system that turns human muscle activity into force-enriched demonstrations. We first collect a 10-hour multimodal dataset containing egocentric video, sEMG, IMU, and fingertip force measurements across diverse actions and objects. Using this dataset, we pre-train an EMG2Force model that predicts per-finger forces from sEMG and IMU signals. After a short user-specific calibration, users can collect target-task demonstrations using only ForceBand and video; EMG2Force then labels these demonstrations with per-finger force traces, producing force-augmented demonstrations for robot policy learning. Experiments show that ForceBand recovers fine-grained fingertip interactions with over 50% lower force prediction error than vision-based baselines and achieves an 87% success rate on pick, squeeze, and place tasks that require object-specific force control across objects with diverse shapes, sizes, and weights. Project website: https://forceband-emg.github.io
匹配关键词: reward model
---

[ACADEMIC - ARXIV]
标题: On-Policy Self-Distillation with Sampled Demonstrations Reduces Output Diversity
作者: Andrei Liviu Nicolicioiu, Mohammad Pezeshki, Aaron Courville
链接: https://arxiv.org/abs/2606.26091v1
完整摘要: On-policy self-distillation achieves strong pass@1 accuracy by using a single model as both teacher and student, with the teacher conditioned on a correct demonstration to provide dense token-level feedback. We show that this could come at a hidden cost: rollout diversity decreases and pass@k curves flatten (i.e., generating more rollouts fails to improve accuracy). We trace this to compounding biases in the design of self-distillation with sampled demonstrations. The teacher scores each student rollout while conditioned on a sampled correct rollout, channeling its feedback through the model's own biases. We theoretically analyze the optimal self-distillation policy and show that it tilts the base distribution by a pointwise conditional mutual information score between the student's rollout and the correct rollout used as context. Unlike the ideal optimal on-policy reinforcement learning (RL), which preserves probability ratios among equally correct rollouts, self-distillation can amplify existing probability gaps, concentrating mass on already-dominant modes. On a controlled graph path-finding task and science question-answering benchmarks, self-distilled models match or exceed RL on average performance but exhibit substantially lower functional and semantic diversity, failing on out-of-distribution settings that require diverse strategies.
匹配关键词: reward model
---

[ACADEMIC - ARXIV]
标题: MVTrack4Gen: Multi-View Point Tracking as Geometric Supervision for 4D Video Generation
作者: JoungBin Lee, Jaewoo Jung, Jongmin Lee, Tongmin Kim, Hyunsung Kim, Takuya Narihira, Kazumi Fukuda, Jahyeok Koo, Jisang Han, Yuki Mitsufuji, Seungryong Kim
链接: https://arxiv.org/abs/2606.26087v1
完整摘要: Synthesizing a novel-view video from a monocular reference video along a target camera trajectory requires both geometric consistency and motion fidelity with respect to the reference video. Existing methods based on explicit 3D representations are limited by the accuracy of off-the-shelf reconstruction modules, which often produce inaccurate geometry for dynamic objects in monocular videos. In contrast, camera-conditioning-only methods can achieve high visual quality but often struggle to preserve geometric and motion consistency. In this work, we introduce MVTrack4Gen (Multi-View point Tracking for Novel-View Generation), a motion-aware training framework that leverages multi-view point tracking as an additional geometric and motion supervision signal for camera-conditioning-only novel-view video diffusion models. Our key finding is that specific attention layers encode strong correspondence cues, where query features attend to key features at geometrically corresponding locations across views and over time, and the misalignment of these correspondences causes motion inconsistency. Based on this observation, we route these features into an auxiliary multi-view tracking head and jointly train the diffusion model with a point-tracking objective. By explicitly strengthening these motion-aware correspondences, MVTrack4Gen improves existing models to better follow the motion in the reference view and maintain cross-view geometric consistency. Across diverse benchmarks, our method achieves state-of-the-art geometric consistency and competitive camera accuracy.
匹配关键词: reward model
---

[ACADEMIC - ARXIV]
标题: Real-Time Voice AI Hears but Does Not Listen
作者: Martijn Bartelds, Federico Bianchi, James Zou
链接: https://arxiv.org/abs/2606.26083v1
完整摘要: Speech conveys information through both words and vocal delivery. We evaluate four leading production realtime voice systems-OpenAI's GPT Realtime 2, Google's Gemini 3.1 Flash Live, and Alibaba's Qwen3.5 Omni Plus and Omni Flash-on tasks where the words and the delivery patterns both convey meaningful information. Across three consequential scenarios, all four systems act on the words rather than the voice. They end calls with crying callers who insist nothing is wrong, approve wire transfers authorized in frightened voices, and enroll callers whose agreement is clearly sarcastic. Surprisingly, this is often not a failure of perception. When asked directly, three of the four systems reliably identify the distress, fear, or sarcasm they later ignore when making decisions. We observe a similar pattern when these realtime voice systems estimate accent and age, as their responses frequently follow the biases of the words rather than the acoustic properties of the speaker. We term this disconnect between perception and action the emotional intelligence gap of voice AI. Prompting systems to explicitly attend to vocal delivery improves performance only partially and inconsistently. Our findings show that current realtime voice AI systems often behave as if speech had been reduced to a transcript, suggesting that they should be used with caution in settings where the tone and emotion of delivery convey important information.
匹配关键词: constitutional AI
---

[ACADEMIC - ARXIV]
标题: Same Evidence, Different Answer: Auditing Order Sensitivity in Multimodal Large Language Models
作者: Akshay Paruchuri, Sanmi Koyejo, Ehsan Adeli
链接: https://arxiv.org/abs/2606.26079v1
完整摘要: Standard benchmarks for multimodal large language models (MLLMs) score each item on one canonical ordering and miss whether order-irrelevant shuffling changes the answer, a baseline reliability property called for by emerging AI evaluation guidelines. We introduce Facet-Probe, a five-facet audit (option, evidence-chunk, document-rank, image-set, and mixed-modality ordering) of 18 frontier and open-weight MLLMs. A Bayesian item-response model separates ordering noise from per-facet bias, and a same-ordering control estimates the decoder-stochastic floor for observed flips. We find that none of the 18 MLLMs we audit are order-invariant: screened per-facet panel-mean flip rates span 24-50%. A Gemini same-ordering control at temperature 0 estimates a substantial ordering excess over a same-input decoder-noise floor in verified cells. Capability predicts but does not eliminate flips; the best model still flips on 13.4% of trials. In our Gemini mitigation tests, training-free prompt changes are modality-conditional and do not transfer from text to visual reasoning. These results suggest that prompt-level mitigation alone is unlikely to provide general order robustness, motivating future work on training-time and architectural approaches. We propose cross-ordering flip rate as a standard reporting axis for MLLMs.
匹配关键词: constitutional AI
---

[ACADEMIC - ARXIV]
标题: A welding penetration prediction model for laser welding process based on self-supervised learning using physics-informed neural networks
作者: Sen Li, Xiaoying Liu, Xiaojian Xu, Chendong Shao, Yaqi Wang, Ling Lan, Xinhua Tang, Haichao Cui
链接: https://arxiv.org/abs/2606.26059v1
完整摘要: The laser welding full-penetration is of critical importance, as it constitutes one of the fundamental factors in achieving defect-free welded joints. Accurate prediction of the penetration state is therefore essential for ensuring weld quality. To this end, this paper introduces SimPhysNet, a novel algorithm that achieves high classification accuracy in laser welding penetration prediction using only a limited number of labelled images. This approach effectively overcomes the limitations of supervised learning classification algorithms, which are hindered in industrial applications by their dependence on extensive, high-quality labelled data. The core of SimPhysNet is a unique self-supervised learning paradigm that embeds physical priors into a contrastive learning framework. By incorporating a physics-informed neural network (PINN), the model is guided to extract physically meaningful features of the molten pool and keyhole from a large set of unlabelled data, while three image augmentation tasks further enhance its generalization capabilities. Subsequently, a few-shot learning strategy, based on prototypical networks, enables robust classification by constructing class representations from a minimal set of labelled images. Experimental results demonstrate that SimPhysNet achieves a classification accuracy of 96.06% using only 200 labelled images (approximately 5% of the total labelled dataset), which is comparable to the performance of conventional supervised learning algorithms that utilize the entire labelled dataset. This work presents a new, efficient, and highly accurate method, providing the way for the intelligent automation of laser welding.
匹配关键词: constitutional AI
---

[ACADEMIC - ARXIV]
标题: The Unfireable Safety Kernel: Execution-Time AI Alignment for AI Agents and Other Escapable AI Systems
作者: Seth Dobrin, Łukasz Chmiel
链接: https://arxiv.org/abs/2606.26057v1
完整摘要: AI agents are granted access to tools, APIs, and other infrastructure, making them active principals in those systems. The dominant approach places controls inside the agent's own runtime: system prompts, output filters, and guardrail libraries. Any control in the agent's address space is reachable by inputs that influence it; this generalizes to any AI system with sufficient reach into its own runtime, a class we term escapable AI systems. We identify four properties that an authorization mechanism must satisfy for architectural control rather than for cooperative requests: process separation, pre-action enforcement on a structurally only path, fail-closed at both the request and system levels, and externalized signed evidence verifiable outside the controlled system's trust boundary. We position this layer as execution-time AI alignment, complementing training-time alignment (RLHF, Constitutional AI) and inference-time alignment. We present the Unfireable Safety Kernel, a Rust reference implementation realizing all four. Its fail-closed invariant is machine-checked at two levels: an SMT theorem (Z3) and an exhaustive bounded-model-checking proof of the production decision function (Kani, 4/4 harnesses). A Python-to-Rust migration was gated on byte-equivalence (1000/1000 fixtures; 17/17 adversarial classes). We evaluate the kernel governing a live, escapable AI system, a deterministic, self-improving world model, against an escape-seeking adversary driving its real self-modification seam: across 1,000 self-modifications, all 704 attempts on the safety-critical core are refused, with no escape; a further 300, under the operator kill switch, are also refused. A separate campaign of 6,240 authorization round-trips had no successful bypass. Against 3 contemporary systems claiming the agent control plane, the agent invokes control; here, it lacks that choice.
匹配关键词: constitutional AI
---

[ACADEMIC - ARXIV]
标题: AI translation of literary texts is "fine", but readers still prefer human translations
作者: Yves Ferstler, Adam Podoxin, Ty Brassington, Roman Grundkiewicz, Maite Taboada, Marzena Karpinska
链接: https://arxiv.org/abs/2606.26040v1
完整摘要: AI translation of literary works is increasingly common. While the content may be rendered adequately, we do not know enough about how readers experience it in terms of immersiveness and literary effect, aspects poorly captured by automatic machine translation metrics or human evaluation targeting fluency and adequacy. We ask 15 avid readers to compare recently published human translations (HT) to machine translations (MT) generated with an agentic large language model (LLM)-based pipeline, for 15 recent novels in French, Polish, and Japanese and translated into English. Readers evaluated approximately 8K-word excerpts in two conditions: immersive reading of the whole excerpt (30 comparisons) and close reading of 386 aligned HT-MT chunk pairs (772 comparisons), with two readers per book and in alternating order of presentation. Overall, readers find MT "fine", but prefer HT (slightly at excerpt-level 19/30, more clearly at chunk-level 522/772) for its ease, clarity, and immersive nature. Readers' highlights show that MT's quality varies more within one book than HT's does. Crucially, readers cannot reliably tell the two apart (17/30 guess correctly) and tend to prefer the version they believe to be human. Automatic metrics, including LLM-as-a-judge approaches, fail to recover reader preferences and favor MT. We release LAIT (Literary AI Translation), a reader-centered evaluation dataset with 1K reader comments, 2K judgments and preference ratings, and 7.2K span-level annotations, along with our evaluation protocol and supporting interface.
匹配关键词: constitutional AI
---

[ACADEMIC - ARXIV]
标题: Tracing Target Answers in Poisoned Retrieval Corpora via Token Influence Attribution
作者: Yan-Lun Chen, Pin-Yu Chen, Chia-Mu Yu, Ying-Dar Lin, Yu-Sung Wu, Wei-Bin Lee
链接: https://arxiv.org/abs/2606.25721v1
完整摘要: Retrieval-Augmented Generation (RAG) systems are vulnerable to corpus poisoning attacks that manipulate model outputs through malicious retrieved documents. Existing detection methods typically rely on auxiliary classifiers or additional LLM-based verification, introducing substantial computational overhead. We present TRACE, a lightweight detection framework that identifies poisoning attacks by tracing answer-related tokens through token influence attribution. TRACE first discovers recurrent high-influence keywords across retrieved documents and then performs a secondary verification to confirm their influence on model predictions. Experiments on three QA benchmarks and six LLMs demonstrate strong detection performance while simultaneously uncovering attacker-specified target answers.
匹配关键词: RAG
---

[ACADEMIC - ARXIV]
标题: Is GraphRAG Needed? From Basic RAG to Graph-/Agentic Solutions with Context Optimization
作者: Long Chen, Ryan Razkenari, Yuxuan Zhou, Yuan Tian, Rahul Ghosh, Venkatesh Pappakrishnan, Disha Ahuja, Vidya Sagar Ravipati
链接: https://arxiv.org/abs/2606.25656v1
完整摘要: As advanced RAG variants like GraphRAG and Agentic RAG emerge, one leading question is when and how to use them. Here, we introduce a framework for different RAG scenarios evaluation and comparison on semi-structured knowledge bases, including regular RAG, GraphRAG, Modular RAG and Agentic RAG. We provide implementation for 9 standardized RAG scenarios, and conduct experiments for a comprehensive comparison. These scenarios are designed for real use cases regarding data and domain restrictions, spanning from simple document-based retrieval to advanced features such as hybrid text-graph retrieval, integration with computed or pre-defined domain knowledge graphs, agentic multi-step planning, and agent-graph integration. Besides, we present a novel context engineering method for GraphRAG and Agentic RAG, addressing the context/memory overflow issues, efficiently managing text and graph retrievals with new representations and agentic loop design, leading to 19%-53% reduction on token usage. Moreover, further analysis identifies a retrieval-generation gap where expanded retrieval does not proportionally improve generation quality, suggesting retrieval-oriented metrics overstate advanced retrieval benefits. This work provides data-driven insights on when and how to use them for building production-ready intelligent RAG systems.
匹配关键词: RAG
---

[ACADEMIC - ARXIV]
标题: Security and Privacy in Retrieval-Augmented Generation: Architectures, Threats, Defenses, and Future Directions for Building Trustworthy Systems
作者: Balamurugan Palanisamy, G S S Chalapathi, Vikas Hassija, Rajkumar Buyya
链接: https://arxiv.org/abs/2606.25533v1
完整摘要: Retrieval-Augmented Generation (RAG) has emerged as a dominant paradigm for enhancing large language models with external knowledge. By coupling retrieval mechanisms with generative models, RAG systems improve factual grounding and adaptability across domains. However, integrating retrieval pipelines introduces new security and privacy risks that extend beyond conventional language modeling threats. Sensitive information may be exposed through retrieval indices, query logs, context construction, or federated updates, while adversarial manipulation of knowledge bases can undermine trust in generated outputs. This survey provides a comprehensive examination of privacy and security challenges across RAG systems deployed in centralized, on-device (Micro-RAG), federated, and hybrid paradigms. We present a unified taxonomy of threat surfaces spanning the retrieval, context construction, and generation stages and systematically analyze attack classes, including membership inference, index inference, poisoning, gradient leakage, and collusion. We further review architectural, algorithmic, and cryptographic defenses, highlighting privacy-utility trade-offs and deployment considerations. Finally, we outline open research challenges toward building trustworthy, secure, and resilient RAG systems for real-world applications.
匹配关键词: RAG
---

[ACADEMIC - ARXIV]
标题: Memory Makes the Difference: Evaluating How Different Memory Roles Shape Conversational Agents
作者: Yuxin Wang, Paul Thomas, Zhiwei Yu, Yuan Gao, Saeed Hassanpour, Soroush Vosoughi, Robert Sim, Nick Craswell
链接: https://arxiv.org/abs/2606.25361v1
完整摘要: Prior research on memory mechanism in RAG-based conversational system has emphasized how memory is stored and retrieved. However, far less is known about how memories with different functional roles influence response quality. Specifically, how they shape an agent's responses under varying conversational contexts and whether they lead to substantively different response behaviors. Existing evaluations in conversational system are also largely reference-based, insufficiently capturing the nuances in responses that may address users' preferences differently. In this work, we probe the impact of different memory types in shaping agents' responses. We present a fine-grained taxonomy of conversational memory, classify retrieved memories into different role types, and design a user-centric evaluation framework that simulates user perspectives. Through comparative experiments on long-term datasets and frontier LLMs, our analysis reveal many differentiated effects of memories: e.g., clarifying memory improves responses' factual accuracy and constraint awareness, making them more correct and personalized; irrelevant memory reduces topic relevance and degrades constraint awareness. Despite the power of frontier LLMs, these findings shed light on how different memory types can be leveraged to produce more personalized responses and inspire further research in this direction.
匹配关键词: RAG
---

[ACADEMIC - ARXIV]
标题: Invoice Haystack: Benchmarking Document Retrieval and Visual Question Answering Under Strong Visual Homogeneity
作者: Heethanjan Kanagalingam, Thenukan Pathmanathan, Mokeeshan Vathanakumar, Basim Azam, Sarah Monazam Erfani
链接: https://arxiv.org/abs/2606.25343v1
完整摘要: Vision Language Models have achieved near-human performance on single-document Visual Question Answering, yet their effectiveness degrades significantly when retrieving information from large collections of visually homogeneous documents. Existing multi-document benchmarks aggregate diverse document types, creating artificial separation in embedding space that does not reflect enterprise document repositories where thousands of records share identical visual templates. We identify this as embedding collapse and introduce Invoice Haystack, a benchmark with 1,500 anonymized invoice images paired with 200 discriminative question-answer pairs, specifically designed to stress-test retrieval under strong visual homogeneity. Invoice Haystack exhibits a mean pairwise cosine similarity of 0.73, compared to 0.38 (DocHaystack) and 0.31 (InfoHaystack) in existing benchmarks, posing a fundamentally more challenging retrieval problem. Addressing the identified challenge, we propose VL-RAG, a hybrid retrieval-augmented generation framework that jointly leverages text and visual embeddings to harness the complementary strengths of both modalities, followed by a VLM-based verification filter for precise document identification. VL-RAG achieves 60.0\% Recall@1 on Invoice Haystack-500, outperforming existing state-of-the-art method by up to an absolute 13.5 percentage points. It further improves retrieval considerably on DocHaystack-1000 (77.1\% vs.\ 75.2\%) and InfoHaystack-1000 (84.5\% vs.\ 80.0\%), establishing the proposed dual-stream fusion as a consistently superior retrieval strategy across both homogeneous and heterogeneous document collections.
匹配关键词: RAG
---

[ACADEMIC - ARXIV]
标题: RevengeBench: Reverse Engineering Code-Space Policies from Behavioral Experiments
作者: Babak Rahmani, Sebastian Dziadzio, Joschka Strüber, Sergio Hernández-Gutiérrez, Matthias Bethge
链接: https://arxiv.org/abs/2606.26094v1
完整摘要: For most of scientific history, researchers studying behavior could only infer hidden mechanisms from outward actions: an inverse problem that becomes more tractable when observation is augmented by targeted intervention. We pose a computational analogue: given only behavioral traces of an agent in a game environment, can a learner reconstruct the underlying decision program as executable code, and how much does this reconstruction improve with the ability to design controlled experiments? We introduce RevengeBench, a benchmark of 75 LLM generated, Elo-calibrated policies across five game environments, drawn from CodeClash tournament trajectories. The learner observes the hidden target policy play against sampled opponents and designs behavioral probes in the form of custom opponent policies that elicit informative behavior. It then submits an executable hypothesis, which is evaluated using continuous action-distance metrics. We further validate that recovered code carries informative signal in downstream player-versus-player tournaments. Across twelve frontier LLMs, recovery quality varies substantially (34 to 72% of initial distance closed), with reconstructed policies yielding measurable competitive advantage, particularly for weaker models that otherwise struggle to design effective counter-strategies. Our benchmark positions behavioral recovery of programmatic policies as a tractable inverse problem in code-space, opening a path to opponent modeling, policy interpretability, and the broader question of inferring latent mechanisms from observations.
匹配关键词: code generation
---

[ACADEMIC - ARXIV]
标题: On-Policy Self-Distillation with Sampled Demonstrations Reduces Output Diversity
作者: Andrei Liviu Nicolicioiu, Mohammad Pezeshki, Aaron Courville
链接: https://arxiv.org/abs/2606.26091v1
完整摘要: On-policy self-distillation achieves strong pass@1 accuracy by using a single model as both teacher and student, with the teacher conditioned on a correct demonstration to provide dense token-level feedback. We show that this could come at a hidden cost: rollout diversity decreases and pass@k curves flatten (i.e., generating more rollouts fails to improve accuracy). We trace this to compounding biases in the design of self-distillation with sampled demonstrations. The teacher scores each student rollout while conditioned on a sampled correct rollout, channeling its feedback through the model's own biases. We theoretically analyze the optimal self-distillation policy and show that it tilts the base distribution by a pointwise conditional mutual information score between the student's rollout and the correct rollout used as context. Unlike the ideal optimal on-policy reinforcement learning (RL), which preserves probability ratios among equally correct rollouts, self-distillation can amplify existing probability gaps, concentrating mass on already-dominant modes. On a controlled graph path-finding task and science question-answering benchmarks, self-distilled models match or exceed RL on average performance but exhibit substantially lower functional and semantic diversity, failing on out-of-distribution settings that require diverse strategies.
匹配关键词: code generation
---

[ACADEMIC - ARXIV]
标题: MVTrack4Gen: Multi-View Point Tracking as Geometric Supervision for 4D Video Generation
作者: JoungBin Lee, Jaewoo Jung, Jongmin Lee, Tongmin Kim, Hyunsung Kim, Takuya Narihira, Kazumi Fukuda, Jahyeok Koo, Jisang Han, Yuki Mitsufuji, Seungryong Kim
链接: https://arxiv.org/abs/2606.26087v1
完整摘要: Synthesizing a novel-view video from a monocular reference video along a target camera trajectory requires both geometric consistency and motion fidelity with respect to the reference video. Existing methods based on explicit 3D representations are limited by the accuracy of off-the-shelf reconstruction modules, which often produce inaccurate geometry for dynamic objects in monocular videos. In contrast, camera-conditioning-only methods can achieve high visual quality but often struggle to preserve geometric and motion consistency. In this work, we introduce MVTrack4Gen (Multi-View point Tracking for Novel-View Generation), a motion-aware training framework that leverages multi-view point tracking as an additional geometric and motion supervision signal for camera-conditioning-only novel-view video diffusion models. Our key finding is that specific attention layers encode strong correspondence cues, where query features attend to key features at geometrically corresponding locations across views and over time, and the misalignment of these correspondences causes motion inconsistency. Based on this observation, we route these features into an auxiliary multi-view tracking head and jointly train the diffusion model with a point-tracking objective. By explicitly strengthening these motion-aware correspondences, MVTrack4Gen improves existing models to better follow the motion in the reference view and maintain cross-view geometric consistency. Across diverse benchmarks, our method achieves state-of-the-art geometric consistency and competitive camera accuracy.
匹配关键词: code generation
---

[ACADEMIC - ARXIV]
标题: Neglected Free Lunch from Post-training: Progress Advantage for LLM Agents
作者: Changdae Oh, Wendi Li, Seongheon Park, Samuel Yeh, Tanwi Mallick, Sharon Li
链接: https://arxiv.org/abs/2606.26080v1
完整摘要: Process reward models enable fine-grained, step-level evaluation of LLMs, yet building them for agentic settings remains prohibitively difficult: long-horizon interactions, irreversible actions, and stochastic environment feedback make both human annotation and Monte Carlo estimation infeasible at scale. In this work, we show that reinforcement learning (RL) post-training already provides the ingredients for effective step-level scoring, eliminating the need for dedicated reward model training altogether. Concretely, we derive an implicit advantage under a general stochastic Markov decision process, which we term progress advantage -- log-probability ratio between the RL-trained policy and its reference policy exactly recovers the optimal advantage function. This formulation makes the resulting signal annotation-free, domain-agnostic, and available as a byproduct of the standard RL post-training pipeline. We validate the effectiveness of the progress advantage across three different applications: test-time scaling, uncertainty quantification, and failure attribution on five benchmarks and four model families. Across all settings, it consistently outperforms confidence-based baselines and, despite requiring no task-specific training, surpasses dedicated trained reward models. We complement these results with deeper analyses on characteristics of progress advantage, offering practical guidance for adoption in real-world agentic systems.
匹配关键词: code generation
---

[ACADEMIC - ARXIV]
标题: Same Evidence, Different Answer: Auditing Order Sensitivity in Multimodal Large Language Models
作者: Akshay Paruchuri, Sanmi Koyejo, Ehsan Adeli
链接: https://arxiv.org/abs/2606.26079v1
完整摘要: Standard benchmarks for multimodal large language models (MLLMs) score each item on one canonical ordering and miss whether order-irrelevant shuffling changes the answer, a baseline reliability property called for by emerging AI evaluation guidelines. We introduce Facet-Probe, a five-facet audit (option, evidence-chunk, document-rank, image-set, and mixed-modality ordering) of 18 frontier and open-weight MLLMs. A Bayesian item-response model separates ordering noise from per-facet bias, and a same-ordering control estimates the decoder-stochastic floor for observed flips. We find that none of the 18 MLLMs we audit are order-invariant: screened per-facet panel-mean flip rates span 24-50%. A Gemini same-ordering control at temperature 0 estimates a substantial ordering excess over a same-input decoder-noise floor in verified cells. Capability predicts but does not eliminate flips; the best model still flips on 13.4% of trials. In our Gemini mitigation tests, training-free prompt changes are modality-conditional and do not transfer from text to visual reasoning. These results suggest that prompt-level mitigation alone is unlikely to provide general order robustness, motivating future work on training-time and architectural approaches. We propose cross-ordering flip rate as a standard reporting axis for MLLMs.
匹配关键词: code generation
---

[ACADEMIC - ARXIV]
标题: RevengeBench: Reverse Engineering Code-Space Policies from Behavioral Experiments
作者: Babak Rahmani, Sebastian Dziadzio, Joschka Strüber, Sergio Hernández-Gutiérrez, Matthias Bethge
链接: https://arxiv.org/abs/2606.26094v1
完整摘要: For most of scientific history, researchers studying behavior could only infer hidden mechanisms from outward actions: an inverse problem that becomes more tractable when observation is augmented by targeted intervention. We pose a computational analogue: given only behavioral traces of an agent in a game environment, can a learner reconstruct the underlying decision program as executable code, and how much does this reconstruction improve with the ability to design controlled experiments? We introduce RevengeBench, a benchmark of 75 LLM generated, Elo-calibrated policies across five game environments, drawn from CodeClash tournament trajectories. The learner observes the hidden target policy play against sampled opponents and designs behavioral probes in the form of custom opponent policies that elicit informative behavior. It then submits an executable hypothesis, which is evaluated using continuous action-distance metrics. We further validate that recovered code carries informative signal in downstream player-versus-player tournaments. Across twelve frontier LLMs, recovery quality varies substantially (34 to 72% of initial distance closed), with reconstructed policies yielding measurable competitive advantage, particularly for weaker models that otherwise struggle to design effective counter-strategies. Our benchmark positions behavioral recovery of programmatic policies as a tractable inverse problem in code-space, opening a path to opponent modeling, policy interpretability, and the broader question of inferring latent mechanisms from observations.
匹配关键词: benchmark
---

[ACADEMIC - ARXIV]
标题: On-Policy Self-Distillation with Sampled Demonstrations Reduces Output Diversity
作者: Andrei Liviu Nicolicioiu, Mohammad Pezeshki, Aaron Courville
链接: https://arxiv.org/abs/2606.26091v1
完整摘要: On-policy self-distillation achieves strong pass@1 accuracy by using a single model as both teacher and student, with the teacher conditioned on a correct demonstration to provide dense token-level feedback. We show that this could come at a hidden cost: rollout diversity decreases and pass@k curves flatten (i.e., generating more rollouts fails to improve accuracy). We trace this to compounding biases in the design of self-distillation with sampled demonstrations. The teacher scores each student rollout while conditioned on a sampled correct rollout, channeling its feedback through the model's own biases. We theoretically analyze the optimal self-distillation policy and show that it tilts the base distribution by a pointwise conditional mutual information score between the student's rollout and the correct rollout used as context. Unlike the ideal optimal on-policy reinforcement learning (RL), which preserves probability ratios among equally correct rollouts, self-distillation can amplify existing probability gaps, concentrating mass on already-dominant modes. On a controlled graph path-finding task and science question-answering benchmarks, self-distilled models match or exceed RL on average performance but exhibit substantially lower functional and semantic diversity, failing on out-of-distribution settings that require diverse strategies.
匹配关键词: benchmark
---

[ACADEMIC - ARXIV]
标题: MVTrack4Gen: Multi-View Point Tracking as Geometric Supervision for 4D Video Generation
作者: JoungBin Lee, Jaewoo Jung, Jongmin Lee, Tongmin Kim, Hyunsung Kim, Takuya Narihira, Kazumi Fukuda, Jahyeok Koo, Jisang Han, Yuki Mitsufuji, Seungryong Kim
链接: https://arxiv.org/abs/2606.26087v1
完整摘要: Synthesizing a novel-view video from a monocular reference video along a target camera trajectory requires both geometric consistency and motion fidelity with respect to the reference video. Existing methods based on explicit 3D representations are limited by the accuracy of off-the-shelf reconstruction modules, which often produce inaccurate geometry for dynamic objects in monocular videos. In contrast, camera-conditioning-only methods can achieve high visual quality but often struggle to preserve geometric and motion consistency. In this work, we introduce MVTrack4Gen (Multi-View point Tracking for Novel-View Generation), a motion-aware training framework that leverages multi-view point tracking as an additional geometric and motion supervision signal for camera-conditioning-only novel-view video diffusion models. Our key finding is that specific attention layers encode strong correspondence cues, where query features attend to key features at geometrically corresponding locations across views and over time, and the misalignment of these correspondences causes motion inconsistency. Based on this observation, we route these features into an auxiliary multi-view tracking head and jointly train the diffusion model with a point-tracking objective. By explicitly strengthening these motion-aware correspondences, MVTrack4Gen improves existing models to better follow the motion in the reference view and maintain cross-view geometric consistency. Across diverse benchmarks, our method achieves state-of-the-art geometric consistency and competitive camera accuracy.
匹配关键词: benchmark
---

[ACADEMIC - ARXIV]
标题: Neglected Free Lunch from Post-training: Progress Advantage for LLM Agents
作者: Changdae Oh, Wendi Li, Seongheon Park, Samuel Yeh, Tanwi Mallick, Sharon Li
链接: https://arxiv.org/abs/2606.26080v1
完整摘要: Process reward models enable fine-grained, step-level evaluation of LLMs, yet building them for agentic settings remains prohibitively difficult: long-horizon interactions, irreversible actions, and stochastic environment feedback make both human annotation and Monte Carlo estimation infeasible at scale. In this work, we show that reinforcement learning (RL) post-training already provides the ingredients for effective step-level scoring, eliminating the need for dedicated reward model training altogether. Concretely, we derive an implicit advantage under a general stochastic Markov decision process, which we term progress advantage -- log-probability ratio between the RL-trained policy and its reference policy exactly recovers the optimal advantage function. This formulation makes the resulting signal annotation-free, domain-agnostic, and available as a byproduct of the standard RL post-training pipeline. We validate the effectiveness of the progress advantage across three different applications: test-time scaling, uncertainty quantification, and failure attribution on five benchmarks and four model families. Across all settings, it consistently outperforms confidence-based baselines and, despite requiring no task-specific training, surpasses dedicated trained reward models. We complement these results with deeper analyses on characteristics of progress advantage, offering practical guidance for adoption in real-world agentic systems.
匹配关键词: benchmark
---

[ACADEMIC - ARXIV]
标题: Same Evidence, Different Answer: Auditing Order Sensitivity in Multimodal Large Language Models
作者: Akshay Paruchuri, Sanmi Koyejo, Ehsan Adeli
链接: https://arxiv.org/abs/2606.26079v1
完整摘要: Standard benchmarks for multimodal large language models (MLLMs) score each item on one canonical ordering and miss whether order-irrelevant shuffling changes the answer, a baseline reliability property called for by emerging AI evaluation guidelines. We introduce Facet-Probe, a five-facet audit (option, evidence-chunk, document-rank, image-set, and mixed-modality ordering) of 18 frontier and open-weight MLLMs. A Bayesian item-response model separates ordering noise from per-facet bias, and a same-ordering control estimates the decoder-stochastic floor for observed flips. We find that none of the 18 MLLMs we audit are order-invariant: screened per-facet panel-mean flip rates span 24-50%. A Gemini same-ordering control at temperature 0 estimates a substantial ordering excess over a same-input decoder-noise floor in verified cells. Capability predicts but does not eliminate flips; the best model still flips on 13.4% of trials. In our Gemini mitigation tests, training-free prompt changes are modality-conditional and do not transfer from text to visual reasoning. These results suggest that prompt-level mitigation alone is unlikely to provide general order robustness, motivating future work on training-time and architectural approaches. We propose cross-ordering flip rate as a standard reporting axis for MLLMs.
匹配关键词: benchmark
---

[ACADEMIC - ARXIV]
标题: Model Forensics: Investigating Whether Concerning Behavior Reflects Misalignment
作者: Aditya Singh, Gerson Kroiz, Senthooran Rajamanoharan, Neel Nanda
链接: https://arxiv.org/abs/2606.26071v1
完整摘要: A central goal of safety research is determining whether a model is misaligned. Prior work has largely focused on detecting concerning behavior. But behavior alone does not establish misalignment: a concerning action can arise from benign causes such as confusion. This motivates model forensics: investigating whether the action was driven by malign intent. In this paper, we propose a baseline protocol for model forensics consisting of two steps, iterated as needed. First, we read the chain of thought (CoT) to generate hypotheses about what drives model behavior. Second, we make edits to the prompt or environment to test these hypotheses. While the CoT is not always faithful, it is a rich source of unsupervised insight that can guide the collection of more rigorous evidence. To evaluate our protocol, we create a suite of six agentic environments where models exhibit concerning behavior, and apply it to each. We establish that Kimi K2 Thinking takes shortcuts due to a genuine disposition towards low-effort actions, by showing this hypothesis successfully predicts its behavior. Through counterfactual experiments, we show DeepSeek R1 deceives out of a desire to be consistent with a previous instance of itself. Our methods nonetheless leave significant room for refinement. For example, when we test whether Kimi K2 Thinking believes it is violating user intent, we find no evidence of such a belief, but without positive controls we cannot confirm our tests would detect it. Overall, we find our simple protocol provides a strong baseline that we hope future work will improve upon. More broadly, our work is a concrete step in developing the growing field of model forensics.
匹配关键词: safety
---

[ACADEMIC - ARXIV]
标题: The Unfireable Safety Kernel: Execution-Time AI Alignment for AI Agents and Other Escapable AI Systems
作者: Seth Dobrin, Łukasz Chmiel
链接: https://arxiv.org/abs/2606.26057v1
完整摘要: AI agents are granted access to tools, APIs, and other infrastructure, making them active principals in those systems. The dominant approach places controls inside the agent's own runtime: system prompts, output filters, and guardrail libraries. Any control in the agent's address space is reachable by inputs that influence it; this generalizes to any AI system with sufficient reach into its own runtime, a class we term escapable AI systems. We identify four properties that an authorization mechanism must satisfy for architectural control rather than for cooperative requests: process separation, pre-action enforcement on a structurally only path, fail-closed at both the request and system levels, and externalized signed evidence verifiable outside the controlled system's trust boundary. We position this layer as execution-time AI alignment, complementing training-time alignment (RLHF, Constitutional AI) and inference-time alignment. We present the Unfireable Safety Kernel, a Rust reference implementation realizing all four. Its fail-closed invariant is machine-checked at two levels: an SMT theorem (Z3) and an exhaustive bounded-model-checking proof of the production decision function (Kani, 4/4 harnesses). A Python-to-Rust migration was gated on byte-equivalence (1000/1000 fixtures; 17/17 adversarial classes). We evaluate the kernel governing a live, escapable AI system, a deterministic, self-improving world model, against an escape-seeking adversary driving its real self-modification seam: across 1,000 self-modifications, all 704 attempts on the safety-critical core are refused, with no escape; a further 300, under the operator kill switch, are also refused. A separate campaign of 6,240 authorization round-trips had no successful bypass. Against 3 contemporary systems claiming the agent control plane, the agent invokes control; here, it lacks that choice.
匹配关键词: safety
---

[ACADEMIC - ARXIV]
标题: G2DP: Diffusion Planning with Spatio-Temporal Grid Guidance
作者: Hang Yu, Ye Jin, Alessandro Canevaro, Julian Schmidt, Julian Jordan, Peizheng Li, Marc Kaufeld, Silvan Lindner, Johannes Betz, Wilhelm Stork
链接: https://arxiv.org/abs/2606.26017v1
完整摘要: In autonomous driving, diffusion-based planners have emerged as a promising paradigm for robust motion planning in dense and interactive traffic, as they can effectively model diverse driving behaviors. However, their inherent stochasticity often requires explicit guidance during denoising to ensure safety and route adherence for robust closed-loop execution. Existing guidance typically relies on sparse, entity-centric geometric queries or post-hoc refinement, yielding limited situational awareness and fragile performance in interactive scenes. To address this issue, we propose G2DP (Grid-Guided Diffusion Planning), a diffusion-based planner that directly enforces dense environmental constraints through inference-time guidance. Specifically, G2DP constructs a differentiable spatio-temporal cost volume by fusing probabilistic future occupancy distributions with a route-progress map. By formulating this volume as a continuous safety energy functional, it injects dense gradients directly into the denoising loop, actively steering trajectory generation toward collision-free and progress-optimal regions. Extensive closed-loop evaluations show that G2DP achieves state-of-the-art performance on nuPlan, outperforming the strongest imitation-learning baseline by +7.2 points in reactive score. It further maintains top scores in zero-shot transfers to interPlan and DeepScenario benchmarks, with collision avoidance improving by +10.15 over the unguided approach on interPlan. These results demonstrate that spatio-temporal cost grids serve as an effective representation for robust guidance in diffusion-based planning.
匹配关键词: safety
---

[ACADEMIC - ARXIV]
标题: The Tatoxa System for Text Detoxification in Low-Resource Languages: The Case of Tatar
作者: Ilseyar Alimova, Bogdan Monogov, Artyom Mazur, Daniil Antonov, Vsevolod Karimov, Vitaliy Egorov, Bulat Khakimov, Alexander Panchenko
链接: https://arxiv.org/abs/2606.26015v1
完整摘要: Text detoxification, the automated detection and mitigation of abusive and harmful content, is essential for ensuring the safety of online communities and protecting users. However, low resource languages such as Tatar have received little research attention. In this paper we present Tatoxa, a novel state-of-the-art system for text detoxification in the Tatar language. Comparative experiments show that the proposed approach outperforms existing open source and proprietary commercial LLMs on key quality metrics. We also introduce a new dataset for text detoxification in Tatar, designed for fine tuning and evaluation in low resource settings. Finally, cross lingual transfer experiments indicate that transfer from other languages, including the culturally close Russian, performs significantly worse than training on native Tatar data even when a large Russian corpus is available.
匹配关键词: safety
---

[ACADEMIC - ARXIV]
标题: SpeechEQ: Benchmarking Emotional Intelligence Quotient in Socially Aware Voice Conversational Models
作者: Liang-Yuan Wu, Zih-Ching Chen, Tongshuang Wu, Chao-Han Huck Yang, Hua Shen
链接: https://arxiv.org/abs/2606.25990v1
完整摘要: As multimodal conversational systems increasingly engage in spoken interaction, their ability to navigate paralinguistic social cues has become a critical bottleneck for natural human-AI communication. However, existing evaluations of machine emotional intelligence assess reasoning exclusively through isolated text or passive acoustic perception, overlooking the complex cross-modal reasoning required for active, multi-turn dialogue. We introduce \textsc{SpeechEQ}, a comprehensive framework designed to evaluate the sociolinguistic reasoning of Speech-Language Models (SLMs). The framework includes a validated dataset of 2,265 dialogues across 15 Emotional Quotient (EQ) subscales grounded in EQ-i 2.0 theory, along with a multi-turn evaluation protocol measured by our proposed Spoken EQ (SEQ) score inspired by human EQ assessments. Experiments show limitations in how both existing Speech Emotion Recognition and end-to-end Speech-Language Models understand and apply paralinguistic cues through speech. While end-to-end architectures outperform cascaded systems, \textsc{SpeechEQ} reveals that current multimodal models remain bottlenecked by a text-reliant ``modality shortcut,'' an alignment-induced ``safety trap,'' and ``contextual amnesia,'' highlighting the barriers to truly emotionally aware AI. Our benchmark can be accessed at https://huggingface.co/datasets/SpeechEQ/SpeechEQ and demo page at https://binomial14.github.io/speecheq-demo/
匹配关键词: safety
---

