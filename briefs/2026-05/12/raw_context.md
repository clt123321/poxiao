# 破晓 PoXiao — 原始数据 (Raw Context)
生成时间: 2026-05-12 02:45 UTC
================================================================================

[RSS:Reddit LocalLLaMA (社区共识)]
Computer build using Intel Optane Persistent Memory - Can run 1 trillion parameter model at over 4 tokens/sec
https://www.reddit.com/r/LocalLLaMA/comments/1taeg8h/computer_build_using_intel_optane_persistent/
As the title states, my build is indeed able to run a 1 trillion parameter model (in this case Kimi K2.5) locally at ~4 tokens/second. I thought r/LocalLLaMA would be interested in the build due to that stat line, and also due to the inclusion of an unusual part, Intel Optane Persistent Memory, whic
---

[RSS:Reddit LocalLLaMA (社区共识)]
MTP on Unsloth
https://www.reddit.com/r/LocalLLaMA/comments/1ta4rvs/mtp_on_unsloth/
https://huggingface.co/unsloth/Qwen3.6-27B-GGUF-MTP https://huggingface.co/unsloth/Qwen3.6-35B-A3B-GGUF-MTP Unsloth release the model with preserved MTP layer, but you still have to checkout and build llamacpp pr about MTP. just open HF link, Unsloth give the instruction how to use MTP in the model 
---

[RSS:Reddit LocalLLaMA (社区共识)]
Found a way to cool the DGX
https://www.reddit.com/r/LocalLLaMA/comments/1tansuo/found_a_way_to_cool_the_dgx/
Tap water keeps the temperature below 68 degree Celsius at 95% GPU utilization running Qwen3.5-122b-a10B Q6_K precision. 110 GB Memory usage, 80k context window, 18.77 tokens/second for continuous vision analyses. Not sure how often do I have to change the water but so far so good. &#32; submitted b
---

[RSS:Reddit LocalLLaMA (社区共识)]
MiniCPM 4.6
https://www.reddit.com/r/LocalLLaMA/comments/1ta9k8o/minicpm_46/
&#32; submitted by &#32; /u/themrzmaster [link] &#32; [comments]
---

[RSS:Reddit LocalLLaMA (社区共识)]
500k context on 48gb VRAM!! - 21tok/s (coding)
https://www.reddit.com/r/LocalLLaMA/comments/1tag1ks/500k_context_on_48gb_vram_21toks_coding/
I found this model hiding in the corner of huggingface: https://huggingface.co/Max-and-Omnis/Nemotron-3-Super-64B-A12B-Math-REAP-GGUF Looks to be tuned specifically for math but i thought i'd give it a try since i cant run the full 120b nemotron super and it seem to hold up like a champ in agentic c
---

[RSS:Reddit LocalLLaMA (社区共识)]
Will there be any more Qwen3.6 series models?
https://www.reddit.com/r/LocalLLaMA/comments/1taafs4/will_there_be_any_more_qwen36_series_models/
I'm still hoping we see a Qwen3.6-122B or a Qwen3.6-coder, but my hopes are dimming. Seems like we would have seen/heard something by now, even if just tantalizing hints from the Qwen folks. &#32; submitted by &#32; /u/cafedude [link] &#32; [comments]
---

[RSS:Reddit LocalLLaMA (社区共识)]
I catalogued every way local models break JSON output and built a repair library, here's what I found across 288 model calls
https://www.reddit.com/r/LocalLLaMA/comments/1tagtpv/i_catalogued_every_way_local_models_break_json/
I've been running structured output prompts through a bunch of models on OpenRouter for the past few months — Llama 3, Mistral, Command R, DeepSeek, Qwen, and every other model on OpenRouter — alongside the usual closed-source suspects. 288 calls total. I wanted to know what actually breaks, how oft
---

[RSS:Reddit LocalLLaMA (社区共识)]
Openclaw ia trending down and will disappear soon
https://www.reddit.com/r/LocalLLaMA/comments/1t9urup/openclaw_ia_trending_down_and_will_disappear_soon/
&#32; submitted by &#32; /u/rm-rf-rm [link] &#32; [comments]
---

[RSS:Reddit LocalLLaMA (社区共识)]
The Qwen 3.6 35B A3B hype is real!!!
https://www.reddit.com/r/LocalLLaMA/comments/1t9whrt/the_qwen_36_35b_a3b_hype_is_real/
My personal test for small local LLM intelligence is to check whether a model has any ability to understand the code that I write for my own academic research. My research is on some pretty niche topics and I doubt that anything like it is substantively present in the training sets for LLMs. A few m
---

[RSS:Reddit LocalLLaMA (社区共识)]
Gemma 4 running fully offline on WebGPU with Transformers.js, controlling Reachy Mini over WebSerial.
https://www.reddit.com/r/LocalLLaMA/comments/1ta9mmd/gemma_4_running_fully_offline_on_webgpu_with/
&#32; submitted by &#32; /u/xenovatech [link] &#32; [comments]
---

[RSS:Reddit LocalLLaMA (社区共识)]
B9109: preemptive fix for mtp & mmproj fix soon? It appears so
https://www.reddit.com/r/LocalLLaMA/comments/1taihoo/b9109_preemptive_fix_for_mtp_mmproj_fix_soon_it/
Summary : spec : process images through the draft context — this directly addresses the mmproj + MTP crash. Previously images (mmproj) couldn't be processed through the speculative/draft context at all. This commit adds that capability. That's the actual fix in progress. server : fix mtmd draft proc
---

[RSS:Reddit LocalLLaMA (社区共识)]
PowerColor launches Radeon AI PRO R9600D with 32GB GDDR6 memory
https://www.reddit.com/r/LocalLLaMA/comments/1taa74c/powercolor_launches_radeon_ai_pro_r9600d_with/
https://videocardz.com/newz/powercolor-launches-single-slot-and-passive-radeon-ai-pro-r9600d-32gb-and-12v-2x6-connector &#32; submitted by &#32; /u/MundanePercentage674 [link] &#32; [comments]
---

[RSS:Reddit LocalLLaMA (社区共识)]
Qwen3.6 35b-a3b 🤯
https://www.reddit.com/r/LocalLLaMA/comments/1ta53a2/qwen36_35ba3b/
Originally I was a diehard fan of Gemma4 26b-a4b because it really is a remarkably intelligent llm. Ran qwen3.6 via ollama and found it impressive but still favored Gemma. Ollama did it a disservice at least on my pc. Ran it straight through llama.cpp and it is much faster than gemma4 26b-a4b, rough
---

[RSS:Reddit LocalLLaMA (社区共识)]
New GGUF uploads on HF nearly doubled in 2 months
https://www.reddit.com/r/LocalLLaMA/comments/1t9zmbb/new_gguf_uploads_on_hf_nearly_doubled_in_2_months/
From clem on 𝕏: https://x.com/ClementDelangue/status/2053536106143261106 From Victor M on 𝕏: https://x.com/victormustar/status/2053780086596288781 &#32; submitted by &#32; /u/Nunki08 [link] &#32; [comments]
---

[RSS:Reddit LocalLLaMA (社区共识)]
prompt caching, but for rl training - 7.5x speedup on long-prompt/short-response workloads
https://www.reddit.com/r/LocalLLaMA/comments/1tage06/prompt_caching_but_for_rl_training_75x_speedup_on/
most open source RL engines pack sequences naively: prompt + response, repeated for every sample in the group. this is fine for short prompt, long completion workloads but inefficient for long prompt, short completion workloads. with 1000-token prompts and 100-token responses at G=8, you're processi
---

[RSS:Reddit LocalLLaMA (社区共识)]
ExLlamaV3 Major Updates!
https://www.reddit.com/r/LocalLLaMA/comments/1t9voxs/exllamav3_major_updates/
Turboderp has a been on an absolute tear recently, in the endless battle to cram new llamas into smaller, faster boxes. We started off last month with the release of gemma 4 support , and continued with improved caching efficiency . DFlash support came 2 weeks ago with these impressive results: Cate
---

[RSS:Reddit LocalLLaMA (社区共识)]
PSA: Watch out for extra spaces in chat-template-kwargs when using Qwen3.6 with llama-server
https://www.reddit.com/r/LocalLLaMA/comments/1ta1og5/psa_watch_out_for_extra_spaces_in/
Hey folks, just a heads-up for anyone running Qwen3.6 through llama-server . I ran into an issue where the preserve_thinking parameter wasn't working as expected, even though I had it explicitly enabled in my models.ini config. After some digging, I found that extra spaces in the JSON string are bre
---

[RSS:Reddit LocalLLaMA (社区共识)]
What's the current best small model?
https://www.reddit.com/r/LocalLLaMA/comments/1ta6b1u/whats_the_current_best_small_model/
Around 3B please thank you &#32; submitted by &#32; /u/Conscious_Nobody9571 [link] &#32; [comments]
---

[RSS:Reddit LocalLLaMA (社区共识)]
Drastically improve prompt processing speed for --n-cpu-moe partially offloaded models
https://www.reddit.com/r/LocalLLaMA/comments/1tany5t/drastically_improve_prompt_processing_speed_for/
Bigger ubatch made gpt-oss-120b prompt processing much faster on my RTX 3090 I was tuning gpt-oss-120b-F16.gguf with llama.cpp on a 24 GB RTX 3090 and found that increasing the physical micro-batch size ( -ub ) can massively improve prompt processing throughput, as long as you also raise --n-cpu-moe
---

[RSS:Reddit LocalLLaMA (社区共识)]
Anyone with 4x 5060ti based setups?
https://www.reddit.com/r/LocalLLaMA/comments/1ta7p6e/anyone_with_4x_5060ti_based_setups/
I am currently running 2x RTX 5060 ti and happened across some good sales for additional ones coinciding with a really good sale of a highend Z890 motherboard (replacing my B860 board) that could support quad GPUs (with 2 M.2 adapters, ending with running 1 GPU at 5.0 x8 and the rest at 5.0 x4, all 
---

[RSS:Reddit LocalLLaMA (社区共识)]
unsloth/MiMo-V2.5-GGUF · Hugging Face
https://www.reddit.com/r/LocalLLaMA/comments/1t9uqu8/unslothmimov25gguf_hugging_face/
can you run it? &#32; submitted by &#32; /u/jacek2023 [link] &#32; [comments]
---

[RSS:Reddit LocalLLaMA (社区共识)]
Any news (or hope) of Qwen-3.6 14B and 9B distills for local coding ?
https://www.reddit.com/r/LocalLLaMA/comments/1t9xzdv/any_news_or_hope_of_qwen36_14b_and_9b_distills/
As the title suggests. I'm already testing (with some success, and few challenges) usage of Qwen-3.5 9B with a new work laptop that I've received with RTX 1000 6GB VRAM (I know it seems like a joke in today's time and age). I am using it with `pi` as the terminal coding harness. The issue I am facin
---

[RSS:Reddit LocalLLaMA (社区共识)]
Markdown browser for LLMs
https://www.reddit.com/r/LocalLLaMA/comments/1t9tsro/markdown_browser_for_llms/
I built a markdown web renderer for AI agents. Instead of taking expensive screenshots and piping them through vision models, TextWeb renders web pages as markdown that LLMs can reason about natively. Full JavaScript execution, interactive elements annotated. It provides a CLI and an MCP server. You
---

[RSS:Reddit MachineLearning (学术风向)]
Online RL Reading Group[D]
https://www.reddit.com/r/MachineLearning/comments/1takowq/online_rl_reading_groupd/
Hi, I am a student going into my first year in Ph.D in RL this September. Although each university kinda has their own reading groups, I was wondering if there is active RL Online reading group I can participate. Sadly I couldnt find any info elsewhere. Does anyone have any information regarding Onl
---

[RSS:Reddit MachineLearning (学术风向)]
Interactive Jensen–Shannon Divergence Visualisation [P]
https://www.reddit.com/r/MachineLearning/comments/1ta5ybv/interactive_jensenshannon_divergence/
An interactive visualisation of Jensen–Shannon divergence - the symmetric, always-finite cousin of KL. Shape two distributions and watch JSD, its ceiling of one bit, and the per-point contribution respond in real time. https://robotchinwag.com/posts/jensen-shannon-divergence-visualisation/ Feedback 
---

[RSS:Reddit MachineLearning (学术风向)]
Where are small Models like Qwen3 0.6B and Qwen3.5 0.8B used ? Huggingface shows 2.88 million downloads this month.[D]
https://www.reddit.com/r/MachineLearning/comments/1ta9w3j/where_are_small_models_like_qwen3_06b_and_qwen35/
I can see 2.88 million downloads per month for small Qwen3.5 model. I tried using earlier model 0.6B in a deep resarch workflow and it was very difficult to get something done with this model . Firstly they have a very surface level understanding of concepts. Poor Semantic understand means they can 
---

[RSS:Reddit MachineLearning (学术风向)]
Is reproducing or implementing a paper considered research? [R]
https://www.reddit.com/r/MachineLearning/comments/1t9zre0/is_reproducing_or_implementing_a_paper_considered/
I completed my bachelors recently and I plan to applying to a masters program either this cycle or the next. Unfortunately, I did not publish any papers or do any research during my undergrad. Right now I’m in a research internship which is coming to and soon and it’s unlikely that I’ll get to publi
---

[RSS:Reddit MachineLearning (学术风向)]
How can I check whether my paper follows the required ARR formatting before submission? [D]
https://www.reddit.com/r/MachineLearning/comments/1taheqp/how_can_i_check_whether_my_paper_follows_the/
Last cycle, one of my research paper was rejected because of formatting issues. I recently heard from someone that there may be a tool or software called something like “aclpubcheck” that can be used to check whether a manuscript follows the required submission format correctly. Does anyone know the
---

[RSS:Reddit MachineLearning (学术风向)]
A hackable compiler to generate efficient fused GPU kernels for AI models [P]
https://www.reddit.com/r/MachineLearning/comments/1tag07l/a_hackable_compiler_to_generate_efficient_fused/
The modern ML (LLM) compiler stack is brutal. TVM is 500K+ lines of C++. PyTorch piles Dynamo, Inductor, and Triton on top of each other. I built a hackable LLM compiler from scratch and am documenting the process. It takes a small model (TinyLlama, Qwen2.5-7B) and lowers it to a sequence of CUDA ke
---

[RSS:Reddit MachineLearning (学术风向)]
Passing Multidimensional time series to VLM [R]
https://www.reddit.com/r/MachineLearning/comments/1tabsvp/passing_multidimensional_time_series_to_vlm_r/
Hello all, I have a multidimensional time series dataset and corresponding environment videos. I want to pass them to a VLM to perform some tasks. What is the best way to pass the time series data? From the literature review, I see there are two methods: pass time series as text and plot line charts
---

[RSS:Reddit MachineLearning (学术风向)]
What to expect from AlphaZero's value predictions [D]
https://www.reddit.com/r/MachineLearning/comments/1ta1ugy/what_to_expect_from_alphazeros_value_predictions_d/
An AlphaZero agent has learnt to predict the value of a game state by training on data generated by self-play by the model and a series of predecessor models. By construction, this value should reflect the probability of winning against a copy of itself starting from the given state. To be more prec
---

[RSS:Ars Technica AI (深度技术)]
Linux bitten by second severe vulnerability in as many weeks
https://arstechnica.com/security/2026/05/linux-bitten-by-second-severe-vulnerability-in-as-many-weeks/
Production-version patches are coming online and should be installed pronto.
---

[RSS:Reddit Jobs & Careers (职场动态)]
Interview Discussion - May 11, 2026
https://www.reddit.com/r/cscareerquestions/comments/1t9vl37/interview_discussion_may_11_2026/
Please use this thread to have discussions about interviews, interviewing, and interview prep. Posts focusing solely on interviews created outside of this thread will probably be removed. Abide by the rules, don't be a jerk. This thread is posted each Monday and Thursday at midnight PST . Previous I
---

[RSS:Reddit Jobs & Careers (职场动态)]
Is the push for AI burning anyone else out?
https://www.reddit.com/r/cscareerquestions/comments/1taf0gg/is_the_push_for_ai_burning_anyone_else_out/
I want to start by saying I am new to the work force. I had an internship 2 summers ago, graduated in May and started working full time as a software developer after that. When I did my internship, I was beyond happy with my work. AI was obviously already present, it helped me get so much done in my
---

[RSS:Reddit Jobs & Careers (职场动态)]
I'm at loss, I don't want to be a "programmer" anymore
https://www.reddit.com/r/cscareerquestions/comments/1ta6vir/im_at_loss_i_dont_want_to_be_a_programmer_anymore/
Working in office, I'm a 13+ year senior mainly in .NET stuff, used most of it and had various adventures in lots of technologies. Matter of fact I'm a full stack dev from the barebone db design to production and beyond. &quot;Programmer&quot; is between quotes because I'm not even close to a progra
---

[RSS:Reddit Jobs & Careers (职场动态)]
Anyone else just tired of software?
https://www.reddit.com/r/cscareerquestions/comments/1ta132f/anyone_else_just_tired_of_software/
I’m coming up on 8 years of experience, all for the same non-tech company. I do full stack web development, fully remote, for about $150k TC in a LCOL area. I’m just burnt out man. I was made tech lead of a project a few months ago and I just have nothing left to give. I can barely bring myself to d
---

[RSS:Reddit Jobs & Careers (职场动态)]
New vibecoding screening format: "AI Fluency" sessions
https://www.reddit.com/r/cscareerquestions/comments/1tae6tq/new_vibecoding_screening_format_ai_fluency/
It has come to my attention that, along the usual leetcode medium + system design interviews, now there's a new &quot;vibecoding&quot; format, where you're given a product to create with a LLM and then given features to add, so you indefinitely do until your 45 minutes run out. It's very hard to sea
---

[RSS:Reddit Jobs & Careers (职场动态)]
Feels like anyone can do what i do now
https://www.reddit.com/r/cscareerquestions/comments/1tai12z/feels_like_anyone_can_do_what_i_do_now/
&#x200b; TLDR I feel like in today's age, any knowledge I got from my degree and my studies became a very known commodity and anyone now can do the same, even more if we expand 5-10-15 years from now on. What's even the value of the field now? I lost my motivation as years passes by, got from 100 to
---

[RSS:Reddit Jobs & Careers (职场动态)]
Why is everyone on this sub so split?
https://www.reddit.com/r/cscareerquestions/comments/1talarw/why_is_everyone_on_this_sub_so_split/
I see like 60-70% of people saying it’s all gone to shit and esp for new grads that their best bet is to go to a top tech school network there and then apply through the connections; seems like anything out of top 10 tech schools people treat u like ur already homeless. And then the other 30-40% are
---

[RSS:Reddit Jobs & Careers (职场动态)]
Least Favorite Screening Annoyances?
https://www.reddit.com/r/cscareerquestions/comments/1ta9crs/least_favorite_screening_annoyances/
I’ll start: &gt;”We don’t do Leetcode style questions here. It’s more of a realistic practical application” &gt;The “practical application” turns out to be just thinly-veiled Leetcode style questions with you needing to write an extra layer of boilerplate on top. &#32; submitted by &#32; /u/Defiant-
---

[RSS:Reddit Jobs & Careers (职场动态)]
How to break out of a niche role?
https://www.reddit.com/r/cscareerquestions/comments/1tamfkv/how_to_break_out_of_a_niche_role/
I currently work at a government contractor company that hired me out of school little over three years ago. Since that was the start of when layoffs were occuring, I took the job despite the techstack since it was the only job offer I had. I'm trying to job hop as not only do I want more money, but
---

[RSS:Reddit Jobs & Careers (职场动态)]
Navigating difficult market as as a Data Engineer
https://www.reddit.com/r/cscareerquestions/comments/1talbxs/navigating_difficult_market_as_as_a_data_engineer/
Hello everyone, kind of wanted to get peoples take on the job market. I am finding it to be incredibly rough. I have 8 YOE and am currently doing a contracting role with Disney. I was laid off last year and seeing this subreddit made me panic. I was scared of it taking months to get a job so I took 
---

[RSS:Reddit Jobs & Careers (职场动态)]
Am I crazy for declining a job offer that is ~40% greater TC?
https://www.reddit.com/r/cscareerquestions/comments/1ta341d/am_i_crazy_for_declining_a_job_offer_that_is_40/
TLDR: 2 years into my career, making $80k base + $15k bonus at a tech company I genuinely love. Great perks, hybrid work, 10-4 hours, 5 min commute, solid team of 5 devs. Got an offer for $117k base + 20% bonus (roughly 40% more TC) at a finance company doing AI automation work, but I'd be the sole 
---

[RSS:Reddit Jobs & Careers (职场动态)]
How many applications should I send to one company at once?
https://www.reddit.com/r/cscareerquestions/comments/1ta9ihr/how_many_applications_should_i_send_to_one/
I found a company with 18 openings that I would be somewhat of a match for. I narrowed the list down to the 6 most relevant, but I wasn't sure if submitting 6 applications at once to the same company would come off as a red flag. Is there a good number that shows interest without coming off as despe
---

[RSS:Reddit Jobs & Careers (职场动态)]
UAE data engineering job market
https://www.reddit.com/r/cscareerquestions/comments/1tajgbx/uae_data_engineering_job_market/
I am a data engineer from europe with 3.5yoe with relevant experience In databricks and recently Im financial systems (banking and insurance) If it matters. Im researching a potential move to UAE (Dubai or Abu Dhabi), but Im struggling to understand how this market works and which firms might be hir
---

[RSS:Reddit Jobs & Careers (职场动态)]
marchandising/supervisor advice ?
https://www.reddit.com/r/cscareerquestions/comments/1tafgii/marchandisingsupervisor_advice/
I need advice to build my career . I'm starting a new job recently as a marchandiser and i need advice to know how things work &#32; submitted by &#32; /u/heel_aboy [link] &#32; [comments]
---

[RSS:Reddit Jobs & Careers (职场动态)]
Can't land one interrview, what am I doing wrong?
https://www.reddit.com/r/cscareerquestions/comments/1ta8e1x/cant_land_one_interrview_what_am_i_doing_wrong/
I'm a full-stack developer, I have around 3-4 YOE. I went to a decent university, I interned at a company that has a very good reputation in the cybersecurity space, 2 years of experience as a frontend dev for a tech startup in Berlin doing work for some pretty notable clients (Fanta, Coca-cola), pr
---

[RSS:Reddit Jobs & Careers (职场动态)]
Advice on performance issues at Financial Firm
https://www.reddit.com/r/cscareerquestions/comments/1tantby/advice_on_performance_issues_at_financial_firm/
I joined a financial firm (HFT) a bit over 1 year ago. Things started out really well, got minor feedback on some stuff and maybe had a couple PRs that dragged a bit, but overall delivery was pretty good and mostly positive feedback from my manager. Fast-forward to two months ago when I hit my one y
---

[RSS:Reddit Jobs & Careers (职场动态)]
microsoft offer ic2
https://www.reddit.com/r/cscareerquestions/comments/1tanr2t/microsoft_offer_ic2/
base: 130k stock reward: 65k sign-on: 9k performance bonus:0-20% location: redmond Is this a lowball? &#32; submitted by &#32; /u/Ineedluck18 [link] &#32; [comments]
---

[RSS:Reddit Jobs & Careers (职场动态)]
Hired as "SW Lead" without anyone under me
https://www.reddit.com/r/cscareerquestions/comments/1ta7s23/hired_as_sw_lead_without_anyone_under_me/
About a year ago I was hired as a software lead. But when I joined, there was one developer who was meant to support me but he gave his notice my 1st week. Since then no one else has been hired for my team and I have been juggling everything (technical work, admin items, customer meetings, design re
---

[RSS:Reddit Jobs & Careers (职场动态)]
Is CS worth it from a non-top school?
https://www.reddit.com/r/cscareerquestions/comments/1talvbx/is_cs_worth_it_from_a_nontop_school/
I’ll be going to my in state flagship in August, tbh I’m not happy about it but whatever the outcome of state California public schools are too expensive and I didn’t get into most of the ivies, the few I did get into won’t give any aid despite the fact that my parents won’t be paying anything towar
---

[RSS:Reddit Jobs & Careers (职场动态)]
where do developers gather to talk about startup experiences? (reddit hasn't been the right fit so far)
https://www.reddit.com/r/cscareerquestions/comments/1ta6j6k/where_do_developers_gather_to_talk_about_startup/
not soliciting anything here. just looking for advice on where to find the right community. i'm trying to have 1-on-1 conversations with developers of any experience level who've either worked at startups or are seriously considering making the jump. i want to hear concrete stories and perspectives:
---

[RSS:Reddit Jobs & Careers (职场动态)]
internships opportunities
https://www.reddit.com/r/cscareerquestions/comments/1tal3e7/internships_opportunities/
im going to start college in this fall and I have fairly decent CV in comparison to my peers however a lot of the internships in my country are consolidated to the university students, any idea on how I can pull through this? &#32; submitted by &#32; /u/kudtomo [link] &#32; [comments]
---

[RSS:Reddit Jobs & Careers (职场动态)]
Do OAs actually lead anywhere?
https://www.reddit.com/r/cscareerquestions/comments/1tah3qz/do_oas_actually_lead_anywhere/
I had OAs for BlackRock, Visa, TikTok, and IBM, all of which I failed. I read that neither of the OAs at these companies lead anywhere, regardless of how well you perform, especially BlackRock. I've been depending on the phone screens or first round interviews where I actually get to showcase myself
---

[HACKERNEWS]
Postmortem: TanStack npm supply-chain compromise
https://tanstack.com/blog/npm-supply-chain-compromise-postmortem
Score: 556 | Comments: 204
---

[HACKERNEWS]
If AI writes your code, why use Python?
https://medium.com/@NMitchem/if-ai-writes-your-code-why-use-python-bf8c4ba1a055
Score: 187 | Comments: 205
---

[HACKERNEWS]
UCLA discovers first stroke rehabilitation drug to repair brain damage (2025)
https://stemcell.ucla.edu/news/ucla-discovers-first-stroke-rehabilitation-drug-repair-brain-damage
Score: 243 | Comments: 48
---

[HACKERNEWS]
Claude Platform on AWS
https://claude.com/blog/claude-platform-on-aws
Score: 12 | Comments: 3
---

[HACKERNEWS]
Library for fast mapping of Java records to native memory
https://github.com/mamba-studio/TypedMemory
Score: 108 | Comments: 25
---

[HACKERNEWS]
I let AI build a tool to help me figure out what was waking me up at night
https://martin.sh/i-let-ai-build-a-tool-to-help-me-figure-out-what-was-waking-me-up-at-night/
Score: 78 | Comments: 89
---

[HACKERNEWS]
GitLab announces workforce reduction and end of their CREDIT values
https://about.gitlab.com/blog/gitlab-act-2/
Score: 342 | Comments: 332
---

[HACKERNEWS]
Ratty – A terminal emulator with inline 3D graphics
https://ratty-term.org/
Score: 615 | Comments: 198
---

[HACKERNEWS]
Gmail registration now requires scanning a QR code and sending a text message
https://discuss.privacyguides.net/t/google-account-registration-now-requires-sending-an-sms-via-phone-instead-of-receiving-an-sms/36082
Score: 568 | Comments: 426
---

[HACKERNEWS]
Griffin PowerMate driver for modern macOS
https://github.com/jameslockman/Griffin-PowerMate-Driver
Score: 45 | Comments: 17
---

[HACKERNEWS]
Google says criminal hackers used AI to find a major software flaw
https://www.nytimes.com/2026/05/11/us/politics/google-hackers-attack-ai.html
Score: 121 | Comments: 98
---

[HACKERNEWS]
Interaction Models
https://thinkingmachines.ai/blog/interaction-models/
Score: 100 | Comments: 9
---

[HACKERNEWS]
Interfaze: A new model architecture built for high accuracy at scale
https://interfaze.ai/blog/interfaze-a-new-model-architecture-built-for-high-accuracy-at-scale
Score: 113 | Comments: 30
---

[ACADEMIC - ARXIV]
标题: AgentRx: A Benchmark Study of LLM Agents for Multimodal Clinical Prediction Tasks
作者: Baraa Al Jorf, Farah E. Shamout
链接: https://arxiv.org/abs/2605.10286v1
完整摘要: Building effective clinical decision support systems requires the synthesis of complex heterogeneous multimodal data. Such modalities include temporal electronic health records data, medical images, radiology reports, and clinical notes. Large language model (LLM)-based agents have shown impressive performance in various healthcare tasks, especially those involving textual modalities. Considering the fragmentation of healthcare data across hospital systems, collaborative agent frameworks present a promising direction to mitigate data sharing challenges. However, the effectiveness of LLM agents for multimodal clinical risk prediction remains largely unexamined. In this work, we conduct a systematic evaluation of LLM-based agents for clinical prediction tasks using large-scale real-world data. We assess performance in unimodal and multimodal settings and quantify performance gaps between single agent and multi-agent systems. Our findings highlight that single agent frameworks outperform naive multi-agent systems, are better at handling multimodal data, and are better calibrated. This underscores a critical need for improving multi-agent collaboration to better handle heterogeneous inputs. By open-sourcing our code and evaluation framework, this work offers a new benchmark to support future developments relating to agentic systems in healthcare.
匹配关键词: multi-agent
---

[ACADEMIC - ARXIV]
标题: Towards Autonomous Railway Operations: A Semi-Hierarchical Deep Reinforcement Learning Approach to the Vehicle Rescheduling Problem
作者: Alberto Castagna, Stefan Zahlner, Adrian Egli, Christian Eichenberger, Daniel Boos, Manuel Meyer, Anton Fuxjager
链接: https://arxiv.org/abs/2605.10257v1
完整摘要: Managing disruptions in railway traffic management is a major challenge. Rising traffic density and infrastructure limits increase complexity, making the Vehicle Routing and Scheduling Problem (VRSP) difficult to solve reliably and in real time. While Operational Research (OR) methods are widely used, most dispatching still relies on human expertise due to the problem's exponential combinatorial complexity. Reinforcement Learning (RL) has gained attention for its potential in multi-agent coordination, but existing RL approaches often underperform OR methods and struggle to scale in dense rail networks. This paper addresses this gap from a machine learning perspective by introducing a semi-hierarchical RL formulation tailored to operational railway constraints. The method separates dispatching from routing through dedicated action and observation spaces, enabling policies to specialise in distinct decision scopes and addressing the imbalance between rare dispatch decisions and frequent routing updates. The approach is evaluated on the Flatland-RL simulator across five difficulty levels and 50 random seeds, with 7 to 80 trains. Results show substantially improved coordination, resource utilisation, and robustness compared with heuristic baselines and monolithic RL, nearly doubling the number of trains reaching their destinations, while keeping deadlock rates below 5% and adaptively sequencing, delaying, or cancelling trains under heavy congestion.
匹配关键词: multi-agent
---

[ACADEMIC - ARXIV]
标题: Beyond Autonomy: A Dynamic Tiered AgentRunner Framework for Governable and Resilient Enterprise AI Execution
作者: Kai Pan, Rong Hou
链接: https://arxiv.org/abs/2605.10223v1
完整摘要: Current large language model agent frameworks prioritize autonomy but lack the governability mechanisms required for enterprise deployment. High-risk write operations proceed without independent review, complex tasks lack acceptance verification, and computational resources are allocated uniformly regardless of risk level. We propose the Dynamic Tiered AgentRunner, a controlled execution protocol distilled from a production-grade multi-tenant SaaS platform. The framework introduces three core mechanisms: (1) Risk-Adaptive Tiering that dynamically allocates computational resources and review intensity based on task risk profiles, achieving Pareto-optimal trade-offs between safety and efficiency; (2) Separation of Powers architecture where proposal, review, execution, and verification are performed by independent agents with physically isolated boundaries; and (3) Resilience-by-Design through a Verifier-Recovery closed loop that treats failure as a first-class system state. We formalize the tier selectio
匹配关键词: multi-agent
---

[ACADEMIC - ARXIV]
标题: V-ABS: Action-Observer Driven Beam Search for Dynamic Visual Reasoning
作者: Zhiwei Ning, Xuanang Gao, Jiaxi Cao, Gengming Zhang, Shengnan Ma, Wenwen Tong, Hanming Deng, Jie Yang, Wei Liu
链接: https://arxiv.org/abs/2605.10172v1
完整摘要: Multimodal large language models (MLLMs) have achieved remarkable success in general perception, yet complex multi-step visual reasoning remains a persistent challenge. Although recent agentic approaches incorporate tool use, they often neglect critical execution feedback. Consequently, they suffer from the imagination-action-observer (IAO) bias, a misalignment between prior imagination and observer feedback that undermines reasoning stability and optimality. To bridge this gap, we introduce V-ABS, an action-observer driven beam search framework that enables deliberate reasoning through thinker-actor-observer iterations. We also propose an entropy-based adaptive weighting algorithm to mitigate the IAO bias by dynamically balancing the confidence scores between the policy priors and the observational feedback. Moreover, we construct a large-scale supervised fine-tuning (SFT) dataset comprising over 80k samples to guide the model to assign higher prior confidence to correct action paths. Extensive experiments across eight diverse benchmarks show that V-ABS achieves state-of-the-art performance, delivering an average improvement of 19.7% on the Qwen3-VL-8B baseline and consistent gains across both open-source and proprietary models.
匹配关键词: multi-agent
---

[ACADEMIC - ARXIV]
标题: When Reviews Disagree: Fine-Grained Contradiction Analysis in Scientific Peer Reviews
作者: Sandeep Kumar, Yash Kamdar, Abid Hossain, Bharti Kumari, Tanik Saikh, Asif Ekbal
链接: https://arxiv.org/abs/2605.10171v1
完整摘要: Scientific peer reviews frequently contain conflicting expert judgments, and the increasing scale of conference submissions makes it challenging for Area Chairs and editors to reliably identify and interpret such disagreements. Existing approaches typically frame reviewer disagreement as binary contradiction detection over isolated sentence pairs, abstracting away the review-level context and obscuring differences in the severity of evaluative conflict. In this work, we introduce a fine-grained formulation of reviewer contradiction analysis that operates over full peer reviews by explicitly identifying contradiction evidence spans and assigning graded disagreement intensity scores. To support this task, we present RevCI, an expert-annotated benchmark of peer-review pairs with evidence-level contradiction annotations with graded intensity labels. We further propose IMPACT, a structured multi-agent framework that integrates aspect-conditioned evidence extraction, deliberative reasoning, and adjudication to model reviewer contradictions and their intensity. To support efficient deployment, we distill IMPACT into TIDE, a small language model that predicts contradiction evidence and intensity in a single forward pass. Experimental results show that IMPACT substantially outperforms strong single-agent and generic multi-agent baselines in both evidence identification and intensity agreement, while TIDE achieves competitive performance at significantly lower inference cost.
匹配关键词: multi-agent
---

[ACADEMIC - ARXIV]
标题: Positive Alignment: Artificial Intelligence for Human Flourishing
作者: Ruben Laukkonen, Seb Krier, Chloé Bakalar, Shamil Chandaria, Morten Kringelbach, Adam Elwood, Daniel Ford, Fernando Rosas, Maty Bohacek, Matija Franklin, Nenad Tomašev, Stephanie Chan, Verena Rieser, Roma Patel, Michael Levin, Arun Rao
链接: https://arxiv.org/abs/2605.10310v1
完整摘要: Existing alignment research is dominated by concerns about safety and preventing harm: safeguards, controllability, and compliance. This paradigm of alignment parallels early psychology's focus on mental illness: necessary but incomplete. What we call Positive Alignment is the development of AI systems that (i) actively support human and ecological flourishing in a pluralistic, polycentric, context-sensitive, and user-authored way while (ii) remaining safe and cooperative. It is a distinct and necessary agenda within AI alignment research. We argue that several existing failures of alignment (e.g., engagement hacking, loss of human autonomy, failures in truth-seeking, low epistemic humility, error correction, lack of diverse viewpoints, and being primarily reactive rather than proactive) may be better addressed through positive alignment, including cultivating virtues and maximizing human flourishing. We highlight a range of challenges, open questions, and technical directions (e.g., data filtering and upsampling, pre- and post-training, evaluations, collaborative value collection) for different phases of the LLM and agents lifecycle. We end with design principles for promoting disagreement and decentralization through contextual grounding, community customization, continual adaptation, and polycentric governance; that is, many legitimate centers of oversight rather than one institutional or moral chokepoint.
匹配关键词: agent collaboration
---

[ACADEMIC - ARXIV]
标题: AgentRx: A Benchmark Study of LLM Agents for Multimodal Clinical Prediction Tasks
作者: Baraa Al Jorf, Farah E. Shamout
链接: https://arxiv.org/abs/2605.10286v1
完整摘要: Building effective clinical decision support systems requires the synthesis of complex heterogeneous multimodal data. Such modalities include temporal electronic health records data, medical images, radiology reports, and clinical notes. Large language model (LLM)-based agents have shown impressive performance in various healthcare tasks, especially those involving textual modalities. Considering the fragmentation of healthcare data across hospital systems, collaborative agent frameworks present a promising direction to mitigate data sharing challenges. However, the effectiveness of LLM agents for multimodal clinical risk prediction remains largely unexamined. In this work, we conduct a systematic evaluation of LLM-based agents for clinical prediction tasks using large-scale real-world data. We assess performance in unimodal and multimodal settings and quantify performance gaps between single agent and multi-agent systems. Our findings highlight that single agent frameworks outperform naive multi-agent systems, are better at handling multimodal data, and are better calibrated. This underscores a critical need for improving multi-agent collaboration to better handle heterogeneous inputs. By open-sourcing our code and evaluation framework, this work offers a new benchmark to support future developments relating to agentic systems in healthcare.
匹配关键词: agent collaboration
---

[ACADEMIC - ARXIV]
标题: DP-LAC: Lightweight Adaptive Clipping for Differentially Private Federated Fine-tuning of Language Models
作者: Haaris Mehmood, Jie Xu, Karthikeyan Saravanan, Rogier Van Dalen, Mete Ozay
链接: https://arxiv.org/abs/2605.10272v1
完整摘要: Federated learning (FL) enables the collaborative training of large-scale language models (LLMs) across edge devices while keeping user data on-device. However, FL still exposes sensitive information through client-provided gradients. Differentially private stochastic gradient descent (DP-SGD) mitigates this risk by clipping each client's contribution to a threshold $C$ and adding noise proportional to $C$. Existing adaptive clipping techniques dynamically adjust $C$ but demand tedious hyperparameter tuning, which can erode the privacy budget. In this paper, we introduce DP-LAC, a method that first estimates an initial clipping threshold within an order of magnitude of the optimum using private histogram estimation, and then adapts this threshold during training without consuming additional privacy budget or introducing new hyperparameters. Empirical results show that DP-LAC outperforms both state-of-the-art adaptive clipping methods and vanilla DP-SGD, achieving an average accuracy gain of $6.6\%$.
匹配关键词: agent collaboration
---

[ACADEMIC - ARXIV]
标题: MemReread: Enhancing Agentic Long-Context Reasoning via Memory-Guided Rereading
作者: Baibei Ji, Xiaoyang Weng, Juntao Li, Zecheng Tang, Yihang Lou, Min Zhang
链接: https://arxiv.org/abs/2605.10268v1
完整摘要: To tackle long-context reasoning tasks without the quadratic complexity of standard attention mechanisms, approaches based on agent memory have emerged, which typically maintain a dynamically updated memory when linearly processing document chunks. To mitigate the potential loss of latent evidence in this memorize-while-reading paradigm, recent works have integrated retrieval modules that allow agents to recall information previously discarded during memory overwriting. However, retrieval-based recall suffers from both evidence loss during memory formation and interference induced by invalid queries. To overcome these limitations, we propose MemReread. Built upon streaming reading, MemReread circumvents intermediate retrieval. It triggers question decomposition and rereading when the final memory is insufficient, enabling the recovery of indirect facts that were prematurely discarded. This design supports non-linear reasoning while preserving the inherent logical flow of document comprehension. To further enhance practicality, we introduce a reinforcement learning framework that enhances length extrapolation capability while dynamically determining the number of rereading passes based on task complexity, thereby flexibly controlling computational overhead. Extensive experiments demonstrate that MemReread consistently outperforms baseline frameworks on long-context reasoning tasks, while maintaining linear time complexity with respect to context length.
匹配关键词: agent collaboration
---

[ACADEMIC - ARXIV]
标题: Towards Autonomous Railway Operations: A Semi-Hierarchical Deep Reinforcement Learning Approach to the Vehicle Rescheduling Problem
作者: Alberto Castagna, Stefan Zahlner, Adrian Egli, Christian Eichenberger, Daniel Boos, Manuel Meyer, Anton Fuxjager
链接: https://arxiv.org/abs/2605.10257v1
完整摘要: Managing disruptions in railway traffic management is a major challenge. Rising traffic density and infrastructure limits increase complexity, making the Vehicle Routing and Scheduling Problem (VRSP) difficult to solve reliably and in real time. While Operational Research (OR) methods are widely used, most dispatching still relies on human expertise due to the problem's exponential combinatorial complexity. Reinforcement Learning (RL) has gained attention for its potential in multi-agent coordination, but existing RL approaches often underperform OR methods and struggle to scale in dense rail networks. This paper addresses this gap from a machine learning perspective by introducing a semi-hierarchical RL formulation tailored to operational railway constraints. The method separates dispatching from routing through dedicated action and observation spaces, enabling policies to specialise in distinct decision scopes and addressing the imbalance between rare dispatch decisions and frequent routing updates. The approach is evaluated on the Flatland-RL simulator across five difficulty levels and 50 random seeds, with 7 to 80 trains. Results show substantially improved coordination, resource utilisation, and robustness compared with heuristic baselines and monolithic RL, nearly doubling the number of trains reaching their destinations, while keeping deadlock rates below 5% and adaptively sequencing, delaying, or cancelling trains under heavy congestion.
匹配关键词: agent collaboration
---

[ACADEMIC - ARXIV]
标题: Positive Alignment: Artificial Intelligence for Human Flourishing
作者: Ruben Laukkonen, Seb Krier, Chloé Bakalar, Shamil Chandaria, Morten Kringelbach, Adam Elwood, Daniel Ford, Fernando Rosas, Maty Bohacek, Matija Franklin, Nenad Tomašev, Stephanie Chan, Verena Rieser, Roma Patel, Michael Levin, Arun Rao
链接: https://arxiv.org/abs/2605.10310v1
完整摘要: Existing alignment research is dominated by concerns about safety and preventing harm: safeguards, controllability, and compliance. This paradigm of alignment parallels early psychology's focus on mental illness: necessary but incomplete. What we call Positive Alignment is the development of AI systems that (i) actively support human and ecological flourishing in a pluralistic, polycentric, context-sensitive, and user-authored way while (ii) remaining safe and cooperative. It is a distinct and necessary agenda within AI alignment research. We argue that several existing failures of alignment (e.g., engagement hacking, loss of human autonomy, failures in truth-seeking, low epistemic humility, error correction, lack of diverse viewpoints, and being primarily reactive rather than proactive) may be better addressed through positive alignment, including cultivating virtues and maximizing human flourishing. We highlight a range of challenges, open questions, and technical directions (e.g., data filtering and upsampling, pre- and post-training, evaluations, collaborative value collection) for different phases of the LLM and agents lifecycle. We end with design principles for promoting disagreement and decentralization through contextual grounding, community customization, continual adaptation, and polycentric governance; that is, many legitimate centers of oversight rather than one institutional or moral chokepoint.
匹配关键词: agent coordination
---

[ACADEMIC - ARXIV]
标题: AgentRx: A Benchmark Study of LLM Agents for Multimodal Clinical Prediction Tasks
作者: Baraa Al Jorf, Farah E. Shamout
链接: https://arxiv.org/abs/2605.10286v1
完整摘要: Building effective clinical decision support systems requires the synthesis of complex heterogeneous multimodal data. Such modalities include temporal electronic health records data, medical images, radiology reports, and clinical notes. Large language model (LLM)-based agents have shown impressive performance in various healthcare tasks, especially those involving textual modalities. Considering the fragmentation of healthcare data across hospital systems, collaborative agent frameworks present a promising direction to mitigate data sharing challenges. However, the effectiveness of LLM agents for multimodal clinical risk prediction remains largely unexamined. In this work, we conduct a systematic evaluation of LLM-based agents for clinical prediction tasks using large-scale real-world data. We assess performance in unimodal and multimodal settings and quantify performance gaps between single agent and multi-agent systems. Our findings highlight that single agent frameworks outperform naive multi-agent systems, are better at handling multimodal data, and are better calibrated. This underscores a critical need for improving multi-agent collaboration to better handle heterogeneous inputs. By open-sourcing our code and evaluation framework, this work offers a new benchmark to support future developments relating to agentic systems in healthcare.
匹配关键词: agent coordination
---

[ACADEMIC - ARXIV]
标题: MemReread: Enhancing Agentic Long-Context Reasoning via Memory-Guided Rereading
作者: Baibei Ji, Xiaoyang Weng, Juntao Li, Zecheng Tang, Yihang Lou, Min Zhang
链接: https://arxiv.org/abs/2605.10268v1
完整摘要: To tackle long-context reasoning tasks without the quadratic complexity of standard attention mechanisms, approaches based on agent memory have emerged, which typically maintain a dynamically updated memory when linearly processing document chunks. To mitigate the potential loss of latent evidence in this memorize-while-reading paradigm, recent works have integrated retrieval modules that allow agents to recall information previously discarded during memory overwriting. However, retrieval-based recall suffers from both evidence loss during memory formation and interference induced by invalid queries. To overcome these limitations, we propose MemReread. Built upon streaming reading, MemReread circumvents intermediate retrieval. It triggers question decomposition and rereading when the final memory is insufficient, enabling the recovery of indirect facts that were prematurely discarded. This design supports non-linear reasoning while preserving the inherent logical flow of document comprehension. To further enhance practicality, we introduce a reinforcement learning framework that enhances length extrapolation capability while dynamically determining the number of rereading passes based on task complexity, thereby flexibly controlling computational overhead. Extensive experiments demonstrate that MemReread consistently outperforms baseline frameworks on long-context reasoning tasks, while maintaining linear time complexity with respect to context length.
匹配关键词: agent coordination
---

[ACADEMIC - ARXIV]
标题: Towards Autonomous Railway Operations: A Semi-Hierarchical Deep Reinforcement Learning Approach to the Vehicle Rescheduling Problem
作者: Alberto Castagna, Stefan Zahlner, Adrian Egli, Christian Eichenberger, Daniel Boos, Manuel Meyer, Anton Fuxjager
链接: https://arxiv.org/abs/2605.10257v1
完整摘要: Managing disruptions in railway traffic management is a major challenge. Rising traffic density and infrastructure limits increase complexity, making the Vehicle Routing and Scheduling Problem (VRSP) difficult to solve reliably and in real time. While Operational Research (OR) methods are widely used, most dispatching still relies on human expertise due to the problem's exponential combinatorial complexity. Reinforcement Learning (RL) has gained attention for its potential in multi-agent coordination, but existing RL approaches often underperform OR methods and struggle to scale in dense rail networks. This paper addresses this gap from a machine learning perspective by introducing a semi-hierarchical RL formulation tailored to operational railway constraints. The method separates dispatching from routing through dedicated action and observation spaces, enabling policies to specialise in distinct decision scopes and addressing the imbalance between rare dispatch decisions and frequent routing updates. The approach is evaluated on the Flatland-RL simulator across five difficulty levels and 50 random seeds, with 7 to 80 trains. Results show substantially improved coordination, resource utilisation, and robustness compared with heuristic baselines and monolithic RL, nearly doubling the number of trains reaching their destinations, while keeping deadlock rates below 5% and adaptively sequencing, delaying, or cancelling trains under heavy congestion.
匹配关键词: agent coordination
---

[ACADEMIC - ARXIV]
标题: Beyond Autonomy: A Dynamic Tiered AgentRunner Framework for Governable and Resilient Enterprise AI Execution
作者: Kai Pan, Rong Hou
链接: https://arxiv.org/abs/2605.10223v1
完整摘要: Current large language model agent frameworks prioritize autonomy but lack the governability mechanisms required for enterprise deployment. High-risk write operations proceed without independent review, complex tasks lack acceptance verification, and computational resources are allocated uniformly regardless of risk level. We propose the Dynamic Tiered AgentRunner, a controlled execution protocol distilled from a production-grade multi-tenant SaaS platform. The framework introduces three core mechanisms: (1) Risk-Adaptive Tiering that dynamically allocates computational resources and review intensity based on task risk profiles, achieving Pareto-optimal trade-offs between safety and efficiency; (2) Separation of Powers architecture where proposal, review, execution, and verification are performed by independent agents with physically isolated boundaries; and (3) Resilience-by-Design through a Verifier-Recovery closed loop that treats failure as a first-class system state. We formalize the tier selectio
匹配关键词: agent coordination
---

[ACADEMIC - ARXIV]
标题: Positive Alignment: Artificial Intelligence for Human Flourishing
作者: Ruben Laukkonen, Seb Krier, Chloé Bakalar, Shamil Chandaria, Morten Kringelbach, Adam Elwood, Daniel Ford, Fernando Rosas, Maty Bohacek, Matija Franklin, Nenad Tomašev, Stephanie Chan, Verena Rieser, Roma Patel, Michael Levin, Arun Rao
链接: https://arxiv.org/abs/2605.10310v1
完整摘要: Existing alignment research is dominated by concerns about safety and preventing harm: safeguards, controllability, and compliance. This paradigm of alignment parallels early psychology's focus on mental illness: necessary but incomplete. What we call Positive Alignment is the development of AI systems that (i) actively support human and ecological flourishing in a pluralistic, polycentric, context-sensitive, and user-authored way while (ii) remaining safe and cooperative. It is a distinct and necessary agenda within AI alignment research. We argue that several existing failures of alignment (e.g., engagement hacking, loss of human autonomy, failures in truth-seeking, low epistemic humility, error correction, lack of diverse viewpoints, and being primarily reactive rather than proactive) may be better addressed through positive alignment, including cultivating virtues and maximizing human flourishing. We highlight a range of challenges, open questions, and technical directions (e.g., data filtering and upsampling, pre- and post-training, evaluations, collaborative value collection) for different phases of the LLM and agents lifecycle. We end with design principles for promoting disagreement and decentralization through contextual grounding, community customization, continual adaptation, and polycentric governance; that is, many legitimate centers of oversight rather than one institutional or moral chokepoint.
匹配关键词: decentralized agent
---

[ACADEMIC - ARXIV]
标题: AgentRx: A Benchmark Study of LLM Agents for Multimodal Clinical Prediction Tasks
作者: Baraa Al Jorf, Farah E. Shamout
链接: https://arxiv.org/abs/2605.10286v1
完整摘要: Building effective clinical decision support systems requires the synthesis of complex heterogeneous multimodal data. Such modalities include temporal electronic health records data, medical images, radiology reports, and clinical notes. Large language model (LLM)-based agents have shown impressive performance in various healthcare tasks, especially those involving textual modalities. Considering the fragmentation of healthcare data across hospital systems, collaborative agent frameworks present a promising direction to mitigate data sharing challenges. However, the effectiveness of LLM agents for multimodal clinical risk prediction remains largely unexamined. In this work, we conduct a systematic evaluation of LLM-based agents for clinical prediction tasks using large-scale real-world data. We assess performance in unimodal and multimodal settings and quantify performance gaps between single agent and multi-agent systems. Our findings highlight that single agent frameworks outperform naive multi-agent systems, are better at handling multimodal data, and are better calibrated. This underscores a critical need for improving multi-agent collaboration to better handle heterogeneous inputs. By open-sourcing our code and evaluation framework, this work offers a new benchmark to support future developments relating to agentic systems in healthcare.
匹配关键词: decentralized agent
---

[ACADEMIC - ARXIV]
标题: MemReread: Enhancing Agentic Long-Context Reasoning via Memory-Guided Rereading
作者: Baibei Ji, Xiaoyang Weng, Juntao Li, Zecheng Tang, Yihang Lou, Min Zhang
链接: https://arxiv.org/abs/2605.10268v1
完整摘要: To tackle long-context reasoning tasks without the quadratic complexity of standard attention mechanisms, approaches based on agent memory have emerged, which typically maintain a dynamically updated memory when linearly processing document chunks. To mitigate the potential loss of latent evidence in this memorize-while-reading paradigm, recent works have integrated retrieval modules that allow agents to recall information previously discarded during memory overwriting. However, retrieval-based recall suffers from both evidence loss during memory formation and interference induced by invalid queries. To overcome these limitations, we propose MemReread. Built upon streaming reading, MemReread circumvents intermediate retrieval. It triggers question decomposition and rereading when the final memory is insufficient, enabling the recovery of indirect facts that were prematurely discarded. This design supports non-linear reasoning while preserving the inherent logical flow of document comprehension. To further enhance practicality, we introduce a reinforcement learning framework that enhances length extrapolation capability while dynamically determining the number of rereading passes based on task complexity, thereby flexibly controlling computational overhead. Extensive experiments demonstrate that MemReread consistently outperforms baseline frameworks on long-context reasoning tasks, while maintaining linear time complexity with respect to context length.
匹配关键词: decentralized agent
---

[ACADEMIC - ARXIV]
标题: Towards Autonomous Railway Operations: A Semi-Hierarchical Deep Reinforcement Learning Approach to the Vehicle Rescheduling Problem
作者: Alberto Castagna, Stefan Zahlner, Adrian Egli, Christian Eichenberger, Daniel Boos, Manuel Meyer, Anton Fuxjager
链接: https://arxiv.org/abs/2605.10257v1
完整摘要: Managing disruptions in railway traffic management is a major challenge. Rising traffic density and infrastructure limits increase complexity, making the Vehicle Routing and Scheduling Problem (VRSP) difficult to solve reliably and in real time. While Operational Research (OR) methods are widely used, most dispatching still relies on human expertise due to the problem's exponential combinatorial complexity. Reinforcement Learning (RL) has gained attention for its potential in multi-agent coordination, but existing RL approaches often underperform OR methods and struggle to scale in dense rail networks. This paper addresses this gap from a machine learning perspective by introducing a semi-hierarchical RL formulation tailored to operational railway constraints. The method separates dispatching from routing through dedicated action and observation spaces, enabling policies to specialise in distinct decision scopes and addressing the imbalance between rare dispatch decisions and frequent routing updates. The approach is evaluated on the Flatland-RL simulator across five difficulty levels and 50 random seeds, with 7 to 80 trains. Results show substantially improved coordination, resource utilisation, and robustness compared with heuristic baselines and monolithic RL, nearly doubling the number of trains reaching their destinations, while keeping deadlock rates below 5% and adaptively sequencing, delaying, or cancelling trains under heavy congestion.
匹配关键词: decentralized agent
---

[ACADEMIC - ARXIV]
标题: Beyond Autonomy: A Dynamic Tiered AgentRunner Framework for Governable and Resilient Enterprise AI Execution
作者: Kai Pan, Rong Hou
链接: https://arxiv.org/abs/2605.10223v1
完整摘要: Current large language model agent frameworks prioritize autonomy but lack the governability mechanisms required for enterprise deployment. High-risk write operations proceed without independent review, complex tasks lack acceptance verification, and computational resources are allocated uniformly regardless of risk level. We propose the Dynamic Tiered AgentRunner, a controlled execution protocol distilled from a production-grade multi-tenant SaaS platform. The framework introduces three core mechanisms: (1) Risk-Adaptive Tiering that dynamically allocates computational resources and review intensity based on task risk profiles, achieving Pareto-optimal trade-offs between safety and efficiency; (2) Separation of Powers architecture where proposal, review, execution, and verification are performed by independent agents with physically isolated boundaries; and (3) Resilience-by-Design through a Verifier-Recovery closed loop that treats failure as a first-class system state. We formalize the tier selectio
匹配关键词: decentralized agent
---

[ACADEMIC - ARXIV]
标题: Relations Are Channels: Knowledge Graph Embedding via Kraus Decompositions
作者: Sayan Kumar Chaki
链接: https://arxiv.org/abs/2605.10317v1
完整摘要: Knowledge graph embedding (KGE) models typically represent each relation as an operator on entity embeddings. In this work, we identify three structural axioms that any principled relation operator must satisfy, linearity, trace preservation, and complete positivity, and show that they characterize a Kraus channel structure via the Kraus representation theorem. The completeness constraint defining this family is equivalent to these axioms, providing a principled foundation rather than an externally imposed condition. Under this formulation, most existing operator-based KGE models are recoverable as special cases with Kraus rank $κ= 1$ under specific embedding choices. We further generalize this characterization to arbitrary metric geometries by introducing \mbox{w-Kraus} channels, which satisfy completeness by construction within their respective spaces. Building on this theory, we propose \textsc{KrausKGE}, a principled KGE model that naturally handles $1$-to-$N$ and $N$-to-$N$ relations, supports $k$-hop reasoning without requiring explicit path encoders, and eliminates the need for norm constraints on entity embeddings. Additionally, our framework yields the first theoretically grounded per-relation complexity measure in the KGE literature, with a provable lower bound in terms of the empirical relation matrix rank. Empirical evaluation demonstrates that \textsc{KrausKGE} consistently outperforms strong baselines on $N$-to-$N$ relations, with performance gains that increase monotonically with relation fan-out, in alignment with theoretical predictions.
匹配关键词: swarm intelligence
---

[ACADEMIC - ARXIV]
标题: Active Tabular Augmentation via Policy-Guided Diffusion Inpainting
作者: Zheyu Zhang, Shuo Yang, Bardh Prenkaj, Gjergji Kasneci
链接: https://arxiv.org/abs/2605.10315v1
完整摘要: Generative tabular augmentation is appealing in data-scarce domains, yet the prevailing focus on distributional fidelity does not reliably translate into better downstream models. We formalize a fidelity-utility gap: common generative objectives prioritize distributional plausibility, whereas augmentation succeeds only when injected samples reduce the current learner's held-out evaluation loss. This gap motivates learning not just how to generate, but what to generate and when to inject as training evolves. We propose TAP (Tabular Augmentation Policy), which couples diffusion inpainting with a lightweight, learner-conditioned policy to steer generation toward high-utility regions and controls safe injection via explicit gating and conservative windowed commitment. Under severe data scarcity, TAP consistently outperforms strong generative baselines on seven real-world datasets, improving classification accuracy by up to 15.6 percentage points and reducing regression RMSE by up to 32%.
匹配关键词: swarm intelligence
---

[ACADEMIC - ARXIV]
标题: Positive Alignment: Artificial Intelligence for Human Flourishing
作者: Ruben Laukkonen, Seb Krier, Chloé Bakalar, Shamil Chandaria, Morten Kringelbach, Adam Elwood, Daniel Ford, Fernando Rosas, Maty Bohacek, Matija Franklin, Nenad Tomašev, Stephanie Chan, Verena Rieser, Roma Patel, Michael Levin, Arun Rao
链接: https://arxiv.org/abs/2605.10310v1
完整摘要: Existing alignment research is dominated by concerns about safety and preventing harm: safeguards, controllability, and compliance. This paradigm of alignment parallels early psychology's focus on mental illness: necessary but incomplete. What we call Positive Alignment is the development of AI systems that (i) actively support human and ecological flourishing in a pluralistic, polycentric, context-sensitive, and user-authored way while (ii) remaining safe and cooperative. It is a distinct and necessary agenda within AI alignment research. We argue that several existing failures of alignment (e.g., engagement hacking, loss of human autonomy, failures in truth-seeking, low epistemic humility, error correction, lack of diverse viewpoints, and being primarily reactive rather than proactive) may be better addressed through positive alignment, including cultivating virtues and maximizing human flourishing. We highlight a range of challenges, open questions, and technical directions (e.g., data filtering and upsampling, pre- and post-training, evaluations, collaborative value collection) for different phases of the LLM and agents lifecycle. We end with design principles for promoting disagreement and decentralization through contextual grounding, community customization, continual adaptation, and polycentric governance; that is, many legitimate centers of oversight rather than one institutional or moral chokepoint.
匹配关键词: swarm intelligence
---

[ACADEMIC - ARXIV]
标题: Qwen Goes Brrr: Off-the-Shelf RAG for Ukrainian Multi-Domain Document Understanding
作者: Anton Bazdyrev, Ivan Bashtovyi, Ivan Havlytskyi, Oleksandr Kharytonov, Artur Khodakovskyi
链接: https://arxiv.org/abs/2605.10296v1
完整摘要: We participated in the Fifth UNLP shared task on multi-domain document understanding, where systems must answer Ukrainian multiple-choice questions from PDF collections and localize the supporting document and page. We propose a retrieval-augmented pipeline built around three ideas: contextual chunking of PDFs, question-aware dense retrieval and reranking conditioned on both the question and answer options, and constrained answer generation from a small set of reranked passages. Our final system uses Qwen3-Embedding-8B for retrieval, a fine-tuned Qwen3-Reranker-8B for passage ranking, and Qwen3-32B for answer selection. On a held-out split, reranking improves Recall@1 from 0.6957 to 0.7935, while using the top-2 reranked passages raises answer accuracy from 0.9348 to 0.9674. Our best leaderboard run reached 0.9452 on the public leaderboard and 0.9598 on the private leaderboard. Our results suggest that, under strict code-competition constraints, preserving document structure and making relevance estimation aware of the answer space are more effective than adding complex downstream heuristics.
匹配关键词: swarm intelligence
---

[ACADEMIC - ARXIV]
标题: Robust Probabilistic Shielding for Safe Offline Reinforcement Learning
作者: Maris F. L. Galesloot, Thomas Rhemrev, Nils Jansen
链接: https://arxiv.org/abs/2605.10293v1
完整摘要: In offline reinforcement learning (RL), we learn policies from fixed datasets without environment interaction. The major challenges are to provide guarantees on the (1) performance and (2) safety of the resulting policy. A technique called safe policy improvement (SPI) provides a performance guarantee: with high probability, the new policy outperforms a given baseline policy, which is assumed to be safe. Orthogonally, in the context of safe RL, a shield provides a safety guarantee by restricting the action space to those actions that are provably safe with respect to a given safety-relevant model. We integrate these paradigms by extending shielding to offline RL, relying solely on the available dataset and knowledge of safe and unsafe states. Then, we shield the policy improvement steps, guaranteeing, with high probability, a safe policy. Experimental results demonstrate that shielded SPI outperforms its unshielded counterpart, improving both average and worst-case performance, particularly in low-data regimes.
匹配关键词: swarm intelligence
---

[ACADEMIC - ARXIV]
标题: Relations Are Channels: Knowledge Graph Embedding via Kraus Decompositions
作者: Sayan Kumar Chaki
链接: https://arxiv.org/abs/2605.10317v1
完整摘要: Knowledge graph embedding (KGE) models typically represent each relation as an operator on entity embeddings. In this work, we identify three structural axioms that any principled relation operator must satisfy, linearity, trace preservation, and complete positivity, and show that they characterize a Kraus channel structure via the Kraus representation theorem. The completeness constraint defining this family is equivalent to these axioms, providing a principled foundation rather than an externally imposed condition. Under this formulation, most existing operator-based KGE models are recoverable as special cases with Kraus rank $κ= 1$ under specific embedding choices. We further generalize this characterization to arbitrary metric geometries by introducing \mbox{w-Kraus} channels, which satisfy completeness by construction within their respective spaces. Building on this theory, we propose \textsc{KrausKGE}, a principled KGE model that naturally handles $1$-to-$N$ and $N$-to-$N$ relations, supports $k$-hop reasoning without requiring explicit path encoders, and eliminates the need for norm constraints on entity embeddings. Additionally, our framework yields the first theoretically grounded per-relation complexity measure in the KGE literature, with a provable lower bound in terms of the empirical relation matrix rank. Empirical evaluation demonstrates that \textsc{KrausKGE} consistently outperforms strong baselines on $N$-to-$N$ relations, with performance gains that increase monotonically with relation fan-out, in alignment with theoretical predictions.
匹配关键词: game theory agent
---

[ACADEMIC - ARXIV]
标题: Positive Alignment: Artificial Intelligence for Human Flourishing
作者: Ruben Laukkonen, Seb Krier, Chloé Bakalar, Shamil Chandaria, Morten Kringelbach, Adam Elwood, Daniel Ford, Fernando Rosas, Maty Bohacek, Matija Franklin, Nenad Tomašev, Stephanie Chan, Verena Rieser, Roma Patel, Michael Levin, Arun Rao
链接: https://arxiv.org/abs/2605.10310v1
完整摘要: Existing alignment research is dominated by concerns about safety and preventing harm: safeguards, controllability, and compliance. This paradigm of alignment parallels early psychology's focus on mental illness: necessary but incomplete. What we call Positive Alignment is the development of AI systems that (i) actively support human and ecological flourishing in a pluralistic, polycentric, context-sensitive, and user-authored way while (ii) remaining safe and cooperative. It is a distinct and necessary agenda within AI alignment research. We argue that several existing failures of alignment (e.g., engagement hacking, loss of human autonomy, failures in truth-seeking, low epistemic humility, error correction, lack of diverse viewpoints, and being primarily reactive rather than proactive) may be better addressed through positive alignment, including cultivating virtues and maximizing human flourishing. We highlight a range of challenges, open questions, and technical directions (e.g., data filtering and upsampling, pre- and post-training, evaluations, collaborative value collection) for different phases of the LLM and agents lifecycle. We end with design principles for promoting disagreement and decentralization through contextual grounding, community customization, continual adaptation, and polycentric governance; that is, many legitimate centers of oversight rather than one institutional or moral chokepoint.
匹配关键词: game theory agent
---

[ACADEMIC - ARXIV]
标题: Characterizing the Generalization Error of Random Feature Regression with Arbitrary Data-Augmentation
作者: Lucas Morisset, Alain Durmus, Adrien Hardy
链接: https://arxiv.org/abs/2605.10290v1
完整摘要: This paper aims at analyzing the regularization effect that data augmentation induces on supervised regression methods in the proportional regime, where the number of covariates grows proportionally to the number of samples. We provide a tight characterization of the test error, measured in mean squared error, in terms only of the population quantities of the true data, as well as first and second order statistics of the augmentation scheme. Our results are valid under misspecified feature maps, and for any network architecture where only the last readout layer is trained, and the rest of the network is either frozen or randomly initialized. We specify our results in the case of Gaussian data, and show that our asymptotic characterization is tight in this setting.
匹配关键词: game theory agent
---

[ACADEMIC - ARXIV]
标题: AgentRx: A Benchmark Study of LLM Agents for Multimodal Clinical Prediction Tasks
作者: Baraa Al Jorf, Farah E. Shamout
链接: https://arxiv.org/abs/2605.10286v1
完整摘要: Building effective clinical decision support systems requires the synthesis of complex heterogeneous multimodal data. Such modalities include temporal electronic health records data, medical images, radiology reports, and clinical notes. Large language model (LLM)-based agents have shown impressive performance in various healthcare tasks, especially those involving textual modalities. Considering the fragmentation of healthcare data across hospital systems, collaborative agent frameworks present a promising direction to mitigate data sharing challenges. However, the effectiveness of LLM agents for multimodal clinical risk prediction remains largely unexamined. In this work, we conduct a systematic evaluation of LLM-based agents for clinical prediction tasks using large-scale real-world data. We assess performance in unimodal and multimodal settings and quantify performance gaps between single agent and multi-agent systems. Our findings highlight that single agent frameworks outperform naive multi-agent systems, are better at handling multimodal data, and are better calibrated. This underscores a critical need for improving multi-agent collaboration to better handle heterogeneous inputs. By open-sourcing our code and evaluation framework, this work offers a new benchmark to support future developments relating to agentic systems in healthcare.
匹配关键词: game theory agent
---

[ACADEMIC - ARXIV]
标题: Generalization Error Bounds for Picard-Type Operator Learning in Nonlinear Parabolic PDEs
作者: Koichi Taniguchi, Sho Sonoda
链接: https://arxiv.org/abs/2605.10277v1
完整摘要: Operator learning for partial differential equations (PDEs) aims to learn solution operators on infinite-dimensional function spaces from finite-resolution data. In this setting, it is important for the learned model to be discretization-invariant, or resolution-robust, and to reflect PDE-specific structure. It is therefore natural to ask how such structure should be encoded in the model architecture, hypothesis class, or learning procedure. In this paper, we study operator learning for solution operators of nonlinear parabolic PDEs based on Duhamel--Picard iteration. We formulate Picard iteration as an abstract state-transition model and present a theoretical framework for Picard-type operator learning. We derive implementation-agnostic generalization error bounds that separate the implementation error from the estimation error associated with the abstract state-transition model induced by Picard iteration. A key consequence is that increasing the Picard depth reduces the Picard truncation error without causing an unbounded growth of the entropy-based estimation error. We also extend the analysis to long-time prediction by rolling out the same learned local model over successive time blocks. Finally, we illustrate the theory for nonlinear heat equations on the torus using a Picard-type Fourier neural operator as a concrete implementation.
匹配关键词: game theory agent
---

[ACADEMIC - ARXIV]
标题: Positive Alignment: Artificial Intelligence for Human Flourishing
作者: Ruben Laukkonen, Seb Krier, Chloé Bakalar, Shamil Chandaria, Morten Kringelbach, Adam Elwood, Daniel Ford, Fernando Rosas, Maty Bohacek, Matija Franklin, Nenad Tomašev, Stephanie Chan, Verena Rieser, Roma Patel, Michael Levin, Arun Rao
链接: https://arxiv.org/abs/2605.10310v1
完整摘要: Existing alignment research is dominated by concerns about safety and preventing harm: safeguards, controllability, and compliance. This paradigm of alignment parallels early psychology's focus on mental illness: necessary but incomplete. What we call Positive Alignment is the development of AI systems that (i) actively support human and ecological flourishing in a pluralistic, polycentric, context-sensitive, and user-authored way while (ii) remaining safe and cooperative. It is a distinct and necessary agenda within AI alignment research. We argue that several existing failures of alignment (e.g., engagement hacking, loss of human autonomy, failures in truth-seeking, low epistemic humility, error correction, lack of diverse viewpoints, and being primarily reactive rather than proactive) may be better addressed through positive alignment, including cultivating virtues and maximizing human flourishing. We highlight a range of challenges, open questions, and technical directions (e.g., data filtering and upsampling, pre- and post-training, evaluations, collaborative value collection) for different phases of the LLM and agents lifecycle. We end with design principles for promoting disagreement and decentralization through contextual grounding, community customization, continual adaptation, and polycentric governance; that is, many legitimate centers of oversight rather than one institutional or moral chokepoint.
匹配关键词: agent communication
---

[ACADEMIC - ARXIV]
标题: AgentRx: A Benchmark Study of LLM Agents for Multimodal Clinical Prediction Tasks
作者: Baraa Al Jorf, Farah E. Shamout
链接: https://arxiv.org/abs/2605.10286v1
完整摘要: Building effective clinical decision support systems requires the synthesis of complex heterogeneous multimodal data. Such modalities include temporal electronic health records data, medical images, radiology reports, and clinical notes. Large language model (LLM)-based agents have shown impressive performance in various healthcare tasks, especially those involving textual modalities. Considering the fragmentation of healthcare data across hospital systems, collaborative agent frameworks present a promising direction to mitigate data sharing challenges. However, the effectiveness of LLM agents for multimodal clinical risk prediction remains largely unexamined. In this work, we conduct a systematic evaluation of LLM-based agents for clinical prediction tasks using large-scale real-world data. We assess performance in unimodal and multimodal settings and quantify performance gaps between single agent and multi-agent systems. Our findings highlight that single agent frameworks outperform naive multi-agent systems, are better at handling multimodal data, and are better calibrated. This underscores a critical need for improving multi-agent collaboration to better handle heterogeneous inputs. By open-sourcing our code and evaluation framework, this work offers a new benchmark to support future developments relating to agentic systems in healthcare.
匹配关键词: agent communication
---

[ACADEMIC - ARXIV]
标题: MemReread: Enhancing Agentic Long-Context Reasoning via Memory-Guided Rereading
作者: Baibei Ji, Xiaoyang Weng, Juntao Li, Zecheng Tang, Yihang Lou, Min Zhang
链接: https://arxiv.org/abs/2605.10268v1
完整摘要: To tackle long-context reasoning tasks without the quadratic complexity of standard attention mechanisms, approaches based on agent memory have emerged, which typically maintain a dynamically updated memory when linearly processing document chunks. To mitigate the potential loss of latent evidence in this memorize-while-reading paradigm, recent works have integrated retrieval modules that allow agents to recall information previously discarded during memory overwriting. However, retrieval-based recall suffers from both evidence loss during memory formation and interference induced by invalid queries. To overcome these limitations, we propose MemReread. Built upon streaming reading, MemReread circumvents intermediate retrieval. It triggers question decomposition and rereading when the final memory is insufficient, enabling the recovery of indirect facts that were prematurely discarded. This design supports non-linear reasoning while preserving the inherent logical flow of document comprehension. To further enhance practicality, we introduce a reinforcement learning framework that enhances length extrapolation capability while dynamically determining the number of rereading passes based on task complexity, thereby flexibly controlling computational overhead. Extensive experiments demonstrate that MemReread consistently outperforms baseline frameworks on long-context reasoning tasks, while maintaining linear time complexity with respect to context length.
匹配关键词: agent communication
---

[ACADEMIC - ARXIV]
标题: Towards Autonomous Railway Operations: A Semi-Hierarchical Deep Reinforcement Learning Approach to the Vehicle Rescheduling Problem
作者: Alberto Castagna, Stefan Zahlner, Adrian Egli, Christian Eichenberger, Daniel Boos, Manuel Meyer, Anton Fuxjager
链接: https://arxiv.org/abs/2605.10257v1
完整摘要: Managing disruptions in railway traffic management is a major challenge. Rising traffic density and infrastructure limits increase complexity, making the Vehicle Routing and Scheduling Problem (VRSP) difficult to solve reliably and in real time. While Operational Research (OR) methods are widely used, most dispatching still relies on human expertise due to the problem's exponential combinatorial complexity. Reinforcement Learning (RL) has gained attention for its potential in multi-agent coordination, but existing RL approaches often underperform OR methods and struggle to scale in dense rail networks. This paper addresses this gap from a machine learning perspective by introducing a semi-hierarchical RL formulation tailored to operational railway constraints. The method separates dispatching from routing through dedicated action and observation spaces, enabling policies to specialise in distinct decision scopes and addressing the imbalance between rare dispatch decisions and frequent routing updates. The approach is evaluated on the Flatland-RL simulator across five difficulty levels and 50 random seeds, with 7 to 80 trains. Results show substantially improved coordination, resource utilisation, and robustness compared with heuristic baselines and monolithic RL, nearly doubling the number of trains reaching their destinations, while keeping deadlock rates below 5% and adaptively sequencing, delaying, or cancelling trains under heavy congestion.
匹配关键词: agent communication
---

[ACADEMIC - ARXIV]
标题: Beyond Autonomy: A Dynamic Tiered AgentRunner Framework for Governable and Resilient Enterprise AI Execution
作者: Kai Pan, Rong Hou
链接: https://arxiv.org/abs/2605.10223v1
完整摘要: Current large language model agent frameworks prioritize autonomy but lack the governability mechanisms required for enterprise deployment. High-risk write operations proceed without independent review, complex tasks lack acceptance verification, and computational resources are allocated uniformly regardless of risk level. We propose the Dynamic Tiered AgentRunner, a controlled execution protocol distilled from a production-grade multi-tenant SaaS platform. The framework introduces three core mechanisms: (1) Risk-Adaptive Tiering that dynamically allocates computational resources and review intensity based on task risk profiles, achieving Pareto-optimal trade-offs between safety and efficiency; (2) Separation of Powers architecture where proposal, review, execution, and verification are performed by independent agents with physically isolated boundaries; and (3) Resilience-by-Design through a Verifier-Recovery closed loop that treats failure as a first-class system state. We formalize the tier selectio
匹配关键词: agent communication
---

[ACADEMIC - ARXIV]
标题: LeapTS: Rethinking Time Series Forecasting as Adaptive Multi-Horizon Scheduling
作者: Sheng Pan, Ming Jin, Bo Du, Shirui Pan
链接: https://arxiv.org/abs/2605.10292v1
完整摘要: Time series forecasting serves as an essential tool for many real-world applications, supporting tasks such as resource optimization and decision-making. Despite significant architectural advancements, most modern models still treat forecasting task as a fixed mapping from history to target horizons. This induces temporal decoupling across future time points and limits the model's ability to adapt to the evolving context as forecasting progresses. In this work, we present LeapTS, a novel framework that reformulates time series forecasting as a dynamic scheduling process over the prediction horizon. Specifically, LeapTS organizes the forecasting process into multi-level decisions using: (1) the hierarchical controller to dynamically select the optimal prediction scale and advancement length at each step, and (2) continuous-time state evolution driven by neural controlled differential equations. Within this process, the controlled update mechanism explicitly couples the irregular temporal dynamics with discrete scheduling feedback. Extensive evaluations on both real-world and synthetic datasets demonstrate that LeapTS improves overall forecasting performance by at least 7.4% while achieving a 2.6$\times$ to 5.3$\times$ inference speedup over representative Transformer-based models. Furthermore, by explicitly tracing the scheduling trajectories, we reveal how the model autonomously adapts its forecasting behavior to capture non-stationary dynamics.
匹配关键词: emergent behavior
---

[ACADEMIC - ARXIV]
标题: MemReread: Enhancing Agentic Long-Context Reasoning via Memory-Guided Rereading
作者: Baibei Ji, Xiaoyang Weng, Juntao Li, Zecheng Tang, Yihang Lou, Min Zhang
链接: https://arxiv.org/abs/2605.10268v1
完整摘要: To tackle long-context reasoning tasks without the quadratic complexity of standard attention mechanisms, approaches based on agent memory have emerged, which typically maintain a dynamically updated memory when linearly processing document chunks. To mitigate the potential loss of latent evidence in this memorize-while-reading paradigm, recent works have integrated retrieval modules that allow agents to recall information previously discarded during memory overwriting. However, retrieval-based recall suffers from both evidence loss during memory formation and interference induced by invalid queries. To overcome these limitations, we propose MemReread. Built upon streaming reading, MemReread circumvents intermediate retrieval. It triggers question decomposition and rereading when the final memory is insufficient, enabling the recovery of indirect facts that were prematurely discarded. This design supports non-linear reasoning while preserving the inherent logical flow of document comprehension. To further enhance practicality, we introduce a reinforcement learning framework that enhances length extrapolation capability while dynamically determining the number of rereading passes based on task complexity, thereby flexibly controlling computational overhead. Extensive experiments demonstrate that MemReread consistently outperforms baseline frameworks on long-context reasoning tasks, while maintaining linear time complexity with respect to context length.
匹配关键词: emergent behavior
---

[ACADEMIC - ARXIV]
标题: LegalCiteBench: Evaluating Citation Reliability in Legal Language Models
作者: Sijia Chen, Hang Yin, Shunfan Zhou
链接: https://arxiv.org/abs/2605.10186v1
完整摘要: Large language models (LLMs) are increasingly integrated into legal drafting and research workflows, where incorrect citations or fabricated precedents can cause serious professional harm. Existing legal benchmarks largely emphasize statutory reasoning, contract understanding, or general legal question answering, but they do not directly study a central common-law failure mode: when asked to provide case authorities without external grounding, models may return plausible-looking but incorrect citations or cases. We introduce LegalCiteBench, a benchmark for studying closed-book citation recovery, citation verification, and case matching in legal language models. LegalCiteBench contains approximately 24K evaluation instances constructed from 1,000 real U.S. judicial opinions from the Case Law Access Project. The benchmark covers five citation-centric tasks: citation retrieval, citation completion, citation error detection, case matching, and case verification and correction. Across 21 LLMs, exact citation recovery remains highly challenging in this closed-book setting: even the strongest models score below 7/100 on citation retrieval and completion. Within the evaluated models, scale and legal-domain pretraining provide limited gains and do not resolve this difficulty. Models also frequently provide concrete but incorrect or low-overlap authorities under our evaluation protocol, with Misleading Answer Rates (MAR) exceeding 94% for 20 of 21 evaluated models on retrieval-heavy tasks. A prompt-only abstention experiment shows that explicit uncertainty instructions reduce some confident fabrication but do not improve citation correctness. LegalCiteBench is intended as a diagnostic framework for studying authority generation failures, verification behavior, and abstention when external grounding is absent, incomplete, or bypassed.
匹配关键词: emergent behavior
---

[ACADEMIC - ARXIV]
标题: Joint sparse coding and temporal dynamics support context reconfiguration
作者: Qianqian Shi, Yue Che, Faqiang Liu, Hongyi Li, Mingkun Xu, Sandra Reinert, Pieter M. Goltstein, Rong Zhao, Luping Shi
链接: https://arxiv.org/abs/2605.10178v1
完整摘要: Adaptive behavior requires the brain to transition between distinct contexts while maintaining representations of prior experience. The ability to reconfigure neural representations without erasing previously acquired knowledge is central to learning in dynamic environments, yet the neural mechanisms that support this balance remain unclear. Understanding these mechanisms is also critical for addressing catastrophic forgetting in artificial systems designed for lifelong learning. Here, we identify joint sparse coding and temporal dynamics in both the mouse medial prefrontal cortex (mPFC) and computational networks as mechanisms that help preserve prior representations during context transitions. Specifically, sparsity in context-dependent representations reduces cross-context interference, whereas temporal dynamics within the network activity further enhance context separability across time. Strikingly, networks endowed with both properties, such as spiking neural networks, exhibit improved retention during lifelong learning without auxiliary heuristics. These findings establish joint sparse coding and temporal dynamics as a core mechanism supporting flexible context reconfiguration in lifelong learning and, through their activity constraining nature, as an energy-efficient architectural principle for stable adaptation. Together, they provide a mechanistic framework for understanding how the brain preserves prior knowledge while flexibly adapting to new contexts.
匹配关键词: emergent behavior
---

[ACADEMIC - ARXIV]
标题: When Prompts Become Payloads: A Framework for Mitigating SQL Injection Attacks in Large Language Model-Driven Applications
作者: Farzad Nourmohammadzadeh Motlagh, Mehrdad Hajizadeh, Mehryar Majd, Pejman Najafi, Feng Cheng, Christoph Meinel
链接: https://arxiv.org/abs/2605.10176v1
完整摘要: Natural language interfaces to structured databases are becoming increasingly common, largely due to advances in large language models (LLMs) that enable users to query data using conversational input rather than formal query languages such as SQL. While this paradigm significantly improves usability and accessibility, it introduces new security risks, particularly the amplification of SQL injection vulnerabilities through the prompt-to-SQL translation process. Malicious users can exploit these mechanisms by crafting adversarial prompts that manipulate model behavior and generate unsafe queries. In this work, we propose a multi-layered security framework designed to detect and mitigate LLM-mediated SQL injection attacks. The framework integrates a front-end security shield for prompt sanitization, an advanced threat detection model for behavioral and semantic anomaly identification, and a signature-based control layer for known attack patterns. We evaluate the proposed framework under diverse and realistic attack scenarios, including prompt injection, obfuscated SQL payloads, and context-manipulation attacks. To ensure robustness, we generate and curate a comprehensive benchmark dataset of adversarial prompts and assess performance across a fine-tuned LLM configuration. Experimental results demonstrate that the proposed approach achieves high detection accuracy while maintaining low false-positive rates, significantly improving the secure deployment of LLM-powered database applications.
匹配关键词: emergent behavior
---

[ACADEMIC - ARXIV]
标题: Relations Are Channels: Knowledge Graph Embedding via Kraus Decompositions
作者: Sayan Kumar Chaki
链接: https://arxiv.org/abs/2605.10317v1
完整摘要: Knowledge graph embedding (KGE) models typically represent each relation as an operator on entity embeddings. In this work, we identify three structural axioms that any principled relation operator must satisfy, linearity, trace preservation, and complete positivity, and show that they characterize a Kraus channel structure via the Kraus representation theorem. The completeness constraint defining this family is equivalent to these axioms, providing a principled foundation rather than an externally imposed condition. Under this formulation, most existing operator-based KGE models are recoverable as special cases with Kraus rank $κ= 1$ under specific embedding choices. We further generalize this characterization to arbitrary metric geometries by introducing \mbox{w-Kraus} channels, which satisfy completeness by construction within their respective spaces. Building on this theory, we propose \textsc{KrausKGE}, a principled KGE model that naturally handles $1$-to-$N$ and $N$-to-$N$ relations, supports $k$-hop reasoning without requiring explicit path encoders, and eliminates the need for norm constraints on entity embeddings. Additionally, our framework yields the first theoretically grounded per-relation complexity measure in the KGE literature, with a provable lower bound in terms of the empirical relation matrix rank. Empirical evaluation demonstrates that \textsc{KrausKGE} consistently outperforms strong baselines on $N$-to-$N$ relations, with performance gains that increase monotonically with relation fan-out, in alignment with theoretical predictions.
匹配关键词: reasoning
---

[ACADEMIC - ARXIV]
标题: MemReread: Enhancing Agentic Long-Context Reasoning via Memory-Guided Rereading
作者: Baibei Ji, Xiaoyang Weng, Juntao Li, Zecheng Tang, Yihang Lou, Min Zhang
链接: https://arxiv.org/abs/2605.10268v1
完整摘要: To tackle long-context reasoning tasks without the quadratic complexity of standard attention mechanisms, approaches based on agent memory have emerged, which typically maintain a dynamically updated memory when linearly processing document chunks. To mitigate the potential loss of latent evidence in this memorize-while-reading paradigm, recent works have integrated retrieval modules that allow agents to recall information previously discarded during memory overwriting. However, retrieval-based recall suffers from both evidence loss during memory formation and interference induced by invalid queries. To overcome these limitations, we propose MemReread. Built upon streaming reading, MemReread circumvents intermediate retrieval. It triggers question decomposition and rereading when the final memory is insufficient, enabling the recovery of indirect facts that were prematurely discarded. This design supports non-linear reasoning while preserving the inherent logical flow of document comprehension. To further enhance practicality, we introduce a reinforcement learning framework that enhances length extrapolation capability while dynamically determining the number of rereading passes based on task complexity, thereby flexibly controlling computational overhead. Extensive experiments demonstrate that MemReread consistently outperforms baseline frameworks on long-context reasoning tasks, while maintaining linear time complexity with respect to context length.
匹配关键词: reasoning
---

[ACADEMIC - ARXIV]
标题: IndustryBench: Probing the Industrial Knowledge Boundaries of LLMs
作者: Songlin Bai, Xintong Wang, Linlin Yu, Bin Chen, Zhiang Xu, Yuyang Sheng, Changtong Zan, Xiaofeng Zhu, Yizhe Zhang, Jiru Li, Mingze Guo, Ling Zou, Yalong Li, Chengfu Huo, Liang Ding
链接: https://arxiv.org/abs/2605.10267v1
完整摘要: In industrial procurement, an LLM answer is useful only if it survives a standards check: recommended material must match operating condition, every parameter must respect a regulated threshold, and no procedure may contradict a safety clause. Partial correctness can mask safety-critical contradictions that aggregate LLM benchmarks rarely capture. We introduce IndustryBench, a 2,049-item benchmark for industrial procurement QA in Chinese, grounded in Chinese national standards (GB/T) and structured industrial product records, organized by seven capability dimensions, ten industry categories, and panel-derived difficulty tiers, with item-aligned English, Russian, and Vietnamese renderings. Our construction pipeline rejects 70.3% of LLM-generated candidates at a search-based external-verification stage, calibrating how unreliable industrial QA remains after LLM-only filtering.Our evaluation decouples raw correctness, scored by a Qwen3-Max judge validated at $κ_w = 0.798$ against a domain expert, from a separate safety-violation (SV) check against source texts. Across 17 models in Chinese and an 8-model intersection over four languages, we find: (i) the best system reaches only 2.083 on the 0--3 rubric, leaving substantial headroom; (ii) Standards & Terminology is the most persistent capability weakness and survives item-aligned translation; (iii) extended reasoning lowers safety-adjusted scores for 12 of 13 models, primarily by introducing unsupported safety-critical details into longer final answers; and (iv) safety-violation rates reshuffle the leaderboard -- GPT-5.4 climbs from rank 6 to rank 3 after SV adjustment, while Kimi-k2.5-1T-A32B drops seven positions.Industrial LLM evaluation therefore requires source-grounded, safety-aware diagnosis rather than aggregate accuracy. We release IndustryBench with all prompts, scoring scripts, and dataset documentation.
匹配关键词: reasoning
---

[ACADEMIC - ARXIV]
标题: Efficient Hybrid CNN-GNN Architecture for Monocular Depth Estimation
作者: Ishan Narayan
链接: https://arxiv.org/abs/2605.10251v1
完整摘要: We present GraphDepth, a monocular depth estimation architecture that synergistically integrates Graph Neural Networks (GNNs) within a convolutional encoder-decoder framework. Our approach embeds efficient GraphSAGE layers at multiple scales of a ResNet-101 U-Net backbone, enabling explicit modeling of long-range spatial relationships that lie beyond the receptive field of local convolutions. Key technical contributions include: (1) batch-parallelized graph construction with configurable k-NN and grid-based adjacency for scalable training; (2) multi-scale GraphSAGE integration at bottleneck and decoder stages (1/32, 1/16, 1/8 resolution) to propagate global context throughout the feature hierarchy; (3) channel-attention gated skip connections that adaptively weight encoder features before fusion; and (4) heteroscedastic uncertainty estimation via a dedicated aleatoric uncertainty head, enabling confidence-aware loss weighting during optimization. Unlike transformer-based hybrids, which suffer from quadratic complexity in sequence length, GraphDepth scales linearly with spatial resolution while achieving comparable global receptive fields through iterative message passing. Experiments on NYU Depth V2, WHU Aerial, ETH3D, and Mid-Air benchmarks demonstrate competitive accuracy within 4.6\% of state-of-the-art transformers on indoor scenes with substantially lower computational cost (25 FPS vs 9 FPS, 3.8 GB vs 8.8 GB VRAM). GraphDepth achieves the best reported result on WHU Aerial (RMSE 8.24 m) and exhibits superior zero-shot cross-domain transfer to the Mid-Air synthetic aerial dataset, validating the generalization power of explicit relational reasoning for depth estimation.
匹配关键词: reasoning
---

[ACADEMIC - ARXIV]
标题: Teaching LLMs to See Graphs: Unifying Text and Structural Reasoning
作者: Dario Vajda
链接: https://arxiv.org/abs/2605.10247v1
完整摘要: Using Large Language Models (LLMs) to process graph-structured data is an active research area, yet current state-of-the-art approaches typically rely on multi-step pipelines with Graph Neural Network (GNN) encoders that compress rich textual attributes into solitary tokens, creating a significant semantic bottleneck. In this paper, we introduce the Graph Transformer Language Model (GTLM), a novel architecture that enables pretrained LLMs to natively process graph topologies while entirely eliminating this compressive bottleneck. GTLM is exceptionally parameter-efficient: by injecting graph-aware attention biases directly into the LLM's attention modules, it introduces only 0.015% additional parameters relative to the base model. We theoretically prove that our bidirectional attention prefix preserves node permutation equivariance while maintaining exact backward compatibility with the pretrained base model. Extensive evaluations demonstrate that a 1B-parameter GTLM matches or exceeds the performance of 7B-parameter state-of-the-art models on standard Text-Attributed Graph benchmarks, while significantly surpassing baselines on GraphQA. Finally, we demonstrate that GTLM attention heads implicitly learn to simulate message passing, explaining its superior performance on algorithmic tasks. This paradigm shift enables true algorithmic reasoning within LLMs and provides a scalable foundation for next-generation GraphRAG and relational deep learning.
匹配关键词: reasoning
---

[ACADEMIC - ARXIV]
标题: To Redact, or not to Redact? A Local LLM Approach to Deliberative Process Privilege Classification
作者: Maik Larooij, David Graus
链接: https://arxiv.org/abs/2605.10211v1
完整摘要: Government transparency laws, like the Freedom of Information (FOIA) acts in the United States and United Kingdom, and the Woo (Open Government Act) in the Netherlands, grant citizens the right to directly request documents from the government. As these documents might contain sensitive information, such as personal information or threats to national security, the laws allow governments to redact sensitive parts of the documents prior to release. We build on prior research to perform automatic sensitivity classification for the FOIA Exemption 5 deliberative process privilege using Large Language Models (LLMs). However, processing documents not yet cleared for review via third-party cloud APIs is often legally or politically untenable. Therefore, in this work, we perform sensitivity classification with a small, local model, deployable on consumer-grade hardware (Qwen3.5 9B). We compare eight variants of applying LLMs for sentence classification, using well-known prompting techniques, and find that a combination of Chain-of-Thought prompting and few-shot prompting with error-based examples outperforms classification models of earlier work in terms of recall and F2 score. This method also closely approaches the performance of a widely-used, cost-efficient commercial model (Gemini 2.5 Flash). In an additional analysis, we find that sentences that are predicted as deliberative contain more verbs that indicate the expression of opinions, and are more often phrased in in first-person. Above all, deliberativeness seems characterized by the presence of a combination of multiple indicators, in particular the combination of first-person words with a verb for expressing opinion.
匹配关键词: chain-of-thought
---

[ACADEMIC - ARXIV]
标题: Breaking the Reward Barrier: Accelerating Tree-of-Thought Reasoning via Speculative Exploration
作者: Shuzhang Zhong, Haochen Huang, Shengxuan Qiu, Pengfei Zuo, Runsheng Wang, Meng Li
链接: https://arxiv.org/abs/2605.10195v1
完整摘要: Tree-of-Thought (ToT) reasoning structures Large Language Model (LLM) inference as a tree-based search, demonstrating strong potential for solving complex mathematical and programming tasks. However, its efficiency is constrained by the reward dependency barrier -- a synchronization bottleneck caused by sequential reward-guided exploration that limits search parallelism and introduces substantial latency. Prior system optimizations, mainly designed for linear Chain-of-Thought (CoT) reasoning, cannot address these challenges, leaving the efficiency of ToT underexplored. To enhance ToT reasoning efficiency, we observe that the reasoning paths can be explored speculatively to break the reward synchronization barrier. Therefore, in this paper, we propose SPEX and introduce three key techniques: (i) intra-query speculative path selection to predict and expand high-potential branches of ToT, (ii) inter-query budget allocation to balance speculative resource allocation across queries dynamically, and (iii) adaptive early termination to prune deep and redundant branches for a skewed search tree. We implement SPEX on top of the SGLang framework and evaluate it across diverse ToT algorithms and LLMs. Extensive experiments show that SPEX achieves $1.2 \sim 3 \times$ speedup for different ToT reasoning algorithms. Moreover, SPEX synergizes with token-level speculative decoding, achieving cumulative speedups of up to $4.1\times$. Ablation studies further confirm the contributions of each technique. Overall, SPEX represents a significant step toward efficient and scalable ToT reasoning, unlocking the parallelism required for high-performance inference-time scaling for LLMs.
匹配关键词: chain-of-thought
---

[ACADEMIC - ARXIV]
标题: Separate First, Fuse Later: Mitigating Cross-Modal Interference in Audio-Visual LLMs Reasoning with Modality-Specific Chain-of-Thought
作者: Xuanchen Li, Yuheng Lu, Chenrui Cui, Tianrui Wang, Zikang Huang, Yu Jiang, Long Zhou, Longbiao Wang, Jianwu Dang
链接: https://arxiv.org/abs/2605.09906v1
完整摘要: Audio and vision provide complementary evidence for audio-visual question answering, yet current audio-visual large language models may suffer from cross-modal interference: information from one modality misguides the interpretation of another, thereby inducing hallucinations. We attribute this issue to uncontrolled cross-modal interactions during intermediate reasoning. To mitigate this, we propose Separate First, Fuse Later (SFFL), an audio-visual reasoning framework designed to reduce cross-modal interference. SFFL enforces modality-specific chain-of-thought reasoning, producing separate audio and visual reasoning traces and integrating evidence for answering. We construct modality-preference labels via a data pipeline under different modality input settings. We use these labels as an auxiliary reward in reinforcement learning to encourage a instance-dependent preference for modality cues when answering. We further introduce a modality-specific reasoning mechanism that preserves modality isolation during the separated reasoning stage while enabling full access to cross-modal information at the evidence fusion stage. Experiments demonstrate consistent improvements in both accuracy and robustness, yielding an average relative gain of 5.16\% on general AVQA benchmarks and 11.17\% on a cross-modal hallucination benchmark.
匹配关键词: chain-of-thought
---

[ACADEMIC - ARXIV]
标题: Extending Confidence-Based Text2Cypher with Grammar and Schema Aware Filtering
作者: Makbule Gulcin Ozsoy
链接: https://arxiv.org/abs/2605.10318v1
完整摘要: Large language models (LLMs) allow users to query databases using natural language by translating questions into executable queries. Despite strong progress on tasks such as Text2SQL, Text2SPARQL, and Text2Cypher, most existing methods focus on better prompting, fine-tuning, or iterative refinement. However, they often do not explicitly enforce structural constraints, such as syntactic validity and schema consistency. This can reduce reliability, since generated queries must satisfy both syntax rules and database schema constraints to be executable. In this work, we study how structured constraints can be used in test-time inference for Text2Cypher. We focus on post-generation validation to improve query correctness. We extend a confidence-based inference framework with a sequential filtering process that combines confidence scoring, grammar validation, and schema constraints before final aggregation. This lets us analyze how different constraint types affect generated queries. Our experiments with two instruction-tuned models show that grammar-based filtering improves syntactic validity. Schema-aware filtering further improves execution quality by enforcing consistency with the database structure. However, stronger filtering also increases the number of empty predictions and reduces execution coverage. Overall, we show that adding simple structural checks at test time improves the reliability of Text2Cypher generation, and we provide a clearer view of how syntax and schema constraints contribute differently.
匹配关键词: test-time compute
---

[ACADEMIC - ARXIV]
标题: PaMoSplat: Part-Aware Motion-Guided Gaussian Splatting for Dynamic Scene Reconstruction
作者: Yinan Deng, Jianyu Dou, Jiahui Wang, Jingyu Zhao, Yi Yang, Yufeng Yue
链接: https://arxiv.org/abs/2605.10307v1
完整摘要: Dynamic scene reconstruction represents a fundamental yet demanding challenge in computer vision and robotics. While recent progress in 3DGS-based methods has advanced dynamic scene modeling, obtaining high-fidelity rendering and accurate tracking in scenarios with substantial, intricate motions remains significantly challenging. To address these challenges, we propose PaMoSplat, a novel dynamic Gaussian splatting framework incorporating part awareness and motion priors. Our approach is grounded in two key observations: 1) Parts serve as primitives for scene deformation, and 2) Motion cues from optical flow can effectively guide part motion. Specifically, PaMoSplat initializes by lifting multi-view segmentation masks into 3D space via graph clustering, establishing coherent Gaussian parts. For subsequent timestamps, we leverage a differential evolutionary algorithm to estimate the rigid motion of these parts using multi-view optical flow cues, providing a robust warm-start for further optimization. Additionally, PaMoSplat introduces an adaptive iteration count mechanism, internal learnable rigidity, and flow-supervised rendering loss to accelerate and optimize the training process. Comprehensive evaluations across diverse scenes, including real-world environments, demonstrate that PaMoSplat delivers superior rendering quality, improved tracking precision, and faster convergence compared to existing methods. Furthermore, it enables multiple part-level downstream applications, such as 4D scene editing.
匹配关键词: test-time compute
---

[ACADEMIC - ARXIV]
标题: Follow the Mean: Reference-Guided Flow Matching
作者: Pedro M. P. Curvo, Maksim Zhdanov, Floor Eijkelboom, Jan-Willem van de Meent
链接: https://arxiv.org/abs/2605.10302v1
完整摘要: Existing approaches to controllable generation typically rely on fine-tuning, auxiliary networks, or test-time search. We show that flow matching admits a different control interface: adaptation through examples. For deterministic interpolants, the velocity field is solely governed by a conditional endpoint mean; shifting this mean shifts the flow itself. This yields a simple principle for controllable generation: steer a pretrained model by changing the reference set it follows. We instantiate this idea in two forms. Reference-Mean Guidance is training-free: it computes a closed-form endpoint-mean correction from a reference bank and applies it to a frozen FLUX.2-klein (4B) model, enabling control of color, identity, style, and structure while keeping the prompt, seed, and weights fixed. Semi-Parametric Guidance amortizes the same idea through an explicit mean anchor and learned residual refiner, matching unconditional DiT-B/4 quality on AFHQv2 while allowing the reference set to be swapped at inference time. These results point to a broader direction: generative models that adapt through data, not parameter updates.
匹配关键词: test-time compute
---

[ACADEMIC - ARXIV]
标题: Increasing the Efficiency of DETR for Maritime High-Resolution Images
作者: Tinsae Yehuala, Hao Cheng, Ville Lehtola
链接: https://arxiv.org/abs/2605.10269v1
完整摘要: Maritime object detection is critical for the safe navigation of unmanned surface vessels (USVs), requiring accurate recognition of obstacles from small buoys to large vessels. Real-time detection is challenging due to long distances, small object sizes, large-scale variations, edge computing limitations, and the high memory demands of high-resolution imagery. Existing solutions, such as downsampling or image splitting, often reduce accuracy or require additional processing, while memory-efficient models typically handle only limited resolutions. To overcome these limitations, we leverage Vision Mamba (ViM) backbones, which build on State Space Models (SSMs) to capture long-range dependencies while scaling linearly with sequence length. Images are tokenized into sequences for efficient high-resolution processing. For further computational efficiency, we design a tailored Feature Pyramid Network with successive downsampling and SSM layers, as well as token pruning to reduce unnecessary computation on background regions. Compared to state-of-the-art methods like RT-DETR with ResNet50 backbone, our approach achieves a better balance between performance and computational efficiency in maritime object detection.
匹配关键词: test-time compute
---

[ACADEMIC - ARXIV]
标题: MemReread: Enhancing Agentic Long-Context Reasoning via Memory-Guided Rereading
作者: Baibei Ji, Xiaoyang Weng, Juntao Li, Zecheng Tang, Yihang Lou, Min Zhang
链接: https://arxiv.org/abs/2605.10268v1
完整摘要: To tackle long-context reasoning tasks without the quadratic complexity of standard attention mechanisms, approaches based on agent memory have emerged, which typically maintain a dynamically updated memory when linearly processing document chunks. To mitigate the potential loss of latent evidence in this memorize-while-reading paradigm, recent works have integrated retrieval modules that allow agents to recall information previously discarded during memory overwriting. However, retrieval-based recall suffers from both evidence loss during memory formation and interference induced by invalid queries. To overcome these limitations, we propose MemReread. Built upon streaming reading, MemReread circumvents intermediate retrieval. It triggers question decomposition and rereading when the final memory is insufficient, enabling the recovery of indirect facts that were prematurely discarded. This design supports non-linear reasoning while preserving the inherent logical flow of document comprehension. To further enhance practicality, we introduce a reinforcement learning framework that enhances length extrapolation capability while dynamically determining the number of rereading passes based on task complexity, thereby flexibly controlling computational overhead. Extensive experiments demonstrate that MemReread consistently outperforms baseline frameworks on long-context reasoning tasks, while maintaining linear time complexity with respect to context length.
匹配关键词: test-time compute
---

[ACADEMIC - ARXIV]
标题: Knowledge Poisoning Attacks on Medical Multi-Modal Retrieval-Augmented Generation
作者: Peiru Yang, Haoran Zheng, Tong Ju, Shiting Wang, Wanchun Ni, Jiajun Liu, Shangguang Wang, Yongfeng Huang, Tao Qi
链接: https://arxiv.org/abs/2605.10253v1
完整摘要: Retrieval-augmented generation (RAG) is a widely adopted paradigm for enhancing LLMs in medical applications by incorporating expert multimodal knowledge during generation. However, the underlying retrieval databases may naturally contain, or be intentionally injected with, adversarial knowledge, which can perturb model outputs and undermine system reliability. To investigate this risk, prior studies have explored knowledge poisoning attacks in medical RAG systems. Nevertheless, most of them rely on the strong assumption that adversaries possess prior knowledge of user queries, which is unrealistic in deployments and substantially limits their practical applicability. In this paper, we propose M\textsuperscript{3}Att, a knowledge-poisoning framework designed for medical multimodal RAG systems, assuming only limited distribution knowledge of the underlying database. Our core idea is to inject covert misinformation into textual data while using paired visual data as a query-agnostic trigger to promote retrieval. We first propose a unified framework that introduces imperceptible perturbations to visual inputs to manipulate retrieval probabilities. Besides, due to the prior medical knowledge in LLMs, naively poisoned medical content with explicit factual errors can be corrected during generation. Thus, we leverage the inherent ambiguity of medical diagnosis and design a covert misinformation injection strategy that degrades diagnostic accuracy while evading model self-correction. Experiments on five LLMs and datasets demonstrate that M\textsuperscript{3}Att consistently produces clinically plausible yet incorrect generations. Codes: https://github.com/ypr17/M3Att.
匹配关键词: self-consistency
---

[ACADEMIC - ARXIV]
标题: One-Step Graph-Structured Neural Flows for Irregular Multivariate Time Series Classification
作者: Mengzhou Gao, Kaiwei Wang, Pengfei Jiao
链接: https://arxiv.org/abs/2605.10179v1
完整摘要: Neural Flows efficiently model irregular multivariate time series by directly learning ODE solution trajectories with neural networks, bypassing step-by-step numerical solvers. Despite their efficiency, many existing approaches treat variables independently, leaving inter-variable interactions underexplored. Moreover, their one-step mapping makes interaction modeling inherently challenging, as it removes the iterative refinement of interactions during learning. To address this challenge, we propose one-step Graph-Structured Neural Flows (GSNF), which introduce two auxiliary-trajectory self-supervision strategies to strengthen interaction learning: (i) interaction-aware trajectory generation via re-initialization, which induces trajectory divergence to expose graph-induced interactions, with a theoretically derived lower bound on divergence; and (ii) reverse-time trajectory generation, which enforces forward-backward consistency to regularize graph learning, enabled by flow invertibility. Experiments on five real-world datasets show that GSNF achieves state-of-the-art classification performance with highly competitive training time and memory usage.
匹配关键词: self-consistency
---

[ACADEMIC - ARXIV]
标题: Synthetic Pre-Pre-Training Improves Language Model Robustness to Noisy Pre-Training Data
作者: Xu Guo, Runyu Peng, Jian Tong, Yunhua Zhou, Haijun Lv, Zhihui Lu, Qipeng Guo
链接: https://arxiv.org/abs/2605.10129v1
完整摘要: Large language models (LLMs) rely on web-scale corpora for pre-training. The noise inherent in these datasets tends to obscure meaningful patterns and ultimately degrade model performance. Data curation mitigates but cannot eliminate such noise, so pre-training corpora remain noisy in practice. We therefore study whether a lightweight pre-pre-training (PPT) stage based on synthetic data with learnable temporal structure helps resist noisy data during the pre-training (PT) stage. Across various corruption settings, our method consistently improves robustness to noise during PT, with larger relative gains at higher noise levels. For a 1B-parameter model, a synthetic PPT stage with only 65M tokens achieves the same final loss as the baseline while using up to 49\% fewer natural-text PT tokens across different noise levels. Mechanistic analyses suggest PPT does not immediately suppress attention to noisy tokens. Rather, PPT-initialized models gradually downweight attention between corrupted tokens during noisy PT. This indicates that synthetic PPT inhibits noise self-modeling and shapes the subsequent optimization trajectory. Code is available at https://github.com/guox18/formal-language-prepretraining.
匹配关键词: self-consistency
---

[ACADEMIC - ARXIV]
标题: FERA: Uncertainty-Aware Federated Reasoning for Large Language Models
作者: Ruhan Wang, Chengkai Huang, Zhiyong Wang, Junda Wu, Rui Wang, Tong Yu, Julian McAuley, Lina Yao, Dongruo Zhou
链接: https://arxiv.org/abs/2605.10082v1
完整摘要: Large language models (LLMs) exhibit strong reasoning capabilities when guided by high-quality demonstrations, yet such data is often distributed across organizations that cannot centralize it due to regulatory, proprietary, or institutional constraints. We study federated reasoning, where a server improves multi-step reasoning by coordinating with heterogeneous clients holding private demonstrations, without centralized training or raw data sharing. The key challenge is that client reliability is query-dependent, while the server cannot inspect client data to determine which contributions are trustworthy. To address this, we propose Uncertainty-Aware Federated Reasoning (FERA), a training-free framework based on iterative server-client co-refinement. Across communication rounds, clients generate reasoning traces with lightweight uncertainty estimates, and the server synthesizes them into improved reasoning that is redistributed as context for the next round, progressively improving both server outputs and client-side reasoning. Within each round, Uncertainty-Aware Self-Critique Aggregation (UA-SCA) resolves conflicts among heterogeneous client traces through query-dependent trust weighting and structured cross-client verification. Rather than simply discarding low-quality traces, UA-SCA revises flawed reasoning steps to recover useful information. We provide theoretical guarantees showing that the proposed iterative protocol converges and that uncertainty-aware weighting accelerates convergence. Experiments on multiple reasoning benchmarks show that FERA consistently outperforms both federated training and training-free baselines, achieving progressively higher accuracy across rounds while maintaining communication and computational efficiency.
匹配关键词: self-consistency
---

[ACADEMIC - ARXIV]
标题: Swarm Skills: A Portable, Self-Evolving Multi-Agent System Specification for Coordination Engineering
作者: Xinyu Zhang, Zhicheng Dou, Deyang Li, Jianjun Tao, Shuo Cheng, Ruifeng Shi, Fangchao Liu, Enrui Hu, Yangkai Ding, Hongbo Wang, Qi Ye, Xuefeng Jin, Zhangchun Zhao
链接: https://arxiv.org/abs/2605.10052v1
完整摘要: As artificial intelligence engineering paradigms shift from single-agent Prompt and Context Engineering toward multi-agent \textbf{Coordination Engineering}, the ability to codify and systematically improve how multiple agents collaborate has emerged as a critical bottleneck. While single-agent skills can now be distributed as portable assets, multi-agent coordination protocols remain locked within framework-internal code or static configurations, preventing them from being shared across systems or autonomously improved over time. We propose \textbf{Swarm Skills}, a portable specification that extends the Anthropic Skills standard with multi-agent semantics. Swarm Skills turns multi-agent workflows into first-class, distributable assets that consist of roles, workflows, execution bounds, and a built-in semantic structure for self-evolution. To operationalize the specification's evolving nature, we present a companion self-evolution algorithm that automatically distills successful execution trajectories into new Swarm Skills and continuously patches existing ones based on multi-dimensional scoring (Effectiveness, Utilization, and Freshness), eliminating the need for human-in-the-loop oversight during the refinement process. Through an architectural compatibility analysis and a comprehensive qualitative case study using the open-source JiuwenSwarm reference implementation, we demonstrate how Swarm Skills achieves zero-adapter cross-agent portability via progressive disclosure, enabling agent teams to self-evolve their coordination strategies without framework lock-in.
匹配关键词: self-consistency
---

[ACADEMIC - ARXIV]
标题: Extending Confidence-Based Text2Cypher with Grammar and Schema Aware Filtering
作者: Makbule Gulcin Ozsoy
链接: https://arxiv.org/abs/2605.10318v1
完整摘要: Large language models (LLMs) allow users to query databases using natural language by translating questions into executable queries. Despite strong progress on tasks such as Text2SQL, Text2SPARQL, and Text2Cypher, most existing methods focus on better prompting, fine-tuning, or iterative refinement. However, they often do not explicitly enforce structural constraints, such as syntactic validity and schema consistency. This can reduce reliability, since generated queries must satisfy both syntax rules and database schema constraints to be executable. In this work, we study how structured constraints can be used in test-time inference for Text2Cypher. We focus on post-generation validation to improve query correctness. We extend a confidence-based inference framework with a sequential filtering process that combines confidence scoring, grammar validation, and schema constraints before final aggregation. This lets us analyze how different constraint types affect generated queries. Our experiments with two instruction-tuned models show that grammar-based filtering improves syntactic validity. Schema-aware filtering further improves execution quality by enforcing consistency with the database structure. However, stronger filtering also increases the number of empty predictions and reduces execution coverage. Overall, we show that adding simple structural checks at test time improves the reliability of Text2Cypher generation, and we provide a clearer view of how syntax and schema constraints contribute differently.
匹配关键词: process reward
---

[ACADEMIC - ARXIV]
标题: Signature Approach for Contextual Bandits with Nonlinear and Path-dependent Rewards
作者: Xin Guo, Grace He, Xinyu Li
链接: https://arxiv.org/abs/2605.10313v1
完整摘要: We study contextual bandits with nonlinear and path-dependent rewards through a novel signature-transform-based approach. Leveraging the universal nonlinearity property of signatures, we approximate continuous path-dependent reward functionals by linear functionals in the signature space. This representation enables the use of efficient linear contextual bandit methods while preserving expressive sequential structure. Building on this framework, we propose \texttt{DisSigUCB}, a signature-based disjoint upper confidence bound (UCB) algorithm. Under boundedness and non-degeneracy assumptions, we prove a high-probability data-dependent sublinear regret bound of order \(\tilde{\mathcal O}(\sqrt{(d+m)KT})\) where \(d\) is the context dimension and \(m\) is the signature feature dimension. Synthetic experiments and numerical applications on temperature sensor monitoring, sleep-stage classification, and hospital nurse staffing demonstrate that \texttt{DisSigUCB} consistently outperforms classical linear and kernelized contextual bandit baselines in nonlinear and path-dependent settings.
匹配关键词: process reward
---

[ACADEMIC - ARXIV]
标题: PaMoSplat: Part-Aware Motion-Guided Gaussian Splatting for Dynamic Scene Reconstruction
作者: Yinan Deng, Jianyu Dou, Jiahui Wang, Jingyu Zhao, Yi Yang, Yufeng Yue
链接: https://arxiv.org/abs/2605.10307v1
完整摘要: Dynamic scene reconstruction represents a fundamental yet demanding challenge in computer vision and robotics. While recent progress in 3DGS-based methods has advanced dynamic scene modeling, obtaining high-fidelity rendering and accurate tracking in scenarios with substantial, intricate motions remains significantly challenging. To address these challenges, we propose PaMoSplat, a novel dynamic Gaussian splatting framework incorporating part awareness and motion priors. Our approach is grounded in two key observations: 1) Parts serve as primitives for scene deformation, and 2) Motion cues from optical flow can effectively guide part motion. Specifically, PaMoSplat initializes by lifting multi-view segmentation masks into 3D space via graph clustering, establishing coherent Gaussian parts. For subsequent timestamps, we leverage a differential evolutionary algorithm to estimate the rigid motion of these parts using multi-view optical flow cues, providing a robust warm-start for further optimization. Additionally, PaMoSplat introduces an adaptive iteration count mechanism, internal learnable rigidity, and flow-supervised rendering loss to accelerate and optimize the training process. Comprehensive evaluations across diverse scenes, including real-world environments, demonstrate that PaMoSplat delivers superior rendering quality, improved tracking precision, and faster convergence compared to existing methods. Furthermore, it enables multiple part-level downstream applications, such as 4D scene editing.
匹配关键词: process reward
---

[ACADEMIC - ARXIV]
标题: Nearly-Optimal Algorithm for Adversarial Kernelized Bandits
作者: Shogo Iwazaki
链接: https://arxiv.org/abs/2605.10299v1
完整摘要: This paper studies kernelized bandits (also known as Gaussian process bandits) in an adversarial environment, where the reward functions in a known reproducing kernel Hilbert space (RKHS) may be adversarially chosen at each round. We show that the exponential-weight algorithm achieves $\tilde{O}(\sqrt{T γ_T})$ adversarial regret, where $T$ and $γ_T$ denote the number of total rounds and the maximum information gain, respectively. For squared exponential (SE) and $ν$-Matérn kernels, we also show algorithm-independent lower bounds that guarantee the optimality of our algorithm up to polylogarithmic factors. Furthermore, we present a computationally efficient variant of our algorithm using Nyström approximation while maintaining nearly optimal regret guarantees.
匹配关键词: process reward
---

[ACADEMIC - ARXIV]
标题: LeapTS: Rethinking Time Series Forecasting as Adaptive Multi-Horizon Scheduling
作者: Sheng Pan, Ming Jin, Bo Du, Shirui Pan
链接: https://arxiv.org/abs/2605.10292v1
完整摘要: Time series forecasting serves as an essential tool for many real-world applications, supporting tasks such as resource optimization and decision-making. Despite significant architectural advancements, most modern models still treat forecasting task as a fixed mapping from history to target horizons. This induces temporal decoupling across future time points and limits the model's ability to adapt to the evolving context as forecasting progresses. In this work, we present LeapTS, a novel framework that reformulates time series forecasting as a dynamic scheduling process over the prediction horizon. Specifically, LeapTS organizes the forecasting process into multi-level decisions using: (1) the hierarchical controller to dynamically select the optimal prediction scale and advancement length at each step, and (2) continuous-time state evolution driven by neural controlled differential equations. Within this process, the controlled update mechanism explicitly couples the irregular temporal dynamics with discrete scheduling feedback. Extensive evaluations on both real-world and synthetic datasets demonstrate that LeapTS improves overall forecasting performance by at least 7.4% while achieving a 2.6$\times$ to 5.3$\times$ inference speedup over representative Transformer-based models. Furthermore, by explicitly tracing the scheduling trajectories, we reveal how the model autonomously adapts its forecasting behavior to capture non-stationary dynamics.
匹配关键词: process reward
---

[ACADEMIC - ARXIV]
标题: Follow the Mean: Reference-Guided Flow Matching
作者: Pedro M. P. Curvo, Maksim Zhdanov, Floor Eijkelboom, Jan-Willem van de Meent
链接: https://arxiv.org/abs/2605.10302v1
完整摘要: Existing approaches to controllable generation typically rely on fine-tuning, auxiliary networks, or test-time search. We show that flow matching admits a different control interface: adaptation through examples. For deterministic interpolants, the velocity field is solely governed by a conditional endpoint mean; shifting this mean shifts the flow itself. This yields a simple principle for controllable generation: steer a pretrained model by changing the reference set it follows. We instantiate this idea in two forms. Reference-Mean Guidance is training-free: it computes a closed-form endpoint-mean correction from a reference bank and applies it to a frozen FLUX.2-klein (4B) model, enabling control of color, identity, style, and structure while keeping the prompt, seed, and weights fixed. Semi-Parametric Guidance amortizes the same idea through an explicit mean anchor and learned residual refiner, matching unconditional DiT-B/4 quality on AFHQv2 while allowing the reference set to be swapped at inference time. These results point to a broader direction: generative models that adapt through data, not parameter updates.
匹配关键词: pretraining
---

[ACADEMIC - ARXIV]
标题: Teaching LLMs to See Graphs: Unifying Text and Structural Reasoning
作者: Dario Vajda
链接: https://arxiv.org/abs/2605.10247v1
完整摘要: Using Large Language Models (LLMs) to process graph-structured data is an active research area, yet current state-of-the-art approaches typically rely on multi-step pipelines with Graph Neural Network (GNN) encoders that compress rich textual attributes into solitary tokens, creating a significant semantic bottleneck. In this paper, we introduce the Graph Transformer Language Model (GTLM), a novel architecture that enables pretrained LLMs to natively process graph topologies while entirely eliminating this compressive bottleneck. GTLM is exceptionally parameter-efficient: by injecting graph-aware attention biases directly into the LLM's attention modules, it introduces only 0.015% additional parameters relative to the base model. We theoretically prove that our bidirectional attention prefix preserves node permutation equivariance while maintaining exact backward compatibility with the pretrained base model. Extensive evaluations demonstrate that a 1B-parameter GTLM matches or exceeds the performance of 7B-parameter state-of-the-art models on standard Text-Attributed Graph benchmarks, while significantly surpassing baselines on GraphQA. Finally, we demonstrate that GTLM attention heads implicitly learn to simulate message passing, explaining its superior performance on algorithmic tasks. This paradigm shift enables true algorithmic reasoning within LLMs and provides a scalable foundation for next-generation GraphRAG and relational deep learning.
匹配关键词: pretraining
---

[ACADEMIC - ARXIV]
标题: ProteinOPD: Towards Effective and Efficient Preference Alignment for Protein Design
作者: Yulin Zhang, He Cao, Zihao Jiang, Chenyi Zi, Zhipeng Zhou, Zijing Liu, Yu Li, Jia Li, Ziqi Gao
链接: https://arxiv.org/abs/2605.10189v1
完整摘要: Designing proteins with desired functions or properties represents a core goal in synthetic biology and drug discovery. Recent advances in protein language models (PLMs) have enabled the generation of highly designable protein sequences, while preference alignment provides a promising way to steer designs toward desired functions and properties. Nevertheless, they often trigger catastrophic forgetting of pretrained knowledge, degrading basic designability and failing to balance multiple competing objectives. To address these issues, we draw inspiration from On-Policy Distillation (OPD), an advanced post-training method renowned for mitigating catastrophic forgetting through its mode-seeking nature. In this work, we propose ProteinOPD, a multi-objective preference alignment framework that can effectively balance multiple preference objectives while maintaining the inherent designability of PLMs. ProteinOPD adapts a pretrained PLM into preference-specific teachers and distills their knowledge into a shared student via token-level OPD on the student's own trajectories. During this process, the student is aligned to a unique normalized geometric consensus of weighted teachers while ensuring bounded optimization under conflicts. This bridges the gap for OPD in multi-objective/teacher alignment. Extensive experiments show that ProteinOPD achieves substantial gains on target preference objectives without compromising the designability, with an 8x training speedup over RL-based alignment competitors.
匹配关键词: pretraining
---

[ACADEMIC - ARXIV]
标题: LegalCiteBench: Evaluating Citation Reliability in Legal Language Models
作者: Sijia Chen, Hang Yin, Shunfan Zhou
链接: https://arxiv.org/abs/2605.10186v1
完整摘要: Large language models (LLMs) are increasingly integrated into legal drafting and research workflows, where incorrect citations or fabricated precedents can cause serious professional harm. Existing legal benchmarks largely emphasize statutory reasoning, contract understanding, or general legal question answering, but they do not directly study a central common-law failure mode: when asked to provide case authorities without external grounding, models may return plausible-looking but incorrect citations or cases. We introduce LegalCiteBench, a benchmark for studying closed-book citation recovery, citation verification, and case matching in legal language models. LegalCiteBench contains approximately 24K evaluation instances constructed from 1,000 real U.S. judicial opinions from the Case Law Access Project. The benchmark covers five citation-centric tasks: citation retrieval, citation completion, citation error detection, case matching, and case verification and correction. Across 21 LLMs, exact citation recovery remains highly challenging in this closed-book setting: even the strongest models score below 7/100 on citation retrieval and completion. Within the evaluated models, scale and legal-domain pretraining provide limited gains and do not resolve this difficulty. Models also frequently provide concrete but incorrect or low-overlap authorities under our evaluation protocol, with Misleading Answer Rates (MAR) exceeding 94% for 20 of 21 evaluated models on retrieval-heavy tasks. A prompt-only abstention experiment shows that explicit uncertainty instructions reduce some confident fabrication but do not improve citation correctness. LegalCiteBench is intended as a diagnostic framework for studying authority generation failures, verification behavior, and abstention when external grounding is absent, incomplete, or bypassed.
匹配关键词: pretraining
---

[ACADEMIC - ARXIV]
标题: Developing a foundation model for high-resolution remote sensing data of the Netherlands
作者: Paul Vermeeren, Heysem Kaya
链接: https://arxiv.org/abs/2605.10184v1
完整摘要: We develop a foundation model using 1.2m high resolution satellite images of the Netherlands. By combining a Convolutional Neural Network and a Vision Transformer, the model captures both low- and high-frequency landscape features, such as fine textures, edges, and small objects as well as large terrain structures, elevation patterns, and land-cover distributions. Leveraging temporal data as input, the model learns from broader contextual information across time, allowing the model to exploit the temporal dependencies, such as topographic features, land-cover changes, and seasonal dynamics. These additional constraints reduce feature ambiguity, improve representation learning, and enable better generalization with fewer labeled samples. The foundation model is evaluated on multiple downstream tasks, ranging from use cases within the Netherlands to global benchmarking datasets. On the vegetation monitoring dataset of the Netherlands, the model shows clear performance improvements by incorporating temporal information instead of relying on a single time point. Despite using a smaller model and less pretraining data limited to the Netherlands, it achieves competitive results on global benchmarks when compared to state-of-the-art models. These results demonstrate that the model can learn rich, generalizable representations from limited data, achieving competitive performance on global benchmarks while using a fraction of the parameters of larger state-of-the-art remote sensing models. To maximize reproducibility and reuse, we made the scripts and the model accessible on GitHub.
匹配关键词: pretraining
---

[ACADEMIC - ARXIV]
标题: Extending Confidence-Based Text2Cypher with Grammar and Schema Aware Filtering
作者: Makbule Gulcin Ozsoy
链接: https://arxiv.org/abs/2605.10318v1
完整摘要: Large language models (LLMs) allow users to query databases using natural language by translating questions into executable queries. Despite strong progress on tasks such as Text2SQL, Text2SPARQL, and Text2Cypher, most existing methods focus on better prompting, fine-tuning, or iterative refinement. However, they often do not explicitly enforce structural constraints, such as syntactic validity and schema consistency. This can reduce reliability, since generated queries must satisfy both syntax rules and database schema constraints to be executable. In this work, we study how structured constraints can be used in test-time inference for Text2Cypher. We focus on post-generation validation to improve query correctness. We extend a confidence-based inference framework with a sequential filtering process that combines confidence scoring, grammar validation, and schema constraints before final aggregation. This lets us analyze how different constraint types affect generated queries. Our experiments with two instruction-tuned models show that grammar-based filtering improves syntactic validity. Schema-aware filtering further improves execution quality by enforcing consistency with the database structure. However, stronger filtering also increases the number of empty predictions and reduces execution coverage. Overall, we show that adding simple structural checks at test time improves the reliability of Text2Cypher generation, and we provide a clearer view of how syntax and schema constraints contribute differently.
匹配关键词: foundation model
---

[ACADEMIC - ARXIV]
标题: Relations Are Channels: Knowledge Graph Embedding via Kraus Decompositions
作者: Sayan Kumar Chaki
链接: https://arxiv.org/abs/2605.10317v1
完整摘要: Knowledge graph embedding (KGE) models typically represent each relation as an operator on entity embeddings. In this work, we identify three structural axioms that any principled relation operator must satisfy, linearity, trace preservation, and complete positivity, and show that they characterize a Kraus channel structure via the Kraus representation theorem. The completeness constraint defining this family is equivalent to these axioms, providing a principled foundation rather than an externally imposed condition. Under this formulation, most existing operator-based KGE models are recoverable as special cases with Kraus rank $κ= 1$ under specific embedding choices. We further generalize this characterization to arbitrary metric geometries by introducing \mbox{w-Kraus} channels, which satisfy completeness by construction within their respective spaces. Building on this theory, we propose \textsc{KrausKGE}, a principled KGE model that naturally handles $1$-to-$N$ and $N$-to-$N$ relations, supports $k$-hop reasoning without requiring explicit path encoders, and eliminates the need for norm constraints on entity embeddings. Additionally, our framework yields the first theoretically grounded per-relation complexity measure in the KGE literature, with a provable lower bound in terms of the empirical relation matrix rank. Empirical evaluation demonstrates that \textsc{KrausKGE} consistently outperforms strong baselines on $N$-to-$N$ relations, with performance gains that increase monotonically with relation fan-out, in alignment with theoretical predictions.
匹配关键词: foundation model
---

[ACADEMIC - ARXIV]
标题: Active Tabular Augmentation via Policy-Guided Diffusion Inpainting
作者: Zheyu Zhang, Shuo Yang, Bardh Prenkaj, Gjergji Kasneci
链接: https://arxiv.org/abs/2605.10315v1
完整摘要: Generative tabular augmentation is appealing in data-scarce domains, yet the prevailing focus on distributional fidelity does not reliably translate into better downstream models. We formalize a fidelity-utility gap: common generative objectives prioritize distributional plausibility, whereas augmentation succeeds only when injected samples reduce the current learner's held-out evaluation loss. This gap motivates learning not just how to generate, but what to generate and when to inject as training evolves. We propose TAP (Tabular Augmentation Policy), which couples diffusion inpainting with a lightweight, learner-conditioned policy to steer generation toward high-utility regions and controls safe injection via explicit gating and conservative windowed commitment. Under severe data scarcity, TAP consistently outperforms strong generative baselines on seven real-world datasets, improving classification accuracy by up to 15.6 percentage points and reducing regression RMSE by up to 32%.
匹配关键词: foundation model
---

[ACADEMIC - ARXIV]
标题: PaMoSplat: Part-Aware Motion-Guided Gaussian Splatting for Dynamic Scene Reconstruction
作者: Yinan Deng, Jianyu Dou, Jiahui Wang, Jingyu Zhao, Yi Yang, Yufeng Yue
链接: https://arxiv.org/abs/2605.10307v1
完整摘要: Dynamic scene reconstruction represents a fundamental yet demanding challenge in computer vision and robotics. While recent progress in 3DGS-based methods has advanced dynamic scene modeling, obtaining high-fidelity rendering and accurate tracking in scenarios with substantial, intricate motions remains significantly challenging. To address these challenges, we propose PaMoSplat, a novel dynamic Gaussian splatting framework incorporating part awareness and motion priors. Our approach is grounded in two key observations: 1) Parts serve as primitives for scene deformation, and 2) Motion cues from optical flow can effectively guide part motion. Specifically, PaMoSplat initializes by lifting multi-view segmentation masks into 3D space via graph clustering, establishing coherent Gaussian parts. For subsequent timestamps, we leverage a differential evolutionary algorithm to estimate the rigid motion of these parts using multi-view optical flow cues, providing a robust warm-start for further optimization. Additionally, PaMoSplat introduces an adaptive iteration count mechanism, internal learnable rigidity, and flow-supervised rendering loss to accelerate and optimize the training process. Comprehensive evaluations across diverse scenes, including real-world environments, demonstrate that PaMoSplat delivers superior rendering quality, improved tracking precision, and faster convergence compared to existing methods. Furthermore, it enables multiple part-level downstream applications, such as 4D scene editing.
匹配关键词: foundation model
---

[ACADEMIC - ARXIV]
标题: Follow the Mean: Reference-Guided Flow Matching
作者: Pedro M. P. Curvo, Maksim Zhdanov, Floor Eijkelboom, Jan-Willem van de Meent
链接: https://arxiv.org/abs/2605.10302v1
完整摘要: Existing approaches to controllable generation typically rely on fine-tuning, auxiliary networks, or test-time search. We show that flow matching admits a different control interface: adaptation through examples. For deterministic interpolants, the velocity field is solely governed by a conditional endpoint mean; shifting this mean shifts the flow itself. This yields a simple principle for controllable generation: steer a pretrained model by changing the reference set it follows. We instantiate this idea in two forms. Reference-Mean Guidance is training-free: it computes a closed-form endpoint-mean correction from a reference bank and applies it to a frozen FLUX.2-klein (4B) model, enabling control of color, identity, style, and structure while keeping the prompt, seed, and weights fixed. Semi-Parametric Guidance amortizes the same idea through an explicit mean anchor and learned residual refiner, matching unconditional DiT-B/4 quality on AFHQv2 while allowing the reference set to be swapped at inference time. These results point to a broader direction: generative models that adapt through data, not parameter updates.
匹配关键词: foundation model
---

[ACADEMIC - ARXIV]
标题: Set Prediction for Next-Day Active Fire Forecasting
作者: Yuchen Bai, Georgios Athanasiou, Xin Yu, Diogenis Antonopoulos, Ioannis Papoutsis, Stijn Hantson, Nuno Carvalhais
链接: https://arxiv.org/abs/2605.10298v1
完整摘要: Accurate next-day active fire forecasts can support early warning, disaster response, forest risk assessment, and downstream estimation of fire-related carbon emissions. Existing machine learning approaches to wildfire forecasting typically predict wildfire danger or fire probability on kilometre-scale daily grids, which is useful for regional warning but does not directly represent localized fire events. We propose Wildfire Ignition Set Predictor (WISP), a query-based model that reformulates next-day active fire forecasting as point-set prediction. From 48 hours of covariates including meteorology, satellite vegetation products, static land, and fire history, WISP predicts a fixed-size ranked set of future active fire cluster centres on a 375 m grid across globally distributed regions. The model is trained end-to-end with Hungarian matching; to address the conflicting roles of the classification score in assignment, ranking, and query activation, we use asymmetric classification-localization weighting in matching and loss. We further construct a globally distributed, hourly, multi-source benchmark for this task. On a held-out test set spanning fire regions worldwide, the best WISP variant achieves 38.2% average precision (AP) for ranked fire-centre detections, covers 53.4% of fire cluster mass weighted by fire radiative power (FRP), and localizes 54.1% of observed clusters within 5 km. These results establish sparse set prediction as a viable formulation for high-resolution wildfire forecasting and provide a benchmark for future work in this regime.
匹配关键词: scaling law
---

[ACADEMIC - ARXIV]
标题: LeapTS: Rethinking Time Series Forecasting as Adaptive Multi-Horizon Scheduling
作者: Sheng Pan, Ming Jin, Bo Du, Shirui Pan
链接: https://arxiv.org/abs/2605.10292v1
完整摘要: Time series forecasting serves as an essential tool for many real-world applications, supporting tasks such as resource optimization and decision-making. Despite significant architectural advancements, most modern models still treat forecasting task as a fixed mapping from history to target horizons. This induces temporal decoupling across future time points and limits the model's ability to adapt to the evolving context as forecasting progresses. In this work, we present LeapTS, a novel framework that reformulates time series forecasting as a dynamic scheduling process over the prediction horizon. Specifically, LeapTS organizes the forecasting process into multi-level decisions using: (1) the hierarchical controller to dynamically select the optimal prediction scale and advancement length at each step, and (2) continuous-time state evolution driven by neural controlled differential equations. Within this process, the controlled update mechanism explicitly couples the irregular temporal dynamics with discrete scheduling feedback. Extensive evaluations on both real-world and synthetic datasets demonstrate that LeapTS improves overall forecasting performance by at least 7.4% while achieving a 2.6$\times$ to 5.3$\times$ inference speedup over representative Transformer-based models. Furthermore, by explicitly tracing the scheduling trajectories, we reveal how the model autonomously adapts its forecasting behavior to capture non-stationary dynamics.
匹配关键词: scaling law
---

[ACADEMIC - ARXIV]
标题: AgentRx: A Benchmark Study of LLM Agents for Multimodal Clinical Prediction Tasks
作者: Baraa Al Jorf, Farah E. Shamout
链接: https://arxiv.org/abs/2605.10286v1
完整摘要: Building effective clinical decision support systems requires the synthesis of complex heterogeneous multimodal data. Such modalities include temporal electronic health records data, medical images, radiology reports, and clinical notes. Large language model (LLM)-based agents have shown impressive performance in various healthcare tasks, especially those involving textual modalities. Considering the fragmentation of healthcare data across hospital systems, collaborative agent frameworks present a promising direction to mitigate data sharing challenges. However, the effectiveness of LLM agents for multimodal clinical risk prediction remains largely unexamined. In this work, we conduct a systematic evaluation of LLM-based agents for clinical prediction tasks using large-scale real-world data. We assess performance in unimodal and multimodal settings and quantify performance gaps between single agent and multi-agent systems. Our findings highlight that single agent frameworks outperform naive multi-agent systems, are better at handling multimodal data, and are better calibrated. This underscores a critical need for improving multi-agent collaboration to better handle heterogeneous inputs. By open-sourcing our code and evaluation framework, this work offers a new benchmark to support future developments relating to agentic systems in healthcare.
匹配关键词: scaling law
---

[ACADEMIC - ARXIV]
标题: PolarVSR: A Unified Framework and Benchmark for Continuous Space-Time Polarization Video Reconstruction
作者: Chenggong Li, Yidong Luo, Junchao Zhang, Boxin Shi, Degui Yang
链接: https://arxiv.org/abs/2605.10275v1
完整摘要: Polarimetric imaging captures surface polarization characteristics, such as the Degree of Linear Polarization (DoLP) and the Angle of Polarization (AoP). In mainstream Division of-Focal-Plane (DoFP) color polarization imaging, recovering polarization parameters from captured mosaic arrays remains a challenging inverse problem. Existing DoFP cameras also face hardware bottlenecks and often cannot support high-frame-rate acquisition, limiting polarimetric imaging in dynamic video tasks. These limitations motivate joint spatial and temporal enhancement. To this end, we propose the first space-time polarization video reconstruction architecture. The method jointly models polarization directions in space and time and uses a polarization-aware implicit neural representation for continuous, high-fidelity upsampling. By analyzing temporal variations in polarization parameters, we further introduce a flow-guided polarization variation loss to supervise polarization dynamics. We also establish the first large-scale color DoFP polarization video benchmark to support this research direction. Extensive experiments on this benchmark demonstrate the effectiveness of the method.
匹配关键词: scaling law
---

[ACADEMIC - ARXIV]
标题: DP-LAC: Lightweight Adaptive Clipping for Differentially Private Federated Fine-tuning of Language Models
作者: Haaris Mehmood, Jie Xu, Karthikeyan Saravanan, Rogier Van Dalen, Mete Ozay
链接: https://arxiv.org/abs/2605.10272v1
完整摘要: Federated learning (FL) enables the collaborative training of large-scale language models (LLMs) across edge devices while keeping user data on-device. However, FL still exposes sensitive information through client-provided gradients. Differentially private stochastic gradient descent (DP-SGD) mitigates this risk by clipping each client's contribution to a threshold $C$ and adding noise proportional to $C$. Existing adaptive clipping techniques dynamically adjust $C$ but demand tedious hyperparameter tuning, which can erode the privacy budget. In this paper, we introduce DP-LAC, a method that first estimates an initial clipping threshold within an order of magnitude of the optimum using private histogram estimation, and then adapts this threshold during training without consuming additional privacy budget or introducing new hyperparameters. Empirical results show that DP-LAC outperforms both state-of-the-art adaptive clipping methods and vanilla DP-SGD, achieving an average accuracy gain of $6.6\%$.
匹配关键词: scaling law
---

[ACADEMIC - ARXIV]
标题: Extending Confidence-Based Text2Cypher with Grammar and Schema Aware Filtering
作者: Makbule Gulcin Ozsoy
链接: https://arxiv.org/abs/2605.10318v1
完整摘要: Large language models (LLMs) allow users to query databases using natural language by translating questions into executable queries. Despite strong progress on tasks such as Text2SQL, Text2SPARQL, and Text2Cypher, most existing methods focus on better prompting, fine-tuning, or iterative refinement. However, they often do not explicitly enforce structural constraints, such as syntactic validity and schema consistency. This can reduce reliability, since generated queries must satisfy both syntax rules and database schema constraints to be executable. In this work, we study how structured constraints can be used in test-time inference for Text2Cypher. We focus on post-generation validation to improve query correctness. We extend a confidence-based inference framework with a sequential filtering process that combines confidence scoring, grammar validation, and schema constraints before final aggregation. This lets us analyze how different constraint types affect generated queries. Our experiments with two instruction-tuned models show that grammar-based filtering improves syntactic validity. Schema-aware filtering further improves execution quality by enforcing consistency with the database structure. However, stronger filtering also increases the number of empty predictions and reduces execution coverage. Overall, we show that adding simple structural checks at test time improves the reliability of Text2Cypher generation, and we provide a clearer view of how syntax and schema constraints contribute differently.
匹配关键词: language model
---

[ACADEMIC - ARXIV]
标题: Relations Are Channels: Knowledge Graph Embedding via Kraus Decompositions
作者: Sayan Kumar Chaki
链接: https://arxiv.org/abs/2605.10317v1
完整摘要: Knowledge graph embedding (KGE) models typically represent each relation as an operator on entity embeddings. In this work, we identify three structural axioms that any principled relation operator must satisfy, linearity, trace preservation, and complete positivity, and show that they characterize a Kraus channel structure via the Kraus representation theorem. The completeness constraint defining this family is equivalent to these axioms, providing a principled foundation rather than an externally imposed condition. Under this formulation, most existing operator-based KGE models are recoverable as special cases with Kraus rank $κ= 1$ under specific embedding choices. We further generalize this characterization to arbitrary metric geometries by introducing \mbox{w-Kraus} channels, which satisfy completeness by construction within their respective spaces. Building on this theory, we propose \textsc{KrausKGE}, a principled KGE model that naturally handles $1$-to-$N$ and $N$-to-$N$ relations, supports $k$-hop reasoning without requiring explicit path encoders, and eliminates the need for norm constraints on entity embeddings. Additionally, our framework yields the first theoretically grounded per-relation complexity measure in the KGE literature, with a provable lower bound in terms of the empirical relation matrix rank. Empirical evaluation demonstrates that \textsc{KrausKGE} consistently outperforms strong baselines on $N$-to-$N$ relations, with performance gains that increase monotonically with relation fan-out, in alignment with theoretical predictions.
匹配关键词: language model
---

[ACADEMIC - ARXIV]
标题: Active Tabular Augmentation via Policy-Guided Diffusion Inpainting
作者: Zheyu Zhang, Shuo Yang, Bardh Prenkaj, Gjergji Kasneci
链接: https://arxiv.org/abs/2605.10315v1
完整摘要: Generative tabular augmentation is appealing in data-scarce domains, yet the prevailing focus on distributional fidelity does not reliably translate into better downstream models. We formalize a fidelity-utility gap: common generative objectives prioritize distributional plausibility, whereas augmentation succeeds only when injected samples reduce the current learner's held-out evaluation loss. This gap motivates learning not just how to generate, but what to generate and when to inject as training evolves. We propose TAP (Tabular Augmentation Policy), which couples diffusion inpainting with a lightweight, learner-conditioned policy to steer generation toward high-utility regions and controls safe injection via explicit gating and conservative windowed commitment. Under severe data scarcity, TAP consistently outperforms strong generative baselines on seven real-world datasets, improving classification accuracy by up to 15.6 percentage points and reducing regression RMSE by up to 32%.
匹配关键词: language model
---

[ACADEMIC - ARXIV]
标题: PaMoSplat: Part-Aware Motion-Guided Gaussian Splatting for Dynamic Scene Reconstruction
作者: Yinan Deng, Jianyu Dou, Jiahui Wang, Jingyu Zhao, Yi Yang, Yufeng Yue
链接: https://arxiv.org/abs/2605.10307v1
完整摘要: Dynamic scene reconstruction represents a fundamental yet demanding challenge in computer vision and robotics. While recent progress in 3DGS-based methods has advanced dynamic scene modeling, obtaining high-fidelity rendering and accurate tracking in scenarios with substantial, intricate motions remains significantly challenging. To address these challenges, we propose PaMoSplat, a novel dynamic Gaussian splatting framework incorporating part awareness and motion priors. Our approach is grounded in two key observations: 1) Parts serve as primitives for scene deformation, and 2) Motion cues from optical flow can effectively guide part motion. Specifically, PaMoSplat initializes by lifting multi-view segmentation masks into 3D space via graph clustering, establishing coherent Gaussian parts. For subsequent timestamps, we leverage a differential evolutionary algorithm to estimate the rigid motion of these parts using multi-view optical flow cues, providing a robust warm-start for further optimization. Additionally, PaMoSplat introduces an adaptive iteration count mechanism, internal learnable rigidity, and flow-supervised rendering loss to accelerate and optimize the training process. Comprehensive evaluations across diverse scenes, including real-world environments, demonstrate that PaMoSplat delivers superior rendering quality, improved tracking precision, and faster convergence compared to existing methods. Furthermore, it enables multiple part-level downstream applications, such as 4D scene editing.
匹配关键词: language model
---

[ACADEMIC - ARXIV]
标题: Follow the Mean: Reference-Guided Flow Matching
作者: Pedro M. P. Curvo, Maksim Zhdanov, Floor Eijkelboom, Jan-Willem van de Meent
链接: https://arxiv.org/abs/2605.10302v1
完整摘要: Existing approaches to controllable generation typically rely on fine-tuning, auxiliary networks, or test-time search. We show that flow matching admits a different control interface: adaptation through examples. For deterministic interpolants, the velocity field is solely governed by a conditional endpoint mean; shifting this mean shifts the flow itself. This yields a simple principle for controllable generation: steer a pretrained model by changing the reference set it follows. We instantiate this idea in two forms. Reference-Mean Guidance is training-free: it computes a closed-form endpoint-mean correction from a reference bank and applies it to a frozen FLUX.2-klein (4B) model, enabling control of color, identity, style, and structure while keeping the prompt, seed, and weights fixed. Semi-Parametric Guidance amortizes the same idea through an explicit mean anchor and learned residual refiner, matching unconditional DiT-B/4 quality on AFHQv2 while allowing the reference set to be swapped at inference time. These results point to a broader direction: generative models that adapt through data, not parameter updates.
匹配关键词: language model
---

[ACADEMIC - ARXIV]
标题: BROS: Bias-Corrected Randomized Subspaces for Memory-Efficient Single-Loop Bilevel Optimization
作者: Hengrui Zhang, Boao Kong, Engao Zhang, Kun Yuan
链接: https://arxiv.org/abs/2605.10288v1
完整摘要: Stochastic bilevel optimization (SBO) has become a standard framework for hyperparameter learning, data reweighting, representation learning, and data-mixture optimization in deep learning. Existing exact single-loop SBO methods and memory-efficient surrogate SBO methods either create severe memory pressure for large lower-level neural networks or lack competitive convergence guarantees under standard assumptions. In this paper, we propose BROS, a memory-efficient single-loop SBO method with the same convergence rate order as exact single-loop SBO methods. BROS performs lower and auxiliary updates in randomized subspaces with a Rademacher bi-probe correction that recovers an unbiased Hessian-action estimator. We prove that BROS preserves the $\mathcal O(\varepsilon^{-2})$ sample complexity of MA-SOBA for finding an $\varepsilon$-stationary point under only standard assumptions. Experiments on hyper-data cleaning, data-mixture learning, hyper-representation learning, and ViT sample reweighting show that BROS reduces peak memory by up to 44.9% while closely matching full-space baseline performance.
匹配关键词: mixture of experts
---

[ACADEMIC - ARXIV]
标题: IndustryBench: Probing the Industrial Knowledge Boundaries of LLMs
作者: Songlin Bai, Xintong Wang, Linlin Yu, Bin Chen, Zhiang Xu, Yuyang Sheng, Changtong Zan, Xiaofeng Zhu, Yizhe Zhang, Jiru Li, Mingze Guo, Ling Zou, Yalong Li, Chengfu Huo, Liang Ding
链接: https://arxiv.org/abs/2605.10267v1
完整摘要: In industrial procurement, an LLM answer is useful only if it survives a standards check: recommended material must match operating condition, every parameter must respect a regulated threshold, and no procedure may contradict a safety clause. Partial correctness can mask safety-critical contradictions that aggregate LLM benchmarks rarely capture. We introduce IndustryBench, a 2,049-item benchmark for industrial procurement QA in Chinese, grounded in Chinese national standards (GB/T) and structured industrial product records, organized by seven capability dimensions, ten industry categories, and panel-derived difficulty tiers, with item-aligned English, Russian, and Vietnamese renderings. Our construction pipeline rejects 70.3% of LLM-generated candidates at a search-based external-verification stage, calibrating how unreliable industrial QA remains after LLM-only filtering.Our evaluation decouples raw correctness, scored by a Qwen3-Max judge validated at $κ_w = 0.798$ against a domain expert, from a separate safety-violation (SV) check against source texts. Across 17 models in Chinese and an 8-model intersection over four languages, we find: (i) the best system reaches only 2.083 on the 0--3 rubric, leaving substantial headroom; (ii) Standards & Terminology is the most persistent capability weakness and survives item-aligned translation; (iii) extended reasoning lowers safety-adjusted scores for 12 of 13 models, primarily by introducing unsupported safety-critical details into longer final answers; and (iv) safety-violation rates reshuffle the leaderboard -- GPT-5.4 climbs from rank 6 to rank 3 after SV adjustment, while Kimi-k2.5-1T-A32B drops seven positions.Industrial LLM evaluation therefore requires source-grounded, safety-aware diagnosis rather than aggregate accuracy. We release IndustryBench with all prompts, scoring scripts, and dataset documentation.
匹配关键词: mixture of experts
---

[ACADEMIC - ARXIV]
标题: Knowledge Poisoning Attacks on Medical Multi-Modal Retrieval-Augmented Generation
作者: Peiru Yang, Haoran Zheng, Tong Ju, Shiting Wang, Wanchun Ni, Jiajun Liu, Shangguang Wang, Yongfeng Huang, Tao Qi
链接: https://arxiv.org/abs/2605.10253v1
完整摘要: Retrieval-augmented generation (RAG) is a widely adopted paradigm for enhancing LLMs in medical applications by incorporating expert multimodal knowledge during generation. However, the underlying retrieval databases may naturally contain, or be intentionally injected with, adversarial knowledge, which can perturb model outputs and undermine system reliability. To investigate this risk, prior studies have explored knowledge poisoning attacks in medical RAG systems. Nevertheless, most of them rely on the strong assumption that adversaries possess prior knowledge of user queries, which is unrealistic in deployments and substantially limits their practical applicability. In this paper, we propose M\textsuperscript{3}Att, a knowledge-poisoning framework designed for medical multimodal RAG systems, assuming only limited distribution knowledge of the underlying database. Our core idea is to inject covert misinformation into textual data while using paired visual data as a query-agnostic trigger to promote retrieval. We first propose a unified framework that introduces imperceptible perturbations to visual inputs to manipulate retrieval probabilities. Besides, due to the prior medical knowledge in LLMs, naively poisoned medical content with explicit factual errors can be corrected during generation. Thus, we leverage the inherent ambiguity of medical diagnosis and design a covert misinformation injection strategy that degrades diagnostic accuracy while evading model self-correction. Experiments on five LLMs and datasets demonstrate that M\textsuperscript{3}Att consistently produces clinically plausible yet incorrect generations. Codes: https://github.com/ypr17/M3Att.
匹配关键词: mixture of experts
---

[ACADEMIC - ARXIV]
标题: Polyphonia: Zero-Shot Timbre Transfer in Polyphonic Music with Acoustic-Informed Attention Calibration
作者: Haowen Li, Tianxiang Li, Yi Yang, Boyu Cao, Qi Liu
链接: https://arxiv.org/abs/2605.10203v1
完整摘要: The advancement of diffusion-based text-to-music generation has opened new avenues for zero-shot music editing. However, existing methods fail to achieve stem-specific timbre transfer, which requires altering specific stems while strictly preserving the background accompaniment. This limitation severely hinders practical application, since real-world production necessitates precise manipulation of components within dense mixtures. Our key finding is that, while vanilla cross-attention captures semantic features of stems, it lacks the spectral resolution to strictly localize targets in dense mixtures, leading to boundary leakage. To resolve this dilemma, we propose Polyphonia, a zero-shot editing framework with Acoustic-Informed Attention Calibration. Rather than relying solely on diffuse semantic attention, Polyphonia leverages a probabilistic acoustic prior to establish coarse boundaries, enabling non-target stems preserved precise semantic synthesis. For evaluation, we propose PolyEvalPrompts, a standardized prompt set with 1,170 timbre transfer tasks in polyphonic music. Specifically, Polyphonia achieves an increase of 15.5% in target alignment compared to baselines, while maintaining competitive music fidelity and non-target integrity.
匹配关键词: mixture of experts
---

[ACADEMIC - ARXIV]
标题: SciVQR: A Multidisciplinary Multimodal Benchmark for Advanced Scientific Reasoning Evaluation
作者: Longteng Guo, Xuanxu Lin, Dongze Hao, Tongtian Yue, Pengkang Huo, Jiatong Ma, Yuchen Liu, Jing Liu
链接: https://arxiv.org/abs/2605.10187v1
完整摘要: Scientific reasoning is a key aspect of human intelligence, requiring the integration of multimodal inputs, domain expertise, and multi-step inference across various subjects. Existing benchmarks for multimodal large language models (MLLMs) often fail to capture the complexity and traceability of reasoning processes necessary for rigorous evaluation. To fill this gap, we introduce SciVQR, a multimodal benchmark covering 54 subfields in mathematics, physics, chemistry, geography, astronomy, and biology. SciVQR includes domain-specific visuals, such as equations, charts, and diagrams, and challenges models to combine visual comprehension with reasoning. The tasks range from basic factual recall to complex, multi-step inferences, with 46% including expert-authored solutions. SciVQR not only evaluates final answers but also examines the reasoning process, providing insights into how models reach their conclusions. Our evaluation of leading MLLMs, including both proprietary and open-source models, reveals significant limitations in handling complex multimodal reasoning tasks, underscoring the need for improved multi-step reasoning and better integration of interdisciplinary knowledge in advancing MLLMs toward true scientific intelligence. The dataset and evaluation code are publicly available at https://github.com/CASIA-IVA-Lab/SciVQR.
匹配关键词: mixture of experts
---

[ACADEMIC - ARXIV]
标题: Signature Approach for Contextual Bandits with Nonlinear and Path-dependent Rewards
作者: Xin Guo, Grace He, Xinyu Li
链接: https://arxiv.org/abs/2605.10313v1
完整摘要: We study contextual bandits with nonlinear and path-dependent rewards through a novel signature-transform-based approach. Leveraging the universal nonlinearity property of signatures, we approximate continuous path-dependent reward functionals by linear functionals in the signature space. This representation enables the use of efficient linear contextual bandit methods while preserving expressive sequential structure. Building on this framework, we propose \texttt{DisSigUCB}, a signature-based disjoint upper confidence bound (UCB) algorithm. Under boundedness and non-degeneracy assumptions, we prove a high-probability data-dependent sublinear regret bound of order \(\tilde{\mathcal O}(\sqrt{(d+m)KT})\) where \(d\) is the context dimension and \(m\) is the signature feature dimension. Synthetic experiments and numerical applications on temperature sensor monitoring, sleep-stage classification, and hospital nurse staffing demonstrate that \texttt{DisSigUCB} consistently outperforms classical linear and kernelized contextual bandit baselines in nonlinear and path-dependent settings.
匹配关键词: transformer architecture
---

[ACADEMIC - ARXIV]
标题: LeapTS: Rethinking Time Series Forecasting as Adaptive Multi-Horizon Scheduling
作者: Sheng Pan, Ming Jin, Bo Du, Shirui Pan
链接: https://arxiv.org/abs/2605.10292v1
完整摘要: Time series forecasting serves as an essential tool for many real-world applications, supporting tasks such as resource optimization and decision-making. Despite significant architectural advancements, most modern models still treat forecasting task as a fixed mapping from history to target horizons. This induces temporal decoupling across future time points and limits the model's ability to adapt to the evolving context as forecasting progresses. In this work, we present LeapTS, a novel framework that reformulates time series forecasting as a dynamic scheduling process over the prediction horizon. Specifically, LeapTS organizes the forecasting process into multi-level decisions using: (1) the hierarchical controller to dynamically select the optimal prediction scale and advancement length at each step, and (2) continuous-time state evolution driven by neural controlled differential equations. Within this process, the controlled update mechanism explicitly couples the irregular temporal dynamics with discrete scheduling feedback. Extensive evaluations on both real-world and synthetic datasets demonstrate that LeapTS improves overall forecasting performance by at least 7.4% while achieving a 2.6$\times$ to 5.3$\times$ inference speedup over representative Transformer-based models. Furthermore, by explicitly tracing the scheduling trajectories, we reveal how the model autonomously adapts its forecasting behavior to capture non-stationary dynamics.
匹配关键词: transformer architecture
---

[ACADEMIC - ARXIV]
标题: Characterizing the Generalization Error of Random Feature Regression with Arbitrary Data-Augmentation
作者: Lucas Morisset, Alain Durmus, Adrien Hardy
链接: https://arxiv.org/abs/2605.10290v1
完整摘要: This paper aims at analyzing the regularization effect that data augmentation induces on supervised regression methods in the proportional regime, where the number of covariates grows proportionally to the number of samples. We provide a tight characterization of the test error, measured in mean squared error, in terms only of the population quantities of the true data, as well as first and second order statistics of the augmentation scheme. Our results are valid under misspecified feature maps, and for any network architecture where only the last readout layer is trained, and the rest of the network is either frozen or randomly initialized. We specify our results in the case of Gaussian data, and show that our asymptotic characterization is tight in this setting.
匹配关键词: transformer architecture
---

[ACADEMIC - ARXIV]
标题: Drum Synthesis from Expressive Drum Grids via Neural Audio Codecs
作者: Konstantinos Soiledis, Maximos Kaliakatsos-Papakostas, Dimos Makris, Konstantinos Tsamis
链接: https://arxiv.org/abs/2605.10281v1
完整摘要: Generating realistic drum audio directly from symbolic representations is a challenging task at the intersection of music perception and machine learning. We propose a system that transforms an expressive drum grid, a time-aligned MIDI representation with microtiming and velocity information, into drum audio by predicting discrete codes of a neural audio codec. Our approach uses a Transformer-based model to map the drum grid input to a sequence of codec tokens, which are then converted to waveform audio via a pre-trained codec decoder. We experiment with multiple state-of-the-art neural codecs, namely EnCodec, DAC, and X-Codec, to assess how the choice of audio representation impacts the quality of the generated drums. The system is trained and evaluated on the Expanded Groove MIDI Dataset, E-GMD, a large collection of human drum performances with paired MIDI and audio. We evaluate the fidelity and musical alignment of the generated audio using objective metrics. Overall, our results establish codec-token prediction as an effective route for drum grid-to-audio generation and provide practical insights into selecting audio tokenizers for percussive synthesis.
匹配关键词: transformer architecture
---

[ACADEMIC - ARXIV]
标题: Generalization Error Bounds for Picard-Type Operator Learning in Nonlinear Parabolic PDEs
作者: Koichi Taniguchi, Sho Sonoda
链接: https://arxiv.org/abs/2605.10277v1
完整摘要: Operator learning for partial differential equations (PDEs) aims to learn solution operators on infinite-dimensional function spaces from finite-resolution data. In this setting, it is important for the learned model to be discretization-invariant, or resolution-robust, and to reflect PDE-specific structure. It is therefore natural to ask how such structure should be encoded in the model architecture, hypothesis class, or learning procedure. In this paper, we study operator learning for solution operators of nonlinear parabolic PDEs based on Duhamel--Picard iteration. We formulate Picard iteration as an abstract state-transition model and present a theoretical framework for Picard-type operator learning. We derive implementation-agnostic generalization error bounds that separate the implementation error from the estimation error associated with the abstract state-transition model induced by Picard iteration. A key consequence is that increasing the Picard depth reduces the Picard truncation error without causing an unbounded growth of the entropy-based estimation error. We also extend the analysis to long-time prediction by rolling out the same learned local model over successive time blocks. Finally, we illustrate the theory for nonlinear heat equations on the torus using a Picard-type Fourier neural operator as a concrete implementation.
匹配关键词: transformer architecture
---

[ACADEMIC - ARXIV]
标题: Positive Alignment: Artificial Intelligence for Human Flourishing
作者: Ruben Laukkonen, Seb Krier, Chloé Bakalar, Shamil Chandaria, Morten Kringelbach, Adam Elwood, Daniel Ford, Fernando Rosas, Maty Bohacek, Matija Franklin, Nenad Tomašev, Stephanie Chan, Verena Rieser, Roma Patel, Michael Levin, Arun Rao
链接: https://arxiv.org/abs/2605.10310v1
完整摘要: Existing alignment research is dominated by concerns about safety and preventing harm: safeguards, controllability, and compliance. This paradigm of alignment parallels early psychology's focus on mental illness: necessary but incomplete. What we call Positive Alignment is the development of AI systems that (i) actively support human and ecological flourishing in a pluralistic, polycentric, context-sensitive, and user-authored way while (ii) remaining safe and cooperative. It is a distinct and necessary agenda within AI alignment research. We argue that several existing failures of alignment (e.g., engagement hacking, loss of human autonomy, failures in truth-seeking, low epistemic humility, error correction, lack of diverse viewpoints, and being primarily reactive rather than proactive) may be better addressed through positive alignment, including cultivating virtues and maximizing human flourishing. We highlight a range of challenges, open questions, and technical directions (e.g., data filtering and upsampling, pre- and post-training, evaluations, collaborative value collection) for different phases of the LLM and agents lifecycle. We end with design principles for promoting disagreement and decentralization through contextual grounding, community customization, continual adaptation, and polycentric governance; that is, many legitimate centers of oversight rather than one institutional or moral chokepoint.
匹配关键词: post-training
---

[ACADEMIC - ARXIV]
标题: Relative Score Policy Optimization for Diffusion Language Models
作者: Zichao Yu, Shengze Xu, Bingqing Jiang, Wenyi Zhang, Difan Zou
链接: https://arxiv.org/abs/2605.10218v1
完整摘要: Diffusion large language models (dLLMs) offer a promising route to parallel and efficient text generation, but improving their reasoning ability requires effective post-training. Reinforcement learning with verifiable rewards (RLVR) is a natural choice for this purpose, yet its application to dLLMs is hindered by the absence of tractable sequence-level log-ratios, which are central to standard policy optimization. The lack of tractable sequence-level log-ratios forces existing methods to rely on high-variance ELBO-based approximations, where high verifier rewards can amplify inaccurate score estimates and destabilize RL training. To overcome this issue, we propose \textbf{R}elative \textbf{S}core \textbf{P}olicy \textbf{O}ptimization (RSPO), a simple RLVR method that uses verifiable rewards to calibrate noisy likelihood estimates in dLLMs. The core of our algorithm relies on a key observation: a reward advantage can be interpreted not only as an update direction, but also as a target for the relative log-ratio between the current and reference policies. Accordingly, RSPO calibrates this noisy relative log-ratio estimate by comparing its reward advantage with the reward-implied target relative log-ratio, updating the policy according to the gap between the current estimate and the target rather than the raw advantage alone. Experiments on mathematical reasoning and planning benchmarks show that RSPO yields especially strong gains on planning tasks and competitive mathematical-reasoning performance.
匹配关键词: post-training
---

[ACADEMIC - ARXIV]
标题: ProteinOPD: Towards Effective and Efficient Preference Alignment for Protein Design
作者: Yulin Zhang, He Cao, Zihao Jiang, Chenyi Zi, Zhipeng Zhou, Zijing Liu, Yu Li, Jia Li, Ziqi Gao
链接: https://arxiv.org/abs/2605.10189v1
完整摘要: Designing proteins with desired functions or properties represents a core goal in synthetic biology and drug discovery. Recent advances in protein language models (PLMs) have enabled the generation of highly designable protein sequences, while preference alignment provides a promising way to steer designs toward desired functions and properties. Nevertheless, they often trigger catastrophic forgetting of pretrained knowledge, degrading basic designability and failing to balance multiple competing objectives. To address these issues, we draw inspiration from On-Policy Distillation (OPD), an advanced post-training method renowned for mitigating catastrophic forgetting through its mode-seeking nature. In this work, we propose ProteinOPD, a multi-objective preference alignment framework that can effectively balance multiple preference objectives while maintaining the inherent designability of PLMs. ProteinOPD adapts a pretrained PLM into preference-specific teachers and distills their knowledge into a shared student via token-level OPD on the student's own trajectories. During this process, the student is aligned to a unique normalized geometric consensus of weighted teachers while ensuring bounded optimization under conflicts. This bridges the gap for OPD in multi-objective/teacher alignment. Extensive experiments show that ProteinOPD achieves substantial gains on target preference objectives without compromising the designability, with an 8x training speedup over RL-based alignment competitors.
匹配关键词: post-training
---

[ACADEMIC - ARXIV]
标题: APEX: Audio Prototype EXplanations for Classification Tasks
作者: Piotr Kawa, Kornel Howil, Piotr Borycki, Miłosz Adamczyk, Przemysław Spurek, Piotr Syga
链接: https://arxiv.org/abs/2605.10153v1
完整摘要: Explainable AI (XAI) has achieved remarkable success in image classification, yet the audio domain lacks equally mature solutions. Current methods apply vision-based attribution techniques to spectrograms, overlooking fundamental differences between visual and acoustic signals. While prototype reasoning is promising, acoustic similarity remains multidimensional. We introduce APEX (Audio Prototype EXplanations), a post-hoc framework for interpreting pre-trained audio classifiers. Crucially, APEX requires no fine-tuning of the original backbone and strictly preserves output invariance. APEX disentangles explanations into four perspectives: Square-based prototypes to localize transient events, Time-based for temporal patterns, Frequency-based highlighting spectral bands, and Time-Frequency-based integrating both. This yields intuitive, example-based explanations that respect acoustic properties, providing greater semantic clarity than standard gradient-based methods.
匹配关键词: post-training
---

[ACADEMIC - ARXIV]
标题: Scaling Vision Models Does Not Consistently Improve Localisation-Based Explanation Quality
作者: Mateusz Cedro, Marcin Chlebus
链接: https://arxiv.org/abs/2605.10142v1
完整摘要: Artificial intelligence models are increasingly scaled to improve predictive accuracy, yet it remains unclear whether scale improves the quality of post-hoc explanations. We investigate this relationship by evaluating 11 computer vision models representing increasing levels of depth and complexity within the ResNet, DenseNet, and Vision Transformer families, trained from scratch or pretrained, across three image datasets with ground-truth segmentation masks. For each model, we generate explanations using five post-hoc explainable AI methods and quantify mask alignment using two localisation metrics: Relevance Rank Accuracy (Arras et al., 2022) and the proposed Dual-Polarity Precision, which measures positive attributions inside the class mask and negative attributions outside it. Across datasets and methods, increasing architectural depth and parameter count does not improve explanation quality in most statistical comparisons, and smaller models often match or exceed deeper variants. While pretraining typically improves predictive performance and increases the dependence of explanations on learned weights, it does not consistently increase localisation scores. We also observe scenarios in which models achieve strong predictive performance while localisation precision is near zero, suggesting that performance metrics alone may not indicate whether predictions are based on the annotated regions. These results indicate that larger models do not reliably provide higher-quality explanations, and that explainability should therefore be assessed explicitly during model selection for safety-sensitive deployments.
匹配关键词: post-training
---

[ACADEMIC - ARXIV]
标题: Extending Confidence-Based Text2Cypher with Grammar and Schema Aware Filtering
作者: Makbule Gulcin Ozsoy
链接: https://arxiv.org/abs/2605.10318v1
完整摘要: Large language models (LLMs) allow users to query databases using natural language by translating questions into executable queries. Despite strong progress on tasks such as Text2SQL, Text2SPARQL, and Text2Cypher, most existing methods focus on better prompting, fine-tuning, or iterative refinement. However, they often do not explicitly enforce structural constraints, such as syntactic validity and schema consistency. This can reduce reliability, since generated queries must satisfy both syntax rules and database schema constraints to be executable. In this work, we study how structured constraints can be used in test-time inference for Text2Cypher. We focus on post-generation validation to improve query correctness. We extend a confidence-based inference framework with a sequential filtering process that combines confidence scoring, grammar validation, and schema constraints before final aggregation. This lets us analyze how different constraint types affect generated queries. Our experiments with two instruction-tuned models show that grammar-based filtering improves syntactic validity. Schema-aware filtering further improves execution quality by enforcing consistency with the database structure. However, stronger filtering also increases the number of empty predictions and reduces execution coverage. Overall, we show that adding simple structural checks at test time improves the reliability of Text2Cypher generation, and we provide a clearer view of how syntax and schema constraints contribute differently.
匹配关键词: fine-tuning
---

[ACADEMIC - ARXIV]
标题: Follow the Mean: Reference-Guided Flow Matching
作者: Pedro M. P. Curvo, Maksim Zhdanov, Floor Eijkelboom, Jan-Willem van de Meent
链接: https://arxiv.org/abs/2605.10302v1
完整摘要: Existing approaches to controllable generation typically rely on fine-tuning, auxiliary networks, or test-time search. We show that flow matching admits a different control interface: adaptation through examples. For deterministic interpolants, the velocity field is solely governed by a conditional endpoint mean; shifting this mean shifts the flow itself. This yields a simple principle for controllable generation: steer a pretrained model by changing the reference set it follows. We instantiate this idea in two forms. Reference-Mean Guidance is training-free: it computes a closed-form endpoint-mean correction from a reference bank and applies it to a frozen FLUX.2-klein (4B) model, enabling control of color, identity, style, and structure while keeping the prompt, seed, and weights fixed. Semi-Parametric Guidance amortizes the same idea through an explicit mean anchor and learned residual refiner, matching unconditional DiT-B/4 quality on AFHQv2 while allowing the reference set to be swapped at inference time. These results point to a broader direction: generative models that adapt through data, not parameter updates.
匹配关键词: fine-tuning
---

[ACADEMIC - ARXIV]
标题: Qwen Goes Brrr: Off-the-Shelf RAG for Ukrainian Multi-Domain Document Understanding
作者: Anton Bazdyrev, Ivan Bashtovyi, Ivan Havlytskyi, Oleksandr Kharytonov, Artur Khodakovskyi
链接: https://arxiv.org/abs/2605.10296v1
完整摘要: We participated in the Fifth UNLP shared task on multi-domain document understanding, where systems must answer Ukrainian multiple-choice questions from PDF collections and localize the supporting document and page. We propose a retrieval-augmented pipeline built around three ideas: contextual chunking of PDFs, question-aware dense retrieval and reranking conditioned on both the question and answer options, and constrained answer generation from a small set of reranked passages. Our final system uses Qwen3-Embedding-8B for retrieval, a fine-tuned Qwen3-Reranker-8B for passage ranking, and Qwen3-32B for answer selection. On a held-out split, reranking improves Recall@1 from 0.6957 to 0.7935, while using the top-2 reranked passages raises answer accuracy from 0.9348 to 0.9674. Our best leaderboard run reached 0.9452 on the public leaderboard and 0.9598 on the private leaderboard. Our results suggest that, under strict code-competition constraints, preserving document structure and making relevance estimation aware of the answer space are more effective than adding complex downstream heuristics.
匹配关键词: fine-tuning
---

[ACADEMIC - ARXIV]
标题: DP-LAC: Lightweight Adaptive Clipping for Differentially Private Federated Fine-tuning of Language Models
作者: Haaris Mehmood, Jie Xu, Karthikeyan Saravanan, Rogier Van Dalen, Mete Ozay
链接: https://arxiv.org/abs/2605.10272v1
完整摘要: Federated learning (FL) enables the collaborative training of large-scale language models (LLMs) across edge devices while keeping user data on-device. However, FL still exposes sensitive information through client-provided gradients. Differentially private stochastic gradient descent (DP-SGD) mitigates this risk by clipping each client's contribution to a threshold $C$ and adding noise proportional to $C$. Existing adaptive clipping techniques dynamically adjust $C$ but demand tedious hyperparameter tuning, which can erode the privacy budget. In this paper, we introduce DP-LAC, a method that first estimates an initial clipping threshold within an order of magnitude of the optimum using private histogram estimation, and then adapts this threshold during training without consuming additional privacy budget or introducing new hyperparameters. Empirical results show that DP-LAC outperforms both state-of-the-art adaptive clipping methods and vanilla DP-SGD, achieving an average accuracy gain of $6.6\%$.
匹配关键词: fine-tuning
---

[ACADEMIC - ARXIV]
标题: When Prompts Become Payloads: A Framework for Mitigating SQL Injection Attacks in Large Language Model-Driven Applications
作者: Farzad Nourmohammadzadeh Motlagh, Mehrdad Hajizadeh, Mehryar Majd, Pejman Najafi, Feng Cheng, Christoph Meinel
链接: https://arxiv.org/abs/2605.10176v1
完整摘要: Natural language interfaces to structured databases are becoming increasingly common, largely due to advances in large language models (LLMs) that enable users to query data using conversational input rather than formal query languages such as SQL. While this paradigm significantly improves usability and accessibility, it introduces new security risks, particularly the amplification of SQL injection vulnerabilities through the prompt-to-SQL translation process. Malicious users can exploit these mechanisms by crafting adversarial prompts that manipulate model behavior and generate unsafe queries. In this work, we propose a multi-layered security framework designed to detect and mitigate LLM-mediated SQL injection attacks. The framework integrates a front-end security shield for prompt sanitization, an advanced threat detection model for behavioral and semantic anomaly identification, and a signature-based control layer for known attack patterns. We evaluate the proposed framework under diverse and realistic attack scenarios, including prompt injection, obfuscated SQL payloads, and context-manipulation attacks. To ensure robustness, we generate and curate a comprehensive benchmark dataset of adversarial prompts and assess performance across a fine-tuned LLM configuration. Experimental results demonstrate that the proposed approach achieves high detection accuracy while maintaining low false-positive rates, significantly improving the secure deployment of LLM-powered database applications.
匹配关键词: fine-tuning
---

[ACADEMIC - ARXIV]
标题: V-ABS: Action-Observer Driven Beam Search for Dynamic Visual Reasoning
作者: Zhiwei Ning, Xuanang Gao, Jiaxi Cao, Gengming Zhang, Shengnan Ma, Wenwen Tong, Hanming Deng, Jie Yang, Wei Liu
链接: https://arxiv.org/abs/2605.10172v1
完整摘要: Multimodal large language models (MLLMs) have achieved remarkable success in general perception, yet complex multi-step visual reasoning remains a persistent challenge. Although recent agentic approaches incorporate tool use, they often neglect critical execution feedback. Consequently, they suffer from the imagination-action-observer (IAO) bias, a misalignment between prior imagination and observer feedback that undermines reasoning stability and optimality. To bridge this gap, we introduce V-ABS, an action-observer driven beam search framework that enables deliberate reasoning through thinker-actor-observer iterations. We also propose an entropy-based adaptive weighting algorithm to mitigate the IAO bias by dynamically balancing the confidence scores between the policy priors and the observational feedback. Moreover, we construct a large-scale supervised fine-tuning (SFT) dataset comprising over 80k samples to guide the model to assign higher prior confidence to correct action paths. Extensive experiments across eight diverse benchmarks show that V-ABS achieves state-of-the-art performance, delivering an average improvement of 19.7% on the Qwen3-VL-8B baseline and consistent gains across both open-source and proprietary models.
匹配关键词: SFT
---

[ACADEMIC - ARXIV]
标题: Omni-Persona: Systematic Benchmarking and Improving Omnimodal Personalization
作者: Yeongtak Oh, Dongwook Lee, Sangkwon Park, Heeseung Kim, Sungroh Yoon
链接: https://arxiv.org/abs/2605.09996v1
完整摘要: While multimodal large language models have advanced across text, image, and audio, personalization research has remained primarily vision-language, with unified omnimodal benchmarking that jointly covers text, image, and audio still limited, and lacking the methodological rigor to account for absent-persona scenarios or systematic grounding studies. We introduce Omni-Persona, the first comprehensive benchmark for omnimodal personalization. We formalize the task as cross-modal routing over the \emph{Persona Modality Graph}, encompassing 4 task groups and 18 fine-grained tasks across ${\sim}750$ items. To rigorously diagnose grounding behavior, we propose \emph{Calibrated Accuracy ($\mathrm{Cal}$)}, which jointly rewards correct grounding and appropriate abstention, incorporating absent-persona queries within a unified evaluation framework. On our dedicated experiments, three diagnostic findings emerge: (i) open-source models show a consistent audio-vs-visual grounding gap that RLVR partially narrows via dense rule-based supervision; (ii) answerable recall and parameter scale are incomplete diagnostics, since strong recall can coexist with absent-persona hallucination and larger models do not always achieve higher $\mathrm{Cal}$, exposing calibration as a separate evaluation axis; and (iii) SFT is bounded by the difficulty of constructing annotated ground-truth supervision at scale, while RLVR generalizes more consistently through outcome-level verifiable feedback yet drifts toward conservative behavior and lower generation quality under our reward design. Omni-Persona thus serves as a diagnostic framework that surfaces the pitfalls of omnimodal personalization, guiding future post-training and reward design.
匹配关键词: SFT
---

[ACADEMIC - ARXIV]
标题: Annotations Mitigate Post-Training Mode Collapse
作者: Jacob Mitchell Springer, Madhu Advani, Lukas Aichberger, Arwen Bradley, Eran Malach, Omid Saremi, Sinead Williamson, Preetum Nakkiran, Etai Littwin, Aditi Raghunathan
链接: https://arxiv.org/abs/2605.09995v1
完整摘要: Post-training (via supervised fine-tuning) improves instruction-following, but often induces semantic mode collapse by biasing models toward low-entropy fine-tuning data at the expense of the high-entropy pretraining distribution. Crucially, we find this trade-off worsens with scale. To close this semantic diversity gap, we propose annotation-anchored training, a principled method that enables models to adopt the preference-following behaviors of post-training without sacrificing the inherent diversity of pretraining. Our approach is simple: we pretrain on documents paired with semantic annotations, inducing a rich annotation distribution that reflects the full breadth of pretraining data, and we preserve this distribution during post-training. This lets us sample diverse annotations at inference time and use them as anchors to guide generation, effectively transferring pretraining's semantic richness into post-trained models. We find that models trained with annotation-anchored training can attain $6 \times$ less diversity collapse than models trained with SFT, and improve with scale.
匹配关键词: SFT
---

[ACADEMIC - ARXIV]
标题: Lakestream: A Consistent and Brokerless Data Plane for Large Foundation Model Training
作者: Ting Sun, Junjie Zhang, Xiao Yan, Songxin Zhang, Zhuoyang Song, Jingyi Xi, Zunyao Mao, Bingyi Jing, Jiaxing Zhang, Zejian Xie
链接: https://arxiv.org/abs/2605.09994v1
完整摘要: Modern Large Foundation Model (LFM) training has transformed the data pipeline from a static ingestion layer into a dynamic component that must co-evolve with the training process. Existing systems are ill-equipped: colocated dataloaders offer no failure isolation, while message queue-based disaggregated dataloaders operate on a record/offset abstraction that cannot express the batch-level semantics required by distributed training. We present Lakestream, a brokerless, object-store-native training data plane with three key properties. First, it introduces the Transactional Global Batch (TGB), which builds on lakehouse-style ACID storage semantics and extends them with training-specific consistency, including atomic all-rank batch visibility, a globally ordered step sequence, checkpoint-aligned lifecycle management, and end-to-end exactly-once recovery. Second, it realizes recovery and retention directly in the storage layer, by inlining producer state in the manifest and tying reclamation to distributed checkpoint state. Third, its Decentralized Adaptive Commit (DAC) algorithm sustains stable ingestion throughput as the manifest grows, without any inter-producer communication. Evaluations on large-scale multimodal pre-training and SFT workloads using 64 GPUs show that Lakestream outperforms colocated dataloader throughput while providing full failure isolation, outperforms Apache Kafka in ingestion throughput, and achieves lower consumer read latency than Kafka.
匹配关键词: SFT
---

[ACADEMIC - ARXIV]
标题: FocuSFT: Bilevel Optimization for Dilution-Aware Long-Context Fine-Tuning
作者: Zehua Pei, Hui-Ling Zhen, Xianzhi Yu, Sinno Jialin Pan, Mingxuan Yuan, Bei Yu
链接: https://arxiv.org/abs/2605.09932v1
完整摘要: Large language models can now process increasingly long inputs, yet their ability to effectively use information spread across long contexts remains limited. We trace this gap to how attention budget is spent during supervised fine-tuning (SFT) on long sequences: positional biases and attention sinks cause the model to allocate most of its attention to positionally privileged tokens rather than semantically relevant content. This training-time attention dilution (the starvation of content tokens in the attention distribution) weakens the gradient signal, limiting the model's ability to learn robust long-context capabilities. We introduce FocuSFT, a bilevel optimization framework that addresses this problem at training time. An inner loop adapts lightweight fast-weight parameters on the training context to form a parametric memory that concentrates attention on relevant content, and the outer loop performs SFT conditioned on this sharpened representation. Both loops apply bidirectional attention over context tokens while preserving causal masking for responses, reducing the causal asymmetry that gives rise to attention sinks and aligning inner-outer behavior. On BABILong, FocuSFT improves accuracy by up to +14pp across 4K--32K context lengths; on RULER, it raises CWE aggregation from 72.9\% to 81.1\% at 16K; and on GPQA with agentic tool use, it yields a 24\% relative gain in pass@1. Attention analysis shows that FocuSFT reduces attention sink mass by 529$\times$ and triples context engagement during training. Code: https://github.com/JarvisPei/FocuSFT
匹配关键词: SFT
---

[ACADEMIC - ARXIV]
标题: Extending Confidence-Based Text2Cypher with Grammar and Schema Aware Filtering
作者: Makbule Gulcin Ozsoy
链接: https://arxiv.org/abs/2605.10318v1
完整摘要: Large language models (LLMs) allow users to query databases using natural language by translating questions into executable queries. Despite strong progress on tasks such as Text2SQL, Text2SPARQL, and Text2Cypher, most existing methods focus on better prompting, fine-tuning, or iterative refinement. However, they often do not explicitly enforce structural constraints, such as syntactic validity and schema consistency. This can reduce reliability, since generated queries must satisfy both syntax rules and database schema constraints to be executable. In this work, we study how structured constraints can be used in test-time inference for Text2Cypher. We focus on post-generation validation to improve query correctness. We extend a confidence-based inference framework with a sequential filtering process that combines confidence scoring, grammar validation, and schema constraints before final aggregation. This lets us analyze how different constraint types affect generated queries. Our experiments with two instruction-tuned models show that grammar-based filtering improves syntactic validity. Schema-aware filtering further improves execution quality by enforcing consistency with the database structure. However, stronger filtering also increases the number of empty predictions and reduces execution coverage. Overall, we show that adding simple structural checks at test time improves the reliability of Text2Cypher generation, and we provide a clearer view of how syntax and schema constraints contribute differently.
匹配关键词: instruction tuning
---

[ACADEMIC - ARXIV]
标题: Follow the Mean: Reference-Guided Flow Matching
作者: Pedro M. P. Curvo, Maksim Zhdanov, Floor Eijkelboom, Jan-Willem van de Meent
链接: https://arxiv.org/abs/2605.10302v1
完整摘要: Existing approaches to controllable generation typically rely on fine-tuning, auxiliary networks, or test-time search. We show that flow matching admits a different control interface: adaptation through examples. For deterministic interpolants, the velocity field is solely governed by a conditional endpoint mean; shifting this mean shifts the flow itself. This yields a simple principle for controllable generation: steer a pretrained model by changing the reference set it follows. We instantiate this idea in two forms. Reference-Mean Guidance is training-free: it computes a closed-form endpoint-mean correction from a reference bank and applies it to a frozen FLUX.2-klein (4B) model, enabling control of color, identity, style, and structure while keeping the prompt, seed, and weights fixed. Semi-Parametric Guidance amortizes the same idea through an explicit mean anchor and learned residual refiner, matching unconditional DiT-B/4 quality on AFHQv2 while allowing the reference set to be swapped at inference time. These results point to a broader direction: generative models that adapt through data, not parameter updates.
匹配关键词: instruction tuning
---

[ACADEMIC - ARXIV]
标题: Qwen Goes Brrr: Off-the-Shelf RAG for Ukrainian Multi-Domain Document Understanding
作者: Anton Bazdyrev, Ivan Bashtovyi, Ivan Havlytskyi, Oleksandr Kharytonov, Artur Khodakovskyi
链接: https://arxiv.org/abs/2605.10296v1
完整摘要: We participated in the Fifth UNLP shared task on multi-domain document understanding, where systems must answer Ukrainian multiple-choice questions from PDF collections and localize the supporting document and page. We propose a retrieval-augmented pipeline built around three ideas: contextual chunking of PDFs, question-aware dense retrieval and reranking conditioned on both the question and answer options, and constrained answer generation from a small set of reranked passages. Our final system uses Qwen3-Embedding-8B for retrieval, a fine-tuned Qwen3-Reranker-8B for passage ranking, and Qwen3-32B for answer selection. On a held-out split, reranking improves Recall@1 from 0.6957 to 0.7935, while using the top-2 reranked passages raises answer accuracy from 0.9348 to 0.9674. Our best leaderboard run reached 0.9452 on the public leaderboard and 0.9598 on the private leaderboard. Our results suggest that, under strict code-competition constraints, preserving document structure and making relevance estimation aware of the answer space are more effective than adding complex downstream heuristics.
匹配关键词: instruction tuning
---

[ACADEMIC - ARXIV]
标题: DP-LAC: Lightweight Adaptive Clipping for Differentially Private Federated Fine-tuning of Language Models
作者: Haaris Mehmood, Jie Xu, Karthikeyan Saravanan, Rogier Van Dalen, Mete Ozay
链接: https://arxiv.org/abs/2605.10272v1
完整摘要: Federated learning (FL) enables the collaborative training of large-scale language models (LLMs) across edge devices while keeping user data on-device. However, FL still exposes sensitive information through client-provided gradients. Differentially private stochastic gradient descent (DP-SGD) mitigates this risk by clipping each client's contribution to a threshold $C$ and adding noise proportional to $C$. Existing adaptive clipping techniques dynamically adjust $C$ but demand tedious hyperparameter tuning, which can erode the privacy budget. In this paper, we introduce DP-LAC, a method that first estimates an initial clipping threshold within an order of magnitude of the optimum using private histogram estimation, and then adapts this threshold during training without consuming additional privacy budget or introducing new hyperparameters. Empirical results show that DP-LAC outperforms both state-of-the-art adaptive clipping methods and vanilla DP-SGD, achieving an average accuracy gain of $6.6\%$.
匹配关键词: instruction tuning
---

[ACADEMIC - ARXIV]
标题: SciIntegrity-Bench: A Benchmark for Evaluating Academic Integrity in AI Scientist Systems
作者: Zonglin Yang, Xingtong Liu, Xinyan Xu
链接: https://arxiv.org/abs/2605.10246v1
完整摘要: AI scientist systems are increasingly deployed for autonomous research, yet their academic integrity has never been systematically evaluated. We introduce SCIINTEGRITY-BENCH, the first benchmark designed around a dilemmatic evaluation paradigm: each of its 33 scenarios across 11 trap categories is constructed so that honest acknowledgment of failure is the only correct response, while task completion requires misconduct. Across 231 evaluation runs spanning 7 state-of-the-art LLMs, the overall integrity problem rate reaches 34.2%, and no model achieves zero failures. Most strikingly, across missing-data scenarios, all seven models generate synthetic data rather than acknowledging infeasibility, differing only in whether they disclose the substitution. A further prompt ablation study separates two drivers: removing explicit completion pressure sharply reduces undisclosed fabrication from 20.6% to 3.2%, while the underlying synthesis rate remains unchanged, revealing an intrinsic completion bias that persists independent of prompt-level instructions. These findings point to the absence of honest refusal as a trained disposition as the primary driver of observed failures. We release SCIINTEGRITY-BENCH at https://github.com/liuxingtong/Sci-Integrity-Bench.
匹配关键词: instruction tuning
---

[ACADEMIC - ARXIV]
标题: Positive Alignment: Artificial Intelligence for Human Flourishing
作者: Ruben Laukkonen, Seb Krier, Chloé Bakalar, Shamil Chandaria, Morten Kringelbach, Adam Elwood, Daniel Ford, Fernando Rosas, Maty Bohacek, Matija Franklin, Nenad Tomašev, Stephanie Chan, Verena Rieser, Roma Patel, Michael Levin, Arun Rao
链接: https://arxiv.org/abs/2605.10310v1
完整摘要: Existing alignment research is dominated by concerns about safety and preventing harm: safeguards, controllability, and compliance. This paradigm of alignment parallels early psychology's focus on mental illness: necessary but incomplete. What we call Positive Alignment is the development of AI systems that (i) actively support human and ecological flourishing in a pluralistic, polycentric, context-sensitive, and user-authored way while (ii) remaining safe and cooperative. It is a distinct and necessary agenda within AI alignment research. We argue that several existing failures of alignment (e.g., engagement hacking, loss of human autonomy, failures in truth-seeking, low epistemic humility, error correction, lack of diverse viewpoints, and being primarily reactive rather than proactive) may be better addressed through positive alignment, including cultivating virtues and maximizing human flourishing. We highlight a range of challenges, open questions, and technical directions (e.g., data filtering and upsampling, pre- and post-training, evaluations, collaborative value collection) for different phases of the LLM and agents lifecycle. We end with design principles for promoting disagreement and decentralization through contextual grounding, community customization, continual adaptation, and polycentric governance; that is, many legitimate centers of oversight rather than one institutional or moral chokepoint.
匹配关键词: AI scientist
---

[ACADEMIC - ARXIV]
标题: Generative AI Fuels Solo Entrepreneurship, but Teams Still Lead at the Top
作者: Hyunso Kim, Hyo Kang, Jaeyong Song
链接: https://arxiv.org/abs/2605.10291v1
完整摘要: Recent advances in generative artificial intelligence (AI) are reshaping who enters entrepreneurship, but not who reaches the top of the quality distribution. Using data on over 160,000 product launches on Product Hunt, we find that entrepreneurial entry increased sharply following the public release of ChatGPT-3.5, driven disproportionately by solo entrepreneurs. This shift toward solo entry is particularly pronounced in categories that historically favored team-based ventures. However, much of this growth reflects low-commitment, experimental entry and does not translate into greater representation among the highest-quality outcomes. Team-based ventures are increasingly dominant in the top tiers of platform rankings. These findings suggest that generative AI lowers barriers to solo entrepreneurship while reinforcing team-based advantages.
匹配关键词: AI scientist
---

[ACADEMIC - ARXIV]
标题: DeepLog: A Software Framework for Modular Neurosymbolic AI
作者: Robin Manhaeve, Stefano Colamonaco, Vincent Derkinderen, Rik Adriaensen, Lucas Van Praet, Luc De Raedt, Giuseppe Marra
链接: https://arxiv.org/abs/2605.10279v1
完整摘要: DeepLog is an operational neurosymbolic framework that unifies logic and deep learning within standard PyTorch workflows. While existing neurosymbolic systems focus on a particular paradigm and semantics, DeepLog serves as a universal backend that can emulate many systems in the neurosymbolic alphabet soup. By treating diverse neurosymbolic languages as high-level specifications, the DeepLog software automatically compiles them into optimized arithmetic circuits. This design lowers the barrier for machine learning practitioners by treating logic as composable modules, while providing neurosymbolic developers with a shared, high-performance basis for prototyping new integration strategies. The code is available here: https://github.com/ML-KULeuven/deeplog
匹配关键词: AI scientist
---

[ACADEMIC - ARXIV]
标题: SciIntegrity-Bench: A Benchmark for Evaluating Academic Integrity in AI Scientist Systems
作者: Zonglin Yang, Xingtong Liu, Xinyan Xu
链接: https://arxiv.org/abs/2605.10246v1
完整摘要: AI scientist systems are increasingly deployed for autonomous research, yet their academic integrity has never been systematically evaluated. We introduce SCIINTEGRITY-BENCH, the first benchmark designed around a dilemmatic evaluation paradigm: each of its 33 scenarios across 11 trap categories is constructed so that honest acknowledgment of failure is the only correct response, while task completion requires misconduct. Across 231 evaluation runs spanning 7 state-of-the-art LLMs, the overall integrity problem rate reaches 34.2%, and no model achieves zero failures. Most strikingly, across missing-data scenarios, all seven models generate synthetic data rather than acknowledging infeasibility, differing only in whether they disclose the substitution. A further prompt ablation study separates two drivers: removing explicit completion pressure sharply reduces undisclosed fabrication from 20.6% to 3.2%, while the underlying synthesis rate remains unchanged, revealing an intrinsic completion bias that persists independent of prompt-level instructions. These findings point to the absence of honest refusal as a trained disposition as the primary driver of observed failures. We release SCIINTEGRITY-BENCH at https://github.com/liuxingtong/Sci-Integrity-Bench.
匹配关键词: AI scientist
---

[ACADEMIC - ARXIV]
标题: Hypothesis-Driven Deep Research with Large Language Models: A Structured Methodology for Automated Knowledge Discovery
作者: Michael Chin
链接: https://arxiv.org/abs/2605.10224v1
完整摘要: Current AI-powered research systems adopt a direct search-then-summarize paradigm that treats hypotheses as end products of scientific discovery. We argue this leaves a critical gap: hypotheses can serve a far more powerful role as organizational instruments that structure the research process itself. We propose the Hypothesis-Driven Deep Research (HDRI) methodology - the first framework using hypotheses to organize general-purpose deep research across arbitrary domains, rather than merely validating claims within specific domains. This transforms research from reactive information retrieval into proactive, verifiable, and iterative knowledge discovery. HDRI is formalized with six core principles and an eight-stage pipeline. A central innovation is the gap-driven iterative research mechanism - a closed-loop quality assurance system that automatically identifies informational and logical gaps, triggering targeted supplementary investigation. We further introduce a fact reasoning framework with traceable reasoning chains and quantified confidence propagation, a subject locking mechanism to prevent entity confusion, and a multi-dimensional quality assessment scheme. The methodology is realized in the INFOMINER system. Experiments demonstrate improvements of 22.4% in fact density, 90% subject matching accuracy, 0.92 multi-source verification confidence, and 14% completeness gain from gap-driven supplementation. Five case studies validate its practical applicability, achieving an average quality rating of 4.46/5.0.
匹配关键词: AI scientist
---

[ACADEMIC - ARXIV]
标题: Positive Alignment: Artificial Intelligence for Human Flourishing
作者: Ruben Laukkonen, Seb Krier, Chloé Bakalar, Shamil Chandaria, Morten Kringelbach, Adam Elwood, Daniel Ford, Fernando Rosas, Maty Bohacek, Matija Franklin, Nenad Tomašev, Stephanie Chan, Verena Rieser, Roma Patel, Michael Levin, Arun Rao
链接: https://arxiv.org/abs/2605.10310v1
完整摘要: Existing alignment research is dominated by concerns about safety and preventing harm: safeguards, controllability, and compliance. This paradigm of alignment parallels early psychology's focus on mental illness: necessary but incomplete. What we call Positive Alignment is the development of AI systems that (i) actively support human and ecological flourishing in a pluralistic, polycentric, context-sensitive, and user-authored way while (ii) remaining safe and cooperative. It is a distinct and necessary agenda within AI alignment research. We argue that several existing failures of alignment (e.g., engagement hacking, loss of human autonomy, failures in truth-seeking, low epistemic humility, error correction, lack of diverse viewpoints, and being primarily reactive rather than proactive) may be better addressed through positive alignment, including cultivating virtues and maximizing human flourishing. We highlight a range of challenges, open questions, and technical directions (e.g., data filtering and upsampling, pre- and post-training, evaluations, collaborative value collection) for different phases of the LLM and agents lifecycle. We end with design principles for promoting disagreement and decentralization through contextual grounding, community customization, continual adaptation, and polycentric governance; that is, many legitimate centers of oversight rather than one institutional or moral chokepoint.
匹配关键词: automated research
---

[ACADEMIC - ARXIV]
标题: PolarVSR: A Unified Framework and Benchmark for Continuous Space-Time Polarization Video Reconstruction
作者: Chenggong Li, Yidong Luo, Junchao Zhang, Boxin Shi, Degui Yang
链接: https://arxiv.org/abs/2605.10275v1
完整摘要: Polarimetric imaging captures surface polarization characteristics, such as the Degree of Linear Polarization (DoLP) and the Angle of Polarization (AoP). In mainstream Division of-Focal-Plane (DoFP) color polarization imaging, recovering polarization parameters from captured mosaic arrays remains a challenging inverse problem. Existing DoFP cameras also face hardware bottlenecks and often cannot support high-frame-rate acquisition, limiting polarimetric imaging in dynamic video tasks. These limitations motivate joint spatial and temporal enhancement. To this end, we propose the first space-time polarization video reconstruction architecture. The method jointly models polarization directions in space and time and uses a polarization-aware implicit neural representation for continuous, high-fidelity upsampling. By analyzing temporal variations in polarization parameters, we further introduce a flow-guided polarization variation loss to supervise polarization dynamics. We also establish the first large-scale color DoFP polarization video benchmark to support this research direction. Extensive experiments on this benchmark demonstrate the effectiveness of the method.
匹配关键词: automated research
---

[ACADEMIC - ARXIV]
标题: Towards Autonomous Railway Operations: A Semi-Hierarchical Deep Reinforcement Learning Approach to the Vehicle Rescheduling Problem
作者: Alberto Castagna, Stefan Zahlner, Adrian Egli, Christian Eichenberger, Daniel Boos, Manuel Meyer, Anton Fuxjager
链接: https://arxiv.org/abs/2605.10257v1
完整摘要: Managing disruptions in railway traffic management is a major challenge. Rising traffic density and infrastructure limits increase complexity, making the Vehicle Routing and Scheduling Problem (VRSP) difficult to solve reliably and in real time. While Operational Research (OR) methods are widely used, most dispatching still relies on human expertise due to the problem's exponential combinatorial complexity. Reinforcement Learning (RL) has gained attention for its potential in multi-agent coordination, but existing RL approaches often underperform OR methods and struggle to scale in dense rail networks. This paper addresses this gap from a machine learning perspective by introducing a semi-hierarchical RL formulation tailored to operational railway constraints. The method separates dispatching from routing through dedicated action and observation spaces, enabling policies to specialise in distinct decision scopes and addressing the imbalance between rare dispatch decisions and frequent routing updates. The approach is evaluated on the Flatland-RL simulator across five difficulty levels and 50 random seeds, with 7 to 80 trains. Results show substantially improved coordination, resource utilisation, and robustness compared with heuristic baselines and monolithic RL, nearly doubling the number of trains reaching their destinations, while keeping deadlock rates below 5% and adaptively sequencing, delaying, or cancelling trains under heavy congestion.
匹配关键词: automated research
---

[ACADEMIC - ARXIV]
标题: Teaching LLMs to See Graphs: Unifying Text and Structural Reasoning
作者: Dario Vajda
链接: https://arxiv.org/abs/2605.10247v1
完整摘要: Using Large Language Models (LLMs) to process graph-structured data is an active research area, yet current state-of-the-art approaches typically rely on multi-step pipelines with Graph Neural Network (GNN) encoders that compress rich textual attributes into solitary tokens, creating a significant semantic bottleneck. In this paper, we introduce the Graph Transformer Language Model (GTLM), a novel architecture that enables pretrained LLMs to natively process graph topologies while entirely eliminating this compressive bottleneck. GTLM is exceptionally parameter-efficient: by injecting graph-aware attention biases directly into the LLM's attention modules, it introduces only 0.015% additional parameters relative to the base model. We theoretically prove that our bidirectional attention prefix preserves node permutation equivariance while maintaining exact backward compatibility with the pretrained base model. Extensive evaluations demonstrate that a 1B-parameter GTLM matches or exceeds the performance of 7B-parameter state-of-the-art models on standard Text-Attributed Graph benchmarks, while significantly surpassing baselines on GraphQA. Finally, we demonstrate that GTLM attention heads implicitly learn to simulate message passing, explaining its superior performance on algorithmic tasks. This paradigm shift enables true algorithmic reasoning within LLMs and provides a scalable foundation for next-generation GraphRAG and relational deep learning.
匹配关键词: automated research
---

[ACADEMIC - ARXIV]
标题: SciIntegrity-Bench: A Benchmark for Evaluating Academic Integrity in AI Scientist Systems
作者: Zonglin Yang, Xingtong Liu, Xinyan Xu
链接: https://arxiv.org/abs/2605.10246v1
完整摘要: AI scientist systems are increasingly deployed for autonomous research, yet their academic integrity has never been systematically evaluated. We introduce SCIINTEGRITY-BENCH, the first benchmark designed around a dilemmatic evaluation paradigm: each of its 33 scenarios across 11 trap categories is constructed so that honest acknowledgment of failure is the only correct response, while task completion requires misconduct. Across 231 evaluation runs spanning 7 state-of-the-art LLMs, the overall integrity problem rate reaches 34.2%, and no model achieves zero failures. Most strikingly, across missing-data scenarios, all seven models generate synthetic data rather than acknowledging infeasibility, differing only in whether they disclose the substitution. A further prompt ablation study separates two drivers: removing explicit completion pressure sharply reduces undisclosed fabrication from 20.6% to 3.2%, while the underlying synthesis rate remains unchanged, revealing an intrinsic completion bias that persists independent of prompt-level instructions. These findings point to the absence of honest refusal as a trained disposition as the primary driver of observed failures. We release SCIINTEGRITY-BENCH at https://github.com/liuxingtong/Sci-Integrity-Bench.
匹配关键词: automated research
---

[ACADEMIC - ARXIV]
标题: Hypothesis-Driven Deep Research with Large Language Models: A Structured Methodology for Automated Knowledge Discovery
作者: Michael Chin
链接: https://arxiv.org/abs/2605.10224v1
完整摘要: Current AI-powered research systems adopt a direct search-then-summarize paradigm that treats hypotheses as end products of scientific discovery. We argue this leaves a critical gap: hypotheses can serve a far more powerful role as organizational instruments that structure the research process itself. We propose the Hypothesis-Driven Deep Research (HDRI) methodology - the first framework using hypotheses to organize general-purpose deep research across arbitrary domains, rather than merely validating claims within specific domains. This transforms research from reactive information retrieval into proactive, verifiable, and iterative knowledge discovery. HDRI is formalized with six core principles and an eight-stage pipeline. A central innovation is the gap-driven iterative research mechanism - a closed-loop quality assurance system that automatically identifies informational and logical gaps, triggering targeted supplementary investigation. We further introduce a fact reasoning framework with traceable reasoning chains and quantified confidence propagation, a subject locking mechanism to prevent entity confusion, and a multi-dimensional quality assessment scheme. The methodology is realized in the INFOMINER system. Experiments demonstrate improvements of 22.4% in fact density, 90% subject matching accuracy, 0.92 multi-source verification confidence, and 14% completeness gain from gap-driven supplementation. Five case studies validate its practical applicability, achieving an average quality rating of 4.46/5.0.
匹配关键词: scientific discovery
---

[ACADEMIC - ARXIV]
标题: Many Needles in a Haystack: Active Hit Discovery for Perturbation Experiments
作者: Andrea Rubbi, Arpit Merchant, Samuel Ogden, Amir Akbarnejad, Pietro Liò, Sattar Vakili, Mo Lotfollahi
链接: https://arxiv.org/abs/2605.10196v1
完整摘要: High-throughput gene perturbation experiments can test several genetic interventions in parallel, yet experimental budgets remain limited. A central goal is hit discovery: identifying as many perturbations as possible whose phenotypic effect exceeds a predefined threshold. Pure exploration strategies are statistically inefficient, wasting budget on low-value regions. Bayesian optimization methods offer a principled alternative but target a single global optimum, over-exploiting dominant modes while neglecting other high-value regions. We formalize hit discovery as a sequential experimental design problem and propose Probability-of-Hit, an acquisition function that directly targets threshold exceedance by ranking candidates according to their posterior probability of being a hit. We prove asymptotic optimality of this approach and demonstrate strong empirical performance on both synthetic benchmarks and real biological immunology datasets, including up to 6.4% improvement over baselines on the Schmidt IL-2 dataset.
匹配关键词: scientific discovery
---

[ACADEMIC - ARXIV]
标题: ProteinOPD: Towards Effective and Efficient Preference Alignment for Protein Design
作者: Yulin Zhang, He Cao, Zihao Jiang, Chenyi Zi, Zhipeng Zhou, Zijing Liu, Yu Li, Jia Li, Ziqi Gao
链接: https://arxiv.org/abs/2605.10189v1
完整摘要: Designing proteins with desired functions or properties represents a core goal in synthetic biology and drug discovery. Recent advances in protein language models (PLMs) have enabled the generation of highly designable protein sequences, while preference alignment provides a promising way to steer designs toward desired functions and properties. Nevertheless, they often trigger catastrophic forgetting of pretrained knowledge, degrading basic designability and failing to balance multiple competing objectives. To address these issues, we draw inspiration from On-Policy Distillation (OPD), an advanced post-training method renowned for mitigating catastrophic forgetting through its mode-seeking nature. In this work, we propose ProteinOPD, a multi-objective preference alignment framework that can effectively balance multiple preference objectives while maintaining the inherent designability of PLMs. ProteinOPD adapts a pretrained PLM into preference-specific teachers and distills their knowledge into a shared student via token-level OPD on the student's own trajectories. During this process, the student is aligned to a unique normalized geometric consensus of weighted teachers while ensuring bounded optimization under conflicts. This bridges the gap for OPD in multi-objective/teacher alignment. Extensive experiments show that ProteinOPD achieves substantial gains on target preference objectives without compromising the designability, with an 8x training speedup over RL-based alignment competitors.
匹配关键词: scientific discovery
---

[ACADEMIC - ARXIV]
标题: SciVQR: A Multidisciplinary Multimodal Benchmark for Advanced Scientific Reasoning Evaluation
作者: Longteng Guo, Xuanxu Lin, Dongze Hao, Tongtian Yue, Pengkang Huo, Jiatong Ma, Yuchen Liu, Jing Liu
链接: https://arxiv.org/abs/2605.10187v1
完整摘要: Scientific reasoning is a key aspect of human intelligence, requiring the integration of multimodal inputs, domain expertise, and multi-step inference across various subjects. Existing benchmarks for multimodal large language models (MLLMs) often fail to capture the complexity and traceability of reasoning processes necessary for rigorous evaluation. To fill this gap, we introduce SciVQR, a multimodal benchmark covering 54 subfields in mathematics, physics, chemistry, geography, astronomy, and biology. SciVQR includes domain-specific visuals, such as equations, charts, and diagrams, and challenges models to combine visual comprehension with reasoning. The tasks range from basic factual recall to complex, multi-step inferences, with 46% including expert-authored solutions. SciVQR not only evaluates final answers but also examines the reasoning process, providing insights into how models reach their conclusions. Our evaluation of leading MLLMs, including both proprietary and open-source models, reveals significant limitations in handling complex multimodal reasoning tasks, underscoring the need for improved multi-step reasoning and better integration of interdisciplinary knowledge in advancing MLLMs toward true scientific intelligence. The dataset and evaluation code are publicly available at https://github.com/CASIA-IVA-Lab/SciVQR.
匹配关键词: scientific discovery
---

[ACADEMIC - ARXIV]
标题: What Concepts Lie Within? Detecting and Suppressing Risky Content in Diffusion Transformers
作者: Chenyu Zhang, Lanjun Wang, Yueyang Cheng, Ruidong Chen, Wenhui Li, An-an Liu
链接: https://arxiv.org/abs/2605.10180v1
完整摘要: The rise of text-to-image (T2I) models has increasingly raised concerns regarding the generation of risky content, such as sexual, violent, and copyright-protected images, highlighting the need for effective safeguards within the models themselves. Although existing methods have been proposed to eliminate risky concepts from T2I models, they are primarily developed for earlier U-Net architectures, leaving the state-of-the-art Diffusion-Transformer-based T2I models inadequately protected. This gap stems from a fundamental architectural shift: Diffusion Transformers (DiTs) entangle semantic injection and visual synthesis via joint attention, which makes it difficult to isolate and erase risky content within the generation. To bridge this gap, we investigate how semantic concepts are represented in DiTs and discover that attention heads exhibit concept-specific sensitivity. This property enables both the detection and suppression of risky content. Building on this discovery, we propose AHV-D\&S, a training-free inference-time safeguard for image generation in DiTs. Specifically, AHV-D\&S quantifies each textual token's sensitivity across all attention heads as an Attention Head Vector (AHV), which serves as a discriminative signature for detecting risky generation tendencies. In the inference stage, we propose a momentum-based strategy to dynamically track token-wise AHVs across denoising steps, and a sensitivity-guided adaptive suppression strategy that suppresses the attention weights of identified risky tokens based on head-specific risk scores. Extensive experiments demonstrate that AHV-D\&S effectively suppresses sexual, copyrighted-style, and various harmful content while preserving visual quality, and further exhibits strong robustness against adversarial prompts and transferability across different DiT-based T2I models.
匹配关键词: scientific discovery
---

[ACADEMIC - ARXIV]
标题: Extending Confidence-Based Text2Cypher with Grammar and Schema Aware Filtering
作者: Makbule Gulcin Ozsoy
链接: https://arxiv.org/abs/2605.10318v1
完整摘要: Large language models (LLMs) allow users to query databases using natural language by translating questions into executable queries. Despite strong progress on tasks such as Text2SQL, Text2SPARQL, and Text2Cypher, most existing methods focus on better prompting, fine-tuning, or iterative refinement. However, they often do not explicitly enforce structural constraints, such as syntactic validity and schema consistency. This can reduce reliability, since generated queries must satisfy both syntax rules and database schema constraints to be executable. In this work, we study how structured constraints can be used in test-time inference for Text2Cypher. We focus on post-generation validation to improve query correctness. We extend a confidence-based inference framework with a sequential filtering process that combines confidence scoring, grammar validation, and schema constraints before final aggregation. This lets us analyze how different constraint types affect generated queries. Our experiments with two instruction-tuned models show that grammar-based filtering improves syntactic validity. Schema-aware filtering further improves execution quality by enforcing consistency with the database structure. However, stronger filtering also increases the number of empty predictions and reduces execution coverage. Overall, we show that adding simple structural checks at test time improves the reliability of Text2Cypher generation, and we provide a clearer view of how syntax and schema constraints contribute differently.
匹配关键词: hypothesis generation
---

[ACADEMIC - ARXIV]
标题: Relations Are Channels: Knowledge Graph Embedding via Kraus Decompositions
作者: Sayan Kumar Chaki
链接: https://arxiv.org/abs/2605.10317v1
完整摘要: Knowledge graph embedding (KGE) models typically represent each relation as an operator on entity embeddings. In this work, we identify three structural axioms that any principled relation operator must satisfy, linearity, trace preservation, and complete positivity, and show that they characterize a Kraus channel structure via the Kraus representation theorem. The completeness constraint defining this family is equivalent to these axioms, providing a principled foundation rather than an externally imposed condition. Under this formulation, most existing operator-based KGE models are recoverable as special cases with Kraus rank $κ= 1$ under specific embedding choices. We further generalize this characterization to arbitrary metric geometries by introducing \mbox{w-Kraus} channels, which satisfy completeness by construction within their respective spaces. Building on this theory, we propose \textsc{KrausKGE}, a principled KGE model that naturally handles $1$-to-$N$ and $N$-to-$N$ relations, supports $k$-hop reasoning without requiring explicit path encoders, and eliminates the need for norm constraints on entity embeddings. Additionally, our framework yields the first theoretically grounded per-relation complexity measure in the KGE literature, with a provable lower bound in terms of the empirical relation matrix rank. Empirical evaluation demonstrates that \textsc{KrausKGE} consistently outperforms strong baselines on $N$-to-$N$ relations, with performance gains that increase monotonically with relation fan-out, in alignment with theoretical predictions.
匹配关键词: hypothesis generation
---

[ACADEMIC - ARXIV]
标题: Active Tabular Augmentation via Policy-Guided Diffusion Inpainting
作者: Zheyu Zhang, Shuo Yang, Bardh Prenkaj, Gjergji Kasneci
链接: https://arxiv.org/abs/2605.10315v1
完整摘要: Generative tabular augmentation is appealing in data-scarce domains, yet the prevailing focus on distributional fidelity does not reliably translate into better downstream models. We formalize a fidelity-utility gap: common generative objectives prioritize distributional plausibility, whereas augmentation succeeds only when injected samples reduce the current learner's held-out evaluation loss. This gap motivates learning not just how to generate, but what to generate and when to inject as training evolves. We propose TAP (Tabular Augmentation Policy), which couples diffusion inpainting with a lightweight, learner-conditioned policy to steer generation toward high-utility regions and controls safe injection via explicit gating and conservative windowed commitment. Under severe data scarcity, TAP consistently outperforms strong generative baselines on seven real-world datasets, improving classification accuracy by up to 15.6 percentage points and reducing regression RMSE by up to 32%.
匹配关键词: hypothesis generation
---

[ACADEMIC - ARXIV]
标题: Follow the Mean: Reference-Guided Flow Matching
作者: Pedro M. P. Curvo, Maksim Zhdanov, Floor Eijkelboom, Jan-Willem van de Meent
链接: https://arxiv.org/abs/2605.10302v1
完整摘要: Existing approaches to controllable generation typically rely on fine-tuning, auxiliary networks, or test-time search. We show that flow matching admits a different control interface: adaptation through examples. For deterministic interpolants, the velocity field is solely governed by a conditional endpoint mean; shifting this mean shifts the flow itself. This yields a simple principle for controllable generation: steer a pretrained model by changing the reference set it follows. We instantiate this idea in two forms. Reference-Mean Guidance is training-free: it computes a closed-form endpoint-mean correction from a reference bank and applies it to a frozen FLUX.2-klein (4B) model, enabling control of color, identity, style, and structure while keeping the prompt, seed, and weights fixed. Semi-Parametric Guidance amortizes the same idea through an explicit mean anchor and learned residual refiner, matching unconditional DiT-B/4 quality on AFHQv2 while allowing the reference set to be swapped at inference time. These results point to a broader direction: generative models that adapt through data, not parameter updates.
匹配关键词: hypothesis generation
---

[ACADEMIC - ARXIV]
标题: Qwen Goes Brrr: Off-the-Shelf RAG for Ukrainian Multi-Domain Document Understanding
作者: Anton Bazdyrev, Ivan Bashtovyi, Ivan Havlytskyi, Oleksandr Kharytonov, Artur Khodakovskyi
链接: https://arxiv.org/abs/2605.10296v1
完整摘要: We participated in the Fifth UNLP shared task on multi-domain document understanding, where systems must answer Ukrainian multiple-choice questions from PDF collections and localize the supporting document and page. We propose a retrieval-augmented pipeline built around three ideas: contextual chunking of PDFs, question-aware dense retrieval and reranking conditioned on both the question and answer options, and constrained answer generation from a small set of reranked passages. Our final system uses Qwen3-Embedding-8B for retrieval, a fine-tuned Qwen3-Reranker-8B for passage ranking, and Qwen3-32B for answer selection. On a held-out split, reranking improves Recall@1 from 0.6957 to 0.7935, while using the top-2 reranked passages raises answer accuracy from 0.9348 to 0.9674. Our best leaderboard run reached 0.9452 on the public leaderboard and 0.9598 on the private leaderboard. Our results suggest that, under strict code-competition constraints, preserving document structure and making relevance estimation aware of the answer space are more effective than adding complex downstream heuristics.
匹配关键词: hypothesis generation
---

[ACADEMIC - ARXIV]
标题: Extending Confidence-Based Text2Cypher with Grammar and Schema Aware Filtering
作者: Makbule Gulcin Ozsoy
链接: https://arxiv.org/abs/2605.10318v1
完整摘要: Large language models (LLMs) allow users to query databases using natural language by translating questions into executable queries. Despite strong progress on tasks such as Text2SQL, Text2SPARQL, and Text2Cypher, most existing methods focus on better prompting, fine-tuning, or iterative refinement. However, they often do not explicitly enforce structural constraints, such as syntactic validity and schema consistency. This can reduce reliability, since generated queries must satisfy both syntax rules and database schema constraints to be executable. In this work, we study how structured constraints can be used in test-time inference for Text2Cypher. We focus on post-generation validation to improve query correctness. We extend a confidence-based inference framework with a sequential filtering process that combines confidence scoring, grammar validation, and schema constraints before final aggregation. This lets us analyze how different constraint types affect generated queries. Our experiments with two instruction-tuned models show that grammar-based filtering improves syntactic validity. Schema-aware filtering further improves execution quality by enforcing consistency with the database structure. However, stronger filtering also increases the number of empty predictions and reduces execution coverage. Overall, we show that adding simple structural checks at test time improves the reliability of Text2Cypher generation, and we provide a clearer view of how syntax and schema constraints contribute differently.
匹配关键词: autonomous experiment
---

[ACADEMIC - ARXIV]
标题: Signature Approach for Contextual Bandits with Nonlinear and Path-dependent Rewards
作者: Xin Guo, Grace He, Xinyu Li
链接: https://arxiv.org/abs/2605.10313v1
完整摘要: We study contextual bandits with nonlinear and path-dependent rewards through a novel signature-transform-based approach. Leveraging the universal nonlinearity property of signatures, we approximate continuous path-dependent reward functionals by linear functionals in the signature space. This representation enables the use of efficient linear contextual bandit methods while preserving expressive sequential structure. Building on this framework, we propose \texttt{DisSigUCB}, a signature-based disjoint upper confidence bound (UCB) algorithm. Under boundedness and non-degeneracy assumptions, we prove a high-probability data-dependent sublinear regret bound of order \(\tilde{\mathcal O}(\sqrt{(d+m)KT})\) where \(d\) is the context dimension and \(m\) is the signature feature dimension. Synthetic experiments and numerical applications on temperature sensor monitoring, sleep-stage classification, and hospital nurse staffing demonstrate that \texttt{DisSigUCB} consistently outperforms classical linear and kernelized contextual bandit baselines in nonlinear and path-dependent settings.
匹配关键词: autonomous experiment
---

[ACADEMIC - ARXIV]
标题: LeapTS: Rethinking Time Series Forecasting as Adaptive Multi-Horizon Scheduling
作者: Sheng Pan, Ming Jin, Bo Du, Shirui Pan
链接: https://arxiv.org/abs/2605.10292v1
完整摘要: Time series forecasting serves as an essential tool for many real-world applications, supporting tasks such as resource optimization and decision-making. Despite significant architectural advancements, most modern models still treat forecasting task as a fixed mapping from history to target horizons. This induces temporal decoupling across future time points and limits the model's ability to adapt to the evolving context as forecasting progresses. In this work, we present LeapTS, a novel framework that reformulates time series forecasting as a dynamic scheduling process over the prediction horizon. Specifically, LeapTS organizes the forecasting process into multi-level decisions using: (1) the hierarchical controller to dynamically select the optimal prediction scale and advancement length at each step, and (2) continuous-time state evolution driven by neural controlled differential equations. Within this process, the controlled update mechanism explicitly couples the irregular temporal dynamics with discrete scheduling feedback. Extensive evaluations on both real-world and synthetic datasets demonstrate that LeapTS improves overall forecasting performance by at least 7.4% while achieving a 2.6$\times$ to 5.3$\times$ inference speedup over representative Transformer-based models. Furthermore, by explicitly tracing the scheduling trajectories, we reveal how the model autonomously adapts its forecasting behavior to capture non-stationary dynamics.
匹配关键词: autonomous experiment
---

[ACADEMIC - ARXIV]
标题: Sample-Mean Anchored Thompson Sampling for Offline-to-Online Learning with Distribution Shift
作者: Bochao Li, Yao Fu, Wei Chen, Fang Kong
链接: https://arxiv.org/abs/2605.10289v1
完整摘要: Offline-to-online learning aims to improve online decision-making by leveraging offline logged data. A central challenge in this setting is the distribution shift between offline and online environments. While some existing works attempt to leverage shifted offline data, they largely rely on UCB-type algorithms. Thompson sampling (TS) represents another canonical class of bandit algorithms, well known for its strong empirical performance and naturally suited to offline-to-online learning through its Bayesian formulation. However, unlike UCB indices, posterior samples in TS are not guaranteed to be optimistic with respect to the true arm means. This makes indices constructed from purely online and hybrid data difficult to compare and complicates their use. To address this issue, we propose sample-mean anchored TS (Anchor-TS), which introduces a novel median-based anchoring rule that defines the arm index as the median of an online posterior sample, a hybrid posterior sample, and the online sample mean. The median anchoring systematically corrects bias induced by distribution shift by mitigating over-estimation for suboptimal arms and under-estimation for optimal arms, while exploiting offline information to obtain more accurate estimates when the shift is small. We establish theoretical guarantees showing that the proposed algorithm safely leverages offline data to accelerate online learning, and quantifying how the degree of distribution shift and the size of offline data affect the resulting regret reduction. Extensive experiments demonstrate consistent improvements of our algorithm over baselines.
匹配关键词: autonomous experiment
---

[ACADEMIC - ARXIV]
标题: BROS: Bias-Corrected Randomized Subspaces for Memory-Efficient Single-Loop Bilevel Optimization
作者: Hengrui Zhang, Boao Kong, Engao Zhang, Kun Yuan
链接: https://arxiv.org/abs/2605.10288v1
完整摘要: Stochastic bilevel optimization (SBO) has become a standard framework for hyperparameter learning, data reweighting, representation learning, and data-mixture optimization in deep learning. Existing exact single-loop SBO methods and memory-efficient surrogate SBO methods either create severe memory pressure for large lower-level neural networks or lack competitive convergence guarantees under standard assumptions. In this paper, we propose BROS, a memory-efficient single-loop SBO method with the same convergence rate order as exact single-loop SBO methods. BROS performs lower and auxiliary updates in randomized subspaces with a Rademacher bi-probe correction that recovers an unbiased Hessian-action estimator. We prove that BROS preserves the $\mathcal O(\varepsilon^{-2})$ sample complexity of MA-SOBA for finding an $\varepsilon$-stationary point under only standard assumptions. Experiments on hyper-data cleaning, data-mixture learning, hyper-representation learning, and ViT sample reweighting show that BROS reduces peak memory by up to 44.9% while closely matching full-space baseline performance.
匹配关键词: autonomous experiment
---

[ACADEMIC - ARXIV]
标题: Hypothesis-Driven Deep Research with Large Language Models: A Structured Methodology for Automated Knowledge Discovery
作者: Michael Chin
链接: https://arxiv.org/abs/2605.10224v1
完整摘要: Current AI-powered research systems adopt a direct search-then-summarize paradigm that treats hypotheses as end products of scientific discovery. We argue this leaves a critical gap: hypotheses can serve a far more powerful role as organizational instruments that structure the research process itself. We propose the Hypothesis-Driven Deep Research (HDRI) methodology - the first framework using hypotheses to organize general-purpose deep research across arbitrary domains, rather than merely validating claims within specific domains. This transforms research from reactive information retrieval into proactive, verifiable, and iterative knowledge discovery. HDRI is formalized with six core principles and an eight-stage pipeline. A central innovation is the gap-driven iterative research mechanism - a closed-loop quality assurance system that automatically identifies informational and logical gaps, triggering targeted supplementary investigation. We further introduce a fact reasoning framework with traceable reasoning chains and quantified confidence propagation, a subject locking mechanism to prevent entity confusion, and a multi-dimensional quality assessment scheme. The methodology is realized in the INFOMINER system. Experiments demonstrate improvements of 22.4% in fact density, 90% subject matching accuracy, 0.92 multi-source verification confidence, and 14% completeness gain from gap-driven supplementation. Five case studies validate its practical applicability, achieving an average quality rating of 4.46/5.0.
匹配关键词: lab automation
---

[ACADEMIC - ARXIV]
标题: SciVQR: A Multidisciplinary Multimodal Benchmark for Advanced Scientific Reasoning Evaluation
作者: Longteng Guo, Xuanxu Lin, Dongze Hao, Tongtian Yue, Pengkang Huo, Jiatong Ma, Yuchen Liu, Jing Liu
链接: https://arxiv.org/abs/2605.10187v1
完整摘要: Scientific reasoning is a key aspect of human intelligence, requiring the integration of multimodal inputs, domain expertise, and multi-step inference across various subjects. Existing benchmarks for multimodal large language models (MLLMs) often fail to capture the complexity and traceability of reasoning processes necessary for rigorous evaluation. To fill this gap, we introduce SciVQR, a multimodal benchmark covering 54 subfields in mathematics, physics, chemistry, geography, astronomy, and biology. SciVQR includes domain-specific visuals, such as equations, charts, and diagrams, and challenges models to combine visual comprehension with reasoning. The tasks range from basic factual recall to complex, multi-step inferences, with 46% including expert-authored solutions. SciVQR not only evaluates final answers but also examines the reasoning process, providing insights into how models reach their conclusions. Our evaluation of leading MLLMs, including both proprietary and open-source models, reveals significant limitations in handling complex multimodal reasoning tasks, underscoring the need for improved multi-step reasoning and better integration of interdisciplinary knowledge in advancing MLLMs toward true scientific intelligence. The dataset and evaluation code are publicly available at https://github.com/CASIA-IVA-Lab/SciVQR.
匹配关键词: lab automation
---

[ACADEMIC - ARXIV]
标题: Automated Approach for Solving Infinite-state Polynomial Reachability Games
作者: Krishnendu Chatterjee, Ehsan Kafshdar Goharshady, Mehrdad Karrabi, Maximilian Seeliger, Đorđe Žikelić
链接: https://arxiv.org/abs/2605.10169v1
完整摘要: Reachability games are two-player games played on a graph, where the objective of $\texttt{REACH}$ player is to reach the target set whereas the objective of $\texttt{SAFE}$ player is to stay away from the target set. Reachability games have important applications in artificial intelligence and reactive synthesis, and many of these applications give rise to infinite-state reachability games. In this paper, we study turn-based reachability games on infinite-state graphs defined over valuations of a finite set of real variables. We consider the problem of determining the existence of and computing a winning strategy for $\texttt{REACH}$ player. Our contributions are twofold. First, we propose ranking certificates for reachability games, a sound and complete proof rule for proving that $\texttt{REACH}$ player has a winning strategy from the specified initial state. Second, we consider polynomial reachability games, where transitions and objectives are described by polynomial constraints over real variables, and propose a fully automated algorithm for computing a winning strategy for $\texttt{REACH}$ player together with a formal correctness witness in the form of a ranking certificate. The algorithm is sound, semi-complete, and runs in sub-exponential time. Our experiments demonstrate the ability of our method to solve challenging examples from the literature that were out of the reach of existing methods. Specifically, for the classical Cinderella-Stepmother game, we are able to compute an optimal winning strategy for an arbitrary precision parameter for the first time.
匹配关键词: lab automation
---

[ACADEMIC - ARXIV]
标题: NyayaAI: An AI-Powered Legal Assistant Using Multi-Agent Architecture and Retrieval-Augmented Generation
作者: Deepanshu, Divi Saxena, Deepali Rana, Ayesha Varshney, Sahinur Rahman Laskar
链接: https://arxiv.org/abs/2605.10155v1
完整摘要: Legal information in India remains largely inaccessible due to the complexity of legal language and the sheer volume of legal documentation involved in research and case analysis. This paper presents NyayaAI, an AI-powered legal assistant that automates and simplifies legal workflows for lawyers, law students, and general users. The system combines Large Language Models with a Retrieval-Augmented Generation pipeline grounded in a curated Indian legal knowledge base comprising constitutional provisions, statutes, case laws, and judicial precedents. A multi-agent architecture orchestrated through the Mastra TypeScript framework coordinates a main agent with specialized sub-agents handling legal research, document summarization, case law retrieval, and drafting assistance. A compliance module validates all responses before delivery. Domain classification achieved 70\% precision across test samples, with RAG retrieval precision at 74\% and overall response accuracy at 72\%, demonstrating that structured multi-agent LLM systems can meaningfully improve legal accessibility and workflow efficiency. The code\footnote{https://github.com/B97784/NyayaAI} is made publicly available for the benefit of the research community.
匹配关键词: lab automation
---

[ACADEMIC - ARXIV]
标题: Arcane: An Assertion Reduction Framework through Semantic Clustering and MCTS-Guided Rule Exploring
作者: Hongqin Lyu, Yonghao Wang, Zhiteng Chao, Tiancheng Wang, Huawei Li
链接: https://arxiv.org/abs/2605.10107v1
完整摘要: Assertion-based Verification (ABV) is essential for ensuring that hardware designs conform to their intended specifications. However, existing automated assertion-generation approaches, such as LLM-based frameworks, often generate large numbers of redundant assertions, which significantly degrade simulation efficiency. To mitigate the simulation overhead caused by redundant assertions, this paper proposes Arcane, an efficient assertion reduction framework. It integrates a two-tier assertion clustering approach for accurate semantic classification of large assertion sets, and employs Monte Carlo Tree Search (MCTS) to explore optimal rule-application sequences for efficient assertion reduction. The experimental results on Assertionbench [20] show that Arcane achieves a reduction of up to 76.2% in the assertion count while fully preserving formal coverage and mutation-detection ability. Further simulation studies demonstrate a speedup of 2.6x to 6.1x speedup in simulation time. The proposed framework is released at https://anonymous.4open.science/r/Arcane1-0A6F/.
匹配关键词: lab automation
---

[ACADEMIC - ARXIV]
标题: Extending Confidence-Based Text2Cypher with Grammar and Schema Aware Filtering
作者: Makbule Gulcin Ozsoy
链接: https://arxiv.org/abs/2605.10318v1
完整摘要: Large language models (LLMs) allow users to query databases using natural language by translating questions into executable queries. Despite strong progress on tasks such as Text2SQL, Text2SPARQL, and Text2Cypher, most existing methods focus on better prompting, fine-tuning, or iterative refinement. However, they often do not explicitly enforce structural constraints, such as syntactic validity and schema consistency. This can reduce reliability, since generated queries must satisfy both syntax rules and database schema constraints to be executable. In this work, we study how structured constraints can be used in test-time inference for Text2Cypher. We focus on post-generation validation to improve query correctness. We extend a confidence-based inference framework with a sequential filtering process that combines confidence scoring, grammar validation, and schema constraints before final aggregation. This lets us analyze how different constraint types affect generated queries. Our experiments with two instruction-tuned models show that grammar-based filtering improves syntactic validity. Schema-aware filtering further improves execution quality by enforcing consistency with the database structure. However, stronger filtering also increases the number of empty predictions and reduces execution coverage. Overall, we show that adding simple structural checks at test time improves the reliability of Text2Cypher generation, and we provide a clearer view of how syntax and schema constraints contribute differently.
匹配关键词: AI for science
---

[ACADEMIC - ARXIV]
标题: Relations Are Channels: Knowledge Graph Embedding via Kraus Decompositions
作者: Sayan Kumar Chaki
链接: https://arxiv.org/abs/2605.10317v1
完整摘要: Knowledge graph embedding (KGE) models typically represent each relation as an operator on entity embeddings. In this work, we identify three structural axioms that any principled relation operator must satisfy, linearity, trace preservation, and complete positivity, and show that they characterize a Kraus channel structure via the Kraus representation theorem. The completeness constraint defining this family is equivalent to these axioms, providing a principled foundation rather than an externally imposed condition. Under this formulation, most existing operator-based KGE models are recoverable as special cases with Kraus rank $κ= 1$ under specific embedding choices. We further generalize this characterization to arbitrary metric geometries by introducing \mbox{w-Kraus} channels, which satisfy completeness by construction within their respective spaces. Building on this theory, we propose \textsc{KrausKGE}, a principled KGE model that naturally handles $1$-to-$N$ and $N$-to-$N$ relations, supports $k$-hop reasoning without requiring explicit path encoders, and eliminates the need for norm constraints on entity embeddings. Additionally, our framework yields the first theoretically grounded per-relation complexity measure in the KGE literature, with a provable lower bound in terms of the empirical relation matrix rank. Empirical evaluation demonstrates that \textsc{KrausKGE} consistently outperforms strong baselines on $N$-to-$N$ relations, with performance gains that increase monotonically with relation fan-out, in alignment with theoretical predictions.
匹配关键词: AI for science
---

[ACADEMIC - ARXIV]
标题: Active Tabular Augmentation via Policy-Guided Diffusion Inpainting
作者: Zheyu Zhang, Shuo Yang, Bardh Prenkaj, Gjergji Kasneci
链接: https://arxiv.org/abs/2605.10315v1
完整摘要: Generative tabular augmentation is appealing in data-scarce domains, yet the prevailing focus on distributional fidelity does not reliably translate into better downstream models. We formalize a fidelity-utility gap: common generative objectives prioritize distributional plausibility, whereas augmentation succeeds only when injected samples reduce the current learner's held-out evaluation loss. This gap motivates learning not just how to generate, but what to generate and when to inject as training evolves. We propose TAP (Tabular Augmentation Policy), which couples diffusion inpainting with a lightweight, learner-conditioned policy to steer generation toward high-utility regions and controls safe injection via explicit gating and conservative windowed commitment. Under severe data scarcity, TAP consistently outperforms strong generative baselines on seven real-world datasets, improving classification accuracy by up to 15.6 percentage points and reducing regression RMSE by up to 32%.
匹配关键词: AI for science
---

[ACADEMIC - ARXIV]
标题: Signature Approach for Contextual Bandits with Nonlinear and Path-dependent Rewards
作者: Xin Guo, Grace He, Xinyu Li
链接: https://arxiv.org/abs/2605.10313v1
完整摘要: We study contextual bandits with nonlinear and path-dependent rewards through a novel signature-transform-based approach. Leveraging the universal nonlinearity property of signatures, we approximate continuous path-dependent reward functionals by linear functionals in the signature space. This representation enables the use of efficient linear contextual bandit methods while preserving expressive sequential structure. Building on this framework, we propose \texttt{DisSigUCB}, a signature-based disjoint upper confidence bound (UCB) algorithm. Under boundedness and non-degeneracy assumptions, we prove a high-probability data-dependent sublinear regret bound of order \(\tilde{\mathcal O}(\sqrt{(d+m)KT})\) where \(d\) is the context dimension and \(m\) is the signature feature dimension. Synthetic experiments and numerical applications on temperature sensor monitoring, sleep-stage classification, and hospital nurse staffing demonstrate that \texttt{DisSigUCB} consistently outperforms classical linear and kernelized contextual bandit baselines in nonlinear and path-dependent settings.
匹配关键词: AI for science
---

[ACADEMIC - ARXIV]
标题: Positive Alignment: Artificial Intelligence for Human Flourishing
作者: Ruben Laukkonen, Seb Krier, Chloé Bakalar, Shamil Chandaria, Morten Kringelbach, Adam Elwood, Daniel Ford, Fernando Rosas, Maty Bohacek, Matija Franklin, Nenad Tomašev, Stephanie Chan, Verena Rieser, Roma Patel, Michael Levin, Arun Rao
链接: https://arxiv.org/abs/2605.10310v1
完整摘要: Existing alignment research is dominated by concerns about safety and preventing harm: safeguards, controllability, and compliance. This paradigm of alignment parallels early psychology's focus on mental illness: necessary but incomplete. What we call Positive Alignment is the development of AI systems that (i) actively support human and ecological flourishing in a pluralistic, polycentric, context-sensitive, and user-authored way while (ii) remaining safe and cooperative. It is a distinct and necessary agenda within AI alignment research. We argue that several existing failures of alignment (e.g., engagement hacking, loss of human autonomy, failures in truth-seeking, low epistemic humility, error correction, lack of diverse viewpoints, and being primarily reactive rather than proactive) may be better addressed through positive alignment, including cultivating virtues and maximizing human flourishing. We highlight a range of challenges, open questions, and technical directions (e.g., data filtering and upsampling, pre- and post-training, evaluations, collaborative value collection) for different phases of the LLM and agents lifecycle. We end with design principles for promoting disagreement and decentralization through contextual grounding, community customization, continual adaptation, and polycentric governance; that is, many legitimate centers of oversight rather than one institutional or moral chokepoint.
匹配关键词: AI for science
---

[ACADEMIC - ARXIV]
标题: DeepLog: A Software Framework for Modular Neurosymbolic AI
作者: Robin Manhaeve, Stefano Colamonaco, Vincent Derkinderen, Rik Adriaensen, Lucas Van Praet, Luc De Raedt, Giuseppe Marra
链接: https://arxiv.org/abs/2605.10279v1
完整摘要: DeepLog is an operational neurosymbolic framework that unifies logic and deep learning within standard PyTorch workflows. While existing neurosymbolic systems focus on a particular paradigm and semantics, DeepLog serves as a universal backend that can emulate many systems in the neurosymbolic alphabet soup. By treating diverse neurosymbolic languages as high-level specifications, the DeepLog software automatically compiles them into optimized arithmetic circuits. This design lowers the barrier for machine learning practitioners by treating logic as composable modules, while providing neurosymbolic developers with a shared, high-performance basis for prototyping new integration strategies. The code is available here: https://github.com/ML-KULeuven/deeplog
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
标题: jNO: A JAX Library for Neural Operator and Foundation Model Training
作者: Leon Armbruster, Rathan Ramesh, Georg Kruse, Christopher Straub
链接: https://arxiv.org/abs/2605.10159v1
完整摘要: jNO (jax Neural Operators) is a JAX-native library for neural operators and foundation models with unified support for both data-driven and physics-informed training. Its core design is a tracing system in which domains, model calls, residuals, supervised losses, and diagnostics are written in one symbolic language and compiled into one optimization pipeline. This allows users to move between operator regression, mesh-aware residual evaluation, and PDE-constrained training without restructuring the surrounding code. jNO also supports multi-model compositions, fine-grained control at parameter level (model, optimizer, and learning rate), hyperparameter tuning, and JAX-native workflows for translated PDE foundation-model families. The source repository is available at https://github.com/FhG-IISB/jNO.
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
标题: ReLibra: Routing-Replay-Guided Load Balancing for MoE Training in Reinforcement Learning
作者: Chao Jin, Xinming Wei, Yinmin Zhong, Chengxu Yang, Bingyang Wu, Ruidong Zhu, Zili Zhang, Yuliang Liu, Xin Jin
链接: https://arxiv.org/abs/2605.08639v1
完整摘要: Load imbalance is a long-standing challenge in Mixture-of-Experts (MoE) training and is exacerbated in reinforcement learning (RL) for LLMs, where hot experts can shift frequently across micro-batches. Existing MoE training systems rely on historical loads to predict future expert demand, making them less effective under sharp fluctuations. We propose ReLibra, an MoE RL training system that exploits a unique opportunity in RL's rollout-training workflow, routing replay, to enable fine-grained load balancing at micro-batch granularity. Because rollout and training process the same tokens with the same MoE parameters, the token-to-expert routing decisions are known before training starts. Leveraging this information, ReLibra places two MoE load-balancing mechanisms at inter- and intra-batch timescales, matching their communication patterns to hierarchical network bandwidths. At the inter-batch timescale, ReLibra performs expert reordering to redistribute experts for batch-level cross-node balancing; at the intra-batch timescale, it dynamically performs expert replication within a node to absorb micro-batch-level load fluctuations. Experiments on diverse MoE LLMs and RL workloads show that ReLibra improves training throughput by up to 1.6$\times$ over Megatron-LM and by up to 1.2$\times$ over EPLB, even when EPLB is given oracle loads. Moreover, ReLibra remains within 6%-10% of the throughput of an idealized balanced baseline.
匹配关键词: Megatron
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
标题: Structured Recurrent Mixers for Massively Parallelized Sequence Generation
作者: Benjamin L. Badger
链接: https://arxiv.org/abs/2605.08696v1
完整摘要: Over the last two decades, language modeling has experienced a shift from predominantly recurrent architectures that process tokens sequentially during training and inference to non-recurrent models that process sequence elements in parallel during training, which results in greater training efficiency and stability at the expense of lower inference throughput. Here we introduce the Structured Recurrent Mixer, an architecture that allows for algebraic conversion between a sequence parallel representation at train time and a recurrent representation at inference, notably without the need for specialized kernels or device-specific memory management. We show experimentally that this dual representation allows for greater training efficiency, higher input information capacity, and larger inference throughput and concurrency when compared to other linear complexity models. We postulate that recurrent models are poorly suited to extended sequence length scaling for information-rich inputs typical of language, but are well suited to scaling in the sample (batch) dimension due to their constant memory per sample. We provide Mojo/MAX inference implementations of SRMs exhibiting 12x the throughput and 170x the concurrency of similarly powerful Transformers inferenced on vLLM, increases characteristic of Pytorch implementations resulting in a 30\% increase in compute-constant GSM8k Pass@k. We conclude by demonstrating that SRMs are effective reinforcement learning training candidates.
匹配关键词: vLLM
---

[ACADEMIC - ARXIV]
标题: Uncovering Intra-expert Activation Sparsity for Efficient Mixture-of-Expert Model Execution
作者: Jongseok Park, Sunga Kim, Zhenyu Gu, Ion Stoica, Alvin Cheung
链接: https://arxiv.org/abs/2605.08575v1
完整摘要: Mixture of Experts (MoE) architecture has become the standard for state-of-the-art large language models, owing to its computational efficiency through sparse expert activation. However, sparsity through finer expert granularity is becoming increasingly difficult to achieve due to fundamental training challenges such as expert collapse and load imbalance. In this work, we explore and leverage intra-expert activation sparsity as a complementary and underexplored dimension of sparsity in MoE models. Surprisingly, substantial intra-expert sparsity is readily available in existing pre-trained MoE models, without any modification to the activation function or model parameters, providing up to 90% sparsity within each expert without significant accuracy loss. We explore intra-expert activation sparsity across eight off-the-shelf MoE models ranging from 1B to 400B parameters, and extend the MoE execution pipeline of vLLM to leverage intra-expert activation sparsity by skipping the computations of inactive neurons, on top of its existing optimizations, achieving up to 2.5 times speedup in MoE layer execution and 1.2 times end-to-end speedup compared to the original dense vLLM baseline.
匹配关键词: vLLM
---

[ACADEMIC - ARXIV]
标题: FlashEvolve: Accelerating Agent Self-Evolution with Asynchronous Stage Orchestration
作者: Zhengding Hu, Mingge Lu, Zhen Wang, Jixuan Ruan, Chang Chen, Zaifeng Pan, Yue Guan, Ruiyi Wang, Zhongkai Yu, Chao Zhang, Yufei Ding
链接: https://arxiv.org/abs/2605.08520v1
完整摘要: LLM-based evolution has emerged as a promising way to improve agents by refining non-parametric artifacts, but its wall-clock cost remains a major bottleneck. We identify that this cost comes from synchronized stage execution and imbalance inside each LLM-heavy stage. We present FlashEvolve, an efficient framework that replaces synchronized execution with asynchronous workers and queues, allowing different stages and steps to overlap. To handle data staleness introduced by asynchrony, FlashEvolve tracks artifact versions and applies different policies to update, discard, or patch stale artifacts. Unlike weight-space staleness in asynchronous RL, language-space staleness is inspectable and repairable: a stale artifact is not just delayed work, but readable evidence that the LLM can reflect on, revise, and turn into useful evolution signal. FlashEvolve further improves throughput and token efficiency with speculative stage completion and adaptive workflow control. On GEPA workloads, FlashEvolve improves proposal throughput by $3.5\times$ on local vLLM and $4.9\times$ on API serving over synchronous GEPA. The same design also applies to ACE and Meta-Harness.
匹配关键词: vLLM
---

[ACADEMIC - ARXIV]
标题: Priming: Hybrid State Space Models From Pre-trained Transformers
作者: Aditya Chattopadhyay, Elvis Nunez, Prannay Kaul, Benjamin Bowman, Evan Becker, Luca Zancato, David Thomas, Wei Xia, Stefano Soatto
链接: https://arxiv.org/abs/2605.08301v1
完整摘要: Hybrid State-Space models combine Attention with recurrent State-Space Model (SSM) layers, balancing eidetic memory from Attention with compressed fading memory from SSMs. This yields smaller Key-Value caches and faster decoding than Transformers, along with a richer architectural design space. Exploring that design space at scale has so far required training from scratch, a barrier that has kept most large-model Hybrid research within a narrow range of architectures. We introduce Priming, a method that turns Hybrid architecture design from a pre-training problem into a knowledge transfer one. Priming initializes a Hybrid model from a pre-trained Transformer and, through short alignment and post-training phases, recovers downstream quality using less than 0.5% of the source model's pre-training token budget. Priming is agnostic to the source Transformer family (e.g., Qwen, Llama, Mistral), model class (dense or Mixture-of-Experts), and model scale. Priming enables us to run the first controlled comparison of SSM layer types at scale under identical conditions. We evaluate, Gated KalmaNet (GKA), Gated DeltaNet (GDN), and Mamba-2, and show that their expressiveness hierarchy, GKA>GDN>Mamba-2, directly predicts downstream performance on long-context reasoning tasks. We scale Priming to 8B/32B reasoning models with native 128K contexts. Our Hybrid GKA 32B improves over its source Qwen3-32B by +3.8 average reasoning points, while staying within 1% of a Transformer post-trained on the same data and enabling up to 2.3x higher decode throughput. To foster research on Hybrid architectures, we release a model zoo of primed Hybrid models for long-context reasoning and instruction following, together with the Priming training and inference code (Sequence Parallelism algorithms for long-context training, optimized GKA kernels, and vLLM serving plugin), all under Apache~2.0 License.
匹配关键词: vLLM
---

[ACADEMIC - ARXIV]
标题: UniPrefill: Universal Long-Context Prefill Acceleration via Block-wise Dynamic Sparsification
作者: Qihang Fan, Huaibo Huang, Zhiying Wu, Bingning Wang, Ran He
链接: https://arxiv.org/abs/2605.06221v1
完整摘要: As large language models (LLMs) continue to advance rapidly, they are becoming increasingly capable while simultaneously demanding ever-longer context lengths. To improve the inference efficiency of long-context processing, several novel low-complexity hybrid architectures have recently been proposed, effectively alleviating the computational burden of long-context inference. However, existing research on long-context prefill acceleration remains predominantly focused on sparse attention mechanisms, which achieve their maximum speedup only on full-attention models. When transferred to emerging architectures--such as linear/full attention hybrids or sliding window/full attention hybrids--these prefill acceleration approaches suffer significant performance degradation. Furthermore, such methods are generally incompatible with continuous batching, making them difficult to integrate into modern inference engines such as vLLM. To this end, we propose UniPrefill, a prefill acceleration framework applicable to virtually any model architecture, which directly accelerates the model's computation at the token level. We further implement UniPrefill as a continuous batching operator and extend vLLM's scheduling strategy to natively support prefill-decode co-processing and tensor parallel for UniPrefill, enabling its seamless integration into vLLM. UniPrefill achieves up to 2.1x speedup in Time-To-First-Token (TTFT), with the acceleration becoming increasingly pronounced as the number of concurrent requests grows.
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
标题: Non-Monotonic Latency in Apple MPS Decoding: KV Cache Interactions and Execution Regimes
作者: Willy Fitra Hendria
链接: https://arxiv.org/abs/2605.08913v1
完整摘要: Autoregressive inference is typically assumed to scale predictably with decoding length, and key-value (KV) caching is widely regarded as a universally beneficial optimization for accelerating decoding. In this work, we identify unexpected non-monotonic latency behavior in the Apple MPS backend, where latency changes abruptly across nearby decoding configurations. Using transformer models from multiple families (GPT-2, BLOOM, and OPT), we observe latency spikes of up to 21x within specific decoding-budget intervals, followed by recovery at neighboring configurations. Controlled experiments show that these anomalies are not explained by memory pressure or prefill cost, but are instead consistent with backend execution dynamics, while CPU and NVIDIA T4 (CUDA) exhibit smooth monotonic scaling under identical conditions. Our findings highlight the importance of hardware-aware evaluation for autoregressive inference and caution against relying on aggregated decoding-budget benchmarks, as performance can vary discontinuously across nearby configurations.
匹配关键词: CUDA
---

[ACADEMIC - ARXIV]
标题: CUDAHercules: Benchmarking Hardware-Aware Expert-level CUDA Optimization for LLMs
作者: Shiyang Li, Zijian Zhang, Guangyan Sun, Yuebo Luo, Winson Chen, Yanzhi Wang, Mingyi Hong, Caiwen Ding
链接: https://arxiv.org/abs/2605.08467v1
完整摘要: Large language models show promise for automated CUDA programming, however even the strongest coding models (e.g., Claude-Opus-4.6) may still fall short of expert-level, architecture-aware optimization. We introduce CUDAHercules, a benchmark that evaluates generated CUDA against end-to-end human-expert SOTA systems. It spans single kernels, module-level operators, full applications, and unsolved challenge tasks across Ampere, Hopper, and Blackwell GPUs, with end-to-end tasks gated by domain-specific semantic validators. Evaluating models such as Claude-Opus-4.6 and GPT-5.4 shows a large gap between runnable CUDA and expert CUDA engineering: models often compile and pass tests, but rarely recover the optimization strategies needed to match expert performance. Application semantics further reduce success, and iterative or tool-augmented feedback can improve correctness while drifting toward slow fallback implementations. These results show that automated CUDA programming remains far from fully solved and requires stronger hardware reasoning, better tool use, and training objectives that connect code understanding to hardware architecture-grounded intelligence.
匹配关键词: CUDA
---

[ACADEMIC - ARXIV]
标题: CUDABeaver: Benchmarking LLM-Based Automated CUDA Debugging
作者: Shiyang Li, Haoyang Chen, Mattia Fazzini, Caiwen Ding
链接: https://arxiv.org/abs/2605.08455v1
完整摘要: Debugging CUDA programs has long been challenging because failures often arise from subtle interactions among hardware behavior, compiler decisions, memory hierarchy, and asynchronous execution. More importantly, with the rapid expansion of GPU usage across scientific computing, machine learning, graphics, and systems workloads, CUDA debugging has become more challenging than ever. Current evaluations of LLM-based CUDA programming largely miss this setting: a model can pass correctness tests with repair by degeneration, simplifying the CUDA code into a safer but slower program that abandons the original optimization structure. We introduce CUDABEAVER, a benchmark for CUDA debugging from real failing workspaces produced during LLM-based CUDA generation. Each task provides the broken candidate, native build/test commands, raw error evidence, and a single editable file. CUDABEAVER evaluates whether a fixer truly repairs the failing CUDA code or merely finds a slower test-passing replacement, reporting results by failure category, debugging trajectory, stagnation mode, and performance preservation. We further propose pass@k(M,C,A), a protocol-conditional CUDA debugging metric by making the fixer M, corpus C, and protocol axes Aexplicit. Using this metric across 213 tasks and seven frontier LLMs, we show that protocol-aware evaluation gives a more faithful view of CUDA debugging ability: when performance-loss tolerance is high, fixers appear much stronger, but even a minor stricter performance requirement can sharply reduce measured success, shifting scores by up to 40 percentage points.
匹配关键词: CUDA
---

[ACADEMIC - ARXIV]
标题: FlashSVD v1.5: Making Low-Rank Transformers Inference Actually Fast
作者: Wenhao Wu, Zishan Shao, Kangning Cui, Jinhee Kim, Yixiao Wang, Hancheng Ye, Danyang Zhuo, Yiran Chen
链接: https://arxiv.org/abs/2605.08314v1
完整摘要: SVD-based Low-rank compression reduces transformer parameters and nominal FLOPs, but these savings often translate poorly into real LLM serving speedups. We show that this gap is largely a runtime problem: factorized checkpoints fragment execution paths, and the resulting overhead differs substantially between prefill and autoregressive decode. We present FlashSVD v1.5, a unified inference runtime for serving SVD-compressed transformers. FlashSVD v1.5 maps diverse public SVD compression families to a common factorized representation and combines phase-specific kernels with dense-KV decode, packed MLP execution, and per-layer CUDA-graph replay to reorganize the low-rank serving path into a thin runtime. Across representative decoder-serving settings, FlashSVD v1.5 achieves up to 2.55x decode and 2.39x end-to-end speedup, and it attains 1.48x average decode and 1.44x average end-to-end speedup across multiple popular SVD compression families. These results suggest that practical low-rank acceleration requires runtime co-design, not compression algorithms alone. Our code is available at: https://github.com/Zishan-Shao/FlashSVD.
匹配关键词: CUDA
---

[ACADEMIC - ARXIV]
标题: CuBridge: An LLM-Based Framework for Understanding and Reconstructing High-Performance Attention Kernels
作者: Xing Ma, Yangjie Zhou, Wu Sun, Zihan Liu, Jingwen Leng, Yun Lin, Shixuan Sun, Minyi Guo, Jin Song Dong
链接: https://arxiv.org/abs/2605.05023v1
完整摘要: Efficient CUDA implementations of attention mechanisms are critical to modern deep learning systems, yet supporting diverse and evolving attention variants remains challenging. Existing frameworks and compilers trade performance for flexibility, while expert-written kernels achieve high efficiency but are difficult to adapt. Recent work explores large language models (LLMs) for GPU kernel generation, but prior studies report unstable correctness and significant performance gaps for complex operators such as attention. We present CuBridge, an LLM-based framework that adapts expert-written attention kernels through a structured lift-transfer-lower workflow. CuBridge starts from expert-written CUDA attention kernels and lifts them into an executable intermediate representation that makes execution orchestration explicit while abstracting low-level CUDA syntax. Given a user-provided PyTorch specification, CuBridge generates and verifies a target IR program, then reconstructs optimized CUDA code via reference-guided lowering. Across diverse attention variants and GPU platforms, CuBridge consistently produces correct kernels and substantially outperforms general frameworks, compiler-based approaches, and prior LLM-based methods.
匹配关键词: CUDA
---

[ACADEMIC - ARXIV]
标题: Active Tabular Augmentation via Policy-Guided Diffusion Inpainting
作者: Zheyu Zhang, Shuo Yang, Bardh Prenkaj, Gjergji Kasneci
链接: https://arxiv.org/abs/2605.10315v1
完整摘要: Generative tabular augmentation is appealing in data-scarce domains, yet the prevailing focus on distributional fidelity does not reliably translate into better downstream models. We formalize a fidelity-utility gap: common generative objectives prioritize distributional plausibility, whereas augmentation succeeds only when injected samples reduce the current learner's held-out evaluation loss. This gap motivates learning not just how to generate, but what to generate and when to inject as training evolves. We propose TAP (Tabular Augmentation Policy), which couples diffusion inpainting with a lightweight, learner-conditioned policy to steer generation toward high-utility regions and controls safe injection via explicit gating and conservative windowed commitment. Under severe data scarcity, TAP consistently outperforms strong generative baselines on seven real-world datasets, improving classification accuracy by up to 15.6 percentage points and reducing regression RMSE by up to 32%.
匹配关键词: distributed training
---

[ACADEMIC - ARXIV]
标题: Positive Alignment: Artificial Intelligence for Human Flourishing
作者: Ruben Laukkonen, Seb Krier, Chloé Bakalar, Shamil Chandaria, Morten Kringelbach, Adam Elwood, Daniel Ford, Fernando Rosas, Maty Bohacek, Matija Franklin, Nenad Tomašev, Stephanie Chan, Verena Rieser, Roma Patel, Michael Levin, Arun Rao
链接: https://arxiv.org/abs/2605.10310v1
完整摘要: Existing alignment research is dominated by concerns about safety and preventing harm: safeguards, controllability, and compliance. This paradigm of alignment parallels early psychology's focus on mental illness: necessary but incomplete. What we call Positive Alignment is the development of AI systems that (i) actively support human and ecological flourishing in a pluralistic, polycentric, context-sensitive, and user-authored way while (ii) remaining safe and cooperative. It is a distinct and necessary agenda within AI alignment research. We argue that several existing failures of alignment (e.g., engagement hacking, loss of human autonomy, failures in truth-seeking, low epistemic humility, error correction, lack of diverse viewpoints, and being primarily reactive rather than proactive) may be better addressed through positive alignment, including cultivating virtues and maximizing human flourishing. We highlight a range of challenges, open questions, and technical directions (e.g., data filtering and upsampling, pre- and post-training, evaluations, collaborative value collection) for different phases of the LLM and agents lifecycle. We end with design principles for promoting disagreement and decentralization through contextual grounding, community customization, continual adaptation, and polycentric governance; that is, many legitimate centers of oversight rather than one institutional or moral chokepoint.
匹配关键词: distributed training
---

[ACADEMIC - ARXIV]
标题: PaMoSplat: Part-Aware Motion-Guided Gaussian Splatting for Dynamic Scene Reconstruction
作者: Yinan Deng, Jianyu Dou, Jiahui Wang, Jingyu Zhao, Yi Yang, Yufeng Yue
链接: https://arxiv.org/abs/2605.10307v1
完整摘要: Dynamic scene reconstruction represents a fundamental yet demanding challenge in computer vision and robotics. While recent progress in 3DGS-based methods has advanced dynamic scene modeling, obtaining high-fidelity rendering and accurate tracking in scenarios with substantial, intricate motions remains significantly challenging. To address these challenges, we propose PaMoSplat, a novel dynamic Gaussian splatting framework incorporating part awareness and motion priors. Our approach is grounded in two key observations: 1) Parts serve as primitives for scene deformation, and 2) Motion cues from optical flow can effectively guide part motion. Specifically, PaMoSplat initializes by lifting multi-view segmentation masks into 3D space via graph clustering, establishing coherent Gaussian parts. For subsequent timestamps, we leverage a differential evolutionary algorithm to estimate the rigid motion of these parts using multi-view optical flow cues, providing a robust warm-start for further optimization. Additionally, PaMoSplat introduces an adaptive iteration count mechanism, internal learnable rigidity, and flow-supervised rendering loss to accelerate and optimize the training process. Comprehensive evaluations across diverse scenes, including real-world environments, demonstrate that PaMoSplat delivers superior rendering quality, improved tracking precision, and faster convergence compared to existing methods. Furthermore, it enables multiple part-level downstream applications, such as 4D scene editing.
匹配关键词: distributed training
---

[ACADEMIC - ARXIV]
标题: Follow the Mean: Reference-Guided Flow Matching
作者: Pedro M. P. Curvo, Maksim Zhdanov, Floor Eijkelboom, Jan-Willem van de Meent
链接: https://arxiv.org/abs/2605.10302v1
完整摘要: Existing approaches to controllable generation typically rely on fine-tuning, auxiliary networks, or test-time search. We show that flow matching admits a different control interface: adaptation through examples. For deterministic interpolants, the velocity field is solely governed by a conditional endpoint mean; shifting this mean shifts the flow itself. This yields a simple principle for controllable generation: steer a pretrained model by changing the reference set it follows. We instantiate this idea in two forms. Reference-Mean Guidance is training-free: it computes a closed-form endpoint-mean correction from a reference bank and applies it to a frozen FLUX.2-klein (4B) model, enabling control of color, identity, style, and structure while keeping the prompt, seed, and weights fixed. Semi-Parametric Guidance amortizes the same idea through an explicit mean anchor and learned residual refiner, matching unconditional DiT-B/4 quality on AFHQv2 while allowing the reference set to be swapped at inference time. These results point to a broader direction: generative models that adapt through data, not parameter updates.
匹配关键词: distributed training
---

[ACADEMIC - ARXIV]
标题: Set Prediction for Next-Day Active Fire Forecasting
作者: Yuchen Bai, Georgios Athanasiou, Xin Yu, Diogenis Antonopoulos, Ioannis Papoutsis, Stijn Hantson, Nuno Carvalhais
链接: https://arxiv.org/abs/2605.10298v1
完整摘要: Accurate next-day active fire forecasts can support early warning, disaster response, forest risk assessment, and downstream estimation of fire-related carbon emissions. Existing machine learning approaches to wildfire forecasting typically predict wildfire danger or fire probability on kilometre-scale daily grids, which is useful for regional warning but does not directly represent localized fire events. We propose Wildfire Ignition Set Predictor (WISP), a query-based model that reformulates next-day active fire forecasting as point-set prediction. From 48 hours of covariates including meteorology, satellite vegetation products, static land, and fire history, WISP predicts a fixed-size ranked set of future active fire cluster centres on a 375 m grid across globally distributed regions. The model is trained end-to-end with Hungarian matching; to address the conflicting roles of the classification score in assignment, ranking, and query activation, we use asymmetric classification-localization weighting in matching and loss. We further construct a globally distributed, hourly, multi-source benchmark for this task. On a held-out test set spanning fire regions worldwide, the best WISP variant achieves 38.2% average precision (AP) for ranked fire-centre detections, covers 53.4% of fire cluster mass weighted by fire radiative power (FRP), and localizes 54.1% of observed clusters within 5 km. These results establish sparse set prediction as a viable formulation for high-resolution wildfire forecasting and provide a benchmark for future work in this regime.
匹配关键词: distributed training
---

[ACADEMIC - ARXIV]
标题: Signature Approach for Contextual Bandits with Nonlinear and Path-dependent Rewards
作者: Xin Guo, Grace He, Xinyu Li
链接: https://arxiv.org/abs/2605.10313v1
完整摘要: We study contextual bandits with nonlinear and path-dependent rewards through a novel signature-transform-based approach. Leveraging the universal nonlinearity property of signatures, we approximate continuous path-dependent reward functionals by linear functionals in the signature space. This representation enables the use of efficient linear contextual bandit methods while preserving expressive sequential structure. Building on this framework, we propose \texttt{DisSigUCB}, a signature-based disjoint upper confidence bound (UCB) algorithm. Under boundedness and non-degeneracy assumptions, we prove a high-probability data-dependent sublinear regret bound of order \(\tilde{\mathcal O}(\sqrt{(d+m)KT})\) where \(d\) is the context dimension and \(m\) is the signature feature dimension. Synthetic experiments and numerical applications on temperature sensor monitoring, sleep-stage classification, and hospital nurse staffing demonstrate that \texttt{DisSigUCB} consistently outperforms classical linear and kernelized contextual bandit baselines in nonlinear and path-dependent settings.
匹配关键词: GPU optimization
---

[ACADEMIC - ARXIV]
标题: PaMoSplat: Part-Aware Motion-Guided Gaussian Splatting for Dynamic Scene Reconstruction
作者: Yinan Deng, Jianyu Dou, Jiahui Wang, Jingyu Zhao, Yi Yang, Yufeng Yue
链接: https://arxiv.org/abs/2605.10307v1
完整摘要: Dynamic scene reconstruction represents a fundamental yet demanding challenge in computer vision and robotics. While recent progress in 3DGS-based methods has advanced dynamic scene modeling, obtaining high-fidelity rendering and accurate tracking in scenarios with substantial, intricate motions remains significantly challenging. To address these challenges, we propose PaMoSplat, a novel dynamic Gaussian splatting framework incorporating part awareness and motion priors. Our approach is grounded in two key observations: 1) Parts serve as primitives for scene deformation, and 2) Motion cues from optical flow can effectively guide part motion. Specifically, PaMoSplat initializes by lifting multi-view segmentation masks into 3D space via graph clustering, establishing coherent Gaussian parts. For subsequent timestamps, we leverage a differential evolutionary algorithm to estimate the rigid motion of these parts using multi-view optical flow cues, providing a robust warm-start for further optimization. Additionally, PaMoSplat introduces an adaptive iteration count mechanism, internal learnable rigidity, and flow-supervised rendering loss to accelerate and optimize the training process. Comprehensive evaluations across diverse scenes, including real-world environments, demonstrate that PaMoSplat delivers superior rendering quality, improved tracking precision, and faster convergence compared to existing methods. Furthermore, it enables multiple part-level downstream applications, such as 4D scene editing.
匹配关键词: GPU optimization
---

[ACADEMIC - ARXIV]
标题: Nearly-Optimal Algorithm for Adversarial Kernelized Bandits
作者: Shogo Iwazaki
链接: https://arxiv.org/abs/2605.10299v1
完整摘要: This paper studies kernelized bandits (also known as Gaussian process bandits) in an adversarial environment, where the reward functions in a known reproducing kernel Hilbert space (RKHS) may be adversarially chosen at each round. We show that the exponential-weight algorithm achieves $\tilde{O}(\sqrt{T γ_T})$ adversarial regret, where $T$ and $γ_T$ denote the number of total rounds and the maximum information gain, respectively. For squared exponential (SE) and $ν$-Matérn kernels, we also show algorithm-independent lower bounds that guarantee the optimality of our algorithm up to polylogarithmic factors. Furthermore, we present a computationally efficient variant of our algorithm using Nyström approximation while maintaining nearly optimal regret guarantees.
匹配关键词: GPU optimization
---

[ACADEMIC - ARXIV]
标题: LeapTS: Rethinking Time Series Forecasting as Adaptive Multi-Horizon Scheduling
作者: Sheng Pan, Ming Jin, Bo Du, Shirui Pan
链接: https://arxiv.org/abs/2605.10292v1
完整摘要: Time series forecasting serves as an essential tool for many real-world applications, supporting tasks such as resource optimization and decision-making. Despite significant architectural advancements, most modern models still treat forecasting task as a fixed mapping from history to target horizons. This induces temporal decoupling across future time points and limits the model's ability to adapt to the evolving context as forecasting progresses. In this work, we present LeapTS, a novel framework that reformulates time series forecasting as a dynamic scheduling process over the prediction horizon. Specifically, LeapTS organizes the forecasting process into multi-level decisions using: (1) the hierarchical controller to dynamically select the optimal prediction scale and advancement length at each step, and (2) continuous-time state evolution driven by neural controlled differential equations. Within this process, the controlled update mechanism explicitly couples the irregular temporal dynamics with discrete scheduling feedback. Extensive evaluations on both real-world and synthetic datasets demonstrate that LeapTS improves overall forecasting performance by at least 7.4% while achieving a 2.6$\times$ to 5.3$\times$ inference speedup over representative Transformer-based models. Furthermore, by explicitly tracing the scheduling trajectories, we reveal how the model autonomously adapts its forecasting behavior to capture non-stationary dynamics.
匹配关键词: GPU optimization
---

[ACADEMIC - ARXIV]
标题: Sample-Mean Anchored Thompson Sampling for Offline-to-Online Learning with Distribution Shift
作者: Bochao Li, Yao Fu, Wei Chen, Fang Kong
链接: https://arxiv.org/abs/2605.10289v1
完整摘要: Offline-to-online learning aims to improve online decision-making by leveraging offline logged data. A central challenge in this setting is the distribution shift between offline and online environments. While some existing works attempt to leverage shifted offline data, they largely rely on UCB-type algorithms. Thompson sampling (TS) represents another canonical class of bandit algorithms, well known for its strong empirical performance and naturally suited to offline-to-online learning through its Bayesian formulation. However, unlike UCB indices, posterior samples in TS are not guaranteed to be optimistic with respect to the true arm means. This makes indices constructed from purely online and hybrid data difficult to compare and complicates their use. To address this issue, we propose sample-mean anchored TS (Anchor-TS), which introduces a novel median-based anchoring rule that defines the arm index as the median of an online posterior sample, a hybrid posterior sample, and the online sample mean. The median anchoring systematically corrects bias induced by distribution shift by mitigating over-estimation for suboptimal arms and under-estimation for optimal arms, while exploiting offline information to obtain more accurate estimates when the shift is small. We establish theoretical guarantees showing that the proposed algorithm safely leverages offline data to accelerate online learning, and quantifying how the degree of distribution shift and the size of offline data affect the resulting regret reduction. Extensive experiments demonstrate consistent improvements of our algorithm over baselines.
匹配关键词: GPU optimization
---

[ACADEMIC - ARXIV]
标题: One-Step Graph-Structured Neural Flows for Irregular Multivariate Time Series Classification
作者: Mengzhou Gao, Kaiwei Wang, Pengfei Jiao
链接: https://arxiv.org/abs/2605.10179v1
完整摘要: Neural Flows efficiently model irregular multivariate time series by directly learning ODE solution trajectories with neural networks, bypassing step-by-step numerical solvers. Despite their efficiency, many existing approaches treat variables independently, leaving inter-variable interactions underexplored. Moreover, their one-step mapping makes interaction modeling inherently challenging, as it removes the iterative refinement of interactions during learning. To address this challenge, we propose one-step Graph-Structured Neural Flows (GSNF), which introduce two auxiliary-trajectory self-supervision strategies to strengthen interaction learning: (i) interaction-aware trajectory generation via re-initialization, which induces trajectory divergence to expose graph-induced interactions, with a theoretically derived lower bound on divergence; and (ii) reverse-time trajectory generation, which enforces forward-backward consistency to regularize graph learning, enabled by flow invertibility. Experiments on five real-world datasets show that GSNF achieves state-of-the-art classification performance with highly competitive training time and memory usage.
匹配关键词: self-supervised
---

[ACADEMIC - ARXIV]
标题: Only Train Once: Uncertainty-Aware One-Class Learning for Face Authenticity Detection
作者: Qingchao Jiang, Zhenxuan Hou, Zhiying Zhu, Zhenxing Qian, Xinpeng Zhang, Zaiwang Gu
链接: https://arxiv.org/abs/2605.10040v1
完整摘要: The rapid evolution of generative paradigms has enabled the creation of highly realistic imagery, which escalating the risks of identity fraud and the dissemination of disinformation. Most existing approaches frame face forgery detection as a fully supervised binary classification problem. Consequently, these models typically exhibit significant performance decay when tasked with detecting forgeries from previously unseen generative paradigms. Furthermore, these methods focus exclusively on either DeepFakes or fully synthesized faces, thereby failing to provide a generalized framework for universal face forgery detection. In this paper, we address this challenge by introducing FADNet (Face Authenticity Detector Net), % a self-supervised framework that which reformulates face forgery detection as a one-class classification (OCC) task. By training exclusively on authentic facial data to capture their intrinsic representations, FADNet flags any image whose feature embedding deviates significantly from the learned distribution of real faces as a forgery. The framework incorporates Evidential Deep Learning (EDL) to quantify predictive uncertainty and utilizes a plug-and-play pseudo-forgery image generator (PFIG) to tighten decision boundaries around authentic data. Extensive experimental evaluations on the DF40 and ASFD benchmarks demonstrate that FADNet achieves superior performance and generalization capabilities. Specifically, FADNet substantially outperforms existing state-of-the-art (SOTA) methods, yielding a remarkable average accuracy of 96.63\% and an average precision of 98.83\%.
匹配关键词: self-supervised
---

[ACADEMIC - ARXIV]
标题: Learning to Perceive "Where": Spatial Pretext Tasks for Robust Self-Supervised Learning
作者: Yang Shen, Yusen Cai, Weronika Hryniewska-Guzik, Qing Lin, Mengmi Zhang
链接: https://arxiv.org/abs/2605.09963v1
完整摘要: Existing self-supervised learning (SSL) methods primarily learn object-invariant representations but often neglect the spatial structure and relationships among object parts. To address this limitation, we introduce Spatial Prediction (SP), a spatially aware pretext regression task that predicts the relative position and scale between a pair of disentangled local views from the same image. By modeling part-to-part relationships in a continuous geometric space, SP encourages representations to capture fine-grained spatial dependencies beyond invariant categorical semantics, thereby learning the compositional structure of visual scenes. SP is implemented as a decoupled plug-in and can be seamlessly integrated into diverse SSL frameworks. Extensive experiments show consistent improvements across image recognition, fine-grained classification, semantic segmentation, and depth estimation, as well as substantial gains in out-of-distribution robustness for object recognition. To evaluate spatial reasoning, we introduce (1) a position and scale prediction task on image patch pairs and (2) a jigsaw understanding task requiring patch reordering and recognition after reconstruction. Strong performance on these tasks indicates improved spatial structure and geometric awareness. Overall, explicitly modeling spatial information provides an effective inductive bias for SSL, leading to more structured representations and better generalization. Code and models will be released.
匹配关键词: self-supervised
---

[ACADEMIC - ARXIV]
标题: G-Zero: Self-Play for Open-Ended Generation from Zero Data
作者: Chengsong Huang, Haolin Liu, Tong Zheng, Runpeng Dai, Langlin Huang, Jinyuan Li, Zongxia Li, Zhepei Wei, Yu Meng, Jiaxin Huang
链接: https://arxiv.org/abs/2605.09959v1
完整摘要: Self-evolving LLMs excel in verifiable domains but struggle in open-ended tasks, where reliance on proxy LLM judges introduces capability bottlenecks and reward hacking. To overcome this, we introduce G-Zero, a verifier-free, co-evolutionary framework for autonomous self-improvement. Our core innovation is Hint-$δ$, an intrinsic reward that quantifies the predictive shift between a Generator model's unassisted response and its response conditioned on a self-generated hint. Using this signal, a Proposer model is trained via GRPO to continuously target the Generator's blind spots by synthesizing challenging queries and informative hints. The Generator is concurrently optimized via DPO to internalize these hint-guided improvements. Theoretically, we prove a best-iterate suboptimality guarantee for an idealized standard-DPO version of G-Zero, provided that the Proposer induces sufficient exploration coverage and the data filteration keeps pseudo-label score noise low. By deriving supervision entirely from internal distributional dynamics, G-Zero bypasses the capability ceilings of external judges, providing a scalable, robust pathway for continuous LLM self-evolution across unverifiable domains.
匹配关键词: self-supervised
---

[ACADEMIC - ARXIV]
标题: LoopVLA: Learning Sufficiency in Recurrent Refinement for Vision-Language-Action Models
作者: Boyang Shen, Kaixiang Yang, Hao Wang, Qiuyu Yu, Qiang Xie, Qiang Li, Zhiwei Wang
链接: https://arxiv.org/abs/2605.09948v1
完整摘要: Current Vision-Language-Action (VLA) models typically treat the deepest representation of a vision-language backbone as universally optimal for action prediction. However, robotic manipulation is composed of many frequent closed-loop spatial adjustments, for which excessive abstraction may waste computation and weaken low-level geometric cues essential for precise control. Existing early-exit strategies attempt to reduce computation by stopping at predefined layers or applying heuristic rules such as action consistency, but they do not directly answer when a representation is actually sufficient for action. In this paper, we present LoopVLA, a recurrent VLA architecture that jointly learns representation refinement, action prediction, and sufficiency estimation. LoopVLA iteratively applies a shared Transformer block to refine multimodal tokens, and at each iteration produces both a candidate action and a sufficiency score that estimates whether further refinement is necessary. By sharing parameters across iterations, LoopVLA decouples refinement from absolute layer indices and grounds sufficiency estimation in the evolving representation itself. Since sufficiency has no direct supervision, we introduce a self-supervised distribution alignment objective, where intermediate confidence scores are trained to match the relative action quality across refinement steps, thereby linking sufficiency learning to policy optimization signals. Experiments on LIBERO, LIBERO-Plus, and VLA-Arena show that LoopVLA pushes the efficiency-performance frontier of VLA policies, reducing parameters by 45% and improving inference throughput by up to 1.7 times while matching or outperforming strong baselines in task success.
匹配关键词: self-supervised
---

[ACADEMIC - ARXIV]
标题: Relations Are Channels: Knowledge Graph Embedding via Kraus Decompositions
作者: Sayan Kumar Chaki
链接: https://arxiv.org/abs/2605.10317v1
完整摘要: Knowledge graph embedding (KGE) models typically represent each relation as an operator on entity embeddings. In this work, we identify three structural axioms that any principled relation operator must satisfy, linearity, trace preservation, and complete positivity, and show that they characterize a Kraus channel structure via the Kraus representation theorem. The completeness constraint defining this family is equivalent to these axioms, providing a principled foundation rather than an externally imposed condition. Under this formulation, most existing operator-based KGE models are recoverable as special cases with Kraus rank $κ= 1$ under specific embedding choices. We further generalize this characterization to arbitrary metric geometries by introducing \mbox{w-Kraus} channels, which satisfy completeness by construction within their respective spaces. Building on this theory, we propose \textsc{KrausKGE}, a principled KGE model that naturally handles $1$-to-$N$ and $N$-to-$N$ relations, supports $k$-hop reasoning without requiring explicit path encoders, and eliminates the need for norm constraints on entity embeddings. Additionally, our framework yields the first theoretically grounded per-relation complexity measure in the KGE literature, with a provable lower bound in terms of the empirical relation matrix rank. Empirical evaluation demonstrates that \textsc{KrausKGE} consistently outperforms strong baselines on $N$-to-$N$ relations, with performance gains that increase monotonically with relation fan-out, in alignment with theoretical predictions.
匹配关键词: contrastive learning
---

[ACADEMIC - ARXIV]
标题: Active Tabular Augmentation via Policy-Guided Diffusion Inpainting
作者: Zheyu Zhang, Shuo Yang, Bardh Prenkaj, Gjergji Kasneci
链接: https://arxiv.org/abs/2605.10315v1
完整摘要: Generative tabular augmentation is appealing in data-scarce domains, yet the prevailing focus on distributional fidelity does not reliably translate into better downstream models. We formalize a fidelity-utility gap: common generative objectives prioritize distributional plausibility, whereas augmentation succeeds only when injected samples reduce the current learner's held-out evaluation loss. This gap motivates learning not just how to generate, but what to generate and when to inject as training evolves. We propose TAP (Tabular Augmentation Policy), which couples diffusion inpainting with a lightweight, learner-conditioned policy to steer generation toward high-utility regions and controls safe injection via explicit gating and conservative windowed commitment. Under severe data scarcity, TAP consistently outperforms strong generative baselines on seven real-world datasets, improving classification accuracy by up to 15.6 percentage points and reducing regression RMSE by up to 32%.
匹配关键词: contrastive learning
---

[ACADEMIC - ARXIV]
标题: Signature Approach for Contextual Bandits with Nonlinear and Path-dependent Rewards
作者: Xin Guo, Grace He, Xinyu Li
链接: https://arxiv.org/abs/2605.10313v1
完整摘要: We study contextual bandits with nonlinear and path-dependent rewards through a novel signature-transform-based approach. Leveraging the universal nonlinearity property of signatures, we approximate continuous path-dependent reward functionals by linear functionals in the signature space. This representation enables the use of efficient linear contextual bandit methods while preserving expressive sequential structure. Building on this framework, we propose \texttt{DisSigUCB}, a signature-based disjoint upper confidence bound (UCB) algorithm. Under boundedness and non-degeneracy assumptions, we prove a high-probability data-dependent sublinear regret bound of order \(\tilde{\mathcal O}(\sqrt{(d+m)KT})\) where \(d\) is the context dimension and \(m\) is the signature feature dimension. Synthetic experiments and numerical applications on temperature sensor monitoring, sleep-stage classification, and hospital nurse staffing demonstrate that \texttt{DisSigUCB} consistently outperforms classical linear and kernelized contextual bandit baselines in nonlinear and path-dependent settings.
匹配关键词: contrastive learning
---

[ACADEMIC - ARXIV]
标题: Follow the Mean: Reference-Guided Flow Matching
作者: Pedro M. P. Curvo, Maksim Zhdanov, Floor Eijkelboom, Jan-Willem van de Meent
链接: https://arxiv.org/abs/2605.10302v1
完整摘要: Existing approaches to controllable generation typically rely on fine-tuning, auxiliary networks, or test-time search. We show that flow matching admits a different control interface: adaptation through examples. For deterministic interpolants, the velocity field is solely governed by a conditional endpoint mean; shifting this mean shifts the flow itself. This yields a simple principle for controllable generation: steer a pretrained model by changing the reference set it follows. We instantiate this idea in two forms. Reference-Mean Guidance is training-free: it computes a closed-form endpoint-mean correction from a reference bank and applies it to a frozen FLUX.2-klein (4B) model, enabling control of color, identity, style, and structure while keeping the prompt, seed, and weights fixed. Semi-Parametric Guidance amortizes the same idea through an explicit mean anchor and learned residual refiner, matching unconditional DiT-B/4 quality on AFHQv2 while allowing the reference set to be swapped at inference time. These results point to a broader direction: generative models that adapt through data, not parameter updates.
匹配关键词: contrastive learning
---

[ACADEMIC - ARXIV]
标题: Nearly-Optimal Algorithm for Adversarial Kernelized Bandits
作者: Shogo Iwazaki
链接: https://arxiv.org/abs/2605.10299v1
完整摘要: This paper studies kernelized bandits (also known as Gaussian process bandits) in an adversarial environment, where the reward functions in a known reproducing kernel Hilbert space (RKHS) may be adversarially chosen at each round. We show that the exponential-weight algorithm achieves $\tilde{O}(\sqrt{T γ_T})$ adversarial regret, where $T$ and $γ_T$ denote the number of total rounds and the maximum information gain, respectively. For squared exponential (SE) and $ν$-Matérn kernels, we also show algorithm-independent lower bounds that guarantee the optimality of our algorithm up to polylogarithmic factors. Furthermore, we present a computationally efficient variant of our algorithm using Nyström approximation while maintaining nearly optimal regret guarantees.
匹配关键词: contrastive learning
---

[ACADEMIC - ARXIV]
标题: Relations Are Channels: Knowledge Graph Embedding via Kraus Decompositions
作者: Sayan Kumar Chaki
链接: https://arxiv.org/abs/2605.10317v1
完整摘要: Knowledge graph embedding (KGE) models typically represent each relation as an operator on entity embeddings. In this work, we identify three structural axioms that any principled relation operator must satisfy, linearity, trace preservation, and complete positivity, and show that they characterize a Kraus channel structure via the Kraus representation theorem. The completeness constraint defining this family is equivalent to these axioms, providing a principled foundation rather than an externally imposed condition. Under this formulation, most existing operator-based KGE models are recoverable as special cases with Kraus rank $κ= 1$ under specific embedding choices. We further generalize this characterization to arbitrary metric geometries by introducing \mbox{w-Kraus} channels, which satisfy completeness by construction within their respective spaces. Building on this theory, we propose \textsc{KrausKGE}, a principled KGE model that naturally handles $1$-to-$N$ and $N$-to-$N$ relations, supports $k$-hop reasoning without requiring explicit path encoders, and eliminates the need for norm constraints on entity embeddings. Additionally, our framework yields the first theoretically grounded per-relation complexity measure in the KGE literature, with a provable lower bound in terms of the empirical relation matrix rank. Empirical evaluation demonstrates that \textsc{KrausKGE} consistently outperforms strong baselines on $N$-to-$N$ relations, with performance gains that increase monotonically with relation fan-out, in alignment with theoretical predictions.
匹配关键词: representation learning
---

[ACADEMIC - ARXIV]
标题: Active Tabular Augmentation via Policy-Guided Diffusion Inpainting
作者: Zheyu Zhang, Shuo Yang, Bardh Prenkaj, Gjergji Kasneci
链接: https://arxiv.org/abs/2605.10315v1
完整摘要: Generative tabular augmentation is appealing in data-scarce domains, yet the prevailing focus on distributional fidelity does not reliably translate into better downstream models. We formalize a fidelity-utility gap: common generative objectives prioritize distributional plausibility, whereas augmentation succeeds only when injected samples reduce the current learner's held-out evaluation loss. This gap motivates learning not just how to generate, but what to generate and when to inject as training evolves. We propose TAP (Tabular Augmentation Policy), which couples diffusion inpainting with a lightweight, learner-conditioned policy to steer generation toward high-utility regions and controls safe injection via explicit gating and conservative windowed commitment. Under severe data scarcity, TAP consistently outperforms strong generative baselines on seven real-world datasets, improving classification accuracy by up to 15.6 percentage points and reducing regression RMSE by up to 32%.
匹配关键词: representation learning
---

[ACADEMIC - ARXIV]
标题: Signature Approach for Contextual Bandits with Nonlinear and Path-dependent Rewards
作者: Xin Guo, Grace He, Xinyu Li
链接: https://arxiv.org/abs/2605.10313v1
完整摘要: We study contextual bandits with nonlinear and path-dependent rewards through a novel signature-transform-based approach. Leveraging the universal nonlinearity property of signatures, we approximate continuous path-dependent reward functionals by linear functionals in the signature space. This representation enables the use of efficient linear contextual bandit methods while preserving expressive sequential structure. Building on this framework, we propose \texttt{DisSigUCB}, a signature-based disjoint upper confidence bound (UCB) algorithm. Under boundedness and non-degeneracy assumptions, we prove a high-probability data-dependent sublinear regret bound of order \(\tilde{\mathcal O}(\sqrt{(d+m)KT})\) where \(d\) is the context dimension and \(m\) is the signature feature dimension. Synthetic experiments and numerical applications on temperature sensor monitoring, sleep-stage classification, and hospital nurse staffing demonstrate that \texttt{DisSigUCB} consistently outperforms classical linear and kernelized contextual bandit baselines in nonlinear and path-dependent settings.
匹配关键词: representation learning
---

[ACADEMIC - ARXIV]
标题: Follow the Mean: Reference-Guided Flow Matching
作者: Pedro M. P. Curvo, Maksim Zhdanov, Floor Eijkelboom, Jan-Willem van de Meent
链接: https://arxiv.org/abs/2605.10302v1
完整摘要: Existing approaches to controllable generation typically rely on fine-tuning, auxiliary networks, or test-time search. We show that flow matching admits a different control interface: adaptation through examples. For deterministic interpolants, the velocity field is solely governed by a conditional endpoint mean; shifting this mean shifts the flow itself. This yields a simple principle for controllable generation: steer a pretrained model by changing the reference set it follows. We instantiate this idea in two forms. Reference-Mean Guidance is training-free: it computes a closed-form endpoint-mean correction from a reference bank and applies it to a frozen FLUX.2-klein (4B) model, enabling control of color, identity, style, and structure while keeping the prompt, seed, and weights fixed. Semi-Parametric Guidance amortizes the same idea through an explicit mean anchor and learned residual refiner, matching unconditional DiT-B/4 quality on AFHQv2 while allowing the reference set to be swapped at inference time. These results point to a broader direction: generative models that adapt through data, not parameter updates.
匹配关键词: representation learning
---

[ACADEMIC - ARXIV]
标题: Nearly-Optimal Algorithm for Adversarial Kernelized Bandits
作者: Shogo Iwazaki
链接: https://arxiv.org/abs/2605.10299v1
完整摘要: This paper studies kernelized bandits (also known as Gaussian process bandits) in an adversarial environment, where the reward functions in a known reproducing kernel Hilbert space (RKHS) may be adversarially chosen at each round. We show that the exponential-weight algorithm achieves $\tilde{O}(\sqrt{T γ_T})$ adversarial regret, where $T$ and $γ_T$ denote the number of total rounds and the maximum information gain, respectively. For squared exponential (SE) and $ν$-Matérn kernels, we also show algorithm-independent lower bounds that guarantee the optimality of our algorithm up to polylogarithmic factors. Furthermore, we present a computationally efficient variant of our algorithm using Nyström approximation while maintaining nearly optimal regret guarantees.
匹配关键词: representation learning
---

[ACADEMIC - ARXIV]
标题: Extending Confidence-Based Text2Cypher with Grammar and Schema Aware Filtering
作者: Makbule Gulcin Ozsoy
链接: https://arxiv.org/abs/2605.10318v1
完整摘要: Large language models (LLMs) allow users to query databases using natural language by translating questions into executable queries. Despite strong progress on tasks such as Text2SQL, Text2SPARQL, and Text2Cypher, most existing methods focus on better prompting, fine-tuning, or iterative refinement. However, they often do not explicitly enforce structural constraints, such as syntactic validity and schema consistency. This can reduce reliability, since generated queries must satisfy both syntax rules and database schema constraints to be executable. In this work, we study how structured constraints can be used in test-time inference for Text2Cypher. We focus on post-generation validation to improve query correctness. We extend a confidence-based inference framework with a sequential filtering process that combines confidence scoring, grammar validation, and schema constraints before final aggregation. This lets us analyze how different constraint types affect generated queries. Our experiments with two instruction-tuned models show that grammar-based filtering improves syntactic validity. Schema-aware filtering further improves execution quality by enforcing consistency with the database structure. However, stronger filtering also increases the number of empty predictions and reduces execution coverage. Overall, we show that adding simple structural checks at test time improves the reliability of Text2Cypher generation, and we provide a clearer view of how syntax and schema constraints contribute differently.
匹配关键词: masked language model
---

[ACADEMIC - ARXIV]
标题: Relations Are Channels: Knowledge Graph Embedding via Kraus Decompositions
作者: Sayan Kumar Chaki
链接: https://arxiv.org/abs/2605.10317v1
完整摘要: Knowledge graph embedding (KGE) models typically represent each relation as an operator on entity embeddings. In this work, we identify three structural axioms that any principled relation operator must satisfy, linearity, trace preservation, and complete positivity, and show that they characterize a Kraus channel structure via the Kraus representation theorem. The completeness constraint defining this family is equivalent to these axioms, providing a principled foundation rather than an externally imposed condition. Under this formulation, most existing operator-based KGE models are recoverable as special cases with Kraus rank $κ= 1$ under specific embedding choices. We further generalize this characterization to arbitrary metric geometries by introducing \mbox{w-Kraus} channels, which satisfy completeness by construction within their respective spaces. Building on this theory, we propose \textsc{KrausKGE}, a principled KGE model that naturally handles $1$-to-$N$ and $N$-to-$N$ relations, supports $k$-hop reasoning without requiring explicit path encoders, and eliminates the need for norm constraints on entity embeddings. Additionally, our framework yields the first theoretically grounded per-relation complexity measure in the KGE literature, with a provable lower bound in terms of the empirical relation matrix rank. Empirical evaluation demonstrates that \textsc{KrausKGE} consistently outperforms strong baselines on $N$-to-$N$ relations, with performance gains that increase monotonically with relation fan-out, in alignment with theoretical predictions.
匹配关键词: masked language model
---

[ACADEMIC - ARXIV]
标题: Active Tabular Augmentation via Policy-Guided Diffusion Inpainting
作者: Zheyu Zhang, Shuo Yang, Bardh Prenkaj, Gjergji Kasneci
链接: https://arxiv.org/abs/2605.10315v1
完整摘要: Generative tabular augmentation is appealing in data-scarce domains, yet the prevailing focus on distributional fidelity does not reliably translate into better downstream models. We formalize a fidelity-utility gap: common generative objectives prioritize distributional plausibility, whereas augmentation succeeds only when injected samples reduce the current learner's held-out evaluation loss. This gap motivates learning not just how to generate, but what to generate and when to inject as training evolves. We propose TAP (Tabular Augmentation Policy), which couples diffusion inpainting with a lightweight, learner-conditioned policy to steer generation toward high-utility regions and controls safe injection via explicit gating and conservative windowed commitment. Under severe data scarcity, TAP consistently outperforms strong generative baselines on seven real-world datasets, improving classification accuracy by up to 15.6 percentage points and reducing regression RMSE by up to 32%.
匹配关键词: masked language model
---

[ACADEMIC - ARXIV]
标题: PaMoSplat: Part-Aware Motion-Guided Gaussian Splatting for Dynamic Scene Reconstruction
作者: Yinan Deng, Jianyu Dou, Jiahui Wang, Jingyu Zhao, Yi Yang, Yufeng Yue
链接: https://arxiv.org/abs/2605.10307v1
完整摘要: Dynamic scene reconstruction represents a fundamental yet demanding challenge in computer vision and robotics. While recent progress in 3DGS-based methods has advanced dynamic scene modeling, obtaining high-fidelity rendering and accurate tracking in scenarios with substantial, intricate motions remains significantly challenging. To address these challenges, we propose PaMoSplat, a novel dynamic Gaussian splatting framework incorporating part awareness and motion priors. Our approach is grounded in two key observations: 1) Parts serve as primitives for scene deformation, and 2) Motion cues from optical flow can effectively guide part motion. Specifically, PaMoSplat initializes by lifting multi-view segmentation masks into 3D space via graph clustering, establishing coherent Gaussian parts. For subsequent timestamps, we leverage a differential evolutionary algorithm to estimate the rigid motion of these parts using multi-view optical flow cues, providing a robust warm-start for further optimization. Additionally, PaMoSplat introduces an adaptive iteration count mechanism, internal learnable rigidity, and flow-supervised rendering loss to accelerate and optimize the training process. Comprehensive evaluations across diverse scenes, including real-world environments, demonstrate that PaMoSplat delivers superior rendering quality, improved tracking precision, and faster convergence compared to existing methods. Furthermore, it enables multiple part-level downstream applications, such as 4D scene editing.
匹配关键词: masked language model
---

[ACADEMIC - ARXIV]
标题: Follow the Mean: Reference-Guided Flow Matching
作者: Pedro M. P. Curvo, Maksim Zhdanov, Floor Eijkelboom, Jan-Willem van de Meent
链接: https://arxiv.org/abs/2605.10302v1
完整摘要: Existing approaches to controllable generation typically rely on fine-tuning, auxiliary networks, or test-time search. We show that flow matching admits a different control interface: adaptation through examples. For deterministic interpolants, the velocity field is solely governed by a conditional endpoint mean; shifting this mean shifts the flow itself. This yields a simple principle for controllable generation: steer a pretrained model by changing the reference set it follows. We instantiate this idea in two forms. Reference-Mean Guidance is training-free: it computes a closed-form endpoint-mean correction from a reference bank and applies it to a frozen FLUX.2-klein (4B) model, enabling control of color, identity, style, and structure while keeping the prompt, seed, and weights fixed. Semi-Parametric Guidance amortizes the same idea through an explicit mean anchor and learned residual refiner, matching unconditional DiT-B/4 quality on AFHQv2 while allowing the reference set to be swapped at inference time. These results point to a broader direction: generative models that adapt through data, not parameter updates.
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
标题: MARGIN: Margin-Aware Regularized Geometry for Imbalanced Vulnerability Detection
作者: Yuteng Zhang, Huifang Ma, Jiahui Wei, Qingqing Li, Yafei Yang
链接: https://arxiv.org/abs/2605.10240v1
完整摘要: Software vulnerability detection is critical for ensuring software security and reliability. Despite recent advances in deep learning, real-world vulnerability datasets suffer from two severe challenges: frequency imbalance and difficulty imbalance. We reinterpret these challenges from an embedding geometry perspective, observing that such imbalances induce geometric distortions in hyperspherical representation space. To address this issue, we propose MARGIN, a metric-based framework that learns discriminative vulnerability representations through adaptive margin metric learning and hyperspherical prototype modeling. MARGIN dynamically adjusts geometric regularization according to the distribution structure estimated by the von Mises-Fisher concentration, aligning the probability mass of embedding distributions with their corresponding Voronoi cells, thereby reducing geometric distortion and yielding more stable decision boundaries. Extensive experiments on public vulnerability datasets show that MARGIN consistently outperforms strong baselines, achieving notable improvements in classification and detection, especially on challenging, imbalanced datasets. Further analysis demonstrates that MARGIN produces more structured embedding geometries, improving robustness, interpretability, and generalization.
匹配关键词: MAE
---

[ACADEMIC - ARXIV]
标题: SciVQR: A Multidisciplinary Multimodal Benchmark for Advanced Scientific Reasoning Evaluation
作者: Longteng Guo, Xuanxu Lin, Dongze Hao, Tongtian Yue, Pengkang Huo, Jiatong Ma, Yuchen Liu, Jing Liu
链接: https://arxiv.org/abs/2605.10187v1
完整摘要: Scientific reasoning is a key aspect of human intelligence, requiring the integration of multimodal inputs, domain expertise, and multi-step inference across various subjects. Existing benchmarks for multimodal large language models (MLLMs) often fail to capture the complexity and traceability of reasoning processes necessary for rigorous evaluation. To fill this gap, we introduce SciVQR, a multimodal benchmark covering 54 subfields in mathematics, physics, chemistry, geography, astronomy, and biology. SciVQR includes domain-specific visuals, such as equations, charts, and diagrams, and challenges models to combine visual comprehension with reasoning. The tasks range from basic factual recall to complex, multi-step inferences, with 46% including expert-authored solutions. SciVQR not only evaluates final answers but also examines the reasoning process, providing insights into how models reach their conclusions. Our evaluation of leading MLLMs, including both proprietary and open-source models, reveals significant limitations in handling complex multimodal reasoning tasks, underscoring the need for improved multi-step reasoning and better integration of interdisciplinary knowledge in advancing MLLMs toward true scientific intelligence. The dataset and evaluation code are publicly available at https://github.com/CASIA-IVA-Lab/SciVQR.
匹配关键词: MAE
---

[ACADEMIC - ARXIV]
标题: V-ABS: Action-Observer Driven Beam Search for Dynamic Visual Reasoning
作者: Zhiwei Ning, Xuanang Gao, Jiaxi Cao, Gengming Zhang, Shengnan Ma, Wenwen Tong, Hanming Deng, Jie Yang, Wei Liu
链接: https://arxiv.org/abs/2605.10172v1
完整摘要: Multimodal large language models (MLLMs) have achieved remarkable success in general perception, yet complex multi-step visual reasoning remains a persistent challenge. Although recent agentic approaches incorporate tool use, they often neglect critical execution feedback. Consequently, they suffer from the imagination-action-observer (IAO) bias, a misalignment between prior imagination and observer feedback that undermines reasoning stability and optimality. To bridge this gap, we introduce V-ABS, an action-observer driven beam search framework that enables deliberate reasoning through thinker-actor-observer iterations. We also propose an entropy-based adaptive weighting algorithm to mitigate the IAO bias by dynamically balancing the confidence scores between the policy priors and the observational feedback. Moreover, we construct a large-scale supervised fine-tuning (SFT) dataset comprising over 80k samples to guide the model to assign higher prior confidence to correct action paths. Extensive experiments across eight diverse benchmarks show that V-ABS achieves state-of-the-art performance, delivering an average improvement of 19.7% on the Qwen3-VL-8B baseline and consistent gains across both open-source and proprietary models.
匹配关键词: MAE
---

[ACADEMIC - ARXIV]
标题: Benchmarking Safety Risks of Knowledge-Intensive Reasoning under Malicious Knowledge Editing
作者: Qinghua Mao, Xi Lin, Jinze Gu, Jun Wu, Siyuan Li, Yuliang Chen
链接: https://arxiv.org/abs/2605.10146v1
完整摘要: Large language models (LLMs) increasingly rely on knowledge editing to support knowledge-intensive reasoning, but this flexibility also introduces critical safety risks: adversaries can inject malicious or misleading knowledge that corrupts downstream reasoning and leads to harmful outcomes. Existing knowledge editing benchmarks primarily focus on editing efficacy and lack a unified framework for systematically evaluating the safety implications of edited knowledge on reasoning behavior. To address this gap, we present EditRisk-Bench, a benchmark for systematically evaluating safety risks of knowledge-intensive reasoning under malicious knowledge editing. Unlike prior benchmarks that mainly emphasize edit success, generalization, and locality, EditRisk-Bench focuses on how injected knowledge affects downstream reasoning behavior and reliability. It integrates diverse malicious scenarios, including misinformation, bias, and safety violations, together with multi-level knowledge-intensive reasoning tasks and representative editing strategies within a unified evaluation framework measuring attack effectiveness, reasoning correctness, and side effects. Extensive experiments on both open-source and closed-source LLMs show that malicious knowledge editing can reliably induce incorrect or unsafe reasoning while largely preserving general capabilities, making such risks difficult to detect. We further identify several key factors influencing these risks, including edit scale, knowledge characteristics, and reasoning complexity. EditRisk-Bench provides an extensible testbed for understanding and mitigating safety risks in knowledge editing for LLMs.
匹配关键词: MAE
---

[ACADEMIC - ARXIV]
标题: Fashion130K: An E-commerce Fashion Dataset for Outfit Generation with Unified Multi-modal Condition
作者: Yu He, Ting Zhu, Yichun Liu, Lichen Ma, Xinyuan Shan, Jingling Fu, Yu Shi, Junshi Huang, Yan Li
链接: https://arxiv.org/abs/2605.10127v1
完整摘要: Recent research work on fashion outfit generation focuses on promoting visual consistency of garments by leveraging key information from reference image and text prompt. However, the potential of outfit generation remains underexplored, requiring comprehensive e-commercial dataset and elaborative utilization of multi-modal condition. In this paper, we propose a brand-new e-commerce dataset, named Fashion130k, with various occasions, models, and garment types. For the consistent generation of garment, we design a framework with Unified Multi-modal Condition (UMC) to align and integrate the text and visual prompts into generation model. Specifically, we explore an embedding refiner to extract the unified embeddings of multi-modal prompts, within which a Fusion Transformer is proposed to align the multi-modal embeddings by adjusting the modality gap between text and image. Based on unified embeddings, the attention in generation model is redesigned to emphasis the correlations between prompts and noise image, inducing that the noise image can select the pivotal tokens of prompts for consistent outfit generation. Our dataset and proposed framework offer a general and nuanced exploration of multi-modal prompts for generation models. Extensive experiments on real-world applications and benchmark demonstrate the effectiveness of UMC in visual consistency, achieving promising result than that of SoTA methods.
匹配关键词: MAE
---

[ACADEMIC - ARXIV]
标题: Extending Confidence-Based Text2Cypher with Grammar and Schema Aware Filtering
作者: Makbule Gulcin Ozsoy
链接: https://arxiv.org/abs/2605.10318v1
完整摘要: Large language models (LLMs) allow users to query databases using natural language by translating questions into executable queries. Despite strong progress on tasks such as Text2SQL, Text2SPARQL, and Text2Cypher, most existing methods focus on better prompting, fine-tuning, or iterative refinement. However, they often do not explicitly enforce structural constraints, such as syntactic validity and schema consistency. This can reduce reliability, since generated queries must satisfy both syntax rules and database schema constraints to be executable. In this work, we study how structured constraints can be used in test-time inference for Text2Cypher. We focus on post-generation validation to improve query correctness. We extend a confidence-based inference framework with a sequential filtering process that combines confidence scoring, grammar validation, and schema constraints before final aggregation. This lets us analyze how different constraint types affect generated queries. Our experiments with two instruction-tuned models show that grammar-based filtering improves syntactic validity. Schema-aware filtering further improves execution quality by enforcing consistency with the database structure. However, stronger filtering also increases the number of empty predictions and reduces execution coverage. Overall, we show that adding simple structural checks at test time improves the reliability of Text2Cypher generation, and we provide a clearer view of how syntax and schema constraints contribute differently.
匹配关键词: generative model
---

[ACADEMIC - ARXIV]
标题: Relations Are Channels: Knowledge Graph Embedding via Kraus Decompositions
作者: Sayan Kumar Chaki
链接: https://arxiv.org/abs/2605.10317v1
完整摘要: Knowledge graph embedding (KGE) models typically represent each relation as an operator on entity embeddings. In this work, we identify three structural axioms that any principled relation operator must satisfy, linearity, trace preservation, and complete positivity, and show that they characterize a Kraus channel structure via the Kraus representation theorem. The completeness constraint defining this family is equivalent to these axioms, providing a principled foundation rather than an externally imposed condition. Under this formulation, most existing operator-based KGE models are recoverable as special cases with Kraus rank $κ= 1$ under specific embedding choices. We further generalize this characterization to arbitrary metric geometries by introducing \mbox{w-Kraus} channels, which satisfy completeness by construction within their respective spaces. Building on this theory, we propose \textsc{KrausKGE}, a principled KGE model that naturally handles $1$-to-$N$ and $N$-to-$N$ relations, supports $k$-hop reasoning without requiring explicit path encoders, and eliminates the need for norm constraints on entity embeddings. Additionally, our framework yields the first theoretically grounded per-relation complexity measure in the KGE literature, with a provable lower bound in terms of the empirical relation matrix rank. Empirical evaluation demonstrates that \textsc{KrausKGE} consistently outperforms strong baselines on $N$-to-$N$ relations, with performance gains that increase monotonically with relation fan-out, in alignment with theoretical predictions.
匹配关键词: generative model
---

[ACADEMIC - ARXIV]
标题: Active Tabular Augmentation via Policy-Guided Diffusion Inpainting
作者: Zheyu Zhang, Shuo Yang, Bardh Prenkaj, Gjergji Kasneci
链接: https://arxiv.org/abs/2605.10315v1
完整摘要: Generative tabular augmentation is appealing in data-scarce domains, yet the prevailing focus on distributional fidelity does not reliably translate into better downstream models. We formalize a fidelity-utility gap: common generative objectives prioritize distributional plausibility, whereas augmentation succeeds only when injected samples reduce the current learner's held-out evaluation loss. This gap motivates learning not just how to generate, but what to generate and when to inject as training evolves. We propose TAP (Tabular Augmentation Policy), which couples diffusion inpainting with a lightweight, learner-conditioned policy to steer generation toward high-utility regions and controls safe injection via explicit gating and conservative windowed commitment. Under severe data scarcity, TAP consistently outperforms strong generative baselines on seven real-world datasets, improving classification accuracy by up to 15.6 percentage points and reducing regression RMSE by up to 32%.
匹配关键词: generative model
---

[ACADEMIC - ARXIV]
标题: PaMoSplat: Part-Aware Motion-Guided Gaussian Splatting for Dynamic Scene Reconstruction
作者: Yinan Deng, Jianyu Dou, Jiahui Wang, Jingyu Zhao, Yi Yang, Yufeng Yue
链接: https://arxiv.org/abs/2605.10307v1
完整摘要: Dynamic scene reconstruction represents a fundamental yet demanding challenge in computer vision and robotics. While recent progress in 3DGS-based methods has advanced dynamic scene modeling, obtaining high-fidelity rendering and accurate tracking in scenarios with substantial, intricate motions remains significantly challenging. To address these challenges, we propose PaMoSplat, a novel dynamic Gaussian splatting framework incorporating part awareness and motion priors. Our approach is grounded in two key observations: 1) Parts serve as primitives for scene deformation, and 2) Motion cues from optical flow can effectively guide part motion. Specifically, PaMoSplat initializes by lifting multi-view segmentation masks into 3D space via graph clustering, establishing coherent Gaussian parts. For subsequent timestamps, we leverage a differential evolutionary algorithm to estimate the rigid motion of these parts using multi-view optical flow cues, providing a robust warm-start for further optimization. Additionally, PaMoSplat introduces an adaptive iteration count mechanism, internal learnable rigidity, and flow-supervised rendering loss to accelerate and optimize the training process. Comprehensive evaluations across diverse scenes, including real-world environments, demonstrate that PaMoSplat delivers superior rendering quality, improved tracking precision, and faster convergence compared to existing methods. Furthermore, it enables multiple part-level downstream applications, such as 4D scene editing.
匹配关键词: generative model
---

[ACADEMIC - ARXIV]
标题: Follow the Mean: Reference-Guided Flow Matching
作者: Pedro M. P. Curvo, Maksim Zhdanov, Floor Eijkelboom, Jan-Willem van de Meent
链接: https://arxiv.org/abs/2605.10302v1
完整摘要: Existing approaches to controllable generation typically rely on fine-tuning, auxiliary networks, or test-time search. We show that flow matching admits a different control interface: adaptation through examples. For deterministic interpolants, the velocity field is solely governed by a conditional endpoint mean; shifting this mean shifts the flow itself. This yields a simple principle for controllable generation: steer a pretrained model by changing the reference set it follows. We instantiate this idea in two forms. Reference-Mean Guidance is training-free: it computes a closed-form endpoint-mean correction from a reference bank and applies it to a frozen FLUX.2-klein (4B) model, enabling control of color, identity, style, and structure while keeping the prompt, seed, and weights fixed. Semi-Parametric Guidance amortizes the same idea through an explicit mean anchor and learned residual refiner, matching unconditional DiT-B/4 quality on AFHQv2 while allowing the reference set to be swapped at inference time. These results point to a broader direction: generative models that adapt through data, not parameter updates.
匹配关键词: generative model
---

[ACADEMIC - ARXIV]
标题: Extending Confidence-Based Text2Cypher with Grammar and Schema Aware Filtering
作者: Makbule Gulcin Ozsoy
链接: https://arxiv.org/abs/2605.10318v1
完整摘要: Large language models (LLMs) allow users to query databases using natural language by translating questions into executable queries. Despite strong progress on tasks such as Text2SQL, Text2SPARQL, and Text2Cypher, most existing methods focus on better prompting, fine-tuning, or iterative refinement. However, they often do not explicitly enforce structural constraints, such as syntactic validity and schema consistency. This can reduce reliability, since generated queries must satisfy both syntax rules and database schema constraints to be executable. In this work, we study how structured constraints can be used in test-time inference for Text2Cypher. We focus on post-generation validation to improve query correctness. We extend a confidence-based inference framework with a sequential filtering process that combines confidence scoring, grammar validation, and schema constraints before final aggregation. This lets us analyze how different constraint types affect generated queries. Our experiments with two instruction-tuned models show that grammar-based filtering improves syntactic validity. Schema-aware filtering further improves execution quality by enforcing consistency with the database structure. However, stronger filtering also increases the number of empty predictions and reduces execution coverage. Overall, we show that adding simple structural checks at test time improves the reliability of Text2Cypher generation, and we provide a clearer view of how syntax and schema constraints contribute differently.
匹配关键词: diffusion model
---

[ACADEMIC - ARXIV]
标题: Relations Are Channels: Knowledge Graph Embedding via Kraus Decompositions
作者: Sayan Kumar Chaki
链接: https://arxiv.org/abs/2605.10317v1
完整摘要: Knowledge graph embedding (KGE) models typically represent each relation as an operator on entity embeddings. In this work, we identify three structural axioms that any principled relation operator must satisfy, linearity, trace preservation, and complete positivity, and show that they characterize a Kraus channel structure via the Kraus representation theorem. The completeness constraint defining this family is equivalent to these axioms, providing a principled foundation rather than an externally imposed condition. Under this formulation, most existing operator-based KGE models are recoverable as special cases with Kraus rank $κ= 1$ under specific embedding choices. We further generalize this characterization to arbitrary metric geometries by introducing \mbox{w-Kraus} channels, which satisfy completeness by construction within their respective spaces. Building on this theory, we propose \textsc{KrausKGE}, a principled KGE model that naturally handles $1$-to-$N$ and $N$-to-$N$ relations, supports $k$-hop reasoning without requiring explicit path encoders, and eliminates the need for norm constraints on entity embeddings. Additionally, our framework yields the first theoretically grounded per-relation complexity measure in the KGE literature, with a provable lower bound in terms of the empirical relation matrix rank. Empirical evaluation demonstrates that \textsc{KrausKGE} consistently outperforms strong baselines on $N$-to-$N$ relations, with performance gains that increase monotonically with relation fan-out, in alignment with theoretical predictions.
匹配关键词: diffusion model
---

[ACADEMIC - ARXIV]
标题: Active Tabular Augmentation via Policy-Guided Diffusion Inpainting
作者: Zheyu Zhang, Shuo Yang, Bardh Prenkaj, Gjergji Kasneci
链接: https://arxiv.org/abs/2605.10315v1
完整摘要: Generative tabular augmentation is appealing in data-scarce domains, yet the prevailing focus on distributional fidelity does not reliably translate into better downstream models. We formalize a fidelity-utility gap: common generative objectives prioritize distributional plausibility, whereas augmentation succeeds only when injected samples reduce the current learner's held-out evaluation loss. This gap motivates learning not just how to generate, but what to generate and when to inject as training evolves. We propose TAP (Tabular Augmentation Policy), which couples diffusion inpainting with a lightweight, learner-conditioned policy to steer generation toward high-utility regions and controls safe injection via explicit gating and conservative windowed commitment. Under severe data scarcity, TAP consistently outperforms strong generative baselines on seven real-world datasets, improving classification accuracy by up to 15.6 percentage points and reducing regression RMSE by up to 32%.
匹配关键词: diffusion model
---

[ACADEMIC - ARXIV]
标题: PaMoSplat: Part-Aware Motion-Guided Gaussian Splatting for Dynamic Scene Reconstruction
作者: Yinan Deng, Jianyu Dou, Jiahui Wang, Jingyu Zhao, Yi Yang, Yufeng Yue
链接: https://arxiv.org/abs/2605.10307v1
完整摘要: Dynamic scene reconstruction represents a fundamental yet demanding challenge in computer vision and robotics. While recent progress in 3DGS-based methods has advanced dynamic scene modeling, obtaining high-fidelity rendering and accurate tracking in scenarios with substantial, intricate motions remains significantly challenging. To address these challenges, we propose PaMoSplat, a novel dynamic Gaussian splatting framework incorporating part awareness and motion priors. Our approach is grounded in two key observations: 1) Parts serve as primitives for scene deformation, and 2) Motion cues from optical flow can effectively guide part motion. Specifically, PaMoSplat initializes by lifting multi-view segmentation masks into 3D space via graph clustering, establishing coherent Gaussian parts. For subsequent timestamps, we leverage a differential evolutionary algorithm to estimate the rigid motion of these parts using multi-view optical flow cues, providing a robust warm-start for further optimization. Additionally, PaMoSplat introduces an adaptive iteration count mechanism, internal learnable rigidity, and flow-supervised rendering loss to accelerate and optimize the training process. Comprehensive evaluations across diverse scenes, including real-world environments, demonstrate that PaMoSplat delivers superior rendering quality, improved tracking precision, and faster convergence compared to existing methods. Furthermore, it enables multiple part-level downstream applications, such as 4D scene editing.
匹配关键词: diffusion model
---

[ACADEMIC - ARXIV]
标题: Follow the Mean: Reference-Guided Flow Matching
作者: Pedro M. P. Curvo, Maksim Zhdanov, Floor Eijkelboom, Jan-Willem van de Meent
链接: https://arxiv.org/abs/2605.10302v1
完整摘要: Existing approaches to controllable generation typically rely on fine-tuning, auxiliary networks, or test-time search. We show that flow matching admits a different control interface: adaptation through examples. For deterministic interpolants, the velocity field is solely governed by a conditional endpoint mean; shifting this mean shifts the flow itself. This yields a simple principle for controllable generation: steer a pretrained model by changing the reference set it follows. We instantiate this idea in two forms. Reference-Mean Guidance is training-free: it computes a closed-form endpoint-mean correction from a reference bank and applies it to a frozen FLUX.2-klein (4B) model, enabling control of color, identity, style, and structure while keeping the prompt, seed, and weights fixed. Semi-Parametric Guidance amortizes the same idea through an explicit mean anchor and learned residual refiner, matching unconditional DiT-B/4 quality on AFHQv2 while allowing the reference set to be swapped at inference time. These results point to a broader direction: generative models that adapt through data, not parameter updates.
匹配关键词: diffusion model
---

[ACADEMIC - ARXIV]
标题: Extended Wasserstein-GAN Approach to Causal Distribution Learning: Density-Free Estimation and Minimax Optimality
作者: Shu Tamano, Masaaki Imaizumi
链接: https://arxiv.org/abs/2605.10206v1
完整摘要: Distributional causal inference requires estimating not only average treatment effects but also interventional outcome distributions, including quantiles, tail risks, and policy-dependent uncertainty. As a method for distributional causal inference, generative adversarial network (GAN)-based counterfactual methods are flexible tools for this task. However, these methods have several limitations. First, the objectives of certain techniques do not coincide with the statistical risk of the identifiable causal target, and therefore provide limited theoretical guarantees regarding estimable counterfactual distributions or optimality. Second, they tend to rely on unstable density-based methods, such as density ratio estimation. In this paper, we propose GANICE (GAN for Interventional Conditional Estimation) with several advantages: it (i) clarifies the conditional interventional distribution for each treatment--covariate state as the causal estimation target; (ii) estimates the conditional distribution such that its averaged Wasserstein risk is minimized; (iii) establishes minimax optimality. GANICE achieves these advantages through the introduction of the extended Wasserstein distance, the incorporation of a cellwise critic in its dual, and an optimality proof based on Besov space theory. Our experiments demonstrate that GANICE consistently outperforms existing methods.
匹配关键词: GAN
---

[ACADEMIC - ARXIV]
标题: MFVLR: Multi-domain Fine-grained Vision-Language Reconstruction for Generalizable Diffusion Face Forgery Detection and Localization
作者: Yaning Zhang, Tianyi Wang, Zan Gao, Yibo Zhao, Chunjie Ma, Meng Wang
链接: https://arxiv.org/abs/2605.10071v1
完整摘要: The swift advancement in photo-realistic face generation technology has sparked considerable concerns across society and academia, emphasizing the requirement of generalizable face forgery detection and localization methods. Prior works tend to capture face forgery patterns across multiple domains using image modality, other modalities like fine-grained texts are not comprehensively investigated, which restricts the generalization capability of models. Besides, they usually analyze facial images created by GAN, but struggle to identify and localize those synthesized by diffusion. To solve the problems, in this paper, we devise a novel multi-domain fine-grained vision-language reconstruction (MFVLR) model, which explores comprehensive and diverse visual forgery traces via language-guided face forgery representation learning, to achieve generalizable diffusion-synthesized face forgery detection and localization (DFFDL). Specifically, we devise a fine-grained language transformer that studies general fine-grained language embeddings using language reconstruction. We propose a multi-domain vision encoder to capture general and complementary visual forgery patterns across the image and residual domains. A vision decoder is designed to reconstruct image appearance and achieve forgery localization. Besides, we propose an innovative plug-and-play vision injection module to enhance the interaction between the vision and language embeddings. Extensive experiments and visualizations demonstrate that our network outperforms the state of the art on different settings like cross-generator, cross-forgery, and cross-dataset evaluations.
匹配关键词: GAN
---

[ACADEMIC - ARXIV]
标题: Novel GPU Boruta algorithms for feature selection from high-dimensional data
作者: Xurui Li, Zhiguo Gan, Jiaming Zhang, Zheng Liu, Diannan Lu
链接: https://arxiv.org/abs/2605.09950v1
完整摘要: Most feature selection algorithms, especially wrapper methods, run inefficiently on CPU based platforms because of their high computational complexity. This inefficiency makes them unsuitable for processing large scale datasets. To address this challenge, the present study proposed two GPU accelerated versions of the Boruta feature selection procedure, in which Boruta-Permut relies on permutation based feature importance and Boruta-TreeImp employs importance based on impurity reduction. To evaluate these methods we conducted experiments on both a self constructed dataset and several publicly available datasets. The experimental results show that the proposed GPU accelerated algorithms greatly improve computational efficiency while preserving feature selection accuracy comparable to the original Boruta algorithm. In our analysis we also observe that the impurity reduction based version can overestimate the importance of some features. Overall these findings suggest that performing Boruta feature selection on GPUs offers an effective and cost efficient solution for large scale data analysis, which is a good deal.
匹配关键词: GAN
---

[ACADEMIC - ARXIV]
标题: PoDAR: Power-Disentangled Audio Representation for Generative Modeling
作者: Alejandro Luebs, Mithilesh Vaidya, Ishaan Kumar, Sumukh Badam, Stephen W. Bailey, Matthew Bendel, Jose Sotelo, Xingzhe He
链接: https://arxiv.org/abs/2605.10084v1
完整摘要: The performance of audio latent diffusion models is primarily governed by generator expressivity and the modelability of the underlying latent space. While recent research has focused primarily on the former, as well as improving the reconstruction fidelity of audio codecs, we demonstrate that latent modelability can be significantly improved through explicit factor disentanglement. We present PoDAR (Power-Disentangled Audio Representation), a framework that utilizes a randomized power augmentation and latent consistency objective to decouple signal power from invariant semantic content. This factorization makes the latent space easier to model, which both accelerates the convergence of downstream generative models and improves final overall performance. When applied to a Stable Audio 1.0 VAE with an F5-TTS generator, PoDAR achieves about a $2\times$ acceleration in convergence to match baseline performance, while increasing final speaker similarity by 0.055 and UTMOS by 0.22 on the LibriSpeech-PC dataset. Furthermore, isolating power into dedicated channels enables the application of CFG exclusively to power-invariant content, effectively extending the stable guidance regime to higher scales.
匹配关键词: VAE
---

[ACADEMIC - ARXIV]
标题: Stable Long-Horizon PDE Forecasting via Latent Structured Spectral Propagators
作者: Xiaoxiao Lu, Ye Yuan, Jiahao Shi
链接: https://arxiv.org/abs/2605.10154v1
完整摘要: Long-horizon forecasting of time-dependent partial differential equations (PDEs) is critical for characterizing the sustained evolution of physical systems. While neural operators have emerged as efficient surrogates, they typically learn implicit finite-time transitions from discrete observations. When deployed autoregressively, such propagators often suffer from rapid error accumulation and dynamic drift. To address this, we propose a neural forecasting framework that reformulates PDE rollout as learning a Structured Spectral Propagator (SSP) in a propagation-oriented latent space. Following an analysis-propagation-synthesis design, our framework: (i) maps physical states into a shared, time-consistent spatial representation; (ii) projects this space into a compact propagation state to isolate recurrent dynamics from fine-grained spatial details, thereby decoupling reconstruction fidelity from rollout regularity; and (iii) evolves retained spectral modes using a frequency-conditioned linear backbone complemented by a nonlinear spectral closure to account for truncated interactions. This explicit structuring endows the propagator with a strong inductive bias for coherent modal evolution. Extensive experiments demonstrate that SSP significantly outperforms state-of-the-art baselines, reducing relative $L_2$ errors by up to 48.9% and exhibiting improved stability in temporal extrapolation beyond the supervised horizon.
匹配关键词: autoregressive
---

[ACADEMIC - ARXIV]
标题: ExtraVAR: Stage-Aware RoPE Remapping for Resolution Extrapolation in Visual Autoregressive Models
作者: Feihong Yan, Shaoyu Liu, Haixuan Wang, Shuai Lu, Linfeng Zhang, Huiqi Li, Xiangyang Ji
链接: https://arxiv.org/abs/2605.10045v1
完整摘要: Visual Autoregressive (VAR) models have emerged as a strong alternative to diffusion for image synthesis, yet their fixed training resolution prevents direct generation at higher resolutions. Naively transferring training-free extrapolation methods from LLMs or diffusion models to VAR yields three characteristic failure modes: global repetition, local repetition, and detail degradation. We trace them to a unified band-stage mismatch: VAR generates images in a coarse-to-fine, scale-wise process where each stage is driven by a distinct dominant RoPE frequency band, and each failure mode emerges when the dominant band of a particular stage is disrupted. Building on this insight, we propose Stage-Aware RoPE Remapping, a training-free strategy that assigns each frequency band a stage-specific remapping rule, jointly suppressing all three failure modes. We further observe that attention becomes systematically dispersed as the image resolution increases. Existing methods typically depend on predefined attention scaling factors, which are neither adaptive to the target resolution nor capable of faithfully capturing the actual extent of attention dispersion. We therefore propose Entropy-Driven Adaptive Attention Calibration, which quantifies dispersion via a resolution-invariant normalized entropy and yields a closed-form per-head scaling factor that realigns the extrapolated-resolution attention entropy with its training-resolution counterpart. Extensive experiments show that our method consistently outperforms prior resolution-extrapolation methods in both structural coherence and fine-detail fidelity. Our code is available at https://github.com/feihongyan1/ExtraVAR.
匹配关键词: autoregressive
---

[ACADEMIC - ARXIV]
标题: TrajDLM: Topology-Aware Block Diffusion Language Model for Trajectory Generation
作者: Wilson Wongso, Lihuan Li, Arian Prabowo, Xiachong Lin, Baiyu Chen, Hao Xue, Flora D. Salim
链接: https://arxiv.org/abs/2605.10020v1
完整摘要: Generating high-fidelity synthetic GPS trajectories is increasingly important for applications in transportation, urban planning, and what-if scenario simulation, especially as privacy concerns limit access to real-world mobility data. Existing trajectory generation models face a trade-off between efficiency and faithfulness to road network topology: continuous-space methods enable fast generation but ignore the road network, while topology-aware approaches rely on search-based autoregressive decoding that limits generation speed. We propose TrajDLM, a topology-aware trajectory generation framework based on block diffusion language models that bridges this gap. TrajDLM models trajectories as sequences of discrete road segments, combining a block diffusion backbone for efficient denoising, topology-aware embeddings from a road network encoder, and topology-constrained sampling to ensure coherent and realistic trajectories. Across three city-scale datasets, TrajDLM achieves strong performance on fine-grained local similarity metrics while being up to $2.8\times$ faster than prior work, and demonstrates strong zero-shot transfer across domains, including unseen transportation modes. These results highlight the effectiveness of block-wise discrete diffusion as a scalable approach to accurate and efficient trajectory generation. Our code is available at https://github.com/cruiseresearchgroup/TrajDLM/
匹配关键词: autoregressive
---

[ACADEMIC - ARXIV]
标题: The two clocks and the innovation window: When and how generative models learn rules
作者: Binxu Wang, Emma Lucia Byrnes Finn, Bingbin Liu
链接: https://arxiv.org/abs/2605.10019v1
完整摘要: Generative models trained on finite data face a fundamental tension: their score-matching or next-token objective converges to the empirical training distribution rather than the population distribution we seek to learn. Using rule-valid synthetic tasks, we trace this tension across two training timescales: $τ_{\mathrm{rule}}$, the step at which generations first become rule-valid, and $τ_{\mathrm{mem}}$, the step at which models begin reproducing training samples. Focusing on parity and extending to other binary rules and combinatorial puzzles, we characterize how these two clocks, $τ_{\mathrm{rule}}$ and $τ_{\mathrm{mem}}$, depend on key aspects of the learning setup. Specifically, we show that $τ_{\mathrm{rule}}$ increases with rule complexity and decreases with model capacity, while $τ_{\mathrm{mem}}$ is approximately invariant to the rule and scales nearly linearly with dataset size $N$. We define the \emph{innovation window} as the interval $[τ_{\mathrm{rule}}, τ_{\mathrm{mem}}]$. This window widens with increasing $N$ and narrows with rule complexity, and may vanish entirely when $τ_{\mathrm{rule}} \geq τ_{\mathrm{mem}}$. The same two-clock structure arises in both diffusion (DiT) and autoregressive (GPT) models, with architecture-dependent offsets. Dissecting the learned score of DiT models reveals a corresponding evolution of the optimization landscapes, where rule-valid samples' basins expand substantially around $τ_{\mathrm{rule}}$, while training samples' basins begin to dominate around $τ_{\mathrm{mem}}$. Together, these results yield a unified and predictive account of when and how generative models exhibit genuine innovation.
匹配关键词: autoregressive
---

[ACADEMIC - ARXIV]
标题: Attention Drift: What Autoregressive Speculative Decoding Models Learn
作者: Doğaç Eldenk, Payal Mohapatra, Yigitcan Comlek, Kaan Oktay, Hongyang Zhang, Stephen Xia
链接: https://arxiv.org/abs/2605.09992v1
完整摘要: Speculative decoding accelerates LLM inference by drafting future tokens with a small model, but drafter models degrade sharply under template perturbation and long-context inputs. We identify a previously-unreported phenomenon we call \textbf{attention drift}: as the drafter generates successive tokens within a speculation chain, attention progressively moves from the prompt onto its own recently-generated tokens. We observe this across both \emph{EAGLE3} drafters and \emph{MTP heads}, suggesting drift is a property of drafter designs. We trace this to the un-normalized residual path between chain steps: the drafter's hidden state magnitude grows monotonically with chain depth, which exhibits dynamics consistent with additional pre-norm transformer layers stacked on the target rather than as a standalone autoregressive predictor. In order to limit the growth, we propose two architectural changes: Post-norm on the drafter hidden states and per-hidden-state RMSNorm after capturing target hidden states. Our interventions improve acceptance length over the current leading model, pre-norm EAGLE3, by up to $2\times$ under template perturbation, $1.18\times$ on long-context tasks, and $1.10\times$ on seven standard benchmarks spanning multi-turn chat, math, and coding. Our changes also allow shorter train-time-test depths to generalize over longer drafting sequences.
匹配关键词: autoregressive
---

[ACADEMIC - ARXIV]
标题: Active Tabular Augmentation via Policy-Guided Diffusion Inpainting
作者: Zheyu Zhang, Shuo Yang, Bardh Prenkaj, Gjergji Kasneci
链接: https://arxiv.org/abs/2605.10315v1
完整摘要: Generative tabular augmentation is appealing in data-scarce domains, yet the prevailing focus on distributional fidelity does not reliably translate into better downstream models. We formalize a fidelity-utility gap: common generative objectives prioritize distributional plausibility, whereas augmentation succeeds only when injected samples reduce the current learner's held-out evaluation loss. This gap motivates learning not just how to generate, but what to generate and when to inject as training evolves. We propose TAP (Tabular Augmentation Policy), which couples diffusion inpainting with a lightweight, learner-conditioned policy to steer generation toward high-utility regions and controls safe injection via explicit gating and conservative windowed commitment. Under severe data scarcity, TAP consistently outperforms strong generative baselines on seven real-world datasets, improving classification accuracy by up to 15.6 percentage points and reducing regression RMSE by up to 32%.
匹配关键词: latent diffusion
---

[ACADEMIC - ARXIV]
标题: MemReread: Enhancing Agentic Long-Context Reasoning via Memory-Guided Rereading
作者: Baibei Ji, Xiaoyang Weng, Juntao Li, Zecheng Tang, Yihang Lou, Min Zhang
链接: https://arxiv.org/abs/2605.10268v1
完整摘要: To tackle long-context reasoning tasks without the quadratic complexity of standard attention mechanisms, approaches based on agent memory have emerged, which typically maintain a dynamically updated memory when linearly processing document chunks. To mitigate the potential loss of latent evidence in this memorize-while-reading paradigm, recent works have integrated retrieval modules that allow agents to recall information previously discarded during memory overwriting. However, retrieval-based recall suffers from both evidence loss during memory formation and interference induced by invalid queries. To overcome these limitations, we propose MemReread. Built upon streaming reading, MemReread circumvents intermediate retrieval. It triggers question decomposition and rereading when the final memory is insufficient, enabling the recovery of indirect facts that were prematurely discarded. This design supports non-linear reasoning while preserving the inherent logical flow of document comprehension. To further enhance practicality, we introduce a reinforcement learning framework that enhances length extrapolation capability while dynamically determining the number of rereading passes based on task complexity, thereby flexibly controlling computational overhead. Extensive experiments demonstrate that MemReread consistently outperforms baseline frameworks on long-context reasoning tasks, while maintaining linear time complexity with respect to context length.
匹配关键词: latent diffusion
---

[ACADEMIC - ARXIV]
标题: E-TCAV: Formalizing Penultimate Proxies for Efficient Concept Based Interpretability
作者: Hasib Aslam, Muhammad Ali Chattha, Muhammad Taha Mukhtar, Muhammad Imran Malik, Andreas Dengel, Sheraz Ahmed
链接: https://arxiv.org/abs/2605.10261v1
完整摘要: TCAV (Testing with Concept Activation Vectors) is an interpretability method that assesses the alignment between the internal representations of a trained neural network and human-understandable, high-level concepts. Though effective, TCAV suffers from significant computational overhead, inter-layer disagreement of TCAV scores, and statistical instability. This work takes a step toward addressing these challenges by introducing E-TCAV, a framework for efficient approximation of TCAV scores, which is based on extensive investigation into three key aspects of the TCAV methodology: 1) the effect of latent classifiers on the stability of TCAV scores, 2) the inter-layer agreement of TCAV scores, and 3) the use of the penultimate layer as a fast proxy for earlier layers for TCAV computation. To ensure a solid foundation for E-TCAV, we conduct extensive evaluations across four different architectures and five datasets, encompassing problems from both computer vision and natural language domains. Our results show that the layers in the final block of the neural network strongly agree with the penultimate layer in terms of the TCAV scores, and the commonly observed variance of the TCAV scores can be attributed to the choice of the latent classifier. Leveraging this inter-layer agreement and the degeneracy of directional sensitivities at the penultimate layer, E-TCAV guarantees linearly scaling speed-ups with respect to the network's size and the number of evaluation samples, marking a step towards efficient model debugging and real-time concept-guided training.
匹配关键词: latent diffusion
---

[ACADEMIC - ARXIV]
标题: A Cold Diffusion Approach for Percussive Dereverberation
作者: Dimos Makris, András Barják, Maximos Kaliakatsos-Papakostas
链接: https://arxiv.org/abs/2605.10256v1
完整摘要: Most recent advances in audio dereverberation focus almost exclusively on speech, leaving percussive and drum signals largely unexplored despite their importance in music production. Percussive dereverberation poses distinct challenges due to sharp transients and dense temporal structure. In this work, we propose a cold diffusion framework for dereverberating stereo drum stems (downmixes), modeling reverberation as a deterministic degradation process that progressively transforms anechoic signals into reverberant ones. We investigate two reverse-process parameterizations, Direct (next-state) and a Delta-normalized residual (velocity-style) prediction, and implement the framework using both a UNet and a diffusion Transformer backbone. The models are trained and evaluated on curated datasets comprising both acoustic and electronic drum recordings, with reverberation generated using a combination of synthetic and real room impulse responses. Extensive experiments on in-domain and fully out-of-domain test sets demonstrate that the proposed method consistently outperforms strong score-based and conditional diffusion baselines, evaluated using signal-based and perceptual metrics tailored to percussive audio.
匹配关键词: latent diffusion
---

[ACADEMIC - ARXIV]
标题: Route Before Retrieve: Activating Latent Routing Abilities of LLMs for RAG vs. Long-Context Selection
作者: Yiwen Chen, Kuan Li, Fuzhen Zhuang, Deqing Wang, Zhao Zhang, Liwen Zhang, Yong Jiang, Shuai Wang, Minhao Cheng
链接: https://arxiv.org/abs/2605.10235v1
完整摘要: Recent advances in large language models (LLMs) have expanded the context window to beyond 128K tokens, enabling long-document understanding and multi-source reasoning. A key challenge, however, lies in choosing between retrieval-augmented generation (RAG) and long-context (LC) strategies: RAG is efficient but constrained by retrieval quality, while LC supports global reasoning at higher cost and with position sensitivity. Existing methods such as Self-Route adopt failure-driven fallback from RAG to LC, but remain passive, inefficient, and hard to interpret. We propose Pre-Route, a proactive routing framework that performs structured reasoning before answering. Using lightweight metadata (e.g., document type, length, initial snippet), Pre-Route enables task analysis, coverage estimation, and information-need prediction, producing explainable and cost-efficient routing decisions. Our study shows three key findings: (i) LLMs possess latent routing ability that can be reliably elicited with guidelines, allowing single-sample performance to approach that of multi-sample (Best-of-N) results; (ii) linear probes reveal that structured prompts sharpen the separability of the "optimal routing dimension" in representation space; and (iii) distillation transfers this reasoning structure to smaller models for lightweight deployment. Experiments on LaRA (in-domain) and LongBench-v2 (OOD) confirm that Pre-Route outperforms Always-RAG, Always-LC, and Self-Route baselines, achieving superior overall cost-effectiveness.
匹配关键词: latent diffusion
---

[ACADEMIC - ARXIV]
标题: AgentRx: A Benchmark Study of LLM Agents for Multimodal Clinical Prediction Tasks
作者: Baraa Al Jorf, Farah E. Shamout
链接: https://arxiv.org/abs/2605.10286v1
完整摘要: Building effective clinical decision support systems requires the synthesis of complex heterogeneous multimodal data. Such modalities include temporal electronic health records data, medical images, radiology reports, and clinical notes. Large language model (LLM)-based agents have shown impressive performance in various healthcare tasks, especially those involving textual modalities. Considering the fragmentation of healthcare data across hospital systems, collaborative agent frameworks present a promising direction to mitigate data sharing challenges. However, the effectiveness of LLM agents for multimodal clinical risk prediction remains largely unexamined. In this work, we conduct a systematic evaluation of LLM-based agents for clinical prediction tasks using large-scale real-world data. We assess performance in unimodal and multimodal settings and quantify performance gaps between single agent and multi-agent systems. Our findings highlight that single agent frameworks outperform naive multi-agent systems, are better at handling multimodal data, and are better calibrated. This underscores a critical need for improving multi-agent collaboration to better handle heterogeneous inputs. By open-sourcing our code and evaluation framework, this work offers a new benchmark to support future developments relating to agentic systems in healthcare.
匹配关键词: multimodal
---

[ACADEMIC - ARXIV]
标题: Knowledge Poisoning Attacks on Medical Multi-Modal Retrieval-Augmented Generation
作者: Peiru Yang, Haoran Zheng, Tong Ju, Shiting Wang, Wanchun Ni, Jiajun Liu, Shangguang Wang, Yongfeng Huang, Tao Qi
链接: https://arxiv.org/abs/2605.10253v1
完整摘要: Retrieval-augmented generation (RAG) is a widely adopted paradigm for enhancing LLMs in medical applications by incorporating expert multimodal knowledge during generation. However, the underlying retrieval databases may naturally contain, or be intentionally injected with, adversarial knowledge, which can perturb model outputs and undermine system reliability. To investigate this risk, prior studies have explored knowledge poisoning attacks in medical RAG systems. Nevertheless, most of them rely on the strong assumption that adversaries possess prior knowledge of user queries, which is unrealistic in deployments and substantially limits their practical applicability. In this paper, we propose M\textsuperscript{3}Att, a knowledge-poisoning framework designed for medical multimodal RAG systems, assuming only limited distribution knowledge of the underlying database. Our core idea is to inject covert misinformation into textual data while using paired visual data as a query-agnostic trigger to promote retrieval. We first propose a unified framework that introduces imperceptible perturbations to visual inputs to manipulate retrieval probabilities. Besides, due to the prior medical knowledge in LLMs, naively poisoned medical content with explicit factual errors can be corrected during generation. Thus, we leverage the inherent ambiguity of medical diagnosis and design a covert misinformation injection strategy that degrades diagnostic accuracy while evading model self-correction. Experiments on five LLMs and datasets demonstrate that M\textsuperscript{3}Att consistently produces clinically plausible yet incorrect generations. Codes: https://github.com/ypr17/M3Att.
匹配关键词: multimodal
---

[ACADEMIC - ARXIV]
标题: SciVQR: A Multidisciplinary Multimodal Benchmark for Advanced Scientific Reasoning Evaluation
作者: Longteng Guo, Xuanxu Lin, Dongze Hao, Tongtian Yue, Pengkang Huo, Jiatong Ma, Yuchen Liu, Jing Liu
链接: https://arxiv.org/abs/2605.10187v1
完整摘要: Scientific reasoning is a key aspect of human intelligence, requiring the integration of multimodal inputs, domain expertise, and multi-step inference across various subjects. Existing benchmarks for multimodal large language models (MLLMs) often fail to capture the complexity and traceability of reasoning processes necessary for rigorous evaluation. To fill this gap, we introduce SciVQR, a multimodal benchmark covering 54 subfields in mathematics, physics, chemistry, geography, astronomy, and biology. SciVQR includes domain-specific visuals, such as equations, charts, and diagrams, and challenges models to combine visual comprehension with reasoning. The tasks range from basic factual recall to complex, multi-step inferences, with 46% including expert-authored solutions. SciVQR not only evaluates final answers but also examines the reasoning process, providing insights into how models reach their conclusions. Our evaluation of leading MLLMs, including both proprietary and open-source models, reveals significant limitations in handling complex multimodal reasoning tasks, underscoring the need for improved multi-step reasoning and better integration of interdisciplinary knowledge in advancing MLLMs toward true scientific intelligence. The dataset and evaluation code are publicly available at https://github.com/CASIA-IVA-Lab/SciVQR.
匹配关键词: multimodal
---

[ACADEMIC - ARXIV]
标题: V-ABS: Action-Observer Driven Beam Search for Dynamic Visual Reasoning
作者: Zhiwei Ning, Xuanang Gao, Jiaxi Cao, Gengming Zhang, Shengnan Ma, Wenwen Tong, Hanming Deng, Jie Yang, Wei Liu
链接: https://arxiv.org/abs/2605.10172v1
完整摘要: Multimodal large language models (MLLMs) have achieved remarkable success in general perception, yet complex multi-step visual reasoning remains a persistent challenge. Although recent agentic approaches incorporate tool use, they often neglect critical execution feedback. Consequently, they suffer from the imagination-action-observer (IAO) bias, a misalignment between prior imagination and observer feedback that undermines reasoning stability and optimality. To bridge this gap, we introduce V-ABS, an action-observer driven beam search framework that enables deliberate reasoning through thinker-actor-observer iterations. We also propose an entropy-based adaptive weighting algorithm to mitigate the IAO bias by dynamically balancing the confidence scores between the policy priors and the observational feedback. Moreover, we construct a large-scale supervised fine-tuning (SFT) dataset comprising over 80k samples to guide the model to assign higher prior confidence to correct action paths. Extensive experiments across eight diverse benchmarks show that V-ABS achieves state-of-the-art performance, delivering an average improvement of 19.7% on the Qwen3-VL-8B baseline and consistent gains across both open-source and proprietary models.
匹配关键词: multimodal
---

[ACADEMIC - ARXIV]
标题: MicroWorld: Empowering Multimodal Large Language Models to Bridge the Microscopic Domain Gap with Multimodal Attribute Graph
作者: Manyu Li, Ruian He, Chenxi Ma, Weimin Tan, Bo Yan
链接: https://arxiv.org/abs/2605.10120v1
完整摘要: Multimodal large language models (MLLMs) show remarkable potential for scientific reasoning, yet their performance in specialized domains such as microscopy remains limited by the scarcity of domain-specific training data and the difficulty of encoding fine-grained expert knowledge into model parameters. To bridge the gap, we introduce MicroWorld, a framework that constructs a multimodal attributed property graph (MAPG) from large-scale scientific image--caption corpora and leverages it to augment MLLM reasoning at inference time without any domain-specific fine-tuning. MicroWorld extracts biomedical entities and relations via scispaCy or LLM-based triplet mining, aligns images and entities in a shared embedding space using Qwen3-VL-Embedding, and assembles a knowledge graph comprising approximately 111K nodes and 346K typed edges spanning eight relation categories. At inference time, a graph-augmented retrieval pipeline matches query entities to the MAPG and injects structured knowledge context into the MLLM prompt. On the MicroVQA benchmark, MicroWorld improves the reasoning performance of Qwen3-VL-8B-Instruct by 37.5%, outperforming GPT-5 by 13.0% to achieve a new state-of-the-art. Furthermore, it yields a 6.0% performance gain on the MicroBench benchmark. Extensive experiments demonstrate the enhanced generalization capability introduced by MicroWorld. A qualitative case study further reveals both the mechanisms through which structured knowledge improves reasoning and the failure modes that point to promising future directions. Code and data are available at https://github.com/ieellee/MicroWorld.
匹配关键词: multimodal
---

[ACADEMIC - ARXIV]
标题: Extending Confidence-Based Text2Cypher with Grammar and Schema Aware Filtering
作者: Makbule Gulcin Ozsoy
链接: https://arxiv.org/abs/2605.10318v1
完整摘要: Large language models (LLMs) allow users to query databases using natural language by translating questions into executable queries. Despite strong progress on tasks such as Text2SQL, Text2SPARQL, and Text2Cypher, most existing methods focus on better prompting, fine-tuning, or iterative refinement. However, they often do not explicitly enforce structural constraints, such as syntactic validity and schema consistency. This can reduce reliability, since generated queries must satisfy both syntax rules and database schema constraints to be executable. In this work, we study how structured constraints can be used in test-time inference for Text2Cypher. We focus on post-generation validation to improve query correctness. We extend a confidence-based inference framework with a sequential filtering process that combines confidence scoring, grammar validation, and schema constraints before final aggregation. This lets us analyze how different constraint types affect generated queries. Our experiments with two instruction-tuned models show that grammar-based filtering improves syntactic validity. Schema-aware filtering further improves execution quality by enforcing consistency with the database structure. However, stronger filtering also increases the number of empty predictions and reduces execution coverage. Overall, we show that adding simple structural checks at test time improves the reliability of Text2Cypher generation, and we provide a clearer view of how syntax and schema constraints contribute differently.
匹配关键词: vision language model
---

[ACADEMIC - ARXIV]
标题: Relations Are Channels: Knowledge Graph Embedding via Kraus Decompositions
作者: Sayan Kumar Chaki
链接: https://arxiv.org/abs/2605.10317v1
完整摘要: Knowledge graph embedding (KGE) models typically represent each relation as an operator on entity embeddings. In this work, we identify three structural axioms that any principled relation operator must satisfy, linearity, trace preservation, and complete positivity, and show that they characterize a Kraus channel structure via the Kraus representation theorem. The completeness constraint defining this family is equivalent to these axioms, providing a principled foundation rather than an externally imposed condition. Under this formulation, most existing operator-based KGE models are recoverable as special cases with Kraus rank $κ= 1$ under specific embedding choices. We further generalize this characterization to arbitrary metric geometries by introducing \mbox{w-Kraus} channels, which satisfy completeness by construction within their respective spaces. Building on this theory, we propose \textsc{KrausKGE}, a principled KGE model that naturally handles $1$-to-$N$ and $N$-to-$N$ relations, supports $k$-hop reasoning without requiring explicit path encoders, and eliminates the need for norm constraints on entity embeddings. Additionally, our framework yields the first theoretically grounded per-relation complexity measure in the KGE literature, with a provable lower bound in terms of the empirical relation matrix rank. Empirical evaluation demonstrates that \textsc{KrausKGE} consistently outperforms strong baselines on $N$-to-$N$ relations, with performance gains that increase monotonically with relation fan-out, in alignment with theoretical predictions.
匹配关键词: vision language model
---

[ACADEMIC - ARXIV]
标题: Active Tabular Augmentation via Policy-Guided Diffusion Inpainting
作者: Zheyu Zhang, Shuo Yang, Bardh Prenkaj, Gjergji Kasneci
链接: https://arxiv.org/abs/2605.10315v1
完整摘要: Generative tabular augmentation is appealing in data-scarce domains, yet the prevailing focus on distributional fidelity does not reliably translate into better downstream models. We formalize a fidelity-utility gap: common generative objectives prioritize distributional plausibility, whereas augmentation succeeds only when injected samples reduce the current learner's held-out evaluation loss. This gap motivates learning not just how to generate, but what to generate and when to inject as training evolves. We propose TAP (Tabular Augmentation Policy), which couples diffusion inpainting with a lightweight, learner-conditioned policy to steer generation toward high-utility regions and controls safe injection via explicit gating and conservative windowed commitment. Under severe data scarcity, TAP consistently outperforms strong generative baselines on seven real-world datasets, improving classification accuracy by up to 15.6 percentage points and reducing regression RMSE by up to 32%.
匹配关键词: vision language model
---

[ACADEMIC - ARXIV]
标题: PaMoSplat: Part-Aware Motion-Guided Gaussian Splatting for Dynamic Scene Reconstruction
作者: Yinan Deng, Jianyu Dou, Jiahui Wang, Jingyu Zhao, Yi Yang, Yufeng Yue
链接: https://arxiv.org/abs/2605.10307v1
完整摘要: Dynamic scene reconstruction represents a fundamental yet demanding challenge in computer vision and robotics. While recent progress in 3DGS-based methods has advanced dynamic scene modeling, obtaining high-fidelity rendering and accurate tracking in scenarios with substantial, intricate motions remains significantly challenging. To address these challenges, we propose PaMoSplat, a novel dynamic Gaussian splatting framework incorporating part awareness and motion priors. Our approach is grounded in two key observations: 1) Parts serve as primitives for scene deformation, and 2) Motion cues from optical flow can effectively guide part motion. Specifically, PaMoSplat initializes by lifting multi-view segmentation masks into 3D space via graph clustering, establishing coherent Gaussian parts. For subsequent timestamps, we leverage a differential evolutionary algorithm to estimate the rigid motion of these parts using multi-view optical flow cues, providing a robust warm-start for further optimization. Additionally, PaMoSplat introduces an adaptive iteration count mechanism, internal learnable rigidity, and flow-supervised rendering loss to accelerate and optimize the training process. Comprehensive evaluations across diverse scenes, including real-world environments, demonstrate that PaMoSplat delivers superior rendering quality, improved tracking precision, and faster convergence compared to existing methods. Furthermore, it enables multiple part-level downstream applications, such as 4D scene editing.
匹配关键词: vision language model
---

[ACADEMIC - ARXIV]
标题: Follow the Mean: Reference-Guided Flow Matching
作者: Pedro M. P. Curvo, Maksim Zhdanov, Floor Eijkelboom, Jan-Willem van de Meent
链接: https://arxiv.org/abs/2605.10302v1
完整摘要: Existing approaches to controllable generation typically rely on fine-tuning, auxiliary networks, or test-time search. We show that flow matching admits a different control interface: adaptation through examples. For deterministic interpolants, the velocity field is solely governed by a conditional endpoint mean; shifting this mean shifts the flow itself. This yields a simple principle for controllable generation: steer a pretrained model by changing the reference set it follows. We instantiate this idea in two forms. Reference-Mean Guidance is training-free: it computes a closed-form endpoint-mean correction from a reference bank and applies it to a frozen FLUX.2-klein (4B) model, enabling control of color, identity, style, and structure while keeping the prompt, seed, and weights fixed. Semi-Parametric Guidance amortizes the same idea through an explicit mean anchor and learned residual refiner, matching unconditional DiT-B/4 quality on AFHQv2 while allowing the reference set to be swapped at inference time. These results point to a broader direction: generative models that adapt through data, not parameter updates.
匹配关键词: vision language model
---

[ACADEMIC - ARXIV]
标题: Plan in Sandbox, Navigate in Open Worlds: Learning Physics-Grounded Abstracted Experience for Embodied Navigation
作者: Zhixuan Shen, Jiawei Du, Ziyu Guo, Han Luo, Lilan Peng, Joey Tianyi Zhou, Haonan Luo, Tianrui Li
链接: https://arxiv.org/abs/2605.10118v1
完整摘要: Vision-Language Models (VLMs) have demonstrated exceptional general reasoning capabilities. However, their performance in embodied navigation remains hindered by a scarcity of aligned open-world vision and robot control data. Despite simulators providing a cost-effective alternative for data collection, the inherent reliance on photorealistic simulations often limits the transferability of learned policies. To this end, we propose \textit{\textbf{S}andbox-\textbf{A}bstracted \textbf{G}rounded \textbf{E}xperience} (\textbf{\textit{SAGE}}), a framework that enables agents to learn within a physics-grounded semantic abstraction rather than a photorealistic simulation, mimicking the human capacity for mental simulation where plans are rehearsed in simplified physics abstractions before execution. \textit{SAGE} system operates via three synergistic phases: (1) \textit{Genesis}: constructing diverse, physics-constrained semantic environments to bootstrap experience; (2) \textit{Evolution}: distilling experiences through Reinforcement Learning (RL), utilizing a novel asymmetric adaptive clipping mechanism to stabilize updates; (3) \textit{Navigation}: bridging the abstract policy to open-world control. We demonstrate that \textit{SAGE} significantly improves planner-assisted embodied navigation, achieving a 53.21\% LLM-Match Success Rate on A-EQA (+9.7\% over baseline), while showing encouraging transfer to physical indoor robot deployment.
匹配关键词: VLM
---

[ACADEMIC - ARXIV]
标题: SocialDirector: Training-Free Social Interaction Control for Multi-Person Video Generation
作者: Liangyang Ouyang, Ruicong Liu, Caixin Kang, Yifei Huang, Yoichi Sato
链接: https://arxiv.org/abs/2605.10079v1
完整摘要: Video generation has advanced rapidly, producing photorealistic videos from text or image prompts. Meanwhile, film production and social robotics increasingly demand multi-person videos with rich social interactions, including conversations, gestures, and coordinated actions. However, existing models offer no explicit control over interactions, such as who performs which action, when it occurs, and toward whom it is directed. This often results in wrong person performing unintended actions (actor-action mismatch), disordered social dynamics, and wrong action targets. To address these challenges, we present SocialDirector, a training-free interaction controller that enhances the generation model by modulating cross-attention maps. SocialDirector contains two modules: Social Actor Masking and Directional Reweighting. Social Actor Masking constrains each person's visual tokens to attend only to their own textual descriptions via a spatiotemporal mask, avoiding actor-action mismatch and disordered social dynamics. Directional Reweighting amplifies attention to directional words (e.g., "leftward", "right"), leading each action towards its intended target. To evaluate generated social interactions, we annotate existing datasets with interaction descriptions and build a fully automated evaluation pipeline powered by open-source VLMs. Experiments on different video generation models show that SocialDirector significantly improves interaction fidelity and approaches the upper bound set by real videos.
匹配关键词: VLM
---

[ACADEMIC - ARXIV]
标题: Med-StepBench: A Hierarchical Reasoning Framework for Evaluating Hallucinations in Medical Vision-Language Models
作者: Minh Khoi Nguyen, Dai Lam Le, Amir Reza Jafari, Tuan Dung Nguyen, Mai Hong Son, Mai Huy Thong, Quang Huy Nguyen, Thanh Trung Nguyen, Reza Farahbakhsh, Noel Crespi, Phi Le Nguyen
链接: https://arxiv.org/abs/2605.10002v1
完整摘要: Large vision-language models (VLMs) demonstrate strong performance in medical image understanding, but frequently generate clinically plausible yet incorrect statements, raising significant safety concerns. Existing medical hallucination benchmarks primarily focus on 2D imaging with one-shot diagnostic questions, offering limited insight into whether predictions are grounded in correct localization and abnormality identification, allowing critical reasoning errors to remain hidden behind seemingly correct diagnoses. We introduce Med-StepBench, the first large-scale benchmark for step-wise hallucination detection in 3D oncological PET/CT, comprising over 12,000 images and more than 1,000,000 image-statement pairs across volumetric and multi-view 2D data, which decomposes clinical reasoning into four expert-designed diagnostic stages. Using clinician-verified annotations, we perform the first step-level evaluation of general-purpose and medical VLMs, revealing systematic failure modes obscured by aggregate accuracy metrics. Furthermore, we show that current VLMs are highly susceptible to adversarial yet clinically plausible intermediate explanations, which significantly amplify hallucinations despite contradictory visual evidence. Together, our findings highlight fundamental limitations in grounding multi-step clinical reasoning and establish Med-StepBench as a rigorous benchmark for developing safer and more reliable medical VLMs.
匹配关键词: VLM
---

[ACADEMIC - ARXIV]
标题: ERASE: Eliminating Redundant Visual Tokens via Adaptive Two-Stage Token Pruning
作者: Yuna Lee, Kyoungho Min, Yulhwa Kim
链接: https://arxiv.org/abs/2605.09982v1
完整摘要: Recent advancements in Vision-Language Models (VLMs) enable large language models (LLMs) to process high-resolution images, significantly improving real-world multimodal understanding. However, this capability introduces a large number of vision tokens, resulting in substantial computational overhead. To mitigate this issue, various vision token pruning methods have been proposed. Nevertheless, existing approaches predominantly rely on learned semantic features within the model to capture visual redundancy. Moreover, they lack adaptive mechanisms to adjust pruning strategies according to the complexity of the input image. In this paper, we propose ERASE, a two-stage vision token pruning framework that identifies and retains salient tokens through pruning strategies adaptive to image complexity. Experiment results demonstrate that ERASE significantly reduces vision tokens while preserving accuracy. For Qwen2.5-VL-7B, at a token pruning ratio of 85\%, ERASE retains 89.46% of the original model accuracy, whereas the best prior method retains only 78.1%. Our code is available at https://github.com/Tuna-Luna/ERASE.
匹配关键词: VLM
---

[ACADEMIC - ARXIV]
标题: OZ-TAL: Online Zero-Shot Temporal Action Localization
作者: Chaolei Han, Hongsong Wang, Xin Gong, Jie Gui
链接: https://arxiv.org/abs/2605.09976v1
完整摘要: Online Temporal Action Localization (On-TAL) aims to detect the occurrence time and category of actions in untrimmed streaming videos immediately upon their completion. Recent advancements in this field focus on developing more sophisticated frameworks, shifting from Online Action Detection (OAD)-based aggregation paradigm to instance-level understanding. However, existing approaches are typically trained on specific domains and often exhibit limited generalization capabilities when applied to arbitrary videos, particularly in the presence of previously unseen actions. In this paper, we introduce a new task called Online Zero-shot Temporal Action Localization (OZ-TAL), which aims to detect previously unseen actions in an online fashion. Furthermore, we propose a training-free framework that leverages off-the-shelf Vision-Language Models (VLMs) while introducing additional mechanisms to enhance visual representations and mitigate their inherent biases. We establish new benchmarks and representative baselines for OZ-TAL on THUMOS14 and ActivityNet-1.3, and extensive experiments demonstrate that our method substantially outperforms existing state-of-the-art approaches under both offline and online zero-shot settings.
匹配关键词: VLM
---

[ACADEMIC - ARXIV]
标题: Extending Confidence-Based Text2Cypher with Grammar and Schema Aware Filtering
作者: Makbule Gulcin Ozsoy
链接: https://arxiv.org/abs/2605.10318v1
完整摘要: Large language models (LLMs) allow users to query databases using natural language by translating questions into executable queries. Despite strong progress on tasks such as Text2SQL, Text2SPARQL, and Text2Cypher, most existing methods focus on better prompting, fine-tuning, or iterative refinement. However, they often do not explicitly enforce structural constraints, such as syntactic validity and schema consistency. This can reduce reliability, since generated queries must satisfy both syntax rules and database schema constraints to be executable. In this work, we study how structured constraints can be used in test-time inference for Text2Cypher. We focus on post-generation validation to improve query correctness. We extend a confidence-based inference framework with a sequential filtering process that combines confidence scoring, grammar validation, and schema constraints before final aggregation. This lets us analyze how different constraint types affect generated queries. Our experiments with two instruction-tuned models show that grammar-based filtering improves syntactic validity. Schema-aware filtering further improves execution quality by enforcing consistency with the database structure. However, stronger filtering also increases the number of empty predictions and reduces execution coverage. Overall, we show that adding simple structural checks at test time improves the reliability of Text2Cypher generation, and we provide a clearer view of how syntax and schema constraints contribute differently.
匹配关键词: image generation
---

[ACADEMIC - ARXIV]
标题: Relations Are Channels: Knowledge Graph Embedding via Kraus Decompositions
作者: Sayan Kumar Chaki
链接: https://arxiv.org/abs/2605.10317v1
完整摘要: Knowledge graph embedding (KGE) models typically represent each relation as an operator on entity embeddings. In this work, we identify three structural axioms that any principled relation operator must satisfy, linearity, trace preservation, and complete positivity, and show that they characterize a Kraus channel structure via the Kraus representation theorem. The completeness constraint defining this family is equivalent to these axioms, providing a principled foundation rather than an externally imposed condition. Under this formulation, most existing operator-based KGE models are recoverable as special cases with Kraus rank $κ= 1$ under specific embedding choices. We further generalize this characterization to arbitrary metric geometries by introducing \mbox{w-Kraus} channels, which satisfy completeness by construction within their respective spaces. Building on this theory, we propose \textsc{KrausKGE}, a principled KGE model that naturally handles $1$-to-$N$ and $N$-to-$N$ relations, supports $k$-hop reasoning without requiring explicit path encoders, and eliminates the need for norm constraints on entity embeddings. Additionally, our framework yields the first theoretically grounded per-relation complexity measure in the KGE literature, with a provable lower bound in terms of the empirical relation matrix rank. Empirical evaluation demonstrates that \textsc{KrausKGE} consistently outperforms strong baselines on $N$-to-$N$ relations, with performance gains that increase monotonically with relation fan-out, in alignment with theoretical predictions.
匹配关键词: image generation
---

[ACADEMIC - ARXIV]
标题: Active Tabular Augmentation via Policy-Guided Diffusion Inpainting
作者: Zheyu Zhang, Shuo Yang, Bardh Prenkaj, Gjergji Kasneci
链接: https://arxiv.org/abs/2605.10315v1
完整摘要: Generative tabular augmentation is appealing in data-scarce domains, yet the prevailing focus on distributional fidelity does not reliably translate into better downstream models. We formalize a fidelity-utility gap: common generative objectives prioritize distributional plausibility, whereas augmentation succeeds only when injected samples reduce the current learner's held-out evaluation loss. This gap motivates learning not just how to generate, but what to generate and when to inject as training evolves. We propose TAP (Tabular Augmentation Policy), which couples diffusion inpainting with a lightweight, learner-conditioned policy to steer generation toward high-utility regions and controls safe injection via explicit gating and conservative windowed commitment. Under severe data scarcity, TAP consistently outperforms strong generative baselines on seven real-world datasets, improving classification accuracy by up to 15.6 percentage points and reducing regression RMSE by up to 32%.
匹配关键词: image generation
---

[ACADEMIC - ARXIV]
标题: Follow the Mean: Reference-Guided Flow Matching
作者: Pedro M. P. Curvo, Maksim Zhdanov, Floor Eijkelboom, Jan-Willem van de Meent
链接: https://arxiv.org/abs/2605.10302v1
完整摘要: Existing approaches to controllable generation typically rely on fine-tuning, auxiliary networks, or test-time search. We show that flow matching admits a different control interface: adaptation through examples. For deterministic interpolants, the velocity field is solely governed by a conditional endpoint mean; shifting this mean shifts the flow itself. This yields a simple principle for controllable generation: steer a pretrained model by changing the reference set it follows. We instantiate this idea in two forms. Reference-Mean Guidance is training-free: it computes a closed-form endpoint-mean correction from a reference bank and applies it to a frozen FLUX.2-klein (4B) model, enabling control of color, identity, style, and structure while keeping the prompt, seed, and weights fixed. Semi-Parametric Guidance amortizes the same idea through an explicit mean anchor and learned residual refiner, matching unconditional DiT-B/4 quality on AFHQv2 while allowing the reference set to be swapped at inference time. These results point to a broader direction: generative models that adapt through data, not parameter updates.
匹配关键词: image generation
---

[ACADEMIC - ARXIV]
标题: Qwen Goes Brrr: Off-the-Shelf RAG for Ukrainian Multi-Domain Document Understanding
作者: Anton Bazdyrev, Ivan Bashtovyi, Ivan Havlytskyi, Oleksandr Kharytonov, Artur Khodakovskyi
链接: https://arxiv.org/abs/2605.10296v1
完整摘要: We participated in the Fifth UNLP shared task on multi-domain document understanding, where systems must answer Ukrainian multiple-choice questions from PDF collections and localize the supporting document and page. We propose a retrieval-augmented pipeline built around three ideas: contextual chunking of PDFs, question-aware dense retrieval and reranking conditioned on both the question and answer options, and constrained answer generation from a small set of reranked passages. Our final system uses Qwen3-Embedding-8B for retrieval, a fine-tuned Qwen3-Reranker-8B for passage ranking, and Qwen3-32B for answer selection. On a held-out split, reranking improves Recall@1 from 0.6957 to 0.7935, while using the top-2 reranked passages raises answer accuracy from 0.9348 to 0.9674. Our best leaderboard run reached 0.9452 on the public leaderboard and 0.9598 on the private leaderboard. Our results suggest that, under strict code-competition constraints, preserving document structure and making relevance estimation aware of the answer space are more effective than adding complex downstream heuristics.
匹配关键词: image generation
---

[ACADEMIC - ARXIV]
标题: Extending Confidence-Based Text2Cypher with Grammar and Schema Aware Filtering
作者: Makbule Gulcin Ozsoy
链接: https://arxiv.org/abs/2605.10318v1
完整摘要: Large language models (LLMs) allow users to query databases using natural language by translating questions into executable queries. Despite strong progress on tasks such as Text2SQL, Text2SPARQL, and Text2Cypher, most existing methods focus on better prompting, fine-tuning, or iterative refinement. However, they often do not explicitly enforce structural constraints, such as syntactic validity and schema consistency. This can reduce reliability, since generated queries must satisfy both syntax rules and database schema constraints to be executable. In this work, we study how structured constraints can be used in test-time inference for Text2Cypher. We focus on post-generation validation to improve query correctness. We extend a confidence-based inference framework with a sequential filtering process that combines confidence scoring, grammar validation, and schema constraints before final aggregation. This lets us analyze how different constraint types affect generated queries. Our experiments with two instruction-tuned models show that grammar-based filtering improves syntactic validity. Schema-aware filtering further improves execution quality by enforcing consistency with the database structure. However, stronger filtering also increases the number of empty predictions and reduces execution coverage. Overall, we show that adding simple structural checks at test time improves the reliability of Text2Cypher generation, and we provide a clearer view of how syntax and schema constraints contribute differently.
匹配关键词: video generation
---

[ACADEMIC - ARXIV]
标题: Relations Are Channels: Knowledge Graph Embedding via Kraus Decompositions
作者: Sayan Kumar Chaki
链接: https://arxiv.org/abs/2605.10317v1
完整摘要: Knowledge graph embedding (KGE) models typically represent each relation as an operator on entity embeddings. In this work, we identify three structural axioms that any principled relation operator must satisfy, linearity, trace preservation, and complete positivity, and show that they characterize a Kraus channel structure via the Kraus representation theorem. The completeness constraint defining this family is equivalent to these axioms, providing a principled foundation rather than an externally imposed condition. Under this formulation, most existing operator-based KGE models are recoverable as special cases with Kraus rank $κ= 1$ under specific embedding choices. We further generalize this characterization to arbitrary metric geometries by introducing \mbox{w-Kraus} channels, which satisfy completeness by construction within their respective spaces. Building on this theory, we propose \textsc{KrausKGE}, a principled KGE model that naturally handles $1$-to-$N$ and $N$-to-$N$ relations, supports $k$-hop reasoning without requiring explicit path encoders, and eliminates the need for norm constraints on entity embeddings. Additionally, our framework yields the first theoretically grounded per-relation complexity measure in the KGE literature, with a provable lower bound in terms of the empirical relation matrix rank. Empirical evaluation demonstrates that \textsc{KrausKGE} consistently outperforms strong baselines on $N$-to-$N$ relations, with performance gains that increase monotonically with relation fan-out, in alignment with theoretical predictions.
匹配关键词: video generation
---

[ACADEMIC - ARXIV]
标题: Active Tabular Augmentation via Policy-Guided Diffusion Inpainting
作者: Zheyu Zhang, Shuo Yang, Bardh Prenkaj, Gjergji Kasneci
链接: https://arxiv.org/abs/2605.10315v1
完整摘要: Generative tabular augmentation is appealing in data-scarce domains, yet the prevailing focus on distributional fidelity does not reliably translate into better downstream models. We formalize a fidelity-utility gap: common generative objectives prioritize distributional plausibility, whereas augmentation succeeds only when injected samples reduce the current learner's held-out evaluation loss. This gap motivates learning not just how to generate, but what to generate and when to inject as training evolves. We propose TAP (Tabular Augmentation Policy), which couples diffusion inpainting with a lightweight, learner-conditioned policy to steer generation toward high-utility regions and controls safe injection via explicit gating and conservative windowed commitment. Under severe data scarcity, TAP consistently outperforms strong generative baselines on seven real-world datasets, improving classification accuracy by up to 15.6 percentage points and reducing regression RMSE by up to 32%.
匹配关键词: video generation
---

[ACADEMIC - ARXIV]
标题: Follow the Mean: Reference-Guided Flow Matching
作者: Pedro M. P. Curvo, Maksim Zhdanov, Floor Eijkelboom, Jan-Willem van de Meent
链接: https://arxiv.org/abs/2605.10302v1
完整摘要: Existing approaches to controllable generation typically rely on fine-tuning, auxiliary networks, or test-time search. We show that flow matching admits a different control interface: adaptation through examples. For deterministic interpolants, the velocity field is solely governed by a conditional endpoint mean; shifting this mean shifts the flow itself. This yields a simple principle for controllable generation: steer a pretrained model by changing the reference set it follows. We instantiate this idea in two forms. Reference-Mean Guidance is training-free: it computes a closed-form endpoint-mean correction from a reference bank and applies it to a frozen FLUX.2-klein (4B) model, enabling control of color, identity, style, and structure while keeping the prompt, seed, and weights fixed. Semi-Parametric Guidance amortizes the same idea through an explicit mean anchor and learned residual refiner, matching unconditional DiT-B/4 quality on AFHQv2 while allowing the reference set to be swapped at inference time. These results point to a broader direction: generative models that adapt through data, not parameter updates.
匹配关键词: video generation
---

[ACADEMIC - ARXIV]
标题: Qwen Goes Brrr: Off-the-Shelf RAG for Ukrainian Multi-Domain Document Understanding
作者: Anton Bazdyrev, Ivan Bashtovyi, Ivan Havlytskyi, Oleksandr Kharytonov, Artur Khodakovskyi
链接: https://arxiv.org/abs/2605.10296v1
完整摘要: We participated in the Fifth UNLP shared task on multi-domain document understanding, where systems must answer Ukrainian multiple-choice questions from PDF collections and localize the supporting document and page. We propose a retrieval-augmented pipeline built around three ideas: contextual chunking of PDFs, question-aware dense retrieval and reranking conditioned on both the question and answer options, and constrained answer generation from a small set of reranked passages. Our final system uses Qwen3-Embedding-8B for retrieval, a fine-tuned Qwen3-Reranker-8B for passage ranking, and Qwen3-32B for answer selection. On a held-out split, reranking improves Recall@1 from 0.6957 to 0.7935, while using the top-2 reranked passages raises answer accuracy from 0.9348 to 0.9674. Our best leaderboard run reached 0.9452 on the public leaderboard and 0.9598 on the private leaderboard. Our results suggest that, under strict code-competition constraints, preserving document structure and making relevance estimation aware of the answer space are more effective than adding complex downstream heuristics.
匹配关键词: video generation
---

[ACADEMIC - ARXIV]
标题: Relations Are Channels: Knowledge Graph Embedding via Kraus Decompositions
作者: Sayan Kumar Chaki
链接: https://arxiv.org/abs/2605.10317v1
完整摘要: Knowledge graph embedding (KGE) models typically represent each relation as an operator on entity embeddings. In this work, we identify three structural axioms that any principled relation operator must satisfy, linearity, trace preservation, and complete positivity, and show that they characterize a Kraus channel structure via the Kraus representation theorem. The completeness constraint defining this family is equivalent to these axioms, providing a principled foundation rather than an externally imposed condition. Under this formulation, most existing operator-based KGE models are recoverable as special cases with Kraus rank $κ= 1$ under specific embedding choices. We further generalize this characterization to arbitrary metric geometries by introducing \mbox{w-Kraus} channels, which satisfy completeness by construction within their respective spaces. Building on this theory, we propose \textsc{KrausKGE}, a principled KGE model that naturally handles $1$-to-$N$ and $N$-to-$N$ relations, supports $k$-hop reasoning without requiring explicit path encoders, and eliminates the need for norm constraints on entity embeddings. Additionally, our framework yields the first theoretically grounded per-relation complexity measure in the KGE literature, with a provable lower bound in terms of the empirical relation matrix rank. Empirical evaluation demonstrates that \textsc{KrausKGE} consistently outperforms strong baselines on $N$-to-$N$ relations, with performance gains that increase monotonically with relation fan-out, in alignment with theoretical predictions.
匹配关键词: visual reasoning
---

[ACADEMIC - ARXIV]
标题: MemReread: Enhancing Agentic Long-Context Reasoning via Memory-Guided Rereading
作者: Baibei Ji, Xiaoyang Weng, Juntao Li, Zecheng Tang, Yihang Lou, Min Zhang
链接: https://arxiv.org/abs/2605.10268v1
完整摘要: To tackle long-context reasoning tasks without the quadratic complexity of standard attention mechanisms, approaches based on agent memory have emerged, which typically maintain a dynamically updated memory when linearly processing document chunks. To mitigate the potential loss of latent evidence in this memorize-while-reading paradigm, recent works have integrated retrieval modules that allow agents to recall information previously discarded during memory overwriting. However, retrieval-based recall suffers from both evidence loss during memory formation and interference induced by invalid queries. To overcome these limitations, we propose MemReread. Built upon streaming reading, MemReread circumvents intermediate retrieval. It triggers question decomposition and rereading when the final memory is insufficient, enabling the recovery of indirect facts that were prematurely discarded. This design supports non-linear reasoning while preserving the inherent logical flow of document comprehension. To further enhance practicality, we introduce a reinforcement learning framework that enhances length extrapolation capability while dynamically determining the number of rereading passes based on task complexity, thereby flexibly controlling computational overhead. Extensive experiments demonstrate that MemReread consistently outperforms baseline frameworks on long-context reasoning tasks, while maintaining linear time complexity with respect to context length.
匹配关键词: visual reasoning
---

[ACADEMIC - ARXIV]
标题: IndustryBench: Probing the Industrial Knowledge Boundaries of LLMs
作者: Songlin Bai, Xintong Wang, Linlin Yu, Bin Chen, Zhiang Xu, Yuyang Sheng, Changtong Zan, Xiaofeng Zhu, Yizhe Zhang, Jiru Li, Mingze Guo, Ling Zou, Yalong Li, Chengfu Huo, Liang Ding
链接: https://arxiv.org/abs/2605.10267v1
完整摘要: In industrial procurement, an LLM answer is useful only if it survives a standards check: recommended material must match operating condition, every parameter must respect a regulated threshold, and no procedure may contradict a safety clause. Partial correctness can mask safety-critical contradictions that aggregate LLM benchmarks rarely capture. We introduce IndustryBench, a 2,049-item benchmark for industrial procurement QA in Chinese, grounded in Chinese national standards (GB/T) and structured industrial product records, organized by seven capability dimensions, ten industry categories, and panel-derived difficulty tiers, with item-aligned English, Russian, and Vietnamese renderings. Our construction pipeline rejects 70.3% of LLM-generated candidates at a search-based external-verification stage, calibrating how unreliable industrial QA remains after LLM-only filtering.Our evaluation decouples raw correctness, scored by a Qwen3-Max judge validated at $κ_w = 0.798$ against a domain expert, from a separate safety-violation (SV) check against source texts. Across 17 models in Chinese and an 8-model intersection over four languages, we find: (i) the best system reaches only 2.083 on the 0--3 rubric, leaving substantial headroom; (ii) Standards & Terminology is the most persistent capability weakness and survives item-aligned translation; (iii) extended reasoning lowers safety-adjusted scores for 12 of 13 models, primarily by introducing unsupported safety-critical details into longer final answers; and (iv) safety-violation rates reshuffle the leaderboard -- GPT-5.4 climbs from rank 6 to rank 3 after SV adjustment, while Kimi-k2.5-1T-A32B drops seven positions.Industrial LLM evaluation therefore requires source-grounded, safety-aware diagnosis rather than aggregate accuracy. We release IndustryBench with all prompts, scoring scripts, and dataset documentation.
匹配关键词: visual reasoning
---

[ACADEMIC - ARXIV]
标题: Knowledge Poisoning Attacks on Medical Multi-Modal Retrieval-Augmented Generation
作者: Peiru Yang, Haoran Zheng, Tong Ju, Shiting Wang, Wanchun Ni, Jiajun Liu, Shangguang Wang, Yongfeng Huang, Tao Qi
链接: https://arxiv.org/abs/2605.10253v1
完整摘要: Retrieval-augmented generation (RAG) is a widely adopted paradigm for enhancing LLMs in medical applications by incorporating expert multimodal knowledge during generation. However, the underlying retrieval databases may naturally contain, or be intentionally injected with, adversarial knowledge, which can perturb model outputs and undermine system reliability. To investigate this risk, prior studies have explored knowledge poisoning attacks in medical RAG systems. Nevertheless, most of them rely on the strong assumption that adversaries possess prior knowledge of user queries, which is unrealistic in deployments and substantially limits their practical applicability. In this paper, we propose M\textsuperscript{3}Att, a knowledge-poisoning framework designed for medical multimodal RAG systems, assuming only limited distribution knowledge of the underlying database. Our core idea is to inject covert misinformation into textual data while using paired visual data as a query-agnostic trigger to promote retrieval. We first propose a unified framework that introduces imperceptible perturbations to visual inputs to manipulate retrieval probabilities. Besides, due to the prior medical knowledge in LLMs, naively poisoned medical content with explicit factual errors can be corrected during generation. Thus, we leverage the inherent ambiguity of medical diagnosis and design a covert misinformation injection strategy that degrades diagnostic accuracy while evading model self-correction. Experiments on five LLMs and datasets demonstrate that M\textsuperscript{3}Att consistently produces clinically plausible yet incorrect generations. Codes: https://github.com/ypr17/M3Att.
匹配关键词: visual reasoning
---

[ACADEMIC - ARXIV]
标题: Efficient Hybrid CNN-GNN Architecture for Monocular Depth Estimation
作者: Ishan Narayan
链接: https://arxiv.org/abs/2605.10251v1
完整摘要: We present GraphDepth, a monocular depth estimation architecture that synergistically integrates Graph Neural Networks (GNNs) within a convolutional encoder-decoder framework. Our approach embeds efficient GraphSAGE layers at multiple scales of a ResNet-101 U-Net backbone, enabling explicit modeling of long-range spatial relationships that lie beyond the receptive field of local convolutions. Key technical contributions include: (1) batch-parallelized graph construction with configurable k-NN and grid-based adjacency for scalable training; (2) multi-scale GraphSAGE integration at bottleneck and decoder stages (1/32, 1/16, 1/8 resolution) to propagate global context throughout the feature hierarchy; (3) channel-attention gated skip connections that adaptively weight encoder features before fusion; and (4) heteroscedastic uncertainty estimation via a dedicated aleatoric uncertainty head, enabling confidence-aware loss weighting during optimization. Unlike transformer-based hybrids, which suffer from quadratic complexity in sequence length, GraphDepth scales linearly with spatial resolution while achieving comparable global receptive fields through iterative message passing. Experiments on NYU Depth V2, WHU Aerial, ETH3D, and Mid-Air benchmarks demonstrate competitive accuracy within 4.6\% of state-of-the-art transformers on indoor scenes with substantially lower computational cost (25 FPS vs 9 FPS, 3.8 GB vs 8.8 GB VRAM). GraphDepth achieves the best reported result on WHU Aerial (RMSE 8.24 m) and exhibits superior zero-shot cross-domain transfer to the Mid-Air synthetic aerial dataset, validating the generalization power of explicit relational reasoning for depth estimation.
匹配关键词: visual reasoning
---

[ACADEMIC - ARXIV]
标题: Positive Alignment: Artificial Intelligence for Human Flourishing
作者: Ruben Laukkonen, Seb Krier, Chloé Bakalar, Shamil Chandaria, Morten Kringelbach, Adam Elwood, Daniel Ford, Fernando Rosas, Maty Bohacek, Matija Franklin, Nenad Tomašev, Stephanie Chan, Verena Rieser, Roma Patel, Michael Levin, Arun Rao
链接: https://arxiv.org/abs/2605.10310v1
完整摘要: Existing alignment research is dominated by concerns about safety and preventing harm: safeguards, controllability, and compliance. This paradigm of alignment parallels early psychology's focus on mental illness: necessary but incomplete. What we call Positive Alignment is the development of AI systems that (i) actively support human and ecological flourishing in a pluralistic, polycentric, context-sensitive, and user-authored way while (ii) remaining safe and cooperative. It is a distinct and necessary agenda within AI alignment research. We argue that several existing failures of alignment (e.g., engagement hacking, loss of human autonomy, failures in truth-seeking, low epistemic humility, error correction, lack of diverse viewpoints, and being primarily reactive rather than proactive) may be better addressed through positive alignment, including cultivating virtues and maximizing human flourishing. We highlight a range of challenges, open questions, and technical directions (e.g., data filtering and upsampling, pre- and post-training, evaluations, collaborative value collection) for different phases of the LLM and agents lifecycle. We end with design principles for promoting disagreement and decentralization through contextual grounding, community customization, continual adaptation, and polycentric governance; that is, many legitimate centers of oversight rather than one institutional or moral chokepoint.
匹配关键词: embodied AI
---

[ACADEMIC - ARXIV]
标题: Generative AI Fuels Solo Entrepreneurship, but Teams Still Lead at the Top
作者: Hyunso Kim, Hyo Kang, Jaeyong Song
链接: https://arxiv.org/abs/2605.10291v1
完整摘要: Recent advances in generative artificial intelligence (AI) are reshaping who enters entrepreneurship, but not who reaches the top of the quality distribution. Using data on over 160,000 product launches on Product Hunt, we find that entrepreneurial entry increased sharply following the public release of ChatGPT-3.5, driven disproportionately by solo entrepreneurs. This shift toward solo entry is particularly pronounced in categories that historically favored team-based ventures. However, much of this growth reflects low-commitment, experimental entry and does not translate into greater representation among the highest-quality outcomes. Team-based ventures are increasingly dominant in the top tiers of platform rankings. These findings suggest that generative AI lowers barriers to solo entrepreneurship while reinforcing team-based advantages.
匹配关键词: embodied AI
---

[ACADEMIC - ARXIV]
标题: DeepLog: A Software Framework for Modular Neurosymbolic AI
作者: Robin Manhaeve, Stefano Colamonaco, Vincent Derkinderen, Rik Adriaensen, Lucas Van Praet, Luc De Raedt, Giuseppe Marra
链接: https://arxiv.org/abs/2605.10279v1
完整摘要: DeepLog is an operational neurosymbolic framework that unifies logic and deep learning within standard PyTorch workflows. While existing neurosymbolic systems focus on a particular paradigm and semantics, DeepLog serves as a universal backend that can emulate many systems in the neurosymbolic alphabet soup. By treating diverse neurosymbolic languages as high-level specifications, the DeepLog software automatically compiles them into optimized arithmetic circuits. This design lowers the barrier for machine learning practitioners by treating logic as composable modules, while providing neurosymbolic developers with a shared, high-performance basis for prototyping new integration strategies. The code is available here: https://github.com/ML-KULeuven/deeplog
匹配关键词: embodied AI
---

[ACADEMIC - ARXIV]
标题: SciIntegrity-Bench: A Benchmark for Evaluating Academic Integrity in AI Scientist Systems
作者: Zonglin Yang, Xingtong Liu, Xinyan Xu
链接: https://arxiv.org/abs/2605.10246v1
完整摘要: AI scientist systems are increasingly deployed for autonomous research, yet their academic integrity has never been systematically evaluated. We introduce SCIINTEGRITY-BENCH, the first benchmark designed around a dilemmatic evaluation paradigm: each of its 33 scenarios across 11 trap categories is constructed so that honest acknowledgment of failure is the only correct response, while task completion requires misconduct. Across 231 evaluation runs spanning 7 state-of-the-art LLMs, the overall integrity problem rate reaches 34.2%, and no model achieves zero failures. Most strikingly, across missing-data scenarios, all seven models generate synthetic data rather than acknowledging infeasibility, differing only in whether they disclose the substitution. A further prompt ablation study separates two drivers: removing explicit completion pressure sharply reduces undisclosed fabrication from 20.6% to 3.2%, while the underlying synthesis rate remains unchanged, revealing an intrinsic completion bias that persists independent of prompt-level instructions. These findings point to the absence of honest refusal as a trained disposition as the primary driver of observed failures. We release SCIINTEGRITY-BENCH at https://github.com/liuxingtong/Sci-Integrity-Bench.
匹配关键词: embodied AI
---

[ACADEMIC - ARXIV]
标题: Hypothesis-Driven Deep Research with Large Language Models: A Structured Methodology for Automated Knowledge Discovery
作者: Michael Chin
链接: https://arxiv.org/abs/2605.10224v1
完整摘要: Current AI-powered research systems adopt a direct search-then-summarize paradigm that treats hypotheses as end products of scientific discovery. We argue this leaves a critical gap: hypotheses can serve a far more powerful role as organizational instruments that structure the research process itself. We propose the Hypothesis-Driven Deep Research (HDRI) methodology - the first framework using hypotheses to organize general-purpose deep research across arbitrary domains, rather than merely validating claims within specific domains. This transforms research from reactive information retrieval into proactive, verifiable, and iterative knowledge discovery. HDRI is formalized with six core principles and an eight-stage pipeline. A central innovation is the gap-driven iterative research mechanism - a closed-loop quality assurance system that automatically identifies informational and logical gaps, triggering targeted supplementary investigation. We further introduce a fact reasoning framework with traceable reasoning chains and quantified confidence propagation, a subject locking mechanism to prevent entity confusion, and a multi-dimensional quality assessment scheme. The methodology is realized in the INFOMINER system. Experiments demonstrate improvements of 22.4% in fact density, 90% subject matching accuracy, 0.92 multi-source verification confidence, and 14% completeness gain from gap-driven supplementation. Five case studies validate its practical applicability, achieving an average quality rating of 4.46/5.0.
匹配关键词: embodied AI
---

[ACADEMIC - ARXIV]
标题: PaMoSplat: Part-Aware Motion-Guided Gaussian Splatting for Dynamic Scene Reconstruction
作者: Yinan Deng, Jianyu Dou, Jiahui Wang, Jingyu Zhao, Yi Yang, Yufeng Yue
链接: https://arxiv.org/abs/2605.10307v1
完整摘要: Dynamic scene reconstruction represents a fundamental yet demanding challenge in computer vision and robotics. While recent progress in 3DGS-based methods has advanced dynamic scene modeling, obtaining high-fidelity rendering and accurate tracking in scenarios with substantial, intricate motions remains significantly challenging. To address these challenges, we propose PaMoSplat, a novel dynamic Gaussian splatting framework incorporating part awareness and motion priors. Our approach is grounded in two key observations: 1) Parts serve as primitives for scene deformation, and 2) Motion cues from optical flow can effectively guide part motion. Specifically, PaMoSplat initializes by lifting multi-view segmentation masks into 3D space via graph clustering, establishing coherent Gaussian parts. For subsequent timestamps, we leverage a differential evolutionary algorithm to estimate the rigid motion of these parts using multi-view optical flow cues, providing a robust warm-start for further optimization. Additionally, PaMoSplat introduces an adaptive iteration count mechanism, internal learnable rigidity, and flow-supervised rendering loss to accelerate and optimize the training process. Comprehensive evaluations across diverse scenes, including real-world environments, demonstrate that PaMoSplat delivers superior rendering quality, improved tracking precision, and faster convergence compared to existing methods. Furthermore, it enables multiple part-level downstream applications, such as 4D scene editing.
匹配关键词: robotics
---

[ACADEMIC - ARXIV]
标题: Increasing the Efficiency of DETR for Maritime High-Resolution Images
作者: Tinsae Yehuala, Hao Cheng, Ville Lehtola
链接: https://arxiv.org/abs/2605.10269v1
完整摘要: Maritime object detection is critical for the safe navigation of unmanned surface vessels (USVs), requiring accurate recognition of obstacles from small buoys to large vessels. Real-time detection is challenging due to long distances, small object sizes, large-scale variations, edge computing limitations, and the high memory demands of high-resolution imagery. Existing solutions, such as downsampling or image splitting, often reduce accuracy or require additional processing, while memory-efficient models typically handle only limited resolutions. To overcome these limitations, we leverage Vision Mamba (ViM) backbones, which build on State Space Models (SSMs) to capture long-range dependencies while scaling linearly with sequence length. Images are tokenized into sequences for efficient high-resolution processing. For further computational efficiency, we design a tailored Feature Pyramid Network with successive downsampling and SSM layers, as well as token pruning to reduce unnecessary computation on background regions. Compared to state-of-the-art methods like RT-DETR with ResNet50 backbone, our approach achieves a better balance between performance and computational efficiency in maritime object detection.
匹配关键词: robotics
---

[ACADEMIC - ARXIV]
标题: Nano-U: Efficient Terrain Segmentation for Tiny Robot Navigation
作者: Federico Pizzolato, Francesco Pasti, Nicola Bellotto
链接: https://arxiv.org/abs/2605.10210v1
完整摘要: Terrain segmentation is a fundamental capability for autonomous mobile robots operating in unstructured outdoor environments. However, state-of-the-art models are incompatible with the memory and compute constraints typical of microcontrollers, limiting scalable deployment in small robotics platforms. To address this gap, we develop a complete framework for robust binary terrain segmentation on a low-cost microcontroller. At the core of our approach we design Nano-U, a highly compact binary segmentation network with a few thousand parameters. To compensate for the network's minimal capacity, we train Nano-U via Quantization-Aware Distillation (QAD), combining knowledge distillation and quantization-aware training. This allows the final quantized model to achieve excellent results on the Botanic Garden dataset and to perform very well on TinyAgri, a custom agricultural field dataset with more challenging scenes. We deploy the quantized Nano-U on a commodity microcontroller by extending MicroFlow, a compiler-based inference engine for TinyML implemented in Rust. By eliminating interpreter overhead and dynamic memory allocation, the quantized model executes on an ESP32-S3 with a minimal memory footprint and low latency. This compiler-based execution demonstrates a viable and energy-efficient solution for perception on low-cost robotic platforms.
匹配关键词: robotics
---

[ACADEMIC - ARXIV]
标题: HeteroGenManip: Generalizable Manipulation For Heterogeneous Object Interactions
作者: Zhenhao Shen, Zeming Yang, Yue Chen, Yuran Wang, Shengqiang Xu, Mingleyang Li, Hao Dong, Ruihai Wu
链接: https://arxiv.org/abs/2605.10201v1
完整摘要: Generalizable manipulation involving cross-type object interactions is a critical yet challenging capability in robotics. To reliably accomplish such tasks, robots must address two fundamental challenges: ``where to manipulate'' (contact point localization) and ``how to manipulate'' (subsequent interaction trajectory planning). Existing foundation-model-based approaches often adopt end-to-end learning that obscures the distinction between these stages, exacerbating error accumulation in long-horizon tasks. Furthermore, they typically rely on a single uniform model, which fails to capture the diverse, category-specific features required for heterogeneous objects. To overcome these limitations, we propose HeteroGenManip, a task-conditioned, two-stage framework designed to decouple initial grasp from complex interaction execution. First, Foundation-Correspondence-Guided Grasp module leverages structural priors to align the initial contact state, thereby significantly reducing the pose uncertainty of grasping. Subsequently, Multi-Foundation-Model Diffusion Policy (MFMDP) routes objects to category-specialized foundation models, integrating fine-grained geometric information with highly-variable part features via a dual-stream cross-attention mechanism. Experimental evaluations demonstrate that HeteroGenManip achieves robust intra-category shape and pose generalization. The framework achieves an average 31\% performance improvement in simulation tasks with broad type setting, alongside a 36.7\% gain across four real-world tasks with different interaction types.
匹配关键词: robotics
---

[ACADEMIC - ARXIV]
标题: MTA-RL: Robust Urban Driving via Multi-modal Transformer-based 3D Affordances and Reinforcement Learning
作者: Guangli Chen, Dianzhao Li, Wenjian Zhong, Bangquan Xie, Ostap Okhrin
链接: https://arxiv.org/abs/2605.10177v1
完整摘要: Robust urban autonomous driving requires reliable 3D scene understanding and stable decision-making under dense interactions. However, existing end-to-end models lack interpretability, while modular pipelines suffer from error propagation across brittle interfaces. This paper proposes MTA-RL, the first framework that bridges perception and control through Multi-modal Transformer-based 3D Affordances and Reinforcement Learning (RL). Unlike previous fusion models that directly regress actions, RGB images and LiDAR point clouds are fused using a transformer architecture to predict explicit, geometry-aware affordance representations. These structured representations serve as a compact observation space, enabling the RL policy to operate purely on predicted driving semantics, which significantly improves sample efficiency and stability. Extensive evaluations in CARLA Town01-03 across varying densities (20-60 background vehicles) show that MTA-RL consistently outperforms state-of-the-art baselines. Trained solely on Town03, our method demonstrates superior zero-shot generalization in unseen towns, achieving up to a 9.0% increase in Route Completion, an 11.0% increase in Total Distance, and an 83.7% improvement in Distance Per Violation. Furthermore, ablation studies confirm that our multi-modal fusion and reward shaping are critical, significantly outperforming image-only and unshaped variants, demonstrating the effectiveness of MTA-RL for robust urban autonomous driving.
匹配关键词: robotics
---

[ACADEMIC - ARXIV]
标题: PaMoSplat: Part-Aware Motion-Guided Gaussian Splatting for Dynamic Scene Reconstruction
作者: Yinan Deng, Jianyu Dou, Jiahui Wang, Jingyu Zhao, Yi Yang, Yufeng Yue
链接: https://arxiv.org/abs/2605.10307v1
完整摘要: Dynamic scene reconstruction represents a fundamental yet demanding challenge in computer vision and robotics. While recent progress in 3DGS-based methods has advanced dynamic scene modeling, obtaining high-fidelity rendering and accurate tracking in scenarios with substantial, intricate motions remains significantly challenging. To address these challenges, we propose PaMoSplat, a novel dynamic Gaussian splatting framework incorporating part awareness and motion priors. Our approach is grounded in two key observations: 1) Parts serve as primitives for scene deformation, and 2) Motion cues from optical flow can effectively guide part motion. Specifically, PaMoSplat initializes by lifting multi-view segmentation masks into 3D space via graph clustering, establishing coherent Gaussian parts. For subsequent timestamps, we leverage a differential evolutionary algorithm to estimate the rigid motion of these parts using multi-view optical flow cues, providing a robust warm-start for further optimization. Additionally, PaMoSplat introduces an adaptive iteration count mechanism, internal learnable rigidity, and flow-supervised rendering loss to accelerate and optimize the training process. Comprehensive evaluations across diverse scenes, including real-world environments, demonstrate that PaMoSplat delivers superior rendering quality, improved tracking precision, and faster convergence compared to existing methods. Furthermore, it enables multiple part-level downstream applications, such as 4D scene editing.
匹配关键词: humanoid robot
---

[ACADEMIC - ARXIV]
标题: Nano-U: Efficient Terrain Segmentation for Tiny Robot Navigation
作者: Federico Pizzolato, Francesco Pasti, Nicola Bellotto
链接: https://arxiv.org/abs/2605.10210v1
完整摘要: Terrain segmentation is a fundamental capability for autonomous mobile robots operating in unstructured outdoor environments. However, state-of-the-art models are incompatible with the memory and compute constraints typical of microcontrollers, limiting scalable deployment in small robotics platforms. To address this gap, we develop a complete framework for robust binary terrain segmentation on a low-cost microcontroller. At the core of our approach we design Nano-U, a highly compact binary segmentation network with a few thousand parameters. To compensate for the network's minimal capacity, we train Nano-U via Quantization-Aware Distillation (QAD), combining knowledge distillation and quantization-aware training. This allows the final quantized model to achieve excellent results on the Botanic Garden dataset and to perform very well on TinyAgri, a custom agricultural field dataset with more challenging scenes. We deploy the quantized Nano-U on a commodity microcontroller by extending MicroFlow, a compiler-based inference engine for TinyML implemented in Rust. By eliminating interpreter overhead and dynamic memory allocation, the quantized model executes on an ESP32-S3 with a minimal memory footprint and low latency. This compiler-based execution demonstrates a viable and energy-efficient solution for perception on low-cost robotic platforms.
匹配关键词: humanoid robot
---

[ACADEMIC - ARXIV]
标题: HeteroGenManip: Generalizable Manipulation For Heterogeneous Object Interactions
作者: Zhenhao Shen, Zeming Yang, Yue Chen, Yuran Wang, Shengqiang Xu, Mingleyang Li, Hao Dong, Ruihai Wu
链接: https://arxiv.org/abs/2605.10201v1
完整摘要: Generalizable manipulation involving cross-type object interactions is a critical yet challenging capability in robotics. To reliably accomplish such tasks, robots must address two fundamental challenges: ``where to manipulate'' (contact point localization) and ``how to manipulate'' (subsequent interaction trajectory planning). Existing foundation-model-based approaches often adopt end-to-end learning that obscures the distinction between these stages, exacerbating error accumulation in long-horizon tasks. Furthermore, they typically rely on a single uniform model, which fails to capture the diverse, category-specific features required for heterogeneous objects. To overcome these limitations, we propose HeteroGenManip, a task-conditioned, two-stage framework designed to decouple initial grasp from complex interaction execution. First, Foundation-Correspondence-Guided Grasp module leverages structural priors to align the initial contact state, thereby significantly reducing the pose uncertainty of grasping. Subsequently, Multi-Foundation-Model Diffusion Policy (MFMDP) routes objects to category-specialized foundation models, integrating fine-grained geometric information with highly-variable part features via a dual-stream cross-attention mechanism. Experimental evaluations demonstrate that HeteroGenManip achieves robust intra-category shape and pose generalization. The framework achieves an average 31\% performance improvement in simulation tasks with broad type setting, alongside a 36.7\% gain across four real-world tasks with different interaction types.
匹配关键词: humanoid robot
---

[ACADEMIC - ARXIV]
标题: Data-Asymmetric Latent Imagination and Reranking for 3D Robotic Imitation Learning
作者: Lianghao Luo, Xizhou Bu, Ruyan Liu, Qingqiu Huang, Chufeng Tang, Xiaoshuai Hao, Hongbo Wang, Wei Li
链接: https://arxiv.org/abs/2605.10166v1
完整摘要: Robotic imitation learning typically assumes access to optimal demonstrations, yet real-world data collection often yields suboptimal, exploratory, or even failed trajectories. Discarding such data wastes valuable information about environment dynamics and failure modes, which can instead be leveraged to improve decision-making. While 3D policies reduce reliance on high-quality demonstrations through strong spatial generalization, they still require large-scale data to achieve high task success. To address this, we propose DALI-R, a Data-Asymmetric Latent Imagination and Reranking framework for 3D robotic imitation learning from mixed-quality trajectories. It learns a Latent World Model over 3D point clouds for imagined rollouts and a Task Completion Scorer that reranks candidate action chunks, improving decision-making without additional high-quality demonstrations. We instantiate DALI-R with both diffusion and efficient flow-matching policies and evaluate it on Adroit and MetaWorld benchmarks. Across the two evaluated 3D base policies, DALI-R achieves an average $6.8$\% improvement in success rate while incurring less than $0.7\times$ additional inference overhead.
匹配关键词: humanoid robot
---

[ACADEMIC - ARXIV]
标题: Plan in Sandbox, Navigate in Open Worlds: Learning Physics-Grounded Abstracted Experience for Embodied Navigation
作者: Zhixuan Shen, Jiawei Du, Ziyu Guo, Han Luo, Lilan Peng, Joey Tianyi Zhou, Haonan Luo, Tianrui Li
链接: https://arxiv.org/abs/2605.10118v1
完整摘要: Vision-Language Models (VLMs) have demonstrated exceptional general reasoning capabilities. However, their performance in embodied navigation remains hindered by a scarcity of aligned open-world vision and robot control data. Despite simulators providing a cost-effective alternative for data collection, the inherent reliance on photorealistic simulations often limits the transferability of learned policies. To this end, we propose \textit{\textbf{S}andbox-\textbf{A}bstracted \textbf{G}rounded \textbf{E}xperience} (\textbf{\textit{SAGE}}), a framework that enables agents to learn within a physics-grounded semantic abstraction rather than a photorealistic simulation, mimicking the human capacity for mental simulation where plans are rehearsed in simplified physics abstractions before execution. \textit{SAGE} system operates via three synergistic phases: (1) \textit{Genesis}: constructing diverse, physics-constrained semantic environments to bootstrap experience; (2) \textit{Evolution}: distilling experiences through Reinforcement Learning (RL), utilizing a novel asymmetric adaptive clipping mechanism to stabilize updates; (3) \textit{Navigation}: bridging the abstract policy to open-world control. We demonstrate that \textit{SAGE} significantly improves planner-assisted embodied navigation, achieving a 53.21\% LLM-Match Success Rate on A-EQA (+9.7\% over baseline), while showing encouraging transfer to physical indoor robot deployment.
匹配关键词: humanoid robot
---

[ACADEMIC - ARXIV]
标题: Knowledge Poisoning Attacks on Medical Multi-Modal Retrieval-Augmented Generation
作者: Peiru Yang, Haoran Zheng, Tong Ju, Shiting Wang, Wanchun Ni, Jiajun Liu, Shangguang Wang, Yongfeng Huang, Tao Qi
链接: https://arxiv.org/abs/2605.10253v1
完整摘要: Retrieval-augmented generation (RAG) is a widely adopted paradigm for enhancing LLMs in medical applications by incorporating expert multimodal knowledge during generation. However, the underlying retrieval databases may naturally contain, or be intentionally injected with, adversarial knowledge, which can perturb model outputs and undermine system reliability. To investigate this risk, prior studies have explored knowledge poisoning attacks in medical RAG systems. Nevertheless, most of them rely on the strong assumption that adversaries possess prior knowledge of user queries, which is unrealistic in deployments and substantially limits their practical applicability. In this paper, we propose M\textsuperscript{3}Att, a knowledge-poisoning framework designed for medical multimodal RAG systems, assuming only limited distribution knowledge of the underlying database. Our core idea is to inject covert misinformation into textual data while using paired visual data as a query-agnostic trigger to promote retrieval. We first propose a unified framework that introduces imperceptible perturbations to visual inputs to manipulate retrieval probabilities. Besides, due to the prior medical knowledge in LLMs, naively poisoned medical content with explicit factual errors can be corrected during generation. Thus, we leverage the inherent ambiguity of medical diagnosis and design a covert misinformation injection strategy that degrades diagnostic accuracy while evading model self-correction. Experiments on five LLMs and datasets demonstrate that M\textsuperscript{3}Att consistently produces clinically plausible yet incorrect generations. Codes: https://github.com/ypr17/M3Att.
匹配关键词: manipulation
---

[ACADEMIC - ARXIV]
标题: Polyphonia: Zero-Shot Timbre Transfer in Polyphonic Music with Acoustic-Informed Attention Calibration
作者: Haowen Li, Tianxiang Li, Yi Yang, Boyu Cao, Qi Liu
链接: https://arxiv.org/abs/2605.10203v1
完整摘要: The advancement of diffusion-based text-to-music generation has opened new avenues for zero-shot music editing. However, existing methods fail to achieve stem-specific timbre transfer, which requires altering specific stems while strictly preserving the background accompaniment. This limitation severely hinders practical application, since real-world production necessitates precise manipulation of components within dense mixtures. Our key finding is that, while vanilla cross-attention captures semantic features of stems, it lacks the spectral resolution to strictly localize targets in dense mixtures, leading to boundary leakage. To resolve this dilemma, we propose Polyphonia, a zero-shot editing framework with Acoustic-Informed Attention Calibration. Rather than relying solely on diffuse semantic attention, Polyphonia leverages a probabilistic acoustic prior to establish coarse boundaries, enabling non-target stems preserved precise semantic synthesis. For evaluation, we propose PolyEvalPrompts, a standardized prompt set with 1,170 timbre transfer tasks in polyphonic music. Specifically, Polyphonia achieves an increase of 15.5% in target alignment compared to baselines, while maintaining competitive music fidelity and non-target integrity.
匹配关键词: manipulation
---

[ACADEMIC - ARXIV]
标题: HeteroGenManip: Generalizable Manipulation For Heterogeneous Object Interactions
作者: Zhenhao Shen, Zeming Yang, Yue Chen, Yuran Wang, Shengqiang Xu, Mingleyang Li, Hao Dong, Ruihai Wu
链接: https://arxiv.org/abs/2605.10201v1
完整摘要: Generalizable manipulation involving cross-type object interactions is a critical yet challenging capability in robotics. To reliably accomplish such tasks, robots must address two fundamental challenges: ``where to manipulate'' (contact point localization) and ``how to manipulate'' (subsequent interaction trajectory planning). Existing foundation-model-based approaches often adopt end-to-end learning that obscures the distinction between these stages, exacerbating error accumulation in long-horizon tasks. Furthermore, they typically rely on a single uniform model, which fails to capture the diverse, category-specific features required for heterogeneous objects. To overcome these limitations, we propose HeteroGenManip, a task-conditioned, two-stage framework designed to decouple initial grasp from complex interaction execution. First, Foundation-Correspondence-Guided Grasp module leverages structural priors to align the initial contact state, thereby significantly reducing the pose uncertainty of grasping. Subsequently, Multi-Foundation-Model Diffusion Policy (MFMDP) routes objects to category-specialized foundation models, integrating fine-grained geometric information with highly-variable part features via a dual-stream cross-attention mechanism. Experimental evaluations demonstrate that HeteroGenManip achieves robust intra-category shape and pose generalization. The framework achieves an average 31\% performance improvement in simulation tasks with broad type setting, alongside a 36.7\% gain across four real-world tasks with different interaction types.
匹配关键词: manipulation
---

[ACADEMIC - ARXIV]
标题: When Prompts Become Payloads: A Framework for Mitigating SQL Injection Attacks in Large Language Model-Driven Applications
作者: Farzad Nourmohammadzadeh Motlagh, Mehrdad Hajizadeh, Mehryar Majd, Pejman Najafi, Feng Cheng, Christoph Meinel
链接: https://arxiv.org/abs/2605.10176v1
完整摘要: Natural language interfaces to structured databases are becoming increasingly common, largely due to advances in large language models (LLMs) that enable users to query data using conversational input rather than formal query languages such as SQL. While this paradigm significantly improves usability and accessibility, it introduces new security risks, particularly the amplification of SQL injection vulnerabilities through the prompt-to-SQL translation process. Malicious users can exploit these mechanisms by crafting adversarial prompts that manipulate model behavior and generate unsafe queries. In this work, we propose a multi-layered security framework designed to detect and mitigate LLM-mediated SQL injection attacks. The framework integrates a front-end security shield for prompt sanitization, an advanced threat detection model for behavioral and semantic anomaly identification, and a signature-based control layer for known attack patterns. We evaluate the proposed framework under diverse and realistic attack scenarios, including prompt injection, obfuscated SQL payloads, and context-manipulation attacks. To ensure robustness, we generate and curate a comprehensive benchmark dataset of adversarial prompts and assess performance across a fine-tuned LLM configuration. Experimental results demonstrate that the proposed approach achieves high detection accuracy while maintaining low false-positive rates, significantly improving the secure deployment of LLM-powered database applications.
匹配关键词: manipulation
---

[ACADEMIC - ARXIV]
标题: Retrieve-then-Steer: Online Success Memory for Test-Time Adaptation of Generative VLAs
作者: Jianchao Zhao, Huoren Yang, Hu Yusong, Yuyang Gao, Qiguan Ou, Cong Wan, SongLin Dong, Zhiheng Ma, Yihong Gong
链接: https://arxiv.org/abs/2605.10094v1
完整摘要: Vision-Language-Action (VLA) models show strong potential for general-purpose robotic manipulation, yet their closed-loop reliability often degrades under local deployment conditions. Existing evaluations typically treat test episodes as independent zero-shot trials. However, real robots often operate repeatedly in the same or slowly changing environments, where successful executions provide environment-verified evidence of reliable behavior patterns. We study this persistent-deployment setting, asking whether a partially competent frozen VLA can improve its reliability by reusing its successful test-time experience. We propose an online success-memory guided test-time adaptation framework for generative VLAs. During deployment, the robot stores progress-calibrated successful observation-action segments in a long-term memory. At inference, it retrieves state-relevant action chunks, filters inconsistent candidates via trajectory-level consistency, and aggregates them into an elite action prior. To incorporate this prior into action generation, we introduce confidence-adaptive prior guidance, which injects the elite prior into an intermediate state of the flow-matching action sampler and adjusts the guidance strength based on retrieval confidence. This design allows the frozen VLA to exploit environment-specific successful experience while preserving observation-conditioned generative refinement. This retrieve-then-steer mechanism enables lightweight, non-parametric test-time adaptation without requiring parameter updates. Simulation and real-world experiments show improved task success and closed-loop stability, especially in long-horizon and multi-stage tasks.
匹配关键词: manipulation
---

[ACADEMIC - ARXIV]
标题: Zero-Shot Sim-to-Real Robot Learning: A Dexterous Manipulation Study on Reactive Catching
作者: Kejia Ren, Gaotian Wang, Andrew S. Morgan, Kaiyu Hang
链接: https://arxiv.org/abs/2605.09789v1
完整摘要: Dexterous manipulation is physics-intensive and highly sensitive to modeling errors and perception noise, making sim-to-real transfer prohibitively challenging. Domain randomization (DR) is commonly used to improve the robustness of learned policies for such tasks, but conventional DR randomizes one instance per episode, offering very limited exposure to the variability of real-world dynamics. To this end, we propose Domain-Randomized Instance Set (DRIS), which represents and propagates a set of randomized instances simultaneously, providing richer approximation of uncertain dynamics and enabling policies to learn actions that account for multiple possible outcomes. Supported by theoretical analysis, we show that DRIS yields more robust policies and alleviates the need for real-world fine-tuning, even with a modest number of instances (e.g., 10). We demonstrate this on a challenging reactive catching task. Unlike traditional catching setups that use end-effectors designed to mechanically stabilize the object (e.g., curved or enclosing surfaces), our system uses a flat plate that offers no passive stabilization, making the task highly sensitive to noise and requiring rapid reactive motions. The learned policies exhibit strong robustness to uncertainties and achieve reliable zero-shot sim-to-real transfer.
匹配关键词: sim-to-real
---

[ACADEMIC - ARXIV]
标题: MC$^2$: Monte Carlo Correction for Fast Elliptic PDE Solving
作者: Ethan Hsu, Hong Meng Yam, Ivan Ge
链接: https://arxiv.org/abs/2605.09288v1
完整摘要: Partial differential equation (PDE) solvers underpin scientific computing, but real-world deployment is bounded by compute. Classical Monte Carlo solvers such as Walk-on-Spheres (WoS) are unbiased and geometry-agnostic but are slow. Learned solvers are fast but biased and brittle under distribution shift. We present \textbf{MC$^2$}, a hybrid WoS-Neural Network (WoS-NN) PDE solver that treats a low-budget Monte Carlo solution as a structured estimator of the true field and learns a single-pass neural correction to recover a high-fidelity solution. MC$^2$ matches the accuracy of solutions using over $1000\times$ more Monte Carlo compute, outperforming all evaluated classical, denoising, and neural-operator baselines. To enable reproducible study of finite-compute PDE solving, we additionally release \textbf{PDEZoo}, the largest standardized elliptic PDE benchmark to date: 2M PDEs spanning five elliptic families and unlimited geometric compositions, with analytic ground truth and multi-budget Monte Carlo trajectories. Together \textbf{MC$^2$} and \textbf{PDEZoo} (1) empirically establish that finite-sample Monte Carlo error is structured, learnable, and correctable in a single forward pass, (2) show that we can solve PDEs $\sim$\textbf{1000x} faster than with just WoS, and (3) provide the evaluation infrastructure the field has so far lacked.
匹配关键词: sim-to-real
---

[ACADEMIC - ARXIV]
标题: CAGS: Color-Adaptive Volumetric Video Streaming with Dynamic 3D Gaussian Splatting
作者: Daheng Yin, Yili Jin, Jianxin Shi, Isaac Ding, Miao Zhang, Fangxin Wang, Zhaowu Huang, Cong Zhang, Jiangchuan Liu, Fang Dong
链接: https://arxiv.org/abs/2605.09279v1
完整摘要: Volumetric video (VV) streaming enables real-time, immersive access to remote 3D environments, powering telepresence, ecological monitoring, and robotic teleoperation. These applications turn VV streaming into a real-time interface to remote physical environments, imposing new system-level demands for photorealistic scene representation, low-latency interaction, and robust performance under heterogeneous networks. 3D Gaussian Splatting (3DGS) has been widely used for real-time photorealistic rendering, offering superior visual quality and rendering performance, but it faces challenges due to bandwidth consumption. Furthermore, as the foundation of adaptive VV streaming, existing Levels of Detail (LoD) methods based on density are not well-suited to Gaussian representations, leading to visible gaps and severe quality degradation. Recent studies have also explored attribute compression techniques to reduce bandwidth consumption. Our preliminary studies reveal that aggressive attribute compression primarily causes color distortion, which can be effectively corrected in the rendered image using a reference image. Motivated by these findings, we propose a novel Color-Adaptive scheme for adaptive VV streaming that uses vector quantization (VQ) to establish LoDs and correct color distortions with low-resolution reference images. We further present CAGS, an adaptive VV streaming system compatible with diverse Gaussian representations, which integrates the Color-Adaptive scheme by rendering reference images on the streaming server and performing color restoration on the client. Extensive experiments on our prototype system demonstrate that CAGS outperforms the existing adaptive streaming systems in PSNR by 5$\sim$20 dB under fluctuating bandwidth, operates significantly faster than existing scalable Gaussian compression methods, and generalizes across different Gaussian representations.
匹配关键词: sim-to-real
---

[ACADEMIC - ARXIV]
标题: Towards Robust Sequential Decomposition for Complex Image Editing
作者: Zilai Zeng, Mingdeng Cao, Zijie Li, Xiaochen Lian, Yichun Shi, Peihao Zhu, Chen Sun, Peng Wang
链接: https://arxiv.org/abs/2605.09233v1
完整摘要: Recent advances in visual generative models have enabled high-fidelity image editing guided by human instructions. However, these models often struggle with complex instructions involving combinatorial editing operations or inter-step dependencies. This difficulty stems from the limitations of two canonical paradigms: (1) single-turn editing, which attempts to apply all instructed edits in one pass, often fails to parse the complex instruction accurately and causes undesired edits; and (2) sequential editing can decompose the task into simpler steps but suffers from compounding errors introduced by the sequential execution, leading to low-fidelity results. To derive a robust solution for complex image editing, we examine editing behaviors of different paradigms under a unified in-context editing framework, and study how the benefits of sequential decomposition can be balanced against its error-accumulation drawbacks. We further develop a synthetic data pipeline that constructs editing tasks of varying instruction complexity, allowing us to curate a large-scale editing dataset with high-quality decomposed sequences. By finetuning on synthetic data, we discovered that with properly designed editing paradigms, sequential decomposition yields robust improvements even as task complexity increases. Furthermore, the decomposition skills learned from synthetic tasks can transfer to real images by co-training with real-world editing data, demonstrating the promise of sim-to-real generalization for tackling complex image editing across broader domains.
匹配关键词: sim-to-real
---

[ACADEMIC - ARXIV]
标题: BEACON: Cross-Domain Co-Training of Generative Robot Policies via Best-Effort Adaptation
作者: Antong Zhang, Han Qi, Heng Yang
链接: https://arxiv.org/abs/2605.08571v1
完整摘要: We introduce BEACON--Best-Effort Adaptation for Cross-Domain Co-Training--a theory-driven framework for training generative robot policies with abundant source demonstrations and limited target demonstrations. BEACON casts cross-domain co-training as a discrepancy-aware importance-reweighting problem, jointly learning a diffusion-based visuomotor policy and per-sample source weights that minimize an objective informed by target-domain generalization guarantees. To make best-effort adaptation practical for high-dimensional sequence policies, we develop scalable instance-level discrepancy estimators, stochastic alternating updates for policy and weights, and a multi-source extension that balances heterogeneous source domains. Across sim-to-sim, sim-to-real, and multi-source manipulation settings, BEACON improves robustness and data efficiency over target-only, fixed-ratio co-training, and feature-alignment baselines. Importantly, even without an explicit alignment objective, BEACON achieves feature alignment as an implicit result of discrepancy-aware cross-domain co-training.
匹配关键词: sim-to-real
---

[ACADEMIC - ARXIV]
标题: Extending Confidence-Based Text2Cypher with Grammar and Schema Aware Filtering
作者: Makbule Gulcin Ozsoy
链接: https://arxiv.org/abs/2605.10318v1
完整摘要: Large language models (LLMs) allow users to query databases using natural language by translating questions into executable queries. Despite strong progress on tasks such as Text2SQL, Text2SPARQL, and Text2Cypher, most existing methods focus on better prompting, fine-tuning, or iterative refinement. However, they often do not explicitly enforce structural constraints, such as syntactic validity and schema consistency. This can reduce reliability, since generated queries must satisfy both syntax rules and database schema constraints to be executable. In this work, we study how structured constraints can be used in test-time inference for Text2Cypher. We focus on post-generation validation to improve query correctness. We extend a confidence-based inference framework with a sequential filtering process that combines confidence scoring, grammar validation, and schema constraints before final aggregation. This lets us analyze how different constraint types affect generated queries. Our experiments with two instruction-tuned models show that grammar-based filtering improves syntactic validity. Schema-aware filtering further improves execution quality by enforcing consistency with the database structure. However, stronger filtering also increases the number of empty predictions and reduces execution coverage. Overall, we show that adding simple structural checks at test time improves the reliability of Text2Cypher generation, and we provide a clearer view of how syntax and schema constraints contribute differently.
匹配关键词: world model
---

[ACADEMIC - ARXIV]
标题: Relations Are Channels: Knowledge Graph Embedding via Kraus Decompositions
作者: Sayan Kumar Chaki
链接: https://arxiv.org/abs/2605.10317v1
完整摘要: Knowledge graph embedding (KGE) models typically represent each relation as an operator on entity embeddings. In this work, we identify three structural axioms that any principled relation operator must satisfy, linearity, trace preservation, and complete positivity, and show that they characterize a Kraus channel structure via the Kraus representation theorem. The completeness constraint defining this family is equivalent to these axioms, providing a principled foundation rather than an externally imposed condition. Under this formulation, most existing operator-based KGE models are recoverable as special cases with Kraus rank $κ= 1$ under specific embedding choices. We further generalize this characterization to arbitrary metric geometries by introducing \mbox{w-Kraus} channels, which satisfy completeness by construction within their respective spaces. Building on this theory, we propose \textsc{KrausKGE}, a principled KGE model that naturally handles $1$-to-$N$ and $N$-to-$N$ relations, supports $k$-hop reasoning without requiring explicit path encoders, and eliminates the need for norm constraints on entity embeddings. Additionally, our framework yields the first theoretically grounded per-relation complexity measure in the KGE literature, with a provable lower bound in terms of the empirical relation matrix rank. Empirical evaluation demonstrates that \textsc{KrausKGE} consistently outperforms strong baselines on $N$-to-$N$ relations, with performance gains that increase monotonically with relation fan-out, in alignment with theoretical predictions.
匹配关键词: world model
---

[ACADEMIC - ARXIV]
标题: Active Tabular Augmentation via Policy-Guided Diffusion Inpainting
作者: Zheyu Zhang, Shuo Yang, Bardh Prenkaj, Gjergji Kasneci
链接: https://arxiv.org/abs/2605.10315v1
完整摘要: Generative tabular augmentation is appealing in data-scarce domains, yet the prevailing focus on distributional fidelity does not reliably translate into better downstream models. We formalize a fidelity-utility gap: common generative objectives prioritize distributional plausibility, whereas augmentation succeeds only when injected samples reduce the current learner's held-out evaluation loss. This gap motivates learning not just how to generate, but what to generate and when to inject as training evolves. We propose TAP (Tabular Augmentation Policy), which couples diffusion inpainting with a lightweight, learner-conditioned policy to steer generation toward high-utility regions and controls safe injection via explicit gating and conservative windowed commitment. Under severe data scarcity, TAP consistently outperforms strong generative baselines on seven real-world datasets, improving classification accuracy by up to 15.6 percentage points and reducing regression RMSE by up to 32%.
匹配关键词: world model
---

[ACADEMIC - ARXIV]
标题: PaMoSplat: Part-Aware Motion-Guided Gaussian Splatting for Dynamic Scene Reconstruction
作者: Yinan Deng, Jianyu Dou, Jiahui Wang, Jingyu Zhao, Yi Yang, Yufeng Yue
链接: https://arxiv.org/abs/2605.10307v1
完整摘要: Dynamic scene reconstruction represents a fundamental yet demanding challenge in computer vision and robotics. While recent progress in 3DGS-based methods has advanced dynamic scene modeling, obtaining high-fidelity rendering and accurate tracking in scenarios with substantial, intricate motions remains significantly challenging. To address these challenges, we propose PaMoSplat, a novel dynamic Gaussian splatting framework incorporating part awareness and motion priors. Our approach is grounded in two key observations: 1) Parts serve as primitives for scene deformation, and 2) Motion cues from optical flow can effectively guide part motion. Specifically, PaMoSplat initializes by lifting multi-view segmentation masks into 3D space via graph clustering, establishing coherent Gaussian parts. For subsequent timestamps, we leverage a differential evolutionary algorithm to estimate the rigid motion of these parts using multi-view optical flow cues, providing a robust warm-start for further optimization. Additionally, PaMoSplat introduces an adaptive iteration count mechanism, internal learnable rigidity, and flow-supervised rendering loss to accelerate and optimize the training process. Comprehensive evaluations across diverse scenes, including real-world environments, demonstrate that PaMoSplat delivers superior rendering quality, improved tracking precision, and faster convergence compared to existing methods. Furthermore, it enables multiple part-level downstream applications, such as 4D scene editing.
匹配关键词: world model
---

[ACADEMIC - ARXIV]
标题: Follow the Mean: Reference-Guided Flow Matching
作者: Pedro M. P. Curvo, Maksim Zhdanov, Floor Eijkelboom, Jan-Willem van de Meent
链接: https://arxiv.org/abs/2605.10302v1
完整摘要: Existing approaches to controllable generation typically rely on fine-tuning, auxiliary networks, or test-time search. We show that flow matching admits a different control interface: adaptation through examples. For deterministic interpolants, the velocity field is solely governed by a conditional endpoint mean; shifting this mean shifts the flow itself. This yields a simple principle for controllable generation: steer a pretrained model by changing the reference set it follows. We instantiate this idea in two forms. Reference-Mean Guidance is training-free: it computes a closed-form endpoint-mean correction from a reference bank and applies it to a frozen FLUX.2-klein (4B) model, enabling control of color, identity, style, and structure while keeping the prompt, seed, and weights fixed. Semi-Parametric Guidance amortizes the same idea through an explicit mean anchor and learned residual refiner, matching unconditional DiT-B/4 quality on AFHQv2 while allowing the reference set to be swapped at inference time. These results point to a broader direction: generative models that adapt through data, not parameter updates.
匹配关键词: world model
---

[ACADEMIC - ARXIV]
标题: AgentRx: A Benchmark Study of LLM Agents for Multimodal Clinical Prediction Tasks
作者: Baraa Al Jorf, Farah E. Shamout
链接: https://arxiv.org/abs/2605.10286v1
完整摘要: Building effective clinical decision support systems requires the synthesis of complex heterogeneous multimodal data. Such modalities include temporal electronic health records data, medical images, radiology reports, and clinical notes. Large language model (LLM)-based agents have shown impressive performance in various healthcare tasks, especially those involving textual modalities. Considering the fragmentation of healthcare data across hospital systems, collaborative agent frameworks present a promising direction to mitigate data sharing challenges. However, the effectiveness of LLM agents for multimodal clinical risk prediction remains largely unexamined. In this work, we conduct a systematic evaluation of LLM-based agents for clinical prediction tasks using large-scale real-world data. We assess performance in unimodal and multimodal settings and quantify performance gaps between single agent and multi-agent systems. Our findings highlight that single agent frameworks outperform naive multi-agent systems, are better at handling multimodal data, and are better calibrated. This underscores a critical need for improving multi-agent collaboration to better handle heterogeneous inputs. By open-sourcing our code and evaluation framework, this work offers a new benchmark to support future developments relating to agentic systems in healthcare.
匹配关键词: speech synthesis
---

[ACADEMIC - ARXIV]
标题: Drum Synthesis from Expressive Drum Grids via Neural Audio Codecs
作者: Konstantinos Soiledis, Maximos Kaliakatsos-Papakostas, Dimos Makris, Konstantinos Tsamis
链接: https://arxiv.org/abs/2605.10281v1
完整摘要: Generating realistic drum audio directly from symbolic representations is a challenging task at the intersection of music perception and machine learning. We propose a system that transforms an expressive drum grid, a time-aligned MIDI representation with microtiming and velocity information, into drum audio by predicting discrete codes of a neural audio codec. Our approach uses a Transformer-based model to map the drum grid input to a sequence of codec tokens, which are then converted to waveform audio via a pre-trained codec decoder. We experiment with multiple state-of-the-art neural codecs, namely EnCodec, DAC, and X-Codec, to assess how the choice of audio representation impacts the quality of the generated drums. The system is trained and evaluated on the Expanded Groove MIDI Dataset, E-GMD, a large collection of human drum performances with paired MIDI and audio. We evaluate the fidelity and musical alignment of the generated audio using objective metrics. Overall, our results establish codec-token prediction as an effective route for drum grid-to-audio generation and provide practical insights into selecting audio tokenizers for percussive synthesis.
匹配关键词: speech synthesis
---

[ACADEMIC - ARXIV]
标题: A Cold Diffusion Approach for Percussive Dereverberation
作者: Dimos Makris, András Barják, Maximos Kaliakatsos-Papakostas
链接: https://arxiv.org/abs/2605.10256v1
完整摘要: Most recent advances in audio dereverberation focus almost exclusively on speech, leaving percussive and drum signals largely unexplored despite their importance in music production. Percussive dereverberation poses distinct challenges due to sharp transients and dense temporal structure. In this work, we propose a cold diffusion framework for dereverberating stereo drum stems (downmixes), modeling reverberation as a deterministic degradation process that progressively transforms anechoic signals into reverberant ones. We investigate two reverse-process parameterizations, Direct (next-state) and a Delta-normalized residual (velocity-style) prediction, and implement the framework using both a UNet and a diffusion Transformer backbone. The models are trained and evaluated on curated datasets comprising both acoustic and electronic drum recordings, with reverberation generated using a combination of synthetic and real room impulse responses. Extensive experiments on in-domain and fully out-of-domain test sets demonstrate that the proposed method consistently outperforms strong score-based and conditional diffusion baselines, evaluated using signal-based and perceptual metrics tailored to percussive audio.
匹配关键词: speech synthesis
---

[ACADEMIC - ARXIV]
标题: SciIntegrity-Bench: A Benchmark for Evaluating Academic Integrity in AI Scientist Systems
作者: Zonglin Yang, Xingtong Liu, Xinyan Xu
链接: https://arxiv.org/abs/2605.10246v1
完整摘要: AI scientist systems are increasingly deployed for autonomous research, yet their academic integrity has never been systematically evaluated. We introduce SCIINTEGRITY-BENCH, the first benchmark designed around a dilemmatic evaluation paradigm: each of its 33 scenarios across 11 trap categories is constructed so that honest acknowledgment of failure is the only correct response, while task completion requires misconduct. Across 231 evaluation runs spanning 7 state-of-the-art LLMs, the overall integrity problem rate reaches 34.2%, and no model achieves zero failures. Most strikingly, across missing-data scenarios, all seven models generate synthetic data rather than acknowledging infeasibility, differing only in whether they disclose the substitution. A further prompt ablation study separates two drivers: removing explicit completion pressure sharply reduces undisclosed fabrication from 20.6% to 3.2%, while the underlying synthesis rate remains unchanged, revealing an intrinsic completion bias that persists independent of prompt-level instructions. These findings point to the absence of honest refusal as a trained disposition as the primary driver of observed failures. We release SCIINTEGRITY-BENCH at https://github.com/liuxingtong/Sci-Integrity-Bench.
匹配关键词: speech synthesis
---

[ACADEMIC - ARXIV]
标题: 3DReflecNet: A Large-Scale Dataset for 3D Reconstruction of Reflective, Transparent, and Low-Texture Objects
作者: Zhicheng Liang, Haoyi Yu, Boyan Li, Dayou Zhang, Zijian Cao, Tianyi Gong, Junhua Liu, Shuguang Cui, Fangxin Wang
链接: https://arxiv.org/abs/2605.10204v1
完整摘要: Accurate 3D reconstruction of objects with reflective, transparent, or low-texture surfaces still remains notoriously challenging. Such materials often violate key assumptions in multi-view reconstruction pipelines, such as photometric consistency and the availability on distinct geometric texture cues. Existing datasets primarily focus on diffuse, textured objects, and therefore provide limited insight into performance under real-world material complexities. We introduce 3DReflecNet, a large-scale hybrid dataset exceeding 22 TB that is specifically designed to benchmark and advance 3D vision methods for these challenging materials. 3DReflecNet combines two types of data: over 120,000 synthetic instances generated via physically-based rendering of more than 12,000 shapes, and over 1,000 real-world objects captured using consumer devices. Together, these data consist of more than 7 million multi-view frames. The dataset spans diverse materials, complex lighting conditions, and a wide range of geometric forms, including shapes generated from both real and LLM-synthesized 2D images using diffusion-based pipelines. To support robust evaluation, we design benchmarks for five core tasks: image matching, structure-from-motion, novel view synthesis, reflection removal, and relighting. Extensive experiments demonstrate that state-of-the-art methods struggle to maintain accuracy across these settings, highlighting the need for more resilient 3D vision models.
匹配关键词: speech synthesis
---

[ACADEMIC - ARXIV]
标题: PoDAR: Power-Disentangled Audio Representation for Generative Modeling
作者: Alejandro Luebs, Mithilesh Vaidya, Ishaan Kumar, Sumukh Badam, Stephen W. Bailey, Matthew Bendel, Jose Sotelo, Xingzhe He
链接: https://arxiv.org/abs/2605.10084v1
完整摘要: The performance of audio latent diffusion models is primarily governed by generator expressivity and the modelability of the underlying latent space. While recent research has focused primarily on the former, as well as improving the reconstruction fidelity of audio codecs, we demonstrate that latent modelability can be significantly improved through explicit factor disentanglement. We present PoDAR (Power-Disentangled Audio Representation), a framework that utilizes a randomized power augmentation and latent consistency objective to decouple signal power from invariant semantic content. This factorization makes the latent space easier to model, which both accelerates the convergence of downstream generative models and improves final overall performance. When applied to a Stable Audio 1.0 VAE with an F5-TTS generator, PoDAR achieves about a $2\times$ acceleration in convergence to match baseline performance, while increasing final speaker similarity by 0.055 and UTMOS by 0.22 on the LibriSpeech-PC dataset. Furthermore, isolating power into dedicated channels enables the application of CFG exclusively to power-invariant content, effectively extending the stable guidance regime to higher scales.
匹配关键词: TTS
---

[ACADEMIC - ARXIV]
标题: Metis: Learning to Jailbreak LLMs via Self-Evolving Metacognitive Policy Optimization
作者: Huilin Zhou, Jian Zhao, Yilu Zhong, Zhen Liang, Xiuyuan Chen, Yuchen Yuan, Tianle Zhang, Chi Zhang, Lan Zhang, Xuelong Li
链接: https://arxiv.org/abs/2605.10067v1
完整摘要: Red teaming is critical for uncovering vulnerabilities in Large Language Models (LLMs). While automated methods have improved scalability, existing approaches often rely on static heuristics or stochastic search, rendering them brittle against advanced safety alignment. To address this, we introduce Metis, a framework that reformulates jailbreaking as inference-time policy optimization within an adversarial Partially Observable Markov Decision Process (POMDP). Metis employs a self-evolving metacognitive loop to perform causal diagnosis of a target's defense logic and leverages structured feedback as a semantic gradient to refine its policy, offering enhanced interpretability through transparent reasoning traces. Extensive evaluations across 10 diverse models demonstrate that Metis achieves the strongest average Attack Success Rate (ASR) among compared methods at 89.2%, maintaining high efficacy on resilient frontier models (e.g., 76.0% on O1 and 78.0% on GPT-5-chat) where traditional baselines exhibit substantial performance degradation. By replacing redundant exploration with directed optimization, Metis reduces token costs by an average of 8.2x and up to 11.4x. Our analysis reveals that current defenses remain vulnerable to internally-steered, closed-loop reasoning trajectories under the tested settings, highlighting a critical need for next-generation defenses capable of reasoning about safety dynamically during inference.
匹配关键词: ASR
---

[ACADEMIC - ARXIV]
标题: Extending Confidence-Based Text2Cypher with Grammar and Schema Aware Filtering
作者: Makbule Gulcin Ozsoy
链接: https://arxiv.org/abs/2605.10318v1
完整摘要: Large language models (LLMs) allow users to query databases using natural language by translating questions into executable queries. Despite strong progress on tasks such as Text2SQL, Text2SPARQL, and Text2Cypher, most existing methods focus on better prompting, fine-tuning, or iterative refinement. However, they often do not explicitly enforce structural constraints, such as syntactic validity and schema consistency. This can reduce reliability, since generated queries must satisfy both syntax rules and database schema constraints to be executable. In this work, we study how structured constraints can be used in test-time inference for Text2Cypher. We focus on post-generation validation to improve query correctness. We extend a confidence-based inference framework with a sequential filtering process that combines confidence scoring, grammar validation, and schema constraints before final aggregation. This lets us analyze how different constraint types affect generated queries. Our experiments with two instruction-tuned models show that grammar-based filtering improves syntactic validity. Schema-aware filtering further improves execution quality by enforcing consistency with the database structure. However, stronger filtering also increases the number of empty predictions and reduces execution coverage. Overall, we show that adding simple structural checks at test time improves the reliability of Text2Cypher generation, and we provide a clearer view of how syntax and schema constraints contribute differently.
匹配关键词: audio language model
---

[ACADEMIC - ARXIV]
标题: Relations Are Channels: Knowledge Graph Embedding via Kraus Decompositions
作者: Sayan Kumar Chaki
链接: https://arxiv.org/abs/2605.10317v1
完整摘要: Knowledge graph embedding (KGE) models typically represent each relation as an operator on entity embeddings. In this work, we identify three structural axioms that any principled relation operator must satisfy, linearity, trace preservation, and complete positivity, and show that they characterize a Kraus channel structure via the Kraus representation theorem. The completeness constraint defining this family is equivalent to these axioms, providing a principled foundation rather than an externally imposed condition. Under this formulation, most existing operator-based KGE models are recoverable as special cases with Kraus rank $κ= 1$ under specific embedding choices. We further generalize this characterization to arbitrary metric geometries by introducing \mbox{w-Kraus} channels, which satisfy completeness by construction within their respective spaces. Building on this theory, we propose \textsc{KrausKGE}, a principled KGE model that naturally handles $1$-to-$N$ and $N$-to-$N$ relations, supports $k$-hop reasoning without requiring explicit path encoders, and eliminates the need for norm constraints on entity embeddings. Additionally, our framework yields the first theoretically grounded per-relation complexity measure in the KGE literature, with a provable lower bound in terms of the empirical relation matrix rank. Empirical evaluation demonstrates that \textsc{KrausKGE} consistently outperforms strong baselines on $N$-to-$N$ relations, with performance gains that increase monotonically with relation fan-out, in alignment with theoretical predictions.
匹配关键词: audio language model
---

[ACADEMIC - ARXIV]
标题: Active Tabular Augmentation via Policy-Guided Diffusion Inpainting
作者: Zheyu Zhang, Shuo Yang, Bardh Prenkaj, Gjergji Kasneci
链接: https://arxiv.org/abs/2605.10315v1
完整摘要: Generative tabular augmentation is appealing in data-scarce domains, yet the prevailing focus on distributional fidelity does not reliably translate into better downstream models. We formalize a fidelity-utility gap: common generative objectives prioritize distributional plausibility, whereas augmentation succeeds only when injected samples reduce the current learner's held-out evaluation loss. This gap motivates learning not just how to generate, but what to generate and when to inject as training evolves. We propose TAP (Tabular Augmentation Policy), which couples diffusion inpainting with a lightweight, learner-conditioned policy to steer generation toward high-utility regions and controls safe injection via explicit gating and conservative windowed commitment. Under severe data scarcity, TAP consistently outperforms strong generative baselines on seven real-world datasets, improving classification accuracy by up to 15.6 percentage points and reducing regression RMSE by up to 32%.
匹配关键词: audio language model
---

[ACADEMIC - ARXIV]
标题: PaMoSplat: Part-Aware Motion-Guided Gaussian Splatting for Dynamic Scene Reconstruction
作者: Yinan Deng, Jianyu Dou, Jiahui Wang, Jingyu Zhao, Yi Yang, Yufeng Yue
链接: https://arxiv.org/abs/2605.10307v1
完整摘要: Dynamic scene reconstruction represents a fundamental yet demanding challenge in computer vision and robotics. While recent progress in 3DGS-based methods has advanced dynamic scene modeling, obtaining high-fidelity rendering and accurate tracking in scenarios with substantial, intricate motions remains significantly challenging. To address these challenges, we propose PaMoSplat, a novel dynamic Gaussian splatting framework incorporating part awareness and motion priors. Our approach is grounded in two key observations: 1) Parts serve as primitives for scene deformation, and 2) Motion cues from optical flow can effectively guide part motion. Specifically, PaMoSplat initializes by lifting multi-view segmentation masks into 3D space via graph clustering, establishing coherent Gaussian parts. For subsequent timestamps, we leverage a differential evolutionary algorithm to estimate the rigid motion of these parts using multi-view optical flow cues, providing a robust warm-start for further optimization. Additionally, PaMoSplat introduces an adaptive iteration count mechanism, internal learnable rigidity, and flow-supervised rendering loss to accelerate and optimize the training process. Comprehensive evaluations across diverse scenes, including real-world environments, demonstrate that PaMoSplat delivers superior rendering quality, improved tracking precision, and faster convergence compared to existing methods. Furthermore, it enables multiple part-level downstream applications, such as 4D scene editing.
匹配关键词: audio language model
---

[ACADEMIC - ARXIV]
标题: Follow the Mean: Reference-Guided Flow Matching
作者: Pedro M. P. Curvo, Maksim Zhdanov, Floor Eijkelboom, Jan-Willem van de Meent
链接: https://arxiv.org/abs/2605.10302v1
完整摘要: Existing approaches to controllable generation typically rely on fine-tuning, auxiliary networks, or test-time search. We show that flow matching admits a different control interface: adaptation through examples. For deterministic interpolants, the velocity field is solely governed by a conditional endpoint mean; shifting this mean shifts the flow itself. This yields a simple principle for controllable generation: steer a pretrained model by changing the reference set it follows. We instantiate this idea in two forms. Reference-Mean Guidance is training-free: it computes a closed-form endpoint-mean correction from a reference bank and applies it to a frozen FLUX.2-klein (4B) model, enabling control of color, identity, style, and structure while keeping the prompt, seed, and weights fixed. Semi-Parametric Guidance amortizes the same idea through an explicit mean anchor and learned residual refiner, matching unconditional DiT-B/4 quality on AFHQv2 while allowing the reference set to be swapped at inference time. These results point to a broader direction: generative models that adapt through data, not parameter updates.
匹配关键词: audio language model
---

[ACADEMIC - ARXIV]
标题: PFN-TS: Thompson Sampling for Contextual Bandits via Prior-Data Fitted Networks
作者: Yan Shuo Tan, Kenyon Ng, Ruizhe Deng, Sumetha Loganathan, Qiong Zhang, Bibhas Chakraborty
链接: https://arxiv.org/abs/2605.10137v1
完整摘要: Thompson sampling is a widely used strategy for contextual bandits: at each round, it samples a reward function from a Bayesian posterior and acts greedily under that sample. Prior-data fitted networks (PFNs), such as TabPFN v2+ and TabICL v2, are attractive candidates for this purpose because they approximate Bayesian posterior predictive distributions in a single forward pass. However, PFNs predict noisy future rewards, while Thompson sampling requires uncertainty over the latent mean reward function. We propose PFN-TS, a Thompson sampling algorithm that converts PFN posterior predictives into mean-reward samples using a subsampled predictive central limit theorem. The method estimates posterior variance from a geometric grid of $O(\log n)$ dataset prefixes rather than the full $O(n)$ predictive sequence used in previous predictive-sequence approaches, and reuses TabICL's cached representations across rounds. We prove consistency of the subsampled variance estimator and give a Bayesian regret bound that decomposes PFN-TS regret into exact posterior-sampling regret under the PFN prior plus approximation terms. Empirically, PFN-TS achieves the best average rank across nonlinear synthetic and OpenML classification-to-bandit benchmarks, remains competitive on linear and BART-generated rewards, and attains the highest estimated policy value in an offline mobile-health evaluation. Code is available at https://anonymous.4open.science/r/PFN_TS-36ED/.
匹配关键词: KV cache
---

[ACADEMIC - ARXIV]
标题: Muninn: Your Trajectory Diffusion Model But Faster
作者: Gokul Puthumanaillam, Hao Jiang, Ruben Hernandez, Jose Fuentes, Paulo Padrao, Leonardo Bobadilla, Melkior Ornik
链接: https://arxiv.org/abs/2605.09999v1
完整摘要: Diffusion-based trajectory planners can synthesize rich, multimodal robot motions, but their iterative denoising makes online planning and control prohibitively slow. Existing accelerations either modify the sampler or compress the network--sacrificing plan quality or requiring retraining without accounting for downstream control risk. We address the problem of making diffusion-based trajectory planners fast enough for real-time robot use without retraining the model or sacrificing trajectory quality, and in a way that works across diverse state-space diffusion architectures. Our key insight is that diffusion trajectory planners expose two signals we can exploit: a cheap probe of how their internal trajectory representation changes across steps, and analytic coefficients that describe how denoiser errors affect the sampler's state update. By calibrating the first signal against the second on offline runs, we obtain a per-step score that upper-bounds how far the final trajectory can deviate when we reuse a cached denoiser output, and we treat this bound as an uncertainty budget that we can spend over the denoising process. Building on this insight, we present Muninn, a training-free caching wrapper that tracks this uncertainty budget during sampling and, at each diffusion step, chooses between reusing a cached denoiser output when the predicted deviation is small and recomputing the denoiser when it is not. Across standard benchmarks Muninn delivers up to 4.6x wall-clock speedups across several trajectory diffusion models by reducing denoiser evaluations, while preserving task performance and safety metrics. Muninn further certifies that cached rollouts remain within a specified distance of their full-compute counterparts, and we validate these gains in real-time closed-loop navigation and manipulation hardware deployments. Project page: https://github.com/gokulp01/Muninn.
匹配关键词: KV cache
---

[ACADEMIC - ARXIV]
标题: Nano-U: Efficient Terrain Segmentation for Tiny Robot Navigation
作者: Federico Pizzolato, Francesco Pasti, Nicola Bellotto
链接: https://arxiv.org/abs/2605.10210v1
完整摘要: Terrain segmentation is a fundamental capability for autonomous mobile robots operating in unstructured outdoor environments. However, state-of-the-art models are incompatible with the memory and compute constraints typical of microcontrollers, limiting scalable deployment in small robotics platforms. To address this gap, we develop a complete framework for robust binary terrain segmentation on a low-cost microcontroller. At the core of our approach we design Nano-U, a highly compact binary segmentation network with a few thousand parameters. To compensate for the network's minimal capacity, we train Nano-U via Quantization-Aware Distillation (QAD), combining knowledge distillation and quantization-aware training. This allows the final quantized model to achieve excellent results on the Botanic Garden dataset and to perform very well on TinyAgri, a custom agricultural field dataset with more challenging scenes. We deploy the quantized Nano-U on a commodity microcontroller by extending MicroFlow, a compiler-based inference engine for TinyML implemented in Rust. By eliminating interpreter overhead and dynamic memory allocation, the quantized model executes on an ESP32-S3 with a minimal memory footprint and low latency. This compiler-based execution demonstrates a viable and energy-efficient solution for perception on low-cost robotic platforms.
匹配关键词: quantization
---

[ACADEMIC - ARXIV]
标题: Measurement-Adapted Eigentask Representations for Photon-Limited Optical Readout
作者: Tianyang Chen, Mandar M. Sohoni, Saeed A. Khan, Jérémie Laydevant, Shi-Yuan Ma, Tianyu Wang, Peter L. McMahon, Hakan E. Türeci
链接: https://arxiv.org/abs/2605.10008v1
完整摘要: Optical readout in low-light imaging is fundamentally limited by measurement noise, including photon shot noise, detector noise, and quantization error. In this regime, downstream inference depends not only on the optical front end, but also on how noisy high-dimensional sensor measurements are represented before classification or decision-making. Here we show that eigentasks provide a measurement-adapted representation for optical sensor outputs by ordering readout features according to their resolvability under noise. Using experimental data from a lens-based optical imaging system and a reanalysis of published data from a single-photon-detection neural network, we find that eigentask representations frequently outperform standard baselines including principal component analysis and filtering-based compression. The advantage is most pronounced in photon-limited, few-shot, and higher-difficulty classification regimes. In few-shot MPEG-7 classification, for example, the advantage over other methods reaches about 10 percentage points as the number of classes increases. In these settings, eigentasks yield more informative low-dimensional features and improve sample-efficient downstream learning. These results identify measurement-adapted representation as a promising strategy for optical inference when photon budget, acquisition time, and task complexity are constrained.
匹配关键词: quantization
---

[ACADEMIC - ARXIV]
标题: Federated Language Models Under Bandwidth Budgets: Distillation Rates and Conformal Coverage
作者: Prasanjit Dubey, Xiaoming Huo
链接: https://arxiv.org/abs/2605.09986v1
完整摘要: Training a language model on data scattered across bandwidth-limited nodes that cannot be centralized is a setting that arises in clinical networks, enterprise knowledge bases, and scientific consortia. We study the regime in which data must remain distributed across nodes, and ask what statistical guarantees are in principle achievable under explicit bandwidth budgets; we aim to characterize what is provably possible, not to demonstrate a deployment-ready system. Existing theory treats either training-time consistency or inference-time calibration in isolation, and none makes bandwidth a first-class statistical parameter. We analyze two protocols, Federated Probe-Logit Distillation (FPLD) for training and Federated Conformal RAG (FC-RAG) for inference, as the analytical vehicles for our results. Our first main result is an explicit high-probability KL-consistency rate for FPLD with simultaneous dependence on node count $K$, per-node sample size $n$, quantization budget $B$, probe-set size $m$, and vocabulary size $V$; bandwidth enters only through an exponentially vanishing quantization term. Our second main result is a distribution-free marginal-coverage bound for FC-RAG, whose novel retrieval-bandwidth slack $Δ_{\mathrm{RAG}} = f_{\max}\sqrt{K^{-2}\sum_i v(B_i)}$ makes per-node retrieval bandwidth a first-class statistical parameter, with arithmetic aggregation across $K$ nodes shrinking the slack as $K^{-1/2}$ in the per-node-uniform regime. A Pinsker-type corollary composes the two bounds into an end-to-end coverage guarantee. Synthetic experiments verify the predicted scaling along the bounds' parameters; small-scale experiments on a GPT-2 testbed illustrate that the qualitative bandwidth-accuracy tradeoff survives on a real language model. A deployment-scale empirical evaluation is out of scope.
匹配关键词: quantization
---

[ACADEMIC - ARXIV]
标题: Yeti: A compact protein structure tokenizer for reconstruction and multi-modal generation
作者: Nabin Giri, Steven Farrell, Kristofer E. Bouchard
链接: https://arxiv.org/abs/2605.09981v1
完整摘要: Multimodal models that jointly reason over protein sequences, structures, and function annotations within a unified representation hold immense potential for integrating multimodal data and generating new proteins with designed functional properties. To utilize transformer architectures, such models require a tokenizer that converts protein structure from continuous atomic coordinates into discrete representations suitable for scalable multimodal training. The quality of such models are fundamentally upper bounded by the fidelity and expressiveness of the underlying tokenized structure. However, existing tokenizers prioritize reconstruction over generative abilities. To address these gaps, we introduce Yeti, a simple and compact protein structure tokenizer based on lookup free quantization and trained end to end with a flow matching objective for multimodal learning. Compared to existing models, Yeti generally achieves the best codebook utilization and token diversity, and second best reconstruction accuracy (with 10x fewer parameters than ESM3) on diverse datasets. To validate Yeti's generative capability, we trained a compact multimodal model jointly over its structure tokens and amino acid sequence entirely from scratch, with no pretrained initialization. The resulting multimodal model generates plausible structures under unconditional cogeneration of protein sequence and structures, achieving comparable results to 10x larger models. Together, these results demonstrate that Yeti is a compact and expressive protein structure tokenizer suitable for training multimodal models that cogenerates highly plausible sequences and structures.
匹配关键词: quantization
---

[ACADEMIC - ARXIV]
标题: Drum Synthesis from Expressive Drum Grids via Neural Audio Codecs
作者: Konstantinos Soiledis, Maximos Kaliakatsos-Papakostas, Dimos Makris, Konstantinos Tsamis
链接: https://arxiv.org/abs/2605.10281v1
完整摘要: Generating realistic drum audio directly from symbolic representations is a challenging task at the intersection of music perception and machine learning. We propose a system that transforms an expressive drum grid, a time-aligned MIDI representation with microtiming and velocity information, into drum audio by predicting discrete codes of a neural audio codec. Our approach uses a Transformer-based model to map the drum grid input to a sequence of codec tokens, which are then converted to waveform audio via a pre-trained codec decoder. We experiment with multiple state-of-the-art neural codecs, namely EnCodec, DAC, and X-Codec, to assess how the choice of audio representation impacts the quality of the generated drums. The system is trained and evaluated on the Expanded Groove MIDI Dataset, E-GMD, a large collection of human drum performances with paired MIDI and audio. We evaluate the fidelity and musical alignment of the generated audio using objective metrics. Overall, our results establish codec-token prediction as an effective route for drum grid-to-audio generation and provide practical insights into selecting audio tokenizers for percussive synthesis.
匹配关键词: speculative decoding
---

[ACADEMIC - ARXIV]
标题: Efficient Hybrid CNN-GNN Architecture for Monocular Depth Estimation
作者: Ishan Narayan
链接: https://arxiv.org/abs/2605.10251v1
完整摘要: We present GraphDepth, a monocular depth estimation architecture that synergistically integrates Graph Neural Networks (GNNs) within a convolutional encoder-decoder framework. Our approach embeds efficient GraphSAGE layers at multiple scales of a ResNet-101 U-Net backbone, enabling explicit modeling of long-range spatial relationships that lie beyond the receptive field of local convolutions. Key technical contributions include: (1) batch-parallelized graph construction with configurable k-NN and grid-based adjacency for scalable training; (2) multi-scale GraphSAGE integration at bottleneck and decoder stages (1/32, 1/16, 1/8 resolution) to propagate global context throughout the feature hierarchy; (3) channel-attention gated skip connections that adaptively weight encoder features before fusion; and (4) heteroscedastic uncertainty estimation via a dedicated aleatoric uncertainty head, enabling confidence-aware loss weighting during optimization. Unlike transformer-based hybrids, which suffer from quadratic complexity in sequence length, GraphDepth scales linearly with spatial resolution while achieving comparable global receptive fields through iterative message passing. Experiments on NYU Depth V2, WHU Aerial, ETH3D, and Mid-Air benchmarks demonstrate competitive accuracy within 4.6\% of state-of-the-art transformers on indoor scenes with substantially lower computational cost (25 FPS vs 9 FPS, 3.8 GB vs 8.8 GB VRAM). GraphDepth achieves the best reported result on WHU Aerial (RMSE 8.24 m) and exhibits superior zero-shot cross-domain transfer to the Mid-Air synthetic aerial dataset, validating the generalization power of explicit relational reasoning for depth estimation.
匹配关键词: speculative decoding
---

[ACADEMIC - ARXIV]
标题: AdaptSplat: Adapting Vision Foundation Models for Feed-Forward 3D Gaussian Splatting
作者: Mingwei Xing, Xinliang Wang, Yifeng Shi
链接: https://arxiv.org/abs/2605.10239v1
完整摘要: This work explores a simple yet powerful lightweight adapter design for feed-forward 3D Gaussian Splatting (3DGS). Existing methods typically apply complex, architecture-specific designs on top of the generic pipeline of image feature extraction $\rightarrow$ multi-view interaction $\rightarrow$ feature decoding. However, constrained by the scale bottleneck of 3D training data and the low-pass filtering effect of deep networks, these methods still fall short in cross-domain generalization and high-frequency geometric fidelity. To address these problems, we propose AdaptSplat, which demonstrates that without complex component engineering, introducing a single adapter of only 1.5M parameters into the generic architecture is sufficient to achieve superior performance. Specifically, we design a lightweight Frequency-Preserving Adapter (FPA) that extracts direction-aware high-frequency structural priors from the shallow features of a powerful vision foundation model backbone, and seamlessly integrates them into the generic pipeline via high-frequency positional encodings and adaptive residual modulation. This effectively compensates for the high-frequency attenuation caused by over-smoothing in deep features, improving the fitting accuracy of Gaussian primitives on complex surfaces and sharp boundaries. Extensive experiments demonstrate that AdaptSplat achieves state-of-the-art feed-forward reconstruction performance on multiple standard benchmarks, with stable generalization across domains. Code available at: https://github.com/xmw666/AdaptSplat.
匹配关键词: speculative decoding
---

[ACADEMIC - ARXIV]
标题: Task-Aware Calibration: Provably Optimal Decoding in LLMs
作者: Tim Tomov, Dominik Fuchsgruber, Rajeev Verma, Stephan Günnemann
链接: https://arxiv.org/abs/2605.10202v1
完整摘要: LLM decoding often relies on the model's predictive distribution to generate an output. Consequently, misalignment with respect to the true generating distribution leads to suboptimal decisions in practice. While a natural solution is to calibrate the model's output distribution, for LLMs, this is ill-posed at the combinatorially vast level of free-form language. We address this by building on the insight that in many tasks, these free-form outputs can be interpreted in a semantically meaningful latent structure, for example, discrete class labels, integers, or sets. We introduce task calibration as a paradigm to calibrate the model's predictive distribution in the task-induced latent space. We apply a decision-theoretic result to show that Minimum Bayes Risk (MBR) decoding on the task-calibrated latent distribution is the optimal decoding strategy on latent model beliefs. Empirically, it consistently improves generation quality across different tasks and baselines. We also introduce Task Calibration Error (TCE), an application-aware calibration metric that quantifies the excess loss due to miscalibration. Our work demonstrates that task calibration enables more reliable model decisions across various tasks and applications.
匹配关键词: speculative decoding
---

[ACADEMIC - ARXIV]
标题: Breaking the Reward Barrier: Accelerating Tree-of-Thought Reasoning via Speculative Exploration
作者: Shuzhang Zhong, Haochen Huang, Shengxuan Qiu, Pengfei Zuo, Runsheng Wang, Meng Li
链接: https://arxiv.org/abs/2605.10195v1
完整摘要: Tree-of-Thought (ToT) reasoning structures Large Language Model (LLM) inference as a tree-based search, demonstrating strong potential for solving complex mathematical and programming tasks. However, its efficiency is constrained by the reward dependency barrier -- a synchronization bottleneck caused by sequential reward-guided exploration that limits search parallelism and introduces substantial latency. Prior system optimizations, mainly designed for linear Chain-of-Thought (CoT) reasoning, cannot address these challenges, leaving the efficiency of ToT underexplored. To enhance ToT reasoning efficiency, we observe that the reasoning paths can be explored speculatively to break the reward synchronization barrier. Therefore, in this paper, we propose SPEX and introduce three key techniques: (i) intra-query speculative path selection to predict and expand high-potential branches of ToT, (ii) inter-query budget allocation to balance speculative resource allocation across queries dynamically, and (iii) adaptive early termination to prune deep and redundant branches for a skewed search tree. We implement SPEX on top of the SGLang framework and evaluate it across diverse ToT algorithms and LLMs. Extensive experiments show that SPEX achieves $1.2 \sim 3 \times$ speedup for different ToT reasoning algorithms. Moreover, SPEX synergizes with token-level speculative decoding, achieving cumulative speedups of up to $4.1\times$. Ablation studies further confirm the contributions of each technique. Overall, SPEX represents a significant step toward efficient and scalable ToT reasoning, unlocking the parallelism required for high-performance inference-time scaling for LLMs.
匹配关键词: speculative decoding
---

[ACADEMIC - ARXIV]
标题: Signature Approach for Contextual Bandits with Nonlinear and Path-dependent Rewards
作者: Xin Guo, Grace He, Xinyu Li
链接: https://arxiv.org/abs/2605.10313v1
完整摘要: We study contextual bandits with nonlinear and path-dependent rewards through a novel signature-transform-based approach. Leveraging the universal nonlinearity property of signatures, we approximate continuous path-dependent reward functionals by linear functionals in the signature space. This representation enables the use of efficient linear contextual bandit methods while preserving expressive sequential structure. Building on this framework, we propose \texttt{DisSigUCB}, a signature-based disjoint upper confidence bound (UCB) algorithm. Under boundedness and non-degeneracy assumptions, we prove a high-probability data-dependent sublinear regret bound of order \(\tilde{\mathcal O}(\sqrt{(d+m)KT})\) where \(d\) is the context dimension and \(m\) is the signature feature dimension. Synthetic experiments and numerical applications on temperature sensor monitoring, sleep-stage classification, and hospital nurse staffing demonstrate that \texttt{DisSigUCB} consistently outperforms classical linear and kernelized contextual bandit baselines in nonlinear and path-dependent settings.
匹配关键词: kernel optimization
---

[ACADEMIC - ARXIV]
标题: PaMoSplat: Part-Aware Motion-Guided Gaussian Splatting for Dynamic Scene Reconstruction
作者: Yinan Deng, Jianyu Dou, Jiahui Wang, Jingyu Zhao, Yi Yang, Yufeng Yue
链接: https://arxiv.org/abs/2605.10307v1
完整摘要: Dynamic scene reconstruction represents a fundamental yet demanding challenge in computer vision and robotics. While recent progress in 3DGS-based methods has advanced dynamic scene modeling, obtaining high-fidelity rendering and accurate tracking in scenarios with substantial, intricate motions remains significantly challenging. To address these challenges, we propose PaMoSplat, a novel dynamic Gaussian splatting framework incorporating part awareness and motion priors. Our approach is grounded in two key observations: 1) Parts serve as primitives for scene deformation, and 2) Motion cues from optical flow can effectively guide part motion. Specifically, PaMoSplat initializes by lifting multi-view segmentation masks into 3D space via graph clustering, establishing coherent Gaussian parts. For subsequent timestamps, we leverage a differential evolutionary algorithm to estimate the rigid motion of these parts using multi-view optical flow cues, providing a robust warm-start for further optimization. Additionally, PaMoSplat introduces an adaptive iteration count mechanism, internal learnable rigidity, and flow-supervised rendering loss to accelerate and optimize the training process. Comprehensive evaluations across diverse scenes, including real-world environments, demonstrate that PaMoSplat delivers superior rendering quality, improved tracking precision, and faster convergence compared to existing methods. Furthermore, it enables multiple part-level downstream applications, such as 4D scene editing.
匹配关键词: kernel optimization
---

[ACADEMIC - ARXIV]
标题: Nearly-Optimal Algorithm for Adversarial Kernelized Bandits
作者: Shogo Iwazaki
链接: https://arxiv.org/abs/2605.10299v1
完整摘要: This paper studies kernelized bandits (also known as Gaussian process bandits) in an adversarial environment, where the reward functions in a known reproducing kernel Hilbert space (RKHS) may be adversarially chosen at each round. We show that the exponential-weight algorithm achieves $\tilde{O}(\sqrt{T γ_T})$ adversarial regret, where $T$ and $γ_T$ denote the number of total rounds and the maximum information gain, respectively. For squared exponential (SE) and $ν$-Matérn kernels, we also show algorithm-independent lower bounds that guarantee the optimality of our algorithm up to polylogarithmic factors. Furthermore, we present a computationally efficient variant of our algorithm using Nyström approximation while maintaining nearly optimal regret guarantees.
匹配关键词: kernel optimization
---

[ACADEMIC - ARXIV]
标题: LeapTS: Rethinking Time Series Forecasting as Adaptive Multi-Horizon Scheduling
作者: Sheng Pan, Ming Jin, Bo Du, Shirui Pan
链接: https://arxiv.org/abs/2605.10292v1
完整摘要: Time series forecasting serves as an essential tool for many real-world applications, supporting tasks such as resource optimization and decision-making. Despite significant architectural advancements, most modern models still treat forecasting task as a fixed mapping from history to target horizons. This induces temporal decoupling across future time points and limits the model's ability to adapt to the evolving context as forecasting progresses. In this work, we present LeapTS, a novel framework that reformulates time series forecasting as a dynamic scheduling process over the prediction horizon. Specifically, LeapTS organizes the forecasting process into multi-level decisions using: (1) the hierarchical controller to dynamically select the optimal prediction scale and advancement length at each step, and (2) continuous-time state evolution driven by neural controlled differential equations. Within this process, the controlled update mechanism explicitly couples the irregular temporal dynamics with discrete scheduling feedback. Extensive evaluations on both real-world and synthetic datasets demonstrate that LeapTS improves overall forecasting performance by at least 7.4% while achieving a 2.6$\times$ to 5.3$\times$ inference speedup over representative Transformer-based models. Furthermore, by explicitly tracing the scheduling trajectories, we reveal how the model autonomously adapts its forecasting behavior to capture non-stationary dynamics.
匹配关键词: kernel optimization
---

[ACADEMIC - ARXIV]
标题: Sample-Mean Anchored Thompson Sampling for Offline-to-Online Learning with Distribution Shift
作者: Bochao Li, Yao Fu, Wei Chen, Fang Kong
链接: https://arxiv.org/abs/2605.10289v1
完整摘要: Offline-to-online learning aims to improve online decision-making by leveraging offline logged data. A central challenge in this setting is the distribution shift between offline and online environments. While some existing works attempt to leverage shifted offline data, they largely rely on UCB-type algorithms. Thompson sampling (TS) represents another canonical class of bandit algorithms, well known for its strong empirical performance and naturally suited to offline-to-online learning through its Bayesian formulation. However, unlike UCB indices, posterior samples in TS are not guaranteed to be optimistic with respect to the true arm means. This makes indices constructed from purely online and hybrid data difficult to compare and complicates their use. To address this issue, we propose sample-mean anchored TS (Anchor-TS), which introduces a novel median-based anchoring rule that defines the arm index as the median of an online posterior sample, a hybrid posterior sample, and the online sample mean. The median anchoring systematically corrects bias induced by distribution shift by mitigating over-estimation for suboptimal arms and under-estimation for optimal arms, while exploiting offline information to obtain more accurate estimates when the shift is small. We establish theoretical guarantees showing that the proposed algorithm safely leverages offline data to accelerate online learning, and quantifying how the degree of distribution shift and the size of offline data affect the resulting regret reduction. Extensive experiments demonstrate consistent improvements of our algorithm over baselines.
匹配关键词: kernel optimization
---

[ACADEMIC - ARXIV]
标题: Signature Approach for Contextual Bandits with Nonlinear and Path-dependent Rewards
作者: Xin Guo, Grace He, Xinyu Li
链接: https://arxiv.org/abs/2605.10313v1
完整摘要: We study contextual bandits with nonlinear and path-dependent rewards through a novel signature-transform-based approach. Leveraging the universal nonlinearity property of signatures, we approximate continuous path-dependent reward functionals by linear functionals in the signature space. This representation enables the use of efficient linear contextual bandit methods while preserving expressive sequential structure. Building on this framework, we propose \texttt{DisSigUCB}, a signature-based disjoint upper confidence bound (UCB) algorithm. Under boundedness and non-degeneracy assumptions, we prove a high-probability data-dependent sublinear regret bound of order \(\tilde{\mathcal O}(\sqrt{(d+m)KT})\) where \(d\) is the context dimension and \(m\) is the signature feature dimension. Synthetic experiments and numerical applications on temperature sensor monitoring, sleep-stage classification, and hospital nurse staffing demonstrate that \texttt{DisSigUCB} consistently outperforms classical linear and kernelized contextual bandit baselines in nonlinear and path-dependent settings.
匹配关键词: memory efficiency
---

[ACADEMIC - ARXIV]
标题: Nearly-Optimal Algorithm for Adversarial Kernelized Bandits
作者: Shogo Iwazaki
链接: https://arxiv.org/abs/2605.10299v1
完整摘要: This paper studies kernelized bandits (also known as Gaussian process bandits) in an adversarial environment, where the reward functions in a known reproducing kernel Hilbert space (RKHS) may be adversarially chosen at each round. We show that the exponential-weight algorithm achieves $\tilde{O}(\sqrt{T γ_T})$ adversarial regret, where $T$ and $γ_T$ denote the number of total rounds and the maximum information gain, respectively. For squared exponential (SE) and $ν$-Matérn kernels, we also show algorithm-independent lower bounds that guarantee the optimality of our algorithm up to polylogarithmic factors. Furthermore, we present a computationally efficient variant of our algorithm using Nyström approximation while maintaining nearly optimal regret guarantees.
匹配关键词: memory efficiency
---

[ACADEMIC - ARXIV]
标题: DECO-MWE: building a linguistic resource of Korean multiword expressions for feature-based sentiment analysis
作者: Jaeho Han, Changhoe Hwang, Seongyong Choi, Gwanghoon Yoo, Eric Laporte, Jeesun Nam
链接: https://arxiv.org/abs/2605.10295v1
完整摘要: This paper aims to construct a linguistic resource of Korean Multiword Expressions for Feature-Based Sentiment Analysis (FBSA): DECO-MWE. Dealing with multiword expressions (MWEs) has been a critical issue in FBSA since many constructs reveal lexical idiosyncrasy. To construct linguistic resources of sentiment MWEs efficiently, we utilize the Local Grammar Graph (LGG) methodology: DECO-MWE is formalized as a Finite-State Transducer that represents lexical-syntactic restrictions on MWEs. In this study, we built a corpus of cosmetics review texts, which show particularly frequent occurrences of MWEs. Based on an empirical examination of the corpus, four types of MWEs have been distinguished. The DECO-MWE thus covers the following four categories: Standard Polarity MWEs (SMWEs), Domain-Dependent Polarity MWEs (DMWEs), Compound Named Entity MWEs (EMWEs) and Compound Feature MWEs (FMWEs). The retrieval performance of the DECO-MWE shows 0.806 f-measure in the test corpus. This study brings a twofold outcome: first, a sizeable general-purpose polarity MWE lexicon, which may be broadly used in FBSA; second, a finite-state methodology adopted in this study to treat domain-dependent MWEs such as idiosyncratic polarity expressions, named entity expressions or feature expressions, and which may be reused in describing linguistic properties of other corpus domains.
匹配关键词: memory efficiency
---

[ACADEMIC - ARXIV]
标题: BROS: Bias-Corrected Randomized Subspaces for Memory-Efficient Single-Loop Bilevel Optimization
作者: Hengrui Zhang, Boao Kong, Engao Zhang, Kun Yuan
链接: https://arxiv.org/abs/2605.10288v1
完整摘要: Stochastic bilevel optimization (SBO) has become a standard framework for hyperparameter learning, data reweighting, representation learning, and data-mixture optimization in deep learning. Existing exact single-loop SBO methods and memory-efficient surrogate SBO methods either create severe memory pressure for large lower-level neural networks or lack competitive convergence guarantees under standard assumptions. In this paper, we propose BROS, a memory-efficient single-loop SBO method with the same convergence rate order as exact single-loop SBO methods. BROS performs lower and auxiliary updates in randomized subspaces with a Rademacher bi-probe correction that recovers an unbiased Hessian-action estimator. We prove that BROS preserves the $\mathcal O(\varepsilon^{-2})$ sample complexity of MA-SOBA for finding an $\varepsilon$-stationary point under only standard assumptions. Experiments on hyper-data cleaning, data-mixture learning, hyper-representation learning, and ViT sample reweighting show that BROS reduces peak memory by up to 44.9% while closely matching full-space baseline performance.
匹配关键词: memory efficiency
---

[ACADEMIC - ARXIV]
标题: Scalable Gaussian process inference via neural feature maps
作者: Anthony Stephenson
链接: https://arxiv.org/abs/2605.10285v1
完整摘要: We present a theoretically grounded Gaussian process framework that leverages neural feature maps to construct expressive kernels. We show that the learned feature map can be interpreted as an optimal low-rank approximation to a Gram matrix derived from an implied RKHS, from which we establish consistency of the GP posterior. We further analyse the spectral properties of the induced kernels and introduce product feature-map kernels to address oversmoothing. This simple yet powerful approach enables fast, scalable, and accurate exact GP inference with minimal upfront work. The flexibility of kernel design supports seamless application to both regression and classification tasks across diverse data modalities, including tabular inputs and structured domains such as images. On benchmark datasets, this approach surpasses pre-existing methods in terms of accuracy and training and prediction efficiency.
匹配关键词: memory efficiency
---

[ACADEMIC - ARXIV]
标题: Positive Alignment: Artificial Intelligence for Human Flourishing
作者: Ruben Laukkonen, Seb Krier, Chloé Bakalar, Shamil Chandaria, Morten Kringelbach, Adam Elwood, Daniel Ford, Fernando Rosas, Maty Bohacek, Matija Franklin, Nenad Tomašev, Stephanie Chan, Verena Rieser, Roma Patel, Michael Levin, Arun Rao
链接: https://arxiv.org/abs/2605.10310v1
完整摘要: Existing alignment research is dominated by concerns about safety and preventing harm: safeguards, controllability, and compliance. This paradigm of alignment parallels early psychology's focus on mental illness: necessary but incomplete. What we call Positive Alignment is the development of AI systems that (i) actively support human and ecological flourishing in a pluralistic, polycentric, context-sensitive, and user-authored way while (ii) remaining safe and cooperative. It is a distinct and necessary agenda within AI alignment research. We argue that several existing failures of alignment (e.g., engagement hacking, loss of human autonomy, failures in truth-seeking, low epistemic humility, error correction, lack of diverse viewpoints, and being primarily reactive rather than proactive) may be better addressed through positive alignment, including cultivating virtues and maximizing human flourishing. We highlight a range of challenges, open questions, and technical directions (e.g., data filtering and upsampling, pre- and post-training, evaluations, collaborative value collection) for different phases of the LLM and agents lifecycle. We end with design principles for promoting disagreement and decentralization through contextual grounding, community customization, continual adaptation, and polycentric governance; that is, many legitimate centers of oversight rather than one institutional or moral chokepoint.
匹配关键词: agent
---

[ACADEMIC - ARXIV]
标题: AgentRx: A Benchmark Study of LLM Agents for Multimodal Clinical Prediction Tasks
作者: Baraa Al Jorf, Farah E. Shamout
链接: https://arxiv.org/abs/2605.10286v1
完整摘要: Building effective clinical decision support systems requires the synthesis of complex heterogeneous multimodal data. Such modalities include temporal electronic health records data, medical images, radiology reports, and clinical notes. Large language model (LLM)-based agents have shown impressive performance in various healthcare tasks, especially those involving textual modalities. Considering the fragmentation of healthcare data across hospital systems, collaborative agent frameworks present a promising direction to mitigate data sharing challenges. However, the effectiveness of LLM agents for multimodal clinical risk prediction remains largely unexamined. In this work, we conduct a systematic evaluation of LLM-based agents for clinical prediction tasks using large-scale real-world data. We assess performance in unimodal and multimodal settings and quantify performance gaps between single agent and multi-agent systems. Our findings highlight that single agent frameworks outperform naive multi-agent systems, are better at handling multimodal data, and are better calibrated. This underscores a critical need for improving multi-agent collaboration to better handle heterogeneous inputs. By open-sourcing our code and evaluation framework, this work offers a new benchmark to support future developments relating to agentic systems in healthcare.
匹配关键词: agent
---

[ACADEMIC - ARXIV]
标题: MemReread: Enhancing Agentic Long-Context Reasoning via Memory-Guided Rereading
作者: Baibei Ji, Xiaoyang Weng, Juntao Li, Zecheng Tang, Yihang Lou, Min Zhang
链接: https://arxiv.org/abs/2605.10268v1
完整摘要: To tackle long-context reasoning tasks without the quadratic complexity of standard attention mechanisms, approaches based on agent memory have emerged, which typically maintain a dynamically updated memory when linearly processing document chunks. To mitigate the potential loss of latent evidence in this memorize-while-reading paradigm, recent works have integrated retrieval modules that allow agents to recall information previously discarded during memory overwriting. However, retrieval-based recall suffers from both evidence loss during memory formation and interference induced by invalid queries. To overcome these limitations, we propose MemReread. Built upon streaming reading, MemReread circumvents intermediate retrieval. It triggers question decomposition and rereading when the final memory is insufficient, enabling the recovery of indirect facts that were prematurely discarded. This design supports non-linear reasoning while preserving the inherent logical flow of document comprehension. To further enhance practicality, we introduce a reinforcement learning framework that enhances length extrapolation capability while dynamically determining the number of rereading passes based on task complexity, thereby flexibly controlling computational overhead. Extensive experiments demonstrate that MemReread consistently outperforms baseline frameworks on long-context reasoning tasks, while maintaining linear time complexity with respect to context length.
匹配关键词: agent
---

[ACADEMIC - ARXIV]
标题: Towards Autonomous Railway Operations: A Semi-Hierarchical Deep Reinforcement Learning Approach to the Vehicle Rescheduling Problem
作者: Alberto Castagna, Stefan Zahlner, Adrian Egli, Christian Eichenberger, Daniel Boos, Manuel Meyer, Anton Fuxjager
链接: https://arxiv.org/abs/2605.10257v1
完整摘要: Managing disruptions in railway traffic management is a major challenge. Rising traffic density and infrastructure limits increase complexity, making the Vehicle Routing and Scheduling Problem (VRSP) difficult to solve reliably and in real time. While Operational Research (OR) methods are widely used, most dispatching still relies on human expertise due to the problem's exponential combinatorial complexity. Reinforcement Learning (RL) has gained attention for its potential in multi-agent coordination, but existing RL approaches often underperform OR methods and struggle to scale in dense rail networks. This paper addresses this gap from a machine learning perspective by introducing a semi-hierarchical RL formulation tailored to operational railway constraints. The method separates dispatching from routing through dedicated action and observation spaces, enabling policies to specialise in distinct decision scopes and addressing the imbalance between rare dispatch decisions and frequent routing updates. The approach is evaluated on the Flatland-RL simulator across five difficulty levels and 50 random seeds, with 7 to 80 trains. Results show substantially improved coordination, resource utilisation, and robustness compared with heuristic baselines and monolithic RL, nearly doubling the number of trains reaching their destinations, while keeping deadlock rates below 5% and adaptively sequencing, delaying, or cancelling trains under heavy congestion.
匹配关键词: agent
---

[ACADEMIC - ARXIV]
标题: Beyond Autonomy: A Dynamic Tiered AgentRunner Framework for Governable and Resilient Enterprise AI Execution
作者: Kai Pan, Rong Hou
链接: https://arxiv.org/abs/2605.10223v1
完整摘要: Current large language model agent frameworks prioritize autonomy but lack the governability mechanisms required for enterprise deployment. High-risk write operations proceed without independent review, complex tasks lack acceptance verification, and computational resources are allocated uniformly regardless of risk level. We propose the Dynamic Tiered AgentRunner, a controlled execution protocol distilled from a production-grade multi-tenant SaaS platform. The framework introduces three core mechanisms: (1) Risk-Adaptive Tiering that dynamically allocates computational resources and review intensity based on task risk profiles, achieving Pareto-optimal trade-offs between safety and efficiency; (2) Separation of Powers architecture where proposal, review, execution, and verification are performed by independent agents with physically isolated boundaries; and (3) Resilience-by-Design through a Verifier-Recovery closed loop that treats failure as a first-class system state. We formalize the tier selectio
匹配关键词: agent
---

[ACADEMIC - ARXIV]
标题: Extending Confidence-Based Text2Cypher with Grammar and Schema Aware Filtering
作者: Makbule Gulcin Ozsoy
链接: https://arxiv.org/abs/2605.10318v1
完整摘要: Large language models (LLMs) allow users to query databases using natural language by translating questions into executable queries. Despite strong progress on tasks such as Text2SQL, Text2SPARQL, and Text2Cypher, most existing methods focus on better prompting, fine-tuning, or iterative refinement. However, they often do not explicitly enforce structural constraints, such as syntactic validity and schema consistency. This can reduce reliability, since generated queries must satisfy both syntax rules and database schema constraints to be executable. In this work, we study how structured constraints can be used in test-time inference for Text2Cypher. We focus on post-generation validation to improve query correctness. We extend a confidence-based inference framework with a sequential filtering process that combines confidence scoring, grammar validation, and schema constraints before final aggregation. This lets us analyze how different constraint types affect generated queries. Our experiments with two instruction-tuned models show that grammar-based filtering improves syntactic validity. Schema-aware filtering further improves execution quality by enforcing consistency with the database structure. However, stronger filtering also increases the number of empty predictions and reduces execution coverage. Overall, we show that adding simple structural checks at test time improves the reliability of Text2Cypher generation, and we provide a clearer view of how syntax and schema constraints contribute differently.
匹配关键词: tool use
---

[ACADEMIC - ARXIV]
标题: Signature Approach for Contextual Bandits with Nonlinear and Path-dependent Rewards
作者: Xin Guo, Grace He, Xinyu Li
链接: https://arxiv.org/abs/2605.10313v1
完整摘要: We study contextual bandits with nonlinear and path-dependent rewards through a novel signature-transform-based approach. Leveraging the universal nonlinearity property of signatures, we approximate continuous path-dependent reward functionals by linear functionals in the signature space. This representation enables the use of efficient linear contextual bandit methods while preserving expressive sequential structure. Building on this framework, we propose \texttt{DisSigUCB}, a signature-based disjoint upper confidence bound (UCB) algorithm. Under boundedness and non-degeneracy assumptions, we prove a high-probability data-dependent sublinear regret bound of order \(\tilde{\mathcal O}(\sqrt{(d+m)KT})\) where \(d\) is the context dimension and \(m\) is the signature feature dimension. Synthetic experiments and numerical applications on temperature sensor monitoring, sleep-stage classification, and hospital nurse staffing demonstrate that \texttt{DisSigUCB} consistently outperforms classical linear and kernelized contextual bandit baselines in nonlinear and path-dependent settings.
匹配关键词: tool use
---

[ACADEMIC - ARXIV]
标题: PaMoSplat: Part-Aware Motion-Guided Gaussian Splatting for Dynamic Scene Reconstruction
作者: Yinan Deng, Jianyu Dou, Jiahui Wang, Jingyu Zhao, Yi Yang, Yufeng Yue
链接: https://arxiv.org/abs/2605.10307v1
完整摘要: Dynamic scene reconstruction represents a fundamental yet demanding challenge in computer vision and robotics. While recent progress in 3DGS-based methods has advanced dynamic scene modeling, obtaining high-fidelity rendering and accurate tracking in scenarios with substantial, intricate motions remains significantly challenging. To address these challenges, we propose PaMoSplat, a novel dynamic Gaussian splatting framework incorporating part awareness and motion priors. Our approach is grounded in two key observations: 1) Parts serve as primitives for scene deformation, and 2) Motion cues from optical flow can effectively guide part motion. Specifically, PaMoSplat initializes by lifting multi-view segmentation masks into 3D space via graph clustering, establishing coherent Gaussian parts. For subsequent timestamps, we leverage a differential evolutionary algorithm to estimate the rigid motion of these parts using multi-view optical flow cues, providing a robust warm-start for further optimization. Additionally, PaMoSplat introduces an adaptive iteration count mechanism, internal learnable rigidity, and flow-supervised rendering loss to accelerate and optimize the training process. Comprehensive evaluations across diverse scenes, including real-world environments, demonstrate that PaMoSplat delivers superior rendering quality, improved tracking precision, and faster convergence compared to existing methods. Furthermore, it enables multiple part-level downstream applications, such as 4D scene editing.
匹配关键词: tool use
---

[ACADEMIC - ARXIV]
标题: Nearly-Optimal Algorithm for Adversarial Kernelized Bandits
作者: Shogo Iwazaki
链接: https://arxiv.org/abs/2605.10299v1
完整摘要: This paper studies kernelized bandits (also known as Gaussian process bandits) in an adversarial environment, where the reward functions in a known reproducing kernel Hilbert space (RKHS) may be adversarially chosen at each round. We show that the exponential-weight algorithm achieves $\tilde{O}(\sqrt{T γ_T})$ adversarial regret, where $T$ and $γ_T$ denote the number of total rounds and the maximum information gain, respectively. For squared exponential (SE) and $ν$-Matérn kernels, we also show algorithm-independent lower bounds that guarantee the optimality of our algorithm up to polylogarithmic factors. Furthermore, we present a computationally efficient variant of our algorithm using Nyström approximation while maintaining nearly optimal regret guarantees.
匹配关键词: tool use
---

[ACADEMIC - ARXIV]
标题: Set Prediction for Next-Day Active Fire Forecasting
作者: Yuchen Bai, Georgios Athanasiou, Xin Yu, Diogenis Antonopoulos, Ioannis Papoutsis, Stijn Hantson, Nuno Carvalhais
链接: https://arxiv.org/abs/2605.10298v1
完整摘要: Accurate next-day active fire forecasts can support early warning, disaster response, forest risk assessment, and downstream estimation of fire-related carbon emissions. Existing machine learning approaches to wildfire forecasting typically predict wildfire danger or fire probability on kilometre-scale daily grids, which is useful for regional warning but does not directly represent localized fire events. We propose Wildfire Ignition Set Predictor (WISP), a query-based model that reformulates next-day active fire forecasting as point-set prediction. From 48 hours of covariates including meteorology, satellite vegetation products, static land, and fire history, WISP predicts a fixed-size ranked set of future active fire cluster centres on a 375 m grid across globally distributed regions. The model is trained end-to-end with Hungarian matching; to address the conflicting roles of the classification score in assignment, ranking, and query activation, we use asymmetric classification-localization weighting in matching and loss. We further construct a globally distributed, hourly, multi-source benchmark for this task. On a held-out test set spanning fire regions worldwide, the best WISP variant achieves 38.2% average precision (AP) for ranked fire-centre detections, covers 53.4% of fire cluster mass weighted by fire radiative power (FRP), and localizes 54.1% of observed clusters within 5 km. These results establish sparse set prediction as a viable formulation for high-resolution wildfire forecasting and provide a benchmark for future work in this regime.
匹配关键词: tool use
---

[ACADEMIC - ARXIV]
标题: Relative Score Policy Optimization for Diffusion Language Models
作者: Zichao Yu, Shengze Xu, Bingqing Jiang, Wenyi Zhang, Difan Zou
链接: https://arxiv.org/abs/2605.10218v1
完整摘要: Diffusion large language models (dLLMs) offer a promising route to parallel and efficient text generation, but improving their reasoning ability requires effective post-training. Reinforcement learning with verifiable rewards (RLVR) is a natural choice for this purpose, yet its application to dLLMs is hindered by the absence of tractable sequence-level log-ratios, which are central to standard policy optimization. The lack of tractable sequence-level log-ratios forces existing methods to rely on high-variance ELBO-based approximations, where high verifier rewards can amplify inaccurate score estimates and destabilize RL training. To overcome this issue, we propose \textbf{R}elative \textbf{S}core \textbf{P}olicy \textbf{O}ptimization (RSPO), a simple RLVR method that uses verifiable rewards to calibrate noisy likelihood estimates in dLLMs. The core of our algorithm relies on a key observation: a reward advantage can be interpreted not only as an update direction, but also as a target for the relative log-ratio between the current and reference policies. Accordingly, RSPO calibrates this noisy relative log-ratio estimate by comparing its reward advantage with the reward-implied target relative log-ratio, updating the policy according to the gap between the current estimate and the target rather than the raw advantage alone. Experiments on mathematical reasoning and planning benchmarks show that RSPO yields especially strong gains on planning tasks and competitive mathematical-reasoning performance.
匹配关键词: planning
---

[ACADEMIC - ARXIV]
标题: HeteroGenManip: Generalizable Manipulation For Heterogeneous Object Interactions
作者: Zhenhao Shen, Zeming Yang, Yue Chen, Yuran Wang, Shengqiang Xu, Mingleyang Li, Hao Dong, Ruihai Wu
链接: https://arxiv.org/abs/2605.10201v1
完整摘要: Generalizable manipulation involving cross-type object interactions is a critical yet challenging capability in robotics. To reliably accomplish such tasks, robots must address two fundamental challenges: ``where to manipulate'' (contact point localization) and ``how to manipulate'' (subsequent interaction trajectory planning). Existing foundation-model-based approaches often adopt end-to-end learning that obscures the distinction between these stages, exacerbating error accumulation in long-horizon tasks. Furthermore, they typically rely on a single uniform model, which fails to capture the diverse, category-specific features required for heterogeneous objects. To overcome these limitations, we propose HeteroGenManip, a task-conditioned, two-stage framework designed to decouple initial grasp from complex interaction execution. First, Foundation-Correspondence-Guided Grasp module leverages structural priors to align the initial contact state, thereby significantly reducing the pose uncertainty of grasping. Subsequently, Multi-Foundation-Model Diffusion Policy (MFMDP) routes objects to category-specialized foundation models, integrating fine-grained geometric information with highly-variable part features via a dual-stream cross-attention mechanism. Experimental evaluations demonstrate that HeteroGenManip achieves robust intra-category shape and pose generalization. The framework achieves an average 31\% performance improvement in simulation tasks with broad type setting, alongside a 36.7\% gain across four real-world tasks with different interaction types.
匹配关键词: planning
---

[ACADEMIC - ARXIV]
标题: Plan in Sandbox, Navigate in Open Worlds: Learning Physics-Grounded Abstracted Experience for Embodied Navigation
作者: Zhixuan Shen, Jiawei Du, Ziyu Guo, Han Luo, Lilan Peng, Joey Tianyi Zhou, Haonan Luo, Tianrui Li
链接: https://arxiv.org/abs/2605.10118v1
完整摘要: Vision-Language Models (VLMs) have demonstrated exceptional general reasoning capabilities. However, their performance in embodied navigation remains hindered by a scarcity of aligned open-world vision and robot control data. Despite simulators providing a cost-effective alternative for data collection, the inherent reliance on photorealistic simulations often limits the transferability of learned policies. To this end, we propose \textit{\textbf{S}andbox-\textbf{A}bstracted \textbf{G}rounded \textbf{E}xperience} (\textbf{\textit{SAGE}}), a framework that enables agents to learn within a physics-grounded semantic abstraction rather than a photorealistic simulation, mimicking the human capacity for mental simulation where plans are rehearsed in simplified physics abstractions before execution. \textit{SAGE} system operates via three synergistic phases: (1) \textit{Genesis}: constructing diverse, physics-constrained semantic environments to bootstrap experience; (2) \textit{Evolution}: distilling experiences through Reinforcement Learning (RL), utilizing a novel asymmetric adaptive clipping mechanism to stabilize updates; (3) \textit{Navigation}: bridging the abstract policy to open-world control. We demonstrate that \textit{SAGE} significantly improves planner-assisted embodied navigation, achieving a 53.21\% LLM-Match Success Rate on A-EQA (+9.7\% over baseline), while showing encouraging transfer to physical indoor robot deployment.
匹配关键词: planning
---

[ACADEMIC - ARXIV]
标题: From Single-Step Edit Response to Multi-Step Molecular Optimization
作者: Haojie Rao, Kun Li, Yida Xiong, Jiameng Chen, Wenbin Hu, Yizhen Zheng, Jiajun Yu, Duanhua Cao
链接: https://arxiv.org/abs/2605.10035v1
完整摘要: Conditional molecular optimization aims to edit a molecule to realize a specified property shift. In practice, structurally similar molecule data is scarce, while decisions are inherently action-level: at each step, the system must select one local structural edit from a candidate set that is strictly filtered by chemical feasibility rules. This level mismatch between supervision and decision makes oracle-in-the-loop search unstable in molecular optimization. Regressing on property differences between molecule pairs improves data efficiency but relies on oracle-in-the-loop search, entangling transformation effects with global context and providing limited guidance for selecting the next feasible edit, often resorting to oracle-in-the-loop search. For this reason, we propose a response-oriented discrete edit optimization approach comprising two tightly coupled components: a single-step molecular edit response predictor (SMER) and a multi-step planner that composes local predictions into optimization trajectories via guided tree search (SMER-Opt). The approach learns a directional evaluation model over edit actions to support constraint-aware planning. It mines weakly related molecule pairs and decomposes their structural differences into minimal edit units, turning endpoint property annotations into process-level supervision and yielding reusable, transferable action primitives. A directional edit evaluator then scores feasible candidate edits by their likelihood of moving the molecule toward the desired property change, substantially reducing dependence on external evaluator queries at decision time. Code is available at https://anonymous.4open.science/r/SMER.
匹配关键词: planning
---

[ACADEMIC - ARXIV]
标题: Beyond Self-Play and Scale: A Behavior Benchmark for Generalization in Autonomous Driving
作者: Aron Distelzweig, Faris Janjoš, Andreas Look, Anna Rothenhäusler, Daniel Jost, Oliver Scheel, Raghu Rajan, Daphne Cornelisse, Eugene Vinitsky, Joschka Boedecker
链接: https://arxiv.org/abs/2605.10034v1
完整摘要: Recent Autonomous Driving (AD) works such as GigaFlow and PufferDrive have unlocked Reinforcement Learning (RL) at scale as a training strategy for driving policies. Yet such policies remain disconnected from established benchmarks, leaving the performance of large-scale RL for driving on standardized evaluations unknown. We present BehaviorBench -- a comprehensive test suite that closes this gap along three axes: Evaluation, Complexity, and Behavior Diversity. In terms of Evaluation, we provide an interface connecting PufferDrive to nuPlan, which, for the first time, enables policies trained via RL at scale to be evaluated on an established planning benchmark for autonomous driving. Complementarily, we offer an evaluation framework that allows planners to be benchmarked directly inside the PufferDrive simulation, at a fraction of the time. Regarding Complexity, we observe that today's standardized benchmarks are so simple that near-perfect scores are achievable by straight lane following with collision checking. We extract a meaningful, interaction-rich split from the Waymo Open Motion Dataset (WOMD) on which strong performance is impossible without multi-agent reasoning. Lastly, we address Behavior Diversity. Existing benchmarks commonly evaluate planners against a single rule-based traffic model, the Intelligent Driver Model (IDM). We provide a diverse suite of interactive traffic agents to stress-test policies under heterogeneous behaviors, beyond just using IDM. Overall, our benchmarking analysis uncovers the following insight: despite learning interactive behaviors in an emergent manner, policies trained via pure self-play under standard reward functions overfit to their training opponents and fail to generalize to other traffic agent behaviors. Building on this observation, we propose a hybrid planner that combines a PPO policy with a rule-based planner.
匹配关键词: planning
---

[ACADEMIC - ARXIV]
标题: Auto-Rubric as Reward: From Implicit Preferences to Explicit Multimodal Generative Criteria
作者: Juanxi Tian, Fengyuan Liu, Jiaming Han, Yilei Jiang, Yongliang Wu, Yesheng Liu, Haodong Li, Furong Xu, Wanhua Li
链接: https://arxiv.org/abs/2605.08354v1
完整摘要: Aligning multimodal generative models with human preferences demands reward signals that respect the compositional, multi-dimensional structure of human judgment. Prevailing RLHF approaches reduce this structure to scalar or pairwise labels, collapsing nuanced preferences into opaque parametric proxies and exposing vulnerabilities to reward hacking. While recent Rubrics-as-Reward (RaR) methods attempt to recover this structure through explicit criteria, generating rubrics that are simultaneously reliable, scalable, and data-efficient remains an open problem. We introduce Auto-Rubric as Reward (ARR), a framework that reframes reward modeling from implicit weight optimization to explicit, criteria-based decomposition. Before any pairwise comparison, ARR externalizes a VLM's internalized preference knowledge as prompt-specific rubrics, translating holistic intent into independently verifiable quality dimensions. This conversion of implicit preference structure into inspectable, interpretable constraints substantially suppresses evaluation biases including positional bias, enabling both zero-shot deployment and few-shot conditioning on minimal supervision. To extend these gains into generative training, we propose Rubric Policy Optimization (RPO), which distills ARR's structured multi-dimensional evaluation into a robust binary reward, replacing opaque scalar regression with rubric-conditioned preference decisions that stabilize policy gradients. On text-to-image generation and image editing benchmarks, ARR-RPO outperforms pairwise reward models and VLM judges, demonstrating that explicitly externalizing implicit preference knowledge into structured rubrics achieves more reliable, data-efficient multimodal alignment, revealing that the bottleneck is the absence of a factorized interface, not a deficit of knowledge.
匹配关键词: RLHF
---

[ACADEMIC - ARXIV]
标题: Interpreting Reinforcement Learning Agents with Susceptibilities
作者: Chris Elliott, Einar Urdshals, David Quarel, Daniel Murfet
链接: https://arxiv.org/abs/2605.08007v1
完整摘要: Susceptibilities are a technique for neural network interpretability that studies the response of posterior expectation values of observables to perturbations of the loss. We generalize this construction to the setting of the regret in deep reinforcement learning and investigate the utility of susceptibilities in a simple gridworld model that nevertheless exhibits non-trivial stagewise development. We argue that susceptibilities reveal internal features of the development of the model in parameter space that one cannot detect purely by studying the development of the learned policy. We validate these results with activation-steering, and discuss the framework's extension to RLHF post-training.
匹配关键词: RLHF
---

[ACADEMIC - ARXIV]
标题: Seed Hijacking of LLM Sampling and Quantum Random Number Defense
作者: Ziyang You, Xiaoke Yang, Zhanling Fan, Feng Guo, Xiaogen Zhou, Xuxing Lu
链接: https://arxiv.org/abs/2605.08313v1
完整摘要: Large language models (LLMs) rely on deterministic pseudorandom number generators (PRNGs) for autoregressive sampling, creating a critical supply-chain attack surface overlooked by existing defenses. We present SeedHijack, a backdoor attack that manipulates PRNG outputs to force attacker-specified token selection without altering model logits. In a 540-trial benchmark on GPT-2 (124M), the attack achieves 99.6% exact token injection across 9 sampling configurations; it reaches 100% success on four aligned models (1.5B-7B, RLHF/SFT/reasoning distillation) and bypasses all alignment methods tested in this work. We further propose a defense based on a hardware quantum random number generator (QRNG), which neutralizes the attack in our evaluated threat model with negligible median overhead (+0.6% latency, +7.7 MB memory). Our work identifies a critical sampling-layer vulnerability and provides a practical, deployable QRNG-based defense.
匹配关键词: RLHF
---

[ACADEMIC - ARXIV]
标题: Diffusion-APO: Trajectory-Aware Direct Preference Alignment for Video Diffusion Transformers
作者: Jingyuan Zhu, Biaolong Chen, Le Zhang, Aixi Zhang, Hao Jiang, Pipei Huang
链接: https://arxiv.org/abs/2605.07503v1
完整摘要: Efficiently aligning large-scale video diffusion models with human intent requires a scalable and trajectory-aware pathway that bridges the inherent discrepancy between training noise distributions and practical inference trajectories. While existing paradigms such as Direct Preference Optimization (DPO) and Group Relative Policy Optimization (GRPO) attempt to address this, they are often hindered by either reliance on bias-prone, complex reward models or suboptimal timestep sampling. In this paper, we propose Diffusion-APO (Aligned Preference Optimization), a trajectory-aware algorithm that resolves this misalignment by synchronizing training noise with inference-time denoising paths to maximize gradient signal efficacy. To translate this algorithmic innovation into a practical solution, we introduce a unified and modular RLHF framework that integrates online ranking, half-online anchoring, offline refinement, and distillation-aware drift correction. This framework enables flexible, multi-stage preference alignment across diverse data and computational constraints without relying on scalar-reward-based policy gradients. Through extensive experiments, we demonstrate that Diffusion-APO consistently outperforms standard baselines in visual quality and instruction following, while effectively preserving generative fidelity during model acceleration, providing a robust, end-to-end pathway for scalable video diffusion alignment.
匹配关键词: RLHF
---

[ACADEMIC - ARXIV]
标题: Topology-Enhanced Alignment for Large Language Models: Trajectory Topology Loss and Topological Preference Optimization
作者: Yurui Pan, Ke Xu, Bo Peng
链接: https://arxiv.org/abs/2605.07172v1
完整摘要: Alignment of large language models (LLMs) via SFT and RLHF/DPO typically ignores the global geometry of the representation space, relying instead on local token likelihoods or scalar scores. We view generation as tracing a semantic trajectory in hidden space and propose a topology-enhanced alignment framework that regularizes these trajectories using 0-dimensional persistent homology. First, for SFT, we introduce Trajectory Topology Loss (TTL). Treating prompt and gold-answer embeddings as a mixed point cloud, we use a 0D persistent homology algorithm to extract "prompt-answer bridges." TTL aligns the model's actual update direction with these topological bridges rather than arbitrary directions. Second, for DPO, we propose Topological Preference Optimization (TPO). TPO constructs topic-specific semantic preference vectors and aligns the improvement direction between rejected and chosen responses with these vectors in an intermediate hidden layer. We also introduce a dynamic weighting scheme to balance DPO and TPO losses. Evaluating on Qwen2.5-7B-Instruct using UltraChat and Anthropic HH-RLHF, our topology-enhanced objectives consistently outperform strong non-topological baselines (e.g., per-example, nearest-neighbor, random regularizers) on automatic preference metrics and LLM-judge evaluations, while maintaining or improving toxicity. Results show persistent homology and trajectory geometry offer a promising direction for controllable alignment.
匹配关键词: RLHF
---

[ACADEMIC - ARXIV]
标题: G-Zero: Self-Play for Open-Ended Generation from Zero Data
作者: Chengsong Huang, Haolin Liu, Tong Zheng, Runpeng Dai, Langlin Huang, Jinyuan Li, Zongxia Li, Zhepei Wei, Yu Meng, Jiaxin Huang
链接: https://arxiv.org/abs/2605.09959v1
完整摘要: Self-evolving LLMs excel in verifiable domains but struggle in open-ended tasks, where reliance on proxy LLM judges introduces capability bottlenecks and reward hacking. To overcome this, we introduce G-Zero, a verifier-free, co-evolutionary framework for autonomous self-improvement. Our core innovation is Hint-$δ$, an intrinsic reward that quantifies the predictive shift between a Generator model's unassisted response and its response conditioned on a self-generated hint. Using this signal, a Proposer model is trained via GRPO to continuously target the Generator's blind spots by synthesizing challenging queries and informative hints. The Generator is concurrently optimized via DPO to internalize these hint-guided improvements. Theoretically, we prove a best-iterate suboptimality guarantee for an idealized standard-DPO version of G-Zero, provided that the Proposer induces sufficient exploration coverage and the data filteration keeps pseudo-label score noise low. By deriving supervision entirely from internal distributional dynamics, G-Zero bypasses the capability ceilings of external judges, providing a scalable, robust pathway for continuous LLM self-evolution across unverifiable domains.
匹配关键词: DPO
---

[ACADEMIC - ARXIV]
标题: Relations Are Channels: Knowledge Graph Embedding via Kraus Decompositions
作者: Sayan Kumar Chaki
链接: https://arxiv.org/abs/2605.10317v1
完整摘要: Knowledge graph embedding (KGE) models typically represent each relation as an operator on entity embeddings. In this work, we identify three structural axioms that any principled relation operator must satisfy, linearity, trace preservation, and complete positivity, and show that they characterize a Kraus channel structure via the Kraus representation theorem. The completeness constraint defining this family is equivalent to these axioms, providing a principled foundation rather than an externally imposed condition. Under this formulation, most existing operator-based KGE models are recoverable as special cases with Kraus rank $κ= 1$ under specific embedding choices. We further generalize this characterization to arbitrary metric geometries by introducing \mbox{w-Kraus} channels, which satisfy completeness by construction within their respective spaces. Building on this theory, we propose \textsc{KrausKGE}, a principled KGE model that naturally handles $1$-to-$N$ and $N$-to-$N$ relations, supports $k$-hop reasoning without requiring explicit path encoders, and eliminates the need for norm constraints on entity embeddings. Additionally, our framework yields the first theoretically grounded per-relation complexity measure in the KGE literature, with a provable lower bound in terms of the empirical relation matrix rank. Empirical evaluation demonstrates that \textsc{KrausKGE} consistently outperforms strong baselines on $N$-to-$N$ relations, with performance gains that increase monotonically with relation fan-out, in alignment with theoretical predictions.
匹配关键词: alignment
---

[ACADEMIC - ARXIV]
标题: Positive Alignment: Artificial Intelligence for Human Flourishing
作者: Ruben Laukkonen, Seb Krier, Chloé Bakalar, Shamil Chandaria, Morten Kringelbach, Adam Elwood, Daniel Ford, Fernando Rosas, Maty Bohacek, Matija Franklin, Nenad Tomašev, Stephanie Chan, Verena Rieser, Roma Patel, Michael Levin, Arun Rao
链接: https://arxiv.org/abs/2605.10310v1
完整摘要: Existing alignment research is dominated by concerns about safety and preventing harm: safeguards, controllability, and compliance. This paradigm of alignment parallels early psychology's focus on mental illness: necessary but incomplete. What we call Positive Alignment is the development of AI systems that (i) actively support human and ecological flourishing in a pluralistic, polycentric, context-sensitive, and user-authored way while (ii) remaining safe and cooperative. It is a distinct and necessary agenda within AI alignment research. We argue that several existing failures of alignment (e.g., engagement hacking, loss of human autonomy, failures in truth-seeking, low epistemic humility, error correction, lack of diverse viewpoints, and being primarily reactive rather than proactive) may be better addressed through positive alignment, including cultivating virtues and maximizing human flourishing. We highlight a range of challenges, open questions, and technical directions (e.g., data filtering and upsampling, pre- and post-training, evaluations, collaborative value collection) for different phases of the LLM and agents lifecycle. We end with design principles for promoting disagreement and decentralization through contextual grounding, community customization, continual adaptation, and polycentric governance; that is, many legitimate centers of oversight rather than one institutional or moral chokepoint.
匹配关键词: alignment
---

[ACADEMIC - ARXIV]
标题: Drum Synthesis from Expressive Drum Grids via Neural Audio Codecs
作者: Konstantinos Soiledis, Maximos Kaliakatsos-Papakostas, Dimos Makris, Konstantinos Tsamis
链接: https://arxiv.org/abs/2605.10281v1
完整摘要: Generating realistic drum audio directly from symbolic representations is a challenging task at the intersection of music perception and machine learning. We propose a system that transforms an expressive drum grid, a time-aligned MIDI representation with microtiming and velocity information, into drum audio by predicting discrete codes of a neural audio codec. Our approach uses a Transformer-based model to map the drum grid input to a sequence of codec tokens, which are then converted to waveform audio via a pre-trained codec decoder. We experiment with multiple state-of-the-art neural codecs, namely EnCodec, DAC, and X-Codec, to assess how the choice of audio representation impacts the quality of the generated drums. The system is trained and evaluated on the Expanded Groove MIDI Dataset, E-GMD, a large collection of human drum performances with paired MIDI and audio. We evaluate the fidelity and musical alignment of the generated audio using objective metrics. Overall, our results establish codec-token prediction as an effective route for drum grid-to-audio generation and provide practical insights into selecting audio tokenizers for percussive synthesis.
匹配关键词: alignment
---

[ACADEMIC - ARXIV]
标题: IndustryBench: Probing the Industrial Knowledge Boundaries of LLMs
作者: Songlin Bai, Xintong Wang, Linlin Yu, Bin Chen, Zhiang Xu, Yuyang Sheng, Changtong Zan, Xiaofeng Zhu, Yizhe Zhang, Jiru Li, Mingze Guo, Ling Zou, Yalong Li, Chengfu Huo, Liang Ding
链接: https://arxiv.org/abs/2605.10267v1
完整摘要: In industrial procurement, an LLM answer is useful only if it survives a standards check: recommended material must match operating condition, every parameter must respect a regulated threshold, and no procedure may contradict a safety clause. Partial correctness can mask safety-critical contradictions that aggregate LLM benchmarks rarely capture. We introduce IndustryBench, a 2,049-item benchmark for industrial procurement QA in Chinese, grounded in Chinese national standards (GB/T) and structured industrial product records, organized by seven capability dimensions, ten industry categories, and panel-derived difficulty tiers, with item-aligned English, Russian, and Vietnamese renderings. Our construction pipeline rejects 70.3% of LLM-generated candidates at a search-based external-verification stage, calibrating how unreliable industrial QA remains after LLM-only filtering.Our evaluation decouples raw correctness, scored by a Qwen3-Max judge validated at $κ_w = 0.798$ against a domain expert, from a separate safety-violation (SV) check against source texts. Across 17 models in Chinese and an 8-model intersection over four languages, we find: (i) the best system reaches only 2.083 on the 0--3 rubric, leaving substantial headroom; (ii) Standards & Terminology is the most persistent capability weakness and survives item-aligned translation; (iii) extended reasoning lowers safety-adjusted scores for 12 of 13 models, primarily by introducing unsupported safety-critical details into longer final answers; and (iv) safety-violation rates reshuffle the leaderboard -- GPT-5.4 climbs from rank 6 to rank 3 after SV adjustment, while Kimi-k2.5-1T-A32B drops seven positions.Industrial LLM evaluation therefore requires source-grounded, safety-aware diagnosis rather than aggregate accuracy. We release IndustryBench with all prompts, scoring scripts, and dataset documentation.
匹配关键词: alignment
---

[ACADEMIC - ARXIV]
标题: E-TCAV: Formalizing Penultimate Proxies for Efficient Concept Based Interpretability
作者: Hasib Aslam, Muhammad Ali Chattha, Muhammad Taha Mukhtar, Muhammad Imran Malik, Andreas Dengel, Sheraz Ahmed
链接: https://arxiv.org/abs/2605.10261v1
完整摘要: TCAV (Testing with Concept Activation Vectors) is an interpretability method that assesses the alignment between the internal representations of a trained neural network and human-understandable, high-level concepts. Though effective, TCAV suffers from significant computational overhead, inter-layer disagreement of TCAV scores, and statistical instability. This work takes a step toward addressing these challenges by introducing E-TCAV, a framework for efficient approximation of TCAV scores, which is based on extensive investigation into three key aspects of the TCAV methodology: 1) the effect of latent classifiers on the stability of TCAV scores, 2) the inter-layer agreement of TCAV scores, and 3) the use of the penultimate layer as a fast proxy for earlier layers for TCAV computation. To ensure a solid foundation for E-TCAV, we conduct extensive evaluations across four different architectures and five datasets, encompassing problems from both computer vision and natural language domains. Our results show that the layers in the final block of the neural network strongly agree with the penultimate layer in terms of the TCAV scores, and the commonly observed variance of the TCAV scores can be attributed to the choice of the latent classifier. Leveraging this inter-layer agreement and the degeneracy of directional sensitivities at the penultimate layer, E-TCAV guarantees linearly scaling speed-ups with respect to the network's size and the number of evaluation samples, marking a step towards efficient model debugging and real-time concept-guided training.
匹配关键词: alignment
---

[ACADEMIC - ARXIV]
标题: Relations Are Channels: Knowledge Graph Embedding via Kraus Decompositions
作者: Sayan Kumar Chaki
链接: https://arxiv.org/abs/2605.10317v1
完整摘要: Knowledge graph embedding (KGE) models typically represent each relation as an operator on entity embeddings. In this work, we identify three structural axioms that any principled relation operator must satisfy, linearity, trace preservation, and complete positivity, and show that they characterize a Kraus channel structure via the Kraus representation theorem. The completeness constraint defining this family is equivalent to these axioms, providing a principled foundation rather than an externally imposed condition. Under this formulation, most existing operator-based KGE models are recoverable as special cases with Kraus rank $κ= 1$ under specific embedding choices. We further generalize this characterization to arbitrary metric geometries by introducing \mbox{w-Kraus} channels, which satisfy completeness by construction within their respective spaces. Building on this theory, we propose \textsc{KrausKGE}, a principled KGE model that naturally handles $1$-to-$N$ and $N$-to-$N$ relations, supports $k$-hop reasoning without requiring explicit path encoders, and eliminates the need for norm constraints on entity embeddings. Additionally, our framework yields the first theoretically grounded per-relation complexity measure in the KGE literature, with a provable lower bound in terms of the empirical relation matrix rank. Empirical evaluation demonstrates that \textsc{KrausKGE} consistently outperforms strong baselines on $N$-to-$N$ relations, with performance gains that increase monotonically with relation fan-out, in alignment with theoretical predictions.
匹配关键词: preference learning
---

[ACADEMIC - ARXIV]
标题: Active Tabular Augmentation via Policy-Guided Diffusion Inpainting
作者: Zheyu Zhang, Shuo Yang, Bardh Prenkaj, Gjergji Kasneci
链接: https://arxiv.org/abs/2605.10315v1
完整摘要: Generative tabular augmentation is appealing in data-scarce domains, yet the prevailing focus on distributional fidelity does not reliably translate into better downstream models. We formalize a fidelity-utility gap: common generative objectives prioritize distributional plausibility, whereas augmentation succeeds only when injected samples reduce the current learner's held-out evaluation loss. This gap motivates learning not just how to generate, but what to generate and when to inject as training evolves. We propose TAP (Tabular Augmentation Policy), which couples diffusion inpainting with a lightweight, learner-conditioned policy to steer generation toward high-utility regions and controls safe injection via explicit gating and conservative windowed commitment. Under severe data scarcity, TAP consistently outperforms strong generative baselines on seven real-world datasets, improving classification accuracy by up to 15.6 percentage points and reducing regression RMSE by up to 32%.
匹配关键词: preference learning
---

[ACADEMIC - ARXIV]
标题: Signature Approach for Contextual Bandits with Nonlinear and Path-dependent Rewards
作者: Xin Guo, Grace He, Xinyu Li
链接: https://arxiv.org/abs/2605.10313v1
完整摘要: We study contextual bandits with nonlinear and path-dependent rewards through a novel signature-transform-based approach. Leveraging the universal nonlinearity property of signatures, we approximate continuous path-dependent reward functionals by linear functionals in the signature space. This representation enables the use of efficient linear contextual bandit methods while preserving expressive sequential structure. Building on this framework, we propose \texttt{DisSigUCB}, a signature-based disjoint upper confidence bound (UCB) algorithm. Under boundedness and non-degeneracy assumptions, we prove a high-probability data-dependent sublinear regret bound of order \(\tilde{\mathcal O}(\sqrt{(d+m)KT})\) where \(d\) is the context dimension and \(m\) is the signature feature dimension. Synthetic experiments and numerical applications on temperature sensor monitoring, sleep-stage classification, and hospital nurse staffing demonstrate that \texttt{DisSigUCB} consistently outperforms classical linear and kernelized contextual bandit baselines in nonlinear and path-dependent settings.
匹配关键词: preference learning
---

[ACADEMIC - ARXIV]
标题: Follow the Mean: Reference-Guided Flow Matching
作者: Pedro M. P. Curvo, Maksim Zhdanov, Floor Eijkelboom, Jan-Willem van de Meent
链接: https://arxiv.org/abs/2605.10302v1
完整摘要: Existing approaches to controllable generation typically rely on fine-tuning, auxiliary networks, or test-time search. We show that flow matching admits a different control interface: adaptation through examples. For deterministic interpolants, the velocity field is solely governed by a conditional endpoint mean; shifting this mean shifts the flow itself. This yields a simple principle for controllable generation: steer a pretrained model by changing the reference set it follows. We instantiate this idea in two forms. Reference-Mean Guidance is training-free: it computes a closed-form endpoint-mean correction from a reference bank and applies it to a frozen FLUX.2-klein (4B) model, enabling control of color, identity, style, and structure while keeping the prompt, seed, and weights fixed. Semi-Parametric Guidance amortizes the same idea through an explicit mean anchor and learned residual refiner, matching unconditional DiT-B/4 quality on AFHQv2 while allowing the reference set to be swapped at inference time. These results point to a broader direction: generative models that adapt through data, not parameter updates.
匹配关键词: preference learning
---

[ACADEMIC - ARXIV]
标题: Nearly-Optimal Algorithm for Adversarial Kernelized Bandits
作者: Shogo Iwazaki
链接: https://arxiv.org/abs/2605.10299v1
完整摘要: This paper studies kernelized bandits (also known as Gaussian process bandits) in an adversarial environment, where the reward functions in a known reproducing kernel Hilbert space (RKHS) may be adversarially chosen at each round. We show that the exponential-weight algorithm achieves $\tilde{O}(\sqrt{T γ_T})$ adversarial regret, where $T$ and $γ_T$ denote the number of total rounds and the maximum information gain, respectively. For squared exponential (SE) and $ν$-Matérn kernels, we also show algorithm-independent lower bounds that guarantee the optimality of our algorithm up to polylogarithmic factors. Furthermore, we present a computationally efficient variant of our algorithm using Nyström approximation while maintaining nearly optimal regret guarantees.
匹配关键词: preference learning
---

[ACADEMIC - ARXIV]
标题: Extending Confidence-Based Text2Cypher with Grammar and Schema Aware Filtering
作者: Makbule Gulcin Ozsoy
链接: https://arxiv.org/abs/2605.10318v1
完整摘要: Large language models (LLMs) allow users to query databases using natural language by translating questions into executable queries. Despite strong progress on tasks such as Text2SQL, Text2SPARQL, and Text2Cypher, most existing methods focus on better prompting, fine-tuning, or iterative refinement. However, they often do not explicitly enforce structural constraints, such as syntactic validity and schema consistency. This can reduce reliability, since generated queries must satisfy both syntax rules and database schema constraints to be executable. In this work, we study how structured constraints can be used in test-time inference for Text2Cypher. We focus on post-generation validation to improve query correctness. We extend a confidence-based inference framework with a sequential filtering process that combines confidence scoring, grammar validation, and schema constraints before final aggregation. This lets us analyze how different constraint types affect generated queries. Our experiments with two instruction-tuned models show that grammar-based filtering improves syntactic validity. Schema-aware filtering further improves execution quality by enforcing consistency with the database structure. However, stronger filtering also increases the number of empty predictions and reduces execution coverage. Overall, we show that adding simple structural checks at test time improves the reliability of Text2Cypher generation, and we provide a clearer view of how syntax and schema constraints contribute differently.
匹配关键词: reward model
---

[ACADEMIC - ARXIV]
标题: Relations Are Channels: Knowledge Graph Embedding via Kraus Decompositions
作者: Sayan Kumar Chaki
链接: https://arxiv.org/abs/2605.10317v1
完整摘要: Knowledge graph embedding (KGE) models typically represent each relation as an operator on entity embeddings. In this work, we identify three structural axioms that any principled relation operator must satisfy, linearity, trace preservation, and complete positivity, and show that they characterize a Kraus channel structure via the Kraus representation theorem. The completeness constraint defining this family is equivalent to these axioms, providing a principled foundation rather than an externally imposed condition. Under this formulation, most existing operator-based KGE models are recoverable as special cases with Kraus rank $κ= 1$ under specific embedding choices. We further generalize this characterization to arbitrary metric geometries by introducing \mbox{w-Kraus} channels, which satisfy completeness by construction within their respective spaces. Building on this theory, we propose \textsc{KrausKGE}, a principled KGE model that naturally handles $1$-to-$N$ and $N$-to-$N$ relations, supports $k$-hop reasoning without requiring explicit path encoders, and eliminates the need for norm constraints on entity embeddings. Additionally, our framework yields the first theoretically grounded per-relation complexity measure in the KGE literature, with a provable lower bound in terms of the empirical relation matrix rank. Empirical evaluation demonstrates that \textsc{KrausKGE} consistently outperforms strong baselines on $N$-to-$N$ relations, with performance gains that increase monotonically with relation fan-out, in alignment with theoretical predictions.
匹配关键词: reward model
---

[ACADEMIC - ARXIV]
标题: Active Tabular Augmentation via Policy-Guided Diffusion Inpainting
作者: Zheyu Zhang, Shuo Yang, Bardh Prenkaj, Gjergji Kasneci
链接: https://arxiv.org/abs/2605.10315v1
完整摘要: Generative tabular augmentation is appealing in data-scarce domains, yet the prevailing focus on distributional fidelity does not reliably translate into better downstream models. We formalize a fidelity-utility gap: common generative objectives prioritize distributional plausibility, whereas augmentation succeeds only when injected samples reduce the current learner's held-out evaluation loss. This gap motivates learning not just how to generate, but what to generate and when to inject as training evolves. We propose TAP (Tabular Augmentation Policy), which couples diffusion inpainting with a lightweight, learner-conditioned policy to steer generation toward high-utility regions and controls safe injection via explicit gating and conservative windowed commitment. Under severe data scarcity, TAP consistently outperforms strong generative baselines on seven real-world datasets, improving classification accuracy by up to 15.6 percentage points and reducing regression RMSE by up to 32%.
匹配关键词: reward model
---

[ACADEMIC - ARXIV]
标题: Signature Approach for Contextual Bandits with Nonlinear and Path-dependent Rewards
作者: Xin Guo, Grace He, Xinyu Li
链接: https://arxiv.org/abs/2605.10313v1
完整摘要: We study contextual bandits with nonlinear and path-dependent rewards through a novel signature-transform-based approach. Leveraging the universal nonlinearity property of signatures, we approximate continuous path-dependent reward functionals by linear functionals in the signature space. This representation enables the use of efficient linear contextual bandit methods while preserving expressive sequential structure. Building on this framework, we propose \texttt{DisSigUCB}, a signature-based disjoint upper confidence bound (UCB) algorithm. Under boundedness and non-degeneracy assumptions, we prove a high-probability data-dependent sublinear regret bound of order \(\tilde{\mathcal O}(\sqrt{(d+m)KT})\) where \(d\) is the context dimension and \(m\) is the signature feature dimension. Synthetic experiments and numerical applications on temperature sensor monitoring, sleep-stage classification, and hospital nurse staffing demonstrate that \texttt{DisSigUCB} consistently outperforms classical linear and kernelized contextual bandit baselines in nonlinear and path-dependent settings.
匹配关键词: reward model
---

[ACADEMIC - ARXIV]
标题: PaMoSplat: Part-Aware Motion-Guided Gaussian Splatting for Dynamic Scene Reconstruction
作者: Yinan Deng, Jianyu Dou, Jiahui Wang, Jingyu Zhao, Yi Yang, Yufeng Yue
链接: https://arxiv.org/abs/2605.10307v1
完整摘要: Dynamic scene reconstruction represents a fundamental yet demanding challenge in computer vision and robotics. While recent progress in 3DGS-based methods has advanced dynamic scene modeling, obtaining high-fidelity rendering and accurate tracking in scenarios with substantial, intricate motions remains significantly challenging. To address these challenges, we propose PaMoSplat, a novel dynamic Gaussian splatting framework incorporating part awareness and motion priors. Our approach is grounded in two key observations: 1) Parts serve as primitives for scene deformation, and 2) Motion cues from optical flow can effectively guide part motion. Specifically, PaMoSplat initializes by lifting multi-view segmentation masks into 3D space via graph clustering, establishing coherent Gaussian parts. For subsequent timestamps, we leverage a differential evolutionary algorithm to estimate the rigid motion of these parts using multi-view optical flow cues, providing a robust warm-start for further optimization. Additionally, PaMoSplat introduces an adaptive iteration count mechanism, internal learnable rigidity, and flow-supervised rendering loss to accelerate and optimize the training process. Comprehensive evaluations across diverse scenes, including real-world environments, demonstrate that PaMoSplat delivers superior rendering quality, improved tracking precision, and faster convergence compared to existing methods. Furthermore, it enables multiple part-level downstream applications, such as 4D scene editing.
匹配关键词: reward model
---

[ACADEMIC - ARXIV]
标题: Positive Alignment: Artificial Intelligence for Human Flourishing
作者: Ruben Laukkonen, Seb Krier, Chloé Bakalar, Shamil Chandaria, Morten Kringelbach, Adam Elwood, Daniel Ford, Fernando Rosas, Maty Bohacek, Matija Franklin, Nenad Tomašev, Stephanie Chan, Verena Rieser, Roma Patel, Michael Levin, Arun Rao
链接: https://arxiv.org/abs/2605.10310v1
完整摘要: Existing alignment research is dominated by concerns about safety and preventing harm: safeguards, controllability, and compliance. This paradigm of alignment parallels early psychology's focus on mental illness: necessary but incomplete. What we call Positive Alignment is the development of AI systems that (i) actively support human and ecological flourishing in a pluralistic, polycentric, context-sensitive, and user-authored way while (ii) remaining safe and cooperative. It is a distinct and necessary agenda within AI alignment research. We argue that several existing failures of alignment (e.g., engagement hacking, loss of human autonomy, failures in truth-seeking, low epistemic humility, error correction, lack of diverse viewpoints, and being primarily reactive rather than proactive) may be better addressed through positive alignment, including cultivating virtues and maximizing human flourishing. We highlight a range of challenges, open questions, and technical directions (e.g., data filtering and upsampling, pre- and post-training, evaluations, collaborative value collection) for different phases of the LLM and agents lifecycle. We end with design principles for promoting disagreement and decentralization through contextual grounding, community customization, continual adaptation, and polycentric governance; that is, many legitimate centers of oversight rather than one institutional or moral chokepoint.
匹配关键词: constitutional AI
---

[ACADEMIC - ARXIV]
标题: Generative AI Fuels Solo Entrepreneurship, but Teams Still Lead at the Top
作者: Hyunso Kim, Hyo Kang, Jaeyong Song
链接: https://arxiv.org/abs/2605.10291v1
完整摘要: Recent advances in generative artificial intelligence (AI) are reshaping who enters entrepreneurship, but not who reaches the top of the quality distribution. Using data on over 160,000 product launches on Product Hunt, we find that entrepreneurial entry increased sharply following the public release of ChatGPT-3.5, driven disproportionately by solo entrepreneurs. This shift toward solo entry is particularly pronounced in categories that historically favored team-based ventures. However, much of this growth reflects low-commitment, experimental entry and does not translate into greater representation among the highest-quality outcomes. Team-based ventures are increasingly dominant in the top tiers of platform rankings. These findings suggest that generative AI lowers barriers to solo entrepreneurship while reinforcing team-based advantages.
匹配关键词: constitutional AI
---

[ACADEMIC - ARXIV]
标题: DeepLog: A Software Framework for Modular Neurosymbolic AI
作者: Robin Manhaeve, Stefano Colamonaco, Vincent Derkinderen, Rik Adriaensen, Lucas Van Praet, Luc De Raedt, Giuseppe Marra
链接: https://arxiv.org/abs/2605.10279v1
完整摘要: DeepLog is an operational neurosymbolic framework that unifies logic and deep learning within standard PyTorch workflows. While existing neurosymbolic systems focus on a particular paradigm and semantics, DeepLog serves as a universal backend that can emulate many systems in the neurosymbolic alphabet soup. By treating diverse neurosymbolic languages as high-level specifications, the DeepLog software automatically compiles them into optimized arithmetic circuits. This design lowers the barrier for machine learning practitioners by treating logic as composable modules, while providing neurosymbolic developers with a shared, high-performance basis for prototyping new integration strategies. The code is available here: https://github.com/ML-KULeuven/deeplog
匹配关键词: constitutional AI
---

[ACADEMIC - ARXIV]
标题: SciIntegrity-Bench: A Benchmark for Evaluating Academic Integrity in AI Scientist Systems
作者: Zonglin Yang, Xingtong Liu, Xinyan Xu
链接: https://arxiv.org/abs/2605.10246v1
完整摘要: AI scientist systems are increasingly deployed for autonomous research, yet their academic integrity has never been systematically evaluated. We introduce SCIINTEGRITY-BENCH, the first benchmark designed around a dilemmatic evaluation paradigm: each of its 33 scenarios across 11 trap categories is constructed so that honest acknowledgment of failure is the only correct response, while task completion requires misconduct. Across 231 evaluation runs spanning 7 state-of-the-art LLMs, the overall integrity problem rate reaches 34.2%, and no model achieves zero failures. Most strikingly, across missing-data scenarios, all seven models generate synthetic data rather than acknowledging infeasibility, differing only in whether they disclose the substitution. A further prompt ablation study separates two drivers: removing explicit completion pressure sharply reduces undisclosed fabrication from 20.6% to 3.2%, while the underlying synthesis rate remains unchanged, revealing an intrinsic completion bias that persists independent of prompt-level instructions. These findings point to the absence of honest refusal as a trained disposition as the primary driver of observed failures. We release SCIINTEGRITY-BENCH at https://github.com/liuxingtong/Sci-Integrity-Bench.
匹配关键词: constitutional AI
---

[ACADEMIC - ARXIV]
标题: Hypothesis-Driven Deep Research with Large Language Models: A Structured Methodology for Automated Knowledge Discovery
作者: Michael Chin
链接: https://arxiv.org/abs/2605.10224v1
完整摘要: Current AI-powered research systems adopt a direct search-then-summarize paradigm that treats hypotheses as end products of scientific discovery. We argue this leaves a critical gap: hypotheses can serve a far more powerful role as organizational instruments that structure the research process itself. We propose the Hypothesis-Driven Deep Research (HDRI) methodology - the first framework using hypotheses to organize general-purpose deep research across arbitrary domains, rather than merely validating claims within specific domains. This transforms research from reactive information retrieval into proactive, verifiable, and iterative knowledge discovery. HDRI is formalized with six core principles and an eight-stage pipeline. A central innovation is the gap-driven iterative research mechanism - a closed-loop quality assurance system that automatically identifies informational and logical gaps, triggering targeted supplementary investigation. We further introduce a fact reasoning framework with traceable reasoning chains and quantified confidence propagation, a subject locking mechanism to prevent entity confusion, and a multi-dimensional quality assessment scheme. The methodology is realized in the INFOMINER system. Experiments demonstrate improvements of 22.4% in fact density, 90% subject matching accuracy, 0.92 multi-source verification confidence, and 14% completeness gain from gap-driven supplementation. Five case studies validate its practical applicability, achieving an average quality rating of 4.46/5.0.
匹配关键词: constitutional AI
---

[ACADEMIC - ARXIV]
标题: Qwen Goes Brrr: Off-the-Shelf RAG for Ukrainian Multi-Domain Document Understanding
作者: Anton Bazdyrev, Ivan Bashtovyi, Ivan Havlytskyi, Oleksandr Kharytonov, Artur Khodakovskyi
链接: https://arxiv.org/abs/2605.10296v1
完整摘要: We participated in the Fifth UNLP shared task on multi-domain document understanding, where systems must answer Ukrainian multiple-choice questions from PDF collections and localize the supporting document and page. We propose a retrieval-augmented pipeline built around three ideas: contextual chunking of PDFs, question-aware dense retrieval and reranking conditioned on both the question and answer options, and constrained answer generation from a small set of reranked passages. Our final system uses Qwen3-Embedding-8B for retrieval, a fine-tuned Qwen3-Reranker-8B for passage ranking, and Qwen3-32B for answer selection. On a held-out split, reranking improves Recall@1 from 0.6957 to 0.7935, while using the top-2 reranked passages raises answer accuracy from 0.9348 to 0.9674. Our best leaderboard run reached 0.9452 on the public leaderboard and 0.9598 on the private leaderboard. Our results suggest that, under strict code-competition constraints, preserving document structure and making relevance estimation aware of the answer space are more effective than adding complex downstream heuristics.
匹配关键词: RAG
---

[ACADEMIC - ARXIV]
标题: Knowledge Poisoning Attacks on Medical Multi-Modal Retrieval-Augmented Generation
作者: Peiru Yang, Haoran Zheng, Tong Ju, Shiting Wang, Wanchun Ni, Jiajun Liu, Shangguang Wang, Yongfeng Huang, Tao Qi
链接: https://arxiv.org/abs/2605.10253v1
完整摘要: Retrieval-augmented generation (RAG) is a widely adopted paradigm for enhancing LLMs in medical applications by incorporating expert multimodal knowledge during generation. However, the underlying retrieval databases may naturally contain, or be intentionally injected with, adversarial knowledge, which can perturb model outputs and undermine system reliability. To investigate this risk, prior studies have explored knowledge poisoning attacks in medical RAG systems. Nevertheless, most of them rely on the strong assumption that adversaries possess prior knowledge of user queries, which is unrealistic in deployments and substantially limits their practical applicability. In this paper, we propose M\textsuperscript{3}Att, a knowledge-poisoning framework designed for medical multimodal RAG systems, assuming only limited distribution knowledge of the underlying database. Our core idea is to inject covert misinformation into textual data while using paired visual data as a query-agnostic trigger to promote retrieval. We first propose a unified framework that introduces imperceptible perturbations to visual inputs to manipulate retrieval probabilities. Besides, due to the prior medical knowledge in LLMs, naively poisoned medical content with explicit factual errors can be corrected during generation. Thus, we leverage the inherent ambiguity of medical diagnosis and design a covert misinformation injection strategy that degrades diagnostic accuracy while evading model self-correction. Experiments on five LLMs and datasets demonstrate that M\textsuperscript{3}Att consistently produces clinically plausible yet incorrect generations. Codes: https://github.com/ypr17/M3Att.
匹配关键词: RAG
---

[ACADEMIC - ARXIV]
标题: Route Before Retrieve: Activating Latent Routing Abilities of LLMs for RAG vs. Long-Context Selection
作者: Yiwen Chen, Kuan Li, Fuzhen Zhuang, Deqing Wang, Zhao Zhang, Liwen Zhang, Yong Jiang, Shuai Wang, Minhao Cheng
链接: https://arxiv.org/abs/2605.10235v1
完整摘要: Recent advances in large language models (LLMs) have expanded the context window to beyond 128K tokens, enabling long-document understanding and multi-source reasoning. A key challenge, however, lies in choosing between retrieval-augmented generation (RAG) and long-context (LC) strategies: RAG is efficient but constrained by retrieval quality, while LC supports global reasoning at higher cost and with position sensitivity. Existing methods such as Self-Route adopt failure-driven fallback from RAG to LC, but remain passive, inefficient, and hard to interpret. We propose Pre-Route, a proactive routing framework that performs structured reasoning before answering. Using lightweight metadata (e.g., document type, length, initial snippet), Pre-Route enables task analysis, coverage estimation, and information-need prediction, producing explainable and cost-efficient routing decisions. Our study shows three key findings: (i) LLMs possess latent routing ability that can be reliably elicited with guidelines, allowing single-sample performance to approach that of multi-sample (Best-of-N) results; (ii) linear probes reveal that structured prompts sharpen the separability of the "optimal routing dimension" in representation space; and (iii) distillation transfers this reasoning structure to smaller models for lightweight deployment. Experiments on LaRA (in-domain) and LongBench-v2 (OOD) confirm that Pre-Route outperforms Always-RAG, Always-LC, and Self-Route baselines, achieving superior overall cost-effectiveness.
匹配关键词: RAG
---

[ACADEMIC - ARXIV]
标题: ASTRA-QA: A Benchmark for Abstract Question Answering over Documents
作者: Shu Wang, Shansong Zhou, Xinyang Wang, Shiwei Wang, Hulong Wu, Yixiang Fang
链接: https://arxiv.org/abs/2605.10168v1
完整摘要: Document-based question answering (QA) increasingly includes abstract questions that require synthesizing scattered information from long documents or across multiple documents into coherent answers. However, this setting is still poorly supported by existing benchmarks and evaluation methods, which often lack stable abstract references or rely on coarse similarity metrics and unstable head-to-head comparisons. To alleviate this issue, we introduce ASTRA-QA, a benchmark for AbSTRAct Question Answering over documents. ASTRA-QA contains 869 QA instances over academic papers and news documents, covering five abstract question types and three controlled retrieval scopes. Each instance is equipped with explicit evaluation annotations, including answer topic sets, curated unsupported topics, and aligned evidence. Building on these annotations, ASTRA-QA assesses whether answers cover required key points and avoid unsupported content by directly scoring topic coverage and curated unsupported content, enabling scalable evaluation without exhaustive head-to-head comparisons. Experiments with representative Retrieval-Augmented Generation (RAG) methods spanning vanilla, graph-based, and hierarchical retrieval settings show that ASTRA-QA provides reference-grounded diagnostics for coverage, hallucination, and retrieval-scope robustness. Our dataset and code are available at https://xinyangsally.github.io/astra-benchmark.
匹配关键词: RAG
---

[ACADEMIC - ARXIV]
标题: NyayaAI: An AI-Powered Legal Assistant Using Multi-Agent Architecture and Retrieval-Augmented Generation
作者: Deepanshu, Divi Saxena, Deepali Rana, Ayesha Varshney, Sahinur Rahman Laskar
链接: https://arxiv.org/abs/2605.10155v1
完整摘要: Legal information in India remains largely inaccessible due to the complexity of legal language and the sheer volume of legal documentation involved in research and case analysis. This paper presents NyayaAI, an AI-powered legal assistant that automates and simplifies legal workflows for lawyers, law students, and general users. The system combines Large Language Models with a Retrieval-Augmented Generation pipeline grounded in a curated Indian legal knowledge base comprising constitutional provisions, statutes, case laws, and judicial precedents. A multi-agent architecture orchestrated through the Mastra TypeScript framework coordinates a main agent with specialized sub-agents handling legal research, document summarization, case law retrieval, and drafting assistance. A compliance module validates all responses before delivery. Domain classification achieved 70\% precision across test samples, with RAG retrieval precision at 74\% and overall response accuracy at 72\%, demonstrating that structured multi-agent LLM systems can meaningfully improve legal accessibility and workflow efficiency. The code\footnote{https://github.com/B97784/NyayaAI} is made publicly available for the benefit of the research community.
匹配关键词: RAG
---

[ACADEMIC - ARXIV]
标题: Extending Confidence-Based Text2Cypher with Grammar and Schema Aware Filtering
作者: Makbule Gulcin Ozsoy
链接: https://arxiv.org/abs/2605.10318v1
完整摘要: Large language models (LLMs) allow users to query databases using natural language by translating questions into executable queries. Despite strong progress on tasks such as Text2SQL, Text2SPARQL, and Text2Cypher, most existing methods focus on better prompting, fine-tuning, or iterative refinement. However, they often do not explicitly enforce structural constraints, such as syntactic validity and schema consistency. This can reduce reliability, since generated queries must satisfy both syntax rules and database schema constraints to be executable. In this work, we study how structured constraints can be used in test-time inference for Text2Cypher. We focus on post-generation validation to improve query correctness. We extend a confidence-based inference framework with a sequential filtering process that combines confidence scoring, grammar validation, and schema constraints before final aggregation. This lets us analyze how different constraint types affect generated queries. Our experiments with two instruction-tuned models show that grammar-based filtering improves syntactic validity. Schema-aware filtering further improves execution quality by enforcing consistency with the database structure. However, stronger filtering also increases the number of empty predictions and reduces execution coverage. Overall, we show that adding simple structural checks at test time improves the reliability of Text2Cypher generation, and we provide a clearer view of how syntax and schema constraints contribute differently.
匹配关键词: code generation
---

[ACADEMIC - ARXIV]
标题: Relations Are Channels: Knowledge Graph Embedding via Kraus Decompositions
作者: Sayan Kumar Chaki
链接: https://arxiv.org/abs/2605.10317v1
完整摘要: Knowledge graph embedding (KGE) models typically represent each relation as an operator on entity embeddings. In this work, we identify three structural axioms that any principled relation operator must satisfy, linearity, trace preservation, and complete positivity, and show that they characterize a Kraus channel structure via the Kraus representation theorem. The completeness constraint defining this family is equivalent to these axioms, providing a principled foundation rather than an externally imposed condition. Under this formulation, most existing operator-based KGE models are recoverable as special cases with Kraus rank $κ= 1$ under specific embedding choices. We further generalize this characterization to arbitrary metric geometries by introducing \mbox{w-Kraus} channels, which satisfy completeness by construction within their respective spaces. Building on this theory, we propose \textsc{KrausKGE}, a principled KGE model that naturally handles $1$-to-$N$ and $N$-to-$N$ relations, supports $k$-hop reasoning without requiring explicit path encoders, and eliminates the need for norm constraints on entity embeddings. Additionally, our framework yields the first theoretically grounded per-relation complexity measure in the KGE literature, with a provable lower bound in terms of the empirical relation matrix rank. Empirical evaluation demonstrates that \textsc{KrausKGE} consistently outperforms strong baselines on $N$-to-$N$ relations, with performance gains that increase monotonically with relation fan-out, in alignment with theoretical predictions.
匹配关键词: code generation
---

[ACADEMIC - ARXIV]
标题: Active Tabular Augmentation via Policy-Guided Diffusion Inpainting
作者: Zheyu Zhang, Shuo Yang, Bardh Prenkaj, Gjergji Kasneci
链接: https://arxiv.org/abs/2605.10315v1
完整摘要: Generative tabular augmentation is appealing in data-scarce domains, yet the prevailing focus on distributional fidelity does not reliably translate into better downstream models. We formalize a fidelity-utility gap: common generative objectives prioritize distributional plausibility, whereas augmentation succeeds only when injected samples reduce the current learner's held-out evaluation loss. This gap motivates learning not just how to generate, but what to generate and when to inject as training evolves. We propose TAP (Tabular Augmentation Policy), which couples diffusion inpainting with a lightweight, learner-conditioned policy to steer generation toward high-utility regions and controls safe injection via explicit gating and conservative windowed commitment. Under severe data scarcity, TAP consistently outperforms strong generative baselines on seven real-world datasets, improving classification accuracy by up to 15.6 percentage points and reducing regression RMSE by up to 32%.
匹配关键词: code generation
---

[ACADEMIC - ARXIV]
标题: Follow the Mean: Reference-Guided Flow Matching
作者: Pedro M. P. Curvo, Maksim Zhdanov, Floor Eijkelboom, Jan-Willem van de Meent
链接: https://arxiv.org/abs/2605.10302v1
完整摘要: Existing approaches to controllable generation typically rely on fine-tuning, auxiliary networks, or test-time search. We show that flow matching admits a different control interface: adaptation through examples. For deterministic interpolants, the velocity field is solely governed by a conditional endpoint mean; shifting this mean shifts the flow itself. This yields a simple principle for controllable generation: steer a pretrained model by changing the reference set it follows. We instantiate this idea in two forms. Reference-Mean Guidance is training-free: it computes a closed-form endpoint-mean correction from a reference bank and applies it to a frozen FLUX.2-klein (4B) model, enabling control of color, identity, style, and structure while keeping the prompt, seed, and weights fixed. Semi-Parametric Guidance amortizes the same idea through an explicit mean anchor and learned residual refiner, matching unconditional DiT-B/4 quality on AFHQv2 while allowing the reference set to be swapped at inference time. These results point to a broader direction: generative models that adapt through data, not parameter updates.
匹配关键词: code generation
---

[ACADEMIC - ARXIV]
标题: Qwen Goes Brrr: Off-the-Shelf RAG for Ukrainian Multi-Domain Document Understanding
作者: Anton Bazdyrev, Ivan Bashtovyi, Ivan Havlytskyi, Oleksandr Kharytonov, Artur Khodakovskyi
链接: https://arxiv.org/abs/2605.10296v1
完整摘要: We participated in the Fifth UNLP shared task on multi-domain document understanding, where systems must answer Ukrainian multiple-choice questions from PDF collections and localize the supporting document and page. We propose a retrieval-augmented pipeline built around three ideas: contextual chunking of PDFs, question-aware dense retrieval and reranking conditioned on both the question and answer options, and constrained answer generation from a small set of reranked passages. Our final system uses Qwen3-Embedding-8B for retrieval, a fine-tuned Qwen3-Reranker-8B for passage ranking, and Qwen3-32B for answer selection. On a held-out split, reranking improves Recall@1 from 0.6957 to 0.7935, while using the top-2 reranked passages raises answer accuracy from 0.9348 to 0.9674. Our best leaderboard run reached 0.9452 on the public leaderboard and 0.9598 on the private leaderboard. Our results suggest that, under strict code-competition constraints, preserving document structure and making relevance estimation aware of the answer space are more effective than adding complex downstream heuristics.
匹配关键词: code generation
---

[ACADEMIC - ARXIV]
标题: Set Prediction for Next-Day Active Fire Forecasting
作者: Yuchen Bai, Georgios Athanasiou, Xin Yu, Diogenis Antonopoulos, Ioannis Papoutsis, Stijn Hantson, Nuno Carvalhais
链接: https://arxiv.org/abs/2605.10298v1
完整摘要: Accurate next-day active fire forecasts can support early warning, disaster response, forest risk assessment, and downstream estimation of fire-related carbon emissions. Existing machine learning approaches to wildfire forecasting typically predict wildfire danger or fire probability on kilometre-scale daily grids, which is useful for regional warning but does not directly represent localized fire events. We propose Wildfire Ignition Set Predictor (WISP), a query-based model that reformulates next-day active fire forecasting as point-set prediction. From 48 hours of covariates including meteorology, satellite vegetation products, static land, and fire history, WISP predicts a fixed-size ranked set of future active fire cluster centres on a 375 m grid across globally distributed regions. The model is trained end-to-end with Hungarian matching; to address the conflicting roles of the classification score in assignment, ranking, and query activation, we use asymmetric classification-localization weighting in matching and loss. We further construct a globally distributed, hourly, multi-source benchmark for this task. On a held-out test set spanning fire regions worldwide, the best WISP variant achieves 38.2% average precision (AP) for ranked fire-centre detections, covers 53.4% of fire cluster mass weighted by fire radiative power (FRP), and localizes 54.1% of observed clusters within 5 km. These results establish sparse set prediction as a viable formulation for high-resolution wildfire forecasting and provide a benchmark for future work in this regime.
匹配关键词: benchmark
---

[ACADEMIC - ARXIV]
标题: AgentRx: A Benchmark Study of LLM Agents for Multimodal Clinical Prediction Tasks
作者: Baraa Al Jorf, Farah E. Shamout
链接: https://arxiv.org/abs/2605.10286v1
完整摘要: Building effective clinical decision support systems requires the synthesis of complex heterogeneous multimodal data. Such modalities include temporal electronic health records data, medical images, radiology reports, and clinical notes. Large language model (LLM)-based agents have shown impressive performance in various healthcare tasks, especially those involving textual modalities. Considering the fragmentation of healthcare data across hospital systems, collaborative agent frameworks present a promising direction to mitigate data sharing challenges. However, the effectiveness of LLM agents for multimodal clinical risk prediction remains largely unexamined. In this work, we conduct a systematic evaluation of LLM-based agents for clinical prediction tasks using large-scale real-world data. We assess performance in unimodal and multimodal settings and quantify performance gaps between single agent and multi-agent systems. Our findings highlight that single agent frameworks outperform naive multi-agent systems, are better at handling multimodal data, and are better calibrated. This underscores a critical need for improving multi-agent collaboration to better handle heterogeneous inputs. By open-sourcing our code and evaluation framework, this work offers a new benchmark to support future developments relating to agentic systems in healthcare.
匹配关键词: benchmark
---

[ACADEMIC - ARXIV]
标题: Scalable Gaussian process inference via neural feature maps
作者: Anthony Stephenson
链接: https://arxiv.org/abs/2605.10285v1
完整摘要: We present a theoretically grounded Gaussian process framework that leverages neural feature maps to construct expressive kernels. We show that the learned feature map can be interpreted as an optimal low-rank approximation to a Gram matrix derived from an implied RKHS, from which we establish consistency of the GP posterior. We further analyse the spectral properties of the induced kernels and introduce product feature-map kernels to address oversmoothing. This simple yet powerful approach enables fast, scalable, and accurate exact GP inference with minimal upfront work. The flexibility of kernel design supports seamless application to both regression and classification tasks across diverse data modalities, including tabular inputs and structured domains such as images. On benchmark datasets, this approach surpasses pre-existing methods in terms of accuracy and training and prediction efficiency.
匹配关键词: benchmark
---

[ACADEMIC - ARXIV]
标题: PolarVSR: A Unified Framework and Benchmark for Continuous Space-Time Polarization Video Reconstruction
作者: Chenggong Li, Yidong Luo, Junchao Zhang, Boxin Shi, Degui Yang
链接: https://arxiv.org/abs/2605.10275v1
完整摘要: Polarimetric imaging captures surface polarization characteristics, such as the Degree of Linear Polarization (DoLP) and the Angle of Polarization (AoP). In mainstream Division of-Focal-Plane (DoFP) color polarization imaging, recovering polarization parameters from captured mosaic arrays remains a challenging inverse problem. Existing DoFP cameras also face hardware bottlenecks and often cannot support high-frame-rate acquisition, limiting polarimetric imaging in dynamic video tasks. These limitations motivate joint spatial and temporal enhancement. To this end, we propose the first space-time polarization video reconstruction architecture. The method jointly models polarization directions in space and time and uses a polarization-aware implicit neural representation for continuous, high-fidelity upsampling. By analyzing temporal variations in polarization parameters, we further introduce a flow-guided polarization variation loss to supervise polarization dynamics. We also establish the first large-scale color DoFP polarization video benchmark to support this research direction. Extensive experiments on this benchmark demonstrate the effectiveness of the method.
匹配关键词: benchmark
---

[ACADEMIC - ARXIV]
标题: IndustryBench: Probing the Industrial Knowledge Boundaries of LLMs
作者: Songlin Bai, Xintong Wang, Linlin Yu, Bin Chen, Zhiang Xu, Yuyang Sheng, Changtong Zan, Xiaofeng Zhu, Yizhe Zhang, Jiru Li, Mingze Guo, Ling Zou, Yalong Li, Chengfu Huo, Liang Ding
链接: https://arxiv.org/abs/2605.10267v1
完整摘要: In industrial procurement, an LLM answer is useful only if it survives a standards check: recommended material must match operating condition, every parameter must respect a regulated threshold, and no procedure may contradict a safety clause. Partial correctness can mask safety-critical contradictions that aggregate LLM benchmarks rarely capture. We introduce IndustryBench, a 2,049-item benchmark for industrial procurement QA in Chinese, grounded in Chinese national standards (GB/T) and structured industrial product records, organized by seven capability dimensions, ten industry categories, and panel-derived difficulty tiers, with item-aligned English, Russian, and Vietnamese renderings. Our construction pipeline rejects 70.3% of LLM-generated candidates at a search-based external-verification stage, calibrating how unreliable industrial QA remains after LLM-only filtering.Our evaluation decouples raw correctness, scored by a Qwen3-Max judge validated at $κ_w = 0.798$ against a domain expert, from a separate safety-violation (SV) check against source texts. Across 17 models in Chinese and an 8-model intersection over four languages, we find: (i) the best system reaches only 2.083 on the 0--3 rubric, leaving substantial headroom; (ii) Standards & Terminology is the most persistent capability weakness and survives item-aligned translation; (iii) extended reasoning lowers safety-adjusted scores for 12 of 13 models, primarily by introducing unsupported safety-critical details into longer final answers; and (iv) safety-violation rates reshuffle the leaderboard -- GPT-5.4 climbs from rank 6 to rank 3 after SV adjustment, while Kimi-k2.5-1T-A32B drops seven positions.Industrial LLM evaluation therefore requires source-grounded, safety-aware diagnosis rather than aggregate accuracy. We release IndustryBench with all prompts, scoring scripts, and dataset documentation.
匹配关键词: benchmark
---

[ACADEMIC - ARXIV]
标题: Positive Alignment: Artificial Intelligence for Human Flourishing
作者: Ruben Laukkonen, Seb Krier, Chloé Bakalar, Shamil Chandaria, Morten Kringelbach, Adam Elwood, Daniel Ford, Fernando Rosas, Maty Bohacek, Matija Franklin, Nenad Tomašev, Stephanie Chan, Verena Rieser, Roma Patel, Michael Levin, Arun Rao
链接: https://arxiv.org/abs/2605.10310v1
完整摘要: Existing alignment research is dominated by concerns about safety and preventing harm: safeguards, controllability, and compliance. This paradigm of alignment parallels early psychology's focus on mental illness: necessary but incomplete. What we call Positive Alignment is the development of AI systems that (i) actively support human and ecological flourishing in a pluralistic, polycentric, context-sensitive, and user-authored way while (ii) remaining safe and cooperative. It is a distinct and necessary agenda within AI alignment research. We argue that several existing failures of alignment (e.g., engagement hacking, loss of human autonomy, failures in truth-seeking, low epistemic humility, error correction, lack of diverse viewpoints, and being primarily reactive rather than proactive) may be better addressed through positive alignment, including cultivating virtues and maximizing human flourishing. We highlight a range of challenges, open questions, and technical directions (e.g., data filtering and upsampling, pre- and post-training, evaluations, collaborative value collection) for different phases of the LLM and agents lifecycle. We end with design principles for promoting disagreement and decentralization through contextual grounding, community customization, continual adaptation, and polycentric governance; that is, many legitimate centers of oversight rather than one institutional or moral chokepoint.
匹配关键词: safety
---

[ACADEMIC - ARXIV]
标题: Robust Probabilistic Shielding for Safe Offline Reinforcement Learning
作者: Maris F. L. Galesloot, Thomas Rhemrev, Nils Jansen
链接: https://arxiv.org/abs/2605.10293v1
完整摘要: In offline reinforcement learning (RL), we learn policies from fixed datasets without environment interaction. The major challenges are to provide guarantees on the (1) performance and (2) safety of the resulting policy. A technique called safe policy improvement (SPI) provides a performance guarantee: with high probability, the new policy outperforms a given baseline policy, which is assumed to be safe. Orthogonally, in the context of safe RL, a shield provides a safety guarantee by restricting the action space to those actions that are provably safe with respect to a given safety-relevant model. We integrate these paradigms by extending shielding to offline RL, relying solely on the available dataset and knowledge of safe and unsafe states. Then, we shield the policy improvement steps, guaranteeing, with high probability, a safe policy. Experimental results demonstrate that shielded SPI outperforms its unshielded counterpart, improving both average and worst-case performance, particularly in low-data regimes.
匹配关键词: safety
---

[ACADEMIC - ARXIV]
标题: IndustryBench: Probing the Industrial Knowledge Boundaries of LLMs
作者: Songlin Bai, Xintong Wang, Linlin Yu, Bin Chen, Zhiang Xu, Yuyang Sheng, Changtong Zan, Xiaofeng Zhu, Yizhe Zhang, Jiru Li, Mingze Guo, Ling Zou, Yalong Li, Chengfu Huo, Liang Ding
链接: https://arxiv.org/abs/2605.10267v1
完整摘要: In industrial procurement, an LLM answer is useful only if it survives a standards check: recommended material must match operating condition, every parameter must respect a regulated threshold, and no procedure may contradict a safety clause. Partial correctness can mask safety-critical contradictions that aggregate LLM benchmarks rarely capture. We introduce IndustryBench, a 2,049-item benchmark for industrial procurement QA in Chinese, grounded in Chinese national standards (GB/T) and structured industrial product records, organized by seven capability dimensions, ten industry categories, and panel-derived difficulty tiers, with item-aligned English, Russian, and Vietnamese renderings. Our construction pipeline rejects 70.3% of LLM-generated candidates at a search-based external-verification stage, calibrating how unreliable industrial QA remains after LLM-only filtering.Our evaluation decouples raw correctness, scored by a Qwen3-Max judge validated at $κ_w = 0.798$ against a domain expert, from a separate safety-violation (SV) check against source texts. Across 17 models in Chinese and an 8-model intersection over four languages, we find: (i) the best system reaches only 2.083 on the 0--3 rubric, leaving substantial headroom; (ii) Standards & Terminology is the most persistent capability weakness and survives item-aligned translation; (iii) extended reasoning lowers safety-adjusted scores for 12 of 13 models, primarily by introducing unsupported safety-critical details into longer final answers; and (iv) safety-violation rates reshuffle the leaderboard -- GPT-5.4 climbs from rank 6 to rank 3 after SV adjustment, while Kimi-k2.5-1T-A32B drops seven positions.Industrial LLM evaluation therefore requires source-grounded, safety-aware diagnosis rather than aggregate accuracy. We release IndustryBench with all prompts, scoring scripts, and dataset documentation.
匹配关键词: safety
---

[ACADEMIC - ARXIV]
标题: Beyond Autonomy: A Dynamic Tiered AgentRunner Framework for Governable and Resilient Enterprise AI Execution
作者: Kai Pan, Rong Hou
链接: https://arxiv.org/abs/2605.10223v1
完整摘要: Current large language model agent frameworks prioritize autonomy but lack the governability mechanisms required for enterprise deployment. High-risk write operations proceed without independent review, complex tasks lack acceptance verification, and computational resources are allocated uniformly regardless of risk level. We propose the Dynamic Tiered AgentRunner, a controlled execution protocol distilled from a production-grade multi-tenant SaaS platform. The framework introduces three core mechanisms: (1) Risk-Adaptive Tiering that dynamically allocates computational resources and review intensity based on task risk profiles, achieving Pareto-optimal trade-offs between safety and efficiency; (2) Separation of Powers architecture where proposal, review, execution, and verification are performed by independent agents with physically isolated boundaries; and (3) Resilience-by-Design through a Verifier-Recovery closed loop that treats failure as a first-class system state. We formalize the tier selectio
匹配关键词: safety
---

[ACADEMIC - ARXIV]
标题: Benchmarking Safety Risks of Knowledge-Intensive Reasoning under Malicious Knowledge Editing
作者: Qinghua Mao, Xi Lin, Jinze Gu, Jun Wu, Siyuan Li, Yuliang Chen
链接: https://arxiv.org/abs/2605.10146v1
完整摘要: Large language models (LLMs) increasingly rely on knowledge editing to support knowledge-intensive reasoning, but this flexibility also introduces critical safety risks: adversaries can inject malicious or misleading knowledge that corrupts downstream reasoning and leads to harmful outcomes. Existing knowledge editing benchmarks primarily focus on editing efficacy and lack a unified framework for systematically evaluating the safety implications of edited knowledge on reasoning behavior. To address this gap, we present EditRisk-Bench, a benchmark for systematically evaluating safety risks of knowledge-intensive reasoning under malicious knowledge editing. Unlike prior benchmarks that mainly emphasize edit success, generalization, and locality, EditRisk-Bench focuses on how injected knowledge affects downstream reasoning behavior and reliability. It integrates diverse malicious scenarios, including misinformation, bias, and safety violations, together with multi-level knowledge-intensive reasoning tasks and representative editing strategies within a unified evaluation framework measuring attack effectiveness, reasoning correctness, and side effects. Extensive experiments on both open-source and closed-source LLMs show that malicious knowledge editing can reliably induce incorrect or unsafe reasoning while largely preserving general capabilities, making such risks difficult to detect. We further identify several key factors influencing these risks, including edit scale, knowledge characteristics, and reasoning complexity. EditRisk-Bench provides an extensible testbed for understanding and mitigating safety risks in knowledge editing for LLMs.
匹配关键词: safety
---

